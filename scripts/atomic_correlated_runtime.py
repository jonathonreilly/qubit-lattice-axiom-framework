#!/usr/bin/env python3
"""Shared correlated-model helpers for the retained atomic lane."""

from __future__ import annotations

from typing import Any

import numpy as np

from scripts.atomic_observable_metrics import candidate_metrics, helium_readout_metrics
from scripts.atomic_two_body_runtime import (
    build_repulsion_kernel,
    build_short_range_pair_kernel,
    one_body_summary,
    orbital_pair_functions,
    pair_operator_tensor,
    solve_one_body_bound_orbitals,
    solve_sector,
    sweep_two_electron_basis,
)


def acceptance_summary(
    *,
    candidate_metrics_payload: dict[str, Any],
    baseline_metrics_payload: dict[str, Any],
    ionization_slack: float,
    gap_slack: float,
    helium_like_bound: bool,
    spin_ground_sector: str,
    allow_one_body_plateau: bool = False,
    one_body_tolerance: float = 0.0,
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
    candidate_one_body = float(candidate_scores["one_body_rms_relative_error"])
    baseline_one_body = float(baseline_scores["one_body_rms_relative_error"])
    if allow_one_body_plateau:
        if candidate_one_body > baseline_one_body + float(one_body_tolerance):
            failed_conditions.append("one_body_rms_relative_error")
    else:
        if candidate_one_body >= baseline_one_body:
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
        "allow_one_body_plateau": bool(allow_one_body_plateau),
        "one_body_tolerance": float(one_body_tolerance),
    }


def _candidate_parameter_dict(payload: dict[str, Any]) -> dict[str, Any]:
    def normalize_model_dict(model: dict[str, Any]) -> dict[str, Any]:
        output = dict(model)
        if "active_sizes" not in output and "custom_sizes" in output:
            output["active_sizes"] = list(output["custom_sizes"])
        if "softening_radius" not in output and "nuclear_softening_radius" in output:
            output["softening_radius"] = output["nuclear_softening_radius"]
        return output

    if "solution" in payload and "model" in payload["solution"]:
        return normalize_model_dict(dict(payload["solution"]["model"]))
    if "candidate_parameters" in payload:
        return normalize_model_dict(dict(payload["candidate_parameters"]))
    if payload.get("accepted_candidate") is not None:
        return normalize_model_dict(dict(payload["accepted_candidate"]["solution"]["model"]))
    if "selected_final_candidate" in payload and payload["selected_final_candidate"] is not None:
        selected = payload["selected_final_candidate"]
        if "solution" in selected:
            return normalize_model_dict(dict(selected["solution"]["model"]))
        if "parameters" in selected:
            return normalize_model_dict(dict(selected["parameters"]))
    if "promoted_candidate" in payload and payload["promoted_candidate"] is not None:
        return normalize_model_dict(dict(payload["promoted_candidate"]["parameters"]))
    if "best_by_one_body_rms" in payload:
        return normalize_model_dict(dict(payload["best_by_one_body_rms"]["parameters"]))
    if "best_by_full_rms" in payload and payload["best_by_full_rms"] is not None:
        best = payload["best_by_full_rms"]
        if "solution" in best:
            return normalize_model_dict(dict(best["solution"]["model"]))
        if "parameters" in best:
            return normalize_model_dict(dict(best["parameters"]))
    raise KeyError("unable to locate candidate parameters in payload")


def _validation_parameter_dict(payload: dict[str, Any]) -> dict[str, Any]:
    if "solution" in payload and "model" in payload["solution"]:
        model = dict(payload["solution"]["model"])
        return {
            "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
            "repulsion_profile": str(model["repulsion_profile"]),
            "repulsion_quadrature_order": int(model["repulsion_quadrature_order"]),
            "max_orbitals": int(model["max_orbitals"]),
            "max_virtual_orbitals": int(model["max_virtual_orbitals"]),
            "n_eig": int(model["n_eig"]),
            "basis_sweep": list(model["basis_sweep"]),
        }
    if "validation_model" in payload:
        return dict(payload["validation_model"])
    if payload.get("accepted_candidate") is not None:
        model = dict(payload["accepted_candidate"]["solution"]["model"])
        return {
            "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
            "repulsion_profile": str(model["repulsion_profile"]),
            "repulsion_quadrature_order": int(model["repulsion_quadrature_order"]),
            "max_orbitals": int(model["max_orbitals"]),
            "max_virtual_orbitals": int(model["max_virtual_orbitals"]),
            "n_eig": int(model["n_eig"]),
            "basis_sweep": list(model["basis_sweep"]),
        }
    if "best_by_full_rms" in payload and payload["best_by_full_rms"] is not None:
        model = dict(payload["best_by_full_rms"]["solution"]["model"])
        return {
            "repulsion_softening_radius": float(model["repulsion_softening_radius"]),
            "repulsion_profile": str(model["repulsion_profile"]),
            "repulsion_quadrature_order": int(model["repulsion_quadrature_order"]),
            "max_orbitals": int(model["max_orbitals"]),
            "max_virtual_orbitals": int(model["max_virtual_orbitals"]),
            "n_eig": int(model["n_eig"]),
            "basis_sweep": list(model["basis_sweep"]),
        }
    raise KeyError("unable to locate validation parameters in payload")


def candidate_and_validation_parameters(
    payload: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, Any]]:
    return _candidate_parameter_dict(payload), _validation_parameter_dict(payload)


def build_correlated_base_payload(
    candidate_parameters: dict[str, Any],
    validation_model: dict[str, Any],
) -> dict[str, Any]:
    custom_sizes = tuple(int(size) for size in candidate_parameters["active_sizes"])
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
        nuclear_shell_strength=float(candidate_parameters.get("nuclear_shell_strength", 0.0)),
        nuclear_shell_radius=candidate_parameters.get("nuclear_shell_radius"),
        nuclear_shell_width=candidate_parameters.get("nuclear_shell_width"),
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
        nuclear_shell_strength=float(candidate_parameters.get("nuclear_shell_strength", 0.0)),
        nuclear_shell_radius=candidate_parameters.get("nuclear_shell_radius"),
        nuclear_shell_width=candidate_parameters.get("nuclear_shell_width"),
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
    model_base = {
        "dimension": int(candidate_parameters["dimension"]),
        "reference_coupling": float(candidate_parameters["reference_coupling"]),
        "nuclear_charge": float(candidate_parameters["nuclear_charge"]),
        "nuclear_coupling": float(candidate_parameters["reference_coupling"])
        * float(candidate_parameters["nuclear_charge"]),
        "electron_repulsion_coupling": float(candidate_parameters["reference_coupling"]),
        "lattice_spacing": float(candidate_parameters["lattice_spacing"]),
        "nuclear_softening_radius": float(candidate_parameters["softening_radius"]),
        "repulsion_softening_radius": float(validation_model["repulsion_softening_radius"]),
        "nuclear_profile": str(candidate_parameters["nuclear_profile"]),
        "nuclear_quadrature_order": int(candidate_parameters["nuclear_quadrature_order"]),
        "repulsion_profile": str(validation_model["repulsion_profile"]),
        "repulsion_quadrature_order": int(validation_model["repulsion_quadrature_order"]),
        "nuclear_counterterm_strength": float(
            candidate_parameters["nuclear_counterterm_strength"]
        ),
        "nuclear_counterterm_radius": candidate_parameters["nuclear_counterterm_radius"],
        "nuclear_shell_strength": float(candidate_parameters.get("nuclear_shell_strength", 0.0)),
        "nuclear_shell_radius": candidate_parameters.get("nuclear_shell_radius"),
        "nuclear_shell_width": candidate_parameters.get("nuclear_shell_width"),
        "kinetic_stencil": str(candidate_parameters["kinetic_stencil"]),
        "max_orbitals": int(validation_model["max_orbitals"]),
        "max_virtual_orbitals": int(validation_model["max_virtual_orbitals"]),
        "n_eig": int(validation_model["n_eig"]),
        "basis_sweep": [int(value) for value in validation_model["basis_sweep"]],
        "custom_sizes": [int(value) for value in custom_sizes],
    }
    return {
        "candidate_parameters": dict(candidate_parameters),
        "validation_model": dict(validation_model),
        "custom_sizes": custom_sizes,
        "hydrogen_result": hydrogen_result,
        "helium_ion_result": helium_ion_result,
        "orbital_energies": orbital_energies,
        "orbital_matrix": orbital_matrix,
        "pair_functions": pair_functions,
        "repulsion_tensor": repulsion_tensor,
        "contact_tensor": contact_tensor,
        "model_base": model_base,
    }


def finite_range_pair_tensor(
    base_payload: dict[str, Any],
    *,
    correlation_radius: float,
    strength: float,
    profile: str = "gaussian",
    cutoff_multiplier: float = 3.0,
) -> np.ndarray:
    kernel = build_short_range_pair_kernel(
        base_payload["custom_sizes"],
        lattice_spacing=float(base_payload["candidate_parameters"]["lattice_spacing"]),
        correlation_radius=float(correlation_radius),
        strength=float(strength),
        profile=str(profile),
        cutoff_multiplier=float(cutoff_multiplier),
    )
    return pair_operator_tensor(
        base_payload["pair_functions"],
        len(base_payload["orbital_energies"]),
        kernel_matrix=kernel,
    )


def pair_diagonal_correlation_tensor(
    n_orbitals: int,
    weight_fn,
) -> np.ndarray:
    tensor = np.zeros((n_orbitals, n_orbitals, n_orbitals, n_orbitals), dtype=float)
    for left in range(n_orbitals):
        for right in range(left, n_orbitals):
            weight = float(weight_fn(left, right))
            if weight == 0.0:
                continue
            diagonal_scale = float(1 + int(left == right))
            tensor[left, left, right, right] += diagonal_scale * weight
            tensor[right, right, left, left] += diagonal_scale * weight
    return tensor


def bound_shell_projector_tensor(
    base_payload: dict[str, Any],
    *,
    ground_excited_strength: float = 0.0,
    excited_excited_strength: float = 0.0,
    ground_ground_strength: float = 0.0,
) -> np.ndarray:
    n_orbitals = len(base_payload["orbital_energies"])
    negative_orbital_count = int(base_payload["helium_ion_result"]["n_negative_selected"])

    def weight_fn(left: int, right: int) -> float:
        left_is_ground = left == 0
        right_is_ground = right == 0
        left_is_excited_bound = 0 < left < negative_orbital_count
        right_is_excited_bound = 0 < right < negative_orbital_count
        ground_excited = (left_is_ground and right_is_excited_bound) or (
            right_is_ground and left_is_excited_bound
        )
        excited_excited = left_is_excited_bound and right_is_excited_bound
        ground_ground = left_is_ground and right_is_ground
        return (
            float(ground_excited_strength) * float(ground_excited)
            + float(excited_excited_strength) * float(excited_excited)
            + float(ground_ground_strength) * float(ground_ground)
        )

    return pair_diagonal_correlation_tensor(
        n_orbitals,
        weight_fn=weight_fn,
    )


def extra_tensor_from_model(
    base_payload: dict[str, Any],
    model: dict[str, Any],
) -> np.ndarray | None:
    pieces: list[np.ndarray] = []
    if "contact_correction_strength" in model:
        pieces.append(
            float(model["contact_correction_strength"]) * base_payload["contact_tensor"]
        )
    if "pair_correction_profile" in model:
        pieces.append(
            finite_range_pair_tensor(
                base_payload,
                correlation_radius=float(model["pair_correction_radius"]),
                strength=float(model["pair_correction_strength"]),
                profile=str(model["pair_correction_profile"]),
                cutoff_multiplier=float(model["pair_correction_cutoff_multiplier"]),
            )
        )
    if (
        "shell_projector_ground_excited_strength" in model
        or "shell_projector_excited_excited_strength" in model
        or "shell_projector_ground_ground_strength" in model
    ):
        pieces.append(
            bound_shell_projector_tensor(
                base_payload,
                ground_excited_strength=float(
                    model.get("shell_projector_ground_excited_strength", 0.0)
                ),
                excited_excited_strength=float(
                    model.get("shell_projector_excited_excited_strength", 0.0)
                ),
                ground_ground_strength=float(
                    model.get("shell_projector_ground_ground_strength", 0.0)
                ),
            )
        )
    if not pieces:
        return None
    total = np.zeros_like(base_payload["repulsion_tensor"], dtype=float)
    for piece in pieces:
        total = total + np.asarray(piece, dtype=float)
    return total


def correlated_operator_fields(model: dict[str, Any]) -> dict[str, Any]:
    fields = {}
    for key in (
        "contact_correction_strength",
        "pair_correction_profile",
        "pair_correction_radius",
        "pair_correction_strength",
        "pair_correction_cutoff_multiplier",
        "shell_projector_ground_excited_strength",
        "shell_projector_excited_excited_strength",
        "shell_projector_ground_ground_strength",
    ):
        if key in model:
            fields[key] = model[key]
    return fields


def solve_correlated_solution(
    base_payload: dict[str, Any],
    *,
    extra_tensor: np.ndarray | None = None,
    extra_model_fields: dict[str, Any] | None = None,
    basis_sweep: tuple[int, ...] | None = None,
) -> dict[str, Any]:
    interaction_tensor = np.array(base_payload["repulsion_tensor"], copy=True)
    if extra_tensor is not None:
        interaction_tensor = interaction_tensor + np.asarray(extra_tensor, dtype=float)
    active_basis_sweep = (
        tuple(int(value) for value in basis_sweep)
        if basis_sweep is not None
        else tuple(int(value) for value in base_payload["validation_model"]["basis_sweep"])
    )
    singlet = solve_sector(
        orbital_energies=base_payload["orbital_energies"],
        interaction_tensor=interaction_tensor,
        contact_tensor=base_payload["contact_tensor"],
        sector="singlet",
    )
    triplet = solve_sector(
        orbital_energies=base_payload["orbital_energies"],
        interaction_tensor=interaction_tensor,
        contact_tensor=base_payload["contact_tensor"],
        sector="triplet",
    )
    basis_rows = sweep_two_electron_basis(
        orbital_energies=base_payload["orbital_energies"],
        interaction_tensor=interaction_tensor,
        contact_tensor=base_payload["contact_tensor"],
        basis_sizes=active_basis_sweep,
    )
    helium_ion_summary = one_body_summary(base_payload["helium_ion_result"])
    hydrogen_summary = one_body_summary(base_payload["hydrogen_result"])
    ion_ground_energy = float(helium_ion_summary["ground_energy"])
    singlet_ground_energy = float(singlet["ground_energy"])
    triplet_ground_energy = float(triplet["ground_energy"])
    model = dict(base_payload["model_base"])
    model["basis_sweep"] = [int(value) for value in active_basis_sweep]
    if extra_model_fields is not None:
        model.update(extra_model_fields)
    return {
        "model": model,
        "hydrogen_reference": hydrogen_summary,
        "helium_ion_reference": helium_ion_summary,
        "two_electron": {
            "spatial_orbital_count": int(len(base_payload["orbital_energies"])),
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
            "triplet_ionization_energy": float(
                ion_ground_energy - triplet_ground_energy
            ),
            "singlet_triplet_gap": float(triplet_ground_energy - singlet_ground_energy),
            "helium_like_bound": bool(singlet_ground_energy < ion_ground_energy),
            "spin_ground_sector": (
                "singlet"
                if singlet_ground_energy <= triplet_ground_energy
                else "triplet"
            ),
        },
    }


def baseline_metrics_from_readout(path_payload: dict[str, Any]) -> dict[str, Any]:
    if "accuracy_metrics" in path_payload and path_payload["accuracy_metrics"] is not None:
        return dict(path_payload["accuracy_metrics"])
    return helium_readout_metrics(path_payload)


def correlated_row_summary(
    solution: dict[str, Any],
    *,
    baseline_metrics_payload: dict[str, Any],
    ionization_slack: float,
    gap_slack: float,
    allow_one_body_plateau: bool = False,
    one_body_tolerance: float = 0.0,
) -> dict[str, Any]:
    metrics = candidate_metrics(solution)
    acceptance = acceptance_summary(
        candidate_metrics_payload=metrics,
        baseline_metrics_payload=baseline_metrics_payload,
        ionization_slack=float(ionization_slack),
        gap_slack=float(gap_slack),
        helium_like_bound=bool(solution["two_electron"]["helium_like_bound"]),
        spin_ground_sector=str(solution["two_electron"]["spin_ground_sector"]),
        allow_one_body_plateau=bool(allow_one_body_plateau),
        one_body_tolerance=float(one_body_tolerance),
    )
    return {
        "solution": solution,
        "metrics": metrics,
        "acceptance": acceptance,
    }
