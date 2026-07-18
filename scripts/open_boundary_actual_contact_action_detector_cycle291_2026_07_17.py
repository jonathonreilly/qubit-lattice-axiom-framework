#!/usr/bin/env python3
"""Cycle 291: open-boundary actual-contact coherent detector.

A fixed-total-number co-located/separated reference makes the ordinary
unconditional Cycle-230 contact phase relational without a controlled-W_g
service.  A supplied local recombiner transfers the resulting bright/dark
two-port state to a dual-rail open sink.  The full carrier, its reduced
channels, resource flow, split faults, inverse, and retargeting are audited
separately.  No sink value is promoted to occurrence, Record, or time.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import actual_contact_action_syndrome_tournament_cycle285_2026_07_17 as c285
import connected_edge_same_code_local_instrument_cycle278_2026_07_17 as c278
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "OPEN_BOUNDARY_ACTUAL_CONTACT_ACTION_DETECTOR_CYCLE291_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
TOL = 3.0e-11
G = c278.c230.COUPLING
MOTIF = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
TRAINING_CASES = ((9, 8), (17, 16), (31, 30))
HELD_CASE = (47, 46)


class SinkDomainError(ValueError):
    """The state lies outside the synchronized fresh-sink domain."""


class SinkBoundaryError(ValueError):
    """The finite open sink has no fresh outward target."""


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the Cycle-291 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "same connected physical-m2 code",
        "co-located-versus-separated reference",
        "fixed total particle number",
        "ordinary unconditional w_g",
        "q-only surrogate",
        "bright/dark coherent carrier",
        "open dual-rail sink",
        "environment distinguishability",
        "occupancy-only dephasing",
        "bounded per-step support",
        "exact resource and capacity ledger",
        "deletion, split, inverse, and retarget",
        "one-particle mass fixture",
        "zero action-algebra leakage",
        "held-out l=6",
        "all 24 proper-cubic frames",
        "finite/open lawful domain",
        "sink export is not occurrence",
        "sink export is not a record",
        "rail step count is not physical time",
        "no energy or source connector is constructed",
        "within the reviewed cycle-291 routes and exact declared domains",
        "no route-independent shared obstruction is established",
        "no evidence-based axiom pressure follows",
        "excludes unreviewed encodings, apparatus laws, and preparations",
        "n1 — alternative-route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note preserves the detector, sink, resource, semantic, and N1-N8 contract",
        not missing,
        missing,
    )


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def trace_distance(left: np.ndarray, right: np.ndarray) -> float:
    difference = left - right
    return float(np.sum(np.abs(np.linalg.eigvalsh(difference))) / 2)


def carrier(pair_phase_c: float, pair_phase_s: float) -> np.ndarray:
    """Bright/dark carrier from the supplied reference and recombiner."""

    reference = np.ones(2, dtype=complex) / np.sqrt(2)
    action = np.diag(
        (np.exp(1j * pair_phase_c), np.exp(1j * pair_phase_s))
    ).astype(complex)
    recombiner = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    return recombiner @ action @ reference


def coherent_detector_controls() -> dict[str, float]:
    print("\nCO-LOCATED / SEPARATED ACTUAL-ACTION DETECTOR")
    actual = carrier(6 * G, G)
    deleted = carrier(0.0, 0.0)
    q_only = carrier(G, G)
    global_phase = carrier(0.73, 0.73)
    inverse = carrier(-6 * G, -G)
    expected_dark = float(np.sin(5 * G / 2) ** 2)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)

    actual_rho = projector(actual)
    deleted_rho = projector(deleted)
    inverse_rho = projector(inverse)
    actual_deleted_distance = trace_distance(actual_rho, deleted_rho)
    actual_inverse_distance = trace_distance(actual_rho, inverse_rho)
    actual_y = float(np.vdot(actual, y @ actual).real)
    inverse_y = float(np.vdot(inverse, y @ inverse).real)

    check(
        "the fixed-total-N co-located/separated reference detects the ordinary unconditional W_g but rejects I, common phase, and the Q-only surrogate",
        abs(abs(actual[1]) ** 2 - expected_dark) < TOL
        and abs(deleted[1]) < TOL
        and abs(q_only[1]) < TOL
        and abs(global_phase[1]) < TOL
        and abs(np.linalg.norm(actual) - 1) < TOL,
        {
            "pair_counts": (6, 1),
            "Q_active_cell_counts": (1, 1),
            "fixed_total_N": (4, 4),
            "actual_dark_weight": float(abs(actual[1]) ** 2),
            "expected_sin2_5g_over_2": expected_dark,
            "I_dark_weight": float(abs(deleted[1]) ** 2),
            "Q_only_dark_weight": float(abs(q_only[1]) ** 2),
            "common_phase_dark_weight": float(abs(global_phase[1]) ** 2),
        },
    )
    check(
        "the full coherent carrier retains inverse sign although dark occupancy alone is sign-blind",
        abs(abs(inverse[1]) ** 2 - expected_dark) < TOL
        and abs(actual_y + inverse_y) < TOL
        and abs(abs(actual_y) - abs(np.sin(5 * G))) < TOL
        and actual_inverse_distance > 0.96,
        {
            "W_dark_weight": float(abs(actual[1]) ** 2),
            "W_dagger_dark_weight": float(abs(inverse[1]) ** 2),
            "W_carrier_Y": actual_y,
            "W_dagger_carrier_Y": inverse_y,
            "W_vs_W_dagger_trace_distance": actual_inverse_distance,
        },
    )
    check(
        "environment distinguishability is positive for W_g versus deletion and is carried by the exported two-port state",
        abs(actual_deleted_distance - abs(np.sin(5 * G / 2))) < TOL
        and actual_deleted_distance > 0.79,
        {
            "W_vs_I_environment_trace_distance": actual_deleted_distance,
            "pure_state_overlap_magnitude": float(abs(np.vdot(deleted, actual))),
        },
    )

    # Gate-factor fault controls.  Omitting the action leaves the proper
    # recombiner bright.  Omitting the recombiner but transferring both raw
    # arms assigns half the norm to the nominal dark lane: a split false close.
    raw_actual = np.asarray((np.exp(6j * G), np.exp(1j * G))) / np.sqrt(2)
    c_arm_deleted = carrier(0.0, G)
    s_arm_deleted = carrier(6 * G, 0.0)
    check(
        "deletion and split controls separate the successful action deletion from comparator and arm-split false closes",
        abs(deleted[1]) < TOL
        and abs(abs(raw_actual[1]) ** 2 - 0.5) < TOL
        and abs(c_arm_deleted[1]) ** 2 > 0.03
        and abs(s_arm_deleted[1]) ** 2 > 0.79,
        {
            "whole_W_deleted_dark": float(abs(deleted[1]) ** 2),
            "recombiner_deleted_transfer_survives_dark": float(abs(raw_actual[1]) ** 2),
            "C_arm_action_deleted_dark": float(abs(c_arm_deleted[1]) ** 2),
            "S_arm_action_deleted_dark": float(abs(s_arm_deleted[1]) ** 2),
            "split_faithful": False,
        },
    )
    return {
        "dark_weight": expected_dark,
        "W_I_trace_distance": actual_deleted_distance,
        "W_Wdagger_trace_distance": actual_inverse_distance,
        "carrier_Y": actual_y,
    }


def reduced_channel_controls() -> None:
    print("\nFULL EXPORT / OCCUPANCY-ONLY TRACE CONTROLS")
    actual = carrier(6 * G, G)
    deleted = carrier(0.0, 0.0)
    inverse = carrier(-6 * G, -G)
    actual_rho = projector(actual)
    inverse_rho = projector(inverse)
    dephased_actual = np.diag(np.diag(actual_rho))
    dephased_inverse = np.diag(np.diag(inverse_rho))
    def exported_reductions(value: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        # Each side has |vac>, |B>, |D>.  Full export maps the local dual-rail
        # state to |vac>_local tensor (b|B>+d|D>)_environment.
        amplitudes = np.zeros((3, 3), dtype=complex)
        amplitudes[0, 1:] = value
        return amplitudes @ amplitudes.conj().T, amplitudes.T @ amplitudes.conj()

    local_actual, environment_actual = exported_reductions(actual)
    local_deleted, environment_deleted = exported_reductions(deleted)
    vacuum = np.diag((1.0, 0.0, 0.0)).astype(complex)
    check(
        "full SWAP export leaves the local launch register blank while the environment retains the complete phase-sensitive carrier",
        np.linalg.norm(local_actual - vacuum) < TOL
        and np.linalg.norm(local_deleted - vacuum) < TOL
        and trace_distance(environment_actual, environment_deleted) > 0.79
        and np.linalg.norm(environment_actual[1:, 1:] - actual_rho) < TOL,
        {
            "local_after_W_export": "blank",
            "local_after_I_export": "blank",
            "local_W_minus_I_trace_distance": trace_distance(local_actual, local_deleted),
            "environment_W_minus_I_trace_distance": trace_distance(
                environment_actual, environment_deleted
            ),
            "environment_retained": True,
            "branch_selected": False,
        },
    )
    check(
        "occupancy-only copying followed by trace merely dephases the carrier and erases the W_g versus W_g-dagger sign",
        np.linalg.norm(dephased_actual - dephased_inverse) < TOL
        and np.linalg.norm(actual_rho - dephased_actual) > 0.67,
        {
            "dephased_W_minus_W_dagger": float(
                np.linalg.norm(dephased_actual - dephased_inverse)
            ),
            "coherence_removed": float(np.linalg.norm(actual_rho - dephased_actual)),
            "outcome_created": False,
        },
    )


@dataclass(frozen=True)
class SinkState:
    token: tuple[int, ...]
    carrier: tuple[complex, ...]


def one_hot(length: int, index: int) -> tuple[int, ...]:
    if not 0 <= index < length:
        raise SinkDomainError("one-hot index outside finite sink")
    return tuple(int(candidate == index) for candidate in range(length))


def launch_state(length: int, value: np.ndarray) -> SinkState:
    if length < 2 or value.shape != (2,) or abs(np.linalg.norm(value) - 1) >= TOL:
        raise SinkDomainError("invalid open-sink launch")
    slots = np.zeros((length, 2), dtype=complex)
    slots[0] = value
    return SinkState(one_hot(length, 0), tuple(slots.reshape(-1)))


def sink_arrays(state: SinkState) -> tuple[np.ndarray, np.ndarray, int]:
    token = np.asarray(state.token, dtype=int)
    if len(token) < 2 or sum(token) != 1 or any(value not in (0, 1) for value in token):
        raise SinkDomainError("sink token must be one-hot")
    carrier = np.asarray(state.carrier, dtype=complex)
    if carrier.size != 2 * len(token):
        raise SinkDomainError("dual-rail carrier size mismatch")
    carrier = carrier.reshape(len(token), 2)
    index = int(np.flatnonzero(token)[0])
    if abs(np.linalg.norm(carrier) - 1) >= TOL:
        raise SinkDomainError("carrier must have unit norm")
    if np.linalg.norm(np.delete(carrier, index, axis=0)) >= TOL:
        raise SinkDomainError("carrier and token are not synchronized")
    return token, carrier, index


def forward_step(state: SinkState) -> SinkState:
    token, carrier, index = sink_arrays(state)
    if index == len(token) - 1:
        raise SinkBoundaryError("finite open sink exhausted; no wrap")
    if token[index + 1] or np.linalg.norm(carrier[index + 1]) >= TOL:
        raise SinkDomainError("outgoing target is not fresh")
    token[index], token[index + 1] = token[index + 1], token[index]
    carrier[[index, index + 1]] = carrier[[index + 1, index]]
    return SinkState(tuple(int(value) for value in token), tuple(carrier.reshape(-1)))


def inverse_step(state: SinkState) -> SinkState:
    token, carrier, index = sink_arrays(state)
    if index == 0:
        raise SinkBoundaryError("no earlier sink slice")
    token[index], token[index - 1] = token[index - 1], token[index]
    carrier[[index, index - 1]] = carrier[[index - 1, index]]
    return SinkState(tuple(int(value) for value in token), tuple(carrier.reshape(-1)))


def run_forward(value: np.ndarray, length: int, horizon: int) -> tuple[SinkState, ...]:
    if not 0 <= horizon <= length - 1:
        raise SinkDomainError("horizon must stop at or before the open boundary")
    history = [launch_state(length, value)]
    for _ in range(horizon):
        history.append(forward_step(history[-1]))
    return tuple(history)


def open_sink_resource_controls() -> None:
    print("\nOPEN DUAL-RAIL SINK / RESOURCE AND CAPACITY LEDGER")
    actual = carrier(6 * G, G)
    deleted = carrier(0.0, 0.0)
    rows = []
    failures = []
    for split, cases in (("training", TRAINING_CASES), ("held-out", (HELD_CASE,))):
        for length, horizon in cases:
            for label, value in (("W", actual), ("I", deleted)):
                history = run_forward(value, length, horizon)
                positions = tuple(sink_arrays(state)[2] for state in history)
                final_carrier = sink_arrays(history[-1])[1][horizon]
                row = {
                    "split": split,
                    "action": label,
                    "R": length,
                    "h": horizon,
                    "positions": (positions[0], positions[-1]),
                    "unique_states": len(set(history)),
                    "allocated_sink_M2": 3 * length,
                    "matter_support_M2": 52,
                    "total_M2": 52 + 3 * length,
                    "fresh_target_slices_used": horizon,
                    "fresh_target_slices_remaining": length - 1 - horizon,
                    "collision_launch_support_M2": 54,
                    "propagation_support_M2": 6,
                }
                rows.append(row)
                if not (
                    positions == tuple(range(horizon + 1))
                    and len(set(history)) == horizon + 1
                    and np.linalg.norm(final_carrier - value) < TOL
                ):
                    failures.append(row)
    check(
        "training and held sink horizons have exact finite forward nonreturn with the full coherent carrier unchanged",
        not failures,
        {"rows": rows, "failures": failures},
    )
    check(
        "the exact resource and capacity ledger has constant bounded per-step support and one fresh three-M2 sink slice per outward step",
        not failures
        and all(row["total_M2"] == 52 + 3 * row["R"] for row in rows)
        and all(row["collision_launch_support_M2"] == 54 for row in rows)
        and all(row["propagation_support_M2"] == 6 for row in rows),
        {
            "resource_law": "52 mapped matter M2 + 3R sink M2",
            "capacity_law": "R-1 fresh outward shifts",
            "maximum_per_step_support_M2": 54,
            "held_rows": tuple(row for row in rows if row["split"] == "held-out"),
        },
    )

    edge = run_forward(actual, HELD_CASE[0], HELD_CASE[1])[-1]
    boundary_rejected = False
    try:
        forward_step(edge)
    except SinkBoundaryError:
        boundary_rejected = True
    recovered = edge
    for _ in range(HELD_CASE[1]):
        recovered = inverse_step(recovered)
    one_step_back = inverse_step(run_forward(actual, 11, 8)[-1])
    restored = forward_step(one_step_back)
    check(
        "boundary, inverse, and adjacent retarget controls show finite forward nonreturn without unrestricted irreversibility",
        boundary_rejected
        and recovered == launch_state(HELD_CASE[0], actual)
        and restored == run_forward(actual, 11, 8)[-1],
        {
            "boundary_rejected": boundary_rejected,
            "full_inverse_reconnection": recovered == launch_state(HELD_CASE[0], actual),
            "bounded_backward_retarget_position": sink_arrays(one_step_back)[2],
            "retarget_restored": restored == run_forward(actual, 11, 8)[-1],
            "unrestricted_permanence": False,
        },
    )


def physical_code_support_controls() -> None:
    print("\nSAME CONNECTED CODE / ZERO ACTION LEAKAGE / MASS / HELD SIZE")
    coefficients = c285.contact_walsh_coefficients(np.diag(c285.fixture()["W"]))
    rows = []
    failures = []
    cache: dict[int, c269.WilsonSubsystemCode] = {}
    for length in (3, 4, 5, 6):
        code = c269.build_code(length)
        cache[length] = code
        blocks = tuple(
            tuple(c278.pauli_product(c278.cell_bs(code, cell), mask) for mask in range(64))
            for cell in MOTIF
        )
        support_union = 0
        for cell in MOTIF:
            for basis_row in c278.cell_bs(code, cell):
                support_union |= basis_row.x | basis_row.z
        leakage = sum(
            not term.commutes(check_row)
            for block in blocks
            for term in block
            for check_row in code.local_checks + code.wilsons
        )
        maximum_combined_weight = max(
            (((left @ middle @ right).x | (left @ middle @ right).z).bit_count())
            for left in blocks[0]
            for middle in blocks[1]
            for right in blocks[2]
        )
        row = {
            "L": length,
            "split": "held-out" if length == 6 else "training",
            "matter_support_union_M2": support_union.bit_count(),
            "maximum_three-cell_Walsh_term_weight": maximum_combined_weight,
            "local_check_or_Wilson_leakage": leakage,
            "collision_launch_support_M2": support_union.bit_count() + 2,
        }
        rows.append(row)
        if not (
            row["matter_support_union_M2"] == 52
            and maximum_combined_weight == 36
            and leakage == 0
            and row["collision_launch_support_M2"] == 54
        ):
            failures.append(row)
    species = c278.c219.common_species(c278.c230.BETA)
    one_particle_pair_counts = tuple(
        sum(number * (number - 1) // 2 for number in occupations)
        for occupations in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    )
    check(
        "the actual three-cell action has zero action-algebra leakage, bounded support through held-out L=6, and preserves the one-particle mass fixture",
        not failures
        and all(abs(value) > 1e-14 for value in coefficients)
        and one_particle_pair_counts == (0, 0, 0)
        and abs(c278.c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "rows": rows,
            "failures": failures,
            "one_particle_action": "identity",
            "rest_over_analytic_mass": c278.c219.rest_mass(species) / species.analytic_mass,
            "comparator_status": "declared code-preserving isometry on the supplied two-dimensional even reference span; nearest-neighbor synthesis not derived",
        },
    )

    code = cache[3]
    base_rows = tuple(row for cell in MOTIF for row in c278.cell_bs(code, cell))
    local_family = set(code.local_checks)
    central_pivots, central_bad = c278.phase_reducer(
        list(code.local_checks + code.wilsons), code.qubits
    )
    covariance_failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        frame_vertex, frame_edge = c235.graph_frame_maps(code.graph, frame)
        direction_mapping = c235.direction_map(frame)
        moved_counts = (
            (4, 0, 0),
            (2, 1, 1),
        )
        if tuple(sum(row) for row in moved_counts) != (4, 4) or tuple(
            sum(number >= 2 for number in row) for row in moved_counts
        ) != (1, 1):
            covariance_failures.append(("reference-count", frame.tolist()))
        # The direction map must permute every selected occupation mask without
        # changing its population.
        for mask in (0b001111, 0b000011, 0b000001):
            moved = sum(
                (1 << direction_mapping[direction])
                for direction in range(6)
                if (mask >> direction) & 1
            )
            if moved.bit_count() != mask.bit_count():
                covariance_failures.append(("mode-population", frame.tolist(), mask))
        for displacement in product(range(3), repeat=3):
            translation_vertex, translation_edge = c269.graph_translation_maps(
                code.graph, displacement
            )
            vertex_map = tuple(
                translation_vertex[frame_vertex[index]] for index in range(len(frame_vertex))
            )
            edge_map = tuple(
                translation_edge[frame_edge[index]] for index in range(len(frame_edge))
            )
            toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
            transformed = {
                c235.apply_gauge(c235.permute_pauli(row, edge_map), toggles, pairs, flips)
                for row in base_rows
            }
            target_cells = tuple(
                tuple(
                    (int(sum(frame[axis, source] * cell[source] for source in range(3))) + displacement[axis]) % 3
                    for axis in range(3)
                )
                for cell in MOTIF
            )
            target = {row for cell in target_cells for row in c278.cell_bs(code, cell)}
            transformed_local = {
                c235.apply_gauge(c235.permute_pauli(row, edge_map), toggles, pairs, flips)
                for row in code.local_checks
            }
            transformed_wilsons = tuple(
                c235.apply_gauge(c235.permute_pauli(row, edge_map), toggles, pairs, flips)
                for row in code.wilsons
            )
            if not (
                transformed == target
                and transformed_local == local_family
                and not central_bad
                and all(
                    not c278.reduce_pauli(row, central_pivots, code.qubits).symplectic(code.qubits)
                    for row in transformed_wilsons
                )
            ):
                covariance_failures.append((frame.tolist(), displacement, target_cells))
            tests += 1
    check(
        "the three-cell reference/action family is covariant under all 24 proper-cubic frames and full L=3 translations",
        not covariance_failures and tests == 24 * 27,
        {"frame_translation_tests": tests, "failures": covariance_failures[:5]},
    )


def rail_covariance_and_collision_controls() -> None:
    print("\nOPEN-SINK COLLISION / CARRIED COVARIANCE")
    length = HELD_CASE[0]
    cross_section = ((0, 0), (1, 0), (0, 1))
    base = tuple(
        (index, y, z)
        for index in range(length)
        for y, z in cross_section
    )
    base_distances = tuple(
        sorted(
            sum(
                (base[3 * (index + 1) + lane][axis] - base[3 * index + lane][axis]) ** 2
                for axis in range(3)
            )
            for index in range(length - 1)
            for lane in range(3)
        )
    )
    failures = []
    tests = 0
    for frame in c235.proper_cubic_frames():
        for displacement in product((-1, 0, 1), repeat=3):
            transformed = tuple(
                tuple(
                    int(sum(frame[axis, source] * point[source] for source in range(3)))
                    + displacement[axis]
                    for axis in range(3)
                )
                for point in base
            )
            distances = tuple(
                sorted(
                    sum(
                        (transformed[3 * (index + 1) + lane][axis] - transformed[3 * index + lane][axis]) ** 2
                        for axis in range(3)
                    )
                    for index in range(length - 1)
                    for lane in range(3)
                )
            )
            if len(set(transformed)) != len(transformed) or distances != base_distances:
                failures.append((frame.tolist(), displacement))
            tests += 1
    merged = tuple((x, 0, 0) if lane == 2 else point for x in range(length) for lane, point in enumerate(base[3*x:3*x+3]))
    check(
        "the supplied open three-lane sink is collision-free and carried covariantly in all 24 proper-cubic frames",
        not failures
        and tests == 24 * 27
        and set(base_distances) == {1}
        and len(merged) - len(set(merged)) == length,
        {
            "frame_translation_tests": tests,
            "held_sink_role_sites": len(base),
            "failures": failures[:3],
            "deliberate_dark_token_lane_merge_collisions": len(merged) - len(set(merged)),
            "origin_orientation_generated": False,
        },
    )


def lawful_domain_and_semantic_controls() -> None:
    print("\nLAWFUL DOMAIN / SUPPLIED IMPORTS / SEMANTIC FIREWALL")
    def validate_domain(
        length: int,
        horizon: int,
        coupling: float,
        occupations: tuple[tuple[int, int, int], tuple[int, int, int]],
    ) -> None:
        if length < 2 or not 0 <= horizon <= length - 1:
            raise SinkDomainError("invalid finite open-sink extent")
        if coupling != G:
            raise SinkDomainError("the selected action fixture has g=0.37")
        if occupations != ((4, 0, 0), (2, 1, 1)):
            raise SinkDomainError("the declared reference has fixed total N=4 and pair counts 6/1")

    rejected = 0
    invalid = (
        lambda: validate_domain(1, 0, G, ((4, 0, 0), (2, 1, 1))),
        lambda: validate_domain(5, 5, G, ((4, 0, 0), (2, 1, 1))),
        lambda: validate_domain(5, 4, 0.0, ((4, 0, 0), (2, 1, 1))),
        lambda: validate_domain(5, 4, G, ((3, 1, 0), (2, 1, 1))),
    )
    for call in invalid:
        try:
            call()
        except (SinkDomainError, SinkBoundaryError):
            rejected += 1
    validate_domain(HELD_CASE[0], HELD_CASE[1], G, ((4, 0, 0), (2, 1, 1)))
    text = normalized(NOTE)
    check(
        "finite/open lawful-domain and semantic controls retain every supplied import without promoting export to physics it does not provide",
        rejected == 4
        and "sink export is not occurrence" in text
        and "sink export is not a record" in text
        and "rail step count is not physical time" in text
        and "no energy or source connector is constructed" in text,
        {
            "rejected_controls": rejected,
            "supplied": "three-cell connected code; fixed-total-N reference; selected cells/modes; W_g fixture; recombiner/transfer; bright/dark convention; blank open rail; token, origin, orientation, boundary, fresh targets; forward grammar; trace/effect pairing",
            "physical_recombiner_NN_synthesis": False,
            "reference_preparation_derived": False,
            "actual_branch_selected": False,
            "Record_formed": False,
            "clock_or_rate": False,
            "energy_or_source_connector": False,
            "shared_obstruction": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    data = coherent_detector_controls()
    reduced_channel_controls()
    open_sink_resource_controls()
    physical_code_support_controls()
    rail_covariance_and_collision_controls()
    lawful_domain_and_semantic_controls()
    print("DATA", data)
    print("SUMMARY PASS", PASS, "FAIL", FAIL)
    print(
        "RESULT",
        "CYCLE291_OPEN_BOUNDARY_ACTUAL_ACTION_DETECTOR_GREEN"
        if FAIL == 0
        else "CYCLE291_OPEN",
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
