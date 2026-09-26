#!/usr/bin/env python3
"""Independent referee for deferred-20260925-band-gauge a1.

The compass carvings and their gauge-reduced singular-value bounds are
rebuilt here. The attempt's script is not imported.
"""
from __future__ import annotations

import itertools
import math
import random
import sys
from fractions import Fraction as F

import numpy as np

FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str = "") -> None:
    print(("PASS " if ok else "FAIL ") + tag + ((": " + msg) if msg else ""), flush=True)
    if not ok:
        FAILS.append(tag)


SIZE = (4, 4, 4)
N20 = (
    (0, 0, 0), (0, 0, 3), (0, 1, 0), (0, 2, 1), (0, 2, 2), (0, 3, 1), (1, 0, 2), (1, 0, 3), (1, 1, 0),
    (1, 1, 1), (1, 2, 1), (2, 0, 1), (2, 0, 2), (2, 1, 1), (2, 1, 2), (3, 0, 0), (3, 1, 2), (3, 2, 2),
    (3, 3, 0), (3, 3, 1),
)
N16 = (
    (0, 0, 2), (0, 1, 1), (0, 1, 2), (0, 2, 1), (1, 1, 2), (1, 1, 3), (2, 0, 3), (2, 1, 0),
    (2, 1, 3), (2, 2, 0), (3, 0, 2), (3, 0, 3), (3, 2, 0), (3, 2, 1), (3, 3, 1), (3, 3, 2),
)
SCALE = 10 ** 40


def neighbour(site, axis, step):
    moved = list(site)
    moved[axis] = (moved[axis] + step) % SIZE[axis]
    return tuple(moved)


def sqrt_bracket(value):
    value = F(value)
    scaled = value.numerator * SCALE * SCALE // value.denominator
    root = math.isqrt(scaled)
    return F(root, SCALE), F(root + 1, SCALE)


class Interval:
    def __init__(self, low, high=None):
        self.low = F(low)
        self.high = F(high if high is not None else low)

    def __add__(self, other):
        other = other if isinstance(other, Interval) else Interval(other)
        return Interval(self.low + other.low, self.high + other.high)

    def scale(self, factor):
        factor = F(factor)
        return Interval(min(factor * self.low, factor * self.high), max(factor * self.low, factor * self.high))

    def mid(self):
        return (self.low + self.high) / 2

    def radius(self):
        return (self.high - self.low) / 2


def carving(sites):
    ordered = sorted(sites)
    index = {site: position for position, site in enumerate(ordered)}
    present = set(ordered)
    bonds = []
    for site in ordered:
        for axis in range(3):
            moved = list(site)
            moved[axis] += 1
            winding = [0, 0, 0]
            if moved[axis] == SIZE[axis]:
                moved[axis] = 0
                winding[axis] = 1
            target = tuple(moved)
            if target in present:
                bonds.append((index[site], index[target], axis, tuple(winding)))
    squares = {}
    for record in itertools.product(*(range(length) for length in SIZE)):
        if record in present:
            continue
        constrained = set()
        for axis in range(3):
            for step in (1, -1):
                carved = neighbour(record, axis, step)
                if carved in present and neighbour(carved, axis, step) in present:
                    constrained.add(axis)
        raw = [F(1), F(2), F(3)]
        for axis in constrained:
            raw[axis] = F(0)
        norm = sum(raw)
        squares[record] = [raw[axis] / norm for axis in range(3)]
    dangling = {}
    for site in ordered:
        for axis in range(3):
            for step in (1, -1):
                record = neighbour(site, axis, step)
                if record in present:
                    continue
                if neighbour(site, axis, -step) in present:
                    continue
                dangling.setdefault((index[site], axis), []).append(squares[record][axis])
    live = [key for key, values in dangling.items() if any(value != 0 for value in values)]
    parent = list(range(len(ordered)))

    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    tree, extra = [], []
    for bond in bonds:
        left, right = find(bond[0]), find(bond[1])
        if left != right:
            parent[left] = right
            tree.append(bond)
        else:
            extra.append(bond)
    fields = {}
    for key in live:
        total = Interval(0)
        for square in dangling[key]:
            low, high = sqrt_bracket(square)
            total = total + Interval(low, high)
        fields[key] = total
    return {"sites": ordered, "count": len(ordered), "bonds": bonds, "live": live, "tree": tree, "extra": extra, "field": fields}


def sides(graph):
    parity = [sum(site) % 2 for site in graph["sites"]]
    left = [site for site in range(graph["count"]) if parity[site] == 0]
    left += [graph["count"] + position for position, (site, _axis) in enumerate(graph["live"]) if parity[site] == 1]
    right = [site for site in range(graph["count"]) if parity[site] == 1]
    right += [graph["count"] + position for position, (site, _axis) in enumerate(graph["live"]) if parity[site] == 0]
    return left, right


def majorana(graph, signs, phase):
    matrix = {}

    def put(row, column, value):
        matrix[(row, column)] = matrix.get((row, column), Interval(0)) + value

    for bond, sign in zip(graph["bonds"], signs):
        left, right, _axis, winding = bond
        amplitude = F(-2 * sign) * phase(winding)
        put(left, right, Interval(amplitude))
        put(right, left, Interval(-amplitude))
    for position, (site, axis) in enumerate(graph["live"]):
        field = graph["field"][(site, axis)]
        put(graph["count"] + position, site, field.scale(2))
        put(site, graph["count"] + position, field.scale(-2))
    return matrix


def signs_of(graph, sector):
    assignment = {bond: 1 for bond in graph["tree"]}
    assignment.update({bond: value for bond, value in zip(graph["extra"], sector)})
    return [assignment[bond] for bond in graph["bonds"]]


def inertia(matrix):
    entries = [row[:] for row in matrix]
    active = list(range(len(entries)))
    positive = negative = 0
    while active:
        pivot = next((index for index in active if entries[index][index] != 0), None)
        if pivot is not None:
            value = entries[pivot][pivot]
            positive += value > 0
            negative += value < 0
            rest = [index for index in active if index != pivot]
            for row in rest:
                factor = entries[row][pivot] / value
                if factor:
                    for column in rest:
                        entries[row][column] -= factor * entries[pivot][column]
            active = rest
            continue
        pair = next(((left, right) for left in active for right in active if left < right and entries[left][right] != 0), None)
        if pair is None:
            break
        left, right = pair
        positive += 1
        negative += 1
        rest = [index for index in active if index not in (left, right)]
        slope = entries[left][right]
        for row in rest:
            left_coupling, right_coupling = entries[row][left], entries[row][right]
            if left_coupling == 0 and right_coupling == 0:
                continue
            for column in rest:
                entries[row][column] -= (right_coupling / slope) * entries[left][column] + (left_coupling / slope) * entries[right][column]
        active = rest
    return positive, negative, len(matrix) - positive - negative


def positive_definite(matrix):
    entries = [row[:] for row in matrix]
    for pivot in range(len(entries)):
        if entries[pivot][pivot] <= 0:
            return False
        for row in range(pivot + 1, len(entries)):
            factor = entries[row][pivot] / entries[pivot][pivot]
            if factor:
                for column in range(pivot, len(entries)):
                    entries[row][column] -= factor * entries[pivot][column]
    return True


def maximum_matching(rows, columns, edges):
    adjacency = {row: [] for row in rows}
    for row, column in edges:
        adjacency[row].append(column)
    matched = {}

    def search(row, seen):
        for column in adjacency[row]:
            if column in seen:
                continue
            seen.add(column)
            if column not in matched or search(matched[column], seen):
                matched[column] = row
                return True
        return False

    return sum(1 for row in rows if search(row, set()))


def unwrap(graph, tree):
    adjacency = {site: [] for site in range(graph["count"])}
    for left, right, _axis, winding in tree:
        adjacency[left].append((right, winding))
        adjacency[right].append((left, tuple(-coordinate for coordinate in winding)))
    position = {0: (0, 0, 0)}
    stack = [0]
    while stack:
        current = stack.pop()
        for other, winding in adjacency[current]:
            if other not in position:
                position[other] = tuple(position[current][axis] + winding[axis] for axis in range(3))
                stack.append(other)
    return position


def certify(graph, zeros, sector, threshold):
    left, right = sides(graph)
    needed = len(left) - zeros
    matrix = majorana(graph, signs_of(graph, sector), lambda winding: 1)
    generator = random.Random(11)
    for _attempt in range(2000):
        order = graph["bonds"][:]
        generator.shuffle(order)
        parent = list(range(graph["count"]))

        def find(node):
            while parent[node] != node:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        tree = []
        for bond in order:
            left_root, right_root = find(bond[0]), find(bond[1])
            if left_root != right_root:
                parent[left_root] = right_root
                tree.append(bond)
        if len(tree) != graph["count"] - 1:
            continue
        position = unwrap(graph, tree)
        dependent = []
        for bond in graph["bonds"]:
            start, finish, _axis, winding = bond
            if any(winding[axis] + position[start][axis] - position[finish][axis] != 0 for axis in range(3)):
                dependent.append(bond)
        ends = []
        for start, finish, _axis, _winding in dependent:
            row = start if start in left else finish
            column = finish if finish in right else start
            ends.append((row, column))
        for choice in itertools.product((0, 1), repeat=len(ends)):
            deleted_rows = {end[0] for end, bit in zip(ends, choice) if bit == 0}
            deleted_columns = {end[1] for end, bit in zip(ends, choice) if bit == 1}
            if len(deleted_rows) + len(deleted_columns) > 2:
                continue
            rows = [row for row in left if row not in deleted_rows]
            columns = [column for column in right if column not in deleted_columns]
            if min(len(rows), len(columns)) < needed:
                continue
            if not all(row in deleted_rows or column in deleted_columns for row, column in ends):
                continue
            numeric = np.array([[float(matrix.get((row, column), Interval(0)).mid()) for column in columns] for row in rows])
            values = np.sort(np.linalg.svd(numeric, compute_uv=False))[::-1]
            if values[needed - 1] < float(threshold):
                continue
            width = len(columns)
            height = len(rows)
            middle = [[matrix.get((row, column), Interval(0)).mid() for column in columns] for row in rows]
            radius = max(matrix.get((row, column), Interval(0)).radius() for row in rows for column in columns)
            error = radius * height * width
            shifted = (threshold + error) ** 2
            gram = [
                [sum(middle[entry][left_index] * middle[entry][right_index] for entry in range(height)) - (shifted if left_index == right_index else 0) for right_index in range(width)]
                for left_index in range(width)
            ]
            positive, negative, zero = inertia(gram)
            if negative + zero <= width - needed:
                return {"dependent": len(dependent), "rows": sorted(deleted_rows), "columns": sorted(deleted_columns), "size": (height, width), "inertia": (positive, negative, zero), "error": error}
    return None


def upper_bound(graph, zeros, sector, momentum, ceiling):
    left, right = sides(graph)
    phase = lambda winding: (-1) ** sum(coordinate for coordinate, bit in zip(winding, momentum) if bit)
    matrix = majorana(graph, signs_of(graph, sector), phase)
    middle = [[matrix.get((row, column), Interval(0)).mid() for column in right] for row in left]
    radius = max(matrix.get((row, column), Interval(0)).radius() for row in left for column in right)
    error = radius * len(left) * len(right)
    numeric = np.array([[float(entry) for entry in row] for row in middle])
    _left_vectors, values, right_vectors = np.linalg.svd(numeric)
    test = right_vectors[::-1][: zeros + 1]
    rational = [[F(int(round(entry * 10 ** 12)), 10 ** 12) for entry in vector] for vector in test]
    image = [[sum(middle[row][column] * vector[column] for column in range(len(right))) for row in range(len(left))] for vector in rational]
    stiffness = [[sum(left_image * right_image for left_image, right_image in zip(image[left_index], image[right_index])) for right_index in range(zeros + 1)] for left_index in range(zeros + 1)]
    gram = [[sum(left_vector * right_vector for left_vector, right_vector in zip(rational[left_index], rational[right_index])) for right_index in range(zeros + 1)] for left_index in range(zeros + 1)]
    target = (ceiling - error) ** 2
    difference = [[target * gram[left_index][right_index] - stiffness[left_index][right_index] for right_index in range(zeros + 1)] for left_index in range(zeros + 1)]
    return positive_definite(difference), float(values[::-1][zeros])


graphs = {"N20": carving(N20), "N16": carving(N16)}
structure_ok = True
for name, zeros in (("N20", 1), ("N16", 2)):
    graph = graphs[name]
    left, right = sides(graph)
    matrix = majorana(graph, [1] * len(graph["bonds"]), lambda winding: 1)
    bipartite = all((row in left) != (column in left) for row, column in matrix) and len(left) == len(right)
    matching = maximum_matching(left, right, [(row, column) for row, column in matrix if row in left])
    structure_ok = structure_ok and bipartite and matching == len(left) - zeros and len(graph["tree"]) == graph["count"] - 1
check(
    "structure",
    structure_ok and len(graphs["N20"]["bonds"]) - 20 + 1 == 4 and len(graphs["N16"]["bonds"]) - 16 + 1 == 3,
    "both nets are bipartite with one or two structural zero singular values, and the quotient cycle ranks are 4 and 3",
)

bounds = {"N20": [F(7858, 10000), F(6079, 10000)], "N16": [F(14333, 10000)]}
certificates = {}
lower_ok = True
for name, zeros in (("N20", 1), ("N16", 2)):
    graph = graphs[name]
    sectors = list(itertools.product((1, -1), repeat=len(graph["extra"])))
    for sector in sectors:
        found = None
        for threshold in bounds[name]:
            found = certify(graph, zeros, sector, threshold)
            if found:
                certificates[(name, sector)] = (threshold, found)
                break
        lower_ok = lower_ok and found is not None and found["dependent"] == 3
    print(f"  {name}: {len(sectors)} sectors certified", flush=True)
counts = {}
for (name, _sector), (threshold, _found) in certificates.items():
    counts.setdefault(name, {}).setdefault(threshold, 0)
    counts[name][threshold] += 1
check(
    "lower bounds",
    lower_ok and counts["N20"] == {F(6079, 10000): 8, F(7858, 10000): 8} and counts["N16"] == {F(14333, 10000): 8},
    "N20 is at least 0.6079 in eight sectors and 0.7858 in eight; N16 is at least 1.4333 in all eight",
)

uppers = (
    ("N20", 1, (-1, 1, -1, 1), (1, 0, 1), F(6179, 10000)),
    ("N20", 1, (1, 1, 1, 1), (0, 1, 1), F(7959, 10000)),
    ("N16", 2, (-1, 1, 1), (1, 1, 1), F(14368, 10000)),
)
upper_ok = True
for name, zeros, sector, momentum, ceiling in uppers:
    passed, value = upper_bound(graphs[name], zeros, sector, momentum, ceiling)
    upper_ok = upper_ok and passed
    print(f"  upper {name} {sector}: {value:.6f} <= {float(ceiling)}", flush=True)
check("upper bounds", upper_ok, "the three minimising momenta lie at most 0.6179, 0.7959 and 1.4368")

cycle = (
    (4, -3, 2), (4, -3, 1), (4, -2, 1), (3, -2, 1), (3, -1, 1), (3, -1, 2), (3, 0, 2), (3, 0, 3),
    (2, 0, 3), (2, 1, 3), (1, 1, 3), (1, 1, 2), (0, 1, 2), (0, 0, 2), (-1, 0, 2), (-1, -1, 2),
    (-1, -1, 1), (-1, -2, 1), (0, -2, 1), (0, -3, 1), (0, -3, 2), (1, -3, 2), (1, -3, 3), (2, -3, 3),
    (2, -4, 3), (3, -4, 3), (3, -4, 2), (4, -4, 2),
)
check(
    "lift cycle",
    len(set(cycle)) == 28
    and all(tuple(coordinate % 4 for coordinate in site) in N16 for site in cycle)
    and all(sum(abs(left - right) for left, right in zip(current, nxt)) == 1 for current, nxt in zip(cycle, cycle[1:] + cycle[:1])),
    "the N16 lift contains a simple 28-edge cycle, so it is not a tree",
)

if FAILS:
    print("SUMMARY: fails at " + ", ".join(FAILS), flush=True)
    sys.exit(1)
print(
    "SUMMARY: confirmed partial. In every translation-invariant gauge sector the auxiliary Bloch operator of N20 has "
    "exactly two zero bands and every other energy at least 0.6079 in eight sectors and 0.7858 in the other eight. "
    "N16 has exactly four zero bands and every other energy at least 1.4333 in all eight sectors. The three sampled "
    "minima sit at most 0.6179, 0.7959 and 1.4368. Non-periodic gauge fields and the physical projection were not treated.",
    flush=True,
)
print(
    "HIT: confirmed - the N20 and N16 compass carvings have uniform band gaps in every translation-invariant gauge sector, "
    "with the stated zero-band counts and lower bounds",
    flush=True,
)
