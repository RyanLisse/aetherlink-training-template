#!/usr/bin/env python3
"""Fixture check for the fictional reconciliation case. Exit 0 = PASS.

Same arithmetic as the snippet in README.md, runnable from any directory and
usable as a Claude Code Stop hook: an agent may not claim a batch is
reconciled before this check passes.
"""
import csv
import sys
from collections import Counter, defaultdict
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "data"
CUTOFF = date.fromisoformat("2026-09-10")


def read(name):
    with (ROOT / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def fee_ok(gross, fee):
    return (Decimal(gross) * Decimal("0.02")).quantize(Decimal("1"), rounding=ROUND_HALF_UP) == Decimal(fee)


def main():
    ledger, psp, bank = read("internal-ledger.csv"), read("psp-settlements.csv"), read("bank-credits.csv")
    assert len({r["transaction_id"] for r in ledger}) == len(ledger), "ledger transaction ids must be unique"
    assert all(r["currency"] == "EUR" for rows in (ledger, psp, bank) for r in rows), "EUR only"
    assert all(fee_ok(r["gross_minor"], r["expected_fee_minor"]) for r in ledger), "ledger fee rule"
    assert all(int(r["gross_minor"]) - int(r["expected_fee_minor"]) == int(r["expected_net_minor"]) for r in ledger), "ledger net"
    ledger_by_tx = {r["transaction_id"]: r for r in ledger}
    assert all(r["transaction_id"] in ledger_by_tx for r in psp), "psp rows reference the ledger"
    psp_by_tx = defaultdict(list)
    for r in psp:
        psp_by_tx[r["transaction_id"]].append(r)
    dupes = [k for k, n in Counter((r["transaction_id"], r["psp_reference"]) for r in psp).items() if n > 1]
    fee_ids = sorted({r["transaction_id"] for r in psp if not fee_ok(r["gross_minor"], r["fee_minor"])})
    overdue = sorted(tx for tx, l in ledger_by_tx.items() if not psp_by_tx.get(tx) and date.fromisoformat(l["settlement_due_date"]) < CUTOFF)
    timing = sorted(tx for tx, l in ledger_by_tx.items() if not psp_by_tx.get(tx) and date.fromisoformat(l["settlement_due_date"]) > CUTOFF)
    bank_by_batch = defaultdict(int)
    for r in bank:
        bank_by_batch[r["batch_id"]] += int(r["amount_minor"])
    unique_by_batch = defaultdict(int)
    for rows in psp_by_tx.values():
        unique_by_batch[rows[0]["batch_id"]] += int(rows[0]["net_minor"])
    bank_mismatch = sorted(b for b, n in unique_by_batch.items() if n != bank_by_batch[b])
    expected = {
        "EX-001 overdue": overdue == ["TX-NS-1007"],
        "EX-002 duplicate": dupes == [("TX-NS-1003", "PSP-NS-1003")],
        "EX-003 fee": fee_ids == ["TX-NS-1004"],
        "EX-004 bank": bank_mismatch == ["B-20260910-02"],
        "EX-005 timing": timing == ["TX-NS-1008"],
    }
    failed = [k for k, ok in expected.items() if not ok]
    assert not failed, f"documented cases not reproduced: {failed}"
    print(f"PASS ledger={len(ledger)} psp={len(psp)} bank={len(bank)} duplicates={len(dupes)} fee_mismatches={len(fee_ids)} overdue={len(overdue)} not_yet_due={len(timing)} bank_mismatch_batches={len(bank_mismatch)} cases=5")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"FAIL {e}", file=sys.stderr)
        sys.exit(2)
