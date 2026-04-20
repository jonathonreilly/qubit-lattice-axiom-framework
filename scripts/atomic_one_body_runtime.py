#!/usr/bin/env python3
"""Shared one-body benchmark helpers for the retained atomic lane."""

from __future__ import annotations

from typing import Any

from scripts.atomic_observable_metrics import one_body_pair_metrics
from scripts.atomic_two_body_runtime import (
    find_bound_state_config,
    one_body_summary,
    rescale_sizes_for_physical_box,
    solve_one_body_bound_orbitals,
)


def resolve_candidate_sizes(
    *,
    dimension: int = 3,
    lattice_spacing: float = 1.0,
    fixed_physical_box: bool = True,
    reference_spacing: float = 1.0,
    reference_sizes: tuple[int, ...] | None = None,
    custom_sizes: tuple[int, ...] | None = None,
    min_size: int = 8,
) -> tuple[int, ...]:
    if custom_sizes is not None:
        return tuple(int(size) for size in custom_sizes)
    if reference_sizes is None:
        _d, default_sizes, _g = find_bound_state_config(dimension)
        reference_sizes = default_sizes
    if not fixed_physical_box:
        return tuple(int(size) for size in reference_sizes)
    return rescale_sizes_for_physical_box(
        tuple(int(size) for size in reference_sizes),
        reference_spacing=float(reference_spacing),
        lattice_spacing=float(lattice_spacing),
        min_size=int(min_size),
    )


def _ground_orbital_summary(one_body_result: dict[str, Any]) -> dict[str, Any]:
    ground_row = dict(one_body_result["orbital_rows"][0])
    return {
        "energy": float(ground_row["energy"]),
        "mean_radius": float(ground_row["mean_radius"]),
        "radius_std": float(ground_row["radius_std"]),
        "ipr": float(ground_row["ipr"]),
        "center_weight": float(ground_row["center_weight"]),
        "decay_rate": float(ground_row["decay_rate"]),
        "genuinely_localized": bool(ground_row["genuinely_localized"]),
        "physical_bound": bool(ground_row["physical_bound"]),
    }


def benchmark_one_body_candidate(
    *,
    dimension: int = 3,
    reference_coupling: float = 1.595,
    nuclear_charge: float = 2.0,
    lattice_spacing: float = 1.0,
    softening_radius: float | None = None,
    softening_multiplier: float = 0.75,
    nuclear_profile: str = "hard_floor",
    nuclear_quadrature_order: int = 1,
    nuclear_counterterm_strength: float = 0.0,
    nuclear_counterterm_radius: float | None = None,
    nuclear_shell_strength: float = 0.0,
    nuclear_shell_radius: float | None = None,
    nuclear_shell_width: float | None = None,
    kinetic_stencil: str = "three_point",
    max_orbitals: int = 16,
    n_eig: int = 40,
    fixed_physical_box: bool = True,
    reference_spacing: float = 1.0,
    reference_sizes: tuple[int, ...] | None = None,
    custom_sizes: tuple[int, ...] | None = None,
    min_size: int = 8,
) -> dict[str, Any]:
    if softening_radius is None:
        softening_radius = float(softening_multiplier) * float(lattice_spacing)
    active_sizes = resolve_candidate_sizes(
        dimension=int(dimension),
        lattice_spacing=float(lattice_spacing),
        fixed_physical_box=bool(fixed_physical_box),
        reference_spacing=float(reference_spacing),
        reference_sizes=reference_sizes,
        custom_sizes=custom_sizes,
        min_size=int(min_size),
    )
    hydrogen = solve_one_body_bound_orbitals(
        dimension=int(dimension),
        coupling=float(reference_coupling),
        max_orbitals=int(max_orbitals),
        n_eig=int(n_eig),
        lattice_spacing=float(lattice_spacing),
        softening_radius=float(softening_radius),
        nuclear_profile=str(nuclear_profile),
        nuclear_quadrature_order=int(nuclear_quadrature_order),
        nuclear_counterterm_strength=float(nuclear_counterterm_strength),
        nuclear_counterterm_radius=nuclear_counterterm_radius,
        nuclear_shell_strength=float(nuclear_shell_strength),
        nuclear_shell_radius=nuclear_shell_radius,
        nuclear_shell_width=nuclear_shell_width,
        kinetic_stencil=str(kinetic_stencil),
        custom_sizes=active_sizes,
    )
    helium_ion = solve_one_body_bound_orbitals(
        dimension=int(dimension),
        coupling=float(reference_coupling) * float(nuclear_charge),
        max_orbitals=int(max_orbitals),
        n_eig=int(n_eig),
        lattice_spacing=float(lattice_spacing),
        softening_radius=float(softening_radius),
        nuclear_profile=str(nuclear_profile),
        nuclear_quadrature_order=int(nuclear_quadrature_order),
        nuclear_counterterm_strength=float(nuclear_counterterm_strength),
        nuclear_counterterm_radius=nuclear_counterterm_radius,
        nuclear_shell_strength=float(nuclear_shell_strength),
        nuclear_shell_radius=nuclear_shell_radius,
        nuclear_shell_width=nuclear_shell_width,
        kinetic_stencil=str(kinetic_stencil),
        custom_sizes=active_sizes,
    )
    metrics = one_body_pair_metrics(hydrogen, helium_ion)
    return {
        "parameters": {
            "dimension": int(dimension),
            "reference_coupling": float(reference_coupling),
            "nuclear_charge": float(nuclear_charge),
            "lattice_spacing": float(lattice_spacing),
            "softening_radius": float(softening_radius),
            "softening_multiplier": float(softening_multiplier),
            "nuclear_profile": str(nuclear_profile),
            "nuclear_quadrature_order": int(nuclear_quadrature_order),
            "nuclear_counterterm_strength": float(nuclear_counterterm_strength),
            "nuclear_counterterm_radius": (
                float(nuclear_counterterm_radius)
                if nuclear_counterterm_radius is not None
                else None
            ),
            "nuclear_shell_strength": float(nuclear_shell_strength),
            "nuclear_shell_radius": (
                float(nuclear_shell_radius)
                if nuclear_shell_radius is not None
                else None
            ),
            "nuclear_shell_width": (
                float(nuclear_shell_width)
                if nuclear_shell_width is not None
                else None
            ),
            "kinetic_stencil": str(kinetic_stencil),
            "max_orbitals": int(max_orbitals),
            "n_eig": int(n_eig),
            "fixed_physical_box": bool(fixed_physical_box),
            "reference_spacing": float(reference_spacing),
            "reference_sizes": (
                [int(size) for size in reference_sizes]
                if reference_sizes is not None
                else None
            ),
            "custom_sizes": (
                [int(size) for size in custom_sizes]
                if custom_sizes is not None
                else None
            ),
            "active_sizes": [int(size) for size in active_sizes],
            "physical_box_lengths": [
                float(size) * float(lattice_spacing) for size in active_sizes
            ],
        },
        "hydrogen_reference": one_body_summary(hydrogen),
        "helium_ion_reference": one_body_summary(helium_ion),
        "hydrogen_ground_orbital": _ground_orbital_summary(hydrogen),
        "helium_ion_ground_orbital": _ground_orbital_summary(helium_ion),
        "metrics": metrics,
    }
