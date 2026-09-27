#!/usr/bin/env python3
"""Scan bound-shell projector corrections on top of the retained contact candidate."""

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
    correlated_operator_fields,
    correlated_row_summary,
    extra_tensor_from_model,
    solve_correlated_solution,
)
from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_selected.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_contact.json",
    )
    parser.add_argument(
        "--ground-excited-strengths",
        type=float,
        nargs="*",
        default=(0.0, -0.01, -0.02, -0.05, -0.08),
    )
    parser.add_argument(
        "--excited-excited-strengths",
        type=float,
        nargs="*",
        default=(0.0, -0.005, -0.01, -0.02),
    )
    parser.add_argument(
        "--ground-ground-strengths",
        type=float,
        nargs="*",
        default=(0.0,),
    )
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_projector_scan.json",
    )
    args = parser.parse_args()

    payload = read_json(args.candidate_json)
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    candidate_payload = (
        payload["accepted_candidate"] if payload.get("accepted_candidate") is not None else payload
    )
    candidate_parameters, validation_model = candidate_and_validation_parameters(
        candidate_payload
    )
    base_payload = build_correlated_base_payload(candidate_parameters, validation_model)
    source_model = (
        candidate_payload["solution"]["model"]
        if "solution" in candidate_payload
        else {}
    )
    source_operator_fields = correlated_operator_fields(source_model)

    ge_strengths = [float(value) for value in args.ground_excited_strengths]
    ee_strengths = [float(value) for value in args.excited_excited_strengths]
    gg_strengths = [float(value) for value in args.ground_ground_strengths]
    total_points = len(ge_strengths) * len(ee_strengths) * len(gg_strengths)

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    current_index = 0
    for ground_excited_strength in ge_strengths:
        for excited_excited_strength in ee_strengths:
            for ground_ground_strength in gg_strengths:
                current_index += 1
                scan_started = time.perf_counter()
                model_fields = {
                    **source_operator_fields,
                    "shell_projector_ground_excited_strength": float(
                        ground_excited_strength
                    ),
                    "shell_projector_excited_excited_strength": float(
                        excited_excited_strength
                    ),
                    "shell_projector_ground_ground_strength": float(
                        ground_ground_strength
                    ),
                }
                solution = solve_correlated_solution(
                    base_payload,
                    extra_tensor=extra_tensor_from_model(base_payload, model_fields),
                    extra_model_fields=model_fields,
                )
                row = correlated_row_summary(
                    solution,
                    baseline_metrics_payload=baseline_metrics,
                    ionization_slack=float(args.ionization_slack),
                    gap_slack=float(args.gap_slack),
                )
                row["shell_projector_ground_excited_strength"] = float(
                    ground_excited_strength
                )
                row["shell_projector_excited_excited_strength"] = float(
                    excited_excited_strength
                )
                row["shell_projector_ground_ground_strength"] = float(
                    ground_ground_strength
                )
                row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
                rows.append(row)
                print(
                    f"[{current_index}/{total_points}] "
                    f"ge={ground_excited_strength:+.3f} "
                    f"ee={excited_excited_strength:+.3f} "
                    f"gg={ground_ground_strength:+.3f} "
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
        "rows": rows,
        "best_by_full_rms": min(
            rows,
            key=lambda row: (
                float(row["metrics"]["scores"]["full_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        ),
        "accepted_candidate": (
            min(
                accepted_rows,
                key=lambda row: (
                    float(row["metrics"]["scores"]["full_rms_relative_error"]),
                    float(row["metrics"]["scores"]["max_relative_error"]),
                ),
            )
            if accepted_rows
            else None
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Bound-Shell Projector Scan")
    print("=================================")
    if output_payload["accepted_candidate"] is None:
        print("- No bound-shell projector candidate cleared the acceptance gate.")
    else:
        accepted = output_payload["accepted_candidate"]
        print(
            f"- Accepted candidate: ge={accepted['shell_projector_ground_excited_strength']:+.3f} "
            f"ee={accepted['shell_projector_excited_excited_strength']:+.3f} "
            f"full={accepted['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    print(f"- Wrote scan output to {args.write_json}.")


if __name__ == "__main__":
    main()
