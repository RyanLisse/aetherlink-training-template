#!/usr/bin/env python3
"""Place every concept as definition → visual → how-we-use-it in the day decks.

Idempotent: concept slides are matched by title, removed, and re-inserted after
their anchor. Run from the repository root or from presentations/.

  python3 presentations/apply_concepts.py            # apply
  python3 presentations/apply_concepts.py --check    # exit 1 if decks would change
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REG = json.loads((HERE / "concepts.json").read_text(encoding="utf-8"))
SITE = HERE.parent.parent.parent / "work" / "aether-site" / "dist"
REGISTRY_VAR = {"day-decks.json": "DAYS", "../squads/squad-2/presentations.json": "SQUAD2"}
SITE_FILE = {"day-decks.json": "days.js", "../squads/squad-2/presentations.json": "squad2.js"}
KICKER = {"definition": "CONCEPT DEFINITION · {name}", "visual": "VISUAL · {name}", "usage": "HOW WE USE IT · {name}"}


def slide(concept, kind, spec_override=None):
    spec = REG["concepts"][concept]
    s = dict(spec_override if spec_override is not None else spec[kind])
    layout = s.get("layout") or ("image" if kind == "visual" else "cards")
    out = {
        "title": s["title"],
        "kicker": KICKER[kind].format(name=spec["name"].upper()),
        "subtitle": s["subtitle"],
        "cards": s.get("cards", []),
        "prompt": s["prompt"],
        "notes": s.get("notes", REG["notes_default"]),
        "dark": False,
        "steps": s["steps"],
        "expected": s["expected"],
        "check": s["check"],
        "layout": layout,
    }
    for k in ("image", "imageAlt", "imageCaption", "columns", "items", "tagline"):
        if k in s:
            out[k] = s[k]
    return out


def recap_slide(concept):
    spec = REG["concepts"][concept]
    d, v, u = spec["definition"], spec["visual"], spec["usage"]
    return {
        "title": f"{spec['name']} · recap",
        "kicker": f"RECAP · {spec['name'].upper()}",
        "subtitle": d["subtitle"],
        "cards": d.get("cards", []),
        "prompt": "One-minute recap: read the definition cards, point at the picture, then ask the room to say it in one sentence before the exercise.",
        "notes": REG["notes_default"],
        "dark": False,
        "steps": ["Say the definition in one sentence."] + u["steps"][:1],
        "expected": d["expected"],
        "check": d["check"],
        "layout": "image",
        "keepCards": True,
        "image": v["image"],
        "imageAlt": v["imageAlt"],
        "imageCaption": v["imageCaption"],
    }


def concept_titles():
    titles = {spec[k]["title"] for spec in REG["concepts"].values() for k in ("definition", "visual", "usage")}
    titles |= {v["title"] for spec in REG["concepts"].values() for v in spec.get("extra_visuals", [])}
    titles |= {f"{spec['name']} · recap" for spec in REG["concepts"].values()}
    titles |= {d["slide"]["title"] for ex in REG.get("examples", {}).values() for d in ex["days"].values()}
    return titles


def example_slides(rel, day):
    """Worked-example slides for one deck day, keyed 'day4' or 'day4-value'."""
    days = REG.get("examples", {}).get(rel, {}).get("days", {})
    return [(d["after"], d["slide"]) for key, d in days.items() if key.split("-")[0] == day]


def apply(rel, deck_path, placements, removals, patches):
    decks = json.loads(deck_path.read_text(encoding="utf-8"))
    titles = concept_titles()
    for day, deck in decks.items():
        drop = set(removals.get(day, [])) | titles
        deck["slides"] = [s for s in deck["slides"] if s["title"] not in drop]
        for patch in patches:
            if patch["day"] in ("*", day):
                for s in deck["slides"]:
                    if s["title"] == patch.get("title") or s["kicker"] == patch.get("kicker"):
                        s.update(patch["set"])
        for p in placements.get(day, []):
            idx = next(i for i, s in enumerate(deck["slides"]) if s["title"] == p["after"])
            spec = REG["concepts"][p["concept"]]
            if p.get("mode") == "recap":
                triplet = [recap_slide(p["concept"])]
            else:
                triplet = [slide(p["concept"], "definition"), slide(p["concept"], "visual")]
                triplet += [slide(p["concept"], "visual", v) for v in spec.get("extra_visuals", [])]
                triplet.append(slide(p["concept"], "usage"))
            deck["slides"][idx + 1:idx + 1] = triplet
        for after, s in example_slides(rel, day):
            idx = next(i for i, x in enumerate(deck["slides"]) if x["title"] == after)
            deck["slides"].insert(idx + 1, s)
    return decks


START, END = "<!-- concepts:start -->", "<!-- concepts:end -->"
EX_START, EX_END = "<!-- example:start -->", "<!-- example:end -->"


def example_section(rel, deck, day):
    slides = example_slides(rel, day)
    if not slides:
        return ""
    name = REG["examples"][rel]["name"]
    titles = [s["title"] for s in deck["slides"]]
    lines = [EX_START, f"## Worked example · {name}", "", "One example runs from Day 1 to Day 5; see [worked-example.md](worked-example.md). Today's step, with the site slide number in brackets:", ""]
    for _, s in slides:
        lines.append(f"- **{s['title']}** [{titles.index(s['title']) + 1}] · {s['subtitle']}")
        lines.append(f"  - Expected: {s['expected']}")
        lines.append(f"  - Checkpoint: {s['check']}")
    return "\n".join([*lines, EX_END])


def workbook_section(deck, placements):
    lines = ["## Concept slides", "", "Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.", ""]
    titles = [s["title"] for s in deck["slides"]]
    for p in placements:
        spec = REG["concepts"][p["concept"]]
        if p.get("mode") == "recap":
            lines.append(f"- **{spec['name']}** · recap in one slide [{titles.index(spec['name'] + ' · recap') + 1}]")
            continue
        nums = [titles.index(spec[k]["title"]) + 1 for k in ("definition", "visual", "usage")]
        lines.append(f"- **{spec['name']}** · {spec['definition']['title']} [{nums[0]}] → {spec['visual']['title']} [{nums[1]}] → {spec['usage']['title']} [{nums[2]}]")
    return "\n".join([START, *lines, END])


def write_workbooks(rel, decks, placements, check):
    changed = False
    for day, deck in decks.items():
        if not placements.get(day):
            continue
        path = (HERE / REG["workbooks"][rel].format(n=day[-1])).resolve()
        text = path.read_text(encoding="utf-8")
        block = workbook_section(deck, placements[day])
        if START in text:
            new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
        else:
            new = re.sub(r"^## Schedule", block + "\n\n## Schedule", text, count=1, flags=re.M)
        ex_block = example_section(rel, deck, day)
        if EX_START in new:
            new = re.sub(re.escape(EX_START) + ".*?" + re.escape(EX_END), lambda _: ex_block, new, flags=re.S)
        elif ex_block:
            new = new.replace(END, END + "\n\n" + ex_block, 1)
        if new != text:
            changed = True
            if not check:
                path.write_text(new, encoding="utf-8")
    return changed


def main():
    check = "--check" in sys.argv
    changed = False
    for rel, placements in REG["placements"].items():
        path = (HERE / rel).resolve()
        decks = apply(rel, path, placements, REG.get("remove", {}).get(rel, {}), REG.get("patches", {}).get(rel, []))
        text = json.dumps(decks, ensure_ascii=False, indent=2) + "\n"
        if path.read_text(encoding="utf-8") != text:
            changed = True
            if not check:
                path.write_text(text, encoding="utf-8")
        site = SITE / SITE_FILE[rel]
        js = f"window.{REGISTRY_VAR[rel]} = " + json.dumps(decks, ensure_ascii=False) + ";\n"
        if site.exists() and site.read_text(encoding="utf-8") != js:
            changed = True
            if not check:
                site.write_text(js, encoding="utf-8")
        changed = write_workbooks(rel, decks, placements, check) or changed
        for day, deck in decks.items():
            print(f"{path.name} {day}: {len(deck['slides'])} slides")
    if check and changed:
        print("decks are out of date; run apply_concepts.py", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
