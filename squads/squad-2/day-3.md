# Squad 2 Day 3 — same-ticket analyst, developer, tester relay

Mode: `COACHED` · Time: `10:00–16:00` · Status: `FUTURE CURRICULUM`

Run all prompts and commands from the repository root.

## Outcome and boundary

Groups pass the same fictional `GL-REVIEW-001` ticket through analyst, developer,
and tester roles. The analyst states visible behavior, the developer adds a
small technical proposal without changing that behavior, and the tester
derives positive and negative checks. The group produces one role-preserving
packet with source IDs and `UNRESOLVED` finding handling.

Read [GL-REVIEW-001](../../scenarios/gitlab-repository-review/tickets/GL-REVIEW-001.md),
the [guided ticket exercise](../../scenarios/gitlab-repository-review/README.md),
the [scenario README](../../scenarios/gitlab-repository-review/README.md), and
[squad 2 Day 2](day-2.md). No code or remote workflow is required.

## Fixed agenda

| Time | Minutes | Block | Artifact |
| --- | ---: | --- | --- |
| 10:00–10:15 | 15 | Open | Kahoot + wordcloud, relay roles, blockers |
| 10:15–10:35 | 20 | Demo | Analyst-to-developer-to-tester pass |
| 10:35–11:00 | 25 | Individual attempt | Personal analyst statement |
| 11:00–11:20 | 20 | Review | Behavior and source readback |
| 11:20–11:35 | 15 | Break | — |
| 11:35–12:00 | 25 | Practice | Analyst pass in groups of 3–4 |
| 12:00–13:00 | 60 | Lunch | — |
| 13:00–13:15 | 15 | Check | Analyst human gate |
| 13:15–14:00 | 45 | Practice | Developer and tester passes |
| 14:00–14:15 | 15 | Break | — |
| 14:15–15:05 | 50 | Transfer | Fresh tester reproduces checks |
| 15:05–15:40 | 35 | Handoff | Role packet and next owner |
| 15:40–16:00 | 20 | Close | Rating and MOB recap |

Total: **360 minutes**. Each learner attempts the analyst task alone for 25
minutes before the coached relay. Groups of 3–4 then use one navigator and
rotate navigator and driver every 5–7 minutes.

## Phase lens

`Plan`, `Design`, `Build` (proposal only), and `Test` are in scope. `Deploy`
and `Maintain` are `NOT IN SCOPE — no implementation, publication, or
production decision is made`.

## Literal task cards

### 1. Open and demo — 10:00–10:35

**Task card:** Demonstrate one ticket crossing three role boundaries. Keep
functional requirements and technical additions in separate sections.

**Example prompt:**

> Read GL-REVIEW-001 and only its cited source rows. As analyst, state the finding
> behavior and evidence. As developer, propose a smallest local change under a
> labelled technical section. As tester, derive one passing and one failing
> check. Do not approve a payout or invent team links.

**Output:** Trainer's three-pass packet with an explicit human gate.

**Human acceptance:** Facilitator shows that the tester received the analyst
behavior unchanged.

### 2. Individual attempt — 10:35–11:00

**Task card:** Draft `lab-notes/squad-2/day-3-analyst.md` alone. State visible
finding behavior, source IDs, date scope, status, and two acceptance examples.

**Example prompt:**

> Act as a GL-REVIEW-001 analyst. Read the ticket, scenario README, and cited repository fixture
> rows. Write functional acceptance wording for both finding rows, the
> provisional unique net, raw net, and `UNRESOLVED` state. Keep unknown policy
> questions `OPEN`; do not propose storage or APIs yet.

**Output:** One personal analyst statement, even if incomplete.

**Human acceptance:** Learner cites `SET-1003-A` and `SET-1003-B` and does not
silently collapse the finding.

### 3. Review — 11:00–11:20

**Task card:** Pair-review the statement for source fidelity and user-visible
behavior. Separate facts, calculations, and policy questions.

**Example prompt:**

> Reopen the cited rows. Mark each statement `PASS`, `FAIL`, or `OPEN`. Flag
> any technical choice that has been presented as a functional requirement.
> Record one correction for the analyst.

**Output:** Readback with a correction log.

**Human acceptance:** Facilitator accepts the wording before the developer
pass starts.

### 4. Analyst group practice — 11:35–12:00

**Task card:** Groups of 3–4 consolidate analyst statements. Navigator directs
the driver; scribe records source IDs; skeptic pauses on unstated policy.

**Example prompt:**

> Consolidate only the accepted analyst behavior for GL-REVIEW-001. Keep both source
> rows, raw 43,610, provisional unique 24,010, bank 24,010, and
> `UNRESOLVED` visible when observed. Park any missing proof as `OPEN`.

**Output:** Accepted analyst section in the shared packet.

**Human acceptance:** Facilitator signs the analyst gate by role and records
any open confirmation question.

### 5. Check — 13:00–13:15

**Task card:** Pass the accepted analyst section to the developer. The human
reviewer confirms no behavior was changed during transfer.

**Example prompt:**

> Compare the packet's analyst section with the accepted gate. List preserved
> behavior, source IDs, and one implementation question. Do not answer the
> question by inventing a policy.

**Output:** Developer-ready packet and `PASS`/`OPEN` gate.

**Human acceptance:** Analyst role confirms the developer received the same
visible behavior.

### 6. Developer and tester practice — 13:15–14:00

**Task card:** Developer adds a smallest local implementation sketch under
`Technical addition — proposal`. Tester writes positive and negative checks.

**Example prompt:**

> Preserve every analyst requirement. Add a local worksheet or function sketch
> only as a proposal. Then write checks for both finding IDs visible,
> provisional unique net 24,010, raw net 43,610, `UNRESOLVED`, and rejection of
> silent deletion, double counting, or payout approval.

**Output:** Developer and tester sections in the same ticket packet.

**Human acceptance:** Analyst confirms no technical proposal changed behavior;
tester labels checks as `PASS`, `FAIL`, or `OPEN` based on actual runs.

### 7. Transfer — 14:15–15:05

**Task card:** Give the packet to a fresh tester. They reproduce one arithmetic
check and one negative behavior check from the packet alone.

**Example prompt:**

> You are the receiving tester. Use only the packet's cited sources and exact
> commands. Reproduce one positive and one negative check. If the command was
> not run, write `OPEN`; do not turn an expected sample into evidence.

**Output:** Fresh-tester readback and discrepancy list.

**Human acceptance:** Receiver can name the next owner and any unresolved
source confirmation without oral coaching.

### 8. Handoff and close — 15:05–16:00

**Task card:** Store the complete relay packet with role boundaries, commands,
reviewer, open questions, and next action. Close with rating and MOB recap.

**Example prompt:**

> Draft the GL-REVIEW-001 handoff: analyst behavior, developer proposals, tester
> checks/results, source IDs, exact commands run, reviewer role, next owner,
> rollback or stop rule, and `OPEN` items. Rate yourself and add one agreed
> relay lesson; exclude private feedback.

**Output:** `lab-notes/squad-2/day-3-GL-REVIEW-001-packet.md`.

**Human acceptance:** Facilitator verifies one ticket stayed intact across all
three passes and the financial case remains `UNRESOLVED` pending human action.

## Close script

Repeat the opening Kahoot and wordcloud. Each learner rates their next role as
independent, with help, or needs practice. Record one group lesson about
preserving behavior across handoffs; leave unrun checks `OPEN`.
