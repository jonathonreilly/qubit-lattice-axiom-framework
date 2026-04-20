#!/usr/bin/env python3
"""Retune the contact model on top of the promoted one-body family candidates."""

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
    correlated_row_summary,
    solve_correlated_solution,
)
from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def _basis_sweep_for_total(total_spatial: int) -> tuple[int, ...]:
    return tuple(
        size
        for size in (16, 24, 32, 40, 48, 56, 64, total_spatial)
        if 0 < size <= int(total_spatial)
    )


def _candidate_rows_from_continuum(payload: dict[str, Any], limit: int) -> list[dict[str, Any]]:
    rows = list(payload.get("surviving_candidates") or [])
    if not rows:
        rows = sorted(
            payload["family_rows"],
            key=lambda row: (
                float(row["observables"]["hydrogen_ground_magnitude"]["limit_relative_error"]),
                float(row["candidate"]["metrics"]["relative_errors"]["helium_ion_ground"]),
            ),
        )
    return rows[: int(limit)]


def _candidate_rank_key(row: dict[str, Any]) -> tuple[float, float]:
    return (
        float(row["metrics"]["scores"]["full_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--continuum-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_multi_family_continuum.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_contact.json",
    )
    parser.add_argument(
        "--validation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_fixed_basis_validation.json",
    )
    parser.add_argument("--candidate-limit", type=int, default=3)
    parser.add_argument(
        "--contact-correction-strengths",
        type=float,
        nargs="*",
        default=(1.6, 1.7, 1.8, 1.9, 2.0),
    )
    parser.add_argument(
        "--robustness-max-virtual-options",
        type=int,
        nargs="*",
        default=(32, 40, 48),
    )
    parser.add_argument("--min-accepted-basis-count", type=int, default=2)
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_contact_retune_round.json",
    )
    args = parser.parse_args()

    continuum_payload = read_json(args.continuum_json)
    validation_payload = read_json(args.validation_json)
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    validation_model = dict(validation_payload["validation_model"])
    candidate_rows = _candidate_rows_from_continuum(
        continuum_payload,
        limit=int(args.candidate_limit),
    )

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    round_rows = []
    total_points = len(candidate_rows) * len(args.contact_correction_strengths)
    current_index = 0
    for family_index, family_row in enumerate(candidate_rows, start=1):
        candidate = family_row["candidate"]
        candidate_parameters = dict(candidate["parameters"])
        base_payload = build_correlated_base_payload(candidate_parameters, validation_model)
        lambda_rows = []
        for contact_strength in args.contact_correction_strengths:
            current_index += 1
            scan_started = time.perf_counter()
            solution = solve_correlated_solution(
                base_payload,
                extra_tensor=float(contact_strength) * base_payload["contact_tensor"],
                extra_model_fields={
                    "contact_correction_strength": float(contact_strength),
                },
            )
            row = correlated_row_summary(
                solution,
                baseline_metrics_payload=baseline_metrics,
                ionization_slack=float(args.ionization_slack),
                gap_slack=float(args.gap_slack),
            )
            row["contact_correction_strength"] = float(contact_strength)
            row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            lambda_rows.append(row)
            print(
                f"[{current_index}/{total_points}] family={family_index} "
                f"lambda={float(contact_strength):.3f} "
                f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
                f"accepted={'YES' if row['acceptance']['accepted_on_full_lane'] else 'NO'}",
                flush=True,
            )

        accepted_rows = [row for row in lambda_rows if row["acceptance"]["accepted_on_full_lane"]]
        best_lambda_row = min(lambda_rows, key=_candidate_rank_key)
        selected_lambda_row = (
            min(accepted_rows, key=_candidate_rank_key)
            if accepted_rows
            else None
        )

        robustness_rows = []
        accepted_basis_count = 0
        if selected_lambda_row is not None:
            for max_virtual_orbitals in args.robustness_max_virtual_options:
                validation_model_local = dict(validation_model)
                validation_model_local["max_virtual_orbitals"] = int(max_virtual_orbitals)
                validation_model_local["basis_sweep"] = list(
                    _basis_sweep_for_total(
                        int(validation_model_local["max_orbitals"])
                        + int(validation_model_local["max_virtual_orbitals"])
                    )
                )
                base_payload_local = build_correlated_base_payload(
                    candidate_parameters,
                    validation_model_local,
                )
                robustness_solution = solve_correlated_solution(
                    base_payload_local,
                    extra_tensor=float(selected_lambda_row["contact_correction_strength"])
                    * base_payload_local["contact_tensor"],
                    extra_model_fields={
                        "contact_correction_strength": float(
                            selected_lambda_row["contact_correction_strength"]
                        ),
                    },
                    basis_sweep=tuple(validation_model_local["basis_sweep"]),
                )
                robustness_row = correlated_row_summary(
                    robustness_solution,
                    baseline_metrics_payload=baseline_metrics,
                    ionization_slack=float(args.ionization_slack),
                    gap_slack=float(args.gap_slack),
                )
                robustness_row["max_virtual_orbitals"] = int(max_virtual_orbitals)
                robustness_rows.append(robustness_row)
                accepted_basis_count += int(
                    robustness_row["acceptance"]["accepted_on_full_lane"]
                )

        candidate_round = {
            "source_candidate": family_row,
            "lambda_rows": lambda_rows,
            "best_lambda_row": best_lambda_row,
            "selected_lambda_row": selected_lambda_row,
            "robustness_rows": robustness_rows,
            "accepted_basis_count": int(accepted_basis_count),
            "strong_robust": bool(
                selected_lambda_row is not None
                and accepted_basis_count >= int(args.min_accepted_basis_count)
            ),
        }
        round_rows.append(candidate_round)

    accepted_rounds = [
        row for row in round_rows if row["selected_lambda_row"] is not None
    ]
    strong_rounds = [row for row in round_rows if row["strong_robust"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_continuum_json": str(args.continuum_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "source_validation_json": str(args.validation_json),
        "candidate_rows": round_rows,
        "best_accepted_candidate": (
            min(accepted_rounds, key=lambda row: _candidate_rank_key(row["selected_lambda_row"]))
            if accepted_rounds
            else None
        ),
        "best_strong_candidate": (
            min(strong_rounds, key=lambda row: _candidate_rank_key(row["selected_lambda_row"]))
            if strong_rounds
            else None
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Contact Retune Round")
    print("===========================")
    if output_payload["best_strong_candidate"] is not None:
        best = output_payload["best_strong_candidate"]["selected_lambda_row"]
        print(
            f"- Strong candidate: lambda={best['contact_correction_strength']:.3f} "
            f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    elif output_payload["best_accepted_candidate"] is not None:
        best = output_payload["best_accepted_candidate"]["selected_lambda_row"]
        print(
            f"- Accepted but not strong: lambda={best['contact_correction_strength']:.3f} "
            f"full={best['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    else:
        print("- No retuned contact candidate cleared the baseline contact gate.")
    print(f"- Wrote retune output to {args.write_json}.")


if __name__ == "__main__":
    main()
