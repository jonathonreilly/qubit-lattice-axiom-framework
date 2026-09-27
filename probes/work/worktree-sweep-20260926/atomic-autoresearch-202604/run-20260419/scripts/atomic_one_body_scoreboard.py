#!/usr/bin/env python3
"""Compare one-body benchmark JSON files on a common scorecard."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def _parse_entry(raw_value: str) -> tuple[str, Path]:
    label, raw_path = raw_value.split("=", 1)
    return label, Path(raw_path)


def _entry_summary(label: str, payload: dict[str, Any], source_path: Path) -> dict[str, Any]:
    benchmark = payload["benchmark"]
    return {
        "label": label,
        "source_json": str(source_path),
        "parameters": benchmark["parameters"],
        "scores": benchmark["metrics"]["scores"],
        "relative_errors": benchmark["metrics"]["relative_errors"],
        "model_observables": benchmark["metrics"]["model_observables"],
    }


def _delta_summary(entry: dict[str, Any], baseline: dict[str, Any]) -> dict[str, float]:
    output: dict[str, float] = {}
    for key, value in entry["scores"].items():
        output[f"{key}_delta"] = float(value) - float(baseline["scores"][key])
    for key, value in entry["relative_errors"].items():
        output[f"{key}_delta"] = float(value) - float(baseline["relative_errors"][key])
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--entry",
        action="append",
        required=True,
        help="comparison entry in label=path.json form",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_scoreboard.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    entries = [
        _entry_summary(label, read_json(path), path)
        for label, path in (_parse_entry(raw_entry) for raw_entry in args.entry)
    ]
    baseline = entries[0]
    for entry in entries:
        entry["improvement_vs_baseline"] = _delta_summary(entry, baseline)

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "baseline_label": baseline["label"],
        "entries": entries,
        "best_by_one_body_rms": min(
            entries,
            key=lambda row: (
                float(row["scores"]["one_body_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic One-Body Scoreboard")
    print("==========================")
    for entry in entries:
        print(
            f"- {entry['label']}: "
            f"stencil={entry['parameters']['kinetic_stencil']} "
            f"spacing={entry['parameters']['lattice_spacing']:.4f} "
            f"one-body RMS={entry['scores']['one_body_rms_relative_error']:.6f}."
        )
    print(
        f"- Best one-body entry: {output_payload['best_by_one_body_rms']['label']}."
    )
    print(f"- Wrote scoreboard to {args.write_json}.")


if __name__ == "__main__":
    main()
