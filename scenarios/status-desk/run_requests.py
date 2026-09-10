"""Run Northstar's supplemental requests against the existing status API.

This is a read-only learner aid. The starter status module is intentionally
unimplemented, so a NotImplementedError is reported as a failed request and
the process exits nonzero until the learner implements the lab functions.
"""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any


SCENARIO_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCENARIO_DIR.parents[1]
STATUS_PATH = REPO_ROOT / "training-lab" / "status.py"


def _load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as data_file:
        return json.load(data_file)


def _load_status_module():
    spec = importlib.util.spec_from_file_location("northstar_training_status", STATUS_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import status module from {STATUS_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _public_shape(value: Any) -> bool:
    if isinstance(value, dict):
        return set(value) == {"reference", "status"}
    if isinstance(value, list):
        return all(_public_shape(item) for item in value)
    return value is None


def _run_request(status_module: Any, request: dict[str, Any], records: list[dict[str, Any]]) -> tuple[bool, str]:
    original_records = copy.deepcopy(records)
    expected_error = request.get("expected_error")
    try:
        if request["operation"] == "lookup":
            actual = status_module.lookup_status(request["reference"], records)
        elif request["operation"] == "filter":
            actual = status_module.filter_status(request["status"], records)
        else:
            return False, f"unknown operation {request['operation']!r}"
    except Exception as exc:  # report learner failures without hiding the request ID
        if records != original_records:
            return False, "records input was mutated before the exception"
        if expected_error == type(exc).__name__:
            return True, f"raised {type(exc).__name__} as expected"
        return False, f"raised {type(exc).__name__}: {exc}"

    if expected_error is not None:
        return False, f"expected {expected_error}, returned {actual!r}"
    if actual != request.get("expected"):
        return False, f"expected {request.get('expected')!r}, got {actual!r}"
    if not _public_shape(actual):
        return False, "result exposes fields outside reference/status"
    if records != original_records:
        return False, "records input was mutated"
    return True, "matched expected fixture result"


def main() -> int:
    records = _load_json(SCENARIO_DIR / "data" / "records.json")
    requests = _load_json(SCENARIO_DIR / "data" / "requests.json")
    if not isinstance(records, list) or not isinstance(requests, list):
        print("FAIL fixture files must contain arrays", file=sys.stderr)
        return 1

    try:
        status_module = _load_status_module()
    except Exception as exc:
        print(f"FAIL import status module: {type(exc).__name__}: {exc}")
        return 1

    failures = 0
    for request in requests:
        passed, detail = _run_request(status_module, request, copy.deepcopy(records))
        label = "PASS" if passed else "FAIL"
        print(f"{request.get('id', '<missing-id>')} {label} — {detail}")
        failures += not passed
    print(f"Summary: {len(requests) - failures} passed, {failures} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
