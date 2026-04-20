#!/usr/bin/env python3
"""Test a small finite-range pair add-on on top of the refined shell/contact model."""

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

from scripts.atomic_correlated_runtime import (  # noqa: E402
    baseline_metrics_from_readout,
    build_correlated_base_payload,
    candidate_and_validation_parameters,
    correlated_operator_fields,
    correlated_row_summary,
    extra_tensor_from_model,
    solve_correlated_solution,
)
from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def _rank_key(row: dict[str, Any]) -> tuple[float, float]:
    return (
        float(row["metrics"]["scores"]["full_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
    )


def _basis_sweep_for_total(total_spatial: int) -> tuple[int, ...]:
    return tuple(
        size
        for size in (16, 24, 32, 40, 48, 56, 64, total_spatial)
        if 0 < size <= int(total_spatial)
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_contact_joint_refine.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_contact_joint.json",
    )
    parser.add_argument(
        "--pair-profiles",
        nargs="*",
        default=("gaussian", "exponential"),
    )
    parser.add_argument(
        "--pair-radii",
        type=float,
        nargs="*",
        default=(0.6, 0.8, 1.0),
    )
    parser.add_argument(
        "--pair-strengths",
        type=float,
        nargs="*",
        default=(-0.10, -0.05, 0.05, 0.10),
    )
    parser.add_argument("--max-virtual-orbitals", type=int)
    parser.add_argument("--pair-cutoff-multiplier", type=float, default=3.0)
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--allow-one-body-plateau",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    parser.add_argument("--one-body-tolerance", type=float, default=1.0e-9)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_pair_addon_scan.json",
    )
    args = parser.parse_args()

    candidate_payload = read_json(args.candidate_json)
    source_row = candidate_payload.get("accepted_candidate") or candidate_payload["best_by_full_rms"]
    candidate_parameters, validation_model = candidate_and_validation_parameters(source_row)
    if args.max_virtual_orbitals is not None:
        validation_model["max_virtual_orbitals"] = int(args.max_virtual_orbitals)
        validation_model["basis_sweep"] = list(
            _basis_sweep_for_total(
                int(validation_model["max_orbitals"])
                + int(validation_model["max_virtual_orbitals"])
            )
        )
    base_payload = build_correlated_base_payload(candidate_parameters, validation_model)
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    source_model = dict(source_row["solution"]["model"])
    base_model_fields = correlated_operator_fields(source_model)

    pair_profiles = [str(value) for value in args.pair_profiles]
    pair_radii = [float(value) for value in args.pair_radii]
    pair_strengths = [float(value) for value in args.pair_strengths]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    total_points = len(pair_profiles) * len(pair_radii) * len(pair_strengths)
    current_index = 0
    for pair_profile in pair_profiles:
        for pair_radius in pair_radii:
            for pair_strength in pair_strengths:
                current_index += 1
                scan_started = time.perf_counter()
                model_fields = dict(base_model_fields)
                model_fields.update(
                    {
                        "pair_correction_profile": str(pair_profile),
                        "pair_correction_radius": float(pair_radius),
                        "pair_correction_strength": float(pair_strength),
                        "pair_correction_cutoff_multiplier": float(
                            args.pair_cutoff_multiplier
                        ),
                    }
                )
                extra_tensor = extra_tensor_from_model(base_payload, model_fields)
                solution = solve_correlated_solution(
                    base_payload,
                    extra_tensor=extra_tensor,
                    extra_model_fields=model_fields,
                )
                row = correlated_row_summary(
                    solution,
                    baseline_metrics_payload=baseline_metrics,
                    ionization_slack=float(args.ionization_slack),
                    gap_slack=float(args.gap_slack),
                    allow_one_body_plateau=bool(args.allow_one_body_plateau),
                    one_body_tolerance=float(args.one_body_tolerance),
                )
                row["pair_profile"] = str(pair_profile)
                row["pair_radius"] = float(pair_radius)
                row["pair_strength"] = float(pair_strength)
                row["pair_cutoff_multiplier"] = float(args.pair_cutoff_multiplier)
                row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
                rows.append(row)
                print(
                    f"[{current_index}/{total_points}] "
                    f"profile={pair_profile} "
                    f"r={pair_radius:.3f} "
                    f"s={pair_strength:+.3f} "
                    f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
                    f"{'ACCEPT' if row['acceptance']['accepted_on_full_lane'] else 'reject'}",
                    flush=True,
                )

    accepted_rows = [row for row in rows if row["acceptance"]["accepted_on_full_lane"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_candidate_json": str(args.candidate_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "scan_configuration": {
            "pair_profiles": pair_profiles,
            "pair_radii": pair_radii,
            "pair_strengths": pair_strengths,
            "pair_cutoff_multiplier": float(args.pair_cutoff_multiplier),
            "ionization_slack": float(args.ionization_slack),
            "gap_slack": float(args.gap_slack),
            "allow_one_body_plateau": bool(args.allow_one_body_plateau),
            "one_body_tolerance": float(args.one_body_tolerance),
        },
        "rows": rows,
        "accepted_candidate": (
            min(accepted_rows, key=_rank_key) if accepted_rows else None
        ),
        "best_by_full_rms": min(rows, key=_rank_key),
        "accepted_row_count": len(accepted_rows),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell+Pair Add-on Scan")
    print("=============================")
    print(f"- Accepted rows: {len(accepted_rows)}.")
    best = output_payload["accepted_candidate"] or output_payload["best_by_full_rms"]
    print(
        f"- Best row: profile={best['pair_profile']} "
        f"r={best['pair_radius']:.3f} "
        f"s={best['pair_strength']:+.3f} "
        f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote pair add-on scan to {args.write_json}.")


if __name__ == "__main__":
    main()
