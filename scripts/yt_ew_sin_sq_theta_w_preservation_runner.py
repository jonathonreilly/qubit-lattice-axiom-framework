#!/usr/bin/env python3
"""Sympy companion for YT_EW_SIN_SQ_THETA_W_PRESERVATION_BOUNDED_NOTE_2026-05-25.

Verifies symbolically that the multiplicative-universality K_EW(kappa_EW)
correction from `yt_ew_color_projection_theorem` cancels in the Weinberg
angle ratio sin^2(theta_W) = g_Y^2 / (g_Y^2 + g_2^2), making the ratio
invariant under any value of kappa_EW.
"""
from __future__ import annotations

import sys

try:
    from sympy import Rational, Symbol, simplify
except ImportError:
    print("FAIL: sympy required for exact algebra")
    sys.exit(1)


def main() -> int:
    g_Y = Symbol("g_Y", positive=True)
    g_2 = Symbol("g_2", positive=True)
    kappa_EW = Symbol("kappa_EW", real=True)

    # K_EW form from parent theorem at N_c = 3.
    K_EW = 1 / (Rational(8, 9) + kappa_EW / 9)

    sin_sq_before = g_Y**2 / (g_Y**2 + g_2**2)
    sin_sq_after = (K_EW * g_Y) ** 2 / ((K_EW * g_Y) ** 2 + (K_EW * g_2) ** 2)

    diff = simplify(sin_sq_after - sin_sq_before)
    universal = diff == 0

    # Sanity at kappa_EW = 0 (K_EW = 9/8) and at kappa_EW = 1 (K_EW = 1).
    at_zero = simplify(sin_sq_after.subs(kappa_EW, 0) - sin_sq_before) == 0
    at_one = simplify(sin_sq_after.subs(kappa_EW, 1) - sin_sq_before) == 0

    passed = universal and at_zero and at_one
    PASS = 1 if passed else 0
    FAIL = 0 if passed else 1

    print("Audit companion: sin^2(theta_W) preservation under K_EW")
    print(f"  symbolic diff = {diff}")
    print(f"  identity holds universally: {universal}")
    print(f"  identity at kappa_EW = 0 (K_EW = 9/8): {at_zero}")
    print(f"  identity at kappa_EW = 1 (K_EW = 1): {at_one}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if passed:
        print(
            "VERDICT: bounded proof-walk passes; sin^2(theta_W) is invariant "
            "under the multiplicative-universality K_EW(kappa_EW) correction."
        )
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
