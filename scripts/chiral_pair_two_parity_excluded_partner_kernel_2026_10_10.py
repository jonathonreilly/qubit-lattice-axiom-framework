#!/usr/bin/env python3
"""Partner kernels of the two oblique-matched ratio spans."""

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


def formula(s1: int, s2: int, s3: int, negative: bool) -> list[int]:
    matched_sign = -1 if negative else 1
    tail_sign = 1 if negative else -1
    dot_sign = -1 if negative else 1
    return kernel_vector(
        ts=tail_sign * s3,
        prod=tail_sign * s3,
        matched=matched_sign * s1 + 2 * s3,
        swapped=-s2,
        oblique=s1,
        swapped_dot=dot_sign * s2,
        orthogonal=s2,
        scaled=2 * s3,
    )


def pattern(vector: list[int]) -> bool:
    index = {name: position for position, name in enumerate(KERNELS)}
    parity = sum(vector[index[name]] != 0 for name in PARITY)
    excluded = sum(vector[index[name]] != 0 for name in EXCLUDED)
    return parity >= 2 and excluded >= 1


def normalized(row: list[int]) -> tuple[int, ...]:
    pivot = next(value for value in row if value)
    return tuple(int(Fraction(value, pivot)) for value in row)


def ratio(source: list[int], image: list[int]) -> Fraction | None:
    scale = None
    for left, right in zip(source, image):
        if left == 0:
            if right != 0:
                return None
            continue
        value = Fraction(right, left)
        if scale is None:
            scale = value
        elif value != scale:
            return None
    return scale


def scalar_rank() -> int:
    rows = [
        [1, 0, 2],
        [1, 0, -2],
        [0, 1, 2],
        [0, 1, -2],
    ]
    return rank(rows)


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

    formulas_match = rank([list(vector) for vector in SPAN_PLUS]) == 3 and rank(
        [list(vector) for vector in SPAN_MINUS]
    ) == 3
    for negative, span in ((False, SPAN_PLUS), (True, SPAN_MINUS)):
        for position, unit in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
            if formula(*unit, negative) != list(span[position]):
                formulas_match = False
    checks.check(
        "the two spans are the named three-vector formulas and each has rank 3",
        formulas_match,
    )

    index = {name: position for position, name in enumerate(KERNELS)}

    def support(vector: list[int]) -> set[str]:
        return {name for name in KERNELS if vector[index[name]] != 0}

    pattern_matches = True
    for negative, span in ((False, SPAN_PLUS), (True, SPAN_MINUS)):
        line, mixed, caps = span
        line_support = support(line)
        mixed_support = support(mixed)
        cap_support = support(caps)
        parity_line = line_support & set(PARITY)
        parity_mixed = mixed_support & set(PARITY)
        parity_caps = cap_support & set(PARITY)
        if parity_line != {"oblique"} or parity_mixed != {"swapped", "orthogonal"} or parity_caps != {"ts", "prod"}:
            pattern_matches = False
        if len(parity_line & parity_mixed & parity_caps) != 0:
            pattern_matches = False
        if not parity_line.isdisjoint(parity_mixed) or not parity_line.isdisjoint(parity_caps):
            pattern_matches = False
        if not parity_mixed.isdisjoint(parity_caps):
            pattern_matches = False
        dot_name = "swapped_dot"
        if dot_name not in mixed_support or dot_name in line_support or dot_name in cap_support:
            pattern_matches = False
        if "scaled" not in cap_support or "scaled" in line_support or "scaled" in mixed_support:
            pattern_matches = False
        cancelled = formula(-2 if not negative else 2, 0, 1, negative)
        if cancelled[index["matched"]] != 0 or not pattern(cancelled):
            pattern_matches = False
        if pattern(line) or not pattern(mixed) or not pattern(caps):
            pattern_matches = False
    checks.check(
        "a nonzero vector in either span has two parity coefficients and an excluded coefficient exactly off the oblique-matched line",
        pattern_matches,
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

    def classes_for(height_a: int, height_b: int, span: tuple[list[int], ...]) -> tuple[bool, set[tuple[int, ...]]]:
        classes: dict[tuple[str, int], set[tuple[int, ...]]] = {
            (family, sign): set() for family in ("A", "B") for sign in (1, -1)
        }
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
                        triple = []
                        for vector in span:
                            samples_left = [
                                sum(
                                    vector[column] * entry(height_a, first, left, right_a)[column]
                                    for column in range(10)
                                )
                                for left in lefts
                            ]
                            row = []
                            for column in range(10):
                                total = 0
                                for offset, left in enumerate(lefts):
                                    total += samples_left[offset] * entry(height_b, second, left, right_b)[column]
                                row.append(total)
                            triple.append(row)
                        first_row, second_row, third_row = triple
                        if not any(any(row) for row in triple):
                            continue
                        if any(first_row):
                            scale = None if any(second_row) else ratio(first_row, third_row)
                            if scale not in (Fraction(2), Fraction(-2)):
                                return False, set()
                            classes[("A", int(scale) // 2)].add(normalized(first_row))
                            continue
                        scale = ratio(second_row, third_row) if any(second_row) and any(third_row) else None
                        if scale not in (Fraction(2), Fraction(-2)):
                            return False, set()
                        classes[("B", int(scale) // 2)].add(normalized(second_row))
        shapes: set[tuple[int, ...]] = set()
        for group_shapes in classes.values():
            shapes |= group_shapes
        if len(shapes) != 8 or rank([list(row) for row in shapes]) != 7:
            return False, shapes
        if any(group_shapes != shapes for group_shapes in classes.values()):
            return False, shapes
        return True, shapes

    dichotomy = True
    shape_book: dict[tuple[int, int, str], set[tuple[int, ...]]] = {}
    for height_a, height_b in ORDERED_PAIRS:
        for label, span in (("plus", SPAN_PLUS), ("minus", SPAN_MINUS)):
            ok, shapes = classes_for(height_a, height_b, span)
            shape_book[(height_a, height_b, label)] = shapes
            if not ok:
                dichotomy = False
    checks.check(
        "every height pair splits each span into four bond classes, each carrying the same eight directions of rank 7",
        dichotomy,
    )
    checks.check(
        "the four bond scalars vanish together only at the zero coefficient vector",
        scalar_rank() == 3,
    )

    def orthogonal(shapes: set[tuple[int, ...]], vector: list[int]) -> bool:
        return all(sum(row[column] * vector[column] for column in range(10)) == 0 for row in shapes)

    kernels_match = scalar_rank() == 3 and dichotomy
    for height_a, height_b in ORDERED_PAIRS:
        same = (height_a, height_b) in SAME_PAIRS
        expected = {"plus": "plus" if same else "minus", "minus": "minus" if same else "plus"}
        for label, span in (("plus", SPAN_PLUS), ("minus", SPAN_MINUS)):
            shapes = shape_book[(height_a, height_b, label)]
            partner = SPAN_PLUS if expected[label] == "plus" else SPAN_MINUS
            if rank([list(vector) for vector in partner]) != 3:
                kernels_match = False
            if any(not orthogonal(shapes, vector) for vector in partner):
                kernels_match = False
            rows = partner_rows(height_a, height_b, list(span[1]))
            if rank(rows) != 7 or any(
                sum(row[column] * vector[column] for column in range(10)) != 0
                for row in rows
                for vector in partner
            ):
                kernels_match = False
    checks.check(
        "on matching height pairs the partner kernel is the same span, and on the flipped pairs the spans exchange",
        kernels_match,
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

    pass_samples, pass_total = bond_cross(1, 2, PASS_DIRECTIONS, PASS_LEFTS, PASS_RIGHTS, SPAN_PLUS[1], SPAN_PLUS[0])
    checks.check(
        "the swapped-orthogonal vector at heights 1 and 2 has centre pairs (-2, 0) and (0, 2)",
        pass_samples == [(-2, 0), (0, 2)] and pass_total == 0,
    )
    fail_samples, fail_total = bond_cross(1, 3, FAIL_DIRECTIONS, FAIL_LEFTS, FAIL_RIGHTS, SPAN_PLUS[1], SPAN_PLUS[0])
    checks.check(
        "the same vectors at heights 1 and 3 have centre pairs (0, 0) and (-2, 2) and cross sum -4",
        fail_samples == [(0, 0), (-2, 2)] and fail_total == -4,
    )
    print(f"SAME witness {pass_samples} {pass_total}")
    print(f"FLIP witness {fail_samples} {fail_total}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
