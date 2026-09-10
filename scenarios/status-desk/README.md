# Northstar Demo Support Desk — [TRAINING] fictional scenario

Northstar Demo Support Desk is a public-safe story wrapper for the existing
two-day Python status lab. Northstar is fictional. Every record, request,
ticket, role, count, and outcome in this directory is synthetic training data;
there is no real customer, payment, support queue, Worldline system, or
production monitoring behind it.

## Scenario narrative

The Northstar demo team is preparing a local support desk walkthrough. A
support learner needs to answer a reference-status question from a small local
fixture while keeping an internal note out of the public response. On Day 1,
the team agrees the outcome, writes a small spec and plan, and implements a
single-reference lookup. On Day 2, the team reproduces that evidence, adds a
status filter, records reusable knowledge, performs independent review,
rehearses a local release, and turns a synthetic metric fixture into a new
intent. The story gives those exercises a common vocabulary without changing
the lab API or claiming a working service.

## Roles

| Role | Fictional responsibility in the exercise |
| --- | --- |
| Support learner | Uses the local fixture to answer one request and checks the public field boundary. |
| Product owner | Accepts or revises the intent/spec and decides whether a follow-up is in scope. |
| Implementer | Makes the smallest change in `training-lab/status.py`. |
| Reviewer | Re-runs commands, reads the diff, and records evidence or an open gap. |
| Release manager | Makes the human decision for the local ZIP rehearsal and names rollback. |
| Incident scribe | Records the synthetic metric prompt and the next proposed intent. |

These are exercise roles, not named people or assignments. The tickets contain
no assignees.

## Business scope and boundaries

**In scope:** a local Python 3 standard-library exercise; fixture records with
`reference`, `status`, and `internal_note`; the public output allow-list;
lookup and filtering behavior; review and local release evidence; and a
synthetic error-rate prompt.

**Out of scope:** real customer or payment data, Worldline or other vendor
claims, network calls, credentials, persistence, a deployed service, a real
incident, automated Jira creation, and production monitoring. A sample output
in a ticket is an expected result to check, never evidence that the starter
currently produces it.

## Ticket order and exercise map

Work through the tickets in ID order. The five existing exercises on each day
are named explicitly below; a ticket may cover one connected slice of the
existing workbook. Read the linked ticket for its exact command and acceptance
checklist.

| Order | Ticket | Existing lab exercise |
| ---: | --- | --- |
| 1 | [SCN-001](tickets/SCN-001.md) | Day 1 framing and shared scenario boundary |
| 2 | [SCN-002](tickets/SCN-002.md) | Day 1 Exercise 1 (intent) and Exercise 2 (spec) |
| 3 | [SCN-003](tickets/SCN-003.md) | Day 1 Exercise 3 (plan), Exercise 4 (lookup), and Exercise 5 (handoff) |
| 4 | [SCN-004](tickets/SCN-004.md) | Day 2 Exercise 1 (reproduce and filter) |
| 5 | [SCN-005](tickets/SCN-005.md) | Day 2 Exercise 2 (knowledge) and Exercise 3 (independent review) |
| 6 | [SCN-006](tickets/SCN-006.md) | Day 2 Exercise 4 (conceptual gate and local release rehearsal) |
| 7 | [SCN-007](tickets/SCN-007.md) | Day 2 Exercise 5 (metric prompt, new intent, teach-back) |

Day 1 exercises 1–5 and Day 2 exercises 1–5 remain the source of truth for
the learning flow. This backlog adds narrative and mock inputs only.

## Supplemental fixture layout

- [`data/records.json`](data/records.json) has 12 synthetic rows using the
  same three-field input contract as `training-lab/records.json`.
- [`data/requests.json`](data/requests.json) has five requests, including a
  known lookup, unknown `TX-999`, a valid filter, invalid `cancelled`, and a
  redaction negative control.
- [`data/monitoring.json`](data/monitoring.json) has integer counts for a
  synthetic baseline of 80/2000 (4%) and window of 160/2000 (8%), with a fixed
  5% exercise threshold.

The original `training-lab/records.json` is deliberately unchanged. To use
the larger scenario records with the existing APIs, run this exact command
from the template repository root (the directory containing `training-lab/`):

```sh
python3 scenarios/status-desk/run_requests.py
```

The runner loads the status module with `importlib` and calls the existing
`lookup_status` and `filter_status` functions. It prints `PASS` or `FAIL` for
each request and exits nonzero when the starter is unimplemented or behavior
does not match the request fixture. It performs no writes and no network calls.

For a focused manual check, this is the equivalent root-relative snippet:

```sh
python3 - <<'PY'
import importlib.util
import json
from pathlib import Path

root = Path.cwd()
status_path = root / "training-lab" / "status.py"
records_path = root / "scenarios" / "status-desk" / "data" / "records.json"

spec = importlib.util.spec_from_file_location("training_status", status_path)
status = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(status)
records = json.loads(records_path.read_text(encoding="utf-8"))

print(status.lookup_status("TX-100", records))
print(status.lookup_status("TX-999", records))
print(status.filter_status("settled", records))
try:
    status.filter_status("cancelled", records)
except ValueError as exc:
    print(type(exc).__name__, str(exc))
PY
```

With the starter, `NotImplementedError` is the expected pre-implementation
failure. After a learner implementation, compare observed output with the
request fixture; the JSON and ticket examples remain expected values, not
automated production results.

## Jira mapping

[`jira-mapping.md`](jira-mapping.md) describes a human mapping step. No Jira
project key, issue type ID, user, import CSV, or remote issue is assumed.
Choose those values only after a human identifies the destination project and
reviews the fictional labels.

## Evidence boundary

Acceptance checkboxes in tickets are intentionally unchecked. A participant
or reviewer must run the stated command and record the actual output before
marking one complete. If a command cannot run, record `OPEN` with the exact
failure. Do not convert an expected sample into a claim.
