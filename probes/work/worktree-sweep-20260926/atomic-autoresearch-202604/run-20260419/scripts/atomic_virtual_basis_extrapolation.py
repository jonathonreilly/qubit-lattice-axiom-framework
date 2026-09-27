#!/usr/bin/env python3
"""Estimate the infinite-basis limit from a helium readout basis sweep."""

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
from scripts.atomic_observable_metrics import (  # noqa: E402
    ACTUALS_HARTREE,
    fit_inverse_basis_limit,
)


def _observable_summary(
    basis_rows: list[dict[str, Any]],
    *,
    readout_value: float,
    basis_key: str,
    actual_key: str,
) -> dict[str, Any] | None:
    fit = fit_inverse_basis_limit(basis_rows, key=basis_key)
    if fit is None:
        return None
    actual_value = float(ACTUALS_HARTREE[actual_key])
    fit["current_value"] = float(readout_value)
    fit["current_magnitude"] = abs(float(readout_value))
    fit["current_relative_error"] = abs(abs(float(readout_value)) / actual_value - 1.0)
    fit["limit_magnitude"] = abs(float(fit["fitted_limit"]))
    fit["limit_relative_error"] = abs(abs(float(fit["fitted_limit"])) / actual_value - 1.0)
    fit["actual_value"] = actual_value
    fit["projected_improvement_vs_current"] = (
        float(fit["current_relative_error"]) - float(fit["limit_relative_error"])
    )
    return fit


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
        help="helium readout JSON containing a basis sweep",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_virtual_basis_extrapolation.json",
        help="machine-readable extrapolation output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    readout_payload = read_json(args.readout_json)
    helium = readout_payload["helium_two_electron"]
    basis_rows = list(helium["basis_sweep"])

    observables = {
        "helium_ground_magnitude": _observable_summary(
            basis_rows,
            readout_value=float(helium["singlet_ground_energy"]),
            basis_key="singlet_ground_energy",
            actual_key="helium_ground_magnitude",
        ),
        "helium_triplet_magnitude": _observable_summary(
            basis_rows,
            readout_value=float(helium["triplet_ground_energy"]),
            basis_key="triplet_ground_energy",
            actual_key="helium_triplet_magnitude",
        ),
        "helium_ionization_energy": _observable_summary(
            basis_rows,
            readout_value=float(helium["ionization_energy"]),
            basis_key="ionization_energy",
            actual_key="helium_ionization_energy",
        ),
        "singlet_triplet_gap": _observable_summary(
            basis_rows,
            readout_value=float(helium["singlet_triplet_gap"]),
            basis_key="singlet_triplet_gap",
            actual_key="singlet_triplet_gap",
        ),
    }

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_readout_json": str(args.readout_json),
        "spatial_orbital_count": int(helium["spatial_orbital_count"]),
        "negative_orbital_count": int(helium["negative_orbital_count"]),
        "virtual_orbital_count": int(helium["virtual_orbital_count"]),
        "observables": observables,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Virtual-Basis Extrapolation")
    print("==================================")
    for observable_name, summary in observables.items():
        assert summary is not None
        print(
            f"- {observable_name}: "
            f"current_rel={summary['current_relative_error']:.4%} "
            f"limit_rel={summary['limit_relative_error']:.4%} "
            f"remaining={summary['remaining_to_limit']:+.6e}."
        )
    print(f"- Wrote extrapolation report to {args.write_json}.")


if __name__ == "__main__":
    main()
