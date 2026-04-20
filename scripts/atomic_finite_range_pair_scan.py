#!/usr/bin/env python3
"""Scan finite-range correlated pair operators on the fixed helium basis."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_correlated_runtime import (  # noqa: E402
    baseline_metrics_from_readout,
    build_correlated_base_payload,
    candidate_and_validation_parameters,
    correlated_row_summary,
    finite_range_pair_tensor,
    solve_correlated_solution,
)
from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_coupling_calibration.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
    )
    parser.add_argument(
        "--pair-profile",
        choices=("gaussian", "exponential"),
        default="gaussian",
    )
    parser.add_argument(
        "--pair-radii",
        type=float,
        nargs="*",
        default=(0.8, 1.2, 1.6),
    )
    parser.add_argument(
        "--pair-strengths",
        type=float,
        nargs="*",
        default=(0.75, 1.25, 1.75),
    )
    parser.add_argument("--cutoff-multiplier", type=float, default=3.0)
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_finite_range_pair_scan.json",
    )
    args = parser.parse_args()

    candidate_payload = read_json(args.candidate_json)
    candidate_parameters, validation_model = candidate_and_validation_parameters(candidate_payload)
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    base_payload = build_correlated_base_payload(candidate_parameters, validation_model)
    rows = []
    radii = [float(value) for value in args.pair_radii]
    strengths = [float(value) for value in args.pair_strengths]
    total_points = len(radii) * len(strengths)
    current_index = 0
    for pair_radius in radii:
        extra_tensor_base = finite_range_pair_tensor(
            base_payload,
            correlation_radius=float(pair_radius),
            strength=1.0,
            profile=str(args.pair_profile),
            cutoff_multiplier=float(args.cutoff_multiplier),
        )
        for pair_strength in strengths:
            current_index += 1
            scan_started = time.perf_counter()
            solution = solve_correlated_solution(
                base_payload,
                extra_tensor=float(pair_strength) * extra_tensor_base,
                extra_model_fields={
                    "pair_correction_profile": str(args.pair_profile),
                    "pair_correction_radius": float(pair_radius),
                    "pair_correction_strength": float(pair_strength),
                    "pair_correction_cutoff_multiplier": float(args.cutoff_multiplier),
                },
            )
            row = correlated_row_summary(
                solution,
                baseline_metrics_payload=baseline_metrics,
                ionization_slack=float(args.ionization_slack),
                gap_slack=float(args.gap_slack),
            )
            row["pair_radius"] = float(pair_radius)
            row["pair_strength"] = float(pair_strength)
            row["pair_profile"] = str(args.pair_profile)
            row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            rows.append(row)
            print(
                f"[{current_index}/{total_points}] "
                f"r={pair_radius:.3f} s={pair_strength:.3f} "
                f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
                f"accepted={'YES' if row['acceptance']['accepted_on_full_lane'] else 'NO'}",
                flush=True,
            )

    accepted_rows = [row for row in rows if row["acceptance"]["accepted_on_full_lane"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_candidate_json": str(args.candidate_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "pair_profile": str(args.pair_profile),
        "rows": rows,
        "best_by_full_rms": min(
            rows,
            key=lambda row: (
                float(row["metrics"]["scores"]["full_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        ),
        "accepted_candidate": min(
            accepted_rows,
            key=lambda row: (
                float(row["metrics"]["scores"]["full_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        )
        if accepted_rows
        else None,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Finite-Range Pair Scan")
    print("=============================")
    if output_payload["accepted_candidate"] is None:
        print("- No finite-range pair candidate cleared the acceptance gate.")
    else:
        accepted = output_payload["accepted_candidate"]
        print(
            f"- Accepted candidate: profile={accepted['pair_profile']} "
            f"r={accepted['pair_radius']:.3f} s={accepted['pair_strength']:.3f} "
            f"full={accepted['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    print(f"- Wrote finite-range scan to {args.write_json}.")


if __name__ == "__main__":
    main()
