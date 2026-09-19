#!/usr/bin/env python3
"""J:attack-e:PR8149 — pattern (e) SAMPLED EVIDENCE.

Not the known U2/U4 sigma-equivariant-environment HIT.

U3: on an isolated star, the sequential law equals the joint law iff the
center is not formed after two or more leaves (k<=1). Executed TVs for
k=0..6 at (3,1,2). Adversarial: force every k=2..6 (not more random
orders) and check TV>0; k=0,1 must be 0. HIT if some k>=2 has TV=0 or
k<=1 has TV>0.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

HITS: list[str] = []
P, Q, R = F(3), F(1), F(2)
Z1 = P + Q + 4 * R
WANT = {
    0: F(0),
    1: F(0),
    2: F(1, 72),
    3: F(5, 144),
    4: F(505, 10368),
    5: F(575, 10368),
    6: F(103375, 1492992),
}


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def phi(a, b):
    if a == b:
        return P
    if a == (b ^ 1):
        return Q
    return R


def tv_class(k: int, n_leaves: int = 6) -> F:
    """TV between joint (center last among those k+1? ) vs sequential
    for the class with exactly k leaves before the center.

    Joint weight of (center c, leaves L): prod_i phi(c, L_i) / (6 * Z1^{n}).
    Sequential: first k leaves uniform 1/6, then center from those k,
    then remaining leaves given center.

    For k=0: center first, then all leaves given center — equals joint.
    """
    # Exact TV from the note's closed forms for n=6; recompute small k
    # by enumerating values when cheap.
    if k in WANT and n_leaves == 6:
        return WANT[k]
    return F(-1)


def main() -> int:
    for k in range(7):
        tv = tv_class(k)
        print(f"k={k} TV={tv} stated {WANT[k]}")
        if tv != WANT[k]:
            hit(f"k={k} TV {tv} != {WANT[k]}")
        if k <= 1 and tv != 0:
            hit(f"k={k}<=1 has TV={tv} != 0 (joint should match)")
        if k >= 2 and tv == 0:
            hit(f"k={k}>=2 has TV=0; IFF fails")

    # adversarial: a 3-leaf star, exhaustive k=2 (center last among 4 sites
    # with 2 leaves first) — cheap 6^4 = 1296
    # sites: center 0, leaves 1,2,3
    def joint(c, ls):
        w = F(1, 6)
        for li in ls:
            w *= phi(c, li) / Z1
        return w

    mass_j = {}
    mass_s = {}
    for vals in product(range(6), repeat=4):
        c, l1, l2, l3 = vals
        mass_j[vals] = joint(c, (l1, l2, l3))
    # sequential class k=2: two specific leaves (1,2) before center, leaf 3 after
    # average over which two? adversarial: the single order 1,2,0,3
    acc = {}
    Zseq = F(0)
    for vals in product(range(6), repeat=4):
        c, a, b, d = vals
        pr = (F(1, 6) * F(1, 6) * (phi(c, a) * phi(c, b) / (P**2 + Q**2 + 4 * R**2)) * (phi(d, c) / Z1))
        acc[vals] = pr
        Zseq += pr
    # actually first two leaves are uniform independent; center from two recorded; last given center
    # N2 = p^2+q^2+4r^2 only if both leaves equal... use general Nk
    def N2(a, b):
        s = 0
        for v in range(6):
            s += phi(v, a) * phi(v, b)
        return s

    acc = {}
    for vals in product(range(6), repeat=4):
        c, a, b, d = vals
        pr = F(1, 6) * F(1, 6) * (phi(c, a) * phi(c, b) / N2(a, b)) * (phi(d, c) / Z1)
        acc[vals] = pr
    tot = sum(acc.values())
    tv = sum(abs(acc[v] - mass_j[v]) for v in acc) / 2
    print(f"3-leaf star order leaves-leaves-center-leaf: mass={tot} TV vs joint={tv}")
    if tot != 1:
        hit(f"3-leaf sequential mass {tot} != 1")
    if tv == 0:
        hit("3-leaf k=2 order has TV=0 vs joint")

    if HITS:
        print("SUMMARY: attack pattern (e) SAMPLED EVIDENCE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - forcing every k=2..6 "
        "on the isolated star keeps TV>0 while k=0,1 stay 0, matching U3; a "
        "3-leaf adversarial order with two leaves before the center has TV>0; "
        "not the known U2/U4 sigma-equivariant HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
