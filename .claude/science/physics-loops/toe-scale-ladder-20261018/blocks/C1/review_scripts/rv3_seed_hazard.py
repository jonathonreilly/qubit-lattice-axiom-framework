#!/usr/bin/env python3
"""Reviewer check R3: which sector does the CURRENT driver.Sim start in for the seeds used by step2 (101..131),
dbg_vend (31..36), step3 (201..208) and production (1,2,3,11,100,111)?  Uses the block's driver/lattice only to
build the start state; sector membership is decided by an own BFS + winding (flux) computation."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts"))
import numpy as np
from driver import Sim
from lattice import Lattice
RES = []
def check(n, ok, d=""):
    RES.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {n}" + (f" :: {d}" if d else ""), flush=True)
lat = Lattice(2)
def comp(s):
    seen = {tuple(s)}; st = [s]
    while st:
        c = st.pop()
        for p in np.flatnonzero(lat.flippable(c)):
            t = c.copy(); t[lat.plinks[p]] *= -1
            if tuple(t) not in seen: seen.add(tuple(t)); st.append(t)
    return seen
C0 = comp(lat.canonical())
def flux(s):
    return tuple(int(s[(lat.lori == a) & (lat.coords[lat.tail][:, a] == 0)].sum()) for a in range(3))
out = {}
for sd in list(range(101, 132)) + list(range(31, 37)) + list(range(201, 209)) + [1, 2, 3, 11, 100, 111]:
    s0 = Sim(2, 0.0, 1.0, seed=sd).s0
    out[sd] = (tuple(s0) in C0, flux(s0))
st2 = [sd for sd in range(101, 132)]
check("current driver: every step2 seed (101..131) starts OUTSIDE the W=0 canonical component (hazard confirmed)",
      all(not out[s][0] for s in st2), f"fluxes {sorted({out[s][1] for s in st2})}")
check("current driver: dbg_vend seeds 31..36 start inside the W=0 component", all(out[s][0] for s in range(31, 37)))
check("current driver: step3 seeds 201..208 start outside W=0 with sigma-flux magnitude 2 along x",
      all((not out[s][0]) and abs(out[s][1][0]) == 2 for s in range(201, 209)))
check("current driver: production seeds 1,2,3,11 in W=0; 100,111 in the W=1 sector",
      all(out[s][0] for s in (1, 2, 3, 11)) and all(abs(out[s][1][0]) == 2 and not out[s][0] for s in (100, 111)))
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
