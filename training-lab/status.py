"""Day 1 and Day 2 status exercise.

Participants implement the two pure functions below.  The command-line
wrapper is intentionally kept small so the exercise stays about the contract,
not about a framework.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Optional


Record = dict[str, Any]
Result = dict[str, str]


def lookup_status(reference: str, records: list[Record]) -> Optional[Result]:
    """Return the public status for *reference*, or ``None`` if it is unknown."""

    raise NotImplementedError("Day 1 exercise: implement lookup_status")


def filter_status(status: str, records: list[Record]) -> list[Result]:
    """Return public status records matching *status*."""

    raise NotImplementedError("Day 2 exercise: implement filter_status")


def _load_records() -> list[Record]:
    records_path = Path(__file__).with_name("records.json")
    with records_path.open(encoding="utf-8") as records_file:
        return json.load(records_file)


def main() -> None:
    parser = argparse.ArgumentParser(description="Look up a fictional transaction status")
    parser.add_argument("reference", help="transaction reference, for example TX-100")
    args = parser.parse_args()
    print(json.dumps(lookup_status(args.reference, _load_records())))


if __name__ == "__main__":
    main()
