#!/usr/bin/env python3
"""Reviewer's independent checks for C6 (does not import c6_lib or the author's runners).
 A  generators commute and are Hermitian (or anti-Hermitian, for unsigned corner loops) ; k = n - rank S
 B  TQO-1 on the torus by an explicit construction: basis of the centralizer restricted to a cube M
    (right nullspace of the commutation matrix), then count how many are NOT in S (rank([S;C_M]) - rank S)
 C  frustration-freeness from an explicit relation basis (left kernel) with exact phase products
 D  Levin-Wen T-junction exchange sign with legs of several lengths, toric-code control
Usage: python3 rv_main.py [quick]"""
import os, sys, itertools, time
os.environ.setdefault('OMP_NUM_THREADS', '1')
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rv_gf2 import Pauli, rank, nullspace, left_kernel, vec, prod
import rv_codes as C

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)

def genmat(code):
    return np.array([vec(g) for g in code.gens], bool)

def kval(code, G=None):
    G = genmat(code) if G is None else G
    return code.n - rank(G), G

def commuting(code, sample=None):
    gs = code.gens
    X = np.array([g.x for g in gs], np.uint8); Z = np.array([g.z for g in gs], np.uint8)
    Mx = (X.astype(np.int32) @ Z.T.astype(np.int32) + Z.astype(np.int32) @ X.T.astype(np.int32)) % 2
    return int(Mx.sum()) == 0

def tqo1_counts(code, G, rS):
    """For cubes of side r = 1..L at the origin: number of independent logicals supported in the cube."""
    L = code.L; n = code.n; out = []
    for r in range(1, L + 1):
        cube = set(itertools.product(range(r), repeat=3))
        M = [q for q in range(n) if code.site[q] in cube]
        Mi = np.array(M)
        # Pauli y on M (x_M, z_M) commutes with g iff g.z_M . x_M + g.x_M . z_M = 0
        rows = np.concatenate([G[:, n + Mi], G[:, Mi]], axis=1)   # (z-part, x-part) acting on (x, z)
        rows = rows[rows.any(axis=1)]
        ns = nullspace(rows)
        if len(ns) == 0:
            out.append(0); continue
        full = np.zeros((len(ns), 2 * n), bool)
        full[:, Mi] = ns[:, :len(M)]; full[:, n + Mi] = ns[:, len(M):]
        out.append(rank(np.concatenate([G, full])) - rS)
    return out

def phase_of_relation(code, mask):
    P = Pauli(code.n)
    for i in np.nonzero(mask)[0]:
        P = P * code.gens[i]
    assert P.is_identity()
    return P.ph

def frustration_free(code, G):
    K = left_kernel(G)
    phs = [phase_of_relation(code, row) for row in K]
    return all(p == 0 for p in phs), sorted(set(phs)), len(K)

def lw_sign(t1, t2, t3, n):
    P = prod([t3, t2.inv(), t1, t3.inv(), t2, t1.inv()], n)
    assert P.is_identity()
    return {0: 1, 2: -1}[P.ph]

def leg(code, v, d, ell):
    ops = []; w = v
    a, s = C.D6[d]
    for _ in range(ell):
        ops.append(code.meta['hop'](w, d)); w = C.shift(w, a, s, code.L)
    return prod(ops, code.n), w

def main(quick):
    t0 = time.time()
    order0 = (0, 1, 2, 3, 4, 5)
    order1 = (4, 0, 5, 2, 3, 1)
    order2 = (2, 5, 1, 3, 0, 4)
    FL8 = list(itertools.product((0, 1), repeat=3))
    print('=' * 70); print('A/C. commutation, k = log2 GSD, frustration-freeness (own conventions)'); print('=' * 70)
    kres = {}
    Ls = range(2, 6) if quick else range(2, 8)
    for L in Ls:
        for nm, mk in [('F1o0', lambda L: C.bksf(L, order0)), ('F1o1', lambda L: C.bksf(L, order1)),
                       ('F3', lambda L: C.mpd(L)), ('F4', lambda L: C.mpd(L, spinful=True)),
                       ('toric', lambda L: C.bksf(L, order0, twisted=False))]:
            if nm == 'F4' and L > 5: continue
            code = mk(L)
            k, G = kval(code)
            kres[(nm, L)] = (k, commuting(code) and all(g.hermitian() for g in code.gens))
            print(f'   {nm} L={L}: n={code.n} k={k} commuting={kres[(nm, L)][1]}  ({time.time()-t0:.0f}s)', flush=True)
    for L in ((2, 3) if quick else (2, 3, 4)):
        code = C.corner_code(L, vertex_order_seed=7)
        k, G = kval(code)
        kres[('F5', L)] = (k, commuting(code))
        print(f'   F5 (own ordering) L={L}: n={code.n} gens={len(code.gens)} k={k} commuting={kres[("F5", L)][1]}  ({time.time()-t0:.0f}s)', flush=True)
    check('all built generators pairwise commute (and F1/F3/F4/toric generators are Hermitian)', all(c for _, c in kres.values()))
    check('k = 3 for F1 (two orderings), toric, F5 at every L; F3/F4 k = 3 at even L',
          all(k == 3 for (nm, L), (k, _) in kres.items() if nm in ('F1o0', 'F1o1', 'toric', 'F5') or L % 2 == 0),
          str({key: v[0] for key, v in kres.items()}))
    check('F3/F4 k = 2 at odd L', all(k == 2 for (nm, L), (k, _) in kres.items() if nm in ('F3', 'F4') and L % 2 == 1))

    # frustration-freeness over the 8 uniform sign sectors (own sign convention)
    ffres = {}
    for L in ((2, 3, 4) if quick else (2, 3, 4, 5, 6)):
        for nm, mk in [('F1o1', lambda L, f: C.bksf(L, order1, f)), ('F3', lambda L, f: C.mpd(L, f))]:
            nff = 0
            for f in FL8:
                code = mk(L, f)
                ok, phs, nrel = frustration_free(code, genmat(code))
                nff += ok
            ffres[(nm, L)] = nff
            print(f'   {nm} L={L}: frustration-free sign sectors {nff}/8 (relations={nrel})  ({time.time()-t0:.0f}s)', flush=True)
    check('even L: all 8 uniform sign sectors frustration-free (F1, F3)', all(v == 8 for (nm, L), v in ffres.items() if L % 2 == 0))
    check('odd L: at least one sector frustration-free, but not all 8 (frustration of pi-type sectors)',
          all(0 < v < 8 for (nm, L), v in ffres.items() if L % 2 == 1), str(ffres))

    print('=' * 70); print('B. TQO-1 on the torus (explicit centralizer-in-cube basis vs stabilizer span)'); print('=' * 70)
    cases = [('F1o2', C.bksf(3, order2)), ('F1o2', C.bksf(4, order2)), ('F3', C.mpd(3)), ('F3', C.mpd(4)),
             ('F4', C.mpd(3, spinful=True)), ('toric', C.bksf(4, order0, twisted=False)), ('F5', C.corner_code(2, 3))]
    if not quick:
        cases += [('F1o2', C.bksf(5, order2)), ('F3', C.mpd(5)), ('F5', C.corner_code(3, 3))]
    okB = True
    for nm, code in cases:
        G = genmat(code); rS = rank(G); k = code.n - rS
        cnt = tqo1_counts(code, G, rS)
        ok = all(x == 0 for x in cnt[:-1]) and cnt[-1] == 2 * k
        okB &= ok
        print(f'   {nm} L={code.L} k={k}: nontrivial logicals in cube side r=1..L: {cnt}  ({time.time()-t0:.0f}s)', flush=True)
    check('TQO-1: no nontrivial logical in any cube of side <= L-1; full torus gives 2k', okB, f'{len(cases)} cases')

    print('=' * 70); print('D. Levin-Wen T-junction exchange sign'); print('=' * 70)
    L = 8; v0 = (4, 4, 4)
    stats = {}
    for nm, code in [('F1o1', C.bksf(L, order1)), ('F1o2', C.bksf(L, order2, (1, 0, 1))), ('F3', C.mpd(L)),
                     ('toric', C.bksf(L, order0, twisted=False))]:
        signs = []
        Bv = code.meta['B']
        for trip in itertools.combinations(range(6), 3):
            for ell in (1, 2, 3):
                legs = [leg(code, v0, d, ell) for d in trip]
                # legality: each leg anticommutes only with B at its two ends and commutes with every plaquette
                if ell == 2:
                    for (t, end) in legs:
                        assert not t.comm(Bv(v0)) and not t.comm(Bv(end))
                        assert all(t.comm(g) for g in code.gens[L ** 3:])
                signs.append(lw_sign(legs[0][0], legs[1][0], legs[2][0], code.n))
        stats[nm] = signs
        print(f'   {nm}: T-junction signs over 20 triples x ell in (1,2,3): {dict((s, signs.count(s)) for s in set(signs))}', flush=True)
    check('twisted families give -1 for all triples and leg lengths', all(all(s == -1 for s in stats[k]) for k in stats if k != 'toric'))
    check('toric-code control gives +1', all(s == 1 for s in stats['toric']))
    # corner code: legs = paths on the corner graph from a corner q0, three edge-disjoint branches of length 2
    code = C.corner_code(4, vertex_order_seed=11)
    A, INC = code.meta['A'], code.meta['INC']
    nloop = len(code.meta['cells'])
    loops = code.gens[-nloop:]
    csigns = []
    for q0 in [((1, 1, 1), c) for c in C.CN]:
        nbs = [t[0] for t in INC[q0]]
        for trip in itertools.combinations(nbs, 3):
            legs = []
            used = {q0} | set(trip)
            for r1 in trip:
                # extend to a second vertex not used
                r2 = next(t[0] for t in INC[r1] if t[0] not in used)
                used.add(r2)
                legs.append(A(q0, r1) * A(r1, r2))
            for t in legs:
                assert all(t.comm(g) for g in loops)
            csigns.append(lw_sign(*legs, code.n))
    print(f'   F5 (own ordering): T-junction with length-2 legs at 12 corners x 20 triples: {dict((s, csigns.count(s)) for s in set(csigns))}')
    check('corner code charge: T-junction sign -1 in all 240 cases (own construction and ordering)', all(s == -1 for s in csigns))
    print(f'elapsed {time.time()-t0:.0f}s')
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')

if __name__ == '__main__':
    main('quick' in sys.argv)
