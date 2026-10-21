#!/usr/bin/env python3
"""C4f descriptive: what a magnon pair does at an empty/full interface, and the Theta-mirror check
for collisions (exact simulation on the L=12 torus, dense implementation).

(1) background: full slab z in [7, 10] (empty elsewhere); a magnon face pair {x0, x0+(1,1,0)} at
    height z0 moving +e3 toward the slab, for several lateral positions; record the outcome after
    12 ticks (descriptive).
(2) Theta-mirror: for every configuration c in (1), the image Theta c = complement of P_R c
    (R = C4z) evolves as Theta U^t c (exact check over the whole trajectory).
(3) head-on magnon pair collisions in the empty background (C4e table had all 50 pass through;
    here the dilute 2-pair sector differs from C4e only through the control sets): count
    pass-through / other outcomes (descriptive).
"""
import sys, os, itertools
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c4f_dense as Dn
import c4f_core as C

P = F = 0
def check(name, ok, info=''):
    global P, F
    if ok: P += 1; print('PASS', name, info, flush=True)
    else: F += 1; print('FAIL', name, info, flush=True)

L = 12; DU = Dn.DenseU(L); T = DU.T
O = C.build_O()
R4 = [i for i, M in enumerate(O) if np.array_equal(M, [[0, -1, 0], [1, 0, 0], [0, 0, 1]])][0]
img = T.idx(T.coords @ O[R4].T); inv = np.empty(T.V, int); inv[img] = np.arange(T.V)
def Theta(c): return ~c[inv]

slab = (T.coords[:, 2] >= 7) & (T.coords[:, 2] <= 10)
outcomes = {}
mirror_ok = True
for x0 in itertools.product(range(2), range(2)):
    for z0 in (2, 3):
        c = slab.copy(); c[T.idx([(x0[0], x0[1], z0), (x0[0] + 1, x0[1] + 1, z0)])] = True
        traj = [c]
        for t in range(12): traj.append(DU(traj[-1]))
        # Theta mirror
        m = Theta(c)
        for t in range(12):
            m = DU(m); mirror_ok &= np.array_equal(m, Theta(traj[t + 1]))
        # describe: magnons outside slab, holes inside slab
        out = traj[-1]
        mag = [tuple(int(v) for v in T.coords[i]) for i in np.nonzero(out & ~slab)[0]]
        hol = [tuple(int(v) for v in T.coords[i]) for i in np.nonzero(~out & slab)[0]]
        key = f'x0={x0} z0={z0}'
        outcomes[key] = (mag, hol)
        print(f'{key}: after 12 ticks magnons outside slab {mag}; holes inside slab {hol}')
check('Theta = (P_C4z o C) mirror: Theta U^t c = U^t Theta c along all 8 interface trajectories (12 ticks)', mirror_ok)

# head-on pairs in empty background (C4e set-up: (1,1,0) moving +e3 vs (1,-1,0) moving -e3)
U = C.Dyn()
npass = nother = 0
for dx in range(-2, 3):
    for dy in range(-2, 3):
        for gap in (5, 6):
            a = frozenset({(0, 0, 0), (1, 1, 0)})
            b = frozenset({(dx, dy + 1, gap), (dx + 1, dy, gap)})
            c = a | b; x = c
            for t in range(gap + 6): x = U(x)
            fa = frozenset(C.add(z, (0, 0, gap + 6)) for z in a)
            fb = frozenset(C.add(z, (0, 0, -(gap + 6))) for z in b)
            # pass-through: two face pairs, one (1,1,0)-type above, one (1,-1,0)-type below
            pts = sorted(x)
            ok = len(x) == 4 and max(z[2] for z in x) > gap and min(z[2] for z in x) < 0
            npass += ok; nother += not ok
print(f'head-on pairs (25 lateral offsets x 2 gaps): {npass} separated past each other, {nother} other')
check('head-on collision table computed (descriptive)', npass + nother == 50)
print(f'TOTAL: PASS={P} FAIL={F}')
