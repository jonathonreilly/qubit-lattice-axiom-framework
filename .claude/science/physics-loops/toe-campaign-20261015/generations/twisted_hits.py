import numpy as np, itertools
from scipy.optimize import least_squares
import coinfast as CF, coinrep as CR
d, N, J, K, pairs, nz = CF.build('E12+E52'); fun, jac, unpack = CF.make(d, N, J, K, pairs, nz, 0.05)
S = [tuple(v) for v in CR.stencil('cube')]
rng = np.random.default_rng(7); hits = []
for t in range(40):
    r = least_squares(fun, rng.normal(size=2 * J) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
    if np.linalg.norm(r.fun) < 1e-10:
        hits.append(unpack(r.x)); np.save('twisted_hits_A.npy', np.array(hits))
    if len(hits) >= 6: break
print('hits', len(hits))
gens = CR.rep('E12+E52')
for h, A in enumerate(hits):
    W = lambda k: sum(a * np.exp(1j * np.dot(k, n)) for a, n in zip(A, S))
    rs = np.random.default_rng(2)
    ec = max(np.abs(W(R @ k) - D @ W(k) @ D.conj().T).max() for R, D in gens for k in rs.uniform(-np.pi, np.pi, (20, 3)))
    tg = np.linspace(-np.pi, np.pi, 13)
    spec = np.array([np.sort(np.angle(np.linalg.eigvals(W(np.array(k))))) for k in itertools.product(tg, tg, tg)])
    spread = (spec.max(0) - spec.min(0)).max()
    # TRIM spectra
    trims = {nm: np.round(np.sort(np.angle(np.linalg.eigvals(W(np.array(k) * np.pi)))), 3) for nm, k in (('G', (0, 0, 0)), ('X', (1, 0, 0)), ('M', (1, 1, 0)), ('R', (1, 1, 1)))}
    # cone at Gamma relative to its eigenphase
    p0 = np.sort(np.angle(np.linalg.eigvals(W(np.zeros(3)))))
    slopes = [np.round(np.sort(np.abs(np.angle(np.linalg.eigvals(W(1e-3 * np.array(dd) / np.linalg.norm(dd))) * np.exp(-1j * p0.mean())) - 0)) , 4) for dd in ((1, 0, 0), (1, 1, 1))]
    print(f'hit {h}: covariance err {ec:.1e}, band spread over BZ {spread:.3f}, TRIM eigenphases {trims}')
