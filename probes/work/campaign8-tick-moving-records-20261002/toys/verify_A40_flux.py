#!/usr/bin/env python3
"""Coordinator's check of A40 T5: a U(1) link field with flux pi (W = -1) through every square of the (coarse) cubic lattice
is mapped by every one of the 24 site-centred proper turns to a link field that again has W = -1 on every square
(so the rotated configuration is gauge-equivalent on the infinite lattice). Also: the same holds for a pi-flux field built with
random gauge phases (gauge invariance of the check)."""
import itertools
import numpy as np
L = 4
rng = np.random.default_rng(2)
def ks_links():
    U = np.zeros((L, L, L, 3), complex)
    for x, y, z in itertools.product(range(L), repeat=3):
        U[x, y, z, 0] = 1; U[x, y, z, 1] = (-1) ** x; U[x, y, z, 2] = (-1) ** (x + y)
    return U
def gauge(U):
    th = rng.uniform(0, 2 * np.pi, (L, L, L))
    V = U.copy()
    e = np.eye(3, dtype=int)
    for x, y, z in itertools.product(range(L), repeat=3):
        for a in range(3):
            n = tuple((np.array([x, y, z]) + e[a]) % L)
            V[x, y, z, a] = np.exp(1j * th[x, y, z]) * U[x, y, z, a] * np.exp(-1j * th[n])
    return V
def link(U, r, d):
    """oriented link from site r along unit vector d (d may be negative)"""
    a = int(np.argmax(np.abs(d)))
    if d[a] > 0:
        return U[tuple(np.array(r) % L) + (a,)]
    r2 = (np.array(r) + d) % L
    return np.conj(U[tuple(r2) + (a,)])
def fluxes(U):
    e = np.eye(3, dtype=int); out = []
    for r in itertools.product(range(L), repeat=3):
        r = np.array(r)
        for a, b in ((0, 1), (0, 2), (1, 2)):
            W = link(U, r, e[a]) * link(U, r + e[a], e[b]) * link(U, r + e[a] + e[b], -e[a]) * link(U, r + e[b], -e[b])
            out.append(W)
    return np.array(out)
def rotate(U, R):
    """push the link field forward by rotation R about the origin: U'(R r, R d) = U(r, d)"""
    V = np.zeros_like(U)
    e = np.eye(3, dtype=int)
    for r in itertools.product(range(L), repeat=3):
        r = np.array(r)
        for a in range(3):
            d = R @ e[a]; r2 = (R @ r) % L
            b = int(np.argmax(np.abs(d)))
            if d[b] > 0:
                V[tuple(r2) + (b,)] = U[tuple(r) + (a,)]
            else:
                V[tuple((r2 + d) % L) + (b,)] = np.conj(U[tuple(r) + (a,)])
    return V
rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3), int)
        for i in range(3): R[perm[i], i] = sg[i]
        if round(np.linalg.det(R)) == 1: rots.append(R)
for name, U in (("KS signs", ks_links()), ("KS + random gauge", gauge(ks_links()))):
    f0 = fluxes(U)
    worst = max(np.abs(fluxes(rotate(U, R)) + 1).max() for R in rots)
    print("%-18s: flux -1 on all %d squares: %s ; after each of %d turns, max |W+1| = %.1e" % (name, len(f0), np.allclose(f0, -1), len(rots), worst))
