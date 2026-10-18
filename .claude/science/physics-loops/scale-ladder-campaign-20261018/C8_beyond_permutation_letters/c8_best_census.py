#!/usr/bin/env python3
"""C8: full node census (no early reject) of the closest class-3 screen cases: every (pi/4)Z^3 node at E plus Nelder-Mead
from the 40 lowest 16^3 points, classified by DPT (c8lib.classify2).  Same criterion as c8_screen stage C."""
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c8lib import *
from scipy.optimize import minimize
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
CASES = [(('E+', 'S', 'o'), ('L033',), -np.pi / 4), (('E+', 'Rt', 'S', 'o'), ('L011',), -np.pi / 4), (('E+', 'S', 'R', 'o'), ('L011',), 3 * np.pi / 4),
         (('E+', 'S', 'Rt', 'o'), ('L011',), -np.pi / 4)]
allbad = True
for sk, nm, E in CASES:
    it = iter(nm); w = [PC[next(it)] if L == 'o' else L for L in sk]; vs = abs(nS2(w)) * np.sqrt(2) / 3
    f = lambda k: float(dist_E2(w, np.asarray(k)[None], E)[0])
    ds = dist_E2(w, SPEC, E); d = dist_E2(w, GRID, E)
    nodes = [k for k, x in zip(SPEC, ds) if x < 1e-7]
    for i in np.argsort(d)[:40]:
        r_ = minimize(f, GRID[i], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 3000})
        if r_.fun < 1e-7: nodes.append(r_.x)
    uniq = []
    for k in nodes:
        k = wrap(k)
        if not any(np.linalg.norm(wrap(k - u)) < 1e-4 for u in uniq): uniq.append(k)
    res = [(np.round(k / np.pi, 4), kclass(k)) + tuple(classify2(w, k, E, vs)[:2]) for k in uniq if classify2(w, k, E, vs) is not None]
    bad = [r for r in res if r[3] != 'ok']; allbad &= len(bad) > 0
    print(f"  {sk} {nm} E={E:+.4f}: {len(res)} nodes, {len(bad)} defective; defect classes {collections.Counter((r[1], r[2], r[3]) for r in bad).most_common(6)}", flush=True)
check("each of the closest cases has defective nodes in a full census (none passes)", allbad)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
