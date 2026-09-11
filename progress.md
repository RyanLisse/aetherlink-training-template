# Progress

Status: `VERIFIED — 2026-09-11 by Ryan's DA (Ava); recheck before the next live day`

This file is a current-state board, not a diary. Keep one short entry per fact and attach evidence.

## Current verified state

- Repository structure and route alignment: verified 2026-09-11; evidence: commit `b62e104` on `main` and `rename-crew-to-squad-breaks`.
- Concept cadence: every concept ships as definition → visual → how we use it in both squads, generated from [presentations/concepts.json](presentations/concepts.json) by [presentations/apply_concepts.py](presentations/apply_concepts.py); evidence: `python3 presentations/apply_concepts.py --check` exits 0.
- Slide language: all participant-visible slide text is English; facilitator `notes` stay Dutch; evidence: heuristic Dutch scan over `days.js` and `squad2.js` reports only false positives on "loop", "we", "use".
- Site registries: `days.js` and `squad2.js` are `JSON.stringify`-equal to the canonical decks; evidence: apply_concepts.py regenerates both and the site gate (`work/bundle-update/check_site_dom.cjs`) passes 174 renders.
- Diagrams: seven concept diagrams in `assets/` follow the training-site design system (see the site repo's `design.md`).
- Training outcome: `OPEN — no live outcome recorded yet`.
- Current phase: `Design` and `Build` complete for the route update; public Site `Test` and `Deploy` verified on 2026-09-11.
- Last independently rechecked artifact: site diff reviewed twice by an independent reviewer lane on 2026-09-11; all findings fixed.

## Blockers

| Blocker | Mechanism or impact | Owner | Evidence | Status |
| --- | --- | --- | --- | --- |
| Public Site publication | Version 19 now serves commit `a0724df`; live assets match the site checkout | Ryan | Sites deployment `appgdep_6aa4485c906c8191b30171c676eee6b5`, public URL | `DONE` |
| Live n8n / Claude Code model runs never executed in this repo | Synthetic examples do not prove a model run | Ryan | none | `OPEN` |

## Next actions

| Action | Owner | Due | Acceptance check | Evidence |
| --- | --- | --- | --- | --- |
| Run the live n8n / Claude Code smoke test | Ryan | before the next live day | Real run log or exact `OPEN` evidence per platform | `OPEN` |
| Add dated recap, knowledge and handoff links after each live day | Facilitator | after each session | Fresh reader can find the evidence and next owner | `OPEN` |

## Evidence links

- Recaps: `OPEN` — add dated links under [recaps/](recaps/README.md).
- Knowledge: `OPEN` — add reviewed links under [knowledge/](knowledge/README.md).
- Decisions: concept cadence and English-only rule recorded in the site repo's `intent.md` and `design.md`.
- Handoffs: `OPEN` — add current records under [handoffs/](handoffs/README.md).
