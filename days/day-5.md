# Day 5 — Independent transfer to a synthetic variation

This is the final practice session. All baseline IDs have been taught, so the
facilitator declares a transfer variation before work begins. Use a working
copy, never the source CSVs: from the repository root copy
`scenarios/payment-reconciliation/data/` to
`lab-notes/day-5-variation/data/`, change the working cutoff to
`2026-09-13 12:00 Europe/Amsterdam`, and recalculate due-date status. Under
that variation, `TX-NS-1008` is overdue rather than a timing item; keep the
duplicate case unresolved. Label results synthetic and transfer-based, not
unseen. The baseline README validator is fixed to 2026-09-10 and exactly five
baseline cases; do not claim its PASS proves the variation. Use a separate
worksheet recalculation and record its actual output.

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Opening, scope, and variation declaration |
| 10:15–10:40 | 25 | Clarification and checkpoint: independent evidence |
| 10:40–11:20 | 40 | Exercise 1: inspect and frame the new case |
| 11:20–11:30 | 10 | Break |
| 11:30–12:10 | 40 | Exercise 2: plan the run |
| 12:10–12:30 | 20 | Checkpoint clinic on request |
| 12:30–13:15 | 45 | Lunch |
| 13:15–14:00 | 45 | Exercise 3: execute independently |
| 14:00–14:10 | 10 | Break |
| 14:10–15:00 | 50 | Exercise 4: independent review and gate |
| 15:00–15:10 | 10 | Break |
| 15:10–15:40 | 30 | Exercise 5: final handoff and teach-back |
| 15:40–16:00 | 20 | Individual check-in and MOB reflection |

Total: **360 minutes**.

Learners work independently first, then use peer review and the final MOB
reflection. The trainer clarifies only when requested. MOBs remain 3–4 people,
one screen, facilitator/timekeeper, and driver/navigator rotating every 5–7
minutes; the driver operates the agent. Keep the literal task card visible; if
the group is blocked or drifting for five minutes, the facilitator intervenes by
restating the task, pointing to the source, or stopping at the gate. Use the
pause rule. The learner owns the run; the human gate accepts the evidence.
Observable checks are below.

## Exercises

The facilitator records the per-person support result: **independent** (no
hint), **one hint** (one clarification), or **coached** (several prompts).
Independent transfer is the target; a coached result is evidence of what to
practise next.

1. **Frame.** Facilitator declares the variation above. Individually create
   `lab-notes/day-5-variation/data/` by copying the three source CSVs, and write
   `lab-notes/day-5-scope.md`. Prompt: “State outcome, changed cutoff, source
   files, and success evidence. Do not edit the source CSVs.” Check: working
   copy and source checksums are recorded. From the repository root, run
   `mkdir -p lab-notes/day-5-variation/data && cp scenarios/payment-reconciliation/data/*.csv lab-notes/day-5-variation/data/`.
   Gate: facilitator accepts.
2. **Plan.** Prompt: “Write a root-relative, read-only plan using the Day 4
   runbook. Use `lab-notes/day-5-variation/data/`, cutoff 2026-09-13, and a
   separate worksheet recalculation. Name risks, evidence columns, and
   rollback. Mark this as transfer variation, not unseen data.” Output
   `lab-notes/day-5-plan.md`.
   Check: another learner can execute it. Gate: human accepts before running.
3. **Execute.** Individually run the declared variation, cite rows, calculate
   totals, and record actual worksheet output. Prompt: “Use only the copied
   synthetic inputs; separate observed results, baseline examples, and
   hypotheses. Do not use the fixed README validator as variation proof.”
   Output `lab-notes/day-5-evidence.md`. Check: source files are unchanged and
   `TX-NS-1008` is recalculated against the new cutoff. Gate: reviewer accepts
   or blocks.
4. **Review.** A fresh context reads the plan and evidence without the author's
   conversation. Prompt: “Check arithmetic, duplicate/due-date treatment,
   scope, and reproducibility. Return PASS or BLOCKED with exact missing proof.”
   Output independent review. Check: reviewer finds a deliberate evidence gap
   if present. Gate: facilitator records decision and open action.
5. **Handoff.** Prompt: “Draft a concise final handoff with variation label,
   revision, source IDs, commands, results, limitations, owner, and next gate.
   Keep GitLab/Jira/Confluence links OPEN unless supplied.” Output
   `lab-notes/handoff-day-5.md` and a two-minute teach-back. Check: receiver
   reproduces the declared case. Gate: named human accepts the series outcome.

## Reflection

Write what transferred from the five sessions, which concept still needs
practice, and what evidence would be required before any real operational use.

## Daily opening and closing instructions

At 10:00, the facilitator runs a Kahoot question: "Does the baseline validator prove a changed-cutoff result?"
Expected explanation: No. Recalculate the declared variation and record separate evidence.
Then use the wordcloud prompt: "Which step blocks you today?" Cluster the
answers, choose one blocker, and record it in the day's notes. If Kahoot is
unavailable, collect the same answers on the shared board.

At 15:40, each person answers: "What did I verify, what remains uncertain,
and what will I do next?" In the mob reflection, revisit the opening blocker
and name one helpful role change or prompt correction. Copy
[the daily recap template](../templates/daily-recap.md) to a dated file under
`recaps/` for session 5; record actual evidence, open actions, and owners,
and link it from `recaps/README.md`. Update `progress.md` with observed training
results. Add a reviewed knowledge note and index link, or record
`NONE — no reusable learning yet`. Do not record fictional financial recovery.
