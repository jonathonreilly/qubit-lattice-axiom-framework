import numpy as np, scipy.optimize as so
from check_search import gen
from limits import span_sv, span_dim
rng = np.random.default_rng(2024)
CORN = [np.pi*np.array(v,float) for v in ((1,0,0),(1,1,0),(1,1,1))]
obj = lambda th: sum(span_sv(gen(th), K, eps=1e-3, rank_tol=1e-9)[4] for K in CORN)
samples = rng.uniform(-2, 2, size=(250, 9))
vals = np.array([obj(t) for t in samples]); order = np.argsort(vals)
best = None
for i in order[:3]:
    r = so.minimize(obj, samples[i], method='Nelder-Mead', options={'maxfev': 220})
    if best is None or r.fun < best.fun: best = r
th = best.x
print('theta', np.round(th, 4), 'diag const 1-a1-a2 =', round(1-th[0]-th[1], 5), ' offdiag const 1-b1-b2-b3-b4 =', round(1-sum(th[2:6]), 5), ' chiral l1,l2,l3 =', np.round(th[6:], 4))
D = gen(th)
for eps, tol in ((1e-2, 1e-7), (1e-3, 1e-9), (1e-4, 1e-11), (1e-5, 1e-12)):
    print(f'eps {eps:.0e}: dims', [span_dim(D, K, eps=eps, rank_tol=tol) for K in CORN], ' sv5', [round(span_sv(D, K, eps=eps, rank_tol=tol)[4], 3) for K in CORN])
for K in CORN:
    print('|D(K)| at corner', np.round(K/np.pi).astype(int), '=', np.abs(D(K)).max().round(4), ' |D(K+1e-3 q)| =', np.abs(D(K+1e-3*np.array([.3,.5,-.8]))).max())
