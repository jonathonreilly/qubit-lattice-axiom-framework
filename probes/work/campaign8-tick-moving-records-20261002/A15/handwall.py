#!/usr/bin/env python3
"""A15 aside (task 4): a 'handedness wall' in the A11 toy: region R (vertical strip) runs the mirror word
(-x,+y,+x,-y) at offset k, region L the right-handed word; rigid clocks + handshake. Current per column as in
a11walls.py (positive = toward +y)."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
import a11walls as aw
DR = [(1, 0), (0, 1), (-1, 0), (0, -1)]
DM = [(-1, 0), (0, 1), (1, 0), (0, -1)]
L = 16
def run(k):
    inR = lambda x: 4 <= x < 12
    def partner(x, y, t):
        D = DM if inR(x) else DR
        j = (t + (k if inR(x) else 0)) % 4
        dx, dy = D[j]
        if (x + y) % 2 == 0:
            return ((x + dx) % L, (y + dy) % L)
        return ((x - dx) % L, (y - dy) % L)
    where = {(x, y): (x, y) for x in range(L) for y in range(L)}
    disp = {(x, y): (0, 0) for x in range(L) for y in range(L)}
    for t in range(4):
        sel = {(x, y): partner(x, y, t) for x in range(L) for y in range(L)}
        new = dict(where)
        for a, b in sel.items():
            if sel[b] == a and a < b:
                ia, ib = where[a], where[b]
                new[a], new[b] = ib, ia
                vx = ((b[0] - a[0] + L // 2) % L) - L // 2; vy = ((b[1] - a[1] + L // 2) % L) - L // 2
                disp[ia] = (disp[ia][0] + vx, disp[ia][1] + vy); disp[ib] = (disp[ib][0] - vx, disp[ib][1] - vy)
        where = new
    final = {it: st for st, it in where.items()}
    cross = sum(1 for it, st in final.items() if inR(it[0]) != inR(st[0]))
    cur = np.array([aw.column_current(L, disp, yc) for yc in range(L)]).mean(axis=0)
    return cross, cur
for k in (0, 1, 2, 3):
    cross, cur = run(k)
    print("mirror strip, offset %d: crossing items %d; current per column: %s; wall1 window (cols 1-6) %+.2f, wall2 (cols 9-14) %+.2f"
          % (k, cross, " ".join("%+.1f" % v for v in cur), cur[1:7].sum(), cur[9:15].sum()))
