#!/usr/bin/env python3
"""Screen calibrated one-body families under the retained shell-projector model."""

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


def _basis_sweep_for_total(total_spatial: int) -> tuple[int, ...]:
    return tuple(
        size
        for size in (16, 24, 32, 40, 48, 56, 64, total_spatial)
        if 0 < size <= int(total_spatial)
    )


def _rank_key(row: dict[str, Any]) -> tuple[float, float]:
    return (
        float(row["metrics"]["scores"]["full_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--calibration-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_calibration.json",
    )
    parser.add_argument(
        "--shell-candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_projector_refine.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_shell_projector.json",
    )
    parser.add_argument("--candidate-limit", type=int, default=4)
    parser.add_argument("--max-virtual-orbitals", type=int, default=24)
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_screen.json",
    )
    args = parser.parse_args()

    calibration_payload = read_json(args.calibration_json)
    shell_payload = read_json(args.shell_candidate_json)
    shell_row = (
        shell_payload["accepted_candidate"]
        if shell_payload.get("accepted_candidate") is not None
        else shell_payload["best_by_full_rms"]
    )
    shell_candidate_parameters, validation_model = candidate_and_validation_parameters(shell_row)
    validation_model["max_virtual_orbitals"] = int(args.max_virtual_orbitals)
    validation_model["basis_sweep"] = list(
        _basis_sweep_for_total(
            int(validation_model["max_orbitals"]) + int(validation_model["max_virtual_orbitals"])
        )
    )
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    shell_model_fields = correlated_operator_fields(shell_row["solution"]["model"])
    source_candidates = list(calibration_payload["selected_final_candidates"])[: int(args.candidate_limit)]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    for index, candidate in enumerate(source_candidates, start=1):
        scan_started = time.perf_counter()
        base_payload = build_correlated_base_payload(dict(candidate["parameters"]), validation_model)
        extra_tensor = extra_tensor_from_model(base_payload, shell_model_fields)
        solution = solve_correlated_solution(
            base_payload,
            extra_tensor=extra_tensor,
            extra_model_fields=shell_model_fields,
        )
        row = correlated_row_summary(
            solution,
            baseline_metrics_payload=baseline_metrics,
            ionization_slack=float(args.ionization_slack),
            gap_slack=float(args.gap_slack),
        )
        row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
        row["source_candidate"] = candidate
        rows.append(row)
        print(
            f"[{index}/{len(source_candidates)}] "
            f"stencil={candidate['parameters']['kinetic_stencil']} "
            f"profile={candidate['parameters']['nuclear_profile']} "
            f"g={candidate['parameters']['reference_coupling']:.4f} "
            f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
            f"{'ACCEPT' if row['acceptance']['accepted_on_full_lane'] else 'reject'}",
            flush=True,
        )

    accepted_rows = [row for row in rows if row["acceptance"]["accepted_on_full_lane"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_calibration_json": str(args.calibration_json),
        "source_shell_candidate_json": str(args.shell_candidate_json),
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
    print("Atomic Shell One-Body Screen")
    print("============================")
    print(f"- Accepted rows: {len(accepted_rows)}.")
    best = output_payload["accepted_candidate"] or output_payload["best_by_full_rms"]
    print(
        f"- Best row: "
        f"{best['source_candidate']['parameters']['kinetic_stencil']} "
        f"{best['source_candidate']['parameters']['nuclear_profile']} "
        f"g={best['source_candidate']['parameters']['reference_coupling']:.4f} "
        f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote screen to {args.write_json}.")


if __name__ == "__main__":
    main()
