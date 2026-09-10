# Day 4 — Reliable repetition and peer knowledge handoff

Use the same fictional payment fixtures and reviewed rules. Support is lighter:
the trainer coaches the method, while each learner owns a repeatable runbook.

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Opening and transfer from Day 3 |
| 10:15–10:40 | 25 | Concept recap: repeatability and evidence |
| 10:40–11:15 | 35 | Exercise 1: run the checklist |
| 11:15–11:25 | 10 | Break |
| 11:25–12:00 | 35 | Exercise 2: write the runbook |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:20 | 20 | Optional coaching on request |
| 13:20–14:05 | 45 | Exercise 3: peer reproduce and challenge |
| 14:05–14:15 | 10 | Break |
| 14:15–15:05 | 50 | Exercise 4: improve the handoff |
| 15:05–15:15 | 10 | Break |
| 15:15–15:45 | 30 | Exercise 5: knowledge teach-back |
| 15:45–16:00 | 15 | Individual check-in and MOB reflection |

Total: **360 minutes**.

The trainer gives a clarification or short demo only when requested; exercises
are peer-led. MOBs are 3–4 people on one screen; facilitator/timekeeper and
reviewer are named, driver/navigator rotate every 5–7 minutes, and the driver
operates the agent. Keep the literal task card visible; if the group is blocked
or drifting for five minutes, the facilitator intervenes by restating the task,
pointing to the source, or stopping at the gate. Pause to surface an
assumption. Each check is observable and has a human gate.

## Exercises

1. **Checklist.** Use a prompt requesting inputs, cutoff, identifiers, fee/net,
   duplicates, due dates, batch totals, and evidence columns. Output a completed
   checklist. Check: a peer ticks each item from source paths. Gate: facilitator
   accepts or marks missing proof OPEN.
2. **Runbook.** Prompt: “Write a one-page procedure for this fictional fixture,
   with commands run from `scenarios/payment-reconciliation`, expected outputs,
   duplicate handling, and handoff fields. Separate validated facts from policy
   questions.” Output `lab-notes/payment-runbook-day-4.md`. Check: no invented
   policy. Gate: human policy owner reviews it.
3. **Peer reproduction.** Give the runbook to a new reader without explanation.
   Output a reproduction note with source IDs and actual output. Check: reader
   completes one normal and one exception. Gate: evidence owner compares notes.
4. **Challenge and repair.** Prompt: “Find one ambiguity or missing evidence in
   this runbook; propose the smallest wording repair and explain its effect.”
   Output a reviewed diff or note. Check: reviewer confirms the repair preserves
   scope. Gate: facilitator accepts the change.
5. **Knowledge handoff.** Prompt: “Prepare a two-minute teach-back and a fresh
   handoff for Day 5; list known fixture IDs, allowed variation, open questions,
   and next gate.” Output `lab-notes/handoff-day-4.md`. Check: recipient repeats
   the process without the answer key. Gate: recipient signs PASS/BLOCKED.

## Reflection

Record the one sentence that made the procedure reusable and the evidence that
supports it. Do not describe the fixture as a production control.

## Daily opening and closing instructions

At 10:00, the facilitator runs a Kahoot question: "What makes a runbook reusable?"
Expected explanation: A new reader can reproduce its checks from the stated inputs and commands.
Then use the wordcloud prompt: "Which step blocks you today?" Cluster the
answers, choose one blocker, and record it in the day's notes. If Kahoot is
unavailable, collect the same answers on the shared board.

At 15:40, each person answers: "What did I verify, what remains uncertain,
and what will I do next?" In the mob reflection, revisit the opening blocker
and name one helpful role change or prompt correction. Copy
[the daily recap template](../templates/daily-recap.md) to a dated file under
`recaps/` for session 4; record actual evidence, open actions, and owners,
and link it from `recaps/README.md`. Update `progress.md` with observed training
results. Add a reviewed knowledge note and index link, or record
`NONE — no reusable learning yet`. Do not record fictional financial recovery.
