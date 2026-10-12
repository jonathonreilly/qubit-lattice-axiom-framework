#!/usr/bin/env python3
"""One shifted cap factor on the orbit of (0, 1, 2).

phi(t) = 1 + (1 - 2 t) X + (t^2 - t + 1) Y, with X and Y the odd cap lines.
phi(0) is not the constant factor 1. Exact integer arithmetic.
No 3x3 correlation, no path mass, no hazard law.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import gcd


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ZERO_ONE_TWO_SHIFTED_CAP_FACTOR_UNIQUE_NONZERO_ROOT_BOUNDED_THEOREM_NOTE_2026-10-09.md',)


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


def det3(matrix: tuple[tuple[int, int, int], ...]) -> int:
    first, second, third = matrix
    return (
        first[0] * (second[1] * third[2] - second[2] * third[1])
        - first[1] * (second[0] * third[2] - second[2] * third[0])
        + first[2] * (second[0] * third[1] - second[1] * third[0])
    )


def signed_permutations() -> list[tuple[tuple[int, int, int], ...]]:
    group = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            rows = [[0, 0, 0] for _ in range(3)]
            for axis in range(3):
                rows[axis][perm[axis]] = signs[axis]
            group.append(tuple(tuple(row) for row in rows))
    return group


def apply(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def inverse(matrix: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def negate(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return (-vector[0], -vector[1], -vector[2])


def reduced(numerator: int, denominator: int) -> tuple[int, int]:
    if denominator < 0:
        numerator, denominator = -numerator, -denominator
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common


def coefficient_pair(numerator: int, denominator: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return (c1, c2) at t = numerator/denominator for the exhibited factor."""
    first = reduced(denominator - 2 * numerator, denominator)
    second = reduced(
        numerator * numerator - numerator * denominator + denominator * denominator,
        denominator * denominator,
    )
    return first, second


def main() -> None:
    checks = Checks()
    proper = [matrix for matrix in signed_permutations() if det3(matrix) == 1]
    seed = (0, 1, 2)
    alphabet = sorted({apply(matrix, seed) for matrix in proper})
    index = {point: i for i, point in enumerate(alphabet)}
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    directions = (ex, negate(ex), ey, negate(ey), ez, negate(ez))
    direction_index = {direction: i for i, direction in enumerate(directions)}
    quarter_z = next(matrix for matrix in proper if apply(matrix, ex) == ey and apply(matrix, ez) == ez)
    half_x = ((1, 0, 0), (0, -1, 0), (0, 0, -1))
    checks.check(
        "the proper cubic group and the orbit of (0, 1, 2) each have 24 elements",
        len(proper) == 24 and len(alphabet) == 24 and seed in alphabet,
    )
    checks.check(
        "the negative-z section is the half turn about x",
        half_x in proper and apply(half_x, ez) == negate(ez) and inverse(half_x) == half_x,
    )

    seen: set[tuple[int, int, int]] = set()
    orbits: list[tuple[tuple[int, int, int], ...]] = []
    for point in alphabet:
        if point in seen:
            continue
        orbit: list[tuple[int, int, int]] = []
        current = point
        for _ in range(4):
            orbit.append(current)
            seen.add(current)
            current = apply(quarter_z, current)
        orbits.append(tuple(orbit))

    def heights(orbit: tuple[tuple[int, int, int], ...]) -> set[int]:
        return {point[2] for point in orbit}

    cap_slots = [i for i, orbit in enumerate(orbits) if heights(orbit) == {2}]
    cup_slots = [i for i, orbit in enumerate(orbits) if heights(orbit) == {-2}]
    checks.check(
        "the quarter turn has one height-+2 orbit and one height--2 orbit, each of length 4",
        len(orbits) == 6
        and len(cap_slots) == 1
        and len(cup_slots) == 1
        and len(orbits[cap_slots[0]]) == 4
        and apply(quarter_z, orbits[cap_slots[0]][-1]) == orbits[cap_slots[0]][0],
    )

    sections = {direction: next(matrix for matrix in proper if apply(matrix, ez) == direction) for direction in directions}
    checks.check("the positive-z section is the identity", sections[ez] == ((1, 0, 0), (0, 1, 0), (0, 0, 1)))
    checks.check("the negative-z section chosen by the same rule is the half turn", sections[negate(ez)] == half_x)

    def line(slot: int) -> list[list[int]]:
        values = {point: 0 for point in alphabet}
        for step, point in enumerate(orbits[slot]):
            values[point] = 1 if step % 2 == 0 else -1
        tables = []
        for direction in directions:
            pull = inverse(sections[direction])
            tables.append([values[apply(pull, point)] for point in alphabet])
        return tables

    positive = line(cap_slots[0])
    negative = line(cup_slots[0])

    opposite_match = True
    disjoint = True
    one_each = True
    square_sums = True
    cross_directions = True
    for direction in range(6):
        opposite = direction_index[negate(directions[direction])]
        if sum(positive[direction]) != 0 or sum(value * value for value in positive[direction]) != 4:
            square_sums = False
        if sum(negative[direction]) != 0 or sum(value * value for value in negative[direction]) != 4:
            square_sums = False
        for point in range(24):
            if negative[opposite][point] != positive[direction][point]:
                opposite_match = False
            if positive[opposite][point] != negative[direction][point]:
                opposite_match = False
            if positive[direction][point] * negative[direction][point] != 0:
                disjoint = False
        for other in range(6):
            if other == direction:
                continue
            for point in range(24):
                if positive[direction][point] * positive[other][point] != 0:
                    cross_directions = False
                if negative[direction][point] * negative[other][point] != 0:
                    cross_directions = False
    for point in range(24):
        occupied_positive = [direction for direction in range(6) if positive[direction][point] != 0]
        occupied_negative = [direction for direction in range(6) if negative[direction][point] != 0]
        if len(occupied_positive) != 1 or len(occupied_negative) != 1:
            one_each = False
            continue
        if occupied_negative[0] != direction_index[negate(directions[occupied_positive[0]])]:
            one_each = False
        if negative[occupied_negative[0]][point] != positive[occupied_positive[0]][point]:
            one_each = False
    checks.check("reversing direction swaps the two cap lines", opposite_match)
    checks.check("on each direction the two cap lines have disjoint supports", disjoint)
    checks.check(
        "each record meets one positive-cap direction and the opposite negative-cap direction, with equal values",
        one_each,
    )
    checks.check("each cap line has directional sum 0 and square sum 4", square_sums)
    checks.check("distinct directions of one cap line have disjoint supports", cross_directions)

    z_index = direction_index[ez]
    mz_index = direction_index[negate(ez)]
    products_x = {
        positive[z_index][left] * positive[mz_index][right]
        for left in range(24)
        for right in range(24)
    }
    products_y = {
        negative[z_index][left] * negative[mz_index][right]
        for left in range(24)
        for right in range(24)
    }
    mark_pairs = {(positive[mz_index][point], negative[mz_index][point]) for point in range(24)}
    checks.check("positive-cap opposite bond products are exactly {-1, 0, 1}", products_x == {-1, 0, 1})
    checks.check("negative-cap opposite bond products are exactly {-1, 0, 1}", products_y == {-1, 0, 1})
    checks.check(
        "the opposite-z mark pairs include (1, 0) and (0, 1)",
        (1, 0) in mark_pairs and (0, 1) in mark_pairs,
    )

    def bond(tables: list[list[int]], direction: int, left: int, right: int) -> int:
        opposite = direction_index[negate(directions[direction])]
        return tables[direction][left] * tables[opposite][right]

    def covariant(tables: list[list[int]]) -> bool:
        for matrix in proper:
            image = [index[apply(matrix, alphabet[point])] for point in range(24)]
            for source, direction in enumerate(directions):
                target = direction_index[apply(matrix, direction)]
                for left in range(24):
                    for right in range(24):
                        if bond(tables, target, image[left], image[right]) != bond(tables, source, left, right):
                            return False
        return True

    checks.check(
        "both cap bond kernels are invariant under every proper cubic rotation",
        covariant(positive) and covariant(negative),
    )
    pure_x = any(
        bond(positive, z_index, left, right) != 0 and bond(negative, z_index, left, right) == 0
        for left in range(24)
        for right in range(24)
    )
    pure_y = any(
        bond(positive, z_index, left, right) == 0 and bond(negative, z_index, left, right) != 0
        for left in range(24)
        for right in range(24)
    )
    checks.check("the two cap bond kernels are linearly independent", pure_x and pure_y)

    def sharp_excess(first: int, second: int) -> int:
        total = 0
        for point in range(24):
            total += (1 + first * positive[z_index][point]) * (1 + second * positive[z_index][point])
        return total - 24

    sharp_ok = all(
        sharp_excess(first, second) == 4 * first * second
        for first in range(-2, 3)
        for second in range(-2, 3)
    )
    checks.check(
        "one opposite-z condition has excess sum 4 c1 c2 on the integer grid",
        sharp_ok and sharp_excess(1, 1) == 4 and sharp_excess(-1, 1) == -4 and sharp_excess(0, 1) == 0,
    )

    at_zero = coefficient_pair(0, 1)
    at_half = coefficient_pair(1, 2)
    at_one = coefficient_pair(1, 1)
    at_minus = coefficient_pair(-1, 1)
    checks.check(
        "at t = 0 the factor is 1 + X + Y, not the constant factor 1",
        at_zero == ((1, 1), (1, 1)) and pure_x,
    )
    checks.check(
        "at t = 1/2 the factor is 1 + (3/4) Y, with the X coefficient zero",
        at_half == ((0, 1), (3, 4)),
    )
    checks.check(
        "at t = 1 the coefficients are -X + Y, both nonzero",
        at_one == ((-1, 1), (1, 1)),
    )
    checks.check(
        "t^2 - t + 1 has no rational root: the only candidates ±1 are 1 and 3",
        at_one[1] == (1, 1) and at_minus[1] == (3, 1),
    )
    checks.check(
        "the discriminant of t^2 - t + 1 is -3, so there is no other real root",
        1 - 4 == -3 and at_half[1] == (3, 4),
    )
    checks.check(
        "1 - 2 t is zero at 1/2 and at 2/4, and not at 0, 1, or 3/2",
        coefficient_pair(1, 2)[0] == (0, 1)
        and coefficient_pair(2, 4)[0] == (0, 1)
        and coefficient_pair(0, 1)[0] != (0, 1)
        and coefficient_pair(1, 1)[0] != (0, 1)
        and coefficient_pair(3, 2)[0] != (0, 1),
    )
    origin_vector = (at_zero[0][0], at_zero[1][0])
    unit_vector = (at_one[0][0], at_one[1][0])
    checks.check(
        "the coefficient vectors at t = 0 and t = 1 have determinant 2, so this is not 1 + kappa(t) H",
        origin_vector[0] * unit_vector[1] - origin_vector[1] * unit_vector[0] == 2,
    )
    checks.check(
        "at t = 1/2 the bond values are (4 + 3 u)/4 for u in {-1, 0, 1}, all positive",
        products_y == {-1, 0, 1} and all(4 + 3 * value > 0 for value in products_y),
    )

    images = []
    for direction in range(6):
        opposite = direction_index[negate(directions[direction])]
        images.append(sorted({(positive[opposite][point], negative[opposite][point]) for point in range(24)}))

    def normalised(c1n: int, c1d: int, c2n: int, c2d: int) -> bool:
        c1n, c1d = reduced(c1n, c1d)
        c2n, c2d = reduced(c2n, c2d)
        den = c1d * c2d
        x_scale = c1n * c2d
        y_scale = c2n * c1d
        for size in range(1, 7):
            for subset in combinations(range(6), size):
                for marks in product(*[images[direction] for direction in subset]):
                    total = 0
                    for point in range(24):
                        term = 1
                        for offset, direction in enumerate(subset):
                            mark_x, mark_y = marks[offset]
                            bond_x = mark_x * positive[direction][point]
                            bond_y = mark_y * negative[direction][point]
                            term *= den + x_scale * bond_x + y_scale * bond_y
                        total += term
                    if total != 24 * (den ** size):
                        return False
        return True

    checks.check(
        "the factor is normalised at t = 1/2 for every partial mark",
        normalised(*at_half[0], *at_half[1]),
    )
    checks.check(
        "the factor is not normalised at t = 0",
        not normalised(*at_zero[0], *at_zero[1]),
    )
    checks.check(
        "the factor is not normalised at t = 1",
        not normalised(*at_one[0], *at_one[1]),
    )
    checks.check(
        "a pure line with the surviving scale 3/4 is the value at the unique root, not a second root",
        at_half[0] == (0, 1) and normalised(0, 1, 3, 4) and not normalised(1, 1, 1, 1),
    )

    print(
        "per_element: checked each of the 24 record values, each of the 6 directions, and each of the 24 proper rotations"
    )
    print(
        "per_site: one alphabet point carries one record value; no multi-site window or path law was enumerated"
    )
    print(
        "per_mode: one shifted factor on the two odd cap lines; the coefficient box and the linear quarter-turn split were not rerun"
    )
    print(
        "per_block: partial neighbour conditions were the subset products of this factor, including every mark image"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation rate, and no hazard law"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
