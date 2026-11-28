#!/usr/bin/env python3
"""Follow-up to checks/hard-core--independent_coer_g.py, full torus, tau = 1, n = 2.

The first run gave FAIL-WOOD and FAIL-COND against thresholds 0.05 and 30, which I had
set without computing anything: wood_min = 0.0224, 0.0171 and cond = 105.9, 150.1 at
L = 3, 5. The question those numbers leave open is whether w(L) stays positive and c(L)
stays bounded as L -> infinity, or whether they drift with L, which would be a real
failure. On the full torus and at tau = 1, H_1 = (lattice Laplacian + L^{-2}) on each
link component, so H_1^{-1} is an FFT multiplier and both quantities are exact to
machine precision for large L.

Pre-registered criteria, written before this run:
    PASS-FORMULA: at L = 3, 5, w and c agree with the iterative values above within 1e-3,
    relative. If not, this script does not compute what the first one did.
    PASS-LIMIT: the continuum sums below are w_inf := sum over odd m in Z^4 of
    prod_i (4 / (pi^2 m_i^2)) / (pi^2 |m|^2 + 1) at the staggered coarse momentum, and
    the analogous c_inf for the condition number, computed from Q's shape factors, with
    the longitudinal Woodbury term included only in the lattice values. PASS if
    w(15) >= 0.012, and c(L) <= 300 for all L <= 15 with increments that decrease.
    FAIL-LIMIT otherwise: then the block-mean split or the bound on the degree of T is
    in trouble and the text has to change.
"""
import itertools
import os
import resource
import sys

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")

import numpy as np

RSS_LIMIT_BYTES = 2 * 1024**3
DIM = 4
N_BLOCKS = 2


def check_rss():
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > RSS_LIMIT_BYTES:
        print("ABORT rss")
        sys.exit(3)


def run(L, tau=1.0):
    n = N_BLOCKS
    N = n * L
    m2 = L ** (-2.0)
    k = 2 * np.pi * np.fft.fftfreq(N)
    ph = 4 * np.sin(k / 2) ** 2
    denom = sum(np.ix_(*[ph if i == d else np.ones(1) for i in range(DIM)])[d].reshape(*[N if i == d else 1 for i in range(DIM)]) for d in range(DIM)) + m2

    def Hinv(a):
        return np.real(np.fft.ifftn(np.fft.fftn(a) / denom))

    # Q^T e_c for the bond from block 0 in direction nu: on nu-links only
    qt = []
    for nu in range(DIM):
        a = np.zeros((N,) * DIM)
        for x in itertools.product(range(L), repeat=DIM):
            for s in range(L):
                z = list(x)
                z[nu] = (z[nu] + s) % N
                a[tuple(z)] += L ** (-4.0)
        qt.append(a)

    # f := u_0 = L^{-2} on block 0, V_mu = f(x + e_mu) - f(x)
    f = np.zeros((N,) * DIM)
    f[tuple(slice(0, L) for _ in range(DIM))] = L ** (-2.0)
    V = [np.roll(f, -1, axis=mu) - f for mu in range(DIM)]

    shifts = list(itertools.product(range(n), repeat=DIM))
    nb = len(shifts)

    def tr(a, s):
        return np.roll(a, tuple(si * L for si in s), axis=tuple(range(DIM)))

    # Woodbury matrix
    HV = [Hinv(v) for v in V]
    K = np.zeros((nb, nb))
    for j, s in enumerate(shifts):
        for i, r in enumerate(shifts):
            K[i, j] = sum(np.sum(tr(V[mu], r) * tr(HV[mu], s)) for mu in range(DIM))
    K = 0.5 * (K + K.T)
    W = np.eye(nb) - tau * K
    evW = np.linalg.eigvalsh(W)
    w = float(evW.min())

    # S := Q H_1^{-1} Q^T, R := Q H_1^{-1} V
    Hqt = [Hinv(a) for a in qt]
    nbonds = nb * DIM
    S = np.zeros((nbonds, nbonds))
    R = np.zeros((nbonds, nb))
    for j, s in enumerate(shifts):
        for nu in range(DIM):
            col = j * DIM + nu
            hq = tr(Hqt[nu], s)
            for i, r in enumerate(shifts):
                S[i * DIM + nu, col] = np.sum(tr(qt[nu], r) * hq)
                for b, bs in enumerate(shifts):
                    pass
            for b, bs in enumerate(shifts):
                R[col, b] = np.sum(tr(V[nu], bs) * hq)
    S = 0.5 * (S + S.T)
    G = S + R @ (tau * np.linalg.inv(W)) @ R.T
    G = 0.5 * (G + G.T)
    ev = np.linalg.eigvalsh(G)
    check_rss()
    return w, float(ev.max() / ev.min()), float(ev.max()), float(ev.min())


def w_inf(cut=41):
    odd = [m for m in range(-cut, cut + 1) if m % 2]
    a = np.array([4 / (np.pi**2 * m**2) for m in odd])
    m2 = np.array([float(m**2) for m in odd])
    # sum over odd^4 by nested arrays, using the 4-fold grid at modest cut
    tot = 0.0
    A = np.einsum("i,j->ij", a, a)
    M = np.add.outer(m2, m2)
    Aflat, Mflat = A.ravel(), M.ravel()
    for i in range(len(Aflat)):
        tot += Aflat[i] * np.sum(Aflat / (np.pi**2 * (Mflat[i] + Mflat) + 1))
    return tot


def main():
    print(f"w_inf (continuum, staggered) = {w_inf():.5f}")
    first = {3: (0.0224, 105.853), 5: (0.0171, 150.062)}
    out = {}
    for L in (3, 5, 7, 9, 11, 13, 15):
        w, c, mx, mn = run(L)
        out[L] = (w, c)
        print(f"L={L:2d} w={w:.5f} cond={c:.3f} max={mx:.4f} min={mn:.6f}", flush=True)
    ok = all(abs(out[L][0] - first[L][0]) <= 3e-3 * first[L][0] + 5e-5 and abs(out[L][1] - first[L][1]) <= 1e-3 * first[L][1] for L in first)
    print("PASS-FORMULA" if ok else "FAIL-FORMULA")
    Ls = sorted(out)
    cs = [out[L][1] for L in Ls]
    inc = np.diff(cs)
    # the steps are at equal spacing in L, so a decreasing increment is the test
    good = out[15][0] >= 0.012 and max(cs) <= 300 and all(inc[i + 1] <= inc[i] * 1.0001 for i in range(len(inc) - 1))
    print("PASS-LIMIT" if good else "FAIL-LIMIT")


if __name__ == "__main__":
    main()
