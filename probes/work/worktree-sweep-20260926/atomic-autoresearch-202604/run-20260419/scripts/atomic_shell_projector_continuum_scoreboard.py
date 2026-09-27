#!/usr/bin/env python3
"""Compare local and continuum-phase shell-projector lane results."""

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


def _correlated_entry(label: str, path: Path) -> dict[str, Any]:
    payload = read_json(path)
    candidate = payload["accepted_candidate"]
    return {
        "label": label,
        "entry_type": "live_correlated",
        "source_json": str(path),
        "scores": candidate["metrics"]["scores"],
        "relative_errors": candidate["metrics"]["relative_errors"],
        "model_observables": candidate["metrics"]["model_observables"],
        "spatial_orbital_count": int(candidate["solution"]["two_electron"]["spatial_orbital_count"]),
    }


def _continuum_projection_entry(path: Path) -> dict[str, Any]:
    payload = read_json(path)
    return {
        "label": "shell_projector_continuum_limit",
        "entry_type": "continuum_projection",
        "source_json": str(path),
        "scores": payload["continuum_limit_accuracy_metrics"]["scores"],
        "relative_errors": payload["continuum_limit_accuracy_metrics"]["relative_errors"],
        "model_observables": payload["continuum_limit_accuracy_metrics"]["model_observables"],
        "spatial_orbital_count": int(
            payload["selected_live_candidate"]["solution"]["two_electron"]["spatial_orbital_count"]
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--local-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--continuum-live-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector_continuum_live.json",
    )
    parser.add_argument(
        "--continuum-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_readout.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_scoreboard.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    entries = [
        _correlated_entry("shell_projector_local", args.local_json),
        _correlated_entry("shell_projector_continuum_live", args.continuum_live_json),
        _continuum_projection_entry(args.continuum_readout_json),
    ]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "entries": entries,
        "best_live_entry": min(
            [entry for entry in entries if entry["entry_type"] == "live_correlated"],
            key=lambda row: (
                float(row["scores"]["full_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "best_projection_entry": min(
            [entry for entry in entries if entry["entry_type"] == "continuum_projection"],
            key=lambda row: (
                float(row["scores"]["full_rms_relative_error"]),
                float(row["scores"]["max_relative_error"]),
            ),
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell-Projector Continuum Scoreboard")
    print("===========================================")
    for entry in entries:
        print(
            f"- {entry['label']}: full={entry['scores']['full_rms_relative_error']:.6f} "
            f"H={entry['relative_errors']['hydrogen_ground']:.4%}."
        )
    print(f"- Best live entry: {output_payload['best_live_entry']['label']}.")
    print(f"- Wrote scoreboard to {args.write_json}.")


if __name__ == "__main__":
    main()
