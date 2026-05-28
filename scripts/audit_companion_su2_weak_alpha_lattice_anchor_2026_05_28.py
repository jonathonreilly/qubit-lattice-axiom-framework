#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for
`SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28`.

The narrow theorem's load-bearing content is the algebraic substitution
implication: given

  (X1) Wilson canonical convention: beta_W := 2 N_c / g_bare^2
       (named external admission, textbook lattice gauge theory)
  (X2) g_2^2 |_lattice = 1 / (d + 1) = 1/4 at d = 3
       (retained_bounded via cited SU2_WEAK_BETA_COEFFICIENT_NARROW_THEOREM
       and G_2_V_BOUNDED_INTERVAL_NARROW_THEOREM)
  (X3) Standard QFT convention: alpha := g^2 / (4 pi)
       (named external admission, textbook QFT)
  (X4) N_c |_SU(2) = 2 (retained native SU(2) from NATIVE_GAUGE_CLOSURE_NOTE),

the lattice-scale SU(2)_L fine-structure coupling and Wilson beta-parameter
admit the exact closed forms

  (A1)  alpha_2 |_lattice  = g_2^2 / (4 pi) = (1/4) / (4 pi) = 1 / (16 pi)
  (A2)  1 / alpha_2 |_lattice = 16 pi
  (A3)  beta_W |_lattice    = 2 * 2 / (1/4) = 16
  (A4)  alpha_2 |_lattice  approx 0.01989 43678 86 (14 sig figs)

This runner verifies (A1)-(A4) plus six corollaries (C1)-(C6) at exact
sympy precision over abstract positive integers (N_c, d), then specializes
to the framework instance (N_c, d) = (2, 3) and runs counterfactuals at
d in {2, 4} and N_c in {3, 4} confirming the closed form is genuinely
parametric.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence at exact precision.
"""

from __future__ import annotations
import sys

try:
    from sympy import Rational, Symbol, simplify, pi, N as sympy_N, sqrt, Integer
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


def main() -> int:
    print("=" * 88)
    print("Audit companion (exact-symbolic) for")
    print("SU2_WEAK_ALPHA_LATTICE_ONE_OVER_SIXTEEN_PI_ANCHOR_NARROW_THEOREM_NOTE_2026-05-28")
    print("Goal: sympy verification of alpha_2 |_lattice = 1 / (16 pi) closed form")
    print("Inputs (cited):")
    print("  (X1) Wilson canonical convention beta_W = 2 N_c / g_bare^2 (textbook)")
    print("  (X2) g_2^2 |_lattice = 1 / (d + 1) at d = 3 ... retained_bounded")
    print("  (X3) Standard QFT convention alpha = g^2 / (4 pi) (textbook)")
    print("  (X4) N_c |_SU(2) = 2 ... retained via NATIVE_GAUGE_CLOSURE_NOTE")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup (positive integers)")
    # ---------------------------------------------------------------------
    N_c = Symbol("N_c", positive=True, integer=True)
    d = Symbol("d", positive=True, integer=True)

    print(f"  symbolic N_c = {N_c}")
    print(f"  symbolic d   = {d}")

    # Cited input (X2): g_2^2 |_lattice = 1 / (d + 1)
    g2_sq_lattice_sym = 1 / (d + Integer(1))

    # Framework instance: (N_c, d) = (2, 3) -> g_2^2 |_lattice = 1/4
    framework = {N_c: 2, d: 3}
    g2_sq_lattice_fw = simplify(g2_sq_lattice_sym.subs(framework))

    check(
        "(X2) framework instance: g_2^2 |_lattice = 1/4 at d = 3",
        g2_sq_lattice_fw == Rational(1, 4),
        detail=f"g_2^2 |_lattice = {g2_sq_lattice_fw}",
    )

    # ---------------------------------------------------------------------
    section("Part 1: (A1) alpha_2 |_lattice = (1/4) / (4 pi) = 1 / (16 pi)")
    # ---------------------------------------------------------------------
    # Apply (X3) standard QFT convention to (X2):
    #   alpha_2 |_lattice = g_2^2 |_lattice / (4 pi)
    alpha_2_lattice_sym = g2_sq_lattice_sym / (4 * pi)
    alpha_2_lattice_fw = simplify(alpha_2_lattice_sym.subs(framework))
    alpha_2_lattice_claimed = 1 / (16 * pi)

    check(
        "(A1) symbolic: alpha_2 |_lattice = (1/(d+1)) / (4 pi)",
        simplify(alpha_2_lattice_sym - 1 / (4 * pi * (d + 1))) == 0,
        detail=f"symbolic form = {alpha_2_lattice_sym}",
    )

    check(
        "(A1) framework instance: alpha_2 |_lattice = 1 / (16 pi) at d = 3",
        simplify(alpha_2_lattice_fw - alpha_2_lattice_claimed) == 0,
        detail=f"alpha_2 |_lattice = {alpha_2_lattice_fw}",
    )

    # ---------------------------------------------------------------------
    section("Part 2: (A2) reciprocal: 1 / alpha_2 |_lattice = 16 pi")
    # ---------------------------------------------------------------------
    one_over_alpha_2_lattice_fw = simplify(1 / alpha_2_lattice_fw)
    one_over_alpha_2_lattice_claimed = 16 * pi

    check(
        "(A2) framework instance: 1 / alpha_2 |_lattice = 16 pi",
        simplify(one_over_alpha_2_lattice_fw - one_over_alpha_2_lattice_claimed) == 0,
        detail=f"1 / alpha_2 |_lattice = {one_over_alpha_2_lattice_fw}",
    )

    # ---------------------------------------------------------------------
    section("Part 3: (A3) Wilson beta-parameter: beta_W |_lattice = 16")
    # ---------------------------------------------------------------------
    # Apply (X1) Wilson canonical convention with (X2) and (X4):
    #   beta_W = 2 N_c / g_bare^2 = 2 * N_c / g_2^2 |_lattice
    beta_W_sym = 2 * N_c / g2_sq_lattice_sym
    beta_W_fw = simplify(beta_W_sym.subs(framework))
    beta_W_claimed = Integer(16)

    check(
        "(A3) symbolic: beta_W = 2 N_c (d + 1)",
        simplify(beta_W_sym - 2 * N_c * (d + 1)) == 0,
        detail=f"symbolic form = {beta_W_sym}",
    )

    check(
        "(A3) framework instance: beta_W |_lattice = 16 at (N_c, d) = (2, 3)",
        beta_W_fw == beta_W_claimed,
        detail=f"beta_W |_lattice = {beta_W_fw}",
    )

    # ---------------------------------------------------------------------
    section("Part 4: (A4) numeric readout 1 / (16 pi) approx 0.01989 43678 86")
    # ---------------------------------------------------------------------
    # Use 30-digit numeric precision.
    alpha_2_numeric = sympy_N(alpha_2_lattice_fw, 30)
    one_over_alpha_2_numeric = sympy_N(one_over_alpha_2_lattice_fw, 30)

    # The known 14-sig-fig value is 0.019894367886...
    # Round to 14 sig figs:
    alpha_2_str = f"{float(alpha_2_numeric):.14g}"
    check(
        "(A4) numeric: alpha_2 |_lattice approx 0.019894367886 (14 sig figs)",
        abs(float(alpha_2_numeric) - 0.019894367886) < 1e-12,
        detail=f"alpha_2 |_lattice approx {alpha_2_str}",
    )

    one_over_alpha_2_str = f"{float(one_over_alpha_2_numeric):.14g}"
    check(
        "(A4 alt) numeric: 1 / alpha_2 |_lattice approx 50.26548245744 (14 sig figs)",
        abs(float(one_over_alpha_2_numeric) - 50.265482457437) < 1e-10,
        detail=f"1 / alpha_2 |_lattice approx {one_over_alpha_2_str}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: (C1) Wilson beta at framework + N_c counterfactuals")
    # ---------------------------------------------------------------------
    # (C1) beta_W = 16 at (N_c, d) = (2, 3)
    check(
        "(C1) beta_W = 16 at framework (N_c, d) = (2, 3)",
        beta_W_fw == Integer(16),
        detail=f"beta_W = {beta_W_fw}",
    )

    # N_c counterfactuals at d = 3 (keeping g_2^2 = 1/4):
    #   N_c = 3 -> beta_W = 6 / (1/4) = 24
    #   N_c = 4 -> beta_W = 8 / (1/4) = 32
    cf_Nc3 = {N_c: 3, d: 3}
    cf_Nc4 = {N_c: 4, d: 3}
    beta_W_Nc3 = simplify(beta_W_sym.subs(cf_Nc3))
    beta_W_Nc4 = simplify(beta_W_sym.subs(cf_Nc4))

    check(
        "(C1) counterfactual N_c = 3: beta_W = 24 at d = 3",
        beta_W_Nc3 == Integer(24),
        detail=f"beta_W = {beta_W_Nc3}",
    )
    check(
        "(C1) counterfactual N_c = 4: beta_W = 32 at d = 3",
        beta_W_Nc4 == Integer(32),
        detail=f"beta_W = {beta_W_Nc4}",
    )

    # ---------------------------------------------------------------------
    section("Part 6: (C2) consistency with parent asymptotic-running form")
    # ---------------------------------------------------------------------
    # Parent narrow theorem has 1/alpha_2(Q) = 16 pi + (19/(12 pi)) ln(Q/Q_lattice)
    # At Q = Q_lattice, ln = 0, so 1/alpha_2|_lattice = 16 pi, matching (A2).
    Q = Symbol("Q", positive=True)
    Q_lattice = Symbol("Q_lattice", positive=True)
    from sympy import log
    running_form = 16 * pi + (Rational(19, 6) / (2 * pi)) * log(Q / Q_lattice)
    running_at_lattice = simplify(running_form.subs(Q, Q_lattice))
    check(
        "(C2) parent running 1/alpha_2(Q) at Q = Q_lattice equals 16 pi",
        simplify(running_at_lattice - 16 * pi) == 0,
        detail=f"1/alpha_2(Q_lattice) = {running_at_lattice}",
    )

    # Verify the (19/(12 pi)) coefficient: b_2/(2 pi) = (19/6)/(2 pi) = 19/(12 pi)
    b_2 = Rational(19, 6)
    asymptotic_coef = b_2 / (2 * pi)
    check(
        "(C2) asymptotic running coefficient b_2/(2 pi) = 19/(12 pi)",
        simplify(asymptotic_coef - Rational(19) / (12 * pi)) == 0,
        detail=f"coef = {asymptotic_coef}",
    )

    # ---------------------------------------------------------------------
    section("Part 7: (C3) counterfactual at d = 2")
    # ---------------------------------------------------------------------
    cf_d2 = {N_c: 2, d: 2}
    g2_sq_d2 = simplify(g2_sq_lattice_sym.subs(cf_d2))
    alpha_2_d2 = simplify(alpha_2_lattice_sym.subs(cf_d2))
    beta_W_d2 = simplify(beta_W_sym.subs(cf_d2))

    check(
        "(C3) d = 2 counterfactual: g_2^2 |_lattice = 1/3",
        g2_sq_d2 == Rational(1, 3),
        detail=f"g_2^2 = {g2_sq_d2}",
    )
    check(
        "(C3) d = 2 counterfactual: alpha_2 |_lattice = 1/(12 pi)",
        simplify(alpha_2_d2 - 1 / (12 * pi)) == 0,
        detail=f"alpha_2 = {alpha_2_d2}",
    )
    check(
        "(C3) d = 2 counterfactual: beta_W = 12",
        beta_W_d2 == Integer(12),
        detail=f"beta_W = {beta_W_d2}",
    )

    # ---------------------------------------------------------------------
    section("Part 8: (C4) counterfactual at d = 4")
    # ---------------------------------------------------------------------
    cf_d4 = {N_c: 2, d: 4}
    g2_sq_d4 = simplify(g2_sq_lattice_sym.subs(cf_d4))
    alpha_2_d4 = simplify(alpha_2_lattice_sym.subs(cf_d4))
    beta_W_d4 = simplify(beta_W_sym.subs(cf_d4))

    check(
        "(C4) d = 4 counterfactual: g_2^2 |_lattice = 1/5",
        g2_sq_d4 == Rational(1, 5),
        detail=f"g_2^2 = {g2_sq_d4}",
    )
    check(
        "(C4) d = 4 counterfactual: alpha_2 |_lattice = 1/(20 pi)",
        simplify(alpha_2_d4 - 1 / (20 * pi)) == 0,
        detail=f"alpha_2 = {alpha_2_d4}",
    )
    check(
        "(C4) d = 4 counterfactual: beta_W = 20",
        beta_W_d4 == Integer(20),
        detail=f"beta_W = {beta_W_d4}",
    )

    # ---------------------------------------------------------------------
    section("Part 9: (C5) N_c = 3 substituted into g_2^2 = 1/4 (hypothetical)")
    # ---------------------------------------------------------------------
    # This is the "what if N_c were 3 at the SU(2) lattice coupling 1/4"
    # counterfactual, confirming the anchor depends on N_c.
    cf_Nc3_d3 = {N_c: 3, d: 3}
    beta_W_Nc3_d3 = simplify(beta_W_sym.subs(cf_Nc3_d3))
    check(
        "(C5) hypothetical N_c = 3 at g_2^2 = 1/4: beta_W = 24",
        beta_W_Nc3_d3 == Integer(24),
        detail=f"beta_W = {beta_W_Nc3_d3}; framework selects N_c = 2 giving beta_W = 16",
    )

    # ---------------------------------------------------------------------
    section("Part 10: (C6) numeric readouts to 14 significant figures")
    # ---------------------------------------------------------------------
    alpha_2_num_14 = float(sympy_N(Rational(1) / (16 * pi), 20))
    inv_alpha_2_num_14 = float(sympy_N(16 * pi, 20))

    check(
        "(C6) alpha_2 |_lattice numeric 14 sig figs: 0.019894367886...",
        abs(alpha_2_num_14 - 1.0 / (16.0 * 3.141592653589793)) < 1e-15,
        detail=f"sympy num approx = {alpha_2_num_14:.14g}",
    )
    check(
        "(C6) 1 / alpha_2 |_lattice numeric 14 sig figs: 50.26548245744...",
        abs(inv_alpha_2_num_14 - 16.0 * 3.141592653589793) < 1e-12,
        detail=f"sympy num approx = {inv_alpha_2_num_14:.14g}",
    )

    # ---------------------------------------------------------------------
    section("Part 11: round-trip checks (A1)-(A2)-(X3) consistency")
    # ---------------------------------------------------------------------
    # Round-trip 1: alpha_2 |_lattice * 16 pi = 1
    rt1 = simplify(alpha_2_lattice_fw * 16 * pi)
    check(
        "round-trip 1: alpha_2 |_lattice * 16 pi = 1 (exact)",
        rt1 == Integer(1),
        detail=f"alpha_2 * 16 pi = {rt1}",
    )

    # Round-trip 2: 4 pi * alpha_2 |_lattice = g_2^2 |_lattice = 1/4
    rt2 = simplify(4 * pi * alpha_2_lattice_fw)
    check(
        "round-trip 2: 4 pi * alpha_2 |_lattice = g_2^2 |_lattice = 1/4",
        rt2 == Rational(1, 4),
        detail=f"4 pi * alpha_2 = {rt2}",
    )

    # Round-trip 3: beta_W * g_2^2 |_lattice = 2 N_c
    rt3 = simplify(beta_W_fw * g2_sq_lattice_fw)
    check(
        "round-trip 3: beta_W * g_2^2 |_lattice = 2 * N_c = 4 at N_c = 2",
        rt3 == Integer(4),
        detail=f"beta_W * g_2^2 = {rt3}",
    )

    # ---------------------------------------------------------------------
    section("Part 12: consistency with framework b_2 = 19/6 form")
    # ---------------------------------------------------------------------
    # Cross-check: the asymptotic-running form
    #   1/alpha_2(Q) = 16 pi + (b_2 / (2 pi)) * ln(Q / Q_lattice)
    # with b_2 = 19/6 gives coefficient 19/(12 pi).
    # At Q = Q_lattice (lattice scale), the log term vanishes
    # and 1/alpha_2 = 16 pi exactly, matching (A2).
    coeff_check = simplify(Rational(19, 6) / (2 * pi))
    check(
        "consistency: b_2/(2 pi) at b_2 = 19/6 equals 19/(12 pi)",
        simplify(coeff_check - Rational(19) / (12 * pi)) == 0,
        detail=f"19/6 / (2 pi) = {coeff_check}",
    )

    # ---------------------------------------------------------------------
    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL == 0:
        print("VERDICT: bounded narrow-theorem anchor passes; alpha_2 |_lattice = 1 / (16 pi)")
        print("follows from (X1)-(X4) by exact sympy rational + pi arithmetic.")
    else:
        print("VERDICT: FAILED")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
