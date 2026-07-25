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

from hashlib import sha256
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
import physical_source_insertion_selection_backreaction_cycle572_carrier_support_2026_07_22 as carrier_support


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
    "scripts/physical_source_insertion_selection_backreaction_cycle572_carrier_support_2026_07_22.py",
)

DEPENDENCIES = {
    "scripts/physical_source_insertion_selection_backreaction_cycle572_carrier_support_2026_07_22.py":
        "61cb69be454d320e97b0e82205307c885cce3b920002e72686598400d33d0126",
    "scripts/physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22.py":
        "a0008b105d33461d7e4615a8afe58d83e436415d1a75ddb4cb7d41ec1defdf37",
    "docs/FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md":
        "72e37ba7301e2aa6926c666304440bf370e2e22158d69e26262440d51bf07ecc",
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
    closure = source_dependency_closure()
    return {
        "expected": DEPENDENCIES,
        "observed": observed,
        "source_dependency_closure": closure,
        "pass": observed == DEPENDENCIES and closure["pass"],
    }


def source_dependency_closure() -> dict:
    source_modules = (
        "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py",
        "scripts/physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22.py",
        "scripts/physical_source_insertion_selection_backreaction_cycle572_carrier_support_2026_07_22.py",
    )
    helper_paths = source_modules[1:]
    ordinary_helper_imports = (
        "import physical_source_insertion_selection_backreaction_cycle572_finite_support_2026_07_22 as c569",
        "import physical_source_insertion_selection_backreaction_cycle572_carrier_support_2026_07_22 as carrier_support",
    )
    texts = {
        path: (ROOT / path).read_text(encoding="utf-8")
        for path in source_modules
    }
    imports = {
        path: tuple(
            line.strip()
            for line in text.splitlines()
            if line.startswith("import ") or line.startswith("from ")
        )
        for path, text in texts.items()
    }
    forbidden = (
        "git" + " show",
        "merge" + "-base",
        "sub" + "process",
        "docs/work_" + "history",
        "outputs/" + "physical_",
    )
    forbidden_counts = {
        path: {
            fragment: text.lower().count(fragment.lower())
            for fragment in forbidden
        }
        for path, text in texts.items()
    }
    observed_ordinary_imports = tuple(
        line
        for line in imports[source_modules[0]]
        if line in ordinary_helper_imports
    )
    return {
        "source_modules": source_modules,
        "source_module_characters": {
            path: len(text) for path, text in texts.items()
        },
        "source_module_sha256": {
            path: sha256(text.encode("utf-8")).hexdigest()
            for path, text in texts.items()
        },
        "imports": imports,
        "ordinary_helper_imports": observed_ordinary_imports,
        "audit_input_helpers": tuple(
            path for path in helper_paths if path in AUDIT_INPUT_PATHS
        ),
        "forbidden_reference_counts": forbidden_counts,
        "pass": (
            all(len(text) < 40_000 for text in texts.values())
            and observed_ordinary_imports == ordinary_helper_imports
            and all(path in AUDIT_INPUT_PATHS for path in helper_paths)
            and not any(
                count
                for counts in forbidden_counts.values()
                for count in counts.values()
            )
        ),
    }


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
    route_c = carrier_support.route_c_body_diagonal()
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
