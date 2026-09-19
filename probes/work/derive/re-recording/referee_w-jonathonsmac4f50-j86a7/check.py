#!/usr/bin/env python3
"""Referee check for J:derive:re-recording:a1 (author w-macbookpro90c72-j5e15, grok-4.6); referee w-jonathonsmac4f50-j86a7.

Independent code (exact integers/Fractions, numpy for spectra).

V1  step 1: async heat-bath detailed balance w.r.t. the static law, exhaustive on the 4-cycle (Ising, t = e^beta = 2) and on a six-axis
    3-site path at (3,1,2).
V2  step 2: the bilinear identity sum_x s'_x.S_x(s) = sum_x s_x.S_x(s') for the 6-stencil on (Z/4)^3, random pairs.
V3  step 3: the Laplacian of Gamma_6 (two layers, (x,0)-(y,1) for nearest neighbours) on (Z/4)^3: spectrum = {E(k)} u {12 - E(k)};
    number of zero eigenvalues and connected components (Gamma_6 splits into two components on even tori); with the self-loop
    (7-stencil) the odd corner eigenvalue is 2 and the graph is connected.
V4  step 4: on the L = 2 torus with the doubled 6-stencil, six-axis (3,1,2): sync P(all +x) = Z_1^8/Z_sync; the MATCHED static law
    (the async stationary law of the same stencil: every nearest-neighbour pair carries phi^2) P(all +x) = p^24/Z; and the attempt's
    comparator p^12/Z_cube on the isolated cube (12 single bonds) = 59049/775835648; the sync law's factorisation over the two sublattices.
V5  step 5: log(sinh k/k) = k^2/6 - k^4/180 + ...; the 6-sum's |S|^2 has symbol (6 - E)^2 (mode check).
"""
from __future__ import annotations

import itertools
import math
import random
from fractions import Fraction as F

import numpy as np
import sympy as sp

AXES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi6(a, b, p=3, q=1, r=2):
    d = sum(x * y for x, y in zip(AXES[a], AXES[b]))
    return p if d == 1 else (q if d == -1 else r)


def v1():
    # 4-cycle Ising: static w(s) = t^{sum_bonds s_x s_y}; heat bath at x: P(s_x = v | rest) prop. t^{v * sum nbrs}
    t = F(2)
    n = 4
    nb = {x: [(x - 1) % n, (x + 1) % n] for x in range(n)}
    bonds = [(x, (x + 1) % n) for x in range(n)]

    def w(s):
        return t ** sum(s[a] * s[b] for a, b in bonds)
    ok = True
    for s in itertools.product((-1, 1), repeat=n):
        for x in range(n):
            h = sum(s[y] for y in nb[x])
            for v in (-1, 1):
                s2 = list(s)
                s2[x] = v
                s2 = tuple(s2)
                Kf = t ** (v * h) / (t ** h + t ** (-h))
                Kb = t ** (s[x] * h) / (t ** h + t ** (-h))
                ok &= w(s) * Kf == w(s2) * Kb
    # six-axis path a - b - c at (3,1,2): static prod phi over bonds; heat bath at each site
    ok2 = True
    bonds3 = [(0, 1), (1, 2)]
    nb3 = {0: [1], 1: [0, 2], 2: [1]}

    def w3(s):
        out = 1
        for a, b in bonds3:
            out *= phi6(s[a], s[b])
        return out
    for s in itertools.product(range(6), repeat=3):
        for x in range(3):
            Z = sum(_prod(phi6(u, s[y]) for y in nb3[x]) for u in range(6))
            for u in range(6):
                s2 = list(s)
                s2[x] = u
                s2 = tuple(s2)
                ok2 &= F(w3(s)) * F(_prod(phi6(u, s[y]) for y in nb3[x]), Z) == F(w3(s2)) * F(_prod(phi6(s[x], s[y]) for y in nb3[x]), Z)
    return ok, ok2


def _prod(it):
    out = 1
    for v in it:
        out *= v
    return out


def v2(seed=2):
    rng = random.Random(seed)
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    N6 = {x: [tuple((x[i] + (d if i == j else 0)) % L for i in range(3)) for j in range(3) for d in (1, -1)] for x in sites}
    ok = True
    for _ in range(200):
        s = {x: AXES[rng.randrange(6)] for x in sites}
        t = {x: AXES[rng.randrange(6)] for x in sites}
        lhs = sum(sum(a * b for a, b in zip(t[x], s[y])) for x in sites for y in N6[x])
        rhs = sum(sum(a * b for a, b in zip(s[x], t[y])) for x in sites for y in N6[x])
        ok &= lhs == rhs
    return ok


def v3(L=4):
    sites = list(itertools.product(range(L), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    N = len(sites)

    def laplacian(selfloop):
        A = np.zeros((2 * N, 2 * N))
        for x in sites:
            for j in range(3):
                for d in (1, -1):
                    y = tuple((x[i] + (d if i == j else 0)) % L for i in range(3))
                    A[idx[x], N + idx[y]] += 1
                    A[N + idx[x], idx[y]] += 1
            if selfloop:
                A[idx[x], N + idx[x]] += 1
                A[N + idx[x], idx[x]] += 1
        deg = A.sum(axis=1)
        return np.diag(deg) - A
    ev6 = np.sort(np.linalg.eigvalsh(laplacian(False)))
    ev7 = np.sort(np.linalg.eigvalsh(laplacian(True)))
    ks = [2 * np.pi * np.array(n) / L for n in itertools.product(range(L), repeat=3)]
    E = np.array([2 * sum(1 - np.cos(k)) for k in ks])
    pred6 = np.sort(np.concatenate([E, 12 - E]))
    pred7 = np.sort(np.concatenate([E, 14 - E]))
    zeros6 = int(np.sum(np.abs(ev6) < 1e-9))
    zeros7 = int(np.sum(np.abs(ev7) < 1e-9))
    return np.allclose(ev6, pred6), np.allclose(ev7, pred7), zeros6, zeros7


def v4(p=3, q=1, r=2):
    sites = list(itertools.product((0, 1), repeat=3))
    idx = {x: i for i, x in enumerate(sites)}
    nbrs = {x: [tuple((x[i] + (1 if i == j else 0)) % 2 for i in range(3)) for j in range(3)] for x in sites}
    stencil = {x: nbrs[x] * 2 for x in sites}  # the doubled 6-stencil on L = 2
    pairs = sorted({tuple(sorted((idx[x], idx[y]))) for x in sites for y in nbrs[x]})
    Z1 = p ** 6 + q ** 6 + 4 * r ** 6
    even = [x for x in sites if sum(x) % 2 == 0]
    odd = [x for x in sites if sum(x) % 2 == 1]
    # structural fact: every stencil of an even site lies in the odd sublattice and vice versa, so
    # prod_x Z_x(s) = [prod_{x even} Z_x(s_odd)] [prod_{x odd} Z_x(s_even)] and Z_sync = Z_half(even) * Z_half(odd)
    only_other = all(all(sum(y) % 2 != sum(x) % 2 for y in stencil[x]) for x in sites)

    def z_half(targets, sources):
        tot = 0
        for vals in itertools.product(range(6), repeat=len(sources)):
            sv = dict(zip(sources, vals))
            tot += _prod(sum(_prod(phi6(u, sv[y], p, q, r) for y in stencil[x]) for u in range(6)) for x in targets)
        return tot
    Ze, Zo = z_half(even, odd), z_half(odd, even)
    sync = F(Z1 ** 8, Ze * Zo)
    # matched static law: phi^2 on each of the 12 nearest-neighbour pairs, exact int64 sum over 6^8 configurations
    W2 = np.array([[phi6(a, b, p, q, r) ** 2 for b in range(6)] for a in range(6)], dtype=np.int64)
    grid = np.array(list(itertools.product(range(6), repeat=8)), dtype=np.int64)
    w = np.ones(len(grid), dtype=np.int64)
    for a, b in pairs:
        w *= W2[grid[:, a], grid[:, b]]
    Zstat2 = int(w.sum())
    stat2 = F(p ** 24, Zstat2)
    # the attempt's comparator: the isolated cube with single bonds
    W1 = np.array([[phi6(a, b, p, q, r) for b in range(6)] for a in range(6)], dtype=np.int64)
    w1 = np.ones(len(grid), dtype=np.int64)
    for a, b in pairs:
        w1 *= W1[grid[:, a], grid[:, b]]
    cube = F(p ** 12, int(w1.sum()))
    return sync, stat2, cube, only_other, Ze == Zo, pairs


def v5():
    k = sp.Symbol("k", positive=True)
    ser = sp.series(sp.log(sp.sinh(k) / k), k, 0, 6).removeO()
    # mode check: for s_y = cos(k.y) e (a real mode), sum_x |S_x|^2 / sum_x |s_x|^2 = (2 sum cos k_j)^2 = (6 - E)^2
    L = 4
    sites = list(itertools.product(range(L), repeat=3))
    ok = True
    for n in [(1, 0, 0), (1, 1, 0), (2, 1, 3)]:
        kv = [2 * math.pi * c / L for c in n]
        f = {x: math.cos(sum(a * b for a, b in zip(kv, x))) for x in sites}
        S = {x: sum(f[tuple((x[i] + (d if i == j else 0)) % L for i in range(3))] for j in range(3) for d in (1, -1)) for x in sites}
        lhs = sum(S[x] ** 2 for x in sites) / sum(f[x] ** 2 for x in sites)
        E = 2 * sum(1 - math.cos(c) for c in kv)
        ok &= abs(lhs - (6 - E) ** 2) < 1e-9
    return sp.expand(ser), ok


def main():
    a1, a2 = v1()
    print(f"V1 async detailed balance: 4-cycle Ising (t = 2) exhaustive {a1}; six-axis 3-site path at (3,1,2) exhaustive {a2}")
    print(f"V2 6-stencil bilinear identity on (Z/4)^3, 200 random pairs: {v2()}")
    s6, s7, z6, z7 = v3()
    print(f"V3 (Z/4)^3: Gamma_6 Laplacian spectrum = {{E, 12 - E}}: {s6}, zero eigenvalues {z6} (two components); with the self-loop "
          f"spectrum = {{E, 14 - E}}: {s7}, zero eigenvalues {z7} (connected; odd corner eigenvalue 2)")
    sync, stat2, cube, only_other, sym = v4()[:5]
    print(f"V4 L = 2 torus, doubled 6-stencil, (3,1,2): stencils see only the other sublattice {only_other} (so pi_sync factorises over the two "
          f"sublattices; the two half-sums agree {sym}); sync P(all +x) = {sync} = {float(sync):.6e}; matched static (phi^2 on each pair) "
          f"P(all +x) = {stat2} = {float(stat2):.6e}; attempt's comparator (isolated cube, single bonds) = {cube} = {float(cube):.6e}")
    ser, ok5 = v5()
    print(f"V5 log(sinh k/k) = {ser} + ...; |S|^2 symbol (6 - E)^2 on three modes: {ok5}")
    ok_core = a1 and a2 and s6 and s7 and z6 == 2 and z7 == 1 and ok5
    if ok_core and sync != stat2:
        print("HIT: confirmed - async re-recording is the heat bath of the static law (exact detailed balance), sync is reversible w.r.t. prod Z "
              "(bilinear identity), Gamma_6's spectrum is {E, 12 - E} with the zone-corner zero mode (two zero eigenvalues: Gamma_6 has two "
              "components on even tori) against {E, 14 - E} with the self-loop, the small-beta symbol is (6 - E)^2, and the cube conclusion "
              f"'static and sync differ' holds against the MATCHED static law ({float(sync):.4e} vs {float(stat2):.4e})")
        print(f"SUMMARY: confirmed - the partial survives; corrections: step 4's static number 59049/775835648 is the isolated cube with single "
              f"bonds, not the async stationary law of the doubled L = 2 stencil used for sync (that one gives {float(stat2):.4e}); and the "
              "zone-corner kernel is not an open question: the sync law's stencils see only the other sublattice, so pi factorises over the two "
              "sublattices exactly (checked on L = 2) and the staggered channel is uncoupled")
    else:
        print(f"SUMMARY: fails - core {ok_core}, sync {sync} vs matched static {stat2}")


if __name__ == "__main__":
    main()
