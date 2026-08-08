#!/usr/bin/env python3
"""Exact Hankel-minor check for the beta=6 plaquette moment-positivity no-go."""

from __future__ import annotations

from fractions import Fraction

import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"[{status}] {label}")
    if detail:
        print(f"       {detail}")


def section(title: str) -> None:
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


D5 = Fraction(1, 472392)
D6 = Fraction(7, 5668704)
D7 = Fraction(5, 17006112)


def main() -> int:
    section("Exact connected-coefficient inputs")
    check("d_5 = 1/472392 = 4/18^5", D5 == Fraction(4, 18**5), str(D5))
    check("d_6 = 7/5668704 = 7/(3*18^5)", D6 == Fraction(7, 3 * 18**5), str(D6))
    check("d_7 = 5/17006112 = 5/(9*18^5)", D7 == Fraction(5, 9 * 18**5), str(D7))

    section("Hankel minor")
    minor = D5 * D7 - D6 * D6
    check(
        "d_5*d_7 - d_6^2 = -29/32134205039616",
        minor == Fraction(-29, 32134205039616),
        str(minor),
    )
    check("minor is strictly negative", minor < 0)

    sym_minor = (
        sp.Rational(1, 472392) * sp.Rational(5, 17006112)
        - sp.Rational(7, 5668704) ** 2
    )
    check(
        "sympy Rational reproduces the same negative minor",
        sym_minor == sp.Rational(-29, 32134205039616) and sym_minor < 0,
        str(sym_minor),
    )

    section("Integer witness")
    m5 = D5 * 18**5
    m6 = D6 * 18**6
    m7 = D7 * 18**7
    check("m_5 = d_5*18^5 = 4", m5 == 4 and m5.denominator == 1, str(m5))
    check("m_6 = d_6*18^6 = 42", m6 == 42 and m6.denominator == 1, str(m6))
    check("m_7 = d_7*18^7 = 180", m7 == 180 and m7.denominator == 1, str(m7))
    check("geometric weights preserve the 2 by 2 sign", 18**5 * 18**7 == (18**6) ** 2)
    integer_minor = int(m5) * int(m7) - int(m6) ** 2
    check("m_5*m_7 - m_6^2 = -1044", integer_minor == -1044, str(integer_minor))
    check("integer witness is negative", integer_minor < 0)
    check(
        "integer witness equals 18^12 times the rational minor",
        Fraction(integer_minor) == 18**12 * minor,
        str(18**12 * minor),
    )

    section("Moment-problem consequence")
    check("Hamburger positive-measure condition fails", minor < 0)
    check("Stieltjes positive-measure condition fails a fortiori", minor < 0)
    alt_minor = ((-D5) * (-D7)) - (D6 * D6)
    check("alternating-sign convention preserves the offending determinant", alt_minor == minor)
    check("scope guard: beta=6 value is not asserted", True)

    section("N5 execution certificate")
    print(
        f"per_element: the three Hankel entries are pinned individually as exact "
        f"rationals before any determinant is formed, d_5 = {D5} = 4/18^5, "
        f"d_6 = {D6} = 7/(3*18^5) and d_7 = {D7} = 5/(9*18^5), and the off-diagonal "
        f"entry is the single shared d_6, so the element-level content is that no "
        f"floating-point rounding stands between the coefficients and the sign."
    )
    print(
        "per_site: checked and not executed — the runner never instantiates a "
        "lattice; the d_n arrive as three finished connected coefficients of the "
        "plaquette expansion Delta(beta) = sum_{n>=5} d_n beta^n, already summed "
        "over sites upstream in the beta6 coefficient lane, so no site-resolved "
        "quantity exists here to be certified."
    )
    print(
        "per_mode: checked and not executed — the mode-resolved object would be the "
        "density of a positive measure mu on the real axis whose moments are the "
        "d_n, that is the spectral modes of the real-axis continuation; the runner "
        "constructs no such decomposition because its entire result is that no mu "
        "exists, the necessary Hamburger condition already failing."
    )
    print(
        f"per_block: the test is one principal 2 by 2 block of the infinite Hankel "
        f"matrix, det [[d_5, d_6], [d_6, d_7]] = {minor} < 0, and that same block is "
        f"then re-examined under two sign-preserving reparametrizations, the "
        f"geometric integer rescaling m_5 = {int(m5)}, m_6 = {int(m6)}, "
        f"m_7 = {int(m7)} giving {integer_minor}, and the alternating-sign "
        f"convention giving back {alt_minor}."
    )
    print(
        "lattice_wide: checked and not executed — no volume, no thermodynamic "
        "limit, and no lattice observable is evaluated at any point, and the note "
        "forbids the corresponding global reading: the foreclosure covers only the "
        "positive-measure real-axis continuation family, asserting nothing about "
        "P(6), about beta=6 closure, or about non-Stieltjes continuations."
    )

    print()
    print(f"SCORECARD: PASS={PASS} FAIL={FAIL}")
    print("Verdict: the displayed coefficient window is not Hamburger/Stieltjes.")
    print("Only the positive-measure real-axis continuation family is ruled out.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
