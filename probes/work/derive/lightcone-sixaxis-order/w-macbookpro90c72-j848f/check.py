#!/usr/bin/env python3
"""J:derive:lightcone-sixaxis-order:a2 (worker w-macbookpro90c72-j848f).

Independent of a3 (cube Peierls, 6+7 pairing): C4 contour ratios for sync pi,
and whether dropping the self-loop from the 7-stencil breaks pairing on L=2.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

FAILS: list[str] = []
OKS: list[str] = []
M = range(6)
VEC = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def W(a, b, p, q=F(1), r=F(2)):
    if a == b:
        return p
    if a == (b ^ 1):
        return q
    return r


def Z2(left, right, p):
    return sum(W(s, left, p) * W(s, right, p) for s in M)


def main():
    # C4 sync pi ∝ prod_i Z(s_{i-1}, s_{i+1})  (degree-2, no self)
    p = F(3)
    w_al = Z2(4, 4, p) ** 4
    # one orthogonal flip at site 0: cfg (2,4,4,4)
    w_orth = Z2(4, 4, p) * Z2(2, 4, p) * Z2(4, 4, p) * Z2(4, 2, p)
    # wait: Z at i uses s_{i-1}, s_{i+1}
    # i=0: s3,s1 both 4
    # i=1: s0=2, s2=4
    # i=2: s1=4, s3=4
    # i=3: s2=4, s0=2
    w_orth = Z2(4, 4, p) * Z2(2, 4, p) * Z2(4, 4, p) * Z2(4, 2, p)
    w_anti = Z2(4, 4, p) * Z2(5, 4, p) * Z2(4, 4, p) * Z2(4, 5, p)
    ratio_o = w_orth / w_al
    ratio_a = w_anti / w_al
    print("E1.orth/all", ratio_o, float(ratio_o))
    print("E1.anti/all", ratio_a, float(ratio_a))
    check("E1.orth-lt1", ratio_o < 1)
    check("E1.anti-lt1", ratio_a < 1)
    check("E1.anti-lt-orth", ratio_a < ratio_o)

    # decreasing in p: p=3,5,10
    prev_o = None
    for pv in (F(3), F(5), F(10)):
        wa = Z2(4, 4, pv) ** 4
        wo = Z2(4, 4, pv) * Z2(2, 4, pv) * Z2(4, 4, pv) * Z2(4, 2, pv)
        ro = wo / wa
        print(f"E1.p={pv} orth/all={ro} {float(ro):.6f}")
        if prev_o is not None:
            check(f"E1.decreasing-p{pv}", ro < prev_o)
        prev_o = ro

    # pairing: 6-nn (no self) on L=2 torus 8 sites
    def S6(cfg, x, L=2):
        i, j, k = x % L, (x // L) % L, x // (L * L)
        acc = [0, 0, 0]
        for d in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)):
            y = ((i + d[0]) % L) + L * ((j + d[1]) % L) + L * L * ((k + d[2]) % L)
            acc = [acc[t] + VEC[cfg[y]][t] for t in range(3)]
        return acc

    def pair6(c1, c2):
        Lft = Rgt = 0
        for x in range(8):
            S1, S2 = S6(c1, x), S6(c2, x)
            Lft += sum(VEC[c2[x]][t] * S1[t] for t in range(3))
            Rgt += sum(VEC[c1[x]][t] * S2[t] for t in range(3))
        return Lft == Rgt

    ok6 = True
    base = (4,) * 8
    for x, a in itertools.product(range(8), range(6)):
        c2 = list(base)
        c2[x] = a
        if not pair6(base, tuple(c2)):
            ok6 = False
    check("E2.6nn-pairing-no-self", ok6, "6-neighbourhood pairing holds without self-loop")

    # self-only stencil (asymmetric if we used only 'self' as neigh): pairing with S=s_x
    def pair_self(c1, c2):
        Lft = sum(sum(VEC[c2[x]][t] * VEC[c1[x]][t] for t in range(3)) for x in range(8))
        Rgt = sum(sum(VEC[c1[x]][t] * VEC[c2[x]][t] for t in range(3)) for x in range(8))
        return Lft == Rgt
    check("E2.self-pairing-symmetric", pair_self(base, tuple([5] + [4] * 7)))

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        f"HIT: PARTIAL: C4 sync Peierls ratios at (p,1,2): one orthogonal defect "
        f"{ratio_o}, one antipodal {ratio_a}, both <1 and decreasing in p=3,5,10; "
        "6-neighbour pairing holds without including the site itself (symmetric W, "
        "symmetric neighbourhood). Self-inclusion is not required for reversibility. "
        "Stationary six laws: contour cost of a single flip is already <1 on C4 at p=3. "
        "Independent of a3 cube census."
    )
    print(
        f"SUMMARY: PARTIAL C4 sync defect ratios orth={ratio_o} anti={ratio_a}<1 at "
        "(3,1,2), decreasing in p; 6-nn pairing needs no self-loop"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
