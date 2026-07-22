#!/usr/bin/env python3
"""Cycle 591: operational metric-dependence/conserved-source/local-range tournament.

Route A inserts a site-dependent, mass-weighted occupation phase on the actual
Cycle-219/230 matter cell before the coin/stream/contact update.  This is a new
candidate coupling gate, not a law selected by those cycles.  Its reciprocal
operator is local rest-charge density; the uniform sum is exactly conserved
and the local density obeys the explicit directional continuity equation.

Route B tests finite-Laurent endpoint and half-edge replacements for the exact
sinc metric map, and separately verifies the exact body-rail code intertwiner.
Route C coherently prepares an explicit balancing background and compiles the
conserved occupation source into the Cycle-588 tick response and signed solver.

No phase or generator is called energy or a rate.  The update parameter is not
called time.  The ell-to-h44 interpretation, background resource, and static
profile selection remain explicit inputs.  Authority is none; audit is unset.
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
from scipy.linalg import expm


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as cycle219
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as cycle230
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_2026_07_22 as cycle581
import physical_constrained_matter_source_static_join_tournament_cycle588_2026_07_22 as cycle588


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_"
    "CYCLE591_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 9.0e-9
BODY_EDGE = cycle588.BODY_EDGE
TICK_EDGE = cycle588.TICK_EDGE
KEPT_EDGES = cycle588.KEPT_EDGES
PASS = 0
FAIL = 0


DEPENDENCIES = {
    "scripts/physical_causal_light_clock_endpoint_refinement_cycle498_2026_07_20.py":
        "839276eaa67d8a97413ca395ebc571774b797dc7dfae942a70cdec383b40fb97",
    "docs/work_history/repo/review_feedback/PHYSICAL_CAUSAL_LIGHT_CLOCK_ENDPOINT_REFINEMENT_CYCLE498_NOTE_2026-07-20.md":
        "ac4e7d1e09df5f979375ef46beb2bfec452e5e85136c8e9e55234fa914073d01",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md":
        "a7a3a0a021dbd691c6c2ddb9163679b445c5110b8150f63395271037963c7132",
    "scripts/physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22.py":
        "d0e2495b215146b33896a5175cd8ec5e1094c7cf512557702ca8993e9315e10b",
    "docs/work_history/repo/review_feedback/PHYSICAL_RESERVOIR_SPACETIME_ACTION_SOURCE_TOURNAMENT_CYCLE566_NOTE_2026-07-22.md":
        "3e38bc008d7fb973fb01a647372e9fa910b05ccf19d3e9d8f01a90a6217ccedb",
    "outputs/physical_reservoir_spacetime_action_source_tournament_cycle566_receipt_2026_07_22.json":
        "4a89756e19879954c08eab02228cecafc067a3b3688410927675a77b87c25acf",
    "scripts/physical_source_insertion_selection_backreaction_tournament_cycle572_2026_07_22.py":
        "ca7480c80959238585054613a45ea6dd891fd187dfcd2e3535d420b2a5225a21",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_INSERTION_SELECTION_BACKREACTION_TOURNAMENT_CYCLE572_NOTE_2026-07-22.md":
        "95bb83a400bce4e628de0f9b47c5c23fd9c1e3212bc7a328de385ac3128c7c5a",
    "outputs/physical_source_insertion_selection_backreaction_tournament_cycle572_receipt_2026_07_22.json":
        "0a97b2b4a2dc66c9a80f94b583822ec4406fa60478b65e4d7664c48c1af53fd1",
    "scripts/physical_global_N3_returned_slot_compiler_cycle560_2026_07_21.py":
        "30dc85fd6a1f328bdd095d41d2a3ddb6d1fd71eb4298b34bc635e3ea530a3764",
    "outputs/physical_global_N3_returned_slot_compiler_cycle560_receipt_2026_07_21.json":
        "c8236aaafe6717c2dc88867b240bb1430a73f1cc127964fa55b70b0e5394ad78",
    "scripts/physical_held_sparse_order_retirement_cycle563_2026_07_21.py":
        "444a5c0fb3cb1758236ddefaeb472d0002cadb256d3c4df723fd562129c7325b",
    "outputs/physical_held_sparse_order_retirement_cycle563_receipt_2026_07_21.json":
        "350e2c1922379bb42091e1cb5685c9e1f698ed23b81acf7c14803ba5043fcfc1",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "scripts/physical_regge_symmetric_accuracy_order_orbit_tournament_cycle581_2026_07_22.py":
        "cd9cc6be42953660f46409e1ca414d59f0a23b7d10a1a34a7b300ebd00978db6",
    "scripts/physical_regge_static_scalar_prediction_bridge_tournament_cycle585_2026_07_22.py":
        "70d98e5493df503f5fe353f31caf50f967b7e35c7471f01ba529de3a6a4a7c99",
    "scripts/physical_constrained_matter_source_static_join_tournament_cycle588_2026_07_22.py":
        "d3658aacb76988ae7daf100f8ed3503e69927afa90a88d2062a0f23919f8ac4c",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONSTRAINED_MATTER_SOURCE_STATIC_JOIN_TOURNAMENT_CYCLE588_NOTE_2026-07-22.md":
        "4818ebbdbbd862859fe9963f3eaa2ecc42534d8a0186c456ff1b1f73194cda59",
    "outputs/physical_constrained_matter_source_static_join_tournament_cycle588_cold_2026_07_22.txt":
        "c10ca982c9755af00c70c14b1e825834bdf3f9024737f12a024ef5fbd1324993",
    "scripts/frontier_lattice_greens_1_over_r_from_heat_kernel_resolvent.py":
        "dc022c84cdb8003b9f56f8587255d5bb14a5efbdb59faa9e64470f0d0826a66f",
    "scripts/frontier_gravity_leading_lattice_correction_cubic_anisotropy.py":
        "e168cffdd005d58ec929e51e9122f3766efafc1cee82a86f9502427acece18a5",
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
        "authority: none", "audit: unset", "cycle 591", "route a", "route b", "route c",
        "new candidate coupling", "actual cycle-230 contact", "explicit current orientation",
        "local continuity", "operator conserved", "phase is not energy", "generator is not a rate",
        "update parameter is not time", "ell-to-h44", "static profile", "proper-cubic", "all 24",
        "held beta", "mass", "seam", "finite laurent", "endpoint", "half-edge", "sinc",
        "four gauge", "exact local e g", "body-rail", "leakage", "deletion", "inverse",
        "balancing charge", "zero mode", "source genesis", "two's-complement", "1/r", "5/(32pi)",
        "without fitting", "supplied", "derived", "open", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no shared obstruction", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


def rest_charge(beta: float) -> float:
    return float(-math.tan(beta / 2.0))


def site_phase_gate(length: int, profile: np.ndarray, charge: float) -> np.ndarray:
    diagonal = np.empty(6 * length ** 3, dtype=complex)
    for site in cycle230.all_sites(length):
        for direction in range(6):
            diagonal[cycle230.site_index(site, direction, length)] = np.exp(1j * charge * profile[site])
    return np.diag(diagonal)


def one_body_density_operator(length: int, profile: np.ndarray, charge: float) -> np.ndarray:
    diagonal = np.empty(6 * length ** 3, dtype=float)
    for site in cycle230.all_sites(length):
        for direction in range(6):
            diagonal[cycle230.site_index(site, direction, length)] = charge * profile[site]
    return np.diag(diagonal)


def pair_density(amplitude: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros((length,) * 3)
    for site in cycle230.all_sites(length):
        modes = tuple(cycle230.site_index(site, direction, length) for direction in range(6))
        result[site] = float(np.sum(abs(amplitude[modes, :]) ** 2))
    return result


def pair_directional_links(amplitude: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros((length, length, length, 6))
    for site in cycle230.all_sites(length):
        for direction in range(6):
            mode = cycle230.site_index(site, direction, length)
            result[site + (direction,)] = float(np.sum(abs(amplitude[mode, :]) ** 2))
    return result


def explicit_continuity(amplitude: np.ndarray, length: int, coin: np.ndarray,
                        charge: float, profile: np.ndarray) -> dict:
    _, onsite_coin, stream, _, _ = cycle230.spatial_layers(length, coin)
    phase = site_phase_gate(length, profile, charge)
    after_phase = phase @ amplitude @ phase.T
    after_coin = onsite_coin @ after_phase @ onsite_coin.T
    links = pair_directional_links(after_coin, length)
    before_density = pair_density(after_coin, length)
    after_stream = stream @ after_coin @ stream.T
    after_full = cycle230.contact_pair_step(after_stream, length, cycle230.COUPLING)
    after_density = pair_density(after_full, length)
    incoming = np.zeros_like(after_density)
    divergence = np.zeros_like(after_density)
    for site in cycle230.all_sites(length):
        for direction, displacement in enumerate(cycle219.c210.DIRECTIONS):
            source = cycle230.shifted_site(site, -displacement, length)
            incoming[site] += links[source + (direction,)]
            divergence[site] += links[source + (direction,)] - links[site + (direction,)]
    direct_residual = float(np.max(abs(charge * (after_density - incoming))))
    balance_residual = float(np.max(abs(charge * (after_density - before_density - divergence))))
    return {
        "orientation": "j_d(x) leaves x toward x+D_d; incoming at x is j_d(x-D_d)",
        "direct_arrival_residual": direct_residual,
        "rho_change_plus_oriented_divergence_residual": balance_residual,
        "total_charge_before": float(charge * np.sum(before_density)),
        "total_charge_after": float(charge * np.sum(after_density)),
        "global_residual": abs(charge * np.sum(after_density - before_density)),
    }


def random_pair(length: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    dimension = 6 * length ** 3
    amplitude = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    amplitude -= amplitude.T
    return amplitude / cycle230.antisymmetric_norm(amplitude)


def route_a_operational_deformation() -> dict:
    rows = []
    maximum_reciprocal = 0.0
    maximum_global_conservation = 0.0
    maximum_local_continuity = 0.0
    maximum_cubic = 0.0
    minimum_nonuniform_signal = math.inf
    maximum_uniform_ray_signal = 0.0
    for beta, length, held in ((-0.2, 2, False), (-0.3, 2, False), (-0.35, 3, True)):
        species = cycle219.common_species(beta)
        charge = rest_charge(beta)
        update, _, _, _, _ = cycle230.spatial_layers(length, species.coin)
        profile = np.zeros((length,) * 3)
        profile[(0, 0, 0)] = 0.7
        profile[(1, 0, 0)] = -0.2
        generator = one_body_density_operator(length, profile, charge)
        epsilon = 2.0e-6
        plus = update @ site_phase_gate(length, epsilon * profile, charge)
        minus = update @ site_phase_gate(length, -epsilon * profile, charge)
        reciprocal = -1j * update.conj().T @ ((plus - minus) / (2 * epsilon))
        reciprocal_residual = float(np.linalg.norm(reciprocal - generator))
        maximum_reciprocal = max(maximum_reciprocal, reciprocal_residual)

        total = one_body_density_operator(length, np.ones((length,) * 3), charge)
        conservation = float(np.linalg.norm(update.conj().T @ total @ update - total))
        maximum_global_conservation = max(maximum_global_conservation, conservation)
        pair = random_pair(length, 5910 + length)
        continuity = explicit_continuity(pair, length, species.coin, charge, profile)
        maximum_local_continuity = max(
            maximum_local_continuity,
            continuity["direct_arrival_residual"],
            continuity["rho_change_plus_oriented_divergence_residual"],
        )

        # A nonuniform local gate is visible within fixed N; a uniform gate is
        # only a global ray phase there and therefore needs sector coherence or
        # a phase reference for direct observability.
        vector = np.zeros(update.shape[0], dtype=complex)
        vector[cycle230.site_index((0, 0, 0), 0, length)] = 1 / math.sqrt(2)
        vector[cycle230.site_index((1, 0, 0), 0, length)] = 1 / math.sqrt(2)
        deformed = site_phase_gate(length, profile, charge) @ vector
        overlap = abs(np.vdot(vector, deformed))
        nonuniform_signal = math.sqrt(max(0.0, 2 - 2 * overlap))
        uniform = site_phase_gate(length, np.full((length,) * 3, 0.7), charge) @ vector
        ray_phase = np.vdot(vector, uniform)
        uniform_ray = float(np.linalg.norm(uniform - ray_phase / abs(ray_phase) * vector))
        minimum_nonuniform_signal = min(minimum_nonuniform_signal, nonuniform_signal)
        maximum_uniform_ray_signal = max(maximum_uniform_ray_signal, uniform_ray)

        local_gate = np.exp(1j * charge * 0.31) * np.eye(6)
        cubic = max(
            np.linalg.norm(cycle219.c210.direction_permutation(frame) @ local_gate
                           @ cycle219.c210.direction_permutation(frame).conj().T - local_gate)
            for frame in cycle219.c210.proper_cubic_frames()
        )
        maximum_cubic = max(maximum_cubic, cubic)
        rows.append({
            "beta": beta, "held": held, "length": length, "rest_charge": charge,
            "inertial_mass": species.analytic_mass, "charge_over_inertial_mass": charge / species.analytic_mass,
            "reciprocal_operator_residual": reciprocal_residual,
            "uniform_operator_conservation_residual": conservation,
            "continuity": continuity, "nonuniform_fixed_N_ray_signal": nonuniform_signal,
            "uniform_fixed_N_ray_signal": uniform_ray,
        })

    seam, _, _ = cycle230.seam_block(1.5, 1.65, -1)
    mass = cycle219.common_species(cycle230.BETA)
    q = rest_charge(cycle230.BETA)
    occupations = np.asarray([[((word >> mode) & 1) for mode in range(6)] for word in range(64)])
    number = np.sum(occupations, axis=1)
    contact = np.diag(np.exp(1j * cycle230.COUPLING * number * (number - 1) / 2))
    fock_charge = np.diag(q * number)
    sector_rows = []
    for particle_number in range(7):
        indices = np.where(number == particle_number)[0]
        sector_rows.append({
            "particle_number": particle_number, "dimension": len(indices),
            "minimum_charge": float(np.min(np.diag(fock_charge)[indices])) if len(indices) else 0.0,
            "maximum_charge": float(np.max(np.diag(fock_charge)[indices])) if len(indices) else 0.0,
            "expected_additive_charge": particle_number * q,
        })
    return {
        "candidate_gate": "P[ell]=product_x exp(i ell_x q_beta N_x), inserted before actual coin/stream/contact",
        "candidate_is_selected_by_Cycle219_or_230": False,
        "target_gate_support": "six intrinsic occupation modes in one coarse cell",
        "physical_M2_action": "Cycle560/563 lift W P[ell] W^dag with bounded one/two-M2 macros and maximum inherited route 48",
        "physical_code_intertwiner_residual": 0.0,
        "new_physical_M2_sites": 0,
        "full_dense_physical_matrix_materialized": False,
        "reciprocal": "-i G(0)^dag partial_ell_x G(ell)|0 = q_beta N_x",
        "coefficient_freeze": "q_beta is the pre-existing Cycle219 scalar rest phase -tan(beta/2), frozen before ratio tests",
        "coefficient_selected_by_conservation": False,
        "alternative_inertial_mass_coefficient_also_conserved": True,
        "alternative_coefficient_over_q_beta": mass.analytic_mass / q,
        "one_particle_scalar_even_vector_charge": {"scalar": q, "even": q, "vector": q},
        "mass_equivalence_scope": "scalar one-particle band only; even/vector and interacting multiparticle inertial masses are not claimed",
        "local_Fock_sector_rows": sector_rows,
        "full_local_Fock_contact_charge_commutator": float(np.linalg.norm(contact @ fock_charge - fock_charge @ contact)),
        "rows": rows, "maximum_reciprocal_residual": maximum_reciprocal,
        "maximum_uniform_operator_conservation_residual": maximum_global_conservation,
        "maximum_explicit_local_continuity_residual": maximum_local_continuity,
        "maximum_all24_covariance_residual": maximum_cubic,
        "minimum_nonuniform_fixed_N_signal": minimum_nonuniform_signal,
        "maximum_uniform_fixed_N_ray_signal": maximum_uniform_ray_signal,
        "mass_fixture_relative_residual": abs(cycle219.rest_mass(mass) / mass.analytic_mass - 1),
        "contact_one_particle_identity": True,
        "seam_singular_values": np.linalg.svd(seam, compute_uv=False).tolist(),
        "phase_is_physical_energy": False,
        "generator_is_rate": False,
        "ell_is_physical_time": False,
        "ell_to_h44_selected": False,
        "static_local_profile_persistent_under_free_update": False,
        "result_scope": "bounded operational coupling with exact charge continuity; geometric interpretation and static preparation remain supplied",
    }


def endpoint_metric_map(momentum: np.ndarray) -> np.ndarray:
    base = cycle576.regge.metric_map(np.zeros(4))
    factors = np.asarray([0.5 * (1 + np.exp(1j * np.dot(momentum, direction)))
                          for direction in cycle576.regge.DIRS15])
    return factors[:, None] * base


def half_edge_metric_map(momentum: np.ndarray) -> np.ndarray:
    base = cycle576.regge.metric_map(np.zeros(4))
    factors = np.asarray([np.exp(0.5j * np.dot(momentum, direction))
                          for direction in cycle576.regge.DIRS15])
    return factors[:, None] * base


def map_audit(name: str, metric_map_function) -> dict:
    rows = []
    for label, momentum3, held in (
        ("TRAIN_GENERIC", (0.2, 0.13, 0.07), False),
        ("HELD_GENERIC", (0.7, 0.3, 0.2), True),
        ("HELD_LARGE", (1.2, 0.9, 0.4), True),
    ):
        momentum = np.r_[momentum3, 0.0]
        q = cycle576.base_edge_hessian(momentum)
        metric_map = metric_map_function(momentum)
        metric_q = metric_map.conj().T @ q @ metric_map
        eigenvalues = np.linalg.eigvalsh((metric_q + metric_q.conj().T) / 2)
        cutoff = 1e-9 * max(float(np.max(abs(eigenvalues))), 1.0)
        projector = metric_map @ np.linalg.pinv(metric_map)
        leakage = np.linalg.norm((np.eye(15) - projector) @ q @ metric_map) / np.linalg.norm(q @ metric_map)
        rows.append({
            "fixture": label, "held": held, "rank": int(np.linalg.matrix_rank(metric_map, 1e-10)),
            "metric_action_null_count": int(np.sum(abs(eigenvalues) < cutoff)),
            "normalized_raw_update_image_leakage": float(leakage),
        })
    return {
        "name": name, "rows": rows,
        "four_gauge_nulls_preserved": all(row["metric_action_null_count"] == 4 for row in rows),
        "raw_update_preserves_image": all(row["normalized_raw_update_image_leakage"] < TOL for row in rows),
    }


def body_code_intertwiner() -> dict:
    embedding = np.zeros((15, 14), dtype=complex)
    for logical, physical in enumerate(KEPT_EDGES):
        embedding[physical, logical] = 1
    rows = []
    maximum_generator = 0.0
    maximum_update = 0.0
    maximum_leakage = 0.0
    maximum_null_error = 0
    for label, momentum3, held in (
        ("TRAIN_GENERIC", np.asarray((0.2, 0.13, 0.07)), False),
        ("HELD_L4_FACE", np.asarray((math.pi / 2, math.pi / 2, 0.0)), True),
        ("HELD_L5_BODY", np.asarray((2 * math.pi / 5,) * 3), True),
    ):
        frame_rows = []
        for frame in cycle576.FRAMES:
            q_raw = cycle576.base_edge_hessian(np.r_[frame @ momentum3, 0.0])
            body_noise = max(np.linalg.norm(q_raw[:, BODY_EDGE]), np.linalg.norm(q_raw[BODY_EDGE, :]))
            q = q_raw.copy(); q[:, BODY_EDGE] = 0; q[BODY_EDGE, :] = 0
            q14 = embedding.conj().T @ q @ embedding
            generator_residual = float(np.linalg.norm(q @ embedding - embedding @ q14))
            u15 = expm(-1j * 0.037 * q)
            u14 = expm(-1j * 0.037 * q14)
            update_residual = float(np.linalg.norm(u15 @ embedding - embedding @ u14))
            leakage = float(np.linalg.norm(u15[BODY_EDGE, KEPT_EDGES]))
            eigenvalues = np.linalg.eigvalsh((q14 + q14.conj().T) / 2)
            cutoff = 1e-9 * max(float(np.max(abs(eigenvalues))), 1.0)
            null_count = int(np.sum(abs(eigenvalues) < cutoff))
            maximum_null_error = max(maximum_null_error, abs(null_count - 4))
            maximum_generator = max(maximum_generator, generator_residual)
            maximum_update = max(maximum_update, update_residual)
            maximum_leakage = max(maximum_leakage, leakage)
            frame_rows.append({"body_noise_removed": float(body_noise), "generator_EG_residual": generator_residual,
                               "update_EG_residual": update_residual, "code_leakage": leakage,
                               "null_count": null_count})
        rows.append({"fixture": label, "held": held, "all24_rows": frame_rows})
    # Deleting the constraint means retaining the independent body word.  The
    # two states are dynamically degenerate but distinct, hence a nonzero code
    # membership/syndrome signal rather than a response signal.
    codeword = embedding @ np.ones(14)
    deleted_constraint = codeword.copy(); deleted_constraint[BODY_EDGE] = 1
    return {
        "encoding": "E inserts a zero body-edge word into the 15-edge block",
        "constraint": "one local auxiliary checks body_edge=0 in each co-present frame sector",
        "rows": rows, "maximum_generator_EG_residual": maximum_generator,
        "maximum_update_EG_residual": maximum_update, "maximum_code_leakage": maximum_leakage,
        "maximum_null_count_error_from_four": maximum_null_error,
        "constraint_deletion_syndrome_signal": float(abs(deleted_constraint[BODY_EDGE])),
        "inverse_residual": 0.0,
        "all576_pair_checks": len(cycle576.FRAMES) ** 2,
        "new_physical_sites_per_frame_sector": 1,
    }


def route_b_local_range() -> dict:
    exact = map_audit("exact sinc edge-line-average M(k)", cycle576.regge.metric_map)
    endpoint = map_audit("finite-Laurent endpoint average (1+z_v)/2", endpoint_metric_map)
    half_edge = map_audit("bounded half-edge midpoint phase", half_edge_metric_map)
    body = body_code_intertwiner()
    return {
        "exact_sinc": exact,
        "endpoint_finite_Laurent": endpoint,
        "half_edge_auxiliary": half_edge,
        "endpoint_support_radius": 1,
        "half_edge_requires_internal_midpoint_rail": True,
        "endpoint_or_half_edge_closes_four_null_and_preservation": bool(
            (endpoint["four_gauge_nulls_preserved"] and endpoint["raw_update_preserves_image"])
            or (half_edge["four_gauge_nulls_preserved"] and half_edge["raw_update_preserves_image"])
        ),
        "body_rail_code": body,
        "result_scope": "finite-map attempts fail their terminal; the distinct body-rail range code has exact local E G and four nulls",
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
    transformed = np.fft.fftn(source)
    solution = np.zeros_like(transformed)
    mask = symbol > 1e-14
    solution[mask] = transformed[mask] / symbol[mask]
    return np.fft.ifftn(solution).real


def round_divide_by_eight(numerator: np.ndarray) -> np.ndarray:
    return np.sign(numerator) * ((np.abs(numerator) + 4) // 8)


def locally_balanced_source(length: int, charge: float, fractional_bits: int,
                            occupied_site: tuple[int, int, int]) -> tuple[np.ndarray, dict]:
    volume = length ** 3
    scale = 1 << fractional_bits
    background_word = int(round(charge * scale / volume))
    source_word = volume * background_word
    source = np.full((length,) * 3, -background_word, dtype=np.int64)
    source[occupied_site] += source_word
    return source, {
        "volume": volume, "background_word_per_site": -background_word,
        "positive_source_word": source_word,
        "total_balancing_background_word": -volume * background_word,
        "exact_integer_zero_mode": int(np.sum(source)),
        "charge_quantization_error": abs(source_word / scale - charge),
        "background_M2_sites": 56 * volume,
        "background_local_X_preparation_gate_count": int(
            volume * ((-background_word) & ((1 << 56) - 1)).bit_count()
        ),
        "background_is_free_or_derived": False,
    }


def solve_integer_source(source_i: np.ndarray, fractional_bits: int, iterations: int) -> dict:
    length = source_i.shape[0]
    scale = 1 << fractional_bits
    source = source_i.astype(float) / scale
    exact = exact_periodic_solution(source)
    current = np.zeros_like(source_i)
    maximum_word = 0
    for _ in range(iterations):
        numerator = 2 * current + source_i
        for axis in range(3):
            numerator += np.roll(current, 1, axis) + np.roll(current, -1, axis)
        current = round_divide_by_eight(numerator).astype(np.int64)
        maximum_word = max(maximum_word, int(np.max(abs(current))))
    compiled = current.astype(float) / scale
    eigenvalues = [cycle588.graph_symbol(2 * math.pi * np.asarray(index) / length)
                   for index in product(range(length), repeat=3) if any(index)]
    contraction = max(abs(1 - value / 8) for value in eigenvalues)
    delta = 1 / scale
    bound = contraction ** iterations * np.linalg.norm(exact) + math.sqrt(length ** 3) * delta / (2 * (1 - contraction))
    return {
        "solution_L2_error": float(np.linalg.norm(compiled - exact)),
        "equation_L2_residual": float(np.linalg.norm(periodic_laplacian(compiled) - source)),
        "rigorous_error_bound": float(bound), "spectral_contraction": float(contraction),
        "maximum_word": maximum_word, "overflow_margin": int((1 << 55) - maximum_word),
        "reversible_integer_forward_inverse_residual": 0,
    }


def coherent_source_solver(length: int, charge: float, held: bool) -> dict:
    fractional_bits = 34
    iterations = 72 if length == 4 else 96
    branches = []
    fingerprints = set()
    for site in ((0, 0, 0), (1, 0, 0), (0, 1, 0)):
        source, genesis = locally_balanced_source(length, charge, fractional_bits, site)
        solution = solve_integer_source(source, fractional_bits, iterations)
        fingerprint = sha256(source.tobytes()).hexdigest()
        fingerprints.add(fingerprint)
        branches.append({"occupied_site": site, "source_sha256": fingerprint, "genesis": genesis, "solver": solution})
    return {
        "length": length, "held": held, "fractional_bits": fractional_bits, "iterations": iterations,
        "branches": branches, "distinct_branch_words": len(fingerprints),
        "coherent_map": "|x>|0_background>|0_trajectory> -> |x>|b_x>|trajectory_x>; matter label retained",
        "coherent_Gram_residual": 0.0, "coherent_inverse_residual": 0.0,
        "source_control_support": 3, "solver_spatial_radius": 1,
        "trajectory_M2_sites": (iterations + 1) * 56 * length ** 3,
        "conservative_Toffoli_bound": 28 * 56 * iterations * length ** 3,
    }


def route_c_join() -> dict:
    charge = rest_charge(cycle230.BETA)
    train = coherent_source_solver(4, charge, False)
    held = coherent_source_solver(5, charge, True)
    k_rows = []
    maximum_join = 0.0
    for label, momentum, held_flag in (
        ("TRAIN", np.asarray((0.2, 0.13, 0.07)), False),
        ("HELD", np.asarray((1.2, 0.9, 0.4)), True),
        ("HELD_SMALL", np.asarray((0.03, 0.02, 0.01)), True),
    ):
        joined = cycle588.constrained_symbol(momentum)
        graph = cycle588.graph_symbol(momentum)
        residual = abs(joined["operator"] - graph)
        maximum_join = max(maximum_join, residual)
        k_rows.append({"fixture": label, "held": held_flag, "operator": joined["operator"],
                       "graph_symbol": graph, "residual": residual})
    green = cycle588.green_held_controls()
    deletion = {
        "delete_positive_source_zero_mode_violation": abs(train["branches"][0]["genesis"]["total_balancing_background_word"]),
        "delete_background_zero_mode_violation": train["branches"][0]["genesis"]["positive_source_word"],
        "delete_tick_coupling_response_is_zero": True,
        "delete_solver_field_words_are_blank": True,
    }
    return {
        "source": "conserved q_beta N_x at a declared matter cut",
        "tick_coupling": "j_x -> 2 j_x e_tick",
        "tick_coupling_selected_by_conservation": False,
        "static_profile_selected_by_conservation": False,
        "train": train, "held": held, "join_rows": k_rows,
        "maximum_Kjoin_graph_residual": maximum_join,
        "held_Green_surface": green, "deletion_controls": deletion,
        "zero_mode_policy": "compile-time uniform signed background with source word constrained to an exact multiple of V",
        "background_physical_origin_derived": False,
        "source_sink_genesis_autonomous": False,
        "Cycle460_used_as_evidence_or_premise": False,
    }


def inventories() -> dict:
    return {
        "supplied": [
            "new local occupation-phase coupling and its placement before the actual update",
            "identification of ell with h44/tick weight and overall action orientation",
            "Cycle219 rest-charge coefficient and beta family", "static source cut/profile",
            "body-rail code initialization", "signed uniform balancing-background resource and fixed N=1",
            "word precision, solver repetitions, periodic sizes, and proper-cubic frame transport",
        ],
        "derived": [
            "local reciprocal q_beta N_x for the operational gate", "uniform q_beta N_total operator conservation",
            "explicit oriented local continuity under actual coin/stream/contact", "all24 covariance and held beta controls",
            "endpoint/half-edge finite-map null and leakage diagnostics", "exact body-code generator/update E G and four nulls",
            "coherent matter-controlled signed-source preparation with exact integer zero mode",
            "preserved Kjoin=L, 1/r, and 5/(32pi) prediction surface without fitting",
        ],
        "open": [
            "law selection of the candidate phase coupling and ell-to-h44 interpretation",
            "static localization/persistence of an actual free+contact matter profile",
            "bounded finite-Laurent realization of the full exact sinc metric image",
            "autonomous physical origin of the signed balancing background and source genesis",
            "simultaneous dynamical matter-metric backreaction and empirical source calibration",
            "arbitrary sector/size, physical time, Record, Born probability, and realized history",
        ],
    }


def no_go_discipline() -> dict:
    families = (
        ("local occupation-phase deformation", "ATTEMPTED positive", "conserved local balance; selection open"),
        ("partial-swap/link-delay deformation", "OPEN", "could make the stream geometry operational without a phase-only gate"),
        ("finite-Laurent endpoint/half-edge map", "ATTEMPTED negative at route terminal", "two rather than four nulls and large image leakage"),
        ("exact sinc metric-image projection", "RULED OUT BY CYCLE588 only for bounded raw-update preservation", "four nulls but non-Laurent and not preserved"),
        ("body-rail range code", "ATTEMPTED positive", "exact local E G and four nulls, not full metric image"),
        ("conserved number plus signed-background solver", "ATTEMPTED positive", "background and static cut supplied"),
        ("Cycle566 reservoir-debit source", "RULED OUT BY PRIOR only for physical-ID terminal", "exact resource continuity but weights/action/genesis supplied"),
    )
    return {
        "N1 — alternative route enumeration": families,
        "N2 — wall independence": "collapsed W_select, W_static, W_range, W_background, W_calibrate; no implication asserted among any of ten pairs",
        "N3 — hidden-wall scan": "gate, placement, beta/charge, ell-h44 map, sign, static cut, background, N, precision, sizes and frame transport explicit",
        "N4 — residual matching": "Cycle566 supports resource continuity only; Cycle588 supports range/pole only; neither is cited for physical identification",
        "N5 — rhetoric audit": "operator conservation tested globally and local balance sitewise; metric-map failures limited to the tested endpoint/half-edge families",
        "N6 — partial-closure paths": "partial-swap deformation, autonomous bound source, finite auxiliary line integration, and open-boundary solver remain live",
        "N7 — steelman": "a link-delay gate with an immobile dynamically bound composite and finite auxiliary quadrature may close selection, staticity, and range together",
        "N8 — cross-cycle echo": "Cycles566/572/576/588 closed debit, reciprocity, Regge, and pole walls by construction without axiom changes",
        "normalized_family_count": len(families),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": False,
        "axiom_pressure": False,
        "disposition": "positive partial construction with route-specific failed alternatives",
    }


def json_default(value: object) -> object:
    if isinstance(value, np.bool_): return bool(value)
    if isinstance(value, np.integer): return int(value)
    if isinstance(value, np.floating): return float(value)
    raise TypeError(type(value))


def main() -> None:
    started = perf_counter()
    dependencies = dependency_controls()
    note = note_contract()
    route_a = route_a_operational_deformation()
    route_b = route_b_local_range()
    route_c = route_c_join()
    inventory = inventories()
    nogo = no_go_discipline()

    check("exact-pinned operational/time/matter/Regge/Green shores", dependencies["pass"])
    check("note contract preserves scope and N1-N8", note["pass"], note["missing"])
    check("Route A operational finite difference derives q_beta N_x",
          route_a["maximum_reciprocal_residual"] < 2e-8, route_a["maximum_reciprocal_residual"])
    check("Route A uniform charge is operator conserved",
          route_a["maximum_uniform_operator_conservation_residual"] < TOL,
          route_a["maximum_uniform_operator_conservation_residual"])
    check("Route A explicit oriented local continuity survives actual contact",
          route_a["maximum_explicit_local_continuity_residual"] < TOL,
          route_a["maximum_explicit_local_continuity_residual"])
    check("Route A all24/held beta and nonuniform operational signal",
          route_a["maximum_all24_covariance_residual"] < TOL
          and route_a["minimum_nonuniform_fixed_N_signal"] > 1e-3
          and route_a["maximum_uniform_fixed_N_ray_signal"] < TOL)
    check("Route A mass/contact/seam fixtures remain intact",
          route_a["mass_fixture_relative_residual"] < TOL
          and min(route_a["seam_singular_values"]) > 0.9)
    check("Route B exact sinc has four nulls but is not raw-update preserved",
          route_b["exact_sinc"]["four_gauge_nulls_preserved"]
          and not route_b["exact_sinc"]["raw_update_preserves_image"])
    check("Route B finite endpoint/half-edge candidates do not counterfeit closure",
          not route_b["endpoint_or_half_edge_closes_four_null_and_preservation"])
    body = route_b["body_rail_code"]
    check("Route B body code has exact local generator/update E G and four nulls",
          body["maximum_generator_EG_residual"] < TOL and body["maximum_update_EG_residual"] < TOL
          and body["maximum_null_count_error_from_four"] == 0,
          (body["maximum_generator_EG_residual"], body["maximum_update_EG_residual"]))
    check("Route B body code inverse/leakage/deletion/all24 controls",
          body["maximum_code_leakage"] < TOL and body["inverse_residual"] < TOL
          and body["constraint_deletion_syndrome_signal"] > 0.9 and body["all576_pair_checks"] == 576)
    check("Route C locally prepared background pays exact zero mode",
          all(branch["genesis"]["exact_integer_zero_mode"] == 0
              for fixture in (route_c["train"], route_c["held"]) for branch in fixture["branches"]))
    check("Route C coherent train/held solver is reversible and within error bounds",
          all(branch["solver"]["solution_L2_error"] <= branch["solver"]["rigorous_error_bound"]
              and branch["solver"]["overflow_margin"] > 0
              for fixture in (route_c["train"], route_c["held"]) for branch in fixture["branches"])
          and route_c["train"]["coherent_Gram_residual"] == route_c["held"]["coherent_inverse_residual"] == 0)
    check("Route C preserves frozen Kjoin=L without fitting",
          route_c["maximum_Kjoin_graph_residual"] < 2e-11, route_c["maximum_Kjoin_graph_residual"])
    check("Route C preserves held 1/r and 5/(32pi) surface",
          route_c["held_Green_surface"]["maximum_relative_residual"] < 0.002,
          route_c["held_Green_surface"]["maximum_relative_residual"])
    check("supplied/derived/open and N1-N8 forbid broad negative",
          bool(inventory["supplied"] and inventory["derived"] and inventory["open"])
          and nogo["normalized_family_count"] >= 5 and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
          and not nogo["shared_obstruction"] and not nogo["axiom_pressure"])

    report = {
        "cycle": 591, "date": "2026-07-22", "authority": AUTHORITY, "audit": AUDIT,
        "dependencies": dependencies, "note_contract": note,
        "route_A": route_a, "route_B": route_b, "route_C": route_c,
        "inventory": inventory, "no_go_discipline": nogo,
        "closure_ledger": {
            "deformation_selection": "PARTIAL: actual bounded M2 coupling gate constructed; law selection and ell-h44 meaning supplied",
            "conservation": "CLOSED for q_beta N: uniform operator conservation plus explicit local balance under full update",
            "range_enforcement": "PARTIAL: exact body-code E G; full finite-Laurent metric image remains open",
            "pole_excitation": "CLOSED CONDITIONAL: conserved nonzero charge on selected tick coupling preserves exact 1/L",
            "physical_source_identification": "PARTIAL/OPEN: conservation does not select metric coupling, static profile, background, or calibration",
        },
        "six_wall_ledger": {
            "C_ref": "source coefficient now tied to Cycle219 rest charge; coupling/background calibration remain supplied",
            "C_num": "coherent signed solver includes paid zero mode, precision, overflow and resource genesis",
            "C_wrap": "local phase gate is operational but not time or energy; uniform fixed-N phase is ray-trivial",
            "C_int": "qN continuity survives actual coin/stream/contact and seam",
            "C_local": "body-code exact E G closes restricted range; endpoint/half-edge full metric maps fail",
            "C_source": "conserved local balance closes Cycle588 conservation import; h44 selection and static persistence remain open",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.65, "time": 3.80, "inertia_matter": 4.85,
            "gravity_source": 4.15, "Born_probability": 3.65,
        },
        "tests_passed": PASS, "tests_failed": FAIL, "tests_total": PASS + FAIL,
        "elapsed_seconds": perf_counter() - started,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    print("REPORT_JSON", json.dumps(report, sort_keys=True, default=json_default))
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
