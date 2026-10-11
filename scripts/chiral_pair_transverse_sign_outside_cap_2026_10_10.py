#!/usr/bin/env python3
"""The transverse-sign cap on the chiral pair is order-blind and off the chiral-cap line."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180

KAPPA = Fraction(1, 2)


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


def alphabet() -> list[tuple[int, int, int]]:
    found = []
    for perm in permutations((1, 2, 3)):
        for signs in product((-1, 1), repeat=3):
            found.append(tuple(sign * value for sign, value in zip(signs, perm)))
    return sorted(set(found))


def transverse_sign(direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
    if dot(point, direction) != 3:
        return 0
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def chirality_cap(
    direction: tuple[int, int, int],
    point: tuple[int, int, int],
    positive: set[tuple[int, int, int]],
) -> int:
    if dot(point, direction) != 3:
        return 0
    return 1 if point in positive else -1


def phi(
    direction: tuple[int, int, int],
    left: tuple[int, int, int],
    right: tuple[int, int, int],
) -> Fraction:
    return 1 + KAPPA * transverse_sign(direction, left) * transverse_sign(negate(direction), right)


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    records = alphabet()
    positive = {apply(matrix, (1, 2, 3)) for matrix in group}
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

    soldered = all(
        phi(apply(matrix, direction), apply(matrix, left), apply(matrix, right))
        == phi(direction, left, right)
        for matrix in group
        for direction in axis_steps
        for left in records
        for right in records
    )
    checks.check("the transverse-sign product is soldered under proper rotations", soldered)
    bond_symmetric = all(
        phi(direction, left, right) == phi(negate(direction), right, left)
        for direction in axis_steps
        for left in records
        for right in records
    )
    checks.check("the transverse-sign factor is bond-symmetric", bond_symmetric)

    means_zero = all(
        sum(transverse_sign(direction, point) for point in records) == 0 for direction in axis_steps
    )
    disjoint = all(
        sum(1 for direction in axis_steps if transverse_sign(direction, point)) <= 1 for point in records
    )
    checks.check(
        "the six transverse signs have mean 0 and disjoint supports",
        means_zero and disjoint,
    )

    moment_one = True
    for signs in product((-1, 0, 1), repeat=6):
        total = Fraction(0)
        for point in records:
            weight = Fraction(1)
            for direction, sign in zip(axis_steps, signs):
                weight *= 1 + KAPPA * transverse_sign(direction, point) * sign
            total += weight
        if total / len(records) != 1:
            moment_one = False
            break
    checks.check("all 729 partner patterns have product mean 1", moment_one)

    values = {
        phi(direction, left, right)
        for direction in axis_steps
        for left in records
        for right in records
    }
    checks.check(
        "the factor at coefficient 1/2 takes values 1/2, 1, and 3/2",
        values == {Fraction(1, 2), Fraction(1), Fraction(3, 2)},
    )
    far_end = all(
        sum(phi(direction, left, right) for right in records) == 48
        for direction in axis_steps
        for left in records
    )
    checks.check("every far-end sum equals 48", far_end)

    up = (0, 0, 1)
    first = (1, 2, 3)
    second = (-2, 1, 3)
    partner = (1, 2, -3)
    transverse_first = transverse_sign(up, first) * transverse_sign(negate(up), partner)
    transverse_second = transverse_sign(up, second) * transverse_sign(negate(up), partner)
    chiral_first = chirality_cap(up, first, positive) * chirality_cap(negate(up), partner, positive)
    chiral_second = chirality_cap(up, second, positive) * chirality_cap(negate(up), partner, positive)
    cross_orbit = first in positive and partner not in positive and transverse_first != 0
    not_proportional = transverse_first == 1 and transverse_second == -1 and chiral_first == chiral_second == -1
    checks.check(
        "two bonds from opposite orbits forbid every scale of the chiral cap",
        cross_orbit and not_proportional and second in positive,
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
