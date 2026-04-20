#!/usr/bin/env python3
"""Canonical readout for an accepted correlated atomic-lane candidate."""

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
    helium_readout_metrics,
)


def _selected_candidate(payload: dict[str, Any]) -> tuple[dict[str, Any], str]:
    if "accepted_candidate" in payload and payload["accepted_candidate"] is not None:
        return dict(payload["accepted_candidate"]), "accepted_candidate"
    if "selected_final_candidate" in payload and payload["selected_final_candidate"] is not None:
        return dict(payload["selected_final_candidate"]), "selected_final_candidate"
    if "best_by_full_rms" in payload and payload["best_by_full_rms"] is not None:
        return dict(payload["best_by_full_rms"]), "best_by_full_rms"
    raise KeyError(
        "input JSON does not contain an accepted, selected, or best-by-full-rms candidate"
    )


def _basis_tail_delta(rows: list[dict[str, Any]], key: str) -> float | None:
    usable = [row for row in rows if row.get(key) is not None]
    if len(usable) < 2:
        return None
    return float(usable[-1][key] - usable[-2][key])


def _basis_extrapolation(rows: list[dict[str, Any]]) -> dict[str, Any]:
    mapping = {
        "singlet_ground_energy": "helium_ground_magnitude",
        "triplet_ground_energy": "helium_triplet_magnitude",
        "ionization_energy": "helium_ionization_energy",
        "singlet_triplet_gap": "singlet_triplet_gap",
    }
    output: dict[str, Any] = {}
    for basis_key, actual_key in mapping.items():
        fit = fit_inverse_basis_limit(rows, key=basis_key)
        if fit is None:
            output[basis_key] = None
            continue
        actual_value = float(ACTUALS_HARTREE[actual_key])
        fit["limit_magnitude"] = abs(float(fit["fitted_limit"]))
        fit["limit_relative_error"] = abs(
            abs(float(fit["fitted_limit"])) / actual_value - 1.0
        )
        output[basis_key] = fit
    return output


def _candidate_type(model: dict[str, Any]) -> str:
    if "pair_correction_profile" in model:
        return "finite_range_pair"
    if (
        "shell_projector_ground_excited_strength" in model
        or "shell_projector_excited_excited_strength" in model
        or "shell_projector_ground_ground_strength" in model
    ):
        return "shell_projector"
    if "contact_correction_strength" in model:
        return "contact_correction"
    return "correlated_candidate"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_selected.json",
        help="JSON containing an accepted correlated candidate",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_readout.json",
        help="canonical correlated readout output path",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    payload = read_json(args.candidate_json)
    candidate, selection_source = _selected_candidate(payload)
    solution = candidate["solution"]
    readout_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_candidate_json": str(args.candidate_json),
        "selection_source": selection_source,
        "candidate_type": _candidate_type(solution["model"]),
        "accepted_candidate": candidate,
        "actuals_hartree": ACTUALS_HARTREE,
        "accuracy_metrics": None,
        "basis_tail_delta": {
            "singlet_ground_energy": _basis_tail_delta(
                solution["two_electron"]["basis_sweep"], "singlet_ground_energy"
            ),
            "triplet_ground_energy": _basis_tail_delta(
                solution["two_electron"]["basis_sweep"], "triplet_ground_energy"
            ),
            "ionization_energy": _basis_tail_delta(
                solution["two_electron"]["basis_sweep"], "ionization_energy"
            ),
        },
        "basis_extrapolation": _basis_extrapolation(solution["two_electron"]["basis_sweep"]),
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    synthetic_readout = {
        "helium_two_electron": {
            "hydrogen_ground_energy": solution["hydrogen_reference"]["ground_energy"],
            "helium_ion_ground_energy": solution["helium_ion_reference"]["ground_energy"],
            "singlet_ground_energy": solution["two_electron"]["singlet"]["ground_energy"],
            "triplet_ground_energy": solution["two_electron"]["triplet"]["ground_energy"],
            "ionization_energy": solution["two_electron"]["ionization_energy"],
            "singlet_triplet_gap": solution["two_electron"]["singlet_triplet_gap"],
        }
    }
    readout_payload["accuracy_metrics"] = helium_readout_metrics(synthetic_readout)
    write_json(args.write_json, readout_payload)

    print()
    print("Atomic Correlated Readout")
    print("=========================")
    print(
        f"- Candidate type: {readout_payload['candidate_type']} "
        f"full RMS={readout_payload['accuracy_metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote correlated readout to {args.write_json}.")


if __name__ == "__main__":
    main()
