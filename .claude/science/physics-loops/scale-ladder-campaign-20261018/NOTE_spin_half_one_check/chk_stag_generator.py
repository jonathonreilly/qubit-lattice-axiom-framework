#!/usr/bin/env python3
"""Floating-point diagnostic (not a proof): the staggered timing's induced generator at uniform xi = e_0,
acting on the field strength of a smooth A. Splits D T' A into its Fourier components at the smooth momenta
of A and at the 7 doubler-shifted momenta, and compares the smooth part with the forward generator's
(F - T^-1 F ~ a d_0 F)."""
import sys
import numpy as np
from chk_lattice import Geo, pair_coeffs, induced, Fr

def T_of(g, U, W):
    X = induced(g, pair_coeffs(g, U, W))
    nL = len(g.links)
    T = np.zeros((nL, nL))
    for s in g.sites:
        for (l, b), v in X[(s, 0)].items():
            T[l, b] += float(v)
    return T

for L in [int(a) for a in sys.argv[1:]] or [8, 12, 16]:
    g = Geo(L)
    Us = [{x: Fr(1)} if sum(x) % 2 == 0 else {g.sh(x, j): Fr(1)} for (x, j) in g.links]
    Ws = [{s: Fr(1, 2) for s in g.corners(p).values() if sum(s) % 2 == 1} for p in range(len(g.plaqs))]
    Uf = [{x: Fr(1)} for (x, j) in g.links]
    Wf = [{g.plaqs[p][0]: Fr(1)} for p in range(len(g.plaqs))]
    Ts, Tf = T_of(g, Us, Ws), T_of(g, Uf, Wf)
    k = 2 * np.pi / L
    A = np.zeros(len(g.links))
    for l, (x, j) in enumerate(g.links):
        A[l] = [np.sin(k * x[0] + 2 * k * x[1]), np.cos(k * x[2] - k * x[0]), np.sin(k * (x[0] + x[1] + x[2]))][j]
    res = {}
    for name, T in (("stag", Ts), ("fwd", Tf)):
        Fv = g.D @ (T @ A)
        # per plane: arrange on the grid and FFT
        smooth = dbl = 0.0
        for pi_, ij in enumerate(((0, 1), (0, 2), (1, 2))):
            arr = np.zeros((L, L, L))
            for p, (y, pl) in enumerate(g.plaqs):
                if pl == ij:
                    arr[y] = Fv[p]
            sp_ = np.abs(np.fft.fftn(arr)) ** 2
            idx = np.indices((L, L, L)).reshape(3, -1).T
            for n_ in idx:
                m = np.minimum(n_, L - n_)
                mh = np.minimum(np.abs(n_ - L // 2), L - np.abs(n_ - L // 2))
                v = sp_[tuple(n_)]
                if np.all(m <= 3):
                    smooth += v
                elif np.all(np.minimum(m, mh) <= 3):
                    dbl += v
        res[name] = (np.sqrt(smooth), np.sqrt(dbl))
    Fs, Ff = g.D @ (Ts @ A), g.D @ (Tf @ A)
    # smooth-part comparison: low-pass both and compare
    print(f"L={L}: |smooth(D T' A)| / |smooth(D T_fwd A)| = {res['stag'][0] / res['fwd'][0]:.4f};"
          f" doubler-momentum part of D T' A relative to its smooth part = {res['stag'][1] / res['stag'][0]:.4f};"
          f" (fwd: {res['fwd'][1] / res['fwd'][0]:.2e})", flush=True)
