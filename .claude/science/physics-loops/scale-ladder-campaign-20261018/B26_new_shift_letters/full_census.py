#!/usr/bin/env python3
"""B26: full node census (no early reject) of named words at a level E: (pi/4)Z^3 points + 16^3 & 12^3 grids, 80 Nelder-Mead
starts; DPT classification; level structure at -k*.  Usage: full_census.py 'sk1|sk2..' 'n1,n2' E  (sk tokens; names = PHL)."""
import sys, os, collections, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b26lib import *
from scipy.optimize import minimize
PHL = dict(PC); PHL.update({f"{h}*{l}": PC[h] @ PC[l] for h in PC if h[0] == 'H' for l in PC if l[0] == 'L'})
g12 = np.linspace(-np.pi, np.pi, 12, endpoint=False) + 0.0417; G12 = np.array(list(itertools.product(g12, repeat=3)))
def census(sk, names, E, nstart=80):
    it = iter(names); w = [PHL[next(it)] if L == 'o' else L for L in sk]; vs = abs(nS(w)) * np.sqrt(2) / 3
    f = lambda k: float(dist_E(w, np.asarray(k)[None], E)[0])
    pts = np.vstack([GRID, G12]); d = dist_E(w, pts, E); ds = dist_E(w, SPEC, E)
    nodes = [k for k, x in zip(SPEC, ds) if x < 1e-7]
    for i in np.argsort(d)[:nstart]:
        r_ = minimize(f, pts[i], method='Nelder-Mead', options={'xatol': 1e-11, 'fatol': 1e-13, 'maxiter': 4000})
        if r_.fun < 1e-7: nodes.append(r_.x)
    uniq = []
    for k in nodes:
        k = wrap(k)
        if not any(np.linalg.norm(wrap(k - u)) < 1e-4 for u in uniq): uniq.append(k)
    res = collections.Counter(); ex = {}
    for k in uniq:
        c = classify(w, k, E, vs)
        if c is None: continue
        key = (kclass(k), c[0], c[1]); res[key] += 1; ex.setdefault(key, (np.round(k / np.pi, 4), {a: round(float(b), 4) for a, b in c[2].items() if a in ('smin', 'smax', 'tilt')}))
    lv = levels(Wb(w, (-kst)[None])[0])
    return w, vs, uniq, res, ex, lv, float(np.sort(d)[0])
if __name__ == '__main__':
    t0 = time.time()
    sk = tuple(sys.argv[1].split('|')); names = tuple(sys.argv[2].split(',')); E = float(sys.argv[3])
    w, vs, uniq, res, ex, lv, gmin = census(sk, names, E)
    print(f"{sk} {names} E={E:+.4f} n_S={nS(w)} v={vs:.6f}: nodes {len(uniq)}, defective {sum(n for k_, n in res.items() if k_[2] != 'ok')}")
    for k_, n in sorted(res.items(), key=lambda t: -t[1]): print(f"   {n:3d} x {k_}  e.g. k/pi={ex[k_][0]} {ex[k_][1]}")
    print("   levels at -k*:", [(round(a, 4), m) for a, m in lv])
    print(f"[{time.time() - t0:.0f}s]")
