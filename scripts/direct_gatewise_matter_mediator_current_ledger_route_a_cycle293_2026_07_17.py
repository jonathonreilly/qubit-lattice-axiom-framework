#!/usr/bin/env python3
"""Cycle 293 Route A: bounded gatewise matter/mediator current ledger.

Join the retained common massive coin, the finite six-direction mediator, the
autonomous scalar emission vertex, and the intrinsic CAR contact gate without
calling probability density energy.  The literal sparse update exposes an
onsite signed mediator source and separate one-edge matter and mediator
transfers.  A second exact comparison keeps the Cycle-216 static 3 L^+ target
separate from the nonmatching Cycle-215 injection port.

This is a conditional zero/one-mediator, one-matter dynamical route plus an
algebraic onsite contact-composition control.  It is not a prepared full-Fock
physical compiler, an energy/stress tensor, gravity, a clock, a Record, a Born
law, an empirical prediction, or an axiom proposal.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import local_rough_puncture_odd_sector_cycle247_2026_07_17 as c247
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "DIRECT_GATEWISE_MATTER_MEDIATOR_CURRENT_LEDGER_ROUTE_A_CYCLE293_NOTE_2026-07-17.md"
)

BETA = -0.3
CONTACT_COUPLING = 0.37
MEDIATOR_COUPLING = 0.8
TOLERANCE = 3e-11

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def add_position(
    left: tuple[int, int, int], right: np.ndarray, sign: int = 1
) -> tuple[int, int, int]:
    return tuple(int(left[axis] + sign * right[axis]) for axis in range(3))


def l1(position: tuple[int, int, int]) -> int:
    return sum(abs(value) for value in position)


@dataclass
class SparseState:
    """One matter carrier and zero or one mediator on the infinite cubic grid."""

    vacuum: dict[tuple[int, int, int], np.ndarray]
    pair: dict[
        tuple[tuple[int, int, int], tuple[int, int, int]], np.ndarray
    ]

    def copy(self) -> "SparseState":
        return SparseState(
            {key: value.copy() for key, value in self.vacuum.items()},
            {key: value.copy() for key, value in self.pair.items()},
        )


def zero_vector() -> np.ndarray:
    return np.zeros(6, dtype=complex)


def zero_pair() -> np.ndarray:
    return np.zeros((6, 6), dtype=complex)


def state_norm(state: SparseState) -> float:
    return float(
        sum(np.vdot(value, value).real for value in state.vacuum.values())
        + sum(np.vdot(value, value).real for value in state.pair.values())
    )


def pair_probability(state: SparseState) -> float:
    return float(sum(np.vdot(value, value).real for value in state.pair.values()))


def matter_density(state: SparseState) -> dict[tuple[int, int, int], float]:
    density: dict[tuple[int, int, int], float] = {}
    for position, value in state.vacuum.items():
        density[position] = density.get(position, 0.0) + float(
            np.vdot(value, value).real
        )
    for (body, _field), value in state.pair.items():
        density[body] = density.get(body, 0.0) + float(np.vdot(value, value).real)
    return density


def mediator_density(state: SparseState) -> dict[tuple[int, int, int], float]:
    density: dict[tuple[int, int, int], float] = {}
    for (_body, field), value in state.pair.items():
        density[field] = density.get(field, 0.0) + float(np.vdot(value, value).real)
    return density


def dictionary_residual(
    left: dict[tuple[int, int, int], float],
    right: dict[tuple[int, int, int], float],
) -> float:
    return max(
        (abs(left.get(key, 0.0) - right.get(key, 0.0)) for key in left | right),
        default=0.0,
    )


def state_residual(left: SparseState, right: SparseState) -> float:
    total = 0.0
    for key in left.vacuum.keys() | right.vacuum.keys():
        total += float(
            np.vdot(
                left.vacuum.get(key, zero_vector())
                - right.vacuum.get(key, zero_vector()),
                left.vacuum.get(key, zero_vector())
                - right.vacuum.get(key, zero_vector()),
            ).real
        )
    for key in left.pair.keys() | right.pair.keys():
        difference = left.pair.get(key, zero_pair()) - right.pair.get(
            key, zero_pair()
        )
        total += float(np.vdot(difference, difference).real)
    return float(np.sqrt(total))


def scale_state(state: SparseState, scale: complex) -> SparseState:
    return SparseState(
        {key: scale * value for key, value in state.vacuum.items()},
        {key: scale * value for key, value in state.pair.items()},
    )


def add_states(left: SparseState, right: SparseState) -> SparseState:
    output = left.copy()
    for key, value in right.vacuum.items():
        output.vacuum[key] = output.vacuum.get(key, zero_vector()) + value
    for key, value in right.pair.items():
        output.pair[key] = output.pair.get(key, zero_pair()) + value
    return output


def coin_gate(
    state: SparseState, matter_coin: np.ndarray, field_coin: np.ndarray
) -> SparseState:
    return SparseState(
        {
            position: matter_coin @ value
            for position, value in state.vacuum.items()
        },
        {
            key: np.einsum(
                "ab,cd,bd->ac", matter_coin, field_coin, value, optimize=True
            )
            for key, value in state.pair.items()
        },
    )


def vertex_gate(
    state: SparseState, angle: float
) -> tuple[SparseState, dict[tuple[int, int, int], float], float]:
    """Apply the same scalar vacuum/mediator rotation at every body cell."""
    output = state.copy()
    positions = set(state.vacuum)
    positions.update(body for body, field in state.pair if body == field)
    currents: dict[tuple[int, int, int], float] = {}
    local_residual = 0.0
    for position in positions:
        source = state.vacuum.get(position, zero_vector())
        contact = state.pair.get((position, position), zero_pair())
        before_source = float(np.vdot(source, source).real)
        before_pair = float(np.vdot(contact, contact).real)
        new_source, new_contact = c214.apply_vertex(source, contact, angle)
        after_source = float(np.vdot(new_source, new_source).real)
        after_pair = float(np.vdot(new_contact, new_contact).real)
        currents[position] = after_pair - before_pair
        local_residual = max(
            local_residual,
            abs((after_source - before_source) + currents[position]),
        )
        output.vacuum[position] = new_source
        output.pair[(position, position)] = new_contact
    return output, currents, local_residual


def body_stream(
    state: SparseState, *, inverse: bool = False
) -> tuple[SparseState, dict[tuple[tuple[int, int, int], int], float]]:
    output = SparseState({}, {})
    current: dict[tuple[tuple[int, int, int], int], float] = {}
    sign = -1 if inverse else 1
    for position, value in state.vacuum.items():
        for direction in range(6):
            destination = add_position(position, c210.DIRECTIONS[direction], sign)
            target = output.vacuum.setdefault(destination, zero_vector())
            target[direction] += value[direction]
            current[(position, direction)] = current.get(
                (position, direction), 0.0
            ) + float(abs(value[direction]) ** 2)
    for (body, field), value in state.pair.items():
        for body_direction in range(6):
            destination = add_position(
                body, c210.DIRECTIONS[body_direction], sign
            )
            target = output.pair.setdefault((destination, field), zero_pair())
            target[body_direction, :] += value[body_direction, :]
            current[(body, body_direction)] = current.get(
                (body, body_direction), 0.0
            ) + float(np.vdot(value[body_direction, :], value[body_direction, :]).real)
    return output, current


def field_stream(
    state: SparseState, *, inverse: bool = False
) -> tuple[SparseState, dict[tuple[tuple[int, int, int], int], float]]:
    output = SparseState(
        {key: value.copy() for key, value in state.vacuum.items()}, {}
    )
    current: dict[tuple[tuple[int, int, int], int], float] = {}
    sign = -1 if inverse else 1
    for (body, field), value in state.pair.items():
        for field_direction in range(6):
            destination = add_position(
                field, c210.DIRECTIONS[field_direction], sign
            )
            target = output.pair.setdefault((body, destination), zero_pair())
            target[:, field_direction] += value[:, field_direction]
            current[(field, field_direction)] = current.get(
                (field, field_direction), 0.0
            ) + float(np.vdot(value[:, field_direction], value[:, field_direction]).real)
    return output, current


def incoming_density(
    current: dict[tuple[tuple[int, int, int], int], float], *, inverse: bool = False
) -> dict[tuple[int, int, int], float]:
    answer: dict[tuple[int, int, int], float] = {}
    sign = -1 if inverse else 1
    for (source, direction), value in current.items():
        destination = add_position(source, c210.DIRECTIONS[direction], sign)
        answer[destination] = answer.get(destination, 0.0) + value
    return answer


def sparse_step(
    state: SparseState, matter_coin: np.ndarray, field_coin: np.ndarray, angle: float
) -> tuple[SparseState, dict[str, object]]:
    before_norm = state_norm(state)
    coined = coin_gate(state, matter_coin, field_coin)
    coin_matter_residual = dictionary_residual(
        matter_density(coined), matter_density(state)
    )
    coin_field_residual = dictionary_residual(
        mediator_density(coined), mediator_density(state)
    )
    sourced, source_current, source_residual = vertex_gate(coined, angle)
    matter_before_stream = matter_density(sourced)
    field_before_stream = mediator_density(sourced)
    body_moved, body_current = body_stream(sourced)
    body_residual = dictionary_residual(
        matter_density(body_moved), incoming_density(body_current)
    )
    field_moved, field_current = field_stream(body_moved)
    field_residual = dictionary_residual(
        mediator_density(field_moved), incoming_density(field_current)
    )
    diagnostics: dict[str, object] = {
        "norm_residual": abs(state_norm(field_moved) - before_norm),
        "coin_matter_residual": coin_matter_residual,
        "coin_field_residual": coin_field_residual,
        "source_residual": source_residual,
        "source_current": source_current,
        "source_sum": sum(source_current.values()),
        "source_pair_change": pair_probability(sourced) - pair_probability(coined),
        "matter_vertex_residual": dictionary_residual(
            matter_density(sourced), matter_density(coined)
        ),
        "body_edge_residual": body_residual,
        "body_current_sum": sum(body_current.values()),
        "matter_before_stream_sum": sum(matter_before_stream.values()),
        "field_edge_residual": field_residual,
        "field_current_sum": sum(field_current.values()),
        "field_before_stream_sum": sum(field_before_stream.values()),
    }
    return field_moved, diagnostics


def inverse_sparse_step(
    state: SparseState, matter_coin: np.ndarray, field_coin: np.ndarray, angle: float
) -> SparseState:
    unfielded, _ = field_stream(state, inverse=True)
    unbodied, _ = body_stream(unfielded, inverse=True)
    unsourced, _, _ = vertex_gate(unbodied, -angle)
    return coin_gate(unsourced, matter_coin.conj().T, field_coin.conj().T)


def rotate_state(state: SparseState, frame: np.ndarray) -> SparseState:
    representation = c210.direction_permutation(frame)

    def rotate_position(position: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(int(value) for value in frame @ np.asarray(position))

    return SparseState(
        {
            rotate_position(position): representation @ value
            for position, value in state.vacuum.items()
        },
        {
            (rotate_position(body), rotate_position(field)): representation
            @ value
            @ representation.T
            for (body, field), value in state.pair.items()
        },
    )


@dataclass(frozen=True)
class HardCoreBlocks:
    mediator_coin: np.ndarray
    mediator_rotation: np.ndarray
    mediator_number: np.ndarray
    scalar_number: np.ndarray
    contact: np.ndarray


def computational_mode_permutation(permutation: np.ndarray) -> np.ndarray:
    """Ordinary six-qubit mode permutation, with no fermionic determinant sign."""
    result = np.zeros((64, 64), dtype=complex)
    for basis in range(64):
        target = 0
        for source_mode in range(6):
            if (basis >> source_mode) & 1:
                target_mode = int(np.argmax(permutation[:, source_mode]))
                target |= 1 << target_mode
        result[target, basis] = 1
    return result


def local_m2_and_contact_controls(
    species: c210.Species, angle: float
) -> HardCoreBlocks:
    """Selected six-hard-core-qubit local extension and mapped matter control."""
    identity64 = np.eye(64, dtype=complex)
    one_particle = tuple(1 << direction for direction in range(6))
    vacuum = np.zeros(64, dtype=complex)
    vacuum[0] = 1
    scalar = np.zeros(64, dtype=complex)
    scalar[list(one_particle)] = c210.UNIFORM

    mediator_coin = identity64.copy()
    mediator_coin[np.ix_(one_particle, one_particle)] = c214.FIELD_COIN
    source_projector = np.outer(vacuum, vacuum) + np.outer(
        scalar, scalar.conj()
    )
    source_flip = np.outer(vacuum, scalar.conj()) + np.outer(
        scalar, vacuum.conj()
    )
    mediator_rotation = (
        identity64
        + (np.cos(angle) - 1) * source_projector
        + 1j * np.sin(angle) * source_flip
    )
    mediator_occupations = c229.occupation_table(6)
    mediator_number_values = np.sum(mediator_occupations, axis=1)
    mediator_number = np.diag(mediator_number_values)

    annihilators = c229.annihilation_operators(6)
    scalar_annihilator = sum(
        (
            c210.UNIFORM[index].conjugate() * annihilators[index]
            for index in range(6)
        ),
        np.zeros((64, 64), dtype=complex),
    )
    scalar_number = scalar_annihilator.conj().T @ scalar_annihilator
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    matter_number = np.diag(number)
    contact = np.diag(
        np.exp(1j * CONTACT_COUPLING * number * (number - 1) / 2)
    )
    matter_coin = c229.fock_lift(species.coin)

    swap2 = np.asarray(
        ((1, 0, 0, 0), (0, 0, 1, 0), (0, 1, 0, 0), (0, 0, 0, 1)),
        dtype=complex,
    )
    reverse64 = computational_mode_permutation(c210.REVERSE)

    reverse_labels = (1, 0, 3, 2, 5, 4)

    def permute_basis(basis: int, direction_frame: np.ndarray) -> int:
        output = 0
        for source_direction in range(6):
            if (basis >> source_direction) & 1:
                target_direction = int(
                    np.argmax(direction_frame[:, source_direction])
                )
                output |= 1 << target_direction
        return output

    def edge_swap_basis(left: int, right: int, direction: int) -> tuple[int, int]:
        left_mode = reverse_labels[direction]
        left_bit = (left >> left_mode) & 1
        right_bit = (right >> direction) & 1
        if left_bit != right_bit:
            left ^= 1 << left_mode
            right ^= 1 << direction
        return left, right

    edge_covariance_failures = 0
    for frame in c210.proper_cubic_frames():
        direction_frame = c210.direction_permutation(frame)
        for direction in range(6):
            target_direction = int(np.argmax(direction_frame[:, direction]))
            for left in range(64):
                for right in range(64):
                    moved_left, moved_right = edge_swap_basis(left, right, direction)
                    framed_after = (
                        permute_basis(moved_left, direction_frame),
                        permute_basis(moved_right, direction_frame),
                    )
                    framed_before = (
                        permute_basis(left, direction_frame),
                        permute_basis(right, direction_frame),
                    )
                    after_frame = edge_swap_basis(
                        framed_before[0], framed_before[1], target_direction
                    )
                    edge_covariance_failures += framed_after != after_frame
    check(
        "six hard-core mediator M2 give a tensor-local all-occupancy extension",
        np.linalg.norm(mediator_coin.conj().T @ mediator_coin - identity64)
        < 3e-12
        and np.linalg.norm(mediator_rotation.conj().T @ mediator_rotation - identity64)
        < 3e-12
        and np.linalg.norm(mediator_coin @ vacuum - vacuum) < 2e-15,
        {
            "mediator_dimension": 64,
            "physical_M2_per_cell": 6,
            "higher_local_number_extension": "identity",
        },
    )
    check(
        "ordinary directional qubit swaps give a bounded tensorable stream",
        np.linalg.norm(swap2.conj().T @ swap2 - np.eye(4)) < 2e-15
        and np.linalg.norm(reverse64.conj().T @ reverse64 - identity64) < 2e-15
        and edge_covariance_failures == 0,
        {
            "onsite_support_M2": 6,
            "each_edge_swap_support_M2": 2,
            "all_frame_basis_failures": edge_covariance_failures,
        },
    )
    check(
        "the controlled hard-core vertex is unitary and preserves matter number",
        np.linalg.norm(scalar_number @ scalar_number - scalar_number) < 3e-12
        and np.linalg.norm(matter_number @ scalar_number - scalar_number @ matter_number)
        < 3e-12
        and np.linalg.norm(mediator_rotation.conj().T @ mediator_rotation - identity64)
        < 3e-12,
        "unitarity follows blockwise from projector n_s and R_eta",
    )
    contact_commutator = np.linalg.norm(contact @ scalar_number - scalar_number @ contact)
    coin_commutator = np.linalg.norm(matter_coin @ scalar_number - scalar_number @ matter_coin)
    check(
        "the unchanged intrinsic contact and common matter coin compose with the scalar control",
        contact_commutator < 3e-12
        and coin_commutator < 3e-12
        and np.max(np.abs(np.diag(contact)[number <= 1] - 1)) < 2e-15
        and abs(
            np.diag(contact)[int(np.where(number == 2)[0][0])]
            - np.exp(1j * CONTACT_COUPLING)
        )
        < 2e-15,
        {
            "contact_control_commutator": contact_commutator,
            "coin_control_commutator": coin_commutator,
        },
    )

    emitted = mediator_rotation @ vacuum
    absorbed = mediator_rotation @ scalar
    emission_current = float(np.vdot(emitted, mediator_number @ emitted).real)
    absorption_current = float(
        np.vdot(absorbed, mediator_number @ absorbed).real - 1
    )
    check(
        "the same local tensor gate has exact positive emission and negative absorption currents",
        abs(emission_current - np.sin(angle) ** 2) < 3e-12
        and abs(absorption_current + np.sin(angle) ** 2) < 3e-12,
        {"emission": emission_current, "absorption": absorption_current},
    )

    mapped_support_rows = []
    for length in (3, 4, 5, 6):
        graph = c247.PunctureGraph(length, terminals=1)
        cell = (0, 0, 0)
        sink = graph.sink_index[cell]
        modes = [graph.base.vertex_index[(cell, direction)] for direction in range(6)]
        scalar_terms = [graph.B(mode) for mode in modes]
        scalar_terms.extend(
            graph.A(left, sink) @ graph.A(sink, right)
            for index, left in enumerate(modes)
            for right in modes[index + 1 :]
        )
        support_union = 0
        for term in scalar_terms:
            support_union |= term.x | term.z
        local_checks = [
            graph.loop_pauli(vertices)
            for _mask, vertices, _kind in graph.local_cycles()
        ] + [graph.cell_constraint(item) for item in graph.cells] + graph.boundary_stabilizers()
        wilson_checks = [graph.loop_pauli(vertices) for vertices in graph.wilson_cycles()]
        mapped_support_rows.append(
            (
                length,
                max((term.x | term.z).bit_count() for term in scalar_terms),
                support_union.bit_count(),
                sum(
                    not term.commutes(row)
                    for term in scalar_terms
                    for row in local_checks
                ),
                sum(
                    not term.commutes(row)
                    for term in scalar_terms
                    for row in wilson_checks
                ),
            )
        )
    check(
        "the mapped scalar star has held support 24 and zero local-check/Wilson leakage",
        mapped_support_rows
        == [
            (3, 14, 24, 0, 0),
            (4, 14, 24, 0, 0),
            (5, 14, 24, 0, 0),
            (6, 14, 24, 0, 0),
        ],
        mapped_support_rows,
    )

    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        direction_frame = c210.direction_permutation(frame)
        matter_frame = c229.fock_lift(direction_frame)
        mediator_frame = computational_mode_permutation(direction_frame)
        frame_residuals.extend(
            (
                np.linalg.norm(matter_frame @ scalar_number - scalar_number @ matter_frame),
                np.linalg.norm(
                    mediator_frame @ mediator_rotation
                    - mediator_rotation @ mediator_frame
                ),
                np.linalg.norm(
                    mediator_frame @ mediator_coin - mediator_coin @ mediator_frame
                ),
                np.linalg.norm(matter_frame @ contact - contact @ matter_frame),
            )
        )
    check(
        "hard-core vertex, field coin, and contact commute with all 24 proper-cubic frames",
        len(frame_residuals) == 96 and max(frame_residuals) < 3e-11,
        max(frame_residuals),
    )

    check(
        "vertex and contact deletion are exact local identities",
        np.linalg.norm(
            identity64
            + (np.cos(0.0) - 1) * source_projector
            + 1j * np.sin(0.0) * source_flip
            - identity64
        )
        < 2e-15
        and np.linalg.norm(
            np.diag(np.exp(1j * 0.0 * number * (number - 1) / 2)) - identity64
        )
        < 2e-15,
    )
    return HardCoreBlocks(
        mediator_coin,
        mediator_rotation,
        mediator_number,
        scalar_number,
        contact,
    )


def literal_gatewise_ledger_controls(
    species: c210.Species, angle: float
) -> tuple[SparseState, list[dict[str, object]]]:
    """Cycle-214 global-blockade comparator, not the full tensor trajectory."""
    initial = SparseState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    state = initial
    rows: list[dict[str, object]] = []
    for tick in range(1, 5):
        state, diagnostics = sparse_step(
            state, species.coin, c214.FIELD_COIN, angle
        )
        matter_outside = sum(
            value for position, value in matter_density(state).items() if l1(position) > tick
        )
        field_outside = sum(
            value for position, value in mediator_density(state).items() if l1(position) > tick
        )
        relative_outside = sum(
            float(np.vdot(value, value).real)
            for (body, field), value in state.pair.items()
            if l1(tuple(field[axis] - body[axis] for axis in range(3))) > 2 * tick
        )
        rows.append(
            {
                "tick": tick,
                "norm": state_norm(state),
                "mediator_probability": pair_probability(state),
                "matter_outside": matter_outside,
                "field_outside": field_outside,
                "relative_outside": relative_outside,
                **diagnostics,
            }
        )

    exact_residuals = (
        "norm_residual",
        "coin_matter_residual",
        "coin_field_residual",
        "source_residual",
        "matter_vertex_residual",
        "body_edge_residual",
        "field_edge_residual",
    )
    check(
        "the global-blockade comparator has an exact gatewise current ledger",
        max(float(row[key]) for row in rows for key in exact_residuals) < 3e-12
        and max(
            abs(float(row["source_sum"]) - float(row["source_pair_change"]))
            for row in rows
        )
        < 3e-12
        and max(
            abs(float(row["body_current_sum"]) - float(row["matter_before_stream_sum"]))
            for row in rows
        )
        < 3e-12
        and max(
            abs(float(row["field_current_sum"]) - float(row["field_before_stream_sum"]))
            for row in rows
        )
        < 3e-12,
        [
            {
                "tick": row["tick"],
                "mediator_probability": row["mediator_probability"],
                "source_sum": row["source_sum"],
                "maximum_gate_residual": max(float(row[key]) for key in exact_residuals),
            }
            for row in rows
        ],
    )
    check(
        "the blockade comparator stays inside the local gate cone",
        max(
            max(
                float(row["matter_outside"]),
                float(row["field_outside"]),
                float(row["relative_outside"]),
            )
            for row in rows
        )
        < 3e-14,
        [
            (row["tick"], row["matter_outside"], row["field_outside"], row["relative_outside"])
            for row in rows
        ],
    )
    check(
        "the first blockade tick equals the full hard-core local emission channel",
        abs(float(rows[0]["mediator_probability"]) - np.sin(angle) ** 2) < 3e-12
        and float(rows[0]["source_sum"]) > 0,
        {
            "mediator_probability": rows[0]["mediator_probability"],
            "source_sum": rows[0]["source_sum"],
            "sin_squared_angle": float(np.sin(angle) ** 2),
        },
    )

    restored = inverse_sparse_step(state, species.coin, c214.FIELD_COIN, angle)
    for _ in range(3):
        restored = inverse_sparse_step(
            restored, species.coin, c214.FIELD_COIN, angle
        )
    check(
        "inverse gate order restores the finite-support blockade comparator",
        state_residual(restored, initial) < 3e-11,
        state_residual(restored, initial),
    )
    return state, rows


def emission_absorption_and_recoil_controls(
    species: c210.Species, angle: float
) -> None:
    side = 31
    source = c210.UNIFORM.copy()
    pair = np.zeros((side, side, side, 6, 6), dtype=complex)
    rows = []
    previous_pair_probability = 0.0
    coordinates = np.indices((side, side, side))
    signed = np.minimum(coordinates, side - coordinates)
    manhattan = np.sum(signed, axis=0)
    for tick in range(1, 8):
        coined_source = species.coin @ source
        coined_pair = np.einsum(
            "ab,cd,xyzbd->xyzac",
            species.coin,
            c214.FIELD_COIN,
            pair,
            optimize=True,
        )
        before_source = float(np.vdot(coined_source, coined_source).real)
        before_pair = float(np.vdot(coined_pair, coined_pair).real)
        coined_source, coined_pair[0, 0, 0] = c214.apply_vertex(
            coined_source, coined_pair[0, 0, 0], angle
        )
        after_source = float(np.vdot(coined_source, coined_source).real)
        after_pair = float(np.vdot(coined_pair, coined_pair).real)
        source_current = after_pair - before_pair
        source = c214.source_stream(coined_source, np.zeros(3))
        pair = c214.relative_stream(coined_pair, np.zeros(3))
        pair_value = float(np.vdot(pair, pair).real)
        probability = np.sum(np.abs(pair) ** 2, axis=(3, 4))
        rows.append(
            {
                "tick": tick,
                "source_current": source_current,
                "pair_change": pair_value - previous_pair_probability,
                "vertex_residual": abs(
                    (after_source - before_source) + source_current
                ),
                "outside": float(np.max(probability[manhattan > 2 * tick])),
                "norm": before_source + before_pair,
            }
        )
        previous_pair_probability = pair_value

    check(
        "the old global-blockade comparison has a pre-wrap negative current",
        rows[0]["source_current"] > 0
        and rows[-1]["source_current"] < -1e-3
        and max(abs(row["source_current"] - row["pair_change"]) for row in rows)
        < 3e-12
        and max(row["vertex_residual"] for row in rows) < 3e-12
        and max(row["outside"] for row in rows) < 3e-14
        and 2 * len(rows) < side // 2,
        rows,
    )

    momentum = np.asarray((0.17, -0.11, 0.07))
    source_k = c210.UNIFORM.copy()
    pair_k = np.zeros_like(pair)
    for _ in range(5):
        source_k, pair_k = c214.relative_step(
            source_k, pair_k, species, angle, momentum
        )
    pair_fourier = np.fft.fftn(pair_k, axes=(0, 1, 2), norm="ortho")
    weights = np.sum(np.abs(pair_fourier) ** 2, axis=(3, 4))
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    grids = np.meshgrid(momenta, momenta, momenta, indexing="ij")
    field_mean = np.asarray(
        [float(np.sum(weights * grid) / np.sum(weights)) for grid in grids]
    )
    body_mean = momentum - field_mean
    check(
        "the one-mediator blockade block carries kinematic recoil accounting",
        abs(c214.norm(source_k, pair_k) - 1) < 3e-12
        and np.linalg.norm(body_mean + field_mean - momentum) < 3e-14
        and float(np.sum(weights)) > 0.1,
        {
            "K": momentum.tolist(),
            "body_mean": body_mean.tolist(),
            "field_mean": field_mean.tolist(),
            "mediator_probability": float(np.sum(weights)),
        },
    )


def covariance_composition_deletion_controls(
    species: c210.Species, angle: float, blocks: HardCoreBlocks
) -> None:
    rng = np.random.default_rng(29301)
    random_state = SparseState(
        {
            (0, 0, 0): rng.normal(size=6) + 1j * rng.normal(size=6),
            (2, -1, 0): rng.normal(size=6) + 1j * rng.normal(size=6),
        },
        {
            ((0, 0, 0), (0, 0, 0)): rng.normal(size=(6, 6))
            + 1j * rng.normal(size=(6, 6)),
            ((1, 0, -1), (-1, 1, 0)): rng.normal(size=(6, 6))
            + 1j * rng.normal(size=(6, 6)),
        },
    )
    random_state = scale_state(random_state, 1 / np.sqrt(state_norm(random_state)))
    output, _ = sparse_step(
        random_state, species.coin, c214.FIELD_COIN, angle
    )
    covariance = []
    for frame in c210.proper_cubic_frames():
        rotated_input = rotate_state(random_state, frame)
        rotated_output, _ = sparse_step(
            rotated_input, species.coin, c214.FIELD_COIN, angle
        )
        covariance.append(
            state_residual(rotated_output, rotate_state(output, frame))
        )
    check(
        "the globally blockaded sparse comparator commutes with all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 3e-11,
        max(covariance),
    )

    initial = SparseState({(0, 0, 0): c210.UNIFORM.copy()}, {})
    deleted = initial
    for _ in range(4):
        deleted, _ = sparse_step(
            deleted, species.coin, c214.FIELD_COIN, 0.0
        )
    bare = initial
    for _ in range(4):
        coined = coin_gate(bare, species.coin, c214.FIELD_COIN)
        bare, _ = body_stream(coined)
    check(
        "mediator-vertex deletion returns the bare massive walk and exact field vacuum",
        state_residual(deleted, bare) < 3e-12
        and pair_probability(deleted) < 3e-14,
        state_residual(deleted, bare),
    )

    left = SparseState({(-5, 0, 0): c210.UNIFORM.copy()}, {})
    right = SparseState({(5, 0, 0): c210.UNIFORM.copy()}, {})
    combined = scale_state(add_states(left, right), 1 / np.sqrt(2))
    combined_output, _ = sparse_step(
        combined, species.coin, c214.FIELD_COIN, angle
    )
    left_output, _ = sparse_step(left, species.coin, c214.FIELD_COIN, angle)
    right_output, _ = sparse_step(right, species.coin, c214.FIELD_COIN, angle)
    linear_reference = scale_state(
        add_states(left_output, right_output), 1 / np.sqrt(2)
    )
    density_reference = {
        key: 0.5
        * (matter_density(left_output).get(key, 0.0) + matter_density(right_output).get(key, 0.0))
        for key in matter_density(left_output).keys() | matter_density(right_output).keys()
    }
    check(
        "separated source packets compose linearly without one-step density cross terms",
        state_residual(combined_output, linear_reference) < 3e-12
        and dictionary_residual(matter_density(combined_output), density_reference)
        < 3e-12,
        state_residual(combined_output, linear_reference),
    )

    local_state = rng.normal(size=64) + 1j * rng.normal(size=64)
    local_state /= np.linalg.norm(local_state)
    evolved = blocks.mediator_rotation @ local_state
    mediator_probability = float(
        np.vdot(evolved, blocks.mediator_number @ evolved).real
    )
    record_zero = np.asarray((1, 0), dtype=complex)
    record_plus = np.asarray((1, 1), dtype=complex) / np.sqrt(2)
    archived = tuple(
        float(
            np.vdot(
                np.kron(evolved, record),
                np.kron(blocks.mediator_number @ evolved, record),
            ).real
        )
        for record in (record_zero, record_plus)
    )
    check(
        "normalized spectator records neither multiply source nor mediator density",
        max(abs(value - mediator_probability) for value in archived) < 3e-12,
        archived,
    )


def mass_and_static_target_controls(species: c210.Species) -> None:
    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    check(
        "the mediator-deleted one-particle route retains the common-family mass fixture",
        abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12,
        {
            "analytic_mass": species.analytic_mass,
            "dispersion_mass": dispersion_mass,
            "rest_mass": c219.rest_mass(species),
        },
    )

    side = 9
    source = c211.point_source(side)
    coin_field = c216.solve_coin_field(source)
    scalar = c216.scalar_field(coin_field).real
    green = c211.solve_field(source)
    stiffness_residual = np.linalg.norm(
        c216.apply_stiffness(coin_field) - source[..., None] * c210.UNIFORM
    )
    target_residual = np.linalg.norm(scalar - 3 * green)
    check(
        "the same mediator coin retains the exact static scalar block 3 L^+",
        stiffness_residual < 3e-12 and target_residual < 3e-12,
        {
            "stiffness_residual": float(stiffness_residual),
            "three_L_plus_residual": float(target_residual),
        },
    )

    laplacian_source = 6 * source - sum(
        (
            np.roll(source, displacement, axis=axis)
            for axis in range(3)
            for displacement in (-1, 1)
        ),
        np.zeros_like(source),
    )
    dynamic_port = -laplacian_source / 6
    dynamic_static_response = 3 * c211.solve_field(dynamic_port)
    port_identity_residual = np.linalg.norm(dynamic_static_response + source / 2)
    live_join_residual = np.linalg.norm(dynamic_static_response - 3 * green)
    check(
        "the supplied additive Cycle-215 port/order is not the static 3 L^+ source",
        port_identity_residual < 3e-12 and live_join_residual > 1,
        {
            "port_identity_residual": float(port_identity_residual),
            "dynamic_to_static_residual": float(live_join_residual),
        },
    )

    shifted = c211.point_source(side, (3, 2, 1))
    combined_field = c216.solve_coin_field(source + shifted)
    separate_field = c216.solve_coin_field(source) + c216.solve_coin_field(shifted)
    check(
        "the static coin-field response composes and source deletion is exact",
        np.linalg.norm(combined_field - separate_field) < 3e-12
        and np.linalg.norm(c216.solve_coin_field(np.zeros_like(source))) < 3e-14,
        np.linalg.norm(combined_field - separate_field),
    )


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "probability/configuration current, not energy",
        "25 retained matter m2 plus 6 mediator m2",
        "selected hard-core extension",
        "global-blockade comparison",
        "not a sector restriction",
        "onsite signed source current",
        "one-edge matter transfer",
        "one-edge mediator transfer",
        "negative absorption current",
        "3 l^+",
        "1.3734550110467953",
        "one-particle mass fixture",
        "intrinsic contact",
        "all 24 proper-cubic frames",
        "kinematic recoil accounting",
        "sectorwise physical-m2",
        "not a prepared full-fock physical compiler",
        "supplied structure",
        "no no-go claim",
        "**authority:** none",
        "**audit:** unset",
    )
    missing = tuple(item for item in required if item not in text)
    check("note pins result, residual, semantics, and supplied structure", not missing, missing)


def main() -> int:
    species = c219.common_species(BETA)
    charge = c219.rest_mass(species)
    angle = MEDIATOR_COUPLING * charge
    note_contract()
    blocks = local_m2_and_contact_controls(species, angle)
    literal_gatewise_ledger_controls(species, angle)
    emission_absorption_and_recoil_controls(species, angle)
    covariance_composition_deletion_controls(species, angle, blocks)
    mass_and_static_target_controls(species)
    print(
        "DIAGNOSTIC",
        {
            "beta": BETA,
            "charge": charge,
            "mediator_coupling": MEDIATOR_COUPLING,
            "angle": angle,
            "matter_M2_per_cell_inherited": 25,
            "mediator_M2_per_cell": 6,
            "total_M2_per_cell": 31,
            "mapped_scalar_control_support_M2": 24,
            "combined_vertex_support_M2": 30,
            "each_mediator_edge_swap_support_M2": 2,
        },
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
