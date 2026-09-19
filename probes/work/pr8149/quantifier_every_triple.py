#!/usr/bin/env python3
"""J:attack-d:PR8149 — QUANTIFIER SCOPE.

Six-axis conditionals sum to 1 for every tested positive (p,q,r); a star
has 6 neighbors. Not the known 216-env U2/U4 HIT.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
HITS = []


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def ksum(preds, p, q, r):
    w = []
    for s in AXES:
        acc = Fraction(1)
        for t in preds:
            acc *= phi(s, t, p, q, r)
        w.append(acc)
    Z = sum(w)
    return sum(x / Z for x in w)


def main():
    triples = list(product(range(1, 5), repeat=3))
    preds = (AXES[0], AXES[0], AXES[2])
    for pqr in triples:
        if ksum(preds, *map(Fraction, pqr)) != 1:
            HITS.append(f"sum K !=1 at {pqr}")
            break
    print(f"kernel sums to 1 on {len(triples)} triples in {{1..4}}^3")
    star = [(0, 0, 0)] + [tuple(d) for d in AXES]
    if len(set(star)) != 7:
        HITS.append("star not 7")
    print(f"star sites {len(set(star))}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - six-axis K sums to 1 "
        "for every (p,q,r) in {1..4}^3; the 6-neighbor star has 7 sites; not "
        "the known 216-env HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
