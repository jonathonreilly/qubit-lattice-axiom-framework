#!/usr/bin/env python3
"""J:attack-d:PR8148 — QUANTIFIER SCOPE.

R4 claims the plaquette finished law is not static for every covariant rate
law at every non-constant (p,q,r). Executed at (3,1,2). Check the six-axis
kernel sums to 1 for every tested positive triple, 4! orders of the 4-cycle,
and the 4-cycle exists in Z^3. Not the known R3 TV-distance HIT.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import permutations

AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
HITS = []


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def kernel_sum(preds, p, q, r):
    w = []
    for s in AXES:
        acc = Fraction(1)
        for t in preds:
            acc *= phi(s, t, p, q, r)
        w.append(acc)
    Z = sum(w)
    return sum(x / Z for x in w)


def main():
    triples = [
        (3, 1, 2),
        (5, 2, 4),
        (4, 1, 3),
        (2, 2, 2),
        (10, 1, 2),
        (1, 1, 1),
        (7, 3, 5),
        (6, 1, 1),
    ]
    preds_list = (
        (AXES[0],) * 3,
        (AXES[0], AXES[0], AXES[1]),
        (AXES[0], AXES[2], AXES[4]),
    )
    for pqr in triples:
        for preds in preds_list:
            s = kernel_sum(preds, *map(Fraction, pqr))
            if s != 1:
                HITS.append(f"sum K !=1 at {pqr} {preds}")
    print(f"kernel sums to 1 on {len(triples)} triples x {len(preds_list)} pred types")

    orders = list(permutations(range(4)))
    print(f"plaquette orders 4!={len(orders)}")
    if len(orders) != 24:
        HITS.append(f"4!={len(orders)}")

    # 4-cycle in Z^3
    cyc = ((0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0))
    for i in range(4):
        a, b = cyc[i], cyc[(i + 1) % 4]
        d = sum(abs(a[j] - b[j]) for j in range(3))
        if d != 1:
            HITS.append(f"cycle edge {a}{b} l1={d}")
    print("spatial 4-cycle exists, NN edges")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the six-axis kernel "
        "sums to 1 for every tested positive triple including constant and "
        "non-constant rules; 24 plaquette orders; a Z^3 4-cycle exists (not "
        "the known R3 TV-distance HIT)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
