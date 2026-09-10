# Crew 2 Day 1 — one visible result on your own laptop

Mode: `FULLY GUIDED` · Time: `10:00–16:00` · Status: `FUTURE CURRICULUM`

Run all prompts and commands from the repository root.

## Outcome and boundary

Each learner leaves with one local evidence card for `TX-NS-1004`, citing the
ledger and PSP rows, the expected and observed fee, and a human decision. The
trainer demonstrates the smallest safe read-only loop before learners try it.
No architecture, shared process redesign, code change, remote ticket, network
call, credential, or production claim is part of this day.

Read [the fictional payment scenario](../../scenarios/payment-reconciliation/README.md)
and [the local learner guide](../../scenarios/payment-reconciliation/learner-guide.md).
Use the three CSVs in `scenarios/payment-reconciliation/data/`.

## Fixed agenda

| Time | Minutes | Block | Artifact |
| --- | ---: | --- | --- |
| 10:00–10:15 | 15 | Open | Kahoot + wordcloud, roles, blockers |
| 10:15–10:35 | 20 | Demo | One-row read-only evidence card |
| 10:35–11:00 | 25 | Individual attempt | Learner's first card |
| 11:00–11:20 | 20 | Review | Source-row readback |
| 11:20–11:30 | 10 | Break | — |
| 11:30–12:00 | 30 | Practice | Groups of 3–4, one navigator |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Check | Human acceptance |
| 13:15–14:00 | 45 | Practice | Recheck one nearby row |
| 14:00–14:10 | 10 | Break | — |
| 14:10–15:00 | 50 | Transfer | Fresh-reader reproduction |
| 15:00–15:10 | 10 | Break | — |
| 15:10–15:40 | 30 | Handoff | Store card and next action |
| 15:40–16:00 | 20 | Close | Rating and MOB recap |

Total: **360 minutes**. Every learner has the 25-minute individual attempt
before group work. After basics, one navigator directs the human driver; the
driver rotates every 5–7 minutes.

## Phase lens

`Plan` and `Design` are in scope. `Build`, `Deploy`, and `Maintain` are
`NOT IN SCOPE — this day produces a read-only evidence card, not an
implementation or release`.

## Literal task cards

### 1. Open and trainer demo — 10:00–10:35

**Task card:** Name one observable result, the human reviewer, the evidence
owner, and the stop rule. Introduce `source`, `claim`, `evidence`, and
`OPEN` only as they are used.

**Example prompt:**

> Read only the scenario README and the headers plus the row for `TX-NS-1004`.
> Explain which file is the ledger, which is the PSP, and which values need a
> human check. Draft a one-row evidence card; do not edit source files or call
> a remote service.

**Output:** Trainer's visible example with paths, row IDs, arithmetic, and an
`OPEN` line for anything not checked.

**Human acceptance:** Facilitator confirms the result is one row, fictional,
local, and reviewable on the learner's own laptop.

### 2. Individual attempt — 10:35–11:00

**Task card:** Create `lab-notes/crew-2/day-1-one-row.md` in a learner copy.
Record transaction ID, ledger reference, PSP reference, gross, expected fee,
actual fee, expected net, actual net, and an initial classification for
`TX-NS-1004`.

**Example prompt:**

> Inspect only the cited `TX-NS-1004` ledger and PSP rows. Draft one local
> evidence card with exact source paths and IDs, integer EUR minor units, the
> 2% round-half-up comparison, and a human decision field. Leave uncertain
> policy as `OPEN`; do not modify CSVs.

**Output:** One independently drafted card, even if incomplete.

**Human acceptance:** Learner can point to both source rows and distinguish an
expected example from a value actually read.

### 3. Review — 11:00–11:20

**Task card:** Pair-read the card aloud. The reviewer checks identifiers,
arithmetic, cutoff context, and whether the card says what was actually read.

**Example prompt:**

> Review this card against the two source rows. List one confirmed fact, one
> calculation you reproduced, and every missing proof as `OPEN`. Do not repair
> the writer's card silently.

**Output:** Short readback with `PASS`, `FAIL`, or `OPEN` per check.

**Human acceptance:** Reviewer records a named role (no invented person) and
one concrete correction or `PASS`.

### 4. Group practice — 11:30–12:00

**Task card:** In groups of 3–4, reconcile the same row and compare cards.
One navigator directs the human driver; rotate driver and navigator every
5–7 minutes. The skeptic may pause the run.

**Example prompt:**

> As navigator, ask the driver to open the ledger row first, then the PSP row.
> Ask the scribe to record source IDs and the skeptic to challenge any value
> without a path. Produce one agreed card without changing the fixtures.

**Output:** One group card plus a note of one disagreement.

**Human acceptance:** Facilitator sees that every number has a source or
calculation and that no one silently overwrote a learner's attempt.

### 5. Check — 13:00–13:15

**Task card:** Submit the group card for a human gate. Check that a fee
mismatch remains a fee mismatch even if net values appear close.

**Example prompt:**

> Act as the reviewer. Reopen the exact CSV rows, recompute expected fee and
> net, and mark each acceptance item `PASS`, `FAIL`, or `OPEN`. Do not approve a
> payout or infer a policy beyond the scenario README.

**Output:** Accepted, revised, or parked card.

**Human acceptance:** Facilitator accepts only source-backed arithmetic and a
clear unresolved decision owner.

### 6. Second practice — 13:15–14:00

**Task card:** Apply the same card format to `TX-NS-1003`, preserving both
duplicate PSP rows and labeling the batch `UNRESOLVED`.

**Example prompt:**

> Read `TX-NS-1003`, `SET-1003-A`, and `SET-1003-B`. Keep both source rows
> visible. Record raw and provisional unique totals, the duplicate rule, and
> the human confirmation needed. Do not delete, count twice, or approve.

**Output:** A second card or a documented `OPEN` if a source check failed.

**Human acceptance:** Reviewer confirms both duplicate IDs remain visible and
the status is `UNRESOLVED`.

### 7. Transfer — 14:10–15:00

**Task card:** Give the card to a fresh reader who did not create it. They
must reproduce one number and identify the next human action in five minutes.

**Example prompt:**

> You are receiving this evidence card cold. Use its paths and source IDs to
> reproduce one calculation, then write the next action, owner role, and
> unresolved question. If a link or command is absent, mark it `OPEN`.

**Output:** Fresh-reader readback attached to the card.

**Human acceptance:** Receiver reproduces the stated check without oral help.

### 8. Handoff and close — 15:10–16:00

**Task card:** Store the two cards, exact checks, reviewer role, next action,
and `OPEN` items. Close with a personal rating and a group MOB recap.

**Example prompt:**

> Draft a concise handoff: made, learned, can do next, source paths, checks
> actually run, reviewer, next owner, and `OPEN` items. Rate yourself
> independent, with help, or needs practice. Add one agreed navigator/driver
> learning; exclude private feedback.

**Output:** `lab-notes/crew-2/day-1-handoff.md` or the team's local equivalent.

**Human acceptance:** Facilitator checks the artifact exists, the receiver can
find the next action, and the closing Kahoot/wordcloud delta is recorded as a
learning signal rather than a learner outcome claim.

## Close script

Repeat the opening Kahoot question and wordcloud. Each learner says one
rating and one source check they can reproduce. The facilitator records
`OPEN — preflight approval and team access` for any future workflow dependency.
