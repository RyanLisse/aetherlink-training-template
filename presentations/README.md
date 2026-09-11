# Daily presentation source

[day-decks.json](day-decks.json) contains five trainer decks, copyable exercise prompts, checkpoints, and Dutch facilitator notes. Participant agent work for squad 1 Day 3 and squad 2 Day 2 starts at the [aetherlink-agent-lab](https://github.com/RyanLisse/aetherlink-agent-lab) root; these course workbooks remain trainer references. Day 3 and Day 2 now build the same agent in n8n first and Claude Code after lunch, compare `TICKET-OPS-101` under the same functional contract/input with platform adapters and settings recorded, and transfer to `102` only after the human gate:

| Time | Activity |
| --- | --- |
| 10:00–10:10 | Agent theory and loop before either build |
| 10:10–10:20 | n8n demo with approved login |
| 10:20–10:45 | Individual n8n run on each participant’s own laptop |
| 10:45–11:00 | n8n contract review |
| 11:00–11:15 | Break |
| 11:15–11:45 | n8n evidence capture |
| 11:45–12:00 | Human gate |
| 12:00–13:00 | Lunch |
| 13:00–13:10 | Claude Code rebuild demo |
| 13:10–13:35 | Individual Claude Code run on the same `101` |
| 13:35–13:50 | Claude Code contract review |
| 13:50–14:20 | Same-input comparison |
| 14:20–14:35 | Human gate, then `102` transfer |
| 14:35–14:50 | Break |
| 14:50–15:40 | Handoff and evidence readback |
| 15:40–16:00 | Close |

- [Day 1 — Guided foundations](https://aetherlink-training.ryanlisse.chatgpt.site/?day=1#1)
- [Day 2 — FIN-003 guided ticket relay](https://aetherlink-training.ryanlisse.chatgpt.site/?day=2#1)
- [Day 3 — Individual agent practice](https://aetherlink-training.ryanlisse.chatgpt.site/?day=3#1)
- [Day 4 — Repeatability and handoff](https://aetherlink-training.ryanlisse.chatgpt.site/?day=4#1)
- [Day 5 — Independent transfer](https://aetherlink-training.ryanlisse.chatgpt.site/?day=5#1)
- [Full workbooks and setup](../days/README.md)

Days 1 and later MOB sessions use groups of three or four with one navigator directing the human driver; rotate every 5–7 minutes after individual blocks. If a group is blocked or drifting for five minutes, park the question as `OPEN`. Day 3 and squad 2 Day 2 use the participant lab root above; n8n access and credentials are selected separately in preflight, and missing login remains `OPEN`. Both platforms use the same functional input/output contract while their adapter instructions, models, modes, access, and tools are recorded separately; no business-system write or financial approval is performed. Platform differences are observations of the controlled runs and do not establish causality. Day 5 uses a clearly labelled local transfer worksheet with cutoff `2026-09-13`; source CSVs remain unchanged. The team workflow is GitLab, Jira, and Confluence; GitHub distributes this public material.

The repository imports [intent.md](../intent.md), [progress.md](../progress.md), and [AGENTS.md](../AGENTS.md) through its root `CLAUDE.md`; these are custom conventions for outcome, current-state, and evidence tracking. Read them before changing a deck. Skills are optional follow-up guidance after the visible exercise result exists and never replace a human gate or evidence check.

The interactive presentations use AetherLink styling. The site presentation is
public; editing this JSON does not automatically publish it. Keep prompts and
times aligned with the workbooks when updating. Squad 1 Day 3 and squad 2 Day 2
place agent theory before either build, run n8n first, rebuild in Claude Code
after lunch, and protect at least 25 minutes of individual practice on each
platform.
The AI-native SDLC concept uses a standalone loop illustration at
[`assets/ai-native-sdlc-loop.svg`](../assets/ai-native-sdlc-loop.svg). It shows
the six phases around Claude without the traditional SDLC comparison panel, so
the facilitator can use the loop as a reusable phase reference.

## Concept slides

Every concept a squad meets is taught as three slides: definition, visual, how
we use it. They come from [concepts.json](concepts.json); run
`python3 presentations/apply_concepts.py` after editing it. The script removes
the old triplets by title, inserts them after their anchors in both
`day-decks.json` and `../squads/squad-2/presentations.json`, and regenerates the
site registries when the site checkout sits next to this repository.
`--check` exits non-zero when the decks are out of date. Diagrams live in
[`../assets/`](../assets/) and follow the site's design system.
