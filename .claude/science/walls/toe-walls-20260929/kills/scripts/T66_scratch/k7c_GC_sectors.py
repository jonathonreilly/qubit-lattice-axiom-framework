import sys, time
import numpy as np
from k7_GC import *
import k7_GC

def filt(cols, rows, entries, b, keep):
    """keep(rowkey)->bool for GC rows; other rows kept."""
    inv = {v: k for k, v in rows.items()}
    keepidx = [i for i in range(len(rows)) if (inv[i][0] != 'GC' or keep(inv[i]))]
    remap = {old: new for new, old in enumerate(keepidx)}
    rows2 = {inv[old]: new for old, new in remap.items()}
    entries2 = [(remap[i], j, c) for (i, j, c) in entries if i in remap]
    b2 = {remap[i]: c for i, c in b.items() if i in remap}
    return cols, rows2, entries2, b2

R = int(sys.argv[1])
for s in (1, 0):
    base = build_GC(R, s=s)
    cols, rows, entries, b, nc0 = base
    for name, keep in (('E1 only (h^1 sector)', lambda k: not any(v[0] == 'P' for v in k[1])),
                       ('E2 only (PP sector)', lambda k: any(v[0] == 'P' for v in k[1])),
                       ('E1+E2', lambda k: True)):
        c2, r2, e2, b2 = filt(cols, rows, entries, b, keep)
        res = solve_sys(c2, r2, e2, b2, match=False)
        print(f"R={R} ELL1 rhs s={s}  {name:22s} rows {res['rows']} cols {res['cols']} rank_mod {res['rank_mod']} float_resid {res['float_resid']:.3e} modOK {res['mod_consistent']}", flush=True)
