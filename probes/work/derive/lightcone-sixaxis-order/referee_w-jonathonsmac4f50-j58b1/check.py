#!/usr/bin/env python3
"""Referee of J:derive:lightcone-sixaxis-order:a1 (author w-macbookpro90c72-jb723, grok-4.6); referee w-jonathonsmac4f50-j58b1
(claude-opus-5). Independent code (exact integers and Fractions); nothing from the author's check.py. Disclosure: this referee's model
family refereed attempts a2 and a3 of this problem (grok).

Z(s_1..s_7) = sum_u prod_i W(u, s_i) over the six axes u, W = p (same), q (antipodal), r (orthogonal), (p,q,r) = (3,1,2); the other five
stencil sites aligned at +z where not varied. Mixed differences of log Z over a set of sites, each switching between +z and a second value,
are products of Z^{+-1}; a pair interaction contributes to order-two differences only.

Y1  step 2's cross-ratio: Z(+,+) Z(-,-)/(Z(+,-) Z(-,+)) = (p^7+q^7+4r^7)(p^5q^2+p^2q^5+4r^7)/(p^6q+pq^6+4r^7)^2 = 128925/96721 != 1 at (3,1,2)
Y2  what it shows: a coupling between the two opposite stencil sites (distance 2), so pi is not the nearest-neighbour pair law
    exp(sum_<xy> log W); a distance-2 pair term alone would give the same cross-ratio, so 'not pairwise' needs a higher difference
Y3  the third-order mixed difference in three sites (+z <-> -z) is Z0 Z2^3/(Z1^3 Z3) = 940662585/932487161 != 1: a genuine three-body term,
    so log Z is not a sum of pair terms
Y4  a genuine seven-body term: the seventh-order mixed difference vanishes in the +-z sector by the symmetry Z_k = Z_{7-k}, but with sites
    1-3 switching +z <-> -z and 4-7 switching +z <-> +x it is 1.02646 != 1 (exact rational)
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as F
from math import comb

fails = []


def check(name, ok, msg):
    print(("PASS " if ok else "FAIL ") + name + ": " + msg)
    if not ok:
        fails.append(name)


M = range(6)
p, q, r = 3, 1, 2
W = [[p if a == b else (q if b == (a ^ 1) else r) for b in M] for a in M]
PZ, MZ, PX = 4, 5, 0


def Z(t):
    tot = 0
    for u in M:
        pr = 1
        for a in t:
            pr *= W[u][a]
        tot += pr
    return tot


def mixed(alts, base=PZ):
    num = den = 1
    for bits in itertools.product((0, 1), repeat=len(alts)):
        t = [alts[i] if bits[i] else base for i in range(len(alts))] + [base] * (7 - len(alts))
        if sum(bits) % 2 == 0:
            num *= Z(t)
        else:
            den *= Z(t)
    return F(num, den)


def main():
    cr = mixed([MZ, MZ])
    formula = F((p ** 7 + q ** 7 + 4 * r ** 7) * (p ** 5 * q ** 2 + p ** 2 * q ** 5 + 4 * r ** 7), (p ** 6 * q + p * q ** 6 + 4 * r ** 7) ** 2)
    check("Y1", cr == formula == F(128925, 96721), f"cross-ratio = {cr} = {float(cr):.5f}, the attempt's closed form")

    # a pure distance-2 pair term f(sA, sB) reproduces any cross-ratio: log-cross-ratio = f(-,-) - f(+,-) - f(-,+) + f(+,+)
    import math
    f = {("+", "+"): 0.0, ("+", "-"): 0.0, ("-", "+"): 0.0, ("-", "-"): math.log(float(cr))}
    pair_cr = math.exp(f[("-", "-")] - f[("+", "-")] - f[("-", "+")] + f[("+", "+")])
    check("Y2", abs(pair_cr - float(cr)) < 1e-12, "a single pair term between the two opposite sites gives the same cross-ratio: the test "
          "separates pi from the nearest-neighbour pair law (those sites are not neighbours), not from pairwise interactions in general")

    d3 = mixed([MZ, MZ, MZ])
    Zk = [Z([MZ] * k + [PZ] * (7 - k)) for k in range(8)]
    ok3 = d3 != 1 and d3 == F(Zk[0] * Zk[2] ** 3, Zk[1] ** 3 * Zk[3])
    check("Y3", ok3, f"third-order mixed difference Z0 Z2^3/(Z1^3 Z3) = {d3} = {float(d3):.6f} != 1: a genuine three-body term")

    sym = all(Zk[k] == Zk[7 - k] for k in range(8))
    zero7 = mixed([MZ] * 7) == 1
    d7 = mixed([MZ, MZ, MZ, PX, PX, PX, PX])
    check("Y4", sym and zero7 and d7 != 1, f"+-z sector: Z_k = Z_(7-k) ({sym}) so the seventh difference is 1 ({zero7}); mixed switches (-z x3, "
          f"+x x4): {float(d7):.5f} != 1 - a genuine seven-body term")

    if fails:
        print("SUMMARY: fails at a checked step (see FAIL lines)")
        return 1
    print("HIT: confirmed - lightcone-sixaxis-order a1: pi's interaction log Z_x is not the nearest-neighbour pair law (cross-ratio of the two "
          "opposite stencil sites (p^7+q^7+4r^7)(p^5q^2+p^2q^5+4r^7)/(p^6q+pq^6+4r^7)^2 = 128925/96721 at (3,1,2)), and it is genuinely "
          "many-body: the third-order mixed difference is 940662585/932487161 and a seventh-order one is 1.0265, both != 1. Correction: the "
          "attempt's cross-ratio alone shows only a distance-2 coupling (a pair term would reproduce it); 'not pairwise' and '7-body' need "
          "the higher differences checked here, and in the +-z sector the odd full-order differences vanish by symmetry")
    print("SUMMARY: confirmed with a corrected argument for 'not pairwise' and '7-body'; block 17's pair RP does not transfer, as stated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
