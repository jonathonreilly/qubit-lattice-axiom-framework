#!/usr/bin/env python3
"""Exact CHSH squares of the six-axis product-class pair law.

The law is the normalized orbit weight (p, q, r) on one edge. Readouts are
functions of one record. No two-qubit density is built.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import permutations, product

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/PRODUCT_CLASS_SIX_AXIS_PAIR_CHSH_SQUARES_BOUNDED_THEOREM_NOTE_2026-10-09.md',)


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


class S2:
    """Value a + b√2 with rational a, b."""

    def __init__(self, a: Fraction | int, b: Fraction | int = 0) -> None:
        self.a = Fraction(a)
        self.b = Fraction(b)

    def __add__(self, other: S2) -> S2:
        return S2(self.a + other.a, self.b + other.b)

    def __sub__(self, other: S2) -> S2:
        return S2(self.a - other.a, self.b - other.b)

    def __mul__(self, other: S2) -> S2:
        return S2(
            self.a * other.a + 2 * self.b * other.b,
            self.a * other.b + self.b * other.a,
        )

    def __neg__(self) -> S2:
        return S2(-self.a, -self.b)


def det3(matrix: list[list[int]]) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def all_proper() -> list[list[list[int]]]:
    found = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = [[0, 0, 0] for _ in range(3)]
            for src, dst in enumerate(perm):
                matrix[dst][src] = signs[src]
            if det3(matrix) == 1:
                found.append(matrix)
    return found


def apply(rotation: list[list[int]], vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(rotation[i][k] * vector[k] for k in range(3)) for i in range(3)
    )


MENU: list[tuple[int, int, int]] = []
for axis in range(3):
    for sign in (1, -1):
        vector = [0, 0, 0]
        vector[axis] = sign
        MENU.append((vector[0], vector[1], vector[2]))


def dot(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]


def orbit_index(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    value = dot(left, right)
    if value == 1:
        return 0
    if value == -1:
        return 1
    if value == 0:
        return 2
    raise ValueError(value)


def weight_coeffs(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    coeffs = [0, 0, 0]
    coeffs[orbit_index(left, right)] = 1
    return (coeffs[0], coeffs[1], coeffs[2])


def eval_linear(coeffs: tuple[int, int, int], weights: tuple[int, int, int]) -> int:
    return coeffs[0] * weights[0] + coeffs[1] * weights[1] + coeffs[2] * weights[2]


def correlator_coeffs(i: int, j: int) -> tuple[int, int, int]:
    total = [0, 0, 0]
    for left in MENU:
        for right in MENU:
            product_value = left[i] * right[j]
            if product_value == 0:
                continue
            for slot, coeff in enumerate(weight_coeffs(left, right)):
                total[slot] += product_value * coeff
    return (total[0], total[1], total[2])


def sign_correlator_coeffs() -> tuple[int, int, int]:
    total = [0, 0, 0]
    for left in MENU:
        for right in MENU:
            product_value = sum(left) * sum(right)
            for slot, coeff in enumerate(weight_coeffs(left, right)):
                total[slot] += product_value * coeff
    return (total[0], total[1], total[2])


def mu(left, right, weights: tuple[int, int, int]) -> Fraction:
    denominator = 6 * (weights[0] + weights[1] + 4 * weights[2])
    return Fraction(eval_linear(weight_coeffs(left, right), weights), denominator)


def main() -> None:
    checks = Checks()
    group = all_proper()
    checks.check("proper cubic group has order 24", len(group) == 24)
    checks.check("menu has six signed axes", len(MENU) == 6 and len(set(MENU)) == 6)

    orbit_counts = [0, 0, 0]
    for left in MENU:
        for right in MENU:
            orbit_counts[orbit_index(left, right)] += 1
    checks.check(
        "pair orbits are 6 parallel, 6 antiparallel, 24 orthogonal",
        orbit_counts == [6, 6, 24],
    )

    z_coeffs = [0, 0, 0]
    for left in MENU:
        for right in MENU:
            for slot, coeff in enumerate(weight_coeffs(left, right)):
                z_coeffs[slot] += coeff
    checks.check("pair normalizer is 6p+6q+24r", tuple(z_coeffs) == (6, 6, 24))

    one_site = [0, 0, 0]
    fixed = MENU[0]
    for right in MENU:
        for slot, coeff in enumerate(weight_coeffs(fixed, right)):
            one_site[slot] += coeff
    checks.check("one-neighbor normalizer is p+q+4r", tuple(one_site) == (1, 1, 4))
    checks.check(
        "formation and static pair laws use the same normalizer",
        tuple(6 * c for c in one_site) == tuple(z_coeffs),
    )

    for weights in ((3, 1, 2), (5, 2, 4), (1, 0, 0), (0, 1, 0), (1, 1, 1), (0, 0, 1)):
        total = sum(mu(left, right, weights) for left in MENU for right in MENU)
        checks.check(f"probabilities sum to 1 at {weights}", total == 1)
        marginals = {
            sum(mu(left, right, weights) for right in MENU) for left in MENU
        }
        checks.check(f"both marginals are uniform at {weights}", marginals == {Fraction(1, 6)})

    diagonal = [correlator_coeffs(i, i) for i in range(3)]
    checks.check(
        "each diagonal coordinate sum is 2p-2q",
        diagonal == [(2, -2, 0), (2, -2, 0), (2, -2, 0)],
    )
    off = [
        correlator_coeffs(i, j) == (0, 0, 0)
        for i in range(3)
        for j in range(3)
        if i != j
    ]
    checks.check("off-diagonal coordinate sums vanish", all(off))

    # (2p-2q)/(6p+6q+24r) reduces by 2, then the remaining 3 in the
    # denominator is the coordinate factor. Cross-multiplication checks it.
    checks.check(
        "lambda fraction is the reduced coordinate sum",
        all(
            eval_linear((2, -2, 0), weights) * 3 * (weights[0] + weights[1] + 4 * weights[2])
            == eval_linear((1, -1, 0), weights) * eval_linear((6, 6, 24), weights)
            for weights in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (3, 1, 2), (5, 2, 4), (4, 4, 1))
        ),
    )

    sign_coeffs = sign_correlator_coeffs()
    checks.check("global-sign unnormalized sum is 6p-6q", sign_coeffs == (6, -6, 0))
    checks.check(
        "global-sign correlator is lambda_1 = (p-q)/(p+q+4r)",
        all(
            eval_linear(sign_coeffs, weights) * (weights[0] + weights[1] + 4 * weights[2])
            == eval_linear((1, -1, 0), weights) * eval_linear((6, 6, 24), weights)
            for weights in ((1, 0, 0), (0, 1, 0), (3, 1, 2), (5, 2, 4), (2, 2, 2))
        ),
    )

    def lambda_coord(weights: tuple[int, int, int]) -> Fraction:
        denominator = 3 * (weights[0] + weights[1] + 4 * weights[2])
        return Fraction(weights[0] - weights[1], denominator)

    def lambda_one(weights: tuple[int, int, int]) -> Fraction:
        denominator = weights[0] + weights[1] + 4 * weights[2]
        return Fraction(weights[0] - weights[1], denominator)

    checks.check(
        "three times the coordinate correlator is the odd eigenvalue",
        all(3 * lambda_coord(w) == lambda_one(w) for w in ((3, 1, 2), (5, 2, 4), (1, 1, 4))),
    )
    checks.check(
        "(3,1,2) coordinate correlator is 1/18, not the undivided eigenvalue 1/6",
        lambda_coord((3, 1, 2)) == Fraction(1, 18) and lambda_one((3, 1, 2)) == Fraction(1, 6),
    )
    checks.check(
        "(5,2,4) coordinate correlator is 1/23",
        lambda_coord((5, 2, 4)) == Fraction(1, 23),
    )

    # |p-q| <= p+q+4r, so |lambda| <= 1/3 and |lambda_1| <= 1.
    checks.check(
        "nonnegative weights obey |p-q| <= p+q+4r",
        all(
            abs(p - q) <= p + q + 4 * r
            for p in range(6)
            for q in range(6)
            for r in range(6)
            if p + q + r > 0
        ),
    )
    checks.check(
        "equality |lambda|=1/3 holds only for r=0 and pq=0",
        all(
            (lambda_coord((p, q, r)) ** 2 == Fraction(1, 9)) == (r == 0 and p * q == 0)
            for p in range(5)
            for q in range(5)
            for r in range(5)
            if p + q + r > 0
        ),
    )
    checks.check(
        "coordinate CHSH square 8 lambda^2 is at most 8/9 and below 4 and 8",
        Fraction(8, 9) < 4 and Fraction(8, 9) < 8 and all(
            8 * lambda_coord((p, q, r)) ** 2 <= Fraction(8, 9)
            and 8 * lambda_coord((p, q, r)) ** 2 < 4
            and 8 * lambda_coord((p, q, r)) ** 2 != 8
            for p in range(5)
            for q in range(5)
            for r in range(5)
            if p + q + r > 0
        ),
    )
    checks.check(
        "global-sign CHSH square 4 lambda_1^2 is at most 4 and is never 8",
        all(
            4 * lambda_one((p, q, r)) ** 2 <= 4
            and 4 * lambda_one((p, q, r)) ** 2 != 8
            for p in range(5)
            for q in range(5)
            for r in range(5)
            if p + q + r > 0
        ),
    )
    checks.check(
        "global-sign square equals 4 exactly on the axis-aligned boundary",
        all(
            (4 * lambda_one((p, q, r)) ** 2 == 4) == (r == 0 and p * q == 0)
            for p in range(5)
            for q in range(5)
            for r in range(5)
            if p + q + r > 0
        ),
    )

    half = S2(0, Fraction(1, 2))  # √2/2
    zero = S2(0)
    alice_x = (S2(1), zero, zero)
    alice_y = (zero, S2(1), zero)
    bob = (half, half, zero)
    bob_prime = (half, -half, zero)

    def sdot(left: tuple[S2, S2, S2], right: tuple[S2, S2, S2]) -> S2:
        return left[0] * right[0] + left[1] * right[1] + left[2] * right[2]

    combination = sdot(alice_x, bob) + sdot(alice_x, bob_prime) + sdot(alice_y, bob) - sdot(alice_y, bob_prime)
    square = combination * combination
    checks.check(
        "equatorial unit settings give direction square 8",
        square.a == 8 and square.b == 0,
    )
    for weights in ((3, 1, 2), (5, 2, 4), (1, 0, 0)):
        value = lambda_coord(weights)
        scaled = combination * S2(value)
        scaled_square = scaled * scaled
        checks.check(
            f"coordinate CHSH square equals 8 lambda^2 at {weights}",
            scaled_square.a == 8 * value * value and scaled_square.b == 0,
        )

    # Pathwise classical bound for outcomes in [-1, 1].
    def abs_sum(left: Fraction, right: Fraction) -> Fraction:
        return abs(left + right) + abs(left - right)

    samples = []
    for left in (0, 1, -1, Fraction(1, 2), Fraction(-2, 3), Fraction(4, 5)):
        for right in (0, 1, -1, Fraction(1, 3), Fraction(-3, 7)):
            samples.append((Fraction(left), Fraction(right)))
    checks.check(
        "|B+B'|+|B-B'| equals 2 max(|B|,|B'|)",
        all(abs_sum(left, right) == 2 * max(abs(left), abs(right)) for left, right in samples),
    )
    checks.check(
        "squared absolute-sum identity holds on the same sample",
        all(
            abs_sum(left, right) ** 2 == 4 * max(left * left, right * right)
            for left, right in samples
        ),
    )
    checks.check(
        "sample outcomes in [-1,1] have absolute-sum at most 2",
        all(abs_sum(left, right) <= 2 for left, right in samples if abs(left) <= 1 and abs(right) <= 1),
    )

    response_values = []
    for bits in product((-1, 1), repeat=4):
        a0, a1, b0, b1 = bits
        response_values.append(abs(a0 * b0 + a0 * b1 + a1 * b0 - a1 * b1))
    checks.check(
        "control: all 16 deterministic sign pairs have |CHSH| at most 2, and 2 occurs",
        max(response_values) == 2 and all(value <= 2 for value in response_values),
    )

    signed_axes = MENU
    largest = 0
    attained = False
    for u, u2, v, v2 in product(signed_axes, repeat=4):
        entries = (
            dot(u, v),
            dot(u, v2),
            dot(u2, v),
            dot(u2, v2),
        )
        forms = (
            abs(entries[0] + entries[1] + entries[2] - entries[3]),
            abs(entries[0] + entries[1] - entries[2] + entries[3]),
            abs(entries[0] - entries[1] + entries[2] + entries[3]),
            abs(-entries[0] + entries[1] + entries[2] + entries[3]),
        )
        peak = max(forms)
        if peak > largest:
            largest = peak
        if peak == 2:
            attained = True
    checks.check("signed-axis direction combinations are at most 2", largest <= 2)
    checks.check("signed-axis direction combination 2 is attained", attained and largest == 2)

    for weights, expected in (
        ((1, 0, 0), 2),
        ((0, 1, 0), 2),
        ((3, 1, 2), Fraction(1, 3)),
    ):
        correlator = lambda_one(weights)
        checks.check(
            f"setting-blind global sign has CHSH magnitude 2|lambda_1| at {weights}",
            abs(2 * correlator) == expected,
        )

    # One-axis conditional sign law.
    def conditional_alpha(weights: tuple[int, int, int]) -> Fraction | None:
        if weights[0] + weights[1] == 0:
            return None
        return Fraction(weights[0] - weights[1], weights[0] + weights[1])

    checks.check("conditional alpha is undefined when p=q=0", conditional_alpha((0, 0, 1)) is None)
    checks.check(
        "one-axis event mass is (p+q)/(3(p+q+4r))",
        all(
            Fraction(2 * p + 2 * q, 6 * p + 6 * q + 24 * r)
            == Fraction(p + q, 3 * (p + q + 4 * r))
            for p, q, r in ((3, 1, 2), (1, 0, 0), (0, 1, 2))
        ),
    )
    checks.check(
        "conditional square 4 alpha^2 equals 4 exactly when pq=0 and p+q>0",
        all(
            (
                4 * conditional_alpha((p, q, r)) ** 2 == 4
                if conditional_alpha((p, q, r)) is not None
                else False
            )
            == (p * q == 0 and p + q > 0)
            for p in range(4)
            for q in range(4)
            for r in range(4)
            if p + q + r > 0
        ),
    )
    checks.check(
        "conditional square is never 8",
        all(
            conditional_alpha((p, q, r)) is None
            or 4 * conditional_alpha((p, q, r)) ** 2 != 8
            for p in range(4)
            for q in range(4)
            for r in range(4)
            if p + q + r > 0
        ),
    )
    for weights in ((3, 1, 2), (1, 0, 0), (2, 5, 1)):
        alpha = conditional_alpha(weights)
        assert alpha is not None
        # Four sign choices on one shared axis. The minus-one form has magnitude 2|alpha|.
        magnitude = abs(alpha + alpha + alpha - alpha)
        checks.check(
            f"one-axis conditional CHSH magnitude is 2|alpha| at {weights}",
            magnitude == 2 * abs(alpha),
        )

    preserved = True
    for rotation in group:
        for left in MENU:
            for right in MENU:
                image_left = apply(rotation, left)
                image_right = apply(rotation, right)
                if orbit_index(image_left, image_right) != orbit_index(left, right):
                    preserved = False
    checks.check("simultaneous proper-cubic action preserves orbit weights", preserved)

    # Orthogonal conditional correlator cancels. Same-axis conditional is alpha.
    same = 0
    orthogonal_mass = [0, 0, 0]
    orthogonal_signed = [0, 0, 0]
    same_signed = [0, 0, 0]
    z = (0, 0, 1)
    x = (1, 0, 0)
    for left_sign in (1, -1):
        for right_sign in (1, -1):
            left = (0, 0, left_sign)
            right = (0, 0, right_sign)
            product_value = left_sign * right_sign
            for slot, coeff in enumerate(weight_coeffs(left, right)):
                same_signed[slot] += product_value * coeff
            same += 1
    for left_sign in (1, -1):
        for right_sign in (1, -1):
            left = (0, 0, left_sign)
            right = (right_sign, 0, 0)
            product_value = left_sign * right_sign
            for slot, coeff in enumerate(weight_coeffs(left, right)):
                orthogonal_mass[slot] += coeff
                orthogonal_signed[slot] += product_value * coeff
    checks.check("same-axis sign sum is 2p-2q", tuple(same_signed) == (2, -2, 0) and same == 4)
    checks.check(
        "orthogonal axis-conditional sign sum is 0 while its mass is 4r",
        tuple(orthogonal_signed) == (0, 0, 0) and tuple(orthogonal_mass) == (0, 0, 4),
    )
    checks.check("z and x are orthogonal menu axes", dot(z, x) == 0)

    print("per_element: All 36 ordered pairs of the six signed axes are enumerated, and no other alphabet is tested.")
    print("per_site: The law is one two-site edge. A site with more than one neighbor is not tested.")
    print("per_mode: Coordinate readout, global sign, signed-axis settings, and the one-axis conditional sign law are tested. The sum rule is not.")
    print("per_block: One nearest-neighbor bond is tested. Plaquettes, cubes, and larger windows are not tested.")
    print("lattice_wide: checked and not executed — no infinite-volume statement is claimed or tested.")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    if checks.failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
