# Five session guides

This public-safe programme adapts the AI-native SDLC playbook to a fictional
payment reconciliation exercise. It runs five sessions, each 10:00–16:00,
with the same exact 360-minute schedule. Videos and audio were not watched or
listened to; source URLs are preserved in the first two guides.

## Progression

1. [Day 1](day-1.md) — guided framing: ledger/PSP/bank concepts, agent
   context, intent, spec, plan, MOB programming, SDLC loop, and evidence.
2. [Day 2](day-2.md) — guided repeatability: `CLAUDE.md`, skills, handoffs,
   independent review, tests versus evaluations, GitLab/Jira/Confluence, and
   conceptual release controls.
3. [Day 3](day-3.md) — coached missing and duplicate settlement cases.
4. [Day 4](day-4.md) — peer-led repeatable runbook and knowledge handoff.
5. [Day 5](day-5.md) — independent transfer to a declared synthetic variation.

Days 1 and 2 explain all concepts needed for the practice. Later sessions use
the same vocabulary and rules with graduated support; no new concepts are
required. The primary scenario is [payment reconciliation](../scenarios/payment-reconciliation/README.md).

## Shared MOB and evidence rule

Work in groups of three to five on one screen and one shared task. Name a
facilitator/timekeeper and reviewer. Rotate driver and navigator every 5–7
minutes. The driver operates the agent, while humans decide scope and gates.
Anyone may say “pause” to restate the source, assumption, or decision. Every
exercise has a trainer explanation or clarification, a literal prompt, an
observable check, and a human gate. Record actual commands, source IDs,
revision, and open questions; use `OPEN` for unavailable team links.

## Setup

From the repository root:

```sh
python3 --version
mkdir -p lab-notes
```

Read `intent.md`, `progress.md`, the applicable day guide, and the payment
scenario README. For the scenario validator, change into
`scenarios/payment-reconciliation` first and paste the exact command from its
README. Do not push or publish as part of these exercises.

## Daily opening and close

At 10:00, run a short Kahoot retrieval question and wordcloud: "Which step blocks you today?" Cluster the answers and choose one blocker to revisit at the close. At 15:40, each participant names one reproduced result, one uncertainty, and a next action. Finish with the mob reflection and a dated recap; record a reusable knowledge note only when its evidence has been reviewed.
