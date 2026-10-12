#!/usr/bin/env python3
"""Two cross-height cap mixtures, one with moment 97/96 and one with mean 1."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180

KAPPA = Fraction(1, 2)
WITNESS_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
WITNESS_ENDS = ((1, -3, -2), (-3, 2, -1))
WITNESS_MOMENT = Fraction(97, 96)
FAILING_PAIRS = 1536


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
    first, second, third = matrix
    return (
        first[0] * (second[1] * third[2] - second[2] * third[1])
        - first[1] * (second[0] * third[2] - second[2] * third[0])
        + first[2] * (second[0] * third[1] - second[1] * third[0])
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
    return tuple(sum(matrix[row][col] * vector[col] for col in range(3)) for row in range(3))


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
    chirality = {point: (1 if point in positive else -1) for point in records}
    count = len(records)

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

    def cap_kernel(kind: str, height: int, direction: tuple[int, int, int], left, right) -> int:
        return cap_sign(kind, height, direction, left) * cap_sign(kind, height, negate(direction), right)

    def factor(parts: tuple[tuple[str, int], ...], direction, left, right) -> Fraction:
        total = Fraction(1)
        for kind, height in parts:
            total += KAPPA * cap_kernel(kind, height, direction, left, right)
        return total

    failing = (("chi", 1), ("chi", 2))
    passing = (("chi", 1), ("prod", 2))

    def covariance(parts: tuple[tuple[str, int], ...]) -> bool:
        soldered = all(
            factor(parts, apply(matrix, direction), apply(matrix, left), apply(matrix, right))
            == factor(parts, direction, left, right)
            for matrix in group
            for direction in axis_steps
            for left in records
            for right in records
        )
        bond_symmetric = all(
            factor(parts, direction, left, right) == factor(parts, negate(direction), right, left)
            for direction in axis_steps
            for left in records
            for right in records
        )
        return soldered and bond_symmetric

    checks.check(
        "both cross-height mixtures are soldered and bond-symmetric",
        covariance(failing) and covariance(passing),
    )

    def value_set(parts: tuple[tuple[str, int], ...]) -> set[Fraction]:
        return {
            factor(parts, direction, left, right)
            for direction in axis_steps
            for left in records
            for right in records
        }

    positive_values = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    checks.check(
        "each mixture at coefficient 1/2 takes values 1/2, 1, and 3/2",
        value_set(failing) == positive_values and value_set(passing) == positive_values,
    )

    def live_directions(parts: tuple[tuple[str, int], ...], left) -> list[tuple[int, int, int]]:
        found = []
        for direction in axis_steps:
            if any(factor(parts, direction, left, right) != 1 for right in records):
                found.append(direction)
        return found

    live_ok = True
    both_heights = False
    for parts in (failing, passing):
        for left in records:
            live = live_directions(parts, left)
            if len(live) > 2:
                live_ok = False
            if len(live) == 2 and live[0] == negate(live[1]):
                live_ok = False
            heights = []
            for direction in live:
                for kind, height in parts:
                    if any(cap_kernel(kind, height, direction, left, right) for right in records):
                        heights.append(height)
            if sorted(heights) == [1, 2]:
                both_heights = True
    checks.check(
        "each record meets at most two live directions and both heights occur",
        live_ok and both_heights,
    )

    def one_neighbour(parts: tuple[tuple[str, int], ...]) -> bool:
        return all(
            sum(factor(parts, direction, left, right) for left in records) == count
            for direction in axis_steps
            for right in records
        )

    def two_neighbour(parts: tuple[tuple[str, int], ...]) -> tuple[int, Fraction]:
        bad = 0
        witness = Fraction(0)
        for first_index, first in enumerate(axis_steps):
            for second in axis_steps[first_index + 1 :]:
                for right_a in records:
                    for right_b in records:
                        total = sum(
                            factor(parts, first, left, right_a) * factor(parts, second, left, right_b)
                            for left in records
                        )
                        if total != count:
                            bad += 1
                        if (
                            (first, second) == WITNESS_DIRECTIONS
                            and (right_a, right_b) == WITNESS_ENDS
                        ):
                            witness = Fraction(total, count)
                        if (
                            (second, first) == WITNESS_DIRECTIONS
                            and (right_b, right_a) == WITNESS_ENDS
                        ):
                            witness = Fraction(total, count)
        return bad, witness

    failing_one = one_neighbour(failing)
    passing_one = one_neighbour(passing)
    failing_bad, failing_witness = two_neighbour(failing)
    passing_bad, passing_witness = two_neighbour(passing)
    checks.check(
        "the two chirality caps have one-neighbour mean 1 and witness moment 97/96",
        failing_one and failing_witness == WITNESS_MOMENT and failing_bad == FAILING_PAIRS,
    )
    checks.check(
        "the chirality cap plus the other-height sign product has every two-direction mean equal to 1",
        passing_one and passing_bad == 0 and passing_witness == 1,
    )
    far_end = all(
        sum(factor(parts, direction, left, right) for right in records) == count
        for parts in (failing, passing)
        for direction in axis_steps
        for left in records
    )
    checks.check("every far-end sum equals 48", far_end)
    print(f"FAILING witness moment {failing_witness} bad_pairs {failing_bad}")
    print(f"PASSING witness moment {passing_witness} bad_pairs {passing_bad}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
