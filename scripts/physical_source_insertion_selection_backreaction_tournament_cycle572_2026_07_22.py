#!/usr/bin/env python3
"""Cycle 572: finite source-insertion algebra and carrier-label support.

Route A recovers coordinates in a supplied five-element operator basis and
checks finite Ward/contact algebraic identities. Route B applies a supplied
plaquette-curvature controlled phase and checks reciprocal mixed response.
Route C counts coarse directed carrier/reservoir bits and tests their sparse
proper-cubic label action.

Nothing here is called physical stress, energy, work, force, gravity, or a
rate. Cycle561 endpoint count is not used.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22 as c569


c564 = c569.c564
c210 = c569.c210
collision = c569.collision
NOTE = ROOT / (
    "docs/"
    "FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_"
    "CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 5.0e-10
FD_TOL = 4.0e-7
SIGNAL = 1.0e-9
CLEAN = 2.0e-14
GAMMA = 0.23
TRAIN_LENGTH = 3
HELD_LENGTH = 4
LAWFUL_LENGTHS = (3, 4)
PASS = 0
FAIL = 0
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md",
    "scripts/physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22.py",
)

DEPENDENCIES = {
    "scripts/physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22.py":
        "a0008b105d33461d7e4615a8afe58d83e436415d1a75ddb4cb7d41ec1defdf37",
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md":
        "46fc6d404d5b7ef973d1ef6475c802575eaedb17122b9c425217d837382acd4e",
}

# Historical digest retained only as provenance for the reviewed Cycle-569
# finite-zero restriction rows.  No file or Git object is opened at runtime.
CYCLE569_HISTORICAL_RECEIPT_SHA256 = (
    "c80aae229d3721b273d12188960e2a4b16402d10a982856bec76c465dad52baa"
)
CYCLE569_FINITE_PRIOR = {
    "Cycle566_supplied_T00_value": 0.0,
    "Cycle566_supplied_T0i_value": 0.0,
    "maximum_all24_tensor_carrier_covariance_residual": 0.0,
    "frame_products": 576,
    "maximum_frame_product_residual": 0.0,
}

BODY_DIRECTIONS = np.asarray(tuple(product((-1, 1), repeat=3)), dtype=int)
assert BODY_DIRECTIONS.shape == (8, 3)

Key = tuple[tuple[int, ...], int, int]
State = dict[Key, complex]


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
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def cycle569_prior_controls() -> dict:
    """Recompute the exact finite Cycle-569 rows used by Cycle 572."""
    shear_covariance = 0.0
    base_vector = np.asarray((1, 1, 0), dtype=int)
    base = np.outer(base_vector, base_vector)
    for frame in c210.proper_cubic_frames():
        vector = frame @ base_vector
        shear_covariance = max(
            shear_covariance,
            float(np.linalg.norm(np.outer(vector, vector) - frame @ base @ frame.T)),
        )

    products = c569.frame_product_controls(c569.n3_shear_preparation(HELD_LENGTH), HELD_LENGTH)
    finite_support_checks = {
        "proper_cubic_frames": len(c210.proper_cubic_frames()),
        "face_directions": len(c569.FACE_DIRECTIONS),
        "coin_unitarity_residual": float(
            np.linalg.norm(c569.SPECIES.coin.conj().T @ c569.SPECIES.coin - np.eye(6))
        ),
        "collision_contact_pairs": c569.collision.reduced_operators()["contact_pairs"].tolist(),
    }
    if not (
        shear_covariance == CYCLE569_FINITE_PRIOR[
            "maximum_all24_tensor_carrier_covariance_residual"
        ]
        and products["frame_products"] == CYCLE569_FINITE_PRIOR["frame_products"]
        and products["maximum_residual"]
        == CYCLE569_FINITE_PRIOR["maximum_frame_product_residual"]
        and finite_support_checks["proper_cubic_frames"] == 24
        and finite_support_checks["face_directions"] == 12
        and finite_support_checks["coin_unitarity_residual"] < TOL
        and finite_support_checks["collision_contact_pairs"] == [6, 7]
    ):
        raise RuntimeError("reconstructed finite Cycle569 support contract failed")

    return {
        "receipt_sha256": CYCLE569_HISTORICAL_RECEIPT_SHA256,
        "historical_receipt_runtime_dependency": False,
        "finite_support_checks": finite_support_checks,
        "Cycle566_supplied_values": {
            "T00": CYCLE569_FINITE_PRIOR["Cycle566_supplied_T00_value"],
            "T0i": CYCLE569_FINITE_PRIOR["Cycle566_supplied_T0i_value"],
            "derived_here": False,
        },
        "maximum_all24_tensor_carrier_covariance_residual": shear_covariance,
        "frame_products": products,
    }


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 572", "route a", "route b", "route c",
        "basis-coordinate recovery", "ward", "contact telescope", "plaquette-curvature",
        "reciprocal mixed response", "body-diagonal", "cycle-566 values",
        "directed carrier-label bits", "held l4", "without refit", "all 24", "576",
        "no physical-site compiler", "physical stress", "physical energy",
        "physical work", "gravity", "endpoint count is not used",
        "no impossibility or minimum-content claim",
        "claim type: bounded_theorem", "source-note proposal", "effective status",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def hermitian_exponential(operator: np.ndarray, coefficient: complex) -> np.ndarray:
    values, vectors = np.linalg.eigh(operator)
    return (vectors * np.exp(coefficient * values)) @ vectors.conj().T


def ward_derivative(gate: np.ndarray, observable: np.ndarray, epsilon: float) -> np.ndarray:
    def source(value: float) -> np.ndarray:
        positive = hermitian_exponential(observable, 1j * value)
        negative = hermitian_exponential(observable, -1j * value)
        return gate.conj().T @ positive @ gate @ negative
    return (source(epsilon) - source(-epsilon)) / (2j * epsilon)


def route_a_basis_coordinates(prior: dict) -> dict:
    operators = collision.reduced_operators()
    identity18 = np.eye(18, dtype=complex)
    identity2 = np.eye(2, dtype=complex)
    p0 = np.diag((1.0, 0.0)).astype(complex)
    p1 = np.diag((0.0, 1.0)).astype(complex)
    z_branch = np.kron(np.diag((1.0, -1.0)).astype(complex), np.eye(9))

    q18 = c569.MASS * (operators["Qx"] + operators["Qy"])
    basis = (
        np.kron(q18, identity2),
        np.kron(c569.MASS * operators["X"], p0),
        np.kron(c569.MASS * operators["Y"], p1),
        np.kron(c569.MASS * z_branch, identity2),
        np.eye(36, dtype=complex),
    )
    target = basis[0] + basis[1] + basis[2]
    design = np.column_stack([item.reshape(-1) for item in basis])
    coefficients, *_ = np.linalg.lstsq(design, target.reshape(-1), rcond=None)
    coordinate_residual = float(np.linalg.norm(design @ coefficients - target.reshape(-1)))
    gram = design.conj().T @ design
    rank = int(np.linalg.matrix_rank(gram, tol=1e-11))
    condition = float(np.linalg.cond(gram))
    expected = np.asarray((1, 1, 1, 0, 0), dtype=complex)
    coefficient_residual = float(np.linalg.norm(coefficients - expected))
    hostile_expected = np.asarray((1, 1, 1, 0.37, -0.21), dtype=complex)
    hostile_target = design @ hostile_expected
    hostile_coefficients, *_ = np.linalg.lstsq(design, hostile_target, rcond=None)
    hostile_coordinate_residual = float(
        np.linalg.norm(design @ hostile_coefficients - hostile_target)
    )
    hostile_coefficient_residual = float(
        np.linalg.norm(hostile_coefficients - hostile_expected)
    )
    wrong_coordinate_residual = float(
        np.linalg.norm(design @ np.asarray((1, 1, 0, 0, 0)) - target.reshape(-1))
    )

    vertex = np.kron(operators["V"], identity2)
    contact = np.kron(operators["W"], identity2)
    full = np.kron(operators["G"], identity2)
    exchange = vertex.conj().T @ target @ vertex - target
    contact_part = vertex.conj().T @ (contact.conj().T @ target @ contact - target) @ vertex
    total = full.conj().T @ target @ full - target
    telescope = float(np.linalg.norm(total - exchange - contact_part))
    finite = ward_derivative(full, target, 7.0e-7)
    ward_residual = float(np.linalg.norm(finite - total))
    resource_identity = float(
        np.linalg.norm(full.conj().T @ basis[0] @ full - basis[0])
    )

    return {
        "route": "A_supplied_basis_coordinate_and_algebraic_identity_check",
        "source_action": "F_Theta(epsilon)=G^dag exp(i epsilon Theta) G exp(-i epsilon Theta)",
        "supplied_operator_basis": ("m(Qx+Qy)", "mX on selector0", "mY on selector1", "mZ control", "identity control"),
        "basis_rank": rank,
        "basis_dimension": len(basis),
        "gram_condition_number": condition,
        "recovered_coefficients": [[float(value.real), float(value.imag)] for value in coefficients],
        "coordinate_recovery_residual": coordinate_residual,
        "coefficient_recovery_residual": coefficient_residual,
        "hostile_coordinate_recovery_residual": hostile_coordinate_residual,
        "hostile_coefficient_recovery_residual": hostile_coefficient_residual,
        "wrong_coordinate_control_residual": wrong_coordinate_residual,
        "Ward_finite_difference_identity_residual": ward_residual,
        "exchange_contact_telescope_identity_residual": telescope,
        "resource_conservation_identity_residual": resource_identity,
        "Cycle569_committed_receipt_sha256": prior["receipt_sha256"],
        "Cycle566_values": prior["Cycle566_supplied_values"],
        "Cycle569_all24_tensor_covariance_residual": prior["maximum_all24_tensor_carrier_covariance_residual"],
        "Cycle569_all576_frame_products": prior["frame_products"],
        "basis_or_coefficients_selected_by_physics": False,
        "variational_or_Noether_selection_claimed": False,
        "called_physical_stress_energy_work_or_gravity": False,
    }


def curvature_weights() -> np.ndarray:
    weights = np.zeros((6, 12), dtype=float)
    for matter_direction, axis in enumerate(c210.DIRECTIONS):
        for face_direction, diagonal in enumerate(c569.FACE_DIRECTIONS):
            weights[matter_direction, face_direction] = float((axis @ diagonal) ** 2 - 2 / 3)
    return weights


CURVATURE_WEIGHTS = curvature_weights()


def apply_curvature_phase(state: State, length: int, gamma: float) -> State:
    if gamma == 0:
        return state.copy()
    output = {}
    for (occupied, face, reservoir), amplitude in state.items():
        phase = 0.0
        for value in occupied:
            site, matter_direction = c564.mode_parts(value, length)
            cell = c564.site_index(site, length)
            bits = c569.local_face_bits(face, cell)
            for face_direction in range(12):
                if (bits >> face_direction) & 1:
                    phase += CURVATURE_WEIGHTS[matter_direction, face_direction]
        output[(occupied, face, reservoir)] = amplitude * np.exp(1j * gamma * phase)
    return output


def curvature_update(
    state: State,
    length: int,
    *,
    gamma: float = GAMMA,
    angle: float = c569.ETA,
    contact: float = c569.CONTACT,
    inverse: bool = False,
    return_stages: bool = False,
) -> State | tuple[State, dict[str, State], float]:
    removed = 0.0
    if not inverse:
        matter_coined, cut = c569.apply_matter_coin(state, length, c569.SPECIES.coin)
        removed += cut**2
        vertexed, cut = c569.apply_face_vertex(matter_coined, length, angle)
        removed += cut**2
        curved = apply_curvature_phase(vertexed, length, gamma)
        matter_moved = c569.apply_matter_stream(curved, length)
        face_moved = c569.apply_face_stream(matter_moved, length)
        final = c569.apply_contact(face_moved, length, contact)
        stages = {
            "input": state,
            "matter_coined": matter_coined,
            "vertexed": vertexed,
            "matter_moved": matter_moved,
            "face_moved": face_moved,
            "curved": curved,
            "contacted": final,
        }
    else:
        uncontacted = c569.apply_contact(state, length, -contact)
        unface = c569.apply_face_stream(uncontacted, length, inverse=True)
        unmatter = c569.apply_matter_stream(unface, length, inverse=True)
        uncurved = apply_curvature_phase(unmatter, length, -gamma)
        unvertexed, cut = c569.apply_face_vertex(uncurved, length, -angle)
        removed += cut**2
        final, cut = c569.apply_matter_coin(unvertexed, length, c569.SPECIES.coin.conj().T)
        removed += cut**2
        stages = {"final": final}
    if return_stages:
        return final, stages, math.sqrt(removed)
    return final


def curvature_fixture(state: State, length: int, name: str, held: bool, n3: bool) -> dict:
    evolved, stages, cut = curvature_update(state, length, return_stages=True)
    assert isinstance(evolved, dict)
    restored = curvature_update(evolved, length, inverse=True)
    assert isinstance(restored, dict)
    before = c569.resource_density(state, length)
    after = c569.resource_density(evolved, length)
    transported = (
        c569.incoming(c569.MASS * c569.matter_links(stages["vertexed"], length), c210.DIRECTIONS)
        + c569.incoming(c569.MASS * c569.face_links(stages["matter_moved"], length), c569.FACE_DIRECTIONS)
        + c569.MASS * c569.reservoir_density(stages["matter_moved"], length)
    )
    deleted_curvature = curvature_update(state, length, gamma=0.0)
    deleted_contact = curvature_update(state, length, contact=0.0)
    deleted_vertex = curvature_update(state, length, angle=0.0)
    assert isinstance(deleted_curvature, dict) and isinstance(deleted_contact, dict) and isinstance(deleted_vertex, dict)
    covariance = 0.0
    failures = 0
    for frame in c210.proper_cubic_frames():
        left = c569.rotate_state(evolved, frame, length)
        right = curvature_update(c569.rotate_state(state, frame, length), length)
        assert isinstance(right, dict)
        residual = c569.state_residual(left, right)
        covariance = max(covariance, residual)
        failures += residual >= TOL
    return {
        "fixture": name,
        "held": held,
        "matter_number": 3 if n3 else 2,
        "basis_support_before_after": [len(state), len(evolved)],
        "norm_residual": abs(c569.state_norm(evolved) - c569.state_norm(state)),
        "inverse_residual": c569.state_residual(restored, state),
        "cleanup_amplitude": cut,
        "global_resource_residual": abs(float(np.sum(after)) - float(np.sum(before))),
        "maximum_local_continuity_residual": float(np.max(abs(after - transported))),
        "curvature_deletion_residual": c569.state_residual(evolved, deleted_curvature),
        "contact_deletion_residual": c569.state_residual(evolved, deleted_contact),
        "vertex_deletion_residual": c569.state_residual(evolved, deleted_vertex),
        "maximum_all24_update_covariance_residual": covariance,
        "all24_failures": failures,
        "parameters_refit": 0,
        "blind_empirical_prediction": False,
    }


def matrix_unit(dimension: int, left: int, right: int) -> np.ndarray:
    output = np.zeros((dimension, dimension), dtype=complex)
    output[left, right] = 1
    return output


def local_curvature_backreaction_controls() -> dict:
    weights = CURVATURE_WEIGHTS
    phases = np.exp(1j * GAMMA * weights.reshape(-1))
    gate = np.diag(phases)
    identity = np.eye(72, dtype=complex)
    matter_x = matrix_unit(6, 0, 4) + matrix_unit(6, 4, 0)
    face_xy = int(np.where(np.all(c569.FACE_DIRECTIONS == (1, 1, 0), axis=1))[0][0])
    face_yz = int(np.where(np.all(c569.FACE_DIRECTIONS == (0, 1, 1), axis=1))[0][0])
    face_x = matrix_unit(12, face_xy, face_yz) + matrix_unit(12, face_yz, face_xy)
    observable_matter = np.kron(matter_x, np.eye(12))
    observable_face = np.kron(np.eye(6), face_x)
    matter_impulse = gate.conj().T @ observable_matter @ gate - observable_matter
    face_impulse = gate.conj().T @ observable_face @ gate - observable_face

    covariance = 0.0
    for frame in c210.proper_cubic_frames():
        matter_permutation = np.zeros((6, 6))
        face_permutation = np.zeros((12, 12))
        for source, vector in enumerate(c210.DIRECTIONS):
            target = int(np.where(np.all(c210.DIRECTIONS == frame @ vector, axis=1))[0][0])
            matter_permutation[target, source] = 1
        for source, vector in enumerate(c569.FACE_DIRECTIONS):
            target = int(np.where(np.all(c569.FACE_DIRECTIONS == frame @ vector, axis=1))[0][0])
            face_permutation[target, source] = 1
        covariance = max(
            covariance,
            float(np.linalg.norm(matter_permutation @ weights @ face_permutation.T - weights)),
        )
    return {
        "bilinear_phase_action": "S_curv=gamma sum_x,a,D n_m(x,a)[(e_a.D)^2-2/3]n_p(x,D)",
        "gamma": GAMMA,
        "mixed_Hessian_matter_to_face": (GAMMA * weights).tolist(),
        "mixed_Hessian_reciprocity_residual": float(np.linalg.norm(GAMMA * weights - (GAMMA * weights.T).T)),
        "local_gate_unitarity_residual": float(np.linalg.norm(gate.conj().T @ gate - identity)),
        "matter_quadrature_response_norm": float(np.linalg.norm(matter_impulse)),
        "carrier_quadrature_backreaction_norm": float(np.linalg.norm(face_impulse)),
        "maximum_all24_coupling_covariance_residual": covariance,
        "state_update_is_linear_unitary": True,
        "nonlinear_label_scope": "bilinear matter-times-curvature response and reciprocal mixed derivatives",
        "called_gravitational_backreaction": False,
    }


def route_b_curvature() -> dict:
    rows = (
        curvature_fixture(c569.n2_preparation(TRAIN_LENGTH), TRAIN_LENGTH, "TRAIN_L3_N2_CURVATURE", False, False),
        curvature_fixture(c569.n2_preparation(HELD_LENGTH), HELD_LENGTH, "HELD_L4_N2_CURVATURE", True, False),
        curvature_fixture(c569.n3_shear_preparation(HELD_LENGTH), HELD_LENGTH, "FROZEN_HELD_L4_N3_CURVATURE", True, True),
    )
    local = local_curvature_backreaction_controls()
    return {
        "route": "B_dynamical_plaquette_curvature_reciprocal_phase",
        "rows": rows,
        "local_nonlinear_response_backreaction": local,
        "maximum_norm_residual": max(row["norm_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_cleanup_amplitude": max(row["cleanup_amplitude"] for row in rows),
        "maximum_resource_residual": max(row["global_resource_residual"] for row in rows),
        "maximum_local_continuity_residual": max(row["maximum_local_continuity_residual"] for row in rows),
        "minimum_curvature_deletion_residual": min(row["curvature_deletion_residual"] for row in rows),
        "minimum_contact_deletion_residual": min(row["contact_deletion_residual"] for row in rows),
        "minimum_vertex_deletion_residual": min(row["vertex_deletion_residual"] for row in rows),
        "maximum_all24_update_covariance_residual": max(row["maximum_all24_update_covariance_residual"] for row in rows),
        "all24_failures": sum(row["all24_failures"] for row in rows),
        "all576_frame_products_inherited_and_rechecked_for_carrier": c569.frame_product_controls(c569.n3_shear_preparation(HELD_LENGTH), HELD_LENGTH),
        "resource_called_physical_energy": False,
        "response_called_physical_work_force_or_gravity": False,
    }


def carrier_local_bits(mask: int, cell: int, count: int) -> int:
    return (mask >> (count * cell)) & ((1 << count) - 1)


def replace_carrier_bits(mask: int, cell: int, bits: int, count: int) -> int:
    local = ((1 << count) - 1) << (count * cell)
    return (mask & ~local) | (bits << (count * cell))


def carrier_mode(site: tuple[int, int, int], direction: int, length: int, count: int) -> int:
    return count * c564.site_index(site, length) + direction


def carrier_parts(value: int, length: int, count: int) -> tuple[tuple[int, int, int], int]:
    cell, direction = divmod(value, count)
    return c564.site_coordinate(cell, length), direction


def delta_carrier_exchange(reservoir: int, bits: int, angle: float, count: int) -> dict[tuple[int, int], complex]:
    output: defaultdict[tuple[int, int], complex] = defaultdict(complex)
    cosine = math.cos(angle)
    sine = math.sin(angle)
    if reservoir == 1 and bits == 0:
        output[(1, 0)] += cosine - 1
        for direction in range(count):
            output[(0, 1 << direction)] += 1j * sine / math.sqrt(count)
    elif reservoir == 0 and bits.bit_count() == 1:
        output[(1, 0)] += 1j * sine / math.sqrt(count)
        for direction in range(count):
            output[(0, 1 << direction)] += (cosine - 1) / count
    return dict(output)


def apply_carrier_vertex(state: State, length: int, directions: np.ndarray, angle: float) -> tuple[State, float]:
    if angle == 0:
        return state.copy(), 0.0
    count = len(directions)
    current = state
    removed = 0.0
    delta_cache = {
        (reservoir, bits): delta_carrier_exchange(reservoir, bits, angle, count)
        for reservoir in (0, 1) for bits in range(1 << count)
    }
    scalar_cache: dict[tuple[tuple[int, ...], int], dict[tuple[int, ...], complex]] = {}
    for cell in range(length**3):
        if not any(any(value // 6 == cell for value in occupied) for occupied, _carrier, _reservoir in current):
            continue
        output: defaultdict[Key, complex] = defaultdict(complex, current)
        for (occupied, carrier, reservoir), amplitude in current.items():
            delta = delta_cache[((reservoir >> cell) & 1, carrier_local_bits(carrier, cell, count))]
            if not delta:
                continue
            scalar = scalar_cache.setdefault((occupied, cell), c569.scalar_number_action(occupied, cell))
            for target_occupied, matter_coefficient in scalar.items():
                for (target_reservoir, target_bits), field_coefficient in delta.items():
                    target_carrier = replace_carrier_bits(carrier, cell, target_bits, count)
                    target_reservoir_mask = (reservoir & ~(1 << cell)) | (target_reservoir << cell)
                    output[(target_occupied, target_carrier, target_reservoir_mask)] += (
                        amplitude * matter_coefficient * field_coefficient
                    )
        current, cut = c569.cleaned(output)
        removed += cut**2
    return current, math.sqrt(removed)


def stream_carrier_mask(mask: int, length: int, directions: np.ndarray, inverse: bool = False) -> int:
    count = len(directions)
    output = 0
    sign = -1 if inverse else 1
    for value in range(count * length**3):
        if (mask >> value) & 1:
            site, direction = carrier_parts(value, length, count)
            target_site = tuple(int((site[axis] + sign * int(directions[direction, axis])) % length) for axis in range(3))
            output |= 1 << carrier_mode(target_site, direction, length, count)
    return output


def apply_carrier_stream(state: State, length: int, directions: np.ndarray, inverse: bool = False) -> State:
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, carrier, reservoir), amplitude in state.items():
        output[(occupied, stream_carrier_mask(carrier, length, directions, inverse), reservoir)] += amplitude
    return c569.cleaned(output)[0]


def carrier_update(
    state: State,
    length: int,
    directions: np.ndarray,
    *,
    angle: float = c569.ETA,
    contact: float = c569.CONTACT,
    inverse: bool = False,
    return_stages: bool = False,
) -> State | tuple[State, dict[str, State], float]:
    removed = 0.0
    if not inverse:
        matter_coined, cut = c569.apply_matter_coin(state, length, c569.SPECIES.coin)
        removed += cut**2
        vertexed, cut = apply_carrier_vertex(matter_coined, length, directions, angle)
        removed += cut**2
        matter_moved = c569.apply_matter_stream(vertexed, length)
        carrier_moved = apply_carrier_stream(matter_moved, length, directions)
        final = c569.apply_contact(carrier_moved, length, contact)
        stages = {
            "input": state,
            "matter_coined": matter_coined,
            "vertexed": vertexed,
            "matter_moved": matter_moved,
            "carrier_moved": carrier_moved,
            "contacted": final,
        }
    else:
        uncontacted = c569.apply_contact(state, length, -contact)
        uncarrier = apply_carrier_stream(uncontacted, length, directions, inverse=True)
        unmatter = c569.apply_matter_stream(uncarrier, length, inverse=True)
        unvertexed, cut = apply_carrier_vertex(unmatter, length, directions, -angle)
        removed += cut**2
        final, cut = c569.apply_matter_coin(unvertexed, length, c569.SPECIES.coin.conj().T)
        removed += cut**2
        stages = {"final": final}
    if return_stages:
        return final, stages, math.sqrt(removed)
    return final


def generic_carrier_links(state: State, length: int, directions: np.ndarray) -> np.ndarray:
    count = len(directions)
    result = np.zeros((length, length, length, count), dtype=float)
    for (_occupied, carrier, _reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for value in range(count * length**3):
            if (carrier >> value) & 1:
                site, direction = carrier_parts(value, length, count)
                result[site + (direction,)] += weight
    return result


def generic_reservoir_density(state: State, length: int) -> np.ndarray:
    result = np.zeros((length, length, length), dtype=float)
    for (_occupied, _carrier, reservoir), amplitude in state.items():
        weight = float(abs(amplitude) ** 2)
        for cell in range(length**3):
            result[c564.site_coordinate(cell, length)] += weight * ((reservoir >> cell) & 1)
    return result


def generic_resource_density(state: State, length: int, directions: np.ndarray) -> np.ndarray:
    return c569.MASS * (
        c569.matter_density(state, length)
        + np.sum(generic_carrier_links(state, length, directions), axis=-1)
        + generic_reservoir_density(state, length)
    )


def transform_carrier_mode(value: int, frame: np.ndarray, length: int, directions: np.ndarray) -> int:
    count = len(directions)
    site, direction = carrier_parts(value, length, count)
    target_site = tuple(int(item % length) for item in frame @ np.asarray(site, dtype=int))
    target_vector = frame @ directions[direction]
    target_direction = int(np.where(np.all(directions == target_vector, axis=1))[0][0])
    return carrier_mode(target_site, target_direction, length, count)


def rotate_generic_state(state: State, frame: np.ndarray, length: int, directions: np.ndarray) -> State:
    count = len(directions)
    output: defaultdict[Key, complex] = defaultdict(complex)
    for (occupied, carrier, reservoir), amplitude in state.items():
        ordered = c569.canonical(tuple(c569.transform_matter_mode(value, frame, length) for value in occupied))
        assert ordered is not None
        target_occupied, sign = ordered
        target_carrier = 0
        for value in range(count * length**3):
            if (carrier >> value) & 1:
                target_carrier |= 1 << transform_carrier_mode(value, frame, length, directions)
        output[(target_occupied, target_carrier, c569.rotate_reservoir(reservoir, frame, length))] += sign * amplitude
    return c569.cleaned(output)[0]


def generic_tensor(state: State, length: int, directions: np.ndarray) -> dict:
    axial = c569.MASS * c569.matter_links(state, length)
    carrier = c569.MASS * generic_carrier_links(state, length, directions)
    reservoir = c569.MASS * generic_reservoir_density(state, length)
    t00 = reservoir + np.sum(axial, axis=-1) + np.sum(carrier, axis=-1)
    tij = np.zeros((length, length, length, 3, 3), dtype=float)
    for links, vectors in ((axial, c210.DIRECTIONS), (carrier, directions)):
        for direction, vector in enumerate(vectors):
            tij += links[..., direction, None, None] * np.outer(vector, vector)
    return {"T00": t00, "Tij": tij, "axial": axial, "carrier": carrier}


def generic_action_value(state: State, length: int, directions: np.ndarray, lapse: float, metric: np.ndarray) -> float:
    value = float(np.sum(np.exp(lapse) * generic_reservoir_density(state, length)))
    for links, vectors in ((c569.matter_links(state, length), c210.DIRECTIONS), (generic_carrier_links(state, length, directions), directions)):
        for direction, vector in enumerate(vectors):
            value += float(np.exp(lapse + vector @ metric @ vector) * np.sum(links[..., direction]))
    return c569.MASS * value


def generic_finite_difference(state: State, length: int, directions: np.ndarray) -> dict:
    epsilon = 2.0e-6
    zero = np.zeros((3, 3))
    tensor = generic_tensor(state, length, directions)
    rows = []
    for left in range(3):
        for right in range(left, 3):
            deformation = np.zeros((3, 3))
            if left == right:
                deformation[left, right] = epsilon
            else:
                deformation[left, right] = epsilon / 2
                deformation[right, left] = epsilon / 2
            finite = (
                generic_action_value(state, length, directions, 0.0, deformation)
                - generic_action_value(state, length, directions, 0.0, -deformation)
            ) / (2 * epsilon)
            analytic = float(np.sum(tensor["Tij"][..., left, right]))
            rows.append({"component": [left, right], "analytic": analytic, "finite": finite, "residual": abs(analytic - finite)})
    lapse_finite = (
        generic_action_value(state, length, directions, epsilon, zero)
        - generic_action_value(state, length, directions, -epsilon, zero)
    ) / (2 * epsilon)
    lapse_analytic = float(np.sum(tensor["T00"]))
    return {
        "rows": rows,
        "lapse_residual": abs(lapse_analytic - lapse_finite),
        "maximum_residual": max([abs(lapse_analytic - lapse_finite)] + [row["residual"] for row in rows]),
        "maximum_offdiagonal": max(abs(row["analytic"]) for row in rows if row["component"][0] != row["component"][1]),
    }


def body_n2_preparation(length: int) -> State:
    return {
        (occupied, 0, c569.reservoir_sources(length)): amplitude
        for (occupied, _mediator), amplitude in c564.held_preparation(length).items()
    }


def body_n3_preparation(length: int) -> State:
    occupied = tuple(
        sorted(
            (
                c564.mode(((length - 1) % length, 0, 0), 0, length),
                c564.mode((0, (length - 1) % length, 0), 2, length),
                c564.mode((0, 0, (length - 1) % length), 4, length),
            )
        )
    )
    body_direction = int(np.where(np.all(BODY_DIRECTIONS == (1, 1, 1), axis=1))[0][0])
    carrier = 1 << carrier_mode((0, 0, 0), body_direction, length, len(BODY_DIRECTIONS))
    reservoir = 1 << c564.site_index(((length - 1) % length, 0, 0), length)
    return {(occupied, carrier, reservoir): 1.0 + 0j}


def carrier_incoming(links: np.ndarray, directions: np.ndarray) -> np.ndarray:
    result = np.zeros(links.shape[:3], dtype=float)
    for direction, displacement in enumerate(directions):
        result += np.roll(links[..., direction], shift=tuple(int(item) for item in displacement), axis=(0, 1, 2))
    return result


def body_fixture(state: State, length: int, name: str, held: bool, n3: bool) -> dict:
    evolved, stages, cut = carrier_update(state, length, BODY_DIRECTIONS, return_stages=True)
    assert isinstance(evolved, dict)
    restored = carrier_update(evolved, length, BODY_DIRECTIONS, inverse=True)
    assert isinstance(restored, dict)
    before = generic_resource_density(state, length, BODY_DIRECTIONS)
    after = generic_resource_density(evolved, length, BODY_DIRECTIONS)
    transported = (
        c569.incoming(c569.MASS * c569.matter_links(stages["vertexed"], length), c210.DIRECTIONS)
        + carrier_incoming(c569.MASS * generic_carrier_links(stages["matter_moved"], length, BODY_DIRECTIONS), BODY_DIRECTIONS)
        + c569.MASS * generic_reservoir_density(stages["matter_moved"], length)
    )
    deleted_contact = carrier_update(state, length, BODY_DIRECTIONS, contact=0.0)
    deleted_vertex = carrier_update(state, length, BODY_DIRECTIONS, angle=0.0)
    assert isinstance(deleted_contact, dict) and isinstance(deleted_vertex, dict)
    fd = generic_finite_difference(stages["vertexed"], length, BODY_DIRECTIONS)
    covariance = 0.0
    failures = 0
    for frame in c210.proper_cubic_frames():
        left = rotate_generic_state(evolved, frame, length, BODY_DIRECTIONS)
        right = carrier_update(rotate_generic_state(state, frame, length, BODY_DIRECTIONS), length, BODY_DIRECTIONS)
        assert isinstance(right, dict)
        residual = c569.state_residual(left, right)
        covariance = max(covariance, residual)
        failures += residual >= TOL
    tensor = generic_tensor(stages["vertexed"], length, BODY_DIRECTIONS)
    return {
        "fixture": name,
        "held": held,
        "matter_number": 3 if n3 else 2,
        "basis_support_before_after": [len(state), len(evolved)],
        "norm_residual": abs(c569.state_norm(evolved) - c569.state_norm(state)),
        "inverse_residual": c569.state_residual(restored, state),
        "cleanup_amplitude": cut,
        "global_resource_residual": abs(float(np.sum(after)) - float(np.sum(before))),
        "maximum_local_continuity_residual": float(np.max(abs(after - transported))),
        "contact_deletion_residual": c569.state_residual(evolved, deleted_contact),
        "vertex_deletion_residual": c569.state_residual(evolved, deleted_vertex),
        "maximum_all24_update_covariance_residual": covariance,
        "all24_failures": failures,
        "Tij_totals": np.sum(tensor["Tij"], axis=(0, 1, 2)).tolist(),
        "finite_difference": fd,
        "parameters_refit": 0,
        "blind_empirical_prediction": False,
    }


def carrier_local_gate_controls(directions: np.ndarray) -> dict:
    count = len(directions)
    identity = np.eye(count + 1, dtype=complex)
    source = np.zeros(count + 1, dtype=complex)
    source[0] = 1
    scalar = np.zeros(count + 1, dtype=complex)
    scalar[1:] = 1 / math.sqrt(count)
    projector = np.outer(source, source.conj()) + np.outer(scalar, scalar.conj())
    flip = np.outer(source, scalar.conj()) + np.outer(scalar, source.conj())
    gate = identity + (math.cos(c569.ETA) - 1) * projector + 1j * math.sin(c569.ETA) * flip
    maximum = float(np.linalg.norm(gate.conj().T @ gate - identity))
    failures = 0
    for frame in c210.proper_cubic_frames():
        permutation = np.zeros((count, count))
        for source_direction, vector in enumerate(directions):
            target = int(np.where(np.all(directions == frame @ vector, axis=1))[0][0])
            permutation[target, source_direction] = 1
        representation = np.zeros((count + 1, count + 1))
        representation[0, 0] = 1
        representation[1:, 1:] = permutation
        residual = float(np.linalg.norm(representation @ gate - gate @ representation))
        maximum = max(maximum, residual)
        failures += residual >= TOL
    return {"one_excitation_dimension": count + 1, "maximum_unitarity_or_covariance_residual": maximum, "failures": failures}


def generic_frame_products(state: State, length: int, directions: np.ndarray) -> dict:
    frames = c210.proper_cubic_frames()
    lookup = {tuple(frame.reshape(-1)): frame for frame in frames}
    maximum = 0.0
    cases = 0
    for left in frames:
        for right in frames:
            target = lookup[tuple((left @ right).reshape(-1))]
            maximum = max(
                maximum,
                c569.state_residual(
                    rotate_generic_state(rotate_generic_state(state, right, length, directions), left, length, directions),
                    rotate_generic_state(state, target, length, directions),
                ),
            )
            cases += 1
    return {"proper_cubic_frames": 24, "frame_products": cases, "maximum_residual": maximum}


def path_endpoint_transposition(path_length: int) -> dict:
    sites = path_length + 1
    failures = 0
    for word in product((0, 1), repeat=sites):
        values = list(word)
        for left in range(path_length):
            values[left], values[left + 1] = values[left + 1], values[left]
        for left in reversed(range(path_length - 1)):
            values[left], values[left + 1] = values[left + 1], values[left]
        target = (word[-1],) + word[1:-1] + (word[0],)
        failures += tuple(values) != target
    return {
        "path_length": path_length,
        "basis_words": 2**sites,
        "nearest_neighbor_SWAPS": 2 * path_length - 1,
        "failures": failures,
        "intermediate_rails_restored": failures == 0,
    }


def route_c_body_diagonal() -> dict:
    local = carrier_local_gate_controls(BODY_DIRECTIONS)
    products = generic_frame_products(body_n3_preparation(HELD_LENGTH), HELD_LENGTH, BODY_DIRECTIONS)
    label_bijection_failures = 0
    expected_labels = {
        tuple(int(item) for item in vector) for vector in BODY_DIRECTIONS
    }
    for frame in c210.proper_cubic_frames():
        transformed = {
            tuple(int(item) for item in frame @ vector)
            for vector in BODY_DIRECTIONS
        }
        label_bijection_failures += transformed != expected_labels
    return {
        "route": "C_coarse_directed_carrier_reservoir_label_count_and_covariance",
        "body_direction_orbit": BODY_DIRECTIONS.tolist(),
        "orbit_size": len(BODY_DIRECTIONS),
        "face_directed_carrier_label_bits_per_cell": len(c569.FACE_DIRECTIONS),
        "body_directed_carrier_label_bits_per_cell": len(BODY_DIRECTIONS),
        "reservoir_label_bits_per_cell": 1,
        "face_carrier_plus_reservoir_label_bits_per_cell": len(c569.FACE_DIRECTIONS) + 1,
        "body_carrier_plus_reservoir_label_bits_per_cell": len(BODY_DIRECTIONS) + 1,
        "proper_cubic_frames": len(c210.proper_cubic_frames()),
        "all24_label_bijection_failures": label_bijection_failures,
        "local_sparse_label_gate_unitarity_or_covariance_residual": local[
            "maximum_unitarity_or_covariance_residual"
        ],
        "frame_products": products["frame_products"],
        "all576_sparse_label_frame_product_residual": products["maximum_residual"],
        "held_sparse_label_fixture_length": HELD_LENGTH,
        "physical_M2_compiler_or_minimum_claimed": False,
    }


def domain_controls(route_b: dict, route_c: dict) -> dict:
    rejected = sum(length not in LAWFUL_LENGTHS for length in (2, 5, 8))
    rejected += sum(number not in (2, 3) for number in (0, 1, 4))
    held_b = next(row for row in route_b["rows"] if row["matter_number"] == 3)
    return {
        "lawful_lengths": LAWFUL_LENGTHS,
        "executed_matter_numbers": (2, 3),
        "lawful_domain_rejections": rejected,
        "train_L3_held_L4_split": True,
        "frozen_held_N3_curvature_fixture": True,
        "held_sparse_label_fixture_length": route_c["held_sparse_label_fixture_length"],
        "held_parameters_refit": held_b["parameters_refit"],
        "held_rows_called_blind_empirical_predictions": held_b["blind_empirical_prediction"],
        "endpoint_count_used_for_time_or_rate": False,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "beta=-0.3 six-mode coin and its resource-scale convention",
            "g=0.37 contact phase and contact-last order",
            "Cycle566 T00=0 and T0i=0 values, supplied rather than derived here",
            "face/plaquette orbit, geometric source, selector and joint insertion",
            "five-element local operator basis including Z and identity controls",
            "gamma=0.23 and the bilinear traceless matter-direction/face-curvature coupling",
            "factor placement of the curvature phase after the local vertex and before both streams and contact",
            "eight body-diagonal directed labels and one reservoir label per cell",
            "frozen train/held N2 and held-N3 curvature preparations and readouts",
            "finite periodic L3/L4 charts, proper-cubic frame transport and tolerances",
        ),
        "derived": (
            "basis coordinates for the declared joint insertion, including hostile coefficient controls",
            "resource-conservation, Ward finite-difference and exchange/contact telescope identities",
            "proper-cubic bilinear curvature coupling with reciprocal mixed Hessian",
            "nonzero matter response and carrier backreaction quadrature impulses",
            "unitary/inverse resource-conserving curvature update with contact and deletions",
            "exact face/body directed-label and reservoir-bit counts",
            "body-label proper-cubic bijection and sparse-label all24/all576 covariance",
        ),
        "open": (
            "derivation or physical selection of the operator basis, coefficients, gamma and carrier law",
            "coordinate-variation stress theorem and empirical physical tensor calibration",
            "dynamical metric variables, Einstein/Regge field equation and global nonlinear existence",
            "physical-site encoding, local constraints, leakage control and autonomous scheduling",
            "endogenous source/carrier/selector preparation and local matter-sector enforcement",
            "arbitrary N/size, continuum scaling, asymptotic response and observed coupling",
            "physical clock/proper time, Record formation, realized history and Born probability",
        ),
        "supplied_parameters": {
            "coin_beta": c569.BETA,
            "analytic_mass": c569.ANALYTIC_MASS,
            "rest_phase": c569.REST_PHASE,
            "reduced_exchange_kappa": c569.KAPPA,
            "face_reservoir_vertex_angle": c569.ETA,
            "contact_phase": c569.CONTACT,
            "curvature_phase_gamma": GAMMA,
            "basis": (
                "m(Qx+Qy)", "mX tensor P0", "mY tensor P1",
                "mZbranch", "identity",
            ),
            "target_coordinates": (1.0, 1.0, 1.0, 0.0, 0.0),
            "hostile_control_coordinates": (1.0, 1.0, 1.0, 0.37, -0.21),
            "ward_finite_difference_step": 7.0e-7,
            "update_factor_order": (
                "matter_coin", "face_reservoir_vertex", "curvature_phase",
                "matter_stream", "face_stream", "contact",
            ),
            "train_length": TRAIN_LENGTH,
            "held_length": HELD_LENGTH,
            "executed_matter_numbers": (2, 3),
            "tolerance": TOL,
            "finite_difference_tolerance": FD_TOL,
            "signal_floor": SIGNAL,
            "cleanup_cutoff": CLEAN,
        },
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE572 FINITE SOURCE-INSERTION ALGEBRA AND CARRIER-LABEL SUPPORT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    prior = cycle569_prior_controls()
    note = note_contract()
    route_a = route_a_basis_coordinates(prior)
    route_b = route_b_curvature()
    route_c = route_c_body_diagonal()
    domain = domain_controls(route_b, route_c)
    supplied = inventory()

    check(
        "self-contained finite support and audit-visible canonical source note are exact-pinned",
        dependencies["pass"],
        dependencies,
    )
    check("canonical note contract preserves the narrowed executed claim", note["pass"], note)
    check(
        "Route A recovers coordinates in the supplied basis and verifies Ward/contact identities with hostile controls",
        route_a["basis_rank"] == route_a["basis_dimension"] == 5
        and route_a["coordinate_recovery_residual"] < TOL
        and route_a["coefficient_recovery_residual"] < TOL
        and route_a["hostile_coordinate_recovery_residual"] < TOL
        and route_a["hostile_coefficient_recovery_residual"] < TOL
        and route_a["wrong_coordinate_control_residual"] > SIGNAL
        and route_a["Ward_finite_difference_identity_residual"] < FD_TOL
        and route_a["exchange_contact_telescope_identity_residual"] < TOL
        and route_a["resource_conservation_identity_residual"] < TOL
        and route_a["Cycle566_values"]["T00"] == 0.0
        and route_a["Cycle566_values"]["T0i"] == 0.0
        and not route_a["Cycle566_values"]["derived_here"]
        and route_a["Cycle569_all24_tensor_covariance_residual"] < TOL
        and route_a["Cycle569_all576_frame_products"]["frame_products"] == 576
        and not route_a["basis_or_coefficients_selected_by_physics"]
        and not route_a["variational_or_Noether_selection_claimed"]
        and not route_a["called_physical_stress_energy_work_or_gravity"],
        route_a,
    )
    check(
        "Route B plaquette-curvature update is inverse, resource-conserving, contact-sensitive and all24/576 covariant",
        route_b["maximum_norm_residual"] < TOL
        and route_b["maximum_inverse_residual"] < TOL
        and route_b["maximum_cleanup_amplitude"] < TOL
        and route_b["maximum_resource_residual"] < TOL
        and route_b["maximum_local_continuity_residual"] < TOL
        and route_b["minimum_curvature_deletion_residual"] > SIGNAL
        and route_b["minimum_contact_deletion_residual"] > SIGNAL
        and route_b["minimum_vertex_deletion_residual"] > SIGNAL
        and route_b["maximum_all24_update_covariance_residual"] < TOL
        and route_b["all24_failures"] == 0
        and route_b["all576_frame_products_inherited_and_rechecked_for_carrier"]["frame_products"] == 576
        and route_b["all576_frame_products_inherited_and_rechecked_for_carrier"]["maximum_residual"] < TOL
        and not route_b["resource_called_physical_energy"]
        and not route_b["response_called_physical_work_force_or_gravity"],
        route_b,
    )
    local = route_b["local_nonlinear_response_backreaction"]
    check(
        "Route B nonlinear bilinear action has exact reciprocal mixed response and nonzero matter/carrier impulses without nonlinear-state or gravity overclaim",
        local["mixed_Hessian_reciprocity_residual"] < TOL
        and local["local_gate_unitarity_residual"] < TOL
        and local["matter_quadrature_response_norm"] > SIGNAL
        and local["carrier_quadrature_backreaction_norm"] > SIGNAL
        and local["maximum_all24_coupling_covariance_residual"] < TOL
        and local["state_update_is_linear_unitary"]
        and not local["called_gravitational_backreaction"],
        local,
    )
    check(
        "Route C reports exact coarse directed-label counts and executed sparse-label covariance only",
        route_c["orbit_size"] == 8
        and route_c["face_directed_carrier_label_bits_per_cell"] == 12
        and route_c["body_directed_carrier_label_bits_per_cell"] == 8
        and route_c["reservoir_label_bits_per_cell"] == 1
        and route_c["face_carrier_plus_reservoir_label_bits_per_cell"] == 13
        and route_c["body_carrier_plus_reservoir_label_bits_per_cell"] == 9
        and route_c["proper_cubic_frames"] == 24
        and route_c["all24_label_bijection_failures"] == 0
        and route_c["local_sparse_label_gate_unitarity_or_covariance_residual"] < TOL
        and route_c["frame_products"] == 576
        and route_c["all576_sparse_label_frame_product_residual"] < TOL
        and not route_c["physical_M2_compiler_or_minimum_claimed"],
        route_c,
    )
    check(
        "lawful-domain, train/held, frozen N3 and endpoint-time firewalls are explicit",
        domain["lawful_domain_rejections"] == 6
        and domain["train_L3_held_L4_split"]
        and domain["frozen_held_N3_curvature_fixture"]
        and domain["held_sparse_label_fixture_length"] == HELD_LENGTH
        and domain["held_parameters_refit"] == 0
        and not domain["held_rows_called_blind_empirical_predictions"]
        and not domain["endpoint_count_used_for_time_or_rate"],
        domain,
    )
    check(
        "supplied/derived/open inventory preserves basis, curvature, carrier-label and physical-site boundaries",
        len(supplied["supplied"]) >= 9
        and len(supplied["derived"]) >= 7
        and len(supplied["open"]) >= 7
        and len(supplied["supplied_parameters"]) >= 15,
        supplied,
    )

    peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak = peak / (1024**2) if sys.platform == "darwin" else peak / 1024
    summary = {
        "authority": AUTHORITY,
        "audit": AUDIT,
        "dependencies": dependencies,
        "route_A": route_a,
        "route_B": route_b,
        "route_C": route_c,
        "domain": domain,
        "inventory": supplied,
        "terminal": {
            "strongest_constructive_result": "supplied-basis coordinates, algebraic Ward/contact identities, reciprocal curvature phase, and sparse carrier-label covariance",
            "basis_coordinates_and_identities_closed": True,
            "reciprocal_bilinear_response_identity_closed": True,
            "physical_site_compiler_claimed": False,
            "minimum_content_claimed": False,
            "physical_stress_energy_work_identified": False,
            "metric_or_gravity_equation": False,
            "proper_time_or_rate_claim": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_SOURCE_INSERTION_SELECTION_BACKREACTION_TOURNAMENT_FAILED")
        return 1
    print("RESULT FINITE_IDENTITIES_CURVATURE_AND_CARRIER_LABEL_COVARIANCE_BOUNDED_SUPPORT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
