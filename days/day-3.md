# Day 3 — Coached exceptions: missing and duplicate cases

Use the fictional payment fixtures and the accepted Day 2 evidence chain. This
session increases practice while introducing no new concepts.

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Opening and handoff readback |
| 10:15–10:40 | 25 | Concept recap: source IDs, status, human gate |
| 10:40–11:20 | 40 | Exercise 1: reproduce missing settlement |
| 11:20–11:30 | 10 | Break |
| 11:30–12:10 | 40 | Exercise 2: quarantine duplicate |
| 12:10–12:30 | 20 | Optional coaching on request |
| 12:30–13:15 | 45 | Lunch |
| 13:15–14:00 | 45 | Exercise 3: compare two independent findings |
| 14:00–14:10 | 10 | Break |
| 14:10–15:00 | 50 | Exercise 4: complete evidence table |
| 15:00–15:10 | 10 | Break |
| 15:10–15:40 | 30 | Exercise 5: coached handoff |
| 15:40–16:00 | 20 | Individual check-in and MOB reflection |

Total: **360 minutes**.

For every exercise, the trainer gives a short clarification and demonstrates a
small step only when requested. MOBs have 3–5 people, one screen,
facilitator/timekeeper, and driver/navigator rotating every 5–7 minutes. The
driver operates the agent; the group remains accountable. Use the respectful
pause rule. Each check is observable and has a human gate.

## Exercises

1. **Missing settlement.** Read `TX-NS-1007`, due date, and the absence of a
   PSP row. Prompt: “From the three CSVs, reproduce this case at the fixed
   cutoff. Cite every source ID, calculation, and status; do not call it an
   error until the due-date rule is checked.” Output one evidence row. Check:
   peer reproduces it. Gate: facilitator accepts `OPEN`/overdue classification.
2. **Duplicate settlement.** Read `SET-1003-A` and `SET-1003-B` beside their
   ledger and bank rows. Prompt: “Show raw and provisional unique totals,
   keep both rows visible, and explain why the batch is UNRESOLVED.” Output a
   case note. Check: no silent deletion or double count. Gate: policy owner
   accepts quarantine wording.
3. **Independent findings.** Two mobs separately review Exercises 1–2 using
   read-only evidence. Prompt: “Return PASS or BLOCKED with source IDs and
   reproduction steps; do not read the other review.” Output two findings.
   Check: reviewer can compare without merging drafts. Gate: human resolves
   disagreement or records it OPEN.
4. **Evidence table.** Complete the five-case table from the source files and
   cite calculations. Prompt: “Use only observed rows; separate expected sample
   facts from this run.” Output `lab-notes/day-3-evidence.md`. Check: receiver
   reproduces one missing and one duplicate case. Gate: evidence owner signs.
5. **Handoff.** Prompt: “Draft a receiver-ready handoff with cutoff, revision,
   checked cases, unresolved decisions, next owner, and exact command.” Output
   `lab-notes/handoff-day-3.md`. Check: fresh reader finds next action in two
   minutes. Gate: facilitator accepts PASS or BLOCKED.

## Reflection

Write which source row changed your classification and what remains uncertain.
Keep team links `OPEN` unless the team supplied real links.

## Daily opening and closing instructions

At 10:00, the facilitator runs a Kahoot question: "Does a bank match prove a duplicate PSP row is safe to remove?"
Expected explanation: No. Keep both rows visible and the case unresolved until source confirmation.
Then use the wordcloud prompt: "Which step blocks you today?" Cluster the
answers, choose one blocker, and record it in the day's notes. If Kahoot is
unavailable, collect the same answers on the shared board.

At 15:40, each person answers: "What did I verify, what remains uncertain,
and what will I do next?" In the mob reflection, revisit the opening blocker
and name one helpful role change or prompt correction. Copy
[the daily recap template](../templates/daily-recap.md) to a dated file under
`recaps/` for session 3; record actual evidence, open actions, and owners,
and link it from `recaps/README.md`. Update `progress.md` with observed training
results. Add a reviewed knowledge note and index link, or record
`NONE — no reusable learning yet`. Do not record fictional financial recovery.
