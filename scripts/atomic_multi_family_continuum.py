#!/usr/bin/env python3
"""Run fixed-box continuum screening on the calibrated hydrogen-priority families."""

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

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402
from scripts.atomic_observable_metrics import ACTUALS_HARTREE  # noqa: E402
from scripts.atomic_one_body_runtime import benchmark_one_body_candidate  # noqa: E402


def _fit_limit(
    rows: list[dict[str, Any]],
    *,
    observable_key: str,
    actual_key: str,
    fit_power: int,
) -> dict[str, Any]:
    sorted_rows = sorted(
        rows,
        key=lambda row: float(row["parameters"]["lattice_spacing"]),
        reverse=True,
    )
    spacings = np.asarray(
        [float(row["parameters"]["lattice_spacing"]) for row in sorted_rows],
        dtype=float,
    )
    x = np.power(spacings, int(fit_power))
    y = np.asarray(
        [float(row["metrics"]["model_observables"][observable_key]) for row in sorted_rows],
        dtype=float,
    )
    design = np.column_stack([np.ones_like(x), x])
    coeffs, *_ = np.linalg.lstsq(design, y, rcond=None)
    predicted = design @ coeffs
    limit_value = float(coeffs[0])
    actual_value = float(ACTUALS_HARTREE[actual_key])
    current_value = float(y[-1])
    return {
        "observable_key": observable_key,
        "fit_power": int(fit_power),
        "spacings": [float(value) for value in spacings],
        "values": [float(value) for value in y],
        "fitted_limit": limit_value,
        "actual_value": actual_value,
        "current_value": current_value,
        "current_relative_error": abs(current_value / actual_value - 1.0),
        "limit_relative_error": abs(limit_value / actual_value - 1.0),
        "fit_rmse": float(np.sqrt(np.mean((y - predicted) ** 2))),
    }


def _fit_power(stencil: str) -> int:
    if stencil == "three_point":
        return 2
    if stencil == "five_point":
        return 4
    if stencil == "seven_point":
        return 6
    raise ValueError(f"unsupported stencil {stencil!r}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--calibration-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_multi_family_coupling_calibration.json",
    )
    parser.add_argument(
        "--baseline-continuum-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_continuum_extrapolation_calibrated.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout_contact.json",
    )
    parser.add_argument(
        "--lattice-spacings",
        type=float,
        nargs="*",
        default=(1.0, 0.8, 2.0 / 3.0, 4.0 / 7.0),
    )
    parser.add_argument("--helium-limit-guard-band", type=float, default=0.02)
    parser.add_argument("--family-limit", type=int, default=3)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_multi_family_continuum.json",
    )
    args = parser.parse_args()

    calibration_payload = read_json(args.calibration_json)
    baseline_continuum = read_json(args.baseline_continuum_json)
    baseline_readout = read_json(args.baseline_readout_json)
    baseline_hydrogen_limit = float(
        baseline_continuum["observables"]["hydrogen_ground_magnitude"]["limit_relative_error"]
    )
    baseline_helium_ion_error = float(
        baseline_readout["accuracy_metrics"]["relative_errors"]["helium_ion_ground"]
    )
    source_candidates = list(calibration_payload["selected_final_candidates"])[: int(args.family_limit)]

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    family_rows = []
    total_points = len(source_candidates) * len(args.lattice_spacings)
    current_index = 0
    for family_index, candidate in enumerate(source_candidates, start=1):
        parameters = candidate["parameters"]
        rows = []
        for lattice_spacing in args.lattice_spacings:
            current_index += 1
            scan_started = time.perf_counter()
            benchmark = benchmark_one_body_candidate(
                dimension=int(parameters["dimension"]),
                reference_coupling=float(parameters["reference_coupling"]),
                nuclear_charge=float(parameters["nuclear_charge"]),
                lattice_spacing=float(lattice_spacing),
                softening_multiplier=float(parameters["softening_multiplier"]),
                nuclear_profile=str(parameters["nuclear_profile"]),
                nuclear_quadrature_order=int(parameters["nuclear_quadrature_order"]),
                nuclear_counterterm_strength=float(
                    parameters["nuclear_counterterm_strength"]
                ),
                nuclear_counterterm_radius=parameters["nuclear_counterterm_radius"],
                kinetic_stencil=str(parameters["kinetic_stencil"]),
                max_orbitals=int(parameters["max_orbitals"]),
                n_eig=int(parameters["n_eig"]),
                fixed_physical_box=True,
                reference_spacing=float(parameters["reference_spacing"]),
                reference_sizes=(
                    tuple(int(size) for size in parameters["reference_sizes"])
                    if parameters["reference_sizes"] is not None
                    else None
                ),
            )
            benchmark["elapsed_seconds"] = round(time.perf_counter() - scan_started, 6)
            rows.append(benchmark)
            print(
                f"[{current_index}/{total_points}] family={family_index} "
                f"a={float(lattice_spacing):.4f} "
                f"H={benchmark['metrics']['relative_errors']['hydrogen_ground']:.4%} "
                f"He+={benchmark['metrics']['relative_errors']['helium_ion_ground']:.4%} "
                f"rms={benchmark['metrics']['scores']['one_body_rms_relative_error']:.6f}",
                flush=True,
            )

        fit_power = _fit_power(str(parameters["kinetic_stencil"]))
        hydrogen_fit = _fit_limit(
            rows,
            observable_key="hydrogen_ground_magnitude",
            actual_key="hydrogen_ground_magnitude",
            fit_power=fit_power,
        )
        helium_fit = _fit_limit(
            rows,
            observable_key="helium_ion_ground_magnitude",
            actual_key="helium_ion_ground_magnitude",
            fit_power=fit_power,
        )
        survives = bool(
            hydrogen_fit["limit_relative_error"] < baseline_hydrogen_limit
            and helium_fit["limit_relative_error"]
            <= baseline_helium_ion_error + float(args.helium_limit_guard_band)
        )
        family_rows.append(
            {
                "candidate": candidate,
                "rows": rows,
                "fit_power": fit_power,
                "observables": {
                    "hydrogen_ground_magnitude": hydrogen_fit,
                    "helium_ion_ground_magnitude": helium_fit,
                },
                "survives_continuum_screen": survives,
            }
        )

    surviving_rows = [row for row in family_rows if row["survives_continuum_screen"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_calibration_json": str(args.calibration_json),
        "baseline_hydrogen_limit_relative_error": baseline_hydrogen_limit,
        "family_rows": family_rows,
        "surviving_candidates": surviving_rows,
        "best_hydrogen_limit_candidate": min(
            family_rows,
            key=lambda row: (
                float(row["observables"]["hydrogen_ground_magnitude"]["limit_relative_error"]),
                float(row["observables"]["helium_ion_ground_magnitude"]["limit_relative_error"]),
            ),
        ),
        "best_surviving_candidate": (
            min(
                surviving_rows,
                key=lambda row: (
                    float(row["observables"]["hydrogen_ground_magnitude"]["limit_relative_error"]),
                    float(row["candidate"]["metrics"]["scores"]["one_body_rms_relative_error"]),
                ),
            )
            if surviving_rows
            else None
        ),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Multi-Family Continuum Screen")
    print("====================================")
    print(f"- Surviving families: {len(surviving_rows)}.")
    print(
        f"- Best hydrogen-limit family: "
        f"{output_payload['best_hydrogen_limit_candidate']['candidate']['parameters']['kinetic_stencil']} "
        f"{output_payload['best_hydrogen_limit_candidate']['candidate']['parameters']['nuclear_profile']} "
        f"H_limit="
        f"{output_payload['best_hydrogen_limit_candidate']['observables']['hydrogen_ground_magnitude']['limit_relative_error']:.4%}."
    )
    print(f"- Wrote continuum screen to {args.write_json}.")


if __name__ == "__main__":
    main()
