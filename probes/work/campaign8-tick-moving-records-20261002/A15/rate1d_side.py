#!/usr/bin/env python3
"""A15: rate 2:1 seam, sideband check: fraction of the transmitted weight (both sublattices) within +-0.2 of the
dominant cell momentum; any second peak (e.g. doubler at K+pi) reported."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
import rate1d
from seam1d import ublock, packet, branch

def run_full(th, K0, side, N=700, s=300, sigma=12.0):
    u = ublock(th)
    vg, w, _ = branch(K0, u, +1 if side == 'A' else -1)
    if side == 'A':
        psi = packet(N, s // 2 - 58, K0, sigma, u, +1); psi[s:] = 0
        H = 2 * (int(2 * 116 / abs(vg)) + 30)
    else:
        psi = packet(N + 2, s // 2 + 58, K0, sigma, u, -1)[0:N].copy(); psi[:s] = 0
        H = 2 * (int(116 / abs(vg)) + 30)
    psi = psi.astype(complex) / np.linalg.norm(psi)
    acted = {}
    for h in range(H):
        for (x, y) in rate1d.step_pairs(N, s, h, 0, 0, acted):
            a, b = psi[x], psi[y]
            psi[x] = u[0, 0] * a + u[0, 1] * b
            psi[y] = u[1, 0] * a + u[1, 1] * b
    part = psi.copy()
    if side == 'A': part[:s] = 0
    else: part[s:] = 0
    M = 8192
    f = np.abs(np.fft.fft(part[0::2], M)) ** 2 + np.abs(np.fft.fft(part[1::2], M)) ** 2
    Ks = (2 * np.pi * np.fft.fftfreq(M)) % (2 * np.pi)
    k1 = Ks[np.argmax(f)]
    near = np.abs(np.angle(np.exp(1j * (Ks - k1)))) < 0.5
    frac = f[near].sum() / f.sum()
    g = f.copy(); g[near] = 0
    k2 = Ks[np.argmax(g)]
    near2 = np.abs(np.angle(np.exp(1j * (Ks - k2)))) < 0.2
    return np.sum(np.abs(part) ** 2), k1, frac, k2, f[near2].sum() / f.sum()

for th, K0, side in ((np.pi / 4, 2.742, 'A'), (np.pi / 4, 2.171, 'A'), (np.pi / 4, 2.742, 'B'), (0.3, 2.742, 'A'), (0.3, 2.742, 'B'), (np.pi / 2, 2.742, 'B')):
    tr, k1, frac, k2, frac2 = run_full(th, K0, side)
    print("theta=%.3f K0=%.3f from %s: transmitted %.4f; main peak K=%.3f holds (within +-0.5) %.4f of it; largest outside: peak K=%.3f holds %.4f"
          % (th, K0, side, tr, k1, frac, k2, frac2))
