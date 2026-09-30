"""2D: degree-2 identity + ADM-frame continuum matching rows. Consistency by sparse lsqr."""
import sys, time
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import lsqr
from collections import defaultdict
from fractions import Fraction as F
from solve2d import *
from match2d import *
from refs2d import REF2

LEVELS = {'V2': (0, 1, 2), 'T3': (0,), 'G2': (0, 1), 'xi1': (0, 1, 2), 'chi': (0, 1, 2, 3)}


def npts_for(m, D):
    nv = 2 * (m - 1)
    from math import comb
    return min(90, comb(D + nv - 1, nv - 1) + 6)


def lattice_fun2(lab):
    fam, u = lab
    if fam == 'V2':
        return V2_of(u, 'N')
    if fam == 'T3':
        return V2_of(u, 'N')
    if fam == 'G2':
        dirn, c, p, d, q = u
        bl = ('Xx', 0, (1, 0)) if dirn == 'x' else ('Xy', 0, (0, 1))
        return {(bl, ('P', c, p), ('h', d, q)): F(1)}
    if fam == 'xi1':
        return col_xi1(u)
    if fam == 'chi':
        return col_chi(u)


def slots_of2(mono):
    sl = [((v[0], v[1]), (F(v[2][0], 2), F(v[2][1], 2))) for v in mono]
    sl.sort(key=lambda t: t[0])
    return sl


def match_rows2(cols, fams, levels=LEVELS, seed=7):
    rows = []
    bytype = defaultdict(lambda: defaultdict(list))
    for j, (lab, _) in enumerate(cols):
        fam = lab[0]
        if fam not in fams:
            continue
        fun = lattice_fun2(lab)
        for mono, c in fun.items():
            sl = slots_of2(mono)
            typ = tuple(t[0] for t in sl)
            bytype[(fam, typ)][j].append((c, sl))
    tgt = defaultdict(list)
    for fam in fams:
        for coef, slots in REF2.get(fam, []):
            sl = sorted(slots, key=lambda t: t[0])
            typ = tuple(t[0] for t in sl)
            tgt[(fam, typ)].append((coef, sl))
    keys = set(bytype.keys()) | set(tgt.keys())
    for (fam, typ) in sorted(keys, key=str):
        m = len(typ)
        for D in levels[fam]:
            pts = hyperplane_points2(m, npts_for(m, D), seed=seed + D)
            for ks in pts:
                row = {}
                for j, lst in bytype.get((fam, typ), {}).items():
                    v = sum((c * sym_lattice2(sl, ks, D) for c, sl in lst), F(0))
                    if v != 0:
                        row[j] = v
                rhs = F(0)
                for coef, sl in tgt.get((fam, typ), []):
                    if sum(n[0] + n[1] for _, n in sl) == D:
                        rhs += sym_cont2(coef, sl, ks)
                if row or rhs != 0:
                    rows.append((row, rhs))
    return rows


def run(R, fams=('V2', 'T3', 'G2', 'xi1', 'chi'), use=('V2', 'T3', 'G2', 'xi1', 'chi')):
    t0 = time.time()
    cols, rows_d, entries, b = build(R, 'full', use, verbose=False)
    nr0 = len(rows_d)
    entries = list(entries); b = dict(b)
    mrows = match_rows2(cols, fams)
    for r, (row, rhs) in enumerate(mrows):
        ri = nr0 + r
        for j, v in row.items():
            entries.append((ri, j, v))
        if rhs != 0:
            b[ri] = rhs
    nr = nr0 + len(mrows); nc = len(cols)
    print("R", R, "cols", nc, "identity rows", nr0, "match rows", len(mrows), "t", round(time.time() - t0, 1))
    A, bb = to_sparse(entries, b, nr, nc)
    sol = lsqr(A, bb, atol=1e-15, btol=1e-15, iter_lim=400000, conlim=1e15)
    x = sol[0]
    res = np.linalg.norm(A @ x - bb)
    # separate residual norms: identity block vs matching block
    r_all = A @ x - bb
    r_id = np.linalg.norm(r_all[:nr0]); r_m = np.linalg.norm(r_all[nr0:])
    print("lsqr istop", sol[1], "iters", sol[2], "residual", res, "identity-block", r_id, "match-block", r_m, "|b|", np.linalg.norm(bb))
    return res, (cols, entries, b, A, bb, x, nr0)


if __name__ == '__main__':
    R = int(sys.argv[1])
    fams = tuple(sys.argv[2].split(',')) if len(sys.argv) > 2 else ('V2', 'T3', 'G2', 'xi1', 'chi')
    print("matching:", fams)
    run(R, fams)
