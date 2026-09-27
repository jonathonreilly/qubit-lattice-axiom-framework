#!/usr/bin/env python3
"""Shared observable metrics for the retained atomic lane."""

from __future__ import annotations

from math import sqrt
from typing import Any

import numpy as np

ACTUALS_HARTREE = {
    "hydrogen_ground_magnitude": 0.5,
    "helium_ion_ground_magnitude": 2.0,
    "helium_ground_magnitude": 2.9037243770341196,
    "helium_ionization_energy": 0.9037243770341196,
    "helium_triplet_magnitude": 2.1752293782367913,
    "singlet_triplet_gap": 0.7284949987973282,
}

ONE_BODY_OBSERVABLES = (
    "hydrogen_ground_magnitude",
    "helium_ion_ground_magnitude",
)

HELIUM_OBSERVABLES = (
    "helium_ground_magnitude",
    "helium_ionization_energy",
    "helium_triplet_magnitude",
    "singlet_triplet_gap",
)


def relative_error(model_value: float, actual_value: float) -> float:
    return abs(model_value / actual_value - 1.0)


def rms(values: list[float]) -> float:
    return sqrt(sum(value * value for value in values) / len(values))


def model_observables_from_solution(solution: dict[str, Any]) -> dict[str, float]:
    return {
        "hydrogen_ground_magnitude": abs(float(solution["hydrogen_reference"]["ground_energy"])),
        "helium_ion_ground_magnitude": abs(
            float(solution["helium_ion_reference"]["ground_energy"])
        ),
        "helium_ground_magnitude": abs(
            float(solution["two_electron"]["singlet"]["ground_energy"])
        ),
        "helium_ionization_energy": float(solution["two_electron"]["ionization_energy"]),
        "helium_triplet_magnitude": abs(
            float(solution["two_electron"]["triplet"]["ground_energy"])
        ),
        "singlet_triplet_gap": float(solution["two_electron"]["singlet_triplet_gap"]),
    }


def model_observables_from_readout(readout_payload: dict[str, Any]) -> dict[str, float]:
    helium = readout_payload["helium_two_electron"]
    return {
        "hydrogen_ground_magnitude": abs(float(helium["hydrogen_ground_energy"])),
        "helium_ion_ground_magnitude": abs(float(helium["helium_ion_ground_energy"])),
        "helium_ground_magnitude": abs(float(helium["singlet_ground_energy"])),
        "helium_ionization_energy": float(helium["ionization_energy"]),
        "helium_triplet_magnitude": abs(float(helium["triplet_ground_energy"])),
        "singlet_triplet_gap": float(helium["singlet_triplet_gap"]),
    }


def gap_rows_from_model_observables(
    model_observables: dict[str, float],
) -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for observable_name, actual_value in ACTUALS_HARTREE.items():
        model_value = float(model_observables[observable_name])
        delta = model_value - float(actual_value)
        rows.append(
            {
                "observable": observable_name,
                "model_value": model_value,
                "actual_value": float(actual_value),
                "absolute_delta": delta,
                "relative_error": relative_error(model_value, float(actual_value)),
            }
        )
    return rows


def score_dict_from_gap_rows(
    rows: list[dict[str, float | str]],
) -> dict[str, float]:
    relative_errors = {
        str(row["observable"]): float(row["relative_error"])
        for row in rows
    }
    one_body = rms([relative_errors[name] for name in ONE_BODY_OBSERVABLES])
    helium = rms([relative_errors[name] for name in HELIUM_OBSERVABLES])
    full = rms(list(relative_errors.values()))
    return {
        "one_body_rms_relative_error": one_body,
        "helium_rms_relative_error": helium,
        "full_rms_relative_error": full,
        "max_relative_error": max(relative_errors.values()),
    }


def candidate_metrics(solution: dict[str, Any]) -> dict[str, Any]:
    model_observables = model_observables_from_solution(solution)
    return metrics_from_model_observables(model_observables)


def metrics_from_model_observables(
    model_observables: dict[str, float],
) -> dict[str, Any]:
    gap_rows = gap_rows_from_model_observables(model_observables)
    relative_errors = {
        str(row["observable"]).replace("_magnitude", ""): float(row["relative_error"])
        for row in gap_rows
    }
    if "helium_ionization_energy" in relative_errors:
        relative_errors["helium_ionization"] = float(
            relative_errors["helium_ionization_energy"]
        )
    return {
        "model_observables": model_observables,
        "gap_rows": gap_rows,
        "relative_errors": relative_errors,
        "scores": score_dict_from_gap_rows(gap_rows),
    }


def helium_readout_metrics(readout_payload: dict[str, Any]) -> dict[str, Any]:
    model_observables = model_observables_from_readout(readout_payload)
    return metrics_from_model_observables(model_observables)


def one_body_pair_observables(
    hydrogen_result: dict[str, Any],
    helium_ion_result: dict[str, Any],
) -> dict[str, float]:
    return {
        "hydrogen_ground_magnitude": abs(float(hydrogen_result["ground_energy"])),
        "helium_ion_ground_magnitude": abs(float(helium_ion_result["ground_energy"])),
    }


def one_body_gap_rows(
    hydrogen_result: dict[str, Any],
    helium_ion_result: dict[str, Any],
) -> list[dict[str, float | str]]:
    model_observables = one_body_pair_observables(
        hydrogen_result,
        helium_ion_result,
    )
    rows: list[dict[str, float | str]] = []
    for observable_name in ONE_BODY_OBSERVABLES:
        actual_value = float(ACTUALS_HARTREE[observable_name])
        model_value = float(model_observables[observable_name])
        delta = model_value - actual_value
        rows.append(
            {
                "observable": observable_name,
                "model_value": model_value,
                "actual_value": actual_value,
                "absolute_delta": delta,
                "relative_error": relative_error(model_value, actual_value),
            }
        )
    return rows


def one_body_pair_metrics(
    hydrogen_result: dict[str, Any],
    helium_ion_result: dict[str, Any],
) -> dict[str, Any]:
    gap_rows = one_body_gap_rows(hydrogen_result, helium_ion_result)
    relative_errors = {
        str(row["observable"]).replace("_magnitude", ""): float(row["relative_error"])
        for row in gap_rows
    }
    return {
        "model_observables": one_body_pair_observables(
            hydrogen_result,
            helium_ion_result,
        ),
        "gap_rows": gap_rows,
        "relative_errors": relative_errors,
        "scores": {
            "one_body_rms_relative_error": rms(
                [float(row["relative_error"]) for row in gap_rows]
            ),
            "max_relative_error": max(
                float(row["relative_error"]) for row in gap_rows
            ),
        },
    }


def fit_inverse_basis_limit(
    basis_rows: list[dict[str, Any]],
    *,
    key: str,
    tail_points: int = 4,
) -> dict[str, Any] | None:
    usable = [
        row
        for row in basis_rows
        if row.get(key) is not None and row.get("spatial_orbital_count") is not None
    ]
    if len(usable) < max(3, tail_points):
        return None
    tail = usable[-tail_points:]
    sizes = np.asarray(
        [float(row["spatial_orbital_count"]) for row in tail],
        dtype=float,
    )
    values = np.asarray([float(row[key]) for row in tail], dtype=float)
    design = np.column_stack([np.ones_like(sizes), 1.0 / sizes])
    coeffs, *_ = np.linalg.lstsq(design, values, rcond=None)
    predicted = design @ coeffs
    fitted_limit = float(coeffs[0])
    rmse = float(np.sqrt(np.mean((values - predicted) ** 2)))
    last_value = float(values[-1])
    tail_deltas = [
        float(right - left)
        for left, right in zip(values[:-1], values[1:], strict=False)
    ]
    monotone = all(delta <= 0.0 for delta in tail_deltas) or all(
        delta >= 0.0 for delta in tail_deltas
    )
    return {
        "observable_key": key,
        "tail_point_count": len(tail),
        "basis_sizes": [int(size) for size in sizes],
        "tail_values": [float(value) for value in values],
        "fitted_limit": fitted_limit,
        "last_value": last_value,
        "remaining_to_limit": float(fitted_limit - last_value),
        "tail_fit_rmse": rmse,
        "tail_step_deltas": tail_deltas,
        "tail_is_monotone": bool(monotone),
    }
