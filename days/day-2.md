# Day 2 — Move one ticket through a feedback loop

Guided participant guide. Continue the fictional payment reconciliation from
[Day 1](day-1.md), using one narrow ticket:
[FIN-003 — quarantine duplicate settlement](../scenarios/payment-reconciliation/tickets/FIN-003.md).
Everything today is a local draft. Do not create or update Jira, GitLab,
Confluence, or any other remote record.

## Outcome and boundary

By 16:00, each participant can carry one functional requirement from analyst
statement through developer proposal and tester checks. The group leaves one
reviewed local packet with source IDs, separate technical additions, and
positive and negative behavior tests.

Today's single concept is a feedback loop: each role makes the next role's work
easier to verify without silently changing behavior. Today's single exercise is
the [guided FIN-003 ticket relay](../scenarios/payment-reconciliation/guided-ticket-exercise.md).
The other payment cases are background only; do not classify all five cases.

Use only the three local CSV files and the FIN-003 template. No credentials,
network calls, production data, deployment, recovery claim, payout approval,
or runtime setup test is in scope. Optional CLAUDE.md or skill drafting starts
only after the visible ticket result exists.

## Phase scope

| Phase | Status and reason |
|---|---|
| Plan | IN SCOPE — state the ticket goal, inputs, and exclusions |
| Design | IN SCOPE — define behavior and separate technical proposals |
| Build | PROPOSAL ONLY — no product source is changed |
| Test | IN SCOPE — write local Given/When/Then behavior checks |
| Deploy | NOT IN SCOPE — this is a fictional local draft |
| Maintain | NOT IN SCOPE — no runtime or production control is exercised |

## Schedule — 10:00–16:00 (360 minutes)

The first 90 minutes are guided. The afternoon continues the same packet
through analyst, developer, and tester passes; these are parts of one exercise.

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:05 | 5 | State goal and inspect worked example |
| 10:05–10:15 | 10 | Trainer demo: requirement → evidence → check |
| 10:15–10:35 | 20 | Guided FIN-003 read |
| 10:35–10:55 | 20 | Group analyst acceptance statement |
| 10:55–11:10 | 15 | Review source IDs and wording |
| 11:10–11:25 | 15 | Individual rewrite and check selection |
| 11:25–11:30 | 5 | Recap packet and next role |
| 11:30–11:45 | 15 | Break |
| 11:45–12:00 | 15 | Analyst pass: facts, scope, acceptance (part 1) |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:20 | 20 | Analyst pass: facts, scope, acceptance (part 2) |
| 13:20–14:00 | 40 | Developer pass: local proposal, technical additions |
| 14:00–14:40 | 40 | Tester pass: positive and negative behavior tests |
| 14:40–14:55 | 15 | Break |
| 14:55–15:40 | 45 | Cross-role review of the same packet |
| 15:40–16:00 | 20 | Handoff, close, and optional context/skill note |

Total: **360 minutes**. Work in groups of three or four people on one screen. Rotate
analyst, developer, tester, reviewer/scribe, driver, and navigator at each pass;
with three people the facilitator/timekeeper also holds review notes. Rotate
driver and navigator every 5–7 minutes. The driver operates the agent; people
make decisions together.

Only the navigator gives the driver the next instruction. Other participants
share observations with the navigator; the driver repeats the instruction
before acting. Anyone can call a pause.

## First 90 minutes

Read the assignment card in the [exercise guide](../scenarios/payment-reconciliation/guided-ticket-exercise.md).
The trainer shows its worked example and demonstrates one source row becoming
an acceptance statement and then a behavior check. This is the only concept
explanation before group work.

In the 10:00–10:05 goal block, ask the Kahoot question “What must remain true
when a payment row is duplicated?” and collect one word-cloud blocker. If those
tools are unavailable, capture the same two answers on the shared board.

The group drafts only the analyst section before 11:30. Check:

1. SET-1003-A and SET-1003-B are both cited and remain visible.
2. The wording preserves UNRESOLVED and does not approve a payout.
3. A tester can derive one passing and one failing behavior.

The facilitator accepts the wording or records an exact open question before
the developer pass. An individual may restate the requirement in their own
words; an answer key is not evidence of a learner run.

## One exercise: FIN-003 ticket relay

Use the assignment card, worked example, literal prompts, and tests in the
[guided ticket exercise](../scenarios/payment-reconciliation/guided-ticket-exercise.md).
Append to one local packet rather than rewriting the ticket at each handoff.

| Pass | Preserve | Add | Human gate |
|---|---|---|---|
| Analyst | User-visible duplicate behavior, source IDs, status | Acceptance wording and open policy questions | Facilitator accepts scope |
| Developer | Every accepted analyst behavior | Small local implementation sketch and technical additions | Analyst confirms behavior is intact |
| Tester | Requirement and source facts | Positive/negative behavior tests and result state | Tester marks PASS, FAIL, or OPEN |

Label field names, grouping keys, storage/API choices, ordering, and logging as
Technical addition — proposal after the functional requirement. A technical
choice cannot change visible rows, status, arithmetic, or human confirmation.
If it would change behavior, park it as a policy question.

The positive test expects both duplicate IDs visible, provisional unique net
24,010, raw net 43,610, and batch status UNRESOLVED. Negative tests fail
silent deletion, hidden rows, double counting, or payout approval. A single
normal settlement can be a boundary check; no other FIN ticket is required.

## Five-minute intervention and parking rule

The facilitator may spend up to five minutes clarifying source, wording, or
role boundaries. If a question needs longer, introduces policy, or expands the
ticket, write it under Open questions / parked and continue. Return to it in
cross-role review. Do not guess, and do not publish private learner feedback.

## Handoff and close

At 15:25, assemble lab-notes/day-2/FIN-003-ticket-packet.md with the
assignment, analyst statement, developer proposal, separate technical
additions, tester checks/results, source IDs, exact commands actually run,
reviewer placeholder, and open questions. Use OPEN for unknown links,
decisions, and unrun checks. The optional context/skill note follows the
visible result and is not required for today's gate.

Close with one sentence each:

- **Made:** what changed in the FIN-003 packet.
- **Learned:** which handoff or source check caught an assumption.
- **Can do:** the next ticket step that can be reproduced independently.

Each person also rates the next step as **independent**, **with help**, or
**needs practice**, and names the evidence for that rating. In the MOB
reflection, revisit the opening blocker and state which role rotation or prompt
change helped. Record only agreed group learning in a local recap; keep personal
feedback private. Carry the reviewed packet into Day 3.

## Source map and facilitator notes

Use [Feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop)
for the concept and [AI in the PR review loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/ai-in-the-pr-review-loop)
for handoff discussion. CLAUDE.md and skills are optional follow-up reading.

Facilitator: houd de groep bij FIN-003; laat analyst, developer en tester
hetzelfde ticket doorgeven; label technische ideeën apart; roteer rollen in
groepen van drie of vier mensen; parkeer langere vragen na vijf minuten; sluit af met
gemaakt, geleerd, kan nu. Do not claim runtime setup or external workflow
testing.
