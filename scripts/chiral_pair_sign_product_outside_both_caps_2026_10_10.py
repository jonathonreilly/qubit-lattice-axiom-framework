#!/usr/bin/env python3
"""The sign-product cap on the chiral pair is order-blind and off both exhibited lines."""

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

    def cap_chirality(direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        if dot(point, direction) != 3:
            return 0
        return chirality[point]

    def sign_product(direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        return chirality[point] * transverse_sign(direction, point)

    invariant = all(
        chirality[apply(matrix, point)] == chirality[point] for matrix in group for point in records
    )
    one_cap = all(
        sum(1 for direction in axis_steps if dot(point, direction) == 3) == 1 for point in records
    )
    means_zero = all(
        sum(cap_chirality(direction, point) for point in records) == 0
        and sum(transverse_sign(direction, point) for point in records) == 0
        and sum(sign_product(direction, point) for point in records) == 0
        for direction in axis_steps
    )
    checks.check(
        "chirality is invariant, the caps are disjoint, and all three cap signs have mean 0",
        invariant and one_cap and means_zero,
    )

    cocycle_ok = True
    flips = False
    for matrix in group:
        for direction in axis_steps:
            ratios = {
                transverse_sign(apply(matrix, direction), apply(matrix, point))
                * transverse_sign(direction, point)
                for point in records
                if transverse_sign(direction, point) != 0
            }
            opposite = {
                transverse_sign(apply(matrix, negate(direction)), apply(matrix, point))
                * transverse_sign(negate(direction), point)
                for point in records
                if transverse_sign(negate(direction), point) != 0
            }
            if ratios != opposite or len(ratios) != 1:
                cocycle_ok = False
            if ratios == {-1}:
                flips = True
    checks.check(
        "the transverse sign flips by one global sign shared with the opposite direction",
        cocycle_ok and flips,
    )

    def kernel(
        kind: str,
        direction: tuple[int, int, int],
        left: tuple[int, int, int],
        right: tuple[int, int, int],
    ) -> int:
        if kind == "chiral":
            return cap_chirality(direction, left) * cap_chirality(negate(direction), right)
        if kind == "transverse":
            return transverse_sign(direction, left) * transverse_sign(negate(direction), right)
        return sign_product(direction, left) * sign_product(negate(direction), right)

    soldered = all(
        kernel("product", apply(matrix, direction), apply(matrix, left), apply(matrix, right))
        == kernel("product", direction, left, right)
        for matrix in group
        for direction in axis_steps
        for left in records
        for right in records
    )
    checks.check("the sign-product kernel is soldered under proper rotations", soldered)
    bond_symmetric = all(
        kernel("product", direction, left, right) == kernel("product", negate(direction), right, left)
        for direction in axis_steps
        for left in records
        for right in records
    )
    checks.check("the sign-product factor is bond-symmetric", bond_symmetric)

    moment_one = True
    for signs in product((-1, 0, 1), repeat=6):
        total = Fraction(0)
        for point in records:
            weight = Fraction(1)
            for direction, sign in zip(axis_steps, signs):
                weight *= 1 + KAPPA * sign_product(direction, point) * sign
            total += weight
        if total / len(records) != 1:
            moment_one = False
            break
    checks.check("all 729 partner patterns have product mean 1", moment_one)

    values = {
        1 + KAPPA * kernel("product", direction, left, right)
        for direction in axis_steps
        for left in records
        for right in records
    }
    checks.check(
        "the factor at coefficient 1/2 takes values 1/2, 1, and 3/2",
        values == {Fraction(1, 2), Fraction(1), Fraction(3, 2)},
    )
    far_end = all(
        sum(1 + KAPPA * kernel("product", direction, left, right) for right in records) == 48
        for direction in axis_steps
        for left in records
    )
    checks.check("every far-end sum equals 48", far_end)

    up = (0, 0, 1)
    partner = (-2, -1, -3)
    lefts = ((1, 2, 3), (2, -1, 3), (-2, -1, 3))
    rows = [
        [kernel(kind, up, left, partner) for kind in ("chiral", "transverse", "product")]
        for left in lefts
    ]
    expected = [[1, 1, 1], [1, -1, -1], [-1, 1, -1]]
    idle = (1, 2, 3)
    zero_bond = all(kernel(kind, up, idle, idle) == 0 for kind in ("chiral", "transverse", "product"))
    checks.check(
        "three bonds to (-2, -1, -3) have determinant 4 against the two caps",
        partner in records
        and dot(partner, negate(up)) == 3
        and rows == expected
        and det3(rows) == 4
        and zero_bond,
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
