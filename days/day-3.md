# Day 3 — Bounded agent practice, then coached exceptions

This is the next session for **Wave 2 crew 1**, continuing from its completed
Days 1–2. Crew 2 has a separate fresh five-session curriculum; do not use crew
1's prior results as evidence for it. The first 90 minutes are guided and
individual. From 11:40 onward, the group is coached through the fictional
payment exceptions in MOBs of three to four.

## Session outcome and boundary

By the close, each participant has attempted the same bounded subagent task on
their own laptop, using the starter and two-input template in the [ticket-agent
pack](../scenarios/ticket-agent/README.md). They record the target output, one
before/after rerun where exactly one instruction changed, and a transfer run on
the second agreed ticket. The afternoon MOB then reproduces the missing and
duplicate settlement checks and prepares a receiver-ready handoff.

The only new concept in this session is a **bounded subagent**: a small,
explicitly scoped helper with named inputs, a target output, and a human check.
The pack README is the source of truth for its starter, input names, target
artifacts, handout, and checker. Skills and hooks may be mentioned in the
glossary as context; implementing them is not a session requirement. A hook or
vector-database exercise is optional later in Day 4 or Day 5 only when a
facilitator selects it with a separate learning goal. Do not add a mandatory
concept to this agenda.

## Facilitator preflight — complete before participants arrive

1. Run the exact ticket-agent pack preflight and checker instructions from its
   [README](../scenarios/ticket-agent/README.md) in the same environment,
   model/mode, and account rights participants will use. Record the result;
   do not describe access as available until it has been checked.
2. Inventory the skills, examples, and other context visible to participants.
   Decide which existing context is allowed for this exercise and state that
   boundary before the demo. If an old skill appears, do not silently reuse it.
3. Confirm the exact pack files: the starter
   `.claude/agents/ticket-coach.md`, inputs `ticket-inputs.md`, output
   contract/handout `ticket-template.md`, target shapes `target-examples.md`,
   and checker `check_ticket.py`. The two pairs are `TICKET-OPS-101` →
   `Worked target A` and `TICKET-OPS-102` → `Worked target B`. Prepare a local
   fallback with the same inputs and output target if a participant lacks the
   right to create or invoke a subagent; label that attempt as a fallback and
   record the access gap.
4. Ask the team representative to sign off on those two input/target pairs
   before the session. Until that sign-off exists, keep the pair names and
   decision `OPEN`; the afternoon FIN-002 and FIN-003 fixture tasks are
   separate coached exercises.
5. Prepare the end example from the pack and the two Kahoot/wordcloud prompts.
   Keep the task card, the target output, and the acceptance checklist visible.

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:10 | 10 | Guided recap, end example, Kahoot, and wordcloud |
| 10:10–10:20 | 10 | Facilitator demo: create and invoke one bounded subagent |
| 10:20–10:45 | 25 | Individual practice: create and invoke on each laptop |
| 10:45–10:55 | 10 | Individual review against the pack checklist |
| 10:55–11:10 | 15 | Change one instruction; rerun the same input and settings |
| 11:10–11:25 | 15 | Transfer the unchanged method to the second ticket |
| 11:25–11:30 | 5 | Individual progress record and access note |
| 11:30–11:40 | 10 | Break |
| 11:40–12:20 | 40 | Coached MOB: reproduce the missing settlement |
| 12:20–12:30 | 10 | Check and human gate |
| 12:30–13:15 | 45 | Lunch |
| 13:15–14:00 | 45 | Coached MOB: reproduce the duplicate settlement |
| 14:00–14:10 | 10 | Break |
| 14:10–15:00 | 50 | MOB peer review and evidence readback |
| 15:00–15:10 | 10 | Break |
| 15:10–15:40 | 30 | MOB handoff and receiver check |
| 15:40–16:00 | 20 | Close: made, learned, can do, and next session |

Total: **360 minutes**. The first 90 minutes are individual work; do not
turn them into a driver rotation. In the afternoon, use MOBs of three to four
with one screen, a named facilitator/timekeeper, reviewer, and evidence owner.
Rotate driver and navigator every 5–7 minutes only during the MOB blocks. The
driver operates the agent; humans decide scope, interpretation, and gates.

## First 90 minutes — literal instructions

### 10:00–10:10 — recap, end example, Kahoot, wordcloud

Read the Day 2 handoff and ask each participant to state the prior result in
one sentence. Show the pack's completed end example and point to its input,
target output, and checker. Ask in Kahoot: **“What makes a subagent safe to
test in this exercise?”** Expected explanation: its inputs, allowed boundary,
target output, and human gate are explicit. Use the wordcloud prompt:
**“Which step might block you today?”** Cluster the answers and record one
blocker to revisit at the close. If either tool is unavailable, collect the
same answers on the shared board. Do not record a participant as successful
because they answered the question.

### 10:10–10:20 — one bounded demo

Open the [ticket-agent pack README](../scenarios/ticket-agent/README.md) and
name the exact starter, `ticket-inputs.md`, `ticket-template.md`,
`target-examples.md`, and `check_ticket.py`. Demonstrate one invocation with
`TICKET-OPS-101` and the agreed settings. Say aloud
what is in scope and what is excluded. Show how the result is checked and how
an unknown is marked `OPEN`. Do not add a hook, vector database, extra skill,
or hidden context to the demo. Record the actual command or UI action and
result if they exist; use `OPEN` for anything not run.

Use this copy-ready invocation prompt for the demo and the first learner run:

```text
Use the ticket-coach subagent. Read scenarios/ticket-agent/ticket-inputs.md and use the TICKET-OPS-101 input. Return a draft that follows scenarios/ticket-agent/ticket-template.md. Preview the complete draft in chat; do not write files or use remote tools.
```

### 10:20–10:45 — every participant creates and invokes

Each participant works on their own laptop and follows the pack starter:

1. Read the pack README and identify `TICKET-OPS-101`,
   `ticket-template.md`, the four required headings, and `check_ticket.py`
   before invoking anything.
2. Create the bounded subagent with only the allowed starter instructions.
   Keep the selected input unchanged and do not import an old skill unless
   the facilitator explicitly allowed it during preflight.
3. Invoke it once with the agreed settings using the copy-ready prompt above.
   Save the actual output and note the command, model/mode if visible, revision
   or timestamp, and any access error. Mark an unrun check `OPEN`.
4. Compare the output with the pack's target and handout fields. Ask the
   facilitator about scope or evidence; do not fill missing facts from memory.

If the environment does not permit creation or invocation, use the prepared
fallback with the same inputs and target, record `BLOCKED — access` and the
exact observed limitation, and continue to the review. This is a truthful
partial run, not evidence that the subagent was created.

### 10:45–10:55 — review the first result

Use `check_ticket.py` from the pack. Verify that `TICKET-OPS-101` is identified,
both protected sections are present, the four required headings are present,
assumptions and missing data are separated, and no unsupported
ticket fact was invented. Each participant writes one finding and one `OPEN`
question. The reviewer checks the artifact itself, not the participant's
description.

### 10:55–11:10 — one controlled change

Change **exactly one instruction** in the bounded subagent. Keep the input,
settings, and checker unchanged. Record the original instruction, the changed
instruction, and both outputs. Rerun the same input and settings, then state
one observed difference and one thing that stayed the same. Do not change the
model, mode, input, tool access, or ticket at the same time. If the first run
was blocked, record the blocked comparison and do not claim a before/after
result.

### 11:10–11:25 — second-ticket transfer

Reuse the same bounded subagent and the same single changed instruction. Use
`TICKET-OPS-102` from `ticket-inputs.md` as the only input change. Produce the
same target output and run the same `check_ticket.py` checker. Record whether the method
transferred, what required human judgment, and any `OPEN` question. Do not
silently substitute a third ticket.

Use this copy-ready transfer prompt:

```text
Use the ticket-coach subagent. Read scenarios/ticket-agent/ticket-inputs.md and use the TICKET-OPS-102 input. Return a draft that follows scenarios/ticket-agent/ticket-template.md. Preview the complete draft in chat; do not write files or use remote tools.
```

### 11:25–11:30 — progress record

Each participant records one status: `independent`, `with help`, or
`BLOCKED — access`/`needs practice`; the exact artifact path; the before/after
comparison status; and the next action. The facilitator reports only observed
artifacts and access results. No participant success, tool access, or learning
outcome is inferred from attendance or discussion.

## Afternoon coached practice

### 11:40–12:20 — missing settlement (`FIN-002`, `EX-001`)

In a MOB of three to four, read `TX-NS-1007`, its due date, and the absence of
the PSP row from the three CSVs. Use this literal prompt:

> From the three fictional CSVs, reproduce `EX-001` at the fixed cutoff
> `2026-09-10 12:00 Europe/Amsterdam`. Cite every source ID, compare the due
> date with the cutoff, and classify the result. Do not call it recovered and
> do not invent an owner or missing PSP fact.

Output one evidence row with source IDs, cutoff, calculation or comparison,
status, next evidence request, and `OPEN` owner. Check: a fresh MOB member can
reproduce the row from the cited files. Gate: the facilitator accepts the
overdue classification or records the exact unresolved question.

### 12:20–12:30 — check

The reviewer reads the evidence row without the operator's explanation. Check
the due-date rule, source IDs, and absence claim. Record PASS or BLOCKED and the
missing proof. Keep the ticket fictional and do not claim payment recovery.

### 13:15–14:00 — duplicate settlement (`FIN-003`, `EX-002`)

Read `SET-1003-A` and `SET-1003-B` beside the ledger and bank rows. Use this
literal prompt:

> Show both duplicate PSP rows, the raw and provisional unique totals, and the
> batch status. Quarantine the ambiguous copy, do not silently delete or count
> it twice, and keep the case `UNRESOLVED` pending source confirmation. Cite
> the rows and show the arithmetic.

Output a case note with both source IDs, raw net `43,610`, provisional unique
net `24,010`, batch, status, decision owner, and `OPEN` confirmation request.
Check: a fresh MOB member reproduces the totals and sees both rows. Gate: the
facilitator accepts the quarantine wording; no payout approval is recorded.

## Peer review, evidence, and handoff

From 14:10, each MOB exchanges its two afternoon artifacts with another MOB.
The reviewer checks source IDs, due-date treatment, duplicate visibility,
arithmetic, `OPEN` questions, and whether the ticket signoff is still pending.
Return `PASS` or `BLOCKED` with the exact missing proof. The evidence owner
records actual commands, source paths, revision or timestamp, and reviewer
readback in `lab-notes/day-3-evidence.md`. Do not use the answer key as learner
evidence.

At 15:10, prepare `lab-notes/handoff-day-3.md` with the fixed cutoff, checked
cases, source IDs, actual commands, pack run status, before/after result,
unresolved decisions, access gaps, next owner, and next gate. Keep GitLab,
Jira, and Confluence references `OPEN` until the team supplies real links.
The receiver must find the next action and reproduce one missing or duplicate
check in two minutes. The handoff is a training artifact, not a production
control or a claim that a financial issue was resolved.

## Close and covered/next map — 15:40–16:00

Each person answers: **Made:** what artifact or comparison exists? **Learned:**
which single instruction or source check changed the result? **Can do:** which
step can be repeated and with what support? Revisit the opening wordcloud
blocker and record whether it is `COVERED`, `OPEN`, or `BLOCKED` based on
evidence. Copy [the daily recap template](../templates/daily-recap.md) to a
dated file under `recaps/`, link it from `recaps/README.md`, and update
`progress.md` with observed results only. Add a reviewed knowledge note or
record `NONE — no reusable learning yet`.

The map for this continuation is explicit:

- **Covered today:** bounded subagent inputs and target, one controlled
  before/after rerun, second-ticket transfer, missing settlement, duplicate
  quarantine, peer evidence, and handoff.
- **Next — Day 4:** repeat the evidence method with lighter coaching, write and
  peer-reproduce a runbook, and hand over reviewed knowledge. Hooks or a vector
  database remain optional and require a separate selected learning goal.
- **Next — Day 5:** independently transfer the reviewed method to the declared
  synthetic variation and record what still needs practice.

Do not record fictional financial recovery, participant success that was not
observed, or tool access that was not tested.
