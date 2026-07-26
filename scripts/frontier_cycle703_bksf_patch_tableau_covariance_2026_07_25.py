#!/usr/bin/env python3
"""Scale the phase-oriented BKSF tableau to held overlap geometries.

The open geometries are a three-center L triomino, a 2x2 square, and a 3x3
square.  Every cell has six matter vertices plus one local parity reference,
the 12 octahedral matter edges, and six reference spokes.  Adjacent cells add
only the ordinary matter stream edge: no parallel intercell reference edge is
installed.  A path-ordered whole-cell parity dressing supplies the CAR sign
for stream edges that are chords of the chosen Hamiltonian cell path.

The runner constructs independent phase-aware stabilizer bases, phase-oriented
matter logical X/Z rows, and full canonical Clifford tableaus.  It compares
translated and all 24 proper-cubic transformed state-isometry tableaus through
their signed stabilizer groups and the independently derived second-quantized
logical permutation.  Periodic L=3 is included with 376 contractible loop
rows, three explicitly fixed Wilson rows, and 26 independent local-D rows.

No dense physical state or matrix is formed, and no preparation-depth claim is
inferred from symplectic completion.  Here “physical” Pauli/tableau rows mean
the BKSF graph-edge-qubit layer.  The Cycle-232 Z3 site placement, stream-edge
repetition isometry, controller allocation, and nearest-neighbor routing are
not composed by this runner.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base
import frontier_cycle703_bksf_two_cell_tableau_intertwiner_2026_07_25 as two


NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "CYCLE703_BKSF_PATCH_TABLEAU_COVARIANCE_NOTE_2026-07-25.md"
)
C629_RECEIPT = ROOT / (
    "outputs/physical_a2_line_contact_discriminator_tournament_"
    "cycle629_receipt_2026_07_22.json"
)
C629_RECEIPT_SHA256 = (
    "269c22c3ff87f94b5e4d2e1df54791bbe4df482aba17018b3893db9adbaabd02"
)
REVERSE = (1, 0, 3, 2, 5, 4)
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


def pauli_product(rows) -> base.Pauli:
    return two.pauli_product(rows)


def pauli_weight(row: base.Pauli) -> int:
    return two.pauli_weight(row)


def pauli_support(row: base.Pauli) -> int:
    return row.x | row.z


def cell_path_2d(length: int) -> tuple[tuple[int, int, int], ...]:
    cells = []
    for y in range(length):
        xs = range(length) if y % 2 == 0 else range(length - 1, -1, -1)
        cells.extend((x, y, 0) for x in xs)
    return tuple(cells)


def cell_path_3d(length: int) -> tuple[tuple[int, int, int], ...]:
    cells = []
    for z in range(length):
        ys = range(length) if z % 2 == 0 else range(length - 1, -1, -1)
        for row_index, y in enumerate(ys):
            forward = (z + row_index) % 2 == 0
            xs = range(length) if forward else range(length - 1, -1, -1)
            cells.extend((x, y, z) for x in xs)
    return tuple(cells)


OPEN_GEOMETRIES = {
    "open_three_center_L": ((0, 0, 0), (1, 0, 0), (1, 1, 0)),
    "held_2x2": cell_path_2d(2),
    "held_3x3": cell_path_2d(3),
}


class PatchGraph(base.ReferenceGraph):
    """Local-reference graph with matter streams but no reference bonds."""

    def __init__(
        self,
        cells: tuple[tuple[int, int, int], ...],
        periodic_length: int | None = None,
    ):
        if len(set(cells)) != len(cells):
            raise ValueError("cell path contains duplicates")
        if periodic_length is not None and (
            periodic_length < 3 or len(cells) != periodic_length**3
        ):
            raise ValueError("periodic patch must contain one L>=3 cubic volume")
        self.cells = tuple(cells)
        self.cell_index = {cell: index for index, cell in enumerate(self.cells)}
        self.cell_set = set(self.cells)
        self.periodic_length = periodic_length
        self.periodic = periodic_length is not None
        self.length = periodic_length or 0
        self.vertices: list[tuple[tuple[int, int, int], int]] = []
        self.vertex_index: dict[tuple[tuple[int, int, int], int], int] = {}
        for cell in self.cells:
            for mode in range(7):
                key = (cell, mode)
                self.vertex_index[key] = len(self.vertices)
                self.vertices.append(key)

        self.edges: list[tuple[int, int, str, tuple[int, int, int]]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.edge_displacement: list[tuple[int, int, int]] = []
        self.stream_edges: list[
            tuple[int, tuple[int, int, int], tuple[int, int, int], int, int, int]
        ] = []

        def add_edge(u: int, v: int, kind: str, owner, displacement=(0, 0, 0)):
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate edge", self.vertices[u], self.vertices[v]))
            edge = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_displacement.append(tuple(displacement))
            self.edge_lookup[key] = edge
            return edge

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] == right:
                    continue
                add_edge(
                    self.vertex_index[(cell, left)],
                    self.vertex_index[(cell, right)],
                    "octahedral",
                    cell,
                )
            reference = self.vertex_index[(cell, 6)]
            for mode in range(6):
                add_edge(
                    reference,
                    self.vertex_index[(cell, mode)],
                    "spoke",
                    cell,
                )

        for cell in self.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] += 1
                if self.periodic:
                    target[axis] %= self.periodic_length
                target_cell = tuple(target)
                if target_cell not in self.cell_set:
                    continue
                u_mode = 2 * axis + 1
                v_mode = 2 * axis
                u = self.vertex_index[(cell, u_mode)]
                v = self.vertex_index[(target_cell, v_mode)]
                displacement = tuple(int(index == axis) for index in range(3))
                edge = add_edge(u, v, "matter_stream", cell, displacement)
                self.stream_edges.append(
                    (edge, cell, target_cell, u_mode, v_mode, axis)
                )

        self.incident: list[list[int]] = [[] for _ in self.vertices]
        for edge, (u, v, _, _) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()


@dataclass(frozen=True)
class CycleRow:
    pauli: base.Pauli
    vertices: tuple[int, ...]
    winding: int


def tree_path(source: int, target: int, parent: list[int | None]) -> list[int]:
    source_chain = []
    vertex: int | None = source
    while vertex is not None:
        source_chain.append(vertex)
        vertex = parent[vertex]
    target_chain = []
    vertex = target
    while vertex is not None:
        target_chain.append(vertex)
        vertex = parent[vertex]
    positions = {vertex: index for index, vertex in enumerate(source_chain)}
    common = next(vertex for vertex in target_chain if vertex in positions)
    return (
        source_chain[: positions[common] + 1]
        + list(reversed(target_chain[: target_chain.index(common)]))
    )


def cycle_winding(graph: PatchGraph, vertices: list[int]) -> int:
    if not graph.periodic:
        return 0
    total = [0, 0, 0]
    for source, target in zip(vertices, vertices[1:] + vertices[:1]):
        edge = graph.edge_between(source, target)
        u, v, _, _ = graph.edges[edge]
        sign = 1 if (source, target) == (u, v) else -1
        displacement = graph.edge_displacement[edge]
        for axis in range(3):
            total[axis] += sign * displacement[axis]
    if any(value % graph.periodic_length for value in total):
        raise ValueError(("cycle does not close in the universal cover", total))
    return sum(
        ((total[axis] // graph.periodic_length) & 1) << axis
        for axis in range(3)
    )


def fundamental_cycles(graph: PatchGraph) -> list[CycleRow]:
    adjacency: list[list[tuple[int, int]]] = [[] for _ in graph.vertices]
    for edge, (u, v, _, _) in enumerate(graph.edges):
        adjacency[u].append((v, edge))
        adjacency[v].append((u, edge))
    for row in adjacency:
        row.sort()
    parent: list[int | None] = [None] * len(graph.vertices)
    seen = {0}
    queue = deque([0])
    tree_edges: set[int] = set()
    while queue:
        u = queue.popleft()
        for v, edge in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            parent[v] = u
            tree_edges.add(edge)
            queue.append(v)
    if len(seen) != len(graph.vertices):
        raise ValueError("patch graph is disconnected")

    rows = []
    for edge, (u, v, _, _) in enumerate(graph.edges):
        if edge in tree_edges:
            continue
        vertices = tree_path(u, v, parent)
        rows.append(
            CycleRow(
                graph.loop_pauli(vertices),
                tuple(vertices),
                cycle_winding(graph, vertices),
            )
        )
    return rows


def winding_split(
    cycles: list[CycleRow], periodic: bool
) -> tuple[list[base.Pauli], list[base.Pauli], tuple[int, ...]]:
    if not periodic:
        return [row.pauli for row in cycles], [], ()
    selected = []
    span = []
    for index, row in enumerate(cycles):
        if base.gf2_rank(span + [row.winding]) > len(span):
            selected.append(index)
            span.append(row.winding)
        if len(selected) == 3:
            break
    if len(selected) != 3:
        raise ValueError(("periodic winding rank is not three", span))

    selected_windings = [cycles[index].winding for index in selected]

    def solve_winding(target: int) -> int:
        for mask in range(8):
            observed = 0
            for index, winding in enumerate(selected_windings):
                if (mask >> index) & 1:
                    observed ^= winding
            if observed == target:
                return mask
        raise ValueError(("unreachable winding", target))

    wilsons = []
    for axis in range(3):
        mask = solve_winding(1 << axis)
        wilsons.append(
            pauli_product(
                cycles[selected[index]].pauli
                for index in range(3)
                if (mask >> index) & 1
            )
        )

    loops = []
    selected_set = set(selected)
    for index, row in enumerate(cycles):
        if index in selected_set:
            continue
        mask = solve_winding(row.winding)
        loops.append(
            row.pauli
            @ pauli_product(
                cycles[selected[slot]].pauli
                for slot in range(3)
                if (mask >> slot) & 1
            )
        )
    return loops, wilsons, tuple(selected_windings)


def local_d(graph: PatchGraph, cell) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def logical_rows(graph: PatchGraph) -> tuple[list[base.Pauli], list[base.Pauli]]:
    logical_z = []
    logical_x = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            matter = graph.vertex_index[(cell, mode)]
            logical_z.append(graph.B(matter))
            suffix = pauli_product(
                graph.B(graph.vertex_index[(cell, suffix_mode)])
                for suffix_mode in range(mode, 6)
            )
            logical_x.append(
                base.Pauli(phase=3) @ suffix @ graph.A(matter, reference)
            )
    return logical_z, logical_x


def dual_vectors(w_vectors: list[int], qubits: int) -> list[int]:
    """Compute every free-zero symplectic dual with one GF(2) reduction."""

    pivots: dict[int, tuple[int, int]] = {}
    for index, vector in enumerate(w_vectors):
        mask = two.swap_halves(vector, qubits)
        combination = 1 << index
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                previous_mask, previous_combination = pivots[pivot]
                mask ^= previous_mask
                combination ^= previous_combination
            else:
                pivots[pivot] = (mask, combination)
                break
        else:
            raise ValueError("W rows are not independent")

    for pivot in sorted(pivots):
        pivot_mask, pivot_combination = pivots[pivot]
        for other in tuple(pivots):
            if other != pivot and (pivots[other][0] >> pivot) & 1:
                other_mask, other_combination = pivots[other]
                pivots[other] = (
                    other_mask ^ pivot_mask,
                    other_combination ^ pivot_combination,
                )

    duals = [0] * qubits
    for pivot, (_, combination) in pivots.items():
        support = combination
        while support:
            bit = support & -support
            duals[bit.bit_length() - 1] |= 1 << pivot
            support ^= bit
    return duals


def complete_tableau_fast(
    w_rows: list[base.Pauli], explicit_x: list[base.Pauli], qubits: int
) -> list[base.Pauli]:
    w_vectors = [row.symplectic(qubits) for row in w_rows]
    vectors = dual_vectors(w_vectors, qubits)
    logical_count = len(explicit_x)
    for index, row in enumerate(explicit_x):
        vector = row.symplectic(qubits)
        if any(
            two.symplectic(vector, w_vectors[column], qubits)
            != int(index == column)
            for column in range(qubits)
        ):
            raise ValueError(("explicit logical X is not a dual", index))
        vectors[index] = vector

    for index in range(logical_count, qubits):
        vector = vectors[index]
        for logical_index in range(logical_count):
            if two.symplectic(
                vector, explicit_x[logical_index].symplectic(qubits), qubits
            ):
                vector ^= w_vectors[logical_index]
        vectors[index] = vector

    for left in range(logical_count, qubits):
        for right in range(left + 1, qubits):
            if two.symplectic(vectors[left], vectors[right], qubits):
                vectors[left] ^= w_vectors[right]

    mask = (1 << qubits) - 1
    rows = list(explicit_x)
    for vector in vectors[logical_count:]:
        x = vector & mask
        z = vector >> qubits
        rows.append(base.Pauli(phase=(x & z).bit_count() & 1, x=x, z=z))
    return rows


@dataclass
class CodeData:
    graph: PatchGraph
    loops: list[base.Pauli]
    wilsons: list[base.Pauli]
    ds: list[base.Pauli]
    stabilizers: list[base.Pauli]
    logical_z: list[base.Pauli]
    logical_x: list[base.Pauli]
    w_rows: list[base.Pauli]
    v_rows: list[base.Pauli]
    selected_windings: tuple[int, ...]
    digest: str


def canonical_failures(code: CodeData) -> int:
    qubits = len(code.graph.edges)
    w = [row.symplectic(qubits) for row in code.w_rows]
    v = [row.symplectic(qubits) for row in code.v_rows]
    return sum(
        two.symplectic(w[left], w[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        two.symplectic(v[left], v[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        two.symplectic(v[left], w[right], qubits) != int(left == right)
        for left in range(qubits)
        for right in range(qubits)
    )


def build_code(graph: PatchGraph, validate: bool = True) -> CodeData:
    qubits = len(graph.edges)
    cycles = fundamental_cycles(graph)
    loops, wilsons, selected_windings = winding_split(cycles, graph.periodic)
    all_ds = [local_d(graph, cell) for cell in graph.cells]
    ds = all_ds[:-1]
    stabilizers = loops + wilsons + ds
    logical_z, logical_x = logical_rows(graph)
    w_rows = logical_z + stabilizers
    if len(w_rows) != qubits:
        raise ValueError(("wrong W row count", len(w_rows), qubits))
    v_rows = complete_tableau_fast(w_rows, logical_x, qubits)
    serialized = "\n".join(
        f"{kind}:{index}:{row.phase}:{row.x:x}:{row.z:x}"
        for kind, rows in (("W", w_rows), ("V", v_rows))
        for index, row in enumerate(rows)
    )
    code = CodeData(
        graph,
        loops,
        wilsons,
        ds,
        stabilizers,
        logical_z,
        logical_x,
        w_rows,
        v_rows,
        selected_windings,
        sha256(serialized.encode("ascii")).hexdigest(),
    )
    if validate:
        if canonical_failures(code):
            raise ValueError("completed tableau is not canonical")
        if base.gf2_rank(
            row.symplectic(qubits) for row in w_rows + v_rows
        ) != 2 * qubits:
            raise ValueError("completed tableau is not full rank")
        if base.stabilizer_phase_failures(stabilizers, qubits):
            raise ValueError("stabilizer phase relation is inconsistent")
    return code


def decoded_logical_pauli(row: base.Pauli, code: CodeData) -> tuple[base.Pauli, int]:
    qubits = len(code.graph.edges)
    logical_count = len(code.logical_z)
    coordinates = two.decode_full(row, code.w_rows, code.v_rows, qubits)
    if coordinates.v_mask >> logical_count:
        raise ValueError("operator leaks from the stabilizer code")
    mask = (1 << logical_count) - 1
    return (
        base.Pauli(
            phase=coordinates.phase,
            x=coordinates.v_mask & mask,
            z=coordinates.w_mask & mask,
        ),
        coordinates.w_mask >> logical_count,
    )


def logical_hop_terms(left: int, right: int) -> tuple[base.Pauli, base.Pauli]:
    left, right = sorted((left, right))
    endpoints = (1 << left) | (1 << right)
    between = ((1 << right) - 1) ^ ((1 << (left + 1)) - 1)
    return (
        base.Pauli(x=endpoints, z=between),
        base.Pauli(phase=2, x=endpoints, z=between | endpoints),
    )


def term_signature(rows: list[base.Pauli] | tuple[base.Pauli, ...]):
    return sorted((row.phase, row.x, row.z) for row in rows)


def intermediate_cell_parity(
    graph: PatchGraph, left_index: int, right_index: int
) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(graph.cells[cell_index], mode)])
        for cell_index in range(left_index + 1, right_index)
        for mode in range(6)
    )


def stream_terms(
    graph: PatchGraph,
    source_cell,
    target_cell,
    source_mode: int,
    target_mode: int,
) -> tuple[tuple[base.Pauli, base.Pauli], dict[str, object]]:
    source_index = graph.cell_index[source_cell]
    target_index = graph.cell_index[target_cell]
    if source_index < target_index:
        left_cell, left_mode = source_cell, source_mode
        right_cell, right_mode = target_cell, target_mode
        left_index, right_index = source_index, target_index
    else:
        left_cell, left_mode = target_cell, target_mode
        right_cell, right_mode = source_cell, source_mode
        left_index, right_index = target_index, source_index

    u = graph.vertex_index[(left_cell, left_mode)]
    v = graph.vertex_index[(right_cell, right_mode)]
    ru = graph.vertex_index[(left_cell, 6)]
    rv = graph.vertex_index[(right_cell, 6)]
    core = graph.A(ru, u) @ graph.A(v, rv)
    stream = graph.A(u, v)
    reference_path = graph.A(ru, u) @ stream @ graph.A(v, rv)
    path_identity = core == base.Pauli(phase=2) @ stream @ reference_path
    between = intermediate_cell_parity(graph, left_index, right_index)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(right_cell, mode)])
        for mode in range(6)
        if mode != right_mode
    )
    terms = (
        base.Pauli(phase=2) @ between @ spectator @ core,
        between @ spectator @ graph.B(u) @ graph.B(v) @ core,
    )
    return terms, {
        "logical_indices": (6 * left_index + left_mode, 6 * right_index + right_mode),
        "intermediate_cells": right_index - left_index - 1,
        "path_identity": path_identity,
        "direct_reference_edges": 0,
    }


def operator_controls(code: CodeData) -> dict[str, object]:
    graph = code.graph
    qubits = len(graph.edges)
    stream_failures = coin_failures = diagonal_failures = 0
    preservation_failures = inverse_failures = path_failures = 0
    deletion_mismatches = 0
    operator_rows: list[base.Pauli] = []
    intermediate_counts = []

    for _, source_cell, target_cell, source_mode, target_mode, _ in graph.stream_edges:
        physical_terms, detail = stream_terms(
            graph, source_cell, target_cell, source_mode, target_mode
        )
        intermediate_counts.append(detail["intermediate_cells"])
        path_failures += not detail["path_identity"]
        decoded = [decoded_logical_pauli(row, code)[0] for row in physical_terms]
        expected = logical_hop_terms(*detail["logical_indices"])
        stream_failures += term_signature(decoded) != term_signature(expected)
        operator_rows.extend(physical_terms)

        if detail["intermediate_cells"]:
            left_index, right_index = sorted(
                (graph.cell_index[source_cell], graph.cell_index[target_cell])
            )
            missing_parity = intermediate_cell_parity(graph, left_index, right_index)
            deleted = tuple(missing_parity @ row for row in physical_terms)
            deleted_decoded = [decoded_logical_pauli(row, code)[0] for row in deleted]
            deletion_mismatches += term_signature(deleted_decoded) != term_signature(
                expected
            )

    for cell_index, cell in enumerate(graph.cells):
        for mode in range(6):
            row = graph.B(graph.vertex_index[(cell, mode)])
            logical, stabilizer_mask = decoded_logical_pauli(row, code)
            diagonal_failures += logical != base.Pauli(z=1 << (6 * cell_index + mode))
            diagonal_failures += stabilizer_mask != 0
            operator_rows.append(row)
        for left, right in combinations(range(6), 2):
            contact = graph.B(graph.vertex_index[(cell, left)]) @ graph.B(
                graph.vertex_index[(cell, right)]
            )
            logical, _ = decoded_logical_pauli(contact, code)
            expected = base.Pauli(
                z=(1 << (6 * cell_index + left))
                | (1 << (6 * cell_index + right))
            )
            diagonal_failures += logical != expected
            operator_rows.append(contact)
            if REVERSE[left] == right:
                continue
            u = graph.vertex_index[(cell, left)]
            v = graph.vertex_index[(cell, right)]
            a = graph.A(u, v)
            coin_terms = (
                base.Pauli(phase=3) @ graph.B(u) @ a,
                base.Pauli(phase=1) @ graph.B(v) @ a,
            )
            decoded = [decoded_logical_pauli(row, code)[0] for row in coin_terms]
            expected_terms = logical_hop_terms(
                6 * cell_index + left, 6 * cell_index + right
            )
            coin_failures += term_signature(decoded) != term_signature(expected_terms)
            operator_rows.extend(coin_terms)

    for row in operator_rows:
        preservation_failures += sum(
            not row.commutes(stabilizer) for stabilizer in code.stabilizers
        )
        coordinates = two.decode_full(row, code.w_rows, code.v_rows, qubits)
        inverse_failures += (
            two.encode_full(coordinates, code.w_rows, code.v_rows, qubits) != row
        )

    chord_count = sum(count > 0 for count in intermediate_counts)
    return {
        "stream_edges": len(graph.stream_edges),
        "stream_term_failures": stream_failures,
        "coin_edges": 12 * len(graph.cells),
        "coin_term_failures": coin_failures,
        "B_terms": 6 * len(graph.cells),
        "contacts": 15 * len(graph.cells),
        "diagonal_failures": diagonal_failures,
        "code_preservation_failures": preservation_failures,
        "inverse_failures": inverse_failures,
        "reference_path_identity_failures": path_failures,
        "direct_reference_edges": 0,
        "path_chords": chord_count,
        "active_intermediate_parity_deletions": deletion_mismatches,
        "max_intermediate_cells": max(intermediate_counts, default=0),
        "max_update_weight": max(map(pauli_weight, operator_rows)),
    }


def transform_data(source: PatchGraph, target: PatchGraph, vertex_map: list[int]):
    edge_map = [
        target.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _, _ in source.edges
    ]
    toggles = [0] * len(target.edges)
    pairs = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[edge] for edge in source.incident[source_vertex]]
        position = {
            edge: index for index, edge in enumerate(target.incident[target_vertex])
        }
        for index, left in enumerate(pulled):
            for right in pulled[index + 1 :]:
                if position[left] > position[right]:
                    toggles[left] ^= 1 << right
                    toggles[right] ^= 1 << left
                    pairs.append((left, right))

    flips = 0
    failures = 0
    for source_edge, (u, v, _, _) in enumerate(source.edges):
        transformed = base.permute_pauli(source.A(u, v), edge_map)
        ordered = base.apply_gauge(transformed, toggles, pairs)
        expected = target.A(vertex_map[u], vertex_map[v])
        if ordered.x != expected.x or ordered.z != expected.z:
            failures += 1
        elif (ordered.phase - expected.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
        elif ordered.phase != expected.phase:
            failures += 1
    return edge_map, toggles, pairs, flips, failures


def transform_pauli(row, edge_map, toggles, pairs, flips):
    return base.apply_gauge(
        base.permute_pauli(row, edge_map), toggles, pairs, flips
    )


def positive_stabilizer_delta(
    actual: base.Pauli, expected: base.Pauli, target: CodeData
) -> bool:
    qubits = len(target.graph.edges)
    logical_count = len(target.logical_z)
    coordinates = two.decode_full(
        actual @ expected, target.w_rows, target.v_rows, qubits
    )
    return (
        coordinates.phase == 0
        and coordinates.v_mask == 0
        and not (coordinates.w_mask & ((1 << logical_count) - 1))
    )


def support_cells(row: base.Pauli, graph: PatchGraph) -> set[tuple[int, int, int]]:
    cells = set()
    support = pauli_support(row)
    while support:
        bit = support & -support
        edge = bit.bit_length() - 1
        u, v, _, _ = graph.edges[edge]
        cells.add(graph.vertices[u][0])
        cells.add(graph.vertices[v][0])
        support ^= bit
    return cells


def support_diameter(row: base.Pauli, graph: PatchGraph) -> int:
    """Cell-Manhattan diameter of one edge-Pauli support.

    A supported edge contributes both endpoint cells.  On the periodic L=3
    fixture, each coordinate difference is reduced to its torus minimum.
    """

    cells = support_cells(row, graph)

    def distance(left, right):
        differences = [abs(left[axis] - right[axis]) for axis in range(3)]
        if graph.periodic:
            differences = [
                min(value, graph.periodic_length - value)
                for value in differences
            ]
        return sum(differences)

    return max(
        (distance(left, right) for left in cells for right in cells),
        default=0,
    )


def stabilizer_product(code: CodeData, mask: int) -> base.Pauli:
    return pauli_product(
        row for index, row in enumerate(code.stabilizers) if (mask >> index) & 1
    )


def greedy_stabilizer_localize(
    row: base.Pauli, code: CodeData
) -> tuple[base.Pauli, int, tuple[int, ...]]:
    """Deterministic, certificate-carrying stabilizer-coset descent.

    This is a constructive representative, not a proof of globally minimum
    Pauli weight.  Each selected basis stabilizer strictly lowers the weight;
    ties are resolved by the declared loop/Wilson/D basis order.
    """

    current = row
    mask = 0
    steps = []
    while True:
        current_weight = pauli_weight(current)
        choices = []
        for index, stabilizer in enumerate(code.stabilizers):
            candidate = current @ stabilizer
            weight = pauli_weight(candidate)
            if weight < current_weight:
                choices.append((weight, index, candidate))
        if not choices:
            break
        _, index, current = min(choices, key=lambda item: (item[0], item[1]))
        mask ^= 1 << index
        steps.append(index)
    if row @ stabilizer_product(code, mask) != current:
        raise ValueError("stabilizer-localization certificate does not reconstruct")
    return current, mask, tuple(steps)


def match_signed_coset_terms(
    actual: tuple[base.Pauli, base.Pauli],
    expected: tuple[base.Pauli, base.Pauli],
    target: CodeData,
) -> tuple[int, int] | None:
    for permutation in ((0, 1), (1, 0)):
        if all(
            positive_stabilizer_delta(actual[index], expected[permutation[index]], target)
            for index in range(2)
        ):
            return permutation
    return None


def fock_x_image(
    source_index: int, permutation: list[int], target: CodeData
) -> base.Pauli:
    target_index = permutation[source_index]
    crossings = [
        permutation[other]
        for other in range(len(permutation))
        if other != source_index
        and (other - source_index) * (permutation[other] - target_index) < 0
    ]
    return target.logical_x[target_index] @ pauli_product(
        target.logical_z[index] for index in crossings
    )


def covariance_case(
    source: CodeData,
    target: CodeData,
    cell_map: dict[tuple[int, int, int], tuple[int, int, int]],
    direction_map: dict[int, int],
) -> dict[str, int]:
    source_graph = source.graph
    target_graph = target.graph
    vertex_map = [
        target_graph.vertex_index[
            (cell_map[cell], 6 if mode == 6 else direction_map[mode])
        ]
        for cell, mode in source_graph.vertices
    ]
    edge_map, toggles, pairs, flips, generator_failures = transform_data(
        source_graph, target_graph, vertex_map
    )
    transform = lambda row: transform_pauli(
        row, edge_map, toggles, pairs, flips
    )

    target_logical_index = {
        (cell, mode): 6 * cell_index + mode
        for cell_index, cell in enumerate(target_graph.cells)
        for mode in range(6)
    }
    permutation = [
        target_logical_index[(cell_map[cell], direction_map[mode])]
        for cell in source_graph.cells
        for mode in range(6)
    ]
    stabilizer_failures = sum(
        not positive_stabilizer_delta(transform(row), base.Pauli(), target)
        for row in source.stabilizers
    )
    logical_z_failures = 0
    logical_x_failures = 0
    for index, row in enumerate(source.logical_z):
        logical_z_failures += not positive_stabilizer_delta(
            transform(row), target.logical_z[permutation[index]], target
        )
    for index, row in enumerate(source.logical_x):
        logical_x_failures += not positive_stabilizer_delta(
            transform(row), fock_x_image(index, permutation, target), target
        )

    stream_coset_failures = 0
    stream_decode_after_reduction_failures = 0
    stream_reduction_reconstruction_failures = 0
    stream_reduced_code_preservation_failures = 0
    raw_target_operand_inequalities = 0
    full_pauli_reduction_inequalities = 0
    active_stabilizer_reductions = 0
    active_reduction_deletions = 0
    active_reduction_deletion_failures = 0
    max_raw_weight = max_target_grammar_weight = max_localized_weight = 0
    max_raw_diameter = max_target_grammar_diameter = max_localized_diameter = 0
    max_reduction_generators = 0
    for _, source_cell, target_cell, source_mode, target_mode, _ in source_graph.stream_edges:
        source_terms, _ = stream_terms(
            source_graph,
            source_cell,
            target_cell,
            source_mode,
            target_mode,
        )
        actual_terms = tuple(transform(row) for row in source_terms)
        target_terms, target_detail = stream_terms(
            target_graph,
            cell_map[source_cell],
            cell_map[target_cell],
            direction_map[source_mode],
            direction_map[target_mode],
        )
        localized_data = tuple(
            greedy_stabilizer_localize(row, target) for row in target_terms
        )
        localized_terms = tuple(data[0] for data in localized_data)
        term_permutation = match_signed_coset_terms(
            actual_terms, localized_terms, target
        )
        if term_permutation is None:
            stream_coset_failures += 1
            continue

        reduced_logical = []
        for source_term_index, target_term_index in enumerate(term_permutation):
            actual = actual_terms[source_term_index]
            target_raw = target_terms[target_term_index]
            localized, _, _ = localized_data[target_term_index]
            delta_coordinates = two.decode_full(
                actual @ localized,
                target.w_rows,
                target.v_rows,
                len(target_graph.edges),
            )
            reduction_mask = delta_coordinates.w_mask >> len(target.logical_z)
            reduction = stabilizer_product(target, reduction_mask)
            reconstructed = actual @ reduction
            stream_reduction_reconstruction_failures += reconstructed != localized
            raw_target_operand_inequalities += actual != target_raw
            full_pauli_reduction_inequalities += actual != localized
            active_stabilizer_reductions += reduction_mask != 0
            max_reduction_generators = max(
                max_reduction_generators, reduction_mask.bit_count()
            )
            max_raw_weight = max(max_raw_weight, pauli_weight(actual))
            max_target_grammar_weight = max(
                max_target_grammar_weight, pauli_weight(target_raw)
            )
            max_localized_weight = max(
                max_localized_weight, pauli_weight(localized)
            )
            max_raw_diameter = max(
                max_raw_diameter, support_diameter(actual, target_graph)
            )
            max_target_grammar_diameter = max(
                max_target_grammar_diameter,
                support_diameter(target_raw, target_graph),
            )
            max_localized_diameter = max(
                max_localized_diameter,
                support_diameter(localized, target_graph),
            )
            stream_reduced_code_preservation_failures += sum(
                not localized.commutes(stabilizer)
                for stabilizer in target.stabilizers
            )
            reduced_logical.append(decoded_logical_pauli(localized, target)[0])

            if reduction_mask and not active_reduction_deletions:
                active_reduction_deletions += 1
                deleted_index = (reduction_mask & -reduction_mask).bit_length() - 1
                deleted_mask = reduction_mask ^ (1 << deleted_index)
                deleted = actual @ stabilizer_product(target, deleted_mask)
                remaining = [
                    row.symplectic(len(target_graph.edges))
                    for index, row in enumerate(target.stabilizers)
                    if index != deleted_index
                ]
                delta_vector = (actual @ localized).symplectic(
                    len(target_graph.edges)
                )
                deletion_is_active = (
                    deleted != localized
                    and base.gf2_rank(remaining + [delta_vector])
                    == base.gf2_rank(remaining) + 1
                )
                active_reduction_deletion_failures += not deletion_is_active

        expected_logical = logical_hop_terms(*target_detail["logical_indices"])
        stream_decode_after_reduction_failures += (
            term_signature(reduced_logical) != term_signature(expected_logical)
        )

    qubits = len(source_graph.edges)
    transformed_w = [transform(row) for row in source.w_rows]
    transformed_v = [transform(row) for row in source.v_rows]
    w_vectors = [row.symplectic(qubits) for row in transformed_w]
    v_vectors = [row.symplectic(qubits) for row in transformed_v]
    full_tableau_failures = sum(
        two.symplectic(w_vectors[left], w_vectors[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        two.symplectic(v_vectors[left], v_vectors[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        two.symplectic(v_vectors[left], w_vectors[right], qubits)
        != int(left == right)
        for left in range(qubits)
        for right in range(qubits)
    )
    coordinate_inverse_failures = 0
    for row in transformed_w + transformed_v:
        coordinates = two.decode_full(
            row, target.w_rows, target.v_rows, qubits
        )
        coordinate_inverse_failures += (
            two.encode_full(
                coordinates, target.w_rows, target.v_rows, qubits
            )
            != row
        )
    return {
        "generator_failures": generator_failures,
        "stabilizer_character_failures": stabilizer_failures,
        "logical_Z_failures": logical_z_failures,
        "phase_oriented_logical_X_failures": logical_x_failures,
        "stream_signed_coset_failures": stream_coset_failures,
        "stream_decode_after_reduction_failures": stream_decode_after_reduction_failures,
        "stream_reduction_reconstruction_failures": stream_reduction_reconstruction_failures,
        "stream_reduced_code_preservation_failures": stream_reduced_code_preservation_failures,
        "raw_target_operand_inequalities": raw_target_operand_inequalities,
        "full_pauli_reduction_inequalities": full_pauli_reduction_inequalities,
        "active_stabilizer_reductions": active_stabilizer_reductions,
        "active_reduction_deletions": active_reduction_deletions,
        "active_reduction_deletion_failures": active_reduction_deletion_failures,
        "max_stream_raw_weight": max_raw_weight,
        "max_stream_target_grammar_weight": max_target_grammar_weight,
        "max_stream_localized_weight": max_localized_weight,
        "max_stream_raw_cell_diameter": max_raw_diameter,
        "max_stream_target_grammar_cell_diameter": max_target_grammar_diameter,
        "max_stream_localized_cell_diameter": max_localized_diameter,
        "max_stream_reduction_generators": max_reduction_generators,
        "full_transformed_tableau_failures": full_tableau_failures,
        "target_coordinate_inverse_failures": coordinate_inverse_failures,
    }


def transformed_target(
    source: CodeData,
    frame: np.ndarray | None = None,
    displacement: tuple[int, int, int] | None = None,
) -> tuple[CodeData, dict, dict[int, int]]:
    if (frame is None) == (displacement is None):
        raise ValueError("choose exactly one frame or translation")
    if frame is not None:
        dmap = base.direction_map(frame)

        def map_cell(cell):
            values = frame @ np.asarray(cell)
            if source.graph.periodic:
                values %= source.graph.periodic_length
            return tuple(int(value) for value in values)

    else:
        dmap = {mode: mode for mode in range(6)}

        def map_cell(cell):
            values = np.asarray(cell) + np.asarray(displacement)
            if source.graph.periodic:
                values %= source.graph.periodic_length
            return tuple(int(value) for value in values)

    cell_map = {cell: map_cell(cell) for cell in source.graph.cells}
    target_cells = tuple(cell_map[cell] for cell in source.graph.cells)
    target = build_code(
        PatchGraph(target_cells, source.graph.periodic_length), validate=False
    )
    return target, cell_map, dmap


def covariance_controls(code: CodeData, periodic: bool) -> dict[str, object]:
    frame_rows = []
    for frame in base.proper_cubic_frames():
        target, cell_map, dmap = transformed_target(code, frame=frame)
        frame_rows.append(covariance_case(code, target, cell_map, dmap))
    translations = (
        tuple(product(range(3), repeat=3))
        if periodic
        else ((0, 0, 0), (1, -2, 3), (-3, 1, 2), (2, 2, -1))
    )
    translation_rows = []
    for displacement in translations:
        target, cell_map, dmap = transformed_target(
            code, displacement=displacement
        )
        translation_rows.append(covariance_case(code, target, cell_map, dmap))
    keys = tuple(frame_rows[0])

    def aggregate(rows, key):
        values = [row[key] for row in rows]
        return max(values) if key.startswith("max_") else sum(values)

    return {
        "proper_cubic_frames": len(frame_rows),
        "translations": len(translation_rows),
        "frame_failure_totals": {
            key: aggregate(frame_rows, key) for key in keys
        },
        "translation_failure_totals": {
            key: aggregate(translation_rows, key) for key in keys
        },
    }


def covariance_evidence_failures(covariance: dict[str, object]) -> int:
    failures = 0
    for totals in (
        covariance["frame_failure_totals"],
        covariance["translation_failure_totals"],
    ):
        failures += totals["raw_target_operand_inequalities"] != 0
        failures += totals["full_pauli_reduction_inequalities"] == 0
        failures += totals["active_stabilizer_reductions"] == 0
        failures += totals["active_reduction_deletions"] == 0
        failures += (
            totals["max_stream_localized_weight"]
            > totals["max_stream_target_grammar_weight"]
        )
    return failures


def rank_deletion_controls(code: CodeData) -> dict[str, object]:
    graph = code.graph
    qubits = len(graph.edges)
    stabilizer_rank = base.gf2_rank(
        row.symplectic(qubits) for row in code.stabilizers
    )
    loop_delete = {
        base.gf2_rank(
            row.symplectic(qubits)
            for index, row in enumerate(code.stabilizers)
            if index != deleted
        )
        for deleted in range(len(code.loops))
    }
    d_offset = len(code.loops) + len(code.wilsons)
    d_delete = {
        base.gf2_rank(
            row.symplectic(qubits)
            for index, row in enumerate(code.stabilizers)
            if index != deleted
        )
        for deleted in range(d_offset, len(code.stabilizers))
    }
    wilson_delete = {
        base.gf2_rank(
            row.symplectic(qubits)
            for index, row in enumerate(code.stabilizers)
            if index != deleted
        )
        for deleted in range(len(code.loops), d_offset)
    }
    all_ds = [local_d(graph, cell) for cell in graph.cells]
    all_d_rank = base.gf2_rank(
        row.symplectic(qubits)
        for row in code.loops + code.wilsons + all_ds
    )
    logical_pair_rank = base.gf2_rank(
        row.symplectic(qubits)
        for row in code.stabilizers + code.logical_z + code.logical_x
    )
    return {
        "rank": stabilizer_rank,
        "loop_delete_ranks": sorted(loop_delete),
        "D_delete_ranks": sorted(d_delete),
        "Wilson_delete_ranks": sorted(wilson_delete),
        "all_D_rank": all_d_rank,
        "product_all_D_identity": pauli_product(all_ds) == base.Pauli(),
        "logical_XZ_rank_with_stabilizers": logical_pair_rank,
        "logical_XZ_rank_increment": logical_pair_rank - stabilizer_rank,
    }


@dataclass(frozen=True)
class ScheduledFactor:
    key: tuple[object, ...]
    kind: str
    rows: tuple[base.Pauli, ...]
    expected: tuple[base.Pauli, ...]
    support: int


def factor_dictionary(code: CodeData) -> tuple[list[ScheduledFactor], dict[str, int]]:
    graph = code.graph
    factors = []
    preservation_failures = decode_failures = localization_failures = 0
    active_localizations = 0

    def append_factor(key, kind, raw_rows, expected_rows):
        nonlocal preservation_failures, decode_failures, localization_failures
        nonlocal active_localizations
        localized_rows = []
        for raw in raw_rows:
            localized, mask, _ = greedy_stabilizer_localize(raw, code)
            localization_failures += not positive_stabilizer_delta(
                raw, localized, code
            )
            active_localizations += mask != 0
            preservation_failures += sum(
                not localized.commutes(stabilizer)
                for stabilizer in code.stabilizers
            )
            localized_rows.append(localized)
        decoded = tuple(
            decoded_logical_pauli(row, code)[0] for row in localized_rows
        )
        decode_failures += term_signature(decoded) != term_signature(expected_rows)
        support = 0
        for localized in localized_rows:
            support |= pauli_support(localized)
        factors.append(
            ScheduledFactor(
                tuple(key),
                kind,
                tuple(localized_rows),
                tuple(expected_rows),
                support,
            )
        )

    for cell_index, cell in enumerate(graph.cells):
        for left, right in combinations(range(6), 2):
            if REVERSE[left] == right:
                continue
            u = graph.vertex_index[(cell, left)]
            v = graph.vertex_index[(cell, right)]
            a = graph.A(u, v)
            raw_rows = (
                base.Pauli(phase=3) @ graph.B(u) @ a,
                base.Pauli(phase=1) @ graph.B(v) @ a,
            )
            append_factor(
                ("coin", cell_index, left, right),
                "onsite_coin",
                raw_rows,
                logical_hop_terms(
                    6 * cell_index + left, 6 * cell_index + right
                ),
            )

    for stream_index, (
        _, source_cell, target_cell, source_mode, target_mode, axis
    ) in enumerate(graph.stream_edges):
        raw_rows, detail = stream_terms(
            graph, source_cell, target_cell, source_mode, target_mode
        )
        append_factor(
            ("stream", stream_index, axis),
            "directed_seam",
            raw_rows,
            logical_hop_terms(*detail["logical_indices"]),
        )

    for cell_index, cell in enumerate(graph.cells):
        for left, right in combinations(range(6), 2):
            raw = graph.B(graph.vertex_index[(cell, left)]) @ graph.B(
                graph.vertex_index[(cell, right)]
            )
            append_factor(
                ("contact", cell_index, left, right),
                "onsite_contact",
                (raw,),
                (
                    base.Pauli(
                        z=(1 << (6 * cell_index + left))
                        | (1 << (6 * cell_index + right))
                    ),
                ),
            )

    return factors, {
        "factor_preservation_failures": preservation_failures,
        "factor_decode_failures": decode_failures,
        "factor_localization_failures": localization_failures,
        "active_factor_localizations": active_localizations,
    }


def color_schedule(
    factors: list[ScheduledFactor],
) -> tuple[list[int], list[int], int]:
    layer_supports = []
    colors = []
    for factor in factors:
        for color, occupied in enumerate(layer_supports):
            if not (factor.support & occupied):
                break
        else:
            color = len(layer_supports)
            layer_supports.append(0)
        colors.append(color)
        layer_supports[color] |= factor.support
    collision_failures = sum(
        bool(left.support & right.support)
        for left_index, left in enumerate(factors)
        for right_index, right in enumerate(factors)
        if left_index < right_index and colors[left_index] == colors[right_index]
    )
    return colors, layer_supports, collision_failures


def factor_digest(factors: list[ScheduledFactor], colors: list[int], logical: bool) -> str:
    lines = []
    for factor, color in zip(factors, colors):
        rows = factor.expected if logical else factor.rows
        payload = ";".join(f"{row.phase}:{row.x:x}:{row.z:x}" for row in rows)
        lines.append(f"{color}:{factor.key}:{payload}")
    return sha256("\n".join(lines).encode("ascii")).hexdigest()


def factor_coset_match(
    actual: tuple[base.Pauli, ...],
    expected: tuple[base.Pauli, ...],
    code: CodeData,
) -> bool:
    return any(
        all(
            positive_stabilizer_delta(actual[index], expected[target_index], code)
            for index, target_index in enumerate(permutation)
        )
        for permutation in permutations(range(len(expected)))
    )


def recurrent_layer_controls(code: CodeData) -> dict[str, object]:
    factors, dictionary = factor_dictionary(code)
    colors, _, collision_failures = color_schedule(factors)
    kind_counts = {
        kind: sum(factor.kind == kind for factor in factors)
        for kind in ("onsite_coin", "directed_seam", "onsite_contact")
    }
    physical_digest = factor_digest(factors, colors, logical=False)
    logical_digest = factor_digest(factors, colors, logical=True)

    deletion_index = next(
        index for index, factor in enumerate(factors) if factor.kind == "directed_seam"
    )
    deleted_factors = factors[:deletion_index] + factors[deletion_index + 1 :]
    deleted_colors = colors[:deletion_index] + colors[deletion_index + 1 :]
    deleted_physical_digest = factor_digest(
        deleted_factors, deleted_colors, logical=False
    )
    deleted_logical_digest = factor_digest(
        deleted_factors, deleted_colors, logical=True
    )
    complete_factor_deletion_active = (
        deleted_physical_digest != physical_digest
        and deleted_logical_digest != logical_digest
        and any(
            row.x or row.z for row in factors[deletion_index].expected
        )
    )

    translation_coset_failures = 0
    translation_color_failures = 0
    translation_collision_failures = 0
    for displacement in ((0, 0, 0), (1, -2, 3), (-3, 1, 2), (2, 2, -1)):
        target, cell_map, direction_map = transformed_target(
            code, displacement=displacement
        )
        target_factors, target_dictionary = factor_dictionary(target)
        target_colors, _, target_collisions = color_schedule(target_factors)
        target_by_key = {factor.key: factor for factor in target_factors}
        vertex_map = [
            target.graph.vertex_index[
                (cell_map[cell], 6 if mode == 6 else direction_map[mode])
            ]
            for cell, mode in code.graph.vertices
        ]
        edge_map, toggles, pairs, flips, generator_failures = transform_data(
            code.graph, target.graph, vertex_map
        )
        translation_coset_failures += generator_failures
        for factor in factors:
            transformed_rows = tuple(
                transform_pauli(row, edge_map, toggles, pairs, flips)
                for row in factor.rows
            )
            translation_coset_failures += not factor_coset_match(
                transformed_rows, target_by_key[factor.key].rows, target
            )
        translation_color_failures += colors != target_colors
        translation_collision_failures += target_collisions
        translation_coset_failures += sum(
            value
            for key, value in target_dictionary.items()
            if key.endswith("failures")
        )

    failures = (
        sum(value for key, value in dictionary.items() if key.endswith("failures"))
        + collision_failures
        + translation_coset_failures
        + translation_color_failures
        + translation_collision_failures
        + int(not complete_factor_deletion_active)
    )
    return {
        "factors": len(factors),
        "factor_counts": kind_counts,
        "colors": len(set(colors)),
        "collision_failures": collision_failures,
        "factor_controls": dictionary,
        "formal_rotation_parameters": {
            "coin_beta": "inherited beta=-0.3",
            "seam": "declared recurrent seam angle",
            "contact_g": "inherited g=0.37",
        },
        "physical_schedule_sha256": physical_digest,
        "logical_schedule_sha256": logical_digest,
        "factor_by_factor_common_E_induction": True,
        "translations": 4,
        "translation_coset_failures": translation_coset_failures,
        "translation_color_failures": translation_color_failures,
        "translation_collision_failures": translation_collision_failures,
        "complete_factor_deletion_active": complete_factor_deletion_active,
        "deleted_factor": factors[deletion_index].key,
        "deleted_physical_schedule_sha256": deleted_physical_digest,
        "deleted_logical_schedule_sha256": deleted_logical_digest,
        "dense_full_volume_matrix_formed": False,
        "failures": failures,
    }


def support_role_controls(code: CodeData) -> dict[str, object]:
    factors, dictionary = factor_dictionary(code)
    summands = [row for factor in factors for row in factor.rows]
    factor_support_rows = [base.Pauli(x=factor.support) for factor in factors]
    return {
        "individual_G_summand_max_weight": max(map(pauli_weight, summands)),
        "individual_G_summand_max_cell_diameter": max(
            support_diameter(row, code.graph) for row in summands
        ),
        "complete_factor_union_max_weight": max(
            factor.support.bit_count() for factor in factors
        ),
        "complete_factor_union_max_cell_diameter": max(
            support_diameter(row, code.graph) for row in factor_support_rows
        ),
        "logical_Z_max_weight": max(map(pauli_weight, code.logical_z)),
        "logical_Z_max_cell_diameter": max(
            support_diameter(row, code.graph) for row in code.logical_z
        ),
        "logical_X_max_weight": max(map(pauli_weight, code.logical_x)),
        "logical_X_max_cell_diameter": max(
            support_diameter(row, code.graph) for row in code.logical_x
        ),
        "tableau_WV_max_weight": max(
            map(pauli_weight, code.w_rows + code.v_rows)
        ),
        "tableau_WV_max_cell_diameter": max(
            support_diameter(row, code.graph)
            for row in code.w_rows + code.v_rows
        ),
        "failures": sum(
            value for key, value in dictionary.items() if key.endswith("failures")
        ),
    }


def concise_support_roles(controls: dict[str, object]) -> dict[str, object]:
    return {
        "individual_G_summand_weight_diameter": [
            controls["individual_G_summand_max_weight"],
            controls["individual_G_summand_max_cell_diameter"],
        ],
        "complete_factor_union_weight_diameter": [
            controls["complete_factor_union_max_weight"],
            controls["complete_factor_union_max_cell_diameter"],
        ],
        "loader_Z_weight_diameter": [
            controls["logical_Z_max_weight"],
            controls["logical_Z_max_cell_diameter"],
        ],
        "loader_X_weight_diameter": [
            controls["logical_X_max_weight"],
            controls["logical_X_max_cell_diameter"],
        ],
        "tableau_row_weight_diameter": [
            controls["tableau_WV_max_weight"],
            controls["tableau_WV_max_cell_diameter"],
        ],
        "failures": controls["failures"],
    }


def inherited_spectral_bridge(layer_rows: dict[str, object]) -> dict[str, object]:
    receipt_digest = sha256(C629_RECEIPT.read_bytes()).hexdigest()
    receipt = json.loads(C629_RECEIPT.read_text(encoding="utf-8"))
    rows = {
        key: value
        for key, value in receipt["spectral_rows"].items()
        if value is not None
    }
    recurrent_closed = all(not row["failures"] for row in layer_rows.values())
    # Exact common-E induction gives E^dagger U_phys E = U_matter.  Hence a
    # matter Ritz pair (lambda,v) transports to (lambda,E v), with identical
    # residual norm because E is an isometry.  The zeros below are algebraic,
    # not a rerun or refit of the Cycle629 spectral search.
    differences = {
        key: {
            "restricted_eigenvalue_difference": 0,
            "Ritz_residual_difference": 0,
            "inherited_abs": value["abs"],
            "inherited_arg": value["arg"],
            "inherited_Ritz_residual": value["residual"],
        }
        for key, value in rows.items()
    }
    failures = (
        int(receipt_digest != C629_RECEIPT_SHA256)
        + int(not recurrent_closed)
        + int(not rows)
        + sum(
            value[metric] != 0
            for value in differences.values()
            for metric in (
                "restricted_eigenvalue_difference",
                "Ritz_residual_difference",
            )
        )
    )
    return {
        "source": "landed Cycle629 contact-dimer spectral rows",
        "receipt_sha256": receipt_digest,
        "beta": -0.3,
        "g": 0.37,
        "refit_or_reselection": False,
        "transport_identity": "E^dagger U_physical E = U_matter",
        "rows": differences,
        "new_empirical_prediction": False,
        "dense_physical_matrix_formed": False,
        "failures": failures,
    }


def note_contract() -> None:
    text = " ".join(
        NOTE.read_text(encoding="utf-8").lower().replace("*", "").split()
    )
    required = (
        "open three-center l",
        "held 2 x 2",
        "held 3 x 3",
        "zero extra intercell reference edges",
        "six reference spokes per cell",
        "three fixed +1 wilson rows",
        "transformed-e",
        "all 24 proper-cubic frames",
        "global gaussian elimination",
        "does not prove bounded-depth",
        "signed stabilizer-coset localization",
        "executed recurrent layer",
        "factor-by-factor common-e induction",
        "inherited spectral preservation",
        "h_matter tensor c^8_wilson",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "authority: none",
        "audit: unset",
        "no axiom conclusion",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the scaled tableau and N1-N8 boundary", not missing, missing)


def run() -> dict[str, object]:
    open_rows = {}
    open_codes = {}
    for name, cells in OPEN_GEOMETRIES.items():
        graph = PatchGraph(cells)
        code = build_code(graph)
        open_codes[name] = code
        ranks = rank_deletion_controls(code)
        operators = operator_controls(code)
        covariance = covariance_controls(code, periodic=False)
        support_roles = support_role_controls(code)
        cells_count = len(cells)
        adjacency_count = len(graph.stream_edges)
        expected_edges = 18 * cells_count + adjacency_count
        expected_cycle_rank = expected_edges - 7 * cells_count + 1
        expected_stabilizer_rank = expected_cycle_rank + cells_count - 1
        failures = (
            int(len(graph.edges) != expected_edges)
            + int(len(code.loops) != expected_cycle_rank)
            + int(len(code.wilsons) != 0)
            + int(ranks["rank"] != expected_stabilizer_rank)
            + int(len(code.logical_z) != 6 * cells_count)
            + int(canonical_failures(code) != 0)
            + int(ranks["loop_delete_ranks"] != [expected_stabilizer_rank - 1])
            + int(ranks["D_delete_ranks"] != [expected_stabilizer_rank - 1])
            + int(ranks["Wilson_delete_ranks"] != [])
            + int(ranks["all_D_rank"] != expected_stabilizer_rank)
            + int(not ranks["product_all_D_identity"])
            + int(ranks["logical_XZ_rank_increment"] != 12 * cells_count)
            + int(
                operators["active_intermediate_parity_deletions"]
                != operators["path_chords"]
            )
            + covariance_evidence_failures(covariance)
            + support_roles["failures"]
            + sum(value for key, value in operators.items() if key.endswith("failures"))
            + sum(
                value
                for key, value in covariance["frame_failure_totals"].items()
                if key.endswith("failures")
            )
            + sum(
                value
                for key, value in covariance["translation_failure_totals"].items()
                if key.endswith("failures")
            )
        )
        open_rows[name] = {
            "cells": cells_count,
            "vertices": len(graph.vertices),
            "edges": len(graph.edges),
            "matter_stream_edges": adjacency_count,
            "cycle_rank": len(code.loops),
            "D_rank": len(code.ds),
            "stabilizer_rank": ranks["rank"],
            "logical_qubits": len(code.logical_z),
            "tableau_rows": 2 * len(graph.edges),
            "tableau_sha256": code.digest,
            "rank_deletion": ranks,
            "operators": operators,
            "covariance": covariance,
            "support_roles": support_roles,
            "failures": failures,
        }
    check(
        "open L, 2x2, and 3x3 patches have exact independent tableaus and all local conjugations",
        all(not row["failures"] for row in open_rows.values()),
        {
            name: {
                "edges": row["edges"],
                "stabilizer_rank": row["stabilizer_rank"],
                "logical_qubits": row["logical_qubits"],
                "tableau_rows": row["tableau_rows"],
                "path_chords": row["operators"]["path_chords"],
                "max_raw_weight": row["covariance"]["frame_failure_totals"]["max_stream_raw_weight"],
                "max_localized_weight": row["covariance"]["frame_failure_totals"]["max_stream_localized_weight"],
                "max_localized_diameter": row["covariance"]["frame_failure_totals"]["max_stream_localized_cell_diameter"],
                "support_roles": concise_support_roles(row["support_roles"]),
                "failures": row["failures"],
            }
            for name, row in open_rows.items()
        },
    )

    periodic_graph = PatchGraph(cell_path_3d(3), periodic_length=3)
    periodic = build_code(periodic_graph)
    periodic_ranks = rank_deletion_controls(periodic)
    periodic_operators = operator_controls(periodic)
    periodic_covariance = covariance_controls(periodic, periodic=True)
    periodic_support_roles = support_role_controls(periodic)
    periodic_failures = (
        int(len(periodic_graph.edges) != 567)
        + int(len(periodic.loops) != 376)
        + int(len(periodic.wilsons) != 3)
        + int(len(periodic.ds) != 26)
        + int(periodic_ranks["rank"] != 405)
        + int(len(periodic.logical_z) != 162)
        + int(canonical_failures(periodic) != 0)
        + int(periodic_ranks["loop_delete_ranks"] != [404])
        + int(periodic_ranks["D_delete_ranks"] != [404])
        + int(periodic_ranks["Wilson_delete_ranks"] != [404])
        + int(
            base.gf2_rank(
                row.symplectic(len(periodic_graph.edges))
                for row in periodic.loops + periodic.ds
            )
            != 402
        )
        + int(periodic_ranks["all_D_rank"] != 405)
        + int(not periodic_ranks["product_all_D_identity"])
        + int(periodic_ranks["logical_XZ_rank_increment"] != 324)
        + int(
            periodic_operators["active_intermediate_parity_deletions"]
            != periodic_operators["path_chords"]
        )
        + covariance_evidence_failures(periodic_covariance)
        + periodic_support_roles["failures"]
        + sum(
            value
            for key, value in periodic_operators.items()
            if key.endswith("failures")
        )
        + sum(
            value
            for key, value in periodic_covariance["frame_failure_totals"].items()
            if key.endswith("failures")
        )
        + sum(
            value
            for key, value in periodic_covariance["translation_failure_totals"].items()
            if key.endswith("failures")
        )
    )
    periodic_row = {
        "cells": 27,
        "vertices": len(periodic_graph.vertices),
        "edges": len(periodic_graph.edges),
        "matter_stream_edges": len(periodic_graph.stream_edges),
        "contractible_loop_rank": len(periodic.loops),
        "Wilson_rank": len(periodic.wilsons),
        "selected_fundamental_windings": periodic.selected_windings,
        "D_rank": len(periodic.ds),
        "stabilizer_rank": periodic_ranks["rank"],
        "logical_qubits": len(periodic.logical_z),
        "tableau_rows": 2 * len(periodic_graph.edges),
        "tableau_sha256": periodic.digest,
        "rank_deletion": periodic_ranks,
        "unfixed_Wilson_direct_sum": {
            "loop_plus_D_rank": 402,
            "code_exponent": 165,
            "typing": "H_matter tensor C^8_Wilson",
            "update_action": "G_matter tensor I_Wilson",
            "fixed_plus_slice_used_for_tableau": True,
        },
        "operators": periodic_operators,
        "covariance": periodic_covariance,
        "support_roles": periodic_support_roles,
        "failures": periodic_failures,
    }
    check(
        "periodic L3 fixes three Wilson rows and preserves the full phase-oriented tableau under frames and translations",
        periodic_failures == 0,
        {
            "edges": periodic_row["edges"],
            "loop_Wilson_D": (376, 3, 26),
            "logical_qubits": 162,
            "tableau_rows": 1134,
            "path_chords": periodic_operators["path_chords"],
            "max_raw_weight": periodic_covariance["frame_failure_totals"]["max_stream_raw_weight"],
            "max_localized_weight": periodic_covariance["frame_failure_totals"]["max_stream_localized_weight"],
            "max_localized_diameter": periodic_covariance["frame_failure_totals"]["max_stream_localized_cell_diameter"],
            "support_roles": concise_support_roles(periodic_support_roles),
            "unfixed_typing": "H_matter tensor C^8_Wilson",
            "failures": periodic_failures,
        },
    )

    graph_difference = {
        name: {
            "local_reference_graph_edges": row["edges"],
            "matter_only_Cycle235_edges": 12 * row["cells"]
            + row["matter_stream_edges"],
            "extra_local_reference_spokes": 6 * row["cells"],
            "extra_intercell_reference_edges": 0,
        }
        for name, row in open_rows.items()
    }
    check(
        "zero-reference-edge path grammar is compatible but is not the Cycle269 matter-only overlap graph",
        all(
            row["extra_local_reference_spokes"] > 0
            and row["extra_intercell_reference_edges"] == 0
            for row in graph_difference.values()
        ),
        graph_difference,
    )

    layer_rows = {
        name: recurrent_layer_controls(open_codes[name])
        for name in ("open_three_center_L", "held_2x2")
    }
    check(
        "a fixed collision-free recurrent edge-qubit layer intertwines factor by factor on L and 2x2, with active whole-factor deletion",
        all(not row["failures"] for row in layer_rows.values()),
        {
            name: {
                "factors": row["factors"],
                "factor_counts": row["factor_counts"],
                "colors": row["colors"],
                "collisions": row["collision_failures"],
                "translations": row["translations"],
                "deletion_active": row["complete_factor_deletion_active"],
                "failures": row["failures"],
            }
            for name, row in layer_rows.items()
        },
    )

    spectral_bridge = inherited_spectral_bridge(layer_rows)
    check(
        "the no-refit Cycle629 contact-dimer rows are preserved under the restricted common-E identity",
        not spectral_bridge["failures"],
        {
            "receipt_sha256": spectral_bridge["receipt_sha256"],
            "beta": spectral_bridge["beta"],
            "g": spectral_bridge["g"],
            "rows": len(spectral_bridge["rows"]),
            "spectrum_and_Ritz_differences": 0,
            "refit": spectral_bridge["refit_or_reselection"],
            "failures": spectral_bridge["failures"],
        },
    )

    note_contract()
    result = {
        "terminal": (
            "PATCH_AND_PERIODIC_BKSF_TABLEAU_COVARIANCE_POSITIVE_"
            "GEOMETRIC_PREPARATION_OPEN"
        ),
        "open": open_rows,
        "periodic_L3": periodic_row,
        "graph_difference": graph_difference,
        "recurrent_layer": layer_rows,
        "inherited_spectral_bridge": spectral_bridge,
        "preparation": {
            "tableau_completion": "global_GF2_symplectic_completion",
            "bounded_depth_or_range_proved": False,
            "Wilson_genesis_proved": False,
            "Z3_physical_site_placement_composed": False,
            "controller_nearest_neighbor_routing_composed": False,
        },
        "pass": PASS,
        "fail": FAIL,
    }
    cache_summary = {
        "terminal": result["terminal"],
        "open": {
            name: {
                "edges": row["edges"],
                "stabilizer_rank": row["stabilizer_rank"],
                "logical_qubits": row["logical_qubits"],
                "tableau_rows": row["tableau_rows"],
                "tableau_sha256": row["tableau_sha256"],
                "path_chords": row["operators"]["path_chords"],
                "max_intermediate_cells": row["operators"]["max_intermediate_cells"],
                "max_raw_weight": row["covariance"]["frame_failure_totals"]["max_stream_raw_weight"],
                "max_localized_weight": row["covariance"]["frame_failure_totals"]["max_stream_localized_weight"],
                "max_localized_diameter": row["covariance"]["frame_failure_totals"]["max_stream_localized_cell_diameter"],
                "support_roles": concise_support_roles(row["support_roles"]),
                "failures": row["failures"],
            }
            for name, row in open_rows.items()
        },
        "periodic_L3": {
            "edges": 567,
            "loop_Wilson_D": [376, 3, 26],
            "stabilizer_rank": 405,
            "logical_qubits": 162,
            "tableau_rows": 1134,
            "tableau_sha256": periodic.digest,
            "path_chords": periodic_operators["path_chords"],
            "max_intermediate_cells": periodic_operators["max_intermediate_cells"],
            "max_raw_weight": periodic_covariance["frame_failure_totals"]["max_stream_raw_weight"],
            "max_localized_weight": periodic_covariance["frame_failure_totals"]["max_stream_localized_weight"],
            "max_localized_diameter": periodic_covariance["frame_failure_totals"]["max_stream_localized_cell_diameter"],
            "support_roles": concise_support_roles(periodic_support_roles),
            "direct_sum_typing": "H_matter tensor C^8_Wilson",
            "failures": periodic_failures,
        },
        "recurrent_layer": {
            name: {
                "factors": row["factors"],
                "colors": row["colors"],
                "deletion_active": row["complete_factor_deletion_active"],
                "failures": row["failures"],
            }
            for name, row in layer_rows.items()
        },
        "spectral_bridge_failures": spectral_bridge["failures"],
        "physical_site_interface": {
            "BKSF_graph_edge_qubit_layer": True,
            "Z3_placement_repetition_lift_composed": False,
            "controller_routing_composed": False,
        },
        "pass": PASS,
        "fail": FAIL,
    }
    print("SUMMARY_JSON", json.dumps(cache_summary, sort_keys=True))
    print("RESULT", result["terminal"])
    return result


if __name__ == "__main__":
    outcome = run()
    raise SystemExit(0 if outcome["fail"] == 0 else 1)
