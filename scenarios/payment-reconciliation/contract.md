# Reconciliation reviewer · the one contract

The same contract runs in n8n (Day 3) and in Claude Code (Day 4). Platform,
model, adapter and settings are recorded as observations; the contract does
not change.

## Input

- `data/internal-ledger.csv`, `data/psp-settlements.csv`, `data/bank-credits.csv`
- Cutoff `2026-09-10 12:00 Europe/Amsterdam`; due dates are local calendar dates.
- Fee rule `expected_fee_minor = round_half_up(gross_minor × 2%)`; `expected_net_minor = gross_minor − expected_fee_minor`.
- All amounts are EUR minor units. No decimals, no FX.

## Output

One row per batch, in a Markdown table:

| batch_id | ledger expected net | PSP unique net | bank credit | classification | evidence | next human action |

`classification` is exactly one of: `matched`, `overdue missing settlement`,
`duplicate quarantine · UNRESOLVED`, `fee mismatch`, `bank payout mismatch`,
`not yet due · timing`. `evidence` lists the row ids read
(`TX-…`, `SET-…`, `BANK-…`). Anything not checked is written as `OPEN`.

## Rules

1. A duplicate settlement row is quarantined: keep both rows visible, count one, and leave the batch `UNRESOLVED`. Never approve it.
2. A due date after the cutoff is a timing item, not an error.
3. A fee mismatch stays a fee mismatch even when the PSP net reaches the bank.
4. A bank payout mismatch is a batch-level difference after the source rows were checked.
5. Read-only. No writes, no remote calls, no ticket creation, no approval. Severity and approval are human fields.
6. Do not invent a cause. Write `OPEN` and name who should confirm.

## Stop rule

Say "reconciled" for a batch only when its ledger net, PSP unique net and bank credit match and no rule above applies. Everything else is a finding with a next human action.
