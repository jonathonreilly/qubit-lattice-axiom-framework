#!/usr/bin/env python3
"""Cross moments of the three kernels outside the parity span."""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

import sympy as sp

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_EXCLUDED_KERNEL_SPAN_CROSS_MOMENTS_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_OPPOSITE_HEIGHT_BASIS_MIXTURES_PRODUCT_MEANS_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_SCALED_CROSS_DOT_BASES_OPPOSITE_HEIGHT_ANSATZ_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

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
EXCLUDED = ("matched", "swapped_dot", "scaled")
WEIGHTS = ((1, 0, 0), (0, 1, 0), (0, 1, -1), (0, 1, 1), (2, 1, 1), (2, -1, 1))
ORDERED_PAIRS = ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2))
UNORDERED_PAIRS = ((1, 2), (1, 3), (2, 3))
SCALED_SUMS = {
    (1, 2): (-4, -1, 0, 2),
    (1, 3): (-2, 0, 1, 4),
    (2, 3): (-4, -1, 0, 2),
}
WITNESS_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
WITNESS_LEFTS = ((-1, -2, -3), (-1, -2, 3))
WITNESS_RIGHTS = ((1, 2, 3), (1, 2, 3))
MOMENT_47 = Fraction(47, 48)


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

    def bond_rows(height_a: int, height_b: int) -> list[list[list[int]]]:
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
                        [entry(height_a, first, left, right_a)[kernel_index[name]] for left in lefts]
                        for name in EXCLUDED
                    ]
                    if not any(any(sample) for sample in samples):
                        continue
                    for right_b in records:
                        if dot(right_b, second) != -height_b:
                            continue
                        mats = []
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
                            mats.append(row)
                        if useful:
                            found.append(mats)
        return found

    def pivot_rows(bonds: list[list[list[int]]], weights: tuple[int, int, int]) -> list[int]:
        work: list[list[Fraction]] = []
        picked = []
        for index, mats in enumerate(bonds):
            row = [
                sum(Fraction(weights[kernel]) * mats[kernel][column] for kernel in range(3))
                for column in range(10)
            ]
            if rank(work + [row]) == len(work) + 1:
                work.append(row)
                picked.append(index)
                if len(picked) == 10:
                    break
        return picked

    coefficient_a, coefficient_b, coefficient_c = sp.symbols("a b c")
    minors_only_zero = True
    for height_a, height_b in ORDERED_PAIRS:
        bonds = bond_rows(height_a, height_b)
        determinants = []
        for weights in WEIGHTS:
            picked = pivot_rows(bonds, weights)
            if len(picked) != 10:
                minors_only_zero = False
                continue
            matrix = []
            for index in picked:
                matrix.append(
                    [
                        coefficient_a * bonds[index][0][column]
                        + coefficient_b * bonds[index][1][column]
                        + coefficient_c * bonds[index][2][column]
                        for column in range(10)
                    ]
                )
            determinants.append(sp.Matrix(matrix).det())
        solutions = sp.solve(
            determinants,
            [coefficient_a, coefficient_b, coefficient_c],
            dict=True,
        )
        if solutions != [{coefficient_a: 0, coefficient_b: 0, coefficient_c: 0}]:
            minors_only_zero = False
    checks.check(
        "every ordered height pair has partner minors only at the zero excluded coefficient",
        minors_only_zero,
    )

    def cross_values(height_a: int, height_b: int, name: str) -> set[int]:
        column = kernel_index[name]
        found = set()
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
                    sample_a = [entry(height_a, first, left, right_a)[column] for left in lefts]
                    for right_b in records:
                        if dot(right_b, second) != -height_b:
                            continue
                        sample_b = [entry(height_b, second, left, right_b)[column] for left in lefts]
                        found.add(sample_a[0] * sample_b[0] + sample_a[1] * sample_b[1])
        return found

    cap_sets = all(
        cross_values(height_a, height_b, "matched") == {-1, 0, 1}
        and cross_values(height_a, height_b, "swapped_dot") == {-1, 0, 1}
        for height_a, height_b in UNORDERED_PAIRS
    )
    checks.check(
        "matched and swapped-dot self-cross sums are -1, 0, and 1 on each height pair",
        cap_sets,
    )
    checks.check(
        "scaled self-cross sums are the two height-dependent sets",
        all(
            tuple(sorted(cross_values(height_a, height_b, "scaled"))) == SCALED_SUMS[(height_a, height_b)]
            for height_a, height_b in UNORDERED_PAIRS
        ),
    )

    first_direction, second_direction = WITNESS_DIRECTIONS
    right_a, right_b = WITNESS_RIGHTS
    matched_column = kernel_index["matched"]
    sample_a = [entry(1, first_direction, left, right_a)[matched_column] for left in WITNESS_LEFTS]
    sample_b = [entry(2, second_direction, left, right_b)[matched_column] for left in WITNESS_LEFTS]
    witness_cross = sample_a[0] * sample_b[0] + sample_a[1] * sample_b[1]
    total = 0
    for left in records:
        factor_a = 1
        factor_b = 1
        if dot(left, first_direction) == 1:
            factor_a += entry(1, first_direction, left, right_a)[matched_column]
        if dot(left, second_direction) == 2:
            factor_b += entry(2, second_direction, left, right_b)[matched_column]
        total += factor_a * factor_b
    checks.check(
        "the matched self-pair on the witness bond has cross sum -1 and mean 47/48",
        sample_a == [0, 1]
        and sample_b == [0, -1]
        and witness_cross == -1
        and Fraction(total, 48) == MOMENT_47,
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
                for right_a_point in records:
                    if dot(right_a_point, first) != -height_a:
                        continue
                    for right_b_point in records:
                        if dot(right_b_point, second) != -height_b:
                            continue
                        cross = 0
                        for left in lefts:
                            value_a = sum(
                                coeffs_a[index] * entry(height_a, first, left, right_a_point)[index]
                                for index in range(10)
                            )
                            value_b = sum(
                                coeffs_b[index] * entry(height_b, second, left, right_b_point)[index]
                                for index in range(10)
                            )
                            cross += value_a * value_b
                        if cross != 0:
                            return False
        return True

    matched_vector = [1 if name == "matched" else 0 for name in KERNELS]
    zero_vector = [0 for _ in KERNELS]
    chi_vector = [1 if name == "chi" else 0 for name in KERNELS]
    checks.check(
        "the matched kernel at height 1 with the zero vector at height 2 has every cross sum equal to 0",
        every_cross_zero(1, matched_vector, 2, zero_vector),
    )
    checks.check(
        "the matched kernel at height 1 against the height-2 chirality cap has a nonzero cross sum",
        not every_cross_zero(1, matched_vector, 2, chi_vector),
    )
    print(f"WITNESS slices {sample_a} {sample_b}")
    print(f"WITNESS mean {Fraction(total, 48)}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)
    print("per_element: checked exact arithmetic on the explicitly enumerated finite record and bond data above; no continuum or empirical input is tested.")
    print("per_site: checked and not executed — this runner contains no evolving site ensemble; finite centre-record sums are the local mathematical object.")
    print("per_mode: checked and not executed — no momentum spectrum, physical particle mode or dispersion relation is computed in this finite alphabet runner.")
    print("per_block: checked the finite algebraic blocks and coefficient cases described by the named predicates; unlisted support sectors are outside this execution.")
    print("lattice_wide: checked and not executed — no whole-lattice dynamics is simulated; any all-window statement depends on the source proof and its cited converse.")



if __name__ == "__main__":
    main()
