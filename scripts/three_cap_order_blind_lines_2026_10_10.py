#!/usr/bin/env python3
"""Three cap lines of order-blind factors on one (1, 2, 3) orbit."""

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


def cap(point: tuple[int, ...], direction: tuple[int, int, int], modulus: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * modulus:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    product_sign = transverse[0] * transverse[1]
    return 1 if product_sign > 0 else -1


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)

    for modulus in (1, 2, 3):
        means = {
            sum(cap(point, direction, modulus) for point in orbit)
            for direction in axis_steps
        }
        supports = {
            sum(cap(point, direction, modulus) != 0 for point in orbit)
            for direction in axis_steps
        }
        multi = 0
        for point in orbit:
            hot = [
                direction
                for direction in axis_steps
                if cap(point, direction, modulus)
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
                        moved = cap(apply(matrix, left), image, modulus) * cap(
                            apply(matrix, right), negate(image), modulus
                        )
                        stayed = cap(left, direction, modulus) * cap(
                            right, negate(direction), modulus
                        )
                        if moved != stayed:
                            covariant = False
                if trace(matrix) == 3 or apply(matrix, direction) != direction:
                    continue
                for point in orbit:
                    here = cap(point, direction, modulus)
                    if here == 0:
                        continue
                    there = cap(apply(matrix, point), direction, modulus)
                    if trace(matrix) == -1 and there != here:
                        alternates = False
                    if trace(matrix) == 1 and there != -here:
                        alternates = False
                    if trace(matrix) == 1:
                        seen_quarter += 1
        checks.check(f"modulus {modulus} has mean 0", means == {0})
        checks.check(f"modulus {modulus} cap has 4 points", supports == {4})
        checks.check(
            f"modulus {modulus} activates one direction",
            multi == 0,
        )
        checks.check(f"modulus {modulus} product is covariant", covariant)
        checks.check(
            f"modulus {modulus} quarter-turn alternates",
            alternates and seen_quarter > 0,
        )

    distinct = True
    for left_modulus, right_modulus in ((3, 2), (3, 1), (2, 1)):
        only_left = only_right = 0
        for direction in axis_steps:
            for point in orbit:
                left = cap(point, direction, left_modulus)
                right = cap(point, direction, right_modulus)
                if left and not right:
                    only_left += 1
                if right and not left:
                    only_right += 1
        if only_left == 0 or only_right == 0:
            distinct = False
    checks.check("the three caps are distinct lines", distinct)

    pure_ok = True
    for modulus in (1, 2, 3):
        for weights in product((-1, 0, 1), repeat=6):
            total = 0
            for point in orbit:
                factor = 1
                for index, direction in enumerate(axis_steps):
                    factor += weights[index] * cap(point, direction, modulus)
                total += factor
            if Fraction(total, 24) != 1:
                pure_ok = False
    checks.check("each pure line has product mean 1", pure_ok)

    mixed = []
    for first in range(6):
        for second in range(6):
            if first == second:
                continue
            for left in orbit:
                for right in orbit:
                    weight = cap(left, negate(axis_steps[first]), 3) * cap(
                        right, negate(axis_steps[second]), 2
                    )
                    if weight == 0:
                        continue
                    total = 0
                    for point in orbit:
                        one = 1 + cap(point, axis_steps[first], 3) * cap(
                            left, negate(axis_steps[first]), 3
                        )
                        two = 1 + cap(point, axis_steps[second], 2) * cap(
                            right, negate(axis_steps[second]), 2
                        )
                        total += one * two
                    mixed.append(Fraction(total, 24))
    checks.check(
        "a mixture of modulus 3 and 2 has moment 25/24",
        Fraction(25, 24) in mixed and 1 in mixed,
    )
    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = set()
    for modulus in (1, 2, 3):
        for direction in axis_steps:
            for left in orbit:
                for right in orbit:
                    seen_values.add(
                        1 + Fraction(1, 2) * cap(left, direction, modulus) * cap(
                            right, negate(direction), modulus
                        )
                    )
    checks.check("half-parameter factors stay positive", seen_values == positive)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
