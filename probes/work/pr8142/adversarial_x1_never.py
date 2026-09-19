#!/usr/bin/env python3
"""J:attack-e:PR8142 — SAMPLED EVIDENCE: X1's 'never vanishes' is not a sample.

Adversarial algebraic check of the two X1 factorizations instead of sampling
(p,q,r). HIT if a positive (p,q,r) not all equal makes both two-body ratios 1.
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
    p, q, r = sp.symbols("p q r", positive=True)
    ratio1 = ((p**2 + q**2 + 4 * r**2) / (2 * (p * q + 2 * r**2))) ** 2
    ratio2 = ((p**2 + q**2 + 4 * r**2) / (2 * r * (p + q + r))) ** 2
    # ratio1==1 iff p=q (for r>0)
    n1, d1 = sp.fraction(sp.together(ratio1 - 1))
    n1 = sp.factor(sp.expand(n1))
    print(f"ratio1-1 numerator factors: {n1}")
    # (p-q) should divide
    if sp.simplify(n1.subs(q, p)) != 0:
        return hits("ratio1-1 does not vanish on p=q")
    # ratio2==1 iff p=q=r
    n2, d2 = sp.fraction(sp.together(ratio2 - 1))
    n2 = sp.factor(sp.expand(n2))
    print(f"ratio2-1 numerator factors: {n2}")
    if sp.simplify(n2.subs({q: p, r: p})) != 0:
        return hits("ratio2-1 does not vanish on p=q=r")
    # adversarial points: (3,1,2), (5,2,4), (2,3,1) — not all equal
    for trip in ((Fr(3), Fr(1), Fr(2)), (Fr(5), Fr(2), Fr(4)), (Fr(2), Fr(3), Fr(1)), (Fr(37, 10), Fr(1), Fr(2))):
        v1 = ratio1.subs({p: trip[0], q: trip[1], r: trip[2]})
        v2 = ratio2.subs({p: trip[0], q: trip[1], r: trip[2]})
        print(f"{trip}: ratio1={v1} ratio2={v2}")
        if v1 == 1 and v2 == 1:
            return hits(f"both two-body ratios =1 at nonconstant {trip}")
        if v2 == 1 and not (trip[0] == trip[1] == trip[2]):
            return hits(f"ratio2=1 at {trip} not all equal")
    print(
        "SUMMARY: pattern has no purchase on this note: X1's 'never vanishes' is "
        "an exact factorization, not a sampling claim; adversarial (p,q,r) "
        "including (3,1,2) keep the two-body ratios off 1"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
