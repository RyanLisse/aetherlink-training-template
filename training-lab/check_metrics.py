"""Evaluate the fixed synthetic metric fixture for the exercise."""

from __future__ import annotations

import json
from pathlib import Path


THRESHOLD_PERCENT = 5.0


def main() -> None:
    metrics_path = Path(__file__).with_name("metrics.json")
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    window = float(metrics["window_percent"])
    print(
        json.dumps(
            {
                "fixture_label": metrics["fixture_label"],
                "metric": metrics["metric"],
                "baseline_percent": metrics["baseline_percent"],
                "window_percent": window,
                "threshold_percent": THRESHOLD_PERCENT,
                "breach": window > THRESHOLD_PERCENT,
                "exercise_mapping": "breach=true -> open an incident and write a new intent",
            }
        )
    )


if __name__ == "__main__":
    main()
