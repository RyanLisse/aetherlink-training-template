# Northstar daily payment reconciliation — [TRAINING] fictional scenario

Northstar is a fictional merchant used for a practical FinOps reconciliation
exercise. Every transaction, settlement, bank credit, ticket, amount, and
decision here is synthetic training data. This material does not describe
Worldline systems, contracts, SLAs, controls, or operating procedures.

## Outcome and boundary

By the end of Day 2, a learner can compare the internal transaction ledger,
the PSP settlement file, and the bank credit file; classify five deliberately
documented cases; calculate the expected batch net; and hand over an evidence-
backed action list. The work is a local, read-only exercise. Learners may use
an agent to draft a worksheet or a one-off script, but no coding is required.

In scope: the three CSV fixtures in [`data/`](data/), the reconciliation rules,
the learner guide, the answer key, and local ticket templates. Out of scope:
real payment or customer data, production access, credentials, network calls,
FX, refunds, chargebacks, tax, scheme rules, automatic ticket creation, and
any claim about a real merchant or PSP process.

The fixed reconciliation cutoff is **2026-09-10 12:00 Europe/Amsterdam**.
Settlement due dates are local calendar dates. A ledger row is overdue when it
has no valid PSP settlement and its due date is before the cutoff date. A row
whose due date equals the cutoff date is due today (review it, but do not call
it overdue); a row whose due date is after the cutoff date is a timing item and
is not an error.

## Files and identifiers

| File | Source role | Stable keys |
| --- | --- | --- |
| [`data/internal-ledger.csv`](data/internal-ledger.csv) | Northstar's expected transaction and fee record | `transaction_id`, `ledger_reference` |
| [`data/psp-settlements.csv`](data/psp-settlements.csv) | Fictional PSP settlement rows | `settlement_id`, `transaction_id`, `psp_reference` |
| [`data/bank-credits.csv`](data/bank-credits.csv) | Fictional bank credits by settlement batch | `bank_credit_id`, `batch_id`, `bank_reference` |
| [`trainer-answer-key.md`](trainer-answer-key.md) | Facilitator-only worked arithmetic and case classifications | `EX-001`–`EX-005` |
| [`learner-guide.md`](learner-guide.md) | Literal Day 1/Day 2 exercises and copyable prompts | `FIN-001`–`FIN-006` |
| [`tickets/`](tickets/) | Six local Markdown ticket templates | unchecked acceptance |

All amounts are integer EUR minor units. For example, `12500` means EUR
125.00. Do not introduce decimal amounts or an FX conversion.

## Rules for this fixture

The only fee rule is: `expected_fee_minor = round_half_up(gross_minor × 2%)`.
`expected_net_minor = gross_minor − expected_fee_minor`. The provided ledger
values are the expected values to check, not an invitation to infer another
policy.

For each batch, sum valid, unique PSP settlement rows and compare that sum
with the bank credit. A duplicate settlement row is quarantined as ambiguous:
keep both source rows visible, flag the duplicate, and do not silently delete
or count the ambiguous copy as a second payout. The unique total is provisional
until the duplicate is confirmed, so that batch remains `UNRESOLVED` and is not
approved as reconciled. A fee mismatch remains a fee mismatch even if the PSP
net happens to reach the bank. A bank payout mismatch is a batch-level
difference after the source rows have been checked.

The five and only five documented cases are:

| Case | Classification | Evidence anchors |
| --- | --- | --- |
| `EX-001` | overdue missing settlement | `TX-NS-1007`, due `2026-09-08`; no `SET-1007` |
| `EX-002` | duplicate settlement row, quarantine ambiguity | `SET-1003-A` and `SET-1003-B`, same transaction/reference |
| `EX-003` | fee mismatch | `TX-NS-1004`, `SET-1004-A` |
| `EX-004` | bank payout mismatch | batch `B-20260910-02`, `BANK-0910-02` |
| `EX-005` | not-yet-due timing item, not an error | `TX-NS-1008`, due `2026-09-12`; no settlement at cutoff |

No other row is intended to be exceptional. The answer key is the facilitator
reference; participants must still record the evidence they actually read.

## Running the local check

From this scenario directory, a facilitator can run a one-off Python check
without installing anything:

```sh
python3 - <<'PY'
import csv
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

root = Path('.') / 'data'
read = lambda name: list(csv.DictReader((root / name).open(newline='', encoding='utf-8')))
ledger, psp, bank = read('internal-ledger.csv'), read('psp-settlements.csv'), read('bank-credits.csv')
assert {r['transaction_id'] for r in ledger} >= {r['transaction_id'] for r in psp}
assert len({r['transaction_id'] for r in ledger}) == len(ledger)
from datetime import date
cutoff = date.fromisoformat('2026-09-10')
assert all(r['currency'] == 'EUR' for rows in (ledger, psp, bank) for r in rows)
assert len({r['ledger_reference'] for r in ledger}) == len(ledger)
assert len({r['settlement_id'] for r in psp}) == len(psp)
assert len({r['bank_credit_id'] for r in bank}) == len(bank)
assert len({r['bank_reference'] for r in bank}) == len(bank)
assert len({r['transaction_id'] for r in ledger}) == len(ledger)
assert all(r['transaction_id'] in {l['transaction_id'] for l in ledger} for r in psp)
assert all(r['batch_id'] in {l['batch_id'] for l in ledger} for r in bank)
fee_ok = lambda gross, fee: (Decimal(gross) * Decimal('0.02')).quantize(Decimal('1'), rounding=ROUND_HALF_UP) == Decimal(fee)
assert all(fee_ok(r['gross_minor'], r['expected_fee_minor']) for r in ledger)
assert all(int(r['gross_minor']) - int(r['expected_fee_minor']) == int(r['expected_net_minor']) for r in ledger)
assert all(int(r['gross_minor']) - int(r['fee_minor']) == int(r['net_minor']) for r in psp)
ledger_by_tx = {r['transaction_id']: r for r in ledger}
dupe_keys = [k for k, n in Counter((r['transaction_id'], r['psp_reference']) for r in psp).items() if n > 1]
fee_ids = sorted({r['transaction_id'] for r in psp if not fee_ok(r['gross_minor'], r['fee_minor'])})
psp_by_tx = defaultdict(list)
for r in psp: psp_by_tx[r['transaction_id']].append(r)
overdue_ids = sorted(tx for tx, l in ledger_by_tx.items() if not psp_by_tx.get(tx) and date.fromisoformat(l['settlement_due_date']) < cutoff)
timing_ids = sorted(tx for tx, l in ledger_by_tx.items() if not psp_by_tx.get(tx) and date.fromisoformat(l['settlement_due_date']) > cutoff)
bank_by_batch = defaultdict(int)
for r in bank: bank_by_batch[r['batch_id']] += int(r['amount_minor'])
unique_psp_by_batch = defaultdict(int)
for tx, rows in psp_by_tx.items():
    if rows: unique_psp_by_batch[rows[0]['batch_id']] += int(rows[0]['net_minor'])
bank_mismatch_batches = sorted(b for b, n in unique_psp_by_batch.items() if n != bank_by_batch[b])
derived = {'EX-001' if overdue_ids == ['TX-NS-1007'] else 'BAD', 'EX-002' if dupe_keys == [('TX-NS-1003', 'PSP-NS-1003')] else 'BAD', 'EX-003' if fee_ids == ['TX-NS-1004'] else 'BAD', 'EX-004' if bank_mismatch_batches == ['B-20260910-02'] else 'BAD', 'EX-005' if timing_ids == ['TX-NS-1008'] else 'BAD'}
assert derived == {'EX-001', 'EX-002', 'EX-003', 'EX-004', 'EX-005'}
assert cutoff == date.fromisoformat('2026-09-10')
print(f'PASS rows ledger={len(ledger)} psp={len(psp)} bank={len(bank)} duplicate_keys={len(dupe_keys)} fee_mismatches={len(fee_ids)} overdue_missing={len(overdue_ids)} not_yet_due={len(timing_ids)} bank_mismatch_batches={len(bank_mismatch_batches)} documented_exceptions={len(derived)}')
PY
```

This check validates the fixture's internal arithmetic and identifiers. It is
not a production reconciliation engine and its output is not participant
evidence until a learner reruns it and records the output.

## Ticket use

Read [`tickets/README.md`](tickets/README.md) for the local FIN-001 epic and
five task templates. Acceptance boxes intentionally remain unchecked. These
templates are not published remote issues; a cohort may copy them into its
chosen tracker later with the fictional labels preserved.
