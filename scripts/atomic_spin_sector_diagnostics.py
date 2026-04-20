#!/usr/bin/env python3
"""Summarize spin-sector separation in the retained-lane helium readout."""

from __future__ import annotations

import argparse
from datetime import datetime
from math import log10
from pathlib import Path
import sys
import time

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def _occupancy_cosine_similarity(left: list[float], right: list[float]) -> float:
    left_array = np.asarray(left, dtype=float)
    right_array = np.asarray(right, dtype=float)
    denom = float(np.linalg.norm(left_array) * np.linalg.norm(right_array))
    if denom == 0.0:
        return 0.0
    return float(np.dot(left_array, right_array) / denom)


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
        default=DEFAULT_OUTPUT_ROOT / "atomic_spin_sector_diagnostics.json",
        help="machine-readable spin diagnostic path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    readout_payload = read_json(args.readout_json)
    helium = readout_payload["helium_two_electron"]
    singlet_contact = float(helium["singlet_contact_probability"])
    triplet_contact = float(helium["triplet_contact_probability"])
    tiny = 1.0e-30

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_readout_json": str(args.readout_json),
        "spin_ground_sector": helium["spin_ground_sector"],
        "singlet_triplet_gap": float(helium["singlet_triplet_gap"]),
        "singlet_ionization_energy": float(helium["ionization_energy"]),
        "triplet_ionization_energy": float(helium["triplet_ionization_energy"]),
        "contact": {
            "singlet_probability": singlet_contact,
            "triplet_probability": triplet_contact,
            "suppression_factor_singlet_over_triplet": float(
                singlet_contact / max(triplet_contact, tiny)
            ),
            "triplet_contact_log10": float(log10(max(triplet_contact, tiny))),
        },
        "repulsion": {
            "singlet_energy": float(helium["singlet_repulsion_energy"]),
            "triplet_energy": float(helium["triplet_repulsion_energy"]),
            "triplet_over_singlet_ratio": float(
                helium["triplet_repulsion_energy"] / helium["singlet_repulsion_energy"]
            ),
        },
        "occupancy_comparison": {
            "cosine_similarity": _occupancy_cosine_similarity(
                helium["singlet_orbital_occupancies"],
                helium["triplet_orbital_occupancies"],
            ),
        },
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Spin-Sector Diagnostics")
    print("==============================")
    print(
        f"- Spin ground sector: {output_payload['spin_ground_sector']} "
        f"with gap {output_payload['singlet_triplet_gap']:.6f}."
    )
    print(
        f"- Triplet contact suppression log10: "
        f"{output_payload['contact']['triplet_contact_log10']:.2f}."
    )
    print(f"- Wrote spin diagnostics to {args.write_json}.")


if __name__ == "__main__":
    main()
