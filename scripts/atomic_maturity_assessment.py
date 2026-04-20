#!/usr/bin/env python3
"""Synthesize the retained-lane maturity outputs into one technical verdict."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--gap-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_observable_gap_report.json",
        help="observable gap report JSON",
    )
    parser.add_argument(
        "--extrapolation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_virtual_basis_extrapolation.json",
        help="virtual-basis extrapolation JSON",
    )
    parser.add_argument(
        "--correlation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlation_diagnostics.json",
        help="correlation diagnostic JSON",
    )
    parser.add_argument(
        "--spin-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_spin_sector_diagnostics.json",
        help="spin diagnostic JSON",
    )
    parser.add_argument(
        "--scoreboard-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_maturity_scoreboard.json",
        help="maturity scoreboard JSON",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_maturity_assessment.json",
        help="machine-readable maturity assessment path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    gap_payload = read_json(args.gap_json)
    extrapolation_payload = read_json(args.extrapolation_json)
    correlation_payload = read_json(args.correlation_json)
    spin_payload = read_json(args.spin_json)
    scoreboard_payload = read_json(args.scoreboard_json)

    worst_gap = max(gap_payload["gap_rows"], key=lambda row: float(row["relative_error"]))
    best_entry = scoreboard_payload["best_by_full_rms"]
    baseline_entry = scoreboard_payload["entries"][0]
    singlet_limit = extrapolation_payload["observables"]["helium_ground_magnitude"]
    ionization_limit = extrapolation_payload["observables"]["helium_ionization_energy"]

    recommended_next_move = (
        "Shift effort away from larger virtual-basis scans and toward a one-body/continuum "
        "upgrade that reduces the hydrogen and He+ errors without losing the retained two-electron "
        "sector. The many-body basis is still improving, but only at the fourth-decimal level."
    )
    if str(worst_gap["observable"]) != "hydrogen_ground_magnitude":
        recommended_next_move = (
            "Keep tightening the many-body basis and correlated ansatz before reopening the "
            "one-body UV sector."
        )

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "worst_gap_observable": worst_gap,
        "best_scoreboard_entry": best_entry,
        "baseline_scoreboard_entry": baseline_entry,
        "basis_convergence": {
            "helium_ground_limit_relative_error": singlet_limit["limit_relative_error"],
            "helium_ionization_limit_relative_error": ionization_limit["limit_relative_error"],
            "full_rms_improvement_vs_baseline": float(
                best_entry["scores"]["full_rms_relative_error"]
            )
            - float(baseline_entry["scores"]["full_rms_relative_error"]),
            "basis_is_still_moving": abs(float(singlet_limit["remaining_to_limit"])) > 1.0e-3,
        },
        "correlation_summary": correlation_payload,
        "spin_summary": spin_payload,
        "recommended_next_move": recommended_next_move,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Maturity Assessment")
    print("==========================")
    print(
        f"- Worst residual observable: "
        f"{worst_gap['observable']} at {worst_gap['relative_error']:.4%}."
    )
    print(
        f"- Best milestone: {best_entry['label']} "
        f"(full RMS {best_entry['scores']['full_rms_relative_error']:.6f})."
    )
    print(f"- Recommended next move: {recommended_next_move}")
    print(f"- Wrote maturity assessment to {args.write_json}.")


if __name__ == "__main__":
    main()
