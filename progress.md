# Progress

Status: `VERIFIED — 2026-09-11 by Ryan's DA (Ava); recheck before the next live day`

This file is a current-state board, not a diary. Keep one short entry per fact and attach evidence.

## Current verified state

- Repository structure: verified 2026-09-11; evidence: `git log --oneline -5` on branch `rename-crew-to-squad-breaks`.
- Concept cadence: every concept ships as definition → visual → how we use it in both squads, generated from [presentations/concepts.json](presentations/concepts.json) by [presentations/apply_concepts.py](presentations/apply_concepts.py); evidence: `python3 presentations/apply_concepts.py --check` exits 0.
- Slide language: all participant-visible slide text is English; facilitator `notes` stay Dutch; evidence: heuristic Dutch scan over `days.js` and `squad2.js` reports only false positives on "loop", "we", "use".
- Site registries: `days.js` and `squad2.js` are `JSON.stringify`-equal to the canonical decks; evidence: apply_concepts.py regenerates both and the site gate (`work/bundle-update/check_site_dom.cjs`) passes 185 renders.
- Diagrams: seven concept diagrams in `assets/` follow the training-site design system (see the site repo's `design.md`).
- Training outcome: `OPEN — no live outcome recorded yet`.
- Current phase: `Design` (decks and workbooks), `Build` (site) — Test and Deploy of the public Site remain a separate publish step.
- Last independently rechecked artifact: site diff reviewed twice by an independent reviewer lane on 2026-09-11; all findings fixed.

## Blockers

| Blocker | Mechanism or impact | Owner | Evidence | Status |
| --- | --- | --- | --- | --- |
| Public Site not republished | Sites serves the previous version; participants see old slides until the checkout is published | Ryan | site repo HEAD vs live site | `OPEN` |
| Live n8n / Claude Code model runs never executed in this repo | Synthetic examples do not prove a model run | Ryan | none | `OPEN` |

## Next actions

| Action | Owner | Due | Acceptance check | Evidence |
| --- | --- | --- | --- | --- |
| Publish the site checkout to Sites | Ryan | before the next live day | Live URL serves the concept triplets | `OPEN` |
| Make squad 2 practice slides day-specific (steps, prompts, checkpoints) | Ryan | `YYYY-MM-DD` | No two practice slides share the same four steps | `OPEN` |
| Turn recap slides into three-question quizzes | Ryan | `YYYY-MM-DD` | Each recap slide reveals three answers | `OPEN` |

## Evidence links

- Recaps: `OPEN` — add dated links under [recaps/](recaps/README.md).
- Knowledge: `OPEN` — add reviewed links under [knowledge/](knowledge/README.md).
- Decisions: concept cadence and English-only rule recorded in the site repo's `intent.md` and `design.md`.
- Handoffs: `OPEN` — add current records under [handoffs/](handoffs/README.md).
