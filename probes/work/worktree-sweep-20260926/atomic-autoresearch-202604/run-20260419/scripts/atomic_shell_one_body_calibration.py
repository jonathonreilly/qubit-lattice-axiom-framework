#!/usr/bin/env python3
"""Calibrate coupling across the top shell-local one-body families."""

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

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402
from scripts.atomic_one_body_runtime import benchmark_one_body_candidate  # noqa: E402


def _rank_key(row: dict[str, Any]) -> tuple[float, float, float]:
    return (
        float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
        float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--search-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_family_search.json",
    )
    parser.add_argument("--family-limit", type=int, default=4)
    parser.add_argument(
        "--coupling-offsets",
        type=float,
        nargs="*",
        default=(-0.05, -0.03, -0.015, 0.0, 0.015, 0.03, 0.05),
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_one_body_calibration.json",
    )
    args = parser.parse_args()

    search_payload = read_json(args.search_json)
    baseline = search_payload["baseline_one_body_metrics"]
    families = list(search_payload.get("promoted_candidates") or [])
    if not families:
        families = list(search_payload.get("top_guardrail_candidates") or [])
    if not families:
        families = list(search_payload.get("top_candidates") or [])
    families = families[: int(args.family_limit)]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    family_results = []
    total_points = len(families) * len(args.coupling_offsets)
    current_index = 0
    for family_index, family in enumerate(families, start=1):
        parameters = dict(family["parameters"])
        rows = []
        for offset in args.coupling_offsets:
            current_index += 1
            scan_started = time.perf_counter()
            reference_coupling = float(parameters["reference_coupling"]) + float(offset)
            benchmark = benchmark_one_body_candidate(
                dimension=int(parameters["dimension"]),
                reference_coupling=float(reference_coupling),
                nuclear_charge=float(parameters["nuclear_charge"]),
                lattice_spacing=float(parameters["lattice_spacing"]),
                softening_radius=float(parameters["softening_radius"]),
                softening_multiplier=float(parameters["softening_multiplier"]),
                nuclear_profile=str(parameters["nuclear_profile"]),
                nuclear_quadrature_order=int(parameters["nuclear_quadrature_order"]),
                nuclear_counterterm_strength=float(parameters["nuclear_counterterm_strength"]),
                nuclear_counterterm_radius=parameters["nuclear_counterterm_radius"],
                nuclear_shell_strength=float(parameters.get("nuclear_shell_strength", 0.0)),
                nuclear_shell_radius=parameters.get("nuclear_shell_radius"),
                nuclear_shell_width=parameters.get("nuclear_shell_width"),
                kinetic_stencil=str(parameters["kinetic_stencil"]),
                max_orbitals=int(parameters["max_orbitals"]),
                n_eig=int(parameters["n_eig"]),
                custom_sizes=tuple(int(size) for size in parameters["active_sizes"]),
                fixed_physical_box=False,
            )
            benchmark["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            errors = benchmark["metrics"]["relative_errors"]
            scores = benchmark["metrics"]["scores"]
            hydrogen_error = float(errors["hydrogen_ground"])
            helium_error = float(errors["helium_ion_ground"])
            row = dict(benchmark)
            row["guardrails"] = {
                "hydrogen_improves": hydrogen_error
                < float(baseline["hydrogen_ground_error"]),
                "helium_ion_guardrail_pass": helium_error
                <= float(baseline["helium_ion_ground_error"]) + 0.01,
                "one_body_rms_improves": float(scores["one_body_rms_relative_error"])
                < float(baseline["one_body_rms_relative_error"]),
                "physically_bound": bool(
                    benchmark["hydrogen_ground_orbital"]["physical_bound"]
                    and benchmark["helium_ion_ground_orbital"]["physical_bound"]
                ),
            }
            row["promoted"] = bool(
                row["guardrails"]["hydrogen_improves"]
                and row["guardrails"]["helium_ion_guardrail_pass"]
                and row["guardrails"]["one_body_rms_improves"]
                and row["guardrails"]["physically_bound"]
            )
            rows.append(row)
            print(
                f"[{current_index}/{total_points}] family={family_index} "
                f"g={reference_coupling:.4f} "
                f"H={hydrogen_error:.4%} He+={helium_error:.4%} "
                f"rms={scores['one_body_rms_relative_error']:.6f} "
                f"promoted={'YES' if row['promoted'] else 'NO'}",
                flush=True,
            )

        promoted_rows = [row for row in rows if row["promoted"]]
        family_results.append(
            {
                "source_family": family,
                "rows": rows,
                "selected_family_candidate": (
                    min(promoted_rows, key=_rank_key)
                    if promoted_rows
                    else min(rows, key=_rank_key)
                ),
                "promoted_rows": promoted_rows,
            }
        )

    selected_final_candidates = [
        result["selected_family_candidate"] for result in family_results
    ]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_search_json": str(args.search_json),
        "family_results": family_results,
        "selected_final_candidates": sorted(
            selected_final_candidates,
            key=_rank_key,
        )[: int(args.family_limit)],
        "best_selected_candidate": min(selected_final_candidates, key=_rank_key),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell One-Body Calibration")
    print("=================================")
    print(
        f"- Selected families: {len(output_payload['selected_final_candidates'])} "
        f"best H="
        f"{output_payload['best_selected_candidate']['metrics']['relative_errors']['hydrogen_ground']:.4%}."
    )
    print(f"- Wrote calibration output to {args.write_json}.")


if __name__ == "__main__":
    main()
