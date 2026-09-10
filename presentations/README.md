# Daily presentation source

[day-decks.json](day-decks.json) contains five participant decks, copyable exercise prompts, checkpoints, and Dutch facilitator notes. Days 1, 3, 4, and 5 use the same 10:00–16:00 rhythm: opening 15 minutes; concept/demo 25; exercise 1 40; break 10; exercise 2 40; demo/coaching 20; lunch 45; exercise 3 45; break 10; exercise 4 50; break 10; exercise 5 30; reflection 20. Day 2 is the deliberate exception: its first 90 minutes guide one narrow FIN-003 ticket, then analyst, developer, tester, review, handoff, and close passes run through 16:00; see the [guided ticket exercise](../scenarios/payment-reconciliation/guided-ticket-exercise.md).

- [Day 1 — Guided foundations](https://aetherlink-training.ryanlisse.chatgpt.site/?day=1#1)
- [Day 2 — FIN-003 guided ticket relay](https://aetherlink-training.ryanlisse.chatgpt.site/?day=2#1)
- [Day 3 — Coached investigation](https://aetherlink-training.ryanlisse.chatgpt.site/?day=3#1)
- [Day 4 — Repeatability and handoff](https://aetherlink-training.ryanlisse.chatgpt.site/?day=4#1)
- [Day 5 — Independent transfer](https://aetherlink-training.ryanlisse.chatgpt.site/?day=5#1)
- [Full workbooks and setup](../days/README.md)

Days 1 and 2 introduce MOB programming with literal trainer demonstrations. Use groups of three or four, one navigator directing the human driver, and route other observations through the navigator; rotate driver and navigator every 5–7 minutes. If a group is blocked or drifting for five minutes, the facilitator spends up to five minutes restating the task, pointing to the relevant source, or clarifying the role boundary, then parks any longer policy question as `OPEN`. Days 3–5 progressively reduce coaching. Day 5 uses a clearly labelled local transfer worksheet with cutoff `2026-09-13`; source CSVs remain unchanged. The team workflow is GitLab, Jira, and Confluence; GitHub distributes this public material.

The repository imports [intent.md](../intent.md), [progress.md](../progress.md), and [AGENTS.md](../AGENTS.md) through its root `CLAUDE.md`; these are custom conventions for outcome, current-state, and evidence tracking. Read them before changing a deck. Skills are optional follow-up guidance after the visible exercise result exists and never replace a human gate or evidence check.

The interactive presentations use AetherLink styling. ChatGPT sign-in and site access are separate from this public repository. Editing this JSON does not automatically publish the site. Keep prompts and times aligned with the workbooks when updating.
