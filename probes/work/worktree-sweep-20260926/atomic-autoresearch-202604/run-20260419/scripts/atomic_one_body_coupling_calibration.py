#!/usr/bin/env python3
"""Recalibrate the shared one-body coupling on a promoted UV/discretization family."""

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


def _search_key(row: dict[str, Any]) -> tuple[float, float, float]:
    return (
        float(row["metrics"]["scores"]["one_body_rms_relative_error"]),
        float(row["metrics"]["scores"]["max_relative_error"]),
        float(row["metrics"]["relative_errors"]["hydrogen_ground"]),
    )


def _candidate_parameters(search_payload: dict[str, Any]) -> dict[str, Any]:
    candidate = search_payload.get("promoted_candidate")
    if candidate is None:
        candidate = search_payload["best_by_one_body_rms"]
    return dict(candidate["parameters"])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--search-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_uv_search.json",
    )
    parser.add_argument(
        "--reference-couplings",
        type=float,
        nargs="*",
        default=tuple(1.45 + 0.01 * index for index in range(31)),
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_coupling_calibration.json",
    )
    args = parser.parse_args()

    search_payload = read_json(args.search_json)
    base_parameters = _candidate_parameters(search_payload)
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    rows = []
    for index, reference_coupling in enumerate(args.reference_couplings, start=1):
        scan_started = time.perf_counter()
        benchmark = benchmark_one_body_candidate(
            dimension=int(base_parameters["dimension"]),
            reference_coupling=float(reference_coupling),
            nuclear_charge=float(base_parameters["nuclear_charge"]),
            lattice_spacing=float(base_parameters["lattice_spacing"]),
            softening_radius=float(base_parameters["softening_radius"]),
            softening_multiplier=float(base_parameters["softening_multiplier"]),
            nuclear_profile=str(base_parameters["nuclear_profile"]),
            nuclear_quadrature_order=int(base_parameters["nuclear_quadrature_order"]),
            nuclear_counterterm_strength=float(
                base_parameters["nuclear_counterterm_strength"]
            ),
            nuclear_counterterm_radius=base_parameters["nuclear_counterterm_radius"],
            kinetic_stencil=str(base_parameters["kinetic_stencil"]),
            max_orbitals=int(base_parameters["max_orbitals"]),
            n_eig=int(base_parameters["n_eig"]),
            fixed_physical_box=bool(base_parameters["fixed_physical_box"]),
            reference_spacing=float(base_parameters["reference_spacing"]),
            reference_sizes=(
                tuple(int(size) for size in base_parameters["reference_sizes"])
                if base_parameters["reference_sizes"] is not None
                else None
            ),
            custom_sizes=(
                tuple(int(size) for size in base_parameters["custom_sizes"])
                if base_parameters["custom_sizes"] is not None
                else None
            ),
        )
        benchmark["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
        rows.append(benchmark)
        print(
            f"[{index}/{len(args.reference_couplings)}] "
            f"g={reference_coupling:.4f} "
            f"H={benchmark['metrics']['relative_errors']['hydrogen_ground']:.4%} "
            f"He+={benchmark['metrics']['relative_errors']['helium_ion_ground']:.4%} "
            f"rms={benchmark['metrics']['scores']['one_body_rms_relative_error']:.6f}",
            flush=True,
        )

    baseline = search_payload.get("promoted_candidate") or search_payload["best_by_one_body_rms"]
    selected_final_candidate = min(rows, key=_search_key)
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_search_json": str(args.search_json),
        "baseline_candidate": baseline,
        "selected_final_candidate": selected_final_candidate,
        "top_candidates": sorted(rows, key=_search_key)[:15],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic One-Body Coupling Calibration")
    print("====================================")
    print(
        f"- Selected coupling: "
        f"{selected_final_candidate['parameters']['reference_coupling']:.4f} "
        f"with RMS={selected_final_candidate['metrics']['scores']['one_body_rms_relative_error']:.6f}."
    )
    print(f"- Wrote calibration output to {args.write_json}.")


if __name__ == "__main__":
    main()
