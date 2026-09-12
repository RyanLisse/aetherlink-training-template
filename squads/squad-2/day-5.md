# Squad 2 Day 5 · Own team issue end to end

Mode: INDEPENDENT WITH TEAM GATE · 10:00–16:00

Bring one small issue from the team's real work pattern into the local training workspace. Use a fictional or sanitised copy. The team decides whether the final artifact is ready for a real GitLab, Jira, or Confluence workflow. No remote record is created during training.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **MOB programming** · What is MOB programming? [3] → MOB programming · see the roles [4] → MOB programming · how we use it [5]
- **Human gate** · What is a human gate? [6] → Human gate · see the decision [7] → Human gate · how we use it [8]
<!-- concepts:end -->

<!-- example:start -->
## Worked example · daily payment reconciliation

One example runs from Day 1 to Day 5; see [worked-example.md](worked-example.md). Today's step, with the site slide number in brackets:

- **The example · gate and handoff** [9] · FIN-003 end to end as a MOB, a gate decision per ticket, and three handoff drafts with OPEN links.
  - Expected: Gate decisions, three drafts, and one own-issue brief in the same shape.
  - Checkpoint: The receiver can state current state and next owner without asking the sender.
<!-- example:end -->

## Schedule

| Time | Minutes | Block | Result |
|---|---|---|
| 10:00–10:15 | 15 | Recap + theory | Choose issue, scope, human gate |
| 10:15–10:35 | 20 | Instruction + demo | End-to-end issue flow |
| 10:35–11:00 | 25 | Individual | Write issue brief and plan |
| 11:00–11:20 | 20 | Review | Team checks scope and evidence |
| 11:20–11:35 | 15 | Break | — |
| 11:35–12:00 | 25 | Group practice | Analyst, developer, tester roles |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Theory | Review, release, handoff gates |
| 13:15–14:00 | 45 | Individual + group | Execute local issue flow |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Fresh reader reproduces outcome |
| 15:05–15:40 | 35 | Handoff | GitLab/Jira/Confluence draft fields |
| 15:40–16:00 | 20 | Close | Check-in, Kahoot, wordcloud, MOB reflection |

**Prompt.** Run `FIN-003` (duplicate quarantine) end to end as a MOB: the agent inspects only the named CSVs, runs `check_fixture.py`, and returns evidence. Gate every FIN ticket; `UNRESOLVED` is a valid outcome. Produce the GitLab MR, Jira task, and Confluence recap drafts from `scenarios/payment-reconciliation/workflow.md` with links `OPEN`. Then repeat the shape on the team's own sanitised issue; the status desk scenario (`SCN-001` to `SCN-007`) is the reserve when the team wants a code change. Do not publish or merge.

**Checkpoint.** The team has one issue brief, implementation or explicit `OPEN`, review evidence, human decision, rollback, and receiver-ready handoff.

