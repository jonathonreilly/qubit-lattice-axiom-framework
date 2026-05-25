#!/usr/bin/env python3
"""Narrow proof-walk runner for YT_EW_F_ADJ_FIERZ_FRACTION_BOUNDED_NOTE_2026-05-25.

Verifies the exact-rational-arithmetic half of yt_ew_color_projection_theorem:
F_adj = (N_c^2 - 1) / N_c^2 = 8/9 at N_c = 3.
"""

from sympy import Rational


def main() -> int:
    passed = 0
    failed = 0

    # Step 1: specialize the Fierz adjoint fraction at N_c = 3.
    N_c = 3
    F_adj = Rational(N_c**2 - 1, N_c**2)
    if F_adj == Rational(8, 9):
        passed += 1
    else:
        failed += 1
        print(f"FAIL: F_adj at N_c=3 expected 8/9, got {F_adj}")

    # Step 2: algebraic rearrangement (N_c^2 - 1)/N_c^2 = 1 - 1/N_c^2 at N_c = 3.
    if Rational(8, 9) == 1 - Rational(1, 9):
        passed += 1
    else:
        failed += 1
        print(f"FAIL: 8/9 != 1 - 1/9")

    print(f"TOTAL: PASS={passed} FAIL={failed}")
    if failed == 0:
        print(
            "VERDICT: bounded proof-walk passes; F_adj = (N_c^2 - 1)/N_c^2 = 8/9 "
            "at N_c = 3 is exact rational arithmetic from the cited Fierz "
            "channel-count."
        )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
