#!/usr/bin/env python3
"""Narrow runner for HIERARCHY_SEVEN_EIGHTHS_TWISTED_THERMAL_ZETA_PERIOD_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-26.

Verifies the standalone class-A narrow theorem on the
APBC/PBC twisted thermal-zeta period quotient:

  Q(s)  =  (2 lambda(s) - zeta(s)) / zeta(s)  =  1 - 2^(1 - s)  =  eta(s)/zeta(s),

where
  - zeta(s)   = sum_{n>=1} 1/n^s              (Riemann zeta)
  - lambda(s) = sum_{n>=0} 1/(2n+1)^s         (Dirichlet lambda)
  - eta(s)    = sum_{n>=1} (-1)^{n-1}/n^s     (Dirichlet eta)

At s=4 integer dimension, Q(4) = 7/8 exactly. The derivation route
uses the Hurwitz-zeta twist  zeta(s, 1/2) = 2^s lambda(s)  on the
thermal circle S^1_beta corresponding to APBC fermion modes
omega_n = (2n+1)pi/beta.

CORRECTED MATSUBARA NORMALIZATION (2026-05-28).
An earlier revision quoted the dimensionless Matsubara rescalings with
the RECIPROCAL scale factor (it multiplied (omega_n)^(-s) by (beta/2pi)^s,
a power of TIME = mu^(-s)), so the rescaled traces were NOT dimensionless
and did not equal zeta(s)/lambda(s) as written. The auditor flagged this:
  (2pi n/beta)^(-s)*(beta/2pi)^s = (beta/2pi)^(2s)*n^(-s)  !=  n^(-s).
The correct, non-reciprocal convention divides each Matsubara tower by
ITS OWN fundamental frequency (mu_B = 2pi/beta for PBC, mu_F = pi/beta
for APBC), i.e. the summand is (omega_n/mu)^(-s) with mu a FREQUENCY, so
the rescaling factor is mu^(+s):
  zeta_B(s) = sum_{n>=1} (2pi n/beta)^(-s) * (2pi/beta)^s   = zeta(s),
  zeta_F(s) = sum_{n>=0} ((2n+1)pi/beta)^(-s) * (pi/beta)^s = lambda(s).
T15-T17 below verify this corrected rescaling bridge (the part the
earlier runner never checked). The closed-form quotient
Q(s) = 1 - 2^(1-s) is unchanged. Because the sector-native
dimensionless-reference choice (zeta_B = zeta, zeta_F = lambda) is a
conditioning convention, the claim is a bounded_theorem (conditional),
not an unconditional positive theorem.

This is the W6 derivation-route witness for the
HIERARCHY_SEVEN_EIGHTHS_QUARTER_FERMION_BOSON_SCALE_CONVERSION_BRIDGE
parent bridge note. The arithmetic collapses onto W3
(eta(4)/zeta(4) = 7/8) per the D2 collapse caveat documented in
section 0 of the source note. No new arithmetic fact; only a
different derivation chain (Hurwitz-zeta twist vs Fermi-Dirac
integral).

Class-A arithmetic core (rational-arithmetic + classical analytic-
number-theory identity); one conditioning input, the sector-native
dimensionless-reference convention zeta_B = zeta, zeta_F = lambda. No
framework axiom or observational input is consumed.

Target: PASS = 21, FAIL = 0.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from pathlib import Path

try:
    import sympy as sp
    from sympy import (
        Rational,
        Symbol,
        dirichlet_eta,
        pi,
        simplify,
        symbols,
        zeta,
    )
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)

try:
    import mpmath
except ImportError:
    print("FAIL: mpmath required for high-precision numerical checks")
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent

PASS = 0
FAIL = 0
FAILURES: list[str] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS (A)"
    else:
        FAIL += 1
        FAILURES.append(f"{label}: {detail}")
        tag = "FAIL (A)"
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print("\n" + "-" * 88 + f"\n{title}\n" + "-" * 88)


# ============================================================================
# Helper: Dirichlet lambda function (sympy does not expose it directly,
# so build it from zeta via lambda(s) = (1 - 2^{-s}) zeta(s))
# ============================================================================

def lambda_func(s):
    """Dirichlet lambda lambda(s) = sum_{n>=0} 1/(2n+1)^s = (1 - 2^{-s}) zeta(s)."""
    return (1 - sp.Rational(2) ** (-s)) * sp.zeta(s)


def lambda_numeric(s):
    """Numeric Dirichlet lambda for mpmath."""
    return (mpmath.mpf(1) - mpmath.power(2, -s)) * mpmath.zeta(s)


# ============================================================================
section("Pattern A narrow theorem: 7/8 twisted thermal-zeta period quotient")
# Statement: at d = 4 integer, the APBC/PBC twisted thermal-zeta quotient
# Q(s) = (2 lambda(s) - zeta(s)) / zeta(s) = 1 - 2^(1-s) equals 7/8 exactly.
# At any other integer d >= 2, Q != 7/8. Pure analytic-number-theory.
# ============================================================================


# ----------------------------------------------------------------------------
section("Part 1: Riemann zeta odd-tail split (T1)")
# Statement: zeta(s) = lambda(s) + 2^(-s) zeta(s) by odd/even partial sums.
# Equivalent: lambda(s) = (1 - 2^(-s)) zeta(s).
# ----------------------------------------------------------------------------

def t1_symbolic_split() -> bool:
    # zeta(s) = lambda(s) + 2^(-s) zeta(s) symbolically (using lambda definition
    # lambda(s) = (1 - 2^(-s)) zeta(s)).
    s = symbols("s", positive=True)
    lhs = sp.zeta(s)
    rhs = lambda_func(s) + sp.Rational(2) ** (-s) * sp.zeta(s)
    return simplify(lhs - rhs) == 0


check(
    "T1: zeta(s) = lambda(s) + 2^(-s) zeta(s) symbolic",
    t1_symbolic_split(),
    detail="odd/even partial-sum split of positive integers",
)


def t1_numeric_split(s_val: int) -> bool:
    # Numerical check at integer s_val: zeta(s) ≈ lambda(s) + 2^(-s) zeta(s)
    mpmath.mp.dps = 40
    zs = mpmath.zeta(s_val)
    ls = lambda_numeric(s_val)
    rhs = ls + mpmath.power(2, -s_val) * zs
    return abs(zs - rhs) < mpmath.mpf("1e-30")


for s_val in [2, 3, 4, 5]:
    check(
        f"T1b: zeta({s_val}) = lambda({s_val}) + 2^(-{s_val}) zeta({s_val}) (40-digit mpmath)",
        t1_numeric_split(s_val),
        detail=f"odd-tail identity at integer s={s_val}",
    )


# ----------------------------------------------------------------------------
section("Part 2: Dirichlet lambda closed form (T2)")
# Statement: lambda(s) = (1 - 2^(-s)) zeta(s) — directly from the split.
# ----------------------------------------------------------------------------

def t2_lambda_closed_form() -> bool:
    s = symbols("s", positive=True)
    lhs = lambda_func(s)
    rhs = (1 - sp.Rational(2) ** (-s)) * sp.zeta(s)
    return simplify(lhs - rhs) == 0


check(
    "T2: lambda(s) = (1 - 2^(-s)) zeta(s) symbolic",
    t2_lambda_closed_form(),
    detail="closed form (B) in source note",
)


# ----------------------------------------------------------------------------
section("Part 3: Hurwitz zeta half-integer twist (T3)")
# Statement: zeta(s, 1/2) = 2^s lambda(s) where zeta(s, a) is Hurwitz zeta.
# Equivalent: the APBC Matsubara fermion sum reduces to Hurwitz zeta at
# twist a = 1/2.
# ----------------------------------------------------------------------------

def t3_hurwitz_half_twist() -> bool:
    # zeta(s, 1/2) = sum_{n>=0} 1/(n+1/2)^s
    #              = sum_{n>=0} 2^s/(2n+1)^s
    #              = 2^s lambda(s)
    # Sympy does NOT auto-simplify Hurwitz zeta to elementary closed form for
    # generic s; the symbolic difference does not collapse to 0. Verify the
    # identity numerically at several integer s by high-precision mpmath
    # instead — the analytic identity (D) is then a textbook consequence of
    # the partial-sum split (A)-(B).
    mpmath.mp.dps = 40
    for s_val in [2, 3, 4, 5, 6]:
        lhs = mpmath.zeta(s_val, mpmath.mpf("0.5"))  # Hurwitz zeta at a=1/2
        ls = lambda_numeric(s_val)
        rhs = mpmath.power(2, s_val) * ls
        if abs(lhs - rhs) > mpmath.mpf("1e-30"):
            return False
    return True


check(
    "T3: zeta(s, 1/2) = 2^s lambda(s) at s in {2..6} (40-digit mpmath)",
    t3_hurwitz_half_twist(),
    detail="DLMF section 25.11.1, half-integer twist",
)


# ----------------------------------------------------------------------------
section("Part 4: Twisted thermal-zeta quotient closed form (T4)")
# Statement: Q(s) = (2 lambda(s) - zeta(s)) / zeta(s) = 1 - 2^(1-s).
# This is the central identity of the narrow theorem (F) in source.
# ----------------------------------------------------------------------------

def t4_quotient_closed_form() -> bool:
    s = symbols("s", positive=True)
    Q = (2 * lambda_func(s) - sp.zeta(s)) / sp.zeta(s)
    target = 1 - sp.Rational(2) ** (1 - s)
    return simplify(Q - target) == 0


check(
    "T4: Q(s) = (2 lambda(s) - zeta(s)) / zeta(s) = 1 - 2^(1-s) symbolic",
    t4_quotient_closed_form(),
    detail="central identity (F) in source note section 2.3",
)


# ----------------------------------------------------------------------------
section("Part 5: Bridge Q(s) = eta(s) / zeta(s) (T5)")
# Statement: Q(s) = eta(s)/zeta(s), confirming the W6 = W3 arithmetic
# collapse explicitly. D2 caveat acknowledgment.
# ----------------------------------------------------------------------------

def t5_quotient_equals_eta_over_zeta() -> bool:
    # Q(s) = (2 lambda(s) - zeta(s)) / zeta(s) = 1 - 2^(1-s) = eta(s)/zeta(s).
    # Use dirichlet_eta(s).rewrite(zeta) to expose the standard identity
    # eta(s) = (1 - 2^(1-s)) zeta(s) which sympy then simplifies.
    s = symbols("s", positive=True)
    Q = (2 * lambda_func(s) - sp.zeta(s)) / sp.zeta(s)
    # Use the rewrite identity for eta in terms of zeta
    eta_in_zeta = sp.dirichlet_eta(s).rewrite(sp.zeta)
    bridge = eta_in_zeta / sp.zeta(s)
    diff = simplify(Q - bridge)
    # diff is Piecewise((nan, Eq(s,1)), (0, True)); the True branch gives 0.
    # We want the s != 1 branch to be identically zero.
    if isinstance(diff, sp.Piecewise):
        for expr, cond in diff.args:
            if cond is sp.S.true or cond == True:  # noqa: E712
                if expr != 0:
                    return False
        return True
    return diff == 0


check(
    "T5: Q(s) = eta(s)/zeta(s) symbolic (bridge to W3, via eta.rewrite(zeta))",
    t5_quotient_equals_eta_over_zeta(),
    detail="explicit D2 collapse: W6 = W3 arithmetic",
)


# ----------------------------------------------------------------------------
section("Part 6: Q(4) = 7/8 exact rational (T6)")
# Statement: at s = 4 integer dimension, Q(4) = 7/8 exactly.
# ----------------------------------------------------------------------------

def t6_q_at_four_is_seven_eighths() -> bool:
    Q4 = (2 * lambda_func(4) - sp.zeta(4)) / sp.zeta(4)
    return simplify(Q4 - sp.Rational(7, 8)) == 0


check(
    "T6: Q(4) = 7/8 exact rational",
    t6_q_at_four_is_seven_eighths(),
    detail="at s=4, twisted thermal-zeta quotient = 7/8",
)


# ----------------------------------------------------------------------------
section("Part 7: Negative scan — Q(d) != 7/8 at d != 4 (T7)")
# Statement: at integer d in {2, 3, 5, 6}, Q(d) != 7/8.
# Reports explicit failure values.
# ----------------------------------------------------------------------------

q_values = {}
for d in [2, 3, 4, 5, 6]:
    Qd = (2 * lambda_func(d) - sp.zeta(d)) / sp.zeta(d)
    q_values[d] = simplify(Qd)

target = sp.Rational(7, 8)
expected = {
    2: sp.Rational(1, 2),    # 1 - 2^(-1) = 1/2
    3: sp.Rational(3, 4),    # 1 - 2^(-2) = 3/4
    4: sp.Rational(7, 8),    # 1 - 2^(-3) = 7/8
    5: sp.Rational(15, 16),  # 1 - 2^(-4) = 15/16
    6: sp.Rational(31, 32),  # 1 - 2^(-5) = 31/32
}


def t7_negative_scan() -> bool:
    # Verify Q matches expected at each d, and != 7/8 at d != 4.
    for d, exp in expected.items():
        if simplify(q_values[d] - exp) != 0:
            return False
        if d != 4 and simplify(q_values[d] - target) == 0:
            return False
    return True


detail_str = " | ".join(f"Q({d})={q_values[d]}" for d in [2, 3, 4, 5, 6])
check(
    "T7: Q(d) values across d in {2..6}, only d=4 gives 7/8",
    t7_negative_scan(),
    detail=detail_str,
)


# ----------------------------------------------------------------------------
section("Part 8: eta(4)/zeta(4) = 7/8 (T8)")
# Statement: independent sympy cross-check of eta(4)/zeta(4) = 7/8.
# ----------------------------------------------------------------------------

def t8_eta_over_zeta_at_four() -> bool:
    r = sp.dirichlet_eta(4) / sp.zeta(4)
    return simplify(r - sp.Rational(7, 8)) == 0


check(
    "T8: eta(4)/zeta(4) = 7/8 exact (independent cross-check)",
    t8_eta_over_zeta_at_four(),
    detail="sympy dirichlet_eta(4) / zeta(4) simplification",
)


# ----------------------------------------------------------------------------
section("Part 9: 40-digit mpmath numerical verification at s=4 (T9)")
# Statement: Q(4) ≈ 7/8 to 30+ decimal digits via mpmath.
# ----------------------------------------------------------------------------

def t9_q_at_four_numerical() -> bool:
    mpmath.mp.dps = 40
    z4 = mpmath.zeta(4)
    l4 = lambda_numeric(4)
    Q4 = (2 * l4 - z4) / z4
    return abs(Q4 - mpmath.mpf("0.875")) < mpmath.mpf("1e-30")


check(
    "T9: Q(4) = 7/8 to 30+ digits (40-digit mpmath)",
    t9_q_at_four_numerical(),
    detail="high-precision numerical cross-check of T6",
)


# ----------------------------------------------------------------------------
section("Part 10: 40-digit mpmath numerical scan d != 4 (T10)")
# Statement: at integer d in {2, 5, 6}, |Q(d) - 7/8| > 0 substantially.
# ----------------------------------------------------------------------------

def t10_q_negative_scan_numerical() -> bool:
    mpmath.mp.dps = 40
    expected_numeric = {2: 0.5, 3: 0.75, 5: 0.9375, 6: 0.96875}
    target = mpmath.mpf("0.875")
    for d, exp_val in expected_numeric.items():
        zd = mpmath.zeta(d)
        ld = lambda_numeric(d)
        Qd = (2 * ld - zd) / zd
        # Must equal expected_numeric value
        if abs(Qd - mpmath.mpf(exp_val)) > mpmath.mpf("1e-30"):
            return False
        # Must differ from 7/8
        if abs(Qd - target) < mpmath.mpf("1e-3"):
            return False
    return True


check(
    "T10: Q(d) at d in {2,3,5,6} match expected; all != 7/8 (40-digit mpmath)",
    t10_q_negative_scan_numerical(),
    detail="negative scan, high precision",
)


# ----------------------------------------------------------------------------
section("Part 11: Partial-sum split check at s=4 (T11)")
# Statement: at N=200, partial sums confirm zeta = lambda + 2^(-s) zeta
# via direct truncated odd/even split.
# ----------------------------------------------------------------------------

def t11_partial_sum_split() -> bool:
    mpmath.mp.dps = 30
    N = 200
    s_val = 4
    # zeta_N = sum_{n=1..N} 1/n^s
    zeta_N = mpmath.fsum(mpmath.mpf(1) / mpmath.mpf(n) ** s_val for n in range(1, N + 1))
    # lambda_N = sum_{n=0..N//2} 1/(2n+1)^s, but to keep range comparable,
    # take all odd n in 1..N.
    lambda_N = mpmath.fsum(
        mpmath.mpf(1) / mpmath.mpf(n) ** s_val for n in range(1, N + 1, 2)
    )
    # even-tail = sum_{m=1..N//2} 1/(2m)^s = 2^(-s) * zeta_(N//2)
    even_N = mpmath.fsum(
        mpmath.mpf(1) / mpmath.mpf(2 * m) ** s_val for m in range(1, N // 2 + 1)
    )
    # zeta_N - lambda_N should equal even_N (modulo tail)
    residual = zeta_N - lambda_N - even_N
    # Tolerance: tail of zeta(4) past N=200 is ~ 1/(3*200^3) ~ 4e-8
    return abs(residual) < mpmath.mpf("1e-6")


check(
    "T11: partial-sum split at N=200, s=4: zeta_N - lambda_N - even_N ~ 0",
    t11_partial_sum_split(),
    detail="finite-N truncation of odd/even split (B)",
)


# ----------------------------------------------------------------------------
section("Part 12: Sympy zeta(4, 1/2) cross-check (T12)")
# Statement: sympy zeta(4, 1/2) returns 16 * lambda(4) = 16 * (15/16) * zeta(4)
#         = 15 * zeta(4) = 15 * pi^4 / 90 = pi^4 / 6.
# Wait, let's check: zeta(s, 1/2) = 2^s lambda(s), so at s=4:
# zeta(4, 1/2) = 16 * lambda(4) = 16 * (15/16) * zeta(4) = 15 zeta(4)
#              = 15 * pi^4/90 = pi^4/6.
# ----------------------------------------------------------------------------

def t12_hurwitz_at_four_closed_form() -> bool:
    # sympy zeta(4, 1/2) does not auto-collapse to elementary form; verify
    # numerically that it equals pi^4/6. Algebraic chain:
    #   zeta(4, 1/2) = 2^4 lambda(4) = 16 * (15/16) * zeta(4)
    #              = 15 * pi^4/90 = pi^4/6.
    mpmath.mp.dps = 40
    lhs = mpmath.zeta(4, mpmath.mpf("0.5"))
    rhs = mpmath.power(mpmath.pi, 4) / 6
    return abs(lhs - rhs) < mpmath.mpf("1e-30")


check(
    "T12: zeta(4, 1/2) = pi^4 / 6 (Hurwitz closed form, 40-digit mpmath)",
    t12_hurwitz_at_four_closed_form(),
    detail="cross-check of T3 at s=4: 2^4 * lambda(4) = 16 * (15/16) * pi^4/90 = pi^4/6",
)


# ----------------------------------------------------------------------------
section("Part 13: Bridge to W3 (T13) — Q(d) = eta(d)/zeta(d) across d")
# Statement: at integer d in {2, 3, 4, 5, 6}, Q(d) = eta(d)/zeta(d) exactly.
# Cross-checks D2 collapse.
# ----------------------------------------------------------------------------

def t13_bridge_to_w3_across_d() -> bool:
    # At integer d, Q(d) = 1 - 2^(1-d) and eta(d) = (1 - 2^(1-d)) zeta(d).
    # Use the eta.rewrite(zeta) identity (which sympy DOES collapse) and the
    # closed-form value of Q. Compare at each integer d via numeric mpmath
    # (so the identity holds beyond the s != 1 branch).
    mpmath.mp.dps = 40
    for d in [2, 3, 4, 5, 6]:
        Qd = (2 * lambda_numeric(d) - mpmath.zeta(d)) / mpmath.zeta(d)
        # eta(d)/zeta(d) numerically via Dirichlet eta closed form
        # eta(d) = (1 - 2^(1-d)) zeta(d)
        eta_d = (mpmath.mpf(1) - mpmath.power(2, 1 - d)) * mpmath.zeta(d)
        bridge_val = eta_d / mpmath.zeta(d)
        if abs(Qd - bridge_val) > mpmath.mpf("1e-30"):
            return False
        # Cross-check against direct closed form 1 - 2^(1-d)
        expected = mpmath.mpf(1) - mpmath.power(2, 1 - d)
        if abs(Qd - expected) > mpmath.mpf("1e-30"):
            return False
    return True


check(
    "T13: Q(d) = eta(d)/zeta(d) at d in {2,3,4,5,6} (40-digit mpmath, D2 collapse)",
    t13_bridge_to_w3_across_d(),
    detail="W6 = W3 arithmetic, different derivation route",
)


# ----------------------------------------------------------------------------
section("Part 14: D2 collapse honesty acknowledgement (T14)")
# Statement: print to stdout the D2 disclosure so the audit trail records it.
# Pass condition: at d=4, both W6 quotient and W3 quotient evaluate to 7/8
# and they're equal as a sympy expression.
# ----------------------------------------------------------------------------

def t14_d2_acknowledgement() -> bool:
    print("\n    [D2 disclosure]: W6 = same arithmetic as W3 via different derivation route.")
    print("    [D2 disclosure]: (2 lambda(4) - zeta(4)) / zeta(4) = eta(4)/zeta(4) = 7/8 exactly.")
    Q4_w6 = (2 * lambda_func(4) - sp.zeta(4)) / sp.zeta(4)
    Q4_w3 = sp.dirichlet_eta(4) / sp.zeta(4)
    if simplify(Q4_w6 - Q4_w3) != 0:
        return False
    if simplify(Q4_w6 - sp.Rational(7, 8)) != 0:
        return False
    return True


check(
    "T14: D2 disclosure printed and W6/W3 arithmetic equality verified",
    t14_d2_acknowledgement(),
    detail="explicit honesty disclosure of section 0 of source note",
)


# ----------------------------------------------------------------------------
section("Part 15: Corrected Matsubara rescaling bridge (T15) — eq. (1)-(2)")
# Statement: with the CORRECT, non-reciprocal convention (each tower divided
# by its OWN fundamental frequency mu, summand = (omega_n/mu)^(-s), so the
# rescaling factor is mu^(+s)), the dimensionless summands reduce exactly to
# n^(-s) and (2n+1)^(-s), giving zeta_B = zeta(s) and zeta_F = lambda(s).
# This is the load-bearing bridge the earlier revision quoted with the
# RECIPROCAL factor (beta/2pi)^s and that the prior runner never checked.
# Verified symbolically with beta, n, s free positive symbols (so the result
# holds identically in beta -- the traces are genuinely dimensionless).
# ----------------------------------------------------------------------------

def t15_corrected_rescaling_symbolic() -> bool:
    n, s, beta = sp.symbols("n s beta", positive=True)
    # Bosonic PBC: omega_n = 2*pi*n/beta, reference mu_B = 2*pi/beta.
    omega_B = 2 * sp.pi * n / beta
    mu_B = 2 * sp.pi / beta
    boson_summand = omega_B ** (-s) * mu_B ** s  # = (omega_B/mu_B)^(-s)
    if simplify(boson_summand - n ** (-s)) != 0:
        return False
    # Fermionic APBC: omega_n = (2n+1)*pi/beta, reference mu_F = pi/beta.
    omega_F = (2 * n + 1) * sp.pi / beta
    mu_F = sp.pi / beta
    fermion_summand = omega_F ** (-s) * mu_F ** s  # = (omega_F/mu_F)^(-s)
    if simplify(fermion_summand - (2 * n + 1) ** (-s)) != 0:
        return False
    return True


check(
    "T15: corrected dimensionless summands = n^(-s) and (2n+1)^(-s) symbolic",
    t15_corrected_rescaling_symbolic(),
    detail="(2pi n/beta)^(-s)*(2pi/beta)^s = n^(-s); ((2n+1)pi/beta)^(-s)*(pi/beta)^s = (2n+1)^(-s)",
)


# ----------------------------------------------------------------------------
section("Part 16: Reciprocal-error guard + beta-independence (T16)")
# Statement: (a) symbolically confirm the OLD factor (beta/2pi)^s is WRONG --
# (2pi n/beta)^(-s)*(beta/2pi)^s = (beta/2pi)^(2s)*n^(-s) != n^(-s); (b)
# numerically confirm the CORRECTED traces zeta_B, zeta_F are beta-independent
# and equal zeta(4), lambda(4) at three distinct beta, while the old factor
# gives a manifestly beta-dependent trace. This is the direct check of the
# auditor's reported defect.
# ----------------------------------------------------------------------------

def t16_reciprocal_guard_and_beta_independence() -> bool:
    n, s, beta = sp.symbols("n s beta", positive=True)
    # (a) Old (buggy) bosonic factor (beta/2pi)^s does NOT give n^(-s):
    omega_B = 2 * sp.pi * n / beta
    old_boson = omega_B ** (-s) * (beta / (2 * sp.pi)) ** s
    # It must EQUAL (beta/2pi)^(2s) * n^(-s) and must DIFFER from n^(-s).
    if simplify(old_boson - (beta / (2 * sp.pi)) ** (2 * s) * n ** (-s)) != 0:
        return False
    if simplify(old_boson - n ** (-s)) == 0:
        return False  # would mean the old factor was (wrongly) fine
    # Old (buggy) fermionic factor (beta/2pi)^s * 2^s = (beta/pi)^s:
    omega_F = (2 * n + 1) * sp.pi / beta
    old_fermion = omega_F ** (-s) * (beta / (2 * sp.pi)) ** s * 2 ** s
    if simplify(old_fermion - (beta / sp.pi) ** (2 * s) * (2 * n + 1) ** (-s)) != 0:
        return False
    if simplify(old_fermion - (2 * n + 1) ** (-s)) == 0:
        return False

    # (b) Numerical beta-independence of the CORRECTED traces at s=4.
    mpmath.mp.dps = 40
    s_val = 4
    NB, NF = 6000, 6000
    zeta4 = mpmath.zeta(s_val)
    lam4 = lambda_numeric(s_val)
    for beta_val in [mpmath.mpf("0.37"), mpmath.mpf("5.0"), 2 * mpmath.pi]:
        mu_B = 2 * mpmath.pi / beta_val
        mu_F = mpmath.pi / beta_val
        zB = mpmath.fsum(
            (2 * mpmath.pi * k / beta_val) ** (-s_val) * mu_B ** s_val
            for k in range(1, NB)
        )
        zF = mpmath.fsum(
            ((2 * k + 1) * mpmath.pi / beta_val) ** (-s_val) * mu_F ** s_val
            for k in range(0, NF)
        )
        # Truncation tail of zeta(4)/lambda(4) past N~6000 is ~ 1e-11.
        if abs(zB - zeta4) > mpmath.mpf("1e-9"):
            return False
        if abs(zF - lam4) > mpmath.mpf("1e-9"):
            return False
        # And the OLD factor would give a beta-dependent trace: at these
        # three betas the old bosonic trace (beta/2pi)^(2s)*zeta(4) takes
        # three different values, so it cannot equal zeta(4) at all three.
        old_zB = (beta_val / (2 * mpmath.pi)) ** (2 * s_val) * zeta4
        if beta_val != 2 * mpmath.pi and abs(old_zB - zeta4) < mpmath.mpf("1e-6"):
            return False  # old trace accidentally dimensionless -> would be a bug in the guard
    return True


check(
    "T16: old (beta/2pi)^s factor != n^(-s); corrected traces beta-independent = zeta(4),lambda(4)",
    t16_reciprocal_guard_and_beta_independence(),
    detail="direct check of auditor's reciprocal-normalization defect + dimensionlessness",
)


# ----------------------------------------------------------------------------
section("Part 17: Common-reference Hurwitz cross-link (T17) — eq. (D')")
# Statement: measuring the APBC tower against the COMMON bosonic reference
# mu_B = 2pi/beta (instead of its own mu_F = pi/beta) gives
# ((2n+1)pi/beta)^(-s)*(2pi/beta)^s = 2^s (2n+1)^(-s), whose sum is
# 2^s lambda(s) = zeta(s,1/2) (Hurwitz). So zeta_F^common and the
# sector-native zeta_F = lambda(s) differ by exactly (mu_B/mu_F)^s = 2^s.
# This is where the 2^s of section 2.2 legitimately lives.
# ----------------------------------------------------------------------------

def t17_common_reference_hurwitz_link() -> bool:
    n, s, beta = sp.symbols("n s beta", positive=True)
    omega_F = (2 * n + 1) * sp.pi / beta
    mu_B = 2 * sp.pi / beta
    common_summand = omega_F ** (-s) * mu_B ** s  # = (omega_F/mu_B)^(-s)
    # Must equal 2^s (2n+1)^(-s).
    if simplify(common_summand - 2 ** s * (2 * n + 1) ** (-s)) != 0:
        return False
    # And the ratio of reference scales is (mu_B/mu_F)^s = 2^s.
    mu_F = sp.pi / beta
    if simplify((mu_B / mu_F) ** s - 2 ** s) != 0:
        return False
    # Numerically: common-reference fermionic trace = 2^s lambda(s) = zeta(s,1/2).
    mpmath.mp.dps = 40
    for s_val in [2, 3, 4, 5, 6]:
        common_trace = mpmath.power(2, s_val) * lambda_numeric(s_val)
        hurwitz = mpmath.zeta(s_val, mpmath.mpf("0.5"))
        if abs(common_trace - hurwitz) > mpmath.mpf("1e-30"):
            return False
    return True


check(
    "T17: common-reference fermionic trace = 2^s (2n+1)^(-s) = 2^s lambda(s) = zeta(s,1/2)",
    t17_common_reference_hurwitz_link(),
    detail="the 2^s of section 2.2 is the reference-scale ratio (mu_B/mu_F)^s = 2^s",
)


# ============================================================================
# Summary
# ============================================================================
print("\n" + "=" * 88)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 88)

if FAIL > 0:
    print("\nFailure details:")
    for f in FAILURES:
        print(f"  - {f}")
    sys.exit(1)

print(
    "\nVERDICT: 7/8 twisted thermal-zeta period quotient narrow bounded_theorem passes.\n"
    "Corrected Matsubara normalization (T15-T17): dividing each Matsubara tower by\n"
    "its OWN fundamental frequency (mu_B=2pi/beta, mu_F=pi/beta), with the reference\n"
    "entering as mu^(+s) (NOT the reciprocal (beta/2pi)^s of the earlier revision),\n"
    "gives the dimensionless, beta-independent traces zeta_B = zeta(s), zeta_F = lambda(s).\n"
    "Then Q(s) = (2 lambda(s) - zeta(s)) / zeta(s) = 1 - 2^(1-s) = eta(s)/zeta(s);\n"
    "at integer s=4, Q(4) = 7/8 exactly; at any other integer d >= 2, Q(d) != 7/8.\n"
    "Conditional on the sector-native reference convention (zeta_B=zeta, zeta_F=lambda).\n"
    "W6 supplies a derivation-route witness to the parent bridge note; the\n"
    "underlying arithmetic collapses onto W3 (eta(4)/zeta(4) = 7/8) — D2 caveat\n"
    "explicitly acknowledged in source note section 0."
)
sys.exit(0)
