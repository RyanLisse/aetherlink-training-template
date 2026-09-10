# Trainer answer key — Northstar reconciliation

This is an expected worked answer for the fictional fixture. It is not
evidence that a participant or any real payment operation ran these checks.

## Rules applied

Cutoff: `2026-09-10 12:00 Europe/Amsterdam`. All amounts are EUR minor units.
Expected fee is `round_half_up(gross × 0.02)`; expected net is gross minus fee.
For batch comparison, count one valid PSP row per transaction after
quarantining an ambiguous duplicate. Keep the duplicate source row visible.

## Arithmetic

| Batch | Ledger expected net | PSP provisional unique net | PSP raw net | Bank credit | Result |
| --- | ---: | ---: | ---: | ---: | --- |
| `B-20260908-01` | 12,250 + 8,722 = **20,972** | **20,972** | **20,972** | **20,972** | matched (`SET-1001-A`, `SET-1002-A`, `BANK-0908-01`) |
| `B-20260908-02` | **7,448** | **0** | **0** | **0** | `EX-001`; no PSP settlement for `TX-NS-1007` |
| `B-20260909-01` | 19,600 + 4,410 = **24,010** | **24,010** (provisional) | 19,600 + 19,600 + 4,410 = **43,610** | **24,010** | `EX-002`; duplicate quarantined; batch `UNRESOLVED`, not approved |
| `B-20260909-02` | **15,435** | **15,450** | **15,450** | **15,450** | `EX-003`; fee is 300 vs expected 315 |
| `B-20260910-02` | **3,234** | **3,234** | **3,234** | **3,200** | `EX-004`; bank is 34 lower |
| `B-20260912-01` | **9,702** | **0** | **0** | **0** | `EX-005`; due after cutoff, timing only |

Fee spot checks: `TX-NS-1004` expected `round_half_up(15750 × .02) = 315`,
then `15750 − 315 = 15435`; PSP reports fee `300` and net `15450`. The other
seven ledger rows satisfy the same arithmetic. `TX-NS-1006` is a matched PSP
row (`3300 − 66 = 3234`); its batch bank credit is the separate `EX-004`.

## Exact case key

| Case | Finding and evidence | Required learner classification/action |
| --- | --- | --- |
| `EX-001` | `TX-NS-1007` / `NS-LDG-1007`, due `2026-09-08`; no PSP `SET-1007`, no bank credit | Overdue missing settlement. Escalate for investigation with the source IDs; do not claim recovery. |
| `EX-002` | `SET-1003-A` and `SET-1003-B` share `TX-NS-1003` and `PSP-NS-1003`; raw `43,610` versus provisional unique `24,010` | Duplicate settlement row. Quarantine ambiguity, retain both rows, mark the batch `UNRESOLVED`, and ask for source confirmation; never silently delete or count twice. |
| `EX-003` | `TX-NS-1004` expected fee `315`, `SET-1004-A` fee `300`; net difference `+15` | Fee mismatch. Open a fee investigation; bank match does not erase the fee difference. |
| `EX-004` | `B-20260910-02`; valid PSP net `3,234`, `BANK-0910-02` credit `3,200`; difference `−34` | Bank payout mismatch. Open a bank trace/reconciliation action; do not infer cause. |
| `EX-005` | `TX-NS-1008` / `NS-LDG-1008`, due `2026-09-12`; no settlement at cutoff | Not-yet-due timing item, **not an error**. Monitor after due date; do not escalate as overdue. |

The absence of settlement for `TX-NS-1008` is intentional and is covered by
`EX-005`, not a sixth missing-settlement case. The bank file has one row per
credited batch in this fixture; no unmatched bank credit is intended.

## Expected handoff fields

For each case, the evidence-backed handoff names: case ID, transaction or
batch ID, source row IDs, amount calculation, classification, next action,
owner placeholder, due-date/cutoff reasoning, and `OPEN` status until a human
rechecks it. The answer key supplies expected values only; participants must
record their own command or worksheet output.
