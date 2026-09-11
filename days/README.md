# Five session guides

This public-safe programme adapts the AI-native SDLC playbook to a fictional
payment reconciliation exercise. It runs five sessions, each with its own
10:00–16:00 agenda with lunch fixed at 12:00–13:00. Follow the current guide for the timing; Day 2 includes a
revised n8n-first morning and Claude Code rebuild after lunch. Day 3 uses the
same sequence with a guided individual opening before comparison. Videos and audio were not watched or
listened to; source URLs are preserved in the first two guides.

## Delivery tracks

**Wave 2 crew 1** has completed Days 1–2 and has three sessions remaining:
Days 3–5. Use [Day 3](day-3.md) as its continuation; do not rewrite its prior
handoff as a new five-session start. **Crew 2** is a later, fresh five-session
run; its crew-specific plan is [here](../crews/crew-2/README.md) when that pack
is available. No crew 2 outcome or access is implied by crew 1 material.

## Progression

1. [Day 1](day-1.md) — guided framing: ledger/PSP/bank concepts, agent
   context, intent, spec, plan, MOB programming, SDLC loop, and evidence.
2. [Day 2](day-2.md) — guided FIN-003 ticket relay: one visible result,
   analyst → developer → tester, behavior checks, and individual practice.
   Context and skills are optional after the reviewed result.
3. [Day 3](day-3.md) — build the same bounded agent in n8n, then Claude Code;
   compare `TICKET-OPS-101` and transfer to `102` after the human gate.
4. [Day 4](day-4.md) — choose one of three Claude Code agents, build it with a readable trace.
5. [Day 5](day-5.md) — harden the chosen agent: evaluator-optimizer, trace comparison, handoff.

For the first visible result in the next session after Day 1, use the [guided
ticket exercise](../scenarios/payment-reconciliation/guided-ticket-exercise.md)
with the [Day 2 guide](day-2.md) as a first-90-minute guided reset. Day 1 is
future reusable framing curriculum; this reset continues from its concepts
without asking the cohort to redo that session. Later sessions use the same
vocabulary and rules with graduated support; follow each guide's current
agenda. The primary scenario is [payment reconciliation](../scenarios/payment-reconciliation/README.md).
Day 3's participant workspace is the [aetherlink-agent-lab](https://github.com/RyanLisse/aetherlink-agent-lab).
The trainer workbook's starter, `ticket-inputs.md`, `ticket-template.md` handout,
`target-examples.md`, and `check_ticket.py` are defined in the [ticket-agent
pack](../scenarios/ticket-agent/README.md). Its two input/target pairs are
`TICKET-OPS-101`/Worked target A and `TICKET-OPS-102`/Worked target B. Treat
the pack README as authoritative for preflight steps; both pairs remain `OPEN`
until team signoff.

## Shared MOB and evidence rule

Work in groups of three to four on one screen and one shared task. Keep the
literal task card visible. Name a facilitator/timekeeper and reviewer. Rotate
driver and navigator every 5–7 minutes. If the group is blocked or drifting for
five minutes, the facilitator intervenes by restating the task, pointing to the
source, or stopping at the gate. The driver operates the agent, while humans
decide scope and gates. Anyone may say “pause” to restate the source,
assumption, or decision. Every exercise has a trainer explanation or
clarification, a literal prompt, an observable check, and a human gate. Record
actual commands, source IDs, revision, and open questions; use `OPEN` for
unavailable team links.

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

At 10:00, run the opening specified by the current day guide. On Day 3 this is
a recap, end example, Kahoot, and wordcloud before the individual bounded-agent
practice; the MOB starts only in the afternoon. At 15:40, each participant
names one made artifact, one uncertainty, and a next action. Finish with the
mob reflection and a dated recap; record a reusable knowledge note only when
its evidence has been reviewed. Every close records what was **covered** and
what is **next** from the current guide. Never infer participant success or
tool access from attendance or discussion.
