# Crew 2 Day 5 — independent cutoff-only transfer

Mode: `INDEPENDENT` · Time: `10:00–16:00` · Status: `FUTURE CURRICULUM`

Run all prompts and commands from the repository root.

## Outcome and boundary

Each learner independently copies the existing payment CSVs unchanged into a
separate local working directory, applies only cutoff
`2026-09-13 12:00 Europe/Amsterdam`, and records a fresh reconciliation. The
learner proves that `TX-NS-1008` changes from a timing item to overdue at the
new cutoff while source data and all other rules remain unchanged.

Read the [payment scenario](../../scenarios/payment-reconciliation/README.md),
[FIN-006](../../scenarios/payment-reconciliation/tickets/FIN-006.md), and the
[crew 2 Day 4 handoff](day-4.md). Use a separate path such as
`lab-notes/crew-2/day-5-variation/data/`; do not edit
`scenarios/payment-reconciliation/data/`.

## Fixed agenda

| Time | Minutes | Block | Artifact |
| --- | ---: | --- | --- |
| 10:00–10:15 | 15 | Open | Kahoot + wordcloud, independence contract |
| 10:15–10:35 | 20 | Demo | Hash and cutoff comparison |
| 10:35–11:00 | 25 | Individual attempt | Personal scope and copy check |
| 11:00–11:20 | 20 | Review | Peer readback of boundary |
| 11:20–11:30 | 10 | Break | — |
| 11:30–12:10 | 40 | Practice | Independent local recalculation |
| 12:10–12:30 | 20 | Check | Human data-integrity gate |
| 12:30–13:15 | 45 | Lunch | — |
| 13:15–14:00 | 45 | Practice | Exception and cutoff comparison |
| 14:00–14:10 | 10 | Break | — |
| 14:10–15:00 | 50 | Transfer | Fresh reader reproduces variation |
| 15:00–15:10 | 10 | Break | — |
| 15:10–15:40 | 30 | Handoff | Independent result and rollback |
| 15:40–16:00 | 20 | Close | Rating and MOB recap |

Total: **360 minutes**. The 25-minute personal attempt is mandatory before
any peer comparison. Peer groups of 3–4 may review after that block, with one
navigator and rotating driver only for shared readbacks.

## Phase lens

`Plan`, `Design`, `Test`, `Maintain`, and local transfer are in scope.
`Build` and `Deploy` are `NOT IN SCOPE — the copied fixture is recalculated
locally and never published or deployed`.

## Literal task cards

### 1. Open and demo — 10:00–10:35

**Task card:** Explain the independent contract: copy bytes unchanged, change
one cutoff, prove the changed classification, and preserve a rollback path.
Introduce “transfer variation” before using it.

**Example prompt:**

> Show the source directory, destination directory, and cutoff comparison.
> State what may change (the cutoff input) and what must not change (CSV
> contents, fee rule, duplicate rule, and source IDs). Do not run a production
> command or claim learner evidence.

**Output:** Trainer's hash and cutoff demonstration with expected values clearly
labelled as examples.

**Human acceptance:** Facilitator confirms the destination is separate and the
baseline sources remain read-only.

### 2. Individual attempt — 10:35–11:00

**Task card:** Create the variation directory and record source/destination
paths, copy method, hashes or byte comparison, cutoff, and rollback.

**Example prompt:**

> Copy all three CSVs from `scenarios/payment-reconciliation/data/` into
> `lab-notes/crew-2/day-5-variation/data/` without editing them. Record exact
> commands and a hash or byte comparison. Set cutoff to `2026-09-13` in a
> separate worksheet; do not modify the baseline files.

**Output:** `lab-notes/crew-2/day-5-scope.md`.

**Human acceptance:** Reviewer confirms copied files match the baseline and
the learner can remove only the local variation to roll back.

### 3. Review — 11:00–11:20

**Task card:** Peer reviews the scope note before any recalculation. Check
that exactly one input changed and every expected sample is labelled.

**Example prompt:**

> Read the scope note and inspect source and destination metadata. Mark
> `PASS`, `FAIL`, or `OPEN` for unchanged CSV contents, separate output path,
> cutoff, rollback, and evidence plan. Do not solve the reconciliation.

**Output:** Boundary readback.

**Human acceptance:** Peer identifies the one allowed change and one forbidden
change without oral coaching.

### 4. Independent practice — 11:30–12:10

**Task card:** Recalculate due-date status at cutoff `2026-09-13` using the
copied data and record actual output in a local worksheet.

**Example prompt:**

> Using only the copied CSVs, recalculate missing-settlement due status at
> `2026-09-13 12:00 Europe/Amsterdam`. Cite the ledger row and cutoff
> comparison for `TX-NS-1008`. Record the command/output actually observed;
> do not alter source rows.

**Output:** Variation worksheet with observed status.

**Human acceptance:** Learner shows the new cutoff in the calculation and
marks any unavailable check `OPEN`.

### 5. Check — 12:10–12:30

**Task card:** Human gate data integrity and the changed classification.
Compare against the baseline only as a labelled reference.

**Example prompt:**

> Reopen the baseline and copied files. Verify unchanged contents, the new
> cutoff, and the due-date comparison for `TX-NS-1008`. Mark each item
> `PASS`, `FAIL`, or `OPEN`. Do not call the result a production control.

**Output:** Accepted or parked variation worksheet.

**Human acceptance:** Reviewer confirms only the cutoff changed and
`TX-NS-1008` is overdue at the new cutoff.

### 6. Exception comparison — 13:15–14:00

**Task card:** Compare baseline and variation classifications and show that
fee, duplicate, and bank cases retain their original rules.

**Example prompt:**

> Compare the two local worksheets. Explain which classification changes with
> cutoff and which cases do not. Cite source IDs and calculations. Keep
> `TX-NS-1008` overdue tied to `2026-09-13`; do not edit CSVs or infer a new
> policy.

**Output:** Difference table labelled `TRANSFER VARIATION`.

**Human acceptance:** Facilitator finds one cutoff-caused difference and no
unexplained data difference.

### 7. Transfer — 14:10–15:00

**Task card:** Give the variation to a fresh reader. They reproduce the copy
check and the `TX-NS-1008` cutoff calculation from the artifact alone.

**Example prompt:**

> You are the receiving reviewer. Verify the source and destination contents,
> rerun the local due-date check, and state why `TX-NS-1008` is overdue at
> `2026-09-13`. If a command or hash is missing, mark it `OPEN`.

**Output:** Fresh-reader reproduction and discrepancy list.

**Human acceptance:** Receiver reproduces the result without changing the
copied data or asking the author to explain it.

### 8. Handoff and close — 15:10–16:00

**Task card:** Store scope, copy evidence, recalculation, difference table,
reviewer, rollback, next owner, and `OPEN` items. Close with rating and MOB
recap.

**Example prompt:**

> Draft the independent transfer handoff: baseline path, copied path, hashes
> or byte check, cutoff, exact commands/output, changed classification,
> unchanged rules, reviewer, rollback, and `OPEN` items. Rate yourself
> independent, with help, or needs practice. Add one agreed group lesson.

**Output:** `lab-notes/crew-2/day-5-handoff.md`.

**Human acceptance:** Facilitator confirms the packet is reproducible, the
baseline files are unchanged, and no remote or production outcome is claimed.

## Close script

Repeat the opening Kahoot and wordcloud. Each learner gives a rating and one
check they can now run alone. Record the agreed MOB recap and leave team
approval, access, and any missing runtime evidence as `OPEN`.
