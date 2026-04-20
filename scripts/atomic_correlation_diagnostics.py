#!/usr/bin/env python3
"""Summarize correlation structure in the retained-lane helium readout."""

from __future__ import annotations

import argparse
from datetime import datetime
from math import log
from pathlib import Path
import sys
import time

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def _normalized_entropy(occupancies: list[float]) -> float:
    values = np.asarray(occupancies, dtype=float)
    total = float(values.sum())
    if total <= 0.0 or len(values) <= 1:
        return 0.0
    probs = values / total
    usable = probs[probs > 0.0]
    entropy = -float(np.sum(usable * np.log(usable)))
    return float(entropy / log(len(values)))


def _effective_orbital_count(occupancies: list[float]) -> float:
    values = np.asarray(occupancies, dtype=float)
    total = float(values.sum())
    if total <= 0.0:
        return 0.0
    return float(total * total / np.sum(values * values))


def _sector_summary(
    occupancies: list[float],
    dominant_configurations: list[dict[str, float]],
    *,
    negative_orbital_count: int,
) -> dict[str, float]:
    values = np.asarray(occupancies, dtype=float)
    dominant_weight = float(dominant_configurations[0]["weight"]) if dominant_configurations else 0.0
    return {
        "ground_orbital_occupancy": float(values[0]) if len(values) else 0.0,
        "excited_bound_occupancy": float(values[1:negative_orbital_count].sum()),
        "virtual_occupancy": float(values[negative_orbital_count:].sum()),
        "dominant_configuration_weight": dominant_weight,
        "residual_correlation_weight": float(1.0 - dominant_weight),
        "normalized_occupancy_entropy": _normalized_entropy(occupancies),
        "effective_orbital_count": _effective_orbital_count(occupancies),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
        help="helium readout JSON to analyze",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlation_diagnostics.json",
        help="machine-readable correlation diagnostic path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    readout_payload = read_json(args.readout_json)
    helium = readout_payload["helium_two_electron"]
    negative_orbital_count = int(helium["negative_orbital_count"])
    singlet = _sector_summary(
        helium["singlet_orbital_occupancies"],
        helium["singlet_dominant_configurations"],
        negative_orbital_count=negative_orbital_count,
    )
    triplet = _sector_summary(
        helium["triplet_orbital_occupancies"],
        helium["triplet_dominant_configurations"],
        negative_orbital_count=negative_orbital_count,
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_readout_json": str(args.readout_json),
        "negative_orbital_count": negative_orbital_count,
        "virtual_orbital_count": int(helium["virtual_orbital_count"]),
        "singlet": singlet,
        "triplet": triplet,
        "comparison": {
            "virtual_occupancy_gain_triplet_minus_singlet": (
                float(triplet["virtual_occupancy"]) - float(singlet["virtual_occupancy"])
            ),
            "residual_correlation_gain_triplet_minus_singlet": (
                float(triplet["residual_correlation_weight"])
                - float(singlet["residual_correlation_weight"])
            ),
            "entropy_gap_triplet_minus_singlet": (
                float(triplet["normalized_occupancy_entropy"])
                - float(singlet["normalized_occupancy_entropy"])
            ),
        },
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Correlation Diagnostics")
    print("==============================")
    print(
        f"- Singlet residual correlation weight: "
        f"{singlet['residual_correlation_weight']:.4%}."
    )
    print(
        f"- Singlet virtual occupancy: "
        f"{singlet['virtual_occupancy']:.6f}; "
        f"triplet virtual occupancy: {triplet['virtual_occupancy']:.6f}."
    )
    print(f"- Wrote correlation diagnostics to {args.write_json}.")


if __name__ == "__main__":
    main()
