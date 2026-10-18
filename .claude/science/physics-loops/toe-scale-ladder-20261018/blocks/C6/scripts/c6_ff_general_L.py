#!/usr/bin/env python3
"""C6: frustration-freeness (-I not in S) for every L, for F1, F2, F3, F4, by the relation-basis reduction.

Proof structure (NOTE.md section 3a):
 (i) Relation basis (homological, every L >= 2):
     F1: Z_2(T^3) (cube boundaries + 3 planes) + all-B (pure Z, sign +).
     F2: the same + all-B*all-R (pure Z, sign +).
     F3, F4: Z_2(T^3) + [L even] one all-B relation (B or D P_up P_dn over all sites, times c with dc = all edges).
     This script also checks the predicted relation dimension against #gens - rank at L = 2..6.
 (ii) Generators commute and square to I, so sign: Relations -> Z2 is a homomorphism. FF <=> sign = + on a basis.
 (iii) Each basis relation is an ordered product of translates of one fixed Pauli motif over a discrete torus Z_m^D
     (m = L for planes, m = L/2 for all-B). Its phase is N*p + 2*sum_{i<j} |z_i & x_j| (mod 4), and for m >= 2s-1
     (s = motif support side, in motif units) every pair count is an integer polynomial in m. So the sign is
     periodic in m with period dividing 4 once m >= m0. Checking all m below m0 and one full period at or above it
     proves the sign for every m. The thresholds used here are conservative (s <= 5 sites for F1/F2 planes).
 (iv) Sector dependence: in sector f each plaquette of orientation c gets (-1)^{f_c}. So the cube sign has factor +,
     the plane-c sign has factor (-1)^{f_c L^2}, and the all-B sign has factor (-1)^{sum_c f_c L^3/2} = + for even L.
     The script checks this factor directly in all 8 sectors for some codes.
"""
import itertools
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c6_lib import *   # noqa

PASS = FAIL = 0


def check(name, ok, detail=''):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ''), flush=True)


def sign_of(P):
    if P[0] or P[1]:
        raise ValueError('not a relation: product is not proportional to I')
    if P[2] % 2:
        raise ValueError('imaginary relation phase')
    return 1 if P[2] == 0 else -1


def cube_sign(c):
    pl = c.meta['plaq']
    L = c.L
    ops = []
    for k in range(3):
        ops += [pl((0, 0, 0), k), pl(tadd((0, 0, 0), E3[k], L), k)]
    return sign_of(prod(ops))


def plane_sign(c, k):
    pl = c.meta['plaq']
    vs = sorted(v for v in sites(c.L) if v[k] == 0)
    return sign_of(prod([pl(v, k) for v in vs]))


def allB_sign(c):
    """Only for F3/F4 at even L: prod over 2x2x2 blocks (lex) of [site parities of the block, then the c-plaquettes
    (xy at even y, yz at even z, zx at even x) based at sites of the block]; dc = all edges."""
    L = c.L
    pl = c.meta['plaq']
    kind = c.meta['kind']
    ops = []
    m = L // 2
    for w in itertools.product(range(m), repeat=3):
        blk = [tuple(2 * w[i] + o[i] for i in range(3)) for o in itertools.product((0, 1), repeat=3)]
        for v in blk:
            if kind == 'mpd':
                ops.append(c.meta['B'](v))
            else:
                ops += [c.meta['B'](v), c.meta['Pm'](v, 6), c.meta['Pm'](v, 8)]
        for v in blk:
            # orientation normal 2 = xy plane uses y parity; normal 0 = yz uses z parity; normal 1 = zx uses x parity
            if v[1] % 2 == 0:
                ops.append(pl(v, 2))
            if v[2] % 2 == 0:
                ops.append(pl(v, 0))
            if v[0] % 2 == 0:
                ops.append(pl(v, 1))
    return sign_of(prod(ops))


def rel_dim(c):
    G = c.group(phases=False)
    return len(c.gens) - G.rank


def main():
    t0 = time.time()
    orders = list(itertools.permutations(range(6)))
    FL8 = list(itertools.product((0, 1), repeat=3))

    print('(i) relation-space dimension = predicted basis size, L = 2..6')
    okdim = True
    for L in range(2, 7):
        pairs = [('F1', edge_bksf(L, orders[100]), L ** 3 + 3), ('F2', sixdir_bksf(L, orders[200]), L ** 3 + 3),
                 ('F3', mpd(L), L ** 3 + 2 + (L % 2 == 0)), ('F4', spinful_mpd(L), L ** 3 + 2 + (L % 2 == 0))]
        for nm, c, pred in pairs:
            d = rel_dim(c)
            okdim &= d == pred
            print(f'   {nm} L={L}: dim relations {d}, predicted {pred}')
    check('relation-space dimension equals |cube basis| + 3 planes + all-B term, F1-F4, L=2..6', okdim)

    print('(ii-iv) basis-relation signs (flux 0) for every L via eventual periodicity')
    Ls = list(range(2, 13))
    res = {}
    for fam, mk in (('F1', lambda L, o: edge_bksf(L, o, lazy=True)), ('F2', lambda L, o: sixdir_bksf(L, o, lazy=True))):
        bad = 0
        for o in orders:
            for L in Ls:
                c = mk(L, o)
                cs = cube_sign(c)
                ps = [plane_sign(c, k) for k in range(3)]
                if cs != 1 or ps != [1, 1, 1]:
                    bad += 1
        res[fam] = bad
        print(f'   {fam}: 720 orderings x L=2..12: cases with a basis sign -1 in flux 0: {bad}  ({time.time() - t0:.0f}s)', flush=True)
    check('F1, all 720 orderings, flux 0: cube sign + and all 3 plane signs + for L=2..12 (a full period above the conservative threshold L>=9)', res['F1'] == 0)
    check('F2, all 720 orderings, flux 0: cube sign + and all 3 plane signs + for L=2..12', res['F2'] == 0)
    okM = True
    for fam, mk in (('F3', lambda L: mpd(L, lazy=True)), ('F4', lambda L: spinful_mpd(L, lazy=True))):
        for L in Ls:
            c = mk(L)
            cs = cube_sign(c)
            ps = [plane_sign(c, k) for k in range(3)]
            okM &= cs == 1 and ps == [1, 1, 1]
        bs = []
        for L in range(2, 17, 2):
            c = mk(L)
            bs.append(allB_sign(c))
        okM &= all(b == 1 for b in bs)
        print(f'   {fam}: cube/plane signs + for L=2..12; all-B signs for even L=2..16 (m=1..8): {bs}', flush=True)
    check('F3, F4 flux 0: cube and plane signs + (L=2..12), all-B sign + (L=2..16 even, a full m-period above m>=5)', okM)

    print('(iv) sector factor checked directly; (v) reduction cross-checked against full-group FF')
    okf = True
    for L in (3, 4, 5, 6):
        for f in FL8:
            for c in (edge_bksf(L, orders[7], f, lazy=True), mpd(L, f, lazy=True), spinful_mpd(L, f, lazy=True)):
                okf &= cube_sign(c) == 1
                okf &= all(plane_sign(c, k) == (-1) ** (f[k] * L * L) for k in range(3))
                if L % 2 == 0 and c.meta['kind'] != 'edge':
                    okf &= allB_sign(c) == 1
    check('sector factors: cube +, plane-c (-1)^{f_c L^2}, all-B + (even L), all 8 sectors, L=3..6', okf)
    okx = True
    ncase = 0
    for L in (2, 3, 4, 5):
        for f in FL8:
            for nm, c in (('F1', edge_bksf(L, orders[333], f)), ('F2', sixdir_bksf(L, orders[444], f)), ('F3', mpd(L, f)), ('F4', spinful_mpd(L, f))):
                pred_ff = all((f[k] * L * L) % 2 == 0 for k in range(3))
                G = c.group(phases=True)
                okx &= (not G.neg_identity) == pred_ff
                ncase += 1
    check('reduction agrees with direct phase-tracked FF on full groups (F1-F4, 8 sectors, L=2..5)', okx, f'{ncase} cases')
    print('THEOREM (F1-F4): FF(L, f) <=> f_c L^2 even for all c <=> (L even) or (f = 0); for every L >= 2 and every ordering.')
    print(f'elapsed {time.time() - t0:.0f}s')
    print(f'TOTAL: PASS={PASS} FAIL={FAIL}')


if __name__ == '__main__':
    main()
