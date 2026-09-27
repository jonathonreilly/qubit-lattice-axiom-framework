#!/usr/bin/env python3
"""Compare bound-shell occupancy structure between the contact baseline and shell-projector candidate."""

from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
import sys
import time

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import DEFAULT_OUTPUT_ROOT, read_json, write_json  # noqa: E402


def _selected_solution(payload: dict) -> dict:
    if payload.get("accepted_candidate") is not None:
        return payload["accepted_candidate"]["solution"]
    if payload.get("best_by_full_rms") is not None:
        return payload["best_by_full_rms"]["solution"]
    if payload.get("accepted_candidate") is not None and "solution" in payload["accepted_candidate"]:
        return payload["accepted_candidate"]["solution"]
    raise KeyError("unable to locate solution payload")


def _bound_shell_summary(solution: dict) -> dict:
    helium = solution["two_electron"]
    negative_orbital_count = int(solution["helium_ion_reference"]["n_negative_selected"])

    def summarize(occupancies: list[float]) -> dict[str, float]:
        ground = float(occupancies[0]) if occupancies else 0.0
        excited_bound = float(sum(occupancies[1:negative_orbital_count]))
        virtual = float(sum(occupancies[negative_orbital_count:]))
        return {
            "ground_occupancy": ground,
            "excited_bound_occupancy": excited_bound,
            "virtual_occupancy": virtual,
        }

    return {
        "negative_orbital_count": negative_orbital_count,
        "singlet": summarize(helium["singlet"]["orbital_occupancies"]),
        "triplet": summarize(helium["triplet"]["orbital_occupancies"]),
        "singlet_dominant_configurations": helium["singlet"]["dominant_configurations"][:6],
        "triplet_dominant_configurations": helium["triplet"]["dominant_configurations"][:6],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--baseline-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_selected.json",
    )
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_projector_scan.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_bound_shell_diagnostics.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    baseline_solution = _selected_solution(read_json(args.baseline_json))
    candidate_solution = _selected_solution(read_json(args.candidate_json))
    baseline_summary = _bound_shell_summary(baseline_solution)
    candidate_summary = _bound_shell_summary(candidate_solution)

    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "baseline_source_json": str(args.baseline_json),
        "candidate_source_json": str(args.candidate_json),
        "baseline": baseline_summary,
        "candidate": candidate_summary,
        "delta": {
            "singlet_excited_bound_shift": (
                candidate_summary["singlet"]["excited_bound_occupancy"]
                - baseline_summary["singlet"]["excited_bound_occupancy"]
            ),
            "triplet_excited_bound_shift": (
                candidate_summary["triplet"]["excited_bound_occupancy"]
                - baseline_summary["triplet"]["excited_bound_occupancy"]
            ),
            "singlet_ground_shift": (
                candidate_summary["singlet"]["ground_occupancy"]
                - baseline_summary["singlet"]["ground_occupancy"]
            ),
            "triplet_ground_shift": (
                candidate_summary["triplet"]["ground_occupancy"]
                - baseline_summary["triplet"]["ground_occupancy"]
            ),
        },
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Bound-Shell Diagnostics")
    print("==============================")
    print(
        f"- Triplet excited-bound shift: "
        f"{output_payload['delta']['triplet_excited_bound_shift']:+.6f}."
    )
    print(
        f"- Singlet excited-bound shift: "
        f"{output_payload['delta']['singlet_excited_bound_shift']:+.6f}."
    )
    print(f"- Wrote diagnostics to {args.write_json}.")


if __name__ == "__main__":
    main()
