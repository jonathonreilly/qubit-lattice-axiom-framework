#!/usr/bin/env python3
"""Run a larger-continuum fixed-box sweep for the retained shell-projector lane."""

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
from scripts.atomic_two_body_runtime import rescale_sizes_for_physical_box  # noqa: E402


def _continuum_candidate_parameters(
    candidate_parameters: dict[str, Any],
    *,
    lattice_spacing: float,
    min_size: int,
) -> dict[str, Any]:
    output = dict(candidate_parameters)
    reference_spacing = float(candidate_parameters["lattice_spacing"])
    reference_sizes = tuple(int(size) for size in candidate_parameters["active_sizes"])
    active_sizes = rescale_sizes_for_physical_box(
        reference_sizes,
        reference_spacing=reference_spacing,
        lattice_spacing=float(lattice_spacing),
        min_size=int(min_size),
    )
    output["lattice_spacing"] = float(lattice_spacing)
    output["active_sizes"] = list(active_sizes)
    return output


def _best_row(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    if not rows:
        return None
    return min(
        rows,
        key=lambda row: (
            float(row["metrics"]["scores"]["full_rms_relative_error"]),
            float(row["metrics"]["scores"]["max_relative_error"]),
        ),
    )


def _best_accepted_row(rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    accepted = [
        row
        for row in rows
        if bool(row["acceptance"]["accepted_on_full_lane"])
    ]
    return _best_row(accepted)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_projector_refine.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--lattice-spacings",
        type=float,
        nargs="*",
        default=(1.0, 0.9, 0.8, 0.72, 0.64),
    )
    parser.add_argument("--min-size", type=int, default=12)
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--allow-one-body-plateau",
        action="store_true",
        default=True,
        help="allow the one-body RMS to remain unchanged within tolerance",
    )
    parser.add_argument("--one-body-tolerance", type=float, default=1.0e-9)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_sweep.json",
    )
    args = parser.parse_args()

    candidate_payload = read_json(args.candidate_json)
    baseline_payload = read_json(args.baseline_readout_json)
    baseline_metrics = baseline_metrics_from_readout(baseline_payload)
    candidate_parameters, validation_model = candidate_and_validation_parameters(
        candidate_payload
    )
    extra_model_fields = correlated_operator_fields(candidate_parameters)
    spacings = [float(value) for value in args.lattice_spacings]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows: list[dict[str, Any]] = []
    for index, lattice_spacing in enumerate(spacings, start=1):
        row_started = time.perf_counter()
        spacing_parameters = _continuum_candidate_parameters(
            candidate_parameters,
            lattice_spacing=float(lattice_spacing),
            min_size=int(args.min_size),
        )
        base_payload = build_correlated_base_payload(
            spacing_parameters,
            validation_model,
        )
        extra_tensor = extra_tensor_from_model(base_payload, extra_model_fields)
        row = correlated_row_summary(
            solution=solve_correlated_solution(
                base_payload,
                extra_tensor=extra_tensor,
                extra_model_fields=extra_model_fields,
            ),
            baseline_metrics_payload=baseline_metrics,
            ionization_slack=float(args.ionization_slack),
            gap_slack=float(args.gap_slack),
            allow_one_body_plateau=bool(args.allow_one_body_plateau),
            one_body_tolerance=float(args.one_body_tolerance),
        )
        active_sizes = tuple(int(size) for size in spacing_parameters["active_sizes"])
        row["elapsed_seconds"] = round(time.perf_counter() - row_started, 6)
        row["parameters"] = {
            "lattice_spacing": float(lattice_spacing),
            "active_sizes": [int(size) for size in active_sizes],
            "reference_spacing": float(candidate_parameters["lattice_spacing"]),
            "reference_sizes": [
                int(size) for size in candidate_parameters["active_sizes"]
            ],
            "physical_box_lengths": [
                float(size) * float(lattice_spacing) for size in active_sizes
            ],
        }
        rows.append(row)
        print(
            f"[{index}/{len(spacings)}] "
            f"a={lattice_spacing:.4f} sizes={active_sizes} "
            f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
            f"H={row['metrics']['relative_errors']['hydrogen_ground']:.4%} "
            f"He+={row['metrics']['relative_errors']['helium_ion_ground']:.4%} "
            f"I={row['metrics']['relative_errors']['helium_ionization_energy']:.4%} "
            f"gap={row['metrics']['relative_errors']['singlet_triplet_gap']:.4%} "
            f"{'ACCEPT' if row['acceptance']['accepted_on_full_lane'] else 'reject'}",
            flush=True,
        )

    best_by_full_rms = _best_row(rows)
    accepted_candidate = _best_accepted_row(rows)
    finest_spacing_row = min(
        rows,
        key=lambda row: float(row["parameters"]["lattice_spacing"]),
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_candidate_json": str(args.candidate_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "scan_configuration": {
            "lattice_spacings": spacings,
            "min_size": int(args.min_size),
            "ionization_slack": float(args.ionization_slack),
            "gap_slack": float(args.gap_slack),
            "allow_one_body_plateau": bool(args.allow_one_body_plateau),
            "one_body_tolerance": float(args.one_body_tolerance),
        },
        "rows": rows,
        "accepted_candidate": accepted_candidate,
        "best_by_full_rms": best_by_full_rms,
        "finest_spacing_row": finest_spacing_row,
        "accepted_row_count": sum(
            1 for row in rows if row["acceptance"]["accepted_on_full_lane"]
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell-Projector Continuum Sweep")
    print("======================================")
    print(
        f"- Accepted rows: {output_payload['accepted_row_count']} / {len(rows)}."
    )
    if accepted_candidate is not None:
        print(
            f"- Best accepted spacing: "
            f"a={accepted_candidate['parameters']['lattice_spacing']:.4f} "
            f"full={accepted_candidate['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    print(f"- Wrote sweep to {args.write_json}.")


if __name__ == "__main__":
    main()
