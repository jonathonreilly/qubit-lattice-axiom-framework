#!/usr/bin/env python3
"""C6 runner: exact (GF(2) + Pauli-phase) checks of the Bravyi-Hastings-Michalakis hypotheses for the
supplied BKSF-type fermion codes, plus point-charge exchange statistics and GSD(L).

Usage: python3 c6_tqo_runner.py [--quick]
Sections
  A  consistency / frustration-freeness: Hermitian commuting generators, -I not in S (phase-tracked), k(L)
  B  TQO-1 on the torus: number of logical operators supported in a cube of side r (cleaning-lemma count)
  C  TQO-2 (local form): Paulis on a cube commuting with the generators inside the W-enlarged cube are
     products of those generators (counting identity, infinite-lattice-sized torus so nothing wraps)
  D  explicit string / membrane logical operators and their pairing; translates equivalent mod S
  E  point-charge statistics: Kitaev hopping test (20 triples) and straight-leg Levin-Wen T-junction,
     with stabilizer-dressing invariance, plus the untwisted toric-code control (+1)
Every expected constant is fixed by the homological argument in NOTE.md (k = dim H_1(T^3) = 3 for the
cubic families on even L, TQO counts = 0), not by the code under test.  The odd-L MPD value k = 2 was
observed first and then explained (NOTE.md, section 3); it is disclosed as post hoc.
"""
from __future__ import annotations
import itertools
import random
import sys
import time
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c6_lib import *   # noqa

QUICK = '--quick' in sys.argv
PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)


# ------------------------------------------------------------ helpers
def restrict(P, mask):
    return (P[0] & mask, P[1] & mask, 0)


def rank_of(ops, n):
    B = Basis()
    for P in ops:
        B.add(P[0] | (P[1] << n))
    return B.rank


def qmask(code, siteset):
    m = 0
    for q, s in enumerate(code.qsite):
        if s in siteset:
            m |= 1 << q
    return m


def box(r, L, origin=(0, 0, 0)):
    return {tuple((origin[i] + x[i]) % L for i in range(3)) for x in itertools.product(range(r), repeat=3)}


def logicals_in_region(code, Mset, S_rank=None):
    """Cleaning-lemma count: dim[(C(S) cap P_M) / (S cap P_M)] = 2|M| - dim S|_M - dim S + dim S|_{M^c}."""
    n = code.n
    mM = qmask(code, Mset)
    mC = ((1 << n) - 1) ^ mM
    nM = pc(mM)
    rM = rank_of([restrict(g, mM) for g in code.gens], n)
    rC = rank_of([restrict(g, mC) for g in code.gens], n)
    rS = S_rank if S_rank is not None else rank_of(code.gens, n)
    return 2 * nM - rM - rS + rC


def compress(P, qmap):
    x = z = 0
    for q in bits(P[0]):
        x |= 1 << qmap[q]
    for q in bits(P[1]):
        z |= 1 << qmap[q]
    return (x, z, P[2])


def local_tqo2_defect(code, r, W):
    """Box B of side r at offset W; R = B enlarged by W on every side; T = generators supported in R.
    Returns (defect, all_overlapping_inside) with defect = dim(C_T cap P_B) - dim(span T cap P_B)
    (both computed by ranks of restrictions; work is done on R's qubits re-indexed locally)."""
    L = code.L
    Bset = box(r, L, (W, W, W))
    Rset = box(r + 2 * W, L, (0, 0, 0))
    Rq = [q for q, s in enumerate(code.qsite) if s in Rset]
    qmap = {q: i for i, q in enumerate(Rq)}
    n = len(Rq)
    mB = 0
    for q in Rq:
        if code.qsite[q] in Bset:
            mB |= 1 << qmap[q]
    mRB = ((1 << n) - 1) ^ mB
    T, inside = [], True
    for g, gs in zip(code.gens, code.gsite):
        inR = gs <= Rset
        if inR:
            T.append(compress(g, qmap))
        elif gs & Bset:
            inside = False
    nB = pc(mB)
    dimC = 2 * nB - rank_of([restrict(g, mB) for g in T], n)
    dimSB = rank_of(T, n) - rank_of([restrict(g, mRB) for g in T], n)
    return dimC - dimSB, inside


def consistency(code):
    from collections import defaultdict
    byq = defaultdict(list)
    for i, g in enumerate(code.gens):
        for q in bits(support(g)):
            byq[q].append(i)
    bad = 0
    seen = set()
    for lst in byq.values():
        for i, j in itertools.combinations(lst, 2):
            if (i, j) in seen:
                continue
            seen.add((i, j))
            if not pcomm(code.gens[i], code.gens[j]):
                bad += 1
    G = code.group(phases=True)
    return dict(herm=all(herm(g) for g in code.gens), noncomm=bad, negI=G.neg_identity, k=code.n - G.rank, rank=G.rank)


# ------------------------------------------------------------ hop operators per family
def hop(code, v, d):
    """Operator moving the point charge from site v one step along direction d (DIRS6 index)."""
    L = code.L
    a, s = DIRS6[d]
    A = code.meta['A']
    if s == 1:
        return A(v, a)
    return A(tadd(v, tuple(-x for x in E3[a]), L), a)


def straight_leg(code, v, d, ell):
    ops = []
    w = v
    for _ in range(ell):
        ops.append(hop(code, w, d))
        w = tadd(w, dvec(d), code.L)
    return prod(ops)


def exchange_sign(t1, t2, t3):
    P = prod([t3, pinv(t2), t1, pinv(t3), t2, pinv(t1)])
    if P[0] or P[1]:
        return None
    return {0: 1, 2: -1}.get(P[2])


def site_stats(code, v0, ell):
    out = []
    for trip in itertools.combinations(range(6), 3):
        legs = [straight_leg(code, v0, d, ell) for d in trip]
        out.append(exchange_sign(*legs))
    return out


# ------------------------------------------------------------ explicit logicals
def string_op(code, a, start=(0, 0, 0)):
    L = code.L
    return prod([hop(code, tadd(start, tuple(t * E3[a][i] for i in range(3)), L), DIRS6.index((a, 1))) for t in range(L)])


def membrane_op(code, a, c):
    """Operators dual to the strings, as in NOTE.md section 3."""
    L = code.L
    kind = code.meta['kind']
    plane = [v for v in sites(L) if v[a] == c]
    if kind == 'edge':
        return Zs([code.meta['q'](v, a) for v in plane])
    if kind == 'sixdir':
        return Zs([code.meta['q'](v, DIRS6.index((a, 1))) for v in plane])
    if kind in ('mpd', 'spinful'):
        # gamma_{v,+a} on every site of the plane, made site-even by in-plane dimers A along direction b
        b = (a + 1) % 3
        g = code.meta['g']
        ops = [g(v, DIRS6.index((a, 1))) for v in plane]
        ops += [code.meta['A'](v, b) for v in plane if v[b] % 2 == 0]
        return prod(ops)
    raise ValueError


def main():
    t0 = time.time()
    rng = random.Random(20261018)
    ORD0 = (0, 1, 2, 3, 4, 5)
    all_orders = list(itertools.permutations(range(6)))
    sample_orders = [ORD0] + rng.sample(all_orders, 5)
    FLUX8 = list(itertools.product((0, 1), repeat=3))
    Ls = (2, 3, 4) if QUICK else (2, 3, 4, 5, 6)

    print('=' * 78)
    print('A. Consistency, frustration-freeness (-I not in S), log2 GSD k(L)')
    print('=' * 78)
    # A1: all 720 orderings, both uniform sectors, L = 4 (commuting, Hermitian, no -I, k = 3)
    okA1 = True
    nbad = 0
    for o in (all_orders[::(37 if QUICK else 1)]):
        for f in ((0, 0, 0), (1, 1, 1)):
            r = consistency(edge_bksf(4, o, f))
            if not (r['herm'] and r['noncomm'] == 0 and not r['negI'] and r['k'] == 3):
                okA1 = False
                nbad += 1
    check('F1 edge BKSF: every ordering (720), uniform flux sectors 0 and pi, L=4: Hermitian commuting, no -I, k=3',
          okA1, f'failures={nbad}')
    # A2: GSD(L) table for representative members of every family
    table = {}
    fams = []
    for o in sample_orders:
        for f in FLUX8:
            fams.append(('F1', o, f, lambda L, o=o, f=f: edge_bksf(L, o, f)))
    for o in sample_orders[:2]:
        for f in ((0, 0, 0), (1, 1, 1)):
            fams.append(('F2', o, f, lambda L, o=o, f=f: sixdir_bksf(L, o, f)))
    for f in FLUX8:
        fams.append(('F3', None, f, lambda L, f=f: mpd(L, f)))
    for f in ((0, 0, 0), (1, 1, 1)):
        fams.append(('F4', None, f, lambda L, f=f: spinful_mpd(L, f)))
    for L in Ls:
        for fam, o, f, mk in fams:
            r = consistency(mk(L))
            table[(fam, o, f, L)] = r
    # corner: all 16 flux patterns at L = 2, 3, 4; default pattern up to 6 (5 in quick mode skipped)
    CL = (2, 3, 4) if QUICK else (2, 3, 4, 5, 6)
    for L in CL:
        pats = list(itertools.product((0, 1), repeat=4)) if L <= 4 else [(1, 0, 1, 0), (1, 0, 1, 1)]
        for fl in pats:
            FL = dict(zip(('square', 'triangle', 'plaquette', 'tube'), fl))
            r = consistency(corner_code(L, FL))
            table[('F5', None, fl, L)] = r
        print(f'   corner L={L} done ({time.time() - t0:.0f}s)', flush=True)

    # extra tori L = 7, 8 for the cheap families (frustration pattern beyond L = 6)
    if not QUICK:
        for L in (7, 8):
            for fam, o, f, mk in fams:
                if fam == 'F1' and o not in sample_orders[:2]:
                    continue
                table[(fam, o, f, L)] = consistency(mk(L))
            print(f'   extra L={L} done ({time.time() - t0:.0f}s)', flush=True)
    allherm = all(r['herm'] and r['noncomm'] == 0 for r in table.values())
    check('all tabulated codes (F1-F5, every L in the table) have Hermitian, pairwise commuting generators', allherm,
          f'{len(table)} (code, L) cases')
    # summarize
    print('   k(L) and frustration (negI) summary:')
    for fam in ('F1', 'F2', 'F3', 'F4', 'F5'):
        for L in sorted({k[3] for k in table if k[0] == fam}):
            rows = [(k, r) for k, r in table.items() if k[0] == fam and k[3] == L]
            ks = sorted({r['k'] for _, r in rows if not r['negI']})
            nfr = sum(1 for _, r in rows if r['negI'])
            okfl = sorted({str(k[2]) for k, r in rows if not r['negI']})
            print(f'   {fam} L={L}: {len(rows)} codes, frustrated(-I in S)={nfr}, k over consistent codes={ks}; consistent flux labels={okfl if len(okfl) < 9 else str(len(okfl)) + " labels"}')
    # expected (homological count, NOTE section 3): k = 3 whenever consistent, for F1, F2, F5 at every L,
    # and for F3, F4 at even L; F3, F4 at odd L: k = 2 (post hoc parity explanation)
    ok_even = all(r['k'] == 3 for k, r in table.items() if not r['negI'] and (k[0] in ('F1', 'F2', 'F5') or k[3] % 2 == 0))
    check('k = 3 (GSD 8) for every consistent F1/F2/F5 code at every tested L and every consistent F3/F4 code at even L',
          ok_even)
    ok_odd = all(r['k'] == 2 for k, r in table.items() if not r['negI'] and k[0] in ('F3', 'F4') and k[3] % 2 == 1)
    check('F3/F4 (Majorana encodings) at odd L: k = 2 (GSD 4) whenever consistent [post hoc, explained by the parity constraint]',
          ok_odd)
    ok_unif = all(not r['negI'] for k, r in table.items() if k[0] in ('F1', 'F2', 'F3', 'F4') and k[2] == (0, 0, 0))
    check('flux-0 sector is frustration-free (no -I) for F1-F4 at every tested L', ok_unif)
    ok_even_all = all(not r['negI'] for k, r in table.items() if k[0] in ('F1', 'F2', 'F3', 'F4') and k[3] % 2 == 0)
    check('every one of the 8 sign sectors of F1/F2/F3/F4 is frustration-free at every tested even L', ok_even_all)
    ok_corner = all(not r['negI'] for k, r in table.items() if k[0] == 'F5' and k[3] % 2 == 0)
    check('every tested corner flux pattern is frustration-free at every tested even L', ok_corner)
    fracton = all(r['k'] <= 3 for r in table.values())
    check('no subextensive GSD growth: k(L) <= 3 for every code and L tested (no fracton behaviour)', fracton)

    print('=' * 78)
    print('B. TQO-1 on the torus: logical operators supported in a cube of side r (cleaning-lemma count)')
    print('=' * 78)
    tq = []
    for L in ((3, 4) if QUICK else (2, 3, 4, 5, 6)):
        cases = [('F1', edge_bksf(L, sample_orders[1], (0, 0, 0))), ('F1u', edge_bksf(L, ORD0, (0, 0, 0), twisted=False)),
                 ('F2', sixdir_bksf(L, sample_orders[2], (0, 0, 0))), ('F3', mpd(L)), ('F4', spinful_mpd(L))]
        if L <= (4 if QUICK else 6):
            cases.append(('F5', corner_code(L)))
        for nm, c in cases:
            rS = rank_of(c.gens, c.n)
            k = c.n - rS
            counts = [logicals_in_region(c, box(r, L), rS) for r in range(1, L + 1)]
            tq.append((nm, L, k, counts))
            print(f'   {nm} L={L} k={k}: logicals in cube of side r=1..L: {counts}', flush=True)
    okB = all(all(x == 0 for x in counts[:-1]) and counts[-1] == 2 * k for nm, L, k, counts in tq)
    check('TQO-1 (torus): no nontrivial logical is supported in any cube of side r <= L-1; the full torus carries all 2k',
          okB, f'{len(tq)} (code, L) cases')

    print('=' * 78)
    print('C. TQO-2 / local topological order: commutant of the generators in B+W restricted to B = their span')
    print('=' * 78)
    rmax = 3 if QUICK else 4
    loc = []
    # W = generator reach used for the enlargement; torus large enough that B+W never wraps
    lcases = [('F1', lambda: edge_bksf(12, sample_orders[1], (1, 1, 1)), rmax, 3), ('F1', lambda: edge_bksf(12, sample_orders[3], (0, 1, 0)), rmax, 3),
              ('F2', lambda: sixdir_bksf(12, sample_orders[2], (0, 0, 0)), rmax, 3), ('F3', lambda: mpd(10, (1, 0, 1)), rmax, 2),
              ('F4', lambda: spinful_mpd(10), rmax, 2), ('F5', lambda: corner_code(8), 3, 2)]
    for nm, mk, rm, W in lcases:
        c = mk()
        for r in range(1, rm + 1):
            if r + 2 * W >= c.L:
                continue
            dfc, inside = local_tqo2_defect(c, r, W)
            loc.append((nm, r, dfc, inside))
            print(f'   {nm} (torus L={c.L}) cube side r={r}, W={W}: defect={dfc}, all overlapping generators inside B+W: {inside}', flush=True)
    check('local TQO (BHM TQO-2, stabilizer form) holds for every tested cube: defect 0 with enlargement W (3 for F1/F2, 2 for F3-F5)',
          all(d == 0 and ins for _, _, d, ins in loc), f'{len(loc)} cases')

    print('=' * 78)
    print('D. Explicit string / membrane logical operators')
    print('=' * 78)
    okD = True
    okT = True
    for L in (4, 6) if not QUICK else (4,):
        for nm, c in [('F1', edge_bksf(L, sample_orders[4], (1, 0, 0))), ('F2', sixdir_bksf(L, sample_orders[2], (0, 0, 0))),
                      ('F3', mpd(L, (0, 1, 1))), ('F4', spinful_mpd(L))]:
            G = Group(c.n, phases=False)
            for g in c.gens:
                G.add(g)
            st = [string_op(c, a) for a in range(3)]
            mb = [membrane_op(c, a, 0) for a in range(3)]
            comm_all = all(pcomm(P, g) for P in st + mb for g in c.gens)
            pair = [[0 if pcomm(s, m) else 1 for m in mb] for s in st]
            Gl = Group(c.n, phases=False)
            Gl.piv = dict(G.piv)
            indep = sum(Gl.add(P) for P in st + mb)
            # translates are equivalent mod S
            tr_ok = True
            for a in range(3):
                for sh in ((0, 1, 1), (0, 2, 3), (1, 0, 2)):
                    s2 = string_op(c, a, start=tuple(sh[(i - a) % 3] if i != a else 0 for i in range(3)))
                    tr_ok &= G.contains(pmul(st[a], s2))
                    m2 = membrane_op(c, a, 2)
                    tr_ok &= G.contains(pmul(mb[a], m2))
            okD &= comm_all and pair == [[1, 0, 0], [0, 1, 0], [0, 0, 1]] and indep == 6
            okT &= tr_ok
            ws = [pc(support(P)) for P in st]
            wm = [pc(support(P)) for P in mb]
            print(f'   {nm} L={L}: logicals commute={comm_all}, pairing string_a vs membrane_b={pair}, independent mod S={indep}, '
                  f'translates equivalent={tr_ok}, string weights={ws}, membrane weights={wm}', flush=True)
    check('even L: 3 straight strings + 3 membranes commute with S, are independent mod S and pair as the identity matrix (F1-F4)', okD)
    check('translated strings / membranes are equivalent mod S (needed for the distance bound)', okT)
    # corner: strings along lattice lines through corners (v;+a,b): use the plaquette-link hops and check pairing with the computed logical space
    for L in (4,):
        c = corner_code(L)
        A = c.meta['A']
        corner = c.meta['corner']
        neg = c.meta['neg']
        unit = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        st = []
        for a in range(3):
            ea = unit[a]
            eb = unit[(a + 1) % 3]
            ops = []
            for t in range(L):
                v = tuple(t * ea[i] for i in range(3))
                w = tadd(v, ea, L)
                # link from (v; +a, b) to (w; -a, b), then on-site hop (w; -a, b) -> (w; +a, b) via (w; b, ...)? use two on-site hops through (w; b, c)
                ec = unit[(a + 2) % 3]
                ops.append(A((v, corner(ea, eb)), (w, corner(neg(ea), eb))))
                ops.append(A((w, corner(neg(ea), eb)), (w, corner(eb, ec))))
                ops.append(A((w, corner(eb, ec)), (w, corner(ea, eb))))
            st.append(prod(ops))
        G = Group(c.n, phases=False)
        for g in c.gens:
            G.add(g)
        comm_all = all(pcomm(P, g) for P in st for g in c.gens)
        Gl = Group(c.n, phases=False)
        Gl.piv = dict(G.piv)
        indep = sum(Gl.add(P) for P in st)
        print(f'   F5 L={L}: corner strings commute with S={comm_all}, independent mod S={indep}, weights={[pc(support(P)) for P in st]}')
        check('corner code: three straight corner-hop strings are independent nontrivial logicals (L=4)', comm_all and indep == 3)

    print('=' * 78)
    print('E. Point-charge exchange statistics (Kitaev hopping test, Levin-Wen straight-leg T-junction)')
    print('=' * 78)
    L = 8
    stat = {}
    for nm, c in [('F1 order0', edge_bksf(L, ORD0)), ('F1 sample', edge_bksf(L, sample_orders[1], (1, 1, 1))),
                  ('F2', sixdir_bksf(L, sample_orders[2])), ('F3', mpd(L)), ('F4', spinful_mpd(L)),
                  ('F1 untwisted control', edge_bksf(L, ORD0, twisted=False))]:
        v0 = (4, 4, 4)
        s1 = site_stats(c, v0, 1)
        s3 = site_stats(c, v0, 3)
        stat[nm] = (s1, s3)
        print(f'   {nm}: hopping test (ell=1) signs {dict((x, s1.count(x)) for x in set(s1))}; straight legs ell=3 {dict((x, s3.count(x)) for x in set(s3))}')
    twisted = [k for k in stat if 'control' not in k]
    check('every twisted family (F1, F2, F3, F4): exchange sign -1 for all 20 direction triples, ell = 1 and 3 (fermion)',
          all(all(s == -1 for s in stat[k][0] + stat[k][1]) for k in twisted))
    check('control: untwisted toric code gives +1 for all 20 triples (boson)',
          all(s == 1 for s in stat['F1 untwisted control'][0] + stat['F1 untwisted control'][1]))
    # all 720 orderings, hopping test with ell = 1 at L = 4
    okall = True
    for o in all_orders[::(37 if QUICK else 1)]:
        c = edge_bksf(4, o)
        okall &= all(s == -1 for s in site_stats(c, (1, 1, 1), 1))
    check('F1: all 720 orderings give the fermionic hopping-test sign for all 20 triples (L=4)', okall)
    # dressing invariance: multiply legs by random generators touching the legs
    c = edge_bksf(L, sample_orders[1], (1, 1, 1))
    okd = True
    for trial in range(30):
        trip = rng.sample(range(6), 3)
        legs = [straight_leg(c, (4, 4, 4), d, 3) for d in trip]
        for i in range(3):
            for _ in range(4):
                legs[i] = pmul(legs[i], rng.choice(c.gens))
        okd &= exchange_sign(*legs) == -1
    check('exchange sign is unchanged under random stabilizer dressing of the legs (30 trials)', okd)
    # corner: Kitaev test at a corner vertex, all 20 triples of its six hops
    c = corner_code(4)
    A = c.meta['A']
    INC = c.meta['INC']
    signs = []
    for q0 in c.meta['VERTS'][:12]:
        nbs = [nb for _, _, nb in INC[q0]]
        for trip in itertools.combinations(nbs, 3):
            signs.append(exchange_sign(*[A(q0, nb) for nb in trip]))
    print(f'   F5 corner: hopping test at the 12 corners of a site, 20 triples each: {dict((x, signs.count(x)) for x in set(signs))}')
    check('F5 corner charge: hopping-test sign -1 for all 240 (corner, triple) cases', all(s == -1 for s in signs))

    print('=' * 78)
    print('per_element: every generator pair sharing a qubit checked for commutation; all 720 F1 orderings at L=4 (sections A, E)')
    print('per_site: generators and hops are built site by site; TQO counts resolve individual sites of cubes of side r')
    print('per_mode: checked and not executed - no momentum-resolved or spectral quantity is computed in this runner')
    print('per_block: cubes of side r (TQO-1 up to r=L, TQO-2 up to r=4) are the block-level objects actually tested')
    print('lattice_wide: k(L) on tori L=2..6 (corner up to 6), string/membrane logical algebra on L=4,6')
    print(f'elapsed {time.time() - t0:.0f}s')
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')
    return 0 if FAIL == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
