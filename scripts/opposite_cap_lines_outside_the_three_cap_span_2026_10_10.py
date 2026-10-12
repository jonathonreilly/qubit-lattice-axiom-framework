#!/usr/bin/env python3
"""Opposite-cap lines sit outside the span of the three positive caps."""

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


def trace(matrix: list[list[int]]) -> int:
    return matrix[0][0] + matrix[1][1] + matrix[2][2]


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


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)
    positive_levels = (1, 2, 3)

    for modulus in positive_levels:
        level = -modulus
        means = {
            sum(cap(point, direction, level) for point in orbit)
            for direction in axis_steps
        }
        supports = {
            sum(cap(point, direction, level) != 0 for point in orbit)
            for direction in axis_steps
        }
        multi = 0
        for point in orbit:
            hot = [
                direction
                for direction in axis_steps
                if cap(point, direction, level)
            ]
            if len(hot) > 1:
                multi += 1
        covariant = True
        alternates = True
        seen_quarter = 0
        for matrix in group:
            for direction in axis_steps:
                image = apply(matrix, direction)
                for left in orbit:
                    for right in orbit:
                        moved = cap(apply(matrix, left), image, level) * cap(
                            apply(matrix, right), negate(image), level
                        )
                        stayed = cap(left, direction, level) * cap(
                            right, negate(direction), level
                        )
                        if moved != stayed:
                            covariant = False
                if trace(matrix) == 3 or apply(matrix, direction) != direction:
                    continue
                for point in orbit:
                    here = cap(point, direction, level)
                    if here == 0:
                        continue
                    there = cap(apply(matrix, point), direction, level)
                    if trace(matrix) == -1 and there != here:
                        alternates = False
                    if trace(matrix) == 1 and there != -here:
                        alternates = False
                    if trace(matrix) == 1:
                        seen_quarter += 1
        checks.check(f"level {-modulus} has mean 0", means == {0})
        checks.check(f"level {-modulus} cap has 4 points", supports == {4})
        checks.check(
            f"level {-modulus} activates one direction",
            multi == 0,
        )
        checks.check(f"level {-modulus} product is covariant", covariant)
        checks.check(
            f"level {-modulus} quarter-turn alternates",
            alternates and seen_quarter > 0,
        )

    distinct = True
    for left_modulus, right_modulus in ((3, 2), (3, 1), (2, 1)):
        only_left = only_right = 0
        for direction in axis_steps:
            for point in orbit:
                left = cap(point, direction, -left_modulus)
                right = cap(point, direction, -right_modulus)
                if left and not right:
                    only_left += 1
                if right and not left:
                    only_right += 1
        if only_left == 0 or only_right == 0:
            distinct = False
    checks.check("the three opposite caps are distinct", distinct)

    pure_ok = True
    for modulus in positive_levels:
        for weights in product((-1, 0, 1), repeat=6):
            total = 0
            for point in orbit:
                factor = 1
                for index, direction in enumerate(axis_steps):
                    factor += weights[index] * cap(point, direction, -modulus)
                total += factor
            if Fraction(total, 24) != 1:
                pure_ok = False
    checks.check("each opposite line has product mean 1", pure_ok)

    outside = True
    for modulus in positive_levels:
        witnessed = False
        for direction in axis_steps:
            for left in orbit:
                if cap(left, direction, -modulus) == 0:
                    continue
                if any(cap(left, direction, level) for level in positive_levels):
                    continue
                for right in orbit:
                    if cap(right, negate(direction), -modulus) == 0:
                        continue
                    positive_bond = any(
                        cap(left, direction, level)
                        * cap(right, negate(direction), level)
                        for level in positive_levels
                    )
                    if not positive_bond:
                        witnessed = True
        if not witnessed:
            outside = False
    checks.check("each opposite cap is outside the positive span", outside)
    named_left = (1, -2, -3)
    named_right = (1, 2, 3)
    named_direction = (0, 0, 1)
    named_product = cap(named_left, named_direction, -3) * cap(
        named_right, negate(named_direction), -3
    )
    named_positive = any(
        cap(named_left, named_direction, level)
        * cap(named_right, negate(named_direction), level)
        for level in positive_levels
    )
    checks.check(
        "the modulus-3 witness bond is (1, -2, -3) with (1, 2, 3)",
        named_left in orbit
        and named_right in orbit
        and named_product == -1
        and not named_positive,
    )

    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = set()
    for modulus in positive_levels:
        for direction in axis_steps:
            for left in orbit:
                for right in orbit:
                    seen_values.add(
                        1
                        + Fraction(1, 2)
                        * cap(left, direction, -modulus)
                        * cap(right, negate(direction), -modulus)
                    )
    checks.check("half-parameter factors stay positive", seen_values == positive)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
