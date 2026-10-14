#!/usr/bin/env python3
"""E1 (A) check 1: exact row-to-row transfer matrix of the anisotropic 2D Ising model
on periodic strips of width L, against the free-fermion (Onsager / Schultz-Mattis-Lieb)
single-particle law

    cosh eps(q) = cosh(2 Ky*) cosh(2 Kx) - sinh(2 Ky*) sinh(2 Kx) cos q,   tanh Ky* = exp(-2 Ky)

(Kx = coupling inside a row, Ky = coupling between rows; transfer runs along y).
Checks: (i) top eigenvalue (free energy per site) vs the NS-sector formula;
(ii) gap ln(L0/L1) vs the R-sector formula; (iii) L -> infinity gap -> eps(0) = 2(Ky* - Kx)
in the disordered phase; (iv) the infinite-L free energy vs Onsager's double integral.
Memory: 2^L doubles, L <= 16 -> 0.5 MB per vector.
"""
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

def dual(K):
    return np.arctanh(np.exp(-2.0 * K))

def tm_top(L, Kx, Ky, k=2):
    n = 1 << L
    idx = np.arange(n)
    bits = ((idx[:, None] >> np.arange(L)) & 1) * 2 - 1          # spins +-1, shape (n, L)
    bond = (bits * np.roll(bits, -1, axis=1)).sum(axis=1)        # sum s_i s_{i+1}, periodic
    half = np.exp(0.5 * Kx * bond)
    del bits
    a, b = np.exp(Ky), np.exp(-Ky)
    def apply_vy(v):
        w = v.copy()
        for i in range(L):
            m = 1 << i
            w = a * w + b * w[idx ^ m]
        return w
    def mv(v):
        v = np.asarray(v).ravel()
        return half * apply_vy(half * v)
    op = LinearOperator((n, n), matvec=mv, dtype=float)
    vals = eigsh(op, k=k, which='LA', tol=1e-13)[0]
    return np.sort(vals)[::-1]

def eps(q, Kx, Ky):
    Ks = dual(Ky)
    c = np.cosh(2 * Ks) * np.cosh(2 * Kx) - np.sinh(2 * Ks) * np.sinh(2 * Kx) * np.cos(q)
    return np.arccosh(c)

def ff_logs(L, Kx, Ky):
    pref = 0.5 * L * np.log(2 * np.sinh(2 * Ky))
    qNS = (2 * np.arange(L) + 1) * np.pi / L
    lNS = pref + 0.5 * eps(qNS, Kx, Ky).sum()
    qR = 2 * np.arange(L) * np.pi / L
    eR = eps(qR, Kx, Ky)
    eR[0] = 2 * (Kx - dual(Ky))           # signed q = 0 mode in the R sector
    lR = pref + 0.5 * eR.sum()
    return lNS, lR

def f_onsager(Kx, Ky, N=4000, slab=250):
    # slab-wise accumulation (memory: slab*N doubles per array)
    th = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    c2 = np.sinh(2 * Ky) * np.cos(th)[None, :]
    acc = 0.0
    for i0 in range(0, N, slab):
        c1 = np.sinh(2 * Kx) * np.cos(th[i0:i0 + slab])[:, None]
        acc += np.log(np.cosh(2 * Kx) * np.cosh(2 * Ky) - c1 - c2).sum()
    return np.log(2.0) + 0.5 * acc / N**2

def f_1d(Kx, Ky, N=200000):
    q = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    return 0.5 * np.log(2 * np.sinh(2 * Ky)) + 0.5 * eps(q, Kx, Ky).mean()

if __name__ == "__main__":
    Kc = 0.5 * np.arcsinh(1.0)
    print(f"Kc = {Kc:.15f}")
    cases = [(0.30, 0.25), (0.35, 0.40), (0.25, 0.45), (0.50, 0.42), (Kc * 1.1, Kc * 0.9)]
    print("(i)-(ii) strip checks: L, Kx, Ky, ln L0 (TM), ln L0 (NS formula), gap TM, gap formula")
    worst = 0.0
    for (Kx, Ky) in cases:
        for L in (6, 8, 10, 12, 14):
            v = tm_top(L, Kx, Ky)
            lNS, lR = ff_logs(L, Kx, Ky)
            l0, l1 = sorted([lNS, lR])[::-1]
            d0 = abs(np.log(v[0]) - l0); d1 = abs(np.log(v[0] / v[1]) - (l0 - l1))
            worst = max(worst, d0, d1)
            print(f"L={L:2d} Kx={Kx:.4f} Ky={Ky:.4f}  lnL0 {np.log(v[0]):.12f} {l0:.12f}  gap {np.log(v[0]/v[1]):.12f} {l0-l1:.12f}")
    print(f"worst |TM - free-fermion| over all strips = {worst:.2e}")
    print("(iii) gap at L=16 vs eps(0)=2(Ky*-Kx) (disordered phase cases)")
    for (Kx, Ky) in [(0.30, 0.25), (0.25, 0.35), (0.20, 0.40)]:
        v = tm_top(16, Kx, Ky)
        print(f"Kx={Kx} Ky={Ky}: gap L=16 {np.log(v[0]/v[1]):.10f}  eps(0) {2*(dual(Ky)-Kx):.10f}")
    print("(iv) infinite-L free energy: 1D eps-integral vs Onsager double integral")
    for (Kx, Ky) in [(0.30, 0.25), (Kc * 1.1, Kc * 0.9), (Kc, Kc), (0.6, 0.3)]:
        print(f"Kx={Kx:.5f} Ky={Ky:.5f}: 1D {f_1d(Kx, Ky):.12f}  2D {f_onsager(Kx, Ky):.12f}")
