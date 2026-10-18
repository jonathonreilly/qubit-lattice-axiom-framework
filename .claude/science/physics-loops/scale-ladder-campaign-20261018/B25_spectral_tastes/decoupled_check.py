#!/usr/bin/env python3
"""B25 part 1e: the only census word with [Lambda_sp : Lambda_u] > 2 is decoupled.
B24-skeleton word S4.P9.S4.L101.S4.P6 (on-site letters all plane letters) has (Lambda_u, Lambda_sp) = (bcc(pi/2), sc(pi/4)),
index 4, with three k-dependent cosets.  Every letter commutes with Z_x, Z_y, Z_z, so W(k) is block-diagonal over the three
coordinate planes (4 corners each), the plane-z block depends on (k_x, k_y) only, and every band is flat along the
perpendicular direction of its plane: no point node can be an isotropic cone.  Also: in the census, every word with
index > 2 has only plane/L202/identity on-site letters.  Prints PASS/FAIL, TOTAL."""
import sys, os, time, pickle
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
ALL.update(PLANE6)
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
w = build24(('S4', 'p', 'S4', 'q', 'S4', 'o'), ('P9', 'L101', 'P6'))
rng = np.random.default_rng(8); KS = rng.uniform(-np.pi, np.pi, (5, 3))
check("[W(k), Z_i] = 0 for i = x, y, z (block-diagonal over the coordinate planes)", all(np.allclose(Wb(w, k[None])[0] @ Z, Z @ Wb(w, k[None])[0]) for k in KS for Z in Zs))
pz = np.where(fcI[:, 2] == 0)[0]
def blockz(k): return Wb(w, k[None])[0][np.ix_(pz, pz)]
ok = all(np.allclose(np.sort(np.angle(np.linalg.eigvals(blockz(k)))), np.sort(np.angle(np.linalg.eigvals(blockz(k + np.array([0, 0, dz])))))) for k in KS for dz in (0.37, 1.9))
check("plane-z block spectrum is independent of k_z (bands flat along e_z)", ok)
R = pickle.load(open(os.path.join(HERE, 'census.pkl'), 'rb'))['R']
big = [(j, r) for j, r in R if r and r.get('index', 1) > 2]
planeish = set(PLANE) | set(PLANE6) | {'L202', 'H00', 'L000'}
print("   census words with index > 2:", [(j[1], j[2], r['Lu'], r['Lsp'], r['index']) for j, r in big])
check("every census word with index > 2 has only plane/L202/identity on-site letters (decoupled)", len(big) > 0 and all(set(j[2]) <= planeish for j, r in big))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
