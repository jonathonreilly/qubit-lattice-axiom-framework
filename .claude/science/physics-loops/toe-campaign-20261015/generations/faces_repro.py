import numpy as np, itertools
from scipy.optimize import least_squares
import coinfast as CF, coinrep as CR
rep = 'E12+H'
d, N, J, K, pairs, nz = CF.build(rep); fun, jac, unpack = CF.make(d, N, J, K, pairs, nz, 0.05)
S = [tuple(v) for v in CR.stencil('cube')]
x = np.random.default_rng(9).normal(size=2 * J)   # consume the gradient-check draw as coinfast does
rng = np.random.default_rng(0); best = (1e9, None, -1)
for t in range(20):
    r = least_squares(fun, rng.normal(size=2 * J) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
    res = np.linalg.norm(r.fun)
    if res < best[0]: best = (res, r.x, t)
print('best', best[0], 'trial', best[2], flush=True)
r = least_squares(fun, best[1], jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=50000)
A = unpack(r.x); res = np.linalg.norm(r.fun); mov = np.sum(np.abs(A[nz]) ** 2)
W = lambda k: sum(a * np.exp(1j * np.dot(k, n)) for a, n in zip(A, S))
tg = np.linspace(-np.pi, np.pi, 9)
spec = np.array([np.sort(np.angle(np.linalg.eigvals(W(np.array(k))))) for k in itertools.product(tg, tg, tg)])
print(f'polished residual {res:.2e} moving {mov:.4f} band spread {(spec.max(0) - spec.min(0)).max():.4f}')
np.save('faces_repro_A.npy', A)
