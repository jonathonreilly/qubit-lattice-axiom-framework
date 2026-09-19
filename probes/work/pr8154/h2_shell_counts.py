#!/usr/bin/env python3
"""J:attack-g:PR8154 — pattern (g) PROOF STEP BY BRUTE FORCE.

H2(a): on n in {-L+1,...,L}^2, the sup-norm shell |n|_inf=j has 8j points for
1<=j<=L-1 and 4L-1 points at j=L; every point of shell j has |n|^2 <= 2 j^2.
Also H2(c) half-angle: 2(1-cos u)=4 sin^2(u/2) <= u^2.

Distinct from the H1/H3 ring falsifier and the Fourier-normalization attack.
HIT if a shell count or the half-angle identity fails.
"""
from __future__ import annotations

import sympy as sp

HITS = []


def shells(L):
    rng = range(-L + 1, L + 1)
    buckets = {}
    for n1 in rng:
        for n2 in rng:
            if n1 == 0 and n2 == 0:
                continue
            j = max(abs(n1), abs(n2))
            buckets.setdefault(j, []).append((n1, n2))
    return buckets


def main():
    u = sp.symbols("u", real=True)
    ident = sp.simplify(2 * (1 - sp.cos(u)) - 4 * sp.sin(u / 2) ** 2)
    print(f"2(1-cos u)-4 sin^2(u/2) = {ident}")
    if ident != 0:
        HITS.append("half-angle identity fails")
    # 4 sin^2(t) <= 4 t^2 with t=u/2, i.e. |sin t|<=|t|
    for val in (sp.pi / 2, sp.pi / 3, sp.pi / 5, 1, 0):
        lhs = sp.simplify(2 * (1 - sp.cos(val)))
        rhs = sp.simplify(val**2)
        if not (sp.simplify(rhs - lhs) >= 0):
            HITS.append(f"2(1-cos u)>u^2 at u={val}: {lhs} vs {rhs}")
        print(f"  E vs u^2 at u={val}: {lhs} <= {rhs}")

    for L in range(2, 21):
        b = shells(L)
        for j in range(1, L):
            n = len(b.get(j, []))
            if n != 8 * j:
                HITS.append(f"L={L} j={j}: |shell|={n} != 8j={8*j}")
            for n1, n2 in b.get(j, []):
                if n1 * n1 + n2 * n2 > 2 * j * j:
                    HITS.append(f"L={L} j={j}: |n|^2={n1*n1+n2*n2} > 2j^2={2*j*j}")
        nL = len(b.get(L, []))
        if nL != 4 * L - 1:
            HITS.append(f"L={L} j=L: |shell|={nL} != 4L-1={4*L-1}")
        print(f"L={L} shells j=1..L-1 all 8j; j=L has {nL} (4L-1={4*L-1})")

    if HITS:
        print("HIT: " + "; ".join(HITS))
        print(
            "SUMMARY: attack pattern (g) PROOF STEP BY BRUTE FORCE on H2 shell "
            "counts and half-angle identity - " + "; ".join(HITS)
        )
        return 0
    print(
        "SUMMARY: pattern has no purchase on this note - H2(a) shells have 8j "
        "points for j<L and 4L-1 at j=L with |n|^2<=2j^2 for L=2..20, and "
        "2(1-cos u)=4 sin^2(u/2)<=u^2 holds exactly"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
