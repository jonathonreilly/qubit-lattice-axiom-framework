#!/usr/bin/env python3
"""A transverse-cross kernel lies outside the six oriented caps."""

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


def raw(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    if left[2] != -3 or right[2] != 3:
        return 0
    if abs(left[0]) != abs(right[0]) or abs(left[1]) != abs(right[1]):
        return 0
    cross = left[0] * right[1] - left[1] * right[0]
    if cross == 0:
        return 0
    return 1 if cross > 0 else -1


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

    def transported(direction, left, right, matrix) -> int:
        inverse = transpose(matrix)
        return raw(apply(inverse, left), apply(inverse, right))

    well_defined = True
    for direction, matrices in carriers.items():
        for left in orbit:
            for right in orbit:
                values = {
                    transported(direction, left, right, matrix) for matrix in matrices
                }
                if len(values) != 1:
                    well_defined = False
    checks.check("soldered extension is well defined", well_defined)

    def kernel(direction, left, right) -> int:
        return transported(direction, left, right, carriers[direction][0])

    symmetric = all(
        kernel(direction, left, right) == kernel(negate(direction), right, left)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    )
    checks.check("the kernel is bond-symmetric", symmetric)

    matched_cross = True
    for left in orbit:
        for right in orbit:
            if left[2] != -3 or right[2] != 3:
                continue
            if abs(left[0]) != abs(right[0]) or abs(left[1]) != abs(right[1]):
                continue
            if left[0] * right[1] - left[1] * right[0] == 0:
                matched_cross = False
    checks.check("a matched transverse pair has nonzero cross", matched_cross)

    values = {
        kernel(direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("kernel values lie in {-1, 0, 1}", values == {-1, 0, 1})

    one_live = True
    for point in orbit:
        live = [
            direction
            for direction in axis_steps
            if any(kernel(direction, point, right) for right in orbit)
        ]
        if len(live) != 1:
            one_live = False
    checks.check("each record activates one direction", one_live)

    slice_mean = all(
        sum(kernel(direction, point, right) for point in orbit) == 0
        for direction in axis_steps
        for right in orbit
    )
    checks.check("every slice has sum 0", slice_mean)

    named_left = (-2, -1, -3)
    named_right = (-2, 1, 3)
    named = kernel(upward, named_left, named_right)
    checks.check(
        "the witness bond (-2, -1, -3) with (-2, 1, 3) has value -1",
        named_left in orbit and named_right in orbit and named == -1,
    )

    levels = (-3, -2, -1, 1, 2, 3)
    slice_values = [kernel(upward, point, named_right) for point in orbit]
    orthogonal = all(
        sum(
            slice_values[index] * cap(point, upward, level)
            for index, point in enumerate(orbit)
        )
        == 0
        for level in levels
    )
    checks.check("the witness slice is orthogonal to the six caps", orthogonal)
    outside = any(slice_values) and orthogonal
    checks.check("the witness slice is outside the six-cap span", outside)

    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = {
        1 + Fraction(1, 2) * kernel(direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("half-parameter factors stay positive", seen_values == positive)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
