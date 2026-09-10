# AetherLink training lab: public status exercise

This two-day lab is a tiny, fictional exercise in making a data contract
explicit and checking it with an agent. It is public-safe: `records.json`
contains synthetic records only, and the `internal_note` values are included
to make the public output boundary testable.

## Prerequisites

- Python 3.9 or newer (the examples use `python3`)
- Git, if you want to inspect the diff or use an agent in a checkout
- An agent is optional. A local editor and the exact commands below are a
  supported fallback.

No dependency installation is required.

## Participant setup

Open a terminal in your cloned template repository (the directory containing
`README.md` and `training-lab/`) and run:

```sh
python3 --version
```

Keep the shell in that repository directory for the commands in this guide.
No package or dependency installation is required.

## Day 1: lookup

Implement `lookup_status(reference, records)` in `training-lab/status.py`.
It returns `{'reference': ..., 'status': ...}` for a known reference and
`None` for an unknown reference. It must never return `internal_note`.

The starter intentionally raises `NotImplementedError`. That is the expected
failure before the exercise is completed:

```sh
python3 -m unittest discover -s training-lab/tests/day1 -v
```

After implementing the function, rerun the same command. The CLI reads the
fixture next to the script and renders JSON:

```sh
python3 training-lab/status.py TX-100
python3 training-lab/status.py TX-999
```

Expected completed outputs are `{"reference": "TX-100", "status":
"pending"}` and `null`.

## Day 2: filtering

Implement `filter_status(status, records)` in `training-lab/status.py`.
Valid statuses are `pending`, `settled`, and `failed`; an unknown status must
raise `ValueError`. Return the same two-field public dictionaries, preserve
input order, and do not mutate `records`.

```sh
python3 -m unittest discover -s training-lab/tests/day2 -v
```

## Synthetic metric check

`metrics.json` is a synthetic fixture for a deterministic exercise only. It
contains a 4% baseline and an 8% observation window. The checker uses the
explicit fixed threshold of 5%; it does not make a statistical or “3 sigma”
claim from these values:

```sh
python3 training-lab/check_metrics.py
```

The JSON result contains `"breach": true`. Treat that result as an exercise
prompt: map it to opening an incident and writing a new intent. No real
monitoring, incident system, or external service is contacted.

## Trainer solution and release rehearsal

The reference implementation is intentionally visible to trainers at
`training-lab/trainer/solution.py`. It is not imported by the learner tests and
there is no automatic shortcut from the starter to the solution.

To rehearse a learner-only local release, choose an explicit output path:

```sh
python3 training-lab/release_rehearsal.py --output lab-output/day-2.zip
python3 -m zipfile -l lab-output/day-2.zip
```

The archive contains only `status.py` and `records.json`. The command fails if
the output already exists; pass `--overwrite` only when deliberately replacing
that local archive. This is a local ZIP exercise and performs no upload or
deployment.
