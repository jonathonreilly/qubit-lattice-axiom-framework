#!/usr/bin/env python3
"""Exact checks for the 2026-07-02 generation-moduli selector constraints."""

from fractions import Fraction

import sympy as sp


def fixed_points(expr, r):
    roots = sp.solve(sp.Eq(expr, r), r)
    nonnegative = []
    for root in roots:
        root = sp.simplify(root)
        if root.is_real is False:
            continue
        if sp.simplify(root) == 0 or sp.simplify(root > 0) is sp.S.true:
            nonnegative.append(root)
    return sorted(nonnegative, key=lambda x: float(sp.N(x)))


def same_set(got, expected):
    return len(got) == len(expected) and all(
        sp.simplify(a - b) == 0 for a, b in zip(got, expected)
    )


def main():
    checks = []

    # T1: ratio invariance under common real scale and b-phase.
    a2 = Fraction(49, 1)
    b_abs2 = Fraction(28, 1)
    lam = Fraction(-5, 3)
    r0 = b_abs2 / a2
    r_scaled = (lam * lam * b_abs2) / (lam * lam * a2)
    checks.append(("T1 common real scale invariance", r_scaled == r0))

    mu_abs2 = Fraction(1, 1)
    r_phase = (mu_abs2 * b_abs2) / a2
    checks.append(("T1 b phase invariance", r_phase == r0))

    y0_scale = Fraction(1, 1)
    y1_scale = Fraction(1, 1)
    y0_r = Fraction(0, 1)
    y1_r = Fraction(1, 1)
    checks.append(
        (
            "T1 scale-only witness has same scale and different r",
            y0_scale == y1_scale and y0_r != y1_r,
        )
    )

    # T2: exact fixed sets.
    r = sp.symbols("r", nonnegative=True)
    f = 2 * r**2
    g = r**2
    expected_f = [sp.Integer(0), sp.Rational(1, 2)]
    expected_g = [sp.Integer(0), sp.Integer(1)]
    checks.append(("T2 Fix(f)", same_set(fixed_points(f, r), expected_f)))
    checks.append(("T2 Fix(g)", same_set(fixed_points(g, r), expected_g)))

    for n in range(1, 5):
        f_iter = 2 ** (2**n - 1) * r ** (2**n)
        g_iter = r ** (2**n)
        checks.append((f"T2 Fix(f^{n}) pure iterate", same_set(fixed_points(f_iter, r), expected_f)))
        checks.append((f"T2 Fix(g^{n}) pure iterate", same_set(fixed_points(g_iter, r), expected_g)))

    pairwise = {
        "f after f": (2 * (2 * r**2) ** 2, expected_f),
        "f after g": (2 * (r**2) ** 2, [sp.Integer(0), 2 ** sp.Rational(-1, 3)]),
        "g after f": ((2 * r**2) ** 2, [sp.Integer(0), 2 ** sp.Rational(-2, 3)]),
        "g after g": ((r**2) ** 2, expected_g),
    }
    for name, (expr, expected) in pairwise.items():
        checks.append((f"T2 pairwise {name}", same_set(fixed_points(expr, r), expected)))

    mixed_new = {
        2 ** sp.Rational(-1, 3),
        2 ** sp.Rational(-2, 3),
    }
    base_points = {sp.Integer(0), sp.Rational(1, 2), sp.Integer(1)}
    checks.append(
        (
            "T2 mixed compositions add exact non-base points",
            all(all(sp.simplify(x - y) != 0 for y in base_points) for x in mixed_new),
        )
    )

    # T3: color-only factoring witness.
    c_s1 = "c0"
    c_s2 = "c0"
    selected_s1 = Fraction(1, 2)
    selected_s2 = Fraction(1, 1)
    color_equal_forces_equal = c_s1 == c_s2
    witness_violates_color_factoring = (
        color_equal_forces_equal and selected_s1 != selected_s2
    )
    checks.append(("T3 equal-color distinct-moduli witness", witness_violates_color_factoring))

    passed = sum(1 for _, ok in checks if ok)
    failed = len(checks) - passed
    print(f"PASS {passed}")
    print(f"FAIL {failed}")
    print(f"TOTAL {len(checks)}")
    raise SystemExit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
