import json
import sys
import unittest
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LAB_DIR))

import status  # noqa: E402


class LookupStatusTests(unittest.TestCase):
    def setUp(self):
        self.records = json.loads((LAB_DIR / "records.json").read_text(encoding="utf-8"))

    def test_known_pending_record_exposes_only_public_fields(self):
        self.assertEqual(
            status.lookup_status("TX-100", self.records),
            {"reference": "TX-100", "status": "pending"},
        )

    def test_known_settled_record_exposes_only_public_fields(self):
        self.assertEqual(
            status.lookup_status("TX-101", self.records),
            {"reference": "TX-101", "status": "settled"},
        )

    def test_unknown_reference_returns_none(self):
        self.assertIsNone(status.lookup_status("TX-999", self.records))

    def test_internal_note_never_leaks(self):
        result = status.lookup_status("TX-102", self.records)
        self.assertEqual(result, {"reference": "TX-102", "status": "failed"})
        self.assertNotIn("internal_note", result)


if __name__ == "__main__":
    unittest.main()
