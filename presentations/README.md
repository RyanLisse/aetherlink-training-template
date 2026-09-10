# Daily presentation source

[day-decks.json](day-decks.json) contains five participant decks, copyable exercise prompts, checkpoints, and Dutch facilitator notes. Days 1, 4, and 5 use the same 10:00–16:00 rhythm: opening 15 minutes; concept/demo 25; exercise 1 35; break 10; exercise 2 35; lunch 60; demo/coaching 20; exercise 3 45; break 10; exercise 4 50; break 10; exercise 5 30; reflection 15. Day 2 is the deliberate exception: its first 90 minutes guide one narrow FIN-003 ticket, then analyst, developer, tester, review, handoff, and close passes run through 16:00; see the [guided ticket exercise](../scenarios/payment-reconciliation/guided-ticket-exercise.md). Day 3 is the Wave 2 crew 1 exception, with an agent recap and individual practice before the missing and duplicate case work:

| Time | Activity |
| --- | --- |
| 10:00–10:10 | Agent recap: definition, loop, model/chat/agent/subagent |
| 10:10–10:15 | Build and invoke the ticket-coach demo |
| 10:15–10:40 | Individual 25-minute run on each participant’s own laptop |
| 10:40–10:50 | Review of the first result |
| 10:50–11:05 | Edit one instruction and rerun with the same input and settings |
| 11:05–11:20 | Transfer to a second ticket |
| 11:20–11:30 | Progress checkpoint |
| 11:30–11:40 | Break |
| 11:40–12:00 | Missing case |
| 12:00–13:00 | Lunch |
| 13:00–13:10 | Check and independent reproduction |
| 13:10–13:50 | Duplicate case |
| 13:50–14:00 | Break |
| 14:00–14:50 | Peer review and evidence |
| 14:50–15:00 | Break |
| 15:00–15:35 | Handoff |
| 15:35–16:00 | Close |

- [Day 1 — Guided foundations](https://aetherlink-training.ryanlisse.chatgpt.site/?day=1#1)
- [Day 2 — FIN-003 guided ticket relay](https://aetherlink-training.ryanlisse.chatgpt.site/?day=2#1)
- [Day 3 — Individual agent practice](https://aetherlink-training.ryanlisse.chatgpt.site/?day=3#1)
- [Day 4 — Repeatability and handoff](https://aetherlink-training.ryanlisse.chatgpt.site/?day=4#1)
- [Day 5 — Independent transfer](https://aetherlink-training.ryanlisse.chatgpt.site/?day=5#1)
- [Full workbooks and setup](../days/README.md)

Days 1 and 2 introduce MOB programming with literal trainer demonstrations. Use groups of three or four, one navigator directing the human driver, and route other observations through the navigator; rotate driver and navigator every 5–7 minutes. If a group is blocked or drifting for five minutes, the facilitator spends up to five minutes restating the task, pointing to the relevant source, or clarifying the role boundary, then parks any longer policy question as `OPEN`. Day 3 uses the [individual ticket-agent pack](../scenarios/ticket-agent/README.md): every participant works on their own laptop, with no driver rotation, and a bounded Claude Code subagent may use Read, Glob, and Grep for previews only. The pack’s template, input, target, and agent roles stay distinct; requirements and the checklist lead over the target, Current and Desired sections are protected, and conflicts remain `OPEN`. A glossary skill or hook is optional follow-up guidance; no new infrastructure is required and the exercise performs no Jira writes. Day 5 uses a clearly labelled local transfer worksheet with cutoff `2026-09-13`; source CSVs remain unchanged. The team workflow is GitLab, Jira, and Confluence; GitHub distributes this public material.

The repository imports [intent.md](../intent.md), [progress.md](../progress.md), and [AGENTS.md](../AGENTS.md) through its root `CLAUDE.md`; these are custom conventions for outcome, current-state, and evidence tracking. Read them before changing a deck. Skills are optional follow-up guidance after the visible exercise result exists and never replace a human gate or evidence check.

The interactive presentations use AetherLink styling. ChatGPT sign-in and site access are separate from this public repository. Editing this JSON does not automatically publish the site. Keep prompts and times aligned with the workbooks when updating. Crew 1 Day 3 and crew 2 Day 2 place a 10–15 minute agent theory/demo before the first ticket-coach build and protect at least 25 minutes of individual practice.
