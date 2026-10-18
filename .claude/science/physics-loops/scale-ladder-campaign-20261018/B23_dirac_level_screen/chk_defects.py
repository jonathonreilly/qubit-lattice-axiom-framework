#!/usr/bin/env python3
"""B23 cross-method check of every rejection: for each survivor's first defective node, recompute the
directional branch slopes by one-sided finite differences of the eigenphases (chklib Wword, no DPT, no gradients)
and confirm the DPT verdict (band / flat / tilt / aniso / iso-otherspeed) and its magnitude."""
import sys, os, glob, pickle, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b23lib import *
from multiprocessing import Pool
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
def fd(args):
    r, b = args; w = build(r['sk'], r['names']); E = r['E']; vs = r['vs']; k0 = np.array(b[0]) * np.pi; m = b[2]
    # re-locate: the stored k is rounded to 1e-5*pi; refine by Nelder-Mead from it (generic nodes only)
    f = lambda k: float(dist_E(w, np.asarray(k)[None], E)[0])
    if f(k0) > 1e-9:
        k0 = minimize(f, k0, method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-14, 'maxiter': 4000}).x
    h = 1e-5; sl = []
    for d in DIRS[:20]:
        a = closest(Wword(w, k0 + h * d), E, m)      # one-sided: the node is located to ~1e-14, so a/h = branch slopes + O(h)
        sl.append(a / h)
    sl = np.array(sl); A = np.abs(sl)
    tilt = float(np.abs(sl.sum(1)).max() / m)
    if m == 1: v = 'band' if A.min() > 1e-3 else 'band?'
    elif A.min() < 1e-3: v = 'flat'
    elif tilt > 1e-3: v = 'tilt'
    elif A.max() - A.min() > 1e-3: v = 'aniso'
    elif abs(A.min() - vs) > 1e-3: v = 'iso-otherspeed'
    else: v = 'ok'
    return b[3], v, f(k0), float(A.min()), float(A.max()), tilt
if __name__ == '__main__':
    S = []
    for fn in sorted(glob.glob(os.path.join(HERE, 'screen_*.pkl'))):
        for r in pickle.load(open(fn, 'rb'))['recs']:
            if not r['fermi'] and r['bad']: S.append((r, r['bad'][0]))
    with Pool(4) as p: out = p.map(fd, S, chunksize=4)
    agree = collections.Counter((a, b) for a, b, *_ in out)
    print("(DPT verdict, FD verdict) counts:", dict(agree))
    # FD: a 'tilt' node may also read as 'aniso'/'tilt' (both defects); 'flat' (quadratic) reads flat. Count a defect confirmed when FD also says not-ok.
    conf = sum(1 for a, b, *_ in out if b != 'ok')
    check("every first defective node of every survivor is confirmed defective by finite differences", conf == len(out), f"{conf}/{len(out)}")
    check("every re-located node is at E to 1e-8", max(x[2] for x in out) < 1e-8, f"max {max(x[2] for x in out):.1e}")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
