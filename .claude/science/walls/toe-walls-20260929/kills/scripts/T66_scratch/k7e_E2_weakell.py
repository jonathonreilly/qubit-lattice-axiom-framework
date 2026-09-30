"""E2 alone with the WEAK lapse-action conditions: (xi|>1)(n) may be nonzero beyond D<=1 (only sum_a L_a=0, sum_a a L_a=0), and sum_ab b ell_ab = 1.
Also allow the lattice Lie action on N to include ANY local bilinear (ell range up to 2R)."""
import sys
import numpy as np
from k7_GC import *
import k7_GC

R = int(sys.argv[1]); RL = int(sys.argv[2]) if len(sys.argv) > 2 else R
cols, rows, entries, b = solve.build(R, 'full')
nc0 = len(cols)
rows = dict(rows); entries = list(entries); b = dict(b)
def rid(key):
    if key not in rows: rows[key] = len(rows)
    return rows[key]
G1 = G1X(); T2N = T2('N'); C1N = C1('N')
for j, (lab, d) in enumerate(cols):
    fam, u = lab
    gc = {}
    if fam == 'G2':
        g2 = G2X(u); gc = fadd(bracket(g2, C1N), bracket(g2, T2N))
    elif fam == 'V2':
        gc = bracket(G1, V2_of(u, 'N'))
    elif fam == 'T3':
        gc = bracket(G1, T3_of(u, 'N'))
    for mono, cf in gc.items():
        entries.append((rid(('GC', mono)), j, cf))
ell = [(a, bb) for a in range(-RL, RL + 1) for bb in range(-RL, RL + 1)]
for k_, (a, bb) in enumerate(ell):
    gc = fadd(C1_of_Y(a, bb), T2_of_Y(a, bb))
    for mono, cf in gc.items():
        entries.append((rid(('GC', mono)), nc0 + k_, -cf))
r0 = rid(('ELLW0',)); r1 = rid(('ELLW1',)); r2 = rid(('ELL1',))
for k_, (a, bb) in enumerate(ell):
    entries.append((r0, nc0 + k_, F(1)))
    if a != 0: entries.append((r1, nc0 + k_, F(a)))
    if bb != 0: entries.append((r2, nc0 + k_, F(bb)))
b[r2] = F(1)
cols2 = cols + [(('ell', e), None) for e in ell]
inv = {v: k for k, v in rows.items()}
def sub(keep):
    ki = [i for i in range(len(rows)) if keep(inv[i])]
    rm = {o: n for n, o in enumerate(ki)}
    return cols2, {inv[o]: n for o, n in rm.items()}, [(rm[i], j, c) for (i, j, c) in entries if i in rm], {rm[i]: c for i, c in b.items() if i in rm}
isPP = lambda k: k[0] == 'GC' and any(v[0] == 'P' for v in k[1])
isE1 = lambda k: k[0] == 'GC' and not any(v[0] == 'P' for v in k[1])
ellrow = lambda k: k[0] in ('ELLW0', 'ELLW1', 'ELL1')
for name, keep in (('E2 + weak ell', lambda k: isPP(k) or ellrow(k)), ('E1 + weak ell', lambda k: isE1(k) or ellrow(k)), ('E1+E2 + weak ell', lambda k: isPP(k) or isE1(k) or ellrow(k)),
                   ('identity+norm + E1+E2 + weak ell', lambda k: True)):
    c, r, e, bb = sub(keep)
    print(f"R={R} ell-range={RL} {name:34s}", solve_sys(c, r, e, bb, match=False), flush=True)
