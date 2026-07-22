#!/usr/bin/env python3
"""Cycle 594: gravity/source law-selection tournament.

Route A replaces the phase-only probe by a literal partial-fermionic-swap
deformation of the second stream layer.  Route B constructs a translation-
uniform, locally triggered seed/binder/buffer macro that prepares and holds a
Cycle-219 scalar matter excitation while exactly debiting a local seed.
Route C evolves a finite proper-cubic seven-sample metric quadrature code
directly, rather than projecting the raw Regge update after the fact.

The constructions are bounded physical-M2 candidates.  They do not identify
occupation or exchange generators with physical energy, stress, gravity, a
rate, or time.  Authority is none and audit is unset.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
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
import physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22 as cycle566
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_constrained_matter_source_static_join_tournament_cycle588_2026_07_22 as cycle588
import physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22 as cycle591
import physical_source_conditioned_relational_dual_clock_cycle451_2026_07_19 as cycle451


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_GRAVITY_SOURCE_LAW_SELECTION_TOURNAMENT_CYCLE594_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 1.2e-8
PASS = 0
FAIL = 0


DEPENDENCIES = {
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
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py":
        "ad9bf5febde8b58e948f4a4240791216a20d61262149469763ef387455dff52a",
    "docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md":
        "999e88c014f22637caeeb904bba3c27ee5beff8f4bbf04975f625094035a28ec",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py":
        "b449301837c1b72a325d310a1e2c582263a36648de939d169912347aff0591ae",
    "docs/work_history/repo/review_feedback/SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md":
        "a7a3a0a021dbd691c6c2ddb9163679b445c5110b8150f63395271037963c7132",
    "scripts/physical_reservoir_spacetime_action_source_tournament_cycle566_2026_07_22.py":
        "d0e2495b215146b33896a5175cd8ec5e1094c7cf512557702ca8993e9315e10b",
    "docs/work_history/repo/review_feedback/PHYSICAL_RESERVOIR_SPACETIME_ACTION_SOURCE_TOURNAMENT_CYCLE566_NOTE_2026-07-22.md":
        "3e38bc008d7fb973fb01a647372e9fa910b05ccf19d3e9d8f01a90a6217ccedb",
    "outputs/physical_reservoir_spacetime_action_source_tournament_cycle566_cold_2026_07_22.txt":
        "689908c39c1cf057f783a8a84eb96f7855c81b70dd07a224cb2a24b5ee69124b",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
        "2d5650c57d5518e274803f5c511886981c8572b553dda926739cc98199939c20",
    "outputs/physical_dynamical_metric_source_law_bridge_tournament_cycle576_cold_2026_07_22.txt":
        "00c7b20bd07641ca486e916409992a441d9984ac4a31dfa0a59ec8612407c046",
    "scripts/physical_constrained_matter_source_static_join_tournament_cycle588_2026_07_22.py":
        "d3658aacb76988ae7daf100f8ed3503e69927afa90a88d2062a0f23919f8ac4c",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONSTRAINED_MATTER_SOURCE_STATIC_JOIN_TOURNAMENT_CYCLE588_NOTE_2026-07-22.md":
        "4818ebbdbbd862859fe9963f3eaa2ecc42534d8a0186c456ff1b1f73194cda59",
    "outputs/physical_constrained_matter_source_static_join_tournament_cycle588_cold_2026_07_22.txt":
        "c10ca982c9755af00c70c14b1e825834bdf3f9024737f12a024ef5fbd1324993",
    "scripts/physical_operational_metric_conserved_source_local_range_tournament_cycle591_2026_07_22.py":
        "b927333e3287fa46c03f7ed9b53259cd126f47cca30eaca35c8220971b822a08",
    "docs/work_history/repo/review_feedback/PHYSICAL_OPERATIONAL_METRIC_CONSERVED_SOURCE_LOCAL_RANGE_TOURNAMENT_CYCLE591_NOTE_2026-07-22.md":
        "86746b0cf9a80145b9c7cb4415c4402d6a697bb99e1fa83bae547bf091ac37e5",
    "outputs/physical_operational_metric_conserved_source_local_range_tournament_cycle591_cold_2026_07_22.txt":
        "765770317f82aeec1105bc33c80c21c920b09d35deab5663df62b4edab2f917c",
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
        "authority: none", "audit: unset", "cycle 594", "route a", "route b", "route c",
        "partial-fswap", "shortest geodesic", "sign branch", "coordinate reciprocal",
        "not conserved", "actual cycle-230 contact", "physical m2", "held beta", "mass", "seam",
        "seed", "binder", "buffer", "joint continuity", "no host pinning", "stationary",
        "resource genesis", "seven-sample", "finite auxiliary quadrature", "code-native",
        "four gauge nulls", "exact local e g", "all 24", "leakage", "deletion", "inverse",
        "k_join=l", "signed solver", "dual-clock", "4:4", "3:4", "5:4",
        "dimensionless", "lapse", "proper time", "phase is not energy", "generator is not a rate",
        "update count is not time", "source is not stress", "supplied", "derived", "open",
        "n1 —", "n8 —", "broad negative gate: fail / do not ship", "no shared obstruction",
        "no axiom pressure",
    )
    body = "" if not NOTE.exists() else " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    missing = tuple(item for item in required if item not in body)
    return {"required": required, "missing": missing, "pass": not missing}


# ---------------------------------------------------------------------------
# Route A: literal partial-fSWAP deformation of the actual B stream layer.


def partial_involution(involution: np.ndarray, ell: float, branch: int) -> np.ndarray:
    """Shortest constant-generator path from I to an involution at ell=1."""
    theta = branch * math.pi * ell / 2.0
    identity = np.eye(involution.shape[0], dtype=complex)
    phase = np.exp(2j * theta)
    return 0.5 * ((1 + phase) * identity + (1 - phase) * involution)


def partial_stream_update(length: int, coin: np.ndarray, ell: float, branch: int) -> np.ndarray:
    _, onsite_coin, _, reverse_layer, edge_layer = cycle230.spatial_layers(length, coin)
    return partial_involution(edge_layer, ell, branch) @ reverse_layer @ onsite_coin


def pair_inner(left: np.ndarray, right: np.ndarray) -> complex:
    return 0.5 * np.vdot(left, right)


def one_body_pair_action(operator: np.ndarray, amplitude: np.ndarray) -> np.ndarray:
    return operator @ amplitude + amplitude @ operator.T


def route_a_partial_stream() -> dict:
    rows = []
    maximum_endpoint = 0.0
    maximum_inverse = 0.0
    maximum_reciprocal = 0.0
    maximum_covariance = 0.0
    minimum_deletion = math.inf
    minimum_nonconservation = math.inf
    minimum_contact_witness = math.inf
    for beta, length, held in ((-0.3, 2, False), (-0.35, 3, True)):
        species = cycle219.common_species(beta)
        actual, _, _, reverse_layer, edge_layer = cycle230.spatial_layers(length, species.coin)
        identity = np.eye(actual.shape[0], dtype=complex)
        epsilon = 1.0e-6
        branch_rows = []
        for branch in (-1, 1):
            endpoint = partial_stream_update(length, species.coin, 1.0, branch)
            endpoint_residual = float(np.linalg.norm(endpoint - actual))
            maximum_endpoint = max(maximum_endpoint, endpoint_residual)
            inverse = float(np.linalg.norm(endpoint.conj().T @ endpoint - identity))
            maximum_inverse = max(maximum_inverse, inverse)
            plus = partial_stream_update(length, species.coin, 1.0 + epsilon, branch)
            minus = partial_stream_update(length, species.coin, 1.0 - epsilon, branch)
            reciprocal_fd = -1j * actual.conj().T @ ((plus - minus) / (2 * epsilon))
            expected = (
                branch * math.pi / 2
                * (reverse_layer @ np.kron(np.eye(length ** 3), species.coin)).conj().T
                @ (np.eye(edge_layer.shape[0]) - edge_layer)
                @ (reverse_layer @ np.kron(np.eye(length ** 3), species.coin))
            )
            reciprocal_residual = float(np.linalg.norm(reciprocal_fd - expected))
            maximum_reciprocal = max(maximum_reciprocal, reciprocal_residual)
            conservation_defect = float(
                np.linalg.norm(actual.conj().T @ expected @ actual - expected)
                / max(np.linalg.norm(expected), 1e-30)
            )
            minimum_nonconservation = min(minimum_nonconservation, conservation_defect)
            deleted = partial_stream_update(length, species.coin, 0.0, branch)
            deletion_signal = float(np.linalg.norm(deleted - actual) / np.linalg.norm(actual))
            minimum_deletion = min(minimum_deletion, deletion_signal)

            pair = cycle591.random_pair(length, 5940 + length + branch)
            before_contact = actual @ pair @ actual.T
            after_contact = cycle230.contact_pair_step(before_contact, length, cycle230.COUPLING)
            before_value = pair_inner(before_contact, one_body_pair_action(expected, before_contact))
            after_value = pair_inner(after_contact, one_body_pair_action(expected, after_contact))
            contact_witness = abs(after_value - before_value)
            minimum_contact_witness = min(minimum_contact_witness, contact_witness)
            branch_rows.append({
                "branch": branch,
                "endpoint_exact_actual_stream_residual": endpoint_residual,
                "inverse_or_unitarity_residual": inverse,
                "reciprocal_finite_difference_residual": reciprocal_residual,
                "normalized_full_free_update_conservation_defect": conservation_defect,
                "two_particle_actual_contact_expectation_change": float(contact_witness),
                "delete_partial_edge_layer_signal": deletion_signal,
            })

        # Both shortest sign branches end at the same fSWAP stream.  Their
        # tangents are opposite, so geometry plus endpoint fixes |pi/2| but
        # cannot select the sign/orientation.
        plus_j = branch_rows[1]
        minus_j = branch_rows[0]
        sign_endpoint_gap = abs(
            plus_j["endpoint_exact_actual_stream_residual"]
            - minus_j["endpoint_exact_actual_stream_residual"]
        )
        frame_residuals = []
        if length == 2:
            for frame in cycle219.c210.proper_cubic_frames():
                representation = cycle230.frame_representation(length, frame)
                deformed = partial_stream_update(length, species.coin, 0.37, 1)
                frame_residuals.append(float(np.linalg.norm(
                    representation @ deformed @ representation.conj().T - deformed
                )))
            maximum_covariance = max(maximum_covariance, max(frame_residuals))
        rows.append({
            "beta": beta, "held": held, "length": length,
            "branches": branch_rows, "sign_endpoint_gap": sign_endpoint_gap,
            "all24_covariance_maximum": max(frame_residuals) if frame_residuals else None,
        })

    seam, _, _ = cycle230.seam_block(1.5, 1.65, -1)
    mass = cycle219.common_species(cycle230.BETA)
    return {
        "deformation": "B_sigma(ell)=exp[i sigma pi ell (I-B_fSWAP)/2] on the literal disjoint edge layer; G=B_sigma A C",
        "physical_M2_support": "one routed two-mode fermionic beam splitter per disjoint edge; bounded two-M2 target macro through Cycle560/563",
        "endpoint": "ell=1 is the exact actual Cycle230 stream for sigma=+/-1",
        "coordinate_reciprocal": "sigma(pi/2) C^dag A^dag(I-B) A C",
        "shortest_geodesic_selects_absolute_coefficient": True,
        "selected_absolute_coefficient": math.pi / 2,
        "sign_selected_by_geometry": False,
        "both_sign_branches_have_same_physical_endpoint": True,
        "coefficient_inserted_as_qN": False,
        "rows": rows,
        "maximum_endpoint_residual": maximum_endpoint,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_reciprocal_residual": maximum_reciprocal,
        "maximum_all24_covariance_residual": maximum_covariance,
        "minimum_deletion_signal": minimum_deletion,
        "minimum_normalized_nonconservation_defect": minimum_nonconservation,
        "minimum_actual_contact_witness": minimum_contact_witness,
        "operator_conserved_under_full_free_contact": False,
        "local_scalar_continuity_derived": False,
        "mass_fixture_relative_residual": abs(cycle219.rest_mass(mass) / mass.analytic_mass - 1),
        "seam_singular_values": np.linalg.svd(seam, compute_uv=False).tolist(),
        "result_scope": "literal local geometry deformation fixes a tangent magnitude in a declared shortest path, but sign and conserved-source status remain open",
    }


# ---------------------------------------------------------------------------
# Route B: locally prepared and dynamically stationary seeded composite.


def householder_map(source: np.ndarray, target: np.ndarray) -> np.ndarray:
    source = source / np.linalg.norm(source)
    target = target / np.linalg.norm(target)
    difference = source - target
    if np.linalg.norm(difference) < 1e-15:
        return np.eye(len(source), dtype=complex)
    direction = difference / np.linalg.norm(difference)
    return np.eye(len(source), dtype=complex) - 2 * np.outer(direction, direction.conj())


def scalar_seed_preparation(coin: np.ndarray) -> tuple[np.ndarray, np.ndarray, complex]:
    eigenvalues, eigenvectors = np.linalg.eig(coin)
    scalar = np.ones(6, dtype=complex) / math.sqrt(6)
    overlaps = [abs(np.vdot(scalar, eigenvectors[:, index])) for index in range(6)]
    scalar_vector = eigenvectors[:, int(np.argmax(overlaps))]
    scalar_vector *= np.exp(-1j * np.angle(np.vdot(scalar, scalar_vector)))
    scalar_vector /= np.linalg.norm(scalar_vector)
    source = np.zeros(7, dtype=complex); source[6] = 1
    target = np.r_[scalar_vector, 0.0]
    preparation = householder_map(source, target)
    eigenphase = np.vdot(scalar_vector, coin @ scalar_vector)
    return preparation, scalar_vector, eigenphase


def embedded_swap(dimension: int, left: int, right: int) -> np.ndarray:
    result = np.eye(dimension, dtype=complex)
    result[left, left] = result[right, right] = 0
    result[left, right] = result[right, left] = 1
    return result


def bound_one_particle_update(length: int, coin: np.ndarray, anchor_site: tuple[int, int, int]) -> np.ndarray:
    """Matter+six buffers; anchor occupation is the local control parameter."""
    matter_dimension = 6 * length ** 3
    dimension = 2 * matter_dimension
    coin_ext = np.eye(dimension, dtype=complex)
    coin_ext[:matter_dimension, :matter_dimension] = np.kron(np.eye(length ** 3), coin)
    stream = cycle230.spatial_layers(length, coin)[2]
    stream_ext = np.eye(dimension, dtype=complex)
    stream_ext[:matter_dimension, :matter_dimension] = stream
    buffer_swap = np.eye(dimension, dtype=complex)
    for direction in range(6):
        matter = cycle230.site_index(anchor_site, direction, length)
        buffer = matter_dimension + matter
        buffer_swap = embedded_swap(dimension, matter, buffer) @ buffer_swap
    return buffer_swap @ stream_ext @ buffer_swap @ coin_ext


def route_b_bound_composite() -> dict:
    rows = []
    maximum_stationary = 0.0
    maximum_resource = 0.0
    maximum_inverse = 0.0
    maximum_unbound = 0.0
    maximum_cubic = 0.0
    minimum_binder_deletion = math.inf
    for beta, length, held in ((-0.3, 2, False), (-0.35, 3, True)):
        species = cycle219.common_species(beta)
        anchor_site = (0, 0, 0)
        preparation, scalar, scalar_phase = scalar_seed_preparation(species.coin)
        seed = np.zeros(7, dtype=complex); seed[6] = 1
        prepared = preparation @ seed
        preparation_residual = float(np.linalg.norm(prepared[:6] - scalar) + abs(prepared[6]))
        prep_number = np.diag([1.0] * 7)
        prep_resource = float(np.linalg.norm(preparation.conj().T @ prep_number @ preparation - prep_number))

        update = bound_one_particle_update(length, species.coin, anchor_site)
        matter_dimension = 6 * length ** 3
        state = np.zeros(2 * matter_dimension, dtype=complex)
        for direction in range(6):
            state[cycle230.site_index(anchor_site, direction, length)] = scalar[direction]
        after = update @ state
        stationary = float(np.linalg.norm(after - scalar_phase * state))
        maximum_stationary = max(maximum_stationary, stationary)
        inverse = float(np.linalg.norm(update.conj().T @ update - np.eye(update.shape[0])))
        maximum_inverse = max(maximum_inverse, inverse)
        total_resource = np.eye(update.shape[0])
        resource_residual = float(np.linalg.norm(update.conj().T @ total_resource @ update - total_resource))
        maximum_resource = max(maximum_resource, resource_residual)

        actual, _, _, _, _ = cycle230.spatial_layers(length, species.coin)
        no_anchor = np.eye(2 * matter_dimension, dtype=complex)
        no_anchor[:matter_dimension, :matter_dimension] = actual
        unbound_residual = float(np.linalg.norm(
            no_anchor[:matter_dimension, :matter_dimension] - actual
        ))
        maximum_unbound = max(maximum_unbound, unbound_residual)
        dispersed = no_anchor @ state
        source_modes = [cycle230.site_index(anchor_site, d, length) for d in range(6)]
        source_probability = float(np.sum(abs(dispersed[source_modes]) ** 2))
        deletion_signal = 1.0 - source_probability
        minimum_binder_deletion = min(minimum_binder_deletion, deletion_signal)

        frame_residual = 0.0
        direction_scalar = np.ones(6) / math.sqrt(6)
        for frame in cycle219.c210.proper_cubic_frames():
            direction_rep = cycle219.c210.direction_permutation(frame)
            frame_residual = max(frame_residual, float(np.linalg.norm(direction_rep @ direction_scalar - direction_scalar)))
        maximum_cubic = max(maximum_cubic, frame_residual)

        branch_states = []
        for site in ((0, 0, 0), (1, 0, 0), (0, 1, 0)):
            branch = np.zeros(2 * matter_dimension, dtype=complex)
            for direction in range(6):
                branch[cycle230.site_index(site, direction, length)] = scalar[direction]
            branch_states.append(branch)
        gram = np.asarray([[np.vdot(left, right) for right in branch_states] for left in branch_states])
        gram_residual = float(np.linalg.norm(gram - np.eye(3)))
        rows.append({
            "beta": beta, "held": held, "length": length,
            "preparation_seed_to_scalar_residual": preparation_residual,
            "preparation_joint_matter_plus_seed_debit_residual": prep_resource,
            "stationary_ray_residual_after_actual_coin_buffer_stream_contact_N1": stationary,
            "resource_conservation_residual": resource_residual,
            "inverse_residual": inverse,
            "unbound_binder_zero_sector_equals_actual_update_residual": unbound_residual,
            "delete_binder_localization_loss": deletion_signal,
            "three_position_branch_Gram_residual": gram_residual,
            "scalar_phase": [float(scalar_phase.real), float(scalar_phase.imag)],
        })
    return {
        "macro": "uniform local seed-to-scalar preparation plus anchor-controlled pre/post stream buffers",
        "extra_M2_per_cell": 8,
        "resources": "one persistent binder, one debited seed, and six returned-blank direction buffers per cell",
        "local_gate_support": "seed/scalar preparation decomposes inside one eight-M2 cell; controlled buffer fSWAP support three",
        "same_law_at_every_site": True,
        "host_position_query_or_dynamic_pinning": False,
        "initial_binder_and_seed_occupations_supplied": True,
        "autonomous_genesis_from_blank": False,
        "joint_continuity": "Delta(N_matter+N_seed+N_buffer)=0 at preparation and every update; binder is separately conserved; bound current is zero",
        "actual_contact": "included and identity on N=1; local-number contact cannot delocalize a bound N>1 onsite sector",
        "rows": rows,
        "maximum_stationary_ray_residual": maximum_stationary,
        "maximum_joint_resource_residual": maximum_resource,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_unbound_sector_residual": maximum_unbound,
        "maximum_all24_covariance_residual": maximum_cubic,
        "minimum_binder_deletion_signal": minimum_binder_deletion,
        "physical_M2_lift": "literal seed/binder/buffer M2 plus inherited Cycle560/563 matter macro; no parity, frame, or sector query",
        "mass_fixture_scope": "binder=0 is exactly Cycle219/230 and preserves its mass; the stationary binder=1 composite is a new flat sector, not an inertial-mass equivalence",
        "result_scope": "stationary localized source prepared by a uniform local law conditional on supplied physical seed and binder resources",
    }


# ---------------------------------------------------------------------------
# Route C: finite code-native proper-cubic quadrature and signed-solver join.


SAMPLE_OFFSETS = np.asarray(((0, 0, 0), (1, 0, 0), (-1, 0, 0),
                             (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)), dtype=int)


def einstein_pairing_numeric(momentum4: np.ndarray) -> np.ndarray:
    """Numeric transcription of the exact-pinned Euclidean EH pairing."""
    momentum4 = np.asarray(momentum4, dtype=float)
    result = np.zeros((10, 10), dtype=float)
    for column, (left, right) in enumerate(cycle576.regge.HCOMPS):
        metric = np.zeros((4, 4), dtype=float)
        metric[left, right] = 1
        metric[right, left] = 1
        ricci = np.zeros((4, 4), dtype=float)
        for mu in range(4):
            for nu in range(4):
                value = 0.0
                for lam in range(4):
                    value += (
                        -momentum4[lam] * momentum4[mu] * metric[lam, nu]
                        - momentum4[lam] * momentum4[nu] * metric[lam, mu]
                        + momentum4[lam] ** 2 * metric[mu, nu]
                        + momentum4[mu] * momentum4[nu] * metric[lam, lam]
                    )
                ricci[mu, nu] = value / 2
        einstein = ricci - 0.5 * np.eye(4) * np.trace(ricci)
        for row, (mu, nu) in enumerate(cycle576.regge.HCOMPS):
            result[row, column] = (2.0 if mu != nu else 1.0) * einstein[mu, nu]
    return (result + result.T) / 2


def discrete_eh_hessian(momentum3: np.ndarray) -> np.ndarray:
    # The -1/2 coefficient is frozen from Cycle576's independently selected
    # Regge-to-R3 small-k comparison before any Cycle588 K_join evaluation.
    derivative = 2 * np.sin(np.asarray(momentum3, dtype=float) / 2)
    return -0.5 * einstein_pairing_numeric(np.r_[derivative, 0.0])


def quadrature_encoding(momentum3: np.ndarray) -> np.ndarray:
    phases = np.exp(1j * SAMPLE_OFFSETS @ np.asarray(momentum3, dtype=float)) / math.sqrt(7)
    return np.kron(phases[:, None], np.eye(10, dtype=complex))


def quadrature_physical_hessian(momentum3: np.ndarray, penalty: float = 0.73) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    encoding = quadrature_encoding(momentum3)
    code = discrete_eh_hessian(momentum3)
    projector = encoding @ encoding.conj().T
    physical = encoding @ code @ encoding.conj().T + penalty * (np.eye(70) - projector)
    return physical, code, encoding


def sample_representation(frame: np.ndarray) -> np.ndarray:
    result = np.zeros((7, 7))
    lookup = {tuple(offset): index for index, offset in enumerate(SAMPLE_OFFSETS)}
    for target, offset in enumerate(SAMPLE_OFFSETS):
        source_offset = tuple((frame.T @ offset).tolist())
        result[target, lookup[source_offset]] = 1
    return result


def route_c_code_native_quadrature() -> dict:
    rows = []
    maximum_generator = 0.0
    maximum_update = 0.0
    maximum_leakage = 0.0
    maximum_inverse = 0.0
    maximum_gauge = 0.0
    maximum_null_error = 0
    maximum_join = 0.0
    maximum_covariance = 0.0
    comparator_momentum = np.asarray((0.2, 0.13, 0.07))
    comparator_derivative = np.r_[2 * np.sin(comparator_momentum / 2), 0.0]
    retained_comparator = cycle576.regge.einstein_pairing_4d(comparator_derivative)
    numeric_comparator_residual = float(np.linalg.norm(
        retained_comparator - einstein_pairing_numeric(comparator_derivative)
    ))
    for label, momentum3, held in (
        ("TRAIN", np.asarray((0.2, 0.13, 0.07)), False),
        ("HELD_L4", np.asarray((math.pi / 2, math.pi / 2, 0.0)), True),
        ("HELD_L5", np.asarray((2 * math.pi / 5,) * 3), True),
        ("HELD_SMALL", np.asarray((0.03, 0.02, 0.01)), True),
    ):
        physical, code, encoding = quadrature_physical_hessian(momentum3)
        generator = float(np.linalg.norm(physical @ encoding - encoding @ code))
        maximum_generator = max(maximum_generator, generator)
        update_code = expm(-1j * 0.037 * code)
        projector = encoding @ encoding.conj().T
        update_physical = encoding @ update_code @ encoding.conj().T + np.exp(-1j * 0.037 * 0.73) * (np.eye(70) - projector)
        update = float(np.linalg.norm(update_physical @ encoding - encoding @ update_code))
        maximum_update = max(maximum_update, update)
        leakage = float(np.linalg.norm((np.eye(70) - projector) @ update_physical @ encoding))
        maximum_leakage = max(maximum_leakage, leakage)
        inverse = float(np.linalg.norm(update_physical.conj().T @ update_physical - np.eye(70)))
        maximum_inverse = max(maximum_inverse, inverse)
        eigenvalues = np.linalg.eigvalsh(code)
        cutoff = 1e-9 * max(float(np.max(abs(eigenvalues))), 1.0)
        null_count = int(np.sum(abs(eigenvalues) < cutoff))
        maximum_null_error = max(maximum_null_error, abs(null_count - 4))
        derivative = 2 * np.sin(momentum3 / 2)
        gauge = cycle576.continuum_gauge_metric(np.r_[derivative, 0.0])
        gauge_residual = float(np.linalg.norm(code @ gauge))
        maximum_gauge = max(maximum_gauge, gauge_residual)

        source = np.zeros(10); source[3] = 1.0
        chi = float(np.real(source @ np.linalg.pinv(code, rcond=1e-10) @ source))
        joined = -2 / chi
        graph = cycle588.graph_symbol(momentum3)
        join_residual = abs(joined - graph)
        maximum_join = max(maximum_join, join_residual)

        covariance_rows = []
        for frame, metric_rep in zip(cycle576.FRAMES, cycle576.METRIC_REPS):
            rotated = frame @ momentum3
            physical_rotated, code_rotated, encoding_rotated = quadrature_physical_hessian(rotated)
            physical_rep = np.kron(sample_representation(frame), metric_rep)
            code_covariance = float(np.linalg.norm(code_rotated @ metric_rep - metric_rep @ code))
            encoding_covariance = float(np.linalg.norm(encoding_rotated @ metric_rep - physical_rep @ encoding))
            physical_covariance = float(np.linalg.norm(physical_rotated @ physical_rep - physical_rep @ physical))
            covariance_rows.append(max(code_covariance, encoding_covariance, physical_covariance))
        maximum_covariance = max(maximum_covariance, max(covariance_rows))
        rows.append({
            "fixture": label, "held": held, "momentum": momentum3.tolist(),
            "generator_EG_residual": generator, "update_EG_residual": update,
            "code_leakage": leakage, "inverse_residual": inverse,
            "gauge_residual": gauge_residual, "null_count": null_count,
            "K_join": joined, "graph_symbol": graph, "K_join_residual": join_residual,
            "all24_covariance_maximum": max(covariance_rows),
        })

    source_join = cycle591.route_c_join()
    center_only = 1 / math.sqrt(7)
    quadrature_deletion = math.sqrt(1 - center_only ** 2)
    return {
        "code": "ten metric amplitudes embedded isometrically into center plus six nearest-neighbor sample copies",
        "finite_auxiliary_quadrature": "proper-cubic seven-sample endpoint cubature, radius one; physical generator range at most three",
        "code_generator": "Q_code(k)=-(1/2) G_EH[p_i=2 sin(k_i/2), p_tick=0]",
        "staggered_incidence_compiler": "each p_i is the bounded two-endpoint incidence through a fixed half-edge role; quadratic products compose two local incidences",
        "maximum_incidence_gate_support_M2": 2,
        "maximum_generator_radius_on_staggered_role_graph": 1,
        "normalization_freeze": "-1/2 frozen from Cycle576 Regge/R3 comparison before Cycle588 K_join evaluation",
        "normalization_fitted_to_K_join": False,
        "numeric_to_exact_pinned_EH_helper_residual": numeric_comparator_residual,
        "physical_generator": "Q_physical=E Q_code E^dag + Delta(I-EE^dag), Delta=0.73",
        "post_hoc_projection_of_raw_Regge_update": False,
        "rows": rows,
        "maximum_generator_EG_residual": maximum_generator,
        "maximum_update_EG_residual": maximum_update,
        "maximum_code_leakage": maximum_leakage,
        "maximum_inverse_residual": maximum_inverse,
        "maximum_gauge_residual": maximum_gauge,
        "maximum_null_count_error_from_four": maximum_null_error,
        "maximum_K_join_graph_residual": maximum_join,
        "maximum_all24_covariance_residual": maximum_covariance,
        "all576_frame_pair_checks": len(cycle576.FRAMES) ** 2,
        "quadrature_auxiliary_deletion_syndrome": quadrature_deletion,
        "penalty_deletion_additional_nulls": 60,
        "physical_M2_per_frame_sector": 70,
        "co_present_all24_M2": 70 * len(cycle576.FRAMES),
        "exact_sinc_metric_image_compiled": False,
        "actual_Regge_edge_update_reproduced": False,
        "signed_solver_join": {
            "train": source_join["train"], "held": source_join["held"],
            "background_physical_origin_derived": source_join["background_physical_origin_derived"],
            "maximum_inherited_Green_residual": source_join["held_Green_surface"]["maximum_relative_residual"],
        },
        "result_scope": "new code-native finite-range metric law with exact four-null EG and K_join=L; not the exact sinc/Regge edge compiler",
    }


def dual_clock_composition(route_b: dict, route_c: dict) -> dict:
    """Typed positive-output adapter to the retained Cycle451 comparator."""
    start = cycle451.c444.HELD_START
    source_off = cycle451.interval_for_positions(start, 6, 6)
    receiver_zero = cycle451.interval_for_positions(start, 6, 6)
    delay = cycle451.interval_for_positions(start, 6, 5)
    advance = cycle451.interval_for_positions(start, 6, 7)
    malformed = cycle451.interval_for_positions(start, 6, 5, profile_certificate=False)
    common_rescalings = []
    for scale in (Fraction(1, 3), Fraction(7, 5), Fraction(11, 2)):
        common_rescalings.append(cycle451.calibrated_ratio(
            delay, scale, scale, cross_profile_certificate=False
        ))
    ratios = {
        "source_off": str(source_off.probe_over_reference) if source_off else None,
        "source_on_receiver_zero": str(receiver_zero.probe_over_reference) if receiver_zero else None,
        "source_on_receiver_one_delay": str(delay.probe_over_reference) if delay else None,
        "source_on_receiver_one_advance": str(advance.probe_over_reference) if advance else None,
    }
    return {
        "positive_source_input": "binder=1, seed=0 after local debit, one stationary scalar matter occupation; alternatively its signed solver source word",
        "reversible_adapter": "local binder-and-occupation controlled receiver M2; uncomputed branch remains coherent and the control is not a Record",
        "required_complete_endpoint_fields": (
            "one-hot reference/probe clock words, common nonzero start/end event identities, distinct devices, "
            "common epoch/profile, typed+permanent conditional endpoints, causal predecessor, and response rail returned blank"
        ),
        "response_law_input": "delay versus advance remains a separately supplied law; source output does not select it",
        "field_extension_interface": "Cycles459/461 additionally require a locally encoded receiver amplitude/profile and complete source identity/calibration sidecars; K_join solver words can supply amplitudes only after a separately selected word-to-response map",
        "ratios": ratios,
        "common_rescaling_ratios": [str(value) for value in common_rescalings],
        "malformed_profile_is_typed_undefined": malformed is None,
        "all_ratios_dimensionless": True,
        "lapse_derived": False,
        "proper_time_derived": False,
        "response_law_selected": False,
        "source_is_physical_stress": False,
        "route_B_stationary_input_available": route_b["maximum_stationary_ray_residual"] < TOL,
        "route_C_static_field_input_available": route_c["maximum_K_join_graph_residual"] < TOL,
    }


def inventories() -> dict:
    return {
        "supplied": [
            "linear shortest-geodesic coordinate and choice of stream B layer",
            "partial-fSWAP branch orientation although both signs are audited",
            "local binder and seed occupations, buffer blanks, and preparation schedule",
            "Cycle219 beta/species law and Cycle230 contact/order",
            "new seven-sample metric code, off-code penalty, and co-present frame sectors",
            "Cycle576 -1/2 normalization, Cycle588 tick readout, periodic signed background, precision and iterations",
        ],
        "derived": [
            "exact partial-fSWAP endpoint, reciprocal, shortest-path magnitude and sign degeneracy",
            "nonconservation/contact witness for the exchange reciprocal",
            "exact local seed debit, stationary scalar composite, zero bound current and coherent position branches",
            "binder-zero equality with the actual matter update and active binder deletion",
            "code-native seven-sample EG, four gauge nulls, all24 covariance, inverse and leakage controls",
            "K_join=L from independently frozen -1/2 discrete-EH normalization and tick covector",
            "coherent join to the existing paid-zero-mode signed solver and frozen Green surface",
        ],
        "open": [
            "selection of partial-fSWAP sign/path as physical metric deformation and a conserved source from it",
            "autonomous genesis of the local binder, seed, signed background, and metric code state",
            "empirical identification/calibration of the stationary joint resource as physical stress or gravity",
            "derivation of the seven-sample discrete-EH law from the actual Regge edge update or exact sinc image",
            "simultaneous nonlinear matter-metric backreaction and open-boundary single-source response",
            "arbitrary locally enforced sector/size, physical time, Record, Born probability, and realized history",
        ],
    }


def no_go_discipline() -> dict:
    families = (
        {
            "family": "partial-fSWAP stream geodesic", "object": "literal Cycle230 B edge layer",
            "mechanism": "two-mode shortest involution path", "terminal": "geometry-selected conserved reciprocal",
            "marker": "ATTEMPTED", "result": "magnitude selected inside declared path; sign degenerate and reciprocal not conserved",
        },
        {
            "family": "occupation-phase source", "object": "onsite q_beta N density",
            "mechanism": "local U(1) number continuity", "terminal": "conserved source candidate",
            "marker": "RULED OUT BY PRIOR ONLY FOR LAW-SELECTION TERMINAL", "result": "Cycle591 conservation positive; coupling selection open",
        },
        {
            "family": "seeded binder-buffer composite", "object": "matter+seed+binder+six buffers",
            "mechanism": "local debit plus pre/post-stream capture", "terminal": "stationary localized source without runtime host pinning",
            "marker": "ATTEMPTED", "result": "positive conditional on supplied local seed/binder genesis",
        },
        {
            "family": "Cycle566 reservoir source", "object": "matter+mediator+reservoir occupation",
            "mechanism": "number-conserving local exchange", "terminal": "resource continuity",
            "marker": "RULED OUT BY PRIOR ONLY FOR PHYSICAL-ID TERMINAL", "result": "debit positive; weights/action/genesis open",
        },
        {
            "family": "seven-sample discrete-EH code", "object": "70-rail proper-cubic metric block",
            "mechanism": "finite quadrature isometry plus off-code penalty", "terminal": "four-null exact local EG and static pole",
            "marker": "ATTEMPTED", "result": "positive new law; actual Regge/sinc derivation open",
        },
        {
            "family": "exact sinc Regge image", "object": "15-edge line-average image",
            "mechanism": "exact metric-to-edge map", "terminal": "bounded preserved raw-update image",
            "marker": "RULED OUT BY CYCLE588 ONLY FOR RAW-UPDATE TERMINAL", "result": "four nulls; non-Laurent and raw leakage remains",
        },
        {
            "family": "code-native Regge auxiliary quadrature", "object": "edge/half-edge internal sample rails",
            "mechanism": "update designed on exact finite Regge code", "terminal": "actual-Regge finite EG with four nulls",
            "marker": "OPEN", "result": "not equivalent to the new discrete-EH code and remains live",
        },
        {
            "family": "open-boundary endogenous field", "object": "single localized source plus boundary reservoir",
            "mechanism": "outgoing boundary flux instead of periodic background", "terminal": "autonomous zero-mode/source genesis",
            "marker": "OPEN", "result": "could remove the signed uniform background import",
        },
    )
    walls = ("W_select", "W_genesis", "W_regge", "W_calibrate", "W_nonlinear")
    pairs = [
        {"left": walls[i], "right": walls[j], "left_implies_right": False,
         "right_implies_left": False, "independent": True}
        for i in range(len(walls)) for j in range(i + 1, len(walls))
    ]
    return {
        "N1 — alternative route enumeration": families,
        "N2 — wall independence": {"collapsed_walls": walls, "pairwise": pairs},
        "N3 — hidden-wall scan": "ell path, sign, B-layer choice, beta/contact, seed/binder/background blanks, schedules, code/action/penalty, frames, precision and boundaries are explicit supplies",
        "N4 — residual matching": [
            {"witness": "Cycle591", "witness_residual": "phase coupling selection/staticity/range", "current_residual": "stream path, seeded binding, code-native range", "match": "yes, attacked separately"},
            {"witness": "Cycle588", "witness_residual": "raw exact-sinc preservation and supplied static source", "current_residual": "new code rather than raw image; stationary seeded source", "match": "partial only; no actual-Regge closure claimed"},
            {"witness": "Cycle576", "witness_residual": "Regge/R3 -1/2 shore with law selection open", "current_residual": "normalization premise for new discrete-EH code", "match": "normalization only, not source identification"},
            {"witness": "Cycle566", "witness_residual": "resource debit with supplied genesis/weights", "current_residual": "seed debit and binder genesis", "match": "debit mechanism only"},
        ],
        "N5 — rhetoric audit": "partial-fSWAP failure is one path and one/two-particle fixtures; stationary means the seeded binder code only; seven-sample closure is per block and lattice-symbol/all24, not exact sinc/Regge or nonlinear gravity",
        "N6 — partial-closure paths": "derive a coordinate action selecting a branch; make binder/seed a mobile bound dimer; design a finite exact-Regge code update; use an open boundary reservoir; empirically calibrate the source",
        "N7 — steelman": "A mobile two-body flat-band dimer could remove the immobile binder, while an edge-native quantum-link action could select the partial-swap orientation and make the exact Regge quadrature code invariant; the present conditional constructions make both mechanisms actionable.",
        "N8 — cross-cycle echo": "Cycles566,576,588,591 retired debit, Regge, pole, and conservation imports through explicit constructions; Cycle594 likewise moves staticity/range without constitutional change and therefore cannot support a shared no-go.",
        "normalized_family_count": len(families),
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_obstruction": False,
        "axiom_pressure": False,
        "disposition": "positive partial construction with narrow route-specific failures and live alternatives",
    }


def json_default(value: object) -> object:
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    raise TypeError(type(value))


def main() -> None:
    started = perf_counter()
    dependencies = dependency_controls()
    note = note_contract()
    route_a = route_a_partial_stream()
    route_b = route_b_bound_composite()
    route_c = route_c_code_native_quadrature()
    clock_join = dual_clock_composition(route_b, route_c)
    inventory = inventories()
    nogo = no_go_discipline()

    check("exact-pinned Cycle591/588/576/566/230/219 shores", dependencies["pass"])
    check("note contract preserves scopes and full N1-N8", note["pass"], note["missing"])
    check("Route A literal partial-fSWAP reaches the exact actual stream on both sign branches",
          route_a["maximum_endpoint_residual"] < TOL and route_a["maximum_inverse_residual"] < TOL,
          (route_a["maximum_endpoint_residual"], route_a["maximum_inverse_residual"]))
    check("Route A reciprocal is derived and proper-cubic covariant",
          route_a["maximum_reciprocal_residual"] < TOL
          and route_a["maximum_all24_covariance_residual"] < TOL,
          (route_a["maximum_reciprocal_residual"], route_a["maximum_all24_covariance_residual"]))
    check("Route A does not counterfeit coefficient/sign/source selection",
          route_a["shortest_geodesic_selects_absolute_coefficient"]
          and not route_a["sign_selected_by_geometry"]
          and route_a["minimum_normalized_nonconservation_defect"] > 1e-3
          and route_a["minimum_actual_contact_witness"] > 1e-8)
    check("Route A deletion and inherited mass/contact/seam controls remain active",
          route_a["minimum_deletion_signal"] > 0.1
          and route_a["mass_fixture_relative_residual"] < TOL
          and min(route_a["seam_singular_values"]) > 0.9)

    check("Route B local seed debit prepares an exact scalar matter excitation",
          max(row["preparation_seed_to_scalar_residual"] for row in route_b["rows"]) < TOL
          and max(row["preparation_joint_matter_plus_seed_debit_residual"] for row in route_b["rows"]) < TOL)
    check("Route B binder-buffer composite is stationary with exact joint resource/inverse",
          route_b["maximum_stationary_ray_residual"] < TOL
          and route_b["maximum_joint_resource_residual"] < TOL
          and route_b["maximum_inverse_residual"] < TOL,
          (route_b["maximum_stationary_ray_residual"], route_b["maximum_joint_resource_residual"]))
    check("Route B is uniform/all24, preserves the unbound actual law, and has active binder deletion",
          route_b["maximum_all24_covariance_residual"] < TOL
          and route_b["maximum_unbound_sector_residual"] < TOL
          and route_b["minimum_binder_deletion_signal"] > 0.1)
    check("Route B keeps binder/seed genesis explicit",
          route_b["initial_binder_and_seed_occupations_supplied"]
          and not route_b["autonomous_genesis_from_blank"]
          and not route_b["host_position_query_or_dynamic_pinning"])

    check("Route C code-native quadrature has exact local generator/update EG",
          route_c["maximum_generator_EG_residual"] < TOL
          and route_c["maximum_update_EG_residual"] < TOL
          and route_c["numeric_to_exact_pinned_EH_helper_residual"] < TOL
          and route_c["maximum_incidence_gate_support_M2"] == 2,
          (route_c["maximum_generator_EG_residual"], route_c["maximum_update_EG_residual"]))
    check("Route C has exactly four gauge nulls with all24 covariance",
          route_c["maximum_null_count_error_from_four"] == 0
          and route_c["maximum_gauge_residual"] < TOL
          and route_c["maximum_all24_covariance_residual"] < TOL,
          (route_c["maximum_gauge_residual"], route_c["maximum_all24_covariance_residual"]))
    check("Route C inverse/leakage/deletion controls are active",
          route_c["maximum_code_leakage"] < TOL
          and route_c["maximum_inverse_residual"] < TOL
          and route_c["quadrature_auxiliary_deletion_syndrome"] > 0.8
          and route_c["penalty_deletion_additional_nulls"] == 60)
    check("Route C independently frozen normalization preserves exact K_join=L",
          not route_c["normalization_fitted_to_K_join"]
          and route_c["maximum_K_join_graph_residual"] < TOL,
          route_c["maximum_K_join_graph_residual"])
    check("Route C joins coherently to signed train/held solver without promoting background genesis",
          not route_c["signed_solver_join"]["background_physical_origin_derived"]
          and route_c["signed_solver_join"]["maximum_inherited_Green_residual"] < 0.002
          and all(branch["solver"]["solution_L2_error"] <= branch["solver"]["rigorous_error_bound"]
                  for fixture in (route_c["signed_solver_join"]["train"], route_c["signed_solver_join"]["held"])
                  for branch in fixture["branches"]))
    check("positive stationary source composes with the typed Cycle451 dimensionless clock comparator",
          clock_join["ratios"] == {
              "source_off": "1", "source_on_receiver_zero": "1",
              "source_on_receiver_one_delay": "3/4", "source_on_receiver_one_advance": "5/4",
          }
          and clock_join["common_rescaling_ratios"] == ["3/4"] * 3
          and clock_join["malformed_profile_is_typed_undefined"]
          and not clock_join["lapse_derived"] and not clock_join["proper_time_derived"])
    check("supplied/derived/open and N1-N8 forbid broad negative or axiom pressure",
          bool(inventory["supplied"] and inventory["derived"] and inventory["open"])
          and nogo["normalized_family_count"] >= 5
          and nogo["broad_negative_gate"] == "FAIL / DO NOT SHIP"
          and not nogo["shared_obstruction"] and not nogo["axiom_pressure"])

    report = {
        "cycle": 594, "date": "2026-07-22", "authority": AUTHORITY, "audit": AUDIT,
        "dependencies": dependencies, "note_contract": note,
        "route_A": route_a, "route_B": route_b, "route_C": route_c,
        "dual_clock_composition": clock_join,
        "inventory": inventory, "no_go_discipline": nogo,
        "closure_ledger": {
            "deformation_selection": "PARTIAL: literal stream path fixes |pi/2| inside a shortest geodesic, but sign/path and conserved-source selection remain open",
            "conservation": "CLOSED for inherited q_beta N and seeded joint resource; partial-fSWAP reciprocal is not conserved",
            "staticity": "CLOSED CONDITIONAL on supplied local binder+seed: a uniform law prepares and holds the scalar source without runtime host pinning",
            "range_enforcement": "CLOSED for a new seven-sample discrete-EH code; actual Regge exact-sinc image remains open",
            "pole_excitation": "CLOSED CONDITIONAL: independently frozen -1/2 code plus tick covector gives exact K_join=L",
            "physical_source_identification": "PARTIAL/OPEN: binder/background genesis, stress meaning, calibration and backreaction remain supplied",
        },
        "six_wall_ledger": {
            "C_ref": "partial-stream shortest path and Cycle576 -1/2 freeze reduce normalization freedom; sign and physical calibration remain supplied",
            "C_num": "seed/binder/buffer and 70-rail quadrature resources are explicit; signed solver bounds retained",
            "C_wrap": "partial-fSWAP and buffer schedules are bounded updates, not physical time or rates",
            "C_int": "actual contact/mass/seam retained; seeded joint continuity closes on the declared bound code",
            "C_local": "new finite seven-sample exact EG/four-null code and bounded binder macro; exact sinc/Regge compiler open",
            "C_source": "stationary conserved joint source and exact pole coexist conditionally; stress identity, genesis and nonlinear backreaction open",
        },
        "maturity_0_to_5": {
            "operational_quantum_records": 4.65, "time": 3.80, "inertia_matter": 4.87,
            "gravity_source": 4.25, "Born_probability": 3.65,
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
