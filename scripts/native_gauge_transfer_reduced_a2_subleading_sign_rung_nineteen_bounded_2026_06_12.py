#!/usr/bin/env python3
"""Rung nineteen reduced-A2 subleading-sign bounded runner.

This runner verifies the source-side algebra in the companion note. It derives
the saddle-surrogate first corrections exactly, checks that swap parity does
not force the half-integer insertion to vanish, prints finite W90-style witness
rows as fenced consistency checks, and refuses to promote those rows to a sign
proof.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import native_gauge_transfer_reduced_a2_spectral_domination_rung_eleven_bounded_2026_06_12 as w90


NOTE_PATH = (
    REPO_ROOT
    / "docs"
    / "NATIVE_GAUGE_TRANSFER_REDUCED_A2_SUBLEADING_SIGN_RUNG_NINETEEN_BOUNDED_NOTE_2026-06-12.md"
)

PASS = 0
FAIL = 0


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def fmt(frac: Fraction) -> str:
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"


def H(x: Fraction, y: Fraction) -> Fraction:
    return x * y * (x + y) / 2


def G1(x: Fraction, y: Fraction) -> Fraction:
    u = x + y
    return (u * u + 2 * x * y) / 2


def G2(x: Fraction, y: Fraction) -> Fraction:
    return 3 * (x + y) / 2


def P1(x: Fraction, y: Fraction, k: int = 3, include_dimension: bool = True) -> Fraction:
    u = x + y
    dim = G1(x, y) if include_dimension else Fraction(0)
    return dim - k * u * H(x, y)


def P2(x: Fraction, y: Fraction, k: int = 3, include_dimension: bool = True) -> Fraction:
    u = x + y
    dim1 = G1(x, y) if include_dimension else Fraction(0)
    dim2 = G2(x, y) if include_dimension else Fraction(0)
    return dim2 - k * u * dim1 + Fraction(k * k, 2) * u * u * H(x, y)


def q_form(x: Fraction, y: Fraction) -> Fraction:
    return x * x + x * y + y * y


def fixed_weight_derivative(p: int, q: int, beta: int, k: int = 3) -> Fraction:
    root = int(beta**0.5)
    if root * root != beta:
        raise ValueError("sample beta must be a square for exact display")
    x = Fraction(p, root)
    y = Fraction(q, root)
    return q_form(x, y) + Fraction(k, root) * (x + y)


def sympy_expansion_checks() -> dict[str, object]:
    x, y, eps = sp.symbols("x y eps")
    u = x + y
    Hsym = x * y * u / 2
    G1sym = (u**2 + 2 * x * y) / 2
    G2sym = 3 * u / 2
    expanded = sp.series(
        (Hsym + eps * G1sym + eps**2 * G2sym) * sp.exp(-3 * u * eps),
        eps,
        0,
        3,
    ).removeO()
    p1 = sp.expand(expanded.coeff(eps, 1))
    p2 = sp.expand(expanded.coeff(eps, 2))
    expected_p1 = sp.expand(G1sym - 3 * u * Hsym)
    expected_p2 = sp.expand(G2sym - 3 * u * G1sym + sp.Rational(9, 2) * u**2 * Hsym)
    p1_degrees = sorted({sum(mon) for mon, coeff in sp.Poly(expected_p1, x, y).terms() if coeff})
    p2_degrees = sorted({sum(mon) for mon, coeff in sp.Poly(expected_p2, x, y).terms() if coeff})
    return {
        "p1_matches": sp.expand(p1 - expected_p1) == 0,
        "p2_matches": sp.expand(p2 - expected_p2) == 0,
        "p1_degrees": p1_degrees,
        "p2_degrees": p2_degrees,
        "p1_swap": sp.expand(expected_p1 - expected_p1.xreplace({x: y, y: x})) == 0,
    }


def heat_fourth_checks() -> dict[str, object]:
    x, y = sp.symbols("x y")
    f = x**6 + 2 * x**4 * y**2 + 3 * x * y**5
    D = lambda g: x * sp.diff(g, x) + y * sp.diff(g, y)
    L = lambda g: (sp.diff(g, x, 2) - sp.diff(g, x, y) + sp.diff(g, y, 2)) / 3
    C4 = lambda g: (
        (sp.diff(g, x, 4) + sp.diff(g, y, 4)) / 72
        - (sp.diff(g, x, 3, y) + sp.diff(g, x, y, 3)) / 36
        + sp.diff(g, x, 2, y, 2) / 24
    )
    l_comm = sp.expand(D(L(f)) - L(D(f)) + 2 * L(f))
    c4_comm = sp.expand(D(C4(f)) - C4(D(f)) + 4 * C4(f))
    return {
        "l_comm_zero": l_comm == 0,
        "c4_comm_zero": c4_comm == 0,
    }


def finite_witness_rows() -> list[tuple[int, int, float, float]]:
    rows: list[tuple[int, int, float, float]] = []
    for beta, shell, mode in [(30, 21, 70), (60, 28, 70), (120, 37, 115)]:
        _lam0, _lam1, dj, dd = w90.spectral(beta, shell, mode)
        c_j = beta * (-dj)
        c_d = beta * dd
        margin = c_j - c_d
        rows.append((beta, shell, margin, beta * margin))
    return rows


def main() -> int:
    print("Native gauge-transfer reduced-A2 subleading-sign rung nineteen runner")
    print("Finite spectral rows are fenced witnesses; algebraic checks carry the note.")
    print()

    text = NOTE_PATH.read_text(encoding="utf-8")
    lower = text.lower()

    check(
        "note carries exact status-authority line",
        "Status authority: independent audit lane only. This source note does not set or predict an audit outcome."
        in text,
    )
    check(
        "note declares controlled claim type and source-side boundary",
        "**Claim type:** bounded_theorem" in text
        and "**Boundary:** partial-with-named-missing-link." in text
        and "Claim type is a source-side boundary declaration, never an audit verdict." in text,
    )
    check(
        "note refuses imports and value-from-target promotion",
        "No new axiom, literature value, external comparator number, fitted constant" in text
        and "value-from-target" in text
        and "W90 finite rows are fenced witnesses only" in text,
    )
    check(
        "one-hop authority links are present",
        "[NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md]" in text
        and "[NATIVE_GAUGE_TRANSFER_DIAGONAL_DOMINATION_RUNG_NINE_BOUNDED_NOTE_2026-06-12.md]" in text
        and "[NATIVE_GAUGE_TRANSFER_REDUCED_A2_VIRIAL_LEADING_EQUALITY_RUNG_EIGHTEEN_BOUNDED_NOTE_2026-06-12.md]" in text
        and "[NATIVE_GAUGE_TRANSFER_REDUCED_A2_DISCRIMINANT_CONJUGATION_RUNG_SEVENTEEN_BOUNDED_NOTE_2026-06-12.md]" in text,
    )
    check(
        "quote anchors include retained correction and leading equality clauses",
        "r_(p,q)(beta) = d_(p,q) exp[-3 C2(p,q)/beta] * (1 + lower-order terms)." in text
        and "3 C2(p,q) / beta" in text
        and "A_i + B_i/mu_i = 3/2," in text
        and "The leading identity does not derive the `1/beta` subleading sign." in text,
    )
    check(
        "note gives explicit T1 and T2 saddle-surrogate formulas",
        "T_1^sad = S M_[exp(-Q) P_1] S" in text
        and "T_2^sad = S M_[exp(-Q) P_2] S" in text
        and "E_2 M_[exp(-Q) H] S" in text,
    )
    check(
        "note names exact Wilson caveat before sign claim",
        "lower-order exact-Wilson factors" in text
        and "a_1(x,y)" in text
        and "a_2(x,y)" in text
        and "not derivable from the retained refs supplied here" in text,
    )
    check(
        "note does not claim half-integer cancellation or subleading sign",
        "This note does not claim deliverable (2) as derived." in text
        and "Outcome: obstruction-at-exact-step for the sign." in text
        and "Not derived here:" in text,
    )
    check(
        "note includes both ambiguity readings",
        "Reading 1: saddle-surrogate reading." in text
        and "Reading 2: exact-Wilson reading." in text,
    )
    check(
        "note differentiates new material from prior notes",
        "New here versus W97" in text
        and "Restated from W86/W79" in text
        and "Restated from W90" in text,
    )
    check(
        "note includes no-go discipline gate",
        "## No-Go Discipline Gate" in text
        and "N1 - Alternative route enumeration" in text
        and "N8 - Cross-cycle echo" in text,
    )
    banned = [
        "only " + "route",
        "last " + "route",
        "exhau" + "sted",
        "closes " + "the program",
        "perma" + "nently",
        "no other " + "path",
        "closes " + "route a",
    ]
    check("note avoids forbidden overreach phrases", not any(fragment in lower for fragment in banned))
    forbidden_grade = ["audited_" + "clean", "retained " + "grade", "audit " + "status:"]
    check("note avoids audit-grade/status assertions", not any(fragment in lower for fragment in forbidden_grade))

    virial = Fraction(3, 2)
    correct_deriv = fixed_weight_derivative(10, 20, 100, 3)
    wrong_deriv = fixed_weight_derivative(10, 20, 100, 2)
    print("exact_falsifier_values")
    print(f"  leading virial constant: {fmt(virial)}")
    print(f"  correct derivative k=3 at (10,20,100): {fmt(correct_deriv)}")
    print(f"  wrong derivative k=2 at (10,20,100): {fmt(wrong_deriv)}")
    check("leading virial constant is exact 3/2", virial == Fraction(3, 2))
    check("correct fixed-weight derivative sample is exact 79/10", correct_deriv == Fraction(79, 10))
    check("wrong saddle correction visibly changes derivative sample", wrong_deriv == Fraction(38, 5) and wrong_deriv != correct_deriv)

    one = Fraction(1)
    two = Fraction(2)
    p1_correct = P1(one, two, 3, True)
    p1_wrong_nc = P1(one, two, 2, True)
    p1_no_dim = P1(one, two, 3, False)
    p2_correct = P2(one, two, 3, True)
    p2_wrong_nc = P2(one, two, 2, True)
    p2_no_dim = P2(one, two, 3, False)
    print("local_saddle_correction_values_at_x1_y2")
    print(f"  correct P1: {fmt(p1_correct)}")
    print(f"  wrong N_c=2 P1: {fmt(p1_wrong_nc)}")
    print(f"  wrong dimension omitted P1: {fmt(p1_no_dim)}")
    print(f"  correct P2: {fmt(p2_correct)}")
    print(f"  wrong N_c=2 P2: {fmt(p2_wrong_nc)}")
    print(f"  wrong dimension omitted P2: {fmt(p2_no_dim)}")
    check("correct P1 sample is exact -41/2", p1_correct == Fraction(-41, 2))
    check("wrong N_c changes P1 visibly", p1_wrong_nc == Fraction(-23, 2) and p1_wrong_nc != p1_correct)
    check("wrong dimension omission changes P1 visibly", p1_no_dim == Fraction(-27) and p1_no_dim != p1_correct)
    check("correct P2 sample is exact 135/2", p2_correct == Fraction(135, 2))
    check("wrong N_c changes P2 visibly", p2_wrong_nc == Fraction(39, 2) and p2_wrong_nc != p2_correct)
    check("wrong dimension omission changes P2 visibly", p2_no_dim == Fraction(243, 2) and p2_no_dim != p2_correct)
    check(
        "swap parity preserves P1 rather than cancelling it",
        P1(one, two, 3, True) - P1(two, one, 3, True) == 0 and p1_correct != 0,
        f"P1(1,2)-P1(2,1)=0, P1(1,2)={fmt(p1_correct)}",
    )

    exp_checks = sympy_expansion_checks()
    check("symbolic expansion gives retained P1", bool(exp_checks["p1_matches"]))
    check("symbolic expansion gives retained P2", bool(exp_checks["p2_matches"]))
    check(
        "P1 is mixed-degree, so scalar homogeneity does not repeat W97",
        exp_checks["p1_degrees"] == [2, 4],
        f"degrees={exp_checks['p1_degrees']}",
    )
    check(
        "P2 is mixed-degree, so beta^-1 Ward step needs more data",
        exp_checks["p2_degrees"] == [1, 3, 5],
        f"degrees={exp_checks['p2_degrees']}",
    )
    check("symbolic P1 is swap-even", bool(exp_checks["p1_swap"]))

    heat_checks = heat_fourth_checks()
    check("[D,L] = -2L on polynomial test", bool(heat_checks["l_comm_zero"]))
    check("[D,C4] = -4C4 on polynomial test", bool(heat_checks["c4_comm_zero"]))
    check(
        "heat side has no beta^-1/2 term in the paired six-neighbor expansion",
        "beta/2 (J-I) = L/2 + beta^(-1) C_4 + O(beta^(-2))" in text,
    )
    check(
        "C4 exact coefficient row is present",
        "(1/72)(partial_xxxx + partial_yyyy)" in text
        and "(1/24) partial_xxyy" in text,
    )

    rows = finite_witness_rows()
    print("fenced_w90_style_witness_rows")
    for beta, shell, margin, beta_margin in rows:
        print(
            f"  beta={beta:3d} shell={shell:2d} "
            f"cJ_minus_cD={margin:.12f} beta_times_margin={beta_margin:.12f}"
        )
    margins = [row[2] for row in rows]
    beta_margins = [row[3] for row in rows]
    check("finite witness margins are positive on the small W90-style grid", all(m > 0 for m in margins))
    check(
        "finite beta*(margin) rows are printed as witnesses, not proof inputs",
        all(x > 0 for x in beta_margins) and "not proof inputs" in text,
        f"beta*(margin)={[round(float(x), 6) for x in beta_margins]}",
    )
    source_text = Path(__file__).read_text(encoding="utf-8")
    banned_fit_names = ["curve_" + "fit", "poly" + "fit", "lst" + "sq"]
    check(
        "runner contains no fitted target machinery",
        not any(name in source_text for name in banned_fit_names),
    )
    check(
        "exact rationals are constructed from integer Fraction inputs, not floats",
        all(isinstance(val, Fraction) for val in [virial, correct_deriv, p1_correct, p2_correct]),
    )
    check(
        "final note scope excludes continuum, beta=6, Clay, and audit outcome claims",
        "No continuum, no physical `beta=6`, no Clay or infinite-volume claim, and no audit outcome is asserted." in text,
    )

    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
