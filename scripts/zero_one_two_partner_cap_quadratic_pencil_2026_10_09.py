#!/usr/bin/env python3
"""Quadratic partner-cap pencils on the orbit of (0, 1, 2).

phi = 1 + t (a X + b Y) + t^2 (c X + d Y), with X and Y the odd cap lines.
Exact integer arithmetic. No 3x3 correlation, no path mass, no hazard law.
"""

from __future__ import annotations

from itertools import combinations, permutations, product
from math import gcd


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ZERO_ONE_TWO_PARTNER_CAP_QUADRATIC_PENCIL_NO_UNIQUE_NONZERO_BOUNDED_THEOREM_NOTE_2026-10-09.md',)


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
    checks.check(
        "reversing direction swaps the two cap lines",
        opposite_match,
    )
    checks.check(
        "on each direction the two cap lines have disjoint supports",
        disjoint,
    )
    checks.check(
        "each record meets one positive-cap direction and the opposite negative-cap direction, with equal values",
        one_each,
    )
    checks.check(
        "each cap line has directional sum 0 and square sum 4",
        square_sums,
    )
    checks.check(
        "distinct directions of one cap line have disjoint supports",
        cross_directions,
    )

    z_index = direction_index[ez]
    mz_index = direction_index[negate(ez)]
    products = {
        positive[z_index][left] * positive[mz_index][right]
        for left in range(24)
        for right in range(24)
    }
    mark_pairs = {(positive[mz_index][point], negative[mz_index][point]) for point in range(24)}
    checks.check(
        "positive-cap opposite bond products are exactly {-1, 0, 1}",
        products == {-1, 0, 1},
    )
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

    pure_x = any(bond(positive, z_index, left, right) != 0 and bond(negative, z_index, left, right) == 0 for left in range(24) for right in range(24))
    pure_y = any(bond(positive, z_index, left, right) == 0 and bond(negative, z_index, left, right) != 0 for left in range(24) for right in range(24))
    checks.check(
        "the two cap bond kernels are linearly independent",
        pure_x and pure_y,
    )

    def sharp_excess(first: int, second: int) -> int:
        total = 0
        for point in range(24):
            total += (1 + first * positive[z_index][point]) * (1 + second * positive[z_index][point])
        return total - 24

    sharp_ok = all(sharp_excess(first, second) == 4 * first * second for first in range(-2, 3) for second in range(-2, 3))
    checks.check(
        "one opposite-z condition has excess sum 4 c1 c2 on the coefficient grid",
        sharp_ok and sharp_excess(1, 1) == 4 and sharp_excess(1, 0) == 0,
    )

    def subset_moment(tables: list[list[int]], subset: tuple[int, ...]) -> int:
        total = 0
        for point in range(24):
            term = 1
            for direction in subset:
                term *= tables[direction][point]
            total += term
        return total

    moments_vanish = True
    products_vanish = True
    for size in range(1, 7):
        for subset in combinations(range(6), size):
            if subset_moment(positive, subset) != 0 or subset_moment(negative, subset) != 0:
                moments_vanish = False
            if size >= 2:
                for point in range(24):
                    term_x = 1
                    term_y = 1
                    for direction in subset:
                        term_x *= positive[direction][point]
                        term_y *= negative[direction][point]
                    if term_x != 0 or term_y != 0:
                        products_vanish = False
    checks.check(
        "every nonempty subset moment of each cap line is zero",
        moments_vanish,
    )
    checks.check(
        "a product of two or more directions on one cap line is identically zero",
        products_vanish,
    )

    def coefficient_polynomials(a: int, b: int, c: int, d: int, numerator: int, denominator: int) -> tuple[tuple[int, int], tuple[int, int]]:
        first = reduced(numerator * (a * denominator + c * numerator), denominator * denominator)
        second = reduced(numerator * (b * denominator + d * numerator), denominator * denominator)
        return first, second

    def root_set(a: int, b: int, c: int, d: int) -> set[tuple[int, int]]:
        roots = {(0, 1)}
        if c != 0:
            roots.add(reduced(-a, c))
        if d != 0:
            roots.add(reduced(-b, d))
        return roots

    box = range(-2, 3)
    only_zero = two = three = dependent = 0
    zero_always = True
    no_other_singleton = True
    no_identically_zero_factor = True
    for a, b, c, d in product(box, repeat=4):
        if a * d - b * c == 0:
            dependent += 1
            continue
        if (a == 0 and c == 0) or (b == 0 and d == 0):
            no_identically_zero_factor = False
        roots = root_set(a, b, c, d)
        if (0, 1) not in roots:
            zero_always = False
        if len(roots) == 1 and roots != {(0, 1)}:
            no_other_singleton = False
        if len(roots) == 1:
            only_zero += 1
        elif len(roots) == 2:
            two += 1
        elif len(roots) == 3:
            three += 1
    checks.check(
        "the coefficient box has 129 dependent tuples and 496 independent tuples",
        dependent == 129 and only_zero + two + three == 496,
    )
    checks.check(
        "independent pencils normalise at exactly one, two, or three rationals: 32, 256, and 208",
        only_zero == 32 and two == 256 and three == 208,
    )
    checks.check(
        "every independent pencil in the box is normalised at 0, and no singleton is a nonzero value",
        zero_always and no_other_singleton and only_zero == 32 and no_identically_zero_factor,
    )

    zero_witness = (1, 0, 0, 1)
    balance_witness = (1, 1, 0, -2)
    triple_witness = (1, 1, -1, -2)
    checks.check(
        "the three named tuples are independent",
        all(a * d - b * c != 0 for a, b, c, d in (zero_witness, balance_witness, triple_witness)),
    )
    checks.check(
        "F = X and G = Y normalise only at 0",
        root_set(*zero_witness) == {(0, 1)},
    )
    checks.check(
        "F = X + Y and G = -2 Y normalise exactly at 0 and 1/2",
        root_set(*balance_witness) == {(0, 1), (1, 2)},
    )
    checks.check(
        "F = X + Y and G = -X - 2 Y normalise exactly at 0, 1/2, and 1",
        root_set(*triple_witness) == {(0, 1), (1, 2), (1, 1)},
    )
    balance_at_half = coefficient_polynomials(*balance_witness, 1, 2)
    checks.check(
        "at t = 1/2 the balance pencil is 1 + (1/2) X, with the Y coefficient zero",
        balance_at_half == ((1, 2), (0, 1)),
    )
    checks.check(
        "at t = 1/2 the balance factors are (2 + product)/2 with product in {-1, 0, 1}, all positive",
        products == {-1, 0, 1} and all(2 + value > 0 for value in products),
    )

    def z_bonds(first: int, second: int) -> list[int]:
        values = []
        for left in range(24):
            for right in range(24):
                values.append(first * bond(positive, z_index, left, right) + second * bond(negative, z_index, left, right))
        return values

    def not_parallel(left: list[int], right: list[int]) -> bool:
        return any(left[i] * right[j] != left[j] * right[i]
                   for i in range(len(left)) for j in range(i))

    checks.check(
        "proportionality accepts noninteger ratios and rejects independent vectors",
        not not_parallel([2, 4], [1, 2])
        and not not_parallel([0, 0], [1, 2])
        and not_parallel([1, -1], [2, -6]),
    )

    checks.check(
        "the balance pencil at t = 1 and t = 2 does not lie on one bond line",
        not_parallel(z_bonds(1, -1), z_bonds(2, -6)),
    )

    images = []
    for direction in range(6):
        opposite = direction_index[negate(directions[direction])]
        images.append(sorted({(positive[opposite][point], negative[opposite][point]) for point in range(24)}))

    def normalised_at(a: int, b: int, c: int, d: int, numerator: int, denominator: int) -> bool:
        scale = denominator * denominator
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
                            numerator_factor = (
                                scale
                                + denominator * numerator * (a * bond_x + b * bond_y)
                                + numerator * numerator * (c * bond_x + d * bond_y)
                            )
                            term *= numerator_factor
                        total += term
                    if total != 24 * (scale ** size):
                        return False
        return True

    checks.check(
        "the balance pencil is normalised at 0 and at 1/2 for every partial mark, and not at 1",
        normalised_at(*balance_witness, 0, 1)
        and normalised_at(*balance_witness, 1, 2)
        and not normalised_at(*balance_witness, 1, 1),
    )
    checks.check(
        "the only-zero pencil is normalised at 0 and not at 1",
        normalised_at(*zero_witness, 0, 1) and not normalised_at(*zero_witness, 1, 1),
    )
    checks.check(
        "the three-root pencil is normalised at 0, 1/2, and 1, and not at 2",
        normalised_at(*triple_witness, 0, 1)
        and normalised_at(*triple_witness, 1, 2)
        and normalised_at(*triple_witness, 1, 1)
        and not normalised_at(*triple_witness, 2, 1),
    )
    checks.check(
        "a dependent pure line is the excluded shape 1 + kappa X and stays normalised at nonzero t",
        1 * 0 - 0 * 2 == 0
        and normalised_at(1, 0, 2, 0, 1, 1)
        and normalised_at(1, 0, 2, 0, 3, 1),
    )

    print(
        "per_element: checked each of the 24 record values, each of the 6 directions, and each of the 24 proper rotations"
    )
    print(
        "per_site: one alphabet point carries one record value; no multi-site window or path law was enumerated"
    )
    print(
        "per_mode: the two odd cap lines were used as a bond basis; the even sector and the linear quarter-turn split were not rerun"
    )
    print(
        "per_block: partial neighbour conditions were the subset products of the quadratic pencil, including every mark image"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation rate, and no hazard law"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
