#!/usr/bin/env python3
"""J:attack-g:PR8149 — brute-force U3 isolated-star class TVs at (3,1,2).

Note U3: seven classes by k = number of leaves before the center have TV
0, 0, 1/72, 5/144, 505/10368, 575/10368, 103375/1492992.
Not the known U2/U4 sigma-equivariant environment HIT.
"""
from __future__ import annotations

import sys
from fractions import Fraction as F
from itertools import product

p, q, r = F(3), F(1), F(2)
M = 6
Z1 = p + q + 4 * r  # 12
WANT = [F(0), F(0), F(1, 72), F(5, 144), F(505, 10368), F(575, 10368), F(103375, 1492992)]


def phi(a, b):
    if a == b:
        return p
    if a == (b ^ 1):
        return q
    return r


def prod_phi(c, ls):
    w = F(1)
    for li in ls:
        w *= phi(c, li)
    return w


def tv_class(k):
    acc = F(0)
    for vals in product(range(M), repeat=k + 1):
        c = vals[0]
        ls = vals[1:]
        wj = F(1, 6)
        for li in ls:
            wj *= phi(c, li) / Z1
        ws = F(1, 6) ** k
        num = prod_phi(c, ls)
        den = sum(prod_phi(cc, ls) for cc in range(M))
        ws *= num / den
        acc += abs(wj - ws)
    return acc / 2


def main():
    ok = True
    rows = []
    for k in range(7):
        tv = tv_class(k)
        match = tv == WANT[k]
        ok = ok and match
        rows.append(f"k={k}: {tv} want {WANT[k]} {'OK' if match else 'DIFF'}")
        print(f"class {k}: TV={tv} stated={WANT[k]} match={match}")
    if not ok:
        print("HIT: U3 isolated-star class TVs at (3,1,2) do not match the stated list")
        print("SUMMARY: HIT - U3 star TVs fail: " + "; ".join(rows))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note: U3's seven isolated-star class TVs "
        "at (3,1,2) match 0, 0, 1/72, 5/144, 505/10368, 575/10368, 103375/1492992 exactly "
        "(brute-force over 6^{k+1} centre+leading-leaf configs; remaining leaves share the "
        "same kernel given the centre). Not the known U2/U4 sigma-equivariant HIT"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
