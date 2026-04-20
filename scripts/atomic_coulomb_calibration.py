#!/usr/bin/env python3
"""Calibrate the atomic lane's shared Coulomb scale against H / He+ / He."""

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

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, write_json  # noqa: E402
from scripts.atomic_observable_metrics import (  # noqa: E402
    ACTUALS_HARTREE,
    candidate_metrics,
)
from scripts.atomic_two_body_runtime import solve_two_electron_atomic_model  # noqa: E402


def _scan_grid(start: float, stop: float, step: float) -> list[float]:
    values: list[float] = []
    current = start
    while current <= stop + 0.5 * step:
        values.append(round(current, 12))
        current += step
    return values

def summarize_candidate(solution: dict[str, Any]) -> dict[str, Any]:
    metrics = candidate_metrics(solution)
    model = solution["model"]
    return {
        "parameters": {
            "reference_coupling": float(model["reference_coupling"]),
            "lattice_spacing": float(model["lattice_spacing"]),
            "nuclear_softening_radius": float(model["nuclear_softening_radius"]),
            "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
            "max_orbitals": int(model["max_orbitals"]),
        },
        "metrics": metrics,
        "spin_ground_sector": solution["two_electron"]["spin_ground_sector"],
        "helium_like_bound": bool(solution["two_electron"]["helium_like_bound"]),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--reference-couplings",
        type=float,
        nargs="*",
        default=_scan_grid(1.45, 1.80, 0.025),
        help="reference one-body couplings to scan",
    )
    parser.add_argument(
        "--softening-radii",
        type=float,
        nargs="*",
        default=_scan_grid(0.85, 1.10, 0.025),
        help="shared nuclear/e-e softening radii to scan",
    )
    parser.add_argument(
        "--lattice-spacing",
        type=float,
        default=1.0,
        help="physical lattice spacing used during the calibration sweep",
    )
    parser.add_argument(
        "--scan-max-orbitals",
        type=int,
        default=12,
        help="reduced basis size used during the coarse calibration scan",
    )
    parser.add_argument(
        "--final-max-orbitals",
        type=int,
        default=16,
        help="reduced basis size used to recompute the selected candidate",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_coulomb_calibration.json",
        help="machine-readable calibration output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    scan_rows: list[dict[str, Any]] = []
    best_summary: dict[str, Any] | None = None
    best_params: tuple[float, float] | None = None

    couplings = [float(value) for value in args.reference_couplings]
    softening_radii = [float(value) for value in args.softening_radii]
    total_points = len(couplings) * len(softening_radii)
    current_index = 0

    for reference_coupling in couplings:
        for softening_radius in softening_radii:
            current_index += 1
            scan_started = time.perf_counter()
            solution = solve_two_electron_atomic_model(
                reference_coupling=reference_coupling,
                lattice_spacing=float(args.lattice_spacing),
                nuclear_softening_radius=softening_radius,
                repulsion_softening_radius=softening_radius,
                max_orbitals=int(args.scan_max_orbitals),
                basis_sweep=(int(args.scan_max_orbitals),),
            )
            summary = summarize_candidate(solution)
            summary["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            scan_rows.append(summary)
            print(
                f"[{current_index}/{total_points}] "
                f"g={reference_coupling:.3f} "
                f"r0={softening_radius:.3f} "
                f"full_rms={summary['metrics']['scores']['full_rms_relative_error']:.4f} "
                f"He={summary['metrics']['model_observables']['helium_ground_magnitude']:.6f} "
                f"I={summary['metrics']['model_observables']['helium_ionization_energy']:.6f}",
                flush=True,
            )
            if best_summary is None or (
                summary["metrics"]["scores"]["full_rms_relative_error"],
                summary["metrics"]["scores"]["max_relative_error"],
                summary["metrics"]["scores"]["one_body_rms_relative_error"],
            ) < (
                best_summary["metrics"]["scores"]["full_rms_relative_error"],
                best_summary["metrics"]["scores"]["max_relative_error"],
                best_summary["metrics"]["scores"]["one_body_rms_relative_error"],
            ):
                best_summary = summary
                best_params = (reference_coupling, softening_radius)

    assert best_summary is not None and best_params is not None
    best_reference_coupling, best_softening_radius = best_params
    selected_solution = solve_two_electron_atomic_model(
        reference_coupling=best_reference_coupling,
        lattice_spacing=float(args.lattice_spacing),
        nuclear_softening_radius=best_softening_radius,
        repulsion_softening_radius=best_softening_radius,
        max_orbitals=int(args.final_max_orbitals),
        basis_sweep=tuple(
            size
            for size in (4, 6, 8, 10, 12, 14, int(args.final_max_orbitals))
            if size <= int(args.final_max_orbitals)
        ),
    )
    selected_summary = summarize_candidate(selected_solution)

    top_candidates = sorted(
        scan_rows,
        key=lambda row: (
            row["metrics"]["scores"]["full_rms_relative_error"],
            row["metrics"]["scores"]["max_relative_error"],
            row["metrics"]["scores"]["one_body_rms_relative_error"],
        ),
    )[:15]

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "actuals_hartree": ACTUALS_HARTREE,
        "scan_configuration": {
            "reference_couplings": couplings,
            "softening_radii": softening_radii,
            "lattice_spacing": float(args.lattice_spacing),
            "scan_max_orbitals": int(args.scan_max_orbitals),
            "final_max_orbitals": int(args.final_max_orbitals),
        },
        "best_scan_candidate": best_summary,
        "selected_final_candidate": selected_summary,
        "selected_solution": selected_solution,
        "top_candidates": top_candidates,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Coulomb Calibration")
    print("==========================")
    print(
        f"- Selected reference coupling: {best_reference_coupling:.6f}."
    )
    print(
        f"- Selected shared softening radius: {best_softening_radius:.6f}."
    )
    print(
        f"- Final full RMS relative error: "
        f"{selected_summary['metrics']['scores']['full_rms_relative_error']:.4f}."
    )
    print(
        f"- Final He singlet: "
        f"{selected_summary['metrics']['model_observables']['helium_ground_magnitude']:.6f}, "
        f"ionization: "
        f"{selected_summary['metrics']['model_observables']['helium_ionization_energy']:.6f}."
    )
    print(f"- Wrote calibration output to {args.write_json}.")


if __name__ == "__main__":
    main()
