#!/usr/bin/env python3
"""Companion-bank Bell-character dilation and route-census certificate.

For a fixture with ``N`` cells and ``q = 9N``:

===================  ================================================
wide-register range  ownership
===================  ================================================
``[0, q)``           physical output M2: ``6N`` matter then ``3N`` companion
``[q, 2q)``          companion-encoded live-input mirror of the physical M2
``[2q, 2q+R)``       one retained Bell-syndrome ancilla per direct-basis row
following ``N``      one returned mobile-route rail per cell
===================  ================================================

The Cycle-720 graph row's coarse-input half is dropped entirely.  Each
measured character is the graph row restricted to physical bits times the
same full physical-representation row on the companion-encoded input bank.
Row order is exactly ``P.direct_graph_basis`` order.  The abstract tableau
word is ``H(a); controlled local Pauli letters; H(a)``.  In this conjugation
direction ``X(a)`` is fixed while ``Z(a)`` is transported to
``Z(a) * R_i``.  Thus, with the supplied clean ancilla, the retained Z
readout is the ``R_i`` character; fixed ``X(a)`` means there is no conjugate
leakage.

The returned-route object is a separate support-and-return census.  Its links
are not inserted as SWAPs or other transport gates into the tableau word, so
this runner does not certify a route-expanded nearest-neighbour measurement
circuit.  It also does not claim a collision-free joint epoch with the pump
and recurrent update.  Ordinals are circuit structure, not time.  The result
is state-level algebra only: no matter, FTL, mass, or charge transfer is
asserted.
"""

from __future__ import annotations

from collections import Counter
from copy import copy
from itertools import product
import json
from time import perf_counter

import numpy as np

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P
import frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27 as V
import frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27 as O
import frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27 as EB


AUDIT_TIMEOUT_SEC = 900
NOTE_PATH = (
    "docs/COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_"
    "EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/COMPANION_BANK_BELL_CHARACTER_DILATION_EXCHANGE_PORT_AND_EPOCH_LIVENESS_BOUNDED_THEOREM_NOTE_2026-07-28.md",
    "scripts/frontier_cycle720_cell_majorana_companion_geometry_2026_07_27.py",
    "scripts/frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_overlap_star_mixed_gauge_choi_2026_07_27.py",
    "scripts/frontier_cycle720_companion_fixed_sector_even_car_bell_2026_07_27.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

Pauli = M.Pauli
Coord = tuple[int, int, int]
Gate = tuple
TOL = 1.0e-12


def fields(row: Pauli) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def multiply(left: Pauli, right: Pauli) -> Pauli:
    """Exact Pauli multiplication in the imported ``i^p X^x Z^z`` encoding."""
    return left @ right


def pauli_letter(qubit: int, letter: str) -> Pauli:
    if letter == "X":
        return Pauli(x=1 << qubit)
    if letter == "Z":
        return Pauli(z=1 << qubit)
    if letter == "Y":
        return Pauli(phase=1, x=1 << qubit, z=1 << qubit)
    raise ValueError(f"unsupported Pauli letter {letter!r}")


def letter_at(row: Pauli, qubit: int) -> str:
    x = (row.x >> qubit) & 1
    z = (row.z >> qubit) & 1
    return ("I", "X", "Z", "Y")[x + 2 * z]


def supported_qubits(row: Pauli) -> tuple[int, ...]:
    mask = row.x | row.z
    output = []
    while mask:
        bit = mask & -mask
        output.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(output)


def conjugate_h(row: Pauli, qubit: int) -> Pauli:
    """Conjugate a Pauli by a standard Hadamard, with phase modulo four."""
    bit = 1 << qubit
    x = 1 if row.x & bit else 0
    z = 1 if row.z & bit else 0
    output_x = (row.x & ~bit) | (bit if z else 0)
    output_z = (row.z & ~bit) | (bit if x else 0)
    return Pauli((row.phase + 2 * x * z) % 4, output_x, output_z)


def conjugate_controlled_letter(
    row: Pauli, control: int, target: int, letter: str
) -> Pauli:
    """Conjugate by ``|0><0| I + |1><1| letter`` exactly."""
    if control == target:
        raise ValueError("controlled-Pauli control and target must differ")
    local_mask = (1 << control) | (1 << target)
    rest = Pauli(
        row.phase,
        row.x & ~local_mask,
        row.z & ~local_mask,
    )
    target_pauli = pauli_letter(target, letter)
    xc_image = multiply(Pauli(x=1 << control), target_pauli)
    zc_image = Pauli(z=1 << control)
    xt = Pauli(x=1 << target)
    zt = Pauli(z=1 << target)
    xt_image = (
        multiply(zc_image, xt)
        if target_pauli.z & (1 << target)
        else xt
    )
    zt_image = (
        multiply(zc_image, zt)
        if target_pauli.x & (1 << target)
        else zt
    )
    local = Pauli()
    if row.x & (1 << control):
        local = multiply(local, xc_image)
    if row.x & (1 << target):
        local = multiply(local, xt_image)
    if row.z & (1 << control):
        local = multiply(local, zc_image)
    if row.z & (1 << target):
        local = multiply(local, zt_image)
    return multiply(rest, local)


def conjugate_word(row: Pauli, gates: tuple[Gate, ...]) -> Pauli:
    output = row
    for gate in gates:
        if gate[0] == "H":
            output = conjugate_h(output, gate[1])
        elif gate[0] == "CP":
            output = conjugate_controlled_letter(
                output, gate[1], gate[2], gate[3]
            )
        else:
            raise ValueError(f"unknown compiled gate {gate!r}")
    return output


def row_from_letters(letters: tuple[str, ...]) -> Pauli:
    output = Pauli()
    for qubit, letter in enumerate(letters):
        if letter != "I":
            output = multiply(output, pauli_letter(qubit, letter))
    return output


def dense_pauli(row: Pauli, width: int) -> np.ndarray:
    I = np.eye(2, dtype=complex)
    X = np.asarray(((0, 1), (1, 0)), dtype=complex)
    Y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    Z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    matrices = (I, X, Z, Y)
    output = np.asarray(((1,),), dtype=complex)
    y_count = 0
    for qubit in reversed(range(width)):
        x = (row.x >> qubit) & 1
        z = (row.z >> qubit) & 1
        y_count += x & z
        output = np.kron(output, matrices[x + 2 * z])
    return (1j ** ((row.phase - y_count) % 4)) * output


def dense_h(qubit: int, width: int) -> np.ndarray:
    I = np.eye(2, dtype=complex)
    H = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2)
    output = np.asarray(((1,),), dtype=complex)
    for index in reversed(range(width)):
        output = np.kron(output, H if index == qubit else I)
    return output


def dense_controlled_target(target_row: Pauli, control: int, width: int) -> np.ndarray:
    identity = np.eye(1 << width, dtype=complex)
    z_control = dense_pauli(Pauli(z=1 << control), width)
    projector_zero = (identity + z_control) / 2
    projector_one = (identity - z_control) / 2
    return projector_zero + projector_one @ dense_pauli(target_row, width)


def dense_selftest_certificate() -> dict[str, object]:
    """Exhaust all 16 two-target Paulis and all 64 three-qubit test rows."""
    width = 3
    ancilla = 0
    test_rows = tuple(
        row_from_letters(letters)
        for letters in product(("I", "X", "Z", "Y"), repeat=width)
    )
    mismatches = 0
    maximum_residual = 0.0
    hadamard_tests = 0
    primitive_tests = 0
    pair_tests = 0

    h_matrix = dense_h(ancilla, width)
    for row in test_rows:
        actual = dense_pauli(conjugate_h(row, ancilla), width)
        expected = h_matrix @ dense_pauli(row, width) @ h_matrix.conj().T
        residual = float(np.linalg.norm(actual - expected))
        maximum_residual = max(maximum_residual, residual)
        mismatches += residual > TOL
        hadamard_tests += 1

    for target in (1, 2):
        for letter in ("X", "Z", "Y"):
            target_row = pauli_letter(target, letter)
            unitary = dense_controlled_target(target_row, ancilla, width)
            for row in test_rows:
                actual = dense_pauli(
                    conjugate_controlled_letter(row, ancilla, target, letter),
                    width,
                )
                expected = unitary @ dense_pauli(row, width) @ unitary.conj().T
                residual = float(np.linalg.norm(actual - expected))
                maximum_residual = max(maximum_residual, residual)
                mismatches += residual > TOL
                primitive_tests += 1

    for target_letters in product(("I", "X", "Z", "Y"), repeat=2):
        target_row = Pauli()
        gates: list[Gate] = [("H", ancilla)]
        for target, letter in zip((1, 2), target_letters):
            if letter != "I":
                target_row = multiply(
                    target_row, pauli_letter(target, letter)
                )
                gates.append(("CP", ancilla, target, letter))
        gates.append(("H", ancilla))
        controlled = dense_controlled_target(target_row, ancilla, width)
        unitary = h_matrix @ controlled @ h_matrix
        for row in test_rows:
            actual = dense_pauli(conjugate_word(row, tuple(gates)), width)
            expected = unitary @ dense_pauli(row, width) @ unitary.conj().T
            residual = float(np.linalg.norm(actual - expected))
            maximum_residual = max(maximum_residual, residual)
            mismatches += residual > TOL
            pair_tests += 1

    return {
        "target_Paulis_exhausted": 16,
        "three_qubit_Paulis_exhausted": len(test_rows),
        "Hadamard_conjugation_tests": hadamard_tests,
        "controlled_Pauli_primitive_tests": primitive_tests,
        "Pauli_pair_sandwich_tests": pair_tests,
        "dense_selftest_mismatches": int(mismatches),
        "maximum_dense_residual": maximum_residual,
    }


def anchor_cell(fixture: M.CompanionFixture, tag: tuple) -> Coord:
    if tag[0] != "edge":
        return fixture.cells[tag[1]]
    left, right, owner, *_rest = fixture.edges[tag[1]]
    if isinstance(owner, int):
        anchor = fixture.cells[owner]
    else:
        anchor = tuple(owner)
    endpoints = {fixture.cells[left], fixture.cells[right]}
    if anchor not in endpoints:
        raise ValueError(f"edge owner {owner!r} is not an endpoint for {tag!r}")
    return anchor


def physical_restriction(row: Pauli, q: int) -> Pauli:
    mask = (1 << q) - 1
    return EB.canonical(Pauli(x=row.x & mask, z=row.z & mask))


def shifted_physical_row(row: Pauli, q: int) -> Pauli:
    return Pauli(row.phase, row.x << q, row.z << q)


def physical_row_for_tag(
    fixture: M.CompanionFixture, tag: tuple
) -> Pauli:
    """Rebuild the tag row in the fixture's full physical representation."""
    family = tag[0]
    if family == "onsite_Z":
        cell, mode = tag[1:3]
        return Pauli(z=1 << (6 * cell + mode))
    if family == "onsite_XX":
        cell, left_mode = tag[1:3]
        return Pauli(
            x=(1 << (6 * cell + left_mode))
            | (1 << (6 * cell + left_mode + 1))
        )
    if family == "edge":
        return fixture.physical_terms(tag[1])[2]
    raise ValueError(f"unsupported direct-basis tag {tag!r}")


def joint_companion_row(physical: Pauli, q: int) -> Pauli:
    """Canonical product of code and companion-bank physical rows."""
    return EB.canonical(
        multiply(physical, shifted_physical_row(physical, q))
    )


def compile_fixture(fixture: M.CompanionFixture) -> dict[str, object]:
    graph, tags = P.direct_graph_basis(fixture)
    targets = EB.target_rows(fixture, tags)
    q = fixture.qubits
    m = fixture.matter_qubits
    row_count = len(graph)
    words = []
    coarse_binary_failures = 0
    physical_tag_rebuild_failures = 0
    phase_erasure_rows = 0
    for index, (graph_row, target, tag) in enumerate(
        zip(graph, targets, tags)
    ):
        physical = physical_restriction(graph_row, q)
        rebuilt_physical = physical_row_for_tag(fixture, tag)
        physical_tag_rebuild_failures += (
            fields(physical) != fields(rebuilt_physical)
        )
        coarse_x = (graph_row.x >> q) & ((1 << m) - 1)
        coarse_z = (graph_row.z >> q) & ((1 << m) - 1)
        coarse_binary_failures += (
            (coarse_x, coarse_z) != (target.x, target.z)
        )
        uncanonical = multiply(
            physical, shifted_physical_row(rebuilt_physical, q)
        )
        measured = EB.canonical(uncanonical)
        phase_erasure_rows += uncanonical.phase % 4 != measured.phase % 4
        ancilla = 2 * q + index
        gates: list[Gate] = [("H", ancilla)]
        realized = Pauli()
        for qubit in supported_qubits(measured):
            letter = letter_at(measured, qubit)
            gates.append(("CP", ancilla, qubit, letter))
            realized = multiply(realized, pauli_letter(qubit, letter))
        gates.append(("H", ancilla))
        anchor = anchor_cell(fixture, tag)
        physical_cells = P.pauli_cells(fixture, physical)
        bank_cells = P.pauli_cells(fixture, rebuilt_physical)
        semantic_support_cells = frozenset(
            set(physical_cells) | set(bank_cells) | {anchor}
        )
        route = P.returned_route(anchor, semantic_support_cells)
        forward_failures, inverse_failures = P.route_execution_failures(
            anchor, route
        )
        # A zero-length onsite route touches no mobile rail.  For a nonempty
        # route, only rail sites appearing in literal transitions are owned.
        routed_cells: set[Coord] = set()
        for left, right in route:
            routed_cells.update((left, right))
        support_cells = frozenset(
            set(semantic_support_cells) | routed_cells
        )
        cell_to_index = {
            cell: cell_index
            for cell_index, cell in enumerate(fixture.cells)
        }
        rail_base = 2 * q + row_count
        rail_indices = {
            rail_base + cell_to_index[cell] for cell in routed_cells
        }
        qubit_support = frozenset(
            set(supported_qubits(measured))
            | {ancilla}
            | rail_indices
        )
        words.append({
            "index": index,
            "tag": tag,
            "target": target,
            "graph": graph_row,
            "physical": physical,
            "row": measured,
            "realized_character": realized,
            "ancilla": ancilla,
            "anchor": anchor,
            "support_cells": support_cells,
            "bank_cells": bank_cells,
            "route": route,
            "route_forward_failures": forward_failures,
            "route_inverse_failures": inverse_failures,
            "gates": tuple(gates),
            "qubit_support": qubit_support,
            "controlled_primitives": len(gates) - 2,
            "rail_moves": len(route),
        })
    return {
        "fixture": fixture,
        "graph": graph,
        "tags": tags,
        "targets": targets,
        "words": tuple(words),
        "coarse_input_binary_replacement_failures": coarse_binary_failures,
        "physical_tag_rebuild_failures": physical_tag_rebuild_failures,
        "precanonical_phase_erasure_rows": phase_erasure_rows,
    }


def exhaustive_one_cell_even_rows(modes: int) -> tuple[Pauli, ...]:
    return tuple(
        EB.canonical(Pauli(x=x, z=z))
        for x in range(1 << modes)
        if not (x.bit_count() & 1)
        for z in range(1 << modes)
    )


def box_certificate(
    shape: tuple[int, int, int],
    atlas: dict[str, object],
) -> tuple[dict[str, object], dict[str, object]]:
    fixture = O.arbitrary_fixture(Q.shape_cells(shape))
    compiled = compile_fixture(fixture)
    graph = compiled["graph"]
    tags = compiled["tags"]
    targets = compiled["targets"]
    words = compiled["words"]
    measured_rows = tuple(word["row"] for word in words)
    encoded_graph_rows = tuple(
        joint_companion_row(
            physical_row_for_tag(fixture, tag), fixture.qubits
        )
        for tag in tags
    )
    corrections = tuple(
        P.correction_from_atlas(fixture, tag, atlas) for tag in tags
    )
    q = fixture.qubits
    m = fixture.matter_qubits
    graph_width = q + m
    compiled_width = 2 * q

    target_rank = P.C.R.F.base.gf2_rank(
        row.symplectic(m) for row in targets
    )
    graph_rank = P.C.R.F.base.gf2_rank(
        row.symplectic(graph_width) for row in graph
    )
    compiled_rank = P.C.R.F.base.gf2_rank(
        row.symplectic(compiled_width) for row in measured_rows
    )
    commutator_failures = sum(
        M.symplectic(
            left.symplectic(compiled_width),
            right.symplectic(compiled_width),
            compiled_width,
        )
        for index, left in enumerate(measured_rows)
        for right in measured_rows[:index]
    )
    hermiticity_failures = sum(
        row.phase % 4 != ((row.x & row.z).bit_count() & 1)
        for row in measured_rows
    )
    compiled_character_binary_failures = sum(
        (word["realized_character"].x, word["realized_character"].z)
        != (word["row"].x, word["row"].z)
        for word in words
    )
    compiled_character_phase_failures = sum(
        fields(word["realized_character"]) != fields(word["row"])
        for word in words
    )

    dilation_x_invariance_failures = 0
    dilation_z_character_failures = 0
    dilation_other_measured_row_failures = 0
    dilation_graph_row_failures = 0
    for index, word in enumerate(words):
        ancilla = word["ancilla"]
        x_ancilla = Pauli(x=1 << ancilla)
        z_ancilla = Pauli(z=1 << ancilla)
        actual_x = conjugate_word(x_ancilla, word["gates"])
        actual_z = conjugate_word(z_ancilla, word["gates"])
        expected_z_character = multiply(z_ancilla, word["row"])
        dilation_x_invariance_failures += (
            fields(actual_x) != fields(x_ancilla)
        )
        dilation_z_character_failures += (
            fields(actual_z) != fields(expected_z_character)
        )
        for other_index, other in enumerate(measured_rows):
            if other_index == index:
                continue
            dilation_other_measured_row_failures += (
                fields(conjugate_word(other, word["gates"]))
                != fields(other)
            )
        for graph_row in encoded_graph_rows:
            dilation_graph_row_failures += (
                fields(conjugate_word(graph_row, word["gates"]))
                != fields(graph_row)
            )

    route_forward_failures = sum(
        word["route_forward_failures"] for word in words
    )
    route_inverse_failures = sum(
        word["route_inverse_failures"] for word in words
    )
    maximum_word_support_cells = max(
        (len(word["support_cells"]) for word in words), default=0
    )
    maximum_word_support_diameter = max(
        (
            P.R.support_diameter(word["support_cells"])
            for word in words
        ),
        default=0,
    )
    failing_support_rows = tuple(
        {
            "index": word["index"],
            "tag": word["tag"],
            "support_cells": tuple(sorted(word["support_cells"])),
            "support_cell_count": len(word["support_cells"]),
            "support_diameter": P.R.support_diameter(
                word["support_cells"]
            ),
        }
        for word in words
        if len(word["support_cells"]) > 2
        or P.R.support_diameter(word["support_cells"]) > 1
    )

    correction_syndrome_failures = 0
    correction_support_failures = 0
    correction_supports = []
    maximum_correction_cells = 0
    maximum_correction_diameter = 0
    for target_index, (tag, correction) in enumerate(
        zip(tags, corrections)
    ):
        support = P.pauli_cells(fixture, correction)
        correction_supports.append(support)
        declared = (
            {fixture.cells[tag[1]]}
            if tag[0] != "edge"
            else {
                fixture.cells[cell]
                for cell in fixture.edges[tag[1]][:2]
            }
        )
        correction_support_failures += not support <= declared
        maximum_correction_cells = max(
            maximum_correction_cells, len(support)
        )
        maximum_correction_diameter = max(
            maximum_correction_diameter, P.R.support_diameter(support)
        )
        for row_index, stabilizer in enumerate(graph):
            correction_syndrome_failures += (
                M.symplectic(
                    correction.symplectic(graph_width),
                    stabilizer.symplectic(graph_width),
                    graph_width,
                )
                != int(row_index == target_index)
            )

    relations = M.kernel_relations(tuple(
        target.symplectic(m) for target in targets
    ))
    if len(fixture.cells) == 1:
        branch_rows = exhaustive_one_cell_even_rows(m)
        branch_enumeration = "exhaustive even-X Pauli basis"
    else:
        branch_rows = EB.deterministic_even_samples(m)
        branch_enumeration = "deterministic_even_samples"
    branch_replay_failures = 0
    branch_character_entry_failures = 0
    branch_relation_even_sum_failures = 0
    for error in branch_rows:
        syndrome = tuple(
            M.symplectic(
                error.symplectic(m), target.symplectic(m), m
            )
            for target in targets
        )
        correction = EB.pauli_product(
            row
            for bit, row in zip(syndrome, corrections)
            if bit
        )
        replay = tuple(
            M.symplectic(
                correction.symplectic(graph_width),
                graph_row.symplectic(graph_width),
                graph_width,
            )
            for graph_row in graph
        )
        branch_replay_failures += replay != syndrome
        branch_character_entry_failures += sum(
            actual != expected
            for actual, expected in zip(replay, syndrome)
        )
        branch_relation_even_sum_failures += sum(
            sum(
                syndrome[index]
                for index in range(len(syndrome))
                if (relation >> index) & 1
            )
            & 1
            for relation in relations
        )

    deleted_index = len(corrections) // 2
    deletion_residual = M.symplectic(
        corrections[deleted_index].symplectic(graph_width),
        graph[deleted_index].symplectic(graph_width),
        graph_width,
    )

    measurement_assignment = EB.greedy_layers(tuple(
        word["qubit_support"] for word in words
    ))
    correction_qubit_supports = tuple(
        frozenset(
            qubit
            for qubit in range(q)
            if ((correction.x | correction.z) >> qubit) & 1
        )
        for correction in corrections
    )
    correction_assignment = EB.greedy_layers(correction_qubit_supports)
    measurement_layer_count = max(
        measurement_assignment, default=-1
    ) + 1
    correction_layer_count = max(
        correction_assignment, default=-1
    ) + 1

    def layer_census(
        assignment: tuple[int, ...],
        supports: tuple[frozenset[int], ...],
    ) -> tuple[dict[str, int], ...]:
        return tuple(
            {
                "layer": layer,
                "vertices": sum(value == layer for value in assignment),
                "touched_qubits": len(frozenset().union(*(
                    support
                    for value, support in zip(assignment, supports)
                    if value == layer
                ))),
            }
            for layer in range(max(assignment, default=-1) + 1)
        )

    measurement_supports = tuple(
        word["qubit_support"] for word in words
    )
    measurement_layer_census = layer_census(
        measurement_assignment, measurement_supports
    )
    correction_layer_census = layer_census(
        correction_assignment, correction_qubit_supports
    )

    summary = {
        "shape": shape,
        "cells": len(fixture.cells),
        "edges": len(fixture.edges),
        "physical_output_M2": q,
        "companion_encoded_live_input_M2": q,
        "rows": len(words),
        "target_even_algebra_rank": target_rank,
        "expected_connected_even_algebra_rank": 2 * m - 1,
        "expected_direct_graph_family_rank": (
            11 * len(fixture.cells) + len(fixture.edges)
        ),
        "direct_graph_basis_rank": graph_rank,
        "compiled_measured_row_rank": compiled_rank,
        "compiled_row_commutator_failures": commutator_failures,
        "compiled_row_hermiticity_failures": hermiticity_failures,
        "coarse_input_binary_replacement_failures": compiled[
            "coarse_input_binary_replacement_failures"
        ],
        "physical_tag_rebuild_failures": compiled[
            "physical_tag_rebuild_failures"
        ],
        "precanonical_phase_erasure_rows": compiled[
            "precanonical_phase_erasure_rows"
        ],
        "compiled_character_binary_failures": (
            compiled_character_binary_failures
        ),
        "compiled_character_phase_failures": (
            compiled_character_phase_failures
        ),
        "dilation_X_invariance_failures": (
            dilation_x_invariance_failures
        ),
        "dilation_Z_character_failures": (
            dilation_z_character_failures
        ),
        "dilation_other_measured_row_invariance_failures": (
            dilation_other_measured_row_failures
        ),
        "dilation_graph_row_invariance_failures": (
            dilation_graph_row_failures
        ),
        "Hadamard_primitives": 2 * len(words),
        "controlled_Pauli_primitives": sum(
            word["controlled_primitives"] for word in words
        ),
        "rail_move_primitives": sum(
            word["rail_moves"] for word in words
        ),
        "compiled_primitive_count": sum(
            2 + word["controlled_primitives"] + word["rail_moves"]
            for word in words
        ),
        "route_transitions": sum(len(word["route"]) for word in words),
        "route_forward_failures": route_forward_failures,
        "route_inverse_failures": route_inverse_failures,
        "maximum_compiled_word_support_cells": maximum_word_support_cells,
        "maximum_compiled_word_support_diameter": (
            maximum_word_support_diameter
        ),
        "failing_compiled_word_support_rows": failing_support_rows,
        "physical_private_dual_syndrome_failures": (
            correction_syndrome_failures
        ),
        "physical_private_dual_support_failures": (
            correction_support_failures
        ),
        "maximum_private_dual_support_cells": (
            maximum_correction_cells
        ),
        "maximum_private_dual_support_diameter": (
            maximum_correction_diameter
        ),
        "measurement_conflict_layers": measurement_layer_count,
        "measurement_layer_census": measurement_layer_census,
        "physical_correction_conflict_layers": correction_layer_count,
        "physical_correction_layer_census": correction_layer_census,
        "branch_enumeration": branch_enumeration,
        "lawful_even_characters_tested": len(branch_rows),
        "branch_private_dual_replay_failures": branch_replay_failures,
        "branch_character_entry_failures": (
            branch_character_entry_failures
        ),
        "target_relation_rows": len(relations),
        "branch_target_relation_even_sum_failures": (
            branch_relation_even_sum_failures
        ),
        "delete_matching_private_dual_index": deleted_index,
        "delete_matching_private_dual_sign_residual": deletion_residual,
    }
    compiled.update({
        "corrections": corrections,
        "measurement_assignment": measurement_assignment,
        "correction_assignment": correction_assignment,
        "summary": summary,
    })
    return summary, compiled


def layer_count_vector(
    compiled: dict[str, object], atlas: dict[str, object]
) -> tuple[int, int]:
    fixture = compiled["fixture"]
    words = compiled["words"]
    tags = compiled["tags"]
    measurement_assignment = EB.greedy_layers(tuple(
        word["qubit_support"] for word in words
    ))
    corrections = tuple(
        P.correction_from_atlas(fixture, tag, atlas) for tag in tags
    )
    correction_assignment = EB.greedy_layers(tuple(
        frozenset(
            qubit
            for qubit in range(fixture.qubits)
            if ((row.x | row.z) >> qubit) & 1
        )
        for row in corrections
    ))
    return (
        max(measurement_assignment, default=-1) + 1,
        max(correction_assignment, default=-1) + 1,
    )


def transformed_companion_row(
    word: dict[str, object],
    images: tuple[Pauli, ...],
    q: int,
) -> Pauli:
    """Transport the code physical row, then rebuild its covariant mirror."""
    transported_physical = V.transform_row(word["physical"], images)
    mask = (1 << q) - 1
    transported_physical = Pauli(
        transported_physical.phase,
        transported_physical.x & mask,
        transported_physical.z & mask,
    )
    return joint_companion_row(transported_physical, q)


def reversed_edge_physical_row(
    fixture: M.CompanionFixture, edge_index: int
) -> tuple[Pauli, Coord]:
    """Ask fixture machinery for the explicitly endpoint-reversed edge row."""
    left, right, _owner, axis, left_mode, right_mode = (
        fixture.edges[edge_index]
    )
    reversed_record = (
        right,
        left,
        fixture.cells[right],
        axis,
        right_mode,
        left_mode,
    )
    reversed_fixture = copy(fixture)
    reversed_edges = list(fixture.edges)
    reversed_edges[edge_index] = reversed_record
    object.__setattr__(reversed_fixture, "edges", tuple(reversed_edges))
    return (
        reversed_fixture.physical_terms(edge_index)[2],
        fixture.cells[right],
    )


def word_census_vector(word: dict[str, object]) -> tuple[int, int, int, int]:
    support = word["support_cells"]
    return (
        len(support),
        P.R.support_diameter(support),
        2 + word["controlled_primitives"] + word["rail_moves"],
        len(word["route"]),
    )


def transported_row_census_vector(
    fixture: M.CompanionFixture,
    row: Pauli,
    anchor: Coord,
) -> tuple[int, int, int, int]:
    q = fixture.qubits
    physical = physical_restriction(row, q)
    semantic_support = frozenset(
        set(P.pauli_cells(fixture, physical)) | {anchor}
    )
    route = P.returned_route(anchor, semantic_support)
    routed_cells = {
        cell for transition in route for cell in transition
    }
    support = frozenset(set(semantic_support) | routed_cells)
    return (
        len(support),
        P.R.support_diameter(support),
        2 + len(supported_qubits(row)) + len(route),
        len(route),
    )


def family_census_vectors(
    words: tuple[dict[str, object], ...],
) -> dict[str, tuple[tuple[int, int, int, int], ...]]:
    families = ("onsite_Z", "onsite_XX", "edge")
    return {
        family: tuple(sorted(
            word_census_vector(word)
            for word in words
            if word["tag"][0] == family
        ))
        for family in families
    }


def compressed_family_census(
    vectors: dict[str, tuple[tuple[int, int, int, int], ...]]
) -> dict[str, tuple[dict[str, object], ...]]:
    return {
        family: tuple(
            {"vector": vector, "rows": rows}
            for vector, rows in sorted(Counter(family_rows).items())
        )
        for family, family_rows in vectors.items()
    }


def compiled_schedule_transport_certificate(
    source_by_shape: dict[tuple[int, int, int], dict[str, object]],
    atlas: dict[str, object],
) -> dict[str, object]:
    frames = V.T.proper_cubic_frames()
    shifts = tuple(product((0, 1), repeat=3))
    families = ("onsite_Z", "onsite_XX", "edge")
    shape_reports = []
    total_signed_failures = Counter({family: 0 for family in families})
    total_binary_failures = Counter({family: 0 for family in families})
    total_edge_signed_class_failures = 0
    total_edge_binary_class_failures = 0
    total_edge_forward_classes = 0
    total_edge_reversed_classes = 0
    total_census_failures = Counter({family: 0 for family in families})
    for shape in ((2, 2, 2), (3, 2, 2)):
        source_compiled = source_by_shape[shape]
        source = source_compiled["fixture"]
        source_words = source_compiled["words"]
        source_census = family_census_vectors(source_words)
        signed_failures = Counter({family: 0 for family in families})
        binary_failures = Counter({family: 0 for family in families})
        edge_signed_class_failures = 0
        edge_binary_class_failures = 0
        edge_forward_classes = 0
        edge_reversed_classes = 0
        census_failures = Counter({family: 0 for family in families})
        for frame in frames:
            for shift in shifts:
                # This is the recurrent runner's literal affine rebuild:
                # transform the complete ordered cell tuple, then rebuild one
                # global fixture.  No covering fixture is concatenated.
                transformed_cells = Q.affine_cells(
                    source.cells, frame, shift
                )
                target = O.arbitrary_fixture(transformed_cells)
                target_compiled = compile_fixture(target)
                target_seed = Q.transported_seed(
                    frame, shift, (0, 0, 0)
                )
                images = V.choi_images(
                    source, target, frame, shift, target_seed
                )
                literal_transported_rows = tuple(
                    transformed_companion_row(
                        word, images, source.qubits
                    )
                    for word in source_words
                )
                target_words = target_compiled["words"]
                transported_anchors = tuple(
                    V.affine_cell(word["anchor"], frame, shift)
                    for word in source_words
                )
                target_word_by_tag = {
                    word["tag"]: word for word in target_words
                }
                target_cell_index = {
                    cell: index
                    for index, cell in enumerate(target.cells)
                }
                # Onsite adjacent-XX generators are a local chart basis:
                # transport the family and anchor, then rebuild the complete
                # canonical family at that target cell.  Individual path
                # generators are deliberately not required to be frame
                # equivariant.  Edge rows retain their literal tableau image
                # because their two fixture-derived orientation classes are
                # audited explicitly below.
                comparison_rows = tuple(
                    (
                        target_word_by_tag[(
                            word["tag"][0],
                            target_cell_index[mapped_anchor],
                            word["tag"][2],
                        )]["row"]
                        if word["tag"][0] != "edge"
                        else transported_row
                    )
                    for transported_row, mapped_anchor, word in zip(
                        literal_transported_rows,
                        transported_anchors,
                        source_words,
                    )
                )

                for family in ("onsite_Z", "onsite_XX"):
                    transported_signed = Counter(
                        (fields(row), anchor)
                        for row, anchor, word in zip(
                            comparison_rows,
                            transported_anchors,
                            source_words,
                        )
                        if word["tag"][0] == family
                    )
                    rebuilt_signed = Counter(
                        (fields(word["row"]), word["anchor"])
                        for word in target_words
                        if word["tag"][0] == family
                    )
                    signed_failures[family] += (
                        transported_signed != rebuilt_signed
                    )
                    transported_binary = Counter(
                        ((row.x, row.z), anchor)
                        for row, anchor, word in zip(
                            comparison_rows,
                            transported_anchors,
                            source_words,
                        )
                        if word["tag"][0] == family
                    )
                    rebuilt_binary = Counter(
                        ((word["row"].x, word["row"].z), word["anchor"])
                        for word in target_words
                        if word["tag"][0] == family
                    )
                    binary_failures[family] += (
                        transported_binary != rebuilt_binary
                    )

                target_edge_words = {
                    word["tag"][1]: word
                    for word in target_words
                    if word["tag"][0] == "edge"
                }
                target_edge_by_endpoints = {
                    frozenset((
                        target.cells[edge[0]],
                        target.cells[edge[1]],
                    )): edge_index
                    for edge_index, edge in enumerate(target.edges)
                }
                mapped_edge_indices = Counter()
                context_edge_signed_failures = 0
                context_edge_binary_failures = 0
                for row, mapped_anchor, word in zip(
                    literal_transported_rows,
                    transported_anchors,
                    source_words,
                ):
                    if word["tag"][0] != "edge":
                        continue
                    source_edge = source.edges[word["tag"][1]]
                    mapped_endpoints = frozenset((
                        V.affine_cell(
                            source.cells[source_edge[0]], frame, shift
                        ),
                        V.affine_cell(
                            source.cells[source_edge[1]], frame, shift
                        ),
                    ))
                    target_edge_index = target_edge_by_endpoints.get(
                        mapped_endpoints
                    )
                    if target_edge_index is None:
                        context_edge_signed_failures += 1
                        context_edge_binary_failures += 1
                        continue
                    mapped_edge_indices[target_edge_index] += 1
                    forward_word = target_edge_words[target_edge_index]
                    reversed_physical, reversed_anchor = (
                        reversed_edge_physical_row(
                            target, target_edge_index
                        )
                    )
                    reversed_row = joint_companion_row(
                        reversed_physical, target.qubits
                    )
                    actual_signed = (fields(row), mapped_anchor)
                    forward_signed = (
                        fields(forward_word["row"]),
                        forward_word["anchor"],
                    )
                    reversed_signed = (
                        fields(reversed_row),
                        reversed_anchor,
                    )
                    if actual_signed == forward_signed:
                        edge_forward_classes += 1
                    elif actual_signed == reversed_signed:
                        edge_reversed_classes += 1
                    else:
                        context_edge_signed_failures += 1
                    actual_binary = ((row.x, row.z), mapped_anchor)
                    forward_binary = (
                        (forward_word["row"].x, forward_word["row"].z),
                        forward_word["anchor"],
                    )
                    reversed_binary = (
                        (reversed_row.x, reversed_row.z),
                        reversed_anchor,
                    )
                    if actual_binary not in (
                        forward_binary,
                        reversed_binary,
                    ):
                        context_edge_binary_failures += 1
                expected_edge_indices = Counter(target_edge_words.keys())
                edge_bijection_failure = (
                    mapped_edge_indices != expected_edge_indices
                )
                signed_failures["edge"] += bool(
                    context_edge_signed_failures
                    or edge_bijection_failure
                )
                binary_failures["edge"] += bool(
                    context_edge_binary_failures
                    or edge_bijection_failure
                )
                edge_signed_class_failures += (
                    context_edge_signed_failures
                )
                edge_binary_class_failures += (
                    context_edge_binary_failures
                )

                transported_census = {
                    family: tuple(sorted(
                        transported_row_census_vector(
                            target, row, anchor
                        )
                        for row, anchor, word in zip(
                            comparison_rows,
                            transported_anchors,
                            source_words,
                        )
                        if word["tag"][0] == family
                    ))
                    for family in families
                }
                rebuilt_census = family_census_vectors(target_words)
                for family in families:
                    census_failures[family] += (
                        rebuilt_census[family]
                        != transported_census[family]
                    )
        contexts = len(frames) * len(shifts)
        shape_report = {
            "shape": shape,
            "proper_cubic_frames": len(frames),
            "translation_parities": len(shifts),
            "contexts": contexts,
            "family_signed_multiset_failures": dict(
                signed_failures
            ),
            "family_binary_multiset_failures": dict(
                binary_failures
            ),
            "edge_orientation_signed_class_failures": (
                edge_signed_class_failures
            ),
            "edge_orientation_binary_class_failures": (
                edge_binary_class_failures
            ),
            "edge_forward_orientation_classes": edge_forward_classes,
            "edge_reversed_orientation_classes": edge_reversed_classes,
            "family_census_vector_invariance_failures": dict(
                census_failures
            ),
            "source_family_census_vectors": compressed_family_census(
                source_census
            ),
        }
        shape_reports.append(shape_report)
        total_signed_failures.update(signed_failures)
        total_binary_failures.update(binary_failures)
        total_edge_signed_class_failures += (
            edge_signed_class_failures
        )
        total_edge_binary_class_failures += (
            edge_binary_class_failures
        )
        total_edge_forward_classes += edge_forward_classes
        total_edge_reversed_classes += edge_reversed_classes
        total_census_failures.update(census_failures)
    return {
        "shapes": tuple(shape_reports),
        "proper_cubic_frames": len(frames),
        "translation_parities": len(shifts),
        "contexts": sum(row["contexts"] for row in shape_reports),
        "family_signed_multiset_failures": dict(
            total_signed_failures
        ),
        "family_binary_multiset_failures": dict(
            total_binary_failures
        ),
        "edge_orientation_signed_class_failures": (
            total_edge_signed_class_failures
        ),
        "edge_orientation_binary_class_failures": (
            total_edge_binary_class_failures
        ),
        "edge_forward_orientation_classes": (
            total_edge_forward_classes
        ),
        "edge_reversed_orientation_classes": (
            total_edge_reversed_classes
        ),
        "family_census_vector_invariance_failures": dict(
            total_census_failures
        ),
    }


def fixture_preservation_certificate(
    atlas: dict[str, object],
    baseline_exact: tuple[dict[str, object], ...],
    baseline_box: dict[str, object],
) -> tuple[tuple[dict[str, object], ...], dict[str, object]]:
    exact = tuple(
        EB.abstract_teleportation_certificate(modes)
        for modes in (2, 3)
    )
    rerun_box = EB.box_certificate((2, 2, 2), atlas)
    exact_keys = (
        "Bell_outcomes",
        "expected_outcomes",
        "Bell_basis_orthonormality_residual",
        "corrected_branch_identity_residual",
        "Kraus_completeness_residual",
        "generator_rank",
        "expected_even_rank",
    )
    critical_box_keys = tuple(
        key
        for key in baseline_box
        if key.endswith("failures")
        or key in (
            "target_even_algebra_rank",
            "expected_connected_even_algebra_rank",
            "doubled_Bell_row_rank",
            "maximum_private_dual_support_cells",
            "maximum_private_dual_support_diameter",
        )
    )
    exact_change_failures = sum(
        before[key] != after[key]
        for before, after in zip(baseline_exact, exact)
        for key in exact_keys
    )
    box_change_failures = sum(
        baseline_box[key] != rerun_box[key]
        for key in critical_box_keys
    )
    residual_maximum = max(
        row[key]
        for row in exact
        for key in (
            "Bell_basis_orthonormality_residual",
            "corrected_branch_identity_residual",
            "Kraus_completeness_residual",
        )
    )
    return exact, {
        "exact_certificate_change_failures": exact_change_failures,
        "critical_box_field_change_failures": box_change_failures,
        "critical_box_fields_compared": critical_box_keys,
        "maximum_exact_CPTP_residual": residual_maximum,
        "all_three_residuals_below_1e-12": all(
            row[key] < TOL
            for row in exact
            for key in (
                "Bell_basis_orthonormality_residual",
                "corrected_branch_identity_residual",
                "Kraus_completeness_residual",
            )
        ),
    }


def controls_certificate(
    compiled_by_shape: dict[tuple[int, int, int], dict[str, object]]
) -> dict[str, object]:
    deletion_residuals = {
        str(shape): compiled["summary"][
            "delete_matching_private_dual_sign_residual"
        ]
        for shape, compiled in compiled_by_shape.items()
    }

    route_word = next(
        (
            word
            for compiled in compiled_by_shape.values()
            for word in compiled["words"]
            if word["route"]
        ),
        None,
    )
    if route_word is None:
        deleted_final_route_failures = (0, 0)
        deleted_first_route_failures = (0, 0)
    else:
        deleted_final_route_failures = P.route_execution_failures(
            route_word["anchor"], route_word["route"][:-1]
        )
        deleted_first_route_failures = P.route_execution_failures(
            route_word["anchor"], route_word["route"][1:]
        )

    hostile_pair = None
    for compiled in compiled_by_shape.values():
        assignments = compiled["measurement_assignment"]
        for right in range(len(assignments)):
            for left in range(right):
                if assignments[left] == assignments[right]:
                    hostile_pair = (
                        compiled["words"][left],
                        compiled["words"][right],
                    )
                    break
            if hostile_pair is not None:
                break
        if hostile_pair is not None:
            break
    hostile_dilation_failures = 0
    hostile_indices = None
    if hostile_pair is not None:
        left, right = hostile_pair
        wrong_ancilla = right["ancilla"]
        corrupted_gates = tuple(
            (
                ("H", wrong_ancilla)
                if gate[0] == "H"
                else (
                    "CP",
                    wrong_ancilla,
                    gate[2],
                    gate[3],
                )
            )
            for gate in left["gates"]
        )
        x_left = Pauli(x=1 << left["ancilla"])
        expected = multiply(x_left, left["row"])
        actual = conjugate_word(x_left, corrupted_gates)
        hostile_dilation_failures = (
            fields(actual) != fields(expected)
        )
        hostile_indices = (left["index"], right["index"])

    base = compiled_by_shape[(1, 1, 1)]
    fixture = base["fixture"]
    q = fixture.qubits
    m = fixture.matter_qubits
    width = 2 * q
    odd = Pauli(x=1 << q)
    bank_parity = Pauli(z=((1 << m) - 1) << q)
    odd_parity_symplectic = M.symplectic(
        odd.symplectic(width), bank_parity.symplectic(width), width
    )
    base_rank = P.C.R.F.base.gf2_rank(
        word["row"].symplectic(width) for word in base["words"]
    )
    augmented_rank = P.C.R.F.base.gf2_rank(
        tuple(
            word["row"].symplectic(width)
            for word in base["words"]
        )
        + (odd.symplectic(width),)
    )
    odd_detection_failures = (
        odd_parity_symplectic != 1
    ) + (augmented_rank != base_rank + 1)
    return {
        "delete_private_dual_sign_residuals": deletion_residuals,
        "delete_private_dual_detection_failures": sum(
            residual != 1 for residual in deletion_residuals.values()
        ),
        "deleted_final_route_link_failures": (
            deleted_final_route_failures
        ),
        "deleted_first_route_link_failures": (
            deleted_first_route_failures
        ),
        "hostile_same_layer_word_indices": hostile_indices,
        "hostile_ancilla_swap_dilation_identity_failures": (
            hostile_dilation_failures
        ),
        "odd_bank_character_parity_symplectic": (
            odd_parity_symplectic
        ),
        "doubled_row_span_rank": base_rank,
        "odd_augmented_span_rank": augmented_rank,
        "unlawful_odd_input_detection_failures": (
            int(odd_detection_failures)
        ),
    }


def main() -> None:
    started = perf_counter()
    atlas = P.build_private_atlases()
    baseline_exact = tuple(
        EB.abstract_teleportation_certificate(modes)
        for modes in (2, 3)
    )
    baseline_box = EB.box_certificate((2, 2, 2), atlas)

    shapes = (
        (1, 1, 1),
        (2, 2, 2),
        (3, 2, 2),
        (5, 3, 2),
        (4, 4, 4),
        (5, 5, 3),
    )
    box_pairs = tuple(
        box_certificate(shape, atlas) for shape in shapes
    )
    boxes = tuple(pair[0] for pair in box_pairs)
    compiled_by_shape = {
        shape: pair[1] for shape, pair in zip(shapes, box_pairs)
    }

    dense_selftest = dense_selftest_certificate()
    exact, preservation = fixture_preservation_certificate(
        atlas, baseline_exact, baseline_box
    )
    covariance = V.frame_certificate((2, 2, 2), atlas)
    frame_products = V.product_certificate(atlas)
    transport = compiled_schedule_transport_certificate(
        compiled_by_shape, atlas
    )
    controls = controls_certificate(compiled_by_shape)

    row_family_gate = all(
        box["target_even_algebra_rank"]
        == box["expected_connected_even_algebra_rank"]
        and box["compiled_measured_row_rank"]
        == box["direct_graph_basis_rank"]
        and box["direct_graph_basis_rank"]
        == box["expected_direct_graph_family_rank"]
        and box["expected_direct_graph_family_rank"] == box["rows"]
        and box["compiled_row_commutator_failures"] == 0
        and box["compiled_row_hermiticity_failures"] == 0
        and box["coarse_input_binary_replacement_failures"] == 0
        and box["physical_tag_rebuild_failures"] == 0
        and box["compiled_character_binary_failures"] == 0
        for box in boxes
    )
    dilation_gate = all(
        box["compiled_character_phase_failures"] == 0
        and box["dilation_X_invariance_failures"] == 0
        and box["dilation_Z_character_failures"] == 0
        and (
            box[
                "dilation_other_measured_row_invariance_failures"
            ]
            == 0
        )
        and box["dilation_graph_row_invariance_failures"] == 0
        for box in boxes
    )
    branch_gate = all(
        box["physical_private_dual_syndrome_failures"] == 0
        and box["branch_private_dual_replay_failures"] == 0
        and box["branch_character_entry_failures"] == 0
        and box["branch_target_relation_even_sum_failures"] == 0
        and box["delete_matching_private_dual_sign_residual"] == 1
        for box in boxes
    )
    support_gate = all(
        box["route_forward_failures"] == 0
        and box["route_inverse_failures"] == 0
        and box["maximum_compiled_word_support_cells"] <= 2
        and box["maximum_compiled_word_support_diameter"] <= 1
        and box["physical_private_dual_support_failures"] == 0
        and box["maximum_private_dual_support_cells"] <= 2
        and box["maximum_private_dual_support_diameter"] <= 1
        for box in boxes
    )
    def maximum_cell_degree(shape: tuple[int, int, int]) -> int:
        # A cell's degree is bounded per axis: 2 interior neighbours when the
        # dimension admits an interior coordinate, 1 when the dimension is 2,
        # 0 when it is 1. The maximum over cells attains this bound.
        return sum(2 if dim >= 3 else (1 if dim == 2 else 0) for dim in shape)

    layer_law = tuple(
        {
            "shape": list(shape),
            "maximum_cell_degree": maximum_cell_degree(shape),
            "expected_measurement_layers_3_plus_degree": (
                3 + maximum_cell_degree(shape)
            ),
            "measurement_conflict_layers": box["measurement_conflict_layers"],
            "physical_correction_conflict_layers": (
                box["physical_correction_conflict_layers"]
            ),
        }
        for shape, box in zip(shapes, boxes)
    )
    # Compiled measurement coloring is three onsite layers (the Z/XX path
    # graph) plus exactly one seam layer per unit of maximum cell degree:
    # greedy first-fit attains the Koenig edge-coloring bound of the bipartite
    # box graph in the emitted edge order. Correction coloring saturates once
    # the one-cell dual family is dense enough (from 3x2x2 on). Constancy
    # across arbitrary boxes is NOT the covariant statement; the local
    # incidence profile is.
    layer_gate = (
        all(
            entry["measurement_conflict_layers"]
            == entry["expected_measurement_layers_3_plus_degree"]
            for entry in layer_law
        )
        and max(box["measurement_conflict_layers"] for box in boxes) <= 12
        and max(
            box["physical_correction_conflict_layers"] for box in boxes
        )
        <= 24
        and len({
            box["physical_correction_conflict_layers"]
            for box in boxes[2:]
        })
        == 1
    )
    preservation_gate = (
        preservation["exact_certificate_change_failures"] == 0
        and preservation["critical_box_field_change_failures"] == 0
        and preservation["all_three_residuals_below_1e-12"]
    )
    covariance_failure_keys = (
        "signed_projector_failures",
        "private_correction_syndrome_failures",
        "private_correction_support_failures",
        "route_locality_support_or_return_failures",
        "atlas_key_inverse_transport_failures",
        "schedule_key_inverse_transport_failures",
        "Bell_reference_conjugate_chart_failures",
        "syndrome_register_bijection_failures",
        "oriented_factor_2_or_3_edge_row_failures",
    )
    covariance_gate = (
        covariance["proper_cubic_frames"] == 24
        and all(
            covariance[key] == 0 for key in covariance_failure_keys
        )
        and frame_products["ordered_frame_products"] == 576
        and all(
            value == 0
            for key, value in frame_products.items()
            if key.endswith("failures")
        )
    )
    transport_gate = (
        transport["proper_cubic_frames"] == 24
        and transport["translation_parities"] == 8
        and transport["contexts"] == 24 * 8 * 2
        and all(
            value == 0
            for value in transport[
                "family_signed_multiset_failures"
            ].values()
        )
        and all(
            value == 0
            for value in transport[
                "family_binary_multiset_failures"
            ].values()
        )
        and transport["edge_orientation_signed_class_failures"] == 0
        and transport["edge_orientation_binary_class_failures"] == 0
        and all(
            value == 0
            for value in transport[
                "family_census_vector_invariance_failures"
            ].values()
        )
    )
    controls_gate = (
        controls["delete_private_dual_detection_failures"] == 0
        and controls["deleted_final_route_link_failures"][0] > 0
        and any(controls["deleted_first_route_link_failures"])
        and (
            controls[
                "hostile_ancilla_swap_dilation_identity_failures"
            ]
            > 0
        )
        and controls["unlawful_odd_input_detection_failures"] == 0
    )

    checks: list[dict[str, object]] = []

    def check(label: str, condition: bool) -> None:
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "exhaustive dense 8x8 Clifford conjugation self-test has zero mismatches",
        dense_selftest["dense_selftest_mismatches"] == 0,
    )
    check(
        "every direct-basis row on the five-box ladder compiles to an abelian Hermitian live-bank character with unchanged rank",
        row_family_gate,
    )
    check(
        "literal H-controlled-Pauli-H words fix retained X, transport retained Z to Z times R_i, and leave all other measured and graph rows invariant",
        dilation_gate,
    )
    check(
        "one-hot duality, kernel even sums, deletion signs, exhaustive one-cell branches, and deterministic held-box samples replay exactly",
        branch_gate,
    )
    check(
        "every tableau word and frozen private dual has at most two-cell diameter-one support, and every separately certified route returns",
        support_gate,
    )
    check(
        "measurement coloring equals three onsite layers plus one seam layer per maximum cell degree; correction coloring is constant from 3x2x2 (ceilings 12 and 24)",
        layer_gate,
    )
    check(
        "post-compilation two- and three-mode CPTP residuals and Cycle-720 critical fixture fields are unchanged",
        preservation_gate,
    )
    check(
        "reused 24-frame and 576-product covariance surfaces retain zero named failures",
        covariance_gate,
    )
    check(
        "compiled row families and census vectors transport over 24 frames by 8 translation parities with only fixture-derived edge orientation classes",
        transport_gate,
    )
    check(
        "private-dual deletion, deleting the final return link breaks the forward returned-route walk, first-link deletion, hostile ancilla pairing, and odd-row controls are detected",
        controls_gate,
    )

    dilation_and_route_census_verified = (
        row_family_gate
        and dilation_gate
        and support_gate
        and layer_gate
        and covariance_gate
        and transport_gate
        and controls_gate
        and dense_selftest["dense_selftest_mismatches"] == 0
    )
    runtime_seconds = perf_counter() - started
    report = {
        "status": (
            "PASS" if all(row["pass"] for row in checks) else "FAIL"
        ),
        "checks": checks,
        "boxes": boxes,
        "layer_counts": {
            "measurement_by_box": tuple(
                box["measurement_conflict_layers"] for box in boxes
            ),
            "correction_by_box": tuple(
                box["physical_correction_conflict_layers"]
                for box in boxes
            ),
            "layer_law": layer_law,
            "law_statement": (
                "measurement conflict layers = 3 onsite layers (Z/XX path "
                "coloring) + 1 seam layer per unit of maximum cell degree "
                "(greedy first-fit attains the Koenig edge-coloring bound "
                "of the bipartite box graph in the emitted edge order); "
                "correction layers saturate at their one-cell constant "
                "from 3x2x2 on"
            ),
            "correction_constant_from_3x2x2": len({
                box["physical_correction_conflict_layers"]
                for box in boxes[2:]
            }) == 1,
        },
        "dense_selftest": dense_selftest,
        "exact_CPTP_controls": exact,
        "covariance": covariance,
        "frame_products": frame_products,
        "compiled_schedule_transport": transport,
        "controls": controls,
        "fixture_preservation": preservation,
        "runtime_seconds": runtime_seconds,
        "derived": (
            "abstract tableau instruction data, exact integer-Pauli conjugation, "
            "companion-bank joint-rank and abelian censuses, returned-route/"
            "support census, private-dual branch replay, conflict coloring, "
            "and covariant signed/binary family-multiset diagnostics"
        ),
        "supplied": (
            "fixed parity/center sector; one-time Choi genesis inventory; "
            "mixed gauge reference; clean retained syndrome and mobile-rail "
            "banks; frozen private-dual atlas; finite boxes; the live input "
            "is presented in the code's own companion representation "
            "(companion-encoded input bank); a bare global-JW input register "
            "is not used"
        ),
        "open": (
            "a route-expanded nearest-neighbour measurement circuit with "
            "gate/route agreement; autonomous sector/genesis law; a composite "
            "channel joining pump, input leg, corrections, and recurrent "
            "update; downstream time/source/Record/Born acceptance"
        ),
        "claim_boundary": (
            "exact companion-bank Bell-character tableau dilation plus a "
            "separate support and returned-route census on the declared site "
            "map with supplied sector/genesis inventory; route operations are "
            "not compiled into the tableau word, so no route-expanded "
            "nearest-neighbour measurement circuit or joint composite channel "
            "is claimed; ordinals are structure, not time"
        ),
        "bell_character_dilation_and_route_census_verified": (
            dilation_and_route_census_verified
        ),
        "input_Bell_measurement_physical_M2_compiled": False,
        "route_expanded_nearest_neighbour_measurement_compiled": False,
        "authority": "none",
        "audit": "unset",
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
