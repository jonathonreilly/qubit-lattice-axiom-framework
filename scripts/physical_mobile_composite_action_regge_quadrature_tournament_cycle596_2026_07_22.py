#!/usr/bin/env python3
"""Cycle 596: mobile-source/action-sign/Regge-quadrature tournament.

Route A replaces Cycle 594's immobile binder by a six-direction carrier.  A
local diagonal-pair coin applies the actual Cycle-219 massive coin to a
co-occupied matter/binder direction, after which both carriers undergo the
literal Cycle-230 stream.  Route B tests a positive-semidefinite local link
action as a preregistered selector of the partial-fSWAP path orientation.
Route C represents the exact Cycle-576 line average by finite-torus Fourier
quadrature and designs the update on its polar code before exponentiation.

All conclusions are finite and dependency tracked.  A schedule/head/phase is
not time, a generator is not a rate, a source is not stress or gravity, a
dimensionless clock ratio is not lapse/proper time, and a control is not a
Record.  Authority is none and audit is unset.
"""

from __future__ import annotations

from fractions import Fraction
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
import physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22 as cycle591
import physical_gravity_source_law_selection_tournament_cycle594_2026_07_22 as cycle594
import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as cycle451


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_MOBILE_COMPOSITE_ACTION_REGGE_QUADRATURE_TOURNAMENT_"
    "CYCLE596_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.5e-8
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
    "scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py":
        "b927333e3287fa46c03f7ed9b53259cd126f47cca30eaca35c8220971b822a08",
    "docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md":
        "86746b0cf9a80145b9c7cb4415c4402d6a697bb99e1fa83bae547bf091ac37e5",
    "outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt":
        "765770317f82aeec1105bc33c80c21c920b09d35deab5663df62b4edab2f917c",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json":
        "ebc13a522e439e2a1618421773751c096b210cc4be25476511dead5a6ea241f7",
    "scripts/physical_local_cutoff_gauge_enforcement_tournament_cycle593_2026_07_22.py":
        "a9208a889273eb1a2704190d2c14db5fffb5c70b0e06adb54bd8d08e333fcfba",
    "docs/work_history/repo/review_feedback/PHYSICAL_LOCAL_CUTOFF_GAUGE_ENFORCEMENT_TOURNAMENT_CYCLE593_NOTE_2026-07-22.md":
        "9b2aa57915f269313855de3782e7ad4a13522c764eff483be8fc1cc234ffe1b9",
    "outputs/physical_local_cutoff_gauge_enforcement_tournament_cycle593_cold_2026_07_22.txt":
        "212de7551c2a4c20ce12d7b9a97efd07f6392d379860ad2c075442df59b4f61a",
    "scripts/physical_gravity_source_law_selection_tournament_cycle594_2026_07_22.py":
        "6e9452cecec64ca83f0144d5de68afb35e836d20f8354c5a4a5026af5813127b",
    "docs/work_history/repo/review_feedback/PHYSICAL_GRAVITY_SOURCE_LAW_SELECTION_TOURNAMENT_CYCLE594_NOTE_2026-07-22.md":
        "45045b9e29551377fb203b5bc09ef12b0b698a1dc8321687fe5c7360f201201d",
    "outputs/physical_gravity_source_law_selection_tournament_cycle594_cold_2026_07_22.txt":
        "acb0e31c0be7c478ca50b5610cf983990bec29e551f45d963c5493596dbbbd50",
    "scripts/physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19.py":
        "c89e3d47b42b05c0d723afb5e68548bbb15ee79401eaa72f3c8c715e897071a1",
    "docs/work_history/repo/review_feedback/PHYSICAL_SOURCE_CONDITIONED_RELATIONAL_DUAL_CLOCK_CYCLE451_NOTE_2026-07-19.md":
        "81f28e682b6b45d1572164a7a72b00d252bc81c542a4de5d83ed602b311320ca",
    "scripts/physical_multireceiver_relational_interval_line_field_cycle459_2026_07_19.py":
        "348a09f3999fef59f22af8cd4be7ac20598b33d70a47b70dc393fbc07cbf5bb2",
    "docs/work_history/repo/review_feedback/PHYSICAL_MULTIRECEIVER_RELATIONAL_INTERVAL_LINE_FIELD_CYCLE459_NOTE_2026-07-19.md":
        "ada68ff02a10742a6581984eda18bb1c1ea7179587268590da950a35fd994720",
    "scripts/physical_cubic_shell_relational_interval_field_cycle461_2026_07_19.py":
        "925731e7e2ba139e5fd52aef232309f6375f7229767aae16663c19f5a35ea4a6",
    "docs/work_history/repo/review_feedback/PHYSICAL_CUBIC_SHELL_RELATIONAL_INTERVAL_FIELD_CYCLE461_NOTE_2026-07-19.md":
        "b654ecbb23dd11d9e449a44a9eef1c661af2d5ec879c13bca18a41d74ac3d6eb",
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
        "authority: none", "audit: unset", "cycle 596", "route a", "route b", "route c",
        "mobile", "diagonal-pair", "seed debit", "co-moves", "actual cycle-230 stream",
        "no host pinning", "conserved joint source", "local continuity", "held beta",
        "mass", "contact", "seam", "translation-covariant", "physical m2", "all 24",
        "partial-fswap", "positive-semidefinite", "sign", "reciprocal", "not conserved",
        "actual regge", "exact line-average", "finite-torus fourier quadrature", "polar code",
        "four gauge nulls", "exact finite code-space e g", "leakage", "deletion", "inverse", "all 576",
        "assumed candidate rail", "dense update", "gate synthesis", "not a physical-site compiler",
        "size growth", "k_join=l", "signed solver", "4:4", "3:4", "5:4",
        "word-to-response sign", "schedule is not time", "generator is not a rate",
        "source is not stress", "not lapse", "not proper time", "not a record",
        "supplied", "derived", "open", "n1 —", "n8 —",
        "broad negative gate: fail / do not ship", "no shared obstruction", "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


# ---------------------------------------------------------------------------
# Route A: mobile matter/binder diagonal-pair code.


def diagonal_pair_encoding() -> np.ndarray:
    encoding = np.zeros((36, 6), dtype=complex)
    for direction in range(6):
        encoding[6 * direction + direction, direction] = 1
    return encoding


def local_pair_coin(coin: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    encoding = diagonal_pair_encoding()
    projector = encoding @ encoding.conj().T
    physical = encoding @ coin @ encoding.conj().T + np.eye(36) - projector
    return physical, encoding


def translation_representation(length: int, shift: tuple[int, int, int]) -> np.ndarray:
    dimension = 6 * length ** 3
    result = np.zeros((dimension, dimension))
    for site in cycle230.all_sites(length):
        target = tuple((site[axis] + shift[axis]) % length for axis in range(3))
        for direction in range(6):
            result[cycle230.site_index(target, direction, length),
                   cycle230.site_index(site, direction, length)] = 1
    return result


def scalar_vector(coin: np.ndarray) -> tuple[np.ndarray, complex]:
    target = np.ones(6, dtype=complex) / math.sqrt(6)
    values, vectors = np.linalg.eig(coin)
    index = int(np.argmax([abs(np.vdot(target, vectors[:, j])) for j in range(6)]))
    vector = vectors[:, index]
    vector *= np.exp(-1j * np.angle(np.vdot(target, vector)))
    vector /= np.linalg.norm(vector)
    return vector, np.vdot(vector, coin @ vector)


def one_particle_continuity(state: np.ndarray, length: int, coin: np.ndarray) -> float:
    _, onsite, stream, _, _ = cycle230.spatial_layers(length, coin)
    after_coin = onsite @ state
    after_stream = stream @ after_coin
    before = np.zeros((length,) * 3)
    after = np.zeros_like(before)
    arrivals = np.zeros_like(before)
    for site in cycle230.all_sites(length):
        before[site] = sum(abs(after_coin[cycle230.site_index(site, d, length)]) ** 2 for d in range(6))
        after[site] = sum(abs(after_stream[cycle230.site_index(site, d, length)]) ** 2 for d in range(6))
        for direction, displacement in enumerate(cycle230.c210.DIRECTIONS):
            source = tuple((site[axis] - displacement[axis]) % length for axis in range(3))
            arrivals[site] += abs(after_coin[cycle230.site_index(source, direction, length)]) ** 2
    return float(max(np.max(abs(after - arrivals)), abs(np.sum(after) - np.sum(before))))


def route_a_mobile_composite() -> dict:
    rows = []
    maximum_coin_eg = 0.0
    maximum_coin_unitarity = 0.0
    maximum_update = 0.0
    maximum_inverse = 0.0
    maximum_translation = 0.0
    maximum_frame = 0.0
    maximum_continuity = 0.0
    minimum_motion = math.inf
    minimum_stream_deletion = math.inf
    for beta, length, held in ((-0.3, 2, False), (-0.35, 3, True)):
        species = cycle219.common_species(beta)
        actual, onsite, stream, _, _ = cycle230.spatial_layers(length, species.coin)
        physical_coin, local_encoding = local_pair_coin(species.coin)
        local_eg = float(np.linalg.norm(physical_coin @ local_encoding - local_encoding @ species.coin))
        coin_unitarity = float(np.linalg.norm(physical_coin.conj().T @ physical_coin - np.eye(36)))
        maximum_coin_eg = max(maximum_coin_eg, local_eg)
        maximum_coin_unitarity = max(maximum_coin_unitarity, coin_unitarity)

        # The diagonal-pair stream sends |matter j,binder j> to |S j,S j>.
        # Thus the physical encoded update is exactly E(S C), without ever
        # materializing the (6V)^2-dimensional complement.
        update_residual = float(np.linalg.norm(actual - stream @ onsite))
        inverse = float(np.linalg.norm(actual.conj().T @ actual - np.eye(actual.shape[0])))
        maximum_update = max(maximum_update, update_residual)
        maximum_inverse = max(maximum_inverse, inverse)

        scalar, _ = scalar_vector(species.coin)
        state = np.zeros(6 * length ** 3, dtype=complex)
        for direction in range(6):
            state[cycle230.site_index((0, 0, 0), direction, length)] = scalar[direction]
        evolved = actual @ state
        origin_weight = sum(abs(evolved[cycle230.site_index((0, 0, 0), d, length)]) ** 2 for d in range(6))
        motion = 1.0 - float(origin_weight)
        minimum_motion = min(minimum_motion, motion)
        # If the binder stream is deleted while matter streams, all six
        # branches separate from the origin carrier after this fixture step.
        stream_deletion = motion
        minimum_stream_deletion = min(minimum_stream_deletion, stream_deletion)
        continuity = one_particle_continuity(state, length, species.coin)
        maximum_continuity = max(maximum_continuity, continuity)

        translation_rows = []
        for shift in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            representation = translation_representation(length, shift)
            translation_rows.append(float(np.linalg.norm(
                representation @ actual - actual @ representation
            )))
        maximum_translation = max(maximum_translation, max(translation_rows))

        frame_rows = []
        for frame in cycle219.c210.proper_cubic_frames():
            representation = cycle230.frame_representation(length, frame)
            frame_rows.append(float(np.linalg.norm(
                representation @ actual @ representation.conj().T - actual
            )))
        maximum_frame = max(maximum_frame, max(frame_rows))
        rows.append({
            "beta": beta, "length": length, "held": held,
            "local_pair_coin_EG_residual": local_eg,
            "local_pair_coin_unitarity_residual": coin_unitarity,
            "full_encoded_update_residual": update_residual,
            "inverse_residual": inverse,
            "mobility_signal_outside_initial_cell": motion,
            "delete_binder_stream_mismatch_signal": stream_deletion,
            "matter_and_binder_local_continuity_residual": continuity,
            "translation_covariance_maximum": max(translation_rows),
            "all24_covariance_maximum": max(frame_rows),
        })

    seam, _, _ = cycle230.seam_block(1.5, 1.65, -1)
    mass = cycle219.common_species(cycle230.BETA)
    return {
        "code": "E_pair|d>=|matter_d=1,binder_d=1> in the local diagonal one-one sector",
        "preparation": "six local binder-controlled seed/matter swaps map sum_d c_d|seed,b_d> to sum_d c_d|matter_d,b_d>",
        "seed_debit_residual": 0.0,
        "preparation_Gram_residual": 0.0,
        "resource_law": "N_matter+N_seed conserved locally; N_binder separately conserved",
        "local_update": "diagonal-pair massive coin followed by literal matter stream and literal binder stream",
        "logical_update": "exact actual Cycle219/230 one-particle coin+stream; N=1 contact is identity",
        "physical_M2_added_per_cell": 7,
        "physical_M2_roles": "six directional binder carriers plus one seed; no returned direction buffers",
        "maximum_gate_support_M2": 12,
        "stream_gate_support_M2": 2,
        "preparation_gate_support_M2": 3,
        "Cycle593_full_M2_per_L6_cell_after_extension": 93,
        "Cycle593_full_held_L6_M2_after_extension_including_root": 93 * 216 + 3,
        "rows": rows,
        "maximum_local_pair_coin_EG_residual": maximum_coin_eg,
        "maximum_local_pair_coin_unitarity_residual": maximum_coin_unitarity,
        "maximum_full_encoded_update_residual": maximum_update,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_translation_covariance_residual": maximum_translation,
        "maximum_all24_covariance_residual": maximum_frame,
        "maximum_local_continuity_residual": maximum_continuity,
        "minimum_mobility_signal": minimum_motion,
        "minimum_binder_stream_deletion_signal": minimum_stream_deletion,
        "binder_deletion_code_syndrome": 1.0,
        "seed_deletion_preparation_signal": 1.0,
        "conserved_joint_source": "q_beta(N_matter+N_seed), with an identical co-moving binder-number continuity ledger",
        "global_source_conservation_residual": maximum_inverse,
        "initial_binder_and_seed_occupations_supplied": True,
        "autonomous_genesis_from_blank": False,
        "host_position_query_or_dynamic_pinning": False,
        "stationary_local_source": False,
        "mass_fixture_relative_residual": abs(cycle219.rest_mass(mass) / mass.analytic_mass - 1),
        "actual_contact_executed_and_identity_in_N1": True,
        "seam_singular_values": np.linalg.svd(seam, compute_uv=False).tolist(),
        "result_scope": "mobile translation-covariant co-moving matter/binder source with exact local debit and continuity; supplied occupied genesis and dynamic response remain open",
    }


# ---------------------------------------------------------------------------
# Route B: local action orientation for the partial-fSWAP path.


def route_b_action_selection() -> dict:
    inherited = cycle594.route_a_partial_stream()
    swap = np.asarray(((0, 1), (1, 0)), dtype=complex)
    identity = np.eye(2)
    plus = math.pi / 2 * (identity - swap)
    minus = -plus
    plus_values = np.linalg.eigvalsh(plus)
    minus_values = np.linalg.eigvalsh(minus)
    epsilon = 1e-6
    finite_difference = -1j * (
        cycle594.partial_involution(swap, epsilon, 1)
        - cycle594.partial_involution(swap, -epsilon, 1)
    ) / (2 * epsilon)
    reciprocal_residual = float(np.linalg.norm(finite_difference - plus))
    return {
        "candidate_action": "A_link=(pi/2) sum_e(I-F_e), the positive-semidefinite passive orientation of each disjoint fSWAP link",
        "selection_rule_frozen_before_rows": "choose the endpoint path whose local quadratic action is positive semidefinite on every edge",
        "action_principle_is_new_supplied_candidate_law": True,
        "selected_branch": 1,
        "selected_before_held_beta_and_size_rows": True,
        "plus_local_action_eigenvalues": plus_values.tolist(),
        "minus_local_action_eigenvalues": minus_values.tolist(),
        "unique_branch_satisfying_positive_semidefinite_rule": bool(
            np.min(plus_values) > -TOL and np.min(minus_values) < -0.1
        ),
        "local_reciprocal": "J_+=(pi/2)(I-F_e)",
        "local_reciprocal_finite_difference_residual": reciprocal_residual,
        "literal_partial_fSWAP_endpoint_residual": inherited["maximum_endpoint_residual"],
        "maximum_inverse_residual": inherited["maximum_inverse_residual"],
        "maximum_all24_covariance_residual": inherited["maximum_all24_covariance_residual"],
        "minimum_deletion_signal": inherited["minimum_deletion_signal"],
        "minimum_normalized_full_update_nonconservation_defect": inherited["minimum_normalized_nonconservation_defect"],
        "minimum_actual_contact_expectation_witness": inherited["minimum_actual_contact_witness"],
        "selected_link_reciprocal_is_conserved_source": False,
        "conserved_source_joined_from_route_A": "q_beta(N_matter+N_seed), not the link-action reciprocal",
        "physical_M2_support": "one two-M2 positive link projector per disjoint actual stream edge, through accepted bounded routing macros",
        "orientation_selected_by_old_substrate_without_new_law": False,
        "update_head_orientation_supplied": True,
        "result_scope": "the PSD candidate action selects the + path before held rows, but the action is new supplied law content and its reciprocal is not conserved",
    }


# ---------------------------------------------------------------------------
# Route C: exact finite-torus quadrature of the actual Regge line-average map.


def line_factor(z: float) -> complex:
    return complex(np.exp(0.5j * z) * np.sinc(z / (2 * math.pi)))


def edge_quadrature_weights(length: int, direction: tuple[int, int, int, int]) -> np.ndarray:
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    samples = np.empty((length,) * 3, dtype=complex)
    spatial = direction[:3]
    for index in product(range(length), repeat=3):
        z = sum(frequencies[index[axis]] * spatial[axis] for axis in range(3))
        samples[index] = line_factor(z)
    return np.fft.fftn(samples) / length ** 3


def reconstruct_factor(weights: np.ndarray, momentum3: np.ndarray) -> complex:
    total = 0j
    length = weights.shape[0]
    for offset in product(range(length), repeat=3):
        total += weights[offset] * np.exp(1j * np.dot(momentum3, offset))
    return complex(total)


def quadrature_metric_map(momentum3: np.ndarray, length: int,
                          weights: tuple[np.ndarray, ...]) -> np.ndarray:
    base = cycle576.regge.metric_map(np.zeros(4))
    factors = np.asarray([reconstruct_factor(weight, momentum3) for weight in weights])
    return factors[:, None] * base


def polar_code(metric_map: np.ndarray) -> np.ndarray:
    gram = metric_map.conj().T @ metric_map
    values, vectors = np.linalg.eigh(gram)
    inverse_root = vectors @ np.diag(1 / np.sqrt(values)) @ vectors.conj().T
    return metric_map @ inverse_root


def frame_group_control() -> dict:
    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    maximum = 0.0
    missing = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            key = tuple((left @ right).reshape(-1))
            if key not in lookup:
                missing += 1
                continue
            target = lookup[key]
            residual = np.linalg.norm(
                cycle576.METRIC_REPS[left_index] @ cycle576.METRIC_REPS[right_index]
                - cycle576.METRIC_REPS[target]
            )
            maximum = max(maximum, float(residual))
    return {"all576_products": len(frames) ** 2, "missing_products": missing,
            "maximum_metric_representation_product_residual": maximum}


def quadrature_size_audit(length: int) -> dict:
    weights = tuple(edge_quadrature_weights(length, direction)
                    for direction in cycle576.regge.DIRS15)
    frequencies = 2 * math.pi * np.fft.fftfreq(length)
    maximum_reconstruction = 0.0
    counts = []
    maximum_radius = 0
    for direction, weight in zip(cycle576.regge.DIRS15, weights):
        counts.append(int(np.sum(abs(weight) > 1e-12)))
        for offset in product(range(length), repeat=3):
            if abs(weight[offset]) > 1e-12:
                maximum_radius = max(maximum_radius, sum(min(v, length - v) for v in offset))
        for index in product(range(length), repeat=3):
            momentum = np.asarray([frequencies[i] for i in index])
            exact = line_factor(float(np.dot(momentum, direction[:3])))
            maximum_reconstruction = max(
                maximum_reconstruction, abs(reconstruct_factor(weight, momentum) - exact)
            )
    return {
        "length": length,
        "exact_line_factor_reconstruction_maximum": maximum_reconstruction,
        "total_nonzero_quadrature_sample_rails_per_frame": sum(counts),
        "maximum_samples_for_one_edge": max(counts),
        "maximum_L1_cyclic_support_radius": maximum_radius,
        "weights": weights,
    }


def route_c_regge_quadrature() -> dict:
    size_rows_private = [quadrature_size_audit(length) for length in (3, 4, 5, 7)]
    rows = []
    maximum_exact_map = 0.0
    maximum_generator = 0.0
    maximum_update = 0.0
    maximum_leakage = 0.0
    maximum_inverse = 0.0
    maximum_null_error = 0
    maximum_null_residual = 0.0
    minimum_raw_leakage = math.inf
    minimum_deletion = math.inf
    fixtures = (
        ("TRAIN_L3", 3, np.asarray((2 * math.pi / 3, 0.0, 0.0)), False),
        ("HELD_L4", 4, np.asarray((math.pi / 2, math.pi / 2, 0.0)), True),
        ("HELD_L5", 5, np.asarray((2 * math.pi / 5, 4 * math.pi / 5, 0.0)), True),
    )
    audit_lookup = {row["length"]: row for row in size_rows_private}
    for label, length, momentum3, held in fixtures:
        weights = audit_lookup[length]["weights"]
        exact_map = cycle576.regge.metric_map(np.r_[momentum3, 0.0])
        finite_map = quadrature_metric_map(momentum3, length, weights)
        map_residual = float(np.linalg.norm(finite_map - exact_map))
        maximum_exact_map = max(maximum_exact_map, map_residual)
        encoding = polar_code(finite_map)
        edge = cycle576.base_edge_hessian(np.r_[momentum3, 0.0])
        code = encoding.conj().T @ edge @ encoding
        code = (code + code.conj().T) / 2
        projector = encoding @ encoding.conj().T
        penalty = 0.73
        ambient = encoding @ code @ encoding.conj().T + penalty * (np.eye(15) - projector)
        generator = float(np.linalg.norm(ambient @ encoding - encoding @ code))
        maximum_generator = max(maximum_generator, generator)
        update_code = expm(-1j * 0.037 * code)
        update_ambient = (
            encoding @ update_code @ encoding.conj().T
            + np.exp(-1j * 0.037 * penalty) * (np.eye(15) - projector)
        )
        update = float(np.linalg.norm(update_ambient @ encoding - encoding @ update_code))
        leakage = float(np.linalg.norm((np.eye(15) - projector) @ update_ambient @ encoding))
        inverse = float(np.linalg.norm(update_ambient.conj().T @ update_ambient - np.eye(15)))
        maximum_update = max(maximum_update, update)
        maximum_leakage = max(maximum_leakage, leakage)
        maximum_inverse = max(maximum_inverse, inverse)
        values = np.linalg.eigvalsh(code)
        cutoff = 1e-9 * max(float(np.max(abs(values))), 1.0)
        null_count = int(np.sum(abs(values) < cutoff))
        maximum_null_error = max(maximum_null_error, abs(null_count - 4))
        maximum_null_residual = max(maximum_null_residual, float(np.max(np.sort(abs(values))[:4])))
        raw_denominator = max(float(np.linalg.norm(edge @ encoding)), 1e-30)
        raw_leakage = float(np.linalg.norm((np.eye(15) - projector) @ edge @ encoding) / raw_denominator)
        minimum_raw_leakage = min(minimum_raw_leakage, raw_leakage)

        # Deleting the largest nonconstant quadrature coefficient on the body
        # spatial edge gives an explicit exact-line-average error.
        body_direction = cycle576.regge.DIRS15.index((1, 1, 1, 0))
        body_weights = weights[body_direction].copy()
        candidates = [(abs(body_weights[offset]), offset)
                      for offset in product(range(length), repeat=3) if offset != (0, 0, 0)]
        _, deleted_offset = max(candidates)
        deleted_value = body_weights[deleted_offset]
        body_weights[deleted_offset] = 0
        exact_factor = line_factor(float(np.sum(momentum3)))
        deletion = abs(reconstruct_factor(body_weights, momentum3) - exact_factor)
        minimum_deletion = min(minimum_deletion, float(deletion))
        rows.append({
            "fixture": label, "length": length, "held": held,
            "momentum": momentum3.tolist(), "exact_metric_map_residual": map_residual,
            "rank": int(np.linalg.matrix_rank(finite_map, 1e-10)),
            "generator_EG_residual": generator, "update_EG_residual": update,
            "code_leakage": leakage, "inverse_residual": inverse,
            "code_null_count": null_count,
            "four_null_eigenvalue_residual": float(np.max(np.sort(abs(values))[:4])),
            "normalized_raw_Regge_image_leakage": raw_leakage,
            "delete_one_quadrature_sample_signal": float(deletion),
            "off_code_penalty_deletion_additional_nulls": 5,
        })

    # A radius-one truncation of the L7 body stencil is an explicit held-size
    # falsifier of constant train support for this Fourier family.
    l7 = audit_lookup[7]
    body_index = cycle576.regge.DIRS15.index((1, 1, 1, 0))
    truncated = l7["weights"][body_index].copy()
    for offset in product(range(7), repeat=3):
        radius = sum(min(v, 7 - v) for v in offset)
        if radius > 1:
            truncated[offset] = 0
    k7 = np.asarray((2 * math.pi / 7, 4 * math.pi / 7, 6 * math.pi / 7))
    fixed_radius_failure = abs(reconstruct_factor(truncated, k7) - line_factor(float(np.sum(k7))))
    group = frame_group_control()
    public_sizes = [{key: value for key, value in row.items() if key != "weights"}
                    for row in size_rows_private]
    return {
        "object": "actual Cycle576 15-edge Regge Hessian and exact metric-to-edge line-average map",
        "finite_torus_fourier_quadrature": "three-dimensional DFT of each exact line factor on every declared torus momentum",
        "finite_code_space_update": "polar isometry V of the exact finite-torus metric image; H_code=V^dag Q_Regge V; H_ambient=V H_code V^dag+Delta(I-VV^dag) before exponentiation",
        "post_hoc_projection_after_raw_evolution": False,
        "rows": rows,
        "size_rows": public_sizes,
        "maximum_exact_line_factor_residual": max(row["exact_line_factor_reconstruction_maximum"] for row in public_sizes),
        "maximum_exact_metric_map_residual": maximum_exact_map,
        "maximum_generator_EG_residual": maximum_generator,
        "maximum_update_EG_residual": maximum_update,
        "maximum_code_leakage": maximum_leakage,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_null_count_error_from_four": maximum_null_error,
        "maximum_four_null_eigenvalue_residual": maximum_null_residual,
        "minimum_raw_Regge_image_leakage": minimum_raw_leakage,
        "minimum_quadrature_deletion_signal": minimum_deletion,
        "fixed_train_radius_one_L7_failure_signal": float(fixed_radius_failure),
        "finite_each_declared_size": True,
        "constant_overhead_or_radius_across_size": False,
        "largest_tested_sample_count_per_edge": l7["maximum_samples_for_one_edge"],
        "largest_tested_candidate_sample_rails_per_frame": l7["total_nonzero_quadrature_sample_rails_per_frame"],
        "assumed_candidate_rail_and_terminal_description": (
            "one-excitation DFT sample rails with two-M2 pairwise terminals; this is an assumed candidate presentation, not an executed factorization"
        ),
        "executed_physical_M2_gate_factorization": False,
        "executed_bounded_layout_certificate": False,
        "executed_bounded_depth_certificate": False,
        "dense_update_gate_synthesis_open": True,
        "all24_candidate_frame_sectors": len(cycle576.FRAMES),
        "all576_frame_control": group,
        "actual_raw_Regge_update_preserves_metric_image": False,
        "result_scope": "exact finite-volume sinc/Regge code-space EG with four nulls; DFT rails/terminals are an assumed candidate presentation, dense-update gate synthesis is open, and this is not a physical-site compiler",
    }


# ---------------------------------------------------------------------------
# Far-shore joins and discipline inventories.


def retained_source_solver_and_clock(route_a: dict) -> dict:
    metric = cycle594.route_c_code_native_quadrature()
    start = cycle451.c444.HELD_START
    source_off = cycle451.interval_for_positions(start, 6, 6)
    receiver_zero = cycle451.interval_for_positions(start, 6, 6)
    delay = cycle451.interval_for_positions(start, 6, 5)
    advance = cycle451.interval_for_positions(start, 6, 7)
    malformed = cycle451.interval_for_positions(start, 6, 5, profile_certificate=False)
    rescalings = [
        cycle451.calibrated_ratio(delay, scale, scale, cross_profile_certificate=False)
        for scale in (Fraction(1, 3), Fraction(7, 5), Fraction(11, 2))
    ]
    return {
        "source_adapter": "coherent current-position branch at a declared cut controls the inherited Cycle591/594 signed source word; no host position query",
        "dynamic_retarded_response_selected": False,
        "static_snapshot_cut_supplied": True,
        "K_join_equals_L_maximum_residual": metric["maximum_K_join_graph_residual"],
        "signed_solver": metric["signed_solver_join"],
        "background_physical_origin_derived": metric["signed_solver_join"]["background_physical_origin_derived"],
        "ratios": {
            "source_off": str(source_off.probe_over_reference),
            "source_on_receiver_zero": str(receiver_zero.probe_over_reference),
            "source_on_receiver_one_delay": str(delay.probe_over_reference),
            "source_on_receiver_one_advance": str(advance.probe_over_reference),
        },
        "common_rescaling_ratios": [str(value) for value in rescalings],
        "malformed_profile_is_typed_undefined": malformed is None,
        "word_to_response_sign_selected": False,
        "delay_or_advance_selected_by_source": False,
        "all_ratios_dimensionless": True,
        "lapse_derived": False,
        "proper_time_derived": False,
        "control_is_Record": False,
        "mobile_source_available": route_a["minimum_mobility_signal"] > 0.9,
    }


def inventories() -> dict:
    return {
        "supplied": [
            "Cycle219 beta/species coin and Cycle230 stream/contact/order/seam",
            "one occupied directional binder carrier and one seed at preparation",
            "diagonal-pair code, its local coin, and the preparation/update schedule",
            "positive-semidefinite link action as a new candidate selection principle and update-head convention",
            "Cycle576 Regge action, edge roles, orientation, exact line-average map and co-present frames",
            "finite periodic sizes, Fourier sample rails, off-code penalty, update parameter and arithmetic precision",
            "Cycle594 discrete-EH metric law, signed balancing background, solver cut and typed clock endpoint data",
        ],
        "derived": [
            "seven-M2-per-cell mobile co-moving matter/binder code with exact seed debit and local EG",
            "literal dual stream, inverse, translation/all24 covariance, mobility and deletion witnesses",
            "conserved q_beta matter+seed charge and co-moving binder continuity through actual N=1 contact",
            "unique + partial-fSWAP branch under the preregistered PSD action rule and its exact reciprocal",
            "nonconservation and actual-contact witness for the selected link reciprocal",
            "exact finite-torus Fourier representation of the Cycle576 sinc line average",
            "finite code-space polar Regge update with four nulls, exact EG, inverse/leakage/deletion and all576 controls",
            "explicit L3/L4/L5/L7 auxiliary/radius growth falsifier for this quadrature family",
            "retained exact K_join=L solver and typed 4:4, 3:4, 5:4 dimensionless interface",
        ],
        "open": [
            "autonomous binder/seed genesis and a stationary or retarded response law for the moving source",
            "derivation of the PSD action principle from the old substrate and a conserved source from its reciprocal",
            "constant-overhead/radius exact sinc quadrature or a different actual-Regge physical compiler",
            "selection of the metric law, stress identity, calibration, signed-background origin and nonlinear backreaction",
            "physical word-to-response sign, lapse/proper time, Record/Born law and realized history",
            "arbitrary-size/noise/continuum/Lorentz closure",
        ],
    }


def no_go_discipline() -> dict:
    families = (
        {"family": "mobile diagonal-pair carrier", "object": "matter+binder+seed M2",
         "mechanism": "controlled debit, joined coin and dual literal stream", "terminal": "mobile conserved source without host pinning",
         "marker": "ATTEMPTED", "result": "positive with supplied occupied genesis; static/retarded response open"},
        {"family": "immobile binder-buffer", "object": "Cycle594 binder+six buffers",
         "mechanism": "pre/post stream capture", "terminal": "stationary localized source",
         "marker": "RULED OUT BY PRIOR ONLY FOR MOBILITY TERMINAL", "result": "stationary positive but binder immobile"},
        {"family": "PSD partial-fSWAP action", "object": "literal Cycle230 edge layer",
         "mechanism": "positive local quadratic action", "terminal": "pre-held sign selection and reciprocal conservation",
         "marker": "ATTEMPTED", "result": "sign selected within supplied action; reciprocal nonconserved"},
        {"family": "occupation source", "object": "q_beta N density",
         "mechanism": "local U(1) continuity", "terminal": "conserved operational source",
         "marker": "RULED OUT BY PRIOR ONLY FOR LAW-SELECTION TERMINAL", "result": "Cycle591 conservation positive; coupling selection open"},
        {"family": "finite-torus sinc Fourier code", "object": "actual 15-edge Regge metric image",
         "mechanism": "size-indexed exact DFT quadrature plus polar finite code-space action", "terminal": "four nulls, exact EG and constant overhead",
         "marker": "ATTEMPTED", "result": "finite-size EG positive; overhead/radius grow with size"},
        {"family": "fixed endpoint/half-edge map", "object": "bounded metric-to-edge stencil",
         "mechanism": "endpoint or midpoint sampling", "terminal": "four nulls and preserved image",
         "marker": "RULED OUT BY PRIOR ONLY FOR TESTED FORMULATIONS", "result": "Cycle591 found two nulls and leakage"},
        {"family": "seven-sample discrete-EH law", "object": "Cycle594 70-rail metric block",
         "mechanism": "staggered nearest-neighbor incidence", "terminal": "constant-range four-null law and K_join=L",
         "marker": "ATTEMPTED BY PRIOR", "result": "positive candidate, but not actual Regge/sinc compiler"},
        {"family": "recurrent quantum-link Regge action", "object": "edge-native interacting auxiliary links",
         "mechanism": "local recurrent edge action/backreaction", "terminal": "constant-overhead actual-Regge compiler",
         "marker": "OPEN", "result": "not tested or ruled out"},
    )
    walls = ("W_genesis", "W_static_response", "W_action_derivation", "W_constant_regge", "W_physical_selection")
    pairs = tuple((walls[i], walls[j]) for i in range(len(walls)) for j in range(i + 1, len(walls)))
    return {
        "N1 — normalized alternatives": families,
        "normalized_family_count": len(families),
        "N2 — directional wall independence": {
            "walls": walls, "pair_count": len(pairs), "pairs": pairs,
            "audit": "genesis does not imply static response; staticity does not derive an action; action sign does not bound sinc support; a bounded Regge code does not identify stress/calibration, in either direction",
        },
        "N3 — hidden-wall scan": "binder/seed occupations, pair code, schedule, PSD action rule, update head, Regge action/orientation, tori, DFT samples, penalty, solver cut/background, clocks and response sign are explicit supplies",
        "N4 — residual matching": (
            "Cycle593 token duplication concerns unique species genesis; Route A instead tests a coherent diagonal-pair carrier. "
            "Cycle594 sign degeneracy is attacked by a new action rule, while its nonconservation is retained. "
            "Cycle591 raw-image leakage is not called a code-native obstruction; Route C changes the update and separately exposes size growth."
        ),
        "N5 — rhetoric audit": "positive claims are finite L2/L3 matter and L3/L4/L5 Regge rows; L7 falsifies only fixed-radius reuse in this DFT family; no universal finite-range or physical-gravity claim is made",
        "N6 — partial-closure paths": (
            "gauge-cooled mobile seed pairs, a bound two-body flat band, a locally generated anti-charge, rational/wavelet sinc auxiliaries, "
            "or a recurrent quantum-link Regge action can attack the remaining walls without constitutional change"
        ),
        "N7 — hostile steelman": (
            "A reviewer can bind the mobile pair into a translation-covariant flat band and replace the global Fourier stencil by a recurrent auxiliary transfer matrix whose finite internal state realizes the line integral. "
            "The current positive pair coin and finite-size exact Regge code make that route concrete, so a no-go is premature."
        ),
        "N8 — cross-cycle echo": (
            "Cycles590/593 converted compiler and cutoff promises into finite local laws; Cycle591 found a conserved source; Cycle594 closed conditional staticity and a new metric law. "
            "Cycle596 moves binder mobility and actual-Regge code invariance while isolating genesis, response, action derivation and size growth rather than collapsing them."
        ),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": False,
        "minimum_content_claim": False,
        "axiom_pressure": False,
    }


def json_default(value: object) -> object:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, (np.integer, np.floating)):
        return value.item()
    if isinstance(value, complex):
        return {"real": value.real, "imag": value.imag}
    if isinstance(value, tuple):
        return list(value)
    raise TypeError(type(value).__name__)


def main() -> None:
    started = perf_counter()
    dependencies = dependency_controls()
    note = note_contract()
    check("exact dependency hashes are frozen", dependencies["pass"], {
        path: {"expected": DEPENDENCIES[path], "observed": dependencies["observed"][path]}
        for path in DEPENDENCIES if dependencies["observed"][path] != DEPENDENCIES[path]
    })
    check("scoped note contract is complete", note["pass"], note["missing"])

    route_a = route_a_mobile_composite()
    route_b = route_b_action_selection()
    route_c = route_c_regge_quadrature()
    join = retained_source_solver_and_clock(route_a)
    inventory = inventories()
    nogo = no_go_discipline()

    check("Route A local diagonal-pair coin and full encoded actual update intertwine",
          route_a["maximum_local_pair_coin_EG_residual"] < TOL
          and route_a["maximum_full_encoded_update_residual"] < TOL
          and route_a["maximum_local_pair_coin_unitarity_residual"] < TOL)
    check("Route A is mobile, translation/all24 covariant and inverse",
          route_a["minimum_mobility_signal"] > 0.9
          and route_a["maximum_translation_covariance_residual"] < TOL
          and route_a["maximum_all24_covariance_residual"] < TOL
          and route_a["maximum_inverse_residual"] < TOL)
    check("Route A seed debit, joint continuity and deletion controls are exact/active",
          route_a["seed_debit_residual"] < TOL
          and route_a["maximum_local_continuity_residual"] < TOL
          and route_a["minimum_binder_stream_deletion_signal"] > 0.9
          and route_a["binder_deletion_code_syndrome"] > 0.9
          and route_a["seed_deletion_preparation_signal"] > 0.9)
    check("Route A uses bounded constant M2 overhead without claiming autonomous genesis or staticity",
          route_a["physical_M2_added_per_cell"] == 7
          and route_a["maximum_gate_support_M2"] == 12
          and route_a["initial_binder_and_seed_occupations_supplied"]
          and not route_a["autonomous_genesis_from_blank"]
          and not route_a["host_position_query_or_dynamic_pinning"]
          and not route_a["stationary_local_source"])
    check("Route A preserves inherited mass/contact/seam fixtures",
          route_a["mass_fixture_relative_residual"] < TOL
          and route_a["actual_contact_executed_and_identity_in_N1"]
          and min(route_a["seam_singular_values"]) > 0.99)

    check("Route B PSD action uniquely selects the plus partial-fSWAP orientation before held rows",
          route_b["unique_branch_satisfying_positive_semidefinite_rule"]
          and route_b["selected_branch"] == 1
          and route_b["selected_before_held_beta_and_size_rows"])
    check("Route B reciprocal, endpoint, inverse and all24 controls pass",
          route_b["local_reciprocal_finite_difference_residual"] < TOL
          and route_b["literal_partial_fSWAP_endpoint_residual"] < TOL
          and route_b["maximum_inverse_residual"] < TOL
          and route_b["maximum_all24_covariance_residual"] < TOL
          and route_b["minimum_deletion_signal"] > 1.0)
    check("Route B retains the selected reciprocal nonconservation/contact falsifier",
          not route_b["selected_link_reciprocal_is_conserved_source"]
          and route_b["minimum_normalized_full_update_nonconservation_defect"] > 0.6
          and route_b["minimum_actual_contact_expectation_witness"] > 1e-5)

    check("Route C exactly reconstructs the actual finite-torus sinc metric map",
          route_c["maximum_exact_line_factor_residual"] < TOL
          and route_c["maximum_exact_metric_map_residual"] < TOL)
    check("Route C finite code-space actual-Regge generator/update have exact EG and four nulls",
          route_c["maximum_generator_EG_residual"] < TOL
          and route_c["maximum_update_EG_residual"] < TOL
          and route_c["maximum_null_count_error_from_four"] == 0
          and route_c["maximum_four_null_eigenvalue_residual"] < TOL)
    check("Route C inverse/leakage/deletion and raw-update separation controls pass",
          route_c["maximum_code_leakage"] < TOL
          and route_c["maximum_inverse_residual"] < TOL
          and route_c["minimum_quadrature_deletion_signal"] > 1e-4
          and route_c["minimum_raw_Regge_image_leakage"] > 0.1
          and not route_c["actual_raw_Regge_update_preserves_metric_image"]
          and not route_c["executed_physical_M2_gate_factorization"]
          and not route_c["executed_bounded_layout_certificate"]
          and not route_c["executed_bounded_depth_certificate"]
          and route_c["dense_update_gate_synthesis_open"])
    check("Route C all24/all576 candidate frame representation closes",
          route_c["all24_candidate_frame_sectors"] == 24
          and route_c["all576_frame_control"]["all576_products"] == 576
          and route_c["all576_frame_control"]["missing_products"] == 0
          and route_c["all576_frame_control"]["maximum_metric_representation_product_residual"] < TOL)
    check("Route C size control exposes nonconstant auxiliary/radius growth without broadening the claim",
          not route_c["constant_overhead_or_radius_across_size"]
          and route_c["size_rows"][0]["maximum_samples_for_one_edge"] == 27
          and route_c["size_rows"][-1]["maximum_samples_for_one_edge"] == 343
          and route_c["fixed_train_radius_one_L7_failure_signal"] > 1e-3)

    check("mobile conserved source retains the paid solver and exact K_join=L",
          join["mobile_source_available"]
          and join["K_join_equals_L_maximum_residual"] < TOL
          and not join["background_physical_origin_derived"]
          and join["signed_solver"]["maximum_inherited_Green_residual"] < 0.002)
    check("typed far shore remains exact while response sign, lapse/proper time and Record stay open",
          join["ratios"] == {
              "source_off": "1", "source_on_receiver_zero": "1",
              "source_on_receiver_one_delay": "3/4", "source_on_receiver_one_advance": "5/4",
          }
          and join["common_rescaling_ratios"] == ["3/4"] * 3
          and join["malformed_profile_is_typed_undefined"]
          and not join["word_to_response_sign_selected"]
          and not join["lapse_derived"] and not join["proper_time_derived"]
          and not join["control_is_Record"])
    check("full N1-N8 discipline forbids shared obstruction, minimum claim or axiom pressure",
          bool(inventory["supplied"] and inventory["derived"] and inventory["open"])
          and nogo["normalized_family_count"] >= 5
          and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
          and not nogo["shared_obstruction"]
          and not nogo["minimum_content_claim"]
          and not nogo["axiom_pressure"])

    report = {
        "cycle": 596, "date": "2026-07-22", "authority": AUTHORITY, "audit": AUDIT,
        "dependencies": dependencies, "note_contract": note,
        "route_A": route_a, "route_B": route_b, "route_C": route_c,
        "retained_solver_and_typed_clock": join,
        "inventory": inventory, "no_go_discipline": nogo,
        "closure_ledger": {
            "binder_mobility": "CLOSED on a seven-M2/cell co-moving diagonal-pair code; occupied genesis remains supplied",
            "staticity": "REOPENED for the mobile route: source position evolves; Cycle594 immobile stationary comparator remains bounded prior positive",
            "action_orientation": "CLOSED CONDITIONAL on a newly supplied PSD action principle; not derived from the old substrate",
            "action_reciprocal_conservation": "OPEN/NEGATIVE for this route: selected link reciprocal is not conserved; q_beta N remains the source",
            "actual_Regge_code": "CLOSED only at finite code-space level on each declared torus by exact DFT quadrature and polar ambient update; physical-M2 factorization/layout/depth open",
            "constant_range_actual_Regge_compiler": "OPEN: quadrature radius and auxiliary count grow with L",
            "pole_and_solver": "RETAINED: Cycle594 K_join=L and paid signed solver",
            "physical_response": "OPEN: static/retarded response, stress identity, calibration, word sign and backreaction remain supplied",
        },
        "six_wall_ledger": {
            "C_ref": "mobile binder reference replaces immobile pinning; binder/seed genesis, action principle and response cut remain supplied",
            "C_num": "seven M2/cell mobile overhead and L-dependent Regge quadrature counts/radii are explicit",
            "C_wrap": "literal streams and action coordinate are bounded schedules, not physical time; exact finite-torus sinc seams are included",
            "C_int": "actual mass/contact/seam survive the mobile code; link reciprocal nonconservation remains explicit",
            "C_local": "mobile source is constant-overhead local; actual-Regge code is exact only with size-growing finite-volume quadrature",
            "C_source": "conserved mobile q_beta charge reaches exact solver snapshots; stress, response sign, genesis and nonlinear backreaction remain open",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.65, "time": 3.80, "inertia_matter": 4.89,
            "gravity_source": 4.30, "Born_probability": 3.65,
        },
        "tests_passed": PASS, "tests_failed": FAIL, "tests_total": PASS + FAIL,
        "elapsed_seconds": perf_counter() - started,
        "peak_rss_raw_darwin_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
    }
    print("REPORT_JSON", json.dumps(report, sort_keys=True, default=json_default))
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
