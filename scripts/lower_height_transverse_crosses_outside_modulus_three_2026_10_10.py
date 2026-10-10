#!/usr/bin/env python3
"""Transverse crosses at heights 1 and 2 lie outside the caps and height 3."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180


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


def cap(point: tuple[int, ...], direction: tuple[int, int, int], level: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * level:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def raw(height: int, left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if left[2] != -height or right[2] != height:
        return 0
    if abs(left[0]) != abs(right[0]) or abs(left[1]) != abs(right[1]):
        return 0
    cross = left[0] * right[1] - left[1] * right[0]
    if cross == 0:
        return 0
    return 1 if cross > 0 else -1


def rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank_now = 0
    columns = len(matrix[0]) if matrix else 0
    for col in range(columns):
        pivot = next((i for i in range(rank_now, len(matrix)) if matrix[i][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for i in range(len(matrix)):
            if i != rank_now and matrix[i][col] != 0:
                factor = matrix[i][col]
                matrix[i] = [
                    matrix[i][j] - factor * matrix[rank_now][j] for j in range(columns)
                ]
        rank_now += 1
    return rank_now


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)
    upward = (0, 0, 1)
    carriers = {
        direction: [matrix for matrix in group if apply(matrix, upward) == direction]
        for direction in axis_steps
    }
    checks.check(
        "each direction has four carriers",
        all(len(items) == 4 for items in carriers.values()),
    )

    def transported(height: int, direction, left, right, matrix) -> int:
        inverse = transpose(matrix)
        return raw(height, apply(inverse, left), apply(inverse, right))

    def kernel(height: int, direction, left, right) -> int:
        return transported(height, direction, left, right, carriers[direction][0])

    well_defined = True
    for height in (1, 2, 3):
        for direction, matrices in carriers.items():
            for left in orbit:
                for right in orbit:
                    values = {
                        transported(height, direction, left, right, matrix)
                        for matrix in matrices
                    }
                    if len(values) != 1:
                        well_defined = False
    checks.check("soldered extension is well defined at heights 1, 2, and 3", well_defined)

    symmetric = all(
        kernel(height, direction, left, right)
        == kernel(height, negate(direction), right, left)
        for height in (1, 2)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    )
    checks.check("the height-1 and height-2 kernels are bond-symmetric", symmetric)

    matched_cross = True
    for height in (1, 2):
        for left in orbit:
            for right in orbit:
                if left[2] != -height or right[2] != height:
                    continue
                if abs(left[0]) != abs(right[0]) or abs(left[1]) != abs(right[1]):
                    continue
                if left[0] * right[1] - left[1] * right[0] == 0:
                    matched_cross = False
    checks.check("a matched transverse pair has nonzero cross at heights 1 and 2", matched_cross)

    values = {
        kernel(height, direction, left, right)
        for height in (1, 2)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("kernel values at heights 1 and 2 lie in {-1, 0, 1}", values == {-1, 0, 1})

    one_live = True
    for height in (1, 2):
        for point in orbit:
            live = [
                direction
                for direction in axis_steps
                if any(kernel(height, direction, point, right) for right in orbit)
            ]
            if len(live) != 1:
                one_live = False
    checks.check("each record activates one direction at heights 1 and 2", one_live)

    slice_mean = all(
        sum(kernel(height, direction, point, right) for point in orbit) == 0
        for height in (1, 2)
        for direction in axis_steps
        for right in orbit
    )
    checks.check("every slice has sum 0 at heights 1 and 2", slice_mean)

    witnesses = {
        1: ((-3, -2, -1), (-3, 2, 1)),
        2: ((-3, 1, -2), (3, 1, 2)),
        3: ((-2, -1, -3), (-2, 1, 3)),
    }
    for height, (left, right) in witnesses.items():
        checks.check(
            f"the height-{height} witness bond has value -1",
            left in orbit and right in orbit and kernel(height, upward, left, right) == -1,
        )

    levels = (-3, -2, -1, 1, 2, 3)

    def slice_orthogonal(height: int) -> bool:
        right = witnesses[height][1]
        slice_values = [kernel(height, upward, point, right) for point in orbit]
        cap_dots = all(
            sum(
                slice_values[index] * cap(point, upward, level)
                for index, point in enumerate(orbit)
            )
            == 0
            for level in levels
        )
        cross_dot = sum(
            slice_values[index] * kernel(3, upward, point, right)
            for index, point in enumerate(orbit)
        )
        return any(slice_values) and cap_dots and cross_dot == 0

    checks.check(
        "each lower-height witness slice is orthogonal to the caps and height 3",
        slice_orthogonal(1) and slice_orthogonal(2),
    )

    bonds = [
        (direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    ]

    def cross_row(height: int) -> list[int]:
        return [kernel(height, direction, left, right) for direction, left, right in bonds]

    def cap_row(level: int) -> list[int]:
        return [
            cap(left, direction, level) * cap(right, negate(direction), level)
            for direction, left, right in bonds
        ]

    prior = [cap_row(level) for level in levels] + [cross_row(3)]
    with_one = prior + [cross_row(1)]
    with_two = prior + [cross_row(2)]
    all_nine = prior + [cross_row(1), cross_row(2)]
    checks.check(
        "the height-1 kernel lies outside the six caps and the modulus-3 cross",
        rank(prior) == 7 and rank(with_one) == 8,
    )
    checks.check(
        "the height-2 kernel lies outside the six caps and the modulus-3 cross",
        rank(prior) == 7 and rank(with_two) == 8,
    )
    checks.check(
        "the nine kernels are linearly independent",
        rank(all_nine) == 9,
    )

    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = {
        1 + Fraction(1, 2) * kernel(height, direction, left, right)
        for height in (1, 2)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("half-parameter factors stay positive", seen_values == positive)

    def mixed(direction, left, right) -> int:
        return kernel(1, direction, left, right) + kernel(2, direction, left, right)

    mix_right = (-2, -1, -3)
    mix_directions = ((-1, 0, 0), (0, -1, 0))
    moment = Fraction(
        sum(
            (1 + mixed(mix_directions[0], point, mix_right))
            * (1 + mixed(mix_directions[1], point, mix_right))
            for point in orbit
        ),
        len(orbit),
    )
    checks.check(
        "the sum of the two kernels has two-neighbour moment 23/24",
        mix_right in orbit and moment == Fraction(23, 24),
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
