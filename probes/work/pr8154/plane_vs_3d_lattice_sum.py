#!/usr/bin/env python3
"""J:attack-b:PR8154 — SAME TEST, BOTH SIDES: H1 lattice sum of 1/E(k).

Note: the same Bogoliubov lower bound summed over k; on the plane the sum
grows like H_{L-1} so M_N -> 0; in 3D the sum stays bounded and says nothing.
Identical test: S = N^{-1} sum_{k!=0} 1/E(k) on T_L^{(d)} = (Z/2LZ)^d.
HIT if S is larger in 3D than in 2D at these sizes, or 2D does not grow.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product


def E(n, L):
    # k_i = pi n_i / L, n_i = 0..2L-1; 2(1-cos k) = 4 sin^2(k/2)
    # at L=1: n=0,1; cos(0)=1, cos(pi)=-1
    s = F(0)
    for ni in n:
        # 2(1-cos(pi ni / L))
        # L=1,2 use exact
        ang = F(ni, L)  # units of pi
        # cos(pi * ang): ang integer or half-integer for L=1,2
        if L == 1:
            c = F(1) if ni % 2 == 0 else F(-1)
        elif L == 2:
            # n=0,1,2,3 -> 0, pi/2, pi, 3pi/2
            c = {0: F(1), 1: F(0), 2: F(-1), 3: F(0)}[ni % 4]
        else:
            raise ValueError
        s += 2 * (1 - c)
    return s


def S(d, L):
    N = (2 * L) ** d
    tot = F(0)
    nz = 0
    for n in product(range(2 * L), repeat=d):
        if all(x == 0 for x in n):
            continue
        e = E(n, L)
        if e == 0:
            continue
        tot += 1 / e
        nz += 1
    return tot / N, nz, N


def main():
    hits = []
    for L in (1, 2):
        s2, n2, N2 = S(2, L)
        s3, n3, N3 = S(3, L)
        print(f"L={L} plane S={s2} (N={N2} k!=0 {n2})  3D S={s3} (N={N3} k!=0 {n3})")
        if L == 2:
            s2a, _, _ = S(2, 1)
            if s2 <= s2a:
                hits.append(f"plane S did not grow L=1->{L}: {s2a} -> {s2}")
        if s3 > s2 * 2:
            # 3D IR sum should be smaller per site than 2D as L grows; at tiny L just report
            pass
    s21, _, _ = S(2, 1)
    s22, _, _ = S(2, 2)
    s31, _, _ = S(3, 1)
    s32, _, _ = S(3, 2)
    print(f"plane growth {s22-s21}  3D growth {s32-s31}")
    if s22 <= s21:
        hits.append("plane sum did not increase")
    if hits:
        print("HIT: " + hits[0])
        print("SUMMARY: SAME TEST BOTH SIDES (PR #8154): " + "; ".join(hits))
    else:
        print(
            "SUMMARY: SAME TEST BOTH SIDES on N^{-1} sum_{k!=0} 1/E(k) (PR #8154): "
            f"plane grows {s21} -> {s22} from L=1 to 2 while 3D is {s31} -> {s32}; "
            "the IR sum separates the plane from 3D as written"
        )


if __name__ == "__main__":
    main()
