#!/usr/bin/env python3
"""Mixtures of the modulus-3 complement do not leave the eighteen."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 180

NAMES = ["a", "e0", "e1", "e2", "p0", "p1", "p2", "q0", "q1", "q2"]


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


def signature(direction, left, right) -> tuple[int, int]:
    forward = (dot(left, direction), dot(right, direction))
    backward = (-forward[1], -forward[0])
    return min(forward, backward)


def kernel_basis(rows: list[tuple[int, ...]], width: int) -> list[list[Fraction]]:
    matrix = [[Fraction(value) for value in row] for row in rows]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((index for index in range(rank_now, len(matrix)) if matrix[index][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for index in range(len(matrix)):
            if index != rank_now and matrix[index][col] != 0:
                factor = matrix[index][col]
                matrix[index] = [
                    matrix[index][col_index] - factor * matrix[rank_now][col_index]
                    for col_index in range(width)
                ]
        pivots.append(col)
        rank_now += 1
    basis = []
    for free in [col for col in range(width) if col not in pivots]:
        vector = [Fraction(0) for _ in range(width)]
        vector[free] = Fraction(1)
        for pivot_index, pivot_col in enumerate(pivots):
            vector[pivot_col] = -matrix[pivot_index][free]
        basis.append(vector)
    return basis


def rref(rows: list[list[Fraction]], width: int) -> tuple[list[list[Fraction]], list[int]]:
    matrix = [[Fraction(value) for value in row] for row in rows if any(row)]
    pivots = []
    rank_now = 0
    for col in range(width):
        pivot = next((index for index in range(rank_now, len(matrix)) if matrix[index][col] != 0), None)
        if pivot is None:
            continue
        matrix[rank_now], matrix[pivot] = matrix[pivot], matrix[rank_now]
        scale = matrix[rank_now][col]
        matrix[rank_now] = [value / scale for value in matrix[rank_now]]
        for index in range(len(matrix)):
            if index != rank_now and matrix[index][col] != 0:
                factor = matrix[index][col]
                matrix[index] = [
                    matrix[index][col_index] - factor * matrix[rank_now][col_index]
                    for col_index in range(width)
                ]
        pivots.append(col)
        rank_now += 1
    return matrix[:rank_now], pivots


def monomials() -> list[tuple[int, int]]:
    return [(left, right) for left in range(10) for right in range(left, 10)]


def blank(width: int) -> list[Fraction]:
    return [Fraction(0) for _ in range(width)]


def put(row: list[Fraction], index: dict[tuple[int, int], int], left: int, right: int, value: Fraction) -> None:
    if left > right:
        left, right = right, left
    row[index[(left, right)]] += value


def in_span(rows: list[list[Fraction]], target: list[Fraction], width: int) -> bool:
    if not any(target):
        return False
    base, _ = rref(rows, width)
    larger, _ = rref(rows + [target], width)
    return len(larger) == len(base)


def poly_add(left: dict, right: dict) -> dict:
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, Fraction(0)) + value
        if out[key] == 0:
            del out[key]
    return out


def poly_scale(poly: dict, scale: Fraction) -> dict:
    return {key: value * scale for key, value in poly.items() if value * scale}


def poly_mul(left: dict, right: dict) -> dict:
    out: dict = {}
    for left_key, left_value in left.items():
        for right_key, right_value in right.items():
            key = tuple(left_key[index] + right_key[index] for index in range(len(left_key)))
            out[key] = out.get(key, Fraction(0)) + left_value * right_value
            if out[key] == 0:
                del out[key]
    return out


def coordinate(index: int, width: int) -> dict:
    key = [0] * width
    key[index] = 1
    return {tuple(key): Fraction(1)}


def det_poly(matrix: list[list[dict]]) -> dict:
    width = len(next(iter(matrix[0][0])))
    total: dict = {}
    for perm in permutations(range(3)):
        sign = 1
        for left in range(3):
            for right in range(left + 1, 3):
                if perm[left] > perm[right]:
                    sign = -sign
        term = {tuple(0 for _ in range(width)): Fraction(sign)}
        for row, col in enumerate(perm):
            term = poly_mul(term, matrix[row][col])
        total = poly_add(total, term)
    return total


def substitute_quadratic(coeffs: list[tuple[tuple[int, int], Fraction]], images: list[dict]) -> dict:
    total: dict = {}
    for (left, right), value in coeffs:
        total = poly_add(total, poly_scale(poly_mul(images[left], images[right]), value))
    return total


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check(
        "six axis directions",
        axis_steps == [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)],
    )

    image_of: dict = {}
    sig_of: dict[int, tuple[int, int]] = {}
    for direction in axis_steps:
        for left in orbit:
            for right in orbit:
                images = frozenset(
                    bond_key(apply(matrix, direction), apply(matrix, left), apply(matrix, right))
                    for matrix in group
                )
                if images not in image_of:
                    image_of[images] = len(sig_of)
                    sample = min(next(iter(images)))
                    sig_of[image_of[images]] = signature(*sample)
                image_of[(direction, left, right)] = image_of[images]
    dimension = len(sig_of)
    by_sig: dict[tuple[int, int], list[int]] = defaultdict(list)
    for index, sig in sig_of.items():
        by_sig[sig].append(index)

    slice_rows = []
    seen_rows = set()
    for direction in axis_steps:
        for right in orbit:
            row = [0] * dimension
            for left in orbit:
                row[image_of[(direction, left, right)]] += 1
            key = tuple(row)
            if key not in seen_rows:
                seen_rows.add(key)
                slice_rows.append(key)

    triple = ((-3, -3), (-3, 3), (3, -3))
    columns = [index for sig in triple for index in by_sig[sig]]
    local_rows = []
    seen_local = set()
    for row in slice_rows:
        packed = tuple(row[index] for index in columns)
        if any(packed) and packed not in seen_local:
            seen_local.add(packed)
            local_rows.append(packed)
    joint = kernel_basis(local_rows, len(columns))
    checks.check(
        "the ansatz is the 10-dimensional joint slice kernel on 12 orbits",
        len(joint) == 10 and len(columns) == 12 and dimension == 84,
    )

    internal = []
    offset = 0
    for sig in triple:
        block = by_sig[sig]
        block_rows = []
        seen_block = set()
        for row in slice_rows:
            packed = tuple(row[index] for index in block)
            if any(packed) and packed not in seen_block:
                seen_block.add(packed)
                block_rows.append(packed)
        for local in kernel_basis(block_rows, len(block)):
            full = [Fraction(0) for _ in columns]
            for index, value in enumerate(local):
                full[offset + index] = value
            internal.append(full)
        offset += len(block)
    reduced_internal, _ = rref(internal, len(columns))
    complement = [Fraction(value) for value in (0, 0, 0, -1, 0, 0, 0, 1, 0, 0, 0, 1)]
    basis = [complement] + internal
    checks.check(
        "the line plus the three signature kernels span that kernel",
        len(reduced_internal) == 9 and len(rref(basis, len(columns))[0]) == 10,
    )

    pairs = monomials()
    pair_index = {pair: index for index, pair in enumerate(pairs)}
    col_of = {orbit_index: local for local, orbit_index in enumerate(columns)}
    tables = []
    for vector in basis:
        sparse = {}
        for d_i, direction in enumerate(axis_steps):
            for a_i, left in enumerate(orbit):
                for b_i, right in enumerate(orbit):
                    local = col_of.get(image_of[(direction, left, right)])
                    if local is None:
                        continue
                    value = vector[local]
                    if value:
                        sparse[(d_i, a_i, b_i)] = value
        tables.append(sparse)

    unique: dict[tuple[Fraction, ...], list[Fraction]] = {}
    for d_i in range(6):
        for e_i in range(d_i + 1, 6):
            for b_i in range(24):
                for c_i in range(24):
                    grams = [[Fraction(0) for _ in range(10)] for _ in range(10)]
                    hit = False
                    for a_i in range(24):
                        left_vals = [(p, tables[p][(d_i, a_i, b_i)]) for p in range(10) if (d_i, a_i, b_i) in tables[p]]
                        right_vals = [(q, tables[q][(e_i, a_i, c_i)]) for q in range(10) if (e_i, a_i, c_i) in tables[q]]
                        if not left_vals or not right_vals:
                            continue
                        hit = True
                        for p, left_value in left_vals:
                            for q, right_value in right_vals:
                                grams[p][q] += left_value * right_value
                    if not hit:
                        continue
                    coeffs = blank(len(pairs))
                    for p in range(10):
                        for q in range(p, 10):
                            value = grams[p][q] if p == q else grams[p][q] + grams[q][p]
                            if value:
                                coeffs[pair_index[(p, q)]] = value
                    if any(coeffs):
                        unique[tuple(coeffs)] = coeffs
    moment_rows = list(unique.values())
    reduced_moments, moment_pivots = rref(moment_rows, len(pairs))
    square = blank(len(pairs))
    square[pair_index[(0, 0)]] = Fraction(1)
    checks.check(
        "the pair moments contain the square of the complement coefficient",
        moment_pivots[0] == 0 and reduced_moments[0] == square,
    )

    def explicit_row(terms: list[tuple[int, int, Fraction]]) -> list[Fraction]:
        row = blank(len(pairs))
        for left, right, value in terms:
            put(row, pair_index, left, right, value)
        return row

    half = Fraction(1, 2)
    explicit = [
        explicit_row([(1, 4, Fraction(1)), (3, 5, Fraction(-1)), (2, 6, Fraction(-1)), (3, 6, Fraction(-1))]),
        explicit_row(
            [
                (2, 4, Fraction(1)),
                (1, 5, Fraction(1)),
                (2, 5, Fraction(1)),
                (3, 5, Fraction(1)),
                (2, 6, Fraction(1)),
                (3, 6, Fraction(1)),
            ]
        ),
        explicit_row([(3, 4, Fraction(1)), (2, 5, Fraction(-1)), (1, 6, Fraction(1)), (3, 6, Fraction(1))]),
        explicit_row(
            [
                (1, 7, Fraction(1)),
                (2, 7, Fraction(1)),
                (3, 7, Fraction(1)),
                (2, 8, Fraction(1)),
                (2, 9, Fraction(1)),
                (3, 9, Fraction(1)),
            ]
        ),
        explicit_row([(3, 7, Fraction(-1)), (1, 8, Fraction(1)), (2, 9, Fraction(-1)), (3, 9, Fraction(-1))]),
        explicit_row([(2, 7, Fraction(-1)), (3, 8, Fraction(1)), (1, 9, Fraction(1)), (3, 9, Fraction(1))]),
        explicit_row(
            [
                (1, 1, Fraction(1)),
                (2, 3, Fraction(-2)),
                (3, 3, Fraction(-1)),
                (4, 8, Fraction(1)),
                (5, 9, Fraction(-1)),
                (6, 7, Fraction(-1)),
                (6, 9, Fraction(-1)),
            ]
        ),
        explicit_row(
            [
                (1, 2, Fraction(1)),
                (2, 2, half),
                (2, 3, Fraction(1)),
                (3, 3, half),
                (4, 7, half),
                (5, 7, half),
                (5, 8, half),
                (6, 7, half),
                (5, 9, half),
                (6, 9, half),
            ]
        ),
        explicit_row(
            [
                (1, 3, Fraction(1)),
                (2, 2, -half),
                (3, 3, half),
                (4, 9, half),
                (5, 7, -half),
                (6, 8, half),
                (6, 9, half),
            ]
        ),
    ]
    substituted = []
    for row in moment_rows:
        new_row = row[:]
        for index, (left, right) in enumerate(pairs):
            if left == 0 or right == 0:
                new_row[index] = Fraction(0)
        if any(new_row):
            substituted.append(new_row)
    checks.check(
        "nine explicit forms are pair-moment consequences once the coefficient is zero",
        all(in_span(substituted, row, len(pairs)) for row in explicit)
        and len(rref(explicit, len(pairs))[0]) == 9,
    )

    e0, e1, e2 = (coordinate(index, 3) for index in range(3))
    matrix_a = [
        [e0, poly_scale(e2, Fraction(-1)), poly_add(poly_scale(e1, Fraction(-1)), poly_scale(e2, Fraction(-1)))],
        [e1, poly_add(poly_add(e0, e1), e2), poly_add(e1, e2)],
        [e2, poly_scale(e1, Fraction(-1)), poly_add(e0, e2)],
    ]
    matrix_b = [
        [poly_add(poly_add(e0, e1), e2), e1, poly_add(e1, e2)],
        [poly_scale(e2, Fraction(-1)), e0, poly_add(poly_scale(e1, Fraction(-1)), poly_scale(e2, Fraction(-1)))],
        [poly_scale(e1, Fraction(-1)), e2, poly_add(e0, e2)],
    ]
    square_factor = poly_add(
        poly_mul(poly_add(e0, e2), poly_add(e0, e2)),
        poly_mul(poly_add(e1, e2), poly_add(e1, e2)),
    )
    factored = poly_mul(poly_add(e0, e1), square_factor)
    def bilinear_row(matrix_row: list[dict], vector_offset: int) -> list[Fraction]:
        row = blank(len(pairs))
        for column, entry in enumerate(matrix_row):
            for exponents, value in entry.items():
                e_index = next(index for index, power in enumerate(exponents) if power)
                put(row, pair_index, e_index + 1, vector_offset + column, value)
        return row

    matrix_rows = [bilinear_row(row, 4) for row in matrix_a] + [bilinear_row(row, 7) for row in matrix_b]
    checks.check(
        "both determinants factor as the plane times a sum of two squares",
        matrix_rows == explicit[:6] and det_poly(matrix_a) == factored and det_poly(matrix_b) == factored,
    )

    def on_plane(poly: dict) -> dict:
        out: dict = {}
        for (i, j, k), value in poly.items():
            key = (i + j, k)
            out[key] = out.get(key, Fraction(0)) + value * ((-1) ** j)
            if out[key] == 0:
                del out[key]
        return out

    minor = poly_add(poly_mul(e0, e0), poly_mul(e2, e2))
    kernel = [Fraction(-1), Fraction(-1), Fraction(1)]

    def matrix_times_kernel(matrix: list[list[dict]]) -> list[dict]:
        rows = []
        for row in matrix:
            total: dict = {}
            for entry, weight in zip(row, kernel):
                total = poly_add(total, poly_scale(entry, weight))
            rows.append(on_plane(total))
        return rows

    plane_minor_a = on_plane(
        poly_add(poly_mul(matrix_a[0][0], matrix_a[2][1]), poly_scale(poly_mul(matrix_a[0][1], matrix_a[2][0]), Fraction(-1)))
    )
    plane_minor_b = on_plane(
        poly_add(poly_mul(matrix_b[1][0], matrix_b[2][1]), poly_scale(poly_mul(matrix_b[1][1], matrix_b[2][0]), Fraction(-1)))
    )
    zero_plane = {}
    checks.check(
        "on e0 + e1 = 0 the kernel line is one-dimensional away from the origin",
        on_plane(factored) == zero_plane
        and all(row == zero_plane for row in matrix_times_kernel(matrix_a))
        and all(row == zero_plane for row in matrix_times_kernel(matrix_b))
        and plane_minor_a == {(2, 0): Fraction(1), (0, 2): Fraction(1)}
        and plane_minor_b == {(2, 0): Fraction(-1), (0, 2): Fraction(-1)}
        and minor == {(2, 0, 0): Fraction(1), (0, 0, 2): Fraction(1)},
    )

    m1_terms = [((0, 0), Fraction(1)), ((1, 2), Fraction(-2)), ((2, 2), Fraction(-1))]
    m2_terms = [((0, 1), Fraction(1)), ((1, 1), half), ((1, 2), Fraction(1)), ((2, 2), half)]
    m3_terms = [((0, 2), Fraction(1)), ((1, 1), -half), ((2, 2), half)]

    def quadratic_poly(terms: list[tuple[tuple[int, int], Fraction]]) -> dict:
        total: dict = {}
        variables = [coordinate(index, 3) for index in range(3)]
        for (left, right), value in terms:
            monomial = poly_mul(variables[left], variables[right])
            total = poly_add(total, poly_scale(monomial, value))
        return total

    m1 = quadratic_poly(m1_terms)
    m2 = quadratic_poly(m2_terms)
    m3 = quadratic_poly(m3_terms)
    variables = [coordinate(index, 3) for index in range(3)]
    cross = poly_add(poly_mul(variables[1], m3), poly_scale(poly_mul(variables[2], m2), Fraction(-1)))
    expected_cross = poly_scale(
        poly_mul(poly_add(variables[1], variables[2]), poly_add(poly_mul(variables[1], variables[1]), poly_mul(variables[2], variables[2]))),
        Fraction(-1, 2),
    )
    def replace_e1_by_minus_e2(poly: dict) -> dict:
        out: dict = {}
        for (i, j, k), value in poly.items():
            key = (i, 0, k + j)
            out[key] = out.get(key, Fraction(0)) + value * ((-1) ** j)
            if out[key] == 0:
                del out[key]
        return out

    on_sum_zero = replace_e1_by_minus_e2(m1)
    on_axes_zero = {(i, 0, 0): value for (i, j, k), value in m1.items() if j == 0 and k == 0}
    checks.check(
        "with the opposite blocks zero, the equal-height quadrics vanish only at the origin",
        cross == expected_cross
        and on_sum_zero == {(2, 0, 0): Fraction(1), (0, 0, 2): Fraction(1)}
        and on_axes_zero == {(2, 0, 0): Fraction(1)},
    )

    images = [
        coordinate(0, 4),
        poly_scale(coordinate(0, 4), Fraction(-1)),
        coordinate(1, 4),
        poly_scale(coordinate(2, 4), Fraction(-1)),
        poly_scale(coordinate(2, 4), Fraction(-1)),
        coordinate(2, 4),
        poly_scale(coordinate(3, 4), Fraction(-1)),
        poly_scale(coordinate(3, 4), Fraction(-1)),
        coordinate(3, 4),
    ]
    quadric_terms = []
    for row in explicit[6:]:
        terms = []
        for (left, right), value in zip(pairs, row):
            if value:
                terms.append(((left - 1, right - 1), value))
        quadric_terms.append(terms)
    specials = [substitute_quadratic(terms, images) for terms in quadric_terms]
    u = {
        (2, 0, 0, 0): Fraction(1),
        (1, 1, 0, 0): Fraction(2),
        (0, 2, 0, 0): Fraction(-1),
    }
    w = {
        (2, 0, 0, 0): Fraction(1),
        (1, 1, 0, 0): Fraction(-2),
        (0, 2, 0, 0): Fraction(-1),
    }
    product_lm = {(0, 0, 1, 1): Fraction(1)}
    expected_specials = [
        poly_add(u, poly_scale(product_lm, Fraction(2))),
        poly_scale(poly_add(u, poly_scale(product_lm, Fraction(-2))), Fraction(-1, 2)),
        poly_scale(poly_add(w, poly_scale(product_lm, Fraction(2))), Fraction(-1, 2)),
    ]
    sum_first = poly_add(specials[0], poly_scale(specials[1], Fraction(-2)))
    difference = poly_add(specials[0], poly_scale(specials[1], Fraction(2)))
    checks.check(
        "on e0 + e1 = 0 the kernel line forces the equal-height coordinates to zero",
        specials == expected_specials
        and sum_first == poly_scale(u, Fraction(2))
        and difference == poly_scale(product_lm, Fraction(4))
        and poly_scale(specials[2], Fraction(-2)) == poly_add(w, poly_scale(product_lm, Fraction(2)))
        and poly_add(u, w) == {(2, 0, 0, 0): Fraction(2), (0, 2, 0, 0): Fraction(-2)}
        and poly_add(u, poly_scale(w, Fraction(-1))) == {(1, 1, 0, 0): Fraction(4)},
    )

    def on_equal_line(poly: dict) -> dict:
        out: dict = {}
        for (i, j, k), value in poly.items():
            key = (i + j + k,)
            out[key] = out.get(key, Fraction(0)) + value * ((-1) ** k)
            if out[key] == 0:
                del out[key]
        return out

    def minors_2x2(matrix: list[list[dict]]) -> list[dict]:
        found = []
        for row_a in range(3):
            for row_b in range(row_a + 1, 3):
                for col_a in range(3):
                    for col_b in range(col_a + 1, 3):
                        found.append(
                            poly_add(
                                poly_mul(matrix[row_a][col_a], matrix[row_b][col_b]),
                                poly_scale(poly_mul(matrix[row_a][col_b], matrix[row_b][col_a]), Fraction(-1)),
                            )
                        )
        return found

    def times_vector(matrix: list[list[dict]], weights: list[Fraction]) -> list[dict]:
        rows = []
        for row in matrix:
            total: dict = {}
            for entry, weight in zip(row, weights):
                total = poly_add(total, poly_scale(entry, weight))
            rows.append(on_equal_line(total))
        return rows

    kernel_vectors = ([Fraction(-1), Fraction(1), Fraction(0)], [Fraction(0), Fraction(0), Fraction(1)])
    line_rank = (
        on_equal_line(matrix_a[0][0]) == {(1,): Fraction(1)}
        and on_equal_line(matrix_b[0][0]) == {(1,): Fraction(1)}
        and all(on_equal_line(minor) == {} for minor in minors_2x2(matrix_a) + minors_2x2(matrix_b))
        and all(row == {} for weights in kernel_vectors for row in times_vector(matrix_a, weights))
        and all(row == {} for weights in kernel_vectors for row in times_vector(matrix_b, weights))
    )
    line_images = [
        coordinate(0, 5),
        coordinate(0, 5),
        poly_scale(coordinate(0, 5), Fraction(-1)),
        poly_scale(coordinate(1, 5), Fraction(-1)),
        coordinate(1, 5),
        coordinate(2, 5),
        poly_scale(coordinate(3, 5), Fraction(-1)),
        coordinate(3, 5),
        coordinate(4, 5),
    ]
    line_specials = [substitute_quadratic(terms, line_images) for terms in quadric_terms]
    line_sum = poly_add(line_specials[0], poly_scale(line_specials[1], Fraction(2)))
    checks.check(
        "on e0 = e1 = -e2 the same quadrics force that coordinate to zero",
        line_rank and line_sum == {(2, 0, 0, 0, 0): Fraction(4)},
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
