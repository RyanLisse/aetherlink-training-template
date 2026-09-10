"""Trainer reference implementation for the status exercise."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Optional


Record = dict[str, Any]
Result = dict[str, str]
VALID_STATUSES = {"pending", "settled", "failed"}


def _public_result(record: Record) -> Result:
    return {"reference": str(record["reference"]), "status": str(record["status"])}


def lookup_status(reference: str, records: list[Record]) -> Optional[Result]:
    for record in records:
        if record.get("reference") == reference:
            return _public_result(record)
    return None


def filter_status(status: str, records: list[Record]) -> list[Result]:
    if status not in VALID_STATUSES:
        raise ValueError(f"unknown status: {status}")
    return [_public_result(record) for record in records if record.get("status") == status]


def main() -> None:
    parser = argparse.ArgumentParser(description="Look up a fictional transaction status")
    parser.add_argument("reference", help="transaction reference, for example TX-100")
    args = parser.parse_args()
    records_path = Path(__file__).with_name("records.json")
    records = json.loads(records_path.read_text(encoding="utf-8"))
    print(json.dumps(lookup_status(args.reference, records)))


if __name__ == "__main__":
    main()
