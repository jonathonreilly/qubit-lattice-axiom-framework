#!/usr/bin/env python3
"""Refit nuclear and repulsion softening independently on a correlated candidate."""

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
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_selected.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_contact.json",
    )
    parser.add_argument(
        "--nuclear-softening-radii",
        type=float,
        nargs="*",
        default=(0.5, 0.6, 0.7),
    )
    parser.add_argument(
        "--repulsion-softening-radii",
        type=float,
        nargs="*",
        default=(1.0, 1.1, 1.2),
    )
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_softening_refit.json",
    )
    args = parser.parse_args()

    payload = read_json(args.candidate_json)
    candidate_parameters, validation_model = candidate_and_validation_parameters(
        payload["accepted_candidate"] if "accepted_candidate" in payload else payload
    )
    model = (
        payload["accepted_candidate"]["solution"]["model"]
        if "accepted_candidate" in payload
        else payload["solution"]["model"]
    )
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    nuclear_radii = [float(value) for value in args.nuclear_softening_radii]
    repulsion_radii = [float(value) for value in args.repulsion_softening_radii]
    total_points = len(nuclear_radii) * len(repulsion_radii)
    current_index = 0
    for nuclear_softening_radius in nuclear_radii:
        for repulsion_softening_radius in repulsion_radii:
            current_index += 1
            scan_started = time.perf_counter()
            candidate_parameters_local = dict(candidate_parameters)
            validation_model_local = dict(validation_model)
            candidate_parameters_local["softening_radius"] = float(nuclear_softening_radius)
            validation_model_local["repulsion_softening_radius"] = float(
                repulsion_softening_radius
            )
            base_payload = build_correlated_base_payload(
                candidate_parameters_local,
                validation_model_local,
            )
            extra_fields = {}
            extra_tensor = None
            if "contact_correction_strength" in model:
                extra_fields["contact_correction_strength"] = float(
                    model["contact_correction_strength"]
                )
                extra_tensor = (
                    float(model["contact_correction_strength"])
                    * base_payload["contact_tensor"]
                )
            elif "pair_correction_profile" in model:
                extra_fields["pair_correction_profile"] = str(
                    model["pair_correction_profile"]
                )
                extra_fields["pair_correction_radius"] = float(
                    model["pair_correction_radius"]
                )
                extra_fields["pair_correction_strength"] = float(
                    model["pair_correction_strength"]
                )
                extra_fields["pair_correction_cutoff_multiplier"] = float(
                    model["pair_correction_cutoff_multiplier"]
                )
                extra_tensor = finite_range_pair_tensor(
                    base_payload,
                    correlation_radius=float(model["pair_correction_radius"]),
                    strength=float(model["pair_correction_strength"]),
                    profile=str(model["pair_correction_profile"]),
                    cutoff_multiplier=float(model["pair_correction_cutoff_multiplier"]),
                )
            solution = solve_correlated_solution(
                base_payload,
                extra_tensor=extra_tensor,
                extra_model_fields=extra_fields,
            )
            row = correlated_row_summary(
                solution,
                baseline_metrics_payload=baseline_metrics,
                ionization_slack=float(args.ionization_slack),
                gap_slack=float(args.gap_slack),
            )
            row["nuclear_softening_radius"] = float(nuclear_softening_radius)
            row["repulsion_softening_radius"] = float(repulsion_softening_radius)
            row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            rows.append(row)
            print(
                f"[{current_index}/{total_points}] "
                f"rn={nuclear_softening_radius:.3f} rr={repulsion_softening_radius:.3f} "
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
    print("Atomic Correlated Softening Refit")
    print("=================================")
    if output_payload["accepted_candidate"] is None:
        print("- No softening refit candidate cleared the acceptance gate.")
    else:
        accepted = output_payload["accepted_candidate"]
        print(
            f"- Accepted refit: rn={accepted['nuclear_softening_radius']:.3f} "
            f"rr={accepted['repulsion_softening_radius']:.3f} "
            f"full={accepted['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    print(f"- Wrote softening refit to {args.write_json}.")


if __name__ == "__main__":
    main()
