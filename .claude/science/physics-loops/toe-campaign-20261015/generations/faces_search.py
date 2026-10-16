import numpy as np, itertools, sys
from scipy.optimize import least_squares
import coinfast as CF, coinrep as CR
rep = 'E12+H'; delta = float(sys.argv[1]); ntrial = int(sys.argv[2])
d, N, J, K, pairs, nz = CF.build(rep); fun, jac, unpack = CF.make(d, N, J, K, pairs, nz, delta)
S = [tuple(v) for v in CR.stencil('cube')]
rng = np.random.default_rng(int(delta * 1000) + 3); out = []
for t in range(ntrial):
    r = least_squares(fun, rng.normal(size=2 * J) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=20000)
    res = np.linalg.norm(r.fun); A = unpack(r.x)
    W = lambda k: sum(a * np.exp(1j * np.dot(k, n)) for a, n in zip(A, S))
    tg = np.linspace(-np.pi, np.pi, 9)
    spec = np.array([np.sort(np.angle(np.linalg.eigvals(W(np.array(k))))) for k in itertools.product(tg, tg, tg)])
    spread = (spec.max(0) - spec.min(0)).max()
    mov = np.sum(np.abs(A[nz]) ** 2)
    print(f'trial {t}: residual {res:.2e} moving {mov:.3f} band spread {spread:.3f}', flush=True)
    out.append((res, A))
out.sort(key=lambda z: z[0]); np.save(f'faces_best_{delta}.npy', np.array([a for _, a in out[:5]]))
