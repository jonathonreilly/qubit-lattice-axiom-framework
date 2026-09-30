"""Same as solve2d_fast but with rows de-duplicated by the D4 orbit of their monomial (columns are symmetric, so images are proportional)."""
import sys, time, pickle
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import lsqr
from solve2d_fast import *
from group2d import GROUP, act_mono
from engine2 import canon

def rep_of(mono):
    best = None
    for g in GROUP:
        s, m = act_mono(g, mono)
        m = canon(m)
        if best is None or m < best:
            best = m
    return best

def assemble_dedupe(cols, use_match, deltas=None):
    # replicate assemble_fast but keep only canonical-orbit identity/norm rows
    rows = {}
    ei, ej, ev = [], [], []
    b = {}
    keep = {}
    def rid(key):
        if key not in rows:
            rows[key] = len(rows)
        return rows[key]
    cache = {}
    def keep_key(kind, mono):
        k = (kind, mono)
        if k in cache: return cache[k]
        ok = (rep_of(mono) == mono)
        cache[k] = ok
        return ok
    for j, (lab, cs, fs) in enumerate(cols):
        for mono, c in cs.items():
            if keep_key('I', mono):
                ei.append(rid(('I', mono))); ej.append(j); ev.append(float(c))
    for j, (lab, cs, fs) in enumerate(cols):
        if lab[0] == 'V2':
            u = substitute_uniform(fs, 'N')
            for mono, c in u.items():
                if keep_key('R', mono):
                    ei.append(rid(('R', mono))); ej.append(j); ev.append(float(c))
    for mono, c in R2_2D().items():
        if keep_key('R', mono):
            b[rid(('R', mono))] = float(K * c)
    return rows, ei, ej, ev, b

if __name__ == '__main__':
    R = int(sys.argv[1]); mode = sys.argv[2]
    match = tuple(sys.argv[3].split(',')) if len(sys.argv) > 3 else ('V2', 'T3', 'G2', 'xi1', 'chi')
    t0 = time.time()
    cols = get_cols(R)
    frame = (mode == 'frame')
    rows, ei, ej, ev, b = assemble_dedupe(cols, match, DELTAS if frame else None)
    nr0 = len(rows)
    print("deduped identity+norm rows", nr0, "t", round(time.time() - t0, 1), flush=True)
    # matching rows via assemble_fast machinery but skipping identity part: reuse by calling with use_match and slicing
    nrow, nr0_full, ei_f, ej_f, ev_f, b_f = assemble_fast([(l, {}, fs) if l[0] != 'V2' else (l, {}, fs) for l, cs, fs in cols], match, DELTAS if frame else None)
    # in the call above identity columns were emptied, V2 normalization rows are present in first nr0_full rows; keep only matching rows (index >= nr0_full)
    ei_f = np.array(ei_f); ej_f = np.array(ej_f); ev_f = np.array(ev_f)
    sel = ei_f >= nr0_full
    base = nr0
    ei2 = list(ei) + list(ei_f[sel] - nr0_full + base)
    ej2 = list(ej) + list(ej_f[sel])
    ev2 = list(ev) + list(ev_f[sel])
    b2 = dict(b)
    for i, c in b_f.items():
        if i >= nr0_full:
            b2[i - nr0_full + base] = c
    nrow2 = base + (nrow - nr0_full)
    nc = len(cols) + (len(DELTAS) if frame else 0)
    print("rows", nrow2, "match rows", nrow - nr0_full, "nnz", len(ev2), "t", round(time.time() - t0, 1), flush=True)
    res, x, A, bb = solve_fast(nrow2, nr0, ei2, ej2, ev2, b2, nc)
    print("RESULT-DEDUPED R", R, mode, "match", match, res, "t", round(time.time() - t0, 1), flush=True)
    np.save(f"xfast2_R{R}_{mode}.npy", x)
