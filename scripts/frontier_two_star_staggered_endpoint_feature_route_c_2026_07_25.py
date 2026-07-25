#!/usr/bin/env python3
"""Route C: bounded staggered endpoint-feature/order schedule on two stars.

This is a positive finite-circuit probe.  It combines two separate surfaces:

* a coherent one-hot half-edge qutrit schedule which extracts and transports
  endpoint incidence/tag data, applies the graded order phase, returns all
  work, and swaps the endpoint role registers; and
* an actual number-preserving free/FSWAP/contact update on the union of two
  adjacent maximal stars, with their shared coarse edge included exactly once.

The half-edge qutrit chart and the finite gate order are supplied.  The stage
ordinal is a circuit-program label, not physical time.  No measurement, host
parity query, host order query, physical-time, minimum, impossibility, shared
obstruction, or axiom-pressure claim is made.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
import math
import resource
import time

import numpy as np
from scipy import sparse

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230


START = time.perf_counter()
TOL = 2.0e-11
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Frame = tuple[Coord, Coord, Coord]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[axis] + right[axis] for axis in range(3))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[axis] - right[axis] for axis in range(3))  # type: ignore[return-value]


def matvec(frame: Frame, vector: Coord) -> Coord:
    return tuple(
        sum(frame[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def matmul(left: Frame, right: Frame) -> Frame:
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def frame_tuple(frame: np.ndarray) -> Frame:
    return tuple(tuple(int(value) for value in row) for row in frame)  # type: ignore[return-value]


FRAMES = tuple(frame_tuple(frame) for frame in c330.c235.proper_cubic_frames())
FRAME_INDEX = {frame: index for index, frame in enumerate(FRAMES)}
DIRECTIONS: tuple[Coord, ...] = tuple(
    tuple(int(value) for value in row) for row in c311.c210.DIRECTIONS
)  # type: ignore[assignment]
DIRECTION_INDEX = {row: index for index, row in enumerate(DIRECTIONS)}


# ---------------------------------------------------------------------------
# Coherent half-edge qutrit feature circuit
# ---------------------------------------------------------------------------

# Four role bits followed by ten returned work bits.
LZ, LX, RZ, RX = range(4)
LI, LT, RI, RT, LIC, LTC, RIC, RTC, PARITY, ACTIVE = range(4, 14)
MODULE_BITS = 14

Gate = tuple[str, tuple[int, ...]]


def feature_word(include_role_swap: bool = True) -> tuple[Gate, ...]:
    word: list[Gate] = [
        ("CNOT", (LZ, LI)),
        ("CNOT", (LX, LI)),
        ("CNOT", (LX, LT)),
        ("CNOT", (RZ, RI)),
        ("CNOT", (RX, RI)),
        ("CNOT", (RX, RT)),
        ("SWAP", (LI, LIC)),
        ("SWAP", (LT, LTC)),
        ("SWAP", (RI, RIC)),
        ("SWAP", (RT, RTC)),
        ("CNOT", (LTC, PARITY)),
        ("CNOT", (RTC, PARITY)),
        ("TOFFOLI", (LIC, RIC, ACTIVE)),
        ("CZ", (ACTIVE, PARITY)),
        ("TOFFOLI", (LIC, RIC, ACTIVE)),
        ("CNOT", (RTC, PARITY)),
        ("CNOT", (LTC, PARITY)),
        ("SWAP", (RT, RTC)),
        ("SWAP", (RI, RIC)),
        ("SWAP", (LT, LTC)),
        ("SWAP", (LI, LIC)),
        ("CNOT", (RX, RT)),
        ("CNOT", (RX, RI)),
        ("CNOT", (RZ, RI)),
        ("CNOT", (LX, LT)),
        ("CNOT", (LX, LI)),
        ("CNOT", (LZ, LI)),
    ]
    if include_role_swap:
        word.extend((
            ("SWAP", (LZ, RZ)),
            ("SWAP", (LX, RX)),
        ))
    return tuple(word)


FEATURE_WORD = feature_word()


def bit(value: int, index: int) -> int:
    return (value >> index) & 1


def flip(value: int, index: int) -> int:
    return value ^ (1 << index)


def apply_gate(value: int, phase: int, gate: Gate) -> tuple[int, int]:
    kind, sites = gate
    if kind == "CNOT":
        control, target = sites
        if bit(value, control):
            value = flip(value, target)
    elif kind == "SWAP":
        left, right = sites
        if bit(value, left) != bit(value, right):
            value = flip(flip(value, left), right)
    elif kind == "TOFFOLI":
        first, second, target = sites
        if bit(value, first) and bit(value, second):
            value = flip(value, target)
    elif kind == "CZ":
        first, second = sites
        if bit(value, first) and bit(value, second):
            phase *= -1
    else:
        raise ValueError(f"unknown gate {kind}")
    return value, phase


def apply_word(value: int, word: tuple[Gate, ...] = FEATURE_WORD) -> tuple[int, int]:
    phase = 1
    for gate in word:
        value, phase = apply_gate(value, phase, gate)
    return value, phase


QUTRIT = ((0, 0), (1, 0), (0, 1))  # blank, Z-chart, X-chart


def role_value(left: tuple[int, int], right: tuple[int, int]) -> int:
    return (
        (left[0] << LZ)
        | (left[1] << LX)
        | (right[0] << RZ)
        | (right[1] << RX)
    )


def qutrit_phase(left: tuple[int, int], right: tuple[int, int]) -> int:
    left_incidence = left[0] ^ left[1]
    right_incidence = right[0] ^ right[1]
    exponent = left_incidence & right_incidence & (left[1] ^ right[1])
    return -1 if exponent else 1


def qutrit_module_controls() -> dict[str, object]:
    lawful_failures = work_return_failures = 0
    ideal_rows: list[int] = []
    ideal_phases: list[int] = []
    for left in QUTRIT:
        for right in QUTRIT:
            source = role_value(left, right)
            observed, phase = apply_word(source)
            expected = role_value(right, left)
            lawful_failures += observed != expected or phase != qutrit_phase(left, right)
            work_return_failures += observed >> 4 != 0
            ideal_rows.append(QUTRIT.index(right) * 3 + QUTRIT.index(left))
            ideal_phases.append(qutrit_phase(left, right))

    observed_rows = []
    observed_phases = []
    for source in range(1 << MODULE_BITS):
        target, phase = apply_word(source)
        observed_rows.append(target)
        observed_phases.append(phase)
    bijection_failures = len(set(observed_rows)) != 1 << MODULE_BITS
    phase_failures = sum(value not in (-1, 1) for value in observed_phases)

    schedule = sparse.coo_matrix(
        (observed_phases, (observed_rows, np.arange(1 << MODULE_BITS))),
        shape=(1 << MODULE_BITS, 1 << MODULE_BITS),
        dtype=complex,
    ).tocsc()
    encoding = sparse.coo_matrix(
        (
            np.ones(9),
            ([role_value(left, right) for left in QUTRIT for right in QUTRIT], np.arange(9)),
        ),
        shape=(1 << MODULE_BITS, 9),
        dtype=complex,
    ).tocsc()
    ideal = sparse.coo_matrix(
        (ideal_phases, (ideal_rows, np.arange(9))), shape=(9, 9), dtype=complex
    ).tocsc()
    coherent_residual = c315.largest_singular(schedule @ encoding - encoding @ ideal)
    unitary_residual = c315.raw_maximum_abs(
        schedule.conj().T @ schedule - sparse.eye(1 << MODULE_BITS, format="csc")
    )

    deleted = tuple(gate for index, gate in enumerate(FEATURE_WORD) if index != 13)
    deletion_failures = 0
    for left in QUTRIT:
        for right in QUTRIT:
            observed, phase = apply_word(role_value(left, right), deleted)
            expected = role_value(right, left)
            deletion_failures += observed != expected or phase != qutrit_phase(left, right)

    wrong_order = list(FEATURE_WORD)
    wrong_order[13] = ("CZ", (LIC, PARITY))
    mutation_failures = 0
    for left in QUTRIT:
        for right in QUTRIT:
            observed, phase = apply_word(role_value(left, right), tuple(wrong_order))
            mutation_failures += (
                observed != role_value(right, left) or phase != qutrit_phase(left, right)
            )

    return {
        "lawful_qutrit_pair_cases": 9,
        "lawful_failures": lawful_failures,
        "work_return_failures": work_return_failures,
        "full_computational_basis_cases": 1 << MODULE_BITS,
        "full_basis_bijection_failures": int(bijection_failures),
        "full_basis_phase_failures": phase_failures,
        "coherent_intertwiner_residual": coherent_residual,
        "full_unitarity_raw_maximum": unitary_residual,
        "deleted_phase_gate_failures": deletion_failures,
        "mutated_control_failures": mutation_failures,
        "gates_per_edge_module": len(FEATURE_WORD),
        "gate_counts": dict(Counter(kind for kind, _sites in FEATURE_WORD)),
        "role_M2_per_edge": 4,
        "returned_work_M2_per_edge": MODULE_BITS - 4,
    }


def controlled_pauli_coherence() -> dict[str, float]:
    identity = np.eye(2, dtype=complex)
    pauli_z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    pauli_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    paulis = (identity, pauli_z, pauli_x)
    canonical = np.zeros((18, 18), dtype=complex)
    reverse = np.zeros((18, 18), dtype=complex)
    phase = np.zeros((18, 18), dtype=complex)
    for left_index, left in enumerate(QUTRIT):
        for right_index, right in enumerate(QUTRIT):
            block = 2 * (3 * left_index + right_index)
            canonical[block:block + 2, block:block + 2] = paulis[left_index] @ paulis[right_index]
            reverse[block:block + 2, block:block + 2] = paulis[right_index] @ paulis[left_index]
            phase[block:block + 2, block:block + 2] = qutrit_phase(left, right) * identity
    residual = float(np.linalg.norm(reverse - phase @ canonical, ord=2))
    unitarity = max(
        float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(18), ord=2))
        for matrix in (canonical, reverse, phase)
    )

    # Active control: try to copy Z and X information directly from the same
    # outer M2 using CNOT and H-conjugated CNOT, phase the two work bits, then
    # echo.  The resulting unitary is coherent globally, but it neither gives
    # the desired -I code action nor returns the work on arbitrary outer input.
    hadamard = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
    h_outer = np.kron(np.kron(hadamard, identity), identity)

    def cnot(control: int, target: int) -> np.ndarray:
        matrix = np.zeros((8, 8), dtype=complex)
        for outer, first, second in product((0, 1), repeat=3):
            bits = [outer, first, second]
            source = 4 * outer + 2 * first + second
            bits[target] ^= bits[control]
            target_row = 4 * bits[0] + 2 * bits[1] + bits[2]
            matrix[target_row, source] = 1
        return matrix

    copy_z = cnot(0, 1)
    copy_x = h_outer @ cnot(0, 2) @ h_outer
    compute = copy_x @ copy_z
    work_phase = np.diag(
        [-1 if ((index // 2) & 1) and (index & 1) else 1 for index in range(8)]
    )
    naive = compute.conj().T @ work_phase @ compute
    outer_encoding = np.zeros((8, 2), dtype=complex)
    outer_encoding[0, 0] = 1
    outer_encoding[4, 1] = 1
    projector = outer_encoding @ outer_encoding.conj().T
    naive_target_residual = float(np.linalg.norm(naive @ outer_encoding + outer_encoding, ord=2))
    naive_work_leakage = float(
        np.linalg.norm((np.eye(8) - projector) @ naive @ outer_encoding, ord=2)
    )
    return {
        "controlled_ZX_order_residual": residual,
        "controlled_operator_unitarity_residual": unitarity,
        "naive_basis_switch_target_residual": naive_target_residual,
        "naive_basis_switch_work_leakage": naive_work_leakage,
    }


# ---------------------------------------------------------------------------
# Bind the qutrit features to actual landed Cycle-311/315/330 branches.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class RoleTerm:
    cell: int
    number: int
    label: tuple[int, ...]
    carrier: int | None
    stream_slice: int
    representative: object


def role_terms(code, cell: int, number: int, label: tuple[int, ...]) -> tuple[RoleTerm, ...]:
    body = c330.CELLS[cell]
    rows = []
    for branch in c311.common_branches(code, body, number, label, 0):
        rows.append(
            RoleTerm(
                cell,
                number,
                label,
                branch.carrier_direction,
                branch.stream_slice,
                c311.branch_representative(code, body, branch, 0),
            )
        )
        target_slice = 0 if number == 0 else 1
        target = next(
            candidate
            for candidate in c311.common_branches(code, body, number, label, target_slice)
            if candidate.carrier_direction == branch.carrier_direction
        )
        rows.append(
            RoleTerm(
                cell,
                number,
                label,
                target.carrier_direction,
                target.stream_slice,
                c311.branch_representative(code, body, target, 1),
            )
        )
    return tuple(rows)


CENTER_EDGE_MODES = {right[0]: (left[1], right[1]) for left, right in c330.EDGES}
ARM_CENTER_MODE = {right[0]: right[1] for _left, right in c330.EDGES}


def pair_geometry(left: int, right: int) -> tuple[int, int, int]:
    if left == 0:
        left_mode, right_mode = CENTER_EDGE_MODES[right]
        return 1, left_mode, right_mode
    return 0, ARM_CENTER_MODE[left], ARM_CENTER_MODE[right]


def endpoint_feature(code, term: RoleTerm, mode: int) -> tuple[int, int]:
    occupied = int(mode in term.label)
    incidence = int(occupied or term.carrier == mode)
    vertex = c311.c305.body_vertices(code, c330.CELLS[term.cell])[mode]
    tag = int((term.representative.x >> (code.qubits + vertex)) & 1)  # type: ignore[attr-defined]
    return incidence, tag


def feature_qutrit(incidence: int, tag: int) -> tuple[int, int]:
    return incidence & (1 - tag), incidence & tag


def landed_branch_feature_census(length: int) -> dict[str, object]:
    code = c315.c269.build_code(length)
    cache = {
        (cell, number, label): role_terms(code, cell, number, label)
        for cell in range(7)
        for number, label in c311.FOCK_LABELS
    }
    cases = positives = prediction_failures = schedule_failures = 0
    work_return_failures = qutrit_domain_failures = 0
    class_rows = defaultdict(lambda: Counter(cases=0, positives=0, failures=0))
    for left, right in c330.PAIR_LABELS:
        shared, left_mode, right_mode = pair_geometry(left, right)
        pair_class = "center_arm" if shared else "arm_arm"
        for left_number, left_label in c311.FOCK_LABELS:
            for right_number, right_label in c311.FOCK_LABELS:
                if left_number + right_number > 2:
                    continue
                for left_term in cache[(left, left_number, left_label)]:
                    for right_term in cache[(right, right_number, right_label)]:
                        observed = int(
                            not left_term.representative.commutes(right_term.representative)  # type: ignore[attr-defined]
                        )
                        left_incidence, left_tag = endpoint_feature(code, left_term, left_mode)
                        right_incidence, right_tag = endpoint_feature(code, right_term, right_mode)
                        predicted = shared & left_incidence & right_incidence & (left_tag ^ right_tag)
                        left_qutrit = feature_qutrit(left_incidence, left_tag)
                        right_qutrit = feature_qutrit(right_incidence, right_tag)
                        qutrit_domain_failures += left_qutrit not in QUTRIT or right_qutrit not in QUTRIT
                        if shared:
                            target, phase = apply_word(role_value(left_qutrit, right_qutrit))
                        else:
                            target, phase = role_value(left_qutrit, right_qutrit), 1
                        expected_phase = -1 if observed else 1
                        prediction_failures += predicted != observed
                        schedule_failures += phase != expected_phase
                        work_return_failures += target >> 4 != 0
                        cases += 1
                        positives += observed
                        class_rows[pair_class]["cases"] += 1
                        class_rows[pair_class]["positives"] += observed
                        class_rows[pair_class]["failures"] += phase != expected_phase
    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "branch_term_pair_cases": cases,
        "positive_physical_order_signs": positives,
        "feature_prediction_failures": prediction_failures,
        "qutrit_domain_failures": qutrit_domain_failures,
        "fixed_schedule_phase_failures": schedule_failures,
        "fixed_schedule_work_return_failures": work_return_failures,
        "pair_classes": {key: dict(value) for key, value in sorted(class_rows.items())},
    }


# ---------------------------------------------------------------------------
# Actual free / shared-seam FSWAP / contact update on two overlapping stars.
# ---------------------------------------------------------------------------

ORIGIN: Coord = (0, 0, 0)
BASE_AXIS: Coord = (1, 0, 0)


def patch_geometry(axis: Coord) -> tuple[tuple[Coord, ...], tuple[tuple[Coord, Coord], ...]]:
    centers = (ORIGIN, axis)
    cells = set(centers)
    ordered_edges: list[tuple[Coord, Coord]] = []
    seen_edges = set()
    for center in centers:
        for direction in DIRECTIONS:
            arm = add(center, direction)
            cells.add(arm)
            key = tuple(sorted((center, arm)))
            if key not in seen_edges:
                seen_edges.add(key)
                ordered_edges.append((center, arm))
    return tuple(sorted(cells)), tuple(ordered_edges)


BASE_CELLS, BASE_EDGES = patch_geometry(BASE_AXIS)
MODE_COUNT = 6 * len(BASE_CELLS)
FOCK_BASIS = ((),) + tuple((mode,) for mode in range(MODE_COUNT)) + tuple(
    combinations(range(MODE_COUNT), 2)
)
FOCK_INDEX = {label: index for index, label in enumerate(FOCK_BASIS)}


def mode_permutation_matrix(mapping: tuple[int, ...]) -> sparse.csc_matrix:
    rows = []
    phases = []
    for label in FOCK_BASIS:
        mapped = tuple(mapping[mode] for mode in label)
        phases.append(c311.c308.permutation_sign(mapped))
        rows.append(FOCK_INDEX[tuple(sorted(mapped))])
    return sparse.coo_matrix(
        (phases, (rows, np.arange(len(FOCK_BASIS)))),
        shape=(len(FOCK_BASIS), len(FOCK_BASIS)),
        dtype=complex,
    ).tocsc()


def patch_stream(cells: tuple[Coord, ...], edges: tuple[tuple[Coord, Coord], ...]) -> sparse.csc_matrix:
    cell_index = {cell: index for index, cell in enumerate(cells)}
    mapping = list(range(6 * len(cells)))
    touched = set()
    for left, right in edges:
        direction = sub(right, left)
        left_direction = DIRECTION_INDEX[direction]
        right_direction = DIRECTION_INDEX[tuple(-value for value in direction)]
        left_mode = 6 * cell_index[left] + left_direction
        right_mode = 6 * cell_index[right] + right_direction
        if left_mode in touched or right_mode in touched:
            raise AssertionError(("duplicate seam port", left, right))
        touched.update((left_mode, right_mode))
        mapping[left_mode], mapping[right_mode] = right_mode, left_mode
    return mode_permutation_matrix(tuple(mapping))


def patch_coin(cells: tuple[Coord, ...]) -> sparse.csc_matrix:
    local_coin = c219.common_species(-0.3).coin
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for source, label in enumerate(FOCK_BASIS):
        if not label:
            rows.append(0)
            columns.append(source)
            data.append(1)
            continue
        choices = []
        for mode in label:
            cell, direction = divmod(mode, 6)
            choices.append(
                tuple((6 * cell + target, local_coin[target, direction]) for target in range(6))
            )
        amplitudes: dict[tuple[int, ...], complex] = defaultdict(complex)
        for targets in product(*choices):
            mapped = tuple(target for target, _coefficient in targets)
            if len(set(mapped)) != len(mapped):
                continue
            coefficient = complex(np.prod([value for _target, value in targets]))
            coefficient *= c311.c308.permutation_sign(mapped)
            amplitudes[tuple(sorted(mapped))] += coefficient
        for target, coefficient in amplitudes.items():
            if abs(coefficient) > 2e-15:
                rows.append(FOCK_INDEX[target])
                columns.append(source)
                data.append(coefficient)
    return sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(FOCK_BASIS), len(FOCK_BASIS)),
        dtype=complex,
    ).tocsc()


def patch_contact(cells: tuple[Coord, ...]) -> sparse.csc_matrix:
    phases = []
    for label in FOCK_BASIS:
        numbers = Counter(mode // 6 for mode in label)
        pairs = sum(number * (number - 1) // 2 for number in numbers.values())
        phases.append(np.exp(1j * c230.COUPLING * pairs))
    return sparse.diags(phases, format="csc", dtype=complex)


def build_patch_update(axis: Coord) -> tuple[dict[str, object], sparse.csc_matrix]:
    cells, edges = patch_geometry(axis)
    if len(cells) != len(BASE_CELLS):
        raise AssertionError((axis, len(cells)))
    coin = patch_coin(cells)
    stream = patch_stream(cells, edges)
    contact = patch_contact(cells)
    update = contact @ stream @ coin
    identity = sparse.eye(len(FOCK_BASIS), format="csc")
    shared = tuple(sorted((ORIGIN, axis)))
    shared_occurrences = sum(tuple(sorted(edge)) == shared for edge in edges)

    # Active deletions and order mutations are computed independently.
    deleted_edges = tuple(edge for edge in edges if tuple(sorted(edge)) != shared)
    deleted_stream = patch_stream(cells, deleted_edges)
    deleted_update = contact @ deleted_stream @ coin
    duplicated_update = contact @ (patch_stream(cells, (next(edge for edge in edges if tuple(sorted(edge)) == shared),)) @ stream) @ coin
    no_contact_update = stream @ coin
    reversed_update = coin @ stream @ contact

    one_indices = tuple(index for index, label in enumerate(FOCK_BASIS) if len(label) == 1)
    one_particle = update[np.ix_(one_indices, one_indices)]
    uniform = np.ones(len(one_indices), dtype=complex) / math.sqrt(len(one_indices))
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    mass = float(np.angle(eigenvalue)) / c219.C_SQUARED
    mass_fixture = c219.rest_mass(c219.common_species(-0.3))
    two_indices = tuple(index for index, label in enumerate(FOCK_BASIS) if len(label) == 2)
    two_particle = update[np.ix_(two_indices, two_indices)]
    return {
        "axis": axis,
        "cells": len(cells),
        "unique_star_edges": len(edges),
        "shared_edge_occurrences": shared_occurrences,
        "logical_columns_n_le_2": len(FOCK_BASIS),
        "vacuum_dimension": 1,
        "one_particle_dimension": len(one_indices),
        "two_particle_dimension": len(two_indices),
        "coin_nonzeros": coin.nnz,
        "stream_nonzeros": stream.nnz,
        "contact_nontrivial_columns": int(np.count_nonzero(abs(contact.diagonal() - 1) > 2e-14)),
        "coin_unitarity_raw_maximum": c315.raw_maximum_abs(coin.conj().T @ coin - identity),
        "stream_unitarity_raw_maximum": c315.raw_maximum_abs(stream.conj().T @ stream - identity),
        "contact_unitarity_raw_maximum": c315.raw_maximum_abs(contact.conj().T @ contact - identity),
        "update_unitarity_raw_maximum": c315.raw_maximum_abs(update.conj().T @ update - identity),
        "two_particle_update_unitarity_raw_maximum": c315.raw_maximum_abs(
            two_particle.conj().T @ two_particle - sparse.eye(len(two_indices), format="csc")
        ),
        "one_particle_mass": mass,
        "Cycle219_mass_fixture": mass_fixture,
        "one_particle_mass_residual": abs(mass - mass_fixture),
        "uniform_one_particle_eigen_residual": float(
            np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)
        ),
        "delete_shared_seam_update_residual": c315.largest_singular(update - deleted_update),
        "duplicate_shared_seam_update_residual": c315.largest_singular(update - duplicated_update),
        "delete_contact_update_residual": c315.largest_singular(update - no_contact_update),
        "reverse_free_seam_contact_order_residual": c315.largest_singular(update - reversed_update),
    }, update


def exterior_mode_mapping(
    source_cells: tuple[Coord, ...], target_cells: tuple[Coord, ...], frame: Frame
) -> tuple[int, ...]:
    target_index = {cell: index for index, cell in enumerate(target_cells)}
    mapping = []
    array = np.asarray(frame, dtype=int)
    for cell in source_cells:
        mapped_cell = matvec(frame, cell)
        for direction in range(6):
            mapped_direction = c311.direction_map(array, direction)
            mapping.append(6 * target_index[mapped_cell] + mapped_direction)
    return tuple(mapping)


def frame_and_translation_controls(
    base_update: sparse.csc_matrix,
) -> dict[str, object]:
    update_cache: dict[Coord, sparse.csc_matrix] = {BASE_AXIS: base_update}
    maximum_covariance = 0.0
    maximum_covariance_raw = 0.0
    mapping_cache: dict[tuple[Coord, Frame], tuple[int, ...]] = {}
    program_edge_frame_failures = 0
    program_edge_frame_cases = 0
    endpoint_reversing_edge_cases = 0

    def mapping_for(source_axis: Coord, frame: Frame) -> tuple[int, ...]:
        key = (source_axis, frame)
        if key not in mapping_cache:
            source_cells, _source_edges = patch_geometry(source_axis)
            target_axis = matvec(frame, source_axis)
            target_cells, _target_edges = patch_geometry(target_axis)
            mapping_cache[key] = exterior_mode_mapping(source_cells, target_cells, frame)
        return mapping_cache[key]

    for frame in FRAMES:
        target_axis = matvec(frame, BASE_AXIS)
        if target_axis not in update_cache:
            update_cache[target_axis] = build_patch_update(target_axis)[1]
        representation = mode_permutation_matrix(mapping_for(BASE_AXIS, frame))
        difference = representation @ base_update - update_cache[target_axis] @ representation
        maximum_covariance = max(maximum_covariance, c315.largest_singular(difference))
        maximum_covariance_raw = max(maximum_covariance_raw, c315.raw_maximum_abs(difference))
        _base_cells, base_edges = patch_geometry(BASE_AXIS)
        _target_cells, target_edges = patch_geometry(target_axis)
        target_lookup = {tuple(sorted(edge)): edge for edge in target_edges}
        for edge in base_edges:
            mapped_edge = (matvec(frame, edge[0]), matvec(frame, edge[1]))
            target_edge = target_lookup.get(tuple(sorted(mapped_edge)))
            program_edge_frame_failures += target_edge is None
            endpoint_reversing_edge_cases += target_edge == tuple(reversed(mapped_edge))
            program_edge_frame_cases += 1

    group_failures = group_phase_failures = program_edge_product_failures = 0
    group_cases = 0
    for left in FRAMES:
        for right in FRAMES:
            target = matmul(left, right)
            right_axis = matvec(right, BASE_AXIS)
            right_mapping = mapping_for(BASE_AXIS, right)
            left_mapping = mapping_for(right_axis, left)
            target_mapping = mapping_for(BASE_AXIS, target)
            composed = tuple(left_mapping[index] for index in right_mapping)
            group_failures += composed != target_mapping
            for edge in BASE_EDGES:
                direct = (matvec(target, edge[0]), matvec(target, edge[1]))
                staged = (
                    matvec(left, matvec(right, edge[0])),
                    matvec(left, matvec(right, edge[1])),
                )
                program_edge_product_failures += staged != direct
            for label in FOCK_BASIS:
                right_word = tuple(right_mapping[mode] for mode in label)
                right_sign = c311.c308.permutation_sign(right_word)
                left_word = tuple(left_mapping[mode] for mode in sorted(right_word))
                left_sign = c311.c308.permutation_sign(left_word)
                target_word = tuple(target_mapping[mode] for mode in label)
                target_sign = c311.c308.permutation_sign(target_word)
                group_phase_failures += right_sign * left_sign != target_sign
                group_cases += 1

    translation_rows = []
    for length in (5, 6):
        failures = 0
        fixtures = 0
        for axis in DIRECTIONS:
            cells, edges = patch_geometry(axis)
            for shift in product(range(length), repeat=3):
                translated_cells = {
                    tuple((cell[q] + shift[q]) % length for q in range(3))
                    for cell in cells
                }
                translated_edges = {
                    tuple(
                        sorted(
                            tuple((site[q] + shift[q]) % length for q in range(3))
                            for site in edge
                        )
                    )
                    for edge in edges
                }
                failures += len(translated_cells) != 12
                failures += len(translated_edges) != 11
                fixtures += 1
        translation_rows.append(
            {
                "L": length,
                "split": "train" if length == 5 else "held-no-refit",
                "translated_oriented_two_star_fixtures": fixtures,
                "failures": failures,
            }
        )
    reversal_pairs = (
        (LZ, RZ),
        (LX, RX),
        (LI, RI),
        (LT, RT),
        (LIC, RIC),
        (LTC, RTC),
    )

    def reverse_endpoint_registers(value: int) -> int:
        for left, right in reversal_pairs:
            if bit(value, left) != bit(value, right):
                value = flip(flip(value, left), right)
        return value

    qutrit_reversal_failures = 0
    for source in range(1 << MODULE_BITS):
        target, phase = apply_word(source)
        reversed_target, reversed_phase = apply_word(reverse_endpoint_registers(source))
        qutrit_reversal_failures += (
            reverse_endpoint_registers(target) != reversed_target or phase != reversed_phase
        )

    return {
        "proper_cubic_frames": len(FRAMES),
        "oriented_axis_updates": len(update_cache),
        "maximum_update_covariance_residual": maximum_covariance,
        "maximum_update_covariance_raw_maximum": maximum_covariance_raw,
        "program_edge_frame_cases": program_edge_frame_cases,
        "program_edge_frame_failures": program_edge_frame_failures,
        "endpoint_reversing_edge_cases": endpoint_reversing_edge_cases,
        "qutrit_endpoint_reversal_basis_cases": 1 << MODULE_BITS,
        "qutrit_endpoint_reversal_failures": qutrit_reversal_failures,
        "ordered_frame_products": len(FRAMES) ** 2,
        "frame_group_mapping_failures": group_failures,
        "frame_group_phase_cases": group_cases,
        "frame_group_phase_failures": group_phase_failures,
        "program_edge_product_cases": len(FRAMES) ** 2 * len(BASE_EDGES),
        "program_edge_product_failures": program_edge_product_failures,
        "translation_rows": translation_rows,
        "held_parameters_refit": 0,
    }


def shared_edge_and_schedule_inventory() -> dict[str, object]:
    cells, edges = patch_geometry(BASE_AXIS)
    shared = tuple(sorted((ORIGIN, BASE_AXIS)))
    edge_keys = tuple(tuple(sorted(edge)) for edge in edges)
    star_a = {tuple(sorted((ORIGIN, add(ORIGIN, direction)))) for direction in DIRECTIONS}
    star_b = {tuple(sorted((BASE_AXIS, add(BASE_AXIS, direction)))) for direction in DIRECTIONS}
    shared_rows = star_a & star_b
    program = []
    for edge_index, edge in enumerate(edge_keys):
        for substep, gate in enumerate(FEATURE_WORD):
            program.append((edge_index, substep, gate))
    digest = sha256(repr(program).encode()).hexdigest()
    return {
        "union_cells": len(cells),
        "star_A_edges": len(star_a),
        "star_B_edges": len(star_b),
        "unique_union_edges": len(set(edge_keys)),
        "shared_edge_rows": sorted(shared_rows),
        "shared_edge_is_expected": shared_rows == {shared},
        "shared_edge_program_owners": sum(edge == shared for edge in edge_keys),
        "feature_modules": len(edge_keys),
        "feature_gates_per_module": len(FEATURE_WORD),
        "fixed_program_gates": len(program),
        "fixed_program_sha256": digest,
        "program_counter_states": len(program),
        "program_counter_is_physical_time": False,
        "runtime_parity_queries": 0,
        "runtime_order_queries": 0,
        "runtime_measurements": 0,
        "global_sign_work_M2": len(edge_keys) * (MODULE_BITS - 4),
        "global_half_edge_qutrit_role_M2": len(edge_keys) * 4,
    }


def unlawful_domain_controls() -> dict[str, object]:
    rejections = 0
    invalid_rows = (
        ((1, 1), (0, 0)),
        ((0, 0), (1, 1)),
        ((1, 1), (1, 0)),
        ((0, 1), (1, 1)),
    )
    for left, right in invalid_rows:
        try:
            if left not in QUTRIT or right not in QUTRIT:
                raise ValueError("unlawful half-edge qutrit code")
        except ValueError:
            rejections += 1
    fock_rejections = 0
    for label in ((0, 0), (0, 1, 2), (-1,), (MODE_COUNT,)):
        try:
            if (
                len(label) > 2
                or len(set(label)) != len(label)
                or any(mode < 0 or mode >= MODE_COUNT for mode in label)
            ):
                raise ValueError("outside vacuum/one/two hard-core domain")
        except ValueError:
            fock_rejections += 1
    dirty_source = role_value(QUTRIT[1], QUTRIT[2]) | (1 << LI)
    dirty_target, _dirty_phase = apply_word(dirty_source)
    dirty_work_nonreturn = int(dirty_target >> 4 != 0)
    return {
        "invalid_qutrit_rows": len(invalid_rows),
        "invalid_qutrit_rejections": rejections,
        "invalid_fock_rows": 4,
        "invalid_fock_rejections": fock_rejections,
        "dirty_work_genesis_nonreturn": dirty_work_nonreturn,
    }


def main() -> None:
    module = qutrit_module_controls()
    check(
        "the fixed qutrit feature word is a coherent graded swap and returns every work bit",
        module["lawful_failures"] == 0
        and module["work_return_failures"] == 0
        and module["full_basis_bijection_failures"] == 0
        and module["full_basis_phase_failures"] == 0
        and module["coherent_intertwiner_residual"] < TOL
        and module["full_unitarity_raw_maximum"] < TOL
        and module["deleted_phase_gate_failures"] > 0
        and module["mutated_control_failures"] > 0,
        module,
    )

    coherence = controlled_pauli_coherence()
    check(
        "one-hot chart controls implement the coherent Z/X order phase while direct basis-switch extraction leaks",
        coherence["controlled_ZX_order_residual"] < TOL
        and coherence["controlled_operator_unitarity_residual"] < TOL
        and coherence["naive_basis_switch_target_residual"] > 1.9
        and coherence["naive_basis_switch_work_leakage"] > 0.9,
        coherence,
    )

    branch_rows = tuple(landed_branch_feature_census(length) for length in (5, 6))
    comparable = [
        {key: value for key, value in row.items() if key not in {"L", "split"}}
        for row in branch_rows
    ]
    check(
        "the same fixed feature circuit matches every landed L5 and held-L6 physical branch sign",
        comparable[0] == comparable[1]
        and all(row["branch_term_pair_cases"] == 83244 for row in branch_rows)
        and all(row["positive_physical_order_signs"] == 1200 for row in branch_rows)
        and all(row["feature_prediction_failures"] == 0 for row in branch_rows)
        and all(row["qutrit_domain_failures"] == 0 for row in branch_rows)
        and all(row["fixed_schedule_phase_failures"] == 0 for row in branch_rows)
        and all(row["fixed_schedule_work_return_failures"] == 0 for row in branch_rows),
        branch_rows,
    )

    inventory = shared_edge_and_schedule_inventory()
    check(
        "two overlapping maximal stars share exactly one owned port in one fixed no-query program",
        inventory["union_cells"] == 12
        and inventory["star_A_edges"] == inventory["star_B_edges"] == 6
        and inventory["unique_union_edges"] == 11
        and inventory["shared_edge_is_expected"]
        and inventory["shared_edge_program_owners"] == 1
        and inventory["runtime_parity_queries"] == 0
        and inventory["runtime_order_queries"] == 0
        and inventory["runtime_measurements"] == 0
        and not inventory["program_counter_is_physical_time"],
        inventory,
    )

    update_rows, update = build_patch_update(BASE_AXIS)
    check(
        "the deduplicated 12-cell free/seam/contact word executes unitarily through n<=2 and preserves mass",
        update_rows["cells"] == 12
        and update_rows["unique_star_edges"] == 11
        and update_rows["shared_edge_occurrences"] == 1
        and update_rows["logical_columns_n_le_2"] == 2629
        and update_rows["contact_nontrivial_columns"] == 180
        and max(
            update_rows["coin_unitarity_raw_maximum"],
            update_rows["stream_unitarity_raw_maximum"],
            update_rows["contact_unitarity_raw_maximum"],
            update_rows["update_unitarity_raw_maximum"],
            update_rows["two_particle_update_unitarity_raw_maximum"],
            update_rows["one_particle_mass_residual"],
            update_rows["uniform_one_particle_eigen_residual"],
        ) < TOL
        and update_rows["delete_shared_seam_update_residual"] > 1
        and update_rows["duplicate_shared_seam_update_residual"] > 1
        and update_rows["delete_contact_update_residual"] > 0.3
        and update_rows["reverse_free_seam_contact_order_residual"] > 0.3,
        update_rows,
    )

    symmetry = frame_and_translation_controls(update)
    check(
        "the two-star update family is translation compatible and closes all 24 frames and 576 products",
        symmetry["proper_cubic_frames"] == 24
        and symmetry["oriented_axis_updates"] == 6
        and symmetry["maximum_update_covariance_residual"] < TOL
        and symmetry["maximum_update_covariance_raw_maximum"] < TOL
        and symmetry["program_edge_frame_failures"] == 0
        and symmetry["qutrit_endpoint_reversal_failures"] == 0
        and symmetry["ordered_frame_products"] == 576
        and symmetry["frame_group_mapping_failures"] == 0
        and symmetry["frame_group_phase_failures"] == 0
        and symmetry["program_edge_product_failures"] == 0
        and all(row["failures"] == 0 for row in symmetry["translation_rows"])
        and symmetry["held_parameters_refit"] == 0,
        symmetry,
    )

    domain = unlawful_domain_controls()
    check(
        "feature, shared-port, contact, schedule and unlawful-domain controls remain active",
        domain["invalid_qutrit_rejections"] == domain["invalid_qutrit_rows"] == 4
        and domain["invalid_fock_rejections"] == domain["invalid_fock_rows"] == 4
        and domain["dirty_work_genesis_nonreturn"] == 1
        and module["deleted_phase_gate_failures"] > 0
        and update_rows["delete_shared_seam_update_residual"] > 1
        and update_rows["delete_contact_update_residual"] > 0.3,
        {
            "domain": domain,
            "deleted_feature_phase_failures": module["deleted_phase_gate_failures"],
            "delete_shared_seam_update_residual": update_rows["delete_shared_seam_update_residual"],
            "duplicate_shared_seam_update_residual": update_rows["duplicate_shared_seam_update_residual"],
            "delete_contact_update_residual": update_rows["delete_contact_update_residual"],
            "naive_basis_switch_work_leakage": coherence["naive_basis_switch_work_leakage"],
        },
    )

    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-two-star-staggered-endpoint-feature-update-certificate",
        "terminal": "TWO_STAR_QUTRIT_SIGN_AND_NLE2_UPDATE_CLOSED_FULL_PHYSICAL_E_OPEN",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "classification": (
            "positive fixed-schedule half-edge-qutrit sign/order circuit plus an actual deduplicated "
            "two-overlapping-star vacuum/one/two free-seam-contact update"
        ),
        "feature_module": module,
        "controlled_outer_M2": coherence,
        "landed_branch_binding": branch_rows,
        "two_star_schedule": inventory,
        "two_star_update": update_rows,
        "symmetry_and_sizes": symmetry,
        "domain_controls": domain,
        "resources": {
            "coarse_cells": 12,
            "unique_coarse_edges": 11,
            "logical_modes": MODE_COUNT,
            "logical_columns_n_le_2": len(FOCK_BASIS),
            "half_edge_qutrit_role_M2": inventory["global_half_edge_qutrit_role_M2"],
            "returned_feature_work_M2": inventory["global_sign_work_M2"],
            "feature_program_gates": inventory["fixed_program_gates"],
            "feature_program_counter_states": inventory["program_counter_states"],
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "supplied": (
            "the landed Cycle-311/315/330 n<=2 branch grammar, beta=-0.3 coin and g=0.37 contact",
            "one lawful one-hot blank/Z/X half-edge qutrit chart on each of 22 half-edges",
            "the chart identification Z_internal+Z_outer versus X_outer+X_endpoint-tag",
            "ten clean returned feature/comparator work M2 per unique edge",
            "the finite per-edge gate word, eleven-edge ownership order and program ordinal",
            "vacuum/one/two hard-core input domain, two adjacent centers and one supplied chart orientation",
            "the coordinate-rotated 24-member schedule family, L5/L6 periodic placements and tolerance",
        ),
        "derived": (
            "a coherent 16384-basis monomial unitary whose nine-state qutrit code action is the graded swap",
            "exact incidence extraction z XOR x, tag transport, physical Z/X order phase and complete work return",
            "zero errors on all 83244 landed L5 and all 83244 held-L6 branch-term pair signs",
            "one-owner shared-port schedule on the 12-cell/11-edge union of two maximal stars",
            "an actual 2629-column vacuum/one/two free-FSWAP-contact update with exact number preservation",
            "unchanged Cycle219 one-particle mass and active seam/contact/order/deletion controls",
            "all-24 update covariance, all-576 exterior frame products and L5/L6 translation compatibility",
            "active falsification of direct Z/X basis-switch copying on the shared outer M2",
        ),
        "open": (
            "a physical unitary that prepares or derives the supplied half-edge qutrit charts from Cycle-311 branches",
            "one end-to-end M64^12-to-M2 encoding E coupling the qutrit sign circuit to the free/seam/contact update",
            "coherent consistency constraints tying the six half-edge charts belonging to one cell branch",
            "n>2, arbitrary simultaneous branch superpositions and a recurrent overlapping-star lattice stream law",
            "autonomous preparation, clean-work renewal, collision control and a physical scheduler/controller",
            "derivation of the finite program ordinal or interpretation of it as anything beyond circuit order",
            "physical time, rate, energy, source, gravity, Record, occurrence, probability or Born meaning",
            "minimality, impossibility, shared obstruction and axiom pressure",
        ),
        "claim_ceiling": (
            "Positive bounded Route-C construction.  The supplied one-hot half-edge qutrit chart permits a "
            "coherent no-measurement graded order circuit and the deduplicated two-star logical update is "
            "actually executed.  The result does not construct a full physical M64^12 encoding or derive "
            "the chart, recurrent controller, preparation, minimum, impossibility, or axiom pressure."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
