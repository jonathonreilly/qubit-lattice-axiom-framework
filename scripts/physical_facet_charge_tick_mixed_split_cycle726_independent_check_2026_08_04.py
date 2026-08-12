"""Independent exact checks for Cycle 726.

This checker never imports or executes the primary runner.  It parses only the
primary's carried certificate and witness literals, then reconstructs the geometry
with separate exact algorithms.  In three dimensions it enumerates six-cliques
of pairwise interior-disjoint unit tetrahedra, rather than using the primary's
sample-cover recursion.  In four dimensions it verifies the lower certificate by
exact Cramer barycentric tests and the attaining witness by an integer separator
sweep.
"""

import ast
import sys
from collections import Counter, defaultdict
from itertools import combinations, product
from pathlib import Path

import numpy as np


AUDIT_TIMEOUT_SEC = 90
AUDIT_INPUT_PATHS = (
    "scripts/physical_facet_charge_tick_mixed_split_cycle726_2026_08_04.py",
)

GATES = []


def gate(name, ok, detail=""):
    """Record and print one deterministic check."""
    GATES.append((name, bool(ok)))
    print(
        "{0} {1:48s} {2}".format("PASS" if ok else "FAIL", name, detail),
        flush=True,
    )


def determinant(matrix):
    """Exact recursive determinant for matrices of order at most four."""
    if len(matrix) == 1:
        return matrix[0][0]
    return sum(
        (-1) ** j
        * matrix[0][j]
        * determinant([row[:j] + row[j + 1 :] for row in matrix[1:]])
        for j in range(len(matrix))
    )


def decode(text, width, offset):
    """Decode the primary's base-26 integer-vector representation."""
    values = []
    for start in range(0, len(text), width):
        value = 0
        for char in text[start : start + width]:
            value = 26 * value + ord(char) - 97
        values.append(value - offset)
    return values


def carried_literals():
    """Read only the carried certificate/witness literals from the primary AST."""
    tree = ast.parse(Path(AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8"))
    wanted = {"CIDX", "CVAL", "WIT"}
    found = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if isinstance(target, ast.Name) and target.id in wanted:
            found[target.id] = ast.literal_eval(node.value)
    return found


LITERALS = carried_literals()
CORNERS4 = [tuple((number >> (3 - axis)) & 1 for axis in range(4)) for number in range(16)]


def volume4(cell):
    """Normalized four-volume of one five-corner cell."""
    base = CORNERS4[cell[0]]
    edges = [
        [CORNERS4[vertex][axis] - base[axis] for axis in range(4)]
        for vertex in cell[1:]
    ]
    return abs(determinant(edges))


def facet_charge(cell):
    """Recompute the supplied facet charge directly from corner pairs."""
    charge = 0
    for normal in range(4):
        for bit in (0, 1):
            face = [vertex for vertex in cell if CORNERS4[vertex][normal] == bit]
            if len(face) != 4:
                continue
            charged_axes = [axis for axis in range(3) if axis != normal]
            charge += sum(
                sum(
                    abs(CORNERS4[left][axis] - CORNERS4[right][axis])
                    for axis in charged_axes
                )
                > 1
                for left, right in combinations(face, 2)
            )
    return charge


CELLS4 = [cell for cell in combinations(range(16), 5) if volume4(cell) == 1]
CHARGE4 = [facet_charge(cell) for cell in CELLS4]
gate("independent minimal-cell census", len(CELLS4) == 2672, "cells {0}".format(len(CELLS4)))

SAMPLE_WEIGHTS = [7, 31, 131, 613, 2801]
SAMPLE_SCALE = sum(SAMPLE_WEIGHTS)
SAMPLES4 = sorted(
    {
        tuple(
            sum(SAMPLE_WEIGHTS[i] * CORNERS4[vertex][axis] for i, vertex in enumerate(cell))
            for axis in range(4)
        )
        for cell in CELLS4
    }
)


def unimodular_inverse(matrix):
    """Return the exact integer inverse of a determinant-plus/minus-one matrix."""
    divisor = determinant(matrix)
    return [
        [
            ((-1) ** (row + column))
            * determinant(
                [
                    source[:row] + source[row + 1 :]
                    for source_index, source in enumerate(matrix)
                    if source_index != column
                ]
            )
            // divisor
            for column in range(4)
        ]
        for row in range(4)
    ]


certificate_indices = decode(LITERALS["CIDX"], 3, 0)
certificate_values = decode(LITERALS["CVAL"], 2, 22)
certificate = dict(zip(certificate_indices, certificate_values))
support_points = np.array([SAMPLES4[index] for index in certificate_indices], dtype=np.int64)
support_values = np.array(certificate_values, dtype=np.int64)
slacks = []
for cell, charge in zip(CELLS4, CHARGE4):
    base = CORNERS4[cell[0]]
    edges = [
        [CORNERS4[vertex][axis] - base[axis] for axis in range(4)]
        for vertex in cell[1:]
    ]
    inverse = np.array(unimodular_inverse(edges), dtype=np.int64)
    displacements = support_points - SAMPLE_SCALE * np.array(base, dtype=np.int64)
    numerators = displacements @ inverse
    interior = (numerators > 0).all(axis=1) & (SAMPLE_SCALE - numerators.sum(axis=1) > 0)
    load = int(support_values @ interior.astype(np.int64))
    slacks.append(2 * charge - load)
gate(
    "independent denominator-two certificate",
    len(SAMPLES4) == 2672
    and len(certificate) == 411
    and sum(certificate.values()) == 170
    and min(slacks) == 0,
    "samples {0}, support {1}, weight {2}, least slack {3}".format(
        len(SAMPLES4), len(certificate), sum(certificate.values()), min(slacks)
    ),
)


def decode_witness(text):
    """Decode a carried twenty-four-cell witness."""
    return [
        tuple(sorted(ord(char) - 97 for char in text[start : start + 5]))
        for start in range(0, len(text), 5)
    ]


DIRECTIONS4 = [direction for direction in product(range(-4, 5), repeat=4) if any(direction)]


def disjoint4(left, right):
    """Decide disjoint interiors by a complete bounded integer separator sweep."""
    for direction in DIRECTIONS4:
        project_left = [
            sum(direction[axis] * CORNERS4[vertex][axis] for axis in range(4))
            for vertex in left
        ]
        project_right = [
            sum(direction[axis] * CORNERS4[vertex][axis] for axis in range(4))
            for vertex in right
        ]
        if max(project_left) <= min(project_right) or max(project_right) <= min(project_left):
            return True
    return False


witness1 = decode_witness(LITERALS["WIT"]["W1"])
cell_positions = {cell: index for index, cell in enumerate(CELLS4)}
witness1_indices = [cell_positions[cell] for cell in witness1]
gate(
    "independent attaining witness",
    len(set(witness1)) == 24
    and sum(CHARGE4[index] for index in witness1_indices) == 85
    and all(disjoint4(left, right) for left, right in combinations(witness1, 2)),
    "pieces 24, normalized volume 24, facet charge 85",
)

# Independent three-dimensional route: enumerate compatibility six-cliques.
CORNERS3 = [tuple((number >> (2 - axis)) & 1 for axis in range(3)) for number in range(8)]


def volume3(cell):
    base = CORNERS3[cell[0]]
    return abs(
        determinant(
            [
                [CORNERS3[vertex][axis] - base[axis] for axis in range(3)]
                for vertex in cell[1:]
            ]
        )
    )


TETS = [cell for cell in combinations(range(8), 4) if volume3(cell) == 1]
DIRECTIONS3 = [direction for direction in product(range(-2, 3), repeat=3) if any(direction)]


def disjoint3(left, right):
    for direction in DIRECTIONS3:
        project_left = [
            sum(direction[axis] * CORNERS3[vertex][axis] for axis in range(3))
            for vertex in left
        ]
        project_right = [
            sum(direction[axis] * CORNERS3[vertex][axis] for axis in range(3))
            for vertex in right
        ]
        if max(project_left) <= min(project_right) or max(project_right) <= min(project_left):
            return True
    return False


COMPATIBLE = [set() for _ in TETS]
for left, right in combinations(range(len(TETS)), 2):
    if disjoint3(TETS[left], TETS[right]):
        COMPATIBLE[left].add(right)
        COMPATIBLE[right].add(left)

TRIANGULATIONS = []


def extend_clique(chosen, candidates):
    if len(chosen) == 6:
        TRIANGULATIONS.append(tuple(chosen))
        return
    if len(chosen) + len(candidates) < 6:
        return
    remaining = set(candidates)
    while remaining:
        vertex = min(remaining)
        remaining.remove(vertex)
        extend_clique(chosen + [vertex], remaining & COMPATIBLE[vertex])


extend_clique([], set(range(len(TETS))))
gate(
    "independent facet triangulation census",
    len(TETS) == 56 and len(TRIANGULATIONS) == 180,
    "unit tetrahedra {0}, compatibility six-cliques {1}".format(
        len(TETS), len(TRIANGULATIONS)
    ),
)


def triangulation_cost(triangulation, charged_axes):
    return sum(
        sum(
            sum(
                abs(CORNERS3[left][axis] - CORNERS3[right][axis])
                for axis in charged_axes
            )
            > 1
            for left, right in combinations(TETS[tetrahedron], 2)
        )
        for tetrahedron in triangulation
    )


def diagonal_pattern(triangulation):
    value = 0
    for fixed_axis in range(3):
        free_axes = [axis for axis in range(3) if axis != fixed_axis]
        for bit in (0, 1):
            square = {vertex for vertex in range(8) if CORNERS3[vertex][fixed_axis] == bit}
            diagonals = set()
            for tetrahedron in triangulation:
                triangle = set(TETS[tetrahedron]) & square
                if len(triangle) != 3:
                    continue
                for left, right in combinations(triangle, 2):
                    if (
                        sum(
                            abs(CORNERS3[left][axis] - CORNERS3[right][axis])
                            for axis in free_axes
                        )
                        == 2
                    ):
                        diagonals.add(
                            int(
                                CORNERS3[left][free_axes[0]]
                                == CORNERS3[left][free_axes[1]]
                            )
                        )
            if len(diagonals) != 1:
                return None
            value |= diagonals.pop() << (2 * fixed_axis + bit)
    return value


tick_costs = [triangulation_cost(row, (0, 1, 2)) for row in TRIANGULATIONS]
mixed_costs = [triangulation_cost(row, (0, 1)) for row in TRIANGULATIONS]
patterns = [diagonal_pattern(row) for row in TRIANGULATIONS]
gate(
    "independent tick spectrum",
    Counter(tick_costs) == {18: 16, 19: 72, 20: 84, 21: 8},
    str(dict(sorted(Counter(tick_costs).items()))),
)
gate(
    "independent mixed spectrum",
    Counter(mixed_costs) == {8: 12, 9: 64, 10: 104},
    str(dict(sorted(Counter(mixed_costs).items()))),
)
absent_patterns = set(range(64)) - set(patterns)
gate(
    "independent diagonal-pattern census",
    None not in patterns
    and len(set(patterns)) == 58
    and absent_patterns == {22, 25, 26, 37, 38, 41},
    "realizable 58, absent {0}".format(sorted(absent_patterns)),
)


def collision_count(costs):
    fibers = defaultdict(set)
    for pattern, cost in zip(patterns, costs):
        fibers[pattern].add(cost)
    return sum(len(values) > 1 for values in fibers.values())


tick_parity = {(pattern.bit_count() + cost) & 1 for pattern, cost in zip(patterns, tick_costs)}
mixed_parity = {
    (pattern.bit_count() + cost) & 1 for pattern, cost in zip(patterns, mixed_costs)
}
gate(
    "independent functional-law split",
    collision_count(tick_costs) == 0
    and collision_count(mixed_costs) == 36
    and tick_parity == {0}
    and mixed_parity == {0, 1},
    "pattern collisions tick 0 mixed 36; parity tick {0} mixed {1}".format(
        sorted(tick_parity), sorted(mixed_parity)
    ),
)

npass = sum(ok for _, ok in GATES)
nfail = len(GATES) - npass
print("TOTAL: PASS={0} FAIL={1}".format(npass, nfail), flush=True)
sys.exit(0 if nfail == 0 else 1)
