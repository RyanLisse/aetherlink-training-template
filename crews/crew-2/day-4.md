# Crew 2 Day 4 — peer runbook and shared-skill handoff

Mode: `PEER-LED` · Time: `10:00–16:00` · Status: `FUTURE CURRICULUM`

Run all prompts and commands from the repository root.

## Outcome and boundary

Peers turn the reviewed FIN-003 packet into a concise local runbook and a
reusable shared-skill handoff. A fresh reader can find inputs, cutoff, source
IDs, checks, stop rules, and the next owner. GitLab, Jira, and Confluence are
mock workflow destinations only: no real workspace, ticket, page, merge
request, access grant, or approval is claimed.

Read [the team workflow](../../scenarios/payment-reconciliation/workflow.md),
[FIN-003](../../scenarios/payment-reconciliation/tickets/FIN-003.md), the
[scenario README](../../scenarios/payment-reconciliation/README.md), and
[crew 2 Day 3](day-3.md).

## Fixed agenda

| Time | Minutes | Block | Artifact |
| --- | ---: | --- | --- |
| 10:00–10:15 | 15 | Open | Kahoot + wordcloud, peer roles, blockers |
| 10:15–10:35 | 20 | Demo | Runbook-to-handoff path |
| 10:35–11:00 | 25 | Individual attempt | Personal runbook outline |
| 11:00–11:20 | 20 | Review | Peer usability readback |
| 11:20–11:30 | 10 | Break | — |
| 11:30–12:10 | 40 | Practice | Groups of 3–4, one navigator |
| 12:10–12:30 | 20 | Check | Human scope gate |
| 12:30–13:15 | 45 | Lunch | — |
| 13:15–14:00 | 45 | Practice | Shared-skill and mock workflow fields |
| 14:00–14:10 | 10 | Break | — |
| 14:10–15:00 | 50 | Transfer | Fresh reader runs the runbook |
| 15:00–15:10 | 10 | Break | — |
| 15:10–15:40 | 30 | Handoff | Receiver-ready packet |
| 15:40–16:00 | 20 | Close | Rating and MOB recap |

Total: **360 minutes**. The 25-minute personal attempt comes before peer work.
Groups then use one navigator, rotating navigator and driver every 5–7
minutes.

## Phase lens

`Plan`, `Design`, `Test`, and `Maintain` (documentation ownership) are in
scope. `Build` and `Deploy` are `NOT IN SCOPE — mock workflow fields and a
local handoff do not implement or release anything`.

## Literal task cards

### 1. Open and demo — 10:00–10:35

**Task card:** Show how one checked ticket becomes a runbook, then a shared
skill, then a receiver handoff. Introduce “shared skill” as a reusable
procedure with inputs, checks, stop rule, and owner.

**Example prompt:**

> Read the FIN-003 packet and team workflow. Draft a local runbook outline
> with source paths, cutoff, checks, `UNRESOLVED` handling, and a human gate.
> Add mock GitLab, Jira, and Confluence fields marked `OPEN`; do not contact
> any team system.

**Output:** Trainer's receiver journey on one screen.

**Human acceptance:** Facilitator confirms the demo distinguishes local drafts
from published workflow records.

### 2. Individual attempt — 10:35–11:00

**Task card:** Draft `lab-notes/crew-2/day-4-runbook.md` alone. Include inputs,
cutoff, source IDs, sequence, evidence columns, stop rules, and rollback.

**Example prompt:**

> Using FIN-003 and the workflow guide, write a runbook another learner can
> follow offline. Include exact local paths, the duplicate quarantine rule,
> commands actually run or `OPEN`, reviewer role, next owner, and mock team
> links labelled `OPEN`.

**Output:** Personal runbook outline.

**Human acceptance:** Learner can name the first command/source and the point
where a human must stop and decide.

### 3. Review — 11:00–11:20

**Task card:** A peer attempts to navigate the outline for five minutes and
marks missing information. Do not rewrite it for the author.

**Example prompt:**

> Read this runbook as a first-time receiver. Identify the exact next action,
> one missing source or command, the stop rule, and every unavailable team
> link. Mark unavailable evidence `OPEN`.

**Output:** Usability readback.

**Human acceptance:** Peer finds a next action without oral explanation.

### 4. Group practice — 11:30–12:10

**Task card:** Combine the best runbook details in groups of 3–4. Navigator
directs the driver; scribe maintains an evidence table; skeptic tests scope.

**Example prompt:**

> Consolidate a local FIN-003 runbook: load, validate, reconcile, quarantine,
> classify, review, and hand off. Keep source IDs and `UNRESOLVED` visible.
> Add mock GitLab/Jira/Confluence destinations as `OPEN`; do not invent URLs,
> project keys, access, or approvals.

**Output:** Group runbook with a short evidence table.

**Human acceptance:** Facilitator confirms every completed-looking item has an
actual command/output or is marked `OPEN`.

### 5. Check — 12:10–12:30

**Task card:** Human gate the runbook before extracting a reusable skill.
Check source fidelity, stop rules, and the distinction between documentation
and a live release.

**Example prompt:**

> Review this runbook against the scenario and workflow guides. Mark `PASS`,
> `FAIL`, or `OPEN` for sources, arithmetic, duplicate treatment, cutoff,
> reviewer gate, rollback, and external links. Record one required correction.

**Output:** Accepted or parked runbook.

**Human acceptance:** Named facilitator role accepts scope and records the
remaining open workflow dependencies.

### 6. Shared skill and mock workflow — 13:15–14:00

**Task card:** Extract `lab-notes/crew-2/day-4-shared-skill.md` with trigger,
inputs, steps, evidence contract, stop rule, and receiver test. Fill draft
fields for a GitLab MR, Jira task, and Confluence page without publishing.

**Example prompt:**

> Convert the accepted runbook into a reusable shared skill. Include the
> trigger, allowed local reads, exact evidence columns, human gate, rollback,
> and receiver test. Draft mock GitLab/Jira/Confluence fields with every real
> URL, project key, assignee, and approval as `OPEN`.

**Output:** Shared-skill note plus three mock field blocks.

**Human acceptance:** Peer confirms the skill is runnable from the note and
does not imply any remote side effect.

### 7. Transfer — 14:10–15:00

**Task card:** Give the runbook and skill to a fresh reader. They follow the
sequence, reproduce one source check, and report the first missing access.

**Example prompt:**

> Use only this runbook and shared skill. Reproduce one FIN-003 calculation or
> source-row readback, then list the next action and the first unavailable
> GitLab/Jira/Confluence field. Mark it `OPEN`; do not contact a system.

**Output:** Receiver test and discrepancy list.

**Human acceptance:** Receiver can state the next owner role, check, and stop
rule without oral coaching.

### 8. Handoff and close — 15:10–16:00

**Task card:** Store the runbook, shared skill, receiver test, reviewer role,
mock links, next owner, and `OPEN` items. Close with rating and MOB recap.

**Example prompt:**

> Draft a receiver-ready handoff with artifact paths, FIN-003 source IDs,
> checks actually run, `UNRESOLVED` state, rollback, mock workflow fields,
> next owner, and `OPEN` access. Rate yourself independent, with help, or
> needs practice, and add one agreed peer lesson.

**Output:** `lab-notes/crew-2/day-4-handoff.md`.

**Human acceptance:** Facilitator verifies the fresh-reader test happened and
that no draft is described as a live GitLab, Jira, or Confluence record.

## Close script

Repeat the opening Kahoot and wordcloud. Ask which runbook line let the fresh
reader continue and which missing access stayed `OPEN`. Record one agreed MOB
lesson and each learner's rating in the local recap.
