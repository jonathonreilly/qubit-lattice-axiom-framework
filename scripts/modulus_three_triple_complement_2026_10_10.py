#!/usr/bin/env python3
"""The modulus-3 triple complement is one line and is not order-blind."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import lcm

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/MODULUS_THREE_TRIPLE_COMPLEMENT_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md', 'docs/SINGLE_HEIGHT_SIGNATURE_ORDER_BLIND_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md']


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, name: str, ok: bool) -> None:
        if ok:
            self.passed += 1
            print(f"PASS {name}")
        else:
            self.failed += 1
            print(f"FAIL {name}")


def det3(matrix: list[list[int]]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper() -> list[list[list[int]]]:
    found = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for src, dst in enumerate(perm):
                matrix[dst][src] = signs[src]
            if det3(matrix) == 1:
                found.append(matrix)
    return found


def apply(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def directions() -> list[tuple[int, int, int]]:
    found = []
    for axis in range(3):
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[axis] = sign
            found.append(tuple(vector))
    return found


def negate(direction: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(-coordinate for coordinate in direction)


def dot(point: tuple[int, ...], direction: tuple[int, int, int]) -> int:
    return sum(left * right for left, right in zip(point, direction))


def bond_key(direction, left, right):
    forward = (direction, left, right)
    backward = (negate(direction), right, left)
    return tuple(sorted((forward, backward)))


def signature(direction, left, right) -> tuple[int, int]:
    forward = (dot(left, direction), dot(right, direction))
    backward = (-forward[1], -forward[0])
    return min(forward, backward)


def kernel_basis(rows: list[tuple[int, ...]], width: int) -> list[list[Fraction]]:
    matrix = [[Fraction(value) for value in row] for row in rows]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((index for index in range(rank_now, len(matrix)) if matrix[index][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for index in range(len(matrix)):
            if index != rank_now and matrix[index][col] != 0:
                factor = matrix[index][col]
                matrix[index] = [
                    matrix[index][col_index] - factor * matrix[rank_now][col_index]
                    for col_index in range(width)
                ]
        pivots.append(col)
        rank_now += 1
    basis = []
    for free in [col for col in range(width) if col not in pivots]:
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for pivot_index, pivot_col in enumerate(pivots):
            vector[pivot_col] = -matrix[pivot_index][free]
        basis.append(vector)
    return basis


def reduced_rows(rows: list[list[Fraction]], width: int) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((index for index in range(rank_now, len(matrix)) if matrix[index][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for index in range(len(matrix)):
            if index != rank_now and matrix[index][col] != 0:
                factor = matrix[index][col]
                matrix[index] = [
                    matrix[index][col_index] - factor * matrix[rank_now][col_index]
                    for col_index in range(width)
                ]
        pivots.append(col)
        rank_now += 1
    return matrix[:rank_now], pivots


def integer_vector(vector: list[Fraction]) -> tuple[int, ...]:
    scale = 1
    for value in vector:
        scale = lcm(scale, value.denominator)
    ints = [int(value * scale) for value in vector]
    content = 0
    for value in ints:
        left, right = abs(value), abs(content)
        while right:
            left, right = right, left % right
        content = left
    ints = [value // content for value in ints]
    if ints[3] > 0:
        ints = [-value for value in ints]
    return tuple(ints)


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24 and (-3, -2, -1) in orbit)
    axis_steps = directions()
    checks.check("six axis directions", axis_steps == [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)])

    image_of: dict = {}
    sig_of: dict[int, tuple[int, int]] = {}
    for direction in axis_steps:
        for left in orbit:
            for right in orbit:
                images = frozenset(
                    bond_key(apply(matrix, direction), apply(matrix, left), apply(matrix, right))
                    for matrix in group
                )
                if images not in image_of:
                    image_of[images] = len(sig_of)
                    sample = min(next(iter(images)))
                    sig_of[image_of[images]] = signature(*sample)
                image_of[(direction, left, right)] = image_of[images]
    dimension = len(sig_of)
    by_sig: dict[tuple[int, int], list[int]] = defaultdict(list)
    for index, sig in sig_of.items():
        by_sig[sig].append(index)
    checks.check("height signatures number 21", len(by_sig) == 21)
    checks.check("the signatures partition 84 bond orbits", dimension == 84)

    slice_rows = []
    seen_rows = set()
    for direction in axis_steps:
        for right in orbit:
            row = [0] * dimension
            for left in orbit:
                row[image_of[(direction, left, right)]] += 1
            key = tuple(row)
            if key not in seen_rows:
                seen_rows.add(key)
                slice_rows.append(key)

    triple = ((-3, -3), (-3, 3), (3, -3))
    columns = [index for sig in triple for index in by_sig[sig]]
    local_rows = []
    seen_local = set()
    for row in slice_rows:
        packed = tuple(row[index] for index in columns)
        if any(packed) and packed not in seen_local:
            seen_local.add(packed)
            local_rows.append(packed)
    joint = kernel_basis(local_rows, len(columns))
    checks.check("the modulus-3 triple has joint slice kernel 10", len(joint) == 10 and len(columns) == 12)

    internal = []
    offset = 0
    for sig in triple:
        block = by_sig[sig]
        block_rows = []
        seen_block = set()
        for row in slice_rows:
            packed = tuple(row[index] for index in block)
            if any(packed) and packed not in seen_block:
                seen_block.add(packed)
                block_rows.append(packed)
        for local in kernel_basis(block_rows, len(block)):
            full = [Fraction(0) for _ in columns]
            for index, value in enumerate(local):
                full[offset + index] = value
            internal.append(full)
        offset += len(block)
    reduced, pivots = reduced_rows(internal, len(columns))
    remainders = []
    for vector in joint:
        rest = vector[:]
        for row, pivot in zip(reduced, pivots):
            factor = rest[pivot]
            if factor:
                rest = [rest[index] - factor * row[index] for index in range(len(columns))]
        if any(rest):
            remainders.append(integer_vector(rest))
    complement = (0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 1)
    checks.check(
        "the complement of the three signature kernels is one line",
        len(reduced) == 9 and set(remainders) == {complement},
    )

    coords = [Fraction(0) for _ in range(dimension)]
    for index, value in enumerate(complement):
        coords[columns[index]] = Fraction(value)

    def value_at(direction, left, right) -> Fraction:
        return coords[image_of[(direction, left, right)]]

    record = (-3, -2, -1)
    checks.check(
        "the complement is -1, +1, +1 on one orbit of each signature",
        value_at((-1, 0, 0), record, (-3, 2, 1)) == -1
        and signature((-1, 0, 0), record, (-3, 2, 1)) == (-3, -3)
        and value_at((-1, 0, 0), record, (3, 2, -1)) == 1
        and signature((-1, 0, 0), record, (3, 2, -1)) == (3, -3)
        and value_at((1, 0, 0), record, (3, 2, -1)) == 1
        and signature((1, 0, 0), record, (3, 2, -1)) == (-3, 3)
        and sum(1 for value in coords if value) == 3,
    )
    live_counts = []
    for left in orbit:
        count = 0
        for direction in axis_steps:
            if any(value_at(direction, left, right) for right in orbit):
                count += 1
        live_counts.append(count)
    checks.check("every record has two live directions", live_counts == [2] * 24)
    moment = sum(value_at((-1, 0, 0), left, record) * value_at((1, 0, 0), left, record) for left in orbit)
    checks.check("the opposite x-directions at (-3, -2, -1) have moment 2", moment == 2)
    checks.check("the uniform average of that moment is 1/12", moment / 24 == Fraction(1, 12))
    checks.check(
        "the equal-height block is nonzero, so the line is outside the opposite signatures",
        any(coords[index] for index in by_sig[(-3, -3)]),
    )
    checks.check("a direct-sum stand-in is not this complement", complement != tuple(0 for _ in complement))

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)
    print("per_element: checked exact arithmetic on the explicitly enumerated finite record and bond data above; no continuum or empirical input is tested.")
    print("per_site: checked and not executed — this runner contains no evolving site ensemble; finite centre-record sums are the local mathematical object.")
    print("per_mode: checked and not executed — no momentum spectrum, physical particle mode or dispersion relation is computed in this finite alphabet runner.")
    print("per_block: checked the finite algebraic blocks and coefficient cases described by the named predicates; unlisted support sectors are outside this execution.")
    print("lattice_wide: checked and not executed — no whole-lattice dynamics is simulated; any all-window statement depends on the source proof and its cited converse.")



if __name__ == "__main__":
    main()
