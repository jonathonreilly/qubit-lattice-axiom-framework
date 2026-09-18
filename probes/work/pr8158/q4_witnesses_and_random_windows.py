#!/usr/bin/env python3
"""J:falsifier:PR8158 - block 24 (PR #8158), falsifier bullet D: "A plaquette, cube or forest value other than those of Q4, or a failure of
the average identity (D1-D4)", with the title's criterion ("the readings differ iff an unrecorded component touches two recorded sites")
tested beyond the note's three geometries.

Objects (the note's).  Six-axis menu M = {+-e_1, +-e_2, +-e_3}, phi = p (same), q (antipodal), r (orthogonal); recorded sites W, unrecorded
sites E, nearest-neighbour bonds of Z^3 inside W u E.  R1: mu_W^(1)(v) prop. to the W-bond product.  R2: the W-marginal of the law on W u E
prop. to the product over all bonds.  R3(.|omega): the W-law with the exterior records omega held.  TV = (1/2) sum |mu - nu|.
Machinery (disjoint from the runner's): integer weights (p, q, r integers), every configuration of W u E enumerated as an integer array
(numpy int64 products and exact int64 accumulation), exact rational TV from the integer marginals (Python integers); R3 and the average
identity computed per exterior configuration.  Beyond the note: random connected windows of 6-8 sites in a 3 x 3 x 3 box with a random
W/E split and random integer couplings in [1, 7]^3; each window is classified by its unrecorded components (every component touching at
most one recorded site = 'pendant', else 'bridging').
HIT if a Q4 value differs, the average identity fails, a pendant window has TV != 0 (Q2), or a bridging window at a non-constant rule has
TV = 0 (the title's criterion).  Deterministic (fixed seed), exact.
"""
import itertools
import random
import sys
import time
from fractions import Fraction as Fr

import numpy as np

VALS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def phi_matrix(p, q, r):
    M = np.zeros((6, 6), dtype=np.int64)
    for i, a in enumerate(VALS):
        for j, b in enumerate(VALS):
            M[i, j] = p if a == b else (q if all(x == -y for x, y in zip(a, b)) else r)
    return M


def bonds_of(sites):
    s = list(sites)
    idx = {x: i for i, x in enumerate(s)}
    out = []
    for x in s:
        for d in ((1, 0, 0), (0, 1, 0), (0, 0, 1)):
            y = (x[0] + d[0], x[1] + d[1], x[2] + d[2])
            if y in idx:
                out.append((idx[x], idx[y]))
    return out


def all_configs(n):
    return np.array(list(itertools.product(range(6), repeat=n)), dtype=np.int64) if n <= 5 else \
        np.stack(np.meshgrid(*[np.arange(6)] * n, indexing="ij"), -1).reshape(-1, n)


def weights(conf, bonds, M):
    w = np.ones(conf.shape[0], dtype=np.int64)
    for a, b in bonds:
        w = w * M[conf[:, a], conf[:, b]]
    return w


def readings(W, E, pqr):
    """exact R1 and R2 on W as integer weight vectors over 6^|W| configurations, plus the configurations."""
    M = phi_matrix(*pqr)
    sites = list(W) + list(E)
    nW = len(W)
    b_all = bonds_of(sites)
    b_W = [(a, b) for a, b in b_all if a < nW and b < nW]
    conf_all = all_configs(len(sites))
    w_all = weights(conf_all, b_all, M)
    code = np.zeros(conf_all.shape[0], dtype=np.int64)
    for i in range(nW):
        code = code * 6 + conf_all[:, i]
    w2 = np.zeros(6 ** nW, dtype=np.int64)
    np.add.at(w2, code, w_all)
    confW = all_configs(nW)
    w1 = weights(confW, b_W, M)
    return [int(x) for x in w1], [int(x) for x in w2], conf_all, w_all, code


def tv_exact(w1, w2):
    Z1, Z2 = sum(w1), sum(w2)
    return Fr(sum(abs(a * Z2 - b * Z1) for a, b in zip(w1, w2)), 2 * Z1 * Z2)


def average_identity(W, E, pqr):
    """R2 = sum_omega P(omega) R3(.|omega): compared exactly as rationals."""
    w1, w2, conf_all, w_all, code = readings(W, E, pqr)
    nW, nE = len(W), len(E)
    ecode = np.zeros(conf_all.shape[0], dtype=np.int64)
    for i in range(nE):
        ecode = ecode * 6 + conf_all[:, nW + i]
    Z = int(w_all.sum())
    avg = [Fr(0)] * (6 ** nW)
    for om in range(6 ** nE):
        sel = ecode == om
        wom = np.zeros(6 ** nW, dtype=np.int64)
        np.add.at(wom, code[sel], w_all[sel])
        Zom = int(wom.sum())
        pom = Fr(Zom, Z)
        for v in range(6 ** nW):
            if wom[v]:
                avg[v] += pom * Fr(int(wom[v]), Zom)
    Z2 = sum(w2)
    return all(avg[v] == Fr(w2[v], Z2) for v in range(6 ** nW))


def components(W, E):
    Ws, Es = set(W), set(E)
    comps, seen = [], set()
    nb = lambda x: [(x[0] + d0, x[1] + d1, x[2] + d2) for d0, d1, d2 in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
    for e in E:
        if e in seen:
            continue
        stack, comp = [e], set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(y for y in nb(x) if y in Es and y not in comp)
        seen |= comp
        touch = {y for x in comp for y in nb(x) if y in Ws}
        comps.append((comp, touch))
    return comps


def graph_readings(nW, nE, bonds, pqr):
    """R1/R2 for an abstract graph: sites 0..nW-1 recorded, nW..nW+nE-1 unrecorded, given bond list."""
    M = phi_matrix(*pqr)
    n = nW + nE
    conf_all = all_configs(n)
    w_all = weights(conf_all, bonds, M)
    code = np.zeros(conf_all.shape[0], dtype=np.int64)
    for i in range(nW):
        code = code * 6 + conf_all[:, i]
    w2 = np.zeros(6 ** nW, dtype=np.int64)
    np.add.at(w2, code, w_all)
    confW = all_configs(nW)
    w1 = weights(confW, [(a, b) for a, b in bonds if a < nW and b < nW], M)
    return [int(x) for x in w1], [int(x) for x in w2]


def main():
    t0 = time.time()
    hits = []
    # ---------------------------------------------------------------- Q4 (the note's three geometries as graphs)
    print("== Q4 witnesses recomputed by brute-force integer enumeration")
    plaq = [(0, 1), (1, 2), (2, 3), (3, 0)]
    stated_a = {(3, 1, 2): Fr(78621, 4563820), (5, 2, 4): Fr(675203620, 64463986907), (2, 1, 2): Fr(221667, 30063356)}
    for pqr, val in stated_a.items():
        w1, w2 = graph_readings(4, 1, plaq + [(4, 0), (4, 1)], pqr)
        tv = tv_exact(w1, w2)
        ok = tv == val
        print(f"[Q4a] plaquette + one unrecorded site on two adjacent corners at {pqr}: TV = {tv} (stated {val}): {'agrees' if ok else 'DIFFERS'}")
        if not ok:
            hits.append(f"Q4a at {pqr}: {tv} vs stated {val}")
    cubeW = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)]
    cubeE = [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]
    w1, w2, *_ = readings(cubeW, cubeE, (3, 1, 2))
    tv = tv_exact(w1, w2)
    ok = tv == Fr(9778807, 1312253264)
    print(f"[Q4b] unit cube, top face unrecorded, at (3, 1, 2): TV = {tv} (stated 9778807/1312253264): {'agrees' if ok else 'DIFFERS'}")
    if not ok:
        hits.append(f"Q4b: {tv}")
    # forest: plaquette W, a pendant path of two sites off corner 0 and a pendant site off corner 2 (graph form)
    w1, w2 = graph_readings(4, 3, plaq + [(4, 0), (4, 5), (6, 2)], (2, 1, 2))
    tv = tv_exact(w1, w2)
    print(f"[Q4c] plaquette + pendant path of two + pendant site at (2, 1, 2): TV = {tv} (stated 0): {'agrees' if tv == 0 else 'DIFFERS'}")
    if tv != 0:
        hits.append(f"Q4c: {tv}")
    # the same geometries at more couplings (beyond the note): TV > 0 for bridging, 0 for the forest
    more = [(1, 1, 1), (2, 2, 2), (4, 1, 2), (7, 3, 5), (1, 3, 2), (6, 6, 1), (2, 5, 5)]
    extra = []
    for pqr in more:
        a = tv_exact(*graph_readings(4, 1, plaq + [(4, 0), (4, 1)], pqr))
        c = tv_exact(*graph_readings(4, 3, plaq + [(4, 0), (4, 5), (6, 2)], pqr))
        extra.append((pqr, a, c))
        const = pqr[0] == pqr[1] == pqr[2]
        if (a == 0) != const or c != 0:
            hits.append(f"extra couplings {pqr}: bridging TV {a}, forest TV {c}")
    print("[Q4+] more couplings (plaquette+bridge TV; forest TV): " + "; ".join(f"{p}: {float(a):.3e}, {c}" for p, a, c in extra))
    # ---------------------------------------------------------------- is the Q4(a) geometry a window of Z^3?  (Z^3 is bipartite)
    g_bonds = plaq + [(4, 0), (4, 1)]
    color = {0: 0}
    bip = True
    changed = True
    while changed:
        changed = False
        for a, b in g_bonds:
            for u, v in ((a, b), (b, a)):
                if u in color and v not in color:
                    color[v] = 1 - color[u]
                    changed = True
                elif u in color and v in color and color[u] == color[v]:
                    bip = False
    tri = ((0, 1) in g_bonds) and ((4, 0) in g_bonds) and ((4, 1) in g_bonds)
    print(f"[Q4a-geom] the graph 'plaquette + one site on two adjacent corners' is bipartite: {bip}; it contains the triangle c0-c1-x: {tri}; "
          f"every subgraph of Z^3 is bipartite, so it is not a window of Z^3 (the declared setting)")
    if not bip:
        hits.append("Q4(a) - the stated witness configuration (one unrecorded site adjacent to two adjacent corners of a plaquette) is not a "
                    "window of Z^3: its graph contains the triangle c0-c1-x and Z^3 is bipartite; the stated TV values are reproduced on that "
                    "abstract graph (see [Q4a])")
    ana = []
    for pqr in ((3, 1, 2), (5, 2, 4), (2, 1, 2)):
        t1 = tv_exact(*readings([(0, 0, 0), (1, 0, 0), (1, 1, 0)], [(0, 1, 0)], pqr)[:2])
        t2 = tv_exact(*readings([(0, 0, 0), (2, 0, 0), (0, 1, 0), (2, 1, 0)], [(1, 0, 0)], pqr)[:2])
        ana.append((pqr, t1, t2))
    print("[Q4a-Z3] realizable analogues, TV(R1, R2): L-path of three corners with the fourth corner unrecorded; two recorded pairs with one "
          "unrecorded site bridging a straight gap: " + "; ".join(f"{p}: {a}, {b}" for p, a, b in ana))
    # ---------------------------------------------------------------- the average identity (Q1)
    ok_avg = average_identity(cubeW[:2] + [(1, 1, 0)], [(0, 1, 0)], (3, 1, 2)) and average_identity(cubeW, [(0, 0, 1), (1, 0, 1)], (5, 2, 4))
    print(f"[Q1] average identity R2 = sum_omega P(omega) R3(.|omega) exact on two windows (bent path + bridging site; square + two-site bridge): {ok_avg}")
    if not ok_avg:
        hits.append("average identity")
    # ---------------------------------------------------------------- random windows (beyond the note)
    rng = random.Random(8158)
    box = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
    nwin = 0
    stats = {"pendant": 0, "bridging": 0, "pendant_nonzero": 0, "bridging_zero": 0, "bridging_zero_construle": 0}
    examples = []
    while nwin < 300:
        n = rng.randint(6, 8)
        start = rng.choice(box)
        S = {start}
        while len(S) < n:
            x = rng.choice(sorted(S))
            d = rng.choice(((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)))
            y = (x[0] + d[0], x[1] + d[1], x[2] + d[2])
            if y in box:
                S.add(y)
        S = sorted(S)
        k = rng.randint(1, min(5, n - 1))
        E = sorted(rng.sample(S, n - k))
        W = [x for x in S if x not in E]
        if not W or not E or len(W) > 5:
            continue
        pqr = tuple(rng.randint(1, 7) for _ in range(3))
        comps = components(W, E)
        bridging = any(len(t) >= 2 for _, t in comps)
        tv = tv_exact(*readings(W, E, pqr)[:2])
        nwin += 1
        const = pqr[0] == pqr[1] == pqr[2]
        if bridging:
            stats["bridging"] += 1
            if tv == 0:
                if const:
                    stats["bridging_zero_construle"] += 1
                else:
                    stats["bridging_zero"] += 1
                    examples.append((W, E, pqr))
        else:
            stats["pendant"] += 1
            if tv != 0:
                stats["pendant_nonzero"] += 1
                examples.append((W, E, pqr, tv))
    print(f"[R] {nwin} random windows (6-8 sites in a 3x3x3 box, |W| <= 5, couplings in [1,7]^3): {stats}; first exceptions: {examples[:2]}")
    if stats["pendant_nonzero"]:
        hits.append(f"Q2: {stats['pendant_nonzero']} pendant windows with TV != 0")
    if stats["bridging_zero"]:
        hits.append(f"title criterion: {stats['bridging_zero']} bridging windows with TV = 0 at a non-constant rule")
    print(f"[time] {time.time() - t0:.0f}s")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: Q4 values recomputed by integer enumeration ({'all agree' if not any(h.startswith('Q4a at') or h.startswith('Q4b') or h.startswith('Q4c') for h in hits) else 'DIFFER'}; "
          f"Q4(a)'s graph {'is not' if any(h.startswith('Q4(a)') for h in hits) else 'is'} a Z^3 window); "
          f"average identity {'holds' if ok_avg else 'FAILS'}; {len(more)} more couplings on the plaquette/forest behave as the criterion says; "
          f"{nwin} random windows: {stats['pendant']} pendant ({stats['pendant_nonzero']} with TV != 0), {stats['bridging']} bridging "
          f"({stats['bridging_zero']} with TV = 0 at a non-constant rule; {stats['bridging_zero_construle']} at p = q = r); falsifier "
          f"{'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
