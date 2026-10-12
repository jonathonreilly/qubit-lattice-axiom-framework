#!/usr/bin/env python3
"""Inside the three-cap span, order-blind factors are the three axes."""

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


def cap(point: tuple[int, ...], direction: tuple[int, ...], modulus: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * modulus:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def expectation(orbit, function) -> Fraction:
    return Fraction(sum(function(point) for point in orbit), len(orbit))


def main() -> None:
    checks = Checks()
    group = proper()
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    moduli = (1, 2, 3)
    positive = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    negative = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))

    one_hot = all(
        sum(cap(point, direction, modulus) != 0 for modulus in moduli) <= 1
        for point in orbit
        for direction in positive + negative
    )
    checks.check("one modulus cap is live on a direction", one_hot)
    means_zero = all(
        expectation(orbit, lambda point, direction=direction, modulus=modulus: cap(point, direction, modulus))
        == 0
        for modulus in moduli
        for direction in positive
    )
    checks.check("each positive-axis cap has mean 0", means_zero)

    def pair(first, second, left, right) -> Fraction:
        return expectation(
            orbit,
            lambda point, first=first, second=second, left=left, right=right: (
                cap(point, first, left) * cap(point, second, right)
            ),
        )

    perpendicular = True
    for first, second in ((positive[0], positive[1]), (positive[0], positive[2]), (positive[1], positive[2])):
        for left in moduli:
            for right in moduli:
                value = pair(first, second, left, right)
                expected = 0 if left == right else Fraction(1, 24)
                if value != expected:
                    perpendicular = False
    checks.check("perpendicular caps correlate by 1/24 off diagonal", perpendicular)

    triple = {
        (left, middle, right): expectation(
            orbit,
            lambda point, left=left, middle=middle, right=right: (
                cap(point, positive[0], left)
                * cap(point, positive[1], middle)
                * cap(point, positive[2], right)
            ),
        )
        for left in moduli
        for middle in moduli
        for right in moduli
    }
    cycles = {(1, 2, 3): Fraction(1, 24), (2, 3, 1): Fraction(1, 24), (3, 1, 2): Fraction(1, 24)}
    checks.check(
        "the triple correlations are the three modulus cycles",
        all(triple[key] == cycles.get(key, 0) for key in triple),
    )
    direct = expectation(
        orbit,
        lambda point: (
            sum(cap(point, positive[0], modulus) for modulus in moduli)
            * sum(cap(point, positive[1], modulus) for modulus in moduli)
            * sum(cap(point, positive[2], modulus) for modulus in moduli)
        ),
    )
    checks.check("equal cap weights have triple mean 1/8", direct == Fraction(1, 8))

    neighbours_exist = all(
        any(cap(point, direction, modulus) == 1 for point in orbit)
        for direction in negative
        for modulus in moduli
    )
    checks.check("each opposite cap has a sign of +1", neighbours_exist)

    def shape(point, direction, weights: tuple[int, int, int]) -> int:
        return sum(weights[index] * cap(point, direction, moduli[index]) for index in range(3))

    def moment(weights, directions, neighbour_values) -> Fraction:
        def product_at(point):
            value = 1
            for direction, neighbour in zip(directions, neighbour_values):
                value *= 1 + shape(point, direction, weights) * neighbour
            return value

        return expectation(orbit, product_at)

    two = moment((1, 1, 0), (positive[0], positive[1]), (1, 1))
    checks.check("moduli 1 and 2 have two-neighbour moment 13/12", two == Fraction(13, 12))
    # Neighbour value on a positive modulus-1 cap is the first weight, -2.
    mixed = moment((-2, -2, 1), positive, (-2, -2, -2))
    checks.check("the cancelling mixture has three-neighbour moment -3", mixed == -3)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
