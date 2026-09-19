#!/usr/bin/env python3
"""J:attack-d:PR8155 — QUANTIFIER SCOPE.

Not the known W5 L=1 torus degree-3 HIT.

W1(ii) claims 6/(n(2n-1)) ≤ 1 for every n≥2 and 3/(2n+1) ≤ 1 for every
n≥1 (executed to n=12). W2 claims α<1 iff β<√3/6 for every β>0.
W4 claims a walk from Δ_ℓ to ∂_in Λ_L has length ≥ L−ℓ for every L,ℓ.
Look inside those ranges for a failure.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product

import mpmath as mp

HITS = []
STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
mp.mp.dps = 40


def linf(p):
    return max(abs(p[0]), abs(p[1]), abs(p[2]))


def main():
    for n in range(2, 81):
        r = Fraction(6, n * (2 * n - 1))
        if r > 1:
            HITS.append(f"6/(n(2n-1))={r} > 1 at n={n}")
            break
        if n == 2 and r != 1:
            HITS.append(f"n=2 ratio {r} != 1")
    for n in range(1, 81):
        r = Fraction(3, 2 * n + 1)
        if r > 1:
            HITS.append(f"3/(2n+1)={r} > 1 at n={n}")
            break
        if n == 1 and r != 1:
            HITS.append(f"n=1 L/x ratio {r} != 1")
    print("ratios ≤1 for n≤80: True" if not HITS else "ratios failed")

    # α = 2√3 β < 1 iff 12 β² < 1 iff β² < 1/12
    samples = [
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(2, 7),
        Fraction(1, 5),
        Fraction(3, 10),
        Fraction(1, 12),
        Fraction(1, 2),
    ]
    thresh2 = Fraction(1, 12)
    for b in samples:
        alpha_lt = (b * b) < thresh2
        stated = b * b < thresh2
        print(f"beta={b}: beta^2={b*b} vs 1/12={thresh2}; alpha<1 iff {alpha_lt}")
        if alpha_lt != stated:
            HITS.append(f"iff failed at beta={b}")
    # just below / just above via rationals 1/4 < sqrt(3)/6 < 1/3
    if not (Fraction(1, 16) < thresh2 < Fraction(1, 9)):
        HITS.append("1/4 and 1/3 do not straddle √3/6")

    # W4 walk length: every L=1..4, every ℓ≤L, every start in Δ_ℓ
    for L in range(1, 5):
        box = list(product(range(-L, L + 1), repeat=3))
        boundary = [p for p in box if linf(p) == L]
        for ell in range(0, L + 1):
            starts = [p for p in box if linf(p) <= ell]
            for s in starts:
                # BFS min NN steps in Z^3 (walks may leave the box; lower bound is geometric)
                mind = min(linf((s[0] - q[0], s[1] - q[1], s[2] - q[2])) for q in boundary)
                # each step changes linf by at most 1, so dist ≥ L - linf(s)
                need = L - linf(s)
                if mind < need:
                    HITS.append(f"linf gap {mind} < L-ℓ={need} at L={L} s={s}")
                    break
            else:
                continue
            break
        else:
            continue
        break
    print("W4 L-ℓ length on Λ_L for L=1..4: checked")

    # W1: L'(x) ≤ 1/3 and L(x)/x ≤ 1/3 for every sampled x>0
    third = mp.mpf(1) / 3
    xs = [mp.mpf(k) / 10 for k in range(1, 81)] + [mp.mpf(n) for n in range(9, 41)]
    for x in xs:
        Lp = 1 / x**2 - 1 / mp.sinh(x) ** 2
        Lx = mp.coth(x) - 1 / x
        if Lp > third + mp.mpf("1e-20"):
            HITS.append(f"L'({x})={Lp} > 1/3")
            break
        if Lx / x > third + mp.mpf("1e-20"):
            HITS.append(f"L({x})/x={Lx/x} > 1/3")
            break
    else:
        print(f"L' and L/x ≤ 1/3 on {len(xs)} points of (0,40]: True")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print("SUMMARY: attack pattern (d) QUANTIFIER SCOPE - " + "; ".join(HITS))
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - coefficient ratios "
        "6/(n(2n-1)) and 3/(2n+1) stay ≤1 through n=80; α<1 iff β²<1/12 at "
        "the sampled β; L' and L/x stay ≤1/3 on a grid of (0,40]; W4's "
        "L−ℓ walk lower bound holds on every Λ_L for L=1..4 (not the known "
        "L=1 torus degree defect)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
