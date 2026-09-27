#!/usr/bin/env python3
"""Extrapolate one-body observables toward the continuum limit."""

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


def _fit_continuum_limit(
    rows: list[dict[str, Any]],
    *,
    observable_key: str,
    actual_key: str,
    power: int,
) -> dict[str, Any]:
    spacings = np.asarray(
        [float(row["parameters"]["lattice_spacing"]) for row in rows],
        dtype=float,
    )
    x = np.power(spacings, int(power))
    y = np.asarray(
        [float(row["metrics"]["model_observables"][observable_key]) for row in rows],
        dtype=float,
    )
    design = np.column_stack([np.ones_like(x), x])
    coeffs, *_ = np.linalg.lstsq(design, y, rcond=None)
    predicted = design @ coeffs
    limit_value = float(coeffs[0])
    actual_value = float(ACTUALS_HARTREE[actual_key])
    current_value = float(y[-1])
    current_relative_error = abs(current_value / actual_value - 1.0)
    limit_relative_error = abs(limit_value / actual_value - 1.0)
    spacing_deltas = [
        float(right - left)
        for left, right in zip(y[:-1], y[1:], strict=False)
    ]
    monotone = all(delta <= 0.0 for delta in spacing_deltas) or all(
        delta >= 0.0 for delta in spacing_deltas
    )
    return {
        "observable_key": observable_key,
        "fit_power": int(power),
        "spacings": [float(value) for value in spacings],
        "x_values": [float(value) for value in x],
        "y_values": [float(value) for value in y],
        "fitted_limit": limit_value,
        "current_value": current_value,
        "actual_value": actual_value,
        "current_relative_error": current_relative_error,
        "limit_relative_error": limit_relative_error,
        "projected_improvement_vs_current": (
            float(current_relative_error) - float(limit_relative_error)
        ),
        "fit_rmse": float(np.sqrt(np.mean((y - predicted) ** 2))),
        "spacing_step_deltas": spacing_deltas,
        "trend_is_monotone": bool(monotone),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--scan-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_spacing_scan.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_continuum_extrapolation.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    payload = read_json(args.scan_json)
    rows = sorted(
        payload["rows"],
        key=lambda row: float(row["parameters"]["lattice_spacing"]),
        reverse=True,
    )
    stencil = str(payload["scan_configuration"]["kinetic_stencil"])
    fit_power = 2 if stencil == "three_point" else 4
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_scan_json": str(args.scan_json),
        "fit_power": int(fit_power),
        "kinetic_stencil": stencil,
        "observables": {
            "hydrogen_ground_magnitude": _fit_continuum_limit(
                rows,
                observable_key="hydrogen_ground_magnitude",
                actual_key="hydrogen_ground_magnitude",
                power=fit_power,
            ),
            "helium_ion_ground_magnitude": _fit_continuum_limit(
                rows,
                observable_key="helium_ion_ground_magnitude",
                actual_key="helium_ion_ground_magnitude",
                power=fit_power,
            ),
        },
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic One-Body Continuum Extrapolation")
    print("=======================================")
    for observable_name, summary in output_payload["observables"].items():
        print(
            f"- {observable_name}: "
            f"current_rel={summary['current_relative_error']:.4%} "
            f"limit_rel={summary['limit_relative_error']:.4%}."
        )
    print(f"- Wrote extrapolation to {args.write_json}.")


if __name__ == "__main__":
    main()
