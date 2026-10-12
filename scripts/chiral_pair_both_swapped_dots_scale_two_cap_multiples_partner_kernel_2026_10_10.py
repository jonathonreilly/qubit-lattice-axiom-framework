#!/usr/bin/env python3
"""One positive scale of both swapped-dot generators plus two cap multiples.

On every ordered height pair, t times both swapped-dot generators plus
r times the plus cap and s times the minus cap has partner rank 10 at
every chirality coefficient, for every triple of positive integers
t, r, and s. For t = 1 the eliminant is (2r+1)^20 on the source-same
pairs and r^10 on the other three. None depends on s. Clearing the
positive scale gives (2r+t)^20 or r^10, with no positive integer root.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

import sympy as sp

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = ['docs/CHIRAL_PAIR_BOTH_SWAPPED_DOTS_SCALE_TWO_CAP_MULTIPLES_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_EVEN_SPAN_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/CHIRAL_PAIR_TWO_PARITY_EXCLUDED_PARTNER_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-10.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']

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


def same_bivariate(expr, expected, left_symbol, right_symbol) -> bool:
    def primitive(value):
        polynomial = sp.Poly(sp.together(sp.expand(value)), left_symbol, right_symbol)
        primitive_poly = sp.primitive(polynomial)[1]
        if primitive_poly.LC() < 0:
            primitive_poly = -primitive_poly
        return primitive_poly

    return primitive(expr) == primitive(expected)


def same_primitive(expr, expected, symbol) -> bool:
    def primitive(value):
        numer = sp.numer(sp.together(sp.expand(value)))
        polynomial = sp.primitive(sp.Poly(sp.expand(numer), symbol))[1]
        if polynomial.LC() < 0:
            polynomial = -polynomial
        return polynomial

    return primitive(expr) == primitive(expected)


def linear_has_positive_integer_zero(piece, left_symbol, right_symbol) -> bool:
    left_coeff = int(piece.coeff_monomial(left_symbol))
    right_coeff = int(piece.coeff_monomial(right_symbol))
    constant = int(piece.TC())
    if left_coeff >= 0 and right_coeff >= 0 and constant >= 0:
        return False
    if left_coeff <= 0 and right_coeff <= 0 and constant <= 0:
        return False
    if left_coeff * right_coeff < 0:
        period = abs(right_coeff)
        for left in range(1, period + 1):
            numer = -(left_coeff * left + constant)
            if numer % right_coeff == 0 and numer // right_coeff >= 1:
                return True
        return False
    limit = abs(left_coeff) + abs(right_coeff) + abs(constant) + 2
    for left in range(1, limit + 1):
        for right in range(1, limit + 1):
            if left_coeff * left + right_coeff * right + constant == 0:
                return True
    return False


def no_positive_integer_zero(expr, left_symbol, right_symbol) -> bool:
    polynomial = sp.Poly(sp.together(sp.expand(expr)), left_symbol, right_symbol)
    if polynomial == 0:
        return False
    primitive = sp.primitive(polynomial)[1]
    if primitive.LC() < 0:
        primitive = -primitive
    if primitive.total_degree() <= 0:
        return primitive.LC() != 0
    for factor, _power in sp.factor_list(primitive.as_expr())[1]:
        piece = sp.Poly(sp.expand(factor), left_symbol, right_symbol)
        if piece.total_degree() <= 0:
            continue
        coefficients = piece.coeffs()
        if all(coeff > 0 for coeff in coefficients) or all(coeff < 0 for coeff in coefficients):
            continue
        if piece.total_degree() == 1 and not linear_has_positive_integer_zero(
            piece, left_symbol, right_symbol
        ):
            continue
        return False
    return True


def minor_value(rows, combo, left: int, right: int, chirality: int) -> Fraction:
    minor = []
    for index in combo:
        base, plus, minus, chi = rows[index]
        minor.append(
            [
                base[column] + left * plus[column] + right * minus[column] + chirality * chi[column]
                for column in range(10)
            ]
        )
    return determinant(minor)


def interpolate_bivariate(grid: list[list[Fraction]]) -> dict[tuple[int, int], Fraction]:
    s_polynomials = [trim_polynomial(interpolate_values(grid[left])) for left in range(11)]
    terms: dict[tuple[int, int], Fraction] = {}
    for s_power in range(11):
        series = []
        for left in range(11):
            polynomial = s_polynomials[left]
            series.append(polynomial[s_power] if s_power < len(polynomial) else Fraction(0))
        r_polynomial = trim_polynomial(interpolate_values(series))
        for r_power, coeff in enumerate(r_polynomial):
            if coeff != 0:
                terms[(r_power, s_power)] = coeff
    return terms


def evaluate_bivariate(terms: dict[tuple[int, int], Fraction], left: int, right: int) -> Fraction:
    total = Fraction(0)
    for (r_power, s_power), coeff in terms.items():
        total += coeff * (Fraction(left) ** r_power) * (Fraction(right) ** s_power)
    return total


def cap_free_polynomial(rows, combo, left_symbol, right_symbol):
    if minor_value(rows, combo, 1, 2, 0) != minor_value(rows, combo, 1, 2, 1):
        return None
    probe = trim_polynomial(
        interpolate_values([minor_value(rows, combo, 1, 2, chirality) for chirality in range(11)])
    )
    if len(probe) != 1 or probe[0] == 0:
        return None
    grid = []
    for left in range(11):
        row = []
        for right in range(11):
            samples = [minor_value(rows, combo, left, right, chirality) for chirality in range(11)]
            polynomial = trim_polynomial(interpolate_values(samples))
            if len(polynomial) != 1:
                return None
            row.append(polynomial[0])
        grid.append(row)
    terms = interpolate_bivariate(grid)
    if evaluate_bivariate(terms, 4, 5) != minor_value(rows, combo, 4, 5, 3):
        return None
    expr = 0
    for (r_power, s_power), coeff in terms.items():
        expr += rationalize(coeff) * left_symbol**r_power * right_symbol**s_power
    polynomial = sp.Poly(sp.expand(expr), left_symbol, right_symbol)
    if polynomial == 0:
        return None
    primitive = sp.primitive(polynomial)[1]
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive


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


def span_obstruction(basis, const, plus, minus, left_symbol, right_symbol):
    rows = [[rationalize(entry) for entry in vector] for vector in basis]
    affine = [
        rationalize(const[index])
        + left_symbol * rationalize(plus[index])
        + right_symbol * rationalize(minus[index])
        for index in range(10)
    ]
    matrix = sp.Matrix(rows + [affine])
    gcd = None
    for combo in combinations(range(10), len(rows) + 1):
        minor = sp.expand(matrix[:, combo].det())
        if minor == 0:
            continue
        polynomial = sp.Poly(sp.together(minor), left_symbol, right_symbol)
        gcd = polynomial if gcd is None else sp.gcd(gcd, polynomial)
    if gcd is None:
        return None
    return gcd.as_expr()


TOTAL_MONOMIALS = [(power_r, power_s) for power_r in range(11) for power_s in range(11 - power_r)]
TOTAL_POINTS = [(left, right) for left in range(11) for right in range(11 - left)]


def monomial_value(base: int, power: int) -> Fraction:
    if power == 0:
        return Fraction(1)
    return Fraction(base) ** power


def solve_linear(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    augmented = [list(row) + [rhs[index]] for index, row in enumerate(matrix)]
    width = len(rhs)
    for column in range(width):
        pivot = next(index for index in range(column, width) if augmented[index][column] != 0)
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [entry / scale for entry in augmented[column]]
        for other in range(width):
            if other == column or augmented[other][column] == 0:
                continue
            factor = augmented[other][column]
            augmented[other] = [
                augmented[other][cursor] - factor * augmented[column][cursor] for cursor in range(width + 1)
            ]
    return [augmented[index][width] for index in range(width)]


VANDERMONDE = [
    [monomial_value(left, power_r) * monomial_value(right, power_s) for power_r, power_s in TOTAL_MONOMIALS]
    for left, right in TOTAL_POINTS
]


def evaluated_minor(rows, combo, left: int, right: int, chirality: int) -> Fraction:
    minor = []
    for index in combo:
        base, plus, minus, chi = rows[index]
        minor.append(
            [
                Fraction(base[column])
                + Fraction(left) * plus[column]
                + Fraction(right) * minus[column]
                + Fraction(chirality) * chi[column]
                for column in range(10)
            ]
        )
    return determinant(minor)


def interpolated_minor(rows, combo) -> list[list[Fraction]]:
    samples_by_power = [[] for _ in range(11)]
    for left, right in TOTAL_POINTS:
        samples = [evaluated_minor(rows, combo, left, right, chirality) for chirality in range(11)]
        polynomial = trim_polynomial(interpolate_values(samples))
        padded = polynomial + [Fraction(0)] * (11 - len(polynomial))
        for power, coefficient in enumerate(padded):
            samples_by_power[power].append(coefficient)
    solved = [solve_linear(VANDERMONDE, samples) for samples in samples_by_power]
    witness = evaluated_minor(rows, combo, 6, 6, 4)
    reconstructed = Fraction(0)
    for power, coefficients in enumerate(solved):
        coefficient = sum(
            coeff * monomial_value(6, power_r) * monomial_value(6, power_s)
            for coeff, (power_r, power_s) in zip(coefficients, TOTAL_MONOMIALS)
        )
        reconstructed += coefficient * monomial_value(4, power)
    if reconstructed != witness:
        raise RuntimeError("minor interpolation missed the witness point")
    return solved


def minor_expression(coefficients, left_symbol, right_symbol, chirality_symbol):
    expression = 0
    for power, monomial_coefficients in enumerate(coefficients):
        for coefficient, (power_r, power_s) in zip(monomial_coefficients, TOTAL_MONOMIALS):
            if coefficient == 0:
                continue
            expression += (
                rationalize(coefficient)
                * left_symbol**power_r
                * right_symbol**power_s
                * chirality_symbol**power
            )
    return sp.expand(expression)


def positive_parameter_branch_certificate(expressions, left_symbol,right_symbol,chirality_symbol):
 def positive_domain_nonzero(expr):
  if expr==0:return False
  return all(all(x>0 for x in sp.Poly(f,left_symbol,right_symbol).coeffs()) or all(x<0 for x in sp.Poly(f,left_symbol,right_symbol).coeffs()) for f,_ in sp.factor_list(expr)[1])
 evidence=[]
 for factor,_ in sp.factor_list(expressions[0])[1]:
  p=sp.Poly(factor,chirality_symbol)
  if p.degree()==0:
   if not positive_domain_nonzero(factor):return False,('constant',str(factor))
   continue
  if p.degree()!=1:return False,('degree',str(factor))
  a,b=p.nth(1),p.nth(0)
  if not (positive_domain_nonzero(a) or positive_domain_nonzero(b)):return False,('specialization',str(a),str(b))
  witnesses=[]
  for i,expression in enumerate(expressions):
   numerator=sp.factor(sp.cancel(expression.subs(chirality_symbol,-b/a))).as_numer_denom()[0]
   if positive_domain_nonzero(numerator):witnesses.append((i,str(numerator)));break
  if not witnesses:return False,('no witness',str(factor))
  evidence.append(dict(factor=str(factor),leading=str(a),constant=str(b),witness=witnesses[0]))
 return True,evidence


def elimination_polynomial(rows, left_symbol, right_symbol, chirality_symbol):
    numeric_pairs = []
    for base, plus, minus, chi in rows:
        mixed = [base[index] + plus[index] + 2 * minus[index] for index in range(10)]
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
    for combo_index, combo in enumerate(combinations(chosen, 10)):
        if combo_index >= 400:
            break
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
        minor_expression(
            interpolated_minor(rows, combo),
            left_symbol,
            right_symbol,
            chirality_symbol,
        )
        for combo in reducers
    ]
    # GCD specialization can gain extra roots. Prove absence of a common
    # chirality root directly, for every positive real cap-parameter pair.
    certified, certificate = positive_parameter_branch_certificate(
        expressions, left_symbol, right_symbol, chirality_symbol
    )
    if not certified:
        print("BRANCH_CERTIFICATE_FAIL", certificate)
        return None
    print("BRANCH_CERTIFICATE", certificate)
    # The legacy elimination expression below is a diagnostic, not the proof.
    # CYCLE77_ELIMINANT
    polynomials = [sp.Poly(sp.expand(expression), chirality_symbol) for expression in expressions]
    best = None
    for left_index, right_index in combinations(range(len(polynomials)), 2):
        common = sp.gcd(polynomials[left_index], polynomials[right_index])
        if best is None or common.degree() < best[0]:
            best = (common.degree(), left_index, right_index, common)
    if best is None:
        return None
    degree, left_index, right_index, common = best
    if degree == 0:
        piece = sp.resultant(polynomials[left_index], polynomials[right_index], chirality_symbol)
    else:
        eliminant = None
        for index, polynomial in enumerate(polynomials):
            if index in (left_index, right_index):
                continue
            resultant = sp.together(sp.expand(sp.resultant(common, polynomial, chirality_symbol)))
            if resultant == 0:
                continue
            resultant_polynomial = sp.Poly(resultant, left_symbol, right_symbol)
            eliminant = resultant_polynomial if eliminant is None else sp.gcd(eliminant, resultant_polynomial)
        if eliminant is None:
            return None
        piece = eliminant.as_expr()
    piece = sp.together(sp.expand(piece))
    if piece == 0:
        return None
    polynomial = sp.Poly(piece, left_symbol, right_symbol)
    primitive = sp.primitive(polynomial)[1]
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive.as_expr()



def fraction_entry(value) -> Fraction:
    number = sp.together(value)
    return Fraction(int(sp.numer(number)), int(sp.denom(number)))


def positive_on_line(vector: list[Fraction]) -> bool:
    if any(entry == 0 for entry in vector):
        return False
    return all(entry > 0 for entry in vector) or all(entry < 0 for entry in vector)


def positive_rational_in_kernel(kernel) -> bool:
    basis = [[fraction_entry(entry) for entry in vector] for vector in kernel]
    basis = [vector for vector in basis if any(vector)]
    if not basis:
        return False
    if len(basis) >= 3 and rank(basis) == 3:
        return True
    if len(basis) == 1:
        return positive_on_line(basis[0])
    left, right = basis[0], basis[1]
    normal = [
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    ]
    if all(entry == 0 for entry in normal):
        return positive_on_line(left) or positive_on_line(right)
    return any(entry > 0 for entry in normal) and any(entry < 0 for entry in normal)


def outside_positive_triples(basis, const, plus, minus) -> bool:
    _found, normals = nullspace([list(vector) for vector in basis], 10)
    coefficient_rows = []
    for normal in normals:
        row = []
        for vector in (const, plus, minus):
            row.append(sum((normal[index] * vector[index] for index in range(10)), Fraction(0)))
        if any(row):
            coefficient_rows.append(row)
    if not coefficient_rows:
        return False
    if rank(coefficient_rows) == 3:
        return True
    kernel = sp.Matrix(
        [[rationalize(entry) for entry in row] for row in coefficient_rows]
    ).nullspace()
    return not positive_rational_in_kernel(kernel)


def cleared_pullback(expr, scale_symbol, left_symbol, right_symbol):
    substituted = expr.subs(
        {
            left_symbol: left_symbol / scale_symbol,
            right_symbol: right_symbol / scale_symbol,
        }
    )
    numer = sp.numer(sp.together(sp.expand(substituted)))
    polynomial = sp.Poly(sp.expand(numer), scale_symbol, left_symbol, right_symbol)
    primitive = sp.primitive(polynomial)[1]
    if primitive.LC() < 0:
        primitive = -primitive
    return primitive.as_expr()


def same_trivariate(expr, expected, scale_symbol, left_symbol, right_symbol) -> bool:
    def primitive(value):
        polynomial = sp.Poly(
            sp.together(sp.expand(value)), scale_symbol, left_symbol, right_symbol
        )
        primitive_poly = sp.primitive(polynomial)[1]
        if primitive_poly.LC() < 0:
            primitive_poly = -primitive_poly
        return primitive_poly

    return primitive(expr) == primitive(expected)


def no_positive_integer_triple(expr, scale_symbol, left_symbol, right_symbol) -> bool:
    polynomial = sp.Poly(sp.expand(expr), scale_symbol, left_symbol, right_symbol)
    if polynomial == 0:
        return False
    primitive = sp.primitive(polynomial)[1]
    if primitive.LC() < 0:
        primitive = -primitive
    if primitive.total_degree() <= 0:
        return primitive.LC() != 0
    for factor, _power in sp.factor_list(primitive.as_expr())[1]:
        piece = sp.Poly(sp.expand(factor), scale_symbol, left_symbol, right_symbol)
        if piece.total_degree() <= 0:
            continue
        coefficients = piece.coeffs()
        if all(coeff > 0 for coeff in coefficients) or all(coeff < 0 for coeff in coefficients):
            continue
        return False
    return True


def rows_scale(rows) -> bool:
    scale = Fraction(2)
    left = Fraction(3)
    right = Fraction(5)
    chirality = Fraction(1)
    if not rows:
        return False
    for base, plus, minus, chi in rows:
        scaled = [
            scale * base[column]
            + left * plus[column]
            + right * minus[column]
            + chirality * chi[column]
            for column in range(10)
        ]
        pulled = [
            base[column]
            + (left / scale) * plus[column]
            + (right / scale) * minus[column]
            + (chirality / scale) * chi[column]
            for column in range(10)
        ]
        if scaled != [scale * entry for entry in pulled]:
            return False
    return True


def minor_scale(rows) -> bool:
    chosen = []
    current: list[list[Fraction]] = []
    point = (2, 3, 5, 1)
    for base, plus, minus, chi in rows:
        vector = [
            point[0] * base[column]
            + point[1] * plus[column]
            + point[2] * minus[column]
            + point[3] * chi[column]
            for column in range(10)
        ]
        if rank(current + [vector]) == len(current) + 1:
            current.append(vector)
            chosen.append((base, plus, minus, chi))
        if len(chosen) == 10:
            break
    if len(chosen) != 10:
        return False

    def det_at(scale, left, right, chirality) -> Fraction:
        minor = []
        for base, plus, minus, chi in chosen:
            minor.append(
                [
                    Fraction(scale) * base[column]
                    + Fraction(left) * plus[column]
                    + Fraction(right) * minus[column]
                    + Fraction(chirality) * chi[column]
                    for column in range(10)
                ]
            )
        return determinant(minor)

    direct = det_at(2, 3, 5, 1)
    pulled = det_at(1, Fraction(3, 2), Fraction(5, 2), Fraction(1, 2))
    return direct != 0 and direct == (Fraction(2) ** 10) * pulled


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

    scale_symbol = sp.symbols("t")
    left_symbol = sp.symbols("r")
    right_symbol = sp.symbols("s")
    chirality_symbol = sp.symbols("c")
    plus_const = list(SPAN_PLUS[1])
    minus_const = list(SPAN_MINUS[1])
    plus_slope = list(SPAN_PLUS[2])
    minus_slope = list(SPAN_MINUS[2])
    both_const = [plus_const[index] + minus_const[index] for index in range(10)]

    def family_vector(scale, left, right) -> list[Fraction]:
        return [
            Fraction(scale) * both_const[index]
            + Fraction(left) * plus_slope[index]
            + Fraction(right) * minus_slope[index]
            for index in range(10)
        ]

    def expected_vector(scale, left, right) -> list[Fraction]:
        return kernel_vector(
            ts=-left + right,
            prod=-left + right,
            matched=2 * left + 2 * right,
            swapped=-2 * scale,
            orthogonal=2 * scale,
            scaled=2 * left + 2 * right,
        )

    coordinate_points = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (2, 3, 5))
    coordinate_ok = all(
        family_vector(scale, left, right) == expected_vector(scale, left, right)
        for scale, left, right in coordinate_points
    )

    outside_ok = True
    for basis in (SPAN_PLUS, SPAN_MINUS):
        if not outside_positive_triples(basis, both_const, plus_slope, minus_slope):
            outside_ok = False
            print("SPAN")
    for height_a, height_b in ORDERED_PAIRS:
        even = [list(vector) for vector in source_even(height_a, height_b)]
        if not outside_positive_triples(even, both_const, plus_slope, minus_slope):
            outside_ok = False
            print(f"EVEN {(height_a, height_b)}")

    def source_vector(scale: int, left: int, right: int) -> list[Fraction]:
        return [
            scale * both_const[index] + left * plus_slope[index] + right * minus_slope[index]
            for index in range(10)
        ]

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

    def first_polynomial():
        first, second = ((-1, 0, 0), (0, -1, 0))
        found = []
        for right_a in records:
            if dot(right_a, first) != -1:
                continue
            for right_b in records:
                if dot(right_b, second) != -2:
                    continue
                cross_00 = centre_pair(source_vector(1, 0, 0), right_a, right_b)[2]
                cross_10 = centre_pair(source_vector(1, 1, 0), right_a, right_b)[2]
                cross_01 = centre_pair(source_vector(1, 0, 1), right_a, right_b)[2]
                cross_20 = centre_pair(source_vector(2, 0, 0), right_a, right_b)[2]
                if (
                    cross_00 != 0
                    or cross_10 != cross_00
                    or cross_01 != cross_00
                    or cross_20 != 2 * cross_00
                ):
                    found.append(
                        (
                            right_a,
                            right_b,
                            cross_00,
                            cross_10 - cross_00,
                            cross_01 - cross_00,
                            cross_20 - 2 * cross_00,
                        )
                    )
        found.sort()
        return found[0] if found else None

    chi = kernel_vector(chi=1)
    rights = ((1, -3, -2), (-3, 2, -1))
    hit = first_polynomial()
    centres_10, partner, _cross = centre_pair(source_vector(1, 0, 0), *rights)
    centres_20 = centre_pair(source_vector(2, 0, 0), *rights)[0]
    centres_11 = centre_pair(source_vector(1, 1, 0), *rights)[0]
    centres_01 = centre_pair(source_vector(1, 0, 1), *rights)[0]
    bond_ok = (
        hit == ((1, -3, -2), (-3, 2, -1), Fraction(-2), Fraction(-4), Fraction(0), Fraction(0))
        and partner == [Fraction(1), Fraction(-1)]
        and centres_10 == [Fraction(-2), Fraction(0)]
        and centres_20 == [Fraction(-4), Fraction(0)]
        and centres_11 == [Fraction(-6), Fraction(0)]
        and centres_01 == [Fraction(-2), Fraction(0)]
    )
    if not bond_ok:
        print("BOND", hit, partner, centres_10, centres_20, centres_11, centres_01)
    checks.check(
        "on every ordered height pair, t times both swapped-dot generators plus r times the plus cap and s times the minus cap have swapped-dot coordinate 0, swapped coordinate -2t, orthogonal coordinate 2t, transverse-sign and sign-product coordinates s-r, and matched and scaled coordinates 2r+2s",
        coordinate_ok,
    )
    checks.check(
        "the sum lies outside the even space and outside both ratio spans for every triple of positive integers (t, r, s)",
        outside_ok,
    )
    checks.check(
        "the sum has rights (1, -3, -2) and (-3, 2, -1), centre pairs (-2t-4r, 1) and (0, -1), and kernel cross sum -2t-4r against the chirality cap, for every triple of positive integers (t, r, s)",
        bond_ok,
    )
    if checks.failed:
        print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
        raise SystemExit(1)

    certificate_ok = True
    pullback_ok = True
    scale_ok = True
    for height_a, height_b in ORDERED_PAIRS:
        even = [list(vector) for vector in source_even(height_a, height_b)]
        generators = even + [list(vector) for vector in SPAN_PLUS + SPAN_MINUS]
        chi_rows = configuration_rows(height_a, height_b, generators + [chi])
        rows = []
        for row in chi_rows:
            base = [row[40 + column] + row[70 + column] for column in range(10)]
            plus = [row[50 + column] for column in range(10)]
            minus = [row[80 + column] for column in range(10)]
            chi_row = [row[90 + column] for column in range(10)]
            if any(base) or any(plus) or any(minus) or any(chi_row):
                rows.append((base, plus, minus, chi_row))
        if not rows_scale(rows) or not minor_scale(rows):
            scale_ok = False
            print(f"SCALE {(height_a, height_b)}")
            break
        eliminant = elimination_polynomial(rows, left_symbol, right_symbol, chirality_symbol)
        source_same = (height_a, height_b) in SOURCE_SAME
        if source_same:
            expected = (2 * left_symbol + 1) ** 20
            expected_clear = (2 * left_symbol + scale_symbol) ** 20
        else:
            expected = left_symbol**10
            expected_clear = left_symbol**10
        if eliminant is None or not same_bivariate(
            eliminant, expected, left_symbol, right_symbol
        ):
            certificate_ok = False
            print(
                f"ELIM {(height_a, height_b)} "
                f"{None if eliminant is None else sp.factor(eliminant)}"
            )
            break
        cleared = cleared_pullback(eliminant, scale_symbol, left_symbol, right_symbol)
        specialized = sp.expand(cleared.subs(scale_symbol, 1))
        if (
            not same_trivariate(cleared, expected_clear, scale_symbol, left_symbol, right_symbol)
            or not same_bivariate(specialized, eliminant, left_symbol, right_symbol)
            or not no_positive_integer_triple(cleared, scale_symbol, left_symbol, right_symbol)
        ):
            pullback_ok = False
            print(f"PULL {(height_a, height_b)} {sp.factor(cleared)}")
            break
    checks.check(
        "each partner row at (t, r, s, c) equals t times the row at (1, r/t, s/t, c/t), and one maximal minor scales by t^10",
        scale_ok,
    )
    checks.check(
        "the unit-scale elimination polynomial is (2r+1)^20 on (1, 2), (2, 1), and (3, 1) and r^10 on (1, 3), (2, 3), and (3, 2)",
        certificate_ok,
    )
    checks.check(
        "clearing the positive scale gives (2r+t)^20 on (1, 2), (2, 1), and (3, 1) and r^10 on (1, 3), (2, 3), and (3, 2), with no positive integer root, so every positive integer triple has partner rank 10 at every chirality coefficient",
        pullback_ok,
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
