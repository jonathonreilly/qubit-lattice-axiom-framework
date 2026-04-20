#!/usr/bin/env python3
"""Prototype a short-range correlated contact correction on the fixed helium basis."""

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
    candidate_metrics,
    helium_readout_metrics,
)
from scripts.atomic_two_body_runtime import (  # noqa: E402
    build_repulsion_kernel,
    one_body_summary,
    orbital_pair_functions,
    pair_operator_tensor,
    solve_one_body_bound_orbitals,
    solve_sector,
    sweep_two_electron_basis,
)


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


def _candidate_parameters(payload: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    return dict(payload["candidate_parameters"]), dict(payload["validation_model"])


def _build_solution_like_payload(
    *,
    model: dict[str, Any],
    hydrogen_reference: dict[str, Any],
    helium_ion_reference: dict[str, Any],
    singlet: dict[str, Any],
    triplet: dict[str, Any],
    basis_rows: list[dict[str, Any]],
    contact_correction_strength: float,
) -> dict[str, Any]:
    ion_ground_energy = float(helium_ion_reference["ground_energy"])
    singlet_ground_energy = float(singlet["ground_energy"])
    triplet_ground_energy = float(triplet["ground_energy"])
    return {
        "model": {
            **model,
            "contact_correction_strength": float(contact_correction_strength),
        },
        "hydrogen_reference": hydrogen_reference,
        "helium_ion_reference": helium_ion_reference,
        "two_electron": {
            "spatial_orbital_count": int(len(helium_ion_reference["orbital_rows"])),
            "electron_repulsion_present": True,
            "antisymmetry_present": True,
            "spin_sectors_present": ["singlet", "triplet"],
            "singlet": singlet,
            "triplet": triplet,
            "basis_sweep": basis_rows,
            "noninteracting_double_occupancy_energy": float(2.0 * ion_ground_energy),
            "interaction_shift_from_double_occupancy": float(
                singlet_ground_energy - 2.0 * ion_ground_energy
            ),
            "ionization_energy": float(ion_ground_energy - singlet_ground_energy),
            "triplet_ionization_energy": float(ion_ground_energy - triplet_ground_energy),
            "singlet_triplet_gap": float(triplet_ground_energy - singlet_ground_energy),
            "helium_like_bound": bool(singlet_ground_energy < ion_ground_energy),
            "spin_ground_sector": (
                "singlet"
                if singlet_ground_energy <= triplet_ground_energy
                else "triplet"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--validation-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_fixed_basis_validation.json",
    )
    parser.add_argument(
        "--baseline-readout-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_helium_readout_virtual_basis_tail.json",
    )
    parser.add_argument(
        "--contact-correction-strengths",
        type=float,
        nargs="*",
        default=(0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5),
    )
    parser.add_argument("--ionization-slack", type=float, default=0.003)
    parser.add_argument("--gap-slack", type=float, default=0.003)
    parser.add_argument(
        "--write-json",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT / "atomic_correlated_contact_scan.json",
    )
    args = parser.parse_args()

    validation_payload = read_json(args.validation_json)
    baseline_metrics = helium_readout_metrics(read_json(args.baseline_readout_json))
    candidate_parameters, validation_model = _candidate_parameters(validation_payload)
    custom_sizes = tuple(int(size) for size in candidate_parameters["active_sizes"])
    started_at = datetime.now().isoformat(timespec="seconds")
    total_started = time.perf_counter()

    hydrogen_result = solve_one_body_bound_orbitals(
        dimension=int(candidate_parameters["dimension"]),
        coupling=float(candidate_parameters["reference_coupling"]),
        max_orbitals=int(validation_model["max_orbitals"]),
        max_virtual_orbitals=int(validation_model["max_virtual_orbitals"]),
        n_eig=int(validation_model["n_eig"]),
        lattice_spacing=float(candidate_parameters["lattice_spacing"]),
        softening_radius=float(candidate_parameters["softening_radius"]),
        nuclear_profile=str(candidate_parameters["nuclear_profile"]),
        nuclear_quadrature_order=int(candidate_parameters["nuclear_quadrature_order"]),
        nuclear_counterterm_strength=float(
            candidate_parameters["nuclear_counterterm_strength"]
        ),
        nuclear_counterterm_radius=candidate_parameters["nuclear_counterterm_radius"],
        kinetic_stencil=str(candidate_parameters["kinetic_stencil"]),
        custom_sizes=custom_sizes,
    )
    helium_ion_result = solve_one_body_bound_orbitals(
        dimension=int(candidate_parameters["dimension"]),
        coupling=float(candidate_parameters["reference_coupling"])
        * float(candidate_parameters["nuclear_charge"]),
        max_orbitals=int(validation_model["max_orbitals"]),
        max_virtual_orbitals=int(validation_model["max_virtual_orbitals"]),
        n_eig=int(validation_model["n_eig"]),
        lattice_spacing=float(candidate_parameters["lattice_spacing"]),
        softening_radius=float(candidate_parameters["softening_radius"]),
        nuclear_profile=str(candidate_parameters["nuclear_profile"]),
        nuclear_quadrature_order=int(candidate_parameters["nuclear_quadrature_order"]),
        nuclear_counterterm_strength=float(
            candidate_parameters["nuclear_counterterm_strength"]
        ),
        nuclear_counterterm_radius=candidate_parameters["nuclear_counterterm_radius"],
        kinetic_stencil=str(candidate_parameters["kinetic_stencil"]),
        custom_sizes=custom_sizes,
    )
    orbital_energies = np.asarray(helium_ion_result["orbital_energies"], dtype=float)
    orbital_matrix = np.asarray(helium_ion_result["orbital_matrix"], dtype=float)
    repulsion_kernel = build_repulsion_kernel(
        custom_sizes,
        int(candidate_parameters["dimension"]),
        coupling=float(candidate_parameters["reference_coupling"]),
        lattice_spacing=float(candidate_parameters["lattice_spacing"]),
        softening_radius=float(validation_model["repulsion_softening_radius"]),
        profile=str(validation_model["repulsion_profile"]),
        quadrature_order=int(validation_model["repulsion_quadrature_order"]),
    )
    pair_functions = orbital_pair_functions(orbital_matrix)
    repulsion_tensor = pair_operator_tensor(
        pair_functions,
        len(orbital_energies),
        kernel_matrix=repulsion_kernel,
    )
    contact_tensor = pair_operator_tensor(
        pair_functions,
        len(orbital_energies),
        kernel_matrix=None,
    )

    rows = []
    strengths = [float(value) for value in args.contact_correction_strengths]
    for index, contact_correction_strength in enumerate(strengths, start=1):
        scan_started = time.perf_counter()
        interaction_tensor = repulsion_tensor + float(contact_correction_strength) * contact_tensor
        singlet = solve_sector(
            orbital_energies=orbital_energies,
            interaction_tensor=interaction_tensor,
            contact_tensor=contact_tensor,
            sector="singlet",
        )
        triplet = solve_sector(
            orbital_energies=orbital_energies,
            interaction_tensor=interaction_tensor,
            contact_tensor=contact_tensor,
            sector="triplet",
        )
        basis_rows = sweep_two_electron_basis(
            orbital_energies=orbital_energies,
            interaction_tensor=interaction_tensor,
            contact_tensor=contact_tensor,
            basis_sizes=tuple(int(value) for value in validation_model["basis_sweep"]),
        )
        solution = _build_solution_like_payload(
            model={
                **validation_payload["solution"]["model"],
            },
            hydrogen_reference=one_body_summary(hydrogen_result),
            helium_ion_reference=one_body_summary(helium_ion_result),
            singlet=singlet,
            triplet=triplet,
            basis_rows=basis_rows,
            contact_correction_strength=float(contact_correction_strength),
        )
        metrics = candidate_metrics(solution)
        acceptance = _acceptance_summary(
            candidate_metrics_payload=metrics,
            baseline_metrics_payload=baseline_metrics,
            ionization_slack=float(args.ionization_slack),
            gap_slack=float(args.gap_slack),
            helium_like_bound=bool(solution["two_electron"]["helium_like_bound"]),
            spin_ground_sector=str(solution["two_electron"]["spin_ground_sector"]),
        )
        row = {
            "contact_correction_strength": float(contact_correction_strength),
            "metrics": metrics,
            "acceptance": acceptance,
            "solution": solution,
            "elapsed_seconds": round(time.perf_counter() - scan_started, 6),
        }
        rows.append(row)
        print(
            f"[{index}/{len(strengths)}] "
            f"lambda={contact_correction_strength:.4f} "
            f"full={metrics['scores']['full_rms_relative_error']:.6f} "
            f"gap={metrics['relative_errors']['singlet_triplet_gap']:.4%} "
            f"accepted={'YES' if acceptance['accepted_on_full_lane'] else 'NO'}",
            flush=True,
        )

    accepted_rows = [row for row in rows if row["acceptance"]["accepted_on_full_lane"]]
    output_payload = {
        "started_at": started_at,
        "completed_at": datetime.now().isoformat(timespec="seconds"),
        "source_validation_json": str(args.validation_json),
        "source_baseline_readout_json": str(args.baseline_readout_json),
        "rows": rows,
        "best_by_full_rms": min(
            rows,
            key=lambda row: (
                float(row["metrics"]["scores"]["full_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        ),
        "accepted_candidate": min(
            accepted_rows,
            key=lambda row: (
                float(row["metrics"]["scores"]["full_rms_relative_error"]),
                float(row["metrics"]["scores"]["max_relative_error"]),
            ),
        )
        if accepted_rows
        else None,
        "total_elapsed_seconds": round(time.perf_counter() - total_started, 6),
    }
    write_json(args.write_json, output_payload)

    print()
    print("Atomic Correlated Contact Scan")
    print("==============================")
    if output_payload["accepted_candidate"] is None:
        print("- No correlated contact candidate cleared the acceptance gate.")
    else:
        accepted = output_payload["accepted_candidate"]
        print(
            f"- Accepted candidate: lambda={accepted['contact_correction_strength']:.4f} "
            f"full={accepted['metrics']['scores']['full_rms_relative_error']:.6f}."
        )
    print(f"- Wrote correlated scan output to {args.write_json}.")


if __name__ == "__main__":
    main()
