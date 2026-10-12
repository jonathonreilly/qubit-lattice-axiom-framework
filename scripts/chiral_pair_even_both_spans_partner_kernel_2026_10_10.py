#!/usr/bin/env python3
"""Partner kernel of the even space and both ratio spans.

The nine-generator map has rank 42. The cap ratio 1 : -1/3 has partner
rank 7, and the cap ratio 1 : 1 has partner rank 10.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_EVEN_BOTH_SPANS_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

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
ORDERED_PAIRS = ((1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2))
SOURCE_SAME = {(1, 2), (2, 1), (3, 1)}
INDEX = {name: position for position, name in enumerate(KERNELS)}


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


def nullspace(rows: list[list[int]], width: int) -> tuple[int, list[list[Fraction]]]:
    matrix = [[Fraction(entry) for entry in row] for row in rows if any(row)]
    pivot_columns: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < width:
        pivot = next((probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [matrix[other][index] - factor * matrix[row_index][index] for index in range(width)]
        pivot_columns.append(column)
        row_index += 1
        column += 1
    occupied = set(pivot_columns)
    basis = []
    for free in range(width):
        if free in occupied:
            continue
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for stored, pivot in enumerate(pivot_columns):
            vector[pivot] = -matrix[stored][free]
        basis.append(vector)
    return len(pivot_columns), basis


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


def kernel_vector(**values: Fraction) -> list[Fraction]:
    vector = [Fraction(0) for _ in KERNELS]
    for name, value in values.items():
        vector[INDEX[name]] = Fraction(value)
    return vector


def source_even(height_a: int, height_b: int) -> tuple[list[Fraction], ...]:
    if (height_a, height_b) in SOURCE_SAME:
        return (
            kernel_vector(prod=1),
            kernel_vector(parallel=-1, oblique=1),
            kernel_vector(swapped=Fraction(-1, 2), orthogonal=1),
        )
    return (
        kernel_vector(prod=1),
        kernel_vector(swapped=1),
        kernel_vector(parallel=1, oblique=1),
    )


def in_span(basis: tuple[list[Fraction], ...] | list[list[Fraction]], vector: list[Fraction]) -> bool:
    return rank([list(row) for row in basis] + [vector]) == rank([list(row) for row in basis])


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
def rationals(*values: str) -> tuple[Fraction, ...]:
    return tuple(Fraction(value) for value in values)


_CURVE_SAME = (
    rationals("0", "0", "0", "4/5", "0", "-3/5", "1", "0", "0", "0"),
    rationals("0", "0", "0", "0", "-5/8", "0", "0", "1/2", "1", "0"),
    rationals("0", "-1/4", "-1", "1", "0", "0", "0", "0", "0", "1"),
)
_CURVE_SWAPPED_HEIGHTS = (
    rationals("0", "0", "0", "4/5", "0", "3/5", "1", "0", "0", "0"),
    rationals("0", "0", "0", "0", "-5/2", "0", "0", "2", "1", "0"),
    rationals("0", "-1/4", "-1", "1", "0", "0", "0", "0", "0", "1"),
)
CURVE_KERNELS = {
    (1, 2): _CURVE_SAME,
    (2, 1): _CURVE_SAME,
    (1, 3): (
        rationals("0", "0", "0", "-4/5", "0", "-3/5", "1", "0", "0", "0"),
        rationals("0", "0", "0", "0", "-5/8", "0", "0", "-1/2", "1", "0"),
        rationals("0", "1/4", "1", "1", "0", "0", "0", "0", "0", "1"),
    ),
    (3, 1): (
        rationals("0", "0", "0", "-4/5", "0", "3/5", "1", "0", "0", "0"),
        rationals("0", "0", "0", "0", "-5/2", "0", "0", "-2", "1", "0"),
        rationals("0", "1/4", "1", "1", "0", "0", "0", "0", "0", "1"),
    ),
    (2, 3): _CURVE_SWAPPED_HEIGHTS,
    (3, 2): _CURVE_SWAPPED_HEIGHTS,
}


def combine(*vectors: list[Fraction]) -> list[Fraction]:
    total = [Fraction(0) for _ in range(10)]
    for vector in vectors:
        for index, value in enumerate(vector):
            total[index] += value
    return total


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

    chi = kernel_vector(chi=1)

    def configuration_rows(height_a: int, height_b: int, generators) -> list[list[Fraction]]:
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
                        samples = []
                        for generator in generators:
                            samples.append(
                                [
                                    sum(
                                        generator[column] * entry(height_a, first, left, right_a)[column]
                                        for column in range(10)
                                    )
                                    for left in lefts
                                ]
                            )
                        row = []
                        for sample in samples:
                            for column in range(10):
                                total = Fraction(0)
                                for offset, left in enumerate(lefts):
                                    total += sample[offset] * entry(height_b, second, left, right_b)[column]
                                row.append(total)
                        if any(row):
                            rows.append(row)
        return rows

    def projected_rank(rows: list[list[Fraction]], coefficients: tuple[Fraction, ...]) -> int:
        projected = []
        for row in rows:
            mixed = [Fraction(0) for _ in range(10)]
            for block, coefficient in enumerate(coefficients):
                if coefficient == 0:
                    continue
                for column in range(10):
                    mixed[column] += coefficient * row[10 * block + column]
            if any(mixed):
                projected.append(mixed)
        return rank(projected)

    def partner_basis(rows: list[list[Fraction]], coefficients: tuple[Fraction, ...]) -> tuple[int, tuple[tuple[Fraction, ...], ...]]:
        projected = []
        for row in rows:
            mixed = [Fraction(0) for _ in range(10)]
            for block, coefficient in enumerate(coefficients):
                if coefficient == 0:
                    continue
                for column in range(10):
                    mixed[column] += coefficient * row[10 * block + column]
            if any(mixed):
                projected.append(mixed)
        found, kernel = nullspace(projected, 10)
        return found, tuple(tuple(entry) for entry in kernel)

    membership_ok = True
    outside_chi = True
    for height_a, height_b in ORDERED_PAIRS:
        even = [list(vector) for vector in source_even(height_a, height_b)]
        nine = even + [list(vector) for vector in SPAN_PLUS + SPAN_MINUS]
        if rank(even) != 3 or rank(nine) != 9 or rank(nine + [chi]) != 10:
            membership_ok = False
            outside_chi = False
            print(f"MEMBER {(height_a, height_b)} even {rank(even)} nine {rank(nine)} with chi {rank(nine + [chi])}")
    for vector in source_even(1, 2):
        if vector[INDEX["swapped_dot"]] != 0 or vector[INDEX["scaled"]] != 0:
            membership_ok = False
    dot_coordinate = SPAN_PLUS[1][INDEX["swapped_dot"]] - SPAN_MINUS[1][INDEX["swapped_dot"]]
    scaled_coordinate = SPAN_PLUS[2][INDEX["scaled"]] + SPAN_MINUS[2][INDEX["scaled"]]
    if dot_coordinate != 2 or scaled_coordinate != 4:
        membership_ok = False
    for vector in (SPAN_PLUS[0], SPAN_PLUS[2], SPAN_MINUS[0], SPAN_MINUS[2]):
        if vector[INDEX["swapped_dot"]] != 0:
            membership_ok = False
    for vector in (SPAN_PLUS[0], SPAN_PLUS[1], SPAN_MINUS[0], SPAN_MINUS[1]):
        if vector[INDEX["scaled"]] != 0:
            membership_ok = False
    checks.check(
        "the even space and both ratio spans form a 9-dimensional sum on every ordered height pair, the chirality cap lies outside it, and the excluded kernels sit on the swapped-orthogonal and cap generators",
        membership_ok and outside_chi,
    )

    structure_ok = True
    ratio_ok = True
    for height_a, height_b in ORDERED_PAIRS:
        even = [list(vector) for vector in source_even(height_a, height_b)]
        generators = even + [list(vector) for vector in SPAN_PLUS + SPAN_MINUS]
        rows = configuration_rows(height_a, height_b, generators)
        found, kernel = nullspace(rows, 90)
        dot_coefficients = (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(1), Fraction(0), Fraction(0))
        balanced_coefficients = (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(1))
        curve_coefficients = (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(-1, 3))
        even_only = (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0))
        plus_only = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0))
        minus_only = (Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(0), Fraction(1), Fraction(0), Fraction(0))

        def coordinate_sum(coefficients: tuple[Fraction, ...], name: str) -> Fraction:
            total = Fraction(0)
            for coefficient, generator in zip(coefficients, generators):
                total += coefficient * generator[INDEX[name]]
            return total

        def even_projection_rank() -> int:
            projected_rows = []
            for vector in kernel:
                row: list[Fraction] = []
                for block in range(3):
                    row.extend(vector[10 * block : 10 * block + 10])
                projected_rows.append(row)
            return rank(projected_rows)

        if found != 42 or len(kernel) != 48 or even_projection_rank() != 30:
            structure_ok = False
            print(f"MAP {(height_a, height_b)} rank {found} nullity {len(kernel)} even {even_projection_rank()}")
        curve_source = coordinate_sum(curve_coefficients, "scaled")
        balanced_source = coordinate_sum(balanced_coefficients, "scaled")
        dot_source_coordinate = coordinate_sum(dot_coefficients, "swapped_dot")
        if curve_source != Fraction(4, 3) or coordinate_sum(curve_coefficients, "swapped_dot") != 0:
            ratio_ok = False
        if balanced_source != 4 or coordinate_sum(balanced_coefficients, "swapped_dot") != 0:
            ratio_ok = False
        if dot_source_coordinate != 1 or coordinate_sum(dot_coefficients, "scaled") != 0:
            ratio_ok = False
        curve_found, curve_kernel = partner_basis(rows, curve_coefficients)
        expected = [list(vector) for vector in CURVE_KERNELS[(height_a, height_b)]]
        if curve_found != 7 or len(curve_kernel) != 3 or rank(expected) != 3:
            ratio_ok = False
            print(f"CURVE {(height_a, height_b)} rank {curve_found} kernel {curve_kernel}")
        elif any(not in_span(curve_kernel, vector) for vector in expected) or any(
            not in_span(expected, list(vector)) for vector in curve_kernel
        ):
            ratio_ok = False
            print(f"CURVE SPAN {(height_a, height_b)} kernel {curve_kernel}")
        if projected_rank(rows, balanced_coefficients) != 10:
            ratio_ok = False
        if projected_rank(rows, dot_coefficients) != 10:
            ratio_ok = False
        if projected_rank(rows, even_only) != 6:
            ratio_ok = False
        if projected_rank(rows, plus_only) != 7 or projected_rank(rows, minus_only) != 7:
            ratio_ok = False
        if rank([even[0], list(SPAN_PLUS[2]), list(SPAN_MINUS[2])]) != 3:
            ratio_ok = False
        if rank([even[0], list(SPAN_PLUS[1]), list(SPAN_MINUS[0])]) != 3:
            ratio_ok = False
    checks.check(
        "the nine-generator map has rank 42 and nullity 48, and the kernel projects onto every even coefficient",
        structure_ok,
    )
    checks.check(
        "the cap ratio 1 : -1/3 has scaled coefficient 4/3 and partner rank 7, and the cap ratio 1 : 1 has scaled coefficient 4 and partner rank 10",
        ratio_ok,
    )

    even_probe = [list(vector) for vector in source_even(1, 2)]
    dot_source = combine(even_probe[0], SPAN_PLUS[1], SPAN_MINUS[0])
    scaled_source = combine(even_probe[0], SPAN_PLUS[2], SPAN_MINUS[2])
    curve_source = combine(
        even_probe[0],
        SPAN_PLUS[2],
        [Fraction(-1, 3) * value for value in SPAN_MINUS[2]],
    )

    def bond_cross(source, partner, right_a, right_b):
        first, second = ((-1, 0, 0), (0, -1, 0))
        lefts = ((-1, -2, -3), (-1, -2, 3))
        samples = []
        for left in lefts:
            value_a = sum(Fraction(source[column]) * entry(1, first, left, right_a)[column] for column in range(10))
            value_b = sum(Fraction(partner[column]) * entry(2, second, left, right_b)[column] for column in range(10))
            samples.append((value_a, value_b))
        total = samples[0][0] * samples[0][1] + samples[1][0] * samples[1][1]
        return samples, total

    def first_hit(source, partner):
        first, second = ((-1, 0, 0), (0, -1, 0))
        found_hit = None
        for right_a in records:
            if dot(right_a, first) != -1:
                continue
            for right_b in records:
                if dot(right_b, second) != -2:
                    continue
                samples, total = bond_cross(source, partner, right_a, right_b)
                if total != 0 and (found_hit is None or (right_a, right_b) < found_hit[0]):
                    found_hit = ((right_a, right_b), samples, total)
        return found_hit

    dot_hit = first_hit(dot_source, SPAN_PLUS[0])
    scaled_hit = first_hit(scaled_source, SPAN_PLUS[2])
    checks.check(
        "the swapped-dot witness has rights (1, -3, -2) and (-1, 2, -3), centre pairs (-1, 0) and (1, 2), and kernel cross sum 2",
        dot_hit is not None
        and dot_hit[0] == ((1, -3, -2), (-1, 2, -3))
        and dot_hit[1] == [(Fraction(-1), Fraction(0)), (Fraction(1), Fraction(2))]
        and dot_hit[2] == 2,
    )
    checks.check(
        "the scaled coefficient 4 witness has rights (1, -3, -2) and (-3, 2, 1), centre pairs (-3, 0) and (1, -4), and kernel cross sum -4",
        scaled_hit is not None
        and scaled_hit[0] == ((1, -3, -2), (-3, 2, 1))
        and scaled_hit[1] == [(Fraction(-3), Fraction(0)), (Fraction(1), Fraction(-4))]
        and scaled_hit[2] == -4,
    )
    partner_bonds = [
        first_hit(curve_source, list(vector)) for vector in CURVE_KERNELS[(1, 2)]
    ]
    if partner_bonds != [None, None, None]:
        print(f"PARTNER BONDS {partner_bonds}")
    checks.check(
        "each listed partner of the scaled coefficient 4/3 vector has kernel cross sum 0 on -e_x and -e_y",
        partner_bonds == [None, None, None],
    )
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
