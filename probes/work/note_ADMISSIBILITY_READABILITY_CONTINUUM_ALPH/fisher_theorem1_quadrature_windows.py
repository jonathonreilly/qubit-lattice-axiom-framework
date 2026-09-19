#!/usr/bin/env python3
"""J:note falsifier for ADMISSIBILITY_READABILITY_CONTINUUM_ALPHABET_FISHER_RANK_AND_FORMATION_ORDER_SECOND_ORDER (on main).

Falsifier implemented (the note's Falsifiers section, first bullet): "Any entry of the continuum Fisher matrix differing from Theorem 1 on any
finite window in Z^3". The note's runner checks the windows 2x3 and 2x2x2 only.

Theorem 1: in the basis [P1, P2, P3, P4, S1, H] at theta = 0 with the uniform sphere alphabet,
  I[Pi, Pj] = delta_ij |E|/(2i+1), I[S1, S1] = I[P1, S1] = |E|/9, I[Pk, S1] = 0 (k = 2..4), I[H, H] = 16 n/525, I[H, other] = 0.

Machinery (disjoint from the runner's monomial-moment expansion): the Fisher matrix is Cov(T_a, T_b) with T_a = sum_e f_a(e), T_H = sum_x H(v_x);
it is assembled pair by pair over the window's own edge pairs (same edge, edges sharing a vertex, straight or bent) and site-edge / site-site
pairs, each pair covariance computed by an exact product quadrature on S^2 (Gauss-Legendre in cos theta with 6 nodes, trapezoid in phi with
12 points: exact for every polynomial of degree <= 11 in the vector components; the integrands here have degree <= 8 per vector); disjoint
pairs are independent. Windows beyond the note's: the path P4, a plus shape, the 3x3 square, the 2x2x3 and 3x3x2 boxes and an irregular 3D
window of seven sites.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as F

import numpy as np

gl_u, gl_w = np.polynomial.legendre.leggauss(6)
NPHI = 12
phis = 2 * np.pi * np.arange(NPHI) / NPHI
U, PH = np.meshgrid(gl_u, phis, indexing="ij")
WQ = (np.outer(gl_w, np.full(NPHI, 1.0 / NPHI)) / 2).ravel()            # weights sum to 1 (probability measure)
S = np.sqrt(1 - U ** 2)
NODES = np.stack([(S * np.cos(PH)).ravel(), (S * np.sin(PH)).ravel(), U.ravel()], axis=1)   # (72, 3) unit vectors


def legendre(k, t):
    return {1: t, 2: (3 * t ** 2 - 1) / 2, 3: (5 * t ** 3 - 3 * t) / 2, 4: (35 * t ** 4 - 30 * t ** 2 + 3) / 8}[k]


def edge_feature(a, vx, vy, d):
    """a in 0..4: P1..P4 of the cosine, S1 = v_{x,d} v_{y,d}."""
    t = np.sum(vx * vy, axis=-1)
    return legendre(a + 1, t) if a < 4 else vx[..., d] * vy[..., d]


def H_site(v):
    return np.sum(v ** 4, axis=-1) - 3.0 / 5.0


def E2(f):
    """expectation over two independent uniform vectors of f(v1, v2)."""
    v1 = NODES[:, None, :]
    v2 = NODES[None, :, :]
    w = WQ[:, None] * WQ[None, :]
    return float(np.sum(w * f(v1, v2)))


def E3(f):
    v1 = NODES[:, None, None, :]
    v2 = NODES[None, :, None, :]
    v3 = NODES[None, None, :, :]
    w = WQ[:, None, None] * WQ[None, :, None] * WQ[None, None, :]
    return float(np.sum(w * f(v1, v2, v3)))


def E1(f):
    return float(np.sum(WQ * f(NODES)))


from functools import lru_cache


@lru_cache(maxsize=None)
def cov_same_edge(a, b, d):
    return (E2(lambda p, q: edge_feature(a, p, q, d) * edge_feature(b, p, q, d))
            - E2(lambda p, q: edge_feature(a, p, q, d)) * E2(lambda p, q: edge_feature(b, p, q, d)))


@lru_cache(maxsize=None)
def cov_wedge(a, b, d, d2):
    """edges (u, v) in direction d and (v, w) in direction d2 sharing the vertex v."""
    return (E3(lambda u, v, w: edge_feature(a, u, v, d) * edge_feature(b, v, w, d2))
            - E2(lambda p, q: edge_feature(a, p, q, d)) * E2(lambda p, q: edge_feature(b, p, q, d2)))


@lru_cache(maxsize=None)
def cov_site_edge(a, d):
    return E2(lambda v, w: H_site(v) * edge_feature(a, v, w, d)) - E1(H_site) * E2(lambda v, w: edge_feature(a, v, w, d))


def fisher(sites, edges):
    """edges: list of (x, y, d) with y = x + e_d. Returns the 6x6 covariance of the tangent statistics, assembled pair by pair."""
    I = np.zeros((6, 6))
    for e, f in itertools.product(edges, repeat=2):
        shared = {e[0], e[1]} & {f[0], f[1]}
        for a in range(5):
            for b in range(5):
                if e == f:
                    I[a, b] += cov_same_edge(a, b, e[2])
                elif len(shared) == 1:
                    I[a, b] += cov_wedge(a, b, e[2], f[2])
    var_H = E1(lambda v: H_site(v) ** 2) - E1(H_site) ** 2
    for x in sites:
        I[5, 5] += var_H
        for e in edges:
            if x in (e[0], e[1]):
                for a in range(5):
                    c = cov_site_edge(a, e[2])
                    I[5, a] += c
                    I[a, 5] += c
    return I


def predicted(n, nE):
    P = np.zeros((6, 6))
    for i in range(4):
        P[i, i] = nE / (2 * (i + 1) + 1)
    P[4, 4] = nE / 9
    P[0, 4] = P[4, 0] = nE / 9
    P[5, 5] = 16 * n / 525
    return P


def window(sites):
    sset = set(sites)
    edges = []
    for x in sites:
        for d in range(3):
            y = tuple(x[i] + (1 if i == d else 0) for i in range(3))
            if y in sset:
                edges.append((x, y, d))
    return sites, edges


WINDOWS = {
    "P4": [(i, 0, 0) for i in range(4)],
    "plus5": [(1, 1, 0), (0, 1, 0), (2, 1, 0), (1, 0, 0), (1, 2, 0)],
    "3x3": [(i, j, 0) for i in range(3) for j in range(3)],
    "2x2x3": [(i, j, k) for i in range(2) for j in range(2) for k in range(3)],
    "3x3x2": [(i, j, k) for i in range(3) for j in range(3) for k in range(2)],
    "irregular7": [(0, 0, 0), (1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 1), (0, 0, 1), (0, 1, 1)],
}


def main():
    # sanity of the quadrature: sphere moments against the declared formula
    mom_ok = abs(E1(lambda v: v[..., 0] ** 8) - 1 / 9) < 1e-13 and abs(E1(lambda v: v[..., 0] ** 4 * v[..., 1] ** 4) - 1 / 105) < 1e-13
    print(f"quadrature: E[x^8] = 1/9 and E[x^4 y^4] = 1/105 to 1e-13: {mom_ok}")
    worst = 0.0
    results = []
    for name, pts in WINDOWS.items():
        sites, edges = window(pts)
        I = fisher(sites, edges)
        P = predicted(len(sites), len(edges))
        dev = float(np.max(np.abs(I - P)))
        rank = int(np.linalg.matrix_rank(I, tol=1e-9))
        worst = max(worst, dev)
        wedges = sum(1 for (e, f) in itertools.combinations(edges, 2) if len({e[0], e[1]} & {f[0], f[1]}) == 1)
        results.append((name, len(sites), len(edges), wedges, dev, rank))
        print(f"{name}: n = {len(sites)}, |E| = {len(edges)}, wedges {wedges}: max |I - Theorem 1| = {dev:.2e}; rank {rank}; diag "
              f"{[str(F(v).limit_denominator(2000)) for v in np.diag(I)]}, I[P1,S1] = {F(I[0, 4]).limit_denominator(2000)}")
    if mom_ok and worst < 1e-10 and all(r == 6 for *_, r in results):
        print(f"SUMMARY: falsifier 'a continuum Fisher entry differs from Theorem 1 on a finite window' does not fire beyond the note's windows: "
              f"on P4, a plus shape, 3x3, 2x2x3, 3x3x2 and an irregular 3D window the pair-assembled covariance (exact sphere quadrature) equals "
              f"Theorem 1's closed form to {worst:.1e}, with rank 6 on every window")
    else:
        print(f"HIT: Theorem 1 falsifier fires: max deviation {worst}, ranks {[r for *_, r in results]}")
        print("SUMMARY: falsifier fired; see the lines above")


if __name__ == "__main__":
    main()
