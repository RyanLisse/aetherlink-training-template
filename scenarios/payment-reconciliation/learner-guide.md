# Learner guide — Northstar daily reconciliation

This is a fictional, local exercise. Use only the three CSVs in `data/` and
the fixed cutoff **2026-09-10 12:00 Europe/Amsterdam**. Amounts are integer EUR
minor units (`100` = EUR 1.00). No coding is required; a spreadsheet, written
worksheet, or optional agent-assisted one-off script is enough.

## Roles and evidence rule

Work in pairs and rotate: operator (reads the files), reviewer (challenges the
classification), scribe (keeps the evidence log), and facilitator (human gate).
Every conclusion must name a source file, row identifier, calculation, and
status (`OPEN` until a person reruns the check). Do not create remote tickets.

The fee policy for this exercise is fixed: expected fee is `round_half_up(2%
× gross_minor)` and expected net is gross less that fee. A duplicate PSP row is
quarantined and remains visible; never silently delete it or count it twice.

## Day 1 — frame the work and build a first reconciliation slice (09:00–16:00)

The programme keeps the existing routines and timeboxes: opening 09:00–09:15;
Exercise 1 09:15–10:15 (60 min); break 10:15–10:25; Exercise 2 10:25–11:25
(60 min); break 11:25–11:35; course map 11:35–12:00; lunch 12:00–13:00;
Exercise 3 13:00–14:10 (70 min); break 14:10–14:20; Exercise 4 14:20–15:20
(60 min); break 15:20–15:30; Exercise 5 15:30–15:50 (20 min); close
15:50–16:00.

Opening: answer the wordcloud prompt **“Which reconciliation step takes most
time each day?”** Keep answers generic; do not mention real customer data.

### Exercise 1 — Plan: capture the intent (60 minutes)

1. State the user problem: a FinOps colleague needs a reproducible comparison
   of ledger, PSP settlement, and bank credit records at a named cutoff.
2. Name the observable outcome: five documented cases are classified with
   evidence and exact arithmetic; the timing item is not labelled an error.
3. Record roles, fixture-only constraints, the cutoff/timezone, and open
   questions in a local note.
4. Ask the facilitator to accept the intent before moving on.

Copyable prompt:

```text
Act as an intent interviewer for a fictional local payment reconciliation exercise. Ask one question at a time until we can state the problem, observable outcome, roles, cutoff/timezone, constraints, and open questions. Use only scenarios/payment-reconciliation/data/*.csv; all amounts are integer EUR minor units. Do not claim this describes Worldline or any real process, and do not write code or create tickets. Draft a concise intent note and leave unresolved policy questions visible.
```

Output: `lab-notes/payment-intent.md` (or the cohort's equivalent) with a
human acceptance decision and one evidence target.

### Exercise 2 — Design: write the reconciliation specification (60 minutes)

1. Define the three file schemas and join keys.
2. Write the fee and net formulas, duplicate rule, cutoff rule, and due-date
   rule in plain language.
3. Define the five case labels `EX-001` through `EX-005`, including what is
   and is not an error.
4. Add acceptance examples for batch totals and require source IDs in every
   finding. Have a human policy reviewer accept the spec.

Copyable prompt:

```text
Read scenarios/payment-reconciliation/README.md and all three CSV headers. Draft a local reconciliation spec: schemas and keys, round-half-up 2% fee rule, gross-fee=net arithmetic, batch comparison, duplicate quarantine without silent deletion, 2026-09-10 12:00 Europe/Amsterdam cutoff, and due-date classification. Enumerate exactly EX-001 through EX-005 using source identifiers. Keep FX, refunds, credentials, network, production claims, and automatic ticket creation out of scope. Do not implement code.
```

Output: a reviewed spec with a clear “expected sample versus observed run”
boundary.

### Exercise 3 — Plan: choose the smallest working slice (70 minutes)

1. Plan a read-only worksheet that first validates identifiers and arithmetic,
   then compares unique PSP rows to the bank by `batch_id`.
2. Name the evidence columns: case ID, source IDs, calculation, owner,
   next action, and reproduction command or sheet reference.
3. Identify the riskiest assumptions (duplicate counting and due-date cutoff)
   and obtain human approval before any agent assistance.

Copyable prompt:

```text
In read-only plan mode, inspect the payment reconciliation README and CSVs. Propose the smallest no-code worksheet or optional one-off Python check that validates identifiers, fee/net arithmetic, duplicate quarantine, due dates, and batch-to-bank totals. Name the files you will read, the exact proof commands, risks, and rollback (discard the local worksheet). Ask the human reviewer to accept the plan before any edits. Do not access a network or create tickets.
```

Output: a plan and a blank evidence log. If using an agent, keep the command
local and show it to the reviewer before running it.

### Exercise 4 — Build/Test: reconcile and record evidence (60 minutes)

1. Load the three CSVs without editing them. Check unique ledger IDs, valid
   references, EUR-only currency, and gross-minus-fee equals net.
2. For each batch, calculate expected ledger net, provisional unique PSP net,
   raw PSP net where a duplicate exists, and bank credit. Keep a duplicate
   batch `UNRESOLVED` until its source is confirmed.
3. Record each of the five cases with its exact evidence IDs and classification.
4. Run the README one-off check (or an equivalent spreadsheet check), paste
   the actual output, and ask a peer to reproduce one batch calculation.

Copyable prompt:

```text
Using only the three local CSVs, produce a reconciliation evidence table. Show each batch's ledger expected net, PSP net with duplicate rows visible, bank credit, and difference. Apply the 2% round-half-up rule, quarantine duplicate PSP rows, and classify exactly EX-001 to EX-005 at the stated cutoff. Include source IDs and calculations. Run the README one-off Python check if available, quote its actual output, and label every unrun check OPEN. Do not modify source CSVs, call services, or publish tickets.
```

Output: an evidence log and five case records. A sample answer is in the
trainer key, but it is not proof of a learner run.

### Exercise 5 — Maintain: hand off the open work (20 minutes)

1. Write a short handoff naming the cutoff, files, completed checks, five
   findings, and the next owner for each action.
2. Ask a fresh colleague to reproduce one normal batch and one exception from
   the source IDs alone.
3. Mark unresolved decisions `OPEN`; do not write that money was recovered
   or that a ticket was created.

Copyable prompt:

```text
Act as a fresh verifier. Read the three CSVs and my reconciliation evidence log. Reproduce one matched batch and one exception from the cited IDs, check the cutoff and fee arithmetic, and return PASS or BLOCKED with the exact missing evidence. Then draft a concise Day 2 handoff and do not edit source data or invent operational outcomes.
```

Output: `lab-notes/payment-handoff-day-1.md`, including a receiver, evidence
paths, open questions, and a next-check command.

## Day 2 — reproduce, review, rehearse, and close the loop (09:00–16:00)

Keep the existing schedule routines: opening 09:00–09:15; Exercise 1
09:15–10:15 (60 min); break 10:15–10:25; Exercise 2 10:25–11:25 (60 min);
break 11:25–11:35; course map 11:35–12:00; lunch 12:00–13:00; Exercise 3
13:00–14:10 (70 min); break 14:10–14:20; Exercise 4 14:20–15:20 (60 min);
break 15:20–15:30; Exercise 5 15:30–15:50 (20 min); close 15:50–16:00.

Opening: repeat the cutoff and ask what evidence is missing from yesterday's
handoff. Keep the five labels stable.

### Exercise 1 — Test: reproduce and challenge the findings (60 minutes)

1. Re-run the Day 1 identifier/arithmetic check and reproduce two cited cases.
2. Challenge whether any duplicate was silently dropped and whether the
   timing item was incorrectly escalated.
3. Correct the evidence log only after a human reviewer agrees, preserving the
   original source references.

Copyable prompt:

```text
Read the Day 1 handoff, the three CSVs, and the trainer rules. Reproduce the recorded totals and all five classifications at 2026-09-10 12:00 Europe/Amsterdam. Look specifically for duplicate rows counted twice, a missing settlement treated as overdue without checking the date, or an expected sample presented as observed evidence. Report exact disagreements before suggesting a correction.
```

### Exercise 2 — Maintain: make the knowledge reusable (60 minutes)

1. Extract a one-page procedure: inputs, cutoff, fee rule, duplicate handling,
   batch arithmetic, exception statuses, and evidence minimum.
2. Have a new joiner use the procedure on one batch without the answer key.
3. Record what the new joiner could reproduce and what remains a policy
   question; mark the note `DRAFT` until reviewed.

Copyable prompt:

```text
Turn the verified fixture procedure into a concise reusable knowledge note for a new FinOps learner. Include the three input files, EUR minor-unit convention, 2% round-half-up fee rule, batch net formula, duplicate quarantine, cutoff/due-date distinction, and required evidence IDs. Separate validated fixture facts from hypotheses and real-world policy questions. Do not imply Worldline endorsement or production readiness.
```

### Exercise 3 — Review: independent evidence and ticket shaping (70 minutes)

1. Assign two human peers or two fresh, independent agent contexts: one
   reviews arithmetic and one reviews scope/safety. Both read only.
2. Each writes separate findings with severity, source IDs, and a reproduction
   path; neither reads the other review before submitting it.
3. A human decision maker compares both reviews, then converts accepted
   follow-up needs into the six local FIN ticket templates; leave every
   acceptance checkbox unchecked.

Copyable prompt:

```text
Use two independent read-only contexts or human peers. Review A checks identifiers, fee/net arithmetic, duplicate quarantine, and batch totals. Review B checks cutoff semantics, exactly five exception cases, fixture-only scope, and whether claims have reproducible evidence. Neither reviewer may read the other's draft before submitting. Return separate findings with file/row IDs and PASS or BLOCKED; a human compares them. Suggest which local FIN-002 to FIN-006 template each follow-up belongs to. Keep templates local and unpublished during this exercise.
```

### Exercise 4 — Deploy conceptually: gate and local handoff rehearsal (60 minutes)

1. Design a conceptual gate: source files unchanged, identifier/arithmetic
   check passes, five cases present, and human reviewer signs the handoff.
2. Rehearse a local-only handoff package containing the evidence log, review,
   and knowledge note. There is no deployment or remote issue creation.
3. Write the rollback as “discard the local package and restore the prior
   worksheet”; record any failed check as an incident with exact output.

Copyable prompt:

```text
Design a conceptual approval gate for this local exercise: all three CSVs are unchanged, integer EUR arithmetic passes, duplicate rows remain quarantined, exactly five documented cases are present, and a named human reviewer accepts the evidence. Rehearse a local handoff package only. State clearly which checks ran, which are conceptual, and the rollback. Do not deploy, publish, or claim enforcement.
```

### Exercise 5 — Maintain: recap, metric prompt, and teach-back (20 minutes)

1. Choose a synthetic leading metric such as “cases with source IDs” and
   record its observed count from the evidence log; do not invent production
   thresholds.
2. Draft a next intent for improving reproducibility, then teach back the
   chain: intent → spec → plan → evidence → review → handoff.
3. Complete the daily recap and knowledge output using the repository
   templates, linking only actual local evidence and leaving open actions.

Copyable prompt:

```text
Using only the observed local evidence log, draft a Day 2 recap and a follow-up intent for reproducible payment reconciliation. Include the metric definition and observed count if available, the five case IDs, reviewer decision, open actions, and next human gate. Distinguish fixture evidence from hypotheses; do not claim production monitoring, recovery, or a Worldline process. Prepare a two-minute teach-back.
```

Final check-in: **“Which finding can your colleague reproduce, and what
remains uncertain?”**

## Required closing outputs

Create a dated recap from `templates/daily-recap.md`, a knowledge note from
`templates/knowledge-note.md` (or record `NONE — no reusable learning yet`),
and a handoff from `templates/handoff.md` when ownership changes. Link them in
the relevant indexes only after the human reviewer checks the paths. The
local ticket templates are planning artifacts; leave checkboxes unchecked.
