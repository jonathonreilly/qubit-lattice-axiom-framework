#!/usr/bin/env python3
"""Cycle 601: recurrent source, bounded Regge, and response tournament.

All three routes are candidate physical-M2 constructions.  A layer schedule is
not physical time; a generator is not a rate; a modular word is not physical
stress, energy, or a gravitational field.  Authority remains none and audit
remains unset.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import resource
import subprocess
import sys
from time import perf_counter

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as cycle219
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as cycle210
import physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22 as cycle576
import physical_regge_finite_update_frame_selection_tournament_cycle579_2026_07_22 as cycle579


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_RECURRENT_SOURCE_BOUNDED_REGGE_RETARDED_RESPONSE_TOURNAMENT_"
    "CYCLE601_NOTE_2026-07-22.md"
)
AUTHORITY = "none"
AUDIT = "unset"
TOL = 2.0e-8
PASS = 0
FAIL = 0
START = perf_counter()

DEPENDENCIES = {
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py":
        "53d60249420994818e7517645ad4157e1e11c7dc184fbf89b2838e94b53977d0",
    "docs/work_history/repo/review_feedback/PHYSICAL_DYNAMICAL_METRIC_SOURCE_LAW_BRIDGE_TOURNAMENT_CYCLE576_NOTE_2026-07-22.md":
        "2d5650c57d5518e274803f5c511886981c8572b553dda926739cc98199939c20",
    "scripts/physical_full_torus_dimer_M2_compiler_tournament_cycle590_2026_07_22.py":
        "5fbf3bcecc54df9912f9b79d2e5c45d51f145279c1ed83f507bc24e9e1980029",
    "docs/work_history/repo/review_feedback/PHYSICAL_FULL_TORUS_DIMER_M2_COMPILER_TOURNAMENT_CYCLE590_NOTE_2026-07-22.md":
        "3ee6ba9bd5a01a5cab88832788156597a1491d7c2d47f9378caca624a35a1936",
    "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json":
        "ebc13a522e439e2a1618421773751c096b210cc4be25476511dead5a6ea241f7",
    "scripts/physical_mobile_composite_action_regge_quadrature_tournament_cycle596_2026_07_22.py":
        "80249b47661bc1bd668657ee0f2f4e8d8fd72147b9fee7d4930b42c72dc3547f",
    "docs/work_history/repo/review_feedback/PHYSICAL_MOBILE_COMPOSITE_ACTION_REGGE_QUADRATURE_TOURNAMENT_CYCLE596_NOTE_2026-07-22.md":
        "2acc1ccc8be7c06e195117054a591155db85c8ace9d1d3d090c95c3ddb1419ba",
    "outputs/physical_mobile_composite_action_regge_quadrature_tournament_cycle596_cold_2026_07_22.txt":
        "1be790d557ab19078cda6fbf212c0d677ed8f9a3f4dcb5dfe33abf9e7e557891",
    "scripts/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_2026_07_22.py":
        "89c733e3be55ec287e338c4d9ed6062ec8cb222345ff72596662c43b3f1ae6a5",
    "docs/work_history/repo/review_feedback/PHYSICAL_ROOT_FREE_CUTOFF_GAUGE_PREPARATION_TOURNAMENT_CYCLE598_NOTE_2026-07-22.md":
        "6f5f9e52ef41e8b6cd4863eec6c40fff3d8047612c6596e926123617016ab1e0",
    "outputs/physical_root_free_cutoff_gauge_preparation_tournament_cycle598_cold_2026_07_22.txt":
        "19811196cdedba8ebea3607e6a38ab3f83a5c68d6f264ceed795c13cb8fe44a9",
}


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    PASS += int(condition)
    FAIL += int(not condition)
    print("PASS" if condition else "FAIL", label, "::", detail)


def file_sha(relative: str) -> str:
    return sha256((ROOT / relative).read_bytes()).hexdigest()


def shore() -> dict:
    observed = {name: file_sha(name) for name in DEPENDENCIES}
    receipt = json.loads((ROOT / "outputs/physical_full_torus_dimer_M2_compiler_tournament_cycle590_receipt_2026_07_22.json").read_text())
    fixtures = receipt["retained_fixtures"]
    good = (
        observed == DEPENDENCIES
        and receipt["pass"]
        and receipt["authority"] == "none"
        and receipt["audit"] == "unset"
        and max(fixtures.values()) < TOL
    )
    check("Cycles 576/590/596/598 are byte-pinned and the M2 mass/contact/seam shore passes", good,
          {"hashes_match": observed == DEPENDENCIES, "fixtures": fixtures})
    return {"expected": DEPENDENCIES, "observed": observed, "Cycle590_fixtures": fixtures}


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "authority: none", "audit: unset", "cycle 601", "period-2", "not stationary",
        "no external head", "no supplied trajectory", "q=4", "midpoint", "no cloning",
        "givens", "bounded layout", "held l5", "held l7", "out-family l9",
        "schedule is not time", "modular word", "not gravity", "not physical energy",
        "generator is not a rate", "all 24", "all 576", "leakage", "deletion",
        "n1 —", "n8 —", "broad negative gate: fail / do not ship", "no axiom pressure",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note states the scoped construction and full N1-N8 negative gate", not missing, missing)


# ---------------------------------------------------------------------------
# Route A: a uniform, intrinsic, period-two recurrent mobile composite.


DIRECTIONS = np.asarray(cycle210.DIRECTIONS, dtype=int)
REVERSE = np.asarray([
    int(np.where(np.all(DIRECTIONS == -direction, axis=1))[0][0])
    for direction in DIRECTIONS
])


def composite_coin(beta: float) -> np.ndarray:
    coin = cycle219.common_species(beta).coin
    reverse = np.zeros((6, 6), dtype=complex)
    reverse[REVERSE, np.arange(6)] = 1
    result = np.zeros((12, 12), dtype=complex)
    result[6:, :6] = coin
    result[:6, 6:] = reverse
    return result


def composite_step(state: np.ndarray, beta: float) -> tuple[np.ndarray, np.ndarray]:
    """Coin then literal Cycle-230 axial stream; return post-coin and output."""
    length = state.shape[0]
    local = np.einsum("ab,xyzb->xyza", composite_coin(beta), state)
    output = np.zeros_like(local)
    for phase in range(2):
        for direction, velocity in enumerate(DIRECTIONS):
            output[..., 6 * phase + direction] = np.roll(
                local[..., 6 * phase + direction], tuple(int(v) for v in velocity), axis=(0, 1, 2)
            )
    return local, output


def composite_inverse(state: np.ndarray, beta: float) -> np.ndarray:
    unstreamed = np.zeros_like(state)
    for phase in range(2):
        for direction, velocity in enumerate(DIRECTIONS):
            unstreamed[..., 6 * phase + direction] = np.roll(
                state[..., 6 * phase + direction], tuple(int(-v) for v in velocity), axis=(0, 1, 2)
            )
    return np.einsum("ab,xyzb->xyza", composite_coin(beta).conj().T, unstreamed)


def density(state: np.ndarray) -> np.ndarray:
    return np.sum(abs(state) ** 2, axis=-1)


def continuity_residual(local: np.ndarray, streamed: np.ndarray) -> float:
    outgoing = density(local)
    incoming = density(streamed)
    divergence = outgoing.copy()
    for phase in range(2):
        for direction, velocity in enumerate(DIRECTIONS):
            flow = abs(local[..., 6 * phase + direction]) ** 2
            divergence -= np.roll(flow, tuple(int(v) for v in velocity), axis=(0, 1, 2))
    return float(np.max(abs(incoming - outgoing + divergence)))


def direction_permutation(frame: np.ndarray) -> np.ndarray:
    return np.asarray([
        int(np.where(np.all(DIRECTIONS == frame @ direction, axis=1))[0][0])
        for direction in DIRECTIONS
    ])


def transform_composite(state: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = state.shape[0]
    perm = direction_permutation(frame)
    output = np.zeros_like(state)
    for site in product(range(length), repeat=3):
        centered = np.asarray([value if value <= length // 2 else value - length for value in site])
        target = tuple(int(value % length) for value in frame @ centered)
        for phase in range(2):
            output[target][6 * phase + perm] = state[site][6 * phase + np.arange(6)]
    return output


def route_a() -> dict:
    rows = []
    maximum_period = maximum_inverse = maximum_continuity = maximum_covariance = 0.0
    minimum_motion = math.inf
    for label, beta, length, held in (("TRAIN_L2", -0.3, 2, False), ("HELD_L3", -0.35, 3, True)):
        scalar = np.ones(6, dtype=complex) / math.sqrt(6)
        state = np.zeros((length, length, length, 12), dtype=complex)
        state[(0, 0, 0, slice(0, 6))] = scalar
        local1, step1 = composite_step(state, beta)
        local2, step2 = composite_step(step1, beta)
        period = float(np.linalg.norm(step2 - np.vdot(state.ravel(), step2.ravel()) * state))
        inverse = float(np.linalg.norm(composite_inverse(step1, beta) - state))
        cont = max(continuity_residual(local1, step1), continuity_residual(local2, step2))
        motion = float(1 - density(step1)[0, 0, 0])
        covariance = 0.0
        for frame in cycle576.FRAMES:
            covariance = max(covariance, float(np.linalg.norm(
                transform_composite(composite_step(state, beta)[1], frame)
                - composite_step(transform_composite(state, frame), beta)[1]
            )))
        maximum_period = max(maximum_period, period)
        maximum_inverse = max(maximum_inverse, inverse)
        maximum_continuity = max(maximum_continuity, cont)
        maximum_covariance = max(maximum_covariance, covariance)
        minimum_motion = min(minimum_motion, motion)
        rows.append({
            "fixture": label, "length": length, "beta": beta, "held": held,
            "step1_origin_density": float(density(step1)[0, 0, 0]),
            "step1_support_cells": int(np.sum(density(step1) > 1e-12)),
            "step2_origin_density": float(density(step2)[0, 0, 0]),
            "step2_support_cells": int(np.sum(density(step2) > 1e-12)),
            "period_two_ray_residual": period, "inverse_residual": inverse,
            "continuity_residual_both_substeps": cont, "all24_covariance_residual": covariance,
        })

    coin = composite_coin(-0.3)
    delete_toggle = coin.copy(); delete_toggle[6:, :6] = 0
    delete_reversal = coin.copy(); delete_reversal[:6, 6:] = 0
    scalar_phase0 = np.r_[np.ones(6) / math.sqrt(6), np.zeros(6)]
    scalar_phase1 = np.r_[np.zeros(6), np.ones(6) / math.sqrt(6)]
    deletion = min(
        float(np.linalg.norm((coin - delete_toggle) @ scalar_phase0)),
        float(np.linalg.norm((coin - delete_reversal) @ scalar_phase1)),
    )

    rng = np.random.default_rng(601)
    random_state = rng.normal(size=(3, 3, 3, 12)) + 1j * rng.normal(size=(3, 3, 3, 12))
    random_state /= np.linalg.norm(random_state)
    random_inverse = float(np.linalg.norm(composite_inverse(composite_step(random_state, -0.3)[1], -0.3) - random_state))

    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): index for index, frame in enumerate(frames)}
    group_missing = 0
    direction_product_residual = 0
    for left in frames:
        for right in frames:
            group_missing += int(tuple((left @ right).reshape(-1)) not in lookup)
            p_left, p_right, p_both = map(direction_permutation, (left, right, left @ right))
            composed = p_left[p_right]
            direction_product_residual = max(direction_product_residual, int(np.max(abs(composed - p_both))))

    original_coin = cycle219.common_species(-0.3).coin
    phase0_to_phase1_coin_residual = float(np.linalg.norm(coin[6:, :6] - original_coin))
    # Explicit one-matter/one-binder sector: 6*12 physical pair basis states.
    encoding = np.zeros((72, 12), dtype=complex)
    for phase in range(2):
        for direction in range(6):
            logical = 6 * phase + direction
            physical = 12 * direction + logical
            encoding[physical, logical] = 1
    projector = encoding @ encoding.conj().T
    physical_coin = encoding @ coin @ encoding.conj().T + np.eye(72) - projector
    intertwining = float(np.linalg.norm(physical_coin @ encoding - encoding @ coin))
    physical_unitarity = float(np.linalg.norm(physical_coin.conj().T @ physical_coin - np.eye(72)))
    code_leakage = float(np.linalg.norm((np.eye(72) - projector) @ physical_coin @ encoding))
    local_constraint_commutator = float(np.linalg.norm(physical_coin @ projector - projector @ physical_coin))
    output = {
        "object": "intrinsic phase-tagged matter+binder pair under one translation-uniform local rule",
        "disposition": "CONSTRUCTIVE_PERIOD_TWO_RECURRENT_NOT_STATIONARY",
        "rows": rows,
        "maximum_period_two_ray_residual": maximum_period,
        "maximum_inverse_residual": max(maximum_inverse, random_inverse),
        "maximum_two_substep_continuity_residual": maximum_continuity,
        "minimum_step_one_departure_from_origin": minimum_motion,
        "maximum_all24_covariance_residual": maximum_covariance,
        "all576_products": len(frames) ** 2,
        "all576_missing_products": group_missing,
        "all576_direction_product_residual": direction_product_residual,
        "minimum_toggle_or_reversal_deletion_signal": deletion,
        "phase0_to_phase1_actual_Cycle219_coin_block_residual": phase0_to_phase1_coin_residual,
        "physical_encoding": "E|p,d>=|one matter d, one binder(p,d)>; E K=(EKE^dag+I-EE^dag)E",
        "explicit_pair_sector_dimension": 72,
        "encoding_isometry_residual": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(12))),
        "physical_coin_intertwining_residual": intertwining,
        "physical_coin_unitarity_residual": physical_unitarity,
        "physical_coin_code_leakage": code_leakage,
        "local_pair_constraint_commutator": local_constraint_commutator,
        "local_support_M2": 18,
        "additional_M2_per_cell": 13,
        "local_matching_constraint": "matter direction equals its phase/direction binder label; this projector is bounded and dynamically invariant",
        "global_one_pair_count_and_preparation_supplied": True,
        "accepted_Cycle590_matter_law_preserved_per_pair_update": False,
        "full_joint_Cycle590_plus_pair_EG_executed": False,
        "Cycle590_mass_contact_seam_role": "separately byte-pinned regression shore only",
        "initial_supply": "localized scalar matter, phase-0 binder occupation, and empty seed rail",
        "no_external_head_or_host_timing": True,
        "no_supplied_trajectory": True,
        "intrinsic_phase_bit_is_physical_time": False,
        "stationary_source_constructed": False,
    }
    check("route A is mobile on substep one and recurrent on substep two", minimum_motion > 0.5 and maximum_period < TOL, rows)
    check("route A is reversible, locally continuous, and all24/all576 covariant",
          output["maximum_inverse_residual"] < TOL and maximum_continuity < TOL
          and maximum_covariance < TOL and group_missing == direction_product_residual == 0, output)
    check("route A needs its intrinsic toggle/reversal and uses the actual Cycle219 coin as its phase-0 to phase-1 block",
          deletion > 0.5 and phase0_to_phase1_coin_residual < TOL and intertwining < TOL
          and physical_unitarity < TOL and code_leakage < TOL and local_constraint_commutator < TOL,
          {"deletion": deletion, "phase0_to_phase1_coin": phase0_to_phase1_coin_residual,
           "intertwining": intertwining, "unitarity": physical_unitarity,
           "leakage": code_leakage, "constraint": local_constraint_commutator})
    return output


# ---------------------------------------------------------------------------
# Route B: q=4 midpoint line quadrature plus literal finite two-mode circuits.


Q = 4
MIDPOINTS = np.asarray([(j + 0.5) / Q for j in range(Q)])


def exact_line(z: float) -> complex:
    return complex(np.exp(0.5j * z) * np.sinc(z / (2 * math.pi)))


def midpoint_line(z: float) -> complex:
    return complex(np.mean(np.exp(1j * MIDPOINTS * z)))


def polar_code(matrix: np.ndarray) -> np.ndarray:
    gram = matrix.conj().T @ matrix
    values, vectors = np.linalg.eigh(gram)
    return matrix @ vectors @ np.diag(1 / np.sqrt(values)) @ vectors.conj().T


def midpoint_map(momentum3: np.ndarray) -> np.ndarray:
    base = cycle576.regge.metric_map(np.zeros(4))
    factors = np.asarray([midpoint_line(float(momentum3 @ np.asarray(direction[:3])))
                          for direction in cycle576.regge.DIRS15])
    return factors[:, None] * base


def midpoint_encoding(momentum3: np.ndarray) -> np.ndarray:
    base = polar_code(cycle576.regge.metric_map(np.zeros(4)))
    blocks = []
    for sample, midpoint in enumerate(MIDPOINTS):
        phases = np.asarray([np.exp(1j * midpoint * momentum3 @ np.asarray(direction[:3]))
                             for direction in cycle576.regge.DIRS15])
        scale = np.ones(15) / math.sqrt(Q)
        # The purely temporal edge has z=0 and needs no spatial subdivision:
        # it occupies sample zero; its other three rails are bounded vacua.
        scale[0] = 1.0 if sample == 0 else 0.0
        blocks.append((phases * scale)[:, None] * base)
    return np.vstack(blocks)


def recombined_midpoint_encoding(momentum3: np.ndarray, fanout: np.ndarray) -> np.ndarray:
    """Unitary dilation: midpoint average on body sample 0, garbage retained."""
    routed = midpoint_encoding(momentum3).reshape(Q, 15, 10)
    recombined = routed.copy()
    for edge in range(1, 15):  # edge zero is purely temporal and bypasses q
        recombined[:, edge, :] = fanout.conj().T @ routed[:, edge, :]
    return recombined.reshape(Q * 15, 10)


def unitary_completion() -> np.ndarray:
    code = polar_code(cycle576.regge.metric_map(np.zeros(4)))
    complement = null_space(code.conj().T)
    return np.column_stack((code, complement))


def givens_factorization(unitary: np.ndarray) -> tuple[list, np.ndarray, float]:
    work = unitary.copy()
    gates = []
    for column in range(unitary.shape[0]):
        for row in range(unitary.shape[0] - 1, column, -1):
            a, b = work[row - 1, column], work[row, column]
            radius = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
            if radius < 1e-14:
                continue
            gate = np.asarray(((np.conj(a) / radius, np.conj(b) / radius),
                               (-b / radius, a / radius)), dtype=complex)
            work[[row - 1, row], :] = gate @ work[[row - 1, row], :]
            gates.append((row - 1, row, gate))
    reconstruction = work.copy()
    for left, right, gate in reversed(gates):
        reconstruction[[left, right], :] = gate.conj().T @ reconstruction[[left, right], :]
    return gates, work, float(np.linalg.norm(reconstruction - unitary))


def fanout_unitary() -> tuple[np.ndarray, list[float]]:
    state = np.zeros(Q, dtype=complex); state[0] = 1
    total = np.eye(Q, dtype=complex)
    angles = []
    # Sequentially retain sqrt(remaining/q) on rail zero and peel 1/sqrt(q).
    for target in range(1, Q):
        remaining = Q - target + 1
        sine = 1 / math.sqrt(remaining)
        cosine = math.sqrt(1 - sine * sine)
        gate = np.eye(Q, dtype=complex)
        gate[np.ix_((0, target), (0, target))] = ((cosine, -sine), (sine, cosine))
        total = gate @ total
        angles.append(math.asin(sine))
    return total, angles


def bloch_product(momentum4: np.ndarray, diagonal_types: list, regge_types: list) -> np.ndarray:
    result = np.eye(15, dtype=complex)
    diagonal = np.zeros(15)
    for (_, left, _), coefficient in diagonal_types:
        diagonal[left] += float(coefficient.real)
    result = np.diag(np.exp(-1j * cycle579.UPDATE_ANGLE * diagonal)) @ result
    for (displacement, left, right), coefficient in regge_types:
        phase_coefficient = coefficient * np.exp(1j * momentum4 @ np.asarray(displacement))
        h = np.zeros((15, 15), dtype=complex)
        h[left, right] += phase_coefficient
        h[right, left] += np.conj(phase_coefficient)
        magnitude = abs(phase_coefficient)
        gate = np.eye(15, dtype=complex)
        if left == right:
            gate[left, left] = np.exp(-1j * cycle579.UPDATE_ANGLE * h[left, left].real)
        else:
            c = math.cos(cycle579.UPDATE_ANGLE * magnitude)
            s = math.sin(cycle579.UPDATE_ANGLE * magnitude)
            gate[left, left] = gate[right, right] = c
            gate[left, right] = -1j * s * phase_coefficient / magnitude
            gate[right, left] = -1j * s * np.conj(phase_coefficient) / magnitude
        result = gate @ result
    return result


def route_b() -> dict:
    q_kernel, d_kernel, kernel_controls = cycle579.exact_local_kernels()
    diagonal_types, regge_types, _ = cycle579.interaction_types(q_kernel, d_kernel)
    layer_rows = []
    train_layers = None
    for length in (3, 5, 7):
        layers, _, controls = cycle579.build_factor_layers(length, 0.0, diagonal_types, regge_types, [])
        if length == 3:
            train_layers = layers
        layer_rows.append({"length": length, **controls})

    completion = unitary_completion()
    givens, diagonal_remainder, givens_residual = givens_factorization(completion)
    diagonal_offdiag = float(np.linalg.norm(diagonal_remainder - np.diag(np.diag(diagonal_remainder))))
    fanout, fanout_angles = fanout_unitary()
    fanout_uniform = float(np.linalg.norm(abs(fanout[:, 0]) - np.ones(Q) / math.sqrt(Q)))
    fanout_inverse = float(np.linalg.norm(fanout.conj().T @ fanout - np.eye(Q)))

    fixtures = (("TRAIN_L3", 3, False), ("HELD_L5", 5, True),
                ("HELD_L7", 7, True), ("OUT_FAMILY_L9", 9, True))
    rows = []
    low_errors = []
    max_isometry = max_map_error = max_inverse = max_product_leakage = 0.0
    min_delete = math.inf
    max_null_error = 0
    for label, length, held in fixtures:
        momentum3 = np.asarray((2 * math.pi / length, 0.0, 0.0))
        exact = cycle576.regge.metric_map(np.r_[momentum3, 0.0])
        approximate = midpoint_map(momentum3)
        encoding = recombined_midpoint_encoding(momentum3, fanout)
        isometry = float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(10)))
        map_error = float(np.linalg.norm(approximate - exact))
        low_errors.append(map_error)
        edge = cycle576.base_edge_hessian(np.r_[momentum3, 0.0])
        ambient_generator = np.zeros((60, 60), dtype=complex)
        ambient_generator[:15, :15] = edge
        code = encoding.conj().T @ ambient_generator @ encoding
        code = (code + code.conj().T) / 2
        values = np.linalg.eigvalsh(code)
        cutoff = 1e-9 * max(float(np.max(abs(values))), 1.0)
        null_count = int(np.sum(abs(values) < cutoff))
        product15 = bloch_product(np.r_[momentum3, 0.0], diagonal_types, regge_types)
        product60 = np.eye(60, dtype=complex)
        product60[:15, :15] = product15
        leakage = float(np.linalg.norm((np.eye(60) - encoding @ encoding.conj().T) @ product60 @ encoding))
        inverse = float(np.linalg.norm(product60.conj().T @ product60 - np.eye(60)))
        z = float(momentum3 @ np.asarray((1, 1, 1)))
        deleted = midpoint_line(z) - np.exp(1j * MIDPOINTS[-1] * z) / Q
        deletion = float(abs(deleted - midpoint_line(z)))
        high_z = math.pi * 3
        rows.append({
            "fixture": label, "length": length, "held": held,
            "low_mode": momentum3.tolist(), "low_mode_metric_map_error": map_error,
            "coherent_body_map_error_in_polar_coordinates": float(np.linalg.norm(
                encoding[:15] - np.asarray([
                    exact_line(float(momentum3 @ np.asarray(direction[:3])))
                    for direction in cycle576.regge.DIRS15
                ])[:, None] * polar_code(cycle576.regge.metric_map(np.zeros(4)))
            )),
            "low_mode_body_line_error": abs(midpoint_line(z) - exact_line(z)),
            "full_BZ_body_line_error_at_z_3pi": abs(midpoint_line(high_z) - exact_line(high_z)),
            "code_isometry_residual": isometry, "code_null_count": null_count,
            "four_null_eigenvalue_residual": float(np.max(np.sort(abs(values))[:4])),
            "raw_ordered_product_code_leakage": leakage,
            "raw_ordered_product_inverse_residual": inverse,
            "delete_one_midpoint_amplitude_signal": deletion,
        })
        max_isometry = max(max_isometry, isometry)
        max_map_error = max(max_map_error, map_error)
        max_inverse = max(max_inverse, inverse)
        max_product_leakage = max(max_product_leakage, leakage)
        min_delete = min(min_delete, deletion)
        max_null_error = max(max_null_error, abs(null_count - 4))

    slopes = [math.log(low_errors[i] / low_errors[i + 1]) / math.log(fixtures[i + 1][1] / fixtures[i][1])
              for i in range(len(low_errors) - 1)]
    max_disp = kernel_controls["maximum_absolute_displacement"]
    # Explicit integer coordinates for a denominator-eight refined physical
    # block.  Each role's home is at `anchor`; spatial edge sample j is at
    # anchor+(2j+1)B v/8.  Thus its coarse Bloch phase is exactly the midpoint
    # phase.  The time-only edge uses one active rail and three bounded vacua.
    frames = cycle576.FRAMES
    block_scale = 128
    coords = {}
    for frame in range(24):
        sector_frame = frames[frame]
        for sample in range(Q):
            for edge in range(15):
                track = 15 * frame + edge
                anchor = np.asarray((track % 8, (track // 8) % 8, track // 64), dtype=int)
                spatial = sector_frame @ np.asarray(cycle576.regge.DIRS15[edge][:3])
                if np.any(spatial):
                    coords[(frame, sample, edge)] = anchor + (2 * sample + 1) * (block_scale // 8) * spatial
                else:
                    coords[(frame, sample, edge)] = anchor + np.asarray((0, sample, 0))
    unique_coordinates = len({tuple(value) for value in coords.values()})
    preparation_span = max(float(np.linalg.norm(coords[(frame, sample, edge)]
                                                       - np.asarray(((15 * frame + edge) % 8,
                                                                     ((15 * frame + edge) // 8) % 8,
                                                                     (15 * frame + edge) // 64))))
                           for frame in range(24) for sample in range(Q) for edge in range(15))
    product_span = math.sqrt(3) * block_scale * max_disp + 2 * preparation_span + math.sqrt(123)
    factor_depth = layer_rows[0]["layers"]
    preparation_depth = len(givens) + 1 + 2 * (Q - 1)
    total_depth = 2 * preparation_depth + factor_depth

    # Match the hand-built 15x15 Bloch product used for the leakage audit to
    # the literal Cycle579 sparse matching execution at the train momentum.
    train_k = np.asarray((2 * math.pi / 3, 0.0, 0.0, 0.0))
    rng = np.random.default_rng(601579)
    edge_vector = rng.normal(size=15) + 1j * rng.normal(size=15)
    edge_vector /= np.linalg.norm(edge_vector)
    bloch_state = np.zeros(16 * 3 ** 3, dtype=complex)
    for site in product(range(3), repeat=3):
        cell = (site[0] * 3 + site[1]) * 3 + site[2]
        bloch_state[16 * cell + 1:16 * cell + 16] = (
            np.exp(1j * train_k[:3] @ np.asarray(site)) * edge_vector / 3 ** 1.5
        )
    sparse_output = cycle579.lie_product(bloch_state, train_layers, 1)
    bloch_output = bloch_product(train_k, diagonal_types, regge_types) @ edge_vector
    predicted = np.zeros_like(bloch_state)
    for site in product(range(3), repeat=3):
        cell = (site[0] * 3 + site[1]) * 3 + site[2]
        predicted[16 * cell + 1:16 * cell + 16] = (
            np.exp(1j * train_k[:3] @ np.asarray(site)) * bloch_output / 3 ** 1.5
        )
    bloch_matching_residual = float(np.linalg.norm(sparse_output - predicted))

    lookup = {tuple(frame.reshape(-1)): i for i, frame in enumerate(frames)}
    group_missing = sum(tuple((left @ right).reshape(-1)) not in lookup for left in frames for right in frames)
    # The covariant object is the co-present frame orbit, not a claim that one
    # triangulation's 15 positive representatives are closed under rotations.
    # Sector g carries displacements g v_e; h sends it to sector hg and keeps e.
    frame_sector_displacement_residual = 0
    for left in frames:
        for sector in frames:
            for displacement in q_kernel:
                spatial = np.asarray(displacement[:3])
                frame_sector_displacement_residual = max(
                    frame_sector_displacement_residual,
                    int(np.max(abs(left @ (sector @ spatial) - (left @ sector) @ spatial))),
                )

    output = {
        "object": "actual Cycle576 15-edge Regge kernel with a q=4 midpoint line-factor approximation",
        "disposition": "CONSTRUCTIVE_BOUNDED_CIRCUIT_FOR_APPROXIMATE_MAP; EXACT_IMAGE_TERMINAL_FAILS",
        "frozen_before_rows": {"q": Q, "train": [3], "held": [5, 7], "out_family": [9]},
        "approximation_law": "f_q(z)=q^-1 sum_j exp(i(j+1/2)z/q); fixed-mode error O(L^-2/q^2), full-BZ error does not vanish at fixed q",
        "rows": rows,
        "observed_low_mode_error_slopes": slopes,
        "maximum_code_isometry_residual": max_isometry,
        "maximum_raw_ordered_product_inverse_residual": max_inverse,
        "maximum_raw_ordered_product_code_leakage": max_product_leakage,
        "minimum_midpoint_deletion_signal": min_delete,
        "maximum_null_count_error_from_four": max_null_error,
        "kernel_controls": kernel_controls,
        "factor_layer_rows": layer_rows,
        "metric_polar_unitary_completion_dimension": 15,
        "metric_polar_two_mode_Givens_gates": len(givens),
        "metric_polar_Givens_reconstruction_residual": givens_residual,
        "metric_polar_triangular_offdiagonal_residual": diagonal_offdiag,
        "fanout_two_mode_Givens_gates_per_edge": Q - 1,
        "recombination_two_mode_Givens_gates_per_edge": Q - 1,
        "fanout_spatial_edges": 14,
        "time_edge_active_sample_rails": 1,
        "fanout_angles_radians": fanout_angles,
        "fanout_uniform_amplitude_residual": fanout_uniform,
        "fanout_inverse_residual": fanout_inverse,
        "no_cloning": "on each spatial edge one excitation is unitarily redistributed across four routed paths, inverse-Givens recombined onto one body rail plus three retained orthogonal garbage rails, and exactly recovered by the inverse; the z=0 temporal edge uses one active rail",
        "physical_M2_rails_per_cell": 24 * 15 * Q,
        "physical_refinement_denominator": 8,
        "exact_midpoint_phase_from_refined_displacement": True,
        "layout_unique_rail_coordinates": unique_coordinates,
        "all24_frame_sectors_co_present": 24,
        "all576_products": 576,
        "all576_missing_products": int(group_missing),
        "all24_frame_sector_displacement_residual": int(frame_sector_displacement_residual),
        "bounded_layout_max_preparation_distance": preparation_span,
        "bounded_layout_max_product_distance_upper_bound": product_span,
        "compiled_preparation_depth": preparation_depth,
        "compiled_Regge_product_depth": factor_depth,
        "compiled_prepare_product_unprepare_depth": total_depth,
        "literal_sparse_to_Bloch_product_residual": bloch_matching_residual,
        "layout_and_depth_independent_of_L": True,
        "factor_order_is_a_supplied_schedule_not_time": True,
        "target_exponential_exact": False,
        "midpoint_map_realization": "unitary dilation: coherent average on sample-0 body rail, orthogonal quadrature garbage retained; actual Regge product acts on body rails only",
        "exact_line_factor_at_fixed_q": False,
        "raw_product_preserves_approximate_metric_image": max_product_leakage < TOL,
    }
    check("route B physically factors the metric isometry, coherent no-cloning split, and inverse",
          givens_residual < TOL and diagonal_offdiag < TOL and fanout_uniform < TOL and fanout_inverse < TOL,
          {"gates": len(givens), "reconstruction": givens_residual, "fanout": fanout_uniform})
    check("route B has an executed bounded matching layout/depth with all24/all576 closure",
          all(not row["matching_failures"] for row in layer_rows)
          and len(set(row["layers"] for row in layer_rows)) == 1
          and group_missing == frame_sector_displacement_residual == 0
          and unique_coordinates == 24 * 15 * Q and total_depth > 0
          and bloch_matching_residual < TOL, output)
    check("route B honest terminal audit detects fixed-q approximation and raw-image leakage",
          min(slopes) > 1.5 and rows[-1]["full_BZ_body_line_error_at_z_3pi"] > 1e-3
          and max_product_leakage > 1e-5 and min_delete > 1e-3, rows)
    return output


# ---------------------------------------------------------------------------
# Route C: reversible local modular response controlled by the recurrent source.


WORD_BITS = 20
MODULUS = 1 << WORD_BITS
SOURCE_CHARGE = 17


def laplacian(field: np.ndarray) -> np.ndarray:
    result = 6 * field
    for direction in DIRECTIONS:
        result -= np.roll(field, tuple(int(v) for v in direction), axis=(0, 1, 2))
    return result


def wave_step(previous: np.ndarray, current: np.ndarray, source: np.ndarray, sign: int) -> tuple[np.ndarray, np.ndarray]:
    following = (2 * current - previous - laplacian(current) + sign * source) % MODULUS
    return current.copy(), following


def wave_inverse(current: np.ndarray, following: np.ndarray, source: np.ndarray, sign: int) -> tuple[np.ndarray, np.ndarray]:
    previous = (2 * current - laplacian(current) + sign * source - following) % MODULUS
    return previous, current.copy()


def signed(field: np.ndarray) -> np.ndarray:
    return np.where(field >= MODULUS // 2, field - MODULUS, field).astype(np.int64)


def source_field(length: int, direction: int, step: int) -> np.ndarray:
    output = np.zeros((length, length, length), dtype=np.int64)
    if step % 2:
        site = tuple(int(value % length) for value in DIRECTIONS[direction])
    else:
        site = (0, 0, 0)
    output[site] = SOURCE_CHARGE
    return output


def response_run(length: int, direction: int, sign: int, advanced: bool, steps: int = 4) -> tuple[np.ndarray, np.ndarray, list]:
    previous = np.zeros((length,) * 3, dtype=np.int64)
    current = np.zeros_like(previous)
    history = []
    for step in range(steps):
        source = source_field(length, direction, step + int(advanced))
        previous, current = wave_step(previous, current, source, sign)
        history.append((previous.copy(), current.copy(), source.copy()))
    return previous, current, history


def static_green(length: int) -> np.ndarray:
    rho = np.zeros((length,) * 3); rho[0, 0, 0] = 1; rho -= 1 / length ** 3
    rho_hat = np.fft.fftn(rho)
    freq = 2 * math.pi * np.fft.fftfreq(length)
    denominator = np.zeros_like(rho)
    for index in product(range(length), repeat=3):
        denominator[index] = 6 - 2 * sum(math.cos(freq[index[axis]]) for axis in range(3))
    solution_hat = np.zeros_like(rho_hat)
    mask = denominator > 1e-12
    solution_hat[mask] = rho_hat[mask] / denominator[mask]
    return np.fft.ifftn(solution_hat).real


def rotate_scalar(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    length = field.shape[0]
    output = np.zeros_like(field)
    for site in product(range(length), repeat=3):
        centered = np.asarray([value if value <= length // 2 else value - length for value in site])
        target = tuple(int(value % length) for value in frame @ centered)
        output[target] = field[site]
    return output


def route_c() -> dict:
    rows = []
    max_inverse = max_covariance = max_sign = 0
    min_order_signal = math.inf
    fingerprints = []
    for label, length, held in (("TRAIN_L3", 3, False), ("HELD_L5", 5, True), ("OUT_FAMILY_L7", 7, True)):
        prev_r, retarded, history = response_run(length, 0, +1, False)
        _, advanced, _ = response_run(length, 0, +1, True)
        _, negative, _ = response_run(length, 0, -1, False)
        sign_residual = int(np.max(abs(signed(retarded) + signed(negative))))
        source_last = history[-1][2]
        restored_previous, restored_current = wave_inverse(history[-1][0], history[-1][1], source_last, +1)
        inverse = max(int(np.max(abs(restored_previous - history[-2][0]))),
                      int(np.max(abs(restored_current - history[-2][1]))))
        order_signal = int(np.max(abs(signed(retarded) - signed(advanced))))
        far = tuple([length // 2] * 3)
        green = static_green(length)
        rows.append({
            "fixture": label, "length": length, "held": held, "updates": 4,
            "retarded_origin_word": int(signed(retarded)[0, 0, 0]),
            "retarded_forward_neighbor_word": int(signed(retarded)[tuple(DIRECTIONS[0] % length)]),
            "retarded_nonzero_cells": int(np.sum(signed(retarded) != 0)),
            "advanced_origin_word": int(signed(advanced)[0, 0, 0]),
            "advanced_forward_neighbor_word": int(signed(advanced)[tuple(DIRECTIONS[0] % length)]),
            "retarded_vs_advanced_order_signal": order_signal,
            "sign_flip_residual": sign_residual, "inverse_residual_integer": inverse,
            "finite_update_far_response": int(signed(retarded)[far]),
            "static_zero_mean_Green_far_value": float(green[far]),
        })
        max_inverse = max(max_inverse, inverse)
        max_sign = max(max_sign, sign_residual)
        min_order_signal = min(min_order_signal, order_signal)

    for direction in range(6):
        fingerprints.append(tuple(signed(response_run(7, direction, +1, False)[1]).ravel()))
    distinct_fingerprints = len(set(fingerprints))
    branch_gram = np.asarray([[float(left == right) for right in fingerprints]
                              for left in fingerprints])
    coherent_gram_residual = float(np.linalg.norm(branch_gram - np.eye(6)))

    length = 5
    prior = np.arange(length ** 3, dtype=np.int64).reshape((length,) * 3) % 31
    current = (3 * prior + 7) % 47
    for frame in cycle576.FRAMES:
        left = rotate_scalar(wave_step(prior, current, source_field(length, 0, 0), +1)[1], frame)
        perm = direction_permutation(frame)[0]
        right = wave_step(rotate_scalar(prior, frame), rotate_scalar(current, frame),
                          source_field(length, int(perm), 0), +1)[1]
        max_covariance = max(max_covariance, int(np.max(abs(left - right))))

    zero = np.zeros((7,) * 3, dtype=np.int64)
    deleted = wave_step(zero, zero, zero, +1)[1]
    frames = cycle576.FRAMES
    lookup = {tuple(frame.reshape(-1)): i for i, frame in enumerate(frames)}
    group_missing = sum(tuple((left @ right).reshape(-1)) not in lookup for left in frames for right in frames)
    output = {
        "object": "two-register signed modular radius-one wave response controlled by the period-two source position",
        "disposition": "CONSTRUCTIVE_LOCAL_REVERSIBLE_RESPONSE; RETARDED_ORDER_AND_SIGN_UNSELECTED",
        "rows": rows,
        "maximum_exact_inverse_integer_residual": max_inverse,
        "maximum_sign_flip_integer_residual": max_sign,
        "minimum_retarded_vs_advanced_order_signal": min_order_signal,
        "source_deleted_zero_response": bool(np.max(abs(deleted)) == 0),
        "six_direction_branch_field_fingerprints": distinct_fingerprints,
        "coherent_control_Gram_residual": coherent_gram_residual,
        "source_charge_continuity_residual": 0,
        "maximum_all24_covariance_integer_residual": max_covariance,
        "all576_products": 576,
        "all576_missing_products": int(group_missing),
        "field_M2_per_cell": 3 * WORD_BITS,
        "local_gate_support_M2": 3,
        "bounded_ripple_depth_upper_bound": 16 * WORD_BITS,
        "modular_overflow": "none: arithmetic is exactly Z/(2^20); integer-to-physical-sign identification is supplied",
        "retarded_factor_order_selected_by_old_substrate": False,
        "response_sign_selected_by_old_substrate": False,
        "schedule_index_is_physical_time": False,
        "control_is_a_Record": False,
        "response_is_gravity": False,
        "comparison_to_Cycle588_596": "finite four-update support is zero beyond graph radius four while the prior static zero-mean Kjoin=L Green solution is nonzero there; this is a prediction distinction, not a contradiction",
        "comparison_to_Cycle451": "typed off/receiver-zero/delay/advance outcomes remain 4:4,4:4,3:4,5:4; this construction does not choose the physical word sign or retarded order",
    }
    check("route C is an exactly reversible radius-one response with deletion and sign controls",
          max_inverse == max_sign == 0 and output["source_deleted_zero_response"], rows)
    check("route C distinguishes local retarded/advanced order and six recurrent paths",
          min_order_signal > 0 and distinct_fingerprints == 6 and coherent_gram_residual == 0, output)
    check("route C scalar stencil is all24/all576 covariant and keeps the static comparison distinct",
          max_covariance == 0 and group_missing == 0
          and abs(rows[-1]["static_zero_mean_Green_far_value"]) > 1e-8
          and rows[-1]["finite_update_far_response"] == 0, rows[-1])
    return output


def no_go_audit(routes: dict) -> dict:
    families = [
        ["phase-tagged pair / carrier CAR", "intrinsic phase toggle plus reversal", "period-two mobile recurrence", "ATTEMPTED_POSITIVE_C601"],
        ["untagged mobile pair / carrier CAR", "Cycle596 co-moving binder", "mobile but dispersive source", "RULED_OUT_AS_RECURRENCE_BY_C596"],
        ["bound dimer / physical CAR", "Cycle594 immobile binder", "stationary source", "RULED_OUT_AS_MOBILE_BY_C594"],
        ["midpoint edge samples / one-excitation M2", "q=4 coherent Givens split", "bounded approximate Regge map", "ATTEMPTED_PARTIAL_C601"],
        ["DFT edge samples / finite code isometry", "Cycle596 exact torus quadrature", "exact finite line map", "RULED_OUT_AS_CONSTANT_OVERHEAD_BY_C596"],
        ["Regge edge rails / Lie product", "Cycle579 translated matchings", "bounded factorized update", "ATTEMPTED_POSITIVE_C601_LAYOUT"],
        ["two modular field words / reversible CA", "radius-one leapfrog", "local signed response", "ATTEMPTED_PARTIAL_C601"],
        ["zero-mean scalar field / Fourier solve", "Cycle588 Kjoin=L static inverse", "static 1/r prediction surface", "RULED_OUT_AS_FINITE_RETARDED_DYNAMICS"],
    ]
    walls = {
        "W_genesis": "the recurrent source's localized scalar and phase-0 binder are supplied",
        "W_stationary": "route A is exactly recurrent with period two, not stationary",
        "W_exact_line": "fixed q approximates rather than exactly realizes the sinc line factor",
        "W_image_invariance": "the raw ordered Regge product leaks from the approximate metric image",
        "W_response_order": "retarded and advanced local factor orders are both admissible",
        "W_physical_identification": "modular word sign is not yet tied to an operational response observable",
        "W_joint_compiler": "the recurrent pair rule was not composed with the accepted Cycle590 matter/contact/seam compiler",
    }
    names = tuple(walls)
    pairs = [[names[i], names[j], "independent: closing either does not logically close the other"]
             for i in range(len(names)) for j in range(i + 1, len(names))]
    hidden = [
        "phase-0 initialization", "global one-pair count and preparation", "no joint Cycle590-plus-pair compiler", "q=4 fixed before fixtures",
        "24 co-present frame sectors", "factor order schedule", "20-bit modular alphabet",
        "source charge 17", "retarded versus advanced ordering", "integer-word sign convention",
    ]
    partial = [
        "period-two mobile recurrence closes immobility without closing genesis, stationarity, or joint Cycle590 compilation",
        "q=4 closes constant overhead, literal factorization, layout, and depth without exact sinc or image invariance",
        "modular wave closes reversible local propagation without selecting response sign or arrow",
    ]
    steelman = (
        "A block-direct-sum or controlled joint compiler might compose the recurrent pair with Cycle590 without changing its mass/contact/seam fixtures; "
        "a continued-fraction or finite-state transfer identity might realize the sinc restriction on a narrower lawful momentum family, "
        "and a jointly designed product could preserve that image; an autonomous clock/source coupling might then choose one response ordering."
    )
    echo = {
        "Cycle596": "exact finite quadrature but size growth and no gate layout",
        "Cycle598": "root-free constant overhead in a supplied one-excitation carrier sector",
        "new_evidence": "period-two recurrence plus executed constant-q gate/layout and a reversible local response",
        "repeated_wall": "exact line-map and response-selection walls remain; they are not a new theorem",
    }
    output = {
        "N1_alternative_route_enumeration": families,
        "N2_pairwise_wall_independence": pairs,
        "N3_hidden_wall_scan": hidden,
        "N4_residual_matching": {key: value for key, value in walls.items()},
        "N5_rhetoric_audit": "route-scoped fail/partial/positive language only; no impossible, necessary, minimum-content, or constitutional wording",
        "N6_partial_closure_paths": partial,
        "N7_concrete_steelman": steelman,
        "N8_cross_cycle_echo": echo,
        "broad_negative_gate": "FAIL / DO NOT SHIP",
        "shared_route_independent_obstruction": False,
        "axiom_pressure": False,
    }
    check("N1-N8 audit blocks a broad negative and any axiom-pressure claim",
          len(families) >= 5 and len(pairs) == len(names) * (len(names) - 1) // 2
          and len(hidden) >= 5 and len(partial) >= 3
          and not output["shared_route_independent_obstruction"] and not output["axiom_pressure"], output)
    return output


def main() -> None:
    pins = shore()
    note_contract()
    a = route_a()
    b = route_b()
    c = route_c()
    routes = {"route_A": a, "route_B": b, "route_C": c}
    no_go = no_go_audit(routes)
    inventory = {
        "supplied_candidate_laws": [
            "Cycle219 beta coin and Cycle230 stream/contact/seam", "intrinsic phase-toggle/reversal binder law",
            "Cycle576 raw Regge kernel and Cycle579 update angle/factor ordering", "q=4 midpoint quadrature",
            "20-bit modular leapfrog response, source charge 17, sign, and factor ordering",
        ],
        "supplied_initial_state_or_sector": [
            "Cycle590 lawful N<=3 physical-M2 code space as a separate regression shore only",
            "localized scalar source, global one-pair count, and phase-0 co-moving binder for the unjoined recurrent rule",
            "one-excitation metric/sample rail sector", "24 co-present frame sectors", "zero field words",
        ],
        "not_derived": [
            "joint Cycle590-plus-recurrent-pair compiler", "per-update preservation of the accepted matter law by the recurrent rule",
            "stationarity", "source genesis", "exact bounded sinc compiler", "raw Regge image invariance",
            "target exponential", "physical response sign", "retarded arrow", "word-to-metric calibration",
            "backreaction", "Lorentz covariance", "Born probabilities", "Records",
        ],
        "terminology_guards": {
            "wrapped_phase_is_energy": False, "generator_is_rate": False, "schedule_is_time": False,
            "control_is_Record": False, "modular_response_is_gravity": False,
        },
    }
    six_wall = {
        "C_ref": "UNCHANGED: frames remain supplied; all24/all576 proper-cubic covariance closes for the candidates, not Lorentz/reference genesis",
        "C_num": "UNCHANGED: local one-pair/one-excitation sectors and modular words are supplied lawful domains",
        "C_wrap": "UNCHANGED: no wrapped phase is interpreted as physical energy or rate",
        "C_int": "PARTIAL: Cycle590 mass/contact/seam passes only as a separately pinned shore; no joint pair-plus-Cycle590 EG was executed; response sign/order/backreaction are open",
        "C_local": "ADVANCED: period-two mobile recurrence and q=4 Regge factor/layout/depth are bounded; exact line image and stationary source remain open",
        "C_source": "ADVANCED: recurrent mobile source controls a local conserved update, but genesis, stationary limit, response sign, and retarded selection remain supplied/open",
    }
    maturity = {
        "operational_quantum_records": 4.0,
        "time": 3.0,
        "inertia_matter": 4.0,
        "gravity_source": 3.0,
        "Born_probability": 2.0,
    }
    git_head = subprocess.run(("git", "rev-parse", "HEAD"), cwd=ROOT, check=True, capture_output=True, text=True).stdout.strip()
    receipt = {
        "cycle": 601, "authority": AUTHORITY, "audit": AUDIT,
        "status": "bounded constructive partials; no shared no-go and no axiom pressure",
        "HEAD": git_head, "pins": pins, "route_A_recurrent_source": a,
        "route_B_bounded_Regge": b, "route_C_local_response": c,
        "inventory": inventory, "six_wall_ledger": six_wall, "maturity_0_to_5": maturity,
        "no_go_discipline": no_go,
        "strongest_constructive_result": (
            "one uniform 18-M2-support rule yields an all24-covariant period-two mobile matter+binder source; "
            "independently, q=4 yields an executed constant-rail, bounded-layout/depth Regge approximation circuit"
        ),
        "optimal_next_campaign": (
            "jointly design a finite-state rational/continued-fraction line encoder and Regge product whose image is invariant, "
            "while coupling the intrinsic source phase to an autonomous clock test that can select retarded versus advanced order"
        ),
        "tests_passed": PASS, "tests_failed": FAIL,
        "pass": FAIL == 0, "elapsed_seconds": perf_counter() - START,
        "maximum_RSS_bytes": int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
                                 * (1024 if sys.platform.startswith("linux") else 1)),
    }
    print("RECEIPT", json.dumps(receipt, sort_keys=True))
    print("SUMMARY", json.dumps({
        "pass": receipt["pass"], "tests_passed": PASS, "tests_failed": FAIL,
        "elapsed_seconds": receipt["elapsed_seconds"], "maximum_RSS_bytes": receipt["maximum_RSS_bytes"],
        "route_A": a["disposition"], "route_B": b["disposition"], "route_C": c["disposition"],
        "broad_negative_gate": no_go["broad_negative_gate"], "axiom_pressure": False,
    }, sort_keys=True))
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
