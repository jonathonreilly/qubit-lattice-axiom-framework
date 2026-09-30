"""Does E2 (kinetic-term covariance under the momentum rule) alone -- without the {C,C} identity -- admit a local lattice solution,
with and without the ADM continuum limit of T3, G2 and of the lapse action ell?"""
import sys
from k7_GC import *
import k7_GC
import solve2

def filt_rows(cols, rows, entries, b, keepkey):
    inv = {v: k for k, v in rows.items()}
    keepidx = [i for i in range(len(rows)) if keepkey(inv[i])]
    remap = {old: new for new, old in enumerate(keepidx)}
    rows2 = {inv[old]: new for old, new in remap.items()}
    entries2 = [(remap[i], j, c) for (i, j, c) in entries if i in remap]
    b2 = {remap[i]: c for i, c in b.items() if i in remap}
    return cols, rows2, entries2, b2

R = int(sys.argv[1])
cols, rows, entries, b, nc0 = build_GC(R, s=1)
isPP = lambda k: k[0] == 'GC' and any(v[0] == 'P' for v in k[1])
isE1 = lambda k: k[0] == 'GC' and not any(v[0] == 'P' for v in k[1])
ell_rows = lambda k: k[0] in ('ELL0', 'ELL1')
for name, keep in (('E2 + ell conds', lambda k: isPP(k) or ell_rows(k)),
                   ('E1 + ell conds', lambda k: isE1(k) or ell_rows(k)),
                   ('E1+E2 + ell conds', lambda k: isPP(k) or isE1(k) or ell_rows(k))):
    c2, r2, e2, b2 = filt_rows(cols, rows, entries, b, keep)
    print(f"R={R} {name:22s} no match:", solve_sys(c2, r2, e2, b2, match=False), flush=True)
    print(f"R={R} {name:22s} ADM match (T3,G2 families only):", solve_sys(c2, r2, e2, b2, match=True, fams=('T3', 'G2')), flush=True)
