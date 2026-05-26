#!/usr/bin/env python3
"""Finite Maxwell-Boltzmann/Sommerfeld normalization certificate.

This runner verifies the bounded normalization formulas used by
DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md after the
note is narrowed to an explicit benchmark slice x_f = 25. It does not derive
freeze-out physics or the Sommerfeld factor itself.
"""

from __future__ import annotations

import math


X_F = 25.0
A = X_F / 4.0
ALPHA_EFF = 0.123
T_SAMPLE = 1.7


def integral_power(power: float, a: float = A) -> float:
    """Integral_0^inf v^power exp(-a v^2) dv."""
    return 0.5 * a ** (-(power + 1.0) / 2.0) * math.gamma((power + 1.0) / 2.0)


def normalized_moment(inv_power: int, a: float = A) -> float:
    denom = integral_power(2.0, a)
    numer = integral_power(2.0 - inv_power, a)
    return numer / denom


def sommerfeld_argument_from_v(alpha_eff: float, v_rel: float) -> float:
    return alpha_eff / v_rel


def sommerfeld_argument_from_t(alpha_eff: float, t: float, a: float = A) -> float:
    return alpha_eff * math.sqrt(a / t)


def check(label: str, ok: bool, detail: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'}: {label}: {detail}")
    if not ok:
        raise SystemExit(1)


def main() -> None:
    print("=" * 88)
    print("DM THERMAL AVERAGE / SOMMERFELD NORMALIZATION CERTIFICATE")
    print("=" * 88)
    print(f"x_f = {X_F:g}")
    print(f"a = x_f / 4 = {A:g}")
    print()

    denom = integral_power(2.0)
    expected_denom = math.sqrt(math.pi) / (4.0 * A ** 1.5)
    check(
        "MB denominator",
        math.isclose(denom, expected_denom, rel_tol=1e-14, abs_tol=1e-14),
        f"Integral v^2 exp(-a v^2) dv = {denom:.16g}",
    )

    inv_v = normalized_moment(1)
    expected_inv_v = 2.0 * math.sqrt(A) / math.sqrt(math.pi)
    check(
        "<1/v>",
        math.isclose(inv_v, expected_inv_v, rel_tol=1e-14, abs_tol=1e-14),
        f"{inv_v:.16g} = 2 sqrt(a)/sqrt(pi)",
    )

    inv_v2 = normalized_moment(2)
    expected_inv_v2 = 2.0 * A
    check(
        "<1/v^2>",
        math.isclose(inv_v2, expected_inv_v2, rel_tol=1e-14, abs_tol=1e-14),
        f"{inv_v2:.16g} = 2a",
    )

    check(
        "x_f=25 moments",
        math.isclose(inv_v, 5.0 / math.sqrt(math.pi), rel_tol=1e-14)
        and math.isclose(inv_v2, 25.0 / 2.0, rel_tol=1e-14),
        f"<1/v>={inv_v:.16g}, <1/v^2>={inv_v2:.16g}",
    )

    # Change of variables t = a v^2 gives
    # v = sqrt(t/a), dv = dt/(2 sqrt(a) sqrt(t)), and the normalized
    # weight factor is (2/sqrt(pi)) sqrt(t) exp(-t) dt.
    v_from_t = math.sqrt(T_SAMPLE / A)
    z_v = sommerfeld_argument_from_v(ALPHA_EFF, v_from_t)
    z_t = sommerfeld_argument_from_t(ALPHA_EFF, T_SAMPLE)
    check(
        "Sommerfeld argument normalization",
        math.isclose(z_v, z_t, rel_tol=1e-14, abs_tol=1e-14),
        f"alpha/v = {z_v:.16g} = alpha sqrt(a/t)",
    )

    gamma_3_2 = math.gamma(1.5)
    prefactor = 1.0 / gamma_3_2
    check(
        "thermal-average t-prefactor",
        math.isclose(prefactor, 2.0 / math.sqrt(math.pi), rel_tol=1e-14),
        f"1/Gamma(3/2) = {prefactor:.16g}",
    )

    print()
    print("BOUNDARY")
    print("  This certifies only the finite normalization algebra at the explicit")
    print("  benchmark slice x_f=25. It does not derive x_f, the MB distribution,")
    print("  or the Sommerfeld enhancement law from framework axioms.")


if __name__ == "__main__":
    main()
