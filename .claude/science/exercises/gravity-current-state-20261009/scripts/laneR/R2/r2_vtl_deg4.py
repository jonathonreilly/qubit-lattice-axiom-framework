"""V-tl: the P-even weak-only degree-4 symbol (linearized-NMG-like): sign on the two
helicity-2 polarisations and resulting dispersion (with generic cubic K0)."""
import numpy as np
from r2_common import *
from r2_terms import weak_count
from r2_spectra import reyn, K0, DIRS, summarize, strong_Q
Vf = VERSIONS['V-tl']
w, N, basis, ms = weak_count(Vf, 4)
c = N[:, 0]
def Qw(k):
    mv = np.array([np.prod(k ** np.array(m)) for m in ms])
    return eval_Q(c, basis, mv)
Qw = reyn(Qw)
for dn, n in DIRS.items():
    P = phys_projector(Vf(n))
    ev = np.linalg.eigvalsh(np.real(P.T @ Qw(n) @ P))
    print(f'{dn}: eigenvalues of weak degree-4 symbol on the 2 TT polarisations: {np.round(ev, 4)}')
Kgen = K0(1.3, 0.8, 1.15)
for sgn in (+1, -1):
    summarize(f'V-tl, weak degree-4 term only, sign {sgn:+d} (strong k^6 term absent)', Kgen, lambda k, s=sgn: s * Qw(k), Vf, kaps=(1e-3, 2e-3))
Qs, _ = strong_Q(Vf, 3, seed=3)
summarize('V-tl, strong k^6 + 0.3*(sign chosen positive) weak degree-4', Kgen, lambda k: Qs(k) + 0.3 * np.sign(np.linalg.eigvalsh(np.real(phys_projector(Vf(np.array([0,0,1.]))).T @ Qw(np.array([0,0,1.])) @ phys_projector(Vf(np.array([0,0,1.]))))).sum()) * Qw(k), Vf, kaps=(1e-3, 2e-3))
