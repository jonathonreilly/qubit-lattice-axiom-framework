#!/usr/bin/env python3
"""Reusable parity-even full128/two-cell frame algebra.

This module contains no runner and asserts no audit status.  It isolates the
rank-23 even-CAR basis change and the proper-cubic frame/origin maps used by
the Cycle-820 bounded certificate.  In particular it contains no parity-odd
section, residual character, projective cocycle, literal route, or recurrent
update construction.
"""

from __future__ import annotations

from itertools import product as cartesian_product

import numpy as np

import frontier_companion_bank_bell_character_dilation_2026_07_28 as B
import frontier_cycle720_companion_2cube_m2_stinespring_covariance_2026_07_27 as S720
import frontier_cycle720_companion_checkerboard_frame_cocycle_2026_07_27 as Q720
import frontier_cycle720_companion_fixed_sector_live_input_teleportation_2026_07_27 as L720
import frontier_full128_cycle_encoder_2026_07_24 as F655


Pauli = B.Pauli
Coord = tuple[int, int, int]
SHAPE = (2, 1, 1)
ZERO: Coord = (0, 0, 0)
ORIGIN_SECTORS = tuple(cartesian_product(range(2), repeat=3))


def fields(row: Pauli) -> tuple[int, int, int]:
    return row.phase % 4, row.x, row.z


def multiply(left: Pauli, right: Pauli) -> Pauli:
    return B.multiply(left, right)


def shift(row: Pauli, offset: int) -> Pauli:
    return Pauli(row.phase, row.x << offset, row.z << offset)


def transpose(row: Pauli) -> Pauli:
    return Pauli(
        (row.phase + 2 * (row.x & row.z).bit_count()) % 4,
        row.x,
        row.z,
    )


def pauli_product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = multiply(result, row)
    return result


def signed_pair(
    left: Pauli,
    left_offset: int,
    right: Pauli,
    right_offset: int,
) -> Pauli:
    return multiply(
        shift(left, left_offset),
        shift(transpose(right), right_offset),
    )


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


def span_coordinates(
    target: Pauli,
    rows: tuple[Pauli, ...],
    width: int,
) -> int:
    pivots: dict[int, tuple[int, int]] = {}
    for index, original in enumerate(rows):
        row = original.symplectic(width)
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot][0]
                combination ^= pivots[pivot][1]
            else:
                pivots[pivot] = (row, combination)
                break
    row = target.symplectic(width)
    combination = 0
    while row:
        pivot = row.bit_length() - 1
        if pivot not in pivots:
            raise ValueError("target is outside the declared binary span")
        row ^= pivots[pivot][0]
        combination ^= pivots[pivot][1]
    return combination


def rows_from_mask(rows: tuple[Pauli, ...], mask: int) -> Pauli:
    return pauli_product(
        row for index, row in enumerate(rows) if (mask >> index) & 1
    )


def gf2_inverse(matrix: np.ndarray) -> np.ndarray:
    size = matrix.shape[0]
    augmented = np.concatenate(
        (
            np.asarray(matrix, dtype=np.uint8).copy(),
            np.eye(size, dtype=np.uint8),
        ),
        axis=1,
    )
    for column in range(size):
        candidates = np.flatnonzero(augmented[column:, column])
        if not len(candidates):
            raise AssertionError("singular GF(2) matrix")
        pivot = column + int(candidates[0])
        if pivot != column:
            augmented[[column, pivot]] = augmented[[pivot, column]]
        for row in range(size):
            if row != column and augmented[row, column]:
                augmented[row] ^= augmented[column]
    return augmented[:, size:]


def encoded_x(decoded: int) -> Pauli:
    return Pauli(x=sum(
        int(F655.ENCODER[physical, decoded]) << physical
        for physical in range(F655.PHYSICAL_M2)
    ))


def encoded_z(decoded: int) -> Pauli:
    return Pauli(z=sum(
        int(F655.DECODER[decoded, physical]) << physical
        for physical in range(F655.PHYSICAL_M2)
    ))


def exact_even_mode_tree(fixture):
    """Undo display-only signs and retain the landed signed 23-row tree."""
    displayed, _root = L720.mode_tree(fixture)
    targets = [
        L720.target_z(1 << mode) for mode in range(fixture.matter_qubits)
    ]
    physical = [
        L720.physical_z(fixture, 1 << mode)
        for mode in range(fixture.matter_qubits)
    ]
    tags: list[tuple] = [
        ("Z", mode) for mode in range(fixture.matter_qubits)
    ]
    for left, right, shown_physical, shown_target, kind in displayed:
        if kind == "onsite":
            exact_physical = Pauli(x=(1 << left) | (1 << right))
            exact_target = Pauli(x=(1 << left) | (1 << right))
        else:
            edge = next(
                index for index, record in enumerate(fixture.edges)
                if record[4:6] == (left, right)
                or record[4:6] == (right, left)
            )
            seam_physical = fixture.physical_terms(edge)[2]
            seam_target = fixture.target_terms(edge)[2]
            exact_physical = multiply(
                seam_physical,
                L720.physical_z(fixture, seam_target.z),
            )
            exact_target = multiply(
                seam_target,
                L720.target_z(seam_target.z),
            )
        if (
            exact_physical.x,
            exact_physical.z,
        ) != (shown_physical.x, shown_physical.z):
            raise AssertionError("cleaned physical binary row changed")
        if (
            exact_target.x,
            exact_target.z,
        ) != (shown_target.x, shown_target.z):
            raise AssertionError("cleaned target binary row changed")
        physical.append(exact_physical)
        targets.append(exact_target)
        tags.append((kind, left, right))
    return tuple(physical), tuple(targets), tuple(tags)


def transformed_even_basis_and_duals(fixture, atlas) -> dict[str, object]:
    """Express the exact signed even tree in the landed compiled basis."""
    compiled = B.compile_fixture(fixture)
    old_targets = tuple(compiled["targets"])
    old_physical = tuple(word["physical"] for word in compiled["words"])
    old_graph = tuple(compiled["graph"])
    old_duals = tuple(
        B.P.correction_from_atlas(fixture, tag, atlas)
        for tag in compiled["tags"]
    )
    physical, targets, tags = exact_even_mode_tree(fixture)
    coordinates = tuple(
        span_coordinates(row, old_targets, fixture.matter_qubits)
        for row in targets
    )
    rank = len(targets)
    matrix = np.asarray(tuple(
        tuple((mask >> column) & 1 for column in range(rank))
        for mask in coordinates
    ), dtype=np.uint8)
    inverse_transpose = gf2_inverse(matrix).T
    dual_masks = tuple(sum(
        int(inverse_transpose[row, column]) << column
        for column in range(rank)
    ) for row in range(rank))
    duals = tuple(rows_from_mask(old_duals, mask) for mask in dual_masks)

    signed_graph_failures = 0
    duality_failures = 0
    for new_index, (physical_row, target_row, mask) in enumerate(zip(
        physical,
        targets,
        coordinates,
    )):
        desired = signed_pair(
            physical_row,
            0,
            target_row,
            fixture.qubits,
        )
        signed_graph_failures += (
            fields(rows_from_mask(old_graph, mask)) != fields(desired)
        )
        for dual_index, dual in enumerate(duals):
            duality_failures += B.M.symplectic(
                dual.symplectic(fixture.qubits),
                physical_row.symplectic(fixture.qubits),
                fixture.qubits,
            ) != int(new_index == dual_index)
    return {
        "compiled": compiled,
        "physical": physical,
        "targets": targets,
        "tags": tags,
        "coordinates": coordinates,
        "duals": duals,
        "signed_target_replay_failures": sum(
            fields(rows_from_mask(old_targets, mask)) != fields(row)
            for mask, row in zip(coordinates, targets)
        ),
        "signed_physical_replay_failures": sum(
            fields(rows_from_mask(old_physical, mask)) != fields(row)
            for mask, row in zip(coordinates, physical)
        ),
        "signed_graph_replay_failures": signed_graph_failures,
        "private_dual_syndrome_failures": duality_failures,
    }


def reference_row(row: Pauli) -> Pauli:
    allowed = (1 << F655.LOGICAL_MODES) - 1
    if (row.x | row.z) & ~allowed:
        raise AssertionError("source/reference row touches a vacuum role")
    return Pauli(row.phase, row.x, row.z)


def even_source_tree_indices(tags: tuple[tuple, ...]) -> tuple[int, ...]:
    wanted_edges = {(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (1, 6)}
    indices = list(range(F655.LOGICAL_MODES))
    for index, tag in enumerate(tags):
        if (
            tag[0] in ("onsite", "spatial")
            and tuple(sorted(tag[1:3])) in wanted_edges
        ):
            indices.append(index)
    if len(indices) != 2 * F655.LOGICAL_MODES - 1:
        raise AssertionError("seven-mode source tree is incomplete")
    return tuple(indices)


def as_pauli(row) -> Pauli:
    return Pauli(row.phase % 4, row.x, row.z)


def apply_pauli_images(row: Pauli, images) -> Pauli:
    return as_pauli(S720.apply_images(S720.cpauli(row), images))


def shift_cpauli(row, offset: int):
    return type(row)(row.phase % 4, row.x << offset, row.z << offset)


def frame_key(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(int(value) for value in frame.ravel())


def mode_images(mapping: tuple[int, ...]):
    """Exact exterior/Fock Clifford images for a mode permutation."""
    majoranas = tuple(
        majorana
        for target in mapping
        for majorana in (2 * target, 2 * target + 1)
    )
    return S720.block_majorana_images(len(mapping), 0, 0, majoranas)


def decoded22_images(decoded7_images):
    output = [list(rows) for rows in S720.identity_images(F655.PHYSICAL_M2)]
    for family in range(2):
        for decoded in range(F655.LOGICAL_MODES):
            output[family][decoded] = decoded7_images[family][decoded]
    return tuple(tuple(rows) for rows in output)


def encoder_images():
    return (
        tuple(
            S720.CPauli(
                encoded_x(decoded).phase,
                encoded_x(decoded).x,
                encoded_x(decoded).z,
            )
            for decoded in range(F655.PHYSICAL_M2)
        ),
        tuple(
            S720.CPauli(
                encoded_z(decoded).phase,
                encoded_z(decoded).x,
                encoded_z(decoded).z,
            )
            for decoded in range(F655.PHYSICAL_M2)
        ),
    )


def decoder_images():
    """Return inverse encoder images from raw to decoded coordinates."""
    x_images = tuple(S720.CPauli(x=sum(
        int(F655.DECODER[decoded, raw]) << decoded
        for decoded in range(F655.PHYSICAL_M2)
    )) for raw in range(F655.PHYSICAL_M2))
    z_images = tuple(S720.CPauli(z=sum(
        int(F655.ENCODER[raw, decoded]) << decoded
        for decoded in range(F655.PHYSICAL_M2)
    )) for raw in range(F655.PHYSICAL_M2))
    return x_images, z_images


def direct_sum_images(images, block_width: int):
    return (
        tuple(shift_cpauli(row, 0) for row in images[0])
        + tuple(shift_cpauli(row, block_width) for row in images[0]),
        tuple(shift_cpauli(row, 0) for row in images[1])
        + tuple(shift_cpauli(row, block_width) for row in images[1]),
    )


def fixture_mode_permutation(source, target, frame: np.ndarray) -> tuple[int, ...]:
    target_lookup = {cell: index for index, cell in enumerate(target.cells)}
    direction_map = Q720.direction_permutation(frame)
    output = []
    for cell in source.cells:
        mapped_cell = tuple(int(value) for value in (
            frame @ np.asarray(cell, dtype=int)
        ))
        target_cell = target_lookup[mapped_cell]
        output.extend(
            6 * target_cell + direction_map[mode] for mode in range(6)
        )
    return tuple(output)


def role_action(frame: np.ndarray) -> tuple[int, ...]:
    direction_map = Q720.direction_permutation(frame)
    return direction_map + (6, 7, 8, 9, 10, 11)


def candidate_role_embedding(base, target, frame: np.ndarray) -> tuple[int, ...]:
    """Map abstract local/port/vacuum roles into a rotated sorted fixture."""
    lookup = {cell: index for index, cell in enumerate(target.cells)}
    mapped_cells = tuple(
        tuple(int(value) for value in frame @ np.asarray(cell, dtype=int))
        for cell in base.cells
    )
    local_cell = lookup[mapped_cells[0]]
    neighbour_cell = lookup[mapped_cells[1]]
    direction_map = Q720.direction_permutation(frame)
    return (
        tuple(6 * local_cell + mode for mode in range(6))
        + (6 * neighbour_cell + direction_map[0],)
        + tuple(
            6 * neighbour_cell + direction_map[mode]
            for mode in range(1, 6)
        )
    )


def graph_basis(
    physical: tuple[Pauli, ...],
    target: tuple[Pauli, ...],
    physical_width: int,
) -> tuple[Pauli, ...]:
    return tuple(
        signed_pair(p_row, 0, t_row, physical_width)
        for p_row, t_row in zip(physical, target)
    )


def compare_even_graph_transport(
    base_even: dict[str, object],
    target_images,
    physical_images,
    comparison_basis: tuple[Pauli, ...],
    physical_width: int,
) -> dict[str, int]:
    """Compare all 23 mapped even rows against a signed graph basis."""
    binary_failures = signed_failures = comparisons = 0
    for target_row, physical_row in zip(
        base_even["targets"],
        base_even["physical"],
    ):
        mapped_target = apply_pauli_images(target_row, target_images)
        mapped_physical = apply_pauli_images(physical_row, physical_images)
        actual = signed_pair(
            mapped_physical,
            0,
            mapped_target,
            physical_width,
        )
        comparisons += 1
        try:
            coordinate = span_coordinates(
                actual,
                comparison_basis,
                2 * physical_width - 6,
            )
        except ValueError:
            binary_failures += 1
            continue
        replay = rows_from_mask(comparison_basis, coordinate)
        signed_failures += fields(replay) != fields(actual)
    return {
        "comparisons": comparisons,
        "binary_failures": binary_failures,
        "signed_failures": signed_failures,
    }


def corrected_action(source, target, frame: np.ndarray, target_seed: Coord):
    solution = Q720.seeded_sheet_solution(
        frame,
        Q720.predicted_sheet_solution(frame),
        target_seed,
    )
    return Q720.corrected_images(
        source,
        target,
        frame,
        ZERO,
        solution,
    )


def compact_source_choi(
    base_even: dict[str, object],
    tree_indices: tuple[int, ...],
) -> tuple[Pauli, ...]:
    rows = tuple(
        reference_row(base_even["targets"][index])
        for index in tree_indices
    )
    return tuple(signed_pair(row, 0, row, F655.LOGICAL_MODES) for row in rows)


def source_choi_failures(
    rows: tuple[Pauli, ...],
    images,
) -> tuple[int, int, int]:
    binary = signed = comparisons = 0
    for row in rows:
        comparisons += 1
        mapped = apply_pauli_images(row, images)
        try:
            coordinate = span_coordinates(
                mapped,
                rows,
                2 * F655.LOGICAL_MODES,
            )
        except ValueError:
            binary += 1
            continue
        replay = rows_from_mask(rows, coordinate)
        signed += fields(replay) != fields(mapped)
    return comparisons, binary, signed
