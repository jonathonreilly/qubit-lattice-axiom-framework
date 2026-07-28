#!/usr/bin/env python3
"""Cycle-721 direct local encoded-input Clifford port.

This runner deliberately does not reconstruct the transient mixed-gauge V_s
tableau.  It tests the direct dictionary-level coupling: a six-mode live input
bank co-located with a declared port cell is exchanged with that cell's matter
register, first on the local even-CAR generators and then on incident seam
bilinears.
"""

from __future__ import annotations

AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/CAR_BELL_INPUT_PHYSICAL_M2_COMPILER_CYCLE721_BOUNDED_"
    "THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "docs/CAR_BELL_INPUT_PHYSICAL_M2_COMPILER_CYCLE721_BOUNDED_THEOREM_NOTE_2026-07-28.md",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

from collections import Counter
from dataclasses import dataclass
from itertools import combinations, permutations, product
import json
import time

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P


@dataclass(frozen=True)
class Row:
    """Integer Pauli row i^phase X^x Z^z."""

    phase: int = 0
    x: int = 0
    z: int = 0

    def fields(self) -> tuple[int, int, int]:
        return self.phase % 4, self.x, self.z


@dataclass(frozen=True)
class Gate:
    kind: str
    control: int
    target: int = -1
    pauli: Row = Row()


def row(pauli) -> Row:
    return Row(pauli.phase % 4, pauli.x, pauli.z)


def multiply(left: Row, right: Row) -> Row:
    return Row(
        (
            left.phase
            + right.phase
            + 2 * (left.z & right.x).bit_count()
        )
        % 4,
        left.x ^ right.x,
        left.z ^ right.z,
    )


def product_rows(rows) -> Row:
    output = Row()
    for item in rows:
        output = multiply(output, item)
    return output


def anticommutes(left: Row, right: Row) -> int:
    return (
        (left.x & right.z).bit_count()
        + (left.z & right.x).bit_count()
    ) & 1


def single_x(qubit: int) -> Row:
    return Row(x=1 << qubit)


def single_z(qubit: int) -> Row:
    return Row(z=1 << qubit)


def generator_image(gate: Gate, kind: str, qubit: int) -> Row:
    base = single_x(qubit) if kind == "X" else single_z(qubit)
    if gate.kind == "H":
        if qubit != gate.control:
            return base
        return single_z(qubit) if kind == "X" else single_x(qubit)
    if gate.kind == "CNOT":
        c, t = gate.control, gate.target
        if kind == "X" and qubit == c:
            return Row(x=(1 << c) | (1 << t))
        if kind == "Z" and qubit == t:
            return Row(z=(1 << c) | (1 << t))
        return base
    if gate.kind == "CZ":
        a, b = gate.control, gate.target
        if kind == "X" and qubit == a:
            return Row(x=1 << a, z=1 << b)
        if kind == "X" and qubit == b:
            return Row(x=1 << b, z=1 << a)
        return base
    if gate.kind == "CP":
        c = gate.control
        if kind == "X" and qubit == c:
            return multiply(single_x(c), gate.pauli)
        if qubit == c:
            return base
        if anticommutes(base, gate.pauli):
            return multiply(single_z(c), base)
        return base
    raise ValueError(f"unknown gate {gate.kind}")


def conjugate_gate(input_row: Row, gate: Gate) -> Row:
    """Conjugate by one Clifford using exact signed generator images."""
    output = Row(phase=input_row.phase % 4)
    bits = input_row.x
    while bits:
        low = bits & -bits
        qubit = low.bit_length() - 1
        output = multiply(output, generator_image(gate, "X", qubit))
        bits ^= low
    bits = input_row.z
    while bits:
        low = bits & -bits
        qubit = low.bit_length() - 1
        output = multiply(output, generator_image(gate, "Z", qubit))
        bits ^= low
    return output


def conjugate_word(input_row: Row, word: tuple[Gate, ...]) -> Row:
    output = input_row
    for gate in word:
        output = conjugate_gate(output, gate)
    return output


def swap_block(left: int, right: int) -> tuple[Gate, ...]:
    return (
        Gate("CNOT", left, right),
        Gate("CNOT", right, left),
        Gate("CNOT", left, right),
    )


def port_word(fixture, port: int) -> tuple[Gate, ...]:
    bank = fixture.qubits
    output = []
    for mode in range(6):
        output.extend(swap_block(bank + mode, 6 * port + mode))
    return tuple(output)


def bank_gamma(fixture, port: int, mode: int, odd: bool) -> Row:
    del port  # the one live bank is declared at the selected port cell
    endpoint = fixture.qubits + mode
    prefix = sum(1 << (fixture.qubits + item) for item in range(mode))
    return Row(
        phase=int(odd),
        x=1 << endpoint,
        z=prefix | ((1 << endpoint) if odd else 0),
    )


def replace_port_matter_with_bank(
    input_row: Row, fixture, port: int
) -> Row:
    x, z = input_row.x, input_row.z
    for mode in range(6):
        matter_bit = 1 << (6 * port + mode)
        bank_bit = 1 << (fixture.qubits + mode)
        if x & matter_bit:
            x ^= matter_bit | bank_bit
        if z & matter_bit:
            z ^= matter_bit | bank_bit
    return Row(input_row.phase, x, z)


def dense_row(input_row: Row, qubits: int) -> np.ndarray:
    identity = np.eye(2, dtype=complex)
    x_matrix = np.array([[0, 1], [1, 0]], dtype=complex)
    z_matrix = np.array([[1, 0], [0, -1]], dtype=complex)
    factors = []
    for qubit in reversed(range(qubits)):
        local = identity
        if (input_row.x >> qubit) & 1:
            local = local @ x_matrix
        if (input_row.z >> qubit) & 1:
            local = local @ z_matrix
        factors.append(local)
    output = factors[0]
    for factor in factors[1:]:
        output = np.kron(output, factor)
    return (1j ** (input_row.phase % 4)) * output


def dense_gate(gate: Gate, qubits: int) -> np.ndarray:
    dimension = 1 << qubits
    if gate.kind == "H":
        return (
            dense_row(single_x(gate.control), qubits)
            + dense_row(single_z(gate.control), qubits)
        ) / np.sqrt(2.0)
    if gate.kind == "CNOT":
        output = np.zeros((dimension, dimension), dtype=complex)
        for basis in range(dimension):
            target = basis
            if (basis >> gate.control) & 1:
                target ^= 1 << gate.target
            output[target, basis] = 1.0
        return output
    if gate.kind == "CZ":
        output = np.eye(dimension, dtype=complex)
        for basis in range(dimension):
            if ((basis >> gate.control) & 1) and (
                (basis >> gate.target) & 1
            ):
                output[basis, basis] = -1.0
        return output
    if gate.kind == "CP":
        z_control = dense_row(single_z(gate.control), qubits)
        identity = np.eye(dimension, dtype=complex)
        p0 = (identity + z_control) / 2
        p1 = (identity - z_control) / 2
        return p0 + p1 @ dense_row(gate.pauli, qubits)
    raise ValueError(gate.kind)


def dense_selftest() -> dict[str, object]:
    """All signed weight-one/two Paulis against dense three-qubit gates."""
    base_rows = []
    local = (
        Row(),
        Row(x=1),
        Row(phase=1, x=1, z=1),
        Row(z=1),
    )
    for labels in product(range(4), repeat=3):
        weight = sum(label != 0 for label in labels)
        if weight not in (1, 2):
            continue
        canonical = Row()
        for qubit, label in enumerate(labels):
            item = local[label]
            shifted = Row(
                item.phase,
                item.x << qubit,
                item.z << qubit,
            )
            canonical = multiply(canonical, shifted)
        for extra_phase in range(4):
            base_rows.append(
                Row(
                    canonical.phase + extra_phase,
                    canonical.x,
                    canonical.z,
                )
            )

    gates = []
    gates.extend(Gate("H", qubit) for qubit in range(3))
    gates.extend(
        Gate("CNOT", control, target)
        for control in range(3)
        for target in range(3)
        if control != target
    )
    gates.extend(Gate("CZ", left, right) for left, right in combinations(range(3), 2))
    for control in range(3):
        targets = tuple(qubit for qubit in range(3) if qubit != control)
        for labels in product(range(4), repeat=len(targets)):
            if not any(labels):
                continue
            pauli = Row()
            for target, label in zip(targets, labels):
                item = local[label]
                pauli = multiply(
                    pauli,
                    Row(item.phase, item.x << target, item.z << target),
                )
            gates.append(Gate("CP", control, pauli=pauli))

    mismatches = 0
    maximum_residual = 0.0
    for gate in gates:
        unitary = dense_gate(gate, 3)
        for input_row in base_rows:
            actual = dense_row(conjugate_gate(input_row, gate), 3)
            expected = unitary @ dense_row(input_row, 3) @ unitary.conj().T
            residual = float(np.max(np.abs(actual - expected)))
            maximum_residual = max(maximum_residual, residual)
            mismatches += residual > 1e-10
    return {
        "pauli_rows": len(base_rows),
        "gates": len(gates),
        "comparisons": len(base_rows) * len(gates),
        "mismatches": mismatches,
        "maximum_residual": maximum_residual,
    }


def fixture_for_cells(cells):
    return O.arbitrary_fixture(tuple(cells))


def fixture_for_shape(shape: tuple[int, int, int]):
    return fixture_for_cells(Q.shape_cells(shape))


def displayed_shape(fixture) -> list[int]:
    return [
        max(cell[axis] for cell in fixture.cells)
        - min(cell[axis] for cell in fixture.cells)
        + 1
        for axis in range(3)
    ]


def fixture_path_equivalence() -> dict[str, object]:
    union_fixture = fixture_for_shape((2, 2, 2))
    bare_fixture = M.CompanionFixture.build((2, 2, 2))
    return {
        "shape": [2, 2, 2],
        "cells_identical": union_fixture.cells == bare_fixture.cells,
        "edges_identical": union_fixture.edges == bare_fixture.edges,
        "matter_qubits_identical": (
            union_fixture.matter_qubits == bare_fixture.matter_qubits
        ),
        "qubits_identical": union_fixture.qubits == bare_fixture.qubits,
        "used_constructor": "O.arbitrary_fixture(Q.shape_cells(shape))",
    }


def support_census(fixture, port: int, word: tuple[Gate, ...]) -> dict[str, int]:
    cells = set()
    for gate in word:
        qubits = [gate.control]
        if gate.target >= 0:
            qubits.append(gate.target)
        qubits.extend(
            qubit
            for qubit in range(fixture.qubits + 6)
            if ((gate.pauli.x | gate.pauli.z) >> qubit) & 1
        )
        for qubit in qubits:
            if qubit >= fixture.qubits:
                cells.add(port)
            else:
                cells.add(M.qubit_cell(fixture, qubit))
    diameter = max(
        (
            sum(
                abs(a - b)
                for a, b in zip(fixture.cells[left], fixture.cells[right])
            )
            for left in cells
            for right in cells
        ),
        default=0,
    )
    return {
        "support_cells": len(cells),
        "diameter": diameter,
        "primitive_count": len(word),
        "route_transitions": 0,
    }


def port_target_rows(fixture, port: int) -> tuple[tuple[Row, Row], ...]:
    targets = []
    for mode in range(6):
        targets.append(
            (
                single_z(fixture.qubits + mode),
                single_z(6 * port + mode),
            )
        )
    for mode in range(5):
        targets.append(
            (
                Row(
                    x=(1 << (fixture.qubits + mode))
                    | (1 << (fixture.qubits + mode + 1))
                ),
                Row(
                    x=(1 << (6 * port + mode))
                    | (1 << (6 * port + mode + 1))
                ),
            )
        )
    return tuple(targets)


def port_dictionary_pairs(
    fixture, port: int
) -> tuple[tuple[Row, Row], ...]:
    """Bank/physical pairs for the full onsite dictionary at one cell."""
    cell_mask = sum(1 << (6 * port + mode) for mode in range(6))
    cell_mask |= sum(
        1 << (fixture.matter_qubits + 3 * port + mode)
        for mode in range(3)
    )
    pairs = []
    for family, physical_pauli, _target in M.operator_rows(fixture):
        if family not in ("onsite_B", "onsite_even"):
            continue
        physical = row(physical_pauli)
        support = physical.x | physical.z
        if support and not support & ~cell_mask:
            pairs.append(
                (
                    replace_port_matter_with_bank(physical, fixture, port),
                    physical,
                )
            )
    return tuple(pairs)


def dictionary_port_generation_certificate(fixture, port: int) -> dict[str, int]:
    dictionary = M.operator_rows(fixture)
    onsite_identity_failures = sum(
        row(physical).fields() != row(target).fields()
        for family, physical, target in dictionary
        if family in ("onsite_B", "onsite_even")
    )
    missing = 0
    multiplicity_failures = 0
    for _bank, physical in port_target_rows(fixture, port):
        matches = sum(
            row(candidate).fields() == physical.fields()
            for family, candidate, _target in dictionary
            if family in ("onsite_B", "onsite_even")
        )
        missing += matches == 0
        multiplicity_failures += matches != 1
    return {
        "onsite_physical_target_identity_failures": onsite_identity_failures,
        "declared_11_generator_missing_failures": missing,
        "declared_11_generator_multiplicity_failures": multiplicity_failures,
    }


def parity_certificate(fixture, port: int, word: tuple[Gate, ...]) -> dict[str, int]:
    bank_parity = Row(
        z=sum(1 << (fixture.qubits + mode) for mode in range(6))
    )
    matter = sum(1 << (6 * port + mode) for mode in range(6))
    companion = sum(
        1 << (fixture.matter_qubits + 3 * port + mode)
        for mode in range(3)
    )
    cell_parity = Row(z=matter | companion)
    expected_cell_image = Row(z=bank_parity.z | companion)
    total = multiply(cell_parity, bank_parity)
    odd_detection_failures = 0
    odd_image_detection_failures = 0
    for mode in range(6):
        odd = single_x(fixture.qubits + mode)
        odd_detection_failures += anticommutes(odd, total) != 1
        odd_image_detection_failures += (
            anticommutes(conjugate_word(odd, word), total) != 1
        )
    return {
        "cell_parity_image_failures": (
            conjugate_word(cell_parity, word).fields()
            != expected_cell_image.fields()
        ),
        "total_joint_parity_invariance_failures": (
            conjugate_word(total, word).fields() != total.fields()
        ),
        "odd_bank_detection_failures": odd_detection_failures,
        "odd_matter_image_detection_failures": odd_image_detection_failures,
    }


def incident_edges_by_axis(fixture, port: int) -> dict[int, int]:
    output = {}
    for edge, record in enumerate(fixture.edges):
        left, right, _owner, axis, _left_mode, _right_mode = record
        if port in (left, right) and axis not in output:
            output[axis] = edge
    return output


def part1_certificate(fixture) -> dict[str, object]:
    port = fixture.cells.index(min(fixture.cells))
    word = port_word(fixture, port)
    dictionary = M.operator_rows(fixture)
    generation = dictionary_port_generation_certificate(fixture, port)

    forward_failures = sum(
        conjugate_word(bank, word).fields() != physical.fields()
        for bank, physical in port_target_rows(fixture, port)
    )
    reverse_failures = sum(
        conjugate_word(physical, word).fields() != bank.fields()
        for bank, physical in port_target_rows(fixture, port)
    )
    port_dictionary_pairs_at_cell = port_dictionary_pairs(fixture, port)
    forward_dictionary_failures = sum(
        conjugate_word(bank, word).fields() != physical.fields()
        for bank, physical in port_dictionary_pairs_at_cell
    )

    onsite_exchange_failures = 0
    onsite_other_cell_invariance_failures = 0
    seam_incident_failures = 0
    seam_nonincident_invariance_failures = 0
    seam_cursor = 0
    for family, physical_pauli, _target in dictionary:
        physical = row(physical_pauli)
        actual = conjugate_word(physical, word)
        if family == "seam":
            edge = seam_cursor // 4
            seam_cursor += 1
            left, right, *_rest = fixture.edges[edge]
            if port in (left, right):
                expected = replace_port_matter_with_bank(
                    physical, fixture, port
                )
                seam_incident_failures += actual.fields() != expected.fields()
            else:
                seam_nonincident_invariance_failures += (
                    actual.fields() != physical.fields()
                )
            continue
        support_on_port = bool(
            (physical.x | physical.z)
            & sum(1 << (6 * port + mode) for mode in range(6))
        )
        if support_on_port:
            expected = replace_port_matter_with_bank(physical, fixture, port)
            onsite_exchange_failures += actual.fields() != expected.fields()
        else:
            onsite_other_cell_invariance_failures += (
                actual.fields() != physical.fields()
            )

    parity = parity_certificate(fixture, port, word)
    census = support_census(fixture, port, word)
    return {
        "shape": displayed_shape(fixture),
        "cells": len(fixture.cells),
        "port_cell_index": port,
        "port_cell": list(fixture.cells[port]),
        "generation": generation,
        "forward_11_even_CAR_failures": forward_failures,
        "reverse_11_even_CAR_failures": reverse_failures,
        "port_onsite_dictionary_rows": len(port_dictionary_pairs_at_cell),
        "forward_port_onsite_dictionary_exchange_failures": (
            forward_dictionary_failures
        ),
        "port_onsite_dictionary_exchange_failures": onsite_exchange_failures,
        "other_cell_onsite_invariance_failures": (
            onsite_other_cell_invariance_failures
        ),
        "incident_seam_exchange_failures": seam_incident_failures,
        "nonincident_seam_invariance_failures": (
            seam_nonincident_invariance_failures
        ),
        "parity": parity,
        "census": census,
        "gate_pass": census["support_cells"] <= 2 and census["diameter"] <= 1,
    }


def seam_source_target_rows(fixture, port: int, edge: int):
    left, right, _owner, _axis, left_mode, right_mode = fixture.edges[edge]
    physical = tuple(row(item) for item in fixture.physical_terms(edge))
    left_local, right_local = left_mode % 6, right_mode % 6

    def endpoint(cell: int, mode: int, odd: bool) -> Row:
        if cell == port:
            return multiply(
                bank_gamma(fixture, port, mode, odd),
                row(fixture.companion_eta(cell, mode)),
            )
        return row(fixture.endpoint(cell, mode, odd))

    source = (
        (
            single_z(fixture.qubits + left_local)
            if left == port else single_z(left_mode)
        ),
        (
            single_z(fixture.qubits + right_local)
            if right == port else single_z(right_mode)
        ),
        product_rows(
            (
                Row(phase=2),
                endpoint(left, left_local, False),
                endpoint(right, right_local, True),
            )
        ),
        product_rows(
            (
                endpoint(left, left_local, True),
                endpoint(right, right_local, False),
            )
        ),
    )
    replacement_source = tuple(
        replace_port_matter_with_bank(item, fixture, port)
        for item in physical
    )
    replacement_failures = sum(
        explicit.fields() != replaced.fields()
        for explicit, replaced in zip(source, replacement_source)
    )
    return source, physical, replacement_failures


def row_distance(left: Row, right: Row) -> int:
    return (
        (left.x ^ right.x).bit_count()
        + (left.z ^ right.z).bit_count()
        + int((left.phase - right.phase) % 4 != 0)
    )


def greedy_symplectic_transvection_word(
    fixture, port: int, source: tuple[Row, ...], target: tuple[Row, ...]
) -> tuple[tuple[Gate, ...], dict[str, object]]:
    """Greedy CNOT-transvection synthesis, parity-completed on six modes.

    The seam pairs alone can underdetermine higher bank modes.  The requested
    Part-1 parity image fixes that freedom.  Candidate three-CNOT swaps are
    accepted in their best score order; all are needed by the parity-complete
    signed-pair system.
    """
    bank_parity = Row(
        z=sum(1 << (fixture.qubits + mode) for mode in range(6))
    )
    matter_parity = Row(
        z=sum(1 << (6 * port + mode) for mode in range(6))
    )
    augmented_source = (*source, bank_parity)
    augmented_target = (*target, matter_parity)
    chosen: list[Gate] = []
    remaining = set(range(6))
    score_trace = []
    while remaining:
        candidates = []
        for mode in sorted(remaining):
            trial = (*chosen, *swap_block(
                fixture.qubits + mode, 6 * port + mode
            ))
            score = sum(
                row_distance(conjugate_word(left, trial), right)
                for left, right in zip(augmented_source, augmented_target)
            )
            candidates.append((score, mode, trial))
        score, mode, trial = min(candidates)
        chosen = list(trial)
        remaining.remove(mode)
        score_trace.append({"mode": mode, "remaining_score": score})
    final_failures = sum(
        conjugate_word(left, tuple(chosen)).fields() != right.fields()
        for left, right in zip(augmented_source, augmented_target)
    )
    return tuple(chosen), {
        "method": "greedy elementary symplectic CNOT transvections with parity completion",
        "score_trace": score_trace,
        "augmented_signed_pairs": len(augmented_source),
        "final_pair_failures": final_failures,
    }


def oriented_seam_target_rows(
    fixture, edge: int, reverse_orientation: bool
) -> tuple[Row, ...]:
    """Rebuild the four physical seam factors in either endpoint orientation."""
    left, right, _owner, _axis, left_mode, right_mode = fixture.edges[edge]
    left_local, right_local = left_mode % 6, right_mode % 6
    if reverse_orientation:
        left, right = right, left
        left_local, right_local = right_local, left_local

    def endpoint(cell: int, mode: int, odd: bool) -> Row:
        return row(fixture.endpoint(cell, mode, odd))

    return (
        single_z(6 * left + left_local),
        single_z(6 * right + right_local),
        product_rows(
            (
                Row(phase=2),
                endpoint(left, left_local, False),
                endpoint(right, right_local, True),
            )
        ),
        product_rows(
            (
                endpoint(left, left_local, True),
                endpoint(right, right_local, False),
            )
        ),
    )


def rebuilt_seam_images(
    fixture, port: int, edge: int, reverse_orientation: bool = False
) -> tuple[Row, ...]:
    """Conjugate one bank-ended seam quadruple through its rebuilt seam word."""
    if reverse_orientation:
        target = oriented_seam_target_rows(fixture, edge, True)
        source = tuple(
            replace_port_matter_with_bank(item, fixture, port)
            for item in target
        )
    else:
        source, target, _explicit_failures = seam_source_target_rows(
            fixture, port, edge
        )
    seam_word, _synthesis = greedy_symplectic_transvection_word(
        fixture, port, source, target
    )
    return tuple(conjugate_word(item, seam_word) for item in source)


def seam_certificate(fixture, port: int, edge: int) -> dict[str, object]:
    source, target, explicit_source_failures = seam_source_target_rows(
        fixture, port, edge
    )
    word, synthesis = greedy_symplectic_transvection_word(
        fixture, port, source, target
    )
    seam_failures = sum(
        conjugate_word(left, word).fields() != right.fields()
        for left, right in zip(source, target)
    )
    swapped_port_mask = sum(1 << (6 * port + mode) for mode in range(6))
    dictionary_invariance_failures = 0
    dictionary_invariance_rows = 0
    seam_cursor = 0
    for family, physical_pauli, _logical in M.operator_rows(fixture):
        physical = row(physical_pauli)
        current_edge = None
        if family == "seam":
            current_edge = seam_cursor // 4
            seam_cursor += 1
        involved = current_edge == edge or bool(
            (physical.x | physical.z) & swapped_port_mask
        )
        if not involved:
            dictionary_invariance_rows += 1
            dictionary_invariance_failures += (
                conjugate_word(physical, word).fields() != physical.fields()
            )
    parity = parity_certificate(fixture, port, word)
    census = support_census(fixture, port, word)
    left, right, _owner, axis, _lm, _rm = fixture.edges[edge]
    other = right if left == port else left
    route = ()
    route_forward_failures, route_inverse_failures = (
        P.route_execution_failures(fixture.cells[port], route)
    )
    return {
        "edge": edge,
        "axis": axis,
        "other_endpoint_cell_index": other,
        "explicit_bank_Majorana_source_construction_failures": (
            explicit_source_failures
        ),
        "four_seam_image_failures": seam_failures,
        "noninvolved_dictionary_rows": dictionary_invariance_rows,
        "noninvolved_dictionary_invariance_failures": (
            dictionary_invariance_failures
        ),
        "parity": parity,
        "synthesis": synthesis,
        "routing": {
            "needed_noncolocated_primitive": False,
            "returned_route": route,
            "forward_failures": route_forward_failures,
            "inverse_failures": route_inverse_failures,
        },
        "census": census,
        "gate_pass": census["support_cells"] <= 2 and census["diameter"] <= 1,
    }


def part2_certificate(fixture) -> dict[str, object]:
    port = fixture.cells.index(min(fixture.cells))
    selected = incident_edges_by_axis(fixture, port)
    axes = {
        str(axis): seam_certificate(fixture, port, edge)
        for axis, edge in sorted(selected.items())
    }
    return {
        "port_cell_index": port,
        "tested_axes": len(axes),
        "axes": axes,
        "all_four_seam_images_exact": all(
            item["explicit_bank_Majorana_source_construction_failures"] == 0
            and item["four_seam_image_failures"] == 0
            for item in axes.values()
        ),
        "all_noninvolved_dictionary_rows_invariant": all(
            item["noninvolved_dictionary_invariance_failures"] == 0
            for item in axes.values()
        ),
        "all_parity_bookkeeping_exact": all(
            not any(item["parity"].values()) for item in axes.values()
        ),
        "all_routes_returned": all(
            item["routing"]["forward_failures"] == 0
            and item["routing"]["inverse_failures"] == 0
            for item in axes.values()
        ),
        "gate_pass": all(item["gate_pass"] for item in axes.values()),
    }


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = np.zeros((3, 3), dtype=int)
            for target_axis, source_axis in enumerate(permutation):
                frame[target_axis, source_axis] = signs[target_axis]
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    assert len(frames) == 24
    return tuple(frames)


def canonicalize_row(
    input_row: Row, fixture, port: int, other: int | None = None
) -> tuple[int, int, int]:
    mapping = {}
    for mode in range(6):
        mapping[6 * port + mode] = mode
    for mode in range(3):
        mapping[fixture.matter_qubits + 3 * port + mode] = 6 + mode
    if other is not None:
        for mode in range(6):
            mapping[6 * other + mode] = 9 + mode
        for mode in range(3):
            mapping[fixture.matter_qubits + 3 * other + mode] = 15 + mode
    for mode in range(6):
        mapping[fixture.qubits + mode] = 18 + mode
    x = z = 0
    unknown = 0
    for old in range(fixture.qubits + 6):
        active_x = (input_row.x >> old) & 1
        active_z = (input_row.z >> old) & 1
        if not (active_x or active_z):
            continue
        if old not in mapping:
            unknown += 1
            continue
        new = mapping[old]
        x |= active_x << new
        z |= active_z << new
    if unknown:
        raise AssertionError("row escaped declared port/edge union")
    return input_row.phase % 4, x, z


def covariance_signature(
    fixture, port: int | None = None
) -> tuple[Counter, Counter, tuple]:
    if port is None:
        port = fixture.cells.index(min(fixture.cells))
    word = port_word(fixture, port)
    port_images = Counter(
        canonicalize_row(conjugate_word(bank, word), fixture, port)
        for bank, _target in port_dictionary_pairs(fixture, port)
    )
    seam_images = Counter()
    seam_census = []
    for axis, edge in sorted(incident_edges_by_axis(fixture, port).items()):
        source, target, _explicit_failures = seam_source_target_rows(
            fixture, port, edge
        )
        seam_word, _synthesis = greedy_symplectic_transvection_word(
            fixture, port, source, target
        )
        left, right, *_rest = fixture.edges[edge]
        other = right if left == port else left
        for item in source:
            seam_images[canonicalize_row(
                conjugate_word(item, seam_word), fixture, port, other
            )] += 1
        census = support_census(fixture, port, seam_word)
        seam_census.append(
            (
                axis,
                census["support_cells"],
                census["diameter"],
                census["primitive_count"],
                census["route_transitions"],
            )
        )
    port_census = support_census(fixture, port, word)
    census_vector = (
        port_census["support_cells"],
        port_census["diameter"],
        port_census["primitive_count"],
        port_census["route_transitions"],
        tuple(sorted(item[1:] for item in seam_census)),
    )
    return port_images, seam_images, census_vector


def apply_physical_images(
    input_row: Row, images
) -> Row:
    """Apply Q's signed physical X/Z generator images to one source row."""
    x_images, z_images = images
    output = Row(phase=input_row.phase % 4)
    bits = input_row.x
    while bits:
        low = bits & -bits
        qubit = low.bit_length() - 1
        output = multiply(output, row(x_images[qubit]))
        bits ^= low
    bits = input_row.z
    while bits:
        low = bits & -bits
        qubit = low.bit_length() - 1
        output = multiply(output, row(z_images[qubit]))
        bits ^= low
    return output


def binary_fields(input_row: Row) -> tuple[int, int]:
    return input_row.x, input_row.z


def physical_output_multisets(
    fixture, port: int | None = None
) -> tuple[Counter, dict[int, tuple[Row, ...]]]:
    """Full port dictionary multiset and ordered incident-edge seam images."""
    if port is None:
        port = fixture.cells.index(min(fixture.cells))
    word = port_word(fixture, port)
    port_images = Counter(
        conjugate_word(bank, word).fields()
        for bank, _target in port_dictionary_pairs(fixture, port)
    )
    seam_images = {}
    for _axis, edge in sorted(incident_edges_by_axis(fixture, port).items()):
        seam_images[edge] = rebuilt_seam_images(fixture, port, edge)
    return port_images, seam_images


def transported_edge_lookup(
    source, source_edge: int, target, frame, shift
) -> int | None:
    left, right, *_rest = source.edges[source_edge]
    endpoint_coordinates = frozenset(
        tuple(
            int(value)
            for value in (
                frame @ np.asarray(source.cells[cell])
                + np.asarray(shift)
            )
        )
        for cell in (left, right)
    )
    for edge, record in enumerate(target.edges):
        target_left, target_right, *_target_rest = record
        if frozenset(
            (
                target.cells[target_left],
                target.cells[target_right],
            )
        ) == endpoint_coordinates:
            return edge
    return None


def seam_factor_index_class(
    transported: tuple[Row, ...], rebuilt_forward: tuple[Row, ...]
) -> tuple[int, ...] | None:
    factor_indices = []
    for transported_row in transported:
        matches = tuple(
            factor
            for factor, target_row in enumerate(rebuilt_forward)
            if binary_fields(transported_row) == binary_fields(target_row)
        )
        if len(matches) != 1:
            return None
        factor_indices.append(matches[0])
    return tuple(factor_indices)


def covariance_certificate(
    shape: tuple[int, int, int]
) -> dict[str, object]:
    frames = proper_cubic_frames()
    shifts = tuple(product((0, 1), repeat=3))
    source = fixture_for_shape(shape)
    source_port = source.cells.index(min(source.cells))
    source_port_rows, source_seam_rows = physical_output_multisets(source)
    reference_census = covariance_signature(source)[2]
    signed_port_dictionary_failures = 0
    binary_port_dictionary_failures = 0
    signed_seam_class_failures = 0
    binary_seam_failures = 0
    census_failures = 0
    lexicographic_min_not_transported = 0
    port_relocations = Counter()
    for frame in frames:
        for shift in shifts:
            transformed_cells = Q.affine_cells(
                source.cells, frame, shift
            )
            fixture = fixture_for_cells(transformed_cells)
            source_port_image = tuple(
                int(value)
                for value in (
                    frame @ np.asarray(source.cells[source_port])
                    + np.asarray(shift)
                )
            )
            # The port is supplied chart data: it transports with the frame.
            # The lexicographic-minimum default used at build time is a
            # convention, not a covariant object; count how often they differ
            # as an informational census only.
            port = fixture.cells.index(source_port_image)
            port_relocations[fixture.cells[port]] += 1
            lexicographic_min_not_transported += (
                source_port_image != min(fixture.cells)
            )

            images = Q.physical_images(source, fixture, frame, shift)
            transported_port = Counter()
            for fields, multiplicity in source_port_rows.items():
                transported = apply_physical_images(Row(*fields), images)
                transported_port[transported.fields()] += multiplicity

            target_port, target_seam = physical_output_multisets(
                fixture, port
            )
            signed_port_dictionary_failures += (
                transported_port != target_port
            )
            binary_port_dictionary_failures += Counter(
                (x, z)
                for (_phase, x, z), multiplicity
                in transported_port.items()
                for _copy in range(multiplicity)
            ) != Counter(
                (x, z)
                for (_phase, x, z), multiplicity in target_port.items()
                for _copy in range(multiplicity)
            )

            for source_edge, source_quadruple in source_seam_rows.items():
                target_edge = transported_edge_lookup(
                    source, source_edge, fixture, frame, shift
                )
                transported_quadruple = tuple(
                    apply_physical_images(item, images)
                    for item in source_quadruple
                )
                if target_edge is None or target_edge not in target_seam:
                    signed_seam_class_failures += 1
                    binary_seam_failures += 1
                    continue

                rebuilt_forward = target_seam[target_edge]
                binary_seam_failures += Counter(
                    binary_fields(item) for item in transported_quadruple
                ) != Counter(
                    binary_fields(item) for item in rebuilt_forward
                )
                factor_class = seam_factor_index_class(
                    transported_quadruple, rebuilt_forward
                )
                if factor_class == (0, 1, 2, 3):
                    signed_match = all(
                        transported.fields() == rebuilt.fields()
                        for transported, rebuilt in zip(
                            transported_quadruple, rebuilt_forward
                        )
                    )
                elif factor_class == (1, 0, 3, 2):
                    rebuilt_reversed = rebuilt_seam_images(
                        fixture, port, target_edge, True
                    )
                    reversed_class = seam_factor_index_class(
                        rebuilt_reversed, rebuilt_forward
                    )
                    signed_match = (
                        reversed_class == (1, 0, 3, 2)
                        and all(
                            transported.fields() == rebuilt.fields()
                            for transported, rebuilt in zip(
                                transported_quadruple, rebuilt_reversed
                            )
                        )
                    )
                else:
                    signed_match = False
                signed_seam_class_failures += not signed_match

            census_failures += (
                covariance_signature(fixture, port)[2] != reference_census
            )
    return {
        "shape": list(shape),
        "frames": len(frames),
        "translation_parities": len(shifts),
        "contexts": len(frames) * len(shifts),
        "port_rule": (
            "rebuilt at the transported image of the source port; the "
            "lexicographic-minimum default is a supplied chart convention "
            "and is not frame-covariant"
        ),
        "frame_action": "Q.physical_images exact signed generator transport",
        "distinct_relocated_port_coordinates": len(port_relocations),
        "lexicographic_min_port_not_transported_contexts": (
            lexicographic_min_not_transported
        ),
        "signed_port_dictionary_multiset_failures": (
            signed_port_dictionary_failures
        ),
        "binary_port_dictionary_multiset_failures": (
            binary_port_dictionary_failures
        ),
        "signed_seam_image_class_failures": signed_seam_class_failures,
        "binary_seam_multiset_failures": binary_seam_failures,
        "census_vector_failures": census_failures,
        "failures": (
            signed_port_dictionary_failures
            + binary_port_dictionary_failures
            + signed_seam_class_failures
            + binary_seam_failures
            + census_failures
        ),
    }


def factorization_anchor_certificate() -> dict[str, object]:
    output = {}
    for shape in ((2, 2, 2), (3, 2, 2)):
        report = F.phase_fixed_factorization(shape)
        phase = report["phase_fixed_intertwiner"]
        coordinate_fields = (
            "logical_coordinate_failures",
            "gauge_coordinate_failures_for_every_physical_generator",
            "parity_coordinate_failures",
            "phase_parity_failures",
            "phase_contradictions",
            "even_sector_phase_failures",
            "odd_sector_phase_failures",
            "canonical_tableau_pairing_failures",
        )
        coordinate_failures = sum(int(phase[name]) for name in coordinate_fields)
        output["x".join(map(str, shape))] = {
            "shape": list(shape),
            "dimension_identity": bool(report["dimension_identity"]),
            "finite_box_mixed_gauge_CPTP_E_constructed": bool(
                phase["finite_box_mixed_gauge_CPTP_E_constructed"]
            ),
            "factorwise_full_word_intertwiner_exact": bool(
                phase["factorwise_full_word_intertwiner_exact"]
            ),
            "coordinate_failures": coordinate_failures,
            "coordinate_failure_fields": {
                name: phase[name] for name in coordinate_fields
            },
            "tableau_digest": report["tableau_digest"],
            "locality": report["locality"],
        }
    return {
        "boxes": output,
        "all_regressions_pass": all(
            item["dimension_identity"]
            and item["finite_box_mixed_gauge_CPTP_E_constructed"]
            and item["factorwise_full_word_intertwiner_exact"]
            and item["coordinate_failures"] == 0
            for item in output.values()
        ),
        "v_s_coordinate_rows_returned": False,
        "literal_v_s_restriction_compiled": False,
        "census_role": (
            "reported measured ceiling for a future literal V_s-restriction "
            "word; no route is compiled from the digest or locality metrics"
        ),
    }


def control_certificate(fixture) -> dict[str, object]:
    port = fixture.cells.index(min(fixture.cells))
    word = port_word(fixture, port)
    pairs = port_target_rows(fixture, port)

    deleted = word[1:]
    deletion_mismatches = sum(
        conjugate_word(bank, deleted).fields() != physical.fields()
        for bank, physical in pairs
    )

    # A standard three-CNOT SWAP is A B A, hence literal reversal is the
    # identical Clifford (palindromic) and cannot be a positive control.
    palindromic_reverse = (*reversed(word[:3]), *word[3:])
    palindromic_reverse_mismatches = sum(
        conjugate_word(bank, palindromic_reverse).fields()
        != physical.fields()
        for bank, physical in pairs
    )
    # Positive hostile-order control: flip the middle CNOT of the first SWAP
    # block to the same direction as its neighbours. A A A collapses to a
    # single CNOT, which is not a SWAP, so the exchange must break.
    hostile = (word[0], word[0], word[0], *word[3:])
    hostile_mismatches = sum(
        conjugate_word(bank, hostile).fields() != physical.fields()
        for bank, physical in pairs
    )
    # Second hostile control on the Part-2 seam word.
    axis_edges = incident_edges_by_axis(fixture, port)
    seam_edge = axis_edges[min(axis_edges)]
    seam_source, _seam_target, _explicit = seam_source_target_rows(
        fixture, port, seam_edge
    )
    seam_word, _synthesis = greedy_symplectic_transvection_word(
        fixture, port, seam_source,
        seam_source_target_rows(fixture, port, seam_edge)[1],
    )
    seam_word_palindromic = tuple(reversed(seam_word)) == seam_word
    seam_reference_images = tuple(
        conjugate_word(item, seam_word) for item in seam_source
    )
    seam_support = sorted(
        {
            qubit
            for gate in seam_word
            for qubit in (gate.control, gate.target)
            if qubit >= 0
        }
    )
    stray_primitive_pair = None
    stray_primitive_mismatches = 0
    for control in seam_support:
        for target in seam_support:
            if control == target:
                continue
            appended_word = (*seam_word, Gate("CNOT", control, target))
            mismatch_count = sum(
                conjugate_word(item, appended_word).fields()
                != reference.fields()
                for item, reference in zip(
                    seam_source, seam_reference_images
                )
            )
            if mismatch_count:
                stray_primitive_pair = (control, target)
                stray_primitive_mismatches = mismatch_count
                break
        if stray_primitive_pair is not None:
            break

    total_parity = product_rows(
        (
            Row(
                z=sum(1 << (6 * port + mode) for mode in range(6))
                | sum(
                    1 << (fixture.matter_qubits + 3 * port + mode)
                    for mode in range(3)
                )
            ),
            Row(
                z=sum(
                    1 << (fixture.qubits + mode) for mode in range(6)
                )
            ),
        )
    )
    odd_detection_failures = sum(
        anticommutes(single_x(fixture.qubits + mode), total_parity) != 1
        for mode in range(6)
    )

    nonport = next(
        cell for cell in range(len(fixture.cells)) if cell != port
    )
    wrong_word = port_word(fixture, nonport)
    wrong_port_mismatches = sum(
        conjugate_word(bank, wrong_word).fields() != physical.fields()
        for bank, physical in pairs
    )
    return {
        "delete_one_CNOT_mismatch_count": deletion_mismatches,
        "palindromic_literal_reverse_mismatch_count": (
            palindromic_reverse_mismatches
        ),
        "palindromic_reverse_note": (
            "the standard three-CNOT SWAP is palindromic, so literal "
            "gate-order reversal is the identical Clifford; reported as an "
            "informational identity, not a control"
        ),
        "hostile_middle_CNOT_flip_mismatch_count": hostile_mismatches,
        "seam_word_palindromic": seam_word_palindromic,
        "stray_seam_primitive_pair": (
            list(stray_primitive_pair)
            if stray_primitive_pair is not None else None
        ),
        "stray_seam_primitive_mismatch_count": (
            stray_primitive_mismatches
        ),
        "stray_seam_primitive_not_found": (
            stray_primitive_pair is None
        ),
        "unlawful_odd_input_detection_failures": odd_detection_failures,
        "wrong_port_mismatch_count": wrong_port_mismatches,
    }


def all_zero(mapping: dict[str, int]) -> bool:
    return all(value == 0 for value in mapping.values())


def main() -> None:
    started = time.monotonic()
    checks = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    dense = dense_selftest()
    check(
        "dense exact Clifford tableau self-test has zero mismatches",
        dense["mismatches"] == 0,
    )

    fixture_equivalence = fixture_path_equivalence()
    check(
        "union-safe and bare constructors agree on cells edges and qubits for 2x2x2",
        all(
            fixture_equivalence[name]
            for name in (
                "cells_identical",
                "edges_identical",
                "matter_qubits_identical",
                "qubits_identical",
            )
        ),
    )

    boxes = {}
    requested_shapes = ((1, 1, 1), (2, 2, 2), (3, 2, 2))
    for shape in requested_shapes:
        fixture = fixture_for_shape(shape)
        part1 = part1_certificate(fixture)
        part2 = part2_certificate(fixture)
        boxes["x".join(map(str, shape))] = {
            "shape": list(shape),
            "part1": part1,
            "part2": part2,
        }
        check(
            f"{shape} Part 1 dictionary and exchange images are exact",
            all_zero(part1["generation"])
            and part1["forward_11_even_CAR_failures"] == 0
            and part1["reverse_11_even_CAR_failures"] == 0
            and part1["port_onsite_dictionary_rows"] == 36
            and part1[
                "forward_port_onsite_dictionary_exchange_failures"
            ] == 0
            and part1["port_onsite_dictionary_exchange_failures"] == 0
            and part1["other_cell_onsite_invariance_failures"] == 0
            and part1["incident_seam_exchange_failures"] == 0
            and part1["nonincident_seam_invariance_failures"] == 0,
        )
        check(
            f"{shape} Part 1 parity and bounded gate census pass",
            not any(part1["parity"].values()) and part1["gate_pass"],
        )
        check(
            f"{shape} Part 2 seam images noninvolved rows parity and routing are exact",
            part2["all_four_seam_images_exact"]
            and part2["all_noninvolved_dictionary_rows_invariant"]
            and part2["all_parity_bookkeeping_exact"]
            and part2["all_routes_returned"],
        )
        check(
            f"{shape} Part 2 named support gate passes",
            part2["gate_pass"],
        )

    if time.monotonic() - started < 300:
        shape = (5, 3, 2)
        fixture = fixture_for_shape(shape)
        part1 = part1_certificate(fixture)
        boxes["x".join(map(str, shape))] = {
            "shape": list(shape),
            "part1": part1,
            "part2": {
                "skipped": True,
                "reason": "task limits 5x3x2 to Part 1 plus census",
            },
        }
        check(
            f"{shape} optional Part 1 and census pass",
            all_zero(part1["generation"])
            and part1["forward_11_even_CAR_failures"] == 0
            and part1["reverse_11_even_CAR_failures"] == 0
            and part1["port_onsite_dictionary_rows"] == 36
            and part1[
                "forward_port_onsite_dictionary_exchange_failures"
            ] == 0
            and part1["port_onsite_dictionary_exchange_failures"] == 0
            and part1["other_cell_onsite_invariance_failures"] == 0
            and part1["incident_seam_exchange_failures"] == 0
            and part1["nonincident_seam_invariance_failures"] == 0
            and not any(part1["parity"].values())
            and part1["gate_pass"],
        )

    factorization_anchor = factorization_anchor_certificate()
    check(
        "mixed-gauge factorization anchors regress with exact coordinates",
        factorization_anchor["all_regressions_pass"],
    )

    covariance = {
        "2x2x2": covariance_certificate((2, 2, 2)),
    }
    if time.monotonic() - started < 300:
        covariance["3x2x2"] = covariance_certificate((3, 2, 2))
    check(
        "24 frames x 8 translation parities have exact dictionary-family and seam-class covariance",
        all(item["failures"] == 0 for item in covariance.values()),
    )

    controls = control_certificate(fixture_for_shape((2, 2, 2)))
    check(
        "deleting one CNOT produces a nonzero conjugation mismatch",
        controls["delete_one_CNOT_mismatch_count"] > 0,
    )
    check(
        "flipping the middle CNOT of one SWAP block produces a nonzero mismatch",
        controls["hostile_middle_CNOT_flip_mismatch_count"] > 0,
    )
    check(
        "appending one stray primitive to the seam word is detected",
        not controls["stray_seam_primitive_not_found"]
        and controls["stray_seam_primitive_mismatch_count"] > 0,
    )
    check(
        "an unlawful odd input is detected by joint parity",
        controls["unlawful_odd_input_detection_failures"] == 0,
    )
    check(
        "a wrong-port word leaves the declared port rows unmapped",
        controls["wrong_port_mismatch_count"] > 0,
    )

    passing = all(item["pass"] for item in checks)
    report = {
        "status": (
            "cycle721-direct-local-encoded-input-clifford-port-pass"
            if passing
            else "cycle721-direct-local-encoded-input-clifford-port-incomplete"
        ),
        "checks": checks,
        "dense_selftest": dense,
        "fixture_constructor_equivalence": fixture_equivalence,
        "boxes": boxes,
        "factorization_anchor": factorization_anchor,
        "covariance": covariance,
        "controls": controls,
        "derived": (
            "six co-located three-CNOT SWAP blocks exchange the declared live "
            "even-CAR bank with the full 36-row port-cell onsite dictionary "
            "family exactly",
            "the same parity-complete local word maps bank-ended incident seam "
            "bilinears back to the supplied physical seam rows",
            "all route counts are zero because every synthesized two-M2 "
            "primitive is co-located at the declared port cell",
        ),
        "supplied": (
            "the Cycle-720 companion/center operator dictionary and sector inventory",
            "one clean six-qubit live-input bank co-located at the declared port",
            "the total-parity label and companion center-sector representative",
        ),
        "open": (
            "a public immutable V_s tableau/coordinate API and literal restriction compiler",
            "the Bell/Choi gauge-mixed logical injection E_s",
            "fault-tolerant preparation, decoding, and autonomous sector repair",
            "coframe-origin seeded transport: this bank/dictionary surface touches no coframe registers, so the eight-origin channel covariance stays with the epoch-level composition",
            "autonomous selection of the port cell: the lexicographic-minimum default is a supplied chart convention (covariance evaluates the transported port)",
        ),
        "claim_boundary": (
            "This is a reversible even-exchange port plus seam-extended coupling "
            "on the declared companion/center code with supplied sector inventory. "
            "It is not the gauge-mixed logical injection E_s, which remains the "
            "Bell/Choi route. The factorization locality values are a coordinate-"
            "row census only: no V_s restriction is compiled. There is no autonomy "
            "or genesis claim. Circuit ordinals describe structure, not time. "
            "This is state-level coupling only, with no matter, FTL, mass, or "
            "charge transfer."
        ),
        "direct_encoded_input_clifford_attempted": True,
        "encoded_input_clifford_v_s_restriction_compiled": False,
        "authority": "none",
        "audit": "unset",
        "runtime_seconds": time.monotonic() - started,
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if not passing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
