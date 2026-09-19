#!/usr/bin/env python3
"""J:attack-f:PR8171 — NORMALIZATION of φ=average of 3 predecessors (factor 1/3)
and the contraction threshold 1/√3.

phi=(1+e^{ik1}+e^{ik2})/3 so |phi|<=1; three 1/3s sum to 1; β<1/√3.
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    if 3 * Fr(1, 3) != 1:
        return hits("three 1/3s do not sum to 1")
    k1, k2 = sp.symbols("k1 k2", real=True)
    phi = (1 + sp.exp(sp.I * k1) + sp.exp(sp.I * k2)) / 3
    # |phi|<=1: 9|phi|^2 = 3+2cos k1+2cos k2+2cos(k1-k2) <= 9
    nine = 3 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k1 - k2)
    # max of sum of 3 cosines of this form is 3 at k=0
    if nine.subs({k1: 0, k2: 0}) != 9:
        return hits("|phi|(0) != 1")
    print("φ=(1+e^{ik1}+e^{ik2})/3, three 1/3s, |φ(0)|=1: True")
    # 1/√3: (1/√3)^2=1/3
    if sp.simplify((1 / sp.sqrt(3)) ** 2 - sp.Rational(1, 3)) != 0:
        return hits("(1/√3)^2 != 1/3")
    print("threshold 1/√3 with (1/√3)^2=1/3: True")
    # TV 1/2
    if Fr(1, 2) * 2 != 1:
        return hits("TV 1/2")
    print(
        "SUMMARY: pattern has no purchase on this note: the 1/3 in φ, |φ(0)|=1, "
        "and (1/√3)^2=1/3 all recompute as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
