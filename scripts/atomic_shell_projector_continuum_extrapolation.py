#!/usr/bin/env python3
"""Fit shell-projector continuum trends from the larger-continuum sweep."""

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
from scripts.atomic_observable_metrics import (  # noqa: E402
    ACTUALS_HARTREE,
    metrics_from_model_observables,
)


def _fit_power(stencil: str) -> int:
    normalized = str(stencil).strip().lower()
    if normalized == "three_point":
        return 2
    if normalized == "five_point":
        return 4
    if normalized == "seven_point":
        return 6
    raise ValueError(f"unsupported stencil {stencil!r}")


def _fit_observable(
    rows: list[dict[str, Any]],
    *,
    observable_key: str,
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
    current_value = float(y[-1])
    limit_value = float(coeffs[0])
    actual_value = float(ACTUALS_HARTREE[observable_key])
    step_deltas = [
        float(right - left)
        for left, right in zip(y[:-1], y[1:], strict=False)
    ]
    monotone = all(delta <= 0.0 for delta in step_deltas) or all(
        delta >= 0.0 for delta in step_deltas
    )
    return {
        "observable_key": observable_key,
        "fit_power": int(fit_power),
        "spacings": [float(value) for value in spacings],
        "x_values": [float(value) for value in x],
        "y_values": [float(value) for value in y],
        "fitted_limit": limit_value,
        "current_value": current_value,
        "actual_value": actual_value,
        "current_relative_error": abs(current_value / actual_value - 1.0),
        "limit_relative_error": abs(limit_value / actual_value - 1.0),
        "projected_improvement_vs_current": abs(current_value / actual_value - 1.0)
        - abs(limit_value / actual_value - 1.0),
        "fit_rmse": float(np.sqrt(np.mean((y - predicted) ** 2))),
        "spacing_step_deltas": step_deltas,
        "trend_is_monotone": bool(monotone),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sweep-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_sweep.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_extrapolation.json",
    )
    args = parser.parse_args()

    payload = read_json(args.sweep_json)
    rows = list(payload["rows"])
    if len(rows) < 3:
        raise ValueError("continuum extrapolation requires at least three sweep rows")
    live_row = payload.get("accepted_candidate") or payload["best_by_full_rms"]
    stencil = str(live_row["solution"]["model"]["kinetic_stencil"])
    fit_power = _fit_power(stencil)
    observable_keys = (
        "hydrogen_ground_magnitude",
        "helium_ion_ground_magnitude",
        "helium_ground_magnitude",
        "helium_ionization_energy",
        "helium_triplet_magnitude",
        "singlet_triplet_gap",
    )

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    observable_fits = {
        key: _fit_observable(rows, observable_key=key, fit_power=fit_power)
        for key in observable_keys
    }
    continuum_model_observables = {
        key: float(summary["fitted_limit"])
        for key, summary in observable_fits.items()
    }
    continuum_metrics = metrics_from_model_observables(continuum_model_observables)
    live_metrics = dict(live_row["metrics"])
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_sweep_json": str(args.sweep_json),
        "fit_power": int(fit_power),
        "kinetic_stencil": stencil,
        "observable_fits": observable_fits,
        "best_live_candidate": live_row,
        "continuum_limit_model_observables": continuum_model_observables,
        "continuum_limit_metrics": continuum_metrics,
        "projected_improvement_vs_live": {
            "full_rms_relative_error": float(
                live_metrics["scores"]["full_rms_relative_error"]
                - continuum_metrics["scores"]["full_rms_relative_error"]
            ),
            "hydrogen_ground": float(
                live_metrics["relative_errors"]["hydrogen_ground"]
                - continuum_metrics["relative_errors"]["hydrogen_ground"]
            ),
            "helium_ion_ground": float(
                live_metrics["relative_errors"]["helium_ion_ground"]
                - continuum_metrics["relative_errors"]["helium_ion_ground"]
            ),
            "singlet_triplet_gap": float(
                live_metrics["relative_errors"]["singlet_triplet_gap"]
                - continuum_metrics["relative_errors"]["singlet_triplet_gap"]
            ),
        },
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell-Projector Continuum Extrapolation")
    print("==============================================")
    print(
        f"- Live full RMS: "
        f"{live_metrics['scores']['full_rms_relative_error']:.6f}."
    )
    print(
        f"- Continuum-limit full RMS: "
        f"{continuum_metrics['scores']['full_rms_relative_error']:.6f}."
    )
    print(
        f"- Hydrogen live -> limit: "
        f"{live_metrics['relative_errors']['hydrogen_ground']:.4%} -> "
        f"{continuum_metrics['relative_errors']['hydrogen_ground']:.4%}."
    )
    print(f"- Wrote extrapolation to {args.write_json}.")


if __name__ == "__main__":
    main()
