#!/usr/bin/env python3
"""Cycle-797 core for companion plaquette-center coordinates.

This module reconstructs elementary auxiliary-Majorana plaquette centers,
their independent logical even-CAR coordinates, and lawful edge coboundaries.
It contains no pump verdict and no host-side schedule.
"""

from __future__ import annotations

import frontier_cycle720_cell_majorana_companion_geometry_2026_07_27 as M
import frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27 as F


def rank(rows) -> int:
    pivots = {}
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


def solve(equations, variables):
    rows = [[mask, rhs & 1] for mask, rhs in equations]
    pivots = {}
    cursor = 0
    for column in range(variables):
        pivot = next(
            (item for item in range(cursor, len(rows))
             if (rows[item][0] >> column) & 1),
            None,
        )
        if pivot is None:
            continue
        rows[cursor], rows[pivot] = rows[pivot], rows[cursor]
        for other in range(len(rows)):
            if other != cursor and ((rows[other][0] >> column) & 1):
                rows[other][0] ^= rows[cursor][0]
                rows[other][1] ^= rows[cursor][1]
        pivots[column] = cursor
        cursor += 1
    if any(mask == 0 and rhs for mask, rhs in rows):
        return None
    return sum(rows[row][1] << column for column, row in pivots.items())


def cell_distance(fixture, left, right) -> int:
    return sum(
        abs(a - b)
        for a, b in zip(fixture.cells[left], fixture.cells[right])
    )


def geometry(fixture):
    index = {cell: item for item, cell in enumerate(fixture.cells)}
    links = {}
    edge_index = {}
    for edge, (left, right, owner, axis, *_rest) in enumerate(fixture.edges):
        links[(owner, axis)] = (
            fixture.companion_eta(left, 2 * axis + 1)
            @ fixture.companion_eta(right, 2 * axis)
        )
        edge_index[(owner, axis)] = edge
    plaquettes = []
    for cell in fixture.cells:
        for first in range(3):
            for second in range(first + 1, 3):
                step_first = tuple(
                    cell[d] + int(d == first) for d in range(3)
                )
                step_second = tuple(
                    cell[d] + int(d == second) for d in range(3)
                )
                corner = tuple(
                    cell[d] + int(d in (first, second)) for d in range(3)
                )
                if not all(
                    item in index
                    for item in (step_first, step_second, corner)
                ):
                    continue
                boundary = (
                    (cell, first),
                    (step_first, second),
                    (step_second, first),
                    (cell, second),
                )
                row = M.Pauli()
                for key in boundary:
                    row = row @ links[key]
                plaquettes.append((cell, first, second, boundary, row))
    return edge_index, tuple(plaquettes)


def logical_rows(fixture):
    rows = M.operator_rows(fixture)
    physical = tuple(
        row[1].symplectic(fixture.qubits) for row in rows
    )
    target = tuple(
        row[2].symplectic(fixture.matter_qubits) for row in rows
    )
    paired = F.independent_paired_basis(physical, target)
    _radicals, pairs = F.symplectic_split_paired(
        paired, fixture.qubits
    )
    return tuple(row[0] for pair in pairs for row in pair)


def coboundary(edge_index, plaquettes, edge_word):
    return sum(
        (
            sum(
                (edge_word >> edge_index[edge]) & 1
                for edge in boundary
            )
            & 1
        )
        << index
        for index, (_cell, _first, _second, boundary, _row)
        in enumerate(plaquettes)
    )
