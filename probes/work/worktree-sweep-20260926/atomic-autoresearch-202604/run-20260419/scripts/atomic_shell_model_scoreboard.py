#!/usr/bin/env python3
"""Compare shell-baseline and shell-coupled one-body model-improvement attempts."""

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


def _entry_from_readout(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    candidate = payload["accepted_candidate"]
    return {
        "label": label,
        "source_json": str(path),
        "scores": candidate["metrics"]["scores"],
        "relative_errors": candidate["metrics"]["relative_errors"],
        "accepted": True,
    }


def _entry_from_scan(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    candidate = payload.get("accepted_candidate") or payload["best_by_full_rms"]
    return {
        "label": label,
        "source_json": str(path),
        "scores": candidate["metrics"]["scores"],
        "relative_errors": candidate["metrics"]["relative_errors"],
        "accepted": bool(candidate["acceptance"]["accepted_on_full_lane"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baseline-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--screen-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_screen.json",
    )
    parser.add_argument(
        "--retune-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_retune.json",
    )
    parser.add_argument(
        "--validation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_basis_robustness.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_model_scoreboard.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    entries = [_entry_from_readout("shell_projector_baseline", args.baseline_json)]
    if args.screen_json.exists():
        entries.append(_entry_from_scan("shell_one_body_screen", args.screen_json))
    if args.retune_json.exists():
        entries.append(_entry_from_scan("shell_one_body_retune", args.retune_json))
    if args.validation_json.exists():
        entries.append(_entry_from_scan("shell_one_body_validation", args.validation_json))
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "entries": entries,
        "best_entry": min(
            entries,
            key=lambda row: (
                float(row["scores"]["full_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "accepted_entries": [entry for entry in entries if entry["accepted"]],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell Model Scoreboard")
    print("=============================")
    for entry in entries:
        print(
            f"- {entry['label']}: full={entry['scores']['full_rms_relative_error']:.6f} "
            f"accepted={'YES' if entry['accepted'] else 'NO'}."
        )
    print(f"- Best entry: {output_payload['best_entry']['label']}.")
    print(f"- Wrote shell model scoreboard to {args.write_json}.")


if __name__ == "__main__":
    main()
