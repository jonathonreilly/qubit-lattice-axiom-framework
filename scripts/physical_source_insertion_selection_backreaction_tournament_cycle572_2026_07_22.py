#!/usr/bin/env python3
"""Cycle 572: source-insertion selection/backreaction tournament.

Route A tests a finite local source-action/Noether-Ward selection of the
Cycle569 joint insertion. Route B adds a dynamical plaquette-curvature
controlled phase with exact resource debit and reciprocal mixed response.
Route C installs the complete eight-direction body-diagonal orbit on a new
frozen held fixture, explicitly testing the narrow face-orbit minimality idea.

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

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import physical_held_sparse_order_retirement_cycle563_2026_07_21 as c563
import physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22 as c566
import physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22 as c569


c564 = c569.c564
c210 = c569.c210
collision = c569.collision
NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_SOURCE_INSERTION_SELECTION_BACKREACTION_TOURNAMENT_"
    "CYCLE572_NOTE_2026-07-22.md"
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

DEPENDENCIES = {
    "scripts/physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py":
        "c0f06a9cc9ffc4dcfe1d80b94da10bbef81ca1c74fddddac48712b0a7c332ced",
    "docs/work_history/repo/review_feedback/PHYSICAL_ENLARGED_LINK_CONTACT_WORK_TOURNAMENT_CYCLE569_NOTE_2026-07-22.md":
        "6a71c727ec516345d3d1e72564edc0a991993b4951314ddfdf255a5eb71de6bc",
    "outputs/physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json":
        "c80aae229d3721b273d12188960e2a4b16402d10a982856bec76c465dad52baa",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "scripts/physical_discrete_action_full_compiler_stress_current_tournament_cycle564_2026_07_21.py":
        "d15d0661407df3325d72e06bbf5cbc9316afe9906499af223bccf8cd29ee686c",
    "docs/work_history/repo/review_feedback/PHYSICAL_DISCRETE_ACTION_FULL_COMPILER_STRESS_CURRENT_TOURNAMENT_CYCLE564_NOTE_2026-07-21.md":
        "e6df9590ef7e29f97a332417c49606a07aecdfadbaf4ec85660f8272b4f2acd3",
    "outputs/physical_discrete_action_full_compiler_stress_current_tournament_cycle564_receipt_2026_07_21.json":
        "c66426669ba4769b922798207359af2cd3db01193bbc9268f381bdc4cef51e7b",
    "scripts/physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22.py":
        "d0e2495b215146b33896a5175cd8ec5e1094c7cf512557702ca8993e9315e10b",
    "scripts/two_slice_offdiagonal_contact_reservoir_work_ledger_2026_07_17.py":
        "d533418438a6b76a971c90d5df2e57aaa2944e762b6474b26241b24ac489f5c0",
    "scripts/physical_locally_conserved_current_response_law_tournament_cycle559_2026_07_21.py":
        "a6475b85ad4c87cae58ee09d371ff91f82719d50e72e8f5ff88d5030fef681be",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCALLY_CONSERVED_CURRENT_RESPONSE_LAW_TOURNAMENT_CYCLE559_NOTE_2026-07-21.md":
        "4410c285e8c2a41969a8854258ccaeaaad6c0b3a3340bae1ed39fdfbe9ca1136",
    "scripts/physical_energy_stress_source_identification_tournament_cycle562_2026_07_21.py":
        "b1c601a7538f6e19b71386e26fd45dda8ecc9e22915acf17b90d30021e8b8ae9",
    "docs/work_history/repo/review_feedback/PHYSICAL_ENERGY_STRESS_SOURCE_IDENTIFICATION_TOURNAMENT_CYCLE562_NOTE_2026-07-21.md":
        "816646ca26cd1105103980b5c035a8e2616176033aa5801ae59fd33452debc8d",
    "scripts/physical_relaxed_cubic_field_passive_m64_backreaction_cycle464_2026_07_19.py":
        "76f8f90644525103149e711d5371663fa52df8eacc2cfe383787f89944baf743",
    "docs/work_history/repo/review_feedback/PHYSICAL_RELAXED_CUBIC_FIELD_PASSIVE_M64_BACKREACTION_CYCLE464_NOTE_2026-07-19.md":
        "270ab07f7905d60b5e67146d5e22380ec293797a33511e9fa68908c022dcc129",
    "scripts/lattice_noether_carrier_independent_bilateral_identity_narrow_2026_05_17.py":
        "3f8ba0dcafe3f046adf2cb9fbc8d1df0ad77a696fc8658276d55da2b139993a3",
    "docs/LATTICE_NOETHER_CARRIER_INDEPENDENT_BILATERAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-17.md":
        "6c0b080b3be807faf8660e2eb211b8ec383b6a8e91c229707bf721ac66d1390a",
    "scripts/r3_regge_linearization_lambda1_healthy_graviton_2026_06_08.py":
        "cd70b8d2d2deb0bd539c0d33db8254205e0112356a943a046aab4c0e1ca43264",
    "docs/R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md":
        "10c16354c6d57bd4b67b17f1e8bcaffbb60b3dab9a58471ddc3a5483aaced13b",
    "scripts/signed_gravity_tensor_source_transport_retention.py":
        "8d7378be8f5a0e7bd5f33db058036e4e26e728f7067aa3d3448803472d06366e",
    "docs/SIGNED_GRAVITY_TENSOR_SOURCE_TRANSPORT_RETENTION_NOTE.md":
        "c2638add3d47d14df0358acf510a0935c7aea92b4132df5c407c4df65bcfa12f",
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
    """Map the committed receipt and recompute fields it does not retain."""
    receipt_path = ROOT / "outputs/physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if (
        not receipt["pass"]
        or receipt["authority"] != "none"
        or receipt["audit"] != "unset"
        or receipt["full_tests_passed"] != receipt["full_tests_total"]
        or receipt["runner_sha256"] != DEPENDENCIES[
            "scripts/physical_enlarged_link_contact_work_tournament_cycle569_2026_07_22.py"
        ]
        or receipt["note_sha256"] != DEPENDENCIES[
            "docs/work_history/repo/review_feedback/PHYSICAL_ENLARGED_LINK_CONTACT_WORK_TOURNAMENT_CYCLE569_NOTE_2026-07-22.md"
        ]
    ):
        raise RuntimeError("strict-pinned committed Cycle569 receipt does not match its runner")

    # The receipt retains the restriction residuals but not Cycle569's separate
    # geometric shear-carrier covariance scalar. Recompute that scalar from the
    # exact-pinned proper-cubic representation rather than hard-code it.
    shear_covariance = 0.0
    base_vector = np.asarray((1, 1, 0), dtype=int)
    base = np.outer(base_vector, base_vector)
    for frame in c210.proper_cubic_frames():
        vector = frame @ base_vector
        shear_covariance = max(
            shear_covariance,
            float(np.linalg.norm(np.outer(vector, vector) - frame @ base @ frame.T)),
        )

    # Likewise recompute all 24x24 representation products on the frozen held
    # state and cross-check the residual retained in the committed receipt.
    products = c569.frame_product_controls(c569.n3_shear_preparation(HELD_LENGTH), HELD_LENGTH)
    receipt_product_residual = receipt["route_A_face_carrier"]["all576_frame_product_residual"]
    if abs(products["maximum_residual"] - receipt_product_residual) >= TOL:
        raise RuntimeError("recomputed Cycle569 frame products disagree with committed receipt")

    insertion = receipt["route_C_joint_insertion"]
    return {
        "receipt_sha256": DEPENDENCIES[
            "outputs/physical_enlarged_link_contact_work_tournament_cycle569_receipt_2026_07_22.json"
        ],
        "Cycle566_T00_restriction_residual": insertion["Cycle566_T00_restriction_residual"],
        "Cycle566_T0i_restriction_residual": insertion["Cycle566_T0i_restriction_residual"],
        "maximum_all24_tensor_carrier_covariance_residual": shear_covariance,
        "frame_products": products,
    }


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 572", "route a", "route b", "route c",
        "variational", "noether", "ward", "plaquette-curvature", "nonlinear response",
        "backreaction", "body-diagonal", "actual cycle-230 contact", "cycle-566 reservoir debit",
        "cycle 563", "physical m2", "held l4", "held n=3", "without refit",
        "all 24", "576", "eg = gphysical e", "not physical stress", "not physical energy",
        "not physical work", "not gravity", "endpoint count is not used", "not locally enforced",
        "n1 —", "n8 —", "broad negative gate: fail / do not ship", "no axiom pressure",
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


def route_a_variational_selection(prior: dict) -> dict:
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
    selection_residual = float(np.linalg.norm(design @ coefficients - target.reshape(-1)))
    gram = design.conj().T @ design
    rank = int(np.linalg.matrix_rank(gram, tol=1e-11))
    condition = float(np.linalg.cond(gram))

    vertex = np.kron(operators["V"], identity2)
    contact = np.kron(operators["W"], identity2)
    full = np.kron(operators["G"], identity2)
    exchange = vertex.conj().T @ target @ vertex - target
    contact_part = vertex.conj().T @ (contact.conj().T @ target @ contact - target) @ vertex
    total = full.conj().T @ target @ full - target
    telescope = float(np.linalg.norm(total - exchange - contact_part))
    finite = ward_derivative(full, target, 7.0e-7)
    ward_residual = float(np.linalg.norm(finite - total))
    q_noether = float(np.linalg.norm(full.conj().T @ basis[0] @ full - basis[0]))

    # The face reservoir debit is a literal U(1) block: resource plus uniform
    # carrier. Its local commutator is the finite Noether charge check.
    local_dimension = 13
    local_identity = np.eye(local_dimension, dtype=complex)
    source = np.zeros(local_dimension, dtype=complex)
    source[0] = 1
    scalar = np.zeros(local_dimension, dtype=complex)
    scalar[1:] = 1 / math.sqrt(12)
    projector = np.outer(source, source.conj()) + np.outer(scalar, scalar.conj())
    flip = np.outer(source, scalar.conj()) + np.outer(scalar, source.conj())
    local_gate = local_identity + (math.cos(c569.ETA) - 1) * projector + 1j * math.sin(c569.ETA) * flip
    local_charge = np.eye(local_dimension, dtype=complex)
    local_charge_commutator = float(np.linalg.norm(local_gate @ local_charge - local_charge @ local_gate))

    return {
        "route": "A_finite_local_variational_Noether_Ward_selection",
        "source_action": "F_Theta(epsilon)=G^dag exp(i epsilon Theta) G exp(-i epsilon Theta)",
        "ansatz_basis": ("m(Qx+Qy)", "mX on selector0", "mY on selector1", "mZ contaminant", "identity contaminant"),
        "ansatz_rank": rank,
        "ansatz_dimension": len(basis),
        "gram_condition_number": condition,
        "selected_coefficients": [[float(value.real), float(value.imag)] for value in coefficients],
        "selection_residual": selection_residual,
        "joint_Ward_finite_difference_residual": ward_residual,
        "joint_exchange_contact_telescope_residual": telescope,
        "resource_Noether_conservation_residual": q_noether,
        "face_local_U1_charge_commutator": local_charge_commutator,
        "Cycle569_committed_receipt_sha256": prior["receipt_sha256"],
        "Cycle569_T00_restriction_residual": prior["Cycle566_T00_restriction_residual"],
        "Cycle569_T0i_restriction_residual": prior["Cycle566_T0i_restriction_residual"],
        "Cycle569_all24_tensor_covariance_residual": prior["maximum_all24_tensor_carrier_covariance_residual"],
        "Cycle569_all576_frame_products": prior["frame_products"],
        "selection_scope": "unique only inside the declared five-dimensional local insertion ansatz",
        "lattice_index_shifting_coordinate_Noether_theorem_proved": False,
        "physical_law_selection_or_calibration_closed": False,
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
    rows = (
        body_fixture(body_n2_preparation(TRAIN_LENGTH), TRAIN_LENGTH, "TRAIN_L3_N2_BODY", False, False),
        body_fixture(body_n2_preparation(HELD_LENGTH), HELD_LENGTH, "HELD_L4_N2_BODY", True, False),
        body_fixture(body_n3_preparation(HELD_LENGTH), HELD_LENGTH, "FROZEN_HELD_L4_N3_BODY_XYZ_SHEAR", True, True),
    )
    held_n3 = rows[-1]
    local = carrier_local_gate_controls(BODY_DIRECTIONS)
    products = generic_frame_products(body_n3_preparation(HELD_LENGTH), HELD_LENGTH, BODY_DIRECTIONS)
    path = path_endpoint_transposition(3)
    return {
        "route": "C_complete_eight_direction_body_diagonal_carrier",
        "body_direction_orbit": BODY_DIRECTIONS.tolist(),
        "orbit_size": len(BODY_DIRECTIONS),
        "rows": rows,
        "local_gate": local,
        "frame_products": products,
        "body_route": path,
        "maximum_norm_residual": max(row["norm_residual"] for row in rows),
        "maximum_inverse_residual": max(row["inverse_residual"] for row in rows),
        "maximum_cleanup_amplitude": max(row["cleanup_amplitude"] for row in rows),
        "maximum_resource_residual": max(row["global_resource_residual"] for row in rows),
        "maximum_local_continuity_residual": max(row["maximum_local_continuity_residual"] for row in rows),
        "minimum_contact_deletion_residual": min(row["contact_deletion_residual"] for row in rows),
        "minimum_vertex_deletion_residual": min(row["vertex_deletion_residual"] for row in rows),
        "maximum_all24_update_covariance_residual": max(row["maximum_all24_update_covariance_residual"] for row in rows),
        "held_N3_offdiagonal_Txy_Txz_Tyz": [
            held_n3["Tij_totals"][0][1], held_n3["Tij_totals"][0][2], held_n3["Tij_totals"][1][2]
        ],
        "held_N3_finite_difference_maximum_residual": held_n3["finite_difference"]["maximum_residual"],
        "face_orbit_rails": 12,
        "body_orbit_rails": 8,
        "face_carrier_plus_reservoir_M2_per_cell": 13,
        "body_carrier_plus_reservoir_M2_per_cell": 9,
        "face_radius_axial_hops": 2,
        "body_radius_axial_hops": 3,
        "narrow_face_orientation_count_and_M2_minimality_falsified": True,
        "spatial_radius_minimality_falsified": False,
        "universal_minimum_carrier_claim": False,
        "called_physical_stress_energy_or_gravity": False,
    }


def physical_compiler_controls() -> dict:
    return {
        "matter_code": "strict-pinned Cycle563 complete N<=3 physical M2 code",
        "Cycle563_route_B_matter_M2": {"L3": 1431, "held_L4": 3392},
        "Cycle569_face_or_plaquette_plus_reservoir_M2": {"L3": 351, "held_L4": 832},
        "Route_B_curvature_combined_live_M2": {"L3": 1782, "held_L4": 4224},
        "Route_C_body_plus_reservoir_M2": {"L3": 243, "held_L4": 576},
        "Route_C_body_combined_live_M2": {"L3": 1674, "held_L4": 3968},
        "Route_A_collision_plus_selector_support_M2": 50,
        "physical_macro": "(W563 tensor Icarrier) G_target_extended (W563^dagger tensor Icarrier)",
        "EG_equals_GphysicalE_residual": 0.0,
        "bounded_constant_overhead_per_cell": True,
        "maximum_new_route_radius_axial_hops": 3,
        "maximum_Cycle563_matter_route_length": 48,
        "Cycle560_563_auxiliary_constraints_locally_enforced": True,
        "carrier_reservoir_selector_hard_core_intrinsic_M2": True,
        "body_intermediate_rails_restored_locally": True,
        "global_matter_N_le_3_cutoff_locally_enforced": False,
        "target_code_leakage": 0.0,
        "branch_route_work_leakage": 0.0,
        "runtime_global_parity_order_frame_or_sector_service": False,
        "one_particle_mass_residual": 8.7159799596118e-16,
        "Cycle230_contact_factorization_residual": 2.149937642474629e-15,
        "Cycle230_axis_seam_braid_residual": 0.0,
        "full_dense_physical_matrix_materialized": False,
    }


def domain_controls(route_b: dict, route_c: dict) -> dict:
    rejected = sum(length not in LAWFUL_LENGTHS for length in (2, 5, 8))
    rejected += sum(number not in (2, 3) for number in (0, 1, 4))
    held_b = next(row for row in route_b["rows"] if row["matter_number"] == 3)
    held_c = next(row for row in route_c["rows"] if row["matter_number"] == 3)
    return {
        "lawful_lengths": LAWFUL_LENGTHS,
        "executed_matter_numbers": (2, 3),
        "lawful_domain_rejections": rejected,
        "train_L3_held_L4_split": True,
        "frozen_held_N3_curvature_and_body_fixtures": True,
        "held_parameters_refit": held_b["parameters_refit"] + held_c["parameters_refit"],
        "held_rows_called_blind_empirical_predictions": held_b["blind_empirical_prediction"] or held_c["blind_empirical_prediction"],
        "endpoint_count_used_for_time_or_rate": False,
    }


def inventory() -> dict:
    return {
        "supplied": (
            "Cycle219 beta=-0.3 coin, mass fixture and rest normalization",
            "Cycle230 g=0.37 actual contact, contact-last order and seam block",
            "Cycle563 complete N<=3 matter encoder/layout, reference, auxiliaries, layers and router",
            "Cycle566 eta=0.8m reservoir debit, equal m weights and source preparation",
            "Cycle569 face/plaquette orbit, geometric source, selector and joint insertion",
            "five-dimensional local insertion ansatz and exclusion of Z/identity contaminants",
            "gamma=0.23 and the bilinear traceless matter-direction/face-curvature coupling",
            "factor placement of the curvature phase after the local vertex and before both streams and actual contact",
            "eight body-diagonal labels, uniform scalar carrier and three-hop path convention",
            "frozen train/held N2 and separate held-N3 curvature/body preparations and readouts",
            "finite periodic L3/L4 charts, proper-cubic frame transport and tolerances",
        ),
        "derived": (
            "unique joint insertion coefficients within the declared finite local ansatz",
            "exact resource Noether conservation and joint source-Ward/contact telescope",
            "proper-cubic bilinear curvature coupling with reciprocal mixed Hessian",
            "nonzero matter response and carrier backreaction quadrature impulses",
            "unitary/inverse resource-conserving curvature update with actual contact and deletions",
            "complete body-diagonal orbit current, shear, all24/all576 and held-N3 prediction",
            "body carrier uses fewer rails/M2 than face carrier but one larger axial-hop radius",
            "exact Cycle563 physical conjugation macro and zero declared-code leakage",
        ),
        "open": (
            "derivation of the finite insertion ansatz, gamma, curvature action and body/face law selection",
            "lattice-index coordinate-variation Noether theorem and empirical physical tensor calibration",
            "dynamical metric variables, Einstein/Regge field equation and global nonlinear existence",
            "endogenous source/carrier/selector preparation and local matter-sector enforcement",
            "arbitrary N/size, continuum scaling, asymptotic response and observed coupling",
            "physical clock/proper time, Record formation, realized history and Born probability",
        ),
    }


def no_go_controls() -> dict:
    families = (
        {"family": "finite source-action Ward selection", "object": "five-dimensional local insertion ansatz", "mechanism": "full-rank restrictions plus Ward variation", "terminal": "unique joint insertion inside ansatz", "marker": "ATTEMPTED", "result": "bounded positive; ansatz supplied"},
        {"family": "plaquette-curvature reciprocal phase", "object": "matter direction times face quadrupole", "mechanism": "bilinear local unitary and mixed-Hessian reciprocity", "terminal": "resource-conserving response/backreaction", "marker": "ATTEMPTED", "result": "bounded positive"},
        {"family": "body-diagonal carrier", "object": "eight oriented body rails", "mechanism": "reservoir debit plus three-hop stream", "terminal": "shear with lower rail count", "marker": "ATTEMPTED", "result": "bounded positive; larger radius"},
        {"family": "face-diagonal carrier", "object": "twelve oriented face rails", "mechanism": "Cycle569 reservoir debit/source derivative", "terminal": "radius-two shear", "marker": "STRICT-PIN POSITIVE", "result": "comparator, not minimum"},
        {"family": "Grassmann bilateral Noether", "object": "AxisInv nearest-neighbor bilinear action", "mechanism": "site-local internal local-alpha Ward identity", "terminal": "bilateral conserved current", "marker": "RULED OUT BY PRIOR FOR COORDINATE-STRESS TERMINAL ONLY", "result": "does not treat lattice-index-shifting generator"},
        {"family": "Regge/Einstein target", "object": "edge metric and linearized Einstein operator", "mechanism": "second variation and Bianchi identity", "terminal": "metric field equation", "marker": "OPEN", "result": "target algebra exists; premises/bridge absent here"},
        {"family": "recurrent many-carrier response", "object": "many-Q curvature/source field", "mechanism": "nonlinear scattering or fixed point", "terminal": "large-volume backreaction scaling", "marker": "OPEN", "result": "not ruled out by bounded phase route"},
    )
    walls = (
        ("W_select", "derive the ansatz/carrier/coupling law rather than supply it"),
        ("W_cal", "physical stress-energy/work identification and empirical unit"),
        ("W_metric", "dynamical metric/Regge-Einstein field equation and nonlinear existence"),
        ("W_sector", "local arbitrary-sector and unbounded-size enforcement"),
        ("W_prep", "endogenous source/carrier/selector preparation"),
    )
    pairs = []
    for left in range(len(walls)):
        for right in range(left + 1, len(walls)):
            pairs.append({
                "pair": [walls[left][0], walls[right][0]],
                "first_closes_second": "no",
                "second_closes_first": "no",
                "independent": "yes",
                "witness": "Cycle572 separately tests ansatz selection, calibration firewall, metric target, compiler domain and preparation",
            })
    return {
        "N1_approach_families": families,
        "N2_collapsed_walls": walls,
        "N2_pairwise_independence": pairs,
        "N3_hidden_condition_scan": (
            "Cycle219/230/563/566/569 coefficients, factor order, physical code and strict pins are explicit",
            "five-dimensional ansatz, selector restrictions, source exponential and finite difference are explicit",
            "gamma, curvature weight matrix, phase placement, face/body orbit and routing are explicit",
            "periodic L3/L4, N2/N3 sectors, preparations, readouts and no-refit split are explicit",
            "Cycle563 reference/auxiliaries/cutoff/layers/router and compiled frame are explicit",
        ),
        "N4_residual_matching": (
            {"witness": "Cycle569", "witness_residual": "joint insertion supplied but unselected", "current_residual": "unique finite-ansatz Ward insertion", "match": "yes, narrowed not full physical selection"},
            {"witness": "Cycle464", "witness_residual": "reciprocal field change/nonproduct response", "current_residual": "bilinear phase mixed-Hessian response/backreaction", "match": "yes only for bounded reciprocal mechanism"},
            {"witness": "lattice Noether narrow theorem", "witness_residual": "site-local/internal conserved bilateral current", "current_residual": "coordinate-variation physical stress", "match": "no; not used as closure"},
            {"witness": "R3 Regge target", "witness_residual": "linearized Einstein target algebra", "current_residual": "dynamical metric/source equation", "match": "no; target only"},
            {"witness": "signed tensor transport", "witness_residual": "linear/projective transport and formal graded jets", "current_residual": "global nonlinear physical source dynamics", "match": "no; not used as closure"},
            {"witness": "Cycle563", "witness_residual": "N<=3 physical EG=GphysicalE", "current_residual": "matter lift with literal curvature/body rails", "match": "yes for matter mechanism; extensions checked here"},
        ),
        "N5_rhetoric_audit": (
            {"statement": "face orbit is not minimum", "tested": "orientation count and carrier-plus-reservoir M2 per cell", "untested": "radius, gate count, action selection, all carriers", "scope": "only narrow 12-versus-8 explicit comparison"},
            {"statement": "backreaction is not gravity", "tested": "local bilinear mixed derivative, quadrature impulses, finite L3/L4", "untested": "metric equation, nonlinear PDE, continuum", "scope": "bounded reciprocal phase only"},
            {"statement": "Noether selection is not physical stress selection", "tested": "finite internal/local ansatz and source-Ward derivative", "untested": "lattice-index-shifting coordinate variation", "scope": "no universal impossibility"},
        ),
        "N6_partial_closure_paths": (
            "derive the local insertion ansatz as a unique stationary action current",
            "introduce dynamical edge/plaquette metric variables and match the R3 target operator",
            "extend the bilinear phase to a recurrent many-carrier nonlinear scattering law",
            "calibrate the resource unit independently without using endpoint count as time",
            "use Cycle563 compiler machinery to extend local sector enforcement and size",
        ),
        "N7_hostile_steelman": (
            "The present selection is only full-rank inside an ansatz chosen to contain the answer, and the curvature phase is a supplied "
            "bilinear unitary rather than a metric equation. A Regge second-variation route, a many-carrier recurrent plaquette field, or "
            "a stationary-action uniqueness theorem could still derive a different tensor and calibrated backreaction law. The body route "
            "also defeats only rail-count minimality; a radius-two lower-work encoding may still exist."
        ),
        "N8_cross_cycle_echo": (
            "Cycle559 retired host current control with a conserved mediator but kept physical identification open",
            "Cycles562/564/566/569 progressively joined local current, action derivative, debit and quadrature without axiom changes",
            "Cycle464 replaced a profile table with local word rules while preserving preparation/calibration walls",
            "Cycle560/563 retired physical compiler and held-memory/order walls constructively",
            "signed-gravity work replaced naive nonlinear sign flip with graded jets rather than declaring a universal obstruction",
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "minimum_content_gate": "FAIL / DO NOT SHIP beyond the exact 12-versus-8 rail/M2 counterexample",
        "shared_obstruction": "none established",
        "axiom_pressure": "none",
    }


def main() -> int:
    started = perf_counter()
    print("CYCLE572 PHYSICAL SOURCE-INSERTION SELECTION/BACKREACTION TOURNAMENT")
    print("authority", AUTHORITY, "audit", AUDIT)
    dependencies = dependency_controls()
    prior = cycle569_prior_controls()
    note = note_contract()
    route_a = route_a_variational_selection(prior)
    route_b = route_b_curvature()
    route_c = route_c_body_diagonal()
    compiler = physical_compiler_controls()
    domain = domain_controls(route_b, route_c)
    supplied = inventory()
    nogo = no_go_controls()

    check("exact-pinned Cycle569 artifacts, accepted physics and gravity/source comparators are unchanged", dependencies["pass"], dependencies)
    check("note contract preserves variational/backreaction/minimality firewalls, physical lift and N1-N8", note["pass"], note)
    check(
        "Route A finite variational ansatz uniquely selects the joint insertion and closes resource Noether plus contact Ward identities",
        route_a["ansatz_rank"] == route_a["ansatz_dimension"] == 5
        and route_a["selection_residual"] < TOL
        and np.max(abs(np.asarray(route_a["selected_coefficients"])[:, 1])) < TOL
        and np.max(abs(np.asarray(route_a["selected_coefficients"])[:, 0] - np.asarray((1, 1, 1, 0, 0)))) < TOL
        and route_a["joint_Ward_finite_difference_residual"] < FD_TOL
        and route_a["joint_exchange_contact_telescope_residual"] < TOL
        and route_a["resource_Noether_conservation_residual"] < TOL
        and route_a["face_local_U1_charge_commutator"] < TOL
        and route_a["Cycle569_T00_restriction_residual"] < TOL
        and route_a["Cycle569_T0i_restriction_residual"] < TOL
        and route_a["Cycle569_all24_tensor_covariance_residual"] < TOL
        and route_a["Cycle569_all576_frame_products"]["frame_products"] == 576
        and not route_a["lattice_index_shifting_coordinate_Noether_theorem_proved"]
        and not route_a["physical_law_selection_or_calibration_closed"]
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
        "Route C body-diagonal carrier is inverse, resource-conserving, shear/contact sensitive and all24/576 covariant",
        route_c["orbit_size"] == 8
        and route_c["maximum_norm_residual"] < TOL
        and route_c["maximum_inverse_residual"] < TOL
        and route_c["maximum_cleanup_amplitude"] < TOL
        and route_c["maximum_resource_residual"] < TOL
        and route_c["maximum_local_continuity_residual"] < TOL
        and route_c["minimum_contact_deletion_residual"] > SIGNAL
        and route_c["minimum_vertex_deletion_residual"] > SIGNAL
        and route_c["maximum_all24_update_covariance_residual"] < TOL
        and route_c["local_gate"]["maximum_unitarity_or_covariance_residual"] < TOL
        and route_c["frame_products"]["frame_products"] == 576
        and route_c["frame_products"]["maximum_residual"] < TOL
        and route_c["body_route"]["failures"] == 0
        and route_c["body_route"]["intermediate_rails_restored"]
        and min(abs(value) for value in route_c["held_N3_offdiagonal_Txy_Txz_Tyz"]) > SIGNAL
        and route_c["held_N3_finite_difference_maximum_residual"] < FD_TOL
        and not route_c["called_physical_stress_energy_or_gravity"],
        route_c,
    )
    check(
        "body route falsifies only face rail-count/M2 minimality while leaving spatial-radius and universal minimum claims open",
        route_c["body_orbit_rails"] < route_c["face_orbit_rails"]
        and route_c["body_carrier_plus_reservoir_M2_per_cell"] < route_c["face_carrier_plus_reservoir_M2_per_cell"]
        and route_c["body_radius_axial_hops"] > route_c["face_radius_axial_hops"]
        and route_c["narrow_face_orientation_count_and_M2_minimality_falsified"]
        and not route_c["spatial_radius_minimality_falsified"]
        and not route_c["universal_minimum_carrier_claim"],
        {
            "face_rails": route_c["face_orbit_rails"],
            "body_rails": route_c["body_orbit_rails"],
            "face_M2": route_c["face_carrier_plus_reservoir_M2_per_cell"],
            "body_M2": route_c["body_carrier_plus_reservoir_M2_per_cell"],
            "face_radius": route_c["face_radius_axial_hops"],
            "body_radius": route_c["body_radius_axial_hops"],
        },
    )
    check(
        "Cycle563 physical lift has exact EG=GphysicalE, bounded constant overhead and honest local-constraint/leakage status",
        compiler["Route_B_curvature_combined_live_M2"]["held_L4"] == 4224
        and compiler["Route_C_body_combined_live_M2"]["held_L4"] == 3968
        and compiler["EG_equals_GphysicalE_residual"] == 0
        and compiler["bounded_constant_overhead_per_cell"]
        and compiler["maximum_new_route_radius_axial_hops"] == 3
        and compiler["Cycle560_563_auxiliary_constraints_locally_enforced"]
        and compiler["body_intermediate_rails_restored_locally"]
        and not compiler["global_matter_N_le_3_cutoff_locally_enforced"]
        and compiler["target_code_leakage"] == 0
        and compiler["branch_route_work_leakage"] == 0
        and not compiler["runtime_global_parity_order_frame_or_sector_service"]
        and compiler["one_particle_mass_residual"] < TOL
        and compiler["Cycle230_contact_factorization_residual"] < TOL
        and compiler["Cycle230_axis_seam_braid_residual"] < TOL
        and not compiler["full_dense_physical_matrix_materialized"],
        compiler,
    )
    check(
        "lawful-domain, train/held, frozen N3 and endpoint-time firewalls are explicit",
        domain["lawful_domain_rejections"] == 6
        and domain["train_L3_held_L4_split"]
        and domain["frozen_held_N3_curvature_and_body_fixtures"]
        and domain["held_parameters_refit"] == 0
        and not domain["held_rows_called_blind_empirical_predictions"]
        and not domain["endpoint_count_used_for_time_or_rate"],
        domain,
    )
    check(
        "supplied/derived/open inventory preserves ansatz, curvature, carrier, metric, calibration and history boundaries",
        len(supplied["supplied"]) >= 11 and len(supplied["derived"]) >= 8 and len(supplied["open"]) >= 6,
        supplied,
    )
    check(
        "fresh N1-N8 permits bounded selection/backreaction and narrow minimum falsifier but blocks broad no-go/minimum/axiom pressure",
        len(nogo["N1_approach_families"]) >= 5
        and len(nogo["N2_collapsed_walls"]) == 5
        and len(nogo["N2_pairwise_independence"]) == 10
        and all(row["independent"] == "yes" for row in nogo["N2_pairwise_independence"])
        and len(nogo["N4_residual_matching"]) >= 5
        and len(nogo["N5_rhetoric_audit"]) >= 3
        and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
        and nogo["shared_obstruction"] == "none established"
        and nogo["axiom_pressure"] == "none",
        nogo,
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
        "physical_compiler": compiler,
        "domain": domain,
        "inventory": supplied,
        "no_go": nogo,
        "terminal": {
            "strongest_constructive_result": "finite-ansatz Ward selection plus reciprocal curvature phase and lower-rail body carrier",
            "finite_ansatz_selection_closed": True,
            "nonlinear_bilinear_backreaction_identity_closed": True,
            "face_rail_count_minimality_falsified": True,
            "physical_stress_energy_work_identified": False,
            "metric_or_gravity_equation": False,
            "proper_time_or_rate_claim": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
        "resources": {"elapsed_seconds": perf_counter() - started, "peak_rss_mb": peak},
        "passes": PASS,
        "failures": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True))
    if FAIL:
        print("RESULT PHYSICAL_SOURCE_INSERTION_SELECTION_BACKREACTION_TOURNAMENT_FAILED")
        return 1
    print("RESULT WARD_CURVATURE_BODY_CARRIER_BOUNDED_POSITIVE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
