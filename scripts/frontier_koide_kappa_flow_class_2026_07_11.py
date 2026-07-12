#!/usr/bin/env python3
"""Exact conditional algebra for the positive-kappa bookkeeping flow class.

PASS/FAIL coverage ends before the report-only comparator section. The checks
derive the map, fixed set, conjugacy, special coefficient evaluations,
conditional fixed-point inversion, an independence negative control, and the
distinction from the aggregate equipartition count. Quark and charged-lepton
numbers are then printed only; they never enter ``check`` or the derivation
exit code.
"""

from __future__ import annotations

import sympy as sp


PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str, detail: str = "") -> None:
    """Record one failing-capable derivation check."""
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"; {detail}" if detail else ""
    print(f"CHECK {num:02d}: {tag} -- {desc}{suffix}")


def main() -> int:
    a2, kappa = sp.symbols("a2 kappa", positive=True)
    b2 = sp.symbols("b2", nonnegative=True)
    r_positive = sp.symbols("r_positive", positive=True)
    r_real = sp.symbols("r_real", real=True)
    reciprocal = sp.symbols("reciprocal", nonnegative=True)
    odds_symbol = sp.symbols("odds_symbol", positive=True)

    normalization = a2 + kappa * b2
    probability_s = a2 / normalization
    probability_d = kappa * b2 / normalization
    odds = sp.simplify(probability_d / probability_s)
    coordinate_r = b2 / a2
    check(
        1,
        sp.simplify(odds - kappa * coordinate_r) == 0,
        "T1 odds coordinate is x=kappa r",
        detail=f"x={odds}",
    )

    agreement_normalizer = probability_s**2 + probability_d**2
    next_s = probability_s**2 / agreement_normalizer
    next_d = probability_d**2 / agreement_normalizer
    next_odds = sp.simplify(next_d / next_s)
    check(
        2,
        sp.simplify(next_odds - odds**2) == 0,
        "T1 supplied independent agreement filter sends x to x^2",
        detail=f"x_next={next_odds}",
    )

    flow = kappa * r_positive**2
    flow_from_odds = sp.simplify((kappa * r_positive) ** 2 / kappa)
    check(
        3,
        sp.simplify(flow_from_odds - flow) == 0,
        "T1 induced coordinate flow is f_kappa(r)=kappa r^2",
        detail=f"f={flow}",
    )

    finite_fixed = set(sp.solve(sp.Eq(kappa * r_real**2, r_real), r_real))
    check(
        4,
        finite_fixed == {sp.Integer(0), 1 / kappa},
        "T1 complete finite real fixed set is {0,1/kappa}",
        detail=f"fixed={sorted(finite_fixed, key=str)}",
    )

    reciprocal_flow = sp.simplify(1 / flow.subs(r_positive, 1 / reciprocal))
    check(
        5,
        sp.simplify(reciprocal_flow - reciprocal**2 / kappa) == 0
        and reciprocal_flow.subs(reciprocal, 0) == 0,
        "T1 reciprocal chart fixes the projective r=infinity endpoint",
        detail=f"s_next={reciprocal_flow}",
    )

    positive_fixed = {value for value in finite_fixed if value != 0}
    check(
        6,
        positive_fixed == {1 / kappa},
        "T1 unique positive finite fixed point is 1/kappa",
        detail=f"positive_fixed={positive_fixed}",
    )

    derivative = sp.diff(flow, r_positive)
    multiplier = sp.simplify(derivative.subs(r_positive, 1 / kappa))
    check(
        7,
        multiplier == 2,
        "T1 positive-fixed-point multiplier is two for every positive kappa",
        detail=f"multiplier={multiplier}",
    )

    conjugated = sp.simplify(kappa * flow.subs(r_positive, odds_symbol / kappa))
    check(
        8,
        sp.simplify(conjugated - odds_symbol**2) == 0,
        "T1 h(r)=kappa r conjugates every member to the square map",
        detail=f"h.f.h^-1={conjugated}",
    )

    flow_kappa_two = sp.simplify(flow.subs(kappa, 2))
    fixed_kappa_two = sp.simplify((1 / kappa).subs(kappa, 2))
    check(
        9,
        flow_kappa_two == 2 * r_positive**2
        and fixed_kappa_two == sp.Rational(1, 2),
        "T2 coefficient evaluation kappa=2 gives f(r)=2r^2 and r*=1/2",
    )

    flow_kappa_one = sp.simplify(flow.subs(kappa, 1))
    fixed_kappa_one = sp.simplify((1 / kappa).subs(kappa, 1))
    check(
        10,
        flow_kappa_one == r_positive**2 and fixed_kappa_one == 1,
        "T2 coefficient evaluation kappa=1 gives f(r)=r^2 and r*=1",
    )

    check(
        11,
        fixed_kappa_one != fixed_kappa_two
        and derivative.subs({kappa: 1, r_positive: fixed_kappa_one}) == 2
        and derivative.subs({kappa: 2, r_positive: fixed_kappa_two}) == 2,
        "T2 the two coefficient examples have different fixed points but the same local multiplier",
    )

    inverted = sp.solve(sp.Eq(r_positive, 1 / kappa), kappa)
    check(
        12,
        inverted == [1 / r_positive],
        "T3 conditional fixed-point inversion gives kappa=1/r",
        detail=f"solutions={inverted}",
    )

    wrong_candidate = 2 / kappa
    wrong_residual = sp.simplify(
        flow.subs(r_positive, wrong_candidate) - wrong_candidate
    )
    check(
        13,
        wrong_residual == 2 / kappa and wrong_residual != 0,
        "fixed-point discriminator: r=2/kappa is not fixed",
        detail=f"residual={wrong_residual}",
    )

    # Perfectly correlated repeated outcomes have joint same-cell weights p_i,
    # not p_i^2. Conditioning on their certain agreement leaves the original
    # probabilities and hence the identity coordinate map.
    correlated_next_s = probability_s
    correlated_next_d = probability_d
    correlated_next_r = sp.simplify(
        (correlated_next_d / correlated_next_s) / kappa
    )
    check(
        14,
        sp.simplify(correlated_next_r - coordinate_r) == 0,
        "independence negative control: perfectly correlated registration gives r_next=r",
        detail=f"r_next={correlated_next_r}",
    )

    doublet_count = sp.symbols("doublet_count", positive=True)
    flow_fixed_value = 1 / kappa
    equipartition_value = doublet_count / 2
    equality_condition = sp.solve(
        sp.Eq(flow_fixed_value, equipartition_value), doublet_count
    )
    check(
        15,
        equality_condition == [2 / kappa]
        and sp.simplify(flow_fixed_value - equipartition_value) != 0,
        "parameter distinction: kappa and the equipartition count enter different equations",
        detail=f"numerical equality only if n_d={equality_condition[0]}",
    )

    print(
        "SUMMARY theorem: supplied independent agreement filtering gives "
        "f_kappa(r)=kappa r^2, fixed set {0,1/kappa,infinity}, and multiplier two."
    )
    print(
        "SUMMARY boundary: kappa=1 and kappa=2 are coefficient evaluations only; "
        "kappa is not identified with the aggregate equipartition count."
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    derivation_exit_code = 0 if FAIL == 0 else 1

    # ---------------------------------------------------------------------
    # REPORT-ONLY COMPARATORS. No check() calls or exit-code mutations below.
    # ---------------------------------------------------------------------
    print("\nREPORT ONLY -- comparator arithmetic; no threshold or scientific verdict")
    comparator_rows = (
        ("charged-lepton", sp.Rational(1, 2)),
        ("down-quark", sp.Rational(597, 1000)),
        ("up-quark", sp.Rational(773, 1000)),
    )
    display_unit_r = sp.Rational(1, 1000)
    comparison_grid = (
        sp.Integer(1),
        sp.Rational(5, 4),
        sp.Rational(4, 3),
        sp.Rational(3, 2),
        sp.Rational(5, 3),
        sp.Integer(2),
    )

    for label, comparator_r in comparator_rows:
        comparator_kappa = sp.simplify(1 / comparator_r)
        print(
            f"[REPORT] {label}: r={comparator_r}; "
            f"conditional inverted comparator kappa={sp.N(comparator_kappa, 10)}"
        )
        if label == "charged-lepton":
            continue
        display_unit_kappa = sp.simplify(display_unit_r / comparator_r**2)
        print(
            f"[REPORT] Delta_r={float(display_unit_r):.3f} is a decimal display unit, "
            f"not sigma; linearized Delta_kappa={float(display_unit_kappa):.6f}"
        )
        print(
            "[REPORT] grid     1/t      |kappa-t|  "
            "kappa-display-units  r-display-units"
        )
        for grid_value in comparison_grid:
            inverse_grid = sp.simplify(1 / grid_value)
            kappa_distance = sp.Abs(comparator_kappa - grid_value)
            kappa_display_units = sp.simplify(kappa_distance / display_unit_kappa)
            r_display_units = sp.simplify(
                sp.Abs(comparator_r - inverse_grid) / display_unit_r
            )
            print(
                f"[REPORT] {str(grid_value):>5}  {float(inverse_grid):>8.4f}  "
                f"{float(kappa_distance):>11.6f}  "
                f"{float(kappa_display_units):>19.3f}  "
                f"{float(r_display_units):>15.3f}"
            )

    print(
        "[REPORT] The grid is illustrative and non-exhaustive. No argmin, "
        "acceptance band, uncertainty, exclusion, or lane-scoping inference is applied."
    )
    return derivation_exit_code


if __name__ == "__main__":
    raise SystemExit(main())
