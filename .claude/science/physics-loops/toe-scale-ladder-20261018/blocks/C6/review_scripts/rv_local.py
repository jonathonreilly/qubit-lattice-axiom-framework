#!/usr/bin/env python3
"""Reviewer's checks of the load-bearing local statements of Lemma 1.
 (a) topological input (T1)/(T2) for the corner 2-complex, built from scratch (own cell list: cuboctahedron
     squares+triangles, one tube per lattice edge, one 4-link cell per lattice plaquette), on open boxes.
 (b) local TQO (Lemma 1, stabilizer form) by explicit centralizer construction: Paulis on cube B commuting with
     all generators inside R = B+W are in span(generators inside R)."""
import os, sys, itertools, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from rv_gf2 import rank, nullspace, vec
import rv_codes as C

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)

UNIT, ng, dt, CN = C.UNIT, C.ng, C.dt, C.CN

def corner_complex_open(sites):
    sites = set(sites)
    V = [(v, c) for v in sites for c in CN]
    Eset = set()
    for v in sites:
        for c1, c2 in itertools.combinations(CN, 2):
            if len(c1 & c2) == 1 and dt(next(iter(c1 - c2)), next(iter(c2 - c1))) == 0:
                Eset.add(frozenset(((v, c1), (v, c2))))
        for c in CN:
            for a in c:
                w = tuple(v[i] + a[i] for i in range(3))
                if w in sites:
                    Eset.add(frozenset(((v, c), (w, frozenset((ng(a), next(iter(c - {a}))))))))
    cells = []
    for v in sites:
        for d in UNIT:
            ring = [r for r in UNIT if dt(r, d) == 0]; r0 = ring[0]; r1 = [r for r in ring if dt(r, r0) == 0][0]
            cells.append([(v, frozenset((d, r))) for r in (r0, r1, ng(r0), ng(r1))])
        for s in itertools.product((1, -1), repeat=3):
            x, y, z = (s[0], 0, 0), (0, s[1], 0), (0, 0, s[2])
            cells.append([(v, frozenset((x, y))), (v, frozenset((y, z))), (v, frozenset((z, x)))])
        for d in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
            w = tuple(v[i] + d[i] for i in range(3))
            ring = [r for r in UNIT if dt(r, d) == 0]; r0 = ring[0]; r1 = [r for r in ring if dt(r, r0) == 0][0]
            cyc = [r0, r1, ng(r0), ng(r1)]
            for i in range(4):
                p, q = cyc[i], cyc[(i + 1) % 4]
                cells.append([(v, frozenset((d, p))), (w, frozenset((ng(d), p))), (w, frozenset((ng(d), q))), (v, frozenset((d, q)))])
        for d, e in (((1, 0, 0), (0, 1, 0)), ((0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0))):
            vd = tuple(v[i] + d[i] for i in range(3)); ve = tuple(v[i] + e[i] for i in range(3))
            vde = tuple(v[i] + d[i] + e[i] for i in range(3))
            cells.append([(v, frozenset((d, e))), (vd, frozenset((ng(d), e))), (vde, frozenset((ng(d), ng(e)))), (ve, frozenset((d, ng(e))))])
    cells = [cl for cl in cells if all(q[0] in sites for q in cl)]
    E = sorted(Eset, key=lambda e: str(sorted(map(str, e))))
    eid = {e: i for i, e in enumerate(E)}
    D2 = np.zeros((len(cells), len(E)), bool)
    for i, cl in enumerate(cells):
        for j in range(len(cl)):
            e = frozenset((cl[j], cl[(j + 1) % len(cl)]))
            assert e in eid, 'cell edge missing'
            D2[i, eid[e]] ^= True
    vid = {q: i for i, q in enumerate(V)}
    D1 = np.zeros((len(V), len(E)), bool)          # vertex-edge incidence (coboundary rows)
    for e, j in eid.items():
        for q in e: D1[vid[q], j] = True
    return V, E, D1, D2

def local_homology(r):
    inner = set(itertools.product(range(r), repeat=3))
    outer = set(itertools.product(range(-1, r + 1), repeat=3))
    V, E, D1, D2 = corner_complex_open(outer)
    inE = np.array([all(q[0] in inner for q in e) for e in E])
    # (T1) cycles on inner edges: nullspace of D1 restricted to inner edges; must lie in rowspace of D2
    cyc = nullspace(D1[:, inE])
    full = np.zeros((len(cyc), len(E)), bool); full[:, inE] = cyc
    rD2 = rank(D2)
    t1 = rank(np.concatenate([D2, full])) - rD2 if len(full) else 0
    # (T2) cochains on inner edges vanishing on every cell: nullspace of D2 restricted; must be in rowspace of D1
    clo = nullspace(D2[:, inE])
    full2 = np.zeros((len(clo), len(E)), bool); full2[:, inE] = clo
    rD1 = rank(D1)
    t2 = rank(np.concatenate([D1, full2])) - rD1 if len(full2) else 0
    return len(cyc), t1, len(clo), t2

def local_tqo(code, r, W):
    L = code.L; assert r + 2 * W < L
    R = set(itertools.product(range(r + 2 * W), repeat=3))
    Bc = set(itertools.product(range(W, W + r), repeat=3))
    n = code.n
    qR = np.array([q for q in range(n) if code.site[q] in R])
    qB = np.array([q for q in range(n) if code.site[q] in Bc])
    gsite = [set(code.site[q] for q in np.nonzero(g.x | g.z)[0]) for g in code.gens]
    T = [g for g, s in zip(code.gens, gsite) if s <= R]
    touching_outside = sum(1 for s in gsite if (s & Bc) and not s <= R)
    TM = np.array([vec(g) for g in T], bool)
    TM = np.concatenate([TM[:, qR], TM[:, n + qR]], axis=1)     # compress to R
    posB = np.array([np.searchsorted(qR, q) for q in qB]); nR = len(qR); nB = len(qB)
    rows = np.concatenate([TM[:, nR + posB], TM[:, posB]], axis=1)
    rows = rows[rows.any(axis=1)]
    ns = nullspace(rows)
    full = np.zeros((len(ns), 2 * nR), bool)
    full[:, posB] = ns[:, :nB]; full[:, nR + posB] = ns[:, nB:]
    rT = rank(TM)
    defect = rank(np.concatenate([TM, full])) - rT
    return defect, len(ns), touching_outside

def main(quick):
    t0 = time.time()
    res = []
    for r in ((1, 2, 3) if quick else (1, 2, 3, 4)):
        a = local_homology(r)
        res.append(a)
        print(f'   corner complex (own cells) cube side {r}: cycles in B {a[0]}, not filled in B+1: {a[1]}; closed cochains on B {a[2]}, not coboundaries from B+1: {a[3]}  ({time.time()-t0:.0f}s)', flush=True)
    check('(T1),(T2) for the corner complex on cubes up to side 3-4 (own construction, only one tube per edge)',
          all(a[1] == 0 and a[3] == 0 for a in res))
    out = []
    for nm, code, rs, W in [('F1', C.bksf(9, (4, 0, 5, 2, 3, 1), (1, 0, 1)), (1, 2), 3), ('F3', C.mpd(8, (0, 1, 1)), (1, 2, 3), 2),
                            ('F4', C.mpd(6, spinful=True), (1,), 2)] + ([] if quick else [('F1', C.bksf(10, (2, 5, 1, 3, 0, 4)), (3,), 3), ('F5', C.corner_code(6, 5), (1,), 2), ('F5', C.corner_code(7, 5), (2,), 2)]):
        for r in rs:
            d, dimC, tout = local_tqo(code, r, W)
            out.append((d, tout))
            print(f'   {nm} L={code.L} r={r} W={W}: dim C_T|_B={dimC}, defect (not in span of gens in B+W)={d}, gens touching B not inside B+W={tout}  ({time.time()-t0:.0f}s)', flush=True)
    check('local TQO (Lemma 1 stabilizer form): defect 0 and every generator touching B lies in B+W', all(d == 0 and t == 0 for d, t in out))
    # negative control: drop B_v at a site of B from the F3 generator list -> defect must become 1
    code = C.mpd(8)
    L = code.L; v = (2, 2, 2)
    Bv = code.meta['B'](v)
    code.gens = [g for g in code.gens if not (np.array_equal(g.x, Bv.x) and np.array_equal(g.z, Bv.z))]
    d, dimC, tout = local_tqo(code, 1, 2)
    print(f'   control F3 L=8 with B_(2,2,2) removed: defect={d}')
    check('negative control: the local-TQO test detects a missing on-site generator (defect 1)', d == 1)
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

main('quick' in sys.argv)
