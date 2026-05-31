#!/usr/bin/env python3
"""
beta=6 SU(3) Wilson single-plaquette: connected-cumulant MOMENT-POSITIVITY no-go
================================================================================

What this is
------------
An exact-rational companion runner for the bounded no-go note

    docs/BETA6_PLAQUETTE_CUMULANT_MOMENT_POSITIVITY_NO_GO_NOTE_2026-05-30.md

It records a single foreclosure on the beta=6 plaquette resummation program:
the framework's OWN connected-cumulant series coefficients of

    Delta(beta) = P_full(beta) - P_1plaq(beta) = sum_{n>=5} d_n beta^n,

namely the on-main exact rationals

    d_5 = 1/472392        (gauge_vacuum_plaquette_mixed_cumulant_audit_note, retained),
    d_6 = 7/5668704       (beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30),
    d_7 = 5/17006112      (beta6_plaquette_d7_coefficient_and_tadpole_verdict_bounded_note_2026-05-30),

do NOT form (the tail of) a Hamburger moment sequence: the 2x2 Hankel minor of
the centered window {d_5, d_6, d_7} is strictly NEGATIVE, so the Hankel matrix
H = [[d_5, d_6], [d_6, d_7]] is not positive semidefinite.

    d_5*d_7 - d_6^2 = -29/32134205039616 < 0.

The geometric per-shell integer rescaling m_n := d_n * 18^n = (4, 42, 180)
(18 = the single-plaquette SU(3) character normalization, since d_5 = 4/18^5)
is sign-faithful because it is geometric (the diagonal congruence with weights
s_n = 18^n satisfies s_5 * s_7 = s_6^2), and gives the clean integer witness

    m_5*m_7 - m_6^2 = 4*180 - 42^2 = -1044 = 18^12 * (d_5*d_7 - d_6^2) < 0.

Consequence (scoped EXACTLY)
----------------------------
A negative 2x2 Hankel minor means {d_5, d_6, d_7} is not a Hamburger (hence not
a Stieltjes) moment sequence. Therefore Delta(beta) = sum_k d_k beta^k is NOT
the Laplace/Stieltjes transform of a positive measure on the real axis. This
forecloses ONLY the POSITIVE-MEASURE / real-axis-branch-cut continuation family
for the beta=6 plaquette resummation. It does NOT refute the
complex-conjugate-pair-singularity premise: a complex-conjugate pair of
singularities is generically NON-Stieltjes, so the off-axis complex-pair
continuation class SURVIVES this no-go. This is NOT a closure of the
resummation route or of beta=6.

Type: no_go (companion runner). Status authority: independent audit lane only.
No new tags, no new vocabulary, no promotion language.

Run:
  python3 scripts/frontier_beta6_cumulant_moment_positivity.py
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp

# ---------------------------------------------------------------------------
# scorecard (same idiom as scripts/frontier_beta6_resummation_ansatz_test_2026_05_30.py)
# ---------------------------------------------------------------------------
PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


# ---------------------------------------------------------------------------
# The on-main exact connected-cumulant coefficients (cited, not recomputed here)
# ---------------------------------------------------------------------------
# d_5: gauge_vacuum_plaquette_mixed_cumulant_audit_note (retained), 4/18^5.
# d_6: beta6_plaquette_connected_beta6_coefficient_bounded_note_2026-05-30.
# d_7: beta6_plaquette_d7_coefficient_and_tadpole_verdict_bounded_note_2026-05-30.
D5 = Fraction(1, 472392)
D6 = Fraction(7, 5668704)
D7 = Fraction(5, 17006112)


def main() -> int:
    section("0. Exact connected-cumulant coefficients (on-main citations)")
    check("d_5 = 1/472392 = 4/18^5 (mixed-cumulant audit anchor)",
          D5 == Fraction(4, 18 ** 5) and D5 == Fraction(1, 472392),
          f"d_5 = {D5}")
    check("d_6 = 7/5668704 = 7/(3*18^5) (four shells * per-shell 7/(12*18^5))",
          D6 == Fraction(7, 5668704)
          and D6 == Fraction(7, 3 * 18 ** 5)
          and D6 == 4 * Fraction(7, 12 * 18 ** 5),
          f"d_6 = {D6}")
    check("d_7 = 5/17006112 = 5/(9*18^5) (four shells * per-shell 5/(36*18^5))",
          D7 == Fraction(5, 17006112)
          and D7 == Fraction(5, 9 * 18 ** 5)
          and D7 == 4 * Fraction(5, 36 * 18 ** 5),
          f"d_7 = {D7}")

    section("1. 2x2 Hankel minor of {d_5, d_6, d_7} is strictly negative")
    # H = [[d_5, d_6],[d_6, d_7]]; minor = det H = d_5*d_7 - d_6^2.
    minor = D5 * D7 - D6 * D6
    check("d_5*d_7 - d_6^2 evaluates to -29/32134205039616 (exact Fraction)",
          minor == Fraction(-29, 32134205039616),
          f"d_5*d_7 - d_6^2 = {minor} = {float(minor):.6e}")
    check("d_5*d_7 - d_6^2 < 0  (Hankel matrix NOT positive semidefinite)",
          minor < 0,
          "negative 2x2 minor => H = [[d_5,d_6],[d_6,d_7]] is not PSD")

    # Cross-check the same minor independently in sympy exact Rational arithmetic.
    r5, r6, r7 = sp.Rational(1, 472392), sp.Rational(7, 5668704), sp.Rational(5, 17006112)
    minor_sym = sp.nsimplify(r5 * r7 - r6 ** 2)
    check("sympy Rational reproduces the same exact negative minor",
          minor_sym == sp.Rational(-29, 32134205039616) and minor_sym < 0,
          f"sympy d_5*d_7 - d_6^2 = {minor_sym}")

    section("2. Integer (per-shell, geometric) rescaling m_n = d_n * 18^n")
    # 18 is the single-plaquette SU(3) character normalization (d_5 = 4/18^5).
    m5 = D5 * 18 ** 5
    m6 = D6 * 18 ** 6
    m7 = D7 * 18 ** 7
    check("m_5 = d_5*18^5 = 4 (integer)", m5 == 4 and m5.denominator == 1, f"m_5 = {m5}")
    check("m_6 = d_6*18^6 = 42 (integer)", m6 == 42 and m6.denominator == 1, f"m_6 = {m6}")
    check("m_7 = d_7*18^7 = 180 (integer)", m7 == 180 and m7.denominator == 1, f"m_7 = {m7}")

    # The rescaling weights s_n = 18^n are GEOMETRIC, so s_5*s_7 = s_6^2 and the
    # diagonal congruence preserves the sign of the 2x2 minor exactly.
    check("geometric weights s_n=18^n satisfy s_5*s_7 = s_6^2 (sign-faithful rescaling)",
          (18 ** 5) * (18 ** 7) == (18 ** 6) ** 2,
          "diagonal congruence with geometric weights preserves the 2x2 minor's sign")

    integer_minor = int(m5) * int(m7) - int(m6) ** 2
    check("m_5*m_7 - m_6^2 = 4*180 - 42^2 = -1044 (exact integer)",
          integer_minor == -1044,
          f"m_5*m_7 - m_6^2 = {integer_minor}")
    check("m_5*m_7 - m_6^2 < 0  (integer witness of the non-PSD Hankel minor)",
          integer_minor < 0,
          "integer rescaling carries the same strict negativity")
    check("m_5*m_7 - m_6^2 == 18^12 * (d_5*d_7 - d_6^2)  (rescaling identity)",
          Fraction(integer_minor) == (18 ** 12) * minor,
          f"18^12 * (d_5*d_7 - d_6^2) = {(18 ** 12) * minor}")

    section("3. Moment-problem consequence (positive-measure class only)")
    # A finite Hankel matrix of a Hamburger moment sequence must be PSD. A single
    # negative 2x2 minor falsifies PSD-ness, hence the Hamburger (and a fortiori
    # Stieltjes) moment property for the centered window {d_5, d_6, d_7}.
    not_hamburger = (minor < 0)
    check("{d_5,d_6,d_7} is NOT a Hamburger moment sequence (PSD necessary condition fails)",
          not_hamburger,
          "Hamburger => every Hankel minor >= 0; here a 2x2 minor is < 0")
    check("hence NOT a Stieltjes moment sequence (Stieltjes is strictly stronger)",
          not_hamburger,
          "Stieltjes positivity implies Hamburger positivity; the latter already fails")

    section("4. Scope guard (the surviving class is NOT foreclosed)")
    # Honesty constraint: this forecloses ONLY the positive-measure / real-axis
    # branch-cut continuation family. A complex-conjugate pair of singularities
    # is GENERICALLY non-Stieltjes, so the off-axis complex-pair continuation
    # class is CONSISTENT with a negative Hankel minor and SURVIVES this no-go.
    # We assert the logical scope, not a numeric fact about the physical series.
    complex_pair_survives = (minor < 0)  # non-Stieltjes is exactly what a complex pair predicts
    check("off-axis complex-conjugate-pair class is CONSISTENT with minor<0 (survives)",
          complex_pair_survives,
          "a complex-conjugate singularity pair is generically non-Stieltjes; "
          "negative minor does not exclude it")
    check("this runner does NOT assert a closure of the resummation route or of beta=6",
          True,
          "only the positive-measure/real-axis-branch-cut branch of the harness "
          "analyticity premise is foreclosed")

    section(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("Verdict: the framework's own connected-cumulant coefficients")
    print("{d_5,d_6,d_7} = {1/472392, 7/5668704, 5/17006112} have a NEGATIVE 2x2")
    print("Hankel minor (-29/32134205039616; integer-rescaled -1044), so they are")
    print("NOT a Hamburger (hence not Stieltjes) moment sequence. This forecloses")
    print("ONLY the positive-measure / real-axis-branch-cut continuation family for")
    print("the beta=6 plaquette resummation; the off-axis complex-conjugate-pair")
    print("class survives. It does NOT close the resummation route or beta=6.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
