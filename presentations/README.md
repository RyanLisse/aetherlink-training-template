# Daily presentation source

[day-decks.json](day-decks.json) contains five trainer decks, copyable exercise prompts, checkpoints, and Dutch facilitator notes. Participant agent work starts at the [aetherlink-agent-lab](https://github.com/RyanLisse/aetherlink-agent-lab) root; these course workbooks remain trainer references. The routes are deliberately different: Squad 1 Day 3 is AI-native SDLC planning and evidence, Day 4 builds in n8n, and Day 5 rebuilds in Claude Code with an optional E2E transfer. Squad 2 follows AI-native SDLC on Days 1–2, n8n on Day 3, Claude Code on Day 4, and an own-team issue on Day 5.

| Time | Activity |
| --- | --- |
| 10:00–10:15 | Recap, Kahoot/wordcloud, outcome and roles |
| 10:15–10:35 | AI-native SDLC definition, loop visual and human gates |
| 10:35–11:00 | Individual intent → plan exercise |
| 11:00–11:20 | Fresh-reader review |
| 11:20–11:35 | Break |
| 11:35–12:00 | Group map and human gate |
| 12:00–13:00 | Lunch |
| 13:00–13:30 | Individual evidence route and handoff |
| 13:30–14:00 | Group review of evidence and open questions |
| 14:00–14:15 | Break |
| 14:15–15:05 | Fresh-reader transfer |
| 15:05–15:25 | Human gate and next-day handoff |
| 15:25–15:40 | Recap |
| 15:40–16:00 | Check-out and MOB reflection |

- [Day 1 — Guided foundations](https://aetherlink-training.ryanlisse.chatgpt.site/?day=1#1)
- [Day 2 — FIN-003 guided ticket relay](https://aetherlink-training.ryanlisse.chatgpt.site/?day=2#1)
- [Squad 1 Day 3 — AI-native SDLC](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=1&day=3#1)
- [Squad 1 Day 4 — First agent in n8n](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=1&day=4#1)
- [Squad 1 Day 5 — n8n support triage to Claude Code](https://aetherlink-training.ryanlisse.chatgpt.site/?squad=1&day=5#1)
- [Squad 1 Day 5 — Claude Agent SDK repo, one branch per SDLC step](https://github.com/RyanLisse/aetherlink-day5-n8n-to-agent)
- [Full workbooks and setup](../days/README.md)

Days 1 and later MOB sessions use groups of three or four with one navigator directing the human driver; rotate every 5–7 minutes after individual blocks. If a group is blocked or drifting for five minutes, park the question as `OPEN`. Squad 1 Day 4 and Squad 2 Day 3 use the participant lab root above; n8n access and credentials are selected separately in preflight, and missing login remains `OPEN`. For the 17 September Squad 1 Day 5 route, the [support-triage participant guide](https://github.com/RyanLisse/aetherlink-agent-lab/tree/main/scenarios/support-triage/README.md) and attached n8n export define fictional WL-1026. The n8n source and Claude Code target are a functional translation: Claude preserves `ticket_id` and `risk_note`, validates `priority`, and keeps every action at a human gate. Platform settings and static memory keys are recorded as observations; no business-system write, send, refund or financial approval is performed. The team workflow is GitLab, Jira, and Confluence; GitHub distributes this public material.

The repository imports [intent.md](../intent.md), [progress.md](../progress.md), and [AGENTS.md](../AGENTS.md) through its root `CLAUDE.md`; these are custom conventions for outcome, current-state, and evidence tracking. Read them before changing a deck. Skills are optional follow-up guidance after the visible exercise result exists and never replace a human gate or evidence check.

The interactive presentations use AetherLink styling. The site presentation is
public; editing this JSON does not automatically publish it. Keep prompts and
times aligned with the workbooks when updating. Squad 1 Day 3 and Squad 2 Days 1–2 place the AI-native SDLC theory before
agent building. Squad 1 Day 4 and Squad 2 Day 3 build in n8n; Squad 1 Day 5
translates the attached n8n support flow into Claude Code, while Squad 2 Day 4
builds its own Claude Code workflow. Protect at least 25 minutes of individual
practice in every build block.
The AI-native SDLC concept uses a line-and-loop illustration at
[`assets/ai-native-sdlc-line-and-loop.png`](../assets/ai-native-sdlc-line-and-loop.png). It shows
the traditional line beside the AI-native loop with Claude in the centre, so
the facilitator can use the comparison as a reusable phase reference.

## Concept slides

Every concept a squad meets is taught as three slides: definition, visual, how
we use it. They come from [concepts.json](concepts.json); run
`python3 presentations/apply_concepts.py` after editing it. The script removes
the old triplets by title, inserts them after their anchors in both
`day-decks.json` and `../squads/squad-2/presentations.json`, and regenerates the
site registries when the site checkout sits next to this repository.
`--check` exits non-zero when the decks are out of date. Diagrams live in
[`../assets/`](../assets/) and follow the site's design system. Set `AETHER_SITE`
to the site's `dist/` when the checkout is not next to this repository.

A placement may carry `"mode": "recap"` (the concept's picture and one sentence,
no cards — the definition cards go to the facilitator notes) or
`"order": ["visual", "definition", "usage"]` when the room should see the
picture before it reads the definition. A concept's `visual` may draw a bar
chart (`"layout": "bars"`) instead of an image; `extra_visuals` adds more
visual slides to the triplet. Every day after the first opens with yesterday's
concepts as recap slides, chained after the route slide. A patch may `unset`
keys. A card body is at most 18 words; what is cut goes to the notes verbatim.

## Route slides

`python3 presentations/add_routes.py` gives every deck its route on slide 2 and
the same route again in front of the afternoon. Squad 2's routes are derived
from the deck's own kickers; the two lines no kicker states (lunch before the
human gate, theory and demo until the first timed block) are named in the
script. Run it before `apply_concepts.py`; it is idempotent.

## Worked example (both squads)

The `examples` block in `concepts.json` places one worked-example slide per day (plus the before-and-after slide on Day 4) in the squad 2 deck and writes a `Worked example` block into each workbook. The squad 1 entries use `"from"` to reuse the squad 2 slides with the day counter rewritten, so the example is written once and both squads tell the same story (squad 1 days 3, 4 and 5 map onto squad 2 days 1, 3 and 4). The `_example` patches in the same file rewrite the generic practice slides to name the example step. Design and candidates: [squads/squad-2/worked-example.md](../squads/squad-2/worked-example.md).
