#!/usr/bin/env python3
"""J:attack:PR8154 - block 20, attack pattern (f) NORMALIZATION.

Recompute at small even-side tori the note's Fourier conventions
  s^(k) = N^{-1/2} sum_x e^{ik.x} s_x,  k = (pi/L) n, n in {-L+1,...,L}^d,
  E(k) = sum_i 2(1-cos k_i),  |1-e^{-ik_i}|^2 = 2(1-cos k_i),
Parseval, bond counts, H2 shell counts 8j / 4L-1, sum 1/|n|^2 >= 4 H_{L-1},
and 4/(3N) = |k_min|^2/(3 pi^2). Exact rationals where the note is exact.

HIT if a convention, count or identity fails.
"""
from __future__ import annotations

import cmath
import math
from fractions import Fraction as Fr
from itertools import product

import numpy as np


def harmonic(m: int) -> Fr:
    return sum((Fr(1, k) for k in range(1, m + 1)), Fr(0))


def nrange(L: int):
    return list(range(-L + 1, L + 1))  # {-L+1,...,L}, length 2L


def shells_plane(L: int):
    ns = nrange(L)
    by = {}
    for n in product(ns, repeat=2):
        if n == (0, 0):
            continue
        j = max(abs(n[0]), abs(n[1]))
        by.setdefault(j, []).append(n)
    return by


def parseval_plane(L: int, rng=None) -> complex:
    """sum_k |s^(k)|^2 - sum_x |s_x|^2 on a real 3-vector field (one component)."""
    rng = np.random.default_rng(8154 if rng is None else rng)
    side = 2 * L
    N = side * side
    s = rng.normal(size=(side, side))
    ks = nrange(L)
    acc = 0j
    for n1, n2 in product(ks, repeat=2):
        k1, k2 = math.pi * n1 / L, math.pi * n2 / L
        hat = 0j
        for x1 in range(side):
            for x2 in range(side):
                hat += cmath.exp(1j * (k1 * x1 + k2 * x2)) * s[x1, x2]
        hat *= N ** -0.5
        acc += abs(hat) ** 2
    return acc - float((s ** 2).sum())


def bonds_plane(L: int) -> int:
    side = 2 * L
    # two directions, periodic
    return 2 * side * side


def bonds_line(L: int) -> int:
    return 2 * L  # N = 2L, one direction, periodic


def main() -> None:
    hits = []
    for L in range(2, 9):
        by = shells_plane(L)
        ok_shell = True
        for j in range(1, L):
            got = len(by.get(j, []))
            if got != 8 * j:
                ok_shell = False
                hits.append(f"L={L} shell j={j} has {got} != 8j={8*j}")
        gotL = len(by.get(L, []))
        if gotL != 4 * L - 1:
            hits.append(f"L={L} shell j=L has {gotL} != 4L-1={4*L-1}")
        sm = sum((Fr(1, n[0] * n[0] + n[1] * n[1]) for pts in by.values() for n in pts), Fr(0))
        rhs = 4 * harmonic(L - 1)
        print(f"L={L}: shells j<L 8j ok={ok_shell}; j=L {gotL}; sum 1/|n|^2={sm} >= 4 H_{{L-1}}={rhs}: {sm >= rhs}")
        if sm < rhs:
            hits.append(f"L={L} sum 1/|n|^2={sm} < 4 H={rhs}")

        N = 4 * L * L
        kmin2 = Fr(1, L * L)  # (pi/L)^2 / pi^2 = 1/L^2
        left = Fr(4, 3 * N)
        right = kmin2 / 3  # |k|^2/(3 pi^2) with |k|^2/pi^2 = 1/L^2
        print(f"  4/(3N)={left} vs |k_min|^2/(3 pi^2)={right}")
        if left != right:
            hits.append(f"L={L} 4/(3N)={left} != {right}")

        bp = bonds_plane(L)
        if bp != 2 * N:
            hits.append(f"L={L} plane bonds {bp} != 2N={2*N}")

    # Parseval at L=2,3 (4x4 and 6x6)
    for L in (2, 3, 4):
        d = parseval_plane(L)
        print(f"Parseval L={L} (4-vector? side {2*L}): residual {d.real:.3e}+{d.imag:.3e}j")
        if abs(d) > 1e-8:
            hits.append(f"Parseval L={L} residual {d}")

    # E(k) vs |1-e^{-ik}|^2 and vs |k|^2
    for u in (0.0, 0.1, math.pi / 4, math.pi / 2, math.pi):
        e = 2 * (1 - math.cos(u))
        one = abs(1 - cmath.exp(-1j * u)) ** 2
        if abs(e - one.real) > 1e-12:
            hits.append(f"|1-e^{{-iu}}|^2 {one} != 2(1-cos) {e}")
        if u != 0 and e - 1e-12 > u * u:
            hits.append(f"E={e} > u^2={u*u} at u={u}")
    print("E(k)=|1-e^{-ik}|^2 and E<=|k|^2 on sample angles: ok" if not hits else "E(k) checks done")

    # line N=2L, count of 1<=|n|<=floor(sqrt L)
    for L in range(2, 50):
        m = math.isqrt(L)
        ns = [n for n in nrange(L) if 1 <= abs(n) <= m]
        if len(ns) != 2 * m:
            hits.append(f"line L={L} small-n count {len(ns)} != 2 floor(sqrt L)={2*m}")
        if 4 * m * m < L:
            hits.append(f"4 floor(sqrt L)^2={4*m*m} < L={L}")
        N = 2 * L
        if Fr(4, 3 * N) != Fr(2, 3 * L):
            hits.append(f"line 4/(3N) != 2/(3L) at L={L}")
    print("line small-n counts and 4 floor(sqrt L)^2 >= L for L=2..49 checked")

    # 8-site line: N=8, L=4, bonds=N
    if bonds_line(4) != 8:
        hits.append(f"8-torus bonds {bonds_line(4)} != 8")

    if hits:
        for h in hits:
            print("HIT: " + h)
        print("SUMMARY: pattern (f) NORMALIZATION; " + "; ".join(hits))
    else:
        print(
            "SUMMARY: pattern (f) NORMALIZATION; N^{-1/2} Parseval, E(k)=|1-e^{-ik}|^2 <= |k|^2, "
            "plane shells 8j / 4L-1, sum 1/|n|^2 >= 4 H_{L-1}, 4/(3N)=|k_min|^2/(3 pi^2), "
            "bond counts 2N (plane) and N (line), and line 2 floor(sqrt L) all hold at small L"
        )


if __name__ == "__main__":
    main()
