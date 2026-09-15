#!/usr/bin/env python3
"""Give every day deck its route: once at the start of the day, once again in
front of the afternoon. Idempotent; run from anywhere.

  python3 presentations/add_routes.py

Squad 1 already carries a route slide per day; only the after-lunch repeat is
added. Squad 2 had none, so its route is derived from the deck's own kickers:
the schedule on the slide is the schedule the slides already claim. Two lines
are not in any kicker and are named here, not derived: the hour before the
human gate is lunch, and the day opens with theory and demo until the first
timed block. The after-lunch slide is the route slide with the same cards; the
schedule does not change halfway, only where the room is in it."""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DECKS = {"squad1": HERE / "day-decks.json", "squad2": HERE.parent / "squads" / "squad-2" / "presentations.json"}

RANGE = re.compile(r"(\d{1,2}:\d{2})\s*[–-]\s*(\d{1,2}:\d{2})")
TIME = re.compile(r"(\d{1,2}):(\d{2})")
LABEL = {"theory + demo": "theory and demo", "individual": "individual", "review": "review", "practice": "practice",
         "break": "break", "human gate": "human gate", "transfer": "transfer", "close": "close"}
AFTER_LUNCH = {
    "subtitle": "The same route, halfway. Everything before lunch is behind us.",
    "prompt": "Show the same route again. Point at where the room is now, then name the artifact and the acceptance check for the afternoon blocks.",
    "steps": ["Point at where we are.", "Name the next artifact.", "Name its acceptance check."],
    "expected": "Everyone knows which blocks remain and what each one has to produce.",
    "check": "Everyone can name the next artifact and who accepts it.",
}


def mins(t):
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def is_route(s):
    return bool(re.search(r"route|rhythm", s.get("title", ""), re.I)) or re.match(r"^(FIXED )?SCHEDULE", s.get("kicker", "")) is not None


def resumes_after(s, cut):
    """A block that spans lunch ("11:45–12:00 + 13:00–13:20") resumes at its own
    13:00, so every time in the kicker counts, not just the first."""
    return any(int(h) * 60 + int(m) >= cut for h, m in TIME.findall(s.get("kicker", "")))


def blocks_of(slides):
    """The timed blocks a Squad 2 day's own slides declare, in clock order."""
    timed, floating = [], []
    for s in slides:
        kicker = s.get("kicker", "")
        label = LABEL.get(kicker.split("·")[0].strip().lower())
        if not label:
            continue
        r = RANGE.search(kicker)
        if r:
            if mins(r.group(2)) - mins(r.group(1)) > 240:
                continue  # the opener's full-day range frames the day, it is not a block
            timed.append({"from": r.group(1), "to": r.group(2), "label": label})
            continue
        dur = re.search(r"(\d+)\s*MIN", kicker, re.I)
        if dur:
            floating.append({"dur": int(dur.group(1)), "label": label})
    timed.sort(key=lambda b: mins(b["from"]))
    for f in floating:  # BREAK · 15 MIN drops into the gap of exactly its length
        for i in range(len(timed) - 1):
            if mins(timed[i + 1]["from"]) - mins(timed[i]["to"]) == f["dur"]:
                timed.insert(i + 1, {"from": timed[i]["to"], "to": timed[i + 1]["from"], "label": f["label"]})
                break
    for i in range(len(timed) - 1):
        if timed[i]["to"] == "12:00" and timed[i + 1]["from"] == "13:00":
            timed.insert(i + 1, {"from": "12:00", "to": "13:00", "label": "lunch"})
            break
    day = next((m.group(1) for s in slides for m in [re.match(r"^DAY \d.*?(\d{1,2}:\d{2})", s.get("kicker", ""))] if m), None)
    if day and timed and mins(timed[0]["from"]) > mins(day):
        timed.insert(0, {"from": day, "to": timed[0]["from"], "label": "theory and demo"})
    return timed


def route_cards(blocks):
    part = lambda lo, hi: " · ".join(f"{b['from']}–{b['to']} {b['label']}" for b in blocks if mins(lo) <= mins(b["from"]) < mins(hi))
    cards = [("Morning", part("00:00", "11:35")), ("Midday", part("11:35", "14:00")), ("Afternoon", part("14:00", "23:59"))]
    return [{"title": t, "body": b} for t, b in cards if b]


def route_slide(day_no, blocks):
    return {
        "title": f"Day {day_no} route",
        "kicker": f"FIXED SCHEDULE · {blocks[0]['from']}–{blocks[-1]['to']}",
        "subtitle": "The same rhythm every day: the timeboxes are shared, the exercise changes.",
        "cards": route_cards(blocks),
        "prompt": "Read the route aloud before anything else. Name the artifact and the human acceptance check for the first block. Keep the lunch and the breaks fixed.",
        "notes": "Houd dit schema identiek op alle vijf dagen; verplaats geen pauzes.",
        "dark": False,
        "steps": ["Read the timebox.", "Name its artifact.", "Name its acceptance check."],
        "expected": "Participants can navigate the whole day before it starts.",
        "check": "The opening, lunch, the breaks and the close match the day guide.",
    }


def after_lunch(route, day_no):
    title = route["title"] if re.match(r"^day \d", route["title"], re.I) else f"Day {day_no} route"
    return {**route, "cards": [dict(c) for c in route["cards"]], "title": f"{title} · after lunch", "kicker": "FIXED SCHEDULE · 13:00–16:00", **AFTER_LUNCH}


def main():
    for squad, path in DECKS.items():
        decks = json.loads(path.read_text(encoding="utf-8"))
        for key, deck in decks.items():
            slides, day_no = deck["slides"], int(key[-1])
            at = next((i for i, s in enumerate(slides) if is_route(s) and "after lunch" not in s["title"].lower()), -1)
            if at >= 0:
                # One name and one place on every deck: "Day N route", right after the cover.
                slides[at]["title"] = f"Day {day_no} route"
                if at != 1:
                    slides.insert(1, slides.pop(at))
                    at = 1
            if at < 0:
                blocks = blocks_of(slides)
                if not blocks:
                    print(f"{squad} {key}: no timed blocks, no route")
                    continue
                slides.insert(1, route_slide(day_no, blocks))
                at = 1
            if not any("after lunch" in s.get("title", "").lower() for s in slides):
                resume = next((i for i, s in enumerate(slides) if i > at and resumes_after(s, 13 * 60)), -1)
                if resume > 0:
                    slides.insert(resume, after_lunch(slides[at], day_no))
            print(f"{squad} {key}: route at {at + 1}, {len(slides)} slides")
        path.write_text(json.dumps(decks, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
