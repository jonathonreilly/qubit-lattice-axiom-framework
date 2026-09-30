"""2D degree-2 identity with D4-symmetrised unknowns, optional ADM-frame matching. Sparse lsqr consistency."""
import sys, time, pickle
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import lsqr
from collections import defaultdict
from fractions import Fraction as F
from solve2d import *
from group2d import *
from match2d import *
from refs2d import REF2
from solve2d_matched import LEVELS, npts_for, slots_of2


def family_functional(fam, u):
    """The unknown's own functional (canonical dict): the object matched to the continuum."""
    if fam in ('V2', 'T3'):
        return {tuple(sorted(u)): F(1)} if False else V2_of(u, 'N')
    if fam == 'G2':
        dirn, c, p, d, q = u
        bl = ('Xx', 0, (1, 0)) if dirn == 'x' else ('Xy', 0, (0, 1))
        out = {}
        add(out, (bl, ('P', c, p), ('h', d, q)), F(1))
        return out
    if fam == 'xi1':
        return col_xi1(u)
    if fam == 'chi':
        return col_chi(u)


def base_column(fam, u):
    if fam == 'V2':
        return col_V2(u)
    if fam == 'T3':
        return col_T3(u)
    if fam == 'G2':
        return fscale(col_G2(u), F(-1))
    if fam == 'xi1':
        return fscale(col_xi1(u), F(-1))
    if fam == 'chi':
        return fscale(col_chi(u), F(-1))


def norm_key(fun):
    items = sorted(fun.items())
    if not items:
        return None
    sgn = 1 if items[0][1] > 0 else -1
    return tuple((k, v * sgn) for k, v in items)


def build_sym(R, fams=('V2', 'T3', 'G2', 'xi1', 'chi'), verbose=True):
    t0 = time.time()
    enums = {'V2': enum_V2, 'T3': enum_T3, 'G2': enum_G2, 'xi1': enum_xi1, 'chi': enum_chi}
    cols = []   # (label, colsym, fsym)
    for fam in fams:
        seen = set()
        cnt = 0
        for u in enums[fam](R):
            f = family_functional(fam, u)
            fs = symmetrize(f)
            key = norm_key(fs)
            if key is None or key in seen:
                continue
            seen.add(key)
            # orientation: colsym sign relative to fs sign
            col = base_column(fam, u)
            cs = symmetrize(col)
            cols.append(((fam, u), cs, fs))
            cnt += 1
        if verbose:
            print(fam, "orbits:", cnt, "t", round(time.time() - t0, 1))
    return cols


def assemble(cols, use_match, R, deltas=None):
    rows = {}
    entries = []
    b = {}
    def rid(key):
        if key not in rows:
            rows[key] = len(rows)
        return rows[key]
    for j, (lab, cs, fs) in enumerate(cols):
        for mono, c in cs.items():
            entries.append((rid(('I', mono)), j, c))
    # V2 normalisation (symmetrised N->1)
    for j, (lab, cs, fs) in enumerate(cols):
        if lab[0] == 'V2':
            u = substitute_uniform(fs, 'N')
            for mono, c in u.items():
                entries.append((rid(('R', mono)), j, c))
    # target: R2_2D is D4 invariant
    if any(l[0] == 'V2' for l, _, _ in cols):
        for mono, c in R2_2D().items():
            b[rid(('R', mono))] = K * c
    nr0 = len(rows)
    if use_match:
        bytype = defaultdict(lambda: defaultdict(list))
        for j, (lab, cs, fs) in enumerate(cols):
            fam = lab[0]
            if fam not in use_match:
                continue
            for mono, c in fs.items():
                sl = slots_of2(mono)
                typ = tuple(t[0] for t in sl)
                bytype[(fam, typ)][j].append((c, sl))
        tgt = defaultdict(list)
        for fam in use_match:
            for coef, slots in REF2.get(fam, []):
                sl = sorted(slots, key=lambda t: t[0])
                typ = tuple(t[0] for t in sl)
                tgt[(fam, typ)].append((coef, sl))
        dtypes = set()
        if deltas is not None:
            for dl in deltas:
                for fam in ('T3', 'V2', 'G2'):
                    if fam in use_match:
                        for coef, sl0 in dl[fam]:
                            dtypes.add((fam, tuple(sorted(t[0] for t in sl0))))
        for (fam, typ) in sorted(set(bytype) | set(tgt) | dtypes, key=str):
            m = len(typ)
            for D in LEVELS[fam]:
                pts = hyperplane_points2(m, npts_for(m, D), seed=7 + D)
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
                    if deltas is not None and fam in ('T3', 'V2', 'G2'):
                        for r_i, dl in enumerate(deltas):
                            dv = F(0)
                            for coef, sl0 in dl[fam]:
                                sl = sorted(sl0, key=lambda t: t[0])
                                if tuple(t[0] for t in sl) == typ and sum(n[0] + n[1] for _, n in sl) == D:
                                    dv += sym_cont2(coef, sl, ks)
                            if dv != 0:
                                row[len(cols) + r_i] = -dv
                    if row or rhs != 0:
                        ri = len(rows)
                        rows[('M', fam, typ, D, ri)] = ri
                        for j, v in row.items():
                            entries.append((ri, j, v))
                        if rhs != 0:
                            b[ri] = rhs
    return rows, entries, b, nr0


def solve(rows, entries, b, ncols, nr0, iters=400000):
    A, bb = to_sparse(entries, b, len(rows), ncols)
    sol = lsqr(A, bb, atol=1e-15, btol=1e-15, iter_lim=iters, conlim=1e15)
    x = sol[0]
    r = A @ x - bb
    return dict(istop=sol[1], iters=sol[2], resid=float(np.linalg.norm(r)), r_id=float(np.linalg.norm(r[:nr0])), r_match=float(np.linalg.norm(r[nr0:])), bnorm=float(np.linalg.norm(bb))), x, A, bb


if __name__ == '__main__':
    R = int(sys.argv[1])
    match = tuple(sys.argv[2].split(',')) if len(sys.argv) > 2 and sys.argv[2] != 'none' else ()
    fams = tuple(sys.argv[3].split(',')) if len(sys.argv) > 3 else ('V2', 'T3', 'G2', 'xi1', 'chi')
    t0 = time.time()
    cols = build_sym(R, fams)
    print("orbit columns:", len(cols), " t", round(time.time() - t0, 1))
    rows, entries, b, nr0 = assemble(cols, match, R)
    print("rows", len(rows), "identity+norm rows", nr0, "nnz", len(entries), " t", round(time.time() - t0, 1))
    res, x, A, bb = solve(rows, entries, b, len(cols), nr0)
    print("match:", match, res, " t", round(time.time() - t0, 1))
