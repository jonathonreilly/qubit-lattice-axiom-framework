#!/usr/bin/env python3
"""Cross moments of the chirality, transverse-sign, and matched line."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180

KERNELS = (
    "chi",
    "ts",
    "prod",
    "matched",
    "swapped",
    "parallel",
    "oblique",
    "swapped_dot",
    "orthogonal",
    "scaled",
)
PARITY = ("chi", "ts", "prod", "swapped", "parallel", "oblique", "orthogonal")
EXCLUDED = ("matched", "swapped_dot", "scaled")
ORDERED_PAIRS = ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2))
SAME_PAIRS = {(1, 2), (2, 1), (2, 3), (3, 2)}
PASS_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
PASS_LEFTS = ((-1, -2, -3), (-1, -2, 3))
PASS_RIGHTS = ((1, -3, -2), (-1, 2, -3))
FAIL_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
FAIL_LEFTS = ((-1, -3, -2), (-1, -3, 2))
FAIL_RIGHTS = ((1, -2, 3), (-1, 3, -2))


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


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [[matrix[row][col] for row in range(3)] for col in range(3)]


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


def seed_cross(height: int, left: tuple[int, int, int], right: tuple[int, int, int], swapped: bool) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if swapped:
        matched_abs = abs(x_coord) == abs(y_prime) and abs(y_coord) == abs(x_prime)
    else:
        matched_abs = abs(x_coord) == abs(x_prime) and abs(y_coord) == abs(y_prime)
    if not matched_abs:
        return 0
    raw = x_coord * y_prime - y_coord * x_prime
    if raw == 0:
        return 0
    return 1 if raw > 0 else -1


def seed_parallel(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if x_coord * y_prime - y_coord * x_prime != 0:
        return 0
    raw = x_coord * x_prime + y_coord * y_prime
    if raw == 0:
        return 0
    return -1 if raw > 0 else 1


def seed_oblique(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if abs(x_coord) != abs(x_prime) or abs(y_coord) != abs(y_prime):
        return 0
    if x_coord * y_prime - y_coord * x_prime == 0:
        return 0
    raw = x_coord * x_prime + y_coord * y_prime
    if raw == 0:
        return 0
    return -1 if raw > 0 else 1


def seed_swapped(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if abs(x_coord) != abs(y_prime) or abs(y_coord) != abs(x_prime):
        return 0
    raw = x_coord * x_prime + y_coord * y_prime
    if raw == 0:
        return 0
    return -1 if raw > 0 else 1


def seed_scaled(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    cross = x_coord * y_prime - y_coord * x_prime
    dot_product = x_coord * x_prime + y_coord * y_prime
    if cross == 0 or dot_product == 0:
        return 0
    signed = -1 if cross * dot_product > 0 else 1
    matched = abs(x_coord) == abs(x_prime) and abs(y_coord) == abs(y_prime)
    swapped = abs(x_coord) == abs(y_prime) and abs(y_coord) == abs(x_prime)
    if matched and dot_product > 0:
        return 2 * signed
    if swapped:
        return signed
    return 0


def seed_orthogonal(height: int, left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    x_coord, y_coord, z_coord = left
    x_prime, y_prime, z_prime = right
    if z_coord != height or z_prime != -height:
        return 0
    if abs(x_coord) != abs(y_prime) or abs(y_coord) != abs(x_prime):
        return 0
    if x_coord * x_prime + y_coord * y_prime != 0:
        return 0
    raw = x_coord * y_prime - y_coord * x_prime
    if raw == 0:
        return 0
    return 1 if raw > 0 else -1


def rank(rows: list[list[int]]) -> int:
    if not rows:
        return 0
    width = len(rows[0])
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    pivot_column = 0
    found = 0
    for row_index in range(len(matrix)):
        if pivot_column >= width:
            break
        pivot = None
        while pivot_column < width:
            pivot = next(
                (probe for probe in range(row_index, len(matrix)) if matrix[probe][pivot_column] != 0),
                None,
            )
            if pivot is not None:
                break
            pivot_column += 1
        if pivot is None:
            break
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        scale = matrix[row_index][pivot_column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][pivot_column] == 0:
                continue
            factor = matrix[other][pivot_column]
            matrix[other] = [
                matrix[other][column] - factor * matrix[row_index][column] for column in range(width)
            ]
        found += 1
        pivot_column += 1
    return found


def axis_index(direction: tuple[int, int, int]) -> int:
    return next(index for index, coordinate in enumerate(direction) if coordinate)


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


def kernel_vector(**values: int) -> list[int]:
    vector = [0 for _ in KERNELS]
    index = {name: position for position, name in enumerate(KERNELS)}
    for name, value in values.items():
        vector[index[name]] = value
    return vector


SPAN_PLUS = (
    kernel_vector(matched=1, oblique=1),
    kernel_vector(swapped=-1, swapped_dot=1, orthogonal=1),
    kernel_vector(ts=-1, prod=-1, matched=2, scaled=2),
)
SPAN_MINUS = (
    kernel_vector(matched=-1, oblique=1),
    kernel_vector(swapped=-1, swapped_dot=-1, orthogonal=1),
    kernel_vector(ts=1, prod=1, matched=2, scaled=2),
)


def pattern(vector: list[int]) -> bool:
    index = {name: position for position, name in enumerate(KERNELS)}
    parity = sum(vector[index[name]] != 0 for name in PARITY)
    excluded = sum(vector[index[name]] != 0 for name in EXCLUDED)
    return parity >= 2 and excluded >= 1


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    records = alphabet()
    positive = {apply(matrix, (1, 2, 3)) for matrix in group}
    other = [point for point in records if point not in positive]
    checks.check(
        "the alphabet is the chiral pair of two proper orbits",
        len(records) == 48 and len(positive) == 24 and len(other) == 24 and (2, 1, 3) in other,
    )
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6 and len(set(axis_steps)) == 6)
    chirality = {point: (1 if point in positive else -1) for point in records}
    up = (0, 0, 1)
    frames = {direction: [matrix for matrix in group if apply(matrix, up) == direction] for direction in axis_steps}
    record_index = {point: index for index, point in enumerate(records)}
    direction_index = {direction: index for index, direction in enumerate(axis_steps)}

    def cap_sign(kind: str, height: int, direction: tuple[int, int, int], point: tuple[int, int, int]) -> int:
        if dot(point, direction) != height:
            return 0
        axis = axis_index(direction)
        transverse = [point[index] for index in range(3) if index != axis]
        transverse_sign = 1 if transverse[0] * transverse[1] > 0 else -1
        orbit_sign = chirality[point]
        if kind == "chi":
            return orbit_sign
        if kind == "ts":
            return transverse_sign
        return orbit_sign * transverse_sign

    def raw_kernel(name: str, height: int, direction, left, right) -> int:
        if name in ("chi", "ts", "prod"):
            return cap_sign(name, height, direction, left) * cap_sign(name, height, negate(direction), right)
        seeds = {
            "matched": lambda level, a, b: seed_cross(level, a, b, False),
            "swapped": lambda level, a, b: seed_cross(level, a, b, True),
            "parallel": seed_parallel,
            "oblique": seed_oblique,
            "swapped_dot": seed_swapped,
            "orthogonal": seed_orthogonal,
            "scaled": seed_scaled,
        }
        inverse = transpose(frames[direction][0])
        return seeds[name](height, apply(inverse, left), apply(inverse, right))

    tables: dict[int, list] = {}
    for height in (1, 2, 3):
        tables[height] = [[[None for _ in records] for _ in records] for _ in axis_steps]
        for direction in axis_steps:
            dir_id = direction_index[direction]
            for left in records:
                if dot(left, direction) != height:
                    continue
                for right in records:
                    if dot(right, direction) != -height:
                        continue
                    tables[height][dir_id][record_index[left]][record_index[right]] = [
                        raw_kernel(name, height, direction, left, right) for name in KERNELS
                    ]

    def entry(height: int, direction, left, right) -> list[int]:
        return tables[height][direction_index[direction]][record_index[left]][record_index[right]]

    line_vector = kernel_vector(chi=1, ts=1, matched=1)
    index = {name: position for position, name in enumerate(KERNELS)}
    outside = line_vector[index["chi"]] == 1 and line_vector[index["ts"]] == 1 and line_vector[index["matched"]] == 1
    outside = outside and sum(line_vector) == 3 and pattern(line_vector)
    for span in (SPAN_PLUS, SPAN_MINUS):
        for vector in span:
            if vector[index["chi"]] != 0:
                outside = False
    checks.check(
        "the equal-coefficient line is outside both ratio spans and has two parity coefficients plus one excluded coefficient",
        outside,
    )

    def partner_rows(height_a: int, height_b: int, vector: list[int]) -> list[list[int]]:
        rows = []
        for first in axis_steps:
            for second in axis_steps:
                if axis_index(first) == axis_index(second):
                    continue
                lefts = [
                    left
                    for left in records
                    if dot(left, first) == height_a and dot(left, second) == height_b
                ]
                for right_a in records:
                    if dot(right_a, first) != -height_a:
                        continue
                    for right_b in records:
                        if dot(right_b, second) != -height_b:
                            continue
                        samples_left = [
                            sum(vector[column] * entry(height_a, first, left, right_a)[column] for column in range(10))
                            for left in lefts
                        ]
                        row = []
                        for column in range(10):
                            total = 0
                            for offset, left in enumerate(lefts):
                                total += samples_left[offset] * entry(height_b, second, left, right_b)[column]
                            row.append(total)
                        if any(row):
                            rows.append(row)
        return rows

    full_rank = True
    for height_a, height_b in ORDERED_PAIRS:
        rows = partner_rows(height_a, height_b, line_vector)
        doubled = partner_rows(height_a, height_b, [2 * value for value in line_vector])
        if rank(rows) != 10 or doubled != [[2 * value for value in row] for row in rows]:
            full_rank = False
    checks.check(
        "every ordered height pair gives the line partner rank 10, and the doubled line doubles every partner row",
        full_rank,
    )

    def bond_cross(height_a, height_b, dirs, lefts, rights, coeffs_a, coeffs_b):
        first, second = dirs
        right_a, right_b = rights
        samples = []
        for left in lefts:
            value_a = sum(coeffs_a[column] * entry(height_a, first, left, right_a)[column] for column in range(10))
            value_b = sum(coeffs_b[column] * entry(height_b, second, left, right_b)[column] for column in range(10))
            samples.append((value_a, value_b))
        total = samples[0][0] * samples[0][1] + samples[1][0] * samples[1][1]
        return samples, total

    directions_xy = ((-1, 0, 0), (0, -1, 0))
    lefts = ((-1, -2, -3), (-1, -2, 3))
    rights = ((1, -3, -2), (-3, 2, -1))
    samples, total = bond_cross(1, 2, directions_xy, lefts, rights, line_vector, kernel_vector(chi=1))
    checks.check(
        "the line against the chirality cap has centre pairs (2, 1) and (-2, -1) and cross sum 4",
        samples == [(2, 1), (-2, -1)] and total == 4,
    )
    doubled_samples, doubled_total = bond_cross(
        1, 2, directions_xy, lefts, rights, [2 * value for value in line_vector], kernel_vector(chi=1)
    )
    checks.check(
        "twice the line has centre pairs (4, 1) and (-4, -1) and cross sum 8",
        doubled_samples == [(4, 1), (-4, -1)] and doubled_total == 8,
    )
    print(f"LINE witness {samples} {total}")
    print(f"DOUBLE witness {doubled_samples} {doubled_total}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
