#!/usr/bin/env python3
"""An equal-height signature stays inside the eighteen beside one partner."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, permutations, product

AUDIT_TIMEOUT_SEC = 300


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


def reduced_rows(rows: list[list[Fraction]], width: int) -> tuple[list[list[Fraction]], list[int]]:
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


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    reduced = [row[:] for row in matrix]
    sign = Fraction(1)
    for col in range(size):
        pivot = next((row for row in range(col, size) if reduced[row][col] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            reduced[col], reduced[pivot] = reduced[pivot], reduced[col]
            sign = -sign
        for row in range(col + 1, size):
            if reduced[row][col] == 0:
                continue
            factor = reduced[row][col] / reduced[col][col]
            for index in range(col, size):
                reduced[row][index] -= factor * reduced[col][index]
    value = sign
    for index in range(size):
        value *= reduced[index][index]
    return value


def resultant_degree_four(left: list[int], right: list[int]) -> int:
    matrix = [[Fraction(0) for _ in range(8)] for _ in range(8)]
    for shift in range(4):
        for power, coeff in enumerate(left):
            matrix[shift][shift + power] = Fraction(coeff)
        for power, coeff in enumerate(right):
            matrix[4 + shift][shift + power] = Fraction(coeff)
    return int(determinant(matrix))


def poly_mul(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    out: dict[int, Fraction] = {}
    for degree, coeff in left.items():
        for other, other_coeff in right.items():
            out[degree + other] = out.get(degree + other, Fraction(0)) + coeff * other_coeff
    return {degree: coeff for degree, coeff in out.items() if coeff}


def poly_add(left: dict[int, Fraction], right: dict[int, Fraction]) -> dict[int, Fraction]:
    out = dict(left)
    for degree, coeff in right.items():
        out[degree] = out.get(degree, Fraction(0)) + coeff
    return {degree: coeff for degree, coeff in out.items() if coeff}


def poly_scale(poly: dict[int, Fraction], scale: Fraction) -> dict[int, Fraction]:
    return {degree: coeff * scale for degree, coeff in poly.items() if coeff * scale}


def primitive_coefficients(poly: dict[int, Fraction]) -> list[int]:
    values = [int(poly.get(degree, Fraction(0))) for degree in range(5)]
    content = 0
    for value in values:
        a, b = abs(value), abs(content)
        while b:
            a, b = b, a % b
        content = a
    if values[-1] < 0:
        content = -content
    low_to_high = [value // content for value in values]
    return list(reversed(low_to_high))


def eliminant_quartics() -> tuple[list[int], list[int]]:
    """Substitute the first quadric at third coordinate 1 into the other two."""
    numerator = {2: Fraction(6), 0: Fraction(-8)}
    variable = {1: Fraction(1)}
    second = poly_add(
        poly_add(
            poly_scale(poly_mul(variable, numerator), Fraction(6, 9)),
            poly_scale(poly_mul(numerator, numerator), Fraction(6, 81)),
        ),
        poly_add(numerator, {0: Fraction(4)}),
    )
    third = poly_add(
        poly_add({1: Fraction(6)}, poly_scale(poly_mul(numerator, numerator), Fraction(-6, 81))),
        poly_add(poly_scale(numerator, Fraction(-3, 9)), {0: Fraction(4)}),
    )
    return primitive_coefficients(poly_scale(second, 81)), primitive_coefficients(poly_scale(third, 81))


def main() -> None:
    checks = Checks()
    group = proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    orbit = sorted({apply(matrix, (1, 2, 3)) for matrix in group})
    checks.check("proper orbit of (1, 2, 3) has 24 points", len(orbit) == 24)
    axis_steps = directions()
    checks.check("six axis directions", len(axis_steps) == 6)

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
    signatures = sorted(by_sig)
    checks.check("height signatures number 21", len(signatures) == 21)
    checks.check("the signatures partition 84 bond orbits", dimension == 84)

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

    def joint_dimension(columns: list[int]) -> int:
        local = []
        seen_local = set()
        for row in slice_rows:
            packed = tuple(row[index] for index in columns)
            if any(packed) and packed not in seen_local:
                seen_local.add(packed)
                local.append(packed)
        return len(kernel_basis(local, len(columns)))

    pair_count = 0
    joint_bad = 0
    for left_sig, right_sig in combinations(signatures, 2):
        pair_count += 1
        if joint_dimension(by_sig[left_sig] + by_sig[right_sig]) != 6:
            joint_bad += 1
    checks.check(
        "210 signature pairs each have joint slice kernel 6",
        (pair_count, joint_bad) == (210, 0),
    )
    triple_dimensions = []
    witness_triple = ((-3, -3), (-3, 3), (3, -3))
    witness_dimension = None
    for triple in combinations(signatures, 3):
        columns = [index for sig in triple for index in by_sig[sig]]
        dimension_now = joint_dimension(columns)
        triple_dimensions.append(dimension_now)
        if triple == witness_triple:
            witness_dimension = dimension_now
    checks.check(
        "the triple (-3, -3), (-3, 3), (3, -3) has joint slice kernel 10, the maximum among 1330 triples",
        len(triple_dimensions) == 1330
        and witness_dimension == 10
        and max(triple_dimensions) == 10,
    )

    def support_table(sig: tuple[int, int]):
        columns = by_sig[sig]
        local_rows = []
        seen_local = set()
        for row in slice_rows:
            packed = tuple(row[index] for index in columns)
            if any(packed) and packed not in seen_local:
                seen_local.add(packed)
                local_rows.append(packed)
        basis = kernel_basis(local_rows, len(columns))
        merged = defaultdict(lambda: [Fraction(0), Fraction(0), Fraction(0)])
        for basis_index, local in enumerate(basis):
            coords = [Fraction(0) for _ in range(dimension)]
            for local_index, value in enumerate(local):
                coords[columns[local_index]] = value
            for d_i, direction in enumerate(axis_steps):
                for a_i, left in enumerate(orbit):
                    for b_i, right in enumerate(orbit):
                        value = coords[image_of[(direction, left, right)]]
                        if value:
                            merged[(d_i, a_i, b_i)][basis_index] = value
        by_record = defaultdict(lambda: defaultdict(dict))
        for (d_i, a_i, b_i), coeffs in merged.items():
            by_record[a_i][d_i][b_i] = list(coeffs)
        return by_record

    opposite = [sig for sig in signatures if sig[0] == -sig[1]]
    same_height = [sig for sig in signatures if sig[0] == sig[1]]
    unequal = [sig for sig in signatures if sig[0] != -sig[1] and sig[0] != sig[1]]
    checks.check(
        "six opposite, three equal, and twelve unequal signatures",
        (len(opposite), len(same_height), len(unequal)) == (6, 3, 12),
    )
    tables = {sig: support_table(sig) for sig in same_height + opposite}
    monomials = [(left, right) for left in range(6) for right in range(left, 6)]
    mono_at = {item: index for index, item in enumerate(monomials)}

    def quadric_rows(extra: tuple[int, int], other: tuple[int, int]) -> list[list[Fraction]]:
        blocks = [tables[extra], tables[other]]
        rows: dict[tuple, list[Fraction]] = {}
        for a_i in range(24):
            live = sorted(set(blocks[0].get(a_i, {})) | set(blocks[1].get(a_i, {})))
            for d_i, e_i in combinations(live, 2):
                left_maps = []
                right_maps = []
                for block in blocks:
                    record = block.get(a_i, {})
                    left_maps.append(record.get(d_i, {}))
                    right_maps.append(record.get(e_i, {}))
                b_keys = set(left_maps[0]) | set(left_maps[1])
                c_keys = set(right_maps[0]) | set(right_maps[1])
                for b_i in b_keys:
                    left_values = left_maps[0].get(b_i, [Fraction(0)] * 3) + left_maps[1].get(
                        b_i, [Fraction(0)] * 3
                    )
                    if not any(left_values):
                        continue
                    for c_i in c_keys:
                        right_values = right_maps[0].get(c_i, [Fraction(0)] * 3) + right_maps[1].get(
                            c_i, [Fraction(0)] * 3
                        )
                        if not any(right_values):
                            continue
                        key = (d_i, e_i, b_i, c_i)
                        row = rows.get(key)
                        if row is None:
                            row = [Fraction(0) for _ in monomials]
                            rows[key] = row
                        for left_index in range(6):
                            if left_values[left_index] == 0:
                                continue
                            for right_index in range(left_index, 6):
                                term = left_values[left_index] * right_values[right_index]
                                if left_index != right_index:
                                    term += left_values[right_index] * right_values[left_index]
                                if term:
                                    row[mono_at[(left_index, right_index)]] += term
        reduced, _ = reduced_rows(list(rows.values()), len(monomials))
        return reduced

    def dense(terms: dict[tuple[int, int], Fraction]) -> list[Fraction]:
        row = [Fraction(0) for _ in monomials]
        for (left, right), value in terms.items():
            ordered = (left, right) if left <= right else (right, left)
            row[mono_at[ordered]] += value
        return row

    def quadric_block(base: int) -> list[list[Fraction]]:
        u, v, w = base, base + 1, base + 2
        return [
            dense({(u, u): Fraction(1), (v, w): Fraction(-3, 2), (w, w): Fraction(-4, 3)}),
            dense(
                {
                    (u, v): Fraction(1),
                    (v, v): Fraction(1),
                    (v, w): Fraction(3, 2),
                    (w, w): Fraction(2, 3),
                }
            ),
            dense(
                {
                    (u, w): Fraction(1),
                    (v, v): Fraction(-1),
                    (v, w): Fraction(-1, 2),
                    (w, w): Fraction(2, 3),
                }
            ),
        ]

    def product_rows() -> list[list[Fraction]]:
        return [dense({(left, right): Fraction(1)}) for left in range(3) for right in range(3, 6)]

    def shared_axis_rows(positive: bool) -> list[list[Fraction]]:
        if not positive:
            return [
                dense({(0, 3): Fraction(1), (1, 5): Fraction(-1), (2, 4): Fraction(-1), (2, 5): Fraction(-1)}),
                dense(
                    {
                        (0, 4): Fraction(1),
                        (1, 3): Fraction(1),
                        (1, 4): Fraction(1),
                        (1, 5): Fraction(1),
                        (2, 4): Fraction(1),
                        (2, 5): Fraction(1),
                    }
                ),
                dense({(0, 5): Fraction(1), (1, 4): Fraction(-1), (2, 3): Fraction(1), (2, 5): Fraction(1)}),
            ]
        return [
            dense(
                {
                    (0, 3): Fraction(1),
                    (1, 3): Fraction(1),
                    (1, 4): Fraction(1),
                    (1, 5): Fraction(1),
                    (2, 3): Fraction(1),
                    (2, 5): Fraction(1),
                }
            ),
            dense({(0, 4): Fraction(1), (1, 5): Fraction(-1), (2, 3): Fraction(-1), (2, 5): Fraction(-1)}),
            dense({(0, 5): Fraction(1), (1, 3): Fraction(-1), (2, 4): Fraction(1), (2, 5): Fraction(1)}),
        ]

    def shares_axis(extra: tuple[int, int], other: tuple[int, int]) -> bool:
        for a_i in range(24):
            equal_dirs = set(tables[extra].get(a_i, {}))
            other_dirs = set(tables[other].get(a_i, {}))
            if not other_dirs or not other_dirs <= equal_dirs:
                return False
        return True

    def disjoint_axes(extra: tuple[int, int], other: tuple[int, int]) -> bool:
        for a_i in range(24):
            if set(tables[extra].get(a_i, {})) & set(tables[other].get(a_i, {})):
                return False
        return True

    same_modulus = []
    different_modulus = []
    for extra in same_height:
        for other in opposite:
            if abs(other[0]) == abs(extra[0]):
                same_modulus.append((extra, other))
            else:
                different_modulus.append((extra, other))
    same_modulus_match = all(
        quadric_rows(extra, other) == quadric_block(0) + shared_axis_rows(other[0] > 0)
        and shares_axis(extra, other)
        for extra, other in same_modulus
    )
    different_match = all(
        quadric_rows(extra, other) == quadric_block(0) + product_rows() and disjoint_axes(extra, other)
        for extra, other in different_modulus
    )
    equal_pairs = list(combinations(same_height, 2))
    equal_match = all(
        quadric_rows(extra, other) == quadric_block(0) + product_rows() + quadric_block(3)
        and disjoint_axes(extra, other)
        for extra, other in equal_pairs
    )
    checks.check(
        "six same-modulus pairs share an axis and match the bilinear normal form",
        len(same_modulus) == 6 and same_modulus_match,
    )
    checks.check(
        "twelve different-modulus pairs are disjoint and match the product normal form",
        len(different_modulus) == 12 and different_match,
    )
    checks.check(
        "three equal-height pairs are disjoint and match both quadric blocks",
        len(equal_pairs) == 3 and equal_match,
    )

    def drop_third(row: list[Fraction]) -> list[Fraction]:
        kept = row[:]
        for index, (left, right) in enumerate(monomials):
            if left == 2 or right == 2:
                kept[index] = Fraction(0)
        return kept

    zero_slice = [drop_third(row) for row in quadric_block(0)]
    checks.check(
        "setting the third coordinate to 0 leaves u^2, uv+v^2, and -v^2",
        zero_slice
        == [
            dense({(0, 0): Fraction(1)}),
            dense({(0, 1): Fraction(1), (1, 1): Fraction(1)}),
            dense({(1, 1): Fraction(-1)}),
        ],
    )
    quartic_one, quartic_two = eliminant_quartics()
    checks.check(
        "the eliminant quartics are 36u^4+54u^3-15u^2-72u+10 and 36u^4-69u^2-81u-26",
        (quartic_one, quartic_two)
        == ([36, 54, -15, -72, 10], [36, 0, -69, -81, -26]),
    )
    checks.check(
        "those quartics have resultant 113027603142816",
        resultant_degree_four(quartic_one, quartic_two) == 113027603142816,
    )

    def evaluate(rows: list[list[Fraction]], vector: list[int]) -> list[Fraction]:
        values = []
        for row in rows:
            acc = Fraction(0)
            for index, coeff in enumerate(row):
                left, right = monomials[index]
                acc += coeff * vector[left] * vector[right]
            values.append(acc)
        return values

    partner_vector = [0, 0, 0, 1, 0, 0]
    equal_vector = [1, 0, 0, 0, 0, 0]
    shared_rows = quadric_block(0) + shared_axis_rows(False)
    doubled_rows = quadric_block(0) + product_rows() + quadric_block(3)
    checks.check(
        "a same-modulus partner vector is a zero and a pure equal-height vector is not",
        evaluate(shared_rows, partner_vector) == [Fraction(0)] * len(shared_rows)
        and any(evaluate(shared_rows, equal_vector))
        and any(evaluate(doubled_rows, partner_vector)),
    )
    checks.check("a one-signature stand-in is not this pair count", len(same_modulus) + len(different_modulus) + len(equal_pairs) != 1)

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
