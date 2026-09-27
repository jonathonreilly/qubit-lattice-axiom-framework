#!/usr/bin/env python3
"""Odd/even lattice-geometry sweep for the calibrated atomic lane."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time
from typing import Any

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_coulomb_calibration import (  # noqa: E402
    ACTUALS_HARTREE,
    candidate_metrics,
    summarize_candidate,
)
from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, write_json  # noqa: E402
from scripts.atomic_two_body_runtime import solve_two_electron_atomic_model  # noqa: E402


def family_fit(
    scan_rows: list[dict[str, Any]],
    parity: str,
) -> dict[str, Any] | None:
    family_rows = [
        row
        for row in scan_rows
        if (int(row["lattice_edge"]) % 2 == 1) == (parity == "odd")
    ]
    if len(family_rows) < 2:
        return None

    inverse_sizes = np.array(
        [1.0 / float(row["lattice_edge"]) for row in family_rows],
        dtype=float,
    )

    def fit_key(path: tuple[str, ...]) -> dict[str, float]:
        values = np.array(
            [extract_path(row, path) for row in family_rows],
            dtype=float,
        )
        slope, intercept = np.polyfit(inverse_sizes, values, 1)
        return {
            "slope_vs_inverse_size": float(slope),
            "intercept_infinite_size": float(intercept),
        }

    return {
        "parity": parity,
        "edges": [int(row["lattice_edge"]) for row in family_rows],
        "hydrogen_ground_magnitude": fit_key(
            ("metrics", "model_observables", "hydrogen_ground_magnitude")
        ),
        "helium_ion_ground_magnitude": fit_key(
            ("metrics", "model_observables", "helium_ion_ground_magnitude")
        ),
        "helium_ground_magnitude": fit_key(
            ("metrics", "model_observables", "helium_ground_magnitude")
        ),
        "helium_ionization_energy": fit_key(
            ("metrics", "model_observables", "helium_ionization_energy")
        ),
        "full_rms_relative_error": fit_key(
            ("metrics", "scores", "full_rms_relative_error")
        ),
        "hydrogen_relative_error": fit_key(
            ("metrics", "relative_errors", "hydrogen_ground")
        ),
    }


def extract_path(payload: dict[str, Any], path: tuple[str, ...]) -> float:
    value: Any = payload
    for key in path:
        value = value[key]
    return float(value)


def run_scan_row(
    *,
    lattice_edge: int,
    reference_coupling: float,
    softening_radius: float,
    lattice_spacing: float,
    max_orbitals: int,
) -> dict[str, Any]:
    solution = solve_two_electron_atomic_model(
        reference_coupling=reference_coupling,
        lattice_spacing=lattice_spacing,
        nuclear_softening_radius=softening_radius,
        repulsion_softening_radius=softening_radius,
        max_orbitals=max_orbitals,
        custom_sizes=(lattice_edge, lattice_edge, lattice_edge),
        basis_sweep=(max_orbitals,),
    )
    row = summarize_candidate(solution)
    row["lattice_edge"] = int(lattice_edge)
    row["lattice_parity"] = "odd" if lattice_edge % 2 else "even"
    return row


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--lattice-edges",
        type=int,
        nargs="*",
        default=(14, 15, 16, 17, 18, 19),
        help="cubic lattice edge lengths to scan",
    )
    parser.add_argument(
        "--reference-coupling",
        type=float,
        default=1.625,
        help="calibrated one-body coupling to test on geometry variants",
    )
    parser.add_argument(
        "--softening-radius",
        type=float,
        default=0.85,
        help="shared calibrated Coulomb softening radius",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing",
    )
    parser.add_argument(
        "--scan-max-orbitals",
        type=int,
        default=12,
        help="reduced orbital count used during the geometry scan",
    )
    parser.add_argument(
        "--final-max-orbitals",
        type=int,
        default=16,
        help="reduced orbital count used for the selected geometry rerun",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_geometry_extrapolation.json",
        help="machine-readable geometry sweep output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    scan_rows: list[dict[str, Any]] = []
    edges = [int(edge) for edge in args.lattice_edges]

    for index, lattice_edge in enumerate(edges, start=1):
        row_started = time.perf_counter()
        row = run_scan_row(
            lattice_edge=lattice_edge,
            reference_coupling=float(args.reference_coupling),
            softening_radius=float(args.softening_radius),
            lattice_spacing=float(args.lattice_spacing),
            max_orbitals=int(args.scan_max_orbitals),
        )
        row["elapsed_seconds"] = round(time.perf_counter() - row_started, 6)
        scan_rows.append(row)
        print(
            f"[{index}/{len(edges)}] "
            f"L={lattice_edge} "
            f"parity={row['lattice_parity']} "
            f"H={row['metrics']['model_observables']['hydrogen_ground_magnitude']:.6f} "
            f"He={row['metrics']['model_observables']['helium_ground_magnitude']:.6f} "
            f"I={row['metrics']['model_observables']['helium_ionization_energy']:.6f} "
            f"full_rms={row['metrics']['scores']['full_rms_relative_error']:.4f}",
            flush=True,
        )

    best_by_full = min(
        scan_rows,
        key=lambda row: (
            row["metrics"]["scores"]["full_rms_relative_error"],
            row["metrics"]["scores"]["max_relative_error"],
            row["metrics"]["relative_errors"]["hydrogen_ground"],
        ),
    )
    best_by_hydrogen = min(
        scan_rows,
        key=lambda row: (
            row["metrics"]["relative_errors"]["hydrogen_ground"],
            row["metrics"]["scores"]["full_rms_relative_error"],
        ),
    )
    selected_edge = int(best_by_full["lattice_edge"])
    selected_solution = solve_two_electron_atomic_model(
        reference_coupling=float(args.reference_coupling),
        lattice_spacing=float(args.lattice_spacing),
        nuclear_softening_radius=float(args.softening_radius),
        repulsion_softening_radius=float(args.softening_radius),
        max_orbitals=int(args.final_max_orbitals),
        custom_sizes=(selected_edge, selected_edge, selected_edge),
        basis_sweep=tuple(
            size
            for size in (4, 6, 8, 10, 12, 14, int(args.final_max_orbitals))
            if size <= int(args.final_max_orbitals)
        ),
    )
    selected_summary = summarize_candidate(selected_solution)
    selected_summary["lattice_edge"] = selected_edge
    selected_summary["lattice_parity"] = "odd" if selected_edge % 2 else "even"

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "actuals_hartree": ACTUALS_HARTREE,
        "scan_configuration": {
            "lattice_edges": edges,
            "reference_coupling": float(args.reference_coupling),
            "softening_radius": float(args.softening_radius),
            "lattice_spacing": float(args.lattice_spacing),
            "scan_max_orbitals": int(args.scan_max_orbitals),
            "final_max_orbitals": int(args.final_max_orbitals),
        },
        "scan_rows": scan_rows,
        "best_by_full_rms": best_by_full,
        "best_by_hydrogen_error": best_by_hydrogen,
        "odd_family_fit": family_fit(scan_rows, "odd"),
        "even_family_fit": family_fit(scan_rows, "even"),
        "selected_final_candidate": selected_summary,
        "selected_solution": selected_solution,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Geometry Extrapolation")
    print("=============================")
    print(
        f"- Best full-rms lattice edge: {best_by_full['lattice_edge']} "
        f"({best_by_full['lattice_parity']})."
    )
    print(
        f"- Best hydrogen lattice edge: {best_by_hydrogen['lattice_edge']} "
        f"({best_by_hydrogen['lattice_parity']})."
    )
    print(
        f"- Selected final He singlet: "
        f"{selected_summary['metrics']['model_observables']['helium_ground_magnitude']:.6f}, "
        f"H: {selected_summary['metrics']['model_observables']['hydrogen_ground_magnitude']:.6f}."
    )
    print(f"- Wrote geometry output to {args.write_json}.")


if __name__ == "__main__":
    main()
