#!/usr/bin/env python3
"""Lower-height cap dressings on the chiral pair lie off the nine kernels."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180

KAPPA = Fraction(1, 2)
HEIGHTS = (1, 2)
KINDS = ("chi", "ts", "prod")


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


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [[matrix[j][i] for j in range(3)] for i in range(3)]


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


def alphabet() -> list[tuple[int, int, int]]:
    found = []
    for perm in permutations((1, 2, 3)):
        for signs in product((-1, 1), repeat=3):
            found.append(tuple(sign * value for sign, value in zip(signs, perm)))
    return sorted(set(found))


def seed_cross(
    height: int,
    left: tuple[int, int, int],
    right: tuple[int, int, int],
    swapped: bool,
) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if swapped:
        matched_abs = abs(x_coord) == abs(y_prime) and abs(y_coord) == abs(x_prime)
    else:
        matched_abs = abs(x_coord) == abs(x_prime) and abs(y_coord) == abs(y_prime)
    if not matched_abs:
        return 0
    raw = x_coord * y_prime - y_coord * x_prime
    if raw == 0:
        return 0
    return 1 if raw > 0 else -1


def determinant(rows: list[list[int]]) -> Fraction:
    size = len(rows)
    matrix = [list(map(Fraction, row)) for row in rows]
    sign = Fraction(1)
    for index in range(size):
        pivot = next((row for row in range(index, size) if matrix[row][index] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != index:
            matrix[index], matrix[pivot] = matrix[pivot], matrix[index]
            sign = -sign
        for row in range(index + 1, size):
            factor = matrix[row][index] / matrix[index][index]
            matrix[row] = [
                matrix[row][column] - factor * matrix[index][column] for column in range(size)
            ]
    value = sign
    for index in range(size):
        value *= matrix[index][index]
    return value


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    records = alphabet()
    positive = {apply(matrix, (1, 2, 3)) for matrix in group}
    chirality = {point: (1 if point in positive else -1) for point in records}
    other = [point for point in records if point not in positive]
    checks.check(
        "the alphabet is the chiral pair of two proper orbits",
        len(records) == 48
        and len(positive) == 24
        and len(other) == 24
        and (2, 1, 3) in other
        and (1, 2, -3) in other,
    )
    axis_steps = directions()
    checks.check(
        "six axis directions",
        axis_steps == [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)],
    )
    up = (0, 0, 1)

    def cap_sign(kind: str, height: int, direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        if dot(point, direction) != height:
            return 0
        axis = next(index for index, coordinate in enumerate(direction) if coordinate)
        transverse = [point[index] for index in range(3) if index != axis]
        transverse_sign = 1 if transverse[0] * transverse[1] > 0 else -1
        orbit_sign = chirality[point]
        if kind == "chi":
            return orbit_sign
        if kind == "ts":
            return transverse_sign
        return orbit_sign * transverse_sign

    def kernel(kind: str, height: int, direction: tuple[int, int, int], left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
        return cap_sign(kind, height, direction, left) * cap_sign(kind, height, negate(direction), right)

    soldered = all(
        kernel(kind, height, apply(matrix, direction), apply(matrix, left), apply(matrix, right))
        == kernel(kind, height, direction, left, right)
        for matrix in group
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        for kind in KINDS
    )
    checks.check("all six cap products are soldered under proper rotations", soldered)
    bond_symmetric = all(
        kernel(kind, height, direction, left, right) == kernel(kind, height, negate(direction), right, left)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        for kind in KINDS
    )
    checks.check("all six cap products are bond-symmetric", bond_symmetric)
    means_zero = all(
        sum(cap_sign(kind, height, direction, point) for point in records) == 0
        for direction in axis_steps
        for height in HEIGHTS
        for kind in KINDS
    )
    disjoint = all(
        sum(1 for direction in axis_steps if cap_sign(kind, height, direction, point)) <= 1
        for point in records
        for height in HEIGHTS
        for kind in KINDS
    )
    checks.check(
        "each cap sign has mean 0 and at most one live direction",
        means_zero and disjoint,
    )
    left_slice = all(
        sum(kernel(kind, height, direction, left, right) for left in records) == 0
        for direction in axis_steps
        for right in records
        for height in HEIGHTS
        for kind in KINDS
    )
    not_zero = all(
        any(
            kernel(kind, height, direction, left, right)
            for direction in axis_steps
            for left in records
            for right in records
        )
        for height in HEIGHTS
        for kind in KINDS
    )
    checks.check(
        "every left slice sums to 0",
        left_slice and not_zero,
    )
    kernel_values = {
        kernel(kind, height, direction, left, right)
        for direction in axis_steps
        for left in records
        for right in records
        for height in HEIGHTS
        for kind in KINDS
    }
    factor_values = {1 + KAPPA * value for value in kernel_values}
    checks.check(
        "at coefficient 1/2 each cap takes values 1/2, 1, and 3/2",
        kernel_values == {-1, 0, 1} and factor_values == {Fraction(1, 2), Fraction(1), Fraction(3, 2)},
    )
    far_end = all(
        sum(1 + KAPPA * kernel(kind, height, direction, left, right) for right in records) == 48
        for direction in axis_steps
        for left in records
        for height in HEIGHTS
        for kind in KINDS
    )
    checks.check("every far-end sum equals 48", far_end)

    frames = {
        direction: [matrix for matrix in group if apply(matrix, up) == direction] for direction in axis_steps
    }

    def cross(height: int, direction: tuple[int, int, int], left: tuple[int, int, int], right: tuple[int, int, int], swapped: bool) -> int:
        inverse = transpose(frames[direction][0])
        return seed_cross(height, apply(inverse, left), apply(inverse, right), swapped)

    def five(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> list[int]:
        return [
            kernel("chi", height, up, left, right),
            kernel("ts", height, up, left, right),
            kernel("prod", height, up, left, right),
            cross(height, up, left, right, False),
            cross(height, up, left, right, True),
        ]

    def outside_nine(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> bool:
        other_heights = [3] + [item for item in HEIGHTS if item != height]
        cap_clear = all(
            kernel(kind, other, up, left, right) == 0
            for other in other_heights
            for kind in KINDS
        )
        cross_clear = all(
            cross(other, up, left, right, swapped) == 0
            for other in other_heights
            for swapped in (False, True)
        )
        return cap_clear and cross_clear

    expected = [
        [-1, 1, -1, 0, 0],
        [1, -1, -1, -1, 0],
        [1, -1, -1, 1, 0],
        [1, 1, 1, 0, -1],
        [-1, -1, 1, 0, -1],
    ]
    height_one = (
        ((-2, -3, 1), (-2, -3, -1)),
        ((-2, -3, 1), (-2, 3, -1)),
        ((-2, -3, 1), (2, -3, -1)),
        ((-2, -3, 1), (-3, -2, -1)),
        ((-2, -3, 1), (-3, 2, -1)),
    )
    height_two = (
        ((-1, -3, 2), (-1, -3, -2)),
        ((-1, -3, 2), (-1, 3, -2)),
        ((-1, -3, 2), (1, -3, -2)),
        ((-1, -3, 2), (-3, -1, -2)),
        ((-1, -3, 2), (-3, 1, -2)),
    )
    rows_one = [five(1, left, right) for left, right in height_one]
    rows_two = [five(2, left, right) for left, right in height_two]
    cleared = all(outside_nine(1, left, right) for left, right in height_one) and all(
        outside_nine(2, left, right) for left, right in height_two
    )
    idle = all(
        kernel(kind, height, up, (1, 2, 3), (1, 2, 3)) == 0
        for height in (1, 2, 3)
        for kind in KINDS
    ) and all(
        cross(height, up, (1, 2, 3), (1, 2, 3), swapped) == 0
        for height in (1, 2, 3)
        for swapped in (False, True)
    )
    checks.check(
        "ten bonds have determinant -16 and every kernel from another height vanishes",
        rows_one == expected
        and rows_two == expected
        and determinant(rows_one) == -16
        and determinant(rows_two) == -16
        and cleared
        and idle,
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
