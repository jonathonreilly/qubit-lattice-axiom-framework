"""A1 identity + E1 ({G,C} in the potential sector) + full ADM match, planar: is the potential-sector covariance jointly satisfiable with A1?"""
import sys
from k7_GC import *
import k7_GC
sys.argv = ['x'] + sys.argv[1:]
R = int(sys.argv[1])
cols, rows, entries, b, nc0 = build_GC(R, s=1)
inv = {v: k for k, v in rows.items()}
isPP = lambda k: k[0] == 'GC' and any(v[0] == 'P' for v in k[1])
keep = [i for i in range(len(rows)) if not isPP(inv[i])]
rm = {o: n for n, o in enumerate(keep)}
rows2 = {inv[o]: n for o, n in rm.items()}
ent2 = [(rm[i], j, c) for (i, j, c) in entries if i in rm]
b2 = {rm[i]: c for i, c in b.items() if i in rm}
print(f"R={R} A1 identity + E1 + ell conds, no ADM match:", solve_sys(cols, rows2, ent2, b2, match=False), flush=True)
print(f"R={R} A1 identity + E1 + ell conds, full ADM match (V2,T3,G2,xi1,chi):", solve_sys(cols, rows2, ent2, b2, match=True), flush=True)
