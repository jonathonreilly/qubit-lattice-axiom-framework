#!/usr/bin/env python3
"""J:falsifier:PR8151 — T2 bond partition on extra even tori.

Not the known T3 chessboard-orbit HIT.

T2: on even side n=2L, every NN bond is in exactly one of W_P, W+, W-.
Executed on small even tori. Extra n=10,12,14 in 2D and n=6,8 in 3D.
Disjoint from the attack-g enumerator (different loop over directed steps
then undirect). HIT if a bond is missing or double-counted.
"""
from __future__ import annotations

from itertools import product

HITS: list[str] = []
STEPS2 = ((1, 0), (0, 1))
STEPS3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def bonds(shape):
    d = len(shape)
    steps = STEPS2 if d == 2 else STEPS3
    out = set()
    for x in product(*[range(n) for n in shape]):
        for st in steps:
            y = tuple((x[i] + st[i]) % shape[i] for i in range(d))
            e = tuple(sorted((x, y)))
            out.add(e)
    return out


def classify(shape):
    n = shape[0]
    L = n // 2
    d = len(shape)
    WP, Wp, Wm = set(), set(), set()
    for (a, b) in bonds(shape):
        a1, b1 = a[0], b[0]
        inP = (a1 in (0, L)) and (b1 in (0, L))
        inHp = (0 <= a1 <= L) and (0 <= b1 <= L)
        inHm = (a1 >= L or a1 == 0) and (b1 >= L or b1 == 0)
        # H- = {x1 >= L} union {x1=0}? theta_{1,0} typically x1 -> -x1 mod n = n-x1
        # H+ = 0<=x1<=L, H- = theta H+ = {0} union {L..n-1}? theta(0)=0, theta(L)=n-L=L.
        # Standard: H+ = {0,...,L}, H- = {0, L, L+1, ..., n-1} wait 0 and L are P.
        # Both ends in H+ not both in P -> W+
        if inP:
            WP.add((a, b))
        elif inHp:
            Wp.add((a, b))
        elif inHm:
            Wm.add((a, b))
        else:
            # wrap-around bonds crossing the cut away from P
            pass
    return WP, Wp, Wm


def theta(x, n):
    return ( (-x[0]) % n, ) + x[1:]


def main() -> int:
    shapes = [(10, 10), (12, 12), (14, 14), (6, 6, 6), (8, 8, 8)]
    for shape in shapes:
        n = shape[0]
        L = n // 2
        B = bonds(shape)
        WP, Wp, Wm = classify(shape)
        # rebuild with explicit H+/H-/P
        Pset = {x for x in product(*[range(s) for s in shape]) if x[0] in (0, L)}
        Hp = {x for x in product(*[range(s) for s in shape]) if 0 <= x[0] <= L}
        Hm = {theta(x, n) for x in Hp}
        WP2, Wp2, Wm2 = set(), set(), set()
        for e in B:
            a, b = e
            ends = {a, b}
            if ends <= Pset:
                WP2.add(e)
            elif ends <= Hp:
                Wp2.add(e)
            elif ends <= Hm:
                Wm2.add(e)
        union = WP2 | Wp2 | Wm2
        print(
            f"shape={shape} |B|={len(B)} |WP|={len(WP2)} |W+|={len(Wp2)} |W-|={len(Wm2)} "
            f"union={len(union)} overlap={len(WP2)+len(Wp2)+len(Wm2)-len(union)}"
        )
        if union != B:
            missing = B - union
            extra = union - B
            hit(f"{shape}: partition misses {len(missing)} extra {len(extra)}")
        if WP2 & Wp2 or WP2 & Wm2 or Wp2 & Wm2:
            hit(f"{shape}: class overlap")
        if len(Wp2) != len(Wm2):
            hit(f"{shape}: |W+|={len(Wp2)} != |W-|={len(Wm2)}")
        # theta bijection W+ -> W-
        th_Wp = set()
        for a, b in Wp2:
            ta, tb = theta(a, n), theta(b, n)
            th_Wp.add(tuple(sorted((ta, tb))))
        if th_Wp != Wm2:
            hit(f"{shape}: theta(W+) != W-")

    if HITS:
        print("SUMMARY: T2 partition falsifier FIRED - " + "; ".join(HITS[:4]))
        return 0
    print(
        "SUMMARY: T2 W_P/W+/W- partition and theta bijection hold on extra even "
        "tori (Z/10Z)^2,(Z/12Z)^2,(Z/14Z)^2,(Z/6Z)^3,(Z/8Z)^3; falsifier does "
        "not fire; not the known T3 chessboard-orbit HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
