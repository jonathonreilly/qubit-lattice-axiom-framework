"""E2 with the first-class freedom the attack itself allowed for {C,C} (its chi): {G[xi],C[N]} = C[xi|>N] + G[Z], Z(xi,N;P) linear in P.
In the PP sector: {G2,T2}+{G1,T3} = T2[ell] + G1[Z],  Z(n) = sum z_{a,b,e,i} xi(n+a) N(n+b) P_e(n+i)."""
import sys, itertools
import numpy as np
from k7_GC import *
import k7_GC

R = int(sys.argv[1]); RL = int(sys.argv[2]) if len(sys.argv) > 2 else R; RZ = int(sys.argv[3]) if len(sys.argv) > 3 else R
useZ = (len(sys.argv) <= 4) or sys.argv[4] != 'noZ'
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
nz = 0
if useZ:
    Zs = [(a, bb, e, i) for a in range(-RZ, RZ + 1) for bb in range(-RZ, RZ + 1) for e in COMPS for i in range(-RZ, RZ + 1)]
    for k_, (a, bb, e, i) in enumerate(Zs):
        # G1[Z] = sum_n 2 P_x(n) (Z(n) - Z(n-1)), Z(n) = xi(n+a) N(n+bb) P_e(n+i)
        zm = (Xv(a), V('N', 0, bb), V('P', e, i))
        gz = {}
        add(gz, zm + (V('P', XX, 0),), F(2))
        add(gz, shift_generic(zm, -1) + (V('P', XX, 0),), F(-2))
        for mono, cf in gz.items():
            entries.append((rid(('GC', mono)), nc0 + len(ell) + k_, -cf))
    nz = len(Zs)
ncols = nc0 + len(ell) + nz
cols2 = cols + [(('ell', e), None) for e in ell] + [(('Z', k), None) for k in range(nz)]
inv = {v: k for k, v in rows.items()}
def sub(keep):
    ki = [i for i in range(len(rows)) if keep(inv[i])]
    rm = {o: n for n, o in enumerate(ki)}
    return cols2, {inv[o]: n for o, n in rm.items()}, [(rm[i], j, c) for (i, j, c) in entries if i in rm], {rm[i]: c for i, c in b.items() if i in rm}
isPP = lambda k: k[0] == 'GC' and any(v[0] == 'P' for v in k[1])
isE1 = lambda k: k[0] == 'GC' and not any(v[0] == 'P' for v in k[1])
ellrow = lambda k: k[0] in ('ELLW0', 'ELLW1', 'ELL1')
tag = f"R={R} ellR={RL} Z={'R'+str(RZ) if useZ else 'none'}"
for name, keep in (('E2 + weak ell', lambda k: isPP(k) or ellrow(k)),
                   ('E1+E2 + weak ell', lambda k: isPP(k) or isE1(k) or ellrow(k)),
                   ('identity+norm+E1+E2+weak ell', lambda k: True)):
    c, r, e, bb = sub(keep)
    print(f"{tag} {name:32s}", solve_sys(c, r, e, bb, match=False), flush=True)
