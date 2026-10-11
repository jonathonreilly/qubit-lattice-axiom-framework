#!/usr/bin/env python3
"""Cross moments of the parity span on two opposite-height bases."""

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
EXCLUDED = ("matched", "swapped_dot", "scaled")
KAPPA = Fraction(1, 2)
WITNESS_DIRECTIONS = ((-1, 0, 0), (0, -1, 0))
WITNESS_ENDS = ((1, -3, -2), (-3, 2, -1))
SWAPPED_23_ENDS = ((2, -1, -3), (-1, 3, -2))
MOMENT_97 = Fraction(97, 96)
MOMENT_95 = Fraction(95, 96)


def spec_odd_same() -> tuple[dict[str, Fraction], ...]:
    return (
        {"chi": Fraction(1)},
        {"ts": Fraction(1)},
        {"swapped": Fraction(1)},
        {"parallel": Fraction(1), "oblique": Fraction(1)},
    )


def spec_even_same() -> tuple[dict[str, Fraction], ...]:
    return (
        {"prod": Fraction(1)},
        {"parallel": Fraction(-1), "oblique": Fraction(1)},
        {"swapped": Fraction(-1, 2), "orthogonal": Fraction(1)},
    )


def spec_odd_flip() -> tuple[dict[str, Fraction], ...]:
    return (
        {"chi": Fraction(1)},
        {"ts": Fraction(1)},
        {"parallel": Fraction(-1), "oblique": Fraction(1)},
        {"swapped": Fraction(-1, 2), "orthogonal": Fraction(1)},
    )


def spec_even_flip() -> tuple[dict[str, Fraction], ...]:
    return (
        {"prod": Fraction(1)},
        {"swapped": Fraction(1)},
        {"parallel": Fraction(1), "oblique": Fraction(1)},
    )


EXPECTED = {
    (1, 2): (spec_odd_same(), spec_even_same()),
    (2, 1): (spec_odd_same(), spec_even_same()),
    (1, 3): (spec_odd_flip(), spec_even_flip()),
    (3, 1): (spec_odd_same(), spec_even_same()),
    (2, 3): (spec_odd_flip(), spec_even_flip()),
    (3, 2): (spec_odd_flip(), spec_even_flip()),
}


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


def kernel_dimension(rows: list[list[Fraction]]) -> int:
    if not rows:
        return 0
    return len(rows[0]) - rank(rows)


def vector_from(spec: dict[str, Fraction]) -> list[Fraction]:
    return [spec.get(name, Fraction(0)) for name in KERNELS]


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
    count = len(records)

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

    def cap_kernel(kind: str, height: int, direction: tuple[int, int, int], left, right) -> int:
        return cap_sign(kind, height, direction, left) * cap_sign(kind, height, negate(direction), right)

    def transported(seed, height: int, direction: tuple[int, int, int], left, right) -> int:
        inverse = transpose(frames[direction][0])
        return seed(height, apply(inverse, left), apply(inverse, right))

    def raw_kernel(name: str, height: int, direction, left, right) -> int:
        if name in ("chi", "ts", "prod"):
            return cap_kernel(name, height, direction, left, right)
        seeds = {
            "matched": lambda level, a, b: seed_cross(level, a, b, False),
            "swapped": lambda level, a, b: seed_cross(level, a, b, True),
            "parallel": seed_parallel,
            "oblique": seed_oblique,
            "swapped_dot": seed_swapped,
            "orthogonal": seed_orthogonal,
            "scaled": seed_scaled,
        }
        return transported(seeds[name], height, direction, left, right)

    tables: dict[int, list] = {}
    for height in (1, 2, 3):
        tables[height] = [[[0 for _ in records] for _ in records] for _ in axis_steps]
        for direction in axis_steps:
            dir_id = direction_index[direction]
            for left in records:
                if dot(left, direction) != height:
                    continue
                left_id = record_index[left]
                for right in records:
                    if dot(right, direction) != -height:
                        continue
                    right_id = record_index[right]
                    tables[height][dir_id][left_id][right_id] = [
                        raw_kernel(name, height, direction, left, right) for name in KERNELS
                    ]

    def entry(height: int, direction, left, right) -> list[int]:
        return tables[height][direction_index[direction]][record_index[left]][record_index[right]]

    def slices(height: int, partner: int) -> list[tuple[list[int], list[int]]]:
        found = []
        for first in axis_steps:
            for second in axis_steps:
                if axis_index(first) == axis_index(second):
                    continue
                lefts = sorted(
                    left
                    for left in records
                    if dot(left, first) == height and dot(left, second) == partner
                )
                for right in records:
                    if dot(right, first) != -height:
                        continue
                    found.append((entry(height, first, lefts[0], right), entry(height, first, lefts[1], right)))
        return found

    def satisfies(rows: list[tuple[list[int], list[int]]], vector: list[Fraction], even: bool) -> bool:
        for first, second in rows:
            left = sum(vector[index] * first[index] for index in range(10))
            right = sum(vector[index] * second[index] for index in range(10))
            if even and left != right:
                return False
            if not even and left != -right:
                return False
        return True

    parity_ok = True
    for pair, (odd_specs, even_specs) in EXPECTED.items():
        rows = slices(*pair)
        odd_vectors = [vector_from(spec) for spec in odd_specs]
        even_vectors = [vector_from(spec) for spec in even_specs]
        if not all(satisfies(rows, vector, False) for vector in odd_vectors):
            parity_ok = False
        if not all(satisfies(rows, vector, True) for vector in even_vectors):
            parity_ok = False
        odd_equations = [[left + right for left, right in zip(first, second)] for first, second in rows]
        even_equations = [[left - right for left, right in zip(first, second)] for first, second in rows]
        if kernel_dimension(odd_equations) != 4 or kernel_dimension(even_equations) != 3:
            parity_ok = False
        if rank(odd_vectors) != 4 or rank(even_vectors) != 3:
            parity_ok = False
        both = odd_equations + even_equations
        if kernel_dimension(both) != 0:
            parity_ok = False
        span = odd_vectors + even_vectors
        if rank(span) != 7:
            parity_ok = False
        for name in EXCLUDED:
            extra = vector_from({name: Fraction(1)})
            if rank(span + [extra]) != 8:
                parity_ok = False
    checks.check(
        "each height-partner pair has odd dimension 4, even dimension 3, and trivial intersection",
        parity_ok,
    )

    def product_rank(height_a: int, height_b: int) -> int:
        odd_a = [vector_from(spec) for spec in EXPECTED[(height_a, height_b)][0]]
        even_a = [vector_from(spec) for spec in EXPECTED[(height_a, height_b)][1]]
        odd_b = [vector_from(spec) for spec in EXPECTED[(height_b, height_a)][0]]
        even_b = [vector_from(spec) for spec in EXPECTED[(height_b, height_a)][1]]
        rows = []
        for first in axis_steps:
            for second in axis_steps:
                if axis_index(first) == axis_index(second):
                    continue
                lefts = sorted(
                    left
                    for left in records
                    if dot(left, first) == height_a and dot(left, second) == height_b
                )
                rights_a = [right for right in records if dot(right, first) == -height_a]
                rights_b = [right for right in records if dot(right, second) == -height_b]

                def evaluate(height: int, direction, right, vectors: list[list[Fraction]], odd: bool):
                    centers = [entry(height, direction, left, right) for left in lefts]
                    values = []
                    for vector in vectors:
                        left_value = sum(vector[index] * centers[0][index] for index in range(10))
                        right_value = sum(vector[index] * centers[1][index] for index in range(10))
                        values.append(left_value - right_value if odd else left_value + right_value)
                    return values

                cached_a = [
                    (
                        evaluate(height_a, first, right, odd_a, True),
                        evaluate(height_a, first, right, even_a, False),
                    )
                    for right in rights_a
                ]
                cached_b = [
                    (
                        evaluate(height_b, second, right, odd_b, True),
                        evaluate(height_b, second, right, even_b, False),
                    )
                    for right in rights_b
                ]
                for odd_left, even_left in cached_a:
                    for odd_right, even_right in cached_b:
                        row = [left * right for left in odd_left for right in odd_right]
                        row.extend(left * right for left in even_left for right in even_right)
                        rows.append(row)
        return rank(rows)

    checks.check(
        "the odd-odd and even-even products have rank 25 on each height pair",
        all(product_rank(height_a, height_b) == 25 for height_a, height_b in ((1, 2), (1, 3), (2, 3))),
    )

    def coefficient_vector(spec: dict[str, Fraction]) -> list[Fraction]:
        return vector_from(spec)

    def cross_sum(height_a, coeffs_a, height_b, coeffs_b, first, second, right_a, right_b) -> Fraction:
        lefts = [
            left
            for left in records
            if dot(left, first) == height_a and dot(left, second) == height_b
        ]
        total = Fraction(0)
        for left in lefts:
            left_value = sum(
                coeffs_a[index] * entry(height_a, first, left, right_a)[index] for index in range(10)
            )
            right_value = sum(
                coeffs_b[index] * entry(height_b, second, left, right_b)[index] for index in range(10)
            )
            total += left_value * right_value
        return total

    def moment(height_a, coeffs_a, height_b, coeffs_b, first, second, right_a, right_b) -> Fraction:
        return 1 + cross_sum(height_a, coeffs_a, height_b, coeffs_b, first, second, right_a, right_b) / count

    def all_cross_zero(height_a, coeffs_a, height_b, coeffs_b) -> bool:
        for first in axis_steps:
            for second in axis_steps:
                if axis_index(first) == axis_index(second):
                    continue
                for right_a in records:
                    if dot(right_a, first) != -height_a:
                        continue
                    for right_b in records:
                        if dot(right_b, second) != -height_b:
                            continue
                        if cross_sum(height_a, coeffs_a, height_b, coeffs_b, first, second, right_a, right_b) != 0:
                            return False
        return True

    chi = coefficient_vector({"chi": KAPPA})
    prod_cap = coefficient_vector({"prod": KAPPA})
    swapped = coefficient_vector({"swapped": KAPPA})
    dot_sum = coefficient_vector({"parallel": KAPPA, "oblique": KAPPA})
    first_direction, second_direction = WITNESS_DIRECTIONS
    first_end, second_end = WITNESS_ENDS
    chi_moment = moment(1, chi, 2, chi, first_direction, second_direction, first_end, second_end)
    prod_moment = moment(1, prod_cap, 2, prod_cap, first_direction, second_direction, first_end, second_end)
    swapped_moment = moment(1, swapped, 2, swapped, first_direction, second_direction, first_end, second_end)
    checks.check(
        "both-odd and both-even cap pairs have moment 97/96, and swapped at heights 1 and 2 has moment 95/96",
        chi_moment == MOMENT_97 and prod_moment == MOMENT_97 and swapped_moment == MOMENT_95,
    )
    checks.check(
        "an odd vector with an even vector has every cross moment equal to 0",
        all_cross_zero(1, dot_sum, 2, prod_cap) and all_cross_zero(1, chi, 2, prod_cap),
    )
    swapped_23 = moment(
        2,
        swapped,
        3,
        swapped,
        first_direction,
        second_direction,
        SWAPPED_23_ENDS[0],
        SWAPPED_23_ENDS[1],
    )
    checks.check(
        "swapped kernels pass at heights 1 and 3, and heights 2 and 3 have witness moment 95/96",
        all_cross_zero(1, swapped, 3, swapped) and swapped_23 == MOMENT_95,
    )

    def bond_value(direction, left, right) -> Fraction:
        value = Fraction(1)
        if dot(left, direction) == 1 and dot(right, direction) == -1:
            value += sum(dot_sum[index] * entry(1, direction, left, right)[index] for index in range(10))
        if dot(left, direction) == 2 and dot(right, direction) == -2:
            value += sum(prod_cap[index] * entry(2, direction, left, right)[index] for index in range(10))
        return value

    positive_values = {
        bond_value(direction, left, right)
        for direction in axis_steps
        for left in records
        for right in records
    }
    one_neighbour = all(
        sum(bond_value(direction, left, right) for left in records) == count
        for direction in axis_steps
        for right in records
    )
    far_end = all(
        sum(bond_value(direction, left, right) for right in records) == count
        for direction in axis_steps
        for left in records
    )
    live_ok = True
    both_heights = False
    for left in records:
        live = [
            direction
            for direction in axis_steps
            if any(bond_value(direction, left, right) != 1 for right in records)
        ]
        if len(live) > 2 or (len(live) == 2 and live[0] == negate(live[1])):
            live_ok = False
        heights = []
        for direction in live:
            if dot(left, direction) == 1:
                heights.append(1)
            if dot(left, direction) == 2:
                heights.append(2)
        if sorted(heights) == [1, 2]:
            both_heights = True
    checks.check(
        "the odd-even mixture at coefficient 1/2 is strictly positive, with means 1 and at most two live directions",
        positive_values == {Fraction(1, 2), Fraction(1), Fraction(3, 2)}
        and one_neighbour
        and far_end
        and live_ok
        and both_heights,
    )
    print(f"CHI moment {chi_moment}")
    print(f"PROD moment {prod_moment}")
    print(f"SWAPPED 1,2 moment {swapped_moment}")
    print(f"SWAPPED 2,3 moment {swapped_23}")
    print("MIXTURE values " + " ".join(str(value) for value in sorted(positive_values)))
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
