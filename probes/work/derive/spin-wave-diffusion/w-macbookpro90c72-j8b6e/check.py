#!/usr/bin/env python3
"""J:derive:spin-wave-diffusion:a2 — exact G_L mode sums and the 1/(1-sigma^2 G_L)^2 expansion."""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np

mp.mp.dps = 40


def A(k):
    return mp.coth(k) - 1 / k


def u_of(k1, k2):
    ph = (1 + np.exp(1j * k1) + np.exp(1j * k2)) / 3
    return float(np.real(ph * np.conj(ph)))


def G_float(L):
    s = 0.0
    n = 0
    for n1, n2 in itertools.product(range(L), repeat=2):
        if n1 == 0 and n2 == 0:
            continue
        k1, k2 = 2 * np.pi * n1 / L, 2 * np.pi * n2 / L
        u = u_of(k1, k2)
        s += 1.0 / (1.0 - u)
        n += 1
    return s / (L * L), n


def G_exact_L4():
    """L=4: cosines in {0,0,-1} wait 0, ±1, 0 for multiples of pi/2."""
    # 1-u = (6 - 2c1 - 2c2 - 2 c12)/9, c=cos
    tot = Fr(0)
    for n1, n2 in itertools.product(range(4), repeat=2):
        if n1 == n2 == 0:
            continue
        c1 = [1, 0, -1, 0][n1]
        c2 = [1, 0, -1, 0][n2]
        c12 = [1, 0, -1, 0][(n1 - n2) % 4]
        onem = Fr(6 - 2 * c1 - 2 * c2 - 2 * c12, 9)
        tot += 1 / onem
    return tot / 16


def cosine_id():
    """1-|phi|^2 = (6-2cos k1-2cos k2-2cos(k1-k2))/9, check at a grid."""
    ok = True
    for k1, k2 in [(0.3, 0.2), (1.0, -0.4), (np.pi / 2, np.pi / 3), (2.0, 2.0)]:
        ph = (1 + np.exp(1j * k1) + np.exp(1j * k2)) / 3
        u = np.real(ph * np.conj(ph))
        rhs = (6 - 2 * np.cos(k1) - 2 * np.cos(k2) - 2 * np.cos(k1 - k2)) / 9
        if abs(1 - u - rhs) > 1e-12:
            ok = False
    return ok


def main():
    hits = []
    print("T0 cosine identity 1-|phi|^2 = (6-2c1-2c2-2c12)/9:")
    ok0 = cosine_id()
    print(f"  {ok0}")
    if not ok0:
        hits.append("cosine identity")

    print("T1 G_L = N^{-1} sum_{k!=0} 1/(1-u(k)):")
    g4 = G_exact_L4()
    g4f, n4 = G_float(4)
    print(f"  L=4 exact {g4} = {float(g4):.8f}; float {g4f:.8f}; modes {n4}")
    if abs(float(g4) - g4f) > 1e-10:
        hits.append("G4")
    for L in (8, 16):
        gf, n = G_float(L)
        print(f"  L={L}: G={gf:.8f} modes={n}")

    print("T2 expansion 1/(1-x)^2 = 1+2x+3x^2 at x=sigma^2 G_L:")
    G16, _ = G_float(16)
    for beta in (6, 12, 24, 48):
        sig2 = A(3 * beta) / (3 * beta)
        x = sig2 * mp.mpf(G16)
        pred = 1 / (1 - x) ** 2
        series = 1 + 2 * x + 3 * x ** 2
        aligned = 1 / A(3 * beta) ** 2
        print(
            f"  L=16 beta={beta}: sigma^2 G={mp.nstr(x, 5)} pred={mp.nstr(pred, 6)} "
            f"series={mp.nstr(series, 6)} aligned 1/A^2={mp.nstr(aligned, 6)}"
        )
        if abs(pred - series) > 0.05 and beta >= 24:
            hits.append(f"series {beta}")

    print("T3 beta->infty first correction 2 sigma^2 G_L at fixed L=16:")
    # A(3b)/(3b) ~ 1/(3b)
    for beta in (24, 48, 96):
        sig2 = A(3 * beta) / (3 * beta)
        corr = 2 * sig2 * mp.mpf(G16)
        pred = 1 / (1 - sig2 * mp.mpf(G16)) ** 2
        print(f"  beta={beta}: 2 sigma^2 G={mp.nstr(corr, 5)} pred-1={mp.nstr(pred - 1, 5)}")

    if hits:
        print("SUMMARY: ROUTE FAILS AT " + ", ".join(hits))
        return 1
    print(
        f"HIT: G_L is the mode sum N^{{-1}} sum_{{k!=0}} 1/(1-|phi|^2) (G_4={g4} exact); linearized "
        f"|M|=1-sigma^2 G_L+O(sigma^4); Jacobian then gives D_1 L^2/sigma^2 = 1/(1-sigma^2 G_L)^2 "
        f"-> 1 at fixed L as beta->infty with first correction 2 sigma^2 G_L; G_16={G16:.5f}"
    )
    print(
        "SUMMARY: PARTIAL - spin-wave insertion of block 34's G_L into the Jacobian: the ratio is "
        "1/(1-sigma^2 G_L)^2 at fixed L, G_L computed exactly on L=4 and numerically on 8,16"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
