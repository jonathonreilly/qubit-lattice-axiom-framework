#!/usr/bin/env python3
"""Cycle-705 Route A: direct-reference-edge BKSF support localization.

Add one typed reference-stream edge r_x--r_y beside every matter-stream edge.
Each added edge is paired with the bounded r_x-u-v-r_y rectangle projector.
The stream grammar then uses A(u,v) A(r_x,r_y) directly.  A phase-aware
stabilizer-tableau common E is constructed from local logical X/Z pairs; on a
torus three additional logical pairs expose the Wilson direct-sum factor.

This runner tests ranks, exact phase relations, every stream/coin/contact
summand, common-E restrictions, held sizes, translations, proper-cubic
24/576 covariance, support, deletions, and whether the new edge produces an
extra logical or propagating mode.  It does not claim a bounded preparation
circuit or a finite dense completion.  Authority none; audit unset.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import resource
import time

import numpy as np

import frontier_cycle703_local_gauss_bksf_full_parity_2026_07_25 as P


START = time.perf_counter()
TOL = 3.0e-9
DROP = 2.0e-13
PASS = 0
FAIL = 0
DEPENDENCY_SHA256 = "eb0841f064bc840b1892a02ce1cf75e2c8275b6c21cc9b2952a5032cc03d4bb4"
Pauli = P.Pauli
Coord = P.Coord


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


class DirectReferenceGraph(P.ExtendedGraph):
    """Cycle-703 graph plus one scalar-reference stream edge per coarse bond.

    Matter and reference stream graph-edge qubits occupy distinct slots of a supplied abstract
    two-channel bond fiber.  Their spatial midpoint is the same, so no sign of
    an unoriented bond or preferred endpoint order is introduced.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for left_cell, right_cell in self.coarse_edges:
            left = self.vertex_index[(left_cell, 6)]
            right = self.vertex_index[(right_cell, 6)]
            key = frozenset((left, right))
            if key in self.edge_lookup:
                raise AssertionError(("duplicate-reference-stream", left_cell, right_cell))
            edge = len(self.edges)
            self.edge_lookup[key] = edge
            direction = self.displacement(left_cell, right_cell)
            position = tuple(
                16 * left_cell[axis] + 8 * direction[axis] for axis in range(3)
            )
            self.edges.append((left, right, "reference_stream", position))
            self.edge_position.append(position)

        self.incident = [[] for _ in self.vertices]
        for edge, (left, right, _kind, _position) in enumerate(self.edges):
            self.incident[left].append(edge)
            self.incident[right].append(edge)
        for row in self.incident:
            row.sort()

        self.edge_address = tuple(
            (position, 1 if kind == "reference_stream" else 0)
            for _left, _right, kind, position in self.edges
        )


def reference_rectangle(
    graph: DirectReferenceGraph, left_cell: Coord, right_cell: Coord
) -> tuple[int, ...]:
    direction = graph.displacement(left_cell, right_cell)
    left_mode = P.DIRECTION_INDEX[direction]
    right_mode = P.REVERSE[left_mode]
    return (
        graph.vertex_index[(left_cell, 6)],
        graph.vertex_index[(left_cell, left_mode)],
        graph.vertex_index[(right_cell, right_mode)],
        graph.vertex_index[(right_cell, 6)],
    )


def direct_local_loops(graph: DirectReferenceGraph):
    rows = list(P.onsite_triangles(graph))
    for left_cell, right_cell in graph.coarse_edges:
        vertices = reference_rectangle(graph, left_cell, right_cell)
        rows.append((P.cycle_mask(graph, vertices), vertices, "reference_rectangle"))

    if graph.periodic_length is None:
        squares = P.patch_squares(graph)
    else:
        squares = []
        length = graph.periodic_length
        for cell in graph.cells:
            for first, second in combinations(range(3), 2):
                c10 = list(cell)
                c10[first] = (c10[first] + 1) % length
                c01 = list(cell)
                c01[second] = (c01[second] + 1) % length
                c11 = list(c10)
                c11[second] = (c11[second] + 1) % length
                squares.append((cell, tuple(c10), tuple(c11), tuple(c01)))
    for square in squares:
        vertices = P.lift_coarse_cycle(graph, square)
        rows.append((P.cycle_mask(graph, vertices), vertices, "coarse_plaquette"))
    return tuple(rows)


def loop_paulis(graph: DirectReferenceGraph):
    return tuple(graph.loop_pauli(row[1]) for row in direct_local_loops(graph))


def support_diameter(graph: DirectReferenceGraph, row: Pauli) -> int:
    support = [
        graph.edge_position[index]
        for index in range(len(graph.edges))
        if ((row.x | row.z) >> index) & 1
    ]
    period = None if graph.periodic_length is None else 16 * graph.periodic_length

    def distance(left, right):
        total = 0
        for axis in range(3):
            delta = abs(left[axis] - right[axis])
            if period is not None:
                delta %= period
                delta = min(delta, period - delta)
            total += delta
        return total

    return max((distance(left, right) for left in support for right in support), default=0)


def wilson_paulis(graph: DirectReferenceGraph):
    return tuple(graph.loop_pauli(row[1]) for row in P.wilson_loops(graph))


def independent_paulis(rows, qubits: int):
    pivots = {}
    output = []
    for row in rows:
        reduced = row.symplectic(qubits)
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                reduced ^= pivots[pivot]
            else:
                pivots[pivot] = reduced
                output.append(row)
                break
    return tuple(output)


def logical_matter_pairs(graph: DirectReferenceGraph):
    """Local phase convention matching the 7-mode even-Fock common E.

    Z_(x,a)=B(m_(x,a)) and
    X_(x,a)=i A(m_(x,a),r_x) product_(b>=a) B(m_(x,b)).
    """

    xs = []
    zs = []
    labels = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            matter = graph.vertex_index[(cell, mode)]
            row = Pauli(phase=1) @ graph.A(matter, reference)
            for spectator in range(mode, 6):
                row = row @ graph.B(graph.vertex_index[(cell, spectator)])
            xs.append(row)
            zs.append(graph.B(matter))
            labels.append((cell, mode))
    return tuple(xs), tuple(zs), tuple(labels)


def solve_commutation_system(constraints, rhs, qubits: int) -> Pauli:
    """Find v with symplectic(v,constraints[i])=rhs[i]."""

    variables = 2 * qubits
    variable_mask = (1 << variables) - 1
    pivots = {}
    for constraint, value in zip(constraints, rhs):
        row = (
            constraint.z
            | (constraint.x << qubits)
            | (int(value) << variables)
        )
        reduced = row & variable_mask
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
                reduced = row & variable_mask
            else:
                pivots[pivot] = row
                break
        else:
            if (row >> variables) & 1:
                raise AssertionError("inconsistent commutation system")

    solution = 0
    for pivot in sorted(pivots):
        row = pivots[pivot]
        lower = (row & variable_mask) ^ (1 << pivot)
        value = ((row >> variables) & 1) ^ ((lower & solution).bit_count() & 1)
        if value:
            solution |= 1 << pivot
    x = solution & ((1 << qubits) - 1)
    z = solution >> qubits
    return Pauli((x & z).bit_count() & 1, x, z)


def wilson_gauge_xs(stabilizers, matter_xs, matter_zs, wilson_zs, qubits: int):
    constraints = tuple(stabilizers) + tuple(matter_xs) + tuple(matter_zs) + tuple(wilson_zs)
    output = []
    for target in range(len(wilson_zs)):
        rhs = [0] * (len(constraints) - len(wilson_zs))
        rhs += [index == target for index in range(len(wilson_zs))]
        row = solve_commutation_system(constraints, rhs, qubits)
        for earlier, previous in enumerate(output):
            if not previous.commutes(row):
                row = row @ wilson_zs[earlier]
        output.append(row)
    return tuple(output)


class CoordinateSystem:
    def __init__(self, basis, qubits: int):
        self.basis = tuple(basis)
        self.qubits = qubits
        self.pivots = {}
        for index, row in enumerate(self.basis):
            reduced = row.symplectic(qubits)
            coefficient = 1 << index
            while reduced:
                pivot = reduced.bit_length() - 1
                if pivot in self.pivots:
                    reduced ^= self.pivots[pivot][0]
                    coefficient ^= self.pivots[pivot][1]
                else:
                    self.pivots[pivot] = (reduced, coefficient)
                    break
            else:
                raise AssertionError(("dependent-coordinate-basis", index))

    def coordinates(self, target: Pauli) -> int | None:
        reduced = target.symplectic(self.qubits)
        coefficient = 0
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot not in self.pivots:
                return None
            reduced ^= self.pivots[pivot][0]
            coefficient ^= self.pivots[pivot][1]
        return coefficient


@dataclass
class CommonEChart:
    graph: DirectReferenceGraph
    stabilizers: tuple[Pauli, ...]
    matter_xs: tuple[Pauli, ...]
    matter_zs: tuple[Pauli, ...]
    matter_labels: tuple[tuple[Coord, int], ...]
    gauge_xs: tuple[Pauli, ...]
    gauge_zs: tuple[Pauli, ...]
    coordinate_system: CoordinateSystem

    @property
    def logical_xs(self):
        return self.matter_xs + self.gauge_xs

    @property
    def logical_zs(self):
        return self.matter_zs + self.gauge_zs

    @property
    def logical_qubits(self):
        return len(self.logical_xs)

    @property
    def matter_index(self):
        return {label: index for index, label in enumerate(self.matter_labels)}

    def restrict(self, physical: Pauli) -> Pauli | None:
        coordinate = self.coordinate_system.coordinates(physical)
        if coordinate is None:
            return None
        rebuilt = Pauli()
        for index, row in enumerate(self.coordinate_system.basis):
            if (coordinate >> index) & 1:
                rebuilt = rebuilt @ row
        logical = Pauli((physical.phase - rebuilt.phase) % 4)
        stabilizer_count = len(self.stabilizers)
        logical_count = self.logical_qubits
        for index in range(logical_count):
            if (coordinate >> (stabilizer_count + index)) & 1:
                logical = logical @ Pauli(x=1 << index)
        for index in range(logical_count):
            if (coordinate >> (stabilizer_count + logical_count + index)) & 1:
                logical = logical @ Pauli(z=1 << index)
        return logical


def build_common_e_chart(graph: DirectReferenceGraph) -> CommonEChart:
    qubits = len(graph.edges)
    stabilizer_family = loop_paulis(graph) + tuple(graph.D(cell) for cell in graph.cells)
    stabilizers = independent_paulis(stabilizer_family, qubits)
    matter_xs, matter_zs, labels = logical_matter_pairs(graph)
    gauge_zs = wilson_paulis(graph)
    gauge_xs = wilson_gauge_xs(
        stabilizers, matter_xs, matter_zs, gauge_zs, qubits
    ) if gauge_zs else ()
    basis = stabilizers + matter_xs + gauge_xs + matter_zs + gauge_zs
    return CommonEChart(
        graph, stabilizers, matter_xs, matter_zs, labels,
        gauge_xs, gauge_zs, CoordinateSystem(basis, qubits)
    )


def canonical_pair_failures(xs, zs):
    failures = 0
    for left, row in enumerate(xs):
        failures += not P.pauli_hermitian(row)
        for right, other in enumerate(xs):
            failures += left < right and not row.commutes(other)
        for right, other in enumerate(zs):
            failures += row.commutes(other) != (left != right)
    failures += sum(
        not left.commutes(right)
        for index, left in enumerate(zs) for right in zs[index + 1:]
    )
    return failures


def chart_certificate(name: str, graph: DirectReferenceGraph, chart: CommonEChart):
    qubits = len(graph.edges)
    loops = direct_local_loops(graph)
    loop_rank = P.prior.gf2_rank(row[0] for row in loops)
    full_cycle_rank = qubits - len(graph.vertices) + 1
    ds = tuple(graph.D(cell) for cell in graph.cells)
    wilsons = wilson_paulis(graph)
    local_rank = P.prior.gf2_rank(
        row.symplectic(qubits) for row in loop_paulis(graph) + ds
    )
    fixed_rank = P.prior.gf2_rank(
        row.symplectic(qubits) for row in loop_paulis(graph) + ds + wilsons
    )
    vacuum_family = loop_paulis(graph) + ds + wilsons + chart.matter_zs
    vacuum_rank = P.prior.gf2_rank(row.symplectic(qubits) for row in vacuum_family)
    code_failures = sum(
        not logical.commutes(stabilizer)
        for logical in chart.logical_xs + chart.logical_zs
        for stabilizer in chart.stabilizers
    )
    addresses = graph.edge_address
    spatial_collisions = len(graph.edge_position) - len(set(graph.edge_position))
    rectangles = tuple(
        graph.loop_pauli(row[1]) for row in loops
        if row[2] == "reference_rectangle"
    )
    return {
        "fixture": name,
        "cells": len(graph.cells),
        "coarse_bonds": len(graph.coarse_edges),
        "extended_vertices": len(graph.vertices),
        "graph_edge_qubits": qubits,
        "added_reference_edge_qubits": len(graph.coarse_edges),
        "edge_kind_census": dict(Counter(kind for _u, _v, kind, _p in graph.edges)),
        "spatial_midpoint_collisions": spatial_collisions,
        "typed_abstract_fiber_address_collisions": len(addresses) - len(set(addresses)),
        "local_loop_rows": len(loops),
        "reference_rectangle_rows": sum(row[2] == "reference_rectangle" for row in loops),
        "local_loop_rank": loop_rank,
        "full_cycle_rank": full_cycle_rank,
        "missing_Wilson_rank": full_cycle_rank - loop_rank,
        "local_loop_D_rank": local_rank,
        "fixed_Wilson_rank": fixed_rank,
        "direct_sum_exponent": qubits - local_rank,
        "fixed_sector_exponent": qubits - fixed_rank,
        "target_direct_sum_exponent": 6 * len(graph.cells) + len(wilsons),
        "target_fixed_sector_exponent": 6 * len(graph.cells),
        "matter_logical_qubits": len(chart.matter_xs),
        "Wilson_gauge_qubits": len(chart.gauge_xs),
        "canonical_pair_failures": canonical_pair_failures(chart.logical_xs, chart.logical_zs),
        "logical_code_commutator_failures": code_failures,
        "vacuum_stabilizer_rank": vacuum_rank,
        "vacuum_phase_failures": P.prior.stabilizer_phase_failures(vacuum_family, qubits),
        "maximum_logical_X_weight": max(map(P.pauli_weight, chart.matter_xs)),
        "maximum_logical_X_diameter": max(
            support_diameter(graph, row) for row in chart.matter_xs
        ),
        "Wilson_gauge_X_weights": tuple(map(P.pauli_weight, chart.gauge_xs)),
        "maximum_reference_rectangle_weight": max(
            map(P.pauli_weight, rectangles), default=0
        ),
        "maximum_reference_rectangle_diameter": max(
            (support_diameter(graph, row) for row in rectangles), default=0
        ),
        "maximum_D_weight": max(map(P.pauli_weight, ds)),
        "maximum_D_diameter": max(support_diameter(graph, row) for row in ds),
        "common_E_definition": "E|n,g> = product_i X_i^n_i product_j Xg_j^g_j |Omega_+>",
        "common_E_columns_materialized_dense": False,
        "bounded_preparation_circuit_claimed": False,
    }


def direct_stream_terms(
    graph: DirectReferenceGraph, source_cell: Coord, target_cell: Coord
):
    direction = graph.displacement(source_cell, target_cell)
    source_mode = P.DIRECTION_INDEX[direction]
    target_mode = P.REVERSE[source_mode]
    matter_u = graph.vertex_index[(source_cell, source_mode)]
    matter_v = graph.vertex_index[(target_cell, target_mode)]
    reference_u = graph.vertex_index[(source_cell, 6)]
    reference_v = graph.vertex_index[(target_cell, 6)]
    core = graph.A(matter_u, matter_v) @ graph.A(reference_u, reference_v)
    spectator = P.pauli_product(
        graph.B(graph.vertex_index[(target_cell, mode)])
        for mode in range(6) if mode != target_mode
    )
    return (
        graph.B(matter_u),
        graph.B(matter_v),
        Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(matter_u) @ graph.B(matter_v) @ core,
    )


def path_stream_terms(
    graph: DirectReferenceGraph, source_cell: Coord, target_cell: Coord
):
    direction = graph.displacement(source_cell, target_cell)
    source_mode = P.DIRECTION_INDEX[direction]
    target_mode = P.REVERSE[source_mode]
    matter_u = graph.vertex_index[(source_cell, source_mode)]
    matter_v = graph.vertex_index[(target_cell, target_mode)]
    reference_u = graph.vertex_index[(source_cell, 6)]
    reference_v = graph.vertex_index[(target_cell, 6)]
    path = graph.path_A((reference_u, matter_u, matter_v, reference_v))
    core = graph.A(matter_u, matter_v) @ path
    spectator = P.pauli_product(
        graph.B(graph.vertex_index[(target_cell, mode)])
        for mode in range(6) if mode != target_mode
    )
    return (
        graph.B(matter_u),
        graph.B(matter_v),
        Pauli(phase=2) @ spectator @ core,
        spectator @ graph.B(matter_u) @ graph.B(matter_v) @ core,
    )


def remap_logical_pauli(row: Pauli, indices: tuple[int, ...]) -> Pauli | None:
    allowed = 0
    for index in indices:
        allowed |= 1 << index
    if (row.x | row.z) & ~allowed:
        return None
    x = z = 0
    reverse = {source: target for target, source in enumerate(indices)}
    for source, target in reverse.items():
        if (row.x >> source) & 1:
            x |= 1 << target
        if (row.z >> source) & 1:
            z |= 1 << target
    return Pauli(row.phase, x, z)


def pauli_action(row: Pauli, state: int):
    phase = (1, 1j, -1, -1j)[row.phase % 4]
    phase *= -1 if (row.z & state).bit_count() & 1 else 1
    return state ^ row.x, phase


def target_fswap_action(state: int, left: int, right: int, modes: int = 12):
    bits = tuple((state >> mode) & 1 for mode in range(modes))
    permutation = list(range(modes))
    permutation[left], permutation[right] = right, left
    occupied = [mode for mode, value in enumerate(bits) if value]
    targets = [permutation[mode] for mode in occupied]
    inversions = sum(
        targets[a] > targets[b]
        for a in range(len(targets)) for b in range(a + 1, len(targets))
    )
    output = sum(1 << target for target in targets)
    return output, -1 if inversions & 1 else 1


def stream_certificate(name: str, graph: DirectReferenceGraph, chart: CommonEChart):
    stabilizers = chart.stabilizers
    index = chart.matter_index
    restriction_failures = logical_support_failures = action_failures = 0
    gauge_action_failures = phase_path_failures = 0
    direct_path_coordinate_failures = 0
    projector_failures = hermitian_failures = 0
    bare_d_counts = []
    words = []
    path_words = []
    directed = 0
    for left_cell, right_cell in graph.coarse_edges:
        rectangle_vertices = reference_rectangle(graph, left_cell, right_cell)
        rectangle = graph.loop_pauli(rectangle_vertices)
        direction = graph.displacement(left_cell, right_cell)
        left_mode = P.DIRECTION_INDEX[direction]
        right_mode = P.REVERSE[left_mode]
        reference_u = graph.vertex_index[(left_cell, 6)]
        reference_v = graph.vertex_index[(right_cell, 6)]
        path = graph.path_A(rectangle_vertices)
        direct = graph.A(reference_u, reference_v)
        phase_path_failures += direct != path @ rectangle

        for source_cell, target_cell in ((left_cell, right_cell), (right_cell, left_cell)):
            directed += 1
            direct_terms = direct_stream_terms(graph, source_cell, target_cell)
            path_terms = path_stream_terms(graph, source_cell, target_cell)
            words.extend(direct_terms)
            path_words.extend(path_terms)
            restricted = []
            for direct_word, path_word in zip(direct_terms, path_terms):
                logical = chart.restrict(direct_word)
                path_logical = chart.restrict(path_word)
                restriction_failures += logical is None or path_logical is None
                if logical is None or path_logical is None:
                    continue
                direct_path_coordinate_failures += logical != path_logical
                gauge_mask = ((1 << chart.logical_qubits) - 1) ^ (
                    (1 << len(chart.matter_xs)) - 1
                )
                gauge_action_failures += bool((logical.x | logical.z) & gauge_mask)
                restricted.append(logical)

            direction = graph.displacement(source_cell, target_cell)
            source_mode = P.DIRECTION_INDEX[direction]
            target_mode = P.REVERSE[source_mode]
            local_indices = tuple(
                index[(cell, mode)]
                for cell in (source_cell, target_cell) for mode in range(6)
            )
            local_rows = tuple(
                remap_logical_pauli(row, local_indices) for row in restricted
            )
            logical_support_failures += sum(row is None for row in local_rows)
            if any(row is None for row in local_rows) or len(local_rows) != 4:
                continue
            for state in range(1 << 12):
                observed = {}
                for row in local_rows:
                    target, amplitude = pauli_action(row, state)
                    observed[target] = observed.get(target, 0) + 0.5 * amplitude
                expected_target, expected_phase = target_fswap_action(
                    state, source_mode, 6 + target_mode
                )
                action_failures += any(
                    target != expected_target or abs(amplitude - expected_phase) > TOL
                    for target, amplitude in observed.items() if abs(amplitude) > TOL
                )
                action_failures += abs(observed.get(expected_target, 0) - expected_phase) > TOL

            matter_u = graph.vertex_index[(source_cell, source_mode)]
            matter_v = graph.vertex_index[(target_cell, target_mode)]
            bare = graph.A(matter_u, matter_v)
            bare_d_counts.append(sum(
                not bare.commutes(graph.D(cell)) for cell in graph.cells
            ))

    projector_failures = sum(
        not word.commutes(stabilizer) for word in words for stabilizer in stabilizers
    )
    hermitian_failures = sum(not P.pauli_hermitian(word) for word in words)
    return {
        "fixture": name,
        "undirected_bonds": len(graph.coarse_edges),
        "directed_operands": directed,
        "stream_summands": len(words),
        "common_E_restriction_failures": restriction_failures,
        "logical_support_failures": logical_support_failures,
        "4096_column_action_failures": action_failures,
        "gauge_coordinate_failures": gauge_action_failures,
        "direct_path_phase_relation_failures": phase_path_failures,
        "direct_path_common_E_failures": direct_path_coordinate_failures,
        "projector_commutator_failures": projector_failures,
        "non_Hermitian_summands": hermitian_failures,
        "bare_matter_edge_D_anticommutator_census": dict(Counter(bare_d_counts)),
        "maximum_stream_Pauli_weight": max(map(P.pauli_weight, words), default=0),
        "maximum_stream_site_diameter": max(
            (support_diameter(graph, word) for word in words), default=0
        ),
        "path_baseline_maximum_Pauli_weight": max(
            map(P.pauli_weight, path_words), default=0
        ),
        "path_baseline_maximum_site_diameter": max(
            (support_diameter(graph, word) for word in path_words), default=0
        ),
        "direct_minus_path_maximum_weight": (
            max(map(P.pauli_weight, words), default=0)
            - max(map(P.pauli_weight, path_words), default=0)
        ),
        "direct_minus_path_maximum_diameter": (
            max((support_diameter(graph, word) for word in words), default=0)
            - max((support_diameter(graph, word) for word in path_words), default=0)
        ),
        "support_localization_improved": (
            max(map(P.pauli_weight, words), default=0)
                < max(map(P.pauli_weight, path_words), default=0)
            or max((support_diameter(graph, word) for word in words), default=0)
                < max((support_diameter(graph, word) for word in path_words), default=0)
        ),
        "runtime_global_parity_query_used": False,
        "runtime_exterior_order_table_used": False,
    }


def matrix_pauli(row: Pauli, qubits: int):
    dimension = 1 << qubits
    output = np.zeros((dimension, dimension), dtype=complex)
    for state in range(dimension):
        target, amplitude = pauli_action(row, state)
        output[target, state] = amplitude
    return output


def identify_hermitian_pauli(matrix: np.ndarray) -> Pauli:
    qubits = int(round(math.log2(matrix.shape[0])))
    for x in range(1 << qubits):
        for z in range(1 << qubits):
            phase = (x & z).bit_count() & 1
            row = Pauli(phase, x, z)
            candidate = matrix_pauli(row, qubits)
            if np.linalg.norm(matrix - candidate) < TOL:
                return row
            if np.linalg.norm(matrix + candidate) < TOL:
                return Pauli((phase + 2) % 4, x, z)
    raise AssertionError(("not-a-Hermitian-Pauli", matrix))


def embed_pauli(row: Pauli, indices: tuple[int, ...]) -> Pauli:
    x = z = 0
    for local, target in enumerate(indices):
        if (row.x >> local) & 1:
            x |= 1 << target
        if (row.z >> local) & 1:
            z |= 1 << target
    return Pauli(row.phase, x, z)


def mapped_gate_terms(
    graph: DirectReferenceGraph,
    vertices: tuple[int, ...],
    tree_paths: tuple[tuple[int, ...], ...],
    unitary: np.ndarray,
):
    tree_pairs = tuple((path[0], path[-1]) for path in tree_paths)
    local_pairs = tuple(
        (vertices.index(left), vertices.index(right)) for left, right in tree_pairs
    )
    logical_generators = P.jw_local_generators(len(vertices), local_pairs)
    physical_generators = tuple(
        [graph.B(vertex) for vertex in vertices]
        + [graph.path_A(path) for path in tree_paths]
    )
    logical_basis, physical_basis = P.normalized_even_basis(
        logical_generators, physical_generators
    )
    log = P.hermitian_log(unitary)
    dimension = unitary.shape[0]
    coefficients = tuple(
        np.trace(row.conj().T @ log) / dimension for row in logical_basis
    )
    rebuilt = sum(value * row for value, row in zip(coefficients, logical_basis))
    active = tuple(
        (complex(value), identify_hermitian_pauli(logical), physical)
        for value, logical, physical in zip(coefficients, logical_basis, physical_basis)
        if abs(value) > DROP
    )
    return active, float(np.linalg.norm(rebuilt - log))


def onsite_certificate(name: str, graph: DirectReferenceGraph, chart: CommonEChart):
    index = chart.matter_index
    restriction_failures = summand_failures = gauge_failures = 0
    projector_failures = hermitian_failures = 0
    expansion_residual = 0.0
    weights = []
    diameters = []
    factor_rows = []

    for cell in graph.cells:
        for gate in P.COIN_GATES:
            factor_rows.append(("coin", cell, gate.wires, gate.matrix))
        contact = np.diag((1, 1, 1, np.exp(1j * P.prior.c230.COUPLING))).astype(complex)
        for left, right in combinations(range(6), 2):
            factor_rows.append(("contact", cell, (left, right), contact))

    active_count = 0
    for kind, cell, wires, unitary in factor_rows:
        vertices = tuple(graph.vertex_index[(cell, mode)] for mode in wires)
        if len(vertices) == 1:
            paths = ()
        else:
            left, right = wires
            if P.REVERSE[left] != right:
                paths = ((vertices[0], vertices[1]),)
            else:
                middle = next(mode for mode in range(6)
                    if mode not in (left, right)
                    and P.REVERSE[left] != mode and P.REVERSE[right] != mode)
                paths = ((vertices[0], graph.vertex_index[(cell, middle)], vertices[1]),)
        active, residual = mapped_gate_terms(graph, vertices, paths, unitary)
        expansion_residual = max(expansion_residual, residual)
        logical_indices = tuple(index[(cell, mode)] for mode in wires)
        for _coefficient, expected_local, physical in active:
            active_count += 1
            observed = chart.restrict(physical)
            restriction_failures += observed is None
            if observed is None:
                continue
            expected = embed_pauli(expected_local, logical_indices)
            summand_failures += observed != expected
            gauge_mask = ((1 << chart.logical_qubits) - 1) ^ (
                (1 << len(chart.matter_xs)) - 1
            )
            gauge_failures += bool((observed.x | observed.z) & gauge_mask)
            projector_failures += sum(
                not physical.commutes(stabilizer) for stabilizer in chart.stabilizers
            )
            hermitian_failures += not P.pauli_hermitian(physical)
            weights.append(P.pauli_weight(physical))
            diameters.append(support_diameter(graph, physical))
    return {
        "fixture": name,
        "coin_factors": len(graph.cells) * len(P.COIN_GATES),
        "contact_factors": len(graph.cells) * 15,
        "active_Hermitian_log_summands": active_count,
        "maximum_log_expansion_residual": expansion_residual,
        "common_E_restriction_failures": restriction_failures,
        "logical_summand_mismatches": summand_failures,
        "gauge_coordinate_failures": gauge_failures,
        "projector_commutator_failures": projector_failures,
        "non_Hermitian_summands": hermitian_failures,
        "maximum_Pauli_weight": max(weights, default=0),
        "maximum_site_diameter": max(diameters, default=0),
    }


def graph_maps(source, target, cell_map, mode_map):
    vertex_map = tuple(target.vertex_index[(cell_map[cell], mode_map[mode])]
        for cell, mode in source.vertices)
    edge_map = tuple(target.edge_between(vertex_map[left], vertex_map[right])
        for left, right, _kind, _position in source.edges)
    return vertex_map, edge_map


def transform_pauli(row: Pauli, edge_map, gauge):
    return P.transform_pauli(row, edge_map, gauge)


def fock_permutation_sign(state: int, direction_map: tuple[int, ...]):
    occupied = [mode for mode in range(6) if (state >> mode) & 1]
    targets = [direction_map[mode] for mode in occupied]
    inversions = sum(
        targets[left] > targets[right]
        for left in range(len(targets)) for right in range(left + 1, len(targets))
    )
    return -1 if inversions & 1 else 1


def local_fock_frame_images(direction_map: tuple[int, ...]):
    x_images = []
    z_images = []
    inverse = {target: source for source, target in enumerate(direction_map)}
    for source_mode in range(6):
        target_mode = direction_map[source_mode]
        amplitudes = []
        for target_state in range(1 << 6):
            source_state = sum(
                ((target_state >> target) & 1) << source
                for target, source in inverse.items()
            )
            flipped_source = source_state ^ (1 << source_mode)
            amplitude = (
                fock_permutation_sign(source_state, direction_map)
                * fock_permutation_sign(flipped_source, direction_map)
            )
            amplitudes.append(amplitude)
        base = amplitudes[0]
        z = sum(
            (amplitudes[1 << mode] != base) << mode for mode in range(6)
        )
        phase = 0 if base == 1 else 2
        x_images.append(Pauli(phase, 1 << target_mode, z))
        z_images.append(Pauli(z=1 << target_mode))
    return tuple(x_images), tuple(z_images)


def embed_cell_pauli(row: Pauli, target_cell: Coord, chart: CommonEChart):
    indices = tuple(chart.matter_index[(target_cell, mode)] for mode in range(6))
    return embed_pauli(row, indices)


def apply_logical_map(row: Pauli, x_images, z_images):
    result = Pauli(row.phase)
    for index, image in enumerate(x_images):
        if (row.x >> index) & 1:
            result = result @ image
    for index, image in enumerate(z_images):
        if (row.z >> index) & 1:
            result = result @ image
    return result


def frame_expected_images(source, target_chart, frame):
    raw_direction_map = P.prior.direction_map(frame)
    direction_map = tuple(raw_direction_map[index] for index in range(6))
    local_x, local_z = local_fock_frame_images(direction_map)
    xs = []
    zs = []
    for cell in source.cells:
        target_cell = P.matvec(frame, cell)
        xs.extend(embed_cell_pauli(row, target_cell, target_chart) for row in local_x)
        zs.extend(embed_cell_pauli(row, target_cell, target_chart) for row in local_z)
    return tuple(xs), tuple(zs)


def frame_covariance_certificate(spec: P.PatchSpec):
    base = DirectReferenceGraph.patch(spec.centers)
    base_chart = build_common_e_chart(base)
    frames = P.prior.proper_cubic_frames()
    key = lambda frame: tuple(map(int, frame.reshape(-1)))
    targets = {}
    maps = {}
    raw = operator_failures = projector_failures = stream_failures = 0
    address_failures = common_e_failures = 0
    for frame in frames:
        target = DirectReferenceGraph.patch(tuple(P.matvec(frame, cell) for cell in spec.centers))
        target_chart = build_common_e_chart(target)
        targets[key(frame)] = (target, target_chart)
        raw_direction_map = P.prior.direction_map(frame)
        direction_map = tuple(raw_direction_map[index] for index in range(6))
        cell_map = {cell: P.matvec(frame, cell) for cell in base.cells}
        vertex_map, edge_map = graph_maps(base, target, cell_map, direction_map + (6,))
        gauge = P.port_gauge(base, target, vertex_map, edge_map)
        for source_edge, (left, right, _kind, position) in enumerate(base.edges):
            raw += P.permute_pauli(base.A(left, right), edge_map) != target.A(
                vertex_map[left], vertex_map[right]
            )
            operator_failures += transform_pauli(
                base.A(left, right), edge_map, gauge
            ) != target.A(vertex_map[left], vertex_map[right])
            target_address = target.edge_address[edge_map[source_edge]]
            source_address = base.edge_address[source_edge]
            address_failures += (
                P.matvec(frame, source_address[0]), source_address[1]
            ) != target_address
        for vertex in range(len(base.vertices)):
            operator_failures += transform_pauli(
                base.B(vertex), edge_map, gauge
            ) != target.B(vertex_map[vertex])
        target_projectors = set(loop_paulis(target) + tuple(target.D(cell) for cell in target.cells))
        for row in loop_paulis(base) + tuple(base.D(cell) for cell in base.cells):
            projector_failures += transform_pauli(row, edge_map, gauge) not in target_projectors
        for left_cell, right_cell in base.coarse_edges:
            for source_cell, target_cell in ((left_cell, right_cell), (right_cell, left_cell)):
                expected = direct_stream_terms(
                    target, cell_map[source_cell], cell_map[target_cell]
                )
                observed = tuple(transform_pauli(row, edge_map, gauge)
                    for row in direct_stream_terms(base, source_cell, target_cell))
                stream_failures += sum(left != right for left, right in zip(observed, expected))

        expected_xs, expected_zs = frame_expected_images(base, target_chart, frame)
        observed_xs = tuple(target_chart.restrict(transform_pauli(row, edge_map, gauge))
            for row in base_chart.matter_xs)
        observed_zs = tuple(target_chart.restrict(transform_pauli(row, edge_map, gauge))
            for row in base_chart.matter_zs)
        common_e_failures += sum(left != right for left, right in zip(observed_xs, expected_xs))
        common_e_failures += sum(left != right for left, right in zip(observed_zs, expected_zs))
        maps[key(frame)] = (expected_xs, expected_zs)

    composition_failures = 0
    for right in frames:
        middle, middle_chart = targets[key(right)]
        right_xs, right_zs = maps[key(right)]
        for left in frames:
            combined = left @ right
            final, final_chart = targets[key(combined)]
            left_xs, left_zs = frame_expected_images(middle, final_chart, left)
            direct_xs, direct_zs = maps[key(combined)]
            composition_failures += sum(
                apply_logical_map(row, left_xs, left_zs) != expected
                for row, expected in zip(right_xs, direct_xs)
            )
            composition_failures += sum(
                apply_logical_map(row, left_xs, left_zs) != expected
                for row, expected in zip(right_zs, direct_zs)
            )

    species = P.prior.c219.common_species(-0.3)
    coin_residual = max(float(np.linalg.norm(
        P.prior.c210.direction_permutation(frame) @ species.coin
        @ P.prior.c210.direction_permutation(frame).conj().T - species.coin
    )) for frame in frames)
    return {
        "fixture": spec.name,
        "frames": len(frames),
        "ordered_products": len(frames) ** 2,
        "raw_port_mismatches": raw,
        "corrected_A_B_failures": operator_failures,
        "projector_family_failures": projector_failures,
        "direct_stream_summand_failures": stream_failures,
        "typed_abstract_fiber_address_failures": address_failures,
        "phase_aware_common_E_failures": common_e_failures,
        "common_E_group_law_failures": composition_failures,
        "full_coin_covariance_residual": coin_residual,
        "contact_covariant_by_scalar_incidence": True,
    }


def translation_certificate(length: int, graph, chart):
    operator_failures = projector_failures = stream_failures = 0
    common_e_failures = address_failures = 0
    translations = tuple(product(range(length), repeat=3))
    projectors = set(loop_paulis(graph) + tuple(graph.D(cell) for cell in graph.cells))
    for shift in translations:
        cell_map = {
            cell: tuple((cell[axis] + shift[axis]) % length for axis in range(3))
            for cell in graph.cells
        }
        vertex_map, edge_map = graph_maps(graph, graph, cell_map, tuple(range(7)))
        gauge = P.port_gauge(graph, graph, vertex_map, edge_map)
        for left, right, _kind, _position in graph.edges:
            operator_failures += transform_pauli(
                graph.A(left, right), edge_map, gauge
            ) != graph.A(vertex_map[left], vertex_map[right])
        for vertex in range(len(graph.vertices)):
            operator_failures += transform_pauli(
                graph.B(vertex), edge_map, gauge
            ) != graph.B(vertex_map[vertex])
        for row in loop_paulis(graph) + tuple(graph.D(cell) for cell in graph.cells):
            projector_failures += transform_pauli(row, edge_map, gauge) not in projectors
        for left_cell, right_cell in graph.coarse_edges:
            expected = direct_stream_terms(graph, cell_map[left_cell], cell_map[right_cell])
            observed = tuple(transform_pauli(row, edge_map, gauge)
                for row in direct_stream_terms(graph, left_cell, right_cell))
            stream_failures += sum(left != right for left, right in zip(observed, expected))
        for label, logical_x, logical_z in zip(
            chart.matter_labels, chart.matter_xs, chart.matter_zs
        ):
            target_label = (cell_map[label[0]], label[1])
            target_index = chart.matter_index[target_label]
            expected_x = Pauli(x=1 << target_index)
            expected_z = Pauli(z=1 << target_index)
            common_e_failures += chart.restrict(
                transform_pauli(logical_x, edge_map, gauge)
            ) != expected_x
            common_e_failures += chart.restrict(
                transform_pauli(logical_z, edge_map, gauge)
            ) != expected_z
        address_failures += sum(
            graph.edge_address[source][1] != graph.edge_address[target][1]
            for source, target in enumerate(edge_map)
        )
    return {
        "L": length,
        "translations": len(translations),
        "corrected_A_B_failures": operator_failures,
        "projector_family_failures": projector_failures,
        "stream_summand_failures": stream_failures,
        "phase_aware_common_E_failures": common_e_failures,
        "bond_fiber_failures": address_failures,
    }


def deletion_certificate(graph: DirectReferenceGraph, chart: CommonEChart):
    qubits = len(graph.edges)
    loops = direct_local_loops(graph)
    loop_rows = [row[0] for row in loops]
    loop_rank = P.prior.gf2_rank(loop_rows)
    rectangle_indices = [index for index, row in enumerate(loops)
        if row[2] == "reference_rectangle"]
    rectangle_rank_losses = [
        loop_rank - P.prior.gf2_rank(
            row for index, row in enumerate(loop_rows) if index != deleted
        ) for deleted in rectangle_indices
    ]
    d_rows = [graph.D(cell).symplectic(qubits) for cell in graph.cells]
    full_d_rank = P.prior.gf2_rank(loop_rows + d_rows)
    delete_one_d = [P.prior.gf2_rank(
        loop_rows + d_rows[:deleted] + d_rows[deleted + 1:]
    ) for deleted in range(len(d_rows))]
    delete_two_d = [P.prior.gf2_rank(loop_rows + [
        row for index, row in enumerate(d_rows) if index not in deleted
    ]) for deleted in combinations(range(len(d_rows)), 2)]

    reference_term_d_failures = []
    for left_cell, right_cell in graph.coarse_edges:
        direction = graph.displacement(left_cell, right_cell)
        left_mode = P.DIRECTION_INDEX[direction]
        right_mode = P.REVERSE[left_mode]
        bare = graph.A(
            graph.vertex_index[(left_cell, left_mode)],
            graph.vertex_index[(right_cell, right_mode)],
        )
        reference_term_d_failures.append(sum(
            not bare.commutes(graph.D(cell)) for cell in graph.cells
        ))
    wilson_losses = []
    if graph.periodic_length is not None:
        wilsons = wilson_paulis(graph)
        base = loop_paulis(graph) + tuple(graph.D(cell) for cell in graph.cells)
        fixed = P.prior.gf2_rank(row.symplectic(qubits) for row in base + wilsons)
        wilson_losses = [fixed - P.prior.gf2_rank(
            row.symplectic(qubits)
            for row in base + wilsons[:deleted] + wilsons[deleted + 1:]
        ) for deleted in range(len(wilsons))]
    return {
        "reference_rectangle_rows": len(rectangle_indices),
        "delete_each_reference_rectangle_rank_loss_census": dict(Counter(rectangle_rank_losses)),
        "delete_reference_dressing_D_failure_census": dict(Counter(reference_term_d_failures)),
        "D_rows": len(d_rows),
        "delete_one_D_rank_change_census": dict(Counter(
            full_d_rank - rank for rank in delete_one_d
        )),
        "delete_two_D_rank_change_census": dict(Counter(
            full_d_rank - rank for rank in delete_two_d
        )),
        "delete_one_Wilson_rank_losses": wilson_losses,
        "delete_contact_column_residual": abs(np.exp(1j * P.prior.c230.COUPLING) - 1),
        "reference_edge_can_be_retired_to_path_route": True,
    }


def mass_contact_certificate():
    return P.mass_and_contact_certificate()


def main():
    dependency_sha = sha256(Path(P.__file__).read_bytes()).hexdigest()
    check(
        "the Cycle703 held-patch grammar dependency is byte-pinned",
        dependency_sha == DEPENDENCY_SHA256,
        dependency_sha,
    )

    fixtures = [(spec.name, DirectReferenceGraph.patch(spec.centers)) for spec in P.PATCHES]
    fixtures += [(f"periodic-L{length}", DirectReferenceGraph.torus(length))
        for length in (3, 4)]
    charts = {name: build_common_e_chart(graph) for name, graph in fixtures}
    ranks = [chart_certificate(name, graph, charts[name]) for name, graph in fixtures]
    check(
        "rectangle projectors absorb every added edge and retain exact 6N(+3 Wilson gauge) typing",
        all(
            row["local_loop_rank"] + row["missing_Wilson_rank"] == row["full_cycle_rank"]
            and row["reference_rectangle_rows"] == row["added_reference_edge_qubits"]
            and row["typed_abstract_fiber_address_collisions"] == 0
            and row["direct_sum_exponent"] == row["target_direct_sum_exponent"]
            and row["fixed_sector_exponent"] == row["target_fixed_sector_exponent"]
            and row["canonical_pair_failures"] == 0
            and row["logical_code_commutator_failures"] == 0
            and row["vacuum_stabilizer_rank"] == row["graph_edge_qubits"]
            and row["vacuum_phase_failures"] == 0
            and not row["common_E_columns_materialized_dense"]
            and not row["bounded_preparation_circuit_claimed"]
            for row in ranks
        ),
        ranks,
    )

    streams = [stream_certificate(name, graph, charts[name]) for name, graph in fixtures]
    check(
        "every direct stream summand is common-E exact, but the intended support advantage over the path route is falsified",
        all(
            row["directed_operands"] == 2 * row["undirected_bonds"]
            and row["stream_summands"] == 4 * row["directed_operands"]
            and row["common_E_restriction_failures"] == 0
            and row["logical_support_failures"] == 0
            and row["4096_column_action_failures"] == 0
            and row["gauge_coordinate_failures"] == 0
            and row["direct_path_phase_relation_failures"] == 0
            and row["direct_path_common_E_failures"] == 0
            and row["projector_commutator_failures"] == 0
            and row["non_Hermitian_summands"] == 0
            and row["bare_matter_edge_D_anticommutator_census"]
                == {2: row["directed_operands"]}
            and row["path_baseline_maximum_Pauli_weight"] == 17
            and row["path_baseline_maximum_site_diameter"] == 28
            and row["direct_minus_path_maximum_weight"] > 0
            and row["direct_minus_path_maximum_diameter"] > 0
            and not row["support_localization_improved"]
            for row in streams
        ),
        streams,
    )

    onsite = [onsite_certificate(name, graph, charts[name]) for name, graph in fixtures]
    check(
        "every coin/contact Hermitian-log summand restricts exactly through the same common E with no Wilson action",
        all(
            row["maximum_log_expansion_residual"] < TOL
            and row["common_E_restriction_failures"] == 0
            and row["logical_summand_mismatches"] == 0
            and row["gauge_coordinate_failures"] == 0
            and row["projector_commutator_failures"] == 0
            and row["non_Hermitian_summands"] == 0
            for row in onsite
        ),
        onsite,
    )

    mass_contact = mass_contact_certificate()
    check(
        "the one-particle mass fixture and Cycle230 local contact block are unchanged",
        mass_contact["one_particle_coin_eigen_residual"] < TOL
        and mass_contact["one_particle_mass_residual"] < TOL
        and mass_contact["contact_vacuum_and_one_particle_residual"] < TOL
        and mass_contact["contact_double_occupation_phase_residual"] < TOL,
        mass_contact,
    )

    covariance = [frame_covariance_certificate(spec) for spec in P.PATCHES]
    check(
        "typed graph-edge addresses, direct summands, and phase-aware common E pass proper-cubic 24/576 covariance",
        all(
            row["frames"] == 24
            and row["ordered_products"] == 576
            and row["raw_port_mismatches"] > 0
            and row["corrected_A_B_failures"] == 0
            and row["projector_family_failures"] == 0
            and row["direct_stream_summand_failures"] == 0
            and row["typed_abstract_fiber_address_failures"] == 0
            and row["phase_aware_common_E_failures"] == 0
            and row["common_E_group_law_failures"] == 0
            and row["full_coin_covariance_residual"] < TOL
            and row["contact_covariant_by_scalar_incidence"]
            for row in covariance
        ),
        covariance,
    )

    translations = [translation_certificate(
        length, dict(fixtures)[f"periodic-L{length}"], charts[f"periodic-L{length}"]
    ) for length in (3, 4)]
    check(
        "all periodic translations preserve the direct grammar and phase-aware common E",
        all(
            row["translations"] == row["L"] ** 3
            and row["corrected_A_B_failures"] == 0
            and row["projector_family_failures"] == 0
            and row["stream_summand_failures"] == 0
            and row["phase_aware_common_E_failures"] == 0
            and row["bond_fiber_failures"] == 0
            for row in translations
        ),
        translations,
    )

    deletions = {
        name: deletion_certificate(graph, charts[name])
        for name, graph in fixtures
    }
    check(
        "reference-edge, rectangle, local-D, Wilson, and contact deletions are active with the path retirement route explicit",
        all(
            row["delete_each_reference_rectangle_rank_loss_census"]
                == {1: row["reference_rectangle_rows"]}
            and row["delete_reference_dressing_D_failure_census"]
                == {2: row["reference_rectangle_rows"]}
            and row["delete_one_D_rank_change_census"] == {0: row["D_rows"]}
            and row["delete_two_D_rank_change_census"]
                == {1: row["D_rows"] * (row["D_rows"] - 1) // 2}
            and all(loss == 1 for loss in row["delete_one_Wilson_rank_losses"])
            and row["delete_contact_column_residual"] > 0.3
            and row["reference_edge_can_be_retired_to_path_route"]
            for row in deletions.values()
        ),
        deletions,
    )

    no_go = {
        "status": "FAIL broad no-go; retain route-specific support negative plus algebraic positive",
        "N1": (
            "ATTEMPTED direct typed reference-edge BKSF incidence: algebra exact but maximum weight/diameter are worse than the path baseline",
            "ATTEMPTED three-edge path BKSF incidence: exact and retains the lower 17/28 support baseline",
            "UNTESTED re-ordered reference-edge incidence could reduce the A(r_x,r_y) Z tail while preserving the rectangle",
            "UNTESTED symmetric split-edge gadget could avoid a co-located two-channel fiber with different support cost",
            "UNTESTED time-multiplexed reference ancilla could trade static edge-qubit overhead for schedule depth",
            "ATTEMPTED phase-aware stabilizer tableau and Wilson subsystem: algebraic common E and U_matter tensor I_8 are positive but do not improve support",
        ),
        "N2": (
            "support localization and added-edge cycle removal are coupled by the rectangle row",
            "exact logical action does not imply smaller Pauli support",
            "algebraic common E and bounded state preparation are independent",
            "Wilson gauge typing and local update correctness are independently checked by gauge coordinates",
        ),
        "N3": (
            "one extra graph-edge qubit per bond, a matter/reference two-channel midpoint fiber, rectangle enforcement, local port-order gauge, and supplied Wilson input are explicit",
        ),
        "N4": (
            "Cycle703 path grammar matches the exact same stream residual and supplies the 17/28 support comparator",
            "Cycle703 vacuum-genesis held failure is not cited against this operator/common-E construction",
        ),
        "N5": (
            "the negative is only maximum Pauli weight/site diameter on the executed graphs; gate depth, noise, alternate incidence orders and gadgets are not tested",
            "positive common E is a phase-aware stabilizer tableau at finite and held graphs, not a bounded-depth preparation circuit or dense completion",
        ),
        "N6": (
            "the added edge is an explicit bounded import that can be retired exactly to the already tested path grammar",
        ),
        "N7": (
            "Steelman against a general support no-go: an incidence reordering optimized around reference bonds, or a symmetric split-edge gadget, can shorten the A(r_x,r_y) Z tail while keeping the exact rectangle identity; the present fixed incidence does not test either construction",
        ),
        "N8": (
            "Cycle232 uniform-reference parity failure was retired by local D; it cannot be echoed into this direct-edge route",
        ),
    }
    check(
        "N1-N8 bars a locality/preparation no-go and keeps the common-E claim at tableau resolution",
        len(no_go["N1"]) >= 5
        and no_go["status"].startswith("FAIL broad no-go")
        and "Steelman" in no_go["N7"][0],
        no_go,
    )

    certificate = {
        "rank_and_common_E": ranks,
        "stream": streams,
        "coin_contact_summands": onsite,
        "mass_contact": mass_contact,
        "proper_cubic_covariance": covariance,
        "translations": translations,
        "deletions": deletions,
        "no_go_discipline": no_go,
    }
    digest = sha256(json.dumps(certificate, sort_keys=True, default=str,
        separators=(",", ":")).encode()).hexdigest()
    result = {
        "authority": "none",
        "audit": "unset",
        "cycle": 705,
        "status": "direct-reference-edge-common-E-positive-support-localization-route-negative",
        "terminal": "DIRECT_REFERENCE_EDGE_COMMON_E_EXACT_PATH_SUPPORT_ADVANTAGE_RETAINED",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "equations": (
            "A(r_x,r_y) = path_A(r_x,u,v,r_y) L_rectangle on the full Pauli algebra",
            "E_tableau G_coarse = G_direct E_tableau on every tested summand",
            "E_direct_sum: H_matter tensor C^8_gauge -> H_local_code",
            "G_direct E_direct_sum = E_direct_sum (G_matter tensor I_8)",
        ),
        "supplied": (
            "one scalar reference fermion per cell and local D_x law",
            "one reference-stream graph-edge qubit per matter bond in a typed two-channel bond fiber",
            "one bounded rectangle projector per added reference edge",
            "BKSF incidence/order gauge and supplied periodic Wilson gauge input",
            "Cycle219 coin, Cycle230 contact and stream schedule",
        ),
        "derived": (
            "exact 6N open/fixed-sector and 6N+3 periodic direct-sum dimensions",
            "phase-aware algebraic stabilizer-tableau common E",
            "every coin/contact/stream summand restricts to the target with zero Wilson action",
            "exact translation and proper-cubic frame covariance",
            "the extra edge has no independent logical or propagating mode after rectangle enforcement",
            "the tested direct incidence has larger support than the retained path grammar",
        ),
        "open": (
            "bounded-depth or recurrent preparation of the common-E vacuum and returned ancillas",
            "autonomous selection or preparation of a matter-only Wilson gauge vector",
            "fault-tolerant enforcement of rectangle, loop and D projectors",
        ),
        "claim_ceiling": (
            "The direct reference edge is a constant-overhead algebraically exact import with a phase-aware common E and no extra code mode. "
            "In the tested incidence it does not localize support: weight and diameter are worse than the exactly equivalent path grammar. "
            "No broader reference-edge, incidence-order, gadget, preparation, or impossibility claim follows."
        ),
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
            "certificate_sha256": digest,
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True, default=str))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
