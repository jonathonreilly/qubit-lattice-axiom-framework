#!/usr/bin/env python3
"""J:attack-b:PR8151 — SAME TEST BOTH SIDES on T2's W+ vs W- split.

Not the known T3 chessboard-orbit HIT.
T2: nn bonds split into W_P (both ends in P), W+ (both in H+ not both in P),
W- = mirror. Same tests: cardinality, disjointness, cover of all nn bonds,
and θ: H+→H- inducing a bijection W+→W- — applied to W+ and W- equally.
HIT if W+ and W- fail the same test in the same representation.
"""
from __future__ import annotations

import itertools
import sys


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def nn_bonds(shape):
    d = len(shape)
    bonds = []
    for x in itertools.product(*[range(n) for n in shape]):
        for i in range(d):
            y = list(x)
            y[i] = (y[i] + 1) % shape[i]
            y = tuple(y)
            e = tuple(sorted((x, y)))
            bonds.append(e)
    return list(dict.fromkeys(bonds))


def theta(x, n, axis=0):
    x = list(x)
    x[axis] = (-x[axis]) % n
    return tuple(x)


def classify(shape):
    n = shape[0]
    assert n % 2 == 0
    L = n // 2
    P = {x for x in itertools.product(*[range(s) for s in shape]) if x[0] in (0, L)}
    Hp = {x for x in itertools.product(*[range(s) for s in shape]) if 0 <= x[0] <= L}
    Hm = {theta(x, n) for x in Hp}
    WP, Wp, Wm = set(), set(), set()
    for e in nn_bonds(shape):
        a, b = e
        ends = {a, b}
        if ends <= P:
            WP.add(e)
        elif ends <= Hp:
            Wp.add(e)
        elif ends <= Hm:
            Wm.add(e)
    return WP, Wp, Wm, P, Hp, Hm, n


def main() -> int:
    for shape in ((4, 4), (6, 6), (8, 8), (4, 4, 4), (6, 6, 6)):
        WP, Wp, Wm, P, Hp, Hm, n = classify(shape)
        allb = set(nn_bonds(shape))
        print(f"{shape}: |bonds|={len(allb)} |WP|={len(WP)} |W+|={len(Wp)} |W-|={len(Wm)}")
        # same cover/disjointness test on all three classes
        if WP & Wp or WP & Wm or Wp & Wm:
            return hits(f"{shape}: classes are not disjoint")
        leftover = allb - WP - Wp - Wm
        if leftover:
            return hits(f"{shape}: bonds in no class: {len(leftover)}")
        # same cardinality test on W+ and W-
        if len(Wp) != len(Wm):
            return hits(f"{shape}: |W+|={len(Wp)} != |W-|={len(Wm)} — claimed mirrors fail the same count")
        # same θ-image test
        th_Wp = {tuple(sorted((theta(a, n), theta(b, n)))) for a, b in Wp}
        if th_Wp != Wm:
            return hits(f"{shape}: θ(W+) != W-")
        th_Wm = {tuple(sorted((theta(a, n), theta(b, n)))) for a, b in Wm}
        if th_Wm != Wp:
            return hits(f"{shape}: θ(W-) != W+ (same bijection test on the other side)")
        print(f"{shape}: partition and θ-bijection W+↔W-: True")

    print(
        "SUMMARY: pattern has no purchase on this note: W+ and W- have equal "
        "cardinality, are disjoint from each other and from W_P, cover the nn "
        "bonds with W_P, and are swapped by θ on even tori (2d and 3d)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
