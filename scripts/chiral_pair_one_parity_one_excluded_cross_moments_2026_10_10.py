#!/usr/bin/env python3
"""Cross moments of one parity kernel plus one excluded kernel."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

import sympy as sp

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
FLIP_PAIRS = {(1, 3), (3, 1)}
CHI_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
CHI_LEFTS = ((-1, -2, -3), (-1, -2, 3))
CHI_RIGHTS = ((1, -3, -2), (-3, 2, -1))
SELF_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
SELF_LEFTS = ((-1, -3, -2), (-1, -3, 2))
SELF_RIGHTS = ((1, -3, -2), (-1, 3, -2))
RATIO_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
RATIO_LEFTS = ((-1, -2, -3), (-1, -2, 3))
RATIO_RIGHTS = ((1, -2, -3), (-1, 2, -3))

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


def rank(rows: list[list[Fraction]]) -> int:
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


K_PLUS = (
    kernel_vector(matched=1, oblique=1),
    kernel_vector(swapped=-1, swapped_dot=1, orthogonal=1),
    kernel_vector(ts=-1, prod=-1, matched=2, scaled=2),
)
K_MINUS = (
    kernel_vector(matched=-1, oblique=1),
    kernel_vector(swapped=-1, swapped_dot=-1, orthogonal=1),
    kernel_vector(ts=1, prod=1, matched=2, scaled=2),
)


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
    kernel_index = {name: index for index, name in enumerate(KERNELS)}

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

    def bond_mats(height_a: int, height_b: int) -> list[list[list[int]]]:
        found = []
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
                    samples = [
                        [entry(height_a, first, left, right_a)[column] for left in lefts]
                        for column in range(10)
                    ]
                    if not any(any(sample) for sample in samples):
                        continue
                    for right_b in records:
                        if dot(right_b, second) != -height_b:
                            continue
                        mat = []
                        useful = False
                        for sample in samples:
                            row = [
                                sum(
                                    sample[offset] * entry(height_b, second, left, right_b)[column]
                                    for offset, left in enumerate(lefts)
                                )
                                for column in range(10)
                            ]
                            if any(row):
                                useful = True
                            mat.append(row)
                        if useful:
                            found.append(mat)
        return found

    def partner_rows(mats: list[list[list[int]]], coeffs: list[int]) -> list[list[Fraction]]:
        rows = []
        for mat in mats:
            row = [
                sum(Fraction(coeffs[index]) * mat[index][column] for index in range(10))
                for column in range(10)
            ]
            if any(row):
                rows.append(row)
        return rows

    def ratio_rows(mats: list[list[list[int]]], parity_index: int, excluded_index: int, ratio: Fraction):
        rows = []
        for mat in mats:
            row = [
                Fraction(mat[parity_index][column]) + ratio * mat[excluded_index][column]
                for column in range(10)
            ]
            if any(row):
                rows.append(row)
        return rows

    def minor_polynomial(mats, parity_index: int, excluded_index: int, pivot_ratio: int):
        work: list[list[Fraction]] = []
        picked = []
        for index, mat in enumerate(mats):
            row = [
                Fraction(mat[parity_index][column]) + Fraction(pivot_ratio) * mat[excluded_index][column]
                for column in range(10)
            ]
            if rank(work + [row]) == len(work) + 1:
                work.append(row)
                picked.append(index)
                if len(picked) == 10:
                    break
        if len(picked) != 10:
            return None
        ratio = sp.symbols("t")
        matrix = [
            [
                mats[index][parity_index][column] + ratio * mats[index][excluded_index][column]
                for column in range(10)
            ]
            for index in picked
        ]
        numer, _denom = sp.fraction(sp.together(sp.Matrix(matrix).det()))
        return sp.expand(numer)

    def rational_root(root) -> Fraction | None:
        root = sp.sympify(root)
        if not root.is_rational:
            return None
        return Fraction(int(root.p), int(root.q))

    planes_only_zero = True
    special_ratios = True
    for height_a, height_b in ORDERED_PAIRS:
        mats = bond_mats(height_a, height_b)
        for parity_name in PARITY:
            for excluded_name in EXCLUDED:
                parity_index = kernel_index[parity_name]
                excluded_index = kernel_index[excluded_name]
                special = parity_name == "oblique" and excluded_name == "matched"
                pivot = 2 if special else 1
                polynomial = minor_polynomial(mats, parity_index, excluded_index, pivot)
                if polynomial is None or polynomial == 0:
                    if special:
                        special_ratios = False
                    else:
                        planes_only_zero = False
                    continue
                roots = sp.roots(polynomial)
                if special:
                    found_roots = set()
                    for root in roots:
                        value = rational_root(root)
                        if value is None:
                            special_ratios = False
                            continue
                        found_roots.add(value)
                        if rank(ratio_rows(mats, parity_index, excluded_index, value)) != 7:
                            special_ratios = False
                    if found_roots != {Fraction(-1), Fraction(1)}:
                        special_ratios = False
                    if rank(ratio_rows(mats, parity_index, excluded_index, Fraction(2))) != 10:
                        special_ratios = False
                    continue
                for root in roots:
                    value = rational_root(root)
                    if value is None or value == 0:
                        continue
                    if rank(ratio_rows(mats, parity_index, excluded_index, value)) < 10:
                        planes_only_zero = False
    checks.check(
        "every other parity-excluded plane has full partner rank for a nonzero ratio",
        planes_only_zero,
    )
    checks.check(
        "the oblique-matched ratios with a partner kernel are exactly plus and minus one",
        special_ratios,
    )

    def in_kernel(mats, coeffs_x: list[int], coeffs_y: list[int]) -> bool:
        for row in partner_rows(mats, coeffs_x):
            if sum(row[column] * coeffs_y[column] for column in range(10)) != 0:
                return False
        return True

    kernels_match = True
    for height_a, height_b in ORDERED_PAIRS:
        mats = bond_mats(height_a, height_b)
        for ratio, same_kernel in ((1, K_PLUS), (-1, K_MINUS)):
            if (height_a, height_b) in SAME_PAIRS:
                kernel = same_kernel
            elif (height_a, height_b) in FLIP_PAIRS:
                kernel = K_MINUS if ratio == 1 else K_PLUS
            else:
                kernels_match = False
                continue
            coeffs_x = kernel_vector(oblique=1, matched=ratio)
            rows = partner_rows(mats, coeffs_x)
            if rank(rows) != 7 or rank([list(vector) for vector in kernel]) != 3:
                kernels_match = False
                continue
            if any(not in_kernel(mats, coeffs_x, list(vector)) for vector in kernel):
                kernels_match = False
    checks.check(
        "at ratios plus and minus one the named three vectors span the partner kernel",
        kernels_match,
    )

    def every_cross_zero(height_a: int, coeffs_a: list[int], height_b: int, coeffs_b: list[int]) -> bool:
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
                        cross = 0
                        for left in lefts:
                            value_a = sum(
                                coeffs_a[index] * entry(height_a, first, left, right_a)[index]
                                for index in range(10)
                            )
                            value_b = sum(
                                coeffs_b[index] * entry(height_b, second, left, right_b)[index]
                                for index in range(10)
                            )
                            cross += value_a * value_b
                        if cross != 0:
                            return False
        return True

    both = kernel_vector(oblique=1, matched=1)
    checks.check(
        "oblique plus matched at heights 1 and 2 has every cross sum equal to 0 against itself",
        every_cross_zero(1, both, 2, both),
    )

    def bond_cross(height_a, height_b, directions, lefts, rights, coeffs_a, coeffs_b):
        first, second = directions
        right_a, right_b = rights
        samples = []
        for left in lefts:
            value_a = sum(coeffs_a[index] * entry(height_a, first, left, right_a)[index] for index in range(10))
            value_b = sum(coeffs_b[index] * entry(height_b, second, left, right_b)[index] for index in range(10))
            samples.append((value_a, value_b))
        total = samples[0][0] * samples[0][1] + samples[1][0] * samples[1][1]
        return samples, total

    chi_mixed = kernel_vector(chi=1, matched=1)
    chi_only = kernel_vector(chi=1)
    chi_samples, chi_total = bond_cross(1, 2, CHI_DIRECTIONS, CHI_LEFTS, CHI_RIGHTS, chi_mixed, chi_only)
    checks.check(
        "chirality plus matched against the chirality cap has witness cross sum 2",
        chi_samples == [(1, 1), (-1, -1)] and chi_total == 2,
    )
    self_samples, self_total = bond_cross(1, 3, SELF_DIRECTIONS, SELF_LEFTS, SELF_RIGHTS, both, both)
    checks.check(
        "the same oblique-matched vector has witness cross sum -4 at heights 1 and 3",
        self_samples == [(0, 0), (-2, 2)] and self_total == -4,
    )
    ratio_vector = kernel_vector(oblique=1, matched=2)
    ratio_samples, ratio_total = bond_cross(
        1, 2, RATIO_DIRECTIONS, RATIO_LEFTS, RATIO_RIGHTS, ratio_vector, kernel_vector(oblique=1)
    )
    checks.check(
        "oblique plus twice matched has witness cross sum -1 against oblique",
        ratio_samples == [(0, 0), (-1, 1)] and ratio_total == -1,
    )
    print(f"CHI witness {chi_samples} {chi_total}")
    print(f"SELF witness {self_samples} {self_total}")
    print(f"RATIO witness {ratio_samples} {ratio_total}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()


