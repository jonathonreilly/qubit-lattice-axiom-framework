#!/usr/bin/env python3
"""One-hot cap-pair kernels are spanned by caps and two crosses."""

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


def dot(point: tuple[int, ...], direction: tuple[int, int, int]) -> int:
    return sum(left * right for left, right in zip(point, direction))


def bond_key(direction, left, right):
    forward = (direction, left, right)
    backward = (negate(direction), right, left)
    return tuple(sorted((forward, backward)))


def cap(point: tuple[int, ...], direction: tuple[int, int, int], level: int) -> int:
    axis = next(index for index, coordinate in enumerate(direction) if coordinate)
    if point[axis] != direction[axis] * level:
        return 0
    transverse = [point[index] for index in range(3) if index != axis]
    return 1 if transverse[0] * transverse[1] > 0 else -1


def sign_of(value: int) -> int:
    if value == 0:
        return 0
    return 1 if value > 0 else -1


def cross_raw(orientation: int, swapped: bool, height: int, left, right) -> int:
    if left[2] != orientation * height or right[2] != -orientation * height:
        return 0
    matched = abs(left[0]) == abs(right[0]) and abs(left[1]) == abs(right[1])
    crossed = abs(left[0]) == abs(right[1]) and abs(left[1]) == abs(right[0])
    if swapped:
        if not crossed:
            return 0
    elif not matched:
        return 0
    value = sign_of(left[0] * right[1] - left[1] * right[0])
    if orientation == -1 and swapped:
        return -value
    return value


def rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank_now = 0
    columns = len(matrix[0])
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

    def allowed(sign: int, modulus: int, direction, left, right) -> bool:
        level = sign * modulus
        return dot(left, direction) == level and dot(right, direction) == -level

    soldered_patterns = True
    one_hit = True
    for sign in (1, -1):
        for modulus in (1, 2, 3):
            for point in orbit:
                hits = [
                    direction
                    for direction in axis_steps
                    if dot(point, direction) == sign * modulus
                ]
                if len(hits) != 1:
                    one_hit = False
            for direction in axis_steps:
                for left in orbit:
                    for right in orbit:
                        if not allowed(sign, modulus, direction, left, right):
                            continue
                        for matrix in group:
                            if not allowed(
                                sign,
                                modulus,
                                apply(matrix, direction),
                                apply(matrix, left),
                                apply(matrix, right),
                            ):
                                soldered_patterns = False
    checks.check("each cap pattern gives one direction on every record", one_hit)
    checks.check("each cap pattern is preserved by proper rotations", soldered_patterns)

    pattern_orbits = {}
    orbit_counts = []
    slice_ranks = []
    kernel_dims = []
    for sign in (1, -1):
        for modulus in (1, 2, 3):
            seen: dict[frozenset, int] = {}
            for direction in axis_steps:
                for left in orbit:
                    for right in orbit:
                        if not allowed(sign, modulus, direction, left, right):
                            continue
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
            rows = []
            seen_rows = set()
            for direction in axis_steps:
                for right in orbit:
                    row = [0] * len(seen)
                    used = False
                    for left in orbit:
                        if not allowed(sign, modulus, direction, left, right):
                            continue
                        images = frozenset(
                            bond_key(
                                apply(matrix, direction),
                                apply(matrix, left),
                                apply(matrix, right),
                            )
                            for matrix in group
                        )
                        row[seen[images]] += 1
                        used = True
                    if used:
                        key = tuple(row)
                        if key not in seen_rows:
                            seen_rows.add(key)
                            rows.append(row)
            orbit_counts.append(len(seen))
            slice_ranks.append(rank(rows))
            kernel_dims.append(len(seen) - rank(rows))
            pattern_orbits[(sign, modulus)] = seen
    checks.check("each cap pattern has four bond orbits", orbit_counts == [4, 4, 4, 4, 4, 4])
    checks.check("each cap pattern has slice rank 1", slice_ranks == [1, 1, 1, 1, 1, 1])
    checks.check("each cap pattern has kernel dimension 3", kernel_dims == [3, 3, 3, 3, 3, 3])
    checks.check("the six cap patterns have dimension 18", sum(kernel_dims) == 18)

    def kernel(orientation: int, swapped: bool, height: int, direction, left, right) -> int:
        inverse = transpose(carriers[direction][0])
        return cross_raw(
            orientation,
            swapped,
            height,
            apply(inverse, left),
            apply(inverse, right),
        )

    def cap_kernel(level: int, direction, left, right) -> int:
        return cap(left, direction, level) * cap(right, negate(direction), level)

    well_defined = True
    for orientation in (1, -1):
        for swapped in (False, True):
            for height in (1, 2, 3):
                for direction, matrices in carriers.items():
                    for left in orbit:
                        for right in orbit:
                            values = set()
                            for matrix in matrices:
                                inverse = transpose(matrix)
                                values.add(
                                    cross_raw(
                                        orientation,
                                        swapped,
                                        height,
                                        apply(inverse, left),
                                        apply(inverse, right),
                                    )
                                )
                            if len(values) != 1:
                                well_defined = False
    checks.check("soldered extension of the twelve crosses is well defined", well_defined)

    symmetric = all(
        kernel(orientation, swapped, height, direction, left, right)
        == kernel(orientation, swapped, height, negate(direction), right, left)
        for orientation in (1, -1)
        for swapped in (False, True)
        for height in (1, 2, 3)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    )
    checks.check("the twelve crosses are bond-symmetric", symmetric)

    on_pattern = True
    for sign in (1, -1):
        for modulus in (1, 2, 3):
            for swapped in (False, True):
                for direction in axis_steps:
                    for left in orbit:
                        for right in orbit:
                            value = kernel(sign, swapped, modulus, direction, left, right)
                            if value and not allowed(sign, modulus, direction, left, right):
                                on_pattern = False
                            cap_value = cap_kernel(sign * modulus, direction, left, right)
                            if cap_value and not allowed(sign, modulus, direction, left, right):
                                on_pattern = False
    checks.check("caps and crosses vanish off their cap pattern", on_pattern)

    positive_witnesses = {
        (False, 1): ((-3, 2, 1), (3, 2, -1)),
        (False, 2): ((-3, -1, 2), (-3, 1, -2)),
        (False, 3): ((-2, 1, 3), (2, 1, -3)),
        (True, 1): ((-3, 2, 1), (-2, 3, -1)),
        (True, 2): ((-3, -1, 2), (1, 3, -2)),
        (True, 3): ((-2, 1, 3), (-1, 2, -3)),
    }
    witness_ok = all(
        left in orbit
        and right in orbit
        and kernel(1, swapped, height, upward, left, right) == -1
        for (swapped, height), (left, right) in positive_witnesses.items()
    )
    checks.check("six positive-cap witness bonds have value -1", witness_ok)

    values = {
        kernel(1, swapped, height, direction, left, right)
        for swapped in (False, True)
        for height in (1, 2, 3)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("positive-cap cross values lie in {-1, 0, 1}", values == {-1, 0, 1})

    one_live = True
    slice_mean = True
    for swapped in (False, True):
        for height in (1, 2, 3):
            for point in orbit:
                live = [
                    direction
                    for direction in axis_steps
                    if any(
                        kernel(1, swapped, height, direction, point, right) for right in orbit
                    )
                ]
                if len(live) != 1:
                    one_live = False
            for direction in axis_steps:
                for right in orbit:
                    if (
                        sum(kernel(1, swapped, height, direction, point, right) for point in orbit)
                        != 0
                    ):
                        slice_mean = False
    checks.check("each positive-cap cross activates one direction", one_live)
    checks.check("every positive-cap slice has sum 0", slice_mean)

    bonds = [
        (direction, left, right)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    ]

    def cross_row(orientation: int, swapped: bool, height: int) -> list[int]:
        return [
            kernel(orientation, swapped, height, direction, left, right)
            for direction, left, right in bonds
        ]

    def cap_row(level: int) -> list[int]:
        return [
            cap_kernel(level, direction, left, right) for direction, left, right in bonds
        ]

    levels = (-3, -2, -1, 1, 2, 3)
    prior = [cap_row(level) for level in levels]
    prior += [cross_row(-1, False, height) for height in (1, 2, 3)]
    prior += [cross_row(-1, True, height) for height in (1, 2, 3)]
    positive_rows = [cross_row(1, False, height) for height in (1, 2, 3)]
    positive_rows += [cross_row(1, True, height) for height in (1, 2, 3)]
    outside = rank(prior) == 12 and all(
        rank(prior + [row]) == 13 for row in positive_rows
    )
    checks.check(
        "each positive-cap cross lies outside the previous twelve kernels",
        outside,
    )
    checks.check(
        "the eighteen kernels are linearly independent",
        rank(prior + positive_rows) == 18,
    )

    spans = True
    for sign in (1, -1):
        for modulus in (1, 2, 3):
            seen = pattern_orbits[(sign, modulus)]
            vectors = []
            for builder in (
                lambda direction, left, right, level=sign * modulus: cap_kernel(
                    level, direction, left, right
                ),
                lambda direction, left, right, sign=sign, modulus=modulus: kernel(
                    sign, False, modulus, direction, left, right
                ),
                lambda direction, left, right, sign=sign, modulus=modulus: kernel(
                    sign, True, modulus, direction, left, right
                ),
            ):
                vector = [0] * len(seen)
                for images, index in seen.items():
                    values_on_orbit = set()
                    for key in images:
                        direction, left, right = key[0]
                        values_on_orbit.add(builder(direction, left, right))
                    if len(values_on_orbit) != 1:
                        spans = False
                    vector[index] = next(iter(values_on_orbit))
                vectors.append(vector)
            if rank(vectors) != 3:
                spans = False
    checks.check("cap and two crosses span each three-dimensional pattern", spans)

    positive = {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
    seen_values = {
        1 + Fraction(1, 2) * kernel(1, swapped, height, direction, left, right)
        for swapped in (False, True)
        for height in (1, 2, 3)
        for direction in axis_steps
        for left in orbit
        for right in orbit
    }
    checks.check("half-parameter positive-cap factors stay positive", seen_values == positive)

    def mixed(direction, left, right) -> int:
        return kernel(1, False, 1, direction, left, right) + kernel(
            1, False, 2, direction, left, right
        )

    moment = Fraction(
        sum(
            (1 + mixed((-1, 0, 0), point, (1, -2, -3)))
            * (1 + mixed((0, -1, 0), point, (-1, 2, -3)))
            for point in orbit
        ),
        len(orbit),
    )
    checks.check(
        "the sum of two positive matched crosses has moment 23/24",
        (1, -2, -3) in orbit and (-1, 2, -3) in orbit and moment == Fraction(23, 24),
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
