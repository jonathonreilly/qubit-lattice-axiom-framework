#!/usr/bin/env python3
"""Canonical readout for the shell-projector larger-continuum phase."""

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


def _continuum_limit_readout(
    continuum_model_observables: dict[str, float],
    *,
    spatial_orbital_count: int,
) -> dict[str, object]:
    return {
        "helium_two_electron": {
            "hydrogen_ground_energy": -float(
                continuum_model_observables["hydrogen_ground_magnitude"]
            ),
            "helium_ion_ground_energy": -float(
                continuum_model_observables["helium_ion_ground_magnitude"]
            ),
            "singlet_ground_energy": -float(
                continuum_model_observables["helium_ground_magnitude"]
            ),
            "triplet_ground_energy": -float(
                continuum_model_observables["helium_triplet_magnitude"]
            ),
            "ionization_energy": float(
                continuum_model_observables["helium_ionization_energy"]
            ),
            "singlet_triplet_gap": float(
                continuum_model_observables["singlet_triplet_gap"]
            ),
            "spatial_orbital_count": int(spatial_orbital_count),
        }
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--sweep-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_sweep.json",
    )
    parser.add_argument(
        "--extrapolation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_extrapolation.json",
    )
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_shell_projector_continuum_readout.json",
    )
    args = parser.parse_args()

    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    sweep_payload = read_json(args.sweep_json)
    extrapolation_payload = read_json(args.extrapolation_json)
    live_candidate = sweep_payload.get("accepted_candidate") or sweep_payload["best_by_full_rms"]
    live_spacing = float(live_candidate["parameters"]["lattice_spacing"])
    live_sizes = list(live_candidate["parameters"]["active_sizes"])
    spatial_orbital_count = int(live_candidate["solution"]["two_electron"]["spatial_orbital_count"])
    continuum_limit_readout = _continuum_limit_readout(
        extrapolation_payload["continuum_limit_model_observables"],
        spatial_orbital_count=spatial_orbital_count,
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_sweep_json": str(args.sweep_json),
        "source_extrapolation_json": str(args.extrapolation_json),
        "selected_live_candidate": live_candidate,
        "selected_live_spacing": live_spacing,
        "selected_live_sizes": live_sizes,
        "live_accuracy_metrics": live_candidate["metrics"],
        "continuum_limit_readout": continuum_limit_readout,
        "continuum_limit_accuracy_metrics": extrapolation_payload["continuum_limit_metrics"],
        "observable_fits": extrapolation_payload["observable_fits"],
        "projected_improvement_vs_live": extrapolation_payload["projected_improvement_vs_live"],
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Shell-Projector Continuum Readout")
    print("========================================")
    print(
        f"- Selected live spacing: a={live_spacing:.4f} sizes={tuple(live_sizes)} "
        f"full={live_candidate['metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(
        f"- Continuum-limit full RMS: "
        f"{output_payload['continuum_limit_accuracy_metrics']['scores']['full_rms_relative_error']:.6f}."
    )
    print(f"- Wrote readout to {args.write_json}.")


if __name__ == "__main__":
    main()
