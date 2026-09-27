#!/usr/bin/env python3
"""Coarse joint retune of contact and shell-projector terms on the retained lane."""

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
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_projector_refine.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--contact-correction-strengths",
        type=float,
        nargs="*",
        default=(1.65, 1.75, 1.85, 1.95),
    )
    parser.add_argument(
        "--ground-excited-strengths",
        type=float,
        nargs="*",
        default=(-0.025, -0.03, -0.035),
    )
    parser.add_argument(
        "--excited-excited-strengths",
        type=float,
        nargs="*",
        default=(-0.02, -0.025, -0.03),
    )
    parser.add_argument(
        "--ground-ground-strengths",
        type=float,
        nargs="*",
        default=(-0.0025, -0.005, -0.0075),
    )
    parser.add_argument("--max-virtual-orbitals", type=int)
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
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_contact_joint_scan.json",
    )
    args = parser.parse_args()

    candidate_payload = read_json(args.candidate_json)
    source_row = (
        candidate_payload["accepted_candidate"]
        if candidate_payload.get("accepted_candidate") is not None
        else candidate_payload.get("best_by_full_rms")
    )
    if source_row is None:
        raise KeyError("unable to locate source candidate row")
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

    contact_strengths = [float(value) for value in args.contact_correction_strengths]
    ge_strengths = [float(value) for value in args.ground_excited_strengths]
    ee_strengths = [float(value) for value in args.excited_excited_strengths]
    gg_strengths = [float(value) for value in args.ground_ground_strengths]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    total_points = (
        len(contact_strengths) * len(ge_strengths) * len(ee_strengths) * len(gg_strengths)
    )
    current_index = 0
    for contact_strength in contact_strengths:
        for ge_strength in ge_strengths:
            for ee_strength in ee_strengths:
                for gg_strength in gg_strengths:
                    current_index += 1
                    scan_started = time.perf_counter()
                    model_fields = {
                        "contact_correction_strength": float(contact_strength),
                        "shell_projector_ground_excited_strength": float(ge_strength),
                        "shell_projector_excited_excited_strength": float(ee_strength),
                        "shell_projector_ground_ground_strength": float(gg_strength),
                    }
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
                    row.update(model_fields)
                    row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
                    rows.append(row)
                    print(
                        f"[{current_index}/{total_points}] "
                        f"ct={contact_strength:+.3f} "
                        f"ge={ge_strength:+.3f} "
                        f"ee={ee_strength:+.3f} "
                        f"gg={gg_strength:+.4f} "
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
            "contact_correction_strengths": contact_strengths,
            "ground_excited_strengths": ge_strengths,
            "excited_excited_strengths": ee_strengths,
            "ground_ground_strengths": gg_strengths,
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
    print("Atomic Shell+Contact Joint Scan")
    print("================================")
    print(f"- Accepted rows: {len(accepted_rows)}.")
    best = output_payload["accepted_candidate"] or output_payload["best_by_full_rms"]
    print(
        f"- Best row: ct={best['contact_correction_strength']:+.3f} "
        f"ge={best['shell_projector_ground_excited_strength']:+.3f} "
        f"ee={best['shell_projector_excited_excited_strength']:+.3f} "
        f"gg={best['shell_projector_ground_ground_strength']:+.4f} "
        f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote scan to {args.write_json}.")


if __name__ == "__main__":
    main()
