"""Fast (numpy) assembly of the 2D matched system, with cached orbit columns."""
import sys, time, pickle, os, itertools
from math import factorial, comb
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import lsqr
from collections import defaultdict
from fractions import Fraction as F
from solve2d_sym import build_sym, norm_key
from solve2d import *
from match2d import hyperplane_points2
from refs2d import REF2
from refs2d_frame import DELTAS
from solve2d_matched import LEVELS, npts_for, slots_of2

def get_cols(R):
    fn = f"cols_R{R}.pkl"
    if os.path.exists(fn):
        return pickle.load(open(fn, 'rb'))
    cols = build_sym(R)
    pickle.dump(cols, open(fn, 'wb'))
    return cols

def label_perms(labels):
    groups = defaultdict(list)
    for i, l in enumerate(labels):
        groups[l].append(i)
    idx_groups = list(groups.values())
    perms_per_group = [list(itertools.permutations(idx)) for idx in idx_groups]
    out = []
    for combo in itertools.product(*perms_per_group):
        assign = [None] * len(labels)
        for g, perm in zip(idx_groups, combo):
            for slot_i, k_i in zip(g, perm):
                assign[slot_i] = k_i
        out.append(assign)
    return out    # list of arrays: slot -> k index

def lat_vals(pts, perms, pos, D):
    """average over perms of (sum_j k_{perm(j)} . pos_j)^D / D!  ; pts: (n,m,2), pos: (m,2)"""
    acc = np.zeros(pts.shape[0])
    for pm in perms:
        s = np.einsum('nmk,mk->n', pts[:, pm, :], pos)
        acc += s ** D
    return acc / len(perms) / factorial(D)

def cont_vals(pts, perms, slots, D):
    acc = np.zeros(pts.shape[0])
    for pm in perms:
        v = np.ones(pts.shape[0])
        for i, (lab, (nx, ny)) in enumerate(slots):
            v = v * pts[:, pm[i], 0] ** nx * pts[:, pm[i], 1] ** ny
        acc += v
    return acc / len(perms)

def assemble_fast(cols, use_match, deltas=None):
    rows = {}
    entries_i, entries_j, entries_v = [], [], []
    b = {}
    def rid(key):
        if key not in rows:
            rows[key] = len(rows)
        return rows[key]
    for j, (lab, cs, fs) in enumerate(cols):
        for mono, c in cs.items():
            entries_i.append(rid(('I', mono))); entries_j.append(j); entries_v.append(float(c))
    for j, (lab, cs, fs) in enumerate(cols):
        if lab[0] == 'V2':
            u = substitute_uniform(fs, 'N')
            for mono, c in u.items():
                entries_i.append(rid(('R', mono))); entries_j.append(j); entries_v.append(float(c))
    if any(l[0] == 'V2' for l, _, _ in cols):
        for mono, c in R2_2D().items():
            b[rid(('R', mono))] = float(K * c)
    nr0 = len(rows)
    nrow = nr0
    if use_match:
        bytype = defaultdict(lambda: defaultdict(list))
        for j, (lab, cs, fs) in enumerate(cols):
            fam = lab[0]
            if fam not in use_match:
                continue
            for mono, c in fs.items():
                sl = slots_of2(mono)
                typ = tuple(t[0] for t in sl)
                bytype[(fam, typ)][j].append((float(c), np.array([[float(p[0]), float(p[1])] for _, p in sl])))
        tgt = defaultdict(list)
        for fam in use_match:
            for coef, slots in REF2.get(fam, []):
                sl = sorted(slots, key=lambda t: t[0])
                tgt[(fam, tuple(t[0] for t in sl))].append((float(coef), sl))
        dl = defaultdict(lambda: defaultdict(list))   # (fam,typ) -> r_i -> terms
        if deltas is not None:
            for r_i, d in enumerate(deltas):
                for fam in ('T3', 'V2', 'G2'):
                    if fam in use_match:
                        for coef, sl0 in d[fam]:
                            sl = sorted(sl0, key=lambda t: t[0])
                            dl[(fam, tuple(t[0] for t in sl))][r_i].append((float(coef), sl))
        keys = set(bytype) | set(tgt) | set(dl)
        for (fam, typ) in sorted(keys, key=str):
            m = len(typ)
            perms = label_perms(typ)
            for D in LEVELS[fam]:
                npts = npts_for(m, D)
                pts = np.array([[[float(k[0]), float(k[1])] for k in ks] for ks in hyperplane_points2(m, npts, seed=7 + D)])
                block = np.zeros((npts, len(cols) + (len(deltas) if deltas else 0)))
                for j, lst in bytype.get((fam, typ), {}).items():
                    v = np.zeros(npts)
                    for c, pos in lst:
                        v += c * lat_vals(pts, perms, pos, D)
                    block[:, j] = v
                rhs = np.zeros(npts)
                for coef, sl in tgt.get((fam, typ), []):
                    if sum(n[0] + n[1] for _, n in sl) == D:
                        rhs += coef * cont_vals(pts, perms, sl, D)
                for r_i, lst in dl.get((fam, typ), {}).items():
                    v = np.zeros(npts)
                    for coef, sl in lst:
                        if sum(n[0] + n[1] for _, n in sl) == D:
                            v += coef * cont_vals(pts, perms, sl, D)
                    block[:, len(cols) + r_i] = -v
                nzr = np.nonzero((np.abs(block).sum(axis=1) > 0) | (np.abs(rhs) > 0))[0]
                for r in nzr:
                    ri = nrow; nrow += 1
                    jj = np.nonzero(block[r])[0]
                    for j in jj:
                        entries_i.append(ri); entries_j.append(int(j)); entries_v.append(float(block[r, j]))
                    if rhs[r] != 0:
                        b[ri] = float(rhs[r])
    return nrow, nr0, entries_i, entries_j, entries_v, b

def solve_fast(nrow, nr0, ei, ej, ev, b, ncols, iters=400000):
    A = sps.coo_matrix((np.array(ev), (np.array(ei), np.array(ej))), shape=(nrow, ncols)).tocsr()
    bb = np.zeros(nrow)
    for i, c in b.items():
        bb[i] = c
    sol = lsqr(A, bb, atol=1e-15, btol=1e-15, iter_lim=iters, conlim=1e15)
    x = sol[0]
    r = A @ x - bb
    return dict(istop=sol[1], iters=sol[2], resid=float(np.linalg.norm(r)), r_id=float(np.linalg.norm(r[:nr0])), r_match=float(np.linalg.norm(r[nr0:])), bnorm=float(np.linalg.norm(bb))), x, A, bb

if __name__ == '__main__':
    R = int(sys.argv[1]); mode = sys.argv[2]
    match = tuple(sys.argv[3].split(',')) if len(sys.argv) > 3 else ('V2', 'T3', 'G2', 'xi1', 'chi')
    t0 = time.time()
    cols = get_cols(R)
    print("cols", len(cols), "t", round(time.time() - t0, 1), flush=True)
    frame = (mode == 'frame')
    nrow, nr0, ei, ej, ev, b = assemble_fast(cols, match, DELTAS if frame else None)
    nc = len(cols) + (len(DELTAS) if frame else 0)
    print("rows", nrow, "nr0", nr0, "nnz", len(ev), "t", round(time.time() - t0, 1), flush=True)
    res, x, A, bb = solve_fast(nrow, nr0, ei, ej, ev, b, nc)
    print("RESULT R", R, mode, "match", match, res, "t", round(time.time() - t0, 1), flush=True)
    np.save(f"xfast_R{R}_{mode}.npy", x)
