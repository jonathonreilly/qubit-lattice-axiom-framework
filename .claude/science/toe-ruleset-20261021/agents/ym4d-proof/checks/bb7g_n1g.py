"""bb7g: reproduction of Lemma N1G (REVIEW_BFT_B_S6 D.4), lane B session 7.

Criteria: checks/bb7g_criteria.md (written before this script). Exact FFT inversion of the mean-zero Green function of -Delta
on the 4D torus of side M; cycle heat kernel by its exact eigen-sum.
"""
import time

import numpy as np

T0 = time.time()
out = []


def green4(M):
    k = 2 * np.pi * np.arange(M) / M
    lam1 = 2 - 2 * np.cos(k)
    kr = 2 * np.pi * np.arange(M // 2 + 1) / M
    lamr = 2 - 2 * np.cos(kr)
    lam = (lam1[:, None, None, None] + lam1[None, :, None, None] + lam1[None, None, :, None]
           + lamr[None, None, None, :])
    lam[0, 0, 0, 0] = 1.0
    inv = 1.0 / lam
    inv[0, 0, 0, 0] = 0.0
    del lam
    G = np.fft.irfftn(inv, s=(M, M, M, M))  # = M^{-4} sum_xi e^{i xi y}/lambda(xi)
    return G


def tv1(G):
    return np.abs(np.roll(G, -1, axis=0) - G).sum()


ok = True
g1 = []
for M in (8, 12, 16, 24, 32, 48):
    G = green4(M)
    s = tv1(G)
    dev = abs(s - M / 4)
    p = dev <= 1e-8 * M
    ok &= p
    # G6 informational
    y = np.arange(M)
    yd = np.minimum(y, M - y).astype(float)
    r = np.sqrt(yd[:, None, None, None] ** 2 + yd[None, :, None, None] ** 2 + yd[None, None, :, None] ** 2
                + yd[None, None, None, :] ** 2)
    grad = np.abs(np.roll(G, -1, axis=0) - G)
    # distance of the link midpoint is ~ r; use r at the link tail, excluding the origin links
    r3 = (r ** 3 * grad)
    r3[r < 1.5] = 0.0
    g1.append(f"M = {M}: sum|grad_1 G| = {s:.10f}, M/4 = {M / 4:.4f}, dev {dev:.1e} [{'PASS' if p else 'FAIL'}]; "
              f"max |y|^3|grad G| (|y| >= 1.5) = {r3.max():.4f}")
    del G, r, grad, r3
out.append("G1 (M even):")
out += ["  " + x for x in g1]
G1 = ok

ok2 = True
for M in (9, 15):
    G = green4(M)
    s = tv1(G)
    pred = (M * M - 1) / (4 * M)
    dev = abs(s - pred)
    p = dev <= 1e-8 * M and s < M / 4
    ok2 &= p
    out.append(f"G2 M = {M}: sum|grad_1 G| = {s:.10f}, (M^2-1)/(4M) = {pred:.10f}, dev {dev:.1e} [{'PASS' if p else 'FAIL'}]")
G2 = ok2

ok3 = True
worst = 0.0
for M in (8, 9, 16, 32, 48):
    xi = 2 * np.pi * np.arange(M) / M
    lam = 2 - 2 * np.cos(xi)
    x = np.arange(M)
    for t in (0.1, 0.5, 1.0, 4.0, 16.0, 64.0, float(M * M)):
        q = (np.exp(-t * lam)[None, :] * np.cos(np.outer(x, xi))).sum(axis=1) / M
        h = M // 2
        inc = (q[1:h + 1] - q[:h]).max()
        rel = inc / q.max()
        worst = max(worst, rel)
        ok3 &= rel <= 1e-14
out.append(f"G3 cycle heat kernel unimodal: worst max(q(x+1) - q(x))/max q = {worst:.2e} [{'PASS' if ok3 else 'FAIL'}]")
G3 = ok3

ok4 = True
worst4 = 0.0
for M in (8, 16):
    G = green4(M)
    h = M // 2
    sym = np.abs(G - np.roll(G[::-1], 1, axis=0)).max()
    inc = (G[1:h + 1] - G[:h]).max()
    v = max(sym, inc) / np.abs(G).max()
    worst4 = max(worst4, v)
    ok4 &= v <= 1e-12
out.append(f"G4 G_M(., y') symmetric and non-increasing in |y_1|: worst violation {worst4:.2e} [{'PASS' if ok4 else 'FAIL'}]")
G4 = ok4

ok5 = True
worst5 = 0.0
for M in (8, 16, 32):
    G = green4(M)
    g = G.sum(axis=(1, 2, 3))
    y = np.arange(M)
    yd = np.minimum(y, M - y).astype(float)
    f = -yd / 2 + yd ** 2 / (2 * M)
    f -= f.mean()
    dev = np.abs(g - f).max()
    worst5 = max(worst5, dev)
    ok5 &= dev <= 1e-10
    del G
out.append(f"G5 transverse sum = -|y|/2 + y^2/(2M) + c: worst deviation {worst5:.2e} [{'PASS' if ok5 else 'FAIL'}]")
G5 = ok5

allp = G1 and G2 and G3 and G4 and G5
out.append(f"VERDICT: {'ALL PASS' if allp else 'NOT ALL PASS'} (G1-G5)")
out.append(f"[t = {time.time() - T0:.1f} s]")
print("\n".join(out))
