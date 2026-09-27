#!/usr/bin/env python3
"""Check CI-basis robustness of an accepted correlated candidate."""

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
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_selected.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
    )
    parser.add_argument(
        "--max-virtual-orbital-options",
        type=int,
        nargs="*",
        default=(24, 32, 40, 48),
    )
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--allow-one-body-plateau",
        action=argparse.BooleanOptionalAction,
        default=False,
    )
    parser.add_argument("--one-body-tolerance", type=float, default=0.0)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_basis_robustness.json",
    )
    args = parser.parse_args()

    candidate_payload = read_json(args.candidate_json)
    candidate_parameters, validation_model = candidate_and_validation_parameters(
        candidate_payload["accepted_candidate"]
        if candidate_payload.get("accepted_candidate") is not None
        else candidate_payload
    )
    baseline_metrics = baseline_metrics_from_readout(read_json(args.baseline_readout_json))
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    for index, max_virtual_orbitals in enumerate(args.max_virtual_orbital_options, start=1):
        candidate_parameters_local = dict(candidate_parameters)
        validation_model_local = dict(validation_model)
        validation_model_local["max_virtual_orbitals"] = int(max_virtual_orbitals)
        validation_model_local["basis_sweep"] = list(
            _basis_sweep_for_total(
                int(validation_model_local["max_orbitals"])
                + int(validation_model_local["max_virtual_orbitals"])
            )
        )
        scan_started = time.perf_counter()
        base_payload = build_correlated_base_payload(
            candidate_parameters_local,
            validation_model_local,
        )
        source_row = (
            candidate_payload["accepted_candidate"]
            if candidate_payload.get("accepted_candidate") is not None
            else candidate_payload.get("best_by_full_rms")
        )
        model = source_row["solution"]["model"] if source_row is not None else {}
        extra_fields = correlated_operator_fields(model)
        extra_tensor = extra_tensor_from_model(base_payload, model)
        solution = solve_correlated_solution(
            base_payload,
            extra_tensor=extra_tensor,
            extra_model_fields=extra_fields,
            basis_sweep=tuple(validation_model_local["basis_sweep"]),
        )
        row = correlated_row_summary(
            solution,
            baseline_metrics_payload=baseline_metrics,
            ionization_slack=float(args.ionization_slack),
            gap_slack=float(args.gap_slack),
            allow_one_body_plateau=bool(args.allow_one_body_plateau),
            one_body_tolerance=float(args.one_body_tolerance),
        )
        row["max_virtual_orbitals"] = int(max_virtual_orbitals)
        row["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
        rows.append(row)
        print(
            f"[{index}/{len(args.max_virtual_orbital_options)}] "
            f"virt={max_virtual_orbitals} "
            f"full={row['metrics']['scores']['full_rms_relative_error']:.6f} "
            f"accepted={'YES' if row['acceptance']['accepted_on_full_lane'] else 'NO'}",
            flush=True,
        )

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
        "accepted_rows": [row for row in rows if row["acceptance"]["accepted_on_full_lane"]],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Correlated Basis Robustness")
    print("==================================")
    print(
        f"- Best basis row: virt="
        f"{output_payload['best_by_full_rms']['max_virtual_orbitals']} "
        f"full={output_payload['best_by_full_rms']['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote basis robustness output to {args.write_json}.")


if __name__ == "__main__":
    main()
