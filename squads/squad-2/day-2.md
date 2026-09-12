# Squad 2 Day 2 · AI-native SDLC feedback loop

Mode: FULLY GUIDED · 10:00–16:00

Continue the [Academy course](https://academy.claude.com/courses/ai-native-sdlc-playbook). Turn the lifecycle map into one small, reviewable loop.

<!-- concepts:start -->
## Concept slides

Each concept is taught in three slides: definition, visual, how we use it. Site slide numbers in brackets.

- **Evidence rule** · What is the evidence rule? [3] → Evidence rule · see the ladder [4] → Evidence rule · how we use it [5]
<!-- concepts:end -->

<!-- example:start -->
## Worked example · daily payment reconciliation

One example runs from Day 1 to Day 5; see [worked-example.md](worked-example.md). Today's step, with the site slide number in brackets:

- **The example · plan and hand baseline** [6] · The smallest plan for the batch review, then the six batches by hand. Today's minutes are tomorrow's baseline.
  - Expected: A plan card and a hand worksheet with a time per person.
  - Checkpoint: The worksheet leaves B-20260909-01 UNRESOLVED and calls TX-NS-1008 timing.
<!-- example:end -->

## Schedule

| Time | Minutes | Block | Result |
|---|---|---|
| 10:00–10:15 | 15 | Recap + theory | Rebuild the SDLC map |
| 10:15–10:35 | 20 | Instruction + demo | Intent → plan → change → test |
| 10:35–11:00 | 25 | Individual | Draft a change plan |
| 11:00–11:20 | 20 | Review | Check scope and evidence |
| 11:20–11:35 | 15 | Break | — |
| 11:35–12:00 | 25 | Group practice | Compare plans |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Theory | Feedback, review, and handoff |
| 13:15–14:00 | 45 | Individual + group | Add positive and negative checks |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Fresh reader follows checklist |
| 15:05–15:40 | 35 | Handoff | Evidence card and next owner |
| 15:40–16:00 | 20 | Close | Check-in, Kahoot, wordcloud, MOB reflection |

**Prompt.** For the reconciliation example, write the smallest plan with inputs (three CSVs, cutoff, fee rule), expected result (five cases), two positive checks (`TX-NS-1001` fee is 250; batch `B-20260908-01` sums to bank 20,972), two negative checks (`TX-NS-1008` is not overdue; `SET-1003-B` is not counted), human gate, and rollback. Then classify the six batches by hand and write down your minutes. Do not invoke an agent yet.

**Checkpoint.** The plan is small enough to hand to an agent on Day 3 and clear enough for a human to reject; the hand worksheet leaves `B-20260909-01` `UNRESOLVED` and calls `TX-NS-1008` timing.

