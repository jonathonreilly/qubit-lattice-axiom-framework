"""Dense-grid re-check of the C20 claim-C/D numbers on the supplied optimisation point (vectorized, own search):
band-0 max / band-1 min relative to E_N without mass; folded global gap with the staggered mass."""
import itertools
import numpy as np
from scipy.optimize import minimize
from chk_common import load, bloch_fn, R
Mdl, X, Mm, seeds = load()
shifts, orbit_sum = R.orbit_basis(Mdl)
blo = {}
for (sh, c1, c2, part), cval in R.OPT_POINT.items():
    for s_, Mb in orbit_sum(sh, c1, c2, part).items(): blo[s_] = blo.get(s_, 0) + cval * Mb
H = bloch_fn(blo); HM = bloch_fn(Mdl['blocks_from'](Mm)); kst = Mdl['kst']; Q = Mdl['Q']
EN = np.linalg.eigvalsh(H(kst[None]))[0, 0]
N = 40; g = np.arange(N) * 2 * np.pi / N - np.pi + 0.0071
K = np.array(list(itertools.product(g, g, g)))
E = np.concatenate([np.linalg.eigvalsh(H(K[i:i + 8000]))[:, :2] for i in range(0, len(K), 8000)])
print(f'no mass, {N}^3 grid: max band0 - E_N = {E[:,0].max()-EN:+.4e} at k/pi={np.round(K[E[:,0].argmax()]/np.pi,3)}; '
      f'min band1 - E_N = {E[:,1].min()-EN:+.4e}')
six = [np.array(s) * np.pi / 2 for s in itertools.product((1, -1), repeat=3)]
print('band0 at the eight points - E_N:', np.round([np.linalg.eigvalsh(H(k[None]))[0, 0] - EN for k in six], 6))
for m in (0.02, 0.05):
    def F(Kc):
        A = H(Kc); B = H(Kc + Q); C = m * HM(Kc)
        return np.linalg.eigvalsh(np.block([[A, np.conj(np.transpose(C, (0, 2, 1)))], [C, B]]))
    Ef = np.concatenate([F(K[i:i + 4000])[:, 1:3] for i in range(0, len(K), 4000)])
    i1 = np.argsort(-Ef[:, 0])[:10]; i2 = np.argsort(Ef[:, 1])[:10]
    top = max(-minimize(lambda k: -F(k[None])[0, 1], K[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=4000)).fun for i in i1)
    bot = min(minimize(lambda k: F(k[None])[0, 2], K[i], method='Nelder-Mead', options=dict(xatol=1e-10, fatol=1e-14, maxiter=4000)).fun for i in i2)
    e0 = F(kst[None])[0]
    print(f'm = {m}: direct gap at k* = {e0[2]-e0[1]:.5f}; grid gap {Ef[:,1].min()-Ef[:,0].max():+.5f}; refined global gap {bot-top:+.5f}')
