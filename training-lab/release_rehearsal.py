"""Create a local learner release archive for the status exercise."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def main() -> None:
    parser = argparse.ArgumentParser(description="Package the learner status exercise locally")
    parser.add_argument("--output", required=True, type=Path, help="path for the new ZIP archive")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace an existing archive at --output",
    )
    args = parser.parse_args()
    output = args.output.expanduser()
    if output.exists() and not args.overwrite:
        parser.error(f"output already exists: {output} (pass --overwrite to replace it)")
    output.parent.mkdir(parents=True, exist_ok=True)
    lab_dir = Path(__file__).resolve().parent
    mode = "w" if args.overwrite else "x"
    with ZipFile(output, mode=mode, compression=ZIP_DEFLATED) as archive:
        archive.write(lab_dir / "status.py", arcname="status.py")
        archive.write(lab_dir / "records.json", arcname="records.json")
    print(output)


if __name__ == "__main__":
    main()
