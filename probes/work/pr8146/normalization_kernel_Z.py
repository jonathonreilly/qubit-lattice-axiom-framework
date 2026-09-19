#!/usr/bin/env python3
"""J:attack-f:PR8146 — NORMALIZATION.

Six-axis kernel sums to 1; Z1=p+q+4r; TV 1/2. Not the known S1 2:1 majority
HIT at (5,2,4).
"""
from __future__ import annotations

from fractions import Fraction

AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
HITS = []


def phi(s, t, p, q, r):
    if s == t:
        return p
    if s == (-t[0], -t[1], -t[2]):
        return q
    return r


def kernel(preds, p, q, r):
    w = []
    for s in AXES:
        acc = Fraction(1)
        for t in preds:
            acc *= phi(s, t, p, q, r)
        w.append(acc)
    Z = sum(w)
    return [x / Z for x in w], Z


def tv(mu, nu):
    return Fraction(1, 2) * sum(abs(a - b) for a, b in zip(mu, nu))


def main():
    p, q, r = Fraction(3), Fraction(1), Fraction(2)
    k, Z = kernel((AXES[0],) * 3, p, q, r)
    print(f"Z(aaa)={Z} sum K={sum(k)}")
    if sum(k) != 1:
        HITS.append("sum K")
    Z1 = p + q + 4 * r
    print(f"Z1={Z1}")
    e0 = [Fraction(1)] + [0] * 5
    e1 = [0, Fraction(1)] + [0] * 4
    print(f"TV(e0,e1)={tv(e0, e1)}")
    if tv(e0, e1) != 1:
        HITS.append("TV 1/2")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - six-axis K sums to 1, "
        "Z1=p+q+4r=12 at (3,1,2), TV 1/2; not the known 2:1 majority HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
