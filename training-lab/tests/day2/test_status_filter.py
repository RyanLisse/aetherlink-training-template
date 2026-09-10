import json
import sys
import unittest
from pathlib import Path


LAB_DIR = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(LAB_DIR))

import status  # noqa: E402


class FilterStatusTests(unittest.TestCase):
    def setUp(self):
        self.records = json.loads((LAB_DIR / "records.json").read_text(encoding="utf-8"))

    def test_pending_filter(self):
        self.assertEqual(
            status.filter_status("pending", self.records),
            [{"reference": "TX-100", "status": "pending"}],
        )

    def test_failed_filter(self):
        self.assertEqual(
            status.filter_status("failed", self.records),
            [{"reference": "TX-102", "status": "failed"}],
        )

    def test_settled_filter(self):
        self.assertEqual(
            status.filter_status("settled", self.records),
            [{"reference": "TX-101", "status": "settled"}],
        )

    def test_valid_status_without_matches_returns_empty_list(self):
        self.assertEqual(status.filter_status("pending", self.records[1:]), [])

    def test_unknown_status_raises_value_error(self):
        with self.assertRaises(ValueError):
            status.filter_status("cancelled", self.records)

    def test_filter_does_not_mutate_input_or_leak_internal_note(self):
        before = json.loads(json.dumps(self.records))
        result = status.filter_status("pending", self.records)
        self.assertEqual(self.records, before)
        self.assertNotIn("internal_note", result[0])


if __name__ == "__main__":
    unittest.main()
