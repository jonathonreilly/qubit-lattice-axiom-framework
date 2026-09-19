#!/usr/bin/env python3
"""J:attack-f:PR8149 — NORMALIZATION.

Recompute the six-axis kernel normalizer Z=Σ_s ∏_j φ(s, pred_j) so the
conditional sums to 1, and TV=(1/2)Σ|μ-ν|. Not the known 216-env U2/U4 HIT.
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
    for preds in ((AXES[0],) * 3, (AXES[0], AXES[0], AXES[1]), (AXES[0], AXES[2], AXES[4])):
        k, Z = kernel(preds, p, q, r)
        sm = sum(k)
        print(f"preds={preds}: Z={Z} sum K={sm}")
        if sm != 1:
            HITS.append(f"sum K={sm}")
        if Z <= 0:
            HITS.append(f"Z={Z}")
    k0, _ = kernel((AXES[0],) * 3, p, q, r)
    if tv(k0, k0) != 0:
        HITS.append("TV(μ,μ)")
    e0 = [Fraction(1)] + [Fraction(0)] * 5
    e1 = [Fraction(0), Fraction(1)] + [Fraction(0)] * 4
    if tv(e0, e1) != 1:
        HITS.append(f"TV point masses {tv(e0,e1)}")
    print(f"TV 1/2: TV(μ,μ)=0 TV(e0,e1)={tv(e0,e1)}")
    # Z1 = p+q+4r for one neighbour
    Z1 = p + q + 4 * r
    print(f"one-neighbour Z1=p+q+4r={Z1} at (3,1,2)")
    if Z1 != 12:
        HITS.append(f"Z1={Z1} != 12")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (f) NORMALIZATION - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - six-axis conditionals "
        "sum to 1 at (3,1,2); TV 1/2; Z1=p+q+4r=12; not the known 216-env HIT"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
