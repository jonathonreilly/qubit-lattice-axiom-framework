#!/usr/bin/env python3
"""Order-blind factor on the achiral proper orbit of (0, 1, 2).

The carrier is that 24-point alphabet of record values, not a 3x3 bond
correlation and not the chiral pair of (1, 2, 3). Exact rational arithmetic.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/ACHIRAL_ZERO_ONE_TWO_ORBIT_ORDER_BLIND_FACTOR_BOUNDED_THEOREM_NOTE_2026-10-09.md',)


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


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(x * y for x, y in zip(left, right))


def roles(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    zero = next(i for i in range(3) if vector[i] == 0)
    unit = next(i for i in range(3) if abs(vector[i]) == 1)
    maximum = next(i for i in range(3) if abs(vector[i]) == 2)
    return zero, unit, maximum


def epsilon(vector: tuple[int, int, int]) -> int:
    zero, unit, maximum = roles(vector)
    return perm_sign((zero, unit, maximum)) * (-1) ** maximum


def cap_direction(vector: tuple[int, int, int]) -> tuple[int, int, int]:
    maximum = roles(vector)[2]
    sign = 1 if vector[maximum] > 0 else -1
    direction = [0, 0, 0]
    direction[maximum] = sign
    return (direction[0], direction[1], direction[2])


def factor(direction: tuple[int, int, int], vector: tuple[int, int, int]) -> int:
    if direction == cap_direction(vector):
        return epsilon(vector)
    return 0


def transverse_product(direction: tuple[int, int, int], vector: tuple[int, int, int]) -> int:
    if dot(vector, direction) != 2:
        return 0
    transverse = [vector[i] for i in range(3) if direction[i] == 0]
    return transverse[0] * transverse[1]


def main() -> None:
    checks = Checks()
    full = signed_permutations()
    proper = [matrix for matrix in full if det3(matrix) == 1]
    seed = (0, 1, 2)
    alphabet = sorted({apply(matrix, seed) for matrix in proper})
    full_orbit = {apply(matrix, seed) for matrix in full}
    ex, ey, ez = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    directions = (ex, (-1, 0, 0), ey, (0, -1, 0), ez, (0, 0, -1))
    quarter_z = next(
        matrix
        for matrix in proper
        if apply(matrix, ex) == ey and apply(matrix, ez) == ez
    )
    reflection = ((1, 0, 0), (0, 1, 0), (0, 0, -1))
    kappa = Fraction(1, 2)

    checks.check("proper cubic group has order 24", len(proper) == 24 and len(full) == 48)
    checks.check(
        "orbit of (0, 1, 2) has 24 points and equals its mirror orbit",
        len(alphabet) == 24 and full_orbit == set(alphabet),
    )
    checks.check(
        "every point has coordinates {0, ±1, ±2} with those absolute values once",
        all(sorted(abs(entry) for entry in vector) == [0, 1, 2] for vector in alphabet),
    )
    checks.check(
        "(1, 2, 3) transverse product is identically 0 on this orbit",
        all(transverse_product(direction, vector) == 0 for direction in directions for vector in alphabet)
        and all(3 not in vector and -3 not in vector for vector in alphabet),
    )

    checks.check(
        "each value lies on exactly one cap and the cap sign is ±1",
        all(
            sum(1 for direction in directions if factor(direction, vector) != 0) == 1
            and abs(epsilon(vector)) == 1
            for vector in alphabet
        ),
    )
    checks.check(
        "each direction sums to 0 on its four-point cap",
        all(
            sum(1 for vector in alphabet if factor(direction, vector) != 0) == 4
            and sum(factor(direction, vector) for vector in alphabet) == 0
            for direction in directions
        ),
    )
    checks.check(
        "positive-z cap is a quarter-turn eigenfunction of eigenvalue -1",
        all(factor(ez, apply(quarter_z, vector)) == -factor(ez, vector) for vector in alphabet)
        and any(factor(ez, vector) != 0 for vector in alphabet),
    )

    def phi(
        direction: tuple[int, int, int],
        left: tuple[int, int, int],
        right: tuple[int, int, int],
    ) -> Fraction:
        opposite = tuple(-entry for entry in direction)
        return 1 + kappa * factor(direction, left) * factor(opposite, right)

    checks.check(
        "bond symmetry on all 6 directions and 24 x 24 value pairs",
        all(
            phi(direction, left, right) == phi(tuple(-entry for entry in direction), right, left)
            for direction in directions
            for left in alphabet
            for right in alphabet
        ),
    )
    checks.check(
        "soldered covariance under all 24 proper rotations",
        all(
            phi(apply(matrix, direction), apply(matrix, left), apply(matrix, right))
            == phi(direction, left, right)
            for matrix in proper
            for direction in directions
            for left in alphabet
            for right in alphabet
        ),
    )

    def fixes(matrix: tuple[tuple[int, int, int], ...]) -> bool:
        inverse_matrix = inverse(matrix)
        return all(
            factor(apply(inverse_matrix, direction), apply(inverse_matrix, vector))
            == factor(direction, vector)
            for direction in directions
            for vector in alphabet
        )

    proper_fixed = sum(1 for matrix in proper if fixes(matrix))
    improper_fixed = sum(1 for matrix in full if det3(matrix) == -1 and fixes(matrix))
    checks.check(
        "diag(1, 1, -1) fixes the family, with 4 proper and 4 improper fixers",
        det3(reflection) == -1 and fixes(reflection) and proper_fixed == 4 and improper_fixed == 4,
    )

    def ungauged(direction, vector):
        return perm_sign(roles(vector)) if direction == cap_direction(vector) else 0

    def fixes_ungauged(matrix):
        return all(ungauged(apply(matrix, d), apply(matrix, a)) == ungauged(d, a)
                   for d in directions for a in alphabet)

    checks.check(
        "without the axis gauge both reflections still fix the family, with 12 proper and 12 improper fixers",
        fixes_ungauged(reflection)
        and sum(fixes_ungauged(m) for m in proper) == 12
        and sum(fixes_ungauged(m) for m in full if det3(m) == -1) == 12
        and all(ungauged(d, a) * ungauged(tuple(-x for x in d), b)
                == factor(d, a) * factor(tuple(-x for x in d), b)
                for d in directions for a in alphabet for b in alphabet),
    )

    values = (-1, 0, 1)
    normalised = True
    class_count = 0
    for assignment in product(values, repeat=6):
        class_count += 1
        total = Fraction(0)
        for vector in alphabet:
            weight = Fraction(1)
            for direction, mark in zip(directions, assignment):
                weight *= 1 + kappa * factor(direction, vector) * mark
            total += weight
        normalised = normalised and total == len(alphabet)
    checks.check(
        "every one of the 3^6 neighbor classes has mean 1",
        normalised and class_count == 729,
    )
    checks.check(
        "the factor varies: phi_z((0, 1, 2), (0, 1, -2)) = 3/2",
        phi(ez, (0, 1, 2), (0, 1, -2)) == Fraction(3, 2)
        and factor(ez, (0, 1, 2)) == 1
        and factor((0, 0, -1), (0, 1, -2)) == 1,
    )
    minimum = min(
        phi(direction, left, right)
        for direction in directions
        for left in alphabet
        for right in alphabet
    )
    checks.check("every bond factor at kappa = 1/2 is at least 1/2", minimum == Fraction(1, 2))

    one_site = Fraction(1, 24)

    def rule(value: tuple[int, int, int], condition: dict[tuple[int, int, int], tuple[int, int, int]]) -> Fraction:
        weight = one_site
        for direction, neighbor in condition.items():
            weight *= phi(direction, value, neighbor)
        return weight

    path = ((0, 0, 0), (0, 0, 1), (0, 0, 2))

    def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
        return tuple(x + y for x, y in zip(left, right))

    def finished(order: tuple[tuple[int, int, int], ...]) -> dict[tuple, Fraction]:
        law: dict[tuple, Fraction] = {}
        for config in product(alphabet, repeat=3):
            placed = dict(zip(path, config))
            formed: dict[tuple[int, int, int], tuple[int, int, int]] = {}
            weight = Fraction(1)
            for site in order:
                condition = {
                    direction: formed[add(site, direction)]
                    for direction in directions
                    if add(site, direction) in formed
                }
                weight *= rule(placed[site], condition)
                formed[site] = placed[site]
            law[config] = weight
        return law

    laws = {order: finished(order) for order in permutations(path)}
    base_order = path
    base = laws[base_order]
    checks.check(
        "all 6 formation orders of the 3-site path give one law of mass 1",
        all(law == base for law in laws.values()) and sum(base.values()) == 1 and len(base) == 24 ** 3,
    )
    ends: dict[tuple, Fraction] = {}
    for (first, _middle, last), mass in base.items():
        ends[(first, last)] = ends.get((first, last), Fraction(0)) + mass
    checks.check(
        "nonadjacent ends are uniform and independent: every pair mass is 1/24^2",
        len(ends) == 24 * 24 and set(ends.values()) == {one_site * one_site},
    )
    correlation = sum(
        mass * factor(ez, first) * factor((0, 0, -1), middle)
        for (first, middle, _last), mass in base.items()
    )
    square_sum = sum(factor(ez, vector) ** 2 for vector in alphabet)
    predicted = kappa * square_sum * square_sum / (24 * 24)
    checks.check(
        "adjacent correlation equals kappa/36 = 1/72",
        square_sum == 4 and predicted == kappa / 36 == Fraction(1, 72) and correlation == Fraction(1, 72),
    )

    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
