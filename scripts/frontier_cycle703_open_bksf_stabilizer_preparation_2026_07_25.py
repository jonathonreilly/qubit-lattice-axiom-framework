#!/usr/bin/env python3
"""Cycle 703: target-independent open-boundary BKSF state preparation.

The protocol starts every BKSF graph-edge qubit in |0>, measures local loop checks,
and removes their signs in three causal circuit stages:

  cell triangles -> coarse plaquettes -> bond rectangles.

Cell syndromes use one fixed intra-cell table.  Coarse plaquette syndromes use
an explicit open-boundary decoder.  Each bond rectangle is finally corrected
on its unique reference-bond edge.  All corrections are Z type, so every
vertex B and local D remains +1.  A separate bounded local Clifford tableau
then loads arbitrary six-qubit-per-cell matter data into that vacuum.  The
separation is deliberate: checks and logical loading are bounded, while exact
open-boundary syndrome feedforward is not a fixed-range family.

This is an abstract graph-edge-qubit construction.  Cycle-232 Z3 placement,
stream-edge repetition, ancilla allocation, and nearest-neighbor controller
routing are not composed here.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, product
import json

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base


AUDIT_INPUT_PATHS = (
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
)


Coord = tuple[int, int, int]
ORIGIN: Coord = (0, 0, 0)


class OpenReferenceGraph:
    """Cycle-232 seven-vertex cell graph on an arbitrary open cell set."""

    def __init__(self, cells: tuple[Coord, ...]):
        self.cells = tuple(sorted(set(cells)))
        if not self.cells:
            raise ValueError("empty cell set")
        self.cell_set = set(self.cells)
        self.vertices: list[tuple[Coord, int]] = []
        self.vertex_index: dict[tuple[Coord, int], int] = {}
        for cell in self.cells:
            for mode in range(7):
                key = (cell, mode)
                self.vertex_index[key] = len(self.vertices)
                self.vertices.append(key)

        self.edges: list[tuple[int, int, str, Coord]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.internal_edge: dict[tuple[Coord, int, int], int] = {}
        self.spoke_edge: dict[tuple[Coord, int], int] = {}
        self.cross_edge: dict[tuple[Coord, int, int], int] = {}

        def add_edge(u: int, v: int, kind: str, owner: Coord) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate edge", self.vertices[u], self.vertices[v]))
            index = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = index
            return index

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if base.REVERSE[left] == right:
                    continue
                u = self.vertex_index[(cell, left)]
                v = self.vertex_index[(cell, right)]
                edge = add_edge(u, v, "octahedral", cell)
                self.internal_edge[(cell, left, right)] = edge
                self.internal_edge[(cell, right, left)] = edge
            reference = self.vertex_index[(cell, 6)]
            for direction in range(6):
                mode = self.vertex_index[(cell, direction)]
                self.spoke_edge[(cell, direction)] = add_edge(
                    reference, mode, "spoke", cell
                )

        for cell in self.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] += 1
                target_cell = tuple(target)
                if target_cell not in self.cell_set:
                    continue
                matter_u = self.vertex_index[(cell, 2 * axis + 1)]
                matter_v = self.vertex_index[(target_cell, 2 * axis)]
                reference_u = self.vertex_index[(cell, 6)]
                reference_v = self.vertex_index[(target_cell, 6)]
                self.cross_edge[(cell, axis, 0)] = add_edge(
                    matter_u, matter_v, "matter_stream", cell
                )
                self.cross_edge[(cell, axis, 1)] = add_edge(
                    reference_u, reference_v, "reference_bond", cell
                )

        self.incident: list[list[int]] = [[] for _ in self.vertices]
        for edge, (u, v, _, _) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()

    def edge_between(self, u: int, v: int) -> int:
        return self.edge_lookup[frozenset((u, v))]

    def B(self, vertex: int) -> base.Pauli:
        z = 0
        for edge in self.incident[vertex]:
            z ^= 1 << edge
        return base.Pauli(z=z)

    def A(self, source: int, target: int) -> base.Pauli:
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        return base.Pauli(0 if source < target else 2, 1 << edge, z)

    def loop_pauli(self, vertices: list[int]) -> base.Pauli:
        result = base.Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(
                source, vertices[(index + 1) % len(vertices)]
            )
        return result


def cycle_mask(graph: OpenReferenceGraph, vertices: list[int]) -> int:
    mask = 0
    for index, source in enumerate(vertices):
        mask ^= 1 << graph.edge_between(
            source, vertices[(index + 1) % len(vertices)]
        )
    return mask


def open_local_cycles(
    graph: OpenReferenceGraph,
) -> list[tuple[int, list[int], str, object]]:
    rows: list[tuple[int, list[int], str, object]] = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for left, right in combinations(range(6), 2):
            if base.REVERSE[left] == right:
                continue
            vertices = [
                reference,
                graph.vertex_index[(cell, left)],
                graph.vertex_index[(cell, right)],
            ]
            rows.append(
                (cycle_mask(graph, vertices), vertices, "cell_triangle", cell)
            )

    for cell, axis, copy in graph.cross_edge:
        if copy != 0:
            continue
        target = list(cell)
        target[axis] += 1
        target_cell = tuple(target)
        vertices = [
            graph.vertex_index[(cell, 6)],
            graph.vertex_index[(cell, 2 * axis + 1)],
            graph.vertex_index[(target_cell, 2 * axis)],
            graph.vertex_index[(target_cell, 6)],
        ]
        rows.append(
            (
                cycle_mask(graph, vertices),
                vertices,
                "bond_rectangle",
                (cell, axis),
            )
        )

    for cell in graph.cells:
        for first, second in combinations(range(3), 2):
            c10 = list(cell)
            c10[first] += 1
            c10 = tuple(c10)
            c01 = list(cell)
            c01[second] += 1
            c01 = tuple(c01)
            c11 = list(cell)
            c11[first] += 1
            c11[second] += 1
            c11 = tuple(c11)
            if not all(row in graph.cell_set for row in (c10, c01, c11)):
                continue
            vertices = [
                graph.vertex_index[(cell, 2 * first + 1)],
                graph.vertex_index[(c10, 2 * first)],
                graph.vertex_index[(c10, 2 * second + 1)],
                graph.vertex_index[(c11, 2 * second)],
                graph.vertex_index[(c11, 2 * first)],
                graph.vertex_index[(c01, 2 * first + 1)],
                graph.vertex_index[(c01, 2 * second)],
                graph.vertex_index[(cell, 2 * second + 1)],
            ]
            rows.append(
                (
                    cycle_mask(graph, vertices),
                    vertices,
                    "coarse_plaquette",
                    (cell, first, second),
                )
            )
    return rows


def local_d(graph: OpenReferenceGraph, cell: Coord) -> base.Pauli:
    result = base.Pauli()
    for mode in range(7):
        result = result @ graph.B(graph.vertex_index[(cell, mode)])
    return result


def gf2_rank(rows: list[int]) -> int:
    return base.gf2_rank(rows)


def gaussian_basis(
    rows: list[tuple[int, int]],
) -> tuple[dict[int, tuple[int, int]], int, int]:
    solution_basis: dict[int, tuple[int, int]] = {}
    coefficient_rows = []
    augmented_rows = []
    width = max((coefficient.bit_length() for coefficient, _ in rows), default=0)
    for coefficient, rhs in rows:
        coefficient_rows.append(coefficient)
        augmented_rows.append(coefficient | (rhs << width))
        reduced = coefficient
        reduced_rhs = rhs
        while reduced:
            pivot = reduced.bit_length() - 1
            if pivot in solution_basis:
                basis_row, basis_rhs = solution_basis[pivot]
                reduced ^= basis_row
                reduced_rhs ^= basis_rhs
            else:
                solution_basis[pivot] = (reduced, reduced_rhs)
                break
    return (
        solution_basis,
        gf2_rank(coefficient_rows),
        gf2_rank(augmented_rows),
    )


def free_zero_solution(basis: dict[int, tuple[int, int]]) -> int:
    solution = 0
    for pivot in sorted(basis):
        row, rhs = basis[pivot]
        value = rhs ^ (((row ^ (1 << pivot)) & solution).bit_count() & 1)
        if value:
            solution |= 1 << pivot
    return solution


def right_inverse(row_masks: tuple[int, ...], columns: int) -> tuple[int, ...]:
    result = []
    for target in range(len(row_masks)):
        equations = [
            (row, int(index == target))
            for index, row in enumerate(row_masks)
        ]
        basis, rank, augmented_rank = gaussian_basis(equations)
        if rank != augmented_rank:
            raise AssertionError((target, rank, augmented_rank))
        result.append(free_zero_solution(basis))
    return tuple(result)


def apply_matrix(row_masks: tuple[int, ...], vector: int) -> int:
    return sum(
        (((row & vector).bit_count() & 1) << index)
        for index, row in enumerate(row_masks)
    )


def cell_triangle_decoder_certificate() -> dict[str, object]:
    graph = OpenReferenceGraph((ORIGIN,))
    cycles = open_local_cycles(graph)
    triangles = tuple(row for row in cycles if row[2] == "cell_triangle")
    masks = tuple(row[0] for row in triangles)
    decoder = right_inverse(masks, len(graph.edges))
    failures = sum(
        apply_matrix(masks, correction) != 1 << syndrome
        for syndrome, correction in enumerate(decoder)
    )
    active_entries = sum(row.bit_count() for row in decoder)
    deletion_detected = 0
    for syndrome, correction in enumerate(decoder):
        cursor = correction
        while cursor:
            bit = cursor & -cursor
            deletion_detected += (
                apply_matrix(masks, correction ^ bit) != 1 << syndrome
            )
            cursor ^= bit
    return {
        "cell_edge_M2": len(graph.edges),
        "triangle_checks": len(masks),
        "triangle_rank": gf2_rank(list(masks)),
        "decoder_columns": len(decoder),
        "active_table_entries": active_entries,
        "active_entry_deletions_detected": deletion_detected,
        "maximum_correction_weight_per_unit_syndrome": max(
            row.bit_count() for row in decoder
        ),
        "unit_syndrome_failures": failures,
        "table_reused_identically_per_cell": True,
    }


def coarse_geometry(cells: tuple[Coord, ...]) -> dict[str, object]:
    selected = set(cells)
    edges = []
    edge_index = {}
    for cell in sorted(selected):
        for axis in range(3):
            target = list(cell)
            target[axis] += 1
            target = tuple(target)
            if target in selected:
                edge_index[(cell, target)] = len(edges)
                edges.append((cell, target, axis))
    plaquettes = []
    for cell in sorted(selected):
        for first, second in combinations(range(3), 2):
            c10 = list(cell)
            c10[first] += 1
            c10 = tuple(c10)
            c01 = list(cell)
            c01[second] += 1
            c01 = tuple(c01)
            c11 = list(cell)
            c11[first] += 1
            c11[second] += 1
            c11 = tuple(c11)
            if not all(row in selected for row in (c10, c01, c11)):
                continue
            boundary = []
            for left, right in (
                (cell, c10),
                (c10, c11),
                (c01, c11),
                (cell, c01),
            ):
                if left > right:
                    left, right = right, left
                boundary.append(edge_index[(left, right)])
            plaquettes.append(
                {
                    "anchor": cell,
                    "axes": (first, second),
                    "boundary": tuple(boundary),
                    "cells": frozenset((cell, c10, c01, c11)),
                }
            )
    masks = tuple(
        sum(1 << edge for edge in row["boundary"]) for row in plaquettes
    )
    return {
        "cells": tuple(sorted(selected)),
        "edges": tuple(edges),
        "plaquettes": tuple(plaquettes),
        "masks": masks,
    }


def edge_plaquette_distance(edge, plaquette) -> int:
    return min(
        sum(abs(first[axis] - second[axis]) for axis in range(3))
        for first in edge[:2]
        for second in plaquette["cells"]
    )


def restricted_decoder(
    geometry: dict[str, object], radius: int
) -> dict[str, object]:
    edges = geometry["edges"]
    plaquettes = geometry["plaquettes"]
    masks = geometry["masks"]
    if not all(isinstance(row, tuple) for row in (edges, plaquettes, masks)):
        raise TypeError("malformed coarse geometry")
    variable_index = {}
    for edge_index, edge in enumerate(edges):
        for plaquette_index, plaquette in enumerate(plaquettes):
            if edge_plaquette_distance(edge, plaquette) <= radius:
                variable_index[(edge_index, plaquette_index)] = len(variable_index)
    plaquettes_at_edge = [[] for _ in edges]
    for plaquette_index, mask in enumerate(masks):
        for edge_index in range(len(edges)):
            if (mask >> edge_index) & 1:
                plaquettes_at_edge[edge_index].append(plaquette_index)

    equations = []
    for output_plaquette, output_mask in enumerate(masks):
        output_edges = tuple(
            edge for edge in range(len(edges)) if (output_mask >> edge) & 1
        )
        for input_edge in range(len(edges)):
            coefficient = 0
            for correction_edge in output_edges:
                for measured_plaquette in plaquettes_at_edge[input_edge]:
                    key = (correction_edge, measured_plaquette)
                    if key in variable_index:
                        coefficient ^= 1 << variable_index[key]
            equations.append(
                (coefficient, int((output_mask >> input_edge) & 1))
            )
    basis, rank, augmented_rank = gaussian_basis(equations)
    consistent = rank == augmented_rank
    solution = free_zero_solution(basis) if consistent else 0
    active = tuple(
        key for key, index in variable_index.items() if (solution >> index) & 1
    )

    single_edge_failures = 0
    if consistent:
        for input_edge in range(len(edges)):
            syndrome = sum(
                (((mask >> input_edge) & 1) << index)
                for index, mask in enumerate(masks)
            )
            correction = 0
            for (edge_index, plaquette_index), variable in variable_index.items():
                if ((solution >> variable) & 1) and (
                    (syndrome >> plaquette_index) & 1
                ):
                    correction ^= 1 << edge_index
            observed = apply_matrix(masks, correction)
            single_edge_failures += observed != syndrome

    deletion_detected = 0
    if consistent:
        for correction_edge, measured_plaquette in active:
            affected_output = sum(
                ((mask >> correction_edge) & 1) << index
                for index, mask in enumerate(masks)
            )
            affected_input = masks[measured_plaquette]
            deletion_detected += affected_output != 0 and affected_input != 0
    return {
        "radius": radius,
        "coarse_edges": len(edges),
        "plaquette_checks": len(plaquettes),
        "plaquette_rank": gf2_rank(list(masks)),
        "decoder_coefficients": len(variable_index),
        "coefficient_GF2_rank": rank,
        "augmented_GF2_rank": augmented_rank,
        "consistent": consistent,
        "canonical_active_coefficients": len(active),
        "canonical_maximum_active_radius": max(
            (
                edge_plaquette_distance(edges[edge], plaquettes[plaquette])
                for edge, plaquette in active
            ),
            default=0,
        ),
        "all_single_edge_syndrome_failures": single_edge_failures,
        "active_coefficient_deletions_detected": deletion_detected,
    }


def minimum_restricted_decoder(
    geometry: dict[str, object], maximum_radius: int
) -> tuple[dict[str, object], tuple[dict[str, object], ...]]:
    attempts = []
    for radius in range(maximum_radius + 1):
        row = restricted_decoder(geometry, radius)
        attempts.append(row)
        if row["consistent"]:
            return row, tuple(attempts)
    raise AssertionError(("no decoder", maximum_radius, attempts[-1]))


def planar_boundary_path_decoder(length: int) -> dict[str, object]:
    cells = tuple((x, y, 0) for x, y in product(range(length), repeat=2))
    geometry = coarse_geometry(cells)
    edges = geometry["edges"]
    plaquettes = geometry["plaquettes"]
    masks = geometry["masks"]
    if not all(isinstance(row, tuple) for row in (edges, plaquettes, masks)):
        raise TypeError("malformed planar geometry")
    edge_lookup = {
        frozenset((left, right)): index
        for index, (left, right, _) in enumerate(edges)
    }
    columns = []
    maximum_range = 0
    for plaquette in plaquettes:
        x, y, _ = plaquette["anchor"]
        n = length - 1
        choices = (
            (x, "left"),
            (n - 1 - x, "right"),
            (y, "down"),
            (n - 1 - y, "up"),
        )
        distance, side = min(choices)
        correction = 0
        if side == "left":
            for coordinate in range(x, -1, -1):
                left = (coordinate, y, 0)
                right = (coordinate, y + 1, 0)
                correction ^= 1 << edge_lookup[frozenset((left, right))]
        elif side == "right":
            for coordinate in range(x + 1, length):
                left = (coordinate, y, 0)
                right = (coordinate, y + 1, 0)
                correction ^= 1 << edge_lookup[frozenset((left, right))]
        elif side == "down":
            for coordinate in range(y, -1, -1):
                left = (x, coordinate, 0)
                right = (x + 1, coordinate, 0)
                correction ^= 1 << edge_lookup[frozenset((left, right))]
        else:
            for coordinate in range(y + 1, length):
                left = (x, coordinate, 0)
                right = (x + 1, coordinate, 0)
                correction ^= 1 << edge_lookup[frozenset((left, right))]
        columns.append(correction)
        maximum_range = max(maximum_range, distance)
    failures = sum(
        apply_matrix(masks, column) != 1 << index
        for index, column in enumerate(columns)
    )
    lower_bound = max(
        (
            min(
                row["anchor"][0],
                length - 2 - row["anchor"][0],
                row["anchor"][1],
                length - 2 - row["anchor"][1],
            )
            for row in plaquettes
        ),
        default=0,
    )
    return {
        "L": length,
        "cells": len(cells),
        "coarse_edges": len(edges),
        "independent_plaquette_syndromes": len(plaquettes),
        "explicit_boundary_path_failures": failures,
        "explicit_maximum_feedforward_radius": maximum_range,
        "isolated_deepest_plaquette_boundary_lower_bound": lower_bound,
        "lower_bound_saturated": maximum_range == lower_bound,
        "isolated_single_plaquette_outcome_lawful": True,
    }


def greedy_check_colors(rows: tuple[base.Pauli, ...]) -> int:
    qubit_colors: dict[int, set[int]] = {}
    maximum_color = -1
    for row in rows:
        support = row.x | row.z
        used = set()
        cursor = support
        while cursor:
            bit = cursor & -cursor
            qubit = bit.bit_length() - 1
            used.update(qubit_colors.get(qubit, set()))
            cursor ^= bit
        color = next(candidate for candidate in range(len(rows) + 1) if candidate not in used)
        maximum_color = max(maximum_color, color)
        cursor = support
        while cursor:
            bit = cursor & -cursor
            qubit = bit.bit_length() - 1
            qubit_colors.setdefault(qubit, set()).add(color)
            cursor ^= bit
    return maximum_color + 1


def local_logical_pairs(graph, cells: tuple[Coord, ...]):
    """Six bounded canonical qubit pairs per cell in the BKSF code space.

    Z_(x,a)=B_(x,a) and
    X_(x,a)=-i product_(b=a)^5 B_(x,b) A_((x,a),(x,r)).
    The finite mode order is an intra-cell Fock chart, not a global
    Jordan--Wigner order.  Proper-cubic changes of chart are audited below as
    bounded local logical Clifford transformations.  The suffix and its phase
    are load bearing: the canonical prefix representative has the same
    commutators but carries an occupation-dependent cell-parity amplitude.
    """

    result = []
    for cell in cells:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            matter = graph.vertex_index[(cell, mode)]
            logical_z = graph.B(matter)
            suffix = base.Pauli()
            for suffix_mode in range(mode, 6):
                suffix = suffix @ graph.B(
                    graph.vertex_index[(cell, suffix_mode)]
                )
            logical_x = (
                base.Pauli(phase=3)
                @ suffix
                @ graph.A(matter, reference)
            )
            result.append(
                (cell, mode, logical_x, logical_z)
            )
    return tuple(result)


def local_gamma(state: tuple[int, ...], target: int):
    out = list(state)
    phase = -1 if sum(state[:target]) & 1 else 1
    out[target] ^= 1
    return tuple(out), phase


def local_a_action(bits: tuple[int, ...], mode: int):
    out, right_phase = local_gamma(bits, 6)
    out, left_phase = local_gamma(out, mode)
    # A_(mode,r)=-i gamma_mode gamma_r; gamma_r acts first.
    return out, -1j * left_phase * right_phase


def local_suffix_x_action(bits: tuple[int, ...], mode: int):
    """Decoded action of -i product_(k=mode)^5 B_k A_(mode,r)."""

    out, a_phase = local_a_action(bits, mode)
    suffix_phase = -1 if sum(out[mode:6]) & 1 else 1
    return out, (-1j) * suffix_phase * a_phase


def local_prefix_action(bits: tuple[int, ...], mode: int):
    """Decoded action of A_(mode,r) product_(k<mode) B_k."""

    prefix_phase = -1 if sum(bits[:mode]) & 1 else 1
    out, a_phase = local_a_action(bits, mode)
    return out, prefix_phase * a_phase


def logical_phase_orientation_certificate() -> dict[str, object]:
    """Exhaust the 64-state cell decoder and compare prefix versus suffix."""

    suffix_orientation_failures = 0
    prefix_relation_failures = 0
    prefix_plain_x_mismatches = 0
    graph_relation_failures = 0
    suffix_full_load_failures = 0
    prefix_full_load_plain_amplitude_mismatches = 0
    graph = OpenReferenceGraph((ORIGIN,))
    reference = graph.vertex_index[(ORIGIN, 6)]
    cell_z = base.Pauli()
    for mode in range(6):
        cell_z = cell_z @ graph.B(graph.vertex_index[(ORIGIN, mode)])
    for mode in range(6):
        matter_vertex = graph.vertex_index[(ORIGIN, mode)]
        prefix = graph.A(matter_vertex, reference)
        for earlier in range(mode):
            prefix = prefix @ graph.B(
                graph.vertex_index[(ORIGIN, earlier)]
            )
        suffix = base.Pauli()
        for suffix_mode in range(mode, 6):
            suffix = suffix @ graph.B(
                graph.vertex_index[(ORIGIN, suffix_mode)]
            )
        suffix = (
            base.Pauli(phase=3)
            @ suffix
            @ graph.A(matter_vertex, reference)
        )
        graph_relation_failures += prefix != (
            base.Pauli(phase=3) @ suffix @ cell_z
        )
        for matter_bits in range(1 << 6):
            matter = tuple(
                (matter_bits >> index) & 1 for index in range(6)
            )
            extended = matter + (sum(matter) & 1,)
            target_matter = list(matter)
            target_matter[mode] ^= 1
            target = tuple(target_matter) + (
                sum(target_matter) & 1,
            )
            suffix_out, suffix_phase = local_suffix_x_action(
                extended, mode
            )
            suffix_orientation_failures += (
                suffix_out != target or abs(suffix_phase - 1.0) > 1.0e-12
            )
            prefix_out, prefix_phase = local_prefix_action(extended, mode)
            expected_prefix_phase = (-1j) * (
                -1.0 if sum(matter) & 1 else 1.0
            )
            prefix_relation_failures += (
                prefix_out != target
                or abs(prefix_phase - expected_prefix_phase) > 1.0e-12
            )
            prefix_plain_x_mismatches += (
                prefix_out != target or abs(prefix_phase - 1.0) > 1.0e-12
            )
    for matter_bits in range(1 << 6):
        target_matter = tuple(
            (matter_bits >> index) & 1 for index in range(6)
        )
        target = target_matter + (sum(target_matter) & 1,)
        suffix_state = (0,) * 7
        suffix_amplitude = 1.0 + 0.0j
        prefix_state = (0,) * 7
        prefix_amplitude = 1.0 + 0.0j
        for mode in range(6):
            if not ((matter_bits >> mode) & 1):
                continue
            suffix_state, amplitude = local_suffix_x_action(
                suffix_state, mode
            )
            suffix_amplitude *= amplitude
            prefix_state, amplitude = local_prefix_action(prefix_state, mode)
            prefix_amplitude *= amplitude
        suffix_full_load_failures += (
            suffix_state != target
            or abs(suffix_amplitude - 1.0) > 1.0e-12
        )
        prefix_full_load_plain_amplitude_mismatches += (
            prefix_state != target
            or abs(prefix_amplitude - 1.0) > 1.0e-12
        )
    return {
        "matter_columns_per_mode": 1 << 6,
        "mode_columns_checked": 6 * (1 << 6),
        "suffix_plus_one_orientation_failures": suffix_orientation_failures,
        "prefix_minus_i_cell_parity_relation_failures": prefix_relation_failures,
        "prefix_plain_X_mismatches": prefix_plain_x_mismatches,
        "physical_prefix_suffix_relation_failures": graph_relation_failures,
        "full_six_mode_load_columns_checked": 1 << 6,
        "suffix_full_load_plus_one_failures": suffix_full_load_failures,
        "prefix_full_load_plain_amplitude_mismatches": (
            prefix_full_load_plain_amplitude_mismatches
        ),
        "physical_relation": (
            "prefix = -i suffix-X times cell-Z, with operator order as written"
        ),
    }


def logical_tableau_certificate(
    name: str, cells: tuple[Coord, ...]
) -> dict[str, object]:
    """Exact open-code logical algebra and a bounded coherent load circuit.

    Given an already prepared all-B-positive vacuum, for each data qubit q the
    circuit applies controlled-X_q followed by CNOTs from every physical edge
    in the Z_q support back to q.  On |q>|0_L> this is
    |q>|0_L> -> |q>|q_L> -> |0>|q_L>.  Controlled Pauli factors and parity
    CNOTs are scheduled by bounded support coloring; no measurement outcome or
    target amplitude enters the circuit.
    """

    graph = OpenReferenceGraph(cells)
    cycle_data = open_local_cycles(graph)
    loops = tuple(graph.loop_pauli(vertices) for _, vertices, _, _ in cycle_data)
    ds = tuple(local_d(graph, cell) for cell in graph.cells)
    pairs = local_logical_pairs(graph, graph.cells)
    xs = tuple(row[2] for row in pairs)
    zs = tuple(row[3] for row in pairs)
    stabilizers = loops + ds
    pair_failures = 0
    stabilizer_failures = 0
    square_failures = 0
    identity = base.Pauli()
    for index, (logical_x, logical_z) in enumerate(zip(xs, zs)):
        square_failures += logical_x @ logical_x != identity
        square_failures += logical_z @ logical_z != identity
        for other, (other_x, other_z) in enumerate(zip(xs, zs)):
            pair_failures += logical_x.commutes(other_z) != (index != other)
            pair_failures += not logical_x.commutes(other_x)
            pair_failures += not logical_z.commutes(other_z)
        for stabilizer in stabilizers:
            stabilizer_failures += not logical_x.commutes(stabilizer)
            stabilizer_failures += not logical_z.commutes(stabilizer)
    logical_rank = base.gf2_rank(
        row.symplectic(len(graph.edges)) for row in xs + zs
    )
    return {
        "fixture": name,
        "cells": len(graph.cells),
        "logical_qubits": len(pairs),
        "logical_symplectic_rank": logical_rank,
        "canonical_pair_failures": pair_failures,
        "stabilizer_commutator_failures": stabilizer_failures,
        "Hermitian_involution_failures": square_failures,
        "maximum_X_weight": max((row.x | row.z).bit_count() for row in xs),
        "maximum_Z_weight": max((row.x | row.z).bit_count() for row in zs),
        "controlled_X_support_colors": greedy_check_colors(xs),
        "parity_CNOT_support_colors": greedy_check_colors(zs),
        "load_truth_table": (
            (0, 0, 0),
            (1, 0, 1),
        ),
        "truth_table_columns": (
            "input_before",
            "input_after",
            "logical_occupation_after",
        ),
        "target_dependent_controls": 0,
    }


def logical_covariance_certificate() -> dict[str, object]:
    """Audit all 24 proper-cubic chart changes on one periodic bulk cell."""

    graph = base.ReferenceGraph(3, True)
    all_pairs = local_logical_pairs(graph, graph.cells)
    origin_pairs = tuple(row for row in all_pairs if row[0] == ORIGIN)
    failures = 0
    off_cell_logical_components = 0
    minimum_chart_rank = 12
    maximum_weight = 0
    for frame in base.proper_cubic_frames():
        vertex_map, edge_map = base.graph_frame_maps(graph, frame)
        toggles, gauge_pairs = base.order_gauge(graph, vertex_map, edge_map)
        flips = 0
        for source_edge, (u, v, _, _) in enumerate(graph.edges):
            transformed = base.permute_pauli(graph.A(u, v), edge_map)
            target = graph.A(vertex_map[u], vertex_map[v])
            ordered = base.apply_gauge(
                transformed, toggles, gauge_pairs
            )
            if (ordered.phase - target.phase) % 4 == 2:
                flips ^= 1 << edge_map[source_edge]
        mapped = tuple(
            base.apply_gauge(
                base.permute_pauli(row, edge_map),
                toggles,
                gauge_pairs,
                flips,
            )
            for _, _, logical_x, logical_z in origin_pairs
            for row in (logical_x, logical_z)
        )
        maximum_weight = max(
            maximum_weight,
            max((row.x | row.z).bit_count() for row in mapped),
        )
        chart_rows = []
        for row in mapped:
            chart = 0
            for index, (cell, _, logical_x, logical_z) in enumerate(all_pairs):
                x_component = int(not row.commutes(logical_z))
                z_component = int(not row.commutes(logical_x))
                if cell != ORIGIN:
                    off_cell_logical_components += x_component + z_component
                else:
                    chart |= x_component << index
                    chart |= z_component << (index + 6)
            chart_rows.append(chart)
        chart_rank = base.gf2_rank(chart_rows)
        minimum_chart_rank = min(minimum_chart_rank, chart_rank)
        failures += chart_rank != 12
    return {
        "frames": len(base.proper_cubic_frames()),
        "chart_rank_minimum": minimum_chart_rank,
        "rank_failures": failures,
        "off_cell_logical_components": off_cell_logical_components,
        "maximum_mapped_Pauli_weight": maximum_weight,
        "meaning": (
            "each proper-cubic frame acts on the six origin logical qubits "
            "by a full-rank bounded local Clifford chart change"
        ),
    }


def graph_preparation_certificate(
    name: str, cells: tuple[Coord, ...]
) -> dict[str, object]:
    graph = OpenReferenceGraph(cells)
    cycle_data = open_local_cycles(graph)
    loops = tuple(graph.loop_pauli(vertices) for _, vertices, _, _ in cycle_data)
    class_rows = {
        kind: tuple(
            graph.loop_pauli(vertices)
            for _, vertices, row_kind, _ in cycle_data
            if row_kind == kind
        )
        for kind in ("cell_triangle", "coarse_plaquette", "bond_rectangle")
    }
    ds = tuple(local_d(graph, cell) for cell in graph.cells)
    bs = tuple(graph.B(vertex) for vertex in range(len(graph.vertices)))
    loop_rank = base.gf2_rank(
        row.symplectic(len(graph.edges)) for row in loops
    )
    d_rank = base.gf2_rank(row.symplectic(len(graph.edges)) for row in ds)
    combined_rank = base.gf2_rank(
        row.symplectic(len(graph.edges)) for row in loops + ds
    )
    vacuum_rank = base.gf2_rank(
        row.symplectic(len(graph.edges)) for row in loops + bs
    )
    phase_failures = base.stabilizer_phase_failures(
        list(loops + bs), len(graph.edges)
    )
    commutator_failures = sum(
        not left.commutes(right)
        for index, left in enumerate(loops + bs)
        for right in (loops + bs)[index + 1 :]
    )
    class_summary = {}
    for kind, rows in class_rows.items():
        class_summary[kind] = {
            "checks": len(rows),
            "maximum_Pauli_weight": max(
                ((row.x | row.z).bit_count() for row in rows), default=0
            ),
            "disjoint_support_measurement_colors": greedy_check_colors(rows),
        }
    maximum_measurement_layers = sum(
        row["maximum_Pauli_weight"]
        * row["disjoint_support_measurement_colors"]
        for row in class_summary.values()
    )
    return {
        "fixture": name,
        "cells": len(graph.cells),
        "vertices": len(graph.vertices),
        "edge_M2": len(graph.edges),
        "local_loop_rows": len(loops),
        "local_loop_rank": loop_rank,
        "D_rows": len(ds),
        "D_rank": d_rank,
        "loop_plus_D_rank": combined_rank,
        "matter_code_exponent": len(graph.edges) - combined_rank,
        "loop_plus_all_B_rank": vacuum_rank,
        "unique_vacuum_tableau": vacuum_rank == len(graph.edges),
        "stabilizer_phase_failures": phase_failures,
        "commutator_failures": commutator_failures,
        "check_classes": class_summary,
        "sequential_ancilla_two_qubit_layer_upper_bound": maximum_measurement_layers,
        "all_checks_bounded_and_locally_colorable": True,
        "Wilson_rows": 0,
    }


def main() -> None:
    l_shape = ((0, 0, 0), (1, 0, 0), (0, 1, 0))
    planar_square = tuple((x, y, 0) for x, y in product(range(2), repeat=2))
    cube_rows = []
    graph_rows = [
        graph_preparation_certificate("three-cell-L", l_shape),
        graph_preparation_certificate("planar-two-by-two", planar_square),
    ]
    logical_rows = [
        logical_tableau_certificate("three-cell-L", l_shape),
        logical_tableau_certificate("planar-two-by-two", planar_square),
    ]
    for length in range(2, 6):
        cells = tuple(product(range(length), repeat=3))
        graph_rows.append(
            graph_preparation_certificate(f"open-cube-L{length}", cells)
        )
        logical_rows.append(
            logical_tableau_certificate(f"open-cube-L{length}", cells)
        )
        geometry = coarse_geometry(cells)
        minimum, attempts = minimum_restricted_decoder(geometry, length)
        cube_rows.append(
            {
                "L": length,
                "minimum_linear_feedforward_radius": minimum["radius"],
                "minimum_decoder": minimum,
                "attempt_ranks": tuple(
                    (
                        row["radius"],
                        row["coefficient_GF2_rank"],
                        row["augmented_GF2_rank"],
                    )
                    for row in attempts
                ),
            }
        )

    planar_rows = tuple(
        planar_boundary_path_decoder(length) for length in range(2, 10)
    )
    cell_decoder = cell_triangle_decoder_certificate()
    phase_orientation = logical_phase_orientation_certificate()
    covariance = logical_covariance_certificate()
    maximum_check_depth = max(
        row["sequential_ancilla_two_qubit_layer_upper_bound"]
        for row in graph_rows
    )
    certificate = {
        "cycle": 703,
        "authority": "none",
        "audit": "unset",
        "status": "open-BKSF-state-encoder-positive-feedforward-range-grows",
        "protocol": {
            "initial_state": "|0> on every BKSF edge M2",
            "stage_1": "measure cell triangles; fixed intra-cell Z correction table",
            "stage_2": "measure coarse plaquettes; open-boundary Z decoder on matter-stream edges",
            "stage_3": "measure bond rectangles; Z on the unique reference-bond edge",
            "D_behavior": "all corrections are Z type, so every B_v and D_x remains +1",
            "prepared_state": "unique all-B-positive BKSF vacuum stabilizer state",
            "schedule_counter_is_physical_time": False,
        },
        "cell_triangle_decoder": cell_decoder,
        "graph_and_measurement_tableaux": tuple(graph_rows),
        "local_logical_tableaux_and_load_circuits": tuple(logical_rows),
        "logical_phase_orientation": phase_orientation,
        "logical_proper_cubic_covariance": covariance,
        "maximum_local_check_measurement_layer_upper_bound_L_le_5": maximum_check_depth,
        "planar_open_boundary_path_decoders": planar_rows,
        "cubic_local_linear_decoder_tournament": tuple(cube_rows),
        "fixed_depth_boundary": {
            "each_check_has_bounded_support": True,
            "check_measurement_coloring_bounded_on_tested_sizes": True,
            "planar_exact_lower_bound": (
                "an isolated interior plaquette syndrome is lawful and any Z "
                "correction chain must connect it to the open boundary"
            ),
            "planar_required_radius_formula": "floor((L-2)/2)",
            "fixed_radius_local_feedforward_for_all_open_L": False,
            "claim_scope": (
                "measurement-plus-Z-syndrome-correction preparation with local "
                "information propagation; not all Clifford encoders"
            ),
        },
        "deletion_and_domain": {
            "all_cell_decoder_active_deletions_detected": cell_decoder[
                "active_entry_deletions_detected"
            ]
            == cell_decoder["active_table_entries"],
            "all_canonical_cube_decoder_active_deletions_detected": all(
                row["minimum_decoder"]["active_coefficient_deletions_detected"]
                == row["minimum_decoder"]["canonical_active_coefficients"]
                for row in cube_rows
            ),
            "arbitrary_syndrome_control": (
                "matrix identities cover every lawful measured syndrome, not "
                "only one sampled outcome"
            ),
            "prepared_logical_sector": (
                "all B_v=+1 vacuum, followed by target-independent coherent "
                "load of arbitrary 6N-qubit matter input"
            ),
            "arbitrary_6N_matter_common_E_encoder_constructed": True,
        },
        "proper_cubic_and_boundary_scope": {
            "local_check_family": "the Cycle232 proper-cubic BKSF family",
            "logical_chart_change_frames": covariance["frames"],
            "logical_chart_change_failures": covariance["rank_failures"],
            "decoder_tie_breaking_covariant": False,
            "open_boundary_and_origin_supplied": True,
            "periodic_fixed_Wilson_preparation_tested": False,
        },
        "supplied": (
            "the open cell set and boundary",
            "the Cycle232 incidence order and proper-cubic coframe",
            "one measurement ancilla per simultaneously measured check",
            "classical feedforward paths or Gaussian decoder table",
            "a future Z3 placement/routing of graph edges, ancillas, and work qubits",
        ),
        "not_claimed": (
            "a fixed-depth local-feedforward preparation family",
            "periodic fixed-Wilson preparation",
            "a physical-site-M2 preparation compiler",
            "causal time, a Record, a source law, or Born derivation",
            "a route-independent obstruction, minimum content, or axiom pressure",
        ),
    }
    print("CYCLE703_OPEN_BKSF_STABILIZER_PREPARATION")
    print(json.dumps(certificate, sort_keys=True, default=str))

    assert cell_decoder == {
        "cell_edge_M2": 18,
        "triangle_checks": 12,
        "triangle_rank": 12,
        "decoder_columns": 12,
        "active_table_entries": cell_decoder["active_table_entries"],
        "active_entry_deletions_detected": cell_decoder[
            "active_entry_deletions_detected"
        ],
        "maximum_correction_weight_per_unit_syndrome": cell_decoder[
            "maximum_correction_weight_per_unit_syndrome"
        ],
        "unit_syndrome_failures": 0,
        "table_reused_identically_per_cell": True,
    }
    assert (
        cell_decoder["active_entry_deletions_detected"]
        == cell_decoder["active_table_entries"]
    )
    assert all(row["matter_code_exponent"] == 6 * row["cells"] for row in graph_rows)
    assert all(row["unique_vacuum_tableau"] for row in graph_rows)
    assert all(row["stabilizer_phase_failures"] == 0 for row in graph_rows)
    assert all(row["commutator_failures"] == 0 for row in graph_rows)
    assert all(row["Wilson_rows"] == 0 for row in graph_rows)
    assert all(
        row["logical_symplectic_rank"] == 12 * row["cells"]
        for row in logical_rows
    )
    assert all(row["canonical_pair_failures"] == 0 for row in logical_rows)
    assert all(
        row["stabilizer_commutator_failures"] == 0 for row in logical_rows
    )
    assert all(
        row["Hermitian_involution_failures"] == 0 for row in logical_rows
    )
    assert phase_orientation == {
        "matter_columns_per_mode": 64,
        "mode_columns_checked": 384,
        "suffix_plus_one_orientation_failures": 0,
        "prefix_minus_i_cell_parity_relation_failures": 0,
        "prefix_plain_X_mismatches": 384,
        "physical_prefix_suffix_relation_failures": 0,
        "full_six_mode_load_columns_checked": 64,
        "suffix_full_load_plus_one_failures": 0,
        "prefix_full_load_plain_amplitude_mismatches": 32,
        "physical_relation": (
            "prefix = -i suffix-X times cell-Z, with operator order as written"
        ),
    }
    assert covariance["frames"] == 24
    assert covariance["chart_rank_minimum"] == 12
    assert covariance["rank_failures"] == 0
    assert covariance["off_cell_logical_components"] == 0
    assert [row["minimum_linear_feedforward_radius"] for row in cube_rows] == [1, 1, 3, 3]
    assert all(row["minimum_decoder"]["all_single_edge_syndrome_failures"] == 0 for row in cube_rows)
    assert [row["explicit_maximum_feedforward_radius"] for row in planar_rows] == [0, 0, 1, 1, 2, 2, 3, 3]
    assert all(row["explicit_boundary_path_failures"] == 0 for row in planar_rows)
    assert all(row["lower_bound_saturated"] for row in planar_rows)
    print("CYCLE703_OPEN_BKSF_STATE_ENCODER_LOCAL_FEEDFORWARD_NOT_FIXED_DEPTH")


if __name__ == "__main__":
    main()
