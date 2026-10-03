"""A25 check 4c: limiting gauge spans S_K at the zone corners with an absolute-threshold union count
(limits.py), for named covariant collocated generators and a re-run of the 9-parameter family search.
Supplied toy; finite family."""
import time
import numpy as np
import scipy.optimize as so
from check_search import gen, cov_err, O
from limits import span_sv, span_dim
from stag2 import signed_perms

t0 = time.time()
CORN = {'(pi,0,0)': np.pi * np.array([1., 0, 0]), '(pi,pi,0)': np.pi * np.array([1., 1, 0]), '(pi,pi,pi)': np.pi * np.ones(3)}
named = {'central': np.zeros(9)}
th = np.zeros(9); th[2] = 1; named['smear1 (c2_j)'] = th
th = np.zeros(9); th[4] = 1; named['smear2 (c2_j c2_m)'] = th
th = np.zeros(9); th[6] = 0.5; named['chiral l1=0.5'] = th
th = np.zeros(9); th[2] = 1; th[6] = 0.5; named['smear1 + chiral'] = th
th = np.zeros(9); th[4] = 1; th[7] = 0.5; named['smear2 + chiral*c2_m'] = th
th = np.zeros(9); th[4] = 1; th[0] = 1; named['smear2 + diag c2c2'] = th
Oh = signed_perms()
for nm, th in named.items():
    D = gen(th)
    dims = {k: span_dim(D, K) for k, K in CORN.items()}
    dims3 = {k: span_dim(D, K, eps=1e-3, rank_tol=1e-9) for k, K in CORN.items()}
    gaps = {k: np.round(span_sv(D, K)[3:6], 3).tolist() for k, K in CORN.items()}
    print(f'{nm:22s} O-cov {cov_err(D):.0e}: dim S_K (eps 1e-4) {list(dims.values())}, (eps 1e-3) {list(dims3.values())}; '
          f'sv 4-6 per corner {list(gaps.values())}')
# search (absolute 5th singular value, summed over corner classes)
rng = np.random.default_rng(2024)
obj = lambda th: sum(span_sv(gen(th), K, eps=1e-3, rank_tol=1e-9)[4] for K in CORN.values())
samples = rng.uniform(-2, 2, size=(250, 9))
vals = np.array([obj(t) for t in samples])
order = np.argsort(vals)
seeds = [samples[i] for i in order[:3]] + [named['smear2 (c2_j c2_m)'], named['smear2 + chiral*c2_m'], named['smear2 + diag c2c2']]
res = []
for s in seeds:
    r = so.minimize(obj, s, method='Nelder-Mead', options={'maxfev': 220})
    res.append((r.fun, [round(span_sv(gen(r.x), K, eps=1e-3, rank_tol=1e-9)[4], 3) for K in CORN.values()],
                [span_dim(gen(r.x), K) for K in CORN.values()]))
res.sort(key=lambda t: t[0])
print(f'search: 250 random members, best sum of 5th singular values {vals[order[0]]:.3f}; Nelder-Mead from 3 best + 3 seeds:')
for f, pc, dm in res:
    print(f'   optimum {f:.3f}: per-corner sv5 {pc}; dim S_K {dm}')
print(f'done in {time.time() - t0:.1f}s')
