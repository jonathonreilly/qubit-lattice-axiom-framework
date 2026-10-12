#!/usr/bin/env python3
"""Whether soldered covariance forces kappa on the orbit of (0, 1, 2).

Rank-1 bond products phi = 1 + kappa X_d(a) X_{-d}(b), exact integer arithmetic.
The carrier is that 24-point alphabet. No 3x3 correlation and no path mass.
"""

from __future__ import annotations

from itertools import combinations, permutations, product


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ZERO_ONE_TWO_SOLDERED_BOND_KAPPA_NOT_FORCED_BOUNDED_THEOREM_NOTE_2026-10-09.md',)


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
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def perm_sign(axes: tuple[int, int, int]) -> int:
    sign = 1
    values = list(axes)
    for i in range(3):
        for j in range(i + 1, 3):
            if values[i] > values[j]:
                sign = -sign
    return sign


def roles(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    zero = next(i for i in range(3) if vector[i] == 0)
    unit = next(i for i in range(3) if abs(vector[i]) == 1)
    maximum = next(i for i in range(3) if abs(vector[i]) == 2)
    return zero, unit, maximum


def epsilon(vector: tuple[int, int, int]) -> int:
    zero, unit, maximum = roles(vector)
    return perm_sign((zero, unit, maximum)) * ((-1) ** maximum)


def cap_direction(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    maximum = roles(vector)[2]
    sign = 1 if vector[maximum] > 0 else -1
    direction = [0, 0, 0]
    direction[maximum] = sign
    return (direction[0], direction[1], direction[2])


def signed_permutations() -> list[tuple[tuple[int, int, int], ...]]:
    group = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            rows = [[0, 0, 0] for _ in range(3)]
            for i in range(3):
                rows[i][perm[i]] = signs[i]
            group.append(tuple(tuple(row) for row in rows))
    return group


def apply(matrix: tuple[tuple[int, int, int], ...], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(3)) for i in range(3))


def inverse(matrix: tuple[tuple[int, int, int], ...]) -> tuple[tuple[int, int, int], ...]:
    return tuple(tuple(matrix[j][i] for j in range(3)) for i in range(3))


def negate(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return (-vector[0], -vector[1], -vector[2])


def main() -> None:
    checks = Checks()
    full = signed_permutations()
    proper = [matrix for matrix in full if det3(matrix) == 1]
    seed = (0, 1, 2)
    alphabet = sorted({apply(matrix, seed) for matrix in proper})
    index = {point: i for i, point in enumerate(alphabet)}
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    directions = (ex, negate(ex), ey, negate(ey), ez, negate(ez))
    direction_index = {direction: i for i, direction in enumerate(directions)}
    quarter_z = next(
        matrix
        for matrix in proper
        if apply(matrix, ex) == ey and apply(matrix, ez) == ez
    )
    half_x = ((1, 0, 0), (0, -1, 0), (0, 0, -1))

    seen: set[tuple[int, int, int]] = set()
    orbits: list[tuple[tuple[int, int, int], ...]] = []
    for point in alphabet:
        if point in seen:
            continue
        orbit = []
        current = point
        for _ in range(4):
            orbit.append(current)
            seen.add(current)
            current = apply(quarter_z, current)
        orbits.append(tuple(orbit))

    def kind(orbit: tuple[tuple[int, int, int], ...]) -> str:
        heights = {point[2] for point in orbit}
        if heights == {2}:
            return "cap+"
        if heights == {-2}:
            return "cap-"
        if heights == {1}:
            return "eq+"
        if heights == {-1}:
            return "eq-"
        return "eq0"

    kinds = [kind(orbit) for orbit in orbits]
    by_kind: dict[str, list[int]] = {}
    for i, label in enumerate(kinds):
        by_kind.setdefault(label, []).append(i)

    sections = {
        direction: next(matrix for matrix in proper if apply(matrix, ez) == direction)
        for direction in directions
    }

    def family(coefficients: tuple[int, ...], sector: str) -> list[tuple[int, ...]]:
        values = {point: 0 for point in alphabet}
        for i, orbit in enumerate(orbits):
            for step, point in enumerate(orbit):
                if sector == "even" or step % 2 == 0:
                    values[point] = coefficients[i]
                else:
                    values[point] = -coefficients[i]
        tables = []
        for direction in directions:
            pull = inverse(sections[direction])
            tables.append(tuple(values[apply(pull, point)] for point in alphabet))
        return tables

    def character_table(tables: list[tuple[int, ...]]) -> tuple[int, ...] | None:
        characters: list[int] = []
        for matrix in proper:
            image = [index[apply(matrix, point)] for point in alphabet]
            for source_index, direction in enumerate(directions):
                target_index = direction_index[apply(matrix, direction)]
                character = None
                for source_point, target_point in enumerate(image):
                    source = tables[source_index][source_point]
                    target = tables[target_index][target_point]
                    if source == 0:
                        if target != 0:
                            return None
                        continue
                    ratio = target // source
                    if ratio not in (1, -1) or ratio * source != target:
                        return None
                    if character is None:
                        character = ratio
                    elif character != ratio:
                        return None
                characters.append(1 if character is None else character)
            for source_index, direction in enumerate(directions):
                opposite = direction_index[negate(direction)]
                if characters[-6 + source_index] * characters[-6 + opposite] != 1:
                    return None
        return tuple(characters)

    def cocycle_ok(tables: list[tuple[int, ...]]) -> bool:
        return character_table(tables) is not None

    def direct_product_ok(tables: list[tuple[int, ...]]) -> bool:
        matrix = quarter_z
        image = [index[apply(matrix, point)] for point in alphabet]
        for source_index, direction in enumerate(directions):
            target = direction_index[apply(matrix, direction)]
            opposite_target = direction_index[apply(matrix, negate(direction))]
            opposite = direction_index[negate(direction)]
            for left, left_image in enumerate(image):
                for right, right_image in enumerate(image):
                    if (
                        tables[target][left_image] * tables[opposite_target][right_image]
                        != tables[source_index][left] * tables[opposite][right]
                    ):
                        return False
        return True

    def moment(tables: list[tuple[int, ...]], subset: tuple[int, ...]) -> int:
        total = 0
        for point in range(24):
            term = 1
            for direction in subset:
                term *= tables[direction][point]
            total += term
        return total

    def all_moments(tables: list[tuple[int, ...]]) -> list[tuple[tuple[int, ...], int]]:
        found = []
        for size in range(1, 7):
            for subset in combinations(range(6), size):
                value = moment(tables, subset)
                if value != 0:
                    found.append((subset, value))
        return found

    checks.check("proper cubic group has order 24 and the orbit has 24 points", len(proper) == 24 and len(alphabet) == 24)
    checks.check(
        "quarter turn has six orbits of length 4",
        len(orbits) == 6 and all(len(orbit) == 4 and apply(quarter_z, orbit[-1]) == orbit[0] for orbit in orbits),
    )
    checks.check(
        "the six orbits are the two caps, the two unit heights, and two zero heights",
        sorted(kinds) == ["cap+", "cap-", "eq+", "eq-", "eq0", "eq0"],
    )
    checks.check(
        "the section along e_z is the identity, so X_z reads the eigenfunction",
        sections[ez] == ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
    )
    checks.check(
        "half turn about x is proper, squares to the identity, and sends e_z to -e_z",
        half_x in proper and apply(half_x, ez) == negate(ez) and apply(half_x, apply(half_x, ex)) == ex and apply(half_x, apply(half_x, ez)) == ez,
    )

    even_basis = [family(tuple(1 if i == slot else 0 for i in range(6)), "even") for slot in range(6)]
    odd_basis = [family(tuple(1 if i == slot else 0 for i in range(6)), "odd") for slot in range(6)]
    half = ((1, 0, 0), (0, -1, 0), (0, 0, -1))
    def multiply(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3))
                           for j in range(3)) for i in range(3))
    checks.check(
        "opposite sections are matched by the x half turn",
        all(sections[negate(d)] == multiply(sections[d], half) for d in (ex, ey, ez)),
    )
    # Changing sigma_x to sigma_x Q flips just the x family in the odd sector.
    unmatched = [tuple(-v for v in row) if directions[i] == ex else row
                 for i, row in enumerate(odd_basis[by_kind["cap+"][0]])]
    checks.check(
        "an independently changed positive-x section breaks opposite-character covariance",
        character_table(unmatched) is None,
    )
    even_characters = [character_table(table) for table in even_basis]
    odd_characters = [character_table(table) for table in odd_basis]
    checks.check(
        "all 6 even lines share one cocycle and all 6 odd lines share another",
        all(table is not None for table in even_characters + odd_characters)
        and len(set(even_characters)) == 1
        and len(set(odd_characters)) == 1,
    )
    even_sum = family((1, -2, 3, -4, 5, -6), "even")
    odd_sum = family((1, 2, -3, 4, -5, 6), "odd")
    checks.check(
        "one even combination and one odd combination keep the sector cocycle",
        character_table(even_sum) == even_characters[0] and character_table(odd_sum) == odd_characters[0],
    )
    mixed = [
        tuple(even_basis[by_kind["cap+"][0]][direction][point] + odd_basis[by_kind["cap+"][0]][direction][point] for point in range(24))
        for direction in range(6)
    ]
    checks.check(
        "a sum of the two eigenvalues on the positive cap is not a cocycle",
        not cocycle_ok(mixed),
    )
    checks.check(
        "the quarter turn's raw products match the cocycle on one even and one odd line",
        direct_product_ok(even_basis[by_kind["cap+"][0]]) and direct_product_ok(odd_basis[by_kind["cap+"][0]]),
    )

    def opposite_moment(coefficients: tuple[int, ...], sector: str) -> int:
        tables = family(coefficients, sector)
        return moment(tables, (direction_index[ez], direction_index[negate(ez)]))

    def perpendicular_moment(coefficients: tuple[int, ...], sector: str) -> int:
        tables = family(coefficients, sector)
        return moment(tables, (direction_index[ez], direction_index[ex]))

    def mean_sum(coefficients: tuple[int, ...], sector: str) -> int:
        tables = family(coefficients, sector)
        return moment(tables, (direction_index[ez],))

    partner_slots = (
        (by_kind["cap+"][0], by_kind["cap-"][0]),
        (by_kind["eq+"][0], by_kind["eq-"][0]),
        (by_kind["eq0"][0], by_kind["eq0"][1]),
    )

    def partner_products(coefficients: tuple[int, ...]) -> int:
        return sum(coefficients[left] * coefficients[right] for left, right in partner_slots)

    def partner_sums(coefficients: tuple[int, ...]) -> tuple[int, int, int]:
        return tuple(coefficients[left] + coefficients[right] for left, right in partner_slots)

    probes = []
    for i in range(6):
        probes.append(tuple(1 if j == i else 0 for j in range(6)))
    for i, j in combinations(range(6), 2):
        vector = [0, 0, 0, 0, 0, 0]
        vector[i] = 1
        vector[j] = 1
        probes.append(tuple(vector))
    checks.check(
        "even opposite moment is 8 times the three partner products, on every pair probe",
        all(opposite_moment(vector, "even") == 8 * partner_products(vector) for vector in probes),
    )
    checks.check(
        "odd opposite moment obeys the same partner formula",
        all(opposite_moment(vector, "odd") == 8 * partner_products(vector) for vector in probes),
    )

    def perpendicular_closed(coefficients: tuple[int, ...]) -> int:
        first, second, third = partner_sums(coefficients)
        return 2 * (first * second + first * third + second * third)

    checks.check(
        "even perpendicular moment is 2(st+su+tu) on the partner sums",
        all(perpendicular_moment(vector, "even") == perpendicular_closed(vector) for vector in probes),
    )
    checks.check(
        "even directional sum is 4 times the coefficient sum",
        all(mean_sum(vector, "even") == 4 * sum(vector) for vector in probes),
    )
    checks.check(
        "every odd family has directional sum 0",
        all(mean_sum(vector, "odd") == 0 for vector in probes),
    )

    square_polynomial: dict[tuple[int, int, int], int] = {}

    def add_monomial(powers: tuple[int, int, int], coefficient: int) -> None:
        square_polynomial[powers] = square_polynomial.get(powers, 0) + coefficient

    for powers, coefficient in (
        ((2, 0, 0), 1),
        ((0, 2, 0), 1),
        ((0, 0, 2), 1),
        ((1, 1, 0), 2),
        ((1, 0, 1), 2),
        ((0, 1, 1), 2),
    ):
        add_monomial(powers, coefficient)
    for powers in (((1, 1, 0), -2), ((1, 0, 1), -2), ((0, 1, 1), -2), ((2, 0, 0), -1), ((0, 2, 0), -1), ((0, 0, 2), -1)):
        add_monomial(powers[0], powers[1])
    checks.check(
        "the quadratic (s+t+u)^2 - 2(st+su+tu) - (s^2+t^2+u^2) has every coefficient zero",
        square_polynomial != {} and all(coefficient == 0 for coefficient in square_polynomial.values()),
    )

    antisymmetric_ok = True
    for p_value, q_value, r_value in product((0, 1, 2), repeat=3):
        coefficients = [0, 0, 0, 0, 0, 0]
        for value, (left, right) in zip((p_value, q_value, r_value), partner_slots):
            coefficients[left] = value
            coefficients[right] = -value
        vector = tuple(coefficients)
        squares = p_value * p_value + q_value * q_value + r_value * r_value
        if (
            partner_products(vector) != -squares
            or mean_sum(vector, "even") != 0
            or perpendicular_moment(vector, "even") != 0
            or opposite_moment(vector, "even") != -8 * squares
        ):
            antisymmetric_ok = False
    checks.check(
        "on the degree-determining grid, partner-antisymmetric even moments are mean 0, perpendicular 0, and opposite -8(p^2+q^2+r^2)",
        antisymmetric_ok,
    )

    odd_lines_flat = all(all_moments(table) == [] for table in odd_basis)
    one_support = True
    for table in odd_basis:
        for point in range(24):
            occupied = [direction for direction in range(6) if table[direction][point] != 0]
            if len(occupied) != 1:
                one_support = False
    checks.check(
        "each odd pure orbit line has every subset moment zero",
        odd_lines_flat,
    )
    checks.check(
        "on an odd pure line each point meets exactly one direction",
        one_support,
    )

    cap_pair = [0, 0, 0, 0, 0, 0]
    cap_pair[by_kind["cap+"][0]] = 1
    cap_pair[by_kind["cap-"][0]] = 1
    cap_pair_t = tuple(cap_pair)
    cap_only = [0, 0, 0, 0, 0, 0]
    cap_only[by_kind["cap+"][0]] = 1
    cap_only_t = tuple(cap_only)
    cap_and_eq = [0, 0, 0, 0, 0, 0]
    cap_and_eq[by_kind["cap+"][0]] = 1
    cap_and_eq[by_kind["eq+"][0]] = 1
    cap_and_eq_t = tuple(cap_and_eq)
    checks.check(
        "the odd two-cap family has opposite moment 8, so it is not moment-flat",
        opposite_moment(cap_pair_t, "odd") == 8 and all_moments(family(cap_pair_t, "odd")) != [],
    )
    checks.check(
        "the odd cap-plus-equator family has a nonzero perpendicular moment",
        perpendicular_moment(cap_and_eq_t, "odd") != 0,
    )

    pure = odd_basis[by_kind["cap+"][0]]
    # Find a pair with product +1.
    plus_pair = None
    z_index = direction_index[ez]
    mz_index = direction_index[negate(ez)]
    for left in range(24):
        for right in range(24):
            if pure[z_index][left] * pure[mz_index][right] == 1:
                plus_pair = (left, right)
                break
        if plus_pair:
            break
    checks.check("the odd positive-cap line has a bond with product +1", plus_pair is not None)

    def one_bond_average(tables: list[tuple[int, ...]], left: int, right: int, kappa: int) -> tuple[int, int]:
        mark = tables[mz_index][right]
        total = 0
        for point in range(24):
            total += 1 + kappa * mark * tables[z_index][point]
        return total, 24

    if plus_pair is not None:
        product_value = pure[z_index][plus_pair[0]] * pure[mz_index][plus_pair[1]]
        doubled = family(tuple(2 if i == by_kind["cap+"][0] else 0 for i in range(6)), "odd")
        doubled_product = doubled[z_index][plus_pair[0]] * doubled[mz_index][plus_pair[1]]
        checks.check(
            "a pure line scales by c^2: the bond product at c=2 is 4 times the product at c=1",
            product_value == 1 and doubled_product == 4,
        )
        sum_one, _ = one_bond_average(pure, plus_pair[0], plus_pair[1], 1)
        sum_zero, _ = one_bond_average(pure, plus_pair[0], plus_pair[1], 0)
        point_factor = 1 + product_value
        checks.check(
            "the pure odd line is pointwise 2 at kappa 1 on that bond, while the one-bond average stays 1",
            point_factor == 2 and sum_one == 24 and sum_zero == 24,
        )

    flat_kappas = True
    for kappa in (0, 1, 2, -3):
        for marks in product((-1, 0, 1), repeat=6):
            total = 0
            for point in range(24):
                term = 1
                for direction in range(6):
                    if marks[direction] == 0:
                        continue
                    term *= 1 + kappa * marks[direction] * pure[direction][point]
                total += term
            if total != 24:
                flat_kappas = False
    checks.check(
        "the odd positive-cap line has mean 1 for every mark in {-1,0,1}^6 at four kappa values",
        flat_kappas,
    )

    even_cap = even_basis[by_kind["cap+"][0]]
    even_gamma = next(point for point in range(24) if even_cap[mz_index][point] != 0)
    even_at_one, _ = one_bond_average(even_cap, 0, even_gamma, 1)
    even_at_zero, _ = one_bond_average(even_cap, 0, even_gamma, 0)
    checks.check(
        "the even positive-cap indicator has sum 4 and the one-bond excess scales as kappa",
        mean_sum(cap_only_t, "even") == 4 and even_at_zero == 24 and even_at_one - 24 == 4 * even_cap[mz_index][even_gamma] and even_at_one != 24,
    )

    bond_products = {
        pure[z_index][left] * pure[mz_index][right]
        for left in range(24)
        for right in range(24)
    }
    checks.check(
        "unit pure-line opposite bond products are exactly {-1, 0, 1}",
        bond_products == {-1, 0, 1},
    )

    odd_witness = family(cap_and_eq_t, "odd")
    witness_moment = perpendicular_moment(cap_and_eq_t, "odd")
    # marks are values of the opposite functions, chosen nonzero
    mark_z = next(odd_witness[mz_index][point] for point in range(24) if odd_witness[mz_index][point] != 0)
    mark_x = next(
        odd_witness[direction_index[negate(ex)]][point]
        for point in range(24)
        if odd_witness[direction_index[negate(ex)]][point] != 0
    )
    active = (direction_index[ez], direction_index[ex])

    def two_bond_sum(kappa: int) -> int:
        total = 0
        for point in range(24):
            total += (1 + kappa * mark_z * odd_witness[z_index][point]) * (
                1 + kappa * mark_x * odd_witness[direction_index[ex]][point]
            )
        return total

    excess_one = two_bond_sum(1) - 24
    excess_two = two_bond_sum(2) - 24
    excess_zero = two_bond_sum(0) - 24
    checks.check(
        "a two-bond odd witness is homogeneous of degree 2 and nonzero at kappa 1",
        excess_zero == 0 and excess_two == 4 * excess_one and excess_one == witness_moment * mark_z * mark_x and excess_one != 0,
    )

    # Half turn links opposite functions on odd lines.
    linked = True
    for slot in range(6):
        tables = odd_basis[slot]
        ratios = set()
        for point in alphabet:
            source = tables[z_index][index[apply(half_x, point)]]
            target = tables[mz_index][index[point]]
            if source == 0 and target == 0:
                continue
            if source == 0 or target % source != 0:
                linked = False
                break
            ratios.add(target // source)
        if ratios not in (set(), {1}, {-1}):
            linked = False
    checks.check(
        "on each odd line, X_{-z} is a constant sign times X_z composed with the half turn",
        linked,
    )

    # Cycle-6 axis-role product, compared only as a bond product, not as a path mass.
    cycle6 = []
    for direction in directions:
        cycle6.append(
            tuple(
                epsilon(point) if cap_direction(point) == direction else 0
                for point in alphabet
            )
        )
    cap_slot = by_kind["cap+"][0]
    line = odd_basis[cap_slot]
    sign = line[z_index][index[(0, 1, 2)]]
    products_match = True
    for direction in range(6):
        opposite = direction_index[negate(directions[direction])]
        for left in range(24):
            for right in range(24):
                if line[direction][left] * line[opposite][right] != cycle6[direction][left] * cycle6[opposite][right]:
                    products_match = False
    checks.check(
        "the odd positive-cap line reproduces the axis-role bond product",
        sign != 0 and products_match and all_moments(line) == [],
    )

    # Expansion identity at kappa = 1 for one mixed mark on the witness and the pure line.
    def expansion_holds(tables: list[tuple[int, ...]], marks: tuple[int, ...]) -> bool:
        direct = 0
        for point in range(24):
            term = 1
            for direction in range(6):
                term *= 1 + marks[direction] * tables[direction][point]
            direct += term
        reconstructed = 24
        for size in range(1, 7):
            for subset in combinations(range(6), size):
                coefficient = moment(tables, subset)
                for direction in subset:
                    coefficient *= marks[direction]
                reconstructed += coefficient
        return direct == reconstructed

    sample_marks = (1, -1, 0, 1, 0, -1)
    checks.check(
        "the subset expansion of one full mark agrees on the witness and the pure line",
        expansion_holds(odd_witness, sample_marks) and expansion_holds(pure, sample_marks),
    )

    print(
        "per_element: checked each of the 24 record values and each of the 6 directions for support, cocycle ratios, and subset moments"
    )
    print(
        "per_site: one alphabet point carries one record value; no multi-site window or path law was enumerated"
    )
    print(
        "per_mode: even and odd quarter-turn sectors were separated; their sum on one cap is not a cocycle"
    )
    print(
        "per_block: partial neighbour conditions were used only through subset moments and explicit one-bond and two-bond factors"
    )
    print(
        "lattice_wide: checked and not executed — no infinite lattice, no formation rate, and no hazard law"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
