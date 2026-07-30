#!/usr/bin/env python3
"""Cycle 794: actual proper-cubic generator shear in the O/I/L schedule.

Unlike the landed family-census check, this runner never replaces a literal
transported onsite row by the same-index target generator.  It solves every
transported signed row in the full target basis, independently solves it in
the mapped local cell, constructs the induced clean-syndrome CNOT shear, and
routes the transformed O/I pump, I/L Bell extraction, O correction, syndrome
shear and inversion-CZ firewall on explicit M2 palettes.

This is a conditional bounded circuit theorem.  Circuit layers are schedule
indices, not physical time.  It derives no autonomous genesis or occurrence law.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27 as P
import frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27 as V
import frontier_cycle720_companion_subsystem_m2_update_2026_07_27 as U
import frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30 as S


AUDIT_TIMEOUT_SEC = 1200
NOTE_PATH = (
    "docs/LITERAL_THREE_BANK_PREFIX_RECURRENT_G_ACTUAL_SHEAR_"
    "CYCLE794_BOUNDED_THEOREM_NOTE_2026-07-30.md"
)
AUDIT_INPUT_PATHS = (
    "scripts/frontier_companion_bank_bell_character_dilation_2026_07_28.py",
    "scripts/frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
    "scripts/frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
    "scripts/frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
    "scripts/frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


Coord = tuple[int, int, int]
Frame = tuple[tuple[int, int, int], ...]
ZERO = (0, 0, 0)
TWO_CUBE = (2, 2, 2)
OVERLAP_BOX = (3, 2, 2)


def vector(row, qubits: int) -> int:
    return row.x | (row.z << qubits)


def basis_solver(rows, qubits: int):
    pivots = {}
    for index, row in enumerate(rows):
        value = vector(row, qubits)
        combination = 1 << index
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = (value, combination)
                break
            value ^= pivots[pivot][0]
            combination ^= pivots[pivot][1]
    return pivots


def solve_row(row, pivots, qubits: int):
    value = vector(row, qubits)
    combination = 0
    while value:
        pivot = value.bit_length() - 1
        if pivot not in pivots:
            return None
        value ^= pivots[pivot][0]
        combination ^= pivots[pivot][1]
    return combination


def product_rows(rows, combination: int):
    result = B.Pauli()
    for index, row in enumerate(rows):
        if (combination >> index) & 1:
            result = B.multiply(result, row)
    return result


def inverse_pauli(row):
    inverse = B.Pauli(
        (-row.phase - 2 * (row.x & row.z).bit_count()) % 4,
        row.x,
        row.z,
    )
    if B.fields(B.multiply(row, inverse)) != B.fields(B.Pauli()):
        raise AssertionError("Pauli inverse failed")
    return inverse


def gf2_rank(rows):
    pivots = {}
    for original in rows:
        value = original
        while value:
            pivot = value.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = value
                break
            value ^= pivots[pivot]
    return len(pivots)


def invert_binary(rows):
    size = len(rows)
    mask = (1 << size) - 1
    augmented = [rows[index] | (1 << (size + index)) for index in range(size)]
    for column in range(size):
        pivot = next(
            index for index in range(column, size)
            if (augmented[index] >> column) & 1
        )
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        for index in range(size):
            if index != column and ((augmented[index] >> column) & 1):
                augmented[index] ^= augmented[column]
    if any((row & mask) != 1 << index for index, row in enumerate(augmented)):
        raise AssertionError("binary inverse failed")
    return tuple((row >> size) & mask for row in augmented)


def compose_binary(left_rows, right_rows):
    """Rows of left * right over GF(2)."""
    return tuple(
        _binary_row_product(row, right_rows) for row in left_rows
    )


def _binary_row_product(row: int, target_rows) -> int:
    result = 0
    while row:
        bit = (row & -row).bit_length() - 1
        result ^= target_rows[bit]
        row &= row - 1
    return result


def frame_tuple(frame) -> Frame:
    return tuple(tuple(int(value) for value in row) for row in frame)


def affine(cell: Coord, frame, shift=ZERO) -> Coord:
    return tuple(int(value) for value in (
        np.asarray(frame, dtype=int) @ np.asarray(cell, dtype=int)
        + np.asarray(shift, dtype=int)
    ))


def fixture(shape):
    return B.P.O.arbitrary_fixture(B.P.Q.shape_cells(shape))


def mapped_owner_slot(source, tag, frame, shift=ZERO):
    owner, slot = S.tag_owner_slot(source, tag)
    return affine(owner, frame, shift), slot


def target_alignment(source, target, source_tags, frame, shift=ZERO):
    """Target basis columns labelled by transported source coframe slots."""
    target_compiled = B.compile_fixture(target)
    by_tag = {tag: index for index, tag in enumerate(target_compiled["tags"])}
    target_cell = {cell: index for index, cell in enumerate(target.cells)}
    edge_by_endpoints = {
        frozenset((target.cells[edge[0]], target.cells[edge[1]])): index
        for index, edge in enumerate(target.edges)
    }
    alignment = []
    geometric_failures = 0
    for tag in source_tags:
        if tag[0] != "edge":
            owner, _slot = S.tag_owner_slot(source, tag)
            mapped = affine(owner, frame, shift)
            aligned_tag = (tag[0], target_cell[mapped], tag[2])
            alignment.append(by_tag[aligned_tag])
            continue
        source_edge = source.edges[tag[1]]
        endpoints = frozenset((
            affine(source.cells[source_edge[0]], frame, shift),
            affine(source.cells[source_edge[1]], frame, shift),
        ))
        target_edge = edge_by_endpoints.get(endpoints)
        geometric_failures += target_edge is None
        if target_edge is None:
            alignment.append(-1)
        else:
            alignment.append(by_tag[("edge", target_edge)])
    return tuple(alignment), geometric_failures, target_compiled


def aligned_combination(global_combination: int, alignment) -> int:
    inverse = {target: source for source, target in enumerate(alignment)}
    output = 0
    for target in range(len(alignment)):
        if (global_combination >> target) & 1:
            output |= 1 << inverse[target]
    return output


def signed_span_contains(row, generators, width: int) -> bool:
    pivots = basis_solver(generators, width)
    combination = solve_row(row, pivots, width)
    return (
        combination is not None
        and B.fields(product_rows(generators, combination)) == B.fields(row)
    )


def transport_companion_row(row, images, source_q: int, target_q: int):
    physical = B.physical_restriction(row, source_q)
    mapped = V.transform_row(physical, images)
    mask = (1 << target_q) - 1
    mapped = B.Pauli(mapped.phase, mapped.x & mask, mapped.z & mask)
    return B.joint_companion_row(mapped, target_q)


def local_cnot_synthesis(matrix_rows, groups):
    """CNOT-only implementation of a block-local invertible binary map."""
    operations = []
    failures = 0
    maximum_block_gates = 0
    for group in groups:
        position = {wire: index for index, wire in enumerate(group)}
        local = []
        for wire in group:
            row = matrix_rows[wire]
            outside = row & ~sum(1 << item for item in group)
            failures += outside != 0
            local.append(sum(
                ((row >> target) & 1) << position[target] for target in group
            ))
        if gf2_rank(local) != len(group):
            failures += 1
            continue
        work = list(local)
        elimination = []
        for column in range(len(group)):
            pivot = next(
                index for index in range(column, len(group))
                if (work[index] >> column) & 1
            )
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
                elimination.extend(((column, pivot), (pivot, column), (column, pivot)))
            for index in range(len(group)):
                if index != column and ((work[index] >> column) & 1):
                    work[index] ^= work[column]
                    elimination.append((column, index))
        failures += work != [1 << index for index in range(len(group))]
        block_operations = tuple(
            (group[control], group[target])
            for control, target in reversed(elimination)
        )
        operations.extend(block_operations)
        maximum_block_gates = max(maximum_block_gates, len(block_operations))
        # Exhaust all basis inputs; linearity then certifies the whole block.
        for column in range(len(group)):
            value = 1 << column
            for control, target in block_operations:
                lc = position[control]
                lt = position[target]
                value ^= ((value >> lc) & 1) << lt
            expected = sum(
                ((local[row] >> column) & 1) << row
                for row in range(len(group))
            )
            failures += value != expected
    return tuple(operations), maximum_block_gates, failures


def measurement_gates(rows, system_width: int, ancilla_start: int):
    gates = []
    for index, row in enumerate(rows):
        ancilla = ancilla_start + index
        gates.append(("H", ancilla))
        for qubit in B.supported_qubits(row):
            gates.append(("CP", ancilla, qubit, B.letter_at(row, qubit)))
        gates.append(("H", ancilla))
    return tuple(gates)


def extraction_isometry_certificate(literal_rows, aligned_target_rows, cnot_ops):
    system_width = max(
        max((row.x | row.z).bit_length() for row in literal_rows),
        max((row.x | row.z).bit_length() for row in aligned_target_rows),
    )
    rows = len(literal_rows)
    width = system_width + rows
    literal = measurement_gates(literal_rows, system_width, system_width)
    canonical = measurement_gates(
        aligned_target_rows, system_width, system_width
    )
    shear = tuple(
        ("CP", system_width + control, system_width + target, "X")
        for control, target in cnot_ops
    )
    wrapped = canonical + shear
    literal_stabilizers = tuple(
        B.conjugate_word(B.Pauli(z=1 << (system_width + index)), literal)
        for index in range(rows)
    )
    wrapped_stabilizers = tuple(
        B.conjugate_word(B.Pauli(z=1 << (system_width + index)), wrapped)
        for index in range(rows)
    )
    stabilizer_failures = sum(
        not signed_span_contains(row, wrapped_stabilizers, width)
        for row in literal_stabilizers
    ) + sum(
        not signed_span_contains(row, literal_stabilizers, width)
        for row in wrapped_stabilizers
    )
    logical_failures = 0
    for qubit in range(system_width):
        for letter in ("X", "Z"):
            source = B.pauli_letter(qubit, letter)
            left = B.conjugate_word(source, literal)
            right = B.conjugate_word(source, wrapped)
            logical_failures += not signed_span_contains(
                B.multiply(left, right), wrapped_stabilizers, width
            )
    hostile_order = shear + canonical
    hostile_stabilizers = tuple(
        B.conjugate_word(
            B.Pauli(z=1 << (system_width + index)), hostile_order
        )
        for index in range(rows)
    )
    hostile_failures = sum(
        not signed_span_contains(row, hostile_stabilizers, width)
        for row in literal_stabilizers
    )
    return {
        "system_wires": system_width,
        "clean_syndrome_wires": rows,
        "literal_gates": len(literal),
        "canonical_plus_shear_gates": len(wrapped),
        "signed_output_stabilizer_span_failures": stabilizer_failures,
        "logical_image_mod_output_stabilizer_failures": logical_failures,
        "hostile_shear_before_measurement_span_failures": hostile_failures,
    }


@dataclass
class Context:
    source: object
    target: object
    source_compiled: dict
    target_compiled: dict
    source_corrections: tuple
    target_corrections: tuple
    images: tuple
    rows: tuple
    corrections: tuple
    alignment: tuple
    shear_rows: tuple
    shear_inverse: tuple
    expected_duals: tuple
    repairs: tuple
    owners_slots: tuple
    cnot_ops: tuple
    cnot_max_per_cell: int
    report: dict


def build_context(source, frame, seed, atlas, shift=ZERO):
    frame_array = np.asarray(frame, dtype=int)
    source_compiled = B.compile_fixture(source)
    target = B.O.arbitrary_fixture(B.Q.affine_cells(
        source.cells, frame_array, shift
    ))
    alignment, alignment_failures, target_compiled = target_alignment(
        source, target, source_compiled["tags"], frame_array, shift
    )
    source_corrections = tuple(
        P.correction_from_atlas(source, tag, atlas)
        for tag in source_compiled["tags"]
    )
    target_corrections = tuple(
        P.correction_from_atlas(target, tag, atlas)
        for tag in target_compiled["tags"]
    )
    target_seed = B.Q.transported_seed(frame_array, shift, seed)
    images = V.choi_images(source, target, frame_array, shift, target_seed)
    rows = tuple(
        B.transformed_companion_row(word, images, source.qubits)
        for word in source_compiled["words"]
    )
    corrections = tuple(V.transform_row(row, images) for row in source_corrections)
    target_rows = tuple(word["row"] for word in target_compiled["words"])
    width = 2 * target.qubits
    pivots = basis_solver(target_rows, width)
    global_combinations = tuple(solve_row(row, pivots, width) for row in rows)
    unsolved_rows = sum(value is None for value in global_combinations)
    if unsolved_rows:
        raise AssertionError("literal transported row left target span")
    shear_rows = tuple(
        aligned_combination(value, alignment) for value in global_combinations
    )
    inverse = invert_binary(shear_rows)
    inverse_columns = tuple(
        sum(((inverse[row] >> column) & 1) << row for row in range(len(inverse)))
        for column in range(len(inverse))
    )
    aligned_target_rows = tuple(target_rows[index] for index in alignment)
    aligned_target_corrections = tuple(
        target_corrections[index] for index in alignment
    )
    signed_reconstruction_failures = sum(
        B.fields(product_rows(aligned_target_rows, combination)) != B.fields(row)
        for row, combination in zip(rows, shear_rows)
    )

    # Independent local-cell solve: onsite rows may only use the eleven target
    # rows at the mapped cell.  Edges must solve to the geometrically mapped
    # target edge.  This does not reuse the global combination lookup.
    independent_local_failures = 0
    shear_locality_failures = 0
    maximum_shear_weight = 0
    for source_index, (tag, row, combination) in enumerate(zip(
        source_compiled["tags"], rows, shear_rows
    )):
        owner, _slot = mapped_owner_slot(source, tag, frame_array, shift)
        used = tuple(
            index for index in range(len(shear_rows))
            if (combination >> index) & 1
        )
        maximum_shear_weight = max(maximum_shear_weight, len(used))
        if tag[0] != "edge":
            local_indices = tuple(
                index for index, word in enumerate(target_compiled["words"])
                if word["tag"][0] != "edge" and word["anchor"] == owner
            )
            local_rows = tuple(target_rows[index] for index in local_indices)
            local_pivots = basis_solver(local_rows, width)
            local_combination = solve_row(row, local_pivots, width)
            independent_local_failures += local_combination is None
            if local_combination is not None:
                independent_local_failures += B.fields(product_rows(
                    local_rows, local_combination
                )) != B.fields(row)
            shear_locality_failures += any(
                mapped_owner_slot(
                    source, source_compiled["tags"][index], frame_array, shift
                )[0] != owner
                for index in used
            )
        else:
            source_edge = source.edges[tag[1]]
            endpoints = {
                affine(source.cells[source_edge[0]], frame_array, shift),
                affine(source.cells[source_edge[1]], frame_array, shift),
            }
            used_edge_rows = []
            for index in used:
                used_tag = source_compiled["tags"][index]
                used_owner, _used_slot = mapped_owner_slot(
                    source, used_tag, frame_array, shift
                )
                if used_tag[0] == "edge":
                    used_edge_rows.append(index)
                else:
                    independent_local_failures += used_owner not in endpoints
            independent_local_failures += used_edge_rows != [source_index]

    expected_duals = tuple(
        product_rows(aligned_target_corrections, column)
        for column in inverse_columns
    )
    repairs = tuple(
        B.multiply(mapped, inverse_pauli(expected))
        for mapped, expected in zip(corrections, expected_duals)
    )
    repair_reconstruction_failures = sum(
        B.fields(B.multiply(repair, expected)) != B.fields(mapped)
        for repair, expected, mapped in zip(
            repairs, expected_duals, corrections
        )
    )
    graph_width = target.qubits + target.matter_qubits
    private_dual_failures = sum(
        S.paulis_anticommute(correction, row) != (left == right)
        for left, correction in enumerate(corrections)
        for right, row in enumerate(rows)
    )
    repair_centralizer_failures = sum(
        S.paulis_anticommute(repair, row)
        for repair in repairs for row in rows
    )
    maximum_repair_weight = 0
    maximum_repair_cells = 0
    maximum_repair_diameter = 0
    for repair in repairs:
        cells = P.pauli_cells(target, repair)
        maximum_repair_weight = max(
            maximum_repair_weight, (repair.x | repair.z).bit_count()
        )
        maximum_repair_cells = max(maximum_repair_cells, len(cells))
        maximum_repair_diameter = max(
            maximum_repair_diameter, P.R.support_diameter(cells)
        )

    # Aligned onsite groups are exactly eleven rows/cell.  Aligned edges are
    # one-dimensional permutation blocks and need no CNOT shear.
    onsite_groups = tuple(
        tuple(range(11 * cell, 11 * cell + 11))
        for cell in range(len(source.cells))
    )
    onsite_cnot_ops, cnot_max, cnot_failures = local_cnot_synthesis(
        shear_rows, onsite_groups
    )
    owners_slots = tuple(
        mapped_owner_slot(source, tag, frame_array, shift)
        for tag in source_compiled["tags"]
    )
    onsite_count = 11 * len(source.cells)
    edge_addition_ops = []
    edge_diagonal_failures = 0
    for edge_index in range(onsite_count, len(shear_rows)):
        row = shear_rows[edge_index]
        edge_bits = row & ~((1 << onsite_count) - 1)
        edge_diagonal_failures += edge_bits != 1 << edge_index
        edge_addition_ops.extend(
            (onsite, edge_index)
            for onsite in range(onsite_count)
            if (row >> onsite) & 1
        )
    # Edge additions must act before the onsite block shear: they consume the
    # aligned target onsite syndrome t, whereas the onsite circuit outputs O t.
    cnot_ops = tuple(edge_addition_ops) + onsite_cnot_ops
    # Exhaust every global basis bit, independently of the local synthesis.
    for column in range(len(shear_rows)):
        value = 1 << column
        for control, target_index in cnot_ops:
            value ^= ((value >> control) & 1) << target_index
        expected = sum(
            ((shear_rows[row] >> column) & 1) << row
            for row in range(len(shear_rows))
        )
        cnot_failures += value != expected
    cnot_nonlocal_failures = sum(
        S.manhattan(
            owners_slots[control][0], owners_slots[target_index][0]
        ) > 1
        for control, target_index in cnot_ops
    )
    per_owner_cnot = Counter(owners_slots[target][0] for _control, target in cnot_ops)
    cnot_max = max((cnot_max, *per_owner_cnot.values()))

    # Same-index substitution is the hostile shortcut in the landed family
    # census.  It must fail in active frames while the exact shear succeeds.
    same_slot_signed_mismatches = sum(
        B.fields(row) != B.fields(aligned_target_rows[index])
        for index, row in enumerate(rows)
    )
    deleted_basis = aligned_target_rows[:-1]
    deleted_pivots = basis_solver(deleted_basis, width)
    deleted_basis_unsolved_rows = sum(
        solve_row(row, deleted_pivots, width) is None for row in rows
    )
    report = {
        "rows": len(rows),
        "alignment_failures": alignment_failures,
        "alignment_permutation_failures": (
            len(set(alignment)) != len(alignment)
            or min(alignment) < 0
        ),
        "shear_rank": gf2_rank(shear_rows),
        "maximum_signed_shear_row_weight": maximum_shear_weight,
        "signed_row_reconstruction_failures": signed_reconstruction_failures,
        "independent_local_or_edge_reconstruction_failures": (
            independent_local_failures
        ),
        "shear_locality_failures": shear_locality_failures,
        "private_dual_one_hot_failures": private_dual_failures,
        "repair_reconstruction_failures": repair_reconstruction_failures,
        "repair_centralizer_failures": repair_centralizer_failures,
        "maximum_repair_weight": maximum_repair_weight,
        "maximum_repair_cells": maximum_repair_cells,
        "maximum_repair_diameter": maximum_repair_diameter,
        "cell_and_edge_local_CNOT_shear_gates": len(cnot_ops),
        "maximum_CNOT_shear_gates_per_cell": cnot_max,
        "CNOT_synthesis_or_basis_failures": cnot_failures,
        "CNOT_nonlocal_owner_failures": cnot_nonlocal_failures,
        "aligned_edge_diagonal_failures": edge_diagonal_failures,
        "hostile_same_slot_signed_mismatches": same_slot_signed_mismatches,
        "hostile_deleted_target_basis_unsolved_rows": deleted_basis_unsolved_rows,
    }
    return Context(
        source, target, source_compiled, target_compiled,
        source_corrections, target_corrections, images, rows, corrections,
        alignment, shear_rows, inverse, expected_duals, repairs,
        owners_slots, cnot_ops, cnot_max, report,
    )


def literal_word(context, measured, correction, row_index, stage,
                 include_character=True, include_correction=True):
    centers, placed = S.centers_and_placement(context.target)
    i_sites = S.bank_sites(context.target, centers, 1, S.I_PAIRS)
    l_sites = S.bank_sites(context.target, centers, 2, S.L_PAIRS)
    owner, slot = context.owners_slots[row_index]
    ancilla = S.ancilla_site(centers[owner], slot, stage)
    primitives = [S.Primitive("H", (ancilla,))] if include_character else []
    macros = []
    q = context.target.qubits
    for qubit in B.supported_qubits(measured) if include_character else ():
        if stage == "pump":
            sites = placed["sites_by_qubit"] if qubit < q else i_sites
        else:
            sites = i_sites if qubit < q else l_sites
        local_qubit = qubit if qubit < q else qubit - q
        target = sites[local_qubit]
        cell, _local = S.local_nine_index(context.target, local_qubit)
        path = S.route_path(
            ancilla, centers[owner], target,
            centers[context.target.cells[cell]], stage,
        )
        macro = S.returned_macro(
            stage, "literal_shear_character", owner, slot, ancilla, target,
            path, B.letter_at(measured, qubit),
        )
        macros.append(macro)
        primitives.extend(macro.primitives)
    if include_character:
        primitives.append(S.Primitive("H", (ancilla,)))
    for qubit in B.supported_qubits(correction) if include_correction else ():
        if qubit >= q:
            raise AssertionError("mapped correction left physical O bank")
        target = placed["sites_by_qubit"][qubit]
        cell, _local = S.local_nine_index(context.target, qubit)
        path = S.route_path(
            ancilla, centers[owner], target,
            centers[context.target.cells[cell]], stage,
        )
        macro = S.returned_macro(
            stage, "literal_shear_correction", owner, slot, ancilla, target,
            path, B.letter_at(correction, qubit),
        )
        macros.append(macro)
        primitives.extend(macro.primitives)
    return {
        "stage": stage,
        "owner": owner,
        "slot": slot,
        "colour": tuple(value % 3 for value in owner),
        "primitives": tuple(primitives),
        "macros": tuple(macros),
    }


def routed_cnot_macros(context, stage):
    centers, _placed = S.centers_and_placement(context.target)
    output = []
    for ordinal, (control, target_index) in enumerate(context.cnot_ops):
        owner, control_slot = context.owners_slots[control]
        target_owner, target_slot = context.owners_slots[target_index]
        control_site = S.ancilla_site(centers[owner], control_slot, stage)
        target_site = S.ancilla_site(
            centers[target_owner], target_slot, stage
        )
        path = S.route_path(
            control_site, centers[owner], target_site,
            centers[target_owner], stage,
        )
        macro = S.returned_macro(
            f"{stage}_syndrome_shear", "CNOT", owner, ordinal,
            control_site, target_site, path, "X",
        )
        output.append((macro, ordinal))
    return tuple(output)


def inversion_pairs(context, base_order):
    current_order = tuple(sorted(
        range(len(context.corrections)),
        key=lambda index: (
            tuple(value % 3 for value in context.owners_slots[index][0]),
            context.owners_slots[index][1], index,
        ),
    ))
    base_position = {row: index for index, row in enumerate(base_order)}
    current_position = {row: index for index, row in enumerate(current_order)}
    candidates = set()
    by_qubit = defaultdict(list)
    for index, correction in enumerate(context.corrections):
        for qubit in B.supported_qubits(correction):
            by_qubit[qubit].append(index)
    for rows in by_qubit.values():
        candidates.update(tuple(sorted(pair)) for pair in combinations(rows, 2))
    inversions = tuple(
        pair for pair in sorted(candidates)
        if S.paulis_anticommute(
            context.corrections[pair[0]], context.corrections[pair[1]]
        )
        and (
            (base_position[pair[0]] < base_position[pair[1]])
            != (current_position[pair[0]] < current_position[pair[1]])
        )
    )
    reconstruction_failures = 0
    for pair in candidates:
        left, right = pair
        canonical = (
            B.multiply(context.corrections[left], context.corrections[right])
            if base_position[left] < base_position[right]
            else B.multiply(context.corrections[right], context.corrections[left])
        )
        actual = (
            B.multiply(context.corrections[left], context.corrections[right])
            if current_position[left] < current_position[right]
            else B.multiply(context.corrections[right], context.corrections[left])
        )
        if pair in inversions:
            actual = B.Pauli((actual.phase + 2) % 4, actual.x, actual.z)
        reconstruction_failures += B.fields(actual) != B.fields(canonical)
    return inversions, reconstruction_failures, len(candidates)


def routed_inversion_macros(context, inversions, stage):
    centers, _placed = S.centers_and_placement(context.target)
    output = []
    for left, right in inversions:
        owner, slot = context.owners_slots[left]
        target_owner, target_slot = context.owners_slots[right]
        control = S.ancilla_site(centers[owner], slot, stage)
        target = S.ancilla_site(centers[target_owner], target_slot, stage)
        path = S.route_path(
            control, centers[owner], target, centers[target_owner], stage
        )
        macro = S.returned_macro(
            f"{stage}_inversion_firewall", "CZ", owner, slot,
            control, target, path, "Z",
        )
        output.append((macro, target_owner, target_slot))
    return tuple(output)


def routing_certificate(context, base_order):
    words = []
    for index, (row, correction) in enumerate(zip(
        context.rows, context.corrections
    )):
        words.append(literal_word(
            context, row, correction, index, "pump"
        ))
        words.append(literal_word(
            context, row, correction, index, "bell_measure",
            include_correction=False,
        ))
        words.append(literal_word(
            context, row, correction, index, "bell_correction",
            include_character=False,
        ))
    macros = tuple(macro for word in words for macro in word["macros"])
    conflicts, _microsteps = S.primitive_conflicts(words)
    cnot_macros = (
        routed_cnot_macros(context, "pump")
        + routed_cnot_macros(context, "bell")
    )
    inversions, target_failures, pair_candidates = inversion_pairs(
        context, base_order
    )
    cz_macros = (
        routed_inversion_macros(context, inversions, "pump")
        + routed_inversion_macros(context, inversions, "bell")
    )
    all_aux = tuple(macro for macro, *_rest in cnot_macros + cz_macros)
    aux_return_failures = sum(S.label_return_failures(macro) for macro in all_aux)
    aux_target_failures = sum(S.routed_target_failures(macro) for macro in all_aux)
    aux_deletion_witness = next((
        S.label_return_failures(macro, True) for macro in all_aux
        if any(p.kind == "SWAP" for p in macro.primitives)
    ), 0)
    centers, placed = S.centers_and_placement(context.target)
    i_sites = S.bank_sites(context.target, centers, 1, S.I_PAIRS)
    l_sites = S.bank_sites(context.target, centers, 2, S.L_PAIRS)
    coframe = S.coframe_sites(context.target, centers)
    pump_ancillas = {
        S.ancilla_site(centers[cell], slot, "pump")
        for cell in context.target.cells for slot in range(S.FAMILY_SLOTS)
    }
    bell_ancillas = {
        S.ancilla_site(centers[cell], slot, "bell")
        for cell in context.target.cells for slot in range(S.FAMILY_SLOTS)
    }
    classes = (
        set(placed["sites_by_qubit"]), set(i_sites), set(l_sites),
        set(coframe), pump_ancillas, bell_ancillas,
    )
    palette = set().union(*classes)
    palette_collisions = sum(len(group) for group in classes) - len(palette)
    g_word, _update = U.physical_word(context.target, placed)
    g_touch = {site for instruction in g_word for site in instruction.sites}
    bell_character_g_hits = sum(
        len(set(macro.path[1:-1]) & g_touch)
        for macro in macros
        if macro.stage == "bell_measure" and macro.role == "literal_shear_character"
    )
    return {
        "literal_words": len(words),
        "literal_macros": len(macros),
        "maximum_literal_word_microsteps": max(
            len(word["primitives"]) for word in words
        ),
        "literal_same_block_microstep_collisions": conflicts,
        "literal_NN_failures": sum(
            S.manhattan(left, right) != 1
            for macro in macros
            for left, right in zip(macro.path, macro.path[1:])
        ),
        "literal_return_failures": sum(
            S.label_return_failures(macro) for macro in macros
        ),
        "literal_target_reconstruction_failures": sum(
            S.routed_target_failures(macro) for macro in macros
        ),
        "routed_syndrome_CNOT_macros": len(cnot_macros),
        "active_inversion_pairs": len(inversions),
        "routed_inversion_CZ_macros": len(cz_macros),
        "two_hot_correction_target_failures": target_failures,
        "two_hot_pair_candidates": pair_candidates,
        "auxiliary_route_return_failures": aux_return_failures,
        "auxiliary_route_target_failures": aux_target_failures,
        "auxiliary_route_deletion_label_mismatches": aux_deletion_witness,
        "explicit_M2_per_cell": len(palette) // len(context.target.cells),
        "palette_collisions": palette_collisions,
        "coframe_M2_sites": len(coframe),
        "G_coframe_or_nonO_palette_collisions": len(
            g_touch & (set(coframe) | set(i_sites) | set(l_sites)
                       | pump_ancillas | bell_ancillas)
        ),
        "Bell_character_G_hits": bell_character_g_hits,
    }


def frame_campaign(shape, atlas, run_isometry=False, run_routing=False):
    source = fixture(shape)
    frames = tuple(frame_tuple(frame) for frame in B.V.T.proper_cubic_frames())
    seeds = tuple(product((0, 1), repeat=3))
    base_order = tuple(sorted(
        range(len(B.compile_fixture(source)["tags"])),
        key=lambda index: (
            tuple(value % 3 for value in S.tag_owner_slot(
                source, B.compile_fixture(source)["tags"][index]
            )[0]),
            S.tag_owner_slot(source, B.compile_fixture(source)["tags"][index])[1],
            index,
        ),
    ))
    reports = []
    isometries = []
    routings = []
    seed_row_changes = 0
    seed_shear_changes = 0
    first_by_frame = {}
    for frame_index, frame in enumerate(frames):
        for seed in seeds:
            context = build_context(source, frame, seed, atlas)
            reports.append(context.report)
            key = (
                tuple(B.fields(row) for row in context.rows),
                context.shear_rows,
            )
            if frame_index in first_by_frame:
                seed_row_changes += key[0] != first_by_frame[frame_index][0]
                seed_shear_changes += key[1] != first_by_frame[frame_index][1]
            else:
                first_by_frame[frame_index] = key
            if seed == ZERO and run_isometry:
                aligned_rows = tuple(
                    context.target_compiled["words"][target]["row"]
                    for target in context.alignment
                )
                isometries.append(extraction_isometry_certificate(
                    context.rows, aligned_rows, context.cnot_ops
                ))
            if seed == ZERO and run_routing:
                routings.append(routing_certificate(context, base_order))
    # The zero-shift overlap representatives need no order CZ.  A unit
    # translation changes the numeric mod-3 block order and activates the
    # firewall; route one literal proper-cubic translated context explicitly.
    if run_routing and shape == OVERLAP_BOX:
        shifted = build_context(
            source, frames[0], ZERO, atlas, shift=(1, 0, 0)
        )
        routings.append(routing_certificate(shifted, base_order))
    aggregate = {
        "shape": shape,
        "proper_cubic_frames": len(frames),
        "coframe_origin_sectors": len(seeds),
        "contexts": len(reports),
        "maximum_signed_shear_row_weight": max(
            row["maximum_signed_shear_row_weight"] for row in reports
        ),
        "maximum_repair_weight": max(row["maximum_repair_weight"] for row in reports),
        "maximum_repair_cells": max(row["maximum_repair_cells"] for row in reports),
        "maximum_repair_diameter": max(
            row["maximum_repair_diameter"] for row in reports
        ),
        "maximum_cell_and_edge_local_CNOT_shear_gates": max(
            row["cell_and_edge_local_CNOT_shear_gates"] for row in reports
        ),
        "maximum_CNOT_shear_gates_per_cell": max(
            row["maximum_CNOT_shear_gates_per_cell"] for row in reports
        ),
        "hostile_same_slot_signed_mismatches": sum(
            row["hostile_same_slot_signed_mismatches"] for row in reports
        ),
        "hostile_deleted_target_basis_unsolved_rows": sum(
            row["hostile_deleted_target_basis_unsolved_rows"] for row in reports
        ),
        "seed_signed_row_changes": seed_row_changes,
        "seed_binary_shear_changes": seed_shear_changes,
        "named_failure_sum": sum(
            value
            for row in reports
            for key, value in row.items()
            if key.endswith("failures")
        ),
        "isometry_contexts": len(isometries),
        "isometry_signed_stabilizer_failures": sum(
            row["signed_output_stabilizer_span_failures"] for row in isometries
        ),
        "isometry_logical_failures": sum(
            row["logical_image_mod_output_stabilizer_failures"] for row in isometries
        ),
        "hostile_shear_before_measurement_failures": sum(
            row["hostile_shear_before_measurement_span_failures"] for row in isometries
        ),
        "routing_contexts": len(routings),
        "routing_named_failure_sum": sum(
            value
            for row in routings
            for key, value in row.items()
            if key.endswith("failures") or key.endswith("collisions")
        ),
        "maximum_literal_word_microsteps": max(
            (row["maximum_literal_word_microsteps"] for row in routings),
            default=0,
        ),
        "active_inversion_pairs": sum(
            row["active_inversion_pairs"] for row in routings
        ),
        "routed_inversion_CZ_macros": sum(
            row["routed_inversion_CZ_macros"] for row in routings
        ),
        "routed_syndrome_CNOT_macros": sum(
            row["routed_syndrome_CNOT_macros"] for row in routings
        ),
        "active_auxiliary_route_contexts": sum(
            row["routed_syndrome_CNOT_macros"]
            + row["routed_inversion_CZ_macros"] > 0
            for row in routings
        ),
        "minimum_auxiliary_deletion_mismatches": min(
            (
                row["auxiliary_route_deletion_label_mismatches"]
                for row in routings
                if row["routed_syndrome_CNOT_macros"]
                + row["routed_inversion_CZ_macros"] > 0
            ),
            default=0,
        ),
        "resource_M2_per_cell_values": tuple(sorted(set(
            row["explicit_M2_per_cell"] for row in routings
        ))),
    }
    return aggregate


def product_campaign(atlas):
    source = fixture(TWO_CUBE)
    source_compiled = B.compile_fixture(source)
    source_corrections = tuple(
        P.correction_from_atlas(source, tag, atlas)
        for tag in source_compiled["tags"]
    )
    frames = tuple(np.asarray(frame, dtype=int) for frame in B.V.T.proper_cubic_frames())
    seeds = tuple(product((0, 1), repeat=3))
    row_failures = correction_failures = shear_failures = 0
    route_support_failures = 0
    blocks = 0
    for left in frames:
        for right in frames:
            combined = left @ right
            middle = B.O.arbitrary_fixture(B.Q.affine_cells(
                source.cells, right, ZERO
            ))
            final = B.O.arbitrary_fixture(B.Q.affine_cells(
                source.cells, combined, ZERO
            ))
            final_compiled = B.compile_fixture(final)
            final_rows = tuple(word["row"] for word in final_compiled["words"])
            final_pivots = basis_solver(final_rows, 2 * final.qubits)
            for seed in seeds:
                middle_seed = B.Q.transported_seed(right, ZERO, seed)
                final_seed = B.Q.transported_seed(left, ZERO, middle_seed)
                direct_seed = B.Q.transported_seed(combined, ZERO, seed)
                right_images = V.choi_images(
                    source, middle, right, ZERO, middle_seed
                )
                left_images = V.choi_images(
                    middle, final, left, ZERO, final_seed
                )
                direct_images = V.choi_images(
                    source, final, combined, ZERO, direct_seed
                )
                for word in source_compiled["words"]:
                    source_row = word["row"]
                    middle_row = transport_companion_row(
                        source_row, right_images,
                        source.qubits, middle.qubits,
                    )
                    composed = transport_companion_row(
                        middle_row, left_images,
                        middle.qubits, final.qubits,
                    )
                    direct = transport_companion_row(
                        source_row, direct_images,
                        source.qubits, final.qubits,
                    )
                    row_failures += B.fields(composed) != B.fields(direct)
                    composed_combination = solve_row(
                        composed, final_pivots, 2 * final.qubits
                    )
                    direct_combination = solve_row(
                        direct, final_pivots, 2 * final.qubits
                    )
                    shear_failures += composed_combination != direct_combination
                    composed_cells = P.pauli_cells(final, composed)
                    direct_cells = P.pauli_cells(final, direct)
                    route_support_failures += composed_cells != direct_cells
                for correction in source_corrections:
                    composed = V.transform_row(
                        V.transform_row(correction, right_images), left_images
                    )
                    direct = V.transform_row(correction, direct_images)
                    correction_failures += B.fields(composed) != B.fields(direct)
                    route_support_failures += (
                        P.pauli_cells(final, composed)
                        != P.pauli_cells(final, direct)
                    )
                blocks += 1
    return {
        "ordered_frame_products": len(frames) ** 2,
        "coframe_origin_blocks": blocks,
        "signed_literal_row_product_failures": row_failures,
        "signed_literal_correction_product_failures": correction_failures,
        "actual_generator_shear_product_failures": shear_failures,
        "deterministic_route_support_product_failures": route_support_failures,
    }


def source_hashes():
    root = Path(__file__).resolve().parent
    names = (
        "frontier_companion_bank_bell_character_dilation_2026_07_28.py",
        "frontier_cycle720_companion_local_choi_tree_plaquette_pump_2026_07_27.py",
        "frontier_cycle720_companion_local_choi_pump_covariance_2026_07_27.py",
        "frontier_cycle720_companion_subsystem_m2_update_2026_07_27.py",
        "frontier_cycle789_three_bank_fixed_coframe_schedule_2026_07_30.py",
    )
    return {name: sha256((root / name).read_bytes()).hexdigest() for name in names}


def main():
    atlas = P.build_private_atlases()
    two_cube = frame_campaign(
        TWO_CUBE, atlas, run_isometry=True, run_routing=True
    )
    overlap = frame_campaign(
        OVERLAP_BOX, atlas, run_isometry=False, run_routing=True
    )
    products = product_campaign(atlas)
    checks = []

    def check(label, condition):
        checks.append({"label": label, "pass": bool(condition)})
        print("PASS" if condition else "FAIL", label)

    check(
        "literal signed rows, independent local solves, full-rank shears, transformed private duals and bounded repairs close in all 24x8 contexts",
        two_cube["contexts"] == 192
        and overlap["contexts"] == 192
        and two_cube["named_failure_sum"] == 0
        and overlap["named_failure_sum"] == 0
        and two_cube["maximum_signed_shear_row_weight"] <= 11
        and overlap["maximum_signed_shear_row_weight"] <= 11
        and two_cube["maximum_repair_cells"] <= 2
        and overlap["maximum_repair_cells"] <= 2,
    )
    check(
        "the actual two-cube clean-syndrome extraction isometry equals canonical target extraction followed by the derived bounded cell-and-edge-local CNOT shear in all 24 frames",
        two_cube["isometry_contexts"] == 24
        and two_cube["isometry_signed_stabilizer_failures"] == 0
        and two_cube["isometry_logical_failures"] == 0
        and two_cube["hostile_shear_before_measurement_failures"] > 0,
    )
    check(
        "literal O/I, I/L, O-correction, syndrome-CNOT and active inversion-CZ macros route on the unchanged 64-M2/cell palette",
        two_cube["routing_contexts"] >= 24
        and overlap["routing_contexts"] >= 24
        and two_cube["routing_named_failure_sum"] == 0
        and overlap["routing_named_failure_sum"] == 0
        and two_cube["resource_M2_per_cell_values"] == (64,)
        and overlap["resource_M2_per_cell_values"] == (64,)
        and overlap["routed_inversion_CZ_macros"] > 0
        and two_cube["active_auxiliary_route_contexts"] > 0
        and overlap["active_auxiliary_route_contexts"] > 0
        and min(
            two_cube["minimum_auxiliary_deletion_mismatches"],
            overlap["minimum_auxiliary_deletion_mismatches"],
        ) > 0,
    )
    check(
        "all 576 frame products in every one of eight coframe-origin sectors close on literal signed rows, corrections, actual shear coordinates and route supports",
        products["ordered_frame_products"] == 576
        and products["coframe_origin_blocks"] == 576 * 8
        and all(
            value == 0 for key, value in products.items()
            if key.endswith("failures")
        ),
    )
    check(
        "same-slot and target-basis-deletion shortcuts are actively falsified while coframe-origin changes leave the signed row shear invariant",
        two_cube["hostile_same_slot_signed_mismatches"] > 0
        and overlap["hostile_same_slot_signed_mismatches"] > 0
        and two_cube["hostile_deleted_target_basis_unsolved_rows"] > 0
        and overlap["hostile_deleted_target_basis_unsolved_rows"] > 0
        and two_cube["seed_signed_row_changes"] == 0
        and two_cube["seed_binary_shear_changes"] == 0,
    )

    no_go_gate = {
        "status": "FAIL_negative_claim_prohibited_by_constructive_routes",
        "N1_alternative_routes": (
            "ATTEMPTED literal transported tableau program: closes; "
            "ATTEMPTED canonical target basis plus bounded cell-and-edge-local syndrome CNOT shear: closes; "
            "ATTEMPTED bounded conditional dual-repair words: closes; "
            "ATTEMPTED reduced clean-syndrome isometry quotient: closes; "
            "ATTEMPTED routed inversion-CZ phase firewall: closes on active overlap contexts"
        ),
        "N2_wall_independence": (
            "generator shear, correction centralizer repair and order phase are "
            "not independent walls: the explicit shear+repair+CZ wrapper closes all three; "
            "autonomous program/genesis/enforcement remain separate implementation supplies"
        ),
        "N3_hidden_wall_scan": (
            "coframe origin, frame label, clean syndrome, fixed palette, stage "
            "order, atlas, boundary and G are explicit supplied fields"
        ),
        "N4_residual_matching": (
            "the landed family-multiset comparison attacks census covariance, "
            "not this signed ordered-channel residual; it is not used as a witness"
        ),
        "N5_rhetoric_audit": (
            "only the same-index replacement is falsified, on the tested 2cube "
            "and 3x2x2 contexts; no lattice-wide or route-independent negative is stated"
        ),
        "N6_partial_closure": (
            "literal transported rows or the explicit bounded cell-and-edge-local shear wrapper "
            "retire the generator-basis import without an axiom change"
        ),
        "N7_steelman": (
            "the strongest objection to any no-go is the executable local CNOT "
            "shear plus conditional repair and CZ firewall constructed here"
        ),
        "N8_cross_cycle_echo": (
            "Cycle720 coframe and route-gauge residuals were already retired by "
            "transporting finite coframe data and recompiling returned routes; "
            "the same mechanism succeeds here"
        ),
    }
    report = {
        "status": "PASS" if all(row["pass"] for row in checks) else "FAIL",
        "claim": (
            "conditional actual-generator-shear schedule theorem on 2cube and "
            "3x2x2: literal proper-cubic rows are related to the canonical target "
            "basis by a bounded cell-and-edge-local syndrome shear; a bounded centralizer "
            "repair and inversion-CZ cocycle restore the signed retained dilation"
        ),
        "checks": checks,
        "two_cube": two_cube,
        "overlap_box": overlap,
        "products": products,
        "no_go_discipline": no_go_gate,
        "source_sha256": source_hashes(),
        "derived": (
            "literal signed generator shears, local independent reconstruction, "
            "bounded cell-and-edge-local CNOT synthesis, clean-syndrome stabilizer-isometry equality, "
            "bounded correction-centralizer repair, literal M2 routing, active CZ "
            "order firewall and exact 576x8 products"
        ),
        "supplied": (
            "fixed parity/center and mixed-gauge sector; retained three-bit coframe "
            "origin and frame label; clean pump/Bell syndrome banks; target-basis "
            "atlas, cell chart, boundary, stage/program order and Cycle720 G"
        ),
        "open": (
            "autonomous physical control of the finite coframe-conditioned CNOT/"
            "repair/CZ program; genesis, renewal and local enforcement of the "
            "retained banks/coframe/syndrome code; fault-tolerant gate realization; "
            "law-level time, source/gravity, Record and Born/history bridges"
        ),
        "boundary": (
            "same-index generator replacement is genuinely false but is only a "
            "route-specific shortcut failure. The explicit local shear wrapper "
            "prevents a no-go or axiom-pressure conclusion. Schedule indices are "
            "not physical time and the theorem does not derive autonomous genesis"
        ),
    }
    report["report_sha256"] = sha256(json.dumps(
        report, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()
    print("REPORT_JSON", json.dumps(report, sort_keys=True))
    if report["status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
