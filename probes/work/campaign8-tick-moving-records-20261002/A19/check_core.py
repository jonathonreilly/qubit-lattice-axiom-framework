#!/usr/bin/env python3
"""A19 check 0: validate the core toy (step, Bloch form, dispersion, band packet velocity, single-site kernels)."""
import numpy as np
from core1d import (step, step_layers_sites, bloch_U, vgroup, plus_band, packet, PI)

rng = np.random.default_rng(1)

# (1) fast step == explicit pair gates of the A13 round (theta_e = pi/2, theta_o = pi/2 - m)
err = 0.0
for m in (0.0, 0.3, 0.6, 1.2):
    N = 16
    psi = rng.normal(size=N) + 1j * rng.normal(size=N)
    ref = step_layers_sites(psi, m)
    a, b = step(psi[0::2][None], psi[1::2][None], m)
    out = np.empty(N, complex); out[0::2] = a[0]; out[1::2] = b[0]
    err = max(err, np.abs(out - ref).max())
print(f"(1) fast step vs explicit pair gates: max |diff| = {err:.1e}")

# (2) Bloch form on plane waves, (3) dispersion cos W = cos m cos K and band vector / velocity sign
e2 = e3 = e4 = 0.0
M = 64
for m in (0.1, 0.6, 1.3):
    for kk in (3, 11, 40):
        K = 2 * PI * kk / M
        A, Bv = rng.normal(size=2) + 1j * rng.normal(size=2)
        j = np.arange(M)
        a, b = step((A * np.exp(1j * K * j))[None], (Bv * np.exp(1j * K * j))[None], m)
        U = bloch_U(K, m)
        Ap, Bp = U @ np.array([A, Bv])
        e2 = max(e2, np.abs(a[0] - Ap * np.exp(1j * K * j)).max(), np.abs(b[0] - Bp * np.exp(1j * K * j)).max())
        lam = np.linalg.eigvals(U)
        W = np.arccos(np.cos(m) * np.cos(K))
        e3 = max(e3, np.min(np.abs(np.sort(np.angle(-lam)) - np.sort([-W, W]))))
        uA, uB = plus_band(K, m)
        u = np.array([uA, uB])
        e4 = max(e4, np.abs(U @ u - (-np.exp(-1j * W)) * u).max())
print(f"(2) Bloch matrix vs step on plane waves: {e2:.1e}")
print(f"(3) eigenphases of -U are +-W with cos W = cos m cos K: {e3:.1e};  plus_band is the -e^(-iW) eigenvector: {e4:.1e}")

# (4) packet centroid velocity (no registration) vs v(K0), cells per tick
M = 2048
for m, K0 in ((0.6, 0.3), (0.3, 0.1), (1.0, 0.8), (0.6, -0.3)):
    a, b = packet(M, m, K0, w=20.0, j0=M // 2)
    a, b = a[None], b[None]
    x = np.arange(M)
    def cen(a, b):
        return np.sum(np.abs(a[0]) ** 2 * x + np.abs(b[0]) ** 2 * (x + 0.5))
    c0 = cen(a, b)
    T = 200
    for t in range(T):
        a, b = step(a, b, m)
    v = (cen(a, b) - c0) / T
    print(f"(4) m={m} K0={K0}: packet velocity {v:.5f} vs v(K0) = {vgroup(K0, m):.5f}  (diff {v - vgroup(K0, m):.1e})")

# (5) one tick from a right-sublattice site: P(+1 cell) = cos^2 m, P(+1/2 cell) = sin^2 m
M = 64
for m in (0.3, 1.0):
    a = np.zeros((1, M), complex); b = np.zeros((1, M), complex); a[0, 10] = 1
    a, b = step(a, b, m)
    print(f"(5) m={m}: one tick from site 2j: P(site 2j+2) = {abs(a[0,11])**2:.6f} (cos^2 m = {np.cos(m)**2:.6f}), "
          f"P(site 2j+1) = {abs(b[0,10])**2:.6f} (sin^2 m = {np.sin(m)**2:.6f})")

# (6) long-time mean velocity after a right-sublattice cut: <v>_R = 1 - sin m (cells/tick);  E[V^2] = 1 - sin m
# (7) p_RR(n) = 1 - int dK/2pi sin^2(n W) sin^2 m / sin^2 W
M = 4096
for m in (0.15, 0.6, 1.2):
    a = np.zeros((1, M), complex); b = np.zeros((1, M), complex); a[0, M // 2] = 1
    x = np.arange(M) - M // 2
    n_end = 1500
    Kq = 2 * PI * (np.arange(20000) + 0.5) / 20000
    W = np.arccos(np.cos(m) * np.cos(Kq))
    rows = []
    for n in range(1, n_end + 1):
        a, b = step(a, b, m)
        if n in (1, 2, 5, 50, 1500):
            pa, pb = np.abs(a[0]) ** 2, np.abs(b[0]) ** 2
            pRR = pa.sum()
            pred = 1 - np.mean(np.sin(n * W) ** 2 * np.sin(m) ** 2 / np.sin(W) ** 2)
            mean = np.sum(pa * x + pb * (x + 0.5))
            m2 = np.sum(pa * x ** 2 + pb * (x + 0.5) ** 2)
            rows.append((n, pRR, pred, mean / n, m2 / n ** 2))
    for n, pRR, pred, v, v2 in rows:
        print(f"(6,7) m={m} n={n}: p_RR = {pRR:.6f} (formula {pred:.6f}); mean disp/n = {v:.5f}; E[x^2]/n^2 = {v2:.5f}"
              + (f"   [limits 1-sin m = {1-np.sin(m):.5f}, p_RR(inf) = 1 - sin(m)/2 = {1-np.sin(m)/2:.5f}]" if n == 1500 else ""))
