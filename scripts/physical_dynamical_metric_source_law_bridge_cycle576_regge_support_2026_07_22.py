#!/usr/bin/env python3
"""Actual-Regge route support for the Cycle-576 primary runner.

This ordinary-import helper contains the unchanged finite Regge construction
used by Route A. It is packaging support only and introduces no independent
claim, authority, or audit status.
"""

from __future__ import annotations

from functools import lru_cache
from itertools import permutations, product
import math

import numpy as np
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge


REGGE_UPDATE_SCALE = 0.025
SOURCE_COUPLING = 0.17
UPDATE_PARAMETER = 0.035


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for order in permutations(range(3)):
        permutation = np.zeros((3, 3), dtype=int)
        for row, column in enumerate(order):
            permutation[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    frames.sort(key=lambda item: tuple(item.reshape(-1)))
    return tuple(frames)


FRAMES = proper_cubic_frames()
FRAME_LOOKUP = {tuple(frame.reshape(-1)): index for index, frame in enumerate(FRAMES)}


def lift_frame(frame: np.ndarray) -> np.ndarray:
    result = np.eye(4, dtype=int)
    result[:3, :3] = frame
    return result


def metric_matrix(values: np.ndarray) -> np.ndarray:
    result = np.zeros((4, 4), dtype=complex)
    for value, (left, right) in zip(values, regge.HCOMPS):
        result[left, right] = value
        result[right, left] = value
    return result


def metric_vector(matrix: np.ndarray) -> np.ndarray:
    return np.asarray([matrix[left, right] for left, right in regge.HCOMPS])


def metric_representation(frame: np.ndarray) -> np.ndarray:
    lifted = lift_frame(frame)
    representation = np.zeros((10, 10), dtype=float)
    for column in range(10):
        basis = np.zeros(10)
        basis[column] = 1
        representation[:, column] = metric_vector(
            lifted @ metric_matrix(basis) @ lifted.T
        ).real
    return representation


METRIC_REPS = tuple(metric_representation(frame) for frame in FRAMES)
LIFTED_FRAMES = tuple(lift_frame(frame) for frame in FRAMES)


def momentum_key(momentum: np.ndarray) -> tuple[float, ...]:
    return tuple(float(round(value, 13)) for value in momentum)


@lru_cache(maxsize=None)
def base_edge_hessian_cached(key: tuple[float, ...]) -> np.ndarray:
    return regge.bloch_Q(np.asarray(key, dtype=float))


@lru_cache(maxsize=None)
def base_deficit_source_cached(key: tuple[float, ...]) -> np.ndarray:
    momentum = np.asarray(key, dtype=float)
    source = np.zeros(15, dtype=complex)
    for triangle in regge.TRI_CLASSES:
        source += regge.tri_rows(triangle, momentum)[1]
    return source


def base_edge_hessian(momentum: np.ndarray) -> np.ndarray:
    return base_edge_hessian_cached(momentum_key(momentum)).copy()


def base_deficit_source(momentum: np.ndarray) -> np.ndarray:
    return base_deficit_source_cached(momentum_key(momentum)).copy()


def base_metric_hessian(momentum: np.ndarray) -> np.ndarray:
    metric_map = regge.metric_map(momentum)
    result = metric_map.conj().T @ base_edge_hessian(momentum) @ metric_map
    return (result + result.conj().T) / 2


def frame_averaged_metric_hessian(momentum: np.ndarray) -> np.ndarray:
    result = np.zeros((10, 10), dtype=complex)
    for representation, frame in zip(METRIC_REPS, LIFTED_FRAMES):
        result += representation.T @ base_metric_hessian(frame @ momentum) @ representation
    return result / len(FRAMES)


def base_metric_source_row(momentum: np.ndarray) -> np.ndarray:
    # Fourier row convention: delta(k)=d(k)e(k), e(k)=M(k)h(k).
    return base_deficit_source(momentum) @ regge.metric_map(momentum)


def frame_averaged_source_row(momentum: np.ndarray) -> np.ndarray:
    result = np.zeros(10, dtype=complex)
    for representation, frame in zip(METRIC_REPS, LIFTED_FRAMES):
        result += base_metric_source_row(frame @ momentum) @ representation
    return result / len(FRAMES)


def continuum_gauge_metric(momentum: np.ndarray) -> np.ndarray:
    result = np.zeros((10, 4), dtype=complex)
    for direction in range(4):
        tensor = np.zeros((4, 4), dtype=complex)
        for left in range(4):
            tensor[left, direction] += 1j * momentum[left]
            tensor[direction, left] += 1j * momentum[left]
        result[:, direction] = metric_vector(tensor)
    return result


def frame_sector_permutation(frame: np.ndarray) -> np.ndarray:
    """Active rotation: old sector F moves to F G^{-1}."""
    inverse = frame.T
    dimension = 1 + 24 * 15
    result = np.zeros((dimension, dimension), dtype=float)
    result[0, 0] = 1
    for old, sector in enumerate(FRAMES):
        target = FRAME_LOOKUP[tuple((sector @ inverse).reshape(-1))]
        source_slice = slice(1 + 15 * old, 1 + 15 * (old + 1))
        target_slice = slice(1 + 15 * target, 1 + 15 * (target + 1))
        result[target_slice, source_slice] = np.eye(15)
    return result


FRAME_SECTOR_REPS = tuple(frame_sector_permutation(frame) for frame in FRAMES)


def frame_sector_hamiltonian(
    momentum: np.ndarray,
    *,
    source_amplitude: float = 1.0,
    include_regge: bool = True,
    include_source: bool = True,
) -> np.ndarray:
    dimension = 1 + 24 * 15
    result = np.zeros((dimension, dimension), dtype=complex)
    sources = []
    for index, frame in enumerate(LIFTED_FRAMES):
        local_momentum = frame @ momentum
        block = slice(1 + 15 * index, 1 + 15 * (index + 1))
        if include_regge:
            result[block, block] = REGGE_UPDATE_SCALE * base_edge_hessian(local_momentum)
        sources.append(base_deficit_source(local_momentum))
    joined = np.concatenate(sources)
    if include_source:
        result[0, 1:] = SOURCE_COUPLING * source_amplitude * joined
        result[1:, 0] = np.conj(result[0, 1:])
    return result


def route_a_regge() -> dict:
    directions = (
        np.asarray((1, 0, 0, 0), float),
        np.asarray((1, 1, 0, 0), float) / math.sqrt(2),
        np.asarray((0, 0, 0, 1), float),
        np.asarray((1, 0, 0, 1), float) / math.sqrt(2),
        np.asarray((1, 1, 1, 1), float) / 2,
    )
    small = 1.0e-3
    comparisons = []
    for direction in directions:
        momentum = small * direction
        candidate = frame_averaged_metric_hessian(momentum)
        target = regge.einstein_pairing_4d(momentum)
        coefficient = float(np.vdot(target, candidate).real / np.vdot(target, target).real)
        residual = float(np.linalg.norm(candidate - coefficient * target) / np.linalg.norm(candidate))
        comparisons.append({
            "direction": direction.tolist(),
            "best_fit_coefficient": coefficient,
            "relative_residual": residual,
        })

    generic = np.asarray((0.17, 0.11, 0.07, 0.13))
    candidate = frame_averaged_metric_hessian(generic)
    gauge = continuum_gauge_metric(generic)
    bianchi = float(np.max(abs(candidate @ gauge)))
    source_row = frame_averaged_source_row(generic)
    source_ward = float(np.max(abs(source_row @ gauge)))
    edge_bianchi = 0.0
    deficit_ward = 0.0
    for frame in LIFTED_FRAMES:
        local_momentum = frame @ generic
        edge_bianchi = max(
            edge_bianchi,
            float(np.max(abs(base_edge_hessian(local_momentum) @ regge.gauge_map(local_momentum)))),
        )
        for triangle in regge.TRI_CLASSES:
            deficit = regge.tri_rows(triangle, local_momentum)[1]
            deficit_ward = max(deficit_ward, float(np.max(abs(deficit @ regge.gauge_map(local_momentum)))))

    covariance = 0.0
    source_covariance = 0.0
    for representation, frame in zip(METRIC_REPS, LIFTED_FRAMES):
        covariance = max(
            covariance,
            float(np.linalg.norm(
                representation.T @ frame_averaged_metric_hessian(frame @ generic) @ representation
                - candidate
            )),
        )
        source_covariance = max(
            source_covariance,
            float(np.linalg.norm(frame_averaged_source_row(frame @ generic) @ representation - source_row)),
        )

    product_residual = 0.0
    sector_product_residual = 0.0
    products = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target_index = FRAME_LOOKUP[tuple((left @ right).reshape(-1))]
            product_residual = max(
                product_residual,
                float(np.linalg.norm(METRIC_REPS[left_index] @ METRIC_REPS[right_index] - METRIC_REPS[target_index])),
            )
            sector_product_residual = max(
                sector_product_residual,
                float(np.linalg.norm(
                    FRAME_SECTOR_REPS[left_index] @ FRAME_SECTOR_REPS[right_index]
                    - FRAME_SECTOR_REPS[target_index]
                )),
            )
            products += 1

    finite_hamiltonian = frame_sector_hamiltonian(generic)
    declared_raw_source_generator = SOURCE_COUPLING * np.concatenate([
        base_deficit_source(frame @ generic) for frame in LIFTED_FRAMES
    ])
    raw_source_generator_residual = float(np.linalg.norm(
        finite_hamiltonian[0, 1:] - declared_raw_source_generator
    ))
    hermiticity = float(np.linalg.norm(finite_hamiltonian - finite_hamiltonian.conj().T))
    initial = np.zeros(len(finite_hamiltonian), dtype=complex)
    initial[0] = 1
    evolved = expm_multiply(-1j * UPDATE_PARAMETER * finite_hamiltonian, initial)
    restored = expm_multiply(+1j * UPDATE_PARAMETER * finite_hamiltonian, evolved)
    deleted_source = expm_multiply(
        -1j * UPDATE_PARAMETER * frame_sector_hamiltonian(generic, include_source=False), initial
    )
    deleted_response = expm_multiply(
        -1j * UPDATE_PARAMETER * frame_sector_hamiltonian(generic, include_regge=False), initial
    )
    wrong_sign = expm_multiply(
        -1j * UPDATE_PARAMETER * frame_sector_hamiltonian(generic, source_amplitude=-1.0), initial
    )
    zero_source = deleted_source
    amplitudes = []
    size_fixtures = (
        ("TRAIN_L3", 0.6, False, 3, np.asarray((2 * np.pi / 3, 0, 0, 0))),
        ("HELD_L4_LOW", 0.37, True, 4, np.asarray((np.pi / 2, np.pi / 2, 0, 0))),
        ("HELD_L4_SIGN", -0.81, True, 4, np.asarray((np.pi / 2, 0, np.pi / 2, np.pi / 2))),
    )
    for label, amplitude, held, length, momentum in size_fixtures:
        hamiltonian = frame_sector_hamiltonian(momentum, source_amplitude=amplitude)
        output = expm_multiply(-1j * UPDATE_PARAMETER * hamiltonian, initial)
        back = expm_multiply(+1j * UPDATE_PARAMETER * hamiltonian, output)
        amplitudes.append({
            "fixture": label,
            "source_amplitude": amplitude,
            "held": held,
            "periodic_spatial_length": length,
            "bloch_momentum": momentum.tolist(),
            "metric_carrier_norm": float(np.linalg.norm(output[1:])),
            "inverse_residual": float(np.linalg.norm(back - initial)),
            "parameters_refit": 0,
        })

    h_rotated = frame_sector_hamiltonian(LIFTED_FRAMES[1] @ generic)
    representation = FRAME_SECTOR_REPS[1]
    update_covariance_one_frame = float(np.linalg.norm(
        representation.T @ expm(-1j * UPDATE_PARAMETER * h_rotated) @ representation
        - expm(-1j * UPDATE_PARAMETER * finite_hamiltonian)
    ))

    single = base_metric_hessian(generic)
    anisotropic_control = 0.0
    for representation_metric, frame in zip(METRIC_REPS, LIFTED_FRAMES):
        anisotropic_control = max(
            anisotropic_control,
            float(np.linalg.norm(
                representation_metric.T @ base_metric_hessian(frame @ generic) @ representation_metric - single
            )),
        )

    return {
        "route": "A_supplied_24_sector_actual_Regge_edge_carrier",
        "frame_sector_status": (
            "24 frame sectors are coordinates of a supplied finite one-excitation model; uniform coherent "
            "frame-sector preparation/readout is supplied and not selected"
        ),
        "frame_average_status": (
            "compile-time target comparison and first-order uniform-sector projection only; not a stochastic mixture "
            "and not a separately enacted update"
        ),
        "source_generator": "H_source=+lambda sum_x q_x sum_local_hinges delta_hinge",
        "source_fourier_normalization": "raw finite-range deficit symbol; no momentum-dependent normalization",
        "momentum_dependent_source_normalization_used": False,
        "raw_local_source_generator_residual": raw_source_generator_residual,
        "source_called_physical_stress_energy_or_gravity": False,
        "R3_EH_target_algebra_comparisons": comparisons,
        "mean_best_fit_coefficient": float(np.mean([row["best_fit_coefficient"] for row in comparisons])),
        "coefficient_spread": float(np.ptp([row["best_fit_coefficient"] for row in comparisons])),
        "maximum_R3_relative_residual": max(row["relative_residual"] for row in comparisons),
        "metric_Bianchi_residual": bianchi,
        "edge_Regge_Bianchi_residual": edge_bianchi,
        "local_deficit_source_Ward_residual": deficit_ward,
        "frame_averaged_source_Ward_residual": source_ward,
        "maximum_all24_metric_generator_covariance_residual": covariance,
        "maximum_all24_source_covariance_residual": source_covariance,
        "all576_metric_representation_products": products,
        "all576_metric_representation_residual": product_residual,
        "all576_sector_representation_residual": sector_product_residual,
        "finite_edge_source_Hermiticity_residual": hermiticity,
        "finite_state_update_inverse_residual": float(np.linalg.norm(restored - initial)),
        "finite_state_update_norm_residual": abs(float(np.vdot(evolved, evolved).real) - 1.0),
        "source_deletion_residual": float(np.linalg.norm(evolved - deleted_source)),
        "metric_response_deletion_residual": float(np.linalg.norm(evolved - deleted_response)),
        "zero_source_metric_carrier_norm": float(np.linalg.norm(zero_source[1:])),
        "wrong_sign_response_sum_residual": float(np.linalg.norm(evolved[1:] + wrong_sign[1:])),
        "wrong_sign_is_equally_unitary_and_not_selected": True,
        "single_frame_anisotropic_control_residual": anisotropic_control,
        "one_frame_finite_update_covariance_residual": update_covariance_one_frame,
        "source_amplitude_rows": amplitudes,
        "finite_coordinate_count": 361,
        "finite_coordinate_layout": "one source coordinate plus 24x15 edge coordinates",
        "local_generator_support": "one path 4-cell and its bounded hinge star; tick offsets are internal layer roles",
        "finite_time_state_law_exact_unitary": True,
        "bounded_depth_finite_time_Regge_circuit_compiled": False,
        "target_equation_used_as_update": False,
        "Einstein_equation_or_physical_gravity_derived": False,
        "physical_site_encoding_or_intertwiner_executed": False,
    }
