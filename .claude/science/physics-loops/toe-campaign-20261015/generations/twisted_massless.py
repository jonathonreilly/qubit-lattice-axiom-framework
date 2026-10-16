import numpy as np, itertools, sys
from scipy.optimize import least_squares
import coinfast as CF, coinrep as CR
rep = sys.argv[1] if len(sys.argv) > 1 else 'E12+E52'
d, N, J, K, pairs, nz = CF.build(rep); fun0, jac0, unpack = CF.make(d, N, J, K, pairs, nz, 0.05)
S = [tuple(v) for v in CR.stencil('cube')]; gens = CR.rep(rep)
Ks = K.sum(0)   # U(0) = sum_n A_n
def fun(x):
    p = x[:J] + 1j * x[J:]; U0 = np.einsum('abj,j->ab', Ks, p) - np.eye(d)
    return np.concatenate([fun0(x), 3 * U0.real.ravel(), 3 * U0.imag.ravel()])
def jac(x):
    Jt = np.hstack([Ks.reshape(d * d, J).real, -Ks.reshape(d * d, J).imag]); Ji = np.hstack([Ks.reshape(d * d, J).imag, Ks.reshape(d * d, J).real])
    return np.vstack([jac0(x), 3 * Jt, 3 * Ji])
rng = np.random.default_rng(11); hits = []
for t in range(int(sys.argv[2]) if len(sys.argv) > 2 else 30):
    r = least_squares(fun, rng.normal(size=2 * J) * rng.choice([0.3, 1.0]), jac=jac, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=5000)
    res = np.linalg.norm(r.fun); print(f'trial {t}: residual {res:.2e}', flush=True)
    if res < 1e-10:
        A = unpack(r.x); hits.append(A); np.save(f'massless_{rep}_A.npy', np.array(hits))
        W = lambda k: sum(a * np.exp(1j * np.dot(k, n)) for a, n in zip(A, S))
        trims = {nm: np.round(np.sort(np.angle(np.linalg.eigvals(W(np.array(k) * np.pi)))), 3) for nm, k in (('X', (1, 0, 0)), ('M', (1, 1, 0)), ('R', (1, 1, 1)))}
        cone = [np.round(np.sort(np.abs(np.angle(np.linalg.eigvals(W(1e-3 * np.array(dd) / np.linalg.norm(dd)))))) / 1e-3, 4) for dd in ((1, 0, 0), (1, 1, 0), (1, 1, 1))]
        tg = np.linspace(-np.pi, np.pi, 15)
        zeros = sorted([(np.abs(np.angle(np.linalg.eigvals(W(np.array(k))))).min(), k) for k in itertools.product(tg, tg, tg) if np.linalg.norm(k) > 0.4], key=lambda z: z[0])[:3]
        print(f'   HIT: cone slopes {cone}\n   TRIM phases {trims}\n   smallest |omega| away from 0: {[(round(z[0], 3), np.round(z[1], 2).tolist()) for z in zeros]}', flush=True)
        if len(hits) >= 4: break
