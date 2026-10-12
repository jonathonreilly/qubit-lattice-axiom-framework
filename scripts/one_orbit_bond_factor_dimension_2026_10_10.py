#!/usr/bin/env python3
"""Dimension of soldered bond-symmetric factors on one (1, 2, 3) orbit."""

from __future__ import annotations

from collections import Counter
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


def bond_key(direction, left, right):
    forward = (direction, left, right)
    backward = (tuple(-coordinate for coordinate in direction), right, left)
    return tuple(sorted((forward, backward)))


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
    seed = (1, 2, 3)
    orbit = sorted({apply(matrix, seed) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    checks.check(
        "stabilizer of the seed is trivial",
        sum(apply(matrix, seed) == seed for matrix in group) == 1,
    )
    swapped = (2, 1, 3)
    checks.check("axis swap of the seed is outside this orbit", swapped not in orbit)

    directions = []
    for axis in range(3):
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[axis] = sign
            directions.append(tuple(vector))
    checks.check("six axis directions", len(directions) == 6)
    pair_orbits = {
        frozenset(
            (apply(matrix, direction), apply(matrix, left)) for matrix in group
        )
        for direction in directions
        for left in orbit
    }
    checks.check(
        "six orbits of a direction and one record",
        len(pair_orbits) == 6,
    )

    seen: dict[frozenset, int] = {}
    for direction in directions:
        for left in orbit:
            for right in orbit:
                images = frozenset(
                    bond_key(
                        apply(matrix, direction),
                        apply(matrix, left),
                        apply(matrix, right),
                    )
                    for matrix in group
                )
                if images not in seen:
                    seen[images] = len(seen)
    dimension = len(seen)
    sizes = Counter(len(images) for images in seen)
    key_lengths = Counter(len(next(iter(images))) for images in seen)
    checks.check("bond-symmetric covariant dimension is 84", dimension == 84)
    checks.check(
        "60 orbits have 24 images and 24 orbits have 12",
        sizes == Counter({24: 60, 12: 24}),
    )
    checks.check("no bond equals its reverse", key_lengths == Counter({2: 84}))
    ordered_seen: set[frozenset] = set()
    for direction in directions:
        for left in orbit:
            for right in orbit:
                ordered_seen.add(
                    frozenset(
                        (
                            apply(matrix, direction),
                            apply(matrix, left),
                            apply(matrix, right),
                        )
                        for matrix in group
                    )
                )
    checks.check("ordered covariant bonds form 144 orbits", len(ordered_seen) == 144)

    rows = []
    seen_rows = set()
    for direction in directions:
        for left in orbit:
            row = [0] * dimension
            for right in orbit:
                images = frozenset(
                    bond_key(
                        apply(matrix, direction),
                        apply(matrix, left),
                        apply(matrix, right),
                    )
                    for matrix in group
                )
                row[seen[images]] += 1
            key = tuple(row)
            if key not in seen_rows:
                seen_rows.add(key)
                rows.append(row)
    checks.check("six distinct normalisation rows", len(rows) == 6)
    checks.check("normalisation rank is 6", rank(rows) == 6)
    checks.check(
        "each normalisation row sums to 24",
        all(sum(row) == 24 for row in rows),
    )
    checks.check("a one-dimensional stand-in is not this space", dimension != 1)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
