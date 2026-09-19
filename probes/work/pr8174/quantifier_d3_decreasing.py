#!/usr/bin/env python3
"""J:attack-d:PR8174 — QUANTIFIER SCOPE.

T1(a) claims d3 decreasing in p at fixed q,r>0 (executed on four lines).
T5/T4: ε2<256/531441 for every p>=4165 on (p,1,2). Check d3(p,1,2) decreasing
for p=1..30 and the ceiling test at p=4165,4166,5000,8000.
Not the known T1(a) d1<=max(d2,d3) HIT at (1,2,1) or the W1 8/5 HIT.
"""
from __future__ import annotations

from fractions import Fraction

AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
A, MA, B = AXES[0], AXES[1], AXES[2]
BOUND = Fraction(256, 531441)
HITS = []


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def K(s, pred, p, q, r):
    def w(ss):
        acc = Fraction(1)
        for t in pred:
            acc *= phi(ss, t, p, q, r)
        return acc

    Z = sum(w(ss) for ss in AXES)
    return w(s) / Z


def d3(p, q=1, r=2):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    return 1 - K(A, (A, A, B), p, q, r)


def main():
    prev = None
    for p in range(1, 31):
        val = d3(p)
        print(f"d3({p},1,2)={val}")
        if prev is not None and val >= prev:
            HITS.append(f"d3 not decreasing at p={p}: {val} >= {prev}")
            break
        prev = val
    for p in (4165, 4166, 5000, 8000):
        eps = d3(p)
        ok = eps < BOUND
        print(f"p={p}: d3={eps} < 256/531441 {ok}")
        if not ok:
            HITS.append(f"T4 ceiling fails at p={p}")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - d3(p,1,2) is strictly "
        "decreasing for p=1..30 and ε2<256/531441 at p=4165,4166,5000,8000 "
        "(not the known T1(a) (1,2,1) or W1 8/5 HITs)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
