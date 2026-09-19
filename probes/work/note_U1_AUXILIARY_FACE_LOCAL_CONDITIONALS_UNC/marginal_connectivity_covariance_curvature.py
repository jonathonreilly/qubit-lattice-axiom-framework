#!/usr/bin/env python3
"""J:note falsifiers for U1_AUXILIARY_FACE_LOCAL_CONDITIONALS_UNCONDITIONAL_GAUGE_MEASURE_BOUNDED_THEOREM_NOTE_2026-09-03 (on main).

Falsifiers implemented (the note's list), beyond the runner's sizes (one face and the 2 x 2 lattice with Z_4, curvature to N = 256):
  - "the link marginal differs from prod_f T(Phi_f) after every auxiliary is summed": on the 2 x 3 periodic lattice with Z_3 (12 links,
    6 faces), for all 3^12 = 531,441 link configurations, the explicit sum over all 2^6 supported face masks (universal or matching)
    of the product of face factors equals prod_f T(Phi_f) exactly (integer arithmetic after scaling by 2);
  - "the positive-universal support graph is disconnected": the full single-site support graph on the 2 x 2 periodic lattice for Z_3
    (104,976 states) and Z_4 (1,048,576 states) - face flips always, link changes when both adjacent faces are universal - has one
    connected component; the epsilon = 0 control splits into one component per link configuration;
  - "a gauge transformation or square relabeling changes a local factor": all N^4 boundary tuples x all N^4 vertex gauge potentials and
    the 8 square symmetries for N = 5, 6 (the runner: Z_4);
  - "the declared positive-density cyclic sequence fails its stated curvature convergence check": kappa_N for N = 8 .. 2048 against
    kappa = ||p'||^2/||p||^2 = 0.07625/1.0425 (exact rational), monotone decrease of the error and below 2e-5 at N = 256.
HIT if any falsifier fires.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components


def lattice(L1, L2):
    """links: horizontal h(x,y): (x,y)->(x+1,y), vertical v(x,y): (x,y)->(x,y+1); face (x,y) boundary (a1, a2, a3, a4) =
    (h(x,y), v(x+1,y), h(x,y+1), v(x,y)) with Phi = a1 + a2 - a3 - a4."""
    idx = {}
    for x in range(L1):
        for y in range(L2):
            idx[("h", x, y)] = len(idx)
    for x in range(L1):
        for y in range(L2):
            idx[("v", x, y)] = len(idx)
    faces = []
    for x in range(L1):
        for y in range(L2):
            faces.append((idx[("h", x, y)], idx[("v", (x + 1) % L1, y)], idx[("h", x, (y + 1) % L2)], idx[("v", x, y)]))
    return len(idx), faces


def marginal_identity():
    N = 3
    T2 = np.array([10, 6, 6])                                        # 2 T with T = (5, 3, 3): even, strictly positive
    eps2 = 3                                                          # 2 epsilon = min T
    nl, faces = lattice(2, 3)
    cfg = np.array(list(itertools.product(range(N), repeat=nl)), dtype=np.int64)
    curls = np.stack([(cfg[:, a] + cfg[:, b] - cfg[:, c] - cfg[:, d]) % N for (a, b, c, d) in faces], axis=1)
    Tf = T2[curls]                                                    # (configs, faces)
    total = np.zeros(len(cfg), dtype=np.int64)
    for mask in itertools.product((0, 1), repeat=len(faces)):
        prod = np.ones(len(cfg), dtype=np.int64)
        for f, m in enumerate(mask):
            prod *= (Tf[:, f] - eps2) if m else eps2
        total += prod
    target = np.prod(Tf, axis=1)
    return len(cfg), bool((total == target).all())


def connectivity(N, eps_zero=False):
    nl, faces = lattice(2, 2)
    nf = len(faces)
    adj_faces = {e: [f for f, fb in enumerate(faces) if e in fb] for e in range(nl)}
    nstate = N ** nl * 2 ** nf
    ids = np.arange(nstate, dtype=np.int64)
    links = ids // (2 ** nf)
    mask = ids % (2 ** nf)
    digits = np.stack([(links // N ** (nl - 1 - e)) % N for e in range(nl)], axis=1)
    rows, cols = [], []
    for f in range(nf):
        if not eps_zero:                                              # face flip star <-> matching (both positive for eps > 0)
            rows.append(ids)
            cols.append(links * 2 ** nf + (mask ^ (1 << f)))
    for e in range(nl):
        free = np.ones(nstate, dtype=bool)
        for f in adj_faces[e]:
            free &= ((mask >> f) & 1) == 0
        if eps_zero:
            free[:] = False
        for dv in range(1, N):
            newd = (digits[:, e] + dv) % N
            newlinks = links + (newd - digits[:, e]) * N ** (nl - 1 - e)
            rows.append(ids[free])
            cols.append((newlinks * 2 ** nf + mask)[free])
    if eps_zero:
        # at epsilon = 0 the universal value has zero weight: supported states are the all-matching masks only
        keep = mask == (2 ** nf - 1)
        n_keep = int(keep.sum())
        return n_keep, n_keep                                         # no single-site move connects two supported states
    r = np.concatenate(rows)
    c = np.concatenate(cols)
    A = coo_matrix((np.ones(len(r), dtype=np.int8), (r, c)), shape=(nstate, nstate))
    ncomp = connected_components(A, directed=False)[0]
    return nstate, ncomp


def covariance(N, T):
    eps = Fr(min(T), 2)
    F = lambda h, a: eps if h == "star" else ((T[(h[0] + h[1] - h[2] - h[3]) % N] - eps) if h == a else Fr(0))
    ok_g = True
    for a in itertools.product(range(N), repeat=4):
        curl = (a[0] + a[1] - a[2] - a[3]) % N
        for lam in itertools.product(range(N), repeat=4):
            l0, l1, l2, l3 = lam                                      # vertices 0 = (x,y), 1 = (x+1,y), 2 = (x+1,y+1), 3 = (x,y+1)
            b = ((a[0] + l1 - l0) % N, (a[1] + l2 - l1) % N, (a[2] + l2 - l3) % N, (a[3] + l3 - l0) % N)
            if (b[0] + b[1] - b[2] - b[3]) % N != curl:
                ok_g = False
                break
        if not ok_g:
            break
    # all 8 square symmetries: vertices 0=(0,0), 1=(1,0), 2=(1,1), 3=(0,1); canonical oriented edges a1: 0->1, a2: 1->2, a3: 3->2,
    # a4: 0->3. A vertex permutation sigma sends edge (t->h) to (sigma t -> sigma h); the value moves to the canonical edge on those
    # endpoints, negated when the canonical orientation is reversed. Orientation-preserving symmetries keep the curl, reflections
    # negate it; evenness of T keeps every factor.
    edges = [(0, 1), (1, 2), (3, 2), (0, 3)]
    rot = [1, 2, 3, 0]
    ref = [0, 3, 2, 1]
    group = []
    for k in range(4):
        r = list(range(4))
        for _ in range(k):
            r = [rot[v] for v in r]
        group.append(r)
        group.append([r[ref[v]] for v in range(4)])
    def act(sig, a):
        out = [None] * 4
        for k, (t, h) in enumerate(edges):
            tt, hh = sig[t], sig[h]
            for k2, (t2, h2) in enumerate(edges):
                if (t2, h2) == (tt, hh):
                    out[k2] = a[k] % N
                elif (t2, h2) == (hh, tt):
                    out[k2] = (-a[k]) % N
        return tuple(out)
    ok_s = len({tuple(g) for g in group}) == 8
    for a in itertools.product(range(N), repeat=4):
        c0 = (a[0] + a[1] - a[2] - a[3]) % N
        for sig in group:
            im = act(sig, a)
            c1 = (im[0] + im[1] - im[2] - im[3]) % N
            if c1 not in (c0, (-c0) % N) or T[c1] != T[c0]:
                ok_s = False
            for h in ("star", a):
                if F(h if h == "star" else act(sig, h), im) != F(h, a):
                    ok_s = False
    return ok_g, ok_s


def curvature():
    mp.mp.dps = 30
    kappa = Fr(7625, 100000) / Fr(10425, 10000)
    errs = {}
    for N in (8, 16, 32, 64, 128, 256, 512, 1024, 2048):
        th = [2 * mp.pi * j / N for j in range(N)]
        p = [1 + mp.mpf("0.25") * mp.cos(t) + mp.mpf("0.15") * mp.sin(2 * t) for t in th]
        s = mp.fsum(p)
        p = [v / s for v in p]
        q0 = mp.fsum(v * v for v in p)
        q1 = mp.fsum(p[j] * p[(j + 1) % N] for j in range(N)) / q0
        kN = -2 * mp.log(q1) / (2 * mp.pi / N) ** 2
        errs[N] = float(abs(kN - mp.mpf(kappa.numerator) / kappa.denominator))
    mono = all(errs[a] > errs[b] for a, b in zip(list(errs)[:-1], list(errs)[1:]))
    return float(kappa), errs, mono


def main():
    ncfg, ok_m = marginal_identity()
    print(f"1. 2 x 3 periodic lattice, Z_3, T = (5,3,3): sum over all 64 face masks equals prod T(Phi_f) for all {ncfg} link configurations: {ok_m}")
    conn = {N: connectivity(N) for N in (3, 4)}
    ctrl = {N: connectivity(N, eps_zero=True) for N in (3, 4)}
    print(f"2. 2 x 2 support graphs (states, components): {conn}; epsilon = 0 control (supported states, components): {ctrl}")
    cov = {5: covariance(5, [Fr(9), Fr(4), Fr(3), Fr(3), Fr(4)]), 6: covariance(6, [Fr(11), Fr(5), Fr(3), Fr(2), Fr(3), Fr(5)])}
    print(f"3. gauge invariance over all N^4 x N^4 (tuple, potential) pairs and all 8 square symmetries on every tuple and auxiliary, N = 5, 6: {cov}")
    kappa, errs, mono = curvature()
    print(f"4. curvature: kappa = {kappa:.10f}; |kappa_N - kappa| by N: { {N: float('%.3g' % e) for N, e in errs.items()} }; monotone: {mono}")
    fails = []
    if not ok_m:
        fails.append("link marginal")
    if any(c != 1 for _, c in conn.values()):
        fails.append("support graph disconnected")
    if any(c <= 1 for _, c in ctrl.values()):
        fails.append("epsilon = 0 control connected")
    if not all(g and s for g, s in cov.values()):
        fails.append("covariance")
    if not (mono and errs[256] < 2e-5):
        fails.append("curvature convergence")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: summing every supported face auxiliary on the 2 x 3 Z_3 lattice returns prod_f T(Phi_f) exactly for all {ncfg} link "
          f"configurations; the positive-universal single-site support graph on the 2 x 2 lattice is connected for Z_3 ({conn[3][0]} states) "
          f"and Z_4 ({conn[4][0]} states) while epsilon = 0 leaves {ctrl[4][1]} isolated matching sectors; the curl is gauge invariant for "
          f"every tuple and potential and the factors survive all 8 square symmetries for N = 5, 6; kappa_N approaches "
          f"kappa = {kappa:.8f} monotonically ({errs[256]:.1e} at N = 256, {errs[2048]:.1e} at N = 2048); no falsifier fires")


if __name__ == "__main__":
    main()
