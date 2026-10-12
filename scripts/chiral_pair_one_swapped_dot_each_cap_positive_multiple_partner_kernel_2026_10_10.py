#!/usr/bin/env python3
"""One swapped-dot generator plus a positive multiple of each cap.

On every ordered height pair, one swapped-dot generator plus m times the
cap of each ratio span has transverse-sign coordinate 0, sign-product
coordinate 0, swapped coordinate -1, orthogonal coordinate 1, matched
coordinate 4m, and scaled coordinate 4m. The swapped-dot coordinate is 1
or -1. For every positive integer m, every chirality coefficient has
partner rank 10. The certificate is the elimination polynomial of one
17-row compression. The pivot gcd is not this certificate.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

import sympy as sp

AUDIT_TIMEOUT_SEC = 240
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_ONE_SWAPPED_DOT_EACH_CAP_POSITIVE_MULTIPLE_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

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


def trim_polynomial(polynomial: list[Fraction]) -> list[Fraction]:
    trimmed = [Fraction(term) for term in polynomial]
    while trimmed and trimmed[-1] == 0:
        trimmed.pop()
    return trimmed


def polynomial_gcd(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    left = trim_polynomial(left)
    right = trim_polynomial(right)
    while right:
        while left and len(left) >= len(right):
            factor = left[-1] / right[-1]
            shift = len(left) - len(right)
            for index, term in enumerate(right):
                left[index + shift] -= factor * term
            left = trim_polynomial(left)
        left, right = right, left
    return left or [Fraction(0)]


def interpolate_values(samples: list[Fraction]) -> list[Fraction]:
    coefficients = [Fraction(value) for value in samples]
    points = [Fraction(index) for index in range(len(samples))]
    count = len(points)
    for level in range(1, count):
        for index in range(count - 1, level - 1, -1):
            coefficients[index] = (coefficients[index] - coefficients[index - 1]) / (
                points[index] - points[index - level]
            )
    polynomial = [coefficients[-1]]
    for point, term in zip(reversed(points[:-1]), reversed(coefficients[:-1])):
        nxt = [Fraction(0) for _ in range(len(polynomial) + 1)]
        for index, value in enumerate(polynomial):
            nxt[index + 1] += value
            nxt[index] -= point * value
        nxt[0] += term
        polynomial = nxt
    return polynomial


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    work = [[Fraction(entry) for entry in row] for row in matrix]
    sign = 1
    result = Fraction(1)
    for pivot_column in range(size):
        pivot = next((probe for probe in range(pivot_column, size) if work[probe][pivot_column] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != pivot_column:
            work[pivot_column], work[pivot] = work[pivot], work[pivot_column]
            sign *= -1
        result *= work[pivot_column][pivot_column]
        scale = work[pivot_column][pivot_column]
        for other in range(pivot_column + 1, size):
            factor = work[other][pivot_column] / scale
            work[other] = [
                work[other][column] - factor * work[pivot_column][column] for column in range(size)
            ]
    return sign * result


def pencil_minor_degree(
    pairs: list[tuple[list[Fraction], list[Fraction]]],
    expected_rows: int,
) -> int | None:
    augmented = [list(base) + list(chirality_row) for base, chirality_row in pairs]
    matrix = [[Fraction(entry) for entry in row] for row in augmented]
    origin = list(range(len(matrix)))
    width = 20
    chosen: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < width:
        pivot = next((probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        origin[row_index], origin[pivot] = origin[pivot], origin[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [
                matrix[other][cursor] - factor * matrix[row_index][cursor] for cursor in range(width)
            ]
        chosen.append(origin[row_index])
        row_index += 1
        column += 1
    if len(chosen) != expected_rows:
        return None
    gcd_polynomial: list[Fraction] | None = None
    for combo in combinations(chosen, 10):
        samples = []
        for value in range(11):
            minor = [
                [pairs[index][0][cursor] + Fraction(value) * pairs[index][1][cursor] for cursor in range(10)]
                for index in combo
            ]
            samples.append(determinant(minor))
        minor_polynomial = trim_polynomial(interpolate_values(samples))
        if not minor_polynomial:
            continue
        gcd_polynomial = (
            minor_polynomial
            if gcd_polynomial is None
            else trim_polynomial(polynomial_gcd(gcd_polynomial, minor_polynomial))
        )
        nonzero = [index for index, term in enumerate(gcd_polynomial) if term != 0]
        if len(nonzero) == 1:
            return nonzero[0]
    return None


def pivot_gcd_degree(
    pairs: list[tuple[list[Fraction], list[Fraction]]],
    expected_rows: int,
) -> int | None:
    augmented = [list(base) + list(chirality_row) for base, chirality_row in pairs]
    matrix = [[Fraction(entry) for entry in row] for row in augmented]
    origin = list(range(len(matrix)))
    width = 20
    chosen: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < width:
        pivot = next((probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        origin[row_index], origin[pivot] = origin[pivot], origin[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [
                matrix[other][cursor] - factor * matrix[row_index][cursor] for cursor in range(width)
            ]
        chosen.append(origin[row_index])
        row_index += 1
        column += 1
    if len(chosen) != expected_rows:
        return None
    reduced = [pairs[index] for index in chosen]
    gcd_polynomial: list[Fraction] | None = None
    for value in (Fraction(0), Fraction(1), Fraction(1, 3), Fraction(-1)):
        evaluated = []
        evaluated_origin = list(range(len(reduced)))
        for base, chirality_row in reduced:
            evaluated.append([base[cursor] + value * chirality_row[cursor] for cursor in range(10)])
        pivot_rows: list[int] = []
        row_index = 0
        column = 0
        while row_index < len(evaluated) and column < 10:
            pivot = next(
                (probe for probe in range(row_index, len(evaluated)) if evaluated[probe][column] != 0),
                None,
            )
            if pivot is None:
                column += 1
                continue
            evaluated[row_index], evaluated[pivot] = evaluated[pivot], evaluated[row_index]
            evaluated_origin[row_index], evaluated_origin[pivot] = (
                evaluated_origin[pivot],
                evaluated_origin[row_index],
            )
            scale = evaluated[row_index][column]
            evaluated[row_index] = [entry / scale for entry in evaluated[row_index]]
            for other in range(len(evaluated)):
                if other == row_index or evaluated[other][column] == 0:
                    continue
                factor = evaluated[other][column]
                evaluated[other] = [
                    evaluated[other][cursor] - factor * evaluated[row_index][cursor] for cursor in range(10)
                ]
            pivot_rows.append(evaluated_origin[row_index])
            row_index += 1
            column += 1
        if len(pivot_rows) != 10:
            return None
        samples = []
        for sample_value in range(11):
            minor = [
                [
                    reduced[index][0][cursor] + Fraction(sample_value) * reduced[index][1][cursor]
                    for cursor in range(10)
                ]
                for index in sorted(pivot_rows)
            ]
            samples.append(determinant(minor))
        polynomial = trim_polynomial(interpolate_values(samples))
        if not polynomial:
            return None
        sample = Fraction(0)
        power = Fraction(1)
        for term in polynomial:
            sample += term * power
            power *= value
        if sample == 0:
            return None
        gcd_polynomial = (
            polynomial
            if gcd_polynomial is None
            else trim_polynomial(polynomial_gcd(gcd_polynomial, polynomial))
        )
        nonzero = [index for index, term in enumerate(gcd_polynomial) if term != 0]
        if len(nonzero) == 1:
            return nonzero[0]
    return None


def projected_gcd_degree(
    pairs: list[tuple[list[Fraction], list[Fraction]]],
    expected_rows: int,
    minor_size: int,
) -> int | None:
    augmented = [list(base) + list(chirality_row) for base, chirality_row in pairs]
    matrix = [[Fraction(entry) for entry in row] for row in augmented]
    origin = list(range(len(matrix)))
    width = 20
    chosen: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < width:
        pivot = next((probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        origin[row_index], origin[pivot] = origin[pivot], origin[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [
                matrix[other][cursor] - factor * matrix[row_index][cursor] for cursor in range(width)
            ]
        chosen.append(origin[row_index])
        row_index += 1
        column += 1
    if len(chosen) != expected_rows:
        return None
    reduced = [pairs[index] for index in chosen]
    work = [[Fraction(entry) for entry in base] for base, _chirality_row in reduced]
    pivot_columns: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(work) and column < 10:
        pivot = next((probe for probe in range(row_index, len(work)) if work[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        work[row_index], work[pivot] = work[pivot], work[row_index]
        scale = work[row_index][column]
        work[row_index] = [entry / scale for entry in work[row_index]]
        for other in range(len(work)):
            if other == row_index or work[other][column] == 0:
                continue
            factor = work[other][column]
            work[other] = [
                work[other][cursor] - factor * work[row_index][cursor] for cursor in range(10)
            ]
        pivot_columns.append(column)
        row_index += 1
        column += 1
    if len(pivot_columns) != minor_size:
        return None
    gcd_polynomial: list[Fraction] | None = None
    for value in (Fraction(0), Fraction(-1)):
        evaluated = []
        evaluated_origin = list(range(len(reduced)))
        for base, chirality_row in reduced:
            evaluated.append([base[cursor] + value * chirality_row[cursor] for cursor in pivot_columns])
        pivot_rows: list[int] = []
        row_index = 0
        column = 0
        while row_index < len(evaluated) and column < minor_size:
            pivot = next(
                (probe for probe in range(row_index, len(evaluated)) if evaluated[probe][column] != 0),
                None,
            )
            if pivot is None:
                column += 1
                continue
            evaluated[row_index], evaluated[pivot] = evaluated[pivot], evaluated[row_index]
            evaluated_origin[row_index], evaluated_origin[pivot] = (
                evaluated_origin[pivot],
                evaluated_origin[row_index],
            )
            scale = evaluated[row_index][column]
            evaluated[row_index] = [entry / scale for entry in evaluated[row_index]]
            for other in range(len(evaluated)):
                if other == row_index or evaluated[other][column] == 0:
                    continue
                factor = evaluated[other][column]
                evaluated[other] = [
                    evaluated[other][cursor] - factor * evaluated[row_index][cursor]
                    for cursor in range(minor_size)
                ]
            pivot_rows.append(evaluated_origin[row_index])
            row_index += 1
            column += 1
        if len(pivot_rows) != minor_size:
            return None
        samples = []
        for sample_value in range(minor_size + 1):
            minor = [
                [
                    reduced[index][0][cursor] + Fraction(sample_value) * reduced[index][1][cursor]
                    for cursor in pivot_columns
                ]
                for index in pivot_rows
            ]
            samples.append(determinant(minor))
        polynomial = trim_polynomial(interpolate_values(samples))
        if not polynomial:
            return None
        sample = Fraction(0)
        power = Fraction(1)
        for term in polynomial:
            sample += term * power
            power *= value
        if sample == 0:
            return None
        gcd_polynomial = (
            polynomial
            if gcd_polynomial is None
            else trim_polynomial(polynomial_gcd(gcd_polynomial, polynomial))
        )
        nonzero = [index for index, term in enumerate(gcd_polynomial) if term != 0]
        if len(nonzero) == 1:
            return nonzero[0]
    return None


def monic_polynomial(polynomial: list[Fraction]) -> list[Fraction]:
    trimmed = trim_polynomial(polynomial)
    if not trimmed:
        return []
    leading = trimmed[-1]
    return [term / leading for term in trimmed]


def source_same_pivot(
    pairs: list[tuple[list[Fraction], list[Fraction]]],
    expected_rows: int,
) -> tuple[list[Fraction] | None, list[Fraction] | None, int | None]:
    augmented = [list(base) + list(chirality_row) for base, chirality_row in pairs]
    matrix = [[Fraction(entry) for entry in row] for row in augmented]
    origin = list(range(len(matrix)))
    width = 20
    chosen: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < width:
        pivot = next((probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        origin[row_index], origin[pivot] = origin[pivot], origin[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [
                matrix[other][cursor] - factor * matrix[row_index][cursor] for cursor in range(width)
            ]
        chosen.append(origin[row_index])
        row_index += 1
        column += 1
    if len(chosen) != expected_rows:
        return None, None, None
    reduced = [pairs[index] for index in chosen]
    monic_rows: list[list[Fraction]] = []
    gcd_polynomial: list[Fraction] | None = None
    for value in (Fraction(1), Fraction(2)):
        evaluated = []
        evaluated_origin = list(range(len(reduced)))
        for base, chirality_row in reduced:
            evaluated.append([base[cursor] + value * chirality_row[cursor] for cursor in range(10)])
        pivot_rows: list[int] = []
        row_index = 0
        column = 0
        while row_index < len(evaluated) and column < 10:
            pivot = next(
                (probe for probe in range(row_index, len(evaluated)) if evaluated[probe][column] != 0),
                None,
            )
            if pivot is None:
                column += 1
                continue
            evaluated[row_index], evaluated[pivot] = evaluated[pivot], evaluated[row_index]
            evaluated_origin[row_index], evaluated_origin[pivot] = (
                evaluated_origin[pivot],
                evaluated_origin[row_index],
            )
            scale = evaluated[row_index][column]
            evaluated[row_index] = [entry / scale for entry in evaluated[row_index]]
            for other in range(len(evaluated)):
                if other == row_index or evaluated[other][column] == 0:
                    continue
                factor = evaluated[other][column]
                evaluated[other] = [
                    evaluated[other][cursor] - factor * evaluated[row_index][cursor] for cursor in range(10)
                ]
            pivot_rows.append(evaluated_origin[row_index])
            row_index += 1
            column += 1
        if len(pivot_rows) != 10:
            return None, None, None
        samples = []
        for sample_value in range(11):
            minor = [
                [
                    reduced[index][0][cursor] + Fraction(sample_value) * reduced[index][1][cursor]
                    for cursor in range(10)
                ]
                for index in sorted(pivot_rows)
            ]
            samples.append(determinant(minor))
        polynomial = trim_polynomial(interpolate_values(samples))
        if not polynomial:
            return None, None, None
        sample = Fraction(0)
        power = Fraction(1)
        for term in polynomial:
            sample += term * power
            power *= value
        if sample == 0:
            return None, None, None
        monic_rows.append(monic_polynomial(polynomial))
        gcd_polynomial = (
            polynomial
            if gcd_polynomial is None
            else trim_polynomial(polynomial_gcd(gcd_polynomial, polynomial))
        )
    if gcd_polynomial is None or not monic_polynomial(gcd_polynomial):
        return None, None, None
    degree = len(monic_polynomial(gcd_polynomial)) - 1
    return monic_rows[0], monic_rows[1], degree


def binomial_minus_one(degree: int) -> list[Fraction]:
    coefficients = [Fraction(1)]
    for _ in range(degree):
        nxt = [Fraction(0) for _ in range(len(coefficients) + 1)]
        for index, term in enumerate(coefficients):
            nxt[index + 1] += term
            nxt[index] -= term
        coefficients = nxt
    return coefficients


def pivot_running_degree(
    pairs: list[tuple[list[Fraction], list[Fraction]]],
    expected_rows: int,
    values: tuple[Fraction, ...],
) -> tuple[list[list[Fraction]] | None, int | None]:
    augmented = [list(base) + list(chirality_row) for base, chirality_row in pairs]
    matrix = [[Fraction(entry) for entry in row] for row in augmented]
    origin = list(range(len(matrix)))
    width = 20
    chosen: list[int] = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < width:
        pivot = next((probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0), None)
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        origin[row_index], origin[pivot] = origin[pivot], origin[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [
                matrix[other][cursor] - factor * matrix[row_index][cursor] for cursor in range(width)
            ]
        chosen.append(origin[row_index])
        row_index += 1
        column += 1
    if len(chosen) != expected_rows:
        return None, None
    reduced = [pairs[index] for index in chosen]
    monic_rows: list[list[Fraction]] = []
    gcd_polynomial: list[Fraction] | None = None
    for value in values:
        evaluated = []
        evaluated_origin = list(range(len(reduced)))
        for base, chirality_row in reduced:
            evaluated.append([base[cursor] + value * chirality_row[cursor] for cursor in range(10)])
        pivot_rows: list[int] = []
        row_index = 0
        column = 0
        while row_index < len(evaluated) and column < 10:
            pivot = next(
                (probe for probe in range(row_index, len(evaluated)) if evaluated[probe][column] != 0),
                None,
            )
            if pivot is None:
                column += 1
                continue
            evaluated[row_index], evaluated[pivot] = evaluated[pivot], evaluated[row_index]
            evaluated_origin[row_index], evaluated_origin[pivot] = (
                evaluated_origin[pivot],
                evaluated_origin[row_index],
            )
            scale = evaluated[row_index][column]
            evaluated[row_index] = [entry / scale for entry in evaluated[row_index]]
            for other in range(len(evaluated)):
                if other == row_index or evaluated[other][column] == 0:
                    continue
                factor = evaluated[other][column]
                evaluated[other] = [
                    evaluated[other][cursor] - factor * evaluated[row_index][cursor] for cursor in range(10)
                ]
            pivot_rows.append(evaluated_origin[row_index])
            row_index += 1
            column += 1
        if len(pivot_rows) != 10:
            return None, None
        samples = []
        for sample_value in range(11):
            minor = [
                [
                    reduced[index][0][cursor] + Fraction(sample_value) * reduced[index][1][cursor]
                    for cursor in range(10)
                ]
                for index in sorted(pivot_rows)
            ]
            samples.append(determinant(minor))
        polynomial = trim_polynomial(interpolate_values(samples))
        if not polynomial:
            return None, None
        sample = Fraction(0)
        power = Fraction(1)
        for term in polynomial:
            sample += term * power
            power *= value
        if sample == 0:
            return None, None
        monic_rows.append(monic_polynomial(polynomial))
        gcd_polynomial = (
            polynomial
            if gcd_polynomial is None
            else trim_polynomial(polynomial_gcd(gcd_polynomial, polynomial))
        )
    if gcd_polynomial is None or not monic_polynomial(gcd_polynomial):
        return None, None
    return monic_rows, len(monic_polynomial(gcd_polynomial)) - 1


def combine(*vectors: list[Fraction]) -> list[Fraction]:
    total = [Fraction(0) for _ in range(10)]
    for vector in vectors:
        for index, value in enumerate(vector):
            total[index] += value
    return total



def rationalize(value: Fraction) -> sp.Rational:
    return sp.Rational(int(value.numerator), int(value.denominator))


def positive_integer_roots(expr, symbol) -> list[int]:
    numer = sp.numer(sp.together(sp.expand(expr)))
    polynomial = sp.Poly(sp.expand(numer), symbol)
    if polynomial == 0 or polynomial.degree() < 0:
        return []
    primitive = sp.primitive(polynomial)[1]
    found = []
    for factor, _power in sp.factor_list(primitive.as_expr())[1]:
        piece = sp.Poly(sp.expand(factor), symbol)
        if piece.degree() <= 0:
            continue
        for root in sp.real_roots(piece):
            if root.is_integer and root > 0:
                found.append(int(root))
    return found


def same_primitive(expr, expected, symbol) -> bool:
    def primitive(value):
        numer = sp.numer(sp.together(sp.expand(value)))
        polynomial = sp.primitive(sp.Poly(sp.expand(numer), symbol))[1]
        if polynomial.LC() < 0:
            polynomial = -polynomial
        return polynomial

    return primitive(expr) == primitive(expected)


def bivariate_minor(rows, combo, multiple_symbol, chirality_symbol):
    multiple_polynomials = []
    for chirality in range(11):
        samples = []
        for multiple in range(11):
            minor = []
            for index in combo:
                base, caps, chi = rows[index]
                minor.append(
                    [
                        base[column] + multiple * caps[column] + chirality * chi[column]
                        for column in range(10)
                    ]
                )
            samples.append(determinant(minor))
        multiple_polynomials.append(trim_polynomial(interpolate_values(samples)))
    expr = 0
    for power in range(11):
        series = [
            polynomial[power] if power < len(polynomial) else Fraction(0)
            for polynomial in multiple_polynomials
        ]
        chirality_polynomial = trim_polynomial(interpolate_values(series))
        for chirality_power, term in enumerate(chirality_polynomial):
            expr += rationalize(term) * multiple_symbol**power * chirality_symbol**chirality_power
    return sp.expand(expr)


def minor_gcd(basis, const, slope, symbol):
    rows = [[rationalize(entry) for entry in vector] for vector in basis]
    affine = [
        rationalize(const[index]) + symbol * rationalize(slope[index]) for index in range(10)
    ]
    matrix = sp.Matrix(rows + [affine])
    gcd = None
    for combo in combinations(range(10), len(rows) + 1):
        minor = sp.expand(matrix[:, combo].det())
        if minor == 0:
            continue
        polynomial = sp.Poly(sp.together(minor), symbol)
        gcd = polynomial if gcd is None else sp.gcd(gcd, polynomial)
    if gcd is None:
        return None
    return gcd.as_expr()


def elimination_polynomial(rows, multiple_symbol, chirality_symbol):
    numeric_pairs = []
    for base, caps, chi in rows:
        mixed = [base[index] + caps[index] for index in range(10)]
        if any(mixed) or any(chi):
            numeric_pairs.append((mixed, chi))
    if len(numeric_pairs) != len(rows):
        return None
    augmented = [list(base) + list(chi) for base, chi in numeric_pairs]
    matrix = [[Fraction(entry) for entry in row] for row in augmented]
    origin = list(range(len(matrix)))
    chosen = []
    row_index = 0
    column = 0
    while row_index < len(matrix) and column < 20:
        pivot = next(
            (probe for probe in range(row_index, len(matrix)) if matrix[probe][column] != 0),
            None,
        )
        if pivot is None:
            column += 1
            continue
        matrix[row_index], matrix[pivot] = matrix[pivot], matrix[row_index]
        origin[row_index], origin[pivot] = origin[pivot], origin[row_index]
        scale = matrix[row_index][column]
        matrix[row_index] = [entry / scale for entry in matrix[row_index]]
        for other in range(len(matrix)):
            if other == row_index or matrix[other][column] == 0:
                continue
            factor = matrix[other][column]
            matrix[other] = [
                matrix[other][cursor] - factor * matrix[row_index][cursor] for cursor in range(20)
            ]
        chosen.append(origin[row_index])
        row_index += 1
        column += 1
    if len(chosen) != 17:
        return None
    gcd_polynomial = None
    reducers = []
    for combo in combinations(chosen, 10):
        samples = []
        for value in range(11):
            minor = [
                [
                    numeric_pairs[index][0][cursor] + Fraction(value) * numeric_pairs[index][1][cursor]
                    for cursor in range(10)
                ]
                for index in combo
            ]
            samples.append(determinant(minor))
        polynomial = trim_polynomial(interpolate_values(samples))
        if not polynomial:
            continue
        before = None if gcd_polynomial is None else len(gcd_polynomial) - 1
        gcd_polynomial = (
            polynomial
            if gcd_polynomial is None
            else trim_polynomial(polynomial_gcd(gcd_polynomial, polynomial))
        )
        after = len(gcd_polynomial) - 1
        if before != after:
            reducers.append(combo)
        nonzero = [index for index, term in enumerate(gcd_polynomial) if term != 0]
        if len(nonzero) == 1:
            break
    if not reducers or gcd_polynomial is None or len(gcd_polynomial) != 1:
        return None
    expressions = [
        bivariate_minor(rows, combo, multiple_symbol, chirality_symbol) for combo in reducers
    ]
    specialized = [
        sp.expand(expressions[0]).coeff(chirality_symbol, power).subs(multiple_symbol, 3)
        for power in range(11)
    ]
    while specialized and sp.expand(specialized[-1]) == 0:
        specialized.pop()
    direct = []
    for value in range(11):
        minor = [
            [
                rows[index][0][cursor]
                + 3 * rows[index][1][cursor]
                + value * rows[index][2][cursor]
                for cursor in range(10)
            ]
            for index in reducers[0]
        ]
        direct.append(determinant(minor))
    direct_polynomial = trim_polynomial(interpolate_values(direct))
    if len(direct_polynomial) != len(specialized):
        return None
    for term, value in zip(direct_polynomial, specialized, strict=True):
        if sp.expand(rationalize(term) - value) != 0:
            return None
    basis = sp.groebner(expressions, chirality_symbol, multiple_symbol, order="lex", domain=sp.QQ)
    eliminant = None
    for item in basis:
        expr = sp.expand(sp.sympify(item))
        if expr.free_symbols <= {multiple_symbol} and expr != 0:
            polynomial = sp.Poly(sp.together(expr), multiple_symbol)
            eliminant = polynomial if eliminant is None else sp.gcd(eliminant, polynomial)
    if eliminant is None:
        return None
    return eliminant.as_expr()


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
    frames = {
        direction: [matrix for matrix in group if apply(matrix, up) == direction]
        for direction in axis_steps
    }
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
            return cap_sign(name, height, direction, left) * cap_sign(
                name, height, negate(direction), right
            )
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

    multiple = sp.symbols("m")
    chirality_symbol = sp.symbols("c")
    slope = [
        SPAN_PLUS[2][index] + SPAN_MINUS[2][index] for index in range(10)
    ]
    plus_const = list(SPAN_PLUS[1])
    minus_const = list(SPAN_MINUS[1])
    expected_slope = kernel_vector(matched=4, scaled=4)
    coordinate_ok = plus_const == kernel_vector(swapped=-1, swapped_dot=1, orthogonal=1) and (
        minus_const == kernel_vector(swapped=-1, swapped_dot=-1, orthogonal=1) and slope == expected_slope
    )
    difference = [plus_const[index] - minus_const[index] for index in range(10)]
    independent_ok = difference == kernel_vector(swapped_dot=2)
    outside_ok = True
    for basis in (SPAN_PLUS, SPAN_MINUS):
        for const, sign in ((plus_const, 1), (minus_const, -1)):
            if const[INDEX["swapped_dot"]] != sign:
                outside_ok = False
            obstruction = minor_gcd(basis, const, slope, multiple)
            if obstruction is None or sp.expand(obstruction) == 0 or positive_integer_roots(obstruction, multiple):
                outside_ok = False
                print(f"SPAN {sign} {obstruction}")
    chi = kernel_vector(chi=1)
    certificate_ok = True
    expected = {
        ("PLUS", True): multiple**4 * (2 * multiple + 1) ** 12 * (4 * multiple + 1) ** 4,
        ("MINUS", True): multiple**12 * (2 * multiple + 1) ** 3 * (4 * multiple + 1) ** 4,
        ("PLUS", False): multiple**10,
        ("MINUS", False): multiple**10,
    }
    for height_a, height_b in ORDERED_PAIRS:
        even = [list(vector) for vector in source_even(height_a, height_b)]
        for const in (plus_const, minus_const):
            obstruction = minor_gcd(even, const, slope, multiple)
            if (
                obstruction is None
                or sp.expand(obstruction) == 0
                or positive_integer_roots(obstruction, multiple)
            ):
                outside_ok = False
                print(f"EVEN {(height_a, height_b)} {obstruction}")
        generators = even + [list(vector) for vector in SPAN_PLUS + SPAN_MINUS]
        chi_rows = configuration_rows(height_a, height_b, generators + [chi])
        for label, block in (("PLUS", 4), ("MINUS", 7)):
            rows = []
            for row in chi_rows:
                base = [row[10 * block + column] for column in range(10)]
                caps = [row[50 + column] + row[80 + column] for column in range(10)]
                chi_row = [row[90 + column] for column in range(10)]
                if any(base) or any(caps) or any(chi_row):
                    rows.append((base, caps, chi_row))
            eliminant = elimination_polynomial(rows, multiple, chirality_symbol)
            source_same = (height_a, height_b) in SOURCE_SAME
            if eliminant is None or not same_primitive(eliminant, expected[(label, source_same)], multiple):
                certificate_ok = False
                print(f"ELIM {(height_a, height_b)} {label} {eliminant}")
            elif positive_integer_roots(eliminant, multiple):
                certificate_ok = False
                print(f"ROOT {(height_a, height_b)} {label}")
    checks.check(
        "on every ordered height pair, one swapped-dot generator plus m times each cap has swapped-dot coordinate 1 or -1, matched and scaled coordinates 4m, and the two sums are linearly independent",
        coordinate_ok and independent_ok,
    )
    checks.check(
        "each sum lies outside the even space and outside both ratio spans for every positive integer m",
        outside_ok,
    )
    checks.check(
        "the elimination polynomial is a rational multiple of m^4(2m+1)^12(4m+1)^4 or m^12(2m+1)^3(4m+1)^4 on the source-same pairs and of m^10 on the other three pairs, with no positive integer root, so every positive integer m has partner rank 10 at every chirality coefficient",
        certificate_ok,
    )

    def source_vector(const, value: int) -> list[Fraction]:
        return [const[index] + value * slope[index] for index in range(10)]

    def centre_pair(source, right_a, right_b):
        first, second = ((-1, 0, 0), (0, -1, 0))
        lefts = ((-1, -2, -3), (-1, -2, 3))
        centres = []
        partner = []
        for left in lefts:
            centres.append(
                sum(Fraction(source[column]) * entry(1, first, left, right_a)[column] for column in range(10))
            )
            partner.append(
                sum(Fraction(chi[column]) * entry(2, second, left, right_b)[column] for column in range(10))
            )
        cross = centres[0] * partner[0] + centres[1] * partner[1]
        return centres, partner, cross

    def first_polynomial(const):
        first, second = ((-1, 0, 0), (0, -1, 0))
        found = []
        for right_a in records:
            if dot(right_a, first) != -1:
                continue
            for right_b in records:
                if dot(right_b, second) != -2:
                    continue
                cross_0 = centre_pair(source_vector(const, 0), right_a, right_b)[2]
                cross_1 = centre_pair(source_vector(const, 1), right_a, right_b)[2]
                if cross_0 != 0 or cross_1 - cross_0 != 0:
                    found.append((right_a, right_b, cross_0, cross_1 - cross_0))
        found.sort()
        return found[0] if found else None

    plus_centres, plus_partner, plus_cross = centre_pair(
        source_vector(plus_const, 0), (1, -3, -2), (-3, 2, -1)
    )
    plus_centres_1 = centre_pair(source_vector(plus_const, 1), (1, -3, -2), (-3, 2, -1))[0]
    minus_centres, minus_partner, minus_cross = centre_pair(
        source_vector(minus_const, 0), (1, -3, -2), (-3, 2, -1)
    )
    minus_centres_1 = centre_pair(source_vector(minus_const, 1), (1, -3, -2), (-3, 2, -1))[0]
    checks.check(
        "the plus-dot sum has rights (1, -3, -2) and (-3, 2, -1), centre pairs (-2-4m, 1) and (0, -1), and kernel cross sum -2-4m against the chirality cap, for every positive integer m",
        first_polynomial(plus_const) == ((1, -3, -2), (-3, 2, -1), Fraction(-2), Fraction(-4))
        and plus_partner == [Fraction(1), Fraction(-1)]
        and plus_centres == [Fraction(-2), Fraction(0)]
        and plus_centres_1 == [Fraction(-6), Fraction(0)]
        and plus_cross == Fraction(-2),
    )
    checks.check(
        "the minus-dot sum has rights (1, -3, -2) and (-3, 2, -1), centre pairs (-4m, 1) and (0, -1), and kernel cross sum -4m against the chirality cap, for every positive integer m",
        first_polynomial(minus_const) == ((1, -3, -2), (-3, 2, -1), Fraction(0), Fraction(-4))
        and minus_partner == [Fraction(1), Fraction(-1)]
        and minus_centres == [Fraction(0), Fraction(0)]
        and minus_centres_1 == [Fraction(-4), Fraction(0)]
        and minus_cross == Fraction(0),
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
