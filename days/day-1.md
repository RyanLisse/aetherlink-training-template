# Day 1 — Frame a payment reconciliation change

Guided participant guide. The scenario is fictional and local. Use the three
CSV files in [`../scenarios/payment-reconciliation/data/`](../scenarios/payment-reconciliation/data/)
and the fixed cutoff `2026-09-10 12:00 Europe/Amsterdam`. No credentials,
network calls, production data, or remote publication are used.

## Outcome and setup

By 16:00, the mob has a reviewed intent, specification, and plan for one
small reconciliation slice, plus a source backed evidence log and handoff.
The agent drafts and checks; a human accepts scope and evidence. Work from the
repository root. The team workflow remains GitLab, Jira, and Confluence; use
`OPEN` placeholders for unavailable team links.

Before starting:

```sh
python3 --version
mkdir -p lab-notes
```

### Concepts introduced today

The facilitator explains the AI native SDLC as a loop: Plan → Design → Build →
Test → Deploy → Maintain, returning to an earlier phase when evidence changes
the intent or plan. An agent is a bounded collaborator with repository context,
instructions, and a requested output; the human remains accountable for
decisions. `intent.md` states why and what success means, a spec states the
contract, and a plan states the smallest ordered change and its proof.

MOB programming means one shared task, one screen, and a small group of three
to four. Keep the literal task card visible. The facilitator is timekeeper and
pause point; if the group is blocked or drifting for five minutes, intervene by
restating the task, pointing to the source, or stopping at the gate. Rotate
driver and navigator every 5–7 minutes, with a reviewer/scribe as needed. The
agent is never the human driver: one participant operates the agent, while the
group thinks aloud. Anyone may say “pause” to restate the question, source, or
gate.

Plain-language glossary: the ledger is the merchant's expected transaction
record; a PSP settlement is the payment-provider payout row; a bank credit is
the bank's received amount. Gross is before the fee, net is after it, and the
cutoff is the time at which the comparison is made. A prompt is an instruction
to an agent; context is the files and rules supplied with it. An intent states
the outcome and boundaries, while a task is one bounded piece of work.

## Schedule — 10:00–16:00 (360 minutes)

| Time | Minutes | Activity |
|---|---:|---|
| 10:00–10:15 | 15 | Opening, working agreement, fixture boundary |
| 10:15–10:40 | 25 | Concept recap and trainer demo: agent context, intent, SDLC, MOB |
| 10:40–11:15 | 35 | Exercise 1: interview and draft intent |
| 11:15–11:25 | 10 | Break |
| 11:25–12:00 | 35 | Exercise 2: shape the reconciliation specification |
| 12:00–13:00 | 60 | Lunch |
| 13:00–13:20 | 20 | Trainer demo and coaching: source IDs and evidence |
| 13:20–14:05 | 45 | Exercise 3: plan the smallest slice |
| 14:05–14:15 | 10 | Break |
| 14:15–15:05 | 50 | Exercise 4: read-only reconciliation and evidence |
| 15:05–15:15 | 10 | Break |
| 15:15–15:45 | 30 | Exercise 5: handoff and feedback loop |
| 15:45–16:00 | 15 | Individual check-in and MOB reflection |

Total: **360 minutes**.

Opening Kahoot/wordcloud prompt: “Which reconciliation step takes most time?”
Keep answers generic and fictional. Ask: “What evidence would make this a
safe first slice?” Record blockers as questions, not solutions.

## Exercise 1 — Interview the intent (35 minutes)

Trainer explains the difference between a problem, outcome, constraint, and
open question, then demos an agent receiving only the repository root and
scenario README. MOB: one shared draft; rotate driver/navigator twice, with a
scribe recording unanswered questions. Agent operator types the prompt; humans
challenge every assumption. Observable check: the group can point to one
measurable success sentence and one named human gate.

```text
Act as an intent interviewer for a fictional local payment reconciliation exercise.
Ask one question at a time until we can state the problem, observable outcome,
roles, fixed cutoff/timezone, fixture-only constraints, and open questions.
Use only scenarios/payment-reconciliation/data/*.csv and its README. Do not write
code, call services, create tickets, or claim this describes Worldline. Draft
lab-notes/payment-intent.md, leaving unresolved policy questions visible.
```

Output: `lab-notes/payment-intent.md`, naming comparison of ledger, PSP, and
bank records and five documented case targets. Human gate: facilitator accepts
the boundary or marks it `needs revision`; no spec work before that decision.

## Exercise 2 — Specify the contract (35 minutes)

Trainer explains schemas, join keys, and why a duplicate stays visible, then
demos turning one intent sentence into an acceptance example. MOB: rotate
driver/navigator every 5–7 minutes while the group writes one shared spec.
Pause when the agent infers an unstated fee or due-date policy. Observable
check: a peer can find the fee formula, duplicate rule, and cutoff in the file.

```text
Read lab-notes/payment-intent.md, scenarios/payment-reconciliation/README.md,
and all three CSV headers. Draft lab-notes/payment-spec.md with schemas, keys,
round-half-up 2% fee/net arithmetic, batch comparison, duplicate quarantine,
cutoff and due-date rules, and exactly EX-001 through EX-005. Cite source IDs.
Keep FX, refunds, credentials, network, production claims, and ticket creation
out of scope. Do not implement code.
```

Output: `lab-notes/payment-spec.md` with expected-versus-observed evidence
boundaries. Human gate: a policy owner accepts the rules and labels any open
decision `OPEN`.

## Exercise 3 — Plan before acting (45 minutes)

Trainer explains context selection and plan mode, then demos a read-only plan
that names files, risks, and proof commands. MOB: rotate driver/navigator twice;
the group rejects scope expansion and asks “what could break?” Observable
check: a stranger can follow the ordered plan and knows what proves completion.

```text
In read-only plan mode, inspect scenarios/payment-reconciliation/README.md and
the three CSVs. Draft lab-notes/payment-plan.md for the smallest local worksheet
or one-off check: validate identifiers and arithmetic, quarantine duplicates,
apply due-date semantics, compare batches, and record evidence. Name exact
root-relative paths, proof commands, risks, rollback, and the human gate. Do not
edit source CSVs, access a network, or create tickets.
```

Output: `lab-notes/payment-plan.md` and a blank evidence-log outline. Human
gate: facilitator accepts the plan before any agent-assisted check runs.

## Exercise 4 — Reconcile a first slice (50 minutes)

Trainer explains source-row evidence and demos one batch calculation without
revealing the five classifications. MOB: rotate driver/navigator every 5–7
minutes; the group reads rows aloud and the reviewer asks for a calculation.
Observable check: one matched batch and one exception can be reproduced from
the cited IDs alone.

```text
Using only the three local CSVs and the accepted payment spec, produce a
read-only evidence table. Show ledger expected net, PSP net with duplicates
visible, bank credit, difference, source IDs, calculation, and status. Apply
the fixed cutoff and round-half-up 2% rule. Do not silently delete or count a
duplicate twice. Run the facilitator check only from the scenario directory:
cd scenarios/payment-reconciliation && <paste the exact README command>.
Quote actual output and mark unrun checks OPEN. Do not publish or modify data.
```

Output: `lab-notes/payment-evidence-day-1.md`. Human gate: reviewer reproduces
one normal and one exceptional row calculation; unresolved duplicate work stays
`UNRESOLVED`.

## Exercise 5 — Close the loop with a handoff (30 minutes)

Trainer explains claim/source/reproduction/hypothesis and demos a short
handoff. MOB: rotate driver/navigator once; the group uses the pause rule when
an outcome is asserted without evidence. Observable check: a fresh receiver
can identify the next check, owner, and exact source paths.

```text
Act as a fresh verifier. Read lab-notes/payment-intent.md,
lab-notes/payment-spec.md, lab-notes/payment-plan.md, and the evidence log.
Reproduce one matched batch and one exception from cited IDs. Return PASS or
BLOCKED with exact missing proof, then draft lab-notes/payment-handoff-day-1.md.
Keep GitLab, Jira, and Confluence references OPEN unless a real team link exists.
Do not invent recovery, approval, or production outcomes.
```

Output: handoff with cutoff, revision, checks run, open questions, receiver,
and intended GitLab MR/Jira/Confluence references. Human gate: receiver signs
`PASS` or `BLOCKED` from the evidence.

## Check-in and reflection

Individually answer: “What did the agent need as context, and what did a human
gate decide?” In the MOB reflection, name the rotated roles, one changed
assumption, and the evidence another person can reproduce. Record open work in
the daily recap; do not claim a live system result. Closing check-in prompt:
“What will you transfer to your next work item, and what evidence will prove it?”

## Day 1 source map

These are canonical course pages mapped from the existing repository source
notes. Text was checked; no video or audio is claimed as watched.

| Lesson | Use |
|---|---|
| [Introduction](https://academy.claude.com/courses/ai-native-sdlc-playbook/introduction) | AI-native SDLC loop and bottleneck |
| [Capture as intent.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/capture-intent) | Exercise 1 |
| [Requirements and design](https://academy.claude.com/courses/ai-native-sdlc-playbook/requirements-and-design) | Exercise 2 |
| [Plan mode](https://academy.claude.com/courses/ai-native-sdlc-playbook/plan-mode) | Exercise 3 |
| [Feedback loop](https://academy.claude.com/courses/ai-native-sdlc-playbook/give-claude-a-feedback-loop) | Exercise 5 |
| [CLAUDE.md](https://academy.claude.com/courses/ai-native-sdlc-playbook/claude-md) | Optional preview |
| [Skills as institutional knowledge](https://academy.claude.com/courses/ai-native-sdlc-playbook/skills-as-institutional-knowledge) | Optional preview |
| [Parallel sessions and subagents](https://academy.claude.com/courses/ai-native-sdlc-playbook/parallel-sessions-and-subagents) | Optional overview |

Further reading remains the [course overview](https://academy.claude.com/courses/ai-native-sdlc-playbook).

## Facilitator notes (Nederlands)

Houd de scope fictief en lokaal. Laat de trainer eerst voordoen en daarna de
groep hardop redeneren. De agent schrijft of controleert; een mens beslist bij
iedere gate. Laat de MOB-rollen elke 5–7 minuten wisselen en accepteer “pauze”
als signaal om bron, aanname of bewijs opnieuw te benoemen. Geef de vijf
classificaties niet vooraf weg; stuur op bron-ID's en exacte berekeningen.
