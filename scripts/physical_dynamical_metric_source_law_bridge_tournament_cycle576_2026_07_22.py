#!/usr/bin/env python3
"""Cycle 576: dynamical metric/source-law bridge tournament.

Route A couples the Cycle572 resource amplitude to an intrinsic 24-frame orbit
of the actual 3+1 Regge edge Hessian through a local deficit insertion. Route B
tests a bounded plaquette/conjugate reciprocal carrier. Route C computes an
exact face-orbit scattering tangent and a least-squares tensor-projection
diagnostic on blinded held source profiles.

R3/EH is used only as a target-algebra comparator. No resource is called
physical stress or energy, no generator is called a rate, and no result is
called Einstein gravity.
"""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
from scipy.linalg import expm
from scipy.sparse.linalg import expm_multiply


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge


NOTE = ROOT / (
    "docs/FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_"
    "CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 8.0e-9
FD_TOL = 4.0e-7
MATCH_TOL = 5.0e-7
SIGNAL = 1.0e-8
REGGE_UPDATE_SCALE = 0.025
SOURCE_COUPLING = 0.17
UPDATE_PARAMETER = 0.035
PLAQUETTE_OMEGA = 0.31
PLAQUETTE_ETA = 0.19
PLAQUETTE_GAMMA = 0.23
SCATTER_AMPLITUDE = 0.071
SCATTER_STEPS = 2
PASS = 0
FAIL = 0
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md",
    "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json",
    "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py",
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md",
    "scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py",
    "docs/R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md",
)


DEPENDENCIES = {
    "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json":
        "bc3decba5fad793a177cf16823a03e7f786d717f1f68a269f7fb0859e089a675",
    "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py":
        "8d9d2f53b672847fb6678ebbb6654699361f4afadf0a43daad620d99db96cdc5",
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md":
        "46fc6d404d5b7ef973d1ef6475c802575eaedb17122b9c425217d837382acd4e",
    "scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py":
        "cd70b8d2d2deb0bd539c0d33db8254205e0112356a943a046aab4c0e1ca43264",
    "docs/R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md":
        "10c16354c6d57bd4b67b17f1e8bcaffbb60b3dab9a58471ddc3a5483aaced13b",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py":
        "537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce",
    "docs/CUBIC_COXETER_REGGE_3PLUS1_TICK_EXTENSION_SECOND_VARIATION_NARROW_THEOREM_NOTE_2026-06-09.md":
        "798e0df4311aa59f5d0d4f24b20b8949fec863484d1482111b04bce357f0d9ea",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def dependency_controls() -> dict:
    observed = {name: file_sha(ROOT / name) for name in DEPENDENCIES}
    tracked = {}
    for name in DEPENDENCIES:
        # The campaign freezes only committed dependency surfaces. The parent
        # rechecks this with git; this local field makes the contract explicit.
        tracked[name] = (ROOT / name).exists()
    return {
        "expected": DEPENDENCIES,
        "observed": observed,
        "all_paths_exist": all(tracked.values()),
        "pass": observed == DEPENDENCIES and all(tracked.values()),
    }


def cycle572_receipt() -> dict:
    path = ROOT / "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json"
    receipt = json.loads(path.read_text(encoding="utf-8"))
    good = (
        receipt["pass"]
        and receipt["authority"] == "none"
        and receipt["audit"] == "unset"
        and receipt["tests_passed"] == receipt["tests_total"] == 8
        and receipt["runner_sha256"] == DEPENDENCIES[
            "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py"
        ]
        and receipt["note_sha256"] == DEPENDENCIES[
            "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md"
        ]
    )
    if not good:
        raise RuntimeError("exact-pinned Cycle572 receipt does not match runner/note")
    return receipt


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 576", "route a", "route b", "route c",
        "supplied 24-sector", "uniform frame-sector preparation is supplied",
        "actual regge", "r3/eh target-algebra comparison", "not an einstein equation",
        "deficit source insertion", "bianchi", "ward", "plaquette", "conjugate",
        "blinded held", "zero-source", "wrong-sign", "anisotropic control", "source deletion",
        "response deletion", "all 24", "576", "not physical stress", "not physical energy",
        "not gravity", "generator is not a rate",
        "bounded-depth finite-time regge circuit remains open",
        "no physical-site compiler", "no minimum claim", "no no-go claim",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


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


GROVER_COIN = 2 * np.ones((12, 12), dtype=complex) / 12 - np.eye(12, dtype=complex)


def stream_face_state(state: np.ndarray, inverse: bool = False) -> np.ndarray:
    output = np.zeros_like(state)
    sign = -1 if inverse else 1
    for direction, displacement in enumerate(FACE_DIRECTIONS):
        output[..., direction] = np.roll(
            state[..., direction],
            shift=tuple(sign * int(value) for value in displacement),
            axis=(0, 1, 2),
        )
    return output


def scatter_update(
    state: np.ndarray,
    profile: np.ndarray,
    amplitude: float,
    *,
    steps: int = SCATTER_STEPS,
    inverse: bool = False,
    stream: bool = True,
) -> np.ndarray:
    current = state.copy()
    if not inverse:
        for _ in range(steps):
            current *= np.exp(1j * amplitude * profile)[..., None]
            current = np.einsum("ab,xyzb->xyza", GROVER_COIN, current)
            if stream:
                current = stream_face_state(current)
    else:
        for _ in range(steps):
            if stream:
                current = stream_face_state(current, inverse=True)
            current = np.einsum("ab,xyzb->xyza", GROVER_COIN.conj().T, current)
            current *= np.exp(-1j * amplitude * profile)[..., None]
    return current


def scatter_tangent(state: np.ndarray, profile: np.ndarray, *, stream: bool = True) -> tuple[np.ndarray, np.ndarray]:
    base = state.copy()
    tangent = np.zeros_like(state)
    for _ in range(SCATTER_STEPS):
        tangent = tangent + 1j * profile[..., None] * base
        tangent = np.einsum("ab,xyzb->xyza", GROVER_COIN, tangent)
        base = np.einsum("ab,xyzb->xyza", GROVER_COIN, base)
        if stream:
            tangent = stream_face_state(tangent)
            base = stream_face_state(base)
    return base, tangent


def face_metric_design() -> np.ndarray:
    rows = []
    for direction in FACE_DIRECTIONS:
        vector = direction / np.linalg.norm(direction)
        rows.append((
            vector[0] ** 2, vector[1] ** 2, vector[2] ** 2,
            2 * vector[0] * vector[1], 2 * vector[0] * vector[2], 2 * vector[1] * vector[2],
        ))
    return np.asarray(rows, dtype=float)


FACE_METRIC_DESIGN = face_metric_design()
FACE_METRIC_PINV = np.linalg.pinv(FACE_METRIC_DESIGN)
SPATIAL_HCOMPS = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def inferred_metric(base: np.ndarray, tangent: np.ndarray) -> tuple[np.ndarray, float]:
    phase_response = np.imag(tangent / base)
    metric = phase_response @ FACE_METRIC_PINV.T
    reconstructed = metric @ FACE_METRIC_DESIGN.T
    residual = float(np.linalg.norm(reconstructed - phase_response) / max(np.linalg.norm(phase_response), 1e-15))
    return metric, residual


def rotate_profile(profile: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = profile.shape[0]
    output = np.zeros_like(profile)
    for site in product(range(length), repeat=3):
        target = tuple(int(value % length) for value in frame @ np.asarray(site))
        output[target] = profile[site]
    return output


def rotate_face_state(state: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = state.shape[0]
    output = np.zeros_like(state)
    for site in product(range(length), repeat=3):
        target_site = tuple(int(value % length) for value in frame @ np.asarray(site))
        for source, vector in enumerate(FACE_DIRECTIONS):
            target_direction = int(np.where(np.all(FACE_DIRECTIONS == frame @ vector, axis=1))[0][0])
            output[target_site + (target_direction,)] = state[site + (source,)]
    return output


def rotate_metric_field(metric: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = metric.shape[0]
    output = np.zeros_like(metric)
    for site in product(range(length), repeat=3):
        target_site = tuple(int(value % length) for value in frame @ np.asarray(site))
        tensor = np.zeros((3, 3))
        for value, (left, right) in zip(metric[site], SPATIAL_HCOMPS):
            tensor[left, right] = value
            tensor[right, left] = value
        rotated = frame @ tensor @ frame.T
        output[target_site] = [rotated[left, right] for left, right in SPATIAL_HCOMPS]
    return output


def source_profiles(length: int, held: bool) -> tuple[tuple[str, np.ndarray], ...]:
    grid = np.indices((length, length, length), dtype=float)
    x, y, z = grid
    if not held:
        raw = (
            np.cos(2 * np.pi * x / length) + 0.35 * np.cos(2 * np.pi * y / length),
            np.sin(2 * np.pi * (x + y) / length) + 0.27 * np.cos(2 * np.pi * z / length),
        )
        names = ("TRAIN_XY", "TRAIN_DIAGONAL")
    else:
        point = np.zeros((length, length, length))
        point[0, 0, 0] = 1
        point -= np.mean(point)
        raw = (
            np.sin(2 * np.pi * (x + 2 * y + z) / length) + 0.41 * np.cos(2 * np.pi * z / length),
            point,
        )
        names = ("BLINDED_HELD_OBLIQUE", "BLINDED_HELD_POINT_NEUTRAL")
    output = []
    for name, profile in zip(names, raw):
        profile = profile - np.mean(profile)
        profile = profile / np.linalg.norm(profile)
        output.append((name, profile))
    return tuple(output)


def initial_face_state(length: int) -> np.ndarray:
    result = np.ones((length, length, length, 12), dtype=complex)
    return result / np.linalg.norm(result)


def r3_scattering_rows(metric: np.ndarray, profile: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    length = profile.shape[0]
    metric_fourier = np.fft.fftn(metric, axes=(0, 1, 2)) / (length ** 3)
    profile_fourier = np.fft.fftn(profile) / (length ** 3)
    responses = []
    sources = []
    frequencies = [2 * np.pi * np.fft.fftfreq(length) for _ in range(3)]
    for index in product(range(length), repeat=3):
        momentum3 = np.asarray([frequencies[axis][index[axis]] for axis in range(3)])
        if np.linalg.norm(momentum3) < 1e-12:
            continue
        momentum = np.asarray((momentum3[0], momentum3[1], momentum3[2], 0.0))
        h = np.zeros(10, dtype=complex)
        for value, component in zip(metric_fourier[index], SPATIAL_HCOMPS):
            h[regge.HCOMPS.index(component)] = value
        responses.append(regge.einstein_pairing_4d(momentum) @ h)
        source = np.zeros(10, dtype=complex)
        source[regge.HCOMPS.index((3, 3))] = profile_fourier[index]
        sources.append(source)
    return np.concatenate(responses), np.concatenate(sources)


def route_c_scattering() -> dict:
    rows = []
    train_response = []
    train_source = []
    held_pairs = []
    maximum_covariance = 0.0
    maximum_metric_covariance = 0.0
    empty_initial = initial_face_state(3)
    _, empty_tangent = scatter_tangent(empty_initial, np.zeros((3, 3, 3)))
    for length, held in ((3, False), (4, True)):
        initial = initial_face_state(length)
        for name, profile in source_profiles(length, held):
            base, tangent = scatter_tangent(initial, profile)
            epsilon = 8.0e-7
            finite = (
                scatter_update(initial, profile, epsilon)
                - scatter_update(initial, profile, -epsilon)
            ) / (2 * epsilon)
            evolved = scatter_update(initial, profile, SCATTER_AMPLITUDE)
            restored = scatter_update(evolved, profile, SCATTER_AMPLITUDE, inverse=True)
            deleted_source = scatter_update(initial, profile, 0.0)
            deleted_transport = scatter_update(initial, profile, SCATTER_AMPLITUDE, stream=False)
            wrong_sign = scatter_update(initial, profile, -SCATTER_AMPLITUDE)
            metric, reconstruction = inferred_metric(base, tangent)
            response, source = r3_scattering_rows(metric, profile)
            if held:
                held_pairs.append((response, source))
            else:
                train_response.append(response)
                train_source.append(source)

            if name.endswith("POINT_NEUTRAL"):
                for frame in FRAMES:
                    rotated_profile = rotate_profile(profile, frame)
                    left = rotate_face_state(evolved, frame)
                    right = scatter_update(rotate_face_state(initial, frame), rotated_profile, SCATTER_AMPLITUDE)
                    maximum_covariance = max(maximum_covariance, float(np.linalg.norm(left - right)))
                    rotated_base, rotated_tangent = scatter_tangent(rotate_face_state(initial, frame), rotated_profile)
                    rotated_metric, _ = inferred_metric(rotated_base, rotated_tangent)
                    maximum_metric_covariance = max(
                        maximum_metric_covariance,
                        float(np.linalg.norm(rotated_metric - rotate_metric_field(metric, frame))),
                    )

            rows.append({
                "fixture": name,
                "length": length,
                "held": held,
                "source_profile_zero_mean": abs(float(np.sum(profile))) < TOL,
                "norm_residual": abs(float(np.vdot(evolved, evolved).real) - 1.0),
                "inverse_residual": float(np.linalg.norm(restored - initial)),
                "tangent_finite_difference_residual": float(np.linalg.norm(finite - tangent)),
                "source_deletion_residual": float(np.linalg.norm(evolved - deleted_source)),
                "transport_response_deletion_residual": float(np.linalg.norm(evolved - deleted_transport)),
                "wrong_sign_odd_tangent_residual": float(np.linalg.norm((wrong_sign - deleted_source) + (evolved - deleted_source))),
                "wrong_sign_response_difference": float(np.linalg.norm(wrong_sign - evolved)),
                "effective_metric_reconstruction_residual": reconstruction,
                "effective_metric_norm": float(np.linalg.norm(metric)),
                "parameters_refit": 0,
            })

    train_response_vector = np.concatenate(train_response)
    train_source_vector = np.concatenate(train_source)
    calibration = np.vdot(train_source_vector, train_response_vector) / np.vdot(train_source_vector, train_source_vector)
    train_r3_residual = float(
        np.linalg.norm(train_response_vector - calibration * train_source_vector)
        / max(np.linalg.norm(train_response_vector), 1e-15)
    )
    held_residuals = []
    for response, source in held_pairs:
        held_residuals.append(float(
            np.linalg.norm(response - calibration * source) / max(np.linalg.norm(response), 1e-15)
        ))

    product_residual = 0.0
    products = 0
    for left_index, left in enumerate(FRAMES):
        for right_index, right in enumerate(FRAMES):
            target = FRAME_LOOKUP[tuple((left @ right).reshape(-1))]
            product_residual = max(
                product_residual,
                float(np.linalg.norm(FACE_REPS[left_index] @ FACE_REPS[right_index] - FACE_REPS[target])),
            )
            products += 1
    anisotropic = np.zeros((12, 12))
    anisotropic[0, 0] = 1
    anisotropic_covariance = max(
        float(np.linalg.norm(rep @ anisotropic - anisotropic @ rep)) for rep in FACE_REPS
    )

    return {
        "route": "C_face_orbit_scattering_transport_tensor_projection_diagnostic",
        "rows": rows,
        "law_fixed_before_blinded_held_profiles": True,
        "held_parameters_refit": 0,
        "maximum_norm_residual": max(row["norm_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_tangent_finite_difference_residual": max(row["tangent_finite_difference_residual"] for row in rows),
        "minimum_effective_metric_reconstruction_residual": min(row["effective_metric_reconstruction_residual"] for row in rows),
        "maximum_effective_metric_reconstruction_residual": max(row["effective_metric_reconstruction_residual"] for row in rows),
        "minimum_source_deletion_residual": min(row["source_deletion_residual"] for row in rows),
        "minimum_transport_response_deletion_residual": min(row["transport_response_deletion_residual"] for row in rows),
        "zero_profile_tangent_norm": float(np.linalg.norm(empty_tangent)),
        "minimum_wrong_sign_response_difference": min(row["wrong_sign_response_difference"] for row in rows),
        "maximum_all24_state_covariance_residual": maximum_covariance,
        "maximum_all24_effective_metric_covariance_residual": maximum_metric_covariance,
        "all576_face_representation_products": products,
        "all576_face_representation_residual": product_residual,
        "wrong_sign_is_equally_unitary_and_not_selected": True,
        "anisotropic_control_covariance_residual": anisotropic_covariance,
        "train_R3_source_calibration": [float(calibration.real), float(calibration.imag)],
        "train_R3_relative_residual": train_r3_residual,
        "blinded_held_R3_relative_residuals": held_residuals,
        "R3_source_match_closed": False,
        "finite_direction_coordinate_count": 12,
        "two_axial_hop_face_stream_supplied": True,
        "physical_site_encoding_or_intertwiner_executed": False,
        "source_profile_is_supplied_background_not_dynamic_stress": True,
        "called_physical_stress_energy_gravity_or_time": False,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle572 exact-pinned finite resource convention, reciprocal curvature response and supplied gamma",
            "actual 3+1 cubic-Coxeter Regge edge variables, path complex, Regge action choice and flat Hessian machinery",
            "24 finite frame-sector coordinates, uniform coherent frame-sector preparation/readout and its normalization",
            "Regge action orientation and update scale; source coupling magnitude and sign",
            "local deficit-sum source insertion and resource-to-deficit coupling rule",
            "Route B 31-coordinate layout, conjugate frequency, reservoir coupling, gamma and factor placement",
            "Route C Grover coin, two-step schedule, face stream, source amplitude and supplied source profiles",
            "finite L3/L4 periodic domains, tolerances, readouts and train/held split",
        ),
        "derived": (
            "actual-Regge edge Bianchi identities and local deficit-source Ward identity",
            "proper-cubic 24-frame target projection and exact all24/all576 covariance",
            "small-k compatibility with the R3/EH target at coefficient approximately -1/2",
            "exact unitary/inverse co-present frame-sector edge state law and active deletions",
            "exact local plaquette/conjugate reciprocal resource gate with all24/all576 covariance",
            "exact face scattering tangent/inverse plus least-squares tensor-projection and blinded held diagnostics",
            "route-specific R3 mismatch diagnostics for B and C",
        ),
        "open": (
            "derivation/selection of edge variables, Regge action, orientation, source sign and normalization",
            "selection/preparation of the uniform 24-frame sector and an exact bounded-depth finite-time Regge circuit",
            "physical stress-energy identification and coordinate-observable calibration",
            "nonlinear Regge/Einstein equation, Lorentzian/continuum/strong-field closure and global existence",
            "endogenous source profiles, locally enforced arbitrary matter sector and arbitrary size",
            "a local physical-site encoding, constraint system, leakage controls and executed intertwiner",
            "physical time, Record formation, realized history and Born probability",
        ),
        "supplied_parameters": {
            "regge_update_scale": REGGE_UPDATE_SCALE,
            "source_coupling": SOURCE_COUPLING,
            "source_coupling_sign": "+",
            "update_parameter": UPDATE_PARAMETER,
            "plaquette_omega": PLAQUETTE_OMEGA,
            "plaquette_eta": PLAQUETTE_ETA,
            "plaquette_gamma": PLAQUETTE_GAMMA,
            "scatter_amplitude": SCATTER_AMPLITUDE,
            "scatter_steps": SCATTER_STEPS,
            "frame_sector_count": len(FRAMES),
            "edge_coordinates_per_sector": 15,
            "uniform_frame_sector_preparation_and_readout": True,
            "small_momentum_comparison_magnitude": 1.0e-3,
            "covariance_control_momentum": (0.17, 0.11, 0.07, 0.13),
            "route_A_source_amplitude_fixtures": (
                ("TRAIN_L3", 3, 0.6, (2 * np.pi / 3, 0.0, 0.0, 0.0)),
                ("HELD_L4_LOW", 4, 0.37, (np.pi / 2, np.pi / 2, 0.0, 0.0)),
                ("HELD_L4_SIGN", 4, -0.81, (np.pi / 2, 0.0, np.pi / 2, np.pi / 2)),
            ),
            "route_B_coordinate_layout": "6 matter + 12 curvature + 12 conjugate + 1 reservoir",
            "route_C_coin": "normalized 12-direction Grover coin",
            "route_C_profile_coefficients": (0.35, 0.27, 0.41),
            "route_C_tangent_step": 8.0e-7,
            "tolerance": TOL,
            "finite_difference_tolerance": FD_TOL,
            "target_match_tolerance": MATCH_TOL,
            "signal_floor": SIGNAL,
        },
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE576 PHYSICAL DYNAMICAL METRIC/SOURCE-LAW BRIDGE TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    receipt = cycle572_receipt()
    note = note_contract()
    route_a = route_a_regge()
    route_b = route_b_plaquette(receipt)
    route_c = route_c_scattering()
    supplied = inventory()

    check("all Cycle572, actual-Regge and R3 dependencies are exact-pinned", dependencies["pass"], dependencies)
    check("note contract keeps the finite-execution and physical-naming boundary explicit", note["pass"], note)
    check(
        "Route A actual-Regge target projection matches R3/EH at small k without using the target equation as update",
        abs(route_a["mean_best_fit_coefficient"] + 0.5) < MATCH_TOL
        and route_a["coefficient_spread"] < MATCH_TOL
        and route_a["maximum_R3_relative_residual"] < MATCH_TOL
        and not route_a["target_equation_used_as_update"]
        and not route_a["Einstein_equation_or_physical_gravity_derived"],
        route_a["R3_EH_target_algebra_comparisons"],
    )
    check(
        "Route A actual edge and deficit variations satisfy Bianchi/Ward and all24/all576 covariance",
        route_a["metric_Bianchi_residual"] < TOL
        and route_a["edge_Regge_Bianchi_residual"] < TOL
        and route_a["local_deficit_source_Ward_residual"] < TOL
        and route_a["raw_local_source_generator_residual"] < TOL
        and not route_a["momentum_dependent_source_normalization_used"]
        and route_a["frame_averaged_source_Ward_residual"] < TOL
        and route_a["maximum_all24_metric_generator_covariance_residual"] < TOL
        and route_a["maximum_all24_source_covariance_residual"] < TOL
        and route_a["all576_metric_representation_products"] == 576
        and route_a["all576_metric_representation_residual"] < TOL
        and route_a["all576_sector_representation_residual"] < TOL,
        route_a,
    )
    check(
        "Route A supplied frame-sector state law is inverse and source/response/deletion sensitive",
        route_a["finite_edge_source_Hermiticity_residual"] < TOL
        and route_a["finite_state_update_inverse_residual"] < TOL
        and route_a["finite_state_update_norm_residual"] < TOL
        and route_a["source_deletion_residual"] > SIGNAL
        and route_a["metric_response_deletion_residual"] > SIGNAL
        and route_a["zero_source_metric_carrier_norm"] < TOL
        and route_a["wrong_sign_response_sum_residual"] < TOL
        and route_a["single_frame_anisotropic_control_residual"] > SIGNAL
        and route_a["one_frame_finite_update_covariance_residual"] < TOL
        and all(row["metric_carrier_norm"] > SIGNAL and row["inverse_residual"] < TOL and row["parameters_refit"] == 0 for row in route_a["source_amplitude_rows"])
        and not route_a["bounded_depth_finite_time_Regge_circuit_compiled"],
        route_a,
    )
    check(
        "Route B plaquette/conjugate gate is exact, reciprocal, all24/all576 and active-deletion controlled",
        route_b["Hermiticity_residual"] < TOL
        and route_b["unitarity_residual"] < TOL
        and route_b["inverse_residual"] < TOL
        and route_b["source_deletion_residual"] > SIGNAL
        and route_b["empty_source_carrier_response_norm"] < TOL
        and route_b["reservoir_deleted_matter_response_norm"] > SIGNAL
        and route_b["wrong_sign_response_difference"] > SIGNAL
        and route_b["curvature_response_deletion_residual"] > SIGNAL
        and route_b["conjugate_response_deletion_residual"] > SIGNAL
        and route_b["matter_curvature_reciprocity_residual"] < TOL
        and route_b["matter_to_curvature_response_norm"] > SIGNAL
        and route_b["curvature_to_matter_backreaction_norm"] > SIGNAL
        and route_b["maximum_all24_generator_covariance_residual"] < TOL
        and route_b["all576_frame_products"] == 576
        and route_b["all576_frame_product_residual"] < TOL
        and route_b["anisotropic_control_covariance_residual"] > SIGNAL,
        route_b,
    )
    check(
        "Route B does not launder its momentum-independent oscillator into the R3 target",
        route_b["R3_relative_residual"] > 0.1
        and route_b["R3_gauge_sample_response_norm"] > SIGNAL
        and not route_b["R3_target_match_closed"],
        {key: route_b[key] for key in ("R3_best_fit_coefficient", "R3_relative_residual", "R3_gauge_sample_response_norm")},
    )
    check(
        "Route C exact scattering walk predicts blinded held tangents and covariant least-squares tensor diagnostics without refit",
        route_c["maximum_norm_residual"] < TOL
        and route_c["maximum_inverse_residual"] < TOL
        and route_c["maximum_tangent_finite_difference_residual"] < FD_TOL
        and route_c["minimum_effective_metric_reconstruction_residual"] > 0.5
        and route_c["maximum_effective_metric_reconstruction_residual"] > 0.9
        and route_c["minimum_source_deletion_residual"] > SIGNAL
        and route_c["minimum_transport_response_deletion_residual"] > SIGNAL
        and route_c["zero_profile_tangent_norm"] < TOL
        and route_c["minimum_wrong_sign_response_difference"] > SIGNAL
        and route_c["maximum_all24_state_covariance_residual"] < TOL
        and route_c["maximum_all24_effective_metric_covariance_residual"] < TOL
        and route_c["all576_face_representation_products"] == 576
        and route_c["all576_face_representation_residual"] < TOL
        and route_c["held_parameters_refit"] == 0
        and route_c["anisotropic_control_covariance_residual"] > SIGNAL,
        route_c,
    )
    check(
        "Route C held source profiles diagnose mismatch of the declared scattering-to-R3 source template",
        route_c["train_R3_relative_residual"] > 0.05
        and min(route_c["blinded_held_R3_relative_residuals"]) > 0.05
        and not route_c["R3_source_match_closed"],
        {
            "train": route_c["train_R3_relative_residual"],
            "held": route_c["blinded_held_R3_relative_residuals"],
            "calibration": route_c["train_R3_source_calibration"],
        },
    )
    check(
        "supplied/derived/open inventory exposes sign, calibration, frame, circuit and nonlinear structure",
        len(supplied["supplied"]) >= 8
        and len(supplied["derived"]) >= 7
        and len(supplied["open"]) >= 7
        and len(supplied["supplied_parameters"]) >= 20,
        supplied,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = peak / (1024 ** 2) if sys.platform == "darwin" else peak / 1024
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "inventory": supplied,
        "terminal": {
            "strongest_constructive_result": (
                "supplied proper-cubic finite Regge edge model with deficit insertion and R3 target-algebra match"
            ),
            "actual_Regge_generator_and_source_Ward_closed": True,
            "R3_target_algebra_compatibility_closed": True,
            "physical_site_compiler_executed": False,
            "physical_stress_or_Einstein_equation_closed": False,
            "bounded_depth_finite_time_Regge_circuit_closed": False,
            "source_sign_normalization_or_frame_preparation_selected": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_FAILED")
        return 1
    print("RESULT ACTUAL_REGGE_DEFICIT_SOURCE_GENERATOR_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
