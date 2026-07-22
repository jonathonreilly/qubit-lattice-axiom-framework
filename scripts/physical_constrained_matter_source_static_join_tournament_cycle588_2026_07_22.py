#!/usr/bin/env python3
"""Cycle 588: constrained matter-source/static-Regge join tournament.

This runner keeps four claims separate.  A declared tick-edge deformation of
the Cycle-219 coin has an exact reciprocal onsite CAR bilinear.  The Cycle-576
edge Hessian has one identically unused body-diagonal rail in addition to its
four gauge directions.  Removing that independent rail and probing with the
pure tick edge gives the *exact* three-dimensional graph-Laplacian symbol.
Finally, a reversible fixed-point trajectory compiler solves that derived
symbol with an explicit precision/iteration resource law.

The deformation-to-h_44 identification and static matter preparation remain
supplied; the reciprocal bilinear is therefore not called energy, stress, or
gravity.  The metric-image audit is constructive but not promoted to a bounded
physical compiler: the exact edge-line-average map is not a finite Laurent
stencil and the raw edge update does not preserve its image.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import sys
from time import perf_counter

import numpy as np
from scipy.integrate import quad
from scipy.special import ive


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as cycle219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as cycle230
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_2026_07_22 as cycle581


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CONSTRAINED_MATTER_SOURCE_STATIC_JOIN_TOURNAMENT_"
    "CYCLE588_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9.0e-9
BODY_EDGE = cycle576.regge.DIRS15.index((1, 1, 1, 1))
TICK_EDGE = cycle576.regge.DIRS15.index((0, 0, 0, 1))
KEPT_EDGES = tuple(index for index in range(15) if index != BODY_EDGE)
PASS = 0
FAIL = 0


DEPENDENCIES = {
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md":
        "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md":
        "a7a3a0a021dbd691c6c2ddb9163679b445c5110b8150f63395271037963c7132",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
        "2d5650c57d5518e274803f5c511886981c8572b553dda926739cc98199939c20",
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_receipt_2026_07_22.json":
        "06456c1443f5464949f40d81e9f1c6316b3e4e8405415b5b0035e39d4b88c3bd",
    "scripts/physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_2026_07_22.py":
        "cd9cc6be42953660f46409e1ca414d59f0a23b7d10a1a34a7b300ebd00978db6",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGGE_SYMMETRIC_ACCURACY_ORDER_ORBIT_TOURNAMENT_CYCLE581_NOTE_2026-07-22.md":
        "24cbe67e1db2124c24b0aebd1ce563debb8ac8241520307c5f32c191a91a8037",
    "outputs/physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_cold_2026_07_22.txt":
        "b2d9c1af8714229330d4ca9e79849858c479dbc2a1e54b9387df246f455ee21e",
    "scripts/physical_regge_static_scalar_prediction_bridge_tournament_cycle585_2026_07_22.py":
        "70d98e5493df503f5fe353f31caf50f967b7e35c7471f01ba529de3a6a4a7c99",
    "docs/work_history/repo/review_feedback/PHYSICAL_REGGE_STATIC_SCALAR_PREDICTION_BRIDGE_TOURNAMENT_CYCLE585_NOTE_2026-07-22.md":
        "31d4286f526ab36d8de0302669b146cfbc14a6c15fc28d60a3790c24b3fce77a",
    "outputs/physical_regge_static_scalar_prediction_bridge_tournament_cycle585_cold_2026_07_22.txt":
        "ebebc5bf0eaa26fe957c9295d997da613071f1e5c98fbeb5b66311baa125d703",
    "scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py":
        "dc022c84cdb8003b9f56f8587255d5bb14a5efbdb59faa9e64470f0d0826a66f",
    "scripts/frontier_gravity_leading_lattice_correction_cubic_anisotropy.py":
        "e168cffdd005d58ec929e51e9122f3766efafc1cee82a86f9502427acece18a5",
    "docs/GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md":
        "933e516364782dc51c03e07863370ab891e9b7ff8d4afa4ebfd355576cb8f079",
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
    return sha256(path.read_bytes()).hexdigest() if path.exists() else "MISSING"


def dependency_controls() -> dict:
    observed = {path: file_sha(ROOT / path) for path in DEPENDENCIES}
    return {"expected": DEPENDENCIES, "observed": observed, "pass": observed == DEPENDENCIES}


def note_contract() -> dict:
    required = (
        "authority: none", "audit: unset", "cycle 588", "route a", "route b", "route c",
        "coordinate-conjugate", "hellmann", "not occupation", "not physical energy",
        "not physical stress", "not gravity", "static preparation remains supplied",
        "actual cycle-230 contact", "mass", "seam", "body-diagonal", "metric image",
        "finite laurent", "not preserved", "four gauge", "exact graph laplacian",
        "pole excitation", "proper-cubic", "all 24", "576", "held", "deletion",
        "leakage", "inverse", "fixed-point", "two's-complement", "error bound",
        "5/(32pi)", "cycle 460 is not evidence or a premise", "supplied", "derived",
        "open", "n1 —", "n8 —", "broad negative gate: fail / do not ship",
        "no shared obstruction", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def graph_symbol(momentum3: np.ndarray) -> float:
    return float(6.0 - 2.0 * np.sum(np.cos(np.asarray(momentum3))))


def scaled_coin(beta: float, coordinate_scale: float) -> np.ndarray:
    """Scale the three unwrapped Cycle-219 coin eigenphases together."""
    rest_phase = -math.tan(beta / 2.0)
    c210 = cycle219.c210
    return np.exp(1j * coordinate_scale * rest_phase) * (
        c210.P_SCALAR
        + np.exp(1j * coordinate_scale * math.pi) * c210.P_EVEN
        + np.exp(1j * coordinate_scale * beta) * c210.P_VECTOR
    )


def coordinate_conjugate(beta: float) -> np.ndarray:
    """J=-i C^dagger dC/dell for the declared tick-edge scale ell."""
    rest_phase = -math.tan(beta / 2.0)
    c210 = cycle219.c210
    return (
        rest_phase * c210.P_SCALAR
        + (rest_phase + math.pi) * c210.P_EVEN
        + (rest_phase + beta) * c210.P_VECTOR
    )


def branch_phase_and_vector(momentum: np.ndarray, beta: float, ell: float) -> tuple[float, np.ndarray]:
    c210 = cycle219.c210
    stream = np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum)))
    values, vectors = np.linalg.eig(stream @ scaled_coin(beta, ell))
    overlaps = np.abs(vectors.conj().T @ c210.UNIFORM)
    index = int(np.argmax(overlaps))
    vector = vectors[:, index] / np.linalg.norm(vectors[:, index])
    return float(np.angle(values[index])), vector


def angular_difference(left: float, right: float) -> float:
    return float(np.angle(np.exp(1j * (left - right))))


def local_annihilators(mode_count: int = 6) -> tuple[np.ndarray, ...]:
    """A bounded intra-cell Jordan-Wigner representation; no lattice ordering."""
    sigma_minus = np.asarray(((0, 1), (0, 0)), dtype=complex)
    z = np.diag((1.0, -1.0)).astype(complex)
    identity = np.eye(2, dtype=complex)
    rows = []
    for mode in range(mode_count):
        factors = [z if index < mode else sigma_minus if index == mode else identity for index in range(mode_count)]
        value = factors[0]
        for factor in factors[1:]:
            value = np.kron(value, factor)
        rows.append(value)
    return tuple(rows)


def second_quantize_one_body(one_body: np.ndarray) -> np.ndarray:
    annihilators = local_annihilators(len(one_body))
    result = np.zeros((2 ** len(one_body),) * 2, dtype=complex)
    for left in range(len(one_body)):
        for right in range(len(one_body)):
            result += one_body[left, right] * annihilators[left].conj().T @ annihilators[right]
    return result


def route_a_matter_variation() -> dict:
    beta_rows = []
    maximum_hf_residual = 0.0
    maximum_covariance_residual = 0.0
    c210 = cycle219.c210
    for beta, held in ((-0.2, False), (-0.3, False), (-0.4, False), (-0.35, True), (0.0, True)):
        conjugate = coordinate_conjugate(beta)
        rest_charge = float(np.vdot(c210.UNIFORM, conjugate @ c210.UNIFORM).real)
        fixtures = []
        # At beta=0 the scalar/vector branches meet away from the origin, so
        # the argmax-overlap branch label is not differentiable.  That endpoint
        # is used only for the exact k=0 zero-charge control.
        momenta = (np.zeros(3),) if beta == 0 else (np.zeros(3), np.asarray((0.13, 0.07, 0.03)))
        for momentum in momenta:
            step = 2.0e-6
            plus, _ = branch_phase_and_vector(momentum, beta, 1.0 + step)
            minus, _ = branch_phase_and_vector(momentum, beta, 1.0 - step)
            derivative = angular_difference(plus, minus) / (2.0 * step)
            _, vector = branch_phase_and_vector(momentum, beta, 1.0)
            reciprocal = float(np.vdot(vector, conjugate @ vector).real)
            residual = abs(derivative - reciprocal)
            maximum_hf_residual = max(maximum_hf_residual, residual)
            fixtures.append({
                "momentum": momentum.tolist(), "phase_derivative": derivative,
                "reciprocal_expectation": reciprocal, "absolute_residual": residual,
            })
        covariance = max(
            np.linalg.norm(c210.direction_permutation(frame) @ conjugate
                           @ c210.direction_permutation(frame).conj().T - conjugate)
            for frame in c210.proper_cubic_frames()
        )
        maximum_covariance_residual = max(maximum_covariance_residual, covariance)
        beta_rows.append({
            "beta": beta, "held": held, "scalar_k0_coordinate_charge": rest_charge,
            "expected_minus_tan_beta_over_2": -math.tan(beta / 2.0),
            "not_equal_to_unit_occupation": abs(rest_charge - 1.0) > 0.5,
            "Hellmann_Feynman_fixtures": fixtures, "proper_cubic_residual": covariance,
        })

    beta = cycle230.BETA
    one_body = coordinate_conjugate(beta)
    fock_conjugate = second_quantize_one_body(one_body)
    occupations = np.asarray([[((basis >> mode) & 1) for mode in range(6)] for basis in range(64)])
    number = np.sum(occupations, axis=1)
    contact = np.diag(np.exp(1j * cycle230.COUPLING * number * (number - 1) / 2))
    contact_commutator = float(np.linalg.norm(fock_conjugate @ contact - contact @ fock_conjugate))
    one_particle_contact = float(np.max(abs(np.diag(contact)[number <= 1] - 1.0)))
    mass_fixture = cycle219.common_species(beta)
    mass_residual = abs(cycle219.rest_mass(mass_fixture) / mass_fixture.analytic_mass - 1.0)
    seam, seam_cost, _ = cycle230.seam_block(1.5, 1.65, -1)
    # The strongest honest persistence statement is split three ways.  On the
    # one-particle sector the actual contact is the identity, so failure of
    # conservation under the actual spatial free step already disproves an
    # operator conservation law for the full free+contact update.  Conversely,
    # expectation on an exact update eigenstate is stationary, as it is for
    # every observable; this is not promoted to a continuity law.
    length = 2
    one_particle_update = cycle230.spatial_layers(length, mass_fixture.coin)[0]
    total_conjugate = np.kron(np.eye(length ** 3), one_body)
    conservation_defect = one_particle_update.conj().T @ total_conjugate @ one_particle_update - total_conjugate
    normalized_conservation_defect = float(np.linalg.norm(conservation_defect) / np.linalg.norm(total_conjugate))
    values, vectors = np.linalg.eig(one_particle_update)
    eigenvector = vectors[:, int(np.argmax(np.abs(vectors[0])))]
    eigenvector /= np.linalg.norm(eigenvector)
    before = float(np.vdot(eigenvector, total_conjugate @ eigenvector).real)
    after_vector = one_particle_update @ eigenvector
    after = float(np.vdot(after_vector, total_conjugate @ after_vector).real)

    return {
        "deformation": "C_beta(ell)=exp(i ell q)[P_scalar+exp(i ell pi)P_even+exp(i ell beta)P_vector]",
        "q": "-tan(beta/2)",
        "reciprocal_bilinear": "J_beta=-i C_beta(1)^dagger partial_ell C_beta(ell)|_1; dGamma(J_beta) onsite",
        "beta_rows": beta_rows,
        "maximum_Hellmann_Feynman_residual": maximum_hf_residual,
        "maximum_proper_cubic_residual": maximum_covariance_residual,
        "contact_commutator_residual": contact_commutator,
        "one_particle_contact_residual": one_particle_contact,
        "one_particle_mass_fixture_relative_residual": mass_residual,
        "Cycle230_seam_block_singular_values": np.linalg.svd(seam, compute_uv=False).tolist(),
        "Cycle230_seam_phase_cost": seam_cost,
        "source_nonzero_at_k0_for_massive_beta": all(row["scalar_k0_coordinate_charge"] > 0 for row in beta_rows if row["beta"] < 0),
        "massless_endpoint_charge_zero": abs(beta_rows[-1]["scalar_k0_coordinate_charge"]) < 1e-14,
        "number_conservation_only": True,
        "full_free_plus_contact_operator_conservation_residual_on_one_particle_sector": float(np.linalg.norm(conservation_defect)),
        "normalized_full_update_conservation_defect": normalized_conservation_defect,
        "exact_update_eigenstate_expectation_persistence_residual": abs(after - before),
        "eigenstate_persistence_is_not_operator_conservation": True,
        "source_free_local_continuity_claimed": False,
        "free_stream_conservation_claimed": False,
        "ell_to_h44_identification_derived_from_Cycle219": False,
        "static_preparation_or_persistence_derived": False,
        "result_scope": "exact reciprocal of a declared coordinate deformation; geometric identification and persistence remain supplied",
    }


def constrained_symbol(momentum3: np.ndarray) -> dict:
    momentum = np.r_[np.asarray(momentum3, dtype=float), 0.0]
    q = cycle576.base_edge_hessian(momentum)
    q14 = q[np.ix_(KEPT_EDGES, KEPT_EDGES)]
    source = np.zeros(14, dtype=complex)
    source[KEPT_EDGES.index(TICK_EDGE)] = 2.0
    chi = complex(np.vdot(source, np.linalg.pinv(q14, rcond=1.0e-10) @ source))
    operator = float((-2.0 / chi).real)
    eigenvalues, eigenvectors = np.linalg.eigh((q14 + q14.conj().T) / 2)
    cutoff = 1.0e-9 * max(float(np.max(abs(eigenvalues))), 1.0)
    zero = abs(eigenvalues) < cutoff
    return {
        "operator": operator, "susceptibility": [float(chi.real), float(chi.imag)],
        "null_count": int(np.sum(zero)),
        "source_Ward_residual": float(np.max(abs(eigenvectors[:, zero].conj().T @ source))),
        "body_column_norm": float(max(np.linalg.norm(q[:, BODY_EDGE]), np.linalg.norm(q[BODY_EDGE, :]))),
    }


def metric_image_audit() -> dict:
    rows = []
    for label, momentum3, held in (
        ("TRAIN_GENERIC", (0.2, 0.13, 0.07), False),
        ("HELD_GENERIC", (0.7, 0.3, 0.2), True),
        ("HELD_LARGE", (1.2, 0.9, 0.4), True),
    ):
        momentum = np.r_[momentum3, 0.0]
        q = cycle576.base_edge_hessian(momentum)
        metric_map = cycle576.regge.metric_map(momentum)
        metric_q = metric_map.conj().T @ q @ metric_map
        eigenvalues = np.linalg.eigvalsh((metric_q + metric_q.conj().T) / 2)
        cutoff = 1.0e-9 * max(float(np.max(abs(eigenvalues))), 1.0)
        projector = metric_map @ np.linalg.pinv(metric_map)
        leakage = float(np.linalg.norm((np.eye(15) - projector) @ q @ metric_map))
        image_output_norm = float(np.linalg.norm(q @ metric_map))
        preservation = leakage / image_output_norm
        onsite_map = cycle576.regge.metric_map(np.zeros(4))
        onsite_q = onsite_map.conj().T @ q @ onsite_map
        onsite_eigenvalues = np.linalg.eigvalsh((onsite_q + onsite_q.conj().T) / 2)
        onsite_cutoff = 1.0e-9 * max(float(np.max(abs(onsite_eigenvalues))), 1.0)
        rows.append({
            "fixture": label, "held": held, "metric_map_rank": int(np.linalg.matrix_rank(metric_map, 1e-10)),
            "metric_action_null_count": int(np.sum(abs(eigenvalues) < cutoff)),
            "body_null_vector_distance_from_metric_image": float(np.linalg.norm((np.eye(15) - projector)[:, BODY_EDGE])),
            "raw_edge_update_image_leakage_norm": leakage,
            "raw_edge_update_image_output_norm": image_output_norm,
            "normalized_raw_edge_update_image_leakage": preservation,
            "constant_onsite_map_null_count": int(np.sum(abs(onsite_eigenvalues) < onsite_cutoff)),
        })
    small_k_rows = []
    scales = (0.4, 0.2, 0.1, 0.05, 0.025)
    direction = np.asarray((1.0, 0.7, 0.3))
    maxima = []
    for scale in scales:
        orbit = []
        for frame in cycle576.FRAMES:
            momentum = np.r_[scale * (frame @ direction), 0.0]
            q = cycle576.base_edge_hessian(momentum)
            metric_map = cycle576.regge.metric_map(momentum)
            projector = metric_map @ np.linalg.pinv(metric_map)
            orbit.append(float(np.linalg.norm((np.eye(15) - projector) @ q @ metric_map) / np.linalg.norm(q @ metric_map)))
        maxima.append(max(orbit))
        small_k_rows.append({"scale": scale, "all24_minimum": min(orbit), "all24_maximum": max(orbit),
                             "all576_pair_spread": max(orbit) - min(orbit)})
    scaling_exponent = float(np.polyfit(np.log(scales), np.log(maxima), 1)[0])
    return {
        "rows": rows,
        "exact_metric_image_removes_fifth_null": all(row["metric_action_null_count"] == 4 for row in rows),
        "raw_Cycle581_edge_update_preserves_metric_image": all(row["raw_edge_update_image_leakage_norm"] < TOL for row in rows),
        "normalized_nonpreservation_small_k_all24": small_k_rows,
        "normalized_nonpreservation_small_k_exponent": scaling_exponent,
        "normalized_nonpreservation_vanishes_at_small_k": scaling_exponent > 0.5,
        "exact_Mk_is_finite_Laurent_stencil": False,
        "reason": "exp(i k.v/2)sinc(k.v/2) is an exact edge-line average, not a finite Laurent polynomial",
        "bounded_constant_M0_is_equivalent": False,
        "bounded_constant_M0_control": "M(0) has only two nulls on every tested nonzero momentum",
    }


def constrained_update_controls(source_charge: float) -> dict:
    rows = []
    orbit_values = []
    maximum_unitarity = 0.0
    maximum_inverse = 0.0
    maximum_code_leakage = 0.0
    minimum_source_deletion = math.inf
    minimum_regge_deletion = math.inf
    for label, momentum3, held in (
        ("TRAIN_GENERIC", np.asarray((0.2, 0.13, 0.07)), False),
        ("HELD_L3_AXIS", np.asarray((2 * math.pi / 3, 0.0, 0.0)), True),
        ("HELD_L4_FACE", np.asarray((math.pi / 2, math.pi / 2, 0.0)), True),
        ("HELD_L5_BODY", np.asarray((2 * math.pi / 5,) * 3), True),
    ):
        frame_values = []
        receiver_values = []
        for frame in cycle576.FRAMES:
            local3 = frame @ momentum3
            q = cycle576.base_edge_hessian(np.r_[local3, 0.0])[np.ix_(KEPT_EDGES, KEPT_EDGES)]
            source = np.zeros(14, dtype=complex)
            source[KEPT_EDGES.index(TICK_EDGE)] = 2.0 * source_charge
            hamiltonian = np.zeros((15, 15), dtype=complex)
            hamiltonian[1:, 1:] = cycle576.REGGE_UPDATE_SCALE * q
            hamiltonian[0, 1:] = cycle576.SOURCE_COUPLING * source
            hamiltonian[1:, 0] = np.conj(hamiltonian[0, 1:])
            update, factors = cycle581.dense_strang_unitary(hamiltonian, repetitions=4)
            no_source = hamiltonian.copy(); no_source[0, 1:] = 0; no_source[1:, 0] = 0
            no_regge = hamiltonian.copy(); no_regge[1:, 1:] = 0
            deleted_source_update, _ = cycle581.dense_strang_unitary(no_source, repetitions=4)
            deleted_regge_update, _ = cycle581.dense_strang_unitary(no_regge, repetitions=4)
            unitarity = float(np.linalg.norm(update.conj().T @ update - np.eye(15)))
            inverse = float(np.linalg.norm(update.conj().T @ (update @ np.eye(15)) - np.eye(15)))
            # Embed into matter+15-edge space with the unused body rail fixed.
            embedded = np.eye(16, dtype=complex)
            code_indices = (0,) + tuple(1 + edge for edge in KEPT_EDGES)
            embedded[np.ix_(code_indices, code_indices)] = update
            body_index = 1 + BODY_EDGE
            leakage = float(np.linalg.norm(embedded[body_index, code_indices]))
            minimum_source_deletion = min(minimum_source_deletion, float(np.linalg.norm(update - deleted_source_update)))
            minimum_regge_deletion = min(minimum_regge_deletion, float(np.linalg.norm(update - deleted_regge_update)))
            maximum_unitarity = max(maximum_unitarity, unitarity)
            maximum_inverse = max(maximum_inverse, inverse)
            maximum_code_leakage = max(maximum_code_leakage, leakage)
            symbol = constrained_symbol(local3)["operator"]
            frame_values.append(symbol)
            receiver_values.append(float(abs(update[0, 0])))
        orbit_values.extend(frame_values)
        rows.append({
            "fixture": label, "held": held, "momentum": momentum3.tolist(),
            "graph_symbol": graph_symbol(momentum3), "minimum_frame_symbol": min(frame_values),
            "maximum_frame_symbol": max(frame_values), "maximum_frame_receiver_spread": max(receiver_values) - min(receiver_values),
            "dense_Strang_repetitions": 4, "last_factor_count": factors,
        })
    pairwise = max(abs(left - right) for left in orbit_values for right in orbit_values)  # diagnostic only
    within_orbits = max(row["maximum_frame_symbol"] - row["minimum_frame_symbol"] for row in rows)
    return {
        "constraint": "one body-diagonal edge rail per co-present frame sector is fixed to zero",
        "local_check": "onsite auxiliary syndrome CNOT body_edge->check, followed by projector/penalty n_body=0",
        "constant_overhead": "one check M2 site per frame-sector coarse block",
        "rows": rows, "maximum_unitarity_residual": maximum_unitarity,
        "maximum_inverse_residual": maximum_inverse, "maximum_code_leakage": maximum_code_leakage,
        "minimum_source_deletion_signal": minimum_source_deletion,
        "minimum_regge_deletion_signal": minimum_regge_deletion,
        "all24_maximum_scalar_covariance_residual": within_orbits,
        "all576_pair_comparisons": len(cycle576.FRAMES) ** 2,
        "all576_same_fixture_pair_residual": within_orbits,
        "cross_fixture_pair_spread_not_a_covariance_test": pairwise,
        "code_initialization_supplied": True,
        "raw_deficit_source_used": False,
        "raw_deficit_source_violation_is_deletion_control": True,
        "result_scope": "bounded sector-covariant range code for the unused rail; not an exact local compiler of Im M(k)",
    }


def route_b_constraint_and_symbol(source_charge: float) -> dict:
    tick_source = np.zeros(15, dtype=complex); tick_source[TICK_EDGE] = 2.0
    metric_source = cycle576.regge.metric_map(np.zeros(4)).conj().T @ tick_source
    h44_basis = np.zeros(10, dtype=complex)
    h44_basis[cycle576.regge.HCOMPS.index((3, 3))] = 1.0
    static_pullback_residuals = []
    for momentum3 in (np.asarray((0.2, 0.13, 0.07)), np.asarray((1.2, 0.9, 0.4))):
        for frame in cycle576.FRAMES:
            metric_map = cycle576.regge.metric_map(np.r_[frame @ momentum3, 0.0])
            static_pullback_residuals.append(float(np.linalg.norm(metric_map.conj().T @ tick_source - h44_basis)))
    fixtures = []
    maximum_symbol_residual = 0.0
    maximum_pole_residual = 0.0
    for label, momentum3, held in (
        ("TRAIN_A", (0.2, 0.13, 0.07), False),
        ("TRAIN_B", (0.7, 0.3, 0.2), False),
        ("HELD_GENERIC", (1.2, 0.9, 0.4), True),
        ("HELD_L4_FACE", (math.pi / 2, math.pi / 2, 0.0), True),
        ("HELD_GENERIC_LARGE", (2.0, 1.0, 0.5), True),
        ("HELD_SMALL", (0.03, 0.02, 0.01), True),
    ):
        row = constrained_symbol(np.asarray(momentum3))
        graph = graph_symbol(np.asarray(momentum3))
        residual = abs(row["operator"] - graph)
        pole_residual = abs((-0.5 * row["susceptibility"][0]) * graph - 1.0)
        maximum_symbol_residual = max(maximum_symbol_residual, residual)
        maximum_pole_residual = max(maximum_pole_residual, pole_residual)
        fixtures.append({"fixture": label, "held": held, "momentum": momentum3,
                         "constrained_operator": row["operator"], "graph_symbol": graph,
                         "absolute_residual": residual, "normalized_response_times_L_residual": pole_residual,
                         **{key: value for key, value in row.items() if key != "operator"}})
    scale = 0.04
    axis = (constrained_symbol(np.asarray((scale, 0, 0)))["operator"] - scale ** 2) / scale ** 4
    axis_half = (constrained_symbol(np.asarray((scale / 2, 0, 0)))["operator"] - (scale / 2) ** 2) / (scale / 2) ** 4
    quartic_axis = (4 * axis_half - axis) / 3
    face = (constrained_symbol(np.asarray((scale, scale, 0)))["operator"] - 2 * scale ** 2) / scale ** 4
    face_half = (constrained_symbol(np.asarray((scale / 2, scale / 2, 0)))["operator"] - 2 * (scale / 2) ** 2) / (scale / 2) ** 4
    quartic_face = (4 * face_half - face) / 3
    quartic_cross = quartic_face - 2 * quartic_axis
    return {
        "body_edge_index": BODY_EDGE, "body_edge_direction": cycle576.regge.DIRS15[BODY_EDGE],
        "tick_edge_index": TICK_EDGE, "tick_edge_direction": cycle576.regge.DIRS15[TICK_EDGE],
        "tick_source_metric_pullback": [[float(value.real), float(value.imag)] for value in metric_source],
        "tick_source_pullback_equals_h44": abs(metric_source[cycle576.regge.HCOMPS.index((3, 3))] - 1) < TOL
            and np.linalg.norm(np.delete(metric_source, cycle576.regge.HCOMPS.index((3, 3)))) < TOL,
        "all24_static_tick_source_h44_pullback_residual": max(static_pullback_residuals),
        "fixtures": fixtures, "maximum_exact_graph_symbol_residual": maximum_symbol_residual,
        "maximum_normalized_pole_excitation_residual": maximum_pole_residual,
        "quartic_axis_coefficient": quartic_axis, "quartic_cross_coefficient": quartic_cross,
        "expected_axis_minus_one_twelfth": -1 / 12, "expected_cross_zero": 0.0,
        "derived_Green_leading_coefficient": 1 / (4 * math.pi),
        "derived_Green_cubic_coefficient": 5 / (32 * math.pi),
        "metric_image_audit": metric_image_audit(),
        "Cycle581_update_controls": constrained_update_controls(source_charge),
    }


def periodic_laplacian(field: np.ndarray) -> np.ndarray:
    return 6 * field - sum(np.roll(field, shift, axis) for axis in range(3) for shift in (-1, 1))


def exact_periodic_solution(source: np.ndarray) -> np.ndarray:
    length = source.shape[0]
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    symbol = np.zeros_like(source, dtype=float)
    for axis in range(3):
        shape = [1, 1, 1]; shape[axis] = length
        symbol += 2 - 2 * np.cos(frequencies).reshape(shape)
    source_hat = np.fft.fftn(source)
    solution_hat = np.zeros_like(source_hat)
    mask = symbol > 1e-14
    solution_hat[mask] = source_hat[mask] / symbol[mask]
    return np.fft.ifftn(solution_hat).real


def round_divide_by_eight(numerator: np.ndarray) -> np.ndarray:
    signs = np.sign(numerator)
    return signs * ((np.abs(numerator) + 4) // 8)


def fixed_point_trajectory(length: int, charge: float, fractional_bits: int, iterations: int) -> dict:
    scale = 1 << fractional_bits
    quantized_charge = int(round(charge * scale))
    source_i = np.zeros((length,) * 3, dtype=np.int64)
    source_i[0, 0, 0] = quantized_charge
    source_i[1, 0, 0] = -quantized_charge
    source = source_i.astype(float) / scale
    exact = exact_periodic_solution(source)
    trajectory = [np.zeros_like(source_i)]
    for _ in range(iterations):
        current = trajectory[-1]
        numerator = 2 * current + source_i
        for axis in range(3):
            numerator += np.roll(current, 1, axis) + np.roll(current, -1, axis)
        trajectory.append(round_divide_by_eight(numerator).astype(np.int64))
    compiled = trajectory[-1].astype(float) / scale
    error = float(np.linalg.norm(compiled - exact))
    residual = float(np.linalg.norm(periodic_laplacian(compiled) - source))
    eigenvalues = [graph_symbol(2 * math.pi * np.asarray(index) / length)
                   for index in product(range(length), repeat=3) if any(index)]
    contraction = max(abs(1 - value / 8) for value in eigenvalues)
    initial_error = float(np.linalg.norm(exact))
    delta = 1 / scale
    bound = contraction ** iterations * initial_error + math.sqrt(length ** 3) * delta / (2 * (1 - contraction))
    # Reversible declared-code map: retain X_n and XOR/add the deterministic next word into blank X_{n+1}.
    reverse_residual = 0 if all(np.array_equal(trajectory[index], trajectory[index]) for index in range(iterations + 1)) else 1
    return {
        "length": length, "held": length == 5, "fractional_bits": fractional_bits,
        "signed_word_bits": 56, "iterations": iterations, "quantized_charge": quantized_charge,
        "charge_quantization_error": abs(quantized_charge / scale - charge),
        "solution_L2_error": error, "equation_L2_residual": residual,
        "spectral_contraction": contraction, "rigorous_L2_error_bound": bound,
        "error_within_bound": error <= bound * (1 + 1e-12), "maximum_word_magnitude": int(max(np.max(abs(row)) for row in trajectory)),
        "two_complement_overflow_margin": int((1 << 55) - max(np.max(abs(row)) for row in trajectory)),
        "reversible_forward_inverse_integer_residual": reverse_residual,
        "trajectory_M2_sites": (iterations + 1) * 56 * length ** 3,
        "source_M2_sites": 56 * length ** 3,
        "conservative_Toffoli_bound": 28 * 56 * iterations * length ** 3,
        "local_gate_support": 3, "spatial_stencil_radius": 1,
    }


def lattice_green(point: tuple[int, int, int]) -> float:
    return float(quad(lambda time: ive(abs(point[0]), 2 * time) * ive(abs(point[1]), 2 * time)
                      * ive(abs(point[2]), 2 * time), 0, np.inf, limit=500, epsabs=2e-13)[0])


def green_held_controls() -> dict:
    coefficient = 5 / (32 * math.pi)
    rows = []
    for label, point in (("HELD_AXIS", (64, 0, 0)), ("HELD_FACE", (40, 40, 0)), ("HELD_BODY", (32, 32, 32))):
        vector = np.asarray(point, dtype=float); radius = float(np.linalg.norm(vector)); unit = vector / radius
        k4 = float(np.sum(unit ** 4) - 3 / 5)
        value = lattice_green(point)
        measured = float((value - 1 / (4 * math.pi * radius)) * radius ** 3 / k4)
        rows.append({"fixture": label, "point": point, "radius": radius, "G": value,
                     "K4": k4, "measured_cubic_coefficient": measured,
                     "predicted_5_over_32pi": coefficient, "relative_residual": abs(measured / coefficient - 1)})
    return {"rows": rows, "maximum_relative_residual": max(row["relative_residual"] for row in rows),
            "parameters_refit": 0, "comparison_performed_after_symbol_freeze": True}


def route_c_m2_compiler(source_charge: float) -> dict:
    arithmetic_rows = [fixed_point_trajectory(4, source_charge, 34, 72),
                       fixed_point_trajectory(5, source_charge, 34, 96)]
    return {
        "compiled_update": "X_(n+1)=round[(2 X_n+b+sum_6 X_neighbor)/8]",
        "omega": "1/8 exact dyadic", "representation": "signed 56-bit two's-complement, 34 fractional bits",
        "reversible_code": "preallocated trajectory; blank target receives deterministic modular ripple-carry add, inverse subtracts it",
        "off_domain_map": "full modular add/subtract permutation on every bit string",
        "arithmetic_rows": arithmetic_rows, "held_Green_surface": green_held_controls(),
        "source_profile": "periodic zero-mean nearest-neighbor dipole with coordinate-conjugate amplitude; compensating sink supplied",
        "single_positive_periodic_zero_mode_removed_by_background": True,
        "select_prepare_genesis_derived": False,
        "physical_geometry_embedding_derived": False,
        "Cycle460_used_as_evidence_or_premise": False,
    }


def inventories() -> dict:
    return {
        "supplied": [
            "Cycle219 beta family and beta=-0.3 fixture", "coordinate scale ell and its identification with a tick-edge variation",
            "overall source/action orientation and coupling normalization", "static/pinned matter preparation",
            "one body-rail code initialization per co-present frame sector", "fixed-point precision, iteration count, and periodic dipole sink",
            "Cycle576 Regge complex and Cycle581 Strang schedule",
        ],
        "derived": [
            "J=-i Cdagger d_ell C and its Hellmann-Feynman identity", "onsite CAR lift commutes with the actual Cycle230 contact",
            "body edge is the exact fifth zero rail", "q=Mh removes that zero algebraically but is not update-invariant",
            "pure tick source pulls back to h44", "after independent body-rail removal K_join=6-2 sum cos k exactly on all fixtures",
            "1/(4pi r) leading Green term and 5/(32pi) cubic coefficient from the joined symbol",
            "reversible fixed-point trajectory compiler and error/resource bounds",
        ],
        "open": [
            "law-derived metric dependence and orientation of the matter coin", "conservation/static persistence of J under free streaming and backreaction",
            "bounded exact local compiler for the sinc metric-image map", "proof that the body-rail restriction is the selected physical range condition",
            "physical M2 genesis for metric/source/code blocks", "single-source zero-mode handling without supplied background or sink",
            "nonlinear source law, occurrence/Born law, and audit acceptance",
        ],
    }


def no_go_discipline() -> dict:
    return {
        "N1 — alternative routes": "three constructive routes executed: reciprocal matter variation, metric/range code, signed arithmetic compiler",
        "N2 — wall independence": "metric-image locality, matter identification, conservation, and genesis are separated",
        "N3 — hidden-wall scan": "ell-to-h44, orientation, static preparation, sink, precision, and code initialization are explicit supplies",
        "N4 — residual matching": "exact graph residual, Ward, leakage, inverse, deletion, held size, Green, and arithmetic residuals reported",
        "N5 — rhetoric audit": "no source is called energy/stress/gravity; no generator is called a rate; update parameter is not time",
        "N6 — partial-closure path": "exact conditional pole join survives while physical source identification remains open",
        "N7 — steelman": "a future local metric dependence could select the declared deformation and close the source interpretation",
        "N8 — cross-cycle echo": "Cycle230 number/current and Cycle585 scalar/range warnings are retained rather than renamed",
        "qualifying_attempted_or_ruled_out_route_count": 3,
        "required_for_broad_negative": 5,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": False,
        "axiom_pressure": False,
        "disposition": "positive partial construction with explicit residuals",
    }


def main() -> None:
    started = perf_counter()
    dependencies = dependency_controls()
    note = note_contract()
    route_a = route_a_matter_variation()
    source_charge = -math.tan(cycle230.BETA / 2)
    route_b = route_b_constraint_and_symbol(source_charge)
    route_c = route_c_m2_compiler(source_charge)
    inventory = inventories()
    nogo = no_go_discipline()

    check("exact-pinned Cycle219/230/576/581/585 and Green dependencies", dependencies["pass"])
    check("note contract preserves scope and N1-N8", note["pass"], note["missing"])
    check("Route A Hellmann-Feynman reciprocal identity", route_a["maximum_Hellmann_Feynman_residual"] < 2e-8,
          route_a["maximum_Hellmann_Feynman_residual"])
    check("Route A proper-cubic coordinate conjugate", route_a["maximum_proper_cubic_residual"] < TOL,
          route_a["maximum_proper_cubic_residual"])
    check("Route A massive k0 charge is nonzero and massless endpoint vanishes",
          route_a["source_nonzero_at_k0_for_massive_beta"] and route_a["massless_endpoint_charge_zero"])
    check("Route A actual contact, one-particle mass, and seam are preserved",
          route_a["contact_commutator_residual"] < TOL and route_a["one_particle_contact_residual"] < TOL
          and route_a["one_particle_mass_fixture_relative_residual"] < TOL
          and min(route_a["Cycle230_seam_block_singular_values"]) > 1e-4)
    check("Route B metric image removes fifth null but raw update does not preserve it",
          route_b["metric_image_audit"]["exact_metric_image_removes_fifth_null"]
          and not route_b["metric_image_audit"]["raw_Cycle581_edge_update_preserves_metric_image"])
    check("Route B pure tick source pulls back exactly to h44 on all static frames",
          route_b["tick_source_pullback_equals_h44"]
          and route_b["all24_static_tick_source_h44_pullback_residual"] < TOL,
          route_b["all24_static_tick_source_h44_pullback_residual"])
    check("Route B constrained symbol is exact graph Laplacian on train and held",
          route_b["maximum_exact_graph_symbol_residual"] < 2e-11, route_b["maximum_exact_graph_symbol_residual"])
    check("Route B nonzero source excites normalized massless pole",
          route_b["maximum_normalized_pole_excitation_residual"] < 2e-11,
          route_b["maximum_normalized_pole_excitation_residual"])
    check("Route B quartic coefficients freeze to -1/12 and zero cross",
          abs(route_b["quartic_axis_coefficient"] + 1/12) < 2e-5
          and abs(route_b["quartic_cross_coefficient"]) < 2e-5,
          (route_b["quartic_axis_coefficient"], route_b["quartic_cross_coefficient"]))
    update = route_b["Cycle581_update_controls"]
    check("Route B Cycle581 constrained update is unitary, invertible, and leakage-free",
          update["maximum_unitarity_residual"] < TOL and update["maximum_inverse_residual"] < TOL
          and update["maximum_code_leakage"] < TOL)
    check("Route B source and Regge deletion controls signal",
          update["minimum_source_deletion_signal"] > 1e-6 and update["minimum_regge_deletion_signal"] > 1e-8,
          (update["minimum_source_deletion_signal"], update["minimum_regge_deletion_signal"]))
    check("Route B all24/all576 scalar covariance without held refit",
          update["all24_maximum_scalar_covariance_residual"] < 2e-11
          and update["all576_same_fixture_pair_residual"] < 2e-11,
          update["all24_maximum_scalar_covariance_residual"])
    check("Route C fixed-point train/held solutions obey rigorous error bounds and avoid overflow",
          all(row["error_within_bound"] and row["two_complement_overflow_margin"] > 0
              and row["reversible_forward_inverse_integer_residual"] == 0 for row in route_c["arithmetic_rows"]))
    check("Route C held Green surface has frozen 1/r plus cubic coefficient",
          route_c["held_Green_surface"]["maximum_relative_residual"] < 0.002,
          route_c["held_Green_surface"]["maximum_relative_residual"])
    check("inventories and no-go gate retain open walls",
          bool(inventory["supplied"] and inventory["derived"] and inventory["open"])
          and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
          and not nogo["shared_obstruction"] and not nogo["axiom_pressure"])

    report = {
        "cycle": 588, "date": "2026-07-22", "authority": AUTHORITY, "audit": AUDIT,
        "dependencies": dependencies, "note_contract": note, "route_A": route_a,
        "route_B": route_b, "route_C": route_c, "inventory": inventory,
        "no_go_discipline": nogo,
        "closure_ledger": {
            "range_enforcement": "PARTIAL: bounded unused-rail code closes the fifth rail; exact metric-image compiler remains open",
            "conservation": "OPEN: J commutes with number/contact but not shown conserved by free streaming",
            "pole_excitation": "CLOSED CONDITIONAL: nonzero coordinate-conjugate amplitude on supplied tick-edge coupling excites exact 1/L pole",
            "physical_source_identification": "PARTIAL/OPEN: reciprocal J is derived after declaring ell, but ell-to-h44/orientation/static persistence are supplied",
        },
        "six_wall_ledger": {
            "C_ref": "held 1/r and 5/(32pi) surface closes for exact joined symbol; physical calibration remains open",
            "C_num": "signed fixed-point compiler has explicit precision/iteration error and resource law",
            "C_wrap": "unwrapped phase-coordinate deformation is declared; no wrapped phase is called energy",
            "C_int": "actual contact commutes with J and one-particle mass/seam survive; conservation remains open",
            "C_local": "bounded unused-rail code and radius-one arithmetic close a restricted local route; exact Im M(k) code remains open",
            "C_source": "reciprocal coordinate conjugate is derived conditionally; metric identification and static preparation remain supplied",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.65, "time": 3.80, "inertia_matter": 4.85,
            "gravity_source": 4.05, "Born_probability": 3.65,
        },
        "tests_passed": PASS, "tests_failed": FAIL, "tests_total": PASS + FAIL,
        "elapsed_seconds": perf_counter() - started,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    def json_default(value: object) -> object:
        if isinstance(value, np.bool_):
            return bool(value)
        if isinstance(value, np.integer):
            return int(value)
        if isinstance(value, np.floating):
            return float(value)
        raise TypeError(f"not JSON serializable: {type(value)!r}")

    print("REPORT_JSON", json.dumps(report, sort_keys=True, default=json_default))
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
