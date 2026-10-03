"""A25 check 4b: same 9-parameter generator family as check_search.py, smoother objective (sum over corner
classes of the normalized 5th singular value of the stacked limiting gauge directions), 400 random starts
screened, Nelder-Mead from the 3 best and from 3 seeds built on the double-smearing member.  Supplied toy."""
import time
import numpy as np
import scipy.optimize as so
import itertools
import check_search as cs
from check_search import gen, span_sv, CORN, cov_err
cs.DIRS = [d / np.linalg.norm(d) for d in list(np.random.default_rng(1).normal(size=(24, 3))) + [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=3) if any(v)]]

t0 = time.time()
rng = np.random.default_rng(99)
obj = lambda th: sum(span_sv(gen(th), K)[4] for K in CORN)
samples = rng.uniform(-2, 2, size=(400, 9))
vals = np.array([obj(t) for t in samples])
order = np.argsort(vals)
seeds = [samples[i] for i in order[:3]]
base = np.zeros(9); base[4] = 1.0                       # double smearing (b3=1)
for lam in (0.5,):
    for l3 in (0.0, -1.0, 1.0):
        s = base.copy(); s[6] = lam; s[8] = l3 * lam
        seeds.append(s)
res = []
for s in seeds:
    r = so.minimize(obj, s, method='Nelder-Mead', options={'maxfev': 260, 'xatol': 1e-5, 'fatol': 1e-7})
    pc = [round(span_sv(gen(r.x), K)[4], 3) for K in CORN]
    res.append((r.fun, pc, r.x))
res.sort(key=lambda t: t[0])
print(f'screen: best sum-objective {vals[order[0]]:.3f}; double-smearing member: {obj(base):.3f} '
      f'(per corner {[round(span_sv(gen(base), K)[4], 3) for K in CORN]})')
for f, pc, x in res[:6]:
    print(f'   NM optimum sum {f:.3f}: per-corner s5 (pi,0,0),(pi,pi,0),(pi,pi,pi) = {pc}')
print(f'   smallest max-over-corners reached: {min(max(pc) for f, pc, x in res):.3f}  (passing needs ~0 at all three)')
print(f'done in {time.time() - t0:.1f}s')
