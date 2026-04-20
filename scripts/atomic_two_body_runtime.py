#!/usr/bin/env python3
"""Reduced orbital-basis two-electron helpers for the atomic lane."""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import numpy as np
from scipy import sparse
from scipy.special import erf

REPO_ROOT = Path(__file__).resolve().parent.parent
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.atomic_lane_runtime import BOUND_STATE_CONFIGS  # noqa: E402
from scripts.frontier_bound_state_selection import (  # noqa: E402
    analyze_localization,
    build_nd_laplacian,
    count_bound_states,
)

SUPPORTED_NUCLEAR_PROFILES = (
    "hard_floor",
    "plummer",
    "shifted",
    "erf_softcore",
    "exp_softcore",
    "tanh_softcore",
    "gaussian_floor",
)

SUPPORTED_REPULSION_PROFILES = (
    "hard_floor",
    "plummer",
    "erf_softcore",
    "exp_softcore",
)

SUPPORTED_KINETIC_STENCILS = (
    "three_point",
    "five_point",
    "seven_point",
)

SUPPORTED_CORRELATED_PAIR_PROFILES = (
    "gaussian",
    "exponential",
)


def find_bound_state_config(dimension: int) -> tuple[int, tuple[int, ...], float]:
    for config in BOUND_STATE_CONFIGS:
        if config[0] == dimension:
            return config
    raise KeyError(f"no bound-state config registered for d={dimension}")


def resolve_lattice_sizes(
    dimension: int,
    custom_sizes: tuple[int, ...] | None = None,
) -> tuple[int, ...]:
    _dimension, default_sizes, _reference_coupling = find_bound_state_config(dimension)
    if custom_sizes is None:
        return default_sizes
    if len(custom_sizes) != dimension:
        raise ValueError(
            f"custom sizes {custom_sizes!r} do not match dimension d={dimension}"
        )
    return tuple(int(size) for size in custom_sizes)


def rescale_sizes_for_physical_box(
    reference_sizes: tuple[int, ...],
    *,
    reference_spacing: float = 1.0,
    lattice_spacing: float = 1.0,
    min_size: int = 6,
) -> tuple[int, ...]:
    if lattice_spacing <= 0.0:
        raise ValueError(f"lattice_spacing must be > 0, got {lattice_spacing!r}")
    if reference_spacing <= 0.0:
        raise ValueError(
            f"reference_spacing must be > 0, got {reference_spacing!r}"
        )
    scale = float(reference_spacing) / float(lattice_spacing)
    return tuple(
        max(int(min_size), int(round(float(size) * scale)))
        for size in reference_sizes
    )


def lattice_geometry(sizes: tuple[int, ...]) -> dict[str, np.ndarray]:
    dimension = len(sizes)
    coordinates = np.indices(sizes).reshape(dimension, -1).T.astype(float)
    center = np.array([(size - 1) / 2.0 for size in sizes], dtype=float)
    offsets = coordinates - center[np.newaxis, :]
    radii = np.sqrt(np.sum(offsets**2, axis=1))
    return {
        "coordinates": coordinates,
        "center": center,
        "radii": radii,
    }


def normalize_kinetic_stencil(stencil: str) -> str:
    normalized = str(stencil).strip().lower()
    if normalized not in SUPPORTED_KINETIC_STENCILS:
        raise ValueError(
            f"unsupported kinetic stencil {stencil!r}; "
            f"expected one of {SUPPORTED_KINETIC_STENCILS!r}"
        )
    return normalized


def normalize_correlated_pair_profile(profile: str) -> str:
    normalized = str(profile).strip().lower()
    if normalized not in SUPPORTED_CORRELATED_PAIR_PROFILES:
        raise ValueError(
            f"unsupported correlated pair profile {profile!r}; "
            f"expected one of {SUPPORTED_CORRELATED_PAIR_PROFILES!r}"
        )
    return normalized


def build_1d_negative_laplacian(
    size: int,
    *,
    stencil: str = "three_point",
) -> sparse.csr_matrix:
    normalized_stencil = normalize_kinetic_stencil(stencil)
    if normalized_stencil == "three_point":
        diag = 2.0 * np.ones(size)
        off = -1.0 * np.ones(size - 1)
        return sparse.diags(
            [off, diag, off],
            [-1, 0, 1],
            shape=(size, size),
            format="csr",
        )
    if normalized_stencil == "five_point":
        diag = (30.0 / 12.0) * np.ones(size)
        off1 = (-16.0 / 12.0) * np.ones(size - 1)
        off2 = (1.0 / 12.0) * np.ones(size - 2)
        return sparse.diags(
            [off2, off1, diag, off1, off2],
            [-2, -1, 0, 1, 2],
            shape=(size, size),
            format="csr",
        )
    if normalized_stencil == "seven_point":
        diag = (49.0 / 18.0) * np.ones(size)
        off1 = (-3.0 / 2.0) * np.ones(size - 1)
        off2 = (3.0 / 20.0) * np.ones(size - 2)
        off3 = (-1.0 / 90.0) * np.ones(size - 3)
        return sparse.diags(
            [off3, off2, off1, diag, off1, off2, off3],
            [-3, -2, -1, 0, 1, 2, 3],
            shape=(size, size),
            format="csr",
        )
    raise AssertionError(f"unhandled kinetic stencil {normalized_stencil!r}")


def build_nd_negative_laplacian(
    sizes: tuple[int, ...],
    *,
    stencil: str = "three_point",
) -> sparse.csr_matrix:
    normalized_stencil = normalize_kinetic_stencil(stencil)
    if normalized_stencil == "three_point":
        return build_nd_laplacian(sizes)
    dimension = len(sizes)
    mats = [
        build_1d_negative_laplacian(size, stencil=normalized_stencil)
        for size in sizes
    ]
    n_total = int(np.prod(sizes))
    total = sparse.csr_matrix((n_total, n_total))
    for dim in range(dimension):
        term = sparse.eye(1, format="csr")
        for axis in range(dimension):
            if axis == dim:
                term = sparse.kron(term, mats[axis], format="csr")
            else:
                term = sparse.kron(
                    term,
                    sparse.eye(sizes[axis], format="csr"),
                    format="csr",
                )
        total = total + term
    return total


def build_scaled_laplacian(
    sizes: tuple[int, ...],
    *,
    lattice_spacing: float = 1.0,
    kinetic_stencil: str = "three_point",
) -> sparse.csr_matrix:
    return build_nd_negative_laplacian(
        sizes,
        stencil=kinetic_stencil,
    ) / float(lattice_spacing**2)


def normalize_nuclear_profile(profile: str) -> str:
    normalized = str(profile).strip().lower()
    if normalized not in SUPPORTED_NUCLEAR_PROFILES:
        raise ValueError(
            f"unsupported nuclear profile {profile!r}; "
            f"expected one of {SUPPORTED_NUCLEAR_PROFILES!r}"
        )
    return normalized


def normalize_repulsion_profile(profile: str) -> str:
    normalized = str(profile).strip().lower()
    if normalized not in SUPPORTED_REPULSION_PROFILES:
        raise ValueError(
            f"unsupported repulsion profile {profile!r}; "
            f"expected one of {SUPPORTED_REPULSION_PROFILES!r}"
        )
    return normalized


def regularized_radii_nd(
    radii: np.ndarray,
    *,
    softening_radius: float,
    profile: str,
) -> np.ndarray:
    radius_floor = max(float(softening_radius), 1.0e-12)
    normalized_profile = normalize_nuclear_profile(profile)
    if normalized_profile == "hard_floor":
        return np.maximum(radii, radius_floor)
    if normalized_profile == "plummer":
        return np.sqrt(radii**2 + radius_floor**2)
    if normalized_profile == "shifted":
        return radii + radius_floor
    raise AssertionError(f"unhandled nuclear profile {normalized_profile!r}")


def gaussian_core_counterterm(
    radii: np.ndarray,
    d: int,
    *,
    coupling: float,
    counterterm_strength: float = 0.0,
    counterterm_radius: float | None = None,
) -> np.ndarray:
    if counterterm_strength == 0.0:
        return np.zeros_like(radii, dtype=float)
    effective_radius = max(
        float(counterterm_radius) if counterterm_radius is not None else 1.0,
        1.0e-12,
    )
    amplitude = float(counterterm_strength) * float(coupling)
    if d >= 3:
        amplitude /= effective_radius ** (d - 2)
    return amplitude * np.exp(-np.square(radii / effective_radius))


def radial_shell_counterterm(
    radii: np.ndarray,
    d: int,
    *,
    coupling: float,
    shell_strength: float = 0.0,
    shell_radius: float | None = None,
    shell_width: float | None = None,
) -> np.ndarray:
    if shell_strength == 0.0:
        return np.zeros_like(radii, dtype=float)
    effective_radius = max(
        float(shell_radius) if shell_radius is not None else 1.0,
        1.0e-12,
    )
    effective_width = max(
        float(shell_width) if shell_width is not None else effective_radius,
        1.0e-12,
    )
    amplitude = float(shell_strength) * float(coupling)
    if d >= 3:
        amplitude /= max(effective_radius, effective_width) ** (d - 2)
    shell_distance = (radii - effective_radius) / effective_width
    return amplitude * np.exp(-0.5 * np.square(shell_distance))


def nuclear_potential_from_radii(
    radii: np.ndarray,
    d: int,
    *,
    coupling: float,
    softening_radius: float = 1.0,
    profile: str = "hard_floor",
) -> np.ndarray:
    radius_floor = max(float(softening_radius), 1.0e-12)
    normalized_profile = normalize_nuclear_profile(profile)
    if normalized_profile == "hard_floor":
        regularized_radii = np.maximum(radii, radius_floor)
        if d == 2:
            return -float(coupling) * np.log(regularized_radii)
        return -float(coupling) / regularized_radii ** (d - 2)
    if normalized_profile == "plummer":
        regularized_radii = np.sqrt(radii**2 + radius_floor**2)
        if d == 2:
            return -float(coupling) * np.log(regularized_radii)
        return -float(coupling) / regularized_radii ** (d - 2)
    if normalized_profile == "shifted":
        regularized_radii = radii + radius_floor
        if d == 2:
            return -float(coupling) * np.log(regularized_radii)
        return -float(coupling) / regularized_radii ** (d - 2)
    if d != 3:
        raise ValueError(
            f"nuclear profile {normalized_profile!r} is only implemented for d=3"
        )
    if normalized_profile == "erf_softcore":
        safe_radii = np.maximum(radii, 1.0e-12)
        values = (
            -float(coupling)
            * erf(safe_radii / (np.sqrt(2.0) * radius_floor))
            / safe_radii
        )
        return np.where(
            radii > 1.0e-12,
            values,
            -float(coupling) * np.sqrt(2.0 / np.pi) / radius_floor,
        )
    if normalized_profile == "exp_softcore":
        safe_radii = np.maximum(radii, 1.0e-12)
        values = (
            -float(coupling)
            * (1.0 - np.exp(-safe_radii / radius_floor))
            / safe_radii
        )
        return np.where(
            radii > 1.0e-12,
            values,
            -float(coupling) / radius_floor,
        )
    if normalized_profile == "tanh_softcore":
        safe_radii = np.maximum(radii, 1.0e-12)
        values = (
            -float(coupling)
            * np.tanh(safe_radii / radius_floor)
            / safe_radii
        )
        return np.where(
            radii > 1.0e-12,
            values,
            -float(coupling) / radius_floor,
        )
    if normalized_profile == "gaussian_floor":
        smooth_floor = radius_floor * np.exp(-0.5 * np.square(radii / radius_floor))
        regularized_radii = radii + smooth_floor
        return -float(coupling) / np.maximum(regularized_radii, 1.0e-12)
    raise AssertionError(f"unhandled nuclear profile {normalized_profile!r}")


def repulsion_potential_from_distances(
    distances: np.ndarray,
    d: int,
    *,
    coupling: float,
    softening_radius: float = 1.0,
    profile: str = "hard_floor",
) -> np.ndarray:
    radius_floor = max(float(softening_radius), 1.0e-12)
    normalized_profile = normalize_repulsion_profile(profile)
    if normalized_profile == "hard_floor":
        regularized_distances = np.maximum(distances, radius_floor)
        if d == 2:
            return float(coupling) * np.log(regularized_distances)
        return float(coupling) / regularized_distances ** (d - 2)
    if normalized_profile == "plummer":
        regularized_distances = np.sqrt(distances**2 + radius_floor**2)
        if d == 2:
            return float(coupling) * np.log(regularized_distances)
        return float(coupling) / regularized_distances ** (d - 2)
    if d != 3:
        raise ValueError(
            f"repulsion profile {normalized_profile!r} is only implemented for d=3"
        )
    safe_distances = np.maximum(distances, 1.0e-12)
    if normalized_profile == "erf_softcore":
        values = (
            float(coupling)
            * erf(safe_distances / (np.sqrt(2.0) * radius_floor))
            / safe_distances
        )
        return np.where(
            distances > 1.0e-12,
            values,
            float(coupling) * np.sqrt(2.0 / np.pi) / radius_floor,
        )
    if normalized_profile == "exp_softcore":
        values = (
            float(coupling)
            * (1.0 - np.exp(-safe_distances / radius_floor))
            / safe_distances
        )
        return np.where(
            distances > 1.0e-12,
            values,
            float(coupling) / radius_floor,
        )
    raise AssertionError(f"unhandled repulsion profile {normalized_profile!r}")


def subcell_sample_offsets(
    dimension: int,
    *,
    lattice_spacing: float = 1.0,
    quadrature_order: int = 1,
) -> np.ndarray:
    order = int(quadrature_order)
    if order < 1:
        raise ValueError(f"quadrature_order must be >= 1, got {quadrature_order!r}")
    if order == 1:
        return np.zeros((1, dimension), dtype=float)
    axis_offsets = (
        (np.arange(order, dtype=float) + 0.5) / float(order) - 0.5
    ) * float(lattice_spacing)
    mesh = np.meshgrid(*([axis_offsets] * dimension), indexing="ij")
    return np.stack(mesh, axis=-1).reshape(-1, dimension)


def subcell_difference_offsets(
    dimension: int,
    *,
    lattice_spacing: float = 1.0,
    quadrature_order: int = 1,
) -> tuple[np.ndarray, np.ndarray]:
    sample_offsets = subcell_sample_offsets(
        dimension,
        lattice_spacing=lattice_spacing,
        quadrature_order=quadrature_order,
    )
    if len(sample_offsets) == 1:
        return sample_offsets.copy(), np.ones(1, dtype=float)
    difference_weights: dict[tuple[float, ...], float] = {}
    inverse_weight = 1.0 / float(len(sample_offsets) ** 2)
    for left in sample_offsets:
        for right in sample_offsets:
            key = tuple(np.round(left - right, 12))
            difference_weights[key] = (
                difference_weights.get(key, 0.0) + inverse_weight
            )
    ordered_items = sorted(difference_weights.items())
    return (
        np.asarray([item[0] for item in ordered_items], dtype=float),
        np.asarray([item[1] for item in ordered_items], dtype=float),
    )


def softened_coulomb_potential_nd(
    sizes: tuple[int, ...],
    d: int,
    *,
    coupling: float,
    lattice_spacing: float = 1.0,
    softening_radius: float = 1.0,
    profile: str = "hard_floor",
    counterterm_strength: float = 0.0,
    counterterm_radius: float | None = None,
    shell_strength: float = 0.0,
    shell_radius: float | None = None,
    shell_width: float | None = None,
    quadrature_order: int = 1,
) -> np.ndarray:
    geometry = lattice_geometry(sizes)
    centered_coordinates = (
        geometry["coordinates"] - geometry["center"][np.newaxis, :]
    ) * float(lattice_spacing)
    sample_offsets = subcell_sample_offsets(
        d,
        lattice_spacing=float(lattice_spacing),
        quadrature_order=quadrature_order,
    )
    sampled_coordinates = (
        centered_coordinates[:, np.newaxis, :] + sample_offsets[np.newaxis, :, :]
    )
    sampled_radii = np.sqrt(np.sum(sampled_coordinates**2, axis=2))
    base_potential = np.mean(
        nuclear_potential_from_radii(
            sampled_radii,
            d,
            coupling=coupling,
            softening_radius=softening_radius,
            profile=profile,
        ),
        axis=1,
    )
    counterterm = gaussian_core_counterterm(
        sampled_radii,
        d,
        coupling=float(coupling),
        counterterm_strength=float(counterterm_strength),
        counterterm_radius=counterterm_radius,
    )
    shell_counterterm = radial_shell_counterterm(
        sampled_radii,
        d,
        coupling=float(coupling),
        shell_strength=float(shell_strength),
        shell_radius=shell_radius,
        shell_width=shell_width,
    )
    return (
        base_potential
        + np.mean(counterterm, axis=1)
        + np.mean(shell_counterterm, axis=1)
    )


def pairwise_distances(coordinates: np.ndarray) -> np.ndarray:
    deltas = coordinates[:, np.newaxis, :] - coordinates[np.newaxis, :, :]
    return np.sqrt(np.sum(deltas**2, axis=2))


def correlated_pair_weight(
    distance: float,
    *,
    correlation_radius: float,
    profile: str = "gaussian",
) -> float:
    effective_radius = max(float(correlation_radius), 1.0e-12)
    normalized_profile = normalize_correlated_pair_profile(profile)
    if normalized_profile == "gaussian":
        return float(np.exp(-0.5 * (float(distance) / effective_radius) ** 2))
    if normalized_profile == "exponential":
        return float(np.exp(-float(distance) / effective_radius))
    raise AssertionError(f"unhandled correlated pair profile {normalized_profile!r}")


def build_short_range_pair_kernel(
    sizes: tuple[int, ...],
    *,
    lattice_spacing: float = 1.0,
    correlation_radius: float = 1.0,
    strength: float = 1.0,
    profile: str = "gaussian",
    cutoff_multiplier: float = 3.0,
) -> sparse.csr_matrix:
    normalized_profile = normalize_correlated_pair_profile(profile)
    dimension = len(sizes)
    max_distance = max(float(correlation_radius), 1.0e-12) * float(cutoff_multiplier)
    max_steps = max(0, int(np.ceil(max_distance / float(lattice_spacing))))
    coordinates = lattice_geometry(sizes)["coordinates"].astype(int)
    data_parts: list[np.ndarray] = []
    row_parts: list[np.ndarray] = []
    col_parts: list[np.ndarray] = []
    for offset in np.ndindex(*([2 * max_steps + 1] * dimension)):
        shift = np.array([value - max_steps for value in offset], dtype=int)
        distance = float(np.linalg.norm(shift.astype(float) * float(lattice_spacing)))
        if distance > max_distance:
            continue
        weight = float(strength) * correlated_pair_weight(
            distance,
            correlation_radius=float(correlation_radius),
            profile=normalized_profile,
        )
        if weight == 0.0:
            continue
        shifted_coordinates = coordinates + shift[np.newaxis, :]
        valid_mask = np.ones(len(coordinates), dtype=bool)
        for axis, size in enumerate(sizes):
            valid_mask &= shifted_coordinates[:, axis] >= 0
            valid_mask &= shifted_coordinates[:, axis] < int(size)
        if not np.any(valid_mask):
            continue
        left = coordinates[valid_mask]
        right = shifted_coordinates[valid_mask]
        rows = np.ravel_multi_index(left.T, sizes)
        cols = np.ravel_multi_index(right.T, sizes)
        row_parts.append(rows.astype(np.int64, copy=False))
        col_parts.append(cols.astype(np.int64, copy=False))
        data_parts.append(
            np.full(len(rows), weight, dtype=float)
        )
    if not data_parts:
        n_sites = int(np.prod(sizes))
        return sparse.csr_matrix((n_sites, n_sites))
    kernel = sparse.coo_matrix(
        (
            np.concatenate(data_parts),
            (np.concatenate(row_parts), np.concatenate(col_parts)),
        ),
        shape=(int(np.prod(sizes)), int(np.prod(sizes))),
    ).tocsr()
    return 0.5 * (kernel + kernel.T)


def build_repulsion_kernel(
    sizes: tuple[int, ...],
    d: int,
    coupling: float,
    *,
    lattice_spacing: float = 1.0,
    softening_radius: float = 1.0,
    profile: str = "hard_floor",
    quadrature_order: int = 1,
    block_size: int = 256,
) -> np.ndarray:
    geometry = lattice_geometry(sizes)
    centered_coordinates = (
        geometry["coordinates"] - geometry["center"][np.newaxis, :]
    ) * float(lattice_spacing)
    normalized_profile = normalize_repulsion_profile(profile)
    if quadrature_order == 1:
        distances = pairwise_distances(centered_coordinates)
        return repulsion_potential_from_distances(
            distances,
            d,
            coupling=coupling,
            softening_radius=softening_radius,
            profile=normalized_profile,
        )

    difference_offsets, weights = subcell_difference_offsets(
        d,
        lattice_spacing=float(lattice_spacing),
        quadrature_order=quadrature_order,
    )
    n_sites = len(centered_coordinates)
    kernel = np.zeros((n_sites, n_sites), dtype=float)
    for start in range(0, n_sites, int(block_size)):
        stop = min(start + int(block_size), n_sites)
        left_coordinates = centered_coordinates[start:stop]
        base_deltas = left_coordinates[:, np.newaxis, :] - centered_coordinates[np.newaxis, :, :]
        block_kernel = np.zeros((stop - start, n_sites), dtype=float)
        for offset, weight in zip(difference_offsets, weights, strict=True):
            distances = np.sqrt(
                np.sum((base_deltas + offset[np.newaxis, np.newaxis, :]) ** 2, axis=2)
            )
            block_kernel += weight * repulsion_potential_from_distances(
                distances,
                d,
                coupling=coupling,
                softening_radius=softening_radius,
                profile=normalized_profile,
            )
        kernel[start:stop] = block_kernel
    return kernel


def solve_one_body_bound_orbitals(
    *,
    dimension: int = 3,
    coupling: float | None = None,
    max_orbitals: int | None = None,
    max_virtual_orbitals: int = 0,
    n_eig: int = 40,
    lattice_spacing: float = 1.0,
    softening_radius: float = 1.0,
    nuclear_profile: str = "hard_floor",
    nuclear_quadrature_order: int = 1,
    nuclear_counterterm_strength: float = 0.0,
    nuclear_counterterm_radius: float | None = None,
    nuclear_shell_strength: float = 0.0,
    nuclear_shell_radius: float | None = None,
    nuclear_shell_width: float | None = None,
    kinetic_stencil: str = "three_point",
    custom_sizes: tuple[int, ...] | None = None,
) -> dict[str, Any]:
    dimension, _default_sizes, reference_coupling = find_bound_state_config(dimension)
    sizes = resolve_lattice_sizes(dimension, custom_sizes)
    if coupling is None:
        coupling = reference_coupling
    if nuclear_counterterm_radius is None and nuclear_counterterm_strength != 0.0:
        nuclear_counterterm_radius = softening_radius
    if nuclear_shell_radius is None and nuclear_shell_strength != 0.0:
        nuclear_shell_radius = softening_radius
    if nuclear_shell_width is None and nuclear_shell_strength != 0.0:
        nuclear_shell_width = softening_radius
    geometry = lattice_geometry(sizes)
    laplacian = build_scaled_laplacian(
        sizes,
        lattice_spacing=lattice_spacing,
        kinetic_stencil=kinetic_stencil,
    )
    potential = softened_coulomb_potential_nd(
        sizes,
        dimension,
        coupling=coupling,
        lattice_spacing=lattice_spacing,
        softening_radius=softening_radius,
        profile=nuclear_profile,
        counterterm_strength=nuclear_counterterm_strength,
        counterterm_radius=nuclear_counterterm_radius,
        shell_strength=nuclear_shell_strength,
        shell_radius=nuclear_shell_radius,
        shell_width=nuclear_shell_width,
        quadrature_order=nuclear_quadrature_order,
    )
    hamiltonian = laplacian + sparse.diags(potential, 0, format="csr")
    bound_states = count_bound_states(hamiltonian, n_eig=n_eig)
    eigenvalues = np.asarray(bound_states["eigenvalues"], dtype=float)
    eigenvectors = np.real_if_close(bound_states["eigenvectors"]).astype(float)
    negative_indices = [int(index) for index, value in enumerate(eigenvalues) if value < 0.0]
    selected_negative_indices = list(negative_indices)
    if max_orbitals is not None:
        selected_negative_indices = selected_negative_indices[:max_orbitals]
    if not selected_negative_indices:
        raise ValueError(
            f"no negative one-body orbitals found for d={dimension}, coupling={coupling}"
        )
    positive_indices = [int(index) for index, value in enumerate(eigenvalues) if value >= 0.0]
    selected_virtual_indices: list[int] = []
    if int(max_virtual_orbitals) > 0:
        selected_virtual_indices = positive_indices[: int(max_virtual_orbitals)]
    selected_indices = selected_negative_indices + selected_virtual_indices

    selected_energies = eigenvalues[selected_indices]
    selected_orbitals = eigenvectors[:, selected_indices]
    orbital_rows: list[dict[str, Any]] = []
    for orbital_slot, eigen_index in enumerate(selected_indices):
        orbital = selected_orbitals[:, orbital_slot]
        localization = analyze_localization(orbital, sizes, dimension)
        probability = np.abs(orbital) ** 2
        probability /= np.sum(probability)
        mean_radius = float(np.sum(probability * geometry["radii"]))
        variance_radius = float(
            np.sum(probability * (geometry["radii"] - mean_radius) ** 2)
        )
        orbital_rows.append(
            {
                "orbital_index": orbital_slot,
                "eigen_index": eigen_index,
                "energy": float(selected_energies[orbital_slot]),
                "mean_radius": mean_radius,
                "radius_std": float(np.sqrt(max(variance_radius, 0.0))),
                "ipr": float(localization["ipr"]),
                "center_weight": float(localization["center_weight"]),
                "decay_rate": float(localization["decay_rate"]),
                "genuinely_localized": bool(localization["genuinely_localized"]),
                "continuum_virtual": bool(eigen_index in selected_virtual_indices),
                "selected_role": (
                    "virtual"
                    if eigen_index in selected_virtual_indices
                    else "bound"
                ),
                "physical_bound": bool(
                    selected_energies[orbital_slot] < 0.0
                    and localization["genuinely_localized"]
                    and not localization["fall_to_center"]
                ),
            }
        )

    return {
        "dimension": dimension,
        "sizes": sizes,
        "reference_coupling": float(reference_coupling),
        "coupling": float(coupling),
        "lattice_spacing": float(lattice_spacing),
        "softening_radius": float(softening_radius),
        "max_virtual_orbitals": int(max_virtual_orbitals),
        "kinetic_stencil": normalize_kinetic_stencil(kinetic_stencil),
        "nuclear_profile": normalize_nuclear_profile(nuclear_profile),
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
        "n_bound_total": int(bound_states["n_bound"]),
        "n_selected_orbitals": len(selected_indices),
        "n_negative_selected": len(selected_negative_indices),
        "n_virtual_selected": len(selected_virtual_indices),
        "orbital_rows": orbital_rows,
        "orbital_energies": selected_energies,
        "orbital_matrix": selected_orbitals,
        "ground_energy": float(selected_energies[0]),
    }


def orbital_pair_functions(orbital_matrix: np.ndarray) -> np.ndarray:
    pair_functions = np.einsum("xp,xq->xpq", orbital_matrix, orbital_matrix)
    n_sites, n_orbitals, _ = pair_functions.shape
    return pair_functions.reshape(n_sites, n_orbitals * n_orbitals)


def pair_operator_tensor(
    pair_functions: np.ndarray,
    n_orbitals: int,
    *,
    kernel_matrix: np.ndarray | None = None,
) -> np.ndarray:
    if kernel_matrix is None:
        pair_matrix = pair_functions.T @ pair_functions
    else:
        pair_matrix = pair_functions.T @ (kernel_matrix @ pair_functions)
    pair_matrix = 0.5 * (pair_matrix + pair_matrix.T)
    return pair_matrix.reshape(n_orbitals, n_orbitals, n_orbitals, n_orbitals)


def singlet_basis(n_orbitals: int) -> list[tuple[int, int]]:
    return [(left, right) for left in range(n_orbitals) for right in range(left, n_orbitals)]


def triplet_basis(n_orbitals: int) -> list[tuple[int, int]]:
    return [(left, right) for left in range(n_orbitals) for right in range(left + 1, n_orbitals)]


def configuration_label(pair: tuple[int, int]) -> str:
    left, right = pair
    if left == right:
        return f"{left}{left}"
    return f"{left}{right}"


def sector_operator_matrix(
    basis: list[tuple[int, int]],
    operator_tensor: np.ndarray,
    *,
    sector: str,
) -> np.ndarray:
    matrix = np.zeros((len(basis), len(basis)), dtype=float)
    for row_index, (left_i, right_i) in enumerate(basis):
        for col_index, (left_j, right_j) in enumerate(basis):
            if sector == "singlet":
                norm = np.sqrt(
                    (1 + int(left_i == right_i)) * (1 + int(left_j == right_j))
                )
                value = (
                    operator_tensor[left_i, left_j, right_i, right_j]
                    + operator_tensor[left_i, right_j, right_i, left_j]
                ) / norm
            elif sector == "triplet":
                value = (
                    operator_tensor[left_i, left_j, right_i, right_j]
                    - operator_tensor[left_i, right_j, right_i, left_j]
                )
            else:
                raise ValueError(f"unsupported sector {sector!r}")
            matrix[row_index, col_index] = float(value)
    return 0.5 * (matrix + matrix.T)


def sector_one_body_diagonal(
    basis: list[tuple[int, int]],
    orbital_energies: np.ndarray,
) -> np.ndarray:
    return np.array(
        [
            float(orbital_energies[left] + orbital_energies[right])
            for left, right in basis
        ],
        dtype=float,
    )


def sector_orbital_occupancies(
    basis: list[tuple[int, int]],
    amplitudes: np.ndarray,
    n_orbitals: int,
) -> list[float]:
    weights = np.abs(amplitudes) ** 2
    occupancies = np.zeros(n_orbitals, dtype=float)
    for weight, (left, right) in zip(weights, basis, strict=True):
        if left == right:
            occupancies[left] += 2.0 * weight
        else:
            occupancies[left] += weight
            occupancies[right] += weight
    return [float(value) for value in occupancies]


def dominant_configurations(
    basis: list[tuple[int, int]],
    amplitudes: np.ndarray,
    *,
    top_k: int = 6,
) -> list[dict[str, Any]]:
    rows = []
    for weight, amplitude, pair in sorted(
        zip(np.abs(amplitudes) ** 2, amplitudes, basis, strict=True),
        key=lambda row: row[0],
        reverse=True,
    )[:top_k]:
        rows.append(
            {
                "configuration": configuration_label(pair),
                "orbitals": [int(pair[0]), int(pair[1])],
                "weight": float(weight),
                "amplitude": float(np.real_if_close(amplitude)),
            }
        )
    return rows


def solve_sector(
    *,
    orbital_energies: np.ndarray,
    interaction_tensor: np.ndarray,
    contact_tensor: np.ndarray,
    sector: str,
) -> dict[str, Any]:
    basis = singlet_basis(len(orbital_energies)) if sector == "singlet" else triplet_basis(len(orbital_energies))
    if not basis:
        return {
            "sector": sector,
            "basis_size": 0,
            "lowest_energies": [],
            "ground_energy": None,
            "one_body_energy_expectation": None,
            "interaction_energy_expectation": None,
            "contact_probability": None,
            "orbital_occupancies": [],
            "dominant_configurations": [],
        }

    one_body_diagonal = sector_one_body_diagonal(basis, orbital_energies)
    interaction_matrix = sector_operator_matrix(
        basis,
        interaction_tensor,
        sector=sector,
    )
    contact_matrix = sector_operator_matrix(
        basis,
        contact_tensor,
        sector=sector,
    )
    hamiltonian = np.diag(one_body_diagonal) + interaction_matrix
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    ground_vector = eigenvectors[:, 0]
    one_body_energy_expectation = float(
        np.sum((np.abs(ground_vector) ** 2) * one_body_diagonal)
    )
    interaction_energy_expectation = float(
        np.real_if_close(ground_vector.T @ interaction_matrix @ ground_vector)
    )
    contact_probability = float(
        np.real_if_close(ground_vector.T @ contact_matrix @ ground_vector)
    )
    return {
        "sector": sector,
        "basis_size": len(basis),
        "spin_multiplicity": 1 if sector == "singlet" else 3,
        "lowest_energies": [float(value) for value in eigenvalues[: min(8, len(eigenvalues))]],
        "ground_energy": float(eigenvalues[0]),
        "one_body_energy_expectation": one_body_energy_expectation,
        "interaction_energy_expectation": interaction_energy_expectation,
        "contact_probability": contact_probability,
        "orbital_occupancies": sector_orbital_occupancies(
            basis,
            ground_vector,
            len(orbital_energies),
        ),
        "dominant_configurations": dominant_configurations(basis, ground_vector),
    }


def sweep_two_electron_basis(
    *,
    orbital_energies: np.ndarray,
    interaction_tensor: np.ndarray,
    contact_tensor: np.ndarray,
    basis_sizes: tuple[int, ...],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for basis_size in basis_sizes:
        if basis_size < 1 or basis_size > len(orbital_energies):
            continue
        singlet = solve_sector(
            orbital_energies=orbital_energies[:basis_size],
            interaction_tensor=interaction_tensor[:basis_size, :basis_size, :basis_size, :basis_size],
            contact_tensor=contact_tensor[:basis_size, :basis_size, :basis_size, :basis_size],
            sector="singlet",
        )
        triplet = solve_sector(
            orbital_energies=orbital_energies[:basis_size],
            interaction_tensor=interaction_tensor[:basis_size, :basis_size, :basis_size, :basis_size],
            contact_tensor=contact_tensor[:basis_size, :basis_size, :basis_size, :basis_size],
            sector="triplet",
        )
        ground_energy = singlet["ground_energy"]
        triplet_energy = triplet["ground_energy"]
        ion_reference = float(orbital_energies[0])
        rows.append(
            {
                "spatial_orbital_count": basis_size,
                "singlet_ground_energy": ground_energy,
                "triplet_ground_energy": triplet_energy,
                "ionization_energy": (
                    float(ion_reference - ground_energy)
                    if ground_energy is not None
                    else None
                ),
                "singlet_triplet_gap": (
                    float(triplet_energy - ground_energy)
                    if ground_energy is not None and triplet_energy is not None
                    else None
                ),
            }
        )
    return rows


def one_body_summary(one_body_result: dict[str, Any]) -> dict[str, Any]:
    return {
        "dimension": int(one_body_result["dimension"]),
        "sizes": [int(size) for size in one_body_result["sizes"]],
        "reference_coupling": float(one_body_result["reference_coupling"]),
        "coupling": float(one_body_result["coupling"]),
        "lattice_spacing": float(one_body_result["lattice_spacing"]),
        "softening_radius": float(one_body_result["softening_radius"]),
        "max_virtual_orbitals": int(one_body_result["max_virtual_orbitals"]),
        "kinetic_stencil": str(one_body_result["kinetic_stencil"]),
        "nuclear_profile": str(one_body_result["nuclear_profile"]),
        "nuclear_quadrature_order": int(one_body_result["nuclear_quadrature_order"]),
        "nuclear_counterterm_strength": float(
            one_body_result["nuclear_counterterm_strength"]
        ),
        "nuclear_counterterm_radius": (
            float(one_body_result["nuclear_counterterm_radius"])
            if one_body_result["nuclear_counterterm_radius"] is not None
            else None
        ),
        "nuclear_shell_strength": float(one_body_result["nuclear_shell_strength"]),
        "nuclear_shell_radius": (
            float(one_body_result["nuclear_shell_radius"])
            if one_body_result["nuclear_shell_radius"] is not None
            else None
        ),
        "nuclear_shell_width": (
            float(one_body_result["nuclear_shell_width"])
            if one_body_result["nuclear_shell_width"] is not None
            else None
        ),
        "n_bound_total": int(one_body_result["n_bound_total"]),
        "n_selected_orbitals": int(one_body_result["n_selected_orbitals"]),
        "n_negative_selected": int(one_body_result["n_negative_selected"]),
        "n_virtual_selected": int(one_body_result["n_virtual_selected"]),
        "ground_energy": float(one_body_result["ground_energy"]),
        "orbital_rows": list(one_body_result["orbital_rows"]),
    }


def solve_two_electron_atomic_model(
    *,
    dimension: int = 3,
    nuclear_charge: float = 2.0,
    reference_coupling: float | None = None,
    nuclear_coupling: float | None = None,
    electron_repulsion_coupling: float | None = None,
    lattice_spacing: float = 1.0,
    nuclear_softening_radius: float | None = None,
    repulsion_softening_radius: float | None = None,
    nuclear_profile: str = "hard_floor",
    nuclear_quadrature_order: int = 1,
    repulsion_profile: str = "hard_floor",
    repulsion_quadrature_order: int = 1,
    nuclear_counterterm_strength: float = 0.0,
    nuclear_counterterm_radius: float | None = None,
    nuclear_shell_strength: float = 0.0,
    nuclear_shell_radius: float | None = None,
    nuclear_shell_width: float | None = None,
    kinetic_stencil: str = "three_point",
    max_orbitals: int = 16,
    max_virtual_orbitals: int = 0,
    n_eig: int = 40,
    basis_sweep: tuple[int, ...] = (4, 6, 8, 10, 12, 14, 16),
    custom_sizes: tuple[int, ...] | None = None,
) -> dict[str, Any]:
    dimension, _sizes, config_reference_coupling = find_bound_state_config(dimension)
    active_sizes = resolve_lattice_sizes(dimension, custom_sizes)
    if reference_coupling is None:
        reference_coupling = config_reference_coupling
    if nuclear_coupling is None:
        nuclear_coupling = reference_coupling * nuclear_charge
    if electron_repulsion_coupling is None:
        electron_repulsion_coupling = reference_coupling
    if nuclear_softening_radius is None:
        nuclear_softening_radius = lattice_spacing
    if repulsion_softening_radius is None:
        repulsion_softening_radius = lattice_spacing
    if nuclear_counterterm_radius is None and nuclear_counterterm_strength != 0.0:
        nuclear_counterterm_radius = nuclear_softening_radius
    if nuclear_shell_radius is None and nuclear_shell_strength != 0.0:
        nuclear_shell_radius = nuclear_softening_radius
    if nuclear_shell_width is None and nuclear_shell_strength != 0.0:
        nuclear_shell_width = nuclear_softening_radius

    hydrogen_reference = solve_one_body_bound_orbitals(
        dimension=dimension,
        coupling=reference_coupling,
        max_orbitals=max_orbitals,
        max_virtual_orbitals=max_virtual_orbitals,
        n_eig=n_eig,
        lattice_spacing=lattice_spacing,
        softening_radius=nuclear_softening_radius,
        nuclear_profile=nuclear_profile,
        nuclear_quadrature_order=nuclear_quadrature_order,
        nuclear_counterterm_strength=nuclear_counterterm_strength,
        nuclear_counterterm_radius=nuclear_counterterm_radius,
        nuclear_shell_strength=nuclear_shell_strength,
        nuclear_shell_radius=nuclear_shell_radius,
        nuclear_shell_width=nuclear_shell_width,
        kinetic_stencil=kinetic_stencil,
        custom_sizes=active_sizes,
    )
    helium_ion = solve_one_body_bound_orbitals(
        dimension=dimension,
        coupling=nuclear_coupling,
        max_orbitals=max_orbitals,
        max_virtual_orbitals=max_virtual_orbitals,
        n_eig=n_eig,
        lattice_spacing=lattice_spacing,
        softening_radius=nuclear_softening_radius,
        nuclear_profile=nuclear_profile,
        nuclear_quadrature_order=nuclear_quadrature_order,
        nuclear_counterterm_strength=nuclear_counterterm_strength,
        nuclear_counterterm_radius=nuclear_counterterm_radius,
        nuclear_shell_strength=nuclear_shell_strength,
        nuclear_shell_radius=nuclear_shell_radius,
        nuclear_shell_width=nuclear_shell_width,
        kinetic_stencil=kinetic_stencil,
        custom_sizes=active_sizes,
    )
    orbital_energies = np.asarray(helium_ion["orbital_energies"], dtype=float)
    orbital_matrix = np.asarray(helium_ion["orbital_matrix"], dtype=float)
    repulsion_kernel = build_repulsion_kernel(
        helium_ion["sizes"],
        dimension,
        coupling=float(electron_repulsion_coupling),
        lattice_spacing=lattice_spacing,
        softening_radius=repulsion_softening_radius,
        profile=repulsion_profile,
        quadrature_order=repulsion_quadrature_order,
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
    singlet = solve_sector(
        orbital_energies=orbital_energies,
        interaction_tensor=repulsion_tensor,
        contact_tensor=contact_tensor,
        sector="singlet",
    )
    triplet = solve_sector(
        orbital_energies=orbital_energies,
        interaction_tensor=repulsion_tensor,
        contact_tensor=contact_tensor,
        sector="triplet",
    )
    ion_ground_energy = float(orbital_energies[0])
    singlet_ground_energy = singlet["ground_energy"]
    triplet_ground_energy = triplet["ground_energy"]
    noninteracting_double_occupancy_energy = float(2.0 * ion_ground_energy)
    basis_sweep_rows = sweep_two_electron_basis(
        orbital_energies=orbital_energies,
        interaction_tensor=repulsion_tensor,
        contact_tensor=contact_tensor,
        basis_sizes=tuple(sorted(set(int(size) for size in basis_sweep if size > 0))),
    )
    return {
        "model": {
            "dimension": int(dimension),
            "reference_coupling": float(reference_coupling),
            "nuclear_charge": float(nuclear_charge),
            "nuclear_coupling": float(nuclear_coupling),
            "electron_repulsion_coupling": float(electron_repulsion_coupling),
            "lattice_spacing": float(lattice_spacing),
            "nuclear_softening_radius": float(nuclear_softening_radius),
            "repulsion_softening_radius": float(repulsion_softening_radius),
            "nuclear_profile": normalize_nuclear_profile(nuclear_profile),
            "nuclear_quadrature_order": int(nuclear_quadrature_order),
            "repulsion_profile": normalize_repulsion_profile(repulsion_profile),
            "repulsion_quadrature_order": int(repulsion_quadrature_order),
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
            "kinetic_stencil": normalize_kinetic_stencil(kinetic_stencil),
            "max_orbitals": int(max_orbitals),
            "max_virtual_orbitals": int(max_virtual_orbitals),
            "n_eig": int(n_eig),
            "basis_sweep": [int(size) for size in basis_sweep],
            "custom_sizes": [int(size) for size in active_sizes],
        },
        "hydrogen_reference": one_body_summary(hydrogen_reference),
        "helium_ion_reference": one_body_summary(helium_ion),
        "two_electron": {
            "spatial_orbital_count": int(len(orbital_energies)),
            "electron_repulsion_present": True,
            "antisymmetry_present": True,
            "spin_sectors_present": ["singlet", "triplet"],
            "singlet": singlet,
            "triplet": triplet,
            "basis_sweep": basis_sweep_rows,
            "noninteracting_double_occupancy_energy": noninteracting_double_occupancy_energy,
            "interaction_shift_from_double_occupancy": (
                float(singlet_ground_energy - noninteracting_double_occupancy_energy)
                if singlet_ground_energy is not None
                else None
            ),
            "ionization_energy": (
                float(ion_ground_energy - singlet_ground_energy)
                if singlet_ground_energy is not None
                else None
            ),
            "triplet_ionization_energy": (
                float(ion_ground_energy - triplet_ground_energy)
                if triplet_ground_energy is not None
                else None
            ),
            "singlet_triplet_gap": (
                float(triplet_ground_energy - singlet_ground_energy)
                if singlet_ground_energy is not None and triplet_ground_energy is not None
                else None
            ),
            "helium_like_bound": bool(
                singlet_ground_energy is not None and singlet_ground_energy < ion_ground_energy
            ),
            "spin_ground_sector": (
                "singlet"
                if triplet_ground_energy is None or singlet_ground_energy <= triplet_ground_energy
                else "triplet"
            ),
        },
    }
