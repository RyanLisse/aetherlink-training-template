# Learner guide — payment reconciliation track

This is the index and scenario adaptation for the five-session programme. It
is fictional, local, and read-only. Use only the three CSVs in [`data/`](data/)
and the baseline cutoff `2026-09-10 12:00 Europe/Amsterdam`. Day 5 explicitly
uses a working-copy variation with cutoff `2026-09-13`; the baseline validator
does not verify that variation. Amounts are integer
EUR minor units. No coding, credentials, network calls, or remote publication
are required.

## Session guides

The shared six-hour schedule and guided exercises live in:

1. [Day 1 — frame the change](../../days/day-1.md): ledger, PSP settlements,
   bank credits, intent, spec, plan, MOB programming, and the AI-native SDLC.
2. [Day 2 — make it repeatable](../../days/day-2.md): `CLAUDE.md`, skills,
   handoffs, independent review, tests versus evaluations, team tools, and
   conceptual release controls.
3. [Day 3 — coached exceptions](../../days/day-3.md): missing and duplicate
   settlement cases with close trainer support.
4. [Day 4 — reliable repetition](../../days/day-4.md): runbook practice and
   peer knowledge handoff with lighter coaching.
5. [Day 5 — independent transfer](../../days/day-5.md): a facilitator-declared
   synthetic working-copy variation; baseline IDs are labelled transfer, not
   unseen.

Every session is 10:00–16:00 and totals 360 minutes. Days 1 and 2 are guided:
the trainer explains and demos each exercise before MOB practice. Day 3 is
coached on request, Day 4 is peer-led with clarification on request, and Day 5
starts with individual work before peer review and the final MOB reflection.
MOBs use 3–5 people on one screen, rotate driver/navigator every 5–7 minutes,
and end with an observable check and human gate. The driver operates the agent;
humans make decisions. Use the respectful pause rule.

## Scenario rules

Compare `data/internal-ledger.csv`, `data/psp-settlements.csv`, and
`data/bank-credits.csv` by their documented identifiers and batch IDs. Apply
`round_half_up(2% × gross_minor)` for expected fee and gross minus fee for
expected net. Keep duplicate PSP rows visible and quarantine the ambiguous
copy; never silently delete or count it twice. A due date equal to the cutoff
is due today, and a later date is a timing item rather than an error.

The five documented fixture cases are `EX-001` overdue missing settlement,
`EX-002` duplicate settlement quarantine, `EX-003` fee mismatch, `EX-004` bank
payout mismatch, and `EX-005` not-yet-due timing item. Learners must record the
source IDs and calculations they actually read; the [trainer answer key](trainer-answer-key.md)
is facilitator reference, not learner evidence.

## Team workflow adaptation

Use the team's existing GitLab, Jira, and Confluence workflow described in
[`workflow.md`](workflow.md). GitLab holds branch/MR evidence, Jira tracks the
fictional `FIN-001` epic and child tasks, and Confluence holds intent, spec,
runbook, recap, knowledge, and handoff. Project keys and URLs are supplied by
the team. Keep each reference `OPEN` until a real link or local evidence
exists. If team systems are unavailable, keep the same artifacts under
`lab-notes/` and record the missing destination.

## Local validation

Commands in the session guides run from the repository root. The fixture
validator is intentionally run from this scenario directory, as stated in the
scenario README:

```sh
cd scenarios/payment-reconciliation
# paste and run the exact Python check from README.md
```

Record the actual output, revision, source IDs, and human decision. A validator
pass checks fixture arithmetic and identifiers; it does not prove a production
control, recovery, deployment, or team-system publication.
