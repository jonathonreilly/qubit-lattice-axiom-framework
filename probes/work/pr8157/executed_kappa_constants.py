#!/usr/bin/env python3
"""J:attack:PR8157 - block 23, attack pattern (c) EXECUTED NUMBERS.

Recompute kappa(beta), gamma=min(1,5/(256 beta)), the meeting value 1/2 at
beta=5/256, 18 beta gamma^2 (8/5)=9/16, cosh 1 <= 8/5, and the (cosh t-1)
coefficient ratios 2/((2k)(2k-1)) against the control.

HIT if a stated executed constant disagrees.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import cosh


def kappa(beta: F) -> F:
    thresh = F(5, 256)
    if beta >= thresh:
        return F(5, 1) / (F(512) * beta)
    return 1 - F(128) * beta / 5


def gamma(beta: F) -> F:
    return min(F(1), F(5, 1) / (F(256) * beta))


def main() -> None:
    hits = []
    thresh = F(5, 256)
    k_hi = kappa(thresh)
    k_lo = 1 - F(128) * thresh / 5
    print(f"beta=5/256: kappa from large-beta formula {k_hi}; from small-beta {k_lo}")
    if k_hi != F(1, 2) or k_lo != F(1, 2):
        hits.append(f"kappa at 5/256 is {k_hi}, {k_lo} not 1/2")

    g = gamma(thresh)
    print(f"gamma at 5/256: {g} (stated 1)")
    if g != 1:
        hits.append(f"gamma(5/256)={g} != 1")

    # 18 beta gamma^2 (8/5) at the meeting point
    val = 18 * thresh * g * g * F(8, 5)
    print(f"18 beta gamma^2 (8/5) at 5/256 = {val} (stated 9/16)")
    if val != F(9, 16):
        hits.append(f"18 beta gamma^2 (8/5)={val} != 9/16")

    c1 = cosh(1)
    print(f"cosh(1)={c1:.6f} <= 8/5={1.6}: {c1 <= 1.6}")
    if c1 > 8 / 5:
        hits.append(f"cosh(1)={c1} > 8/5")

    # ratios 2/((2k)(2k-1)) for k=1..9
    stated = [
        F(1),
        F(1, 6),
        F(1, 15),
        F(1, 28),
        F(1, 45),
        F(1, 66),
        F(1, 91),
        F(1, 120),
        F(1, 153),
    ]
    for k, st in zip(range(1, 10), stated):
        got = F(2, (2 * k) * (2 * k - 1))
        print(f"k={k}: 2/((2k)(2k-1))={got} stated {st}")
        if got != st:
            hits.append(f"ratio k={k} {got} != {st}")

    # large-beta kappa = 5/(512 beta); at beta=1
    print(f"kappa(1)={kappa(F(1))} = 5/512")
    if kappa(F(1)) != F(5, 512):
        hits.append(f"kappa(1)={kappa(F(1))} != 5/512")
    print(f"kappa(5/512)={kappa(F(5, 512))} (small-beta branch)")
    if kappa(F(5, 512)) != 1 - F(128) * F(5, 512) / 5:
        hits.append("small-beta kappa formula failed")

    # 3/2 e^{9/16} is just a named constant; e^{9/16} > 1
    from math import exp

    bound = 1.5 * exp(9 / 16)
    print(f"(3/2) e^{{9/16}} = {bound:.6f}")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (c) EXECUTED NUMBERS; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (c) EXECUTED NUMBERS; kappa pieces meet at 1/2 at beta=5/256, "
            "18 beta gamma^2 (8/5)=9/16, cosh 1 <= 8/5, and (cosh t-1) ratios 2/((2k)(2k-1)) all match"
        )


if __name__ == "__main__":
    main()
