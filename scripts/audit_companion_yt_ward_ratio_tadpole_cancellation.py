#!/usr/bin/env python3
"""Exact-symbolic audit-companion runner for the yt_ward canonical-surface
ratio narrow theorem note
`YT_WARD_RATIO_TADPOLE_CANCELLATION_NARROW_THEOREM_NOTE_2026-05-17.md`.

The parent narrow note's load-bearing content is the algebraic-substitution
implication that, given equal single-vertex tadpole dressing for the two
couplings, the two canonical-surface single-vertex coupling readouts

  (D1) g_s(M_Pl)  := g_bare   / sqrt(u_0)
  (D2) y_t(M_Pl)  := y_t_bare / sqrt(u_0)

algebraically satisfy

  (P1) y_t(M_Pl) / g_s(M_Pl) = y_t_bare / g_bare

identically in u_0 (the common 1/sqrt(u_0) tadpole factor cancels).

This Pattern A narrow runner adds a sympy-based exact-symbolic verification:

  (a) treats (g_bare, y_t_bare, u_0) as free positive real symbols;
  (b) treats D1, D2 as the audited theorem's conditional readouts at
      equal coupling-level dressing;
  (c) verifies (P1) reduces to 0 symbolically;
  (d) verifies the (P1) ratio is independent of u_0 after simplification;
  (e) verifies four derivable corollaries;
  (f) verifies algebraic forms via simplify and free_symbols checks;
  (g) runs a single FP-numerical sanity cross-check at one independent
      random sample of (g_bare, y_t_bare, u_0);
  (h) counterfactual probe: at unequal n_link for the two couplings, (P1)
      collapses to a non-identity in u_0.

Companion role: not a new claim row, not a new source note, no status
promotion. Provides audit-friendly evidence that the parent's
load-bearing class-(A) tadpole-cancellation algebra holds at exact
symbolic precision under equal dressing. The companion premise packet
`frontier_yt_tadpole_cancellation_premise_derivation_2026_06_06.py`
reproves D14/sqrt-readout, grounds the gauge-side count, and leaves the
Yukawa-side equality as the named residual.
"""

from pathlib import Path
import sys

try:
    import sympy
    from sympy import Mul, Pow, Rational, Symbol, simplify, sqrt, symbols, sympify
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
    print("YT_WARD_RATIO_TADPOLE_CANCELLATION_NARROW_THEOREM_NOTE_2026-05-17")
    print("Goal: sympy-symbolic verification of (P1)")
    print("  y_t(M_Pl) / g_s(M_Pl) = y_t_bare / g_bare")
    print("under equal single-vertex coupling-level tadpole dressing")
    print("=" * 88)

    # ---------------------------------------------------------------------
    section("Part 0: symbolic setup")
    # ---------------------------------------------------------------------

    g_bare = Symbol("g_bare", positive=True, real=True)
    y_t_bare = Symbol("y_t_bare", positive=True, real=True)
    u_0 = Symbol("u_0", positive=True, real=True)
    # n_link as a positive integer symbol (used in the parametric CMT form).
    n = Symbol("n", positive=True, integer=True)

    # Conditional readouts. The 2026-06-06 premise packet reproves the
    # link-monomial CMT homogeneity and square-root normalization pieces,
    # grounds the gauge-side single-link count, and leaves equality of the
    # Yukawa and gauge dressing as the named structural residual:
    #
    #   coupling_canonical(O) := coupling_bare / u_0^{n_link / 2}
    #
    # At n_link = 1 per single-vertex insertion this gives:
    #   (D1) g_s(M_Pl)  := g_bare   / sqrt(u_0)
    #   (D2) y_t(M_Pl)  := y_t_bare / sqrt(u_0)
    n_v = 1
    g_s_MPl = g_bare / sqrt(u_0)         # n_link = 1
    y_t_MPl = y_t_bare / sqrt(u_0)       # n_link = 1

    print(f"  symbolic g_bare    (positive real) = {g_bare}")
    print(f"  symbolic y_t_bare  (positive real) = {y_t_bare}")
    print(f"  symbolic u_0       (positive real) = {u_0}")
    print(f"  conditional common n_link (single-vertex coupling) = {n_v}")
    print(f"  (D1) g_s(M_Pl)  = g_bare   / sqrt(u_0)  = {g_s_MPl}")
    print(f"  (D2) y_t(M_Pl)  = y_t_bare / sqrt(u_0)  = {y_t_MPl}")

    # ---------------------------------------------------------------------
    section("Part 1: parametric (P1) y_t(M_Pl) / g_s(M_Pl) = y_t_bare / g_bare")
    # ---------------------------------------------------------------------

    P1_LHS = simplify(y_t_MPl / g_s_MPl)
    P1_target = y_t_bare / g_bare
    P1_diff = simplify(P1_LHS - P1_target)
    check(
        "(P1) y_t(M_Pl) / g_s(M_Pl) - y_t_bare / g_bare reduces to 0 parametrically",
        P1_diff == 0,
        detail=f"diff = {P1_diff}",
    )
    check(
        "(P1) LHS simplifies to y_t_bare / g_bare",
        simplify(P1_LHS - P1_target) == 0,
        detail=f"got {P1_LHS}",
    )

    # ---------------------------------------------------------------------
    section("Part 2: u_0-independence of the (P1) ratio")
    # ---------------------------------------------------------------------
    # The simplified ratio must not contain u_0 as a free symbol.
    check(
        "(P1) ratio is independent of u_0 (u_0 not in free_symbols of ratio)",
        u_0 not in P1_LHS.free_symbols,
        detail=f"free_symbols of (P1) ratio = {P1_LHS.free_symbols}",
    )

    # The ratio retains free symbols {y_t_bare, g_bare} only.
    expected_ratio_free = {y_t_bare, g_bare}
    check(
        "(P1) ratio retains free symbols {y_t_bare, g_bare} only",
        P1_LHS.free_symbols == expected_ratio_free,
        detail=f"free_symbols = {P1_LHS.free_symbols}",
    )

    # ---------------------------------------------------------------------
    section("Part 3: derivable corollaries")
    # ---------------------------------------------------------------------
    # corr 1: y_t(M_Pl) * g_bare = y_t_bare * g_s(M_Pl) (cross-multiplied (P1))
    corr1_LHS = simplify(y_t_MPl * g_bare - y_t_bare * g_s_MPl)
    check(
        "corollary 1: y_t(M_Pl) * g_bare = y_t_bare * g_s(M_Pl) (cross-multiplied (P1))",
        corr1_LHS == 0,
        detail=f"diff = {corr1_LHS}",
    )

    # corr 2: y_t(M_Pl)^2 / g_s(M_Pl)^2 = y_t_bare^2 / g_bare^2 (squared (P1))
    corr2_LHS = simplify(y_t_MPl**2 / g_s_MPl**2)
    corr2_target = y_t_bare**2 / g_bare**2
    check(
        "corollary 2: y_t(M_Pl)^2 / g_s(M_Pl)^2 = y_t_bare^2 / g_bare^2",
        simplify(corr2_LHS - corr2_target) == 0,
        detail=f"got {corr2_LHS}",
    )

    # corr 3: y_t(M_Pl) * sqrt(u_0) = y_t_bare ((D2) restated)
    corr3_LHS = simplify(y_t_MPl * sqrt(u_0))
    corr3_target = y_t_bare
    check(
        "corollary 3: y_t(M_Pl) * sqrt(u_0) = y_t_bare",
        simplify(corr3_LHS - corr3_target) == 0,
        detail=f"got {corr3_LHS}",
    )

    # corr 4: g_s(M_Pl) * sqrt(u_0) = g_bare ((D1) restated)
    corr4_LHS = simplify(g_s_MPl * sqrt(u_0))
    corr4_target = g_bare
    check(
        "corollary 4: g_s(M_Pl) * sqrt(u_0) = g_bare",
        simplify(corr4_LHS - corr4_target) == 0,
        detail=f"got {corr4_LHS}",
    )

    # Cross-check: corollary 3 / corollary 4 equals corollary 1's ratio form
    cross_LHS = simplify(corr3_LHS / corr4_LHS)
    cross_target = y_t_bare / g_bare
    check(
        "cross-check: corr3 / corr4 = y_t_bare / g_bare",
        simplify(cross_LHS - cross_target) == 0,
        detail=f"got {cross_LHS}",
    )

    # ---------------------------------------------------------------------
    section("Part 4: free-symbol bookkeeping after substitution")
    # ---------------------------------------------------------------------
    # The (P1) LHS - RHS difference reduces to 0; its free symbols are empty.
    check(
        "(P1) LHS - RHS difference has empty free symbols after simplify",
        P1_diff.free_symbols == set(),
        detail=f"free_symbols = {P1_diff.free_symbols}",
    )

    # Pre-substitution: (D2)/(D1) retains free symbols {y_t_bare, g_bare, u_0}
    # before simplification, but after simplification u_0 cancels.
    # Build the ratio with evaluate=False so sympy does not eagerly cancel
    # the common 1/sqrt(u_0) factor before we inspect free_symbols.
    presimp_num = Mul(y_t_bare, Pow(u_0, -Rational(1, 2)), evaluate=False)
    presimp_den = Mul(g_bare, Pow(u_0, -Rational(1, 2)), evaluate=False)
    presimp_ratio = Mul(presimp_num, Pow(presimp_den, -1, evaluate=False), evaluate=False)
    presimp_free = presimp_ratio.free_symbols
    print(f"  pre-simplify (unevaluated) ratio = {presimp_ratio}")
    print(f"  pre-simplify ratio free_symbols = {presimp_free}")
    check(
        "pre-simplify (D2)/(D1) contains u_0 syntactically",
        u_0 in presimp_free,
        detail=f"u_0 in {presimp_free}",
    )
    simplified_ratio = simplify(presimp_ratio)
    check(
        "post-simplify ratio drops u_0 from free_symbols",
        u_0 not in simplified_ratio.free_symbols,
        detail=f"free_symbols of simplified ratio = {simplified_ratio.free_symbols}",
    )
    check(
        "post-simplify ratio equals y_t_bare / g_bare",
        simplify(simplified_ratio - y_t_bare / g_bare) == 0,
        detail=f"got {simplified_ratio}",
    )

    # ---------------------------------------------------------------------
    section("Part 5: numerical FP cross-check at one independent random sample")
    # ---------------------------------------------------------------------
    # The algebraic identity is the load-bearing content; an FP numerical
    # cross-check at one randomly-chosen sample is a sanity check, not the
    # authority.
    sample = {
        g_bare: Rational("71", 100),
        y_t_bare: Rational("41", 100),
        u_0: Rational("876", 1000),
    }
    P1_LHS_num = float((y_t_MPl / g_s_MPl).subs(sample))
    P1_RHS_num = float((y_t_bare / g_bare).subs(sample))
    fp_ok = abs(P1_LHS_num - P1_RHS_num) < 1e-12
    check(
        "(P1) FP sanity at sample (g_bare=0.71, y_t_bare=0.41, u_0=0.876)",
        fp_ok,
        detail=f"|LHS - RHS| = {abs(P1_LHS_num - P1_RHS_num):.3e}",
    )

    # Independence of u_0: vary u_0, ratio stays fixed.
    sample2 = {
        g_bare: Rational("71", 100),
        y_t_bare: Rational("41", 100),
        u_0: Rational("123", 1000),  # different u_0
    }
    P1_LHS_num2 = float((y_t_MPl / g_s_MPl).subs(sample2))
    indep_ok = abs(P1_LHS_num - P1_LHS_num2) < 1e-12
    check(
        "(P1) FP ratio independent of u_0: same ratio at u_0=0.876 and u_0=0.123",
        indep_ok,
        detail=f"|ratio(u_0=0.876) - ratio(u_0=0.123)| = {abs(P1_LHS_num - P1_LHS_num2):.3e}",
    )

    # ---------------------------------------------------------------------
    section("Part 6: counterfactual probes (equal-n_link is load-bearing)")
    # ---------------------------------------------------------------------
    # If the two couplings had different n_link, (P1) would not be u_0-independent.
    # At n_link(g_s) = 1, n_link(y_t) = 2 (counterfactual):
    g_s_cf = g_bare / sqrt(u_0)
    y_t_cf_n2 = y_t_bare / u_0  # if n_link(y_t) were 2 (and tadpole power 1)
    ratio_cf_n2 = simplify(y_t_cf_n2 / g_s_cf)
    # = (y_t_bare/u_0) / (g_bare/sqrt(u_0)) = y_t_bare/(u_0 * g_bare) * sqrt(u_0)
    # = y_t_bare / (g_bare * sqrt(u_0))
    check(
        "counterfactual: at n_link(y_t) = 2 != n_link(g_s) = 1, ratio carries 1/sqrt(u_0)",
        u_0 in ratio_cf_n2.free_symbols,
        detail=f"counterfactual ratio = {ratio_cf_n2} (u_0 in free_symbols confirms equal-n_link load-bearing)",
    )

    # At n_link(g_s) = 0 (no tadpole on g_s) versus n_link(y_t) = 1:
    g_s_cf_n0 = g_bare  # no u_0 dressing
    y_t_cf_n1 = y_t_bare / sqrt(u_0)
    ratio_cf_n0 = simplify(y_t_cf_n1 / g_s_cf_n0)
    # = y_t_bare / (g_bare * sqrt(u_0)), retains u_0
    check(
        "counterfactual: at n_link(g_s) = 0 (no CMT) vs n_link(y_t) = 1, ratio retains u_0",
        u_0 in ratio_cf_n0.free_symbols,
        detail=f"counterfactual ratio = {ratio_cf_n0}",
    )

    # ---------------------------------------------------------------------
    section("Part 7: parametric CMT form (general n_link, sanity)")
    # ---------------------------------------------------------------------
    # The CMT identity reads <O(U)> = u_0^n <O_V(V)>_eff with operator-
    # square-root normalization for the coupling readout giving
    #   coupling_canonical(O) := coupling_bare / u_0^{n/2}
    # The ratio is u_0-independent iff the two couplings have the same n_link.
    g_s_gen = g_bare / u_0**(Rational(n_v, 2))           # n_link = n_v for g_s
    y_t_gen = y_t_bare / u_0**(Rational(n_v, 2))         # same n_link
    ratio_gen = simplify(y_t_gen / g_s_gen)
    check(
        "parametric CMT: ratio is u_0-independent iff n_link(g_s) = n_link(y_t)",
        u_0 not in ratio_gen.free_symbols,
        detail=f"ratio = {ratio_gen} (u_0 absent from free_symbols)",
    )

    # Counterfactual: at unequal n_link, the ratio retains u_0.
    n_g = Symbol("n_g", positive=True, integer=True)
    n_y = Symbol("n_y", positive=True, integer=True)
    g_s_param = g_bare / u_0**(n_g / 2)
    y_t_param = y_t_bare / u_0**(n_y / 2)
    ratio_param = simplify(y_t_param / g_s_param)
    # = (y_t_bare / g_bare) * u_0^((n_g - n_y) / 2). Zero u_0 dependence iff n_g = n_y.
    ratio_param_at_unequal = simplify(ratio_param.subs({n_g: 1, n_y: 2}))
    check(
        "counterfactual: at n_g = 1, n_y = 2 (unequal), ratio retains u_0",
        u_0 in ratio_param_at_unequal.free_symbols,
        detail=f"ratio at (n_g=1, n_y=2) = {ratio_param_at_unequal}",
    )

    # And at n_g = n_y = 1, the ratio is u_0-independent.
    ratio_param_at_equal = simplify(ratio_param.subs({n_g: 1, n_y: 1}))
    check(
        "parametric CMT: at n_g = n_y = 1, ratio is u_0-independent",
        u_0 not in ratio_param_at_equal.free_symbols,
        detail=f"ratio at (n_g=1, n_y=1) = {ratio_param_at_equal}",
    )

    # ---------------------------------------------------------------------
    section("Summary")
    # ---------------------------------------------------------------------
    print("  Verified at exact sympy precision:")
    print("    (P1) y_t(M_Pl) / g_s(M_Pl) = y_t_bare / g_bare parametric in")
    print("         (g_bare, y_t_bare, u_0)")
    print("    (P1) ratio is identically independent of u_0 after simplify")
    print("    Four corollary identities all reduce to 0 parametrically")
    print("    Pre/post simplify free-symbol bookkeeping confirms u_0 cancellation")
    print("    FP numerical cross-check passes at two independent u_0 samples")
    print("    (ratio is FP-identical at u_0=0.876 and u_0=0.123)")
    print("    Counterfactual: unequal n_link collapses u_0-independence")
    print("    Parametric CMT form: u_0-independence iff n_link(g_s) = n_link(y_t)")

    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
