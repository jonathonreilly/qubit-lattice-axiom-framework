#!/usr/bin/env python3
"""J:attack-b:PR8174 — pattern (b) SAME TEST, BOTH SIDES.

Not the known T1(a) d1<=max(d2,d3) HIT at (1,2,1).

Separation: T5 says T3 applies only if ε2 < 256/531441, and this fails
for every p<=4150 on (p,1,2); T4 claims the region at p>=4165. Same test:
ε2 = max(d2,d3) from the six-axis product kernel versus 256/531441.
HIT if both sides pass or both fail, or if max(d2,d3) is not d3 as T5 uses.
"""
from __future__ import annotations

from fractions import Fraction


AXES = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
A = AXES[0]
MA = AXES[1]
B = AXES[2]
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


def deviations(p, q, r):
    p, q, r = Fraction(p), Fraction(q), Fraction(r)
    d1 = 1 - K(A, (A, A, A), p, q, r)
    d2 = 1 - K(A, (A, A, MA), p, q, r)
    d3 = 1 - K(A, (A, A, B), p, q, r)
    return d1, d2, d3


def main():
    lo, hi = (4150, 1, 2), (4165, 1, 2)
    d_lo = deviations(*lo)
    d_hi = deviations(*hi)
    print(f"d(4150,1,2)={d_lo}")
    print(f"d(4165,1,2)={d_hi}")
    print(f"bound={BOUND}")
    for label, d in (("4150", d_lo), ("4165", d_hi)):
        if d[2] < d[1]:
            HITS.append(f"at p={label} d3={d[2]} < d2={d[1]}; T5 used d3 as ε2")
    eps_lo = max(d_lo[1], d_lo[2])
    eps_hi = max(d_hi[1], d_hi[2])
    lo_ok = eps_lo < BOUND
    hi_ok = eps_hi < BOUND
    print(f"same test ε2<256/531441: p=4150 -> {lo_ok}; p=4165 -> {hi_ok}")
    if lo_ok == hi_ok:
        HITS.append("ceiling test does not separate 4150 from 4165")
    if lo_ok or not hi_ok:
        HITS.append(f"stated sides fail: 4150 in-domain={lo_ok} 4165 in-domain={hi_ok}")
    if d_lo[2] != Fraction(16622, 34461622):
        HITS.append(f"d3(4150)={d_lo[2]} != stated 16622/34461622")
    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (b) SAME TEST BOTH SIDES - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - the same ε2<256/531441 "
        "test fails at (4150,1,2) and holds at (4165,1,2), so T5's ceiling "
        "separates those couplings as written"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
