# Learner guide — payment reconciliation track

This is the scenario adaptation for the five-session programme. It is
fictional, local, and read-only. Wave 2 squad 1 uses this guide for its
remaining Days 3–5 after completing Days 1–2; squad 2 has a separate fresh
curriculum in the [squad 2 plan](../../squads/squad-2/README.md). Do not use squad
1 results as squad 2 evidence. Use only the three CSVs in [`data/`](data/)
and the baseline cutoff `2026-09-10 12:00 Europe/Amsterdam`. Day 5 explicitly
uses a working-copy variation with cutoff `2026-09-13`; the baseline validator
does not verify that variation. Amounts are integer
EUR minor units. No coding, credentials, network calls, or remote publication
are required.

## Session guides

The shared six-hour schedule and guided exercises live in:

1. [Day 1 — frame the change](../../days/day-1.md): ledger, PSP settlements,
   bank credits, intent, spec, plan, MOB programming, and the AI-native SDLC.
2. [Day 2 — one ticket through the team](../../days/day-2.md): guided FIN-003
   analyst → developer → tester relay, behavior checks, and individual practice.
   Context and skills are optional after the reviewed result.
3. [Day 3 — guided individual practice, then coached exceptions](../../days/day-3.md):
   a bounded subagent task and controlled rerun, followed by missing and
   duplicate settlement cases with close trainer support.
4. [Day 4 — reliable repetition](../../days/day-4.md): runbook practice and
   peer knowledge handoff with lighter coaching.
5. [Day 5 — independent transfer](../../days/day-5.md): a facilitator-declared
   synthetic working-copy variation; baseline IDs are labelled transfer, not
   unseen.

## First 90-minute guided reset

For a fresh run's first visible result after Day 1, use the [guided ticket
exercise](guided-ticket-exercise.md) with the [Day 2 guide](../../days/day-2.md).
For Wave 2 squad 1, the next visible result is the guided Day 3 opening. Its
bounded-agent starter, two inputs, target artifacts, handout, and checker are
defined in the [ticket-agent pack](../ticket-agent/README.md). Keep the literal
task card visible and let the facilitator intervene after five minutes of
blockage or drift by restating the task, pointing to the source, or stopping at
the gate. Day 1 is future reusable framing curriculum for a fresh run; squad 1
continues from its completed handoff.

Each guide has its own 10:00–16:00 agenda; check the current guide for the
timing. Days 1 and 2 are guided: the trainer explains and demos each exercise
before MOB practice. Day 3 begins with a guided, individual first 90 minutes,
then uses coached MOBs from 11:40 onward. Day 4 is peer-led with clarification
on request, and Day 5 starts with individual work before peer review and the
final MOB reflection. MOBs use 3–4 people on one screen only in their
afternoon blocks, rotate driver/navigator every 5–7 minutes, and end with an
observable check and human gate. The driver operates the agent; humans make
decisions. Use the respectful pause rule.

Day 3 introduces only the bounded subagent described in the pack README.
Skills and hooks are glossary context rather than promised implementation;
hooks or a vector database may be selected later as optional work with a
separate learning goal. Before Day 3, the facilitator must test the same
participant rights, existing skills/context, settings, and output target. If a
participant cannot create or invoke the subagent, record the exact access gap
and use the documented fallback; do not infer access or success.

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

## Day 3 close and covered/next map

At 15:40, use the Day 3 guide's made/learned/can-do close. Record the opening
blocker as `COVERED`, `OPEN`, or `BLOCKED` from the actual evidence. Copy the
[daily recap template](../../templates/daily-recap.md) to a dated file under
`recaps/`, link it from [`recaps/README.md`](../../recaps/README.md), and update
`progress.md` with observed artifacts and access results only. Add a reviewed
knowledge note or record `NONE — no reusable learning yet`.

For Wave 2 squad 1, Day 3 covers bounded-agent inputs and target, one controlled
before/after rerun, second-ticket transfer, missing settlement, duplicate
quarantine, peer evidence, and handoff. Day 4 covers repeatable runbook and
knowledge handoff with lighter coaching. Day 5 covers independent transfer to
the declared synthetic variation. Hooks and vector databases remain optional
later topics; they are not hidden requirements of this track.
