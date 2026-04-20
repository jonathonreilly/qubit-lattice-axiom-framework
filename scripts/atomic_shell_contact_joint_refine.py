#!/usr/bin/env python3
"""Refine the joint shell/contact operator around the best coarse point."""

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


def _offset_grid(center: float, offsets: list[float]) -> list[float]:
    return [float(center) + float(offset) for offset in offsets]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_contact_joint_scan.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument(
        "--contact-offsets",
        type=float,
        nargs="*",
        default=(-0.05, 0.0, 0.05),
    )
    parser.add_argument(
        "--ground-excited-offsets",
        type=float,
        nargs="*",
        default=(-0.005, -0.0025, 0.0, 0.0025, 0.005),
    )
    parser.add_argument(
        "--excited-excited-offsets",
        type=float,
        nargs="*",
        default=(-0.005, -0.0025, 0.0, 0.0025, 0.005),
    )
    parser.add_argument(
        "--ground-ground-offsets",
        type=float,
        nargs="*",
        default=(-0.0025, 0.0, 0.0025),
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
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_contact_joint_refine.json",
    )
    args = parser.parse_args()

    source_payload = read_json(args.source_json)
    source_row = source_payload.get("accepted_candidate") or source_payload["best_by_full_rms"]
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

    contact_values = _offset_grid(
        float(source_row["contact_correction_strength"]),
        [float(value) for value in args.contact_offsets],
    )
    ge_values = _offset_grid(
        float(source_row["shell_projector_ground_excited_strength"]),
        [float(value) for value in args.ground_excited_offsets],
    )
    ee_values = _offset_grid(
        float(source_row["shell_projector_excited_excited_strength"]),
        [float(value) for value in args.excited_excited_offsets],
    )
    gg_values = _offset_grid(
        float(source_row["shell_projector_ground_ground_strength"]),
        [float(value) for value in args.ground_ground_offsets],
    )

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    total_points = len(contact_values) * len(ge_values) * len(ee_values) * len(gg_values)
    current_index = 0
    for contact_strength in contact_values:
        for ge_strength in ge_values:
            for ee_strength in ee_values:
                for gg_strength in gg_values:
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
                        f"ge={ge_strength:+.4f} "
                        f"ee={ee_strength:+.4f} "
                        f"gg={gg_strength:+.4f} "
                        f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
                        f"{'ACCEPT' if row['acceptance']['accepted_on_full_lane'] else 'reject'}",
                        flush=True,
                    )

    accepted_rows = [row for row in rows if row["acceptance"]["accepted_on_full_lane"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_json": str(args.source_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "refine_configuration": {
            "contact_values": contact_values,
            "ground_excited_values": ge_values,
            "excited_excited_values": ee_values,
            "ground_ground_values": gg_values,
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
    print("Atomic Shell+Contact Joint Refine")
    print("=================================")
    print(f"- Accepted rows: {len(accepted_rows)}.")
    best = output_payload["accepted_candidate"] or output_payload["best_by_full_rms"]
    print(
        f"- Best row: ct={best['contact_correction_strength']:+.3f} "
        f"ge={best['shell_projector_ground_excited_strength']:+.4f} "
        f"ee={best['shell_projector_excited_excited_strength']:+.4f} "
        f"gg={best['shell_projector_ground_ground_strength']:+.4f} "
        f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote refine output to {args.write_json}.")


if __name__ == "__main__":
    main()
