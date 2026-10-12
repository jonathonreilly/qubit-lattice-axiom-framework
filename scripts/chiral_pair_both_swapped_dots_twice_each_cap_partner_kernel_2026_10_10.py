#!/usr/bin/env python3
"""Both swapped-dot generators plus twice the cap of each ratio span.

On every ordered height pair, the swapped-dot coordinates cancel and
the transverse-sign coordinates cancel. The sum lies in neither ratio
span. Every chirality coefficient has partner rank 10. The certificate
is a nonzero constant maximal-minor gcd. The pivot gcd has degree 4 on
every ordered height pair.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 240

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

    seen = 0
    sample_values = (
        Fraction(0),
        Fraction(1),
        Fraction(-1),
        Fraction(-1, 2),
        Fraction(1, 2),
        Fraction(3, 2),
        Fraction(5, 2),
        Fraction(2),
        Fraction(-2),
        Fraction(-2, 3),
    )
    mix_specs = (
        (
            "BOTH_TWICE_EACH",
            (
                Fraction(0),
                Fraction(0),
                Fraction(0),
                Fraction(0),
                Fraction(1),
                Fraction(2),
                Fraction(0),
                Fraction(1),
                Fraction(2),
            ),
            kernel_vector(matched=8, swapped=-2, orthogonal=2, scaled=8),
        ),
    )
    rank_ok = True
    pivot_ok = True

    for height_a, height_b in ORDERED_PAIRS:
        seen += 1
        even = [list(vector) for vector in source_even(height_a, height_b)]
        generators = even + [list(vector) for vector in SPAN_PLUS + SPAN_MINUS]
        chi_rows = configuration_rows(height_a, height_b, generators + [chi])

        def pairs_for(coefficients):
            pairs = []
            base_rows = []
            for row in chi_rows:
                base = [Fraction(0) for _ in range(10)]
                chirality_row = [Fraction(row[90 + column]) for column in range(10)]
                for block, coefficient in enumerate(coefficients):
                    if coefficient == 0:
                        continue
                    for column in range(10):
                        base[column] += coefficient * row[10 * block + column]
                if any(base):
                    base_rows.append(base)
                if any(base) or any(chirality_row):
                    pairs.append((base, chirality_row))
            return pairs, base_rows

        def coordinate_vector(coefficients):
            vector = [Fraction(0) for _ in range(10)]
            for block, coefficient in enumerate(coefficients):
                for column in range(10):
                    vector[column] += coefficient * generators[block][column]
            return vector

        for label, coefficients, expected in mix_specs:
            vector = coordinate_vector(coefficients)
            if (
                vector != expected
                or vector[INDEX["swapped_dot"]] != 0
                or vector[INDEX["ts"]] != 0
                or vector[INDEX["prod"]] != 0
                or vector[INDEX["scaled"]] != 8
                or in_span(SPAN_PLUS, vector)
                or in_span(SPAN_MINUS, vector)
                or in_span(even, vector)
            ):
                rank_ok = False
                print(f"{label} VECTOR {(height_a, height_b)} {vector}")
            pairs, base_rows = pairs_for(coefficients)
            found_image, kernel = nullspace(base_rows, 10)
            minor_degree = pencil_minor_degree(pairs, 17)
            if found_image != 10 or kernel or minor_degree != 0:
                rank_ok = False
                print(
                    f"{label} RANK {(height_a, height_b)} image {found_image} "
                    f"nullity {len(kernel)} minor {minor_degree}"
                )
            _monic, pivot_degree = pivot_running_degree(pairs, 17, sample_values)
            if pivot_degree != 4:
                pivot_ok = False
                print(f"{label} PIVOT {(height_a, height_b)} {pivot_degree} expected 4")
    if seen != 6:
        rank_ok = False
        pivot_ok = False
    checks.check(
        "on every ordered height pair, both swapped-dot generators plus twice the cap of each ratio span have swapped-dot coordinate 0, transverse-sign coordinate 0, scaled coordinate 8, and partner rank 10 at every chirality coefficient",
        rank_ok,
    )
    checks.check(
        "the pivot gcd has degree 4 on every ordered height pair",
        pivot_ok,
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

    witness = combine(
        list(SPAN_PLUS[1]),
        list(SPAN_MINUS[1]),
        list(SPAN_PLUS[2]),
        list(SPAN_PLUS[2]),
        list(SPAN_MINUS[2]),
        list(SPAN_MINUS[2]),
    )
    checks.check(
        "the sum has rights (1, -3, -2) and (-3, 2, -1), centre pairs (-10, 1) and (0, -1), and kernel cross sum -10 against the chirality cap",
        first_hit(witness, chi)
        == (
            ((1, -3, -2), (-3, 2, -1)),
            [(Fraction(-10), Fraction(1)), (Fraction(0), Fraction(-1))],
            Fraction(-10),
        ),
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
