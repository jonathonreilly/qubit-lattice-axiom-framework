#!/usr/bin/env python3
"""Exact runner for the Koide Q = 2/3 Frobenius-extremum bridge.

The paired note checks only the bounded algebraic bridge:

    C_3 circulant eigenvalue identities
    + scoped equal-weight Frobenius extremum a^2 = 2 |b|^2
    => Q_alg(lambda) = 2/3.

It does not derive a charged-lepton readout, a phase value, or a physical
mass-square-root identification.
"""

from __future__ import annotations

from fractions import Fraction


PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f" ({detail})"
    print(msg)
    return cond


def q_alg_from_squares(a_squared: Fraction, b_abs_squared: Fraction) -> Fraction:
    """Q_alg(lambda) from retained C_3 Fourier identities."""
    numerator = 3 * a_squared + 6 * b_abs_squared
    denominator = 9 * a_squared
    return numerator / denominator


def main() -> int:
    for b_abs_squared in (Fraction(1), Fraction(2), Fraction(5), Fraction(9, 4)):
        a_squared = 2 * b_abs_squared
        ratio = q_alg_from_squares(a_squared, b_abs_squared)
        check(
            "at equal-weight Frobenius extremum, Q_alg(lambda) = 2/3",
            ratio == Fraction(2, 3),
            f"a^2 = {a_squared}; |b|^2 = {b_abs_squared}; Q = {ratio}",
        )

    controls = (
        (Fraction(1), Fraction(1), Fraction(1)),
        (Fraction(4), Fraction(1), Fraction(1, 2)),
        (Fraction(1), Fraction(2), Fraction(5, 3)),
    )
    for a_squared, b_abs_squared, expected in controls:
        ratio = q_alg_from_squares(a_squared, b_abs_squared)
        check(
            "non-extremal control does not masquerade as the 2/3 bridge",
            ratio == expected and ratio != Fraction(2, 3),
            f"a^2 = {a_squared}; |b|^2 = {b_abs_squared}; Q = {ratio}",
        )

    # At delta = 0, lambda = (a + 2r, a - r, a - r). Under a^2 = 2r^2,
    # positivity reduces to sqrt(2) > 1.
    check(
        "positive chamber exists at delta = 0",
        Fraction(2) > Fraction(1),
        "lambda_min = (sqrt(2) - 1) |b| > 0",
    )

    # At a phase with one cosine equal to -1, one eigenvalue is a - 2r.
    # Under a^2 = 2r^2 this is negative because 2 > sqrt(2).
    check(
        "not every phase lies in the positive chamber",
        Fraction(4) > Fraction(2),
        "lambda_min = (sqrt(2) - 2) |b| < 0",
    )

    print(
        "INFO boundary: the global claim is the signed algebraic ratio; "
        "positive-vector Koide interpretation requires a separate positive "
        "spectrum/readout bridge."
    )
    print(f"SUMMARY: PASS = {PASS}, FAIL = {FAIL}")
    if FAIL:
        print("Koide Frobenius-extremum algebraic bridge failed.")
        return 1

    print("Koide Frobenius-extremum algebraic bridge passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
