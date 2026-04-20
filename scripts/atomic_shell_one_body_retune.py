#!/usr/bin/env python3
"""Retune shell/contact coefficients around the best shell-coupled one-body family."""

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


def _offset_grid(center: float, offsets: list[float]) -> list[float]:
    return [float(center) + float(offset) for offset in offsets]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--screen-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_screen.json",
    )
    parser.add_argument(
        "--selection-source",
        choices=("accepted_or_best", "accepted", "best_by_full_rms"),
        default="accepted_or_best",
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
        default=(-0.005, 0.0, 0.005),
    )
    parser.add_argument(
        "--excited-excited-offsets",
        type=float,
        nargs="*",
        default=(-0.005, 0.0, 0.005),
    )
    parser.add_argument(
        "--ground-ground-offsets",
        type=float,
        nargs="*",
        default=(-0.0025, 0.0, 0.0025),
    )
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_retune.json",
    )
    args = parser.parse_args()

    screen_payload = read_json(args.screen_json)
    if args.selection_source == "accepted":
        source_row = screen_payload.get("accepted_candidate")
        if source_row is None:
            raise ValueError("requested accepted selection but screen has no accepted candidate")
    elif args.selection_source == "best_by_full_rms":
        source_row = screen_payload["best_by_full_rms"]
    else:
        source_row = screen_payload.get("accepted_candidate") or screen_payload["best_by_full_rms"]
    candidate_parameters, validation_model = candidate_and_validation_parameters(source_row)
    base_payload = build_correlated_base_payload(candidate_parameters, validation_model)
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    source_model = dict(source_row["solution"]["model"])

    contact_values = _offset_grid(
        float(source_model["contact_correction_strength"]),
        [float(value) for value in args.contact_offsets],
    )
    ge_values = _offset_grid(
        float(source_model["shell_projector_ground_excited_strength"]),
        [float(value) for value in args.ground_excited_offsets],
    )
    ee_values = _offset_grid(
        float(source_model["shell_projector_excited_excited_strength"]),
        [float(value) for value in args.excited_excited_offsets],
    )
    gg_values = _offset_grid(
        float(source_model["shell_projector_ground_ground_strength"]),
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
        "source_screen_json": str(args.screen_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
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
    print("Atomic Shell One-Body Retune")
    print("============================")
    print(f"- Accepted rows: {len(accepted_rows)}.")
    best = output_payload["accepted_candidate"] or output_payload["best_by_full_rms"]
    print(
        f"- Best row: ct={best['contact_correction_strength']:+.3f} "
        f"ge={best['shell_projector_ground_excited_strength']:+.4f} "
        f"ee={best['shell_projector_excited_excited_strength']:+.4f} "
        f"gg={best['shell_projector_ground_ground_strength']:+.4f} "
        f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote retune output to {args.write_json}.")


if __name__ == "__main__":
    main()
