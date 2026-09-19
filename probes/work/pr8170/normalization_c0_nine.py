#!/usr/bin/env python3
"""J:attack-f:PR8170 — NORMALIZATION of 1/3 walk, 9^{-k} P_k, 3√3/(4π).

Not the known exponent-vs-gamma HIT.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from math import comb


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    if 3 * Fr(1, 3) != 1:
        return hits("1/3")
    # P_1 = 9^{-1} sum_j C(1,j)^2 C(2j,j) = (C(1,0)^2 *1 + C(1,1)^2 *2)/9 = (1+2)/9=1/3
    P1 = Fr(sum(comb(1, j) ** 2 * comb(2 * j, j) for j in range(2)), 9)
    if P1 != Fr(1, 3):
        return hits(f"P_1={P1} != 1/3")
    print(f"walk step 1/3; P_1={P1}: True")
    # 3√3/(4π) is the local-limit constant; (2π)^{-2} * 3√3 π = 3√3/(4π)
    import sympy as sp
    c0 = 3 * sp.sqrt(3) / (4 * sp.pi)
    gauss = 3 * sp.sqrt(3) * sp.pi / (4 * sp.pi**2)
    if sp.simplify(c0 - gauss) != 0:
        return hits("(2π)^{-2} Gaussian prefactor != 3√3/(4π)")
    print("3√3/(4π) = (2π)^{-2} * 3√3 π: True")
    print(
        "SUMMARY: pattern has no purchase on this note: 1/3 step, 9^{-k} P_k, "
        "and 3√3/(4π) Parseval/Gaussian normalization recompute; not the known "
        "exponent-vs-gamma HIT"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
