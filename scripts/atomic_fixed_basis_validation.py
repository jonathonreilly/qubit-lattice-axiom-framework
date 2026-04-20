#!/usr/bin/env python3
"""Push a promoted one-body candidate through the fixed 64-orbital helium basis."""

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
    candidate_metrics,
    helium_readout_metrics,
)
from scripts.atomic_two_body_runtime import solve_two_electron_atomic_model  # noqa: E402


def _candidate_parameters(payload: dict[str, Any]) -> dict[str, Any]:
    candidate = payload.get("selected_final_candidate")
    if candidate is None:
        candidate = payload.get("promoted_candidate")
    if candidate is None:
        candidate = payload["best_by_one_body_rms"]
    return dict(candidate["parameters"])


def _acceptance_summary(
    *,
    candidate_metrics_payload: dict[str, Any],
    baseline_metrics_payload: dict[str, Any],
    ionization_slack: float,
    gap_slack: float,
    helium_like_bound: bool,
    spin_ground_sector: str,
) -> dict[str, Any]:
    candidate_scores = candidate_metrics_payload["scores"]
    baseline_scores = baseline_metrics_payload["scores"]
    candidate_errors = candidate_metrics_payload["relative_errors"]
    baseline_errors = baseline_metrics_payload["relative_errors"]
    failed_conditions: list[str] = []
    if not helium_like_bound:
        failed_conditions.append("helium_like_bound")
    if spin_ground_sector != "singlet":
        failed_conditions.append("spin_ground_sector")
    if float(candidate_scores["full_rms_relative_error"]) >= float(
        baseline_scores["full_rms_relative_error"]
    ):
        failed_conditions.append("full_rms_relative_error")
    if float(candidate_scores["one_body_rms_relative_error"]) >= float(
        baseline_scores["one_body_rms_relative_error"]
    ):
        failed_conditions.append("one_body_rms_relative_error")
    if float(candidate_scores["max_relative_error"]) > float(
        baseline_scores["max_relative_error"]
    ):
        failed_conditions.append("max_relative_error")
    if float(candidate_errors["helium_ionization_energy"]) > float(
        baseline_errors["helium_ionization_energy"]
    ) + float(ionization_slack):
        failed_conditions.append("helium_ionization_energy")
    if float(candidate_errors["singlet_triplet_gap"]) > float(
        baseline_errors["singlet_triplet_gap"]
    ) + float(gap_slack):
        failed_conditions.append("singlet_triplet_gap")
    return {
        "accepted_on_full_lane": len(failed_conditions) == 0,
        "failed_conditions": failed_conditions,
        "ionization_slack": float(ionization_slack),
        "gap_slack": float(gap_slack),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--candidate-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_one_body_coupling_calibration.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
    )
    parser.add_argument("--repulsion-softening-radius", type=float, default=1.10)
    parser.add_argument(
        "--repulsion-profile",
        choices=("hard_floor", "plummer", "erf_softcore", "exp_softcore"),
        default="hard_floor",
    )
    parser.add_argument("--repulsion-quadrature-order", type=int, default=1)
    parser.add_argument("--max-orbitals", type=int, default=16)
    parser.add_argument("--max-virtual-orbitals", type=int, default=48)
    parser.add_argument("--n-eig", type=int, default=88)
    parser.add_argument(
        "--basis-sweep",
        type=int,
        nargs="*",
        default=(16, 24, 32, 40, 48, 56, 64),
    )
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_fixed_basis_validation.json",
    )
    args = parser.parse_args()

    candidate_payload = read_json(args.candidate_json)
    baseline_readout = read_json(args.baseline_readout_json)
    parameters = _candidate_parameters(candidate_payload)
    custom_sizes = (
        tuple(int(size) for size in parameters["active_sizes"])
        if parameters.get("active_sizes") is not None
        else None
    )
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()
    solution = solve_two_electron_atomic_model(
        dimension=int(parameters["dimension"]),
        reference_coupling=float(parameters["reference_coupling"]),
        nuclear_charge=float(parameters["nuclear_charge"]),
        lattice_spacing=float(parameters["lattice_spacing"]),
        nuclear_softening_radius=float(parameters["softening_radius"]),
        repulsion_softening_radius=float(args.repulsion_softening_radius),
        nuclear_profile=str(parameters["nuclear_profile"]),
        nuclear_quadrature_order=int(parameters["nuclear_quadrature_order"]),
        nuclear_counterterm_strength=float(parameters["nuclear_counterterm_strength"]),
        nuclear_counterterm_radius=parameters["nuclear_counterterm_radius"],
        kinetic_stencil=str(parameters["kinetic_stencil"]),
        repulsion_profile=str(args.repulsion_profile),
        repulsion_quadrature_order=int(args.repulsion_quadrature_order),
        max_orbitals=int(args.max_orbitals),
        max_virtual_orbitals=int(args.max_virtual_orbitals),
        n_eig=int(args.n_eig),
        basis_sweep=tuple(int(value) for value in args.basis_sweep),
        custom_sizes=custom_sizes,
    )
    metrics = candidate_metrics(solution)
    baseline_metrics = helium_readout_metrics(baseline_readout)
    acceptance = _acceptance_summary(
        candidate_metrics_payload=metrics,
        baseline_metrics_payload=baseline_metrics,
        ionization_slack=float(args.ionization_slack),
        gap_slack=float(args.gap_slack),
        helium_like_bound=bool(solution["two_electron"]["helium_like_bound"]),
        spin_ground_sector=str(solution["two_electron"]["spin_ground_sector"]),
    )
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_candidate_json": str(args.candidate_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "candidate_parameters": parameters,
        "validation_model": {
            "repulsion_softening_radius": float(args.repulsion_softening_radius),
            "repulsion_profile": str(args.repulsion_profile),
            "repulsion_quadrature_order": int(args.repulsion_quadrature_order),
            "max_orbitals": int(args.max_orbitals),
            "max_virtual_orbitals": int(args.max_virtual_orbitals),
            "n_eig": int(args.n_eig),
            "basis_sweep": [int(value) for value in args.basis_sweep],
        },
        "solution": solution,
        "metrics": metrics,
        "baseline_metrics": baseline_metrics,
        "improvement_vs_baseline": {
            "full_rms_relative_error_delta": float(
                metrics["scores"]["full_rms_relative_error"]
            )
            - float(baseline_metrics["scores"]["full_rms_relative_error"]),
            "one_body_rms_relative_error_delta": float(
                metrics["scores"]["one_body_rms_relative_error"]
            )
            - float(baseline_metrics["scores"]["one_body_rms_relative_error"]),
            "max_relative_error_delta": float(metrics["scores"]["max_relative_error"])
            - float(baseline_metrics["scores"]["max_relative_error"]),
            "helium_ionization_energy_delta": float(
                metrics["relative_errors"]["helium_ionization_energy"]
            )
            - float(baseline_metrics["relative_errors"]["helium_ionization_energy"]),
            "singlet_triplet_gap_delta": float(
                metrics["relative_errors"]["singlet_triplet_gap"]
            )
            - float(baseline_metrics["relative_errors"]["singlet_triplet_gap"]),
        },
        "acceptance": acceptance,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Fixed-Basis Validation")
    print("=============================")
    print(
        f"- Candidate stencil={parameters['kinetic_stencil']} "
        f"a={parameters['lattice_spacing']:.4f} "
        f"sizes={parameters['active_sizes']}."
    )
    print(
        f"- Full RMS={metrics['scores']['full_rms_relative_error']:.6f} "
        f"accepted={'YES' if acceptance['accepted_on_full_lane'] else 'NO'}."
    )
    print(f"- Wrote validation output to {args.write_json}.")


if __name__ == "__main__":
    main()
