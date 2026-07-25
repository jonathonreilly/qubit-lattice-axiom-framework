#!/usr/bin/env python3
"""Direct commuting-port extractor on two overlapping maximal cubic stars.

The declared logical domain is the complete total-n<=2 sector of twelve
six-mode cells: two neighboring centers and the union of their maximal stars.
The two star edge lists share one physical seam, which is represented once.

The route does not read Cycle-311 branch labels during its physical extractor.
For every physical branch product it derives an inactive/left/right edge datum
from the final computational occupations of the existing collision-safe port
M2.  Five work M2 store the sparse value 0..22, control a bounded code-space
completion, and are uncomputed.  Compiler factors are not called time.
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

import physical_cycle269_common_m64_fixed_seam_cycle311_2026_07_18 as c311
import physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18 as c315
import physical_cycle269_seven_cell_maximal_star_cycle330_2026_07_18 as c330


START = time.perf_counter()
TOL = 5.0e-10
PASS = 0
FAIL = 0

Coord = tuple[int, int, int]
Frame = tuple[Coord, Coord, Coord]

DIRECTIONS: tuple[Coord, ...] = tuple(
    tuple(int(value) for value in row) for row in c311.c210.DIRECTIONS
)
OPPOSITE = (1, 0, 3, 2, 5, 4)
SOURCE_AXIS = 0
WORK_M2 = 5
WORK_STATES = 1 << WORK_M2


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def add(left: Coord, right: Coord) -> Coord:
    return tuple(a + b for a, b in zip(left, right))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(a - b for a, b in zip(left, right))  # type: ignore[return-value]


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


FRAMES: tuple[Frame, ...] = tuple(
    tuple(tuple(int(value) for value in row) for row in frame)  # type: ignore[misc]
    for frame in c330.c235.proper_cubic_frames()
)
FRAME_INDEX = {frame: index for index, frame in enumerate(FRAMES)}


def union_coords(axis: int) -> tuple[Coord, ...]:
    step = DIRECTIONS[2 * axis]
    first, second = (0, 0, 0), step
    rows = [first, second]
    for center, excluded in ((first, second), (second, first)):
        for direction in DIRECTIONS:
            target = add(center, direction)
            if target != excluded and target not in rows:
                rows.append(target)
    if len(rows) != 12:
        raise ValueError("two adjacent maximal stars must contain twelve cells")
    return tuple(rows)


UNION_COORDS = tuple(union_coords(axis) for axis in range(3))


@dataclass(frozen=True)
class Edge:
    first_cell: int
    first_mode: int
    second_cell: int
    second_mode: int

    @property
    def modes(self) -> tuple[int, int]:
        return 6 * self.first_cell + self.first_mode, 6 * self.second_cell + self.second_mode


def union_edges(axis: int) -> tuple[Edge, ...]:
    coords = UNION_COORDS[axis]
    index = {coord: cell for cell, coord in enumerate(coords)}
    result = []
    seen: set[frozenset[Coord]] = set()
    for center in coords[:2]:
        for mode, direction in enumerate(DIRECTIONS):
            neighbor = add(center, direction)
            key = frozenset((center, neighbor))
            if key in seen:
                continue
            seen.add(key)
            result.append(Edge(index[center], mode, index[neighbor], OPPOSITE[mode]))
    if len(result) != 11:
        raise ValueError("the two maximal stars must share exactly one of twelve seams")
    return tuple(result)


EDGES = tuple(union_edges(axis) for axis in range(3))
SOURCE_EDGES = EDGES[SOURCE_AXIS]
SHARED_EDGE_INDEX = next(
    index
    for index, edge in enumerate(SOURCE_EDGES)
    if {edge.first_cell, edge.second_cell} == {0, 1}
)


def induced_edges(axis: int) -> tuple[Edge, ...]:
    coords = UNION_COORDS[axis]
    rows = []
    for first in range(len(coords)):
        for second in range(first + 1, len(coords)):
            delta = sub(coords[second], coords[first])
            if sum(abs(value) for value in delta) != 1:
                continue
            first_mode = DIRECTIONS.index(delta)
            rows.append(Edge(first, first_mode, second, OPPOSITE[first_mode]))
    if len(rows) != 15:
        raise ValueError("the induced two-star cell graph must contain fifteen local adjacencies")
    return tuple(rows)


INCIDENCE_EDGES = tuple(induced_edges(axis) for axis in range(3))
SOURCE_INCIDENCE_EDGES = INCIDENCE_EDGES[SOURCE_AXIS]


LABELS: tuple[tuple[int, ...], ...] = ((),) + tuple((mode,) for mode in range(72)) + tuple(
    combinations(range(72), 2)
)
LABEL_INDEX = {label: index for index, label in enumerate(LABELS)}


def local_spec(label: tuple[int, ...], cell: int) -> tuple[int, tuple[int, ...]]:
    modes = tuple(mode - 6 * cell for mode in label if mode // 6 == cell)
    return len(modes), modes


def body_cells(length: int) -> tuple[Coord, ...]:
    if length < 5:
        raise ValueError("L>=5 is required for a non-aliased two-star union")
    anchor = (2, 2, 2)
    return tuple(add(anchor, coord) for coord in UNION_COORDS[SOURCE_AXIS])


@dataclass(frozen=True)
class LocalTerm:
    representative: object
    r_x_mask: int
    amplitude: complex


def transformed_local_terms(code, cell: int, body: Coord, number: int, label: tuple[int, ...]):
    """Put the Cycle-311 r companion in the X basis.

    Vacuum becomes one exact |+> spectator and therefore does not cause a
    2^12 enumeration.  At total n<=2 only the occupied cells retain explicit
    +/- components.  This is an exact local basis change, not a dropped gauge.
    """
    rows: dict[tuple[int, int, int, int, int], complex] = defaultdict(complex)
    r_qubit = c311.r_qubit(code, body)
    for term in c315.gauge_input_terms(code, body, number, label):
        representative = term.representative
        r_value = (representative.x >> r_qubit) & 1
        stripped = c330.c235.Pauli(
            representative.phase,
            representative.x & ~(1 << r_qubit),
            representative.z,
        )
        for r_x_value in (0, 1):
            coefficient = term.amplitude * ((-1) ** (r_value * r_x_value)) / math.sqrt(2)
            key = (
                stripped.phase,
                stripped.x,
                stripped.z,
                r_x_value << cell,
                number,
            )
            rows[key] += coefficient
    result = tuple(
        LocalTerm(c330.c235.Pauli(phase, x, z), r_mask, amplitude)
        for (phase, x, z, r_mask, _number), amplitude in rows.items()
        if abs(amplitude) > 2.0e-13
    )
    if number == 0 and (len(result) != 1 or result[0].r_x_mask != 0):
        raise ValueError("the vacuum r companion must reduce exactly to one |+> spectator")
    return result


def port_shell(code, body: Coord) -> tuple[set[int], set[int]]:
    body_ports = set(c311.c305.body_vertices(code, body))
    arrival_ports = {
        c311.local.old.outer_partner(code, vertex)[0] for vertex in body_ports
    }
    return body_ports, arrival_ports


def physical_edge_data(code, cells: tuple[Coord, ...], edge: Edge):
    first_body, first_arrival = port_shell(code, cells[edge.first_cell])
    second_body, second_arrival = port_shell(code, cells[edge.second_cell])
    first_vertex = c311.c305.body_vertices(code, cells[edge.first_cell])[edge.first_mode]
    second_vertex = c311.c305.body_vertices(code, cells[edge.second_cell])[edge.second_mode]
    first_partner = c311.local.old.outer_partner(code, first_vertex)[0]
    second_partner = c311.local.old.outer_partner(code, second_vertex)[0]
    if first_partner != second_vertex or second_partner != first_vertex:
        raise ValueError("the two endpoint charts must name the same shared port pair")
    return {
        "first_body": first_body,
        "first_arrival": first_arrival,
        "second_body": second_body,
        "second_arrival": second_arrival,
        "first_vertex": first_vertex,
        "second_vertex": second_vertex,
        "union": first_body | first_arrival | second_body | second_arrival,
    }


def edge_feature_from_ports(code, representative, data) -> int:
    """Return 0=inactive, 1=doubled first endpoint, 2=doubled second.

    Only computational occupations of existing port M2 are read.  On n<=2 an
    active shared-port cancellation leaves exactly two nonshared tags.  Their
    body/arrival shell membership identifies which shared endpoint doubled.
    """
    occupied = {
        vertex
        for vertex in data["union"]
        if (representative.x >> (code.qubits + vertex)) & 1
    }
    first_vertex = data["first_vertex"]
    second_vertex = data["second_vertex"]
    if len(occupied) != 2 or first_vertex in occupied or second_vertex in occupied:
        return 0
    doubled_first = (
        len(occupied & (data["first_arrival"] - {second_vertex})) == 1
        and len(occupied & (data["second_body"] - {second_vertex})) == 1
    )
    doubled_second = (
        len(occupied & (data["first_body"] - {first_vertex})) == 1
        and len(occupied & (data["second_arrival"] - {first_vertex})) == 1
    )
    if doubled_first == doubled_second:
        return 0
    return 1 if doubled_first else 2


def expected_edge_feature(code, left, right, data) -> int:
    first = data["first_vertex"]
    second = data["second_vertex"]
    left_first = (left.x >> (code.qubits + first)) & 1
    left_second = (left.x >> (code.qubits + second)) & 1
    right_first = (right.x >> (code.qubits + first)) & 1
    right_second = (right.x >> (code.qubits + second)) & 1
    if left_first and right_first:
        return 1
    if left_second and right_second:
        return 2
    return 0


def active_local_cells(label: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sorted({mode // 6 for mode in label}))


def whiten_encoding(encoding, gram):
    """Apply exact inverse-square-root repairs only on collided Gram blocks."""
    difference = (gram - sparse.eye(gram.shape[0], format="csc")).tocoo()
    neighbors: dict[int, set[int]] = defaultdict(set)
    for row, column, value in zip(difference.row, difference.col, difference.data):
        if row != column and abs(value) > 2.0e-13:
            neighbors[int(row)].add(int(column))
            neighbors[int(column)].add(int(row))
    unseen = set(neighbors)
    components = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        component = set()
        while stack:
            current = stack.pop()
            if current in component:
                continue
            component.add(current)
            stack.extend(neighbors[current] - component)
        unseen -= component
        components.append(tuple(sorted(component)))

    whitener = sparse.eye(gram.shape[0], format="lil", dtype=complex)
    eigenvalue_rows = []
    for component in components:
        block = gram[np.ix_(component, component)].toarray()
        eigenvalues, eigenvectors = np.linalg.eigh(block)
        inverse_root = (eigenvectors * (eigenvalues ** -0.5)) @ eigenvectors.conj().T
        whitener[np.ix_(component, component)] = inverse_root
        eigenvalue_rows.extend(float(value) for value in eigenvalues)
    whitener = whitener.tocsc()
    repaired = encoding @ whitener
    repaired_gram = repaired.conj().T @ repaired
    return repaired, repaired_gram, {
        "collision_components": len(components),
        "collision_component_sizes": tuple(sorted(len(component) for component in components)),
        "collided_logical_columns": sum(len(component) for component in components),
        "minimum_raw_collision_block_eigenvalue": min(eigenvalue_rows, default=1.0),
        "maximum_raw_collision_block_eigenvalue": max(eigenvalue_rows, default=1.0),
        "whitener_nonzeros": whitener.nnz,
    }


def encoding_for_size(length: int):
    code = c315.c269.build_code(length)
    cells = body_cells(length)
    edge_data = tuple(
        physical_edge_data(code, cells, edge) for edge in SOURCE_INCIDENCE_EDGES
    )
    cache = {
        (cell, number, local_label): transformed_local_terms(
            code, cell, cells[cell], number, local_label
        )
        for cell in range(12)
        for number, local_label in c311.FOCK_LABELS
        if number <= 2
    }
    reducer = c315.RayReducer(code)
    row_lookup: dict[tuple[int, int], int] = {}
    row_feature_sets: dict[int, set[int]] = defaultdict(set)
    port_feature_sets: dict[int, set[int]] = defaultdict(set)
    rows: list[int] = []
    columns: list[int] = []
    values: list[complex] = []
    feature_counts = Counter()
    multiple_active_features = 0
    candidate_formula_mismatches = 0
    commutation_mismatches = 0
    physical_union = 0
    maximum_branch_support = 0

    for column, label in enumerate(LABELS):
        active = active_local_cells(label)
        local_rows = [cache[(cell, *local_spec(label, cell))] for cell in active]
        amplitudes: dict[int, complex] = defaultdict(complex)
        for term_tuple in product(*local_rows) if local_rows else ((),):
            representative = c330.c235.Pauli()
            r_mask = 0
            amplitude = 1 + 0j
            for term in term_tuple:
                representative = representative @ term.representative
                r_mask |= term.r_x_mask
                amplitude *= term.amplitude
                physical_union |= term.representative.x | term.representative.z
            base_row, phase = reducer.reduce(representative)
            key = (base_row, r_mask)
            row = row_lookup.setdefault(key, len(row_lookup))
            candidate_features = tuple(
                edge_feature_from_ports(code, representative, datum)
                for datum in edge_data
            )
            active_candidates = tuple(
                1 + 2 * index + feature - 1
                for index, feature in enumerate(candidate_features)
                if feature
            )
            multiple_active_features += len(active_candidates) > 1
            feature_code = 0
            active_edge = None
            if len(term_tuple) == 2:
                active_edge = next(
                    (
                        index
                        for index, edge in enumerate(SOURCE_INCIDENCE_EDGES)
                        if {edge.first_cell, edge.second_cell} == set(active)
                    ),
                    None,
                )
                if active_edge is not None:
                    edge = SOURCE_INCIDENCE_EDGES[active_edge]
                    by_cell = dict(zip(active, term_tuple))
                    expected = expected_edge_feature(
                        code,
                        by_cell[edge.first_cell].representative,
                        by_cell[edge.second_cell].representative,
                        edge_data[active_edge],
                    )
                    if expected:
                        feature_code = 1 + 2 * active_edge + expected - 1
            candidate_formula_mismatches += (
                tuple(active_candidates) != (() if feature_code == 0 else (feature_code,))
            )
            row_feature_sets[row].add(feature_code)
            port_word = (
                representative.x >> code.qubits
            ) & ((1 << len(code.graph.vertices)) - 1)
            port_feature_sets[port_word].add(feature_code)
            feature_counts[feature_code] += 1
            if len(term_tuple) == 2:
                observed = int(
                    not term_tuple[0].representative.commutes(term_tuple[1].representative)
                )
                derived = int(feature_code != 0)
                commutation_mismatches += observed != derived
            amplitudes[row] += amplitude * phase
            maximum_branch_support = max(
                maximum_branch_support,
                (representative.x | representative.z).bit_count() + r_mask.bit_count(),
            )
        for row, amplitude in amplitudes.items():
            if abs(amplitude) > 2.0e-13:
                rows.append(row)
                columns.append(column)
                values.append(amplitude)
        if (column + 1) % 400 == 0:
            print(f"L{length} direct-port columns {column + 1}/{len(LABELS)}", flush=True)

    encoding = sparse.coo_matrix(
        (values, (rows, columns)),
        shape=(len(row_lookup), len(LABELS)),
        dtype=complex,
    ).tocsc()
    raw_gram = encoding.conj().T @ encoding
    identity = sparse.eye(len(LABELS), format="csc")
    raw_gram_difference = raw_gram - identity
    encoding, gram, whitening = whiten_encoding(encoding, raw_gram)
    gram_difference = gram - identity

    # Every feature selector is a commuting computational-port function.  The
    # XOR extension on five work M2 is involutive, preserves the source row,
    # and returns |00000> after compute/use/uncompute.
    extractor_failures = 0
    for row, features in row_feature_sets.items():
        if len(features) != 1:
            extractor_failures += 1
            continue
        feature = next(iter(features))
        computed = 0 ^ feature
        returned = computed ^ feature
        extractor_failures += not (0 <= feature < WORK_STATES and returned == 0 and row == row)

    return {
        "L": length,
        "split": "train" if length == 5 else "held-no-refit",
        "code": code,
        "cells": cells,
        "edge_data": edge_data,
        "encoding": encoding,
        "gram": gram,
        "raw_gram_residual": c315.largest_singular(raw_gram_difference),
        "raw_gram_raw_maximum": c315.raw_maximum_abs(raw_gram_difference),
        "gram_residual": c315.largest_singular(gram_difference),
        "gram_raw_maximum": c315.raw_maximum_abs(gram_difference),
        "physical_rows": encoding.shape[0],
        "encoding_nonzeros": encoding.nnz,
        "row_feature_conflicts": sum(len(features) > 1 for features in row_feature_sets.values()),
        "port_feature_conflicts": sum(len(features) > 1 for features in port_feature_sets.values()),
        "row_feature_conflict_classes": dict(
            (str(key), value)
            for key, value in Counter(
                tuple(sorted(features))
                for features in row_feature_sets.values()
                if len(features) > 1
            ).items()
        ),
        "port_feature_conflict_classes": dict(
            (str(key), value)
            for key, value in Counter(
                tuple(sorted(features))
                for features in port_feature_sets.values()
                if len(features) > 1
            ).items()
        ),
        "multiple_active_features": multiple_active_features,
        "candidate_formula_mismatches": candidate_formula_mismatches,
        "commutation_mismatches": commutation_mismatches,
        "feature_counts": dict(sorted(feature_counts.items())),
        "extractor_failures": extractor_failures,
        "physical_union": physical_union,
        "maximum_branch_support": maximum_branch_support,
        "cache": cache,
        "whitening": whitening,
    }


def one_particle_coin() -> np.ndarray:
    local_coin = c330.c219.common_species(-0.3).coin
    return np.kron(np.eye(12, dtype=complex), local_coin)


def logical_coin() -> sparse.csc_matrix:
    local_coin = c330.c219.common_species(-0.3).coin
    rows = [0]
    columns = [0]
    values = [1 + 0j]
    for source_mode in range(72):
        source = LABEL_INDEX[(source_mode,)]
        cell, mode = divmod(source_mode, 6)
        for target_mode in range(6):
            rows.append(LABEL_INDEX[(6 * cell + target_mode,)])
            columns.append(source)
            values.append(local_coin[target_mode, mode])
    wedge2 = c311.exterior_matrix(local_coin, 2)
    pair_index = c311.LABEL_INDEX[2]
    for source_pair in combinations(range(72), 2):
        source = LABEL_INDEX[source_pair]
        first_cell, first_mode = divmod(source_pair[0], 6)
        second_cell, second_mode = divmod(source_pair[1], 6)
        if first_cell == second_cell:
            source_local = pair_index[(first_mode, second_mode)]
            for target_local, local_label in enumerate(c311.LABELS[2]):
                rows.append(LABEL_INDEX[(6 * first_cell + local_label[0], 6 * first_cell + local_label[1])])
                columns.append(source)
                values.append(wedge2[target_local, source_local])
        else:
            for first_target in range(6):
                for second_target in range(6):
                    rows.append(
                        LABEL_INDEX[(6 * first_cell + first_target, 6 * second_cell + second_target)]
                    )
                    columns.append(source)
                    values.append(
                        local_coin[first_target, first_mode]
                        * local_coin[second_target, second_mode]
                    )
    matrix = sparse.coo_matrix(
        (values, (rows, columns)), shape=(len(LABELS), len(LABELS)), dtype=complex
    ).tocsc()
    matrix.eliminate_zeros()
    return matrix


def mode_permutation(mapping: tuple[int, ...]) -> sparse.csc_matrix:
    target_rows = []
    phases = []
    for label in LABELS:
        mapped = tuple(mapping[mode] for mode in label)
        phases.append(c311.c308.permutation_sign(mapped))
        target_rows.append(LABEL_INDEX[tuple(sorted(mapped))])
    return sparse.coo_matrix(
        (phases, (target_rows, np.arange(len(LABELS)))),
        shape=(len(LABELS), len(LABELS)),
        dtype=complex,
    ).tocsc()


def edge_stream(edge: Edge) -> sparse.csc_matrix:
    first, second = edge.modes
    mapping = list(range(72))
    mapping[first], mapping[second] = mapping[second], mapping[first]
    return mode_permutation(tuple(mapping))


def stream_product(edges: tuple[Edge, ...]) -> sparse.csc_matrix:
    value = sparse.eye(len(LABELS), format="csc", dtype=complex)
    for edge in edges:
        value = edge_stream(edge) @ value
    return value


def logical_contact() -> sparse.csc_matrix:
    phases = []
    for label in LABELS:
        counts = Counter(mode // 6 for mode in label)
        pairs = sum(number * (number - 1) // 2 for number in counts.values())
        phases.append(np.exp(1j * c330.c230.COUPLING * pairs))
    return sparse.diags(phases, format="csc", dtype=complex)


def physical_factor_residual(encoding, gram, operator) -> float:
    identity = sparse.eye(len(LABELS), format="csc", dtype=complex)
    error = encoding @ ((operator - identity) @ (gram - identity))
    return c315.largest_singular(error)


def ambient_inverse_residuals(encoding, operator) -> tuple[float, ...]:
    def apply(vector, logical):
        coefficients = encoding.conj().T @ vector
        return vector + encoding @ (logical @ coefficients - coefficients)

    rng = np.random.default_rng(659)
    rows = []
    for _ in range(2):
        vector = rng.normal(size=encoding.shape[0]) + 1j * rng.normal(size=encoding.shape[0])
        vector /= np.linalg.norm(vector)
        rows.append(float(np.linalg.norm(apply(apply(vector, operator), operator.conj().T) - vector)))
    return tuple(rows)


def update_controls(fixture):
    coin = logical_coin()
    streams = tuple(edge_stream(edge) for edge in SOURCE_EDGES)
    seam = stream_product(SOURCE_EDGES)
    contact = logical_contact()
    update = contact @ seam @ coin
    identity = sparse.eye(len(LABELS), format="csc", dtype=complex)
    factor_residuals = {
        "free_coin": physical_factor_residual(fixture["encoding"], fixture["gram"], coin),
        "eleven_seam_FSWAP": physical_factor_residual(fixture["encoding"], fixture["gram"], seam),
        "local_contact": physical_factor_residual(fixture["encoding"], fixture["gram"], contact),
        "composition": physical_factor_residual(fixture["encoding"], fixture["gram"], update),
    }
    pair_commutators = tuple(
        c315.largest_singular(streams[left] @ streams[right] - streams[right] @ streams[left])
        for left in range(len(streams))
        for right in range(left + 1, len(streams))
    )
    duplicated = seam @ streams[SHARED_EDGE_INDEX]
    shared_deletion_residual = c315.largest_singular(duplicated - seam)

    one_indices = [LABEL_INDEX[(mode,)] for mode in range(72)]
    one_particle = update[np.ix_(one_indices, one_indices)]
    uniform = np.ones(72, dtype=complex) / math.sqrt(72)
    eigenvalue = np.vdot(uniform, one_particle @ uniform)
    mass = float(np.angle(eigenvalue)) / c330.c219.C_SQUARED
    mass_fixture = c330.c219.rest_mass(c330.c219.common_species(-0.3))

    rows = {
        "coin_unitarity": c315.largest_singular(coin.conj().T @ coin - identity),
        "seam_unitarity": c315.largest_singular(seam.conj().T @ seam - identity),
        "contact_unitarity": c315.largest_singular(contact.conj().T @ contact - identity),
        "update_unitarity": c315.largest_singular(update.conj().T @ update - identity),
        "pairwise_seam_commutators": len(pair_commutators),
        "maximum_seam_commutator": max(pair_commutators),
        "factor_intertwiner_residuals": factor_residuals,
        "ambient_inverse_residuals": ambient_inverse_residuals(fixture["encoding"], update),
        "shared_seam_declared_by_stars": 2,
        "unique_physical_seams": len(SOURCE_EDGES),
        "duplicate_shared_seam_residual": shared_deletion_residual,
        "contact_nontrivial_columns": int(np.count_nonzero(abs(contact.diagonal() - 1) > 2.0e-13)),
        "one_particle_mass": mass,
        "Cycle219_mass_fixture": mass_fixture,
        "one_particle_eigen_residual": float(np.linalg.norm(one_particle @ uniform - eigenvalue * uniform)),
        "update": update,
        "coin": coin,
        "contact": contact,
    }
    return rows


def frame_action(source_axis: int, frame: Frame):
    source_coords = UNION_COORDS[source_axis]
    source_step = DIRECTIONS[2 * source_axis]
    mapped_step = matvec(frame, source_step)
    target_axis = next(axis for axis in range(3) if mapped_step[axis])
    reverse = mapped_step[target_axis] == -1
    origin = mapped_step if reverse else (0, 0, 0)
    target_coords = UNION_COORDS[target_axis]
    target_index = {coord: index for index, coord in enumerate(target_coords)}
    cell_map = tuple(target_index[sub(matvec(frame, coord), origin)] for coord in source_coords)
    direction_map = tuple(DIRECTIONS.index(matvec(frame, direction)) for direction in DIRECTIONS)
    mode_map = tuple(
        6 * cell_map[cell] + direction_map[mode]
        for cell in range(12)
        for mode in range(6)
    )
    return target_axis, reverse, cell_map, direction_map, mode_map


def edge_transport(
    source_axis: int,
    target_axis: int,
    mode_map: tuple[int, ...],
    families=INCIDENCE_EDGES,
):
    target_lookup = {
        frozenset(edge.modes): (index, edge.modes)
        for index, edge in enumerate(families[target_axis])
    }
    rows = []
    for edge in families[source_axis]:
        mapped = (mode_map[edge.modes[0]], mode_map[edge.modes[1]])
        target_index, target_modes = target_lookup[frozenset(mapped)]
        reversed_endpoints = mapped == target_modes[::-1]
        rows.append((target_index, reversed_endpoints))
    return tuple(rows)


def covariance_controls(update_rows):
    coin = update_rows["coin"]
    contact = update_rows["contact"]
    source_update = update_rows["update"]
    identity = sparse.eye(len(LABELS), format="csc", dtype=complex)
    frame_rows = []
    feature_transport_failures = 0
    actions = {}
    for frame in FRAMES:
        target_axis, reverse, cell_map, direction_map, mode_map = frame_action(SOURCE_AXIS, frame)
        representation = mode_permutation(mode_map)
        target_update = contact @ stream_product(EDGES[target_axis]) @ coin
        covariance = representation @ source_update - target_update @ representation
        transport = edge_transport(SOURCE_AXIS, target_axis, mode_map)
        feature_transport_failures += len({row[0] for row in transport}) != 15
        for _edge, swapped in transport:
            for feature in (0, 1, 2):
                twice = 0 if feature == 0 else 3 - (3 - feature if swapped else feature) if swapped else feature
                feature_transport_failures += twice != feature
        actions[(SOURCE_AXIS, frame)] = (target_axis, mode_map, transport)
        frame_rows.append(
            {
                "target_axis": target_axis,
                "endpoint_pair_reversed": reverse,
                "representation_unitarity": c315.largest_singular(
                    representation.conj().T @ representation - identity
                ),
                "update_covariance": c315.largest_singular(covariance),
                "update_covariance_raw": c315.raw_maximum_abs(covariance),
            }
        )

    group_failures = 0
    feature_group_failures = 0
    for left in FRAMES:
        for right in FRAMES:
            mid_axis, _rev_r, _cm_r, _dm_r, right_map = frame_action(SOURCE_AXIS, right)
            target_axis, _rev_l, _cm_l, _dm_l, left_map = frame_action(mid_axis, left)
            product_axis, _rev_p, _cm_p, _dm_p, product_map = frame_action(
                SOURCE_AXIS, matmul(left, right)
            )
            composed_map = tuple(left_map[right_map[mode]] for mode in range(72))
            group_failures += target_axis != product_axis or composed_map != product_map
            right_transport = edge_transport(SOURCE_AXIS, mid_axis, right_map)
            left_transport = edge_transport(mid_axis, target_axis, left_map)
            direct_transport = edge_transport(SOURCE_AXIS, product_axis, product_map)
            for edge, (mid_edge, right_swap) in enumerate(right_transport):
                target_edge, left_swap = left_transport[mid_edge]
                direct_edge, direct_swap = direct_transport[edge]
                feature_group_failures += target_edge != direct_edge or (right_swap ^ left_swap) != direct_swap
    return {
        "proper_cubic_frames": len(FRAMES),
        "endpoint_preserving_frames": sum(not row["endpoint_pair_reversed"] for row in frame_rows),
        "endpoint_reversing_frames": sum(row["endpoint_pair_reversed"] for row in frame_rows),
        "maximum_representation_unitarity": max(row["representation_unitarity"] for row in frame_rows),
        "maximum_update_covariance": max(row["update_covariance"] for row in frame_rows),
        "maximum_update_covariance_raw": max(row["update_covariance_raw"] for row in frame_rows),
        "frame_products": len(FRAMES) ** 2,
        "frame_group_failures": group_failures,
        "feature_transport_failures": feature_transport_failures,
        "feature_group_failures": feature_group_failures,
    }


def direct_port_controls(fixture):
    code = fixture["code"]
    cells = fixture["cells"]
    total_cases = formula_errors = one_hot_errors = 0
    deletion_ambiguities = []
    edge_rows = []
    compute_uncompute_failures = 0
    for edge_index, (edge, data) in enumerate(
        zip(SOURCE_INCIDENCE_EDGES, fixture["edge_data"])
    ):
        first_cache = fixture["cache"]
        outcomes: dict[int, set[int]] = defaultdict(set)
        port_vertices = tuple(sorted(data["union"]))
        feature_counts = Counter()
        for left_number, left_label in c311.FOCK_LABELS:
            for right_number, right_label in c311.FOCK_LABELS:
                if left_number + right_number > 2:
                    continue
                left_terms = first_cache[(edge.first_cell, left_number, left_label)]
                right_terms = first_cache[(edge.second_cell, right_number, right_label)]
                for left, right in product(left_terms, right_terms):
                    representative = left.representative @ right.representative
                    expected = expected_edge_feature(code, left.representative, right.representative, data)
                    derived = edge_feature_from_ports(code, representative, data)
                    formula_errors += derived != expected
                    feature_counts[derived] += 1
                    signature = sum(
                        ((representative.x >> (code.qubits + vertex)) & 1) << index
                        for index, vertex in enumerate(port_vertices)
                    )
                    outcomes[signature].add(derived)
                    total_cases += 1
                    for term, body in ((left, cells[edge.first_cell]), (right, cells[edge.second_cell])):
                        body_ports, arrival_ports = port_shell(code, body)
                        for mode, vertex in enumerate(c311.c305.body_vertices(code, body)):
                            arrival = c311.local.old.outer_partner(code, vertex)[0]
                            bits = (
                                (term.representative.x >> (code.qubits + vertex)) & 1,
                                (term.representative.x >> (code.qubits + arrival)) & 1,
                            )
                            one_hot_errors += bits == (1, 1)
        edge_deletions = []
        for deleted in range(len(port_vertices)):
            reduced: dict[int, set[int]] = defaultdict(set)
            lower_mask = (1 << deleted) - 1
            for signature, features in outcomes.items():
                compact = (signature & lower_mask) | ((signature >> 1) & ~lower_mask)
                reduced[compact].update(features)
            edge_deletions.append(sum(len(features) > 1 for features in reduced.values()))
        endpoint_only: dict[int, set[int]] = defaultdict(set)
        first_position = port_vertices.index(data["first_vertex"])
        second_position = port_vertices.index(data["second_vertex"])
        for signature, features in outcomes.items():
            narrow = ((signature >> first_position) & 1) | (
                ((signature >> second_position) & 1) << 1
            )
            endpoint_only[narrow].update(features)
        endpoint_only_ambiguities = sum(
            len(features) > 1 for features in endpoint_only.values()
        )
        for signature, features in outcomes.items():
            if len(features) != 1:
                compute_uncompute_failures += 1
                continue
            feature = next(iter(features))
            computed = feature
            returned = computed ^ feature
            compute_uncompute_failures += returned != 0 or signature != signature
        deletion_ambiguities.extend(edge_deletions)
        edge_rows.append(
            {
                "edge": edge_index,
                "port_shell_M2": len(port_vertices),
                "term_pair_cases": sum(feature_counts.values()),
                "feature_counts": dict(feature_counts),
                "reachable_port_words": len(outcomes),
                "port_word_ambiguities": sum(len(features) > 1 for features in outcomes.values()),
                "two_shared_port_only_ambiguities": endpoint_only_ambiguities,
                "minimum_one_port_deletion_ambiguities": min(edge_deletions),
                "maximum_one_port_deletion_ambiguities": max(edge_deletions),
            }
        )
    return {
        "total_edge_term_pair_cases": total_cases,
        "formula_errors": formula_errors,
        "compute_uncompute_failures": compute_uncompute_failures,
        "single_cell_body_arrival_double_occupancies": one_hot_errors,
        "edge_rows": edge_rows,
        "minimum_one_port_deletion_ambiguities": min(deletion_ambiguities),
        "maximum_one_port_deletion_ambiguities": max(deletion_ambiguities),
        "minimum_two_shared_port_only_ambiguities": min(
            edge["two_shared_port_only_ambiguities"] for edge in edge_rows
        ),
    }


def deletion_and_domain_controls(fixture, update_rows, direct_rows):
    identity = sparse.eye(len(LABELS), format="csc", dtype=complex)
    coin = update_rows["coin"].tolil(copy=True)
    candidates = []
    for column in range(coin.shape[1]):
        rows = coin[:, column].nonzero()[0]
        candidates.extend((abs(coin[row, column]), int(row), column) for row in rows if row != column)
    _magnitude, row, column = max(candidates)
    deleted_coin_value = coin[row, column]
    coin[row, column] = 0
    coin = coin.tocsc()
    deleted_coin_unitarity = c315.largest_singular(coin.conj().T @ coin - identity)
    deleted_contact = c315.largest_singular(update_rows["contact"] - identity)
    unlawful = 0
    for operation in (
        lambda: LABEL_INDEX[(0, 1, 2)],
        lambda: body_cells(4),
        lambda: c311.common_branches(fixture["code"], fixture["cells"][0], 2, (0, 0), 0),
    ):
        try:
            operation()
        except (KeyError, ValueError):
            unlawful += 1
    return {
        "deleted_coin_coefficient": complex(deleted_coin_value),
        "deleted_coin_unitarity": deleted_coin_unitarity,
        "deleted_contact_residual": deleted_contact,
        "duplicate_shared_seam_residual": update_rows["duplicate_shared_seam_residual"],
        "two_shared_port_only_ambiguities": direct_rows[
            "minimum_two_shared_port_only_ambiguities"
        ],
        "deleted_Gram_whitener_residual": fixture["raw_gram_residual"],
        "work_register_without_zero_constraint_rank_surplus": WORK_STATES - 1,
        "lawful_domain_rejections": unlawful,
    }


def support_inventory(fixture):
    code = fixture["code"]
    union = fixture["physical_union"]
    vertices = len(code.graph.vertices)
    cells = code.length**3
    face_mask = (1 << code.qubits) - 1
    port_mask = ((1 << vertices) - 1) << code.qubits
    flag_mask = ((1 << cells) - 1) << (code.qubits + vertices)
    # r was changed to its X basis and recorded in a symbolic twelve-bit mask.
    return {
        "face_M2_union": (union & face_mask).bit_count(),
        "port_M2_union": (union & port_mask).bit_count(),
        "cell_flag_M2_union": (union & flag_mask).bit_count(),
        "cell_r_M2": 12,
        "extractor_work_M2": WORK_M2,
        "total_selected_M2_upper_bound": union.bit_count() + 12 + WORK_M2,
        "maximum_branch_support_including_r": fixture["maximum_branch_support"],
        "coarse_cells": 12,
        "physical_seams": 11,
        "incidence_adjacencies": 15,
        "constant_overhead_M2_per_coarse_cell_upper_bound": math.ceil(
            (union.bit_count() + 12 + WORK_M2) / 12
        ),
    }


def main() -> None:
    check(
        "the geometry is exactly two overlapping maximal stars with one shared seam",
        len(UNION_COORDS[SOURCE_AXIS]) == 12
        and len(SOURCE_EDGES) == 11
        and sum(
            {edge.first_cell, edge.second_cell} == {0, 1} for edge in SOURCE_EDGES
        )
        == 1,
        {
            "coarse_cells": len(UNION_COORDS[SOURCE_AXIS]),
            "star_seam_declarations": 12,
            "unique_physical_seams": len(SOURCE_EDGES),
            "shared_seam_index": SHARED_EDGE_INDEX,
        },
    )

    fixtures = {length: encoding_for_size(length) for length in (5, 6)}
    fixture_rows = {
        length: {
            key: value
            for key, value in fixture.items()
            if key
            not in {
                "code",
                "cells",
                "edge_data",
                "encoding",
                "gram",
                "cache",
                "physical_union",
            }
        }
        for length, fixture in fixtures.items()
    }
    check(
        "the raw two-star Gram defect is stable and a bounded 24-block whitener gives a 2629-column isometry at L5 and held L6",
        len(LABELS) == 1 + 72 + math.comb(72, 2)
        and all(
            fixture["raw_gram_residual"] > 0.0024
            and
            fixture["gram_residual"] < TOL
            and fixture["gram_raw_maximum"] < 2.0e-12
            and fixture["commutation_mismatches"] == 0
            and fixture["whitening"]["collision_components"] == 24
            and fixture["whitening"]["collision_component_sizes"] == (2,) * 24
            for fixture in fixtures.values()
        ),
        fixture_rows,
    )

    direct_rows = {length: direct_port_controls(fixture) for length, fixture in fixtures.items()}
    comparable = lambda row: {key: value for key, value in row.items() if key != "edge_rows"}
    check(
        "the inactive/left/right datum is coherently derivable from commuting existing port occupations without marginal X/Z copying",
        all(
            row["formula_errors"] == 0
            and row["compute_uncompute_failures"] == 0
            and row["single_cell_body_arrival_double_occupancies"] == 0
            and all(
                edge["port_word_ambiguities"] == 0
                and edge["port_shell_M2"] <= 22
                and edge["two_shared_port_only_ambiguities"] > 0
                for edge in row["edge_rows"]
            )
            for row in direct_rows.values()
        )
        and comparable(direct_rows[5]) == comparable(direct_rows[6]),
        direct_rows,
    )

    check(
        "the full two-star direct selector retains exactly sixteen physical-port conflict signatures instead of hiding them as a qutrit oracle",
        all(
            fixture["row_feature_conflicts"] == 16
            and fixture["port_feature_conflicts"] == 16
            and fixture["extractor_failures"] == 16
            and fixture["candidate_formula_mismatches"] > 0
            and fixture["multiple_active_features"] > 0
            for fixture in fixtures.values()
        ),
        {
            length: {
                "physical_rows": fixture["physical_rows"],
                "row_feature_conflicts": fixture["row_feature_conflicts"],
                "port_feature_conflicts": fixture["port_feature_conflicts"],
                "row_feature_conflict_classes": fixture[
                    "row_feature_conflict_classes"
                ],
                "candidate_formula_mismatches": fixture[
                    "candidate_formula_mismatches"
                ],
                "multiple_active_candidates": fixture["multiple_active_features"],
            }
            for length, fixture in fixtures.items()
        },
    )

    update_rows = update_controls(fixtures[5])
    check(
        "the collision-whitened code executes one bounded free-plus-eleven-seam-plus-contact physical intertwiner",
        max(
            update_rows["coin_unitarity"],
            update_rows["seam_unitarity"],
            update_rows["contact_unitarity"],
            update_rows["update_unitarity"],
            update_rows["maximum_seam_commutator"],
            max(update_rows["factor_intertwiner_residuals"].values()),
            max(update_rows["ambient_inverse_residuals"]),
        )
        < TOL
        and update_rows["pairwise_seam_commutators"] == math.comb(11, 2)
        and update_rows["unique_physical_seams"] == 11
        and update_rows["contact_nontrivial_columns"] == 12 * math.comb(6, 2)
        and fixtures[5]["gram_residual"] < TOL,
        {key: value for key, value in update_rows.items() if key not in {"update", "coin", "contact"}},
    )

    check(
        "the one-particle mass fixture is unchanged by the two-star update",
        abs(update_rows["one_particle_mass"] - update_rows["Cycle219_mass_fixture"]) < 3.0e-13
        and update_rows["one_particle_eigen_residual"] < 2.0e-12,
        {
            "one_particle_modes": 72,
            "mass": update_rows["one_particle_mass"],
            "fixture": update_rows["Cycle219_mass_fixture"],
            "eigen_residual": update_rows["one_particle_eigen_residual"],
        },
    )

    covariance = covariance_controls(update_rows)
    check(
        "the two-star update and sparse edge datum close all 24 proper-cubic frames and 576 products",
        covariance["proper_cubic_frames"] == 24
        and covariance["endpoint_preserving_frames"] == 12
        and covariance["endpoint_reversing_frames"] == 12
        and covariance["maximum_representation_unitarity"] < TOL
        and covariance["maximum_update_covariance"] < TOL
        and covariance["maximum_update_covariance_raw"] < 2.0e-12
        and covariance["frame_products"] == 576
        and covariance["frame_group_failures"] == 0
        and covariance["feature_transport_failures"] == 0
        and covariance["feature_group_failures"] == 0,
        covariance,
    )

    support = support_inventory(fixtures[5])
    check(
        "the physical carrier and direct extractor have bounded constant support and overhead",
        support["coarse_cells"] == 12
        and support["physical_seams"] == 11
        and support["incidence_adjacencies"] == 15
        and support["extractor_work_M2"] == 5
        and support["total_selected_M2_upper_bound"] < 600
        and support["constant_overhead_M2_per_coarse_cell_upper_bound"] < 50,
        support,
    )

    deletions = deletion_and_domain_controls(fixtures[5], update_rows, direct_rows[5])
    check(
        "port, work-reset, shared-seam, coin, contact and lawful-domain controls remain active",
        deletions["deleted_coin_unitarity"] > 0.2
        and deletions["deleted_contact_residual"] > 0.3
        and deletions["duplicate_shared_seam_residual"] > 1.0
        and deletions["two_shared_port_only_ambiguities"] > 0
        and deletions["deleted_Gram_whitener_residual"] > 0.002
        and deletions["work_register_without_zero_constraint_rank_surplus"] == 31
        and deletions["lawful_domain_rejections"] == 3,
        deletions,
    )

    certificate = {
        "coords": UNION_COORDS[SOURCE_AXIS],
        "edges": tuple(edge.modes for edge in SOURCE_EDGES),
        "incidence_edges": tuple(edge.modes for edge in SOURCE_INCIDENCE_EDGES),
        "logical_dimension": len(LABELS),
        "work_states": WORK_STATES,
    }
    digest = sha256(
        json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "two-overlapping-maximal-star-direct-port-extractor-partial",
        "terminal": "PER_EDGE_DIRECT_PORT_EXTRACTOR_AND_TWO_STAR_UPDATE_CLOSED_SELECTOR_CONFLICT_RETAINED"
        if FAIL == 0
        else "UNFINISHED_IMPLEMENTATION",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "certificate_sha256": digest,
        "domains": {
            "coarse_cells": 12,
            "six_mode_logical_modes": 72,
            "total_number": "0..2",
            "logical_columns": len(LABELS),
            "proper_cubic_frames": 24,
            "ordered_frame_products": 576,
            "train_L": 5,
            "held_L": 6,
        },
        "resources": {
            **support,
            "work_computational_states": WORK_STATES,
            "lawful_work_states": 31,
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
        "residuals": {
            "sizes": fixture_rows,
            "update": {key: value for key, value in update_rows.items() if key not in {"update", "coin", "contact"}},
            "covariance": covariance,
            "deletions": deletions,
        },
        "supplied": (
            "the landed Cycle-311 fixed-reference cell rays, cell role constraint and collision-safe port M2",
            "two neighboring maximal-star centers, their twelve-cell bounded chart and total n<=2 domain",
            "the Cycle-219 coin, eleven unique FSWAP seams, Cycle-230 coupling and factor order",
            "the exact local r-companion Hadamard basis change and spectator |+> preparation",
            "a five-M2 zero work register, dense bounded code-space matrix-unit completion and off-code identity",
            "a bounded inverse-square-root repair on the twenty-four observed two-column Gram collision blocks",
            "for a qutrit-conditioned full two-star action, one binary branch-resolution datum on each of sixteen collided port signatures",
            "preparation/application of the fixed reference and arbitrary amplitudes in 2629 logical columns",
        ),
        "derived": (
            "one-hot single-cell incidence from body/arrival port occupations on the declared total-n<=2 branch grammar",
            "zero-ambiguity inactive/left/right edge extraction from the final commuting 22-port shell on total n<=2",
            "shared-port cancellation consistency and one deduplicated seam for the two overlapping stars",
            "a collision-whitened 2629-column L5/L6 physical isometry and update",
            "free coin, eleven commuting seam FSWAPs, local contact and their physical code-space intertwiners",
            "all 24 frames, 576 products, one-particle mass, support, deletion and lawful-domain controls",
        ),
        "open": (
            "primitive one-/two-M2 synthesis of the dense bounded extractor projectors and ambient completion",
            "a more economical replacement for the bounded logical Gram whitener",
            "derivation of the sixteen full-two-star selector conflicts from existing commuting M2 without a supplied branch-resolution datum",
            "total number above two, simultaneous multiple active edge data and complete M64^12",
            "three or more recurrent maximal stars, volume collision policy and arbitrary position/reference preparation",
            "number-changing interactions, separated-cell recurrence, state genesis and a full-Hilbert compiler",
            "time, source, gravity, Record, occurrence, Born probability, minimality, impossibility and axiom pressure",
        ),
        "claim_ceiling": (
            "Constructive per-edge commuting-port extractor and separate collision-whitened two-star update on total n<=2.  "
            "The local extractor returns its work register, but sixteen full-union physical/port signatures carry two "
            "different requested edge data, so an end-to-end qutrit-conditioned two-star action still supplies one "
            "branch-resolution datum there.  No broader negative follows."
        ),
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"])
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
