#!/usr/bin/env python3
"""J:derive:static-law-in-the-hull:a2 (worker w-macbookpro90c72-j67ba).

Independent of a1 (Holder proof) and a3 (2x3/cube brute): C4, all 24 orders,
separator f=1[all +x]. If Z < D_sigma for every order then static all-+x mass
strictly exceeds every sequential formation mass, so static is not in the hull.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

FAILS: list[str] = []
OKS: list[str] = []
M = range(6)


def check(name: str, cond: bool, detail: str = "") -> None:
    if cond:
        OKS.append(name)
        print(f"CHECKED {name}" + (f": {detail}" if detail else ""))
    else:
        FAILS.append(name)
        print(f"FAIL {name}" + (f": {detail}" if detail else ""))


def Nk(k, p, q, r):
    if k == 0:
        return F(6)
    return p**k + q**k + 4 * r**k


def W(a, b, p, q, r):
    if a == b:
        return p
    if a == (b ^ 1):
        return q
    return r


def main():
    nei = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}
    for p, q, r in ((F(3), F(1), F(2)), (F(5), F(2), F(4)), (F(7), F(3), F(5))):
        Z = F(0)
        for cfg in itertools.product(M, repeat=4):
            w = W(cfg[0], cfg[1], p, q, r) * W(cfg[1], cfg[2], p, q, r)
            w *= W(cfg[2], cfg[3], p, q, r) * W(cfg[3], cfg[0], p, q, r)
            Z += w
        wall = p**4
        Pst = wall / Z
        Ds = []
        for perm in itertools.permutations(range(4)):
            seen = set()
            D = F(1)
            ks = []
            for v in perm:
                k = sum(1 for u in nei[v] if u in seen)
                ks.append(k)
                D *= Nk(k, p, q, r)
                seen.add(v)
            Ds.append(D)
            Pf = wall / D
            check(f"E1.Pform-lt-Pstat-{p}-{perm}", Pf < Pst)
        Dmin = min(Ds)
        Dmax = max(Ds)
        print(f"p={p}: Z={Z} Dmin={Dmin} Dmax={Dmax} Z<Dmin={Z < Dmin} Pst={Pst}")
        check(f"E2.Z-lt-Dmin-{p}", Z < Dmin, f"Z={Z} Dmin={Dmin} margin={Dmin - Z}")
        check(f"E2.24-orders-{p}", len(Ds) == 24)

    # path-of-3 (tree): Z should equal D for the unique-up-to-ends formation
    # sites 0-1-2, edges 01,12. Orders with 1 last have k=(0,0,2) wait
    # On a path the static law IS a formation law (block 01 / forest).
    # Order 0,1,2: k0=0, k1=1 (sees 0), k2=1 (sees 1). D=6 N1 N1
    # Z_path = sum_{s0,s1,s2} W(s0,s1)W(s1,s2)
    p, q, r = F(3), F(1), F(2)
    Zp = F(0)
    for cfg in itertools.product(M, repeat=3):
        Zp += W(cfg[0], cfg[1], p, q, r) * W(cfg[1], cfg[2], p, q, r)
    Dpath = Nk(0, p, q, r) * Nk(1, p, q, r) * Nk(1, p, q, r)
    print("E3.path3 Z", Zp, "D", Dpath, "equal", Zp == Dpath)
    check("E3.path3-Z-eq-D", Zp == Dpath)

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        "HIT: PARTIAL: on C4 the all-+x coordinate separates static from every "
        "sequential formation law at (3,1,2), (5,2,4), (7,3,5): Z < D_sigma for all "
        "24 orders so P_static(all +x)=p^4/Z > p^4/D_sigma=P_sigma. Path-of-3 (a tree) "
        "has Z=D. Separator f=1[all +x]. Independent of a1 Holder writeup and a3 2x3/cube."
    )
    print(
        "SUMMARY: PARTIAL C4 static law is outside the convex hull of sequential "
        "formation laws at three rational weights (all-+x separator; Z<D_sigma for "
        "all 24 orders); path-of-3 has Z=D"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
