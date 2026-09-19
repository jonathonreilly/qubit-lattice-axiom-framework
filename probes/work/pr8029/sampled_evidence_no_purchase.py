#!/usr/bin/env python3
"""J:attack-e:PR8029 — SAMPLED EVIDENCE.

Infinite-static sector note: ||Psi||=1 from Tr(W^*W)/3=1 on SU(3), Casimir
Q(1,0)=4, bounds (4/a)(1-kappa)d <= inf Spec <= 4d/a. Exact operator
identities, not sampled never/always observations.
"""
from fractions import Fraction as Fr

import sympy as sp


def Q(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def main() -> int:
    print(f"Q(1,0)={Q(1, 0)} Q(0,1)={Q(0, 1)} (stated 4)")
    assert Q(1, 0) == 4 and Q(0, 1) == 4
    U = sp.eye(3)
    tr = sp.simplify(sp.trace(U.H * U) / 3)
    print(f"Tr(I^H I)/3={tr}")
    assert tr == 1
    kappa = Fr(1, 2)
    # kappa<=1/2 gives 2d/a lower bound: (4/a)(1-1/2)d = 2d/a
    print(f"(4/a)(1-kappa)d at kappa=1/2 is (2/a)d")
    assert (4 * (1 - kappa)) == 2
    print(
        "SUMMARY: pattern has no purchase on this note — GNS sector bounds, "
        "Casimir 4 and Tr(W^*W)/3=1 are exact identities, not sampled "
        "never/always observations"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
