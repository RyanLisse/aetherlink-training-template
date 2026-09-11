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


def concept_titles():
    titles = {spec[k]["title"] for spec in REG["concepts"].values() for k in ("definition", "visual", "usage")}
    titles |= {v["title"] for spec in REG["concepts"].values() for v in spec.get("extra_visuals", [])}
    return titles


def apply(deck_path, placements, removals, patches):
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
            triplet = [slide(p["concept"], "definition"), slide(p["concept"], "visual")]
            triplet += [slide(p["concept"], "visual", v) for v in spec.get("extra_visuals", [])]
            triplet.append(slide(p["concept"], "usage"))
            deck["slides"][idx + 1:idx + 1] = triplet
    return decks


START, END = "<!-- concepts:start -->", "<!-- concepts:end -->"


def workbook_section(deck, placements):
    lines = ["## Concept slides", "", "Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.", ""]
    titles = [s["title"] for s in deck["slides"]]
    for p in placements:
        spec = REG["concepts"][p["concept"]]
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
        decks = apply(path, placements, REG.get("remove", {}).get(rel, {}), REG.get("patches", {}).get(rel, []))
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
