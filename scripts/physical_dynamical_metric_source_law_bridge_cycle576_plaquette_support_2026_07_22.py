#!/usr/bin/env python3
"""Plaquette-route support for the Cycle-576 primary runner.

This ordinary-import helper contains the unchanged finite plaquette and
conjugate construction used by Route B. It is packaging support only and
introduces no independent claim, authority, or audit status.
"""

from __future__ import annotations

from itertools import product
import math

import numpy as np
from scipy.linalg import expm

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge
import physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22 as regge_support


FRAMES = regge_support.FRAMES
FRAME_LOOKUP = regge_support.FRAME_LOOKUP
UPDATE_PARAMETER = 0.035
PLAQUETTE_OMEGA = 0.31
PLAQUETTE_ETA = 0.19
PLAQUETTE_GAMMA = 0.23


AXIAL_DIRECTIONS = np.asarray(
    ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)),
    dtype=int,
)
FACE_DIRECTIONS = np.asarray(
    sorted(direction for direction in product((-1, 0, 1), repeat=3) if sum(value != 0 for value in direction) == 2),
    dtype=int,
)


def direction_permutation(directions: np.ndarray, frame: np.ndarray) -> np.ndarray:
    count = len(directions)
    result = np.zeros((count, count), dtype=float)
    for source, vector in enumerate(directions):
        target = int(np.where(np.all(directions == frame @ vector, axis=1))[0][0])
        result[target, source] = 1
    return result


AXIAL_REPS = tuple(direction_permutation(AXIAL_DIRECTIONS, frame) for frame in FRAMES)
FACE_REPS = tuple(direction_permutation(FACE_DIRECTIONS, frame) for frame in FRAMES)


def plaquette_hamiltonian(
    *,
    gamma: float = PLAQUETTE_GAMMA,
    eta: float = PLAQUETTE_ETA,
    omega: float = PLAQUETTE_OMEGA,
    anisotropic: bool = False,
) -> np.ndarray:
    # 6 matter rails + 12 curvature rails + 12 conjugate rails + 1 reservoir.
    result = np.zeros((31, 31), dtype=complex)
    weights = np.zeros((6, 12))
    for matter, axis in enumerate(AXIAL_DIRECTIONS):
        for face, diagonal in enumerate(FACE_DIRECTIONS):
            weights[matter, face] = (axis @ diagonal) ** 2 - 2 / 3
    if anisotropic:
        weights[:, 1:] = 0
    result[:6, 6:18] = gamma * weights / math.sqrt(12)
    result[6:18, :6] = result[:6, 6:18].T
    result[6:18, 18:30] = omega * np.eye(12)
    result[18:30, 6:18] = omega * np.eye(12)
    scalar = np.ones(12) / math.sqrt(12)
    result[30, 6:18] = eta * scalar
    result[6:18, 30] = eta * scalar
    return result


def plaquette_representation(frame_index: int) -> np.ndarray:
    result = np.zeros((31, 31), dtype=float)
    result[:6, :6] = AXIAL_REPS[frame_index]
    result[6:18, 6:18] = FACE_REPS[frame_index]
    result[18:30, 18:30] = FACE_REPS[frame_index]
    result[30, 30] = 1
    return result


PLAQUETTE_REPS = tuple(plaquette_representation(index) for index in range(24))


def route_b_plaquette(receipt: dict) -> dict:
    hamiltonian = plaquette_hamiltonian()
    unitary = expm(-1j * UPDATE_PARAMETER * hamiltonian)
    initial = np.zeros(31, dtype=complex)
    initial[30] = 1 / math.sqrt(2)
    initial[0] = 1 / math.sqrt(2)
    evolved = unitary @ initial
    restored = unitary.conj().T @ evolved
    deleted_source = expm(-1j * UPDATE_PARAMETER * plaquette_hamiltonian(eta=0.0)) @ initial
    deleted_curvature = expm(-1j * UPDATE_PARAMETER * plaquette_hamiltonian(gamma=0.0)) @ initial
    deleted_conjugate = expm(-1j * UPDATE_PARAMETER * plaquette_hamiltonian(omega=0.0)) @ initial
    empty_source_initial = np.zeros(31, dtype=complex)
    empty_source = unitary @ empty_source_initial
    reservoir_deleted_matter_initial = np.zeros(31, dtype=complex)
    reservoir_deleted_matter_initial[0] = 1
    reservoir_deleted_matter = unitary @ reservoir_deleted_matter_initial
    wrong_sign = expm(-1j * UPDATE_PARAMETER * plaquette_hamiltonian(gamma=-PLAQUETTE_GAMMA)) @ initial
    anisotropic_h = plaquette_hamiltonian(anisotropic=True)

    covariance = 0.0
    anisotropic_covariance = 0.0
    product_residual = 0.0
    products = 0
    for left_index, left in enumerate(FRAMES):
        representation = PLAQUETTE_REPS[left_index]
        covariance = max(covariance, float(np.linalg.norm(representation @ hamiltonian - hamiltonian @ representation)))
        anisotropic_covariance = max(
            anisotropic_covariance,
            float(np.linalg.norm(representation @ anisotropic_h - anisotropic_h @ representation)),
        )
        for right_index, right in enumerate(FRAMES):
            target = FRAME_LOOKUP[tuple((left @ right).reshape(-1))]
            product_residual = max(
                product_residual,
                float(np.linalg.norm(PLAQUETTE_REPS[left_index] @ PLAQUETTE_REPS[right_index] - PLAQUETTE_REPS[target])),
            )
            products += 1

    spatial_components = (0, 1, 2, 4, 5, 7)
    momentum = np.asarray((1.0e-3, 0, 0, 0))
    target = regge.einstein_pairing_4d(momentum)[np.ix_(spatial_components, spatial_components)]
    candidate = PLAQUETTE_OMEGA * np.eye(6)
    coefficient = float(np.vdot(target, candidate).real / np.vdot(target, target).real)
    r3_residual = float(np.linalg.norm(candidate - coefficient * target) / np.linalg.norm(candidate))
    gauge_sample = np.asarray((1, 0, 0, 0, 0, 0), dtype=float)

    weights = hamiltonian[:6, 6:18]
    return {
        "route": "B_local_plaquette_curvature_conjugate_reciprocal_gate",
        "local_dimension": 31,
        "finite_coordinate_count": 31,
        "one_excitation_resource_conserved": True,
        "Hermiticity_residual": float(np.linalg.norm(hamiltonian - hamiltonian.conj().T)),
        "unitarity_residual": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(31))),
        "inverse_residual": float(np.linalg.norm(restored - initial)),
        "source_deletion_residual": float(np.linalg.norm(evolved - deleted_source)),
        "curvature_response_deletion_residual": float(np.linalg.norm(evolved - deleted_curvature)),
        "conjugate_response_deletion_residual": float(np.linalg.norm(evolved - deleted_conjugate)),
        "empty_source_carrier_response_norm": float(np.linalg.norm(empty_source[6:30])),
        "reservoir_deleted_matter_response_norm": float(np.linalg.norm(reservoir_deleted_matter[6:30])),
        "wrong_sign_response_difference": float(np.linalg.norm(evolved - wrong_sign)),
        "wrong_sign_is_equally_unitary_and_not_selected": True,
        "matter_curvature_reciprocity_residual": float(np.linalg.norm(weights - hamiltonian[6:18, :6].T)),
        "matter_to_curvature_response_norm": float(np.linalg.norm(weights)),
        "curvature_to_matter_backreaction_norm": float(np.linalg.norm(hamiltonian[6:18, :6])),
        "maximum_all24_generator_covariance_residual": covariance,
        "all576_frame_products": products,
        "all576_frame_product_residual": product_residual,
        "anisotropic_control_covariance_residual": anisotropic_covariance,
        "R3_candidate": "momentum-independent six-component oscillator metric block",
        "R3_best_fit_coefficient": coefficient,
        "R3_relative_residual": r3_residual,
        "R3_gauge_sample_response_norm": float(np.linalg.norm(candidate @ gauge_sample)),
        "R3_target_match_closed": False,
        "placement": "finite local model only; no compiled placement in a physical-site schedule",
        "Cycle572_gamma_reused_but_not_derived": receipt["route_B_plaquette_curvature_response"]["gamma_supplied"],
        "called_physical_stress_energy_or_gravity": False,
        "physical_site_encoding_or_intertwiner_executed": False,
    }
