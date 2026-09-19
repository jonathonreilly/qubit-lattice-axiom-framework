#!/usr/bin/env python3
"""J:derive:re-recording:a2 (worker w-macbookpro90c72-je4a9).

Different route from a3 (36x36 edge matrices) and a4 (TV on C4): exact all-+x
masses of static vs sync on C4, 6^4 enumeration, (p,q,r)=(3,1,2).
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


def W(a, b, p=F(3), q=F(1), r=F(2)):
    if a == b:
        return p
    if a == (b ^ 1):
        return q
    return r


def Z_deg2(left, right, p=F(3), q=F(1), r=F(2)):
    return sum(W(s, left, p, q, r) * W(s, right, p, q, r) for s in M)


def main():
    p, q, r = F(3), F(1), F(2)
    Zst = F(0)
    Zsy = F(0)
    allplus_st = F(0)
    allplus_sy = F(0)
    n = 0
    for cfg in itertools.product(M, repeat=4):
        n += 1
        wst = W(cfg[0], cfg[1]) * W(cfg[1], cfg[2]) * W(cfg[2], cfg[3]) * W(cfg[3], cfg[0])
        wsy = (
            Z_deg2(cfg[3], cfg[1])
            * Z_deg2(cfg[0], cfg[2])
            * Z_deg2(cfg[1], cfg[3])
            * Z_deg2(cfg[2], cfg[0])
        )
        Zst += wst
        Zsy += wsy
        if cfg == (4, 4, 4, 4):
            allplus_st = wst
            allplus_sy = wsy
    check("E1.6^4", n == 6**4)
    Pst = allplus_st / Zst
    Psy = allplus_sy / Zsy
    print("E2.P_static(all +x)", Pst, float(Pst))
    print("E2.P_sync(all +x)", Psy, float(Psy))
    check("E2.differ", Pst != Psy)
    check("E2.both-pos", Pst > 0 and Psy > 0)
    # pairing on C4: sum s'_i (s_{i-1}+s_{i+1}) = sum s_i (s'_{i-1}+s'_{i+1})
    VEC = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

    def pair(c1, c2):
        L = R = 0
        for i in range(4):
            S1 = [VEC[c1[(i - 1) % 4]][t] + VEC[c1[(i + 1) % 4]][t] for t in range(3)]
            S2 = [VEC[c2[(i - 1) % 4]][t] + VEC[c2[(i + 1) % 4]][t] for t in range(3)]
            L += sum(VEC[c2[i]][t] * S1[t] for t in range(3))
            R += sum(VEC[c1[i]][t] * S2[t] for t in range(3))
        return L == R

    ok = True
    for c1 in itertools.product(M, repeat=4):
        c2 = tuple((c1[i] + 1) % 6 for i in range(4))
        if not pair(c1, c2):
            ok = False
    check("E3.C4-pairing-rotations", ok)

    print(f"CHECKS ok={len(OKS)} fail={len(FAILS)}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + FAILS[0])
        return 1
    print(
        f"HIT: PARTIAL: on C4 at (3,1,2), exact 6^4 enumeration: P_static(all +x)={Pst}, "
        f"P_sync(all +x)={Psy}, distinct; 6-neighbour pairing holds for all 1296 rotations. "
        "Async=static still (not re-enumerated; a3/a4). Transfer of uniqueness/kernel only "
        "to async. Route: all-+x masses, not full TV or 36x36 matrices."
    )
    print(
        f"SUMMARY: PARTIAL C4 all-+x masses static {Pst} vs sync {Psy} at (3,1,2); "
        "pairing exact; laws distinct"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
