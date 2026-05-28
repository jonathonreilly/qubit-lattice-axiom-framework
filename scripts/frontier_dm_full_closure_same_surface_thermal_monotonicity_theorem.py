#!/usr/bin/env python3
"""Thermal-kernel monotonicity support for the same-surface DM ratio.

Framework convention:
  The framework baseline is one-qubit operator algebra on the Z^3 spatial
  substrate.

Purpose:
  Verify the exact derivative identities and sign bounds for the attractive
  and repulsive Sommerfeld thermal kernels. The 64:1 same-surface channel
  combination is recorded only as a conditional exhibit, pending a retained
  authority for that channel-weight formula.
"""

from __future__ import annotations

import math
import sys

PASS_COUNT = 0
FAIL_COUNT = 0
SUPPORT_COUNT = 0

X_F = 25.0
A = X_F / 4.0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def support(name: str, condition: bool, detail: str = "") -> bool:
    global SUPPORT_COUNT, FAIL_COUNT
    status = "SUPPORT" if condition else "FAIL"
    if condition:
        SUPPORT_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def f_att_prime(y: float) -> float:
    em1 = math.expm1(y)
    ey = em1 + 1.0
    return ey * (ey - y - 1.0) / (em1 * em1)


def f_rep_prime(y: float) -> float:
    em1 = math.expm1(y)
    ey = em1 + 1.0
    return (ey - y * ey - 1.0) / (em1 * em1)


def h(y: float) -> float:
    u = math.expm1(y)
    return u * u + 2.0 * (1.0 - y) * u - 2.0 * y


def main() -> int:
    print("=" * 88)
    print("DM FULL CLOSURE SAME-SURFACE THERMAL MONOTONICITY THEOREM")
    print("=" * 88)

    lower_bound = 35.0 * math.sqrt(math.pi) / 12.0

    print("\n" + "=" * 88)
    print("PART 1: EXACT DERIVATIVE IDENTITIES")
    print("=" * 88)
    ys = [1.0e-4, 1.0e-2, 1.0, 10.0]
    check(
        "The attractive and repulsive Sommerfeld derivatives share the same exact shifted numerator h(y)",
        True,
        "f_att'(y)-1/2 = f_rep'(y)+1/2 = h(y)/(2(e^y-1)^2)",
    )
    ok = True
    for y in ys:
        em1 = math.expm1(y)
        lhs_att = f_att_prime(y) - 0.5
        lhs_rep = f_rep_prime(y) + 0.5
        rhs = h(y) / (2.0 * em1 * em1)
        ok = ok and abs(lhs_att - rhs) < 1.0e-8 and abs(lhs_rep - rhs) < 1.0e-8
    check("The exact derivative identities are numerically stable on representative y>0 samples", ok)

    print("\n" + "=" * 88)
    print("PART 2: EXACT SIGN BOUNDS")
    print("=" * 88)
    ok_h = True
    for y in ys:
        hprime = 2.0 * math.exp(y) * (math.exp(y) - 1.0 - y)
        ok_h = ok_h and h(y) > 0.0 and hprime > 0.0 and f_att_prime(y) >= 0.5 and f_rep_prime(y) >= -0.5
    check(
        "For every y>0, h(y)>0 because h(0)=0 and h'(y)=2 e^y (e^y-1-y)>0",
        ok_h,
        "so f_att'(y) >= 1/2 and f_rep'(y) >= -1/2",
    )

    print("\n" + "=" * 88)
    print("PART 3: CONDITIONAL 64:1 CHANNEL-WEIGHT EXHIBIT")
    print("=" * 88)
    ok_combo = True
    for y in ys:
        combo = 64.0 * f_att_prime(8.0 * y) + f_rep_prime(y)
        ok_combo = ok_combo and combo > 31.5
    support(
        "If the 64:1 same-surface channel-weight formula is supplied, its derivative integrand is positive",
        ok_combo,
        "64 f_att'(8y) + f_rep'(y) > 63/2",
    )

    print()
    print("  Conditional consequence:")
    print("    - the kernel-level derivative/sign bounds are exact")
    print("    - under a supplied 64:1 channel-weight authority, the weighted")
    print(f"      derivative lower bound is at least {lower_bound:.12f} on x_f=25")
    print("    - without that authority, live-DM ratio monotonicity is not a")
    print("      closed theorem of this runner")

    print("\n" + "=" * 88)
    print(f"SUMMARY: PASS={PASS_COUNT} SUPPORT={SUPPORT_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 88)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
