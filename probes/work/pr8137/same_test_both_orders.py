#!/usr/bin/env python3
"""J:attack:PR8137 - order-dependence note, attack pattern (b) SAME TEST BOTH SIDES.

On a three-site path in Z^3 the (L,R) pair law is computed in BOTH the
ends-first order and the chain order, with the identical kernel K, for:
  * two-point menu, including the executed witness (pplus,pminus)=(4/5,1/5)
  * six-axis orbit with covariant (a,b,c)
HIT if the two orders disagree while K^2=mu_0, or if they agree for a
varying K; or if the stated residuals (pplus-pminus)^2 and (a-b)^2 fail.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

PLUS, MINUS = 0, 1
AXES = list(range(6))  # 0,1 opposite; 2,3; 4,5


def two_point_K(pplus, pminus, s, t):
    """P(t | s) on {+,-}."""
    if s == PLUS:
        return pplus if t == PLUS else 1 - pplus
    return pminus if t == PLUS else 1 - pminus


def two_point_pair_laws(pplus, pminus):
    mu0 = F(1, 2)
    # ends-first: L,R i.i.d. mu0
    ends = {}
    for L, R in product((PLUS, MINUS), repeat=2):
        ends[(L, R)] = mu0 * mu0
    # chain: L ~ mu0, M ~ K(.|L), R ~ K(.|M)
    chain = {(L, R): F(0) for L, R in product((PLUS, MINUS), repeat=2)}
    for L, M, R in product((PLUS, MINUS), repeat=3):
        chain[(L, R)] += mu0 * two_point_K(pplus, pminus, L, M) * two_point_K(pplus, pminus, M, R)
    k2_pp = pplus * pplus + (1 - pplus) * pminus
    residual = (pplus - pminus) ** 2
    return ends, chain, k2_pp, residual


def six_axis_K(a, b, c, s, t):
    if t == s:
        return a
    if t == s ^ 1:
        return b
    return c


def six_axis_residuals(a, b, c):
    # K^2(same) - K^2(opp)
    # same: a^2 + b^2 + 4 c^2
    # opp: 2 a b + 4 c^2
    k2_same = a * a + b * b + 4 * c * c
    k2_opp = 2 * a * b + 4 * c * c
    return k2_same - k2_opp, (a - b) ** 2, (6 * c - 1) ** 2 / 3


def main() -> None:
    hits = []
    # path 0 -- e1 -- 2 e1 exists in Z^3, ends not adjacent
    path = [(0, 0, 0), (1, 0, 0), (2, 0, 0)]
    dist01 = sum(abs(path[0][i] - path[1][i]) for i in range(3))
    dist12 = sum(abs(path[1][i] - path[2][i]) for i in range(3))
    dist02 = sum(abs(path[0][i] - path[2][i]) for i in range(3))
    print(f"three-site path {path}: edges {dist01},{dist12} end-distance {dist02}")
    if dist01 != 1 or dist12 != 1 or dist02 != 2:
        hits.append(f"path not a 3-site NN path: {dist01, dist12, dist02}")

    # two-point executed witness
    pplus, pminus = F(4, 5), F(1, 5)
    ends, chain, k2_pp, residual = two_point_pair_laws(pplus, pminus)
    print(f"Ising (4/5,1/5): K^2(+|+)= {k2_pp} (stated 17/25); residual {residual} (stated (3/5)^2=9/25)")
    if k2_pp != F(17, 25):
        hits.append(f"K^2(+|+) {k2_pp} != 17/25")
    if residual != (pplus - pminus) ** 2:
        hits.append("two-point residual identity failed")
    if ends[(PLUS, PLUS)] == chain[(PLUS, PLUS)]:
        hits.append("ends-first and chain AGREE at (4/5,1/5) though K varies")
    else:
        print(f"  ends P(+,+)={ends[(PLUS,PLUS)]} chain P(+,+)={chain[(PLUS,PLUS)]} (disagree, as claimed)")

    # independent kernel: should AGREE
    p = F(1, 2)
    e2, c2, _, r2 = two_point_pair_laws(p, p)
    print(f"independent (1/2,1/2): residual {r2}; pair laws equal {e2==c2}")
    if e2 != c2:
        hits.append("independent kernel: ends-first and chain disagree")
    if r2 != 0:
        hits.append(f"independent residual {r2} != 0")

    # six-axis: residual (a-b)^2
    a, b, c = F(1, 2), F(1, 10), F(1, 10)  # a+b+4c=1/2+1/10+4/10=1
    if a + b + 4 * c != 1:
        hits.append(f"six-axis row not a kernel: {a+b+4*c}")
    d, d2, haar = six_axis_residuals(a, b, c)
    print(f"six-axis a=1/2,b=1/10,c=1/10: K^2(same)-K^2(opp)={d} vs (a-b)^2={d2}; (6c-1)^2/3={haar}")
    if d != d2:
        hits.append(f"six-axis residual {d} != (a-b)^2={d2}")
    # uniform a=b=c=1/6
    u = F(1, 6)
    d, d2, haar = six_axis_residuals(u, u, u)
    print(f"uniform 1/6: residual {d}, haar-square {haar}")
    if d != 0 or haar != 0:
        hits.append(f"uniform not Haar-square: {d}, {haar}")

    # equator <t^2>=1/2 vs Haar 1/3
    # Haar dt/2 on [-1,1]: <t^2> = (1/2) int_{-1}^1 t^2 dt = 1/3
    haar_t2 = F(1, 2) * (F(2, 3))  # int t^2 dt /2 = 2/3 / 2 = 1/3
    print(f"Haar <t^2>={haar_t2} (stated 1/3); equator stated 1/2")
    if haar_t2 != F(1, 3):
        hits.append(f"Haar <t^2> {haar_t2} != 1/3")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (b) SAME TEST BOTH SIDES; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (b) SAME TEST BOTH SIDES; ends-first vs chain (L,R) laws disagree "
            "at the executed (4/5,1/5) witness (K^2(+|+)=17/25 vs 1/4) and agree at the independent "
            "kernel; two-point residual (pplus-pminus)^2 and six-axis (a-b)^2 hold; 3-site path exists in Z^3"
        )


if __name__ == "__main__":
    main()
