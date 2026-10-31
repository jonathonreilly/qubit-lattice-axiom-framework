#!/usr/bin/env python3
"""Exact abelian energy of the minimal composite lift of one top bond, N' = 2 or 4, k up to 7, by a Schwinger form of the alias sum.
Added after the registered list, to read the sequence of increments of D^2 Y_k at more levels than a lattice allows. Report only, except the check:
k = 1, 2 must reproduce the SU(2) solver at V = 1: n = 26.4786, 39.6288 (N' = 2, L = 3), to 1e-3.
g_mu(P) = sum over aliases of q_mu^2 / khat^2, q_mu = B D_mu prod_nu D_nu; 1/khat^2 = int dt exp(-t khat^2), so the 4-d alias sum factorises.
Energy of a transverse parent mode c at P: c^T (Perp^T G Perp)^-1 c B^d, as in hard-core--mapped_excess.py forms()."""
import itertools, sys
import numpy as np

def dirichlet(k, B):
    s = np.sin(k / 2)
    out = np.ones_like(k)
    m = np.abs(s) > 1e-14
    out[m] = np.sin(B * k[m] / 2) / (B * s[m])
    return out

def oneD(p, B, tgrid):
    r = np.arange(B) - (B - 1) // 2
    k = (p + 2 * np.pi * r) / B
    D2 = dirichlet(k, B) ** 2
    kh2 = 4 * np.sin(k / 2) ** 2
    ex = np.exp(-np.outer(tgrid, kh2))
    return ex @ D2, ex @ (D2 * D2), np.sum(D2 / np.maximum(kh2, 1e-300))

def G_diag(P, B):
    d = len(P)
    tmin, tmax = 1e-7, 4e3 * B**2
    u = np.linspace(np.log(tmin), np.log(tmax), 4000)
    t = np.exp(u)
    T1 = []; T2 = []
    for p in P:
        a, b, _ = oneD(p, B, t)
        T1.append(a); T2.append(b)
    G = np.zeros(d)
    for mu in range(d):
        integrand = T2[mu].copy()
        for nu in range(d):
            if nu != mu:
                integrand = integrand * T1[nu]
        G[mu] = B**2 * np.trapezoid(integrand * t, u)
    return G

def n_of_k(Np, L, k, mu=0):
    B = L**k
    tot = 0.0
    for ix in itertools.product(range(Np), repeat=4):
        P = 2 * np.pi * np.array(ix, float) / Np
        P = (P + np.pi) % (2 * np.pi) - np.pi
        Ph = 2 * np.sin(P / 2)
        P2 = np.sum(Ph**2)
        if P2 < 1e-12:
            continue
        G = np.diag(G_diag(P, B))
        u = Ph / P2**0.5
        Perp = np.linalg.svd(np.eye(4) - np.outer(u, u))[0][:, :3]
        M = B**4 * Perp @ np.linalg.inv(Perp.T @ G @ Perp) @ Perp.T / P2
        e = np.zeros(4); e[mu] = 1
        tot += P2 * e @ M @ e
    return tot / Np**4

for Np in [2, 4]:
    L = 3
    prev = 6.0
    pd = None
    for k in range(1, 8):
        n = n_of_k(Np, L, k)
        inc = n - prev
        print(f"N'={Np} L={L} k={k}: n={n:.6f} increment={inc:.6f} ratio={(inc/pd if pd else float('nan')):.4f} D2Y_k={2*(n-6):.6f}", flush=True)
        prev, pd = n, inc
