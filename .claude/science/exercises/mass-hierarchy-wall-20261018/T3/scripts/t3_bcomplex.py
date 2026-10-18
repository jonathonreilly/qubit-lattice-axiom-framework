"""Channel B with COMPLEX couplings (post-hoc extension): M = m0 1 + mJ (J-1) + mu1 D(e) + mu2 Off(e), complex mJ, mu1, mu2.
Real case: spectrum depends on theta only through tr M^3 = A + k rho^3 cos3t (proved) -> V monotone in cos3t if M definite.
Complex case: |det M|^2 is QUADRATIC in cos3t, so an interior minimum is not excluded. Test."""
import numpy as np
from t3_landau import *
Ss, W = multiset_S(32)
rng = np.random.default_rng(11)
def VBc(pars, rho):
    m0, mJ, mu1, mu2 = pars
    e = ehat(TH) * rho
    J = np.ones((3, 3)); I = np.eye(3)
    off = np.zeros((TH.size, 3, 3), complex)
    off[:, 1, 2] = off[:, 2, 1] = e[:, 0]; off[:, 0, 2] = off[:, 2, 0] = e[:, 1]; off[:, 0, 1] = off[:, 1, 0] = e[:, 2]
    D = e[:, :, None] * I
    M = m0 * I + mJ * (J - I) + mu1 * D + mu2 * off
    s2 = np.linalg.svd(M, compute_uv=False) ** 2
    return -(np.sqrt(Ss[None, None, :] + s2[:, :, None]) * W).sum(-1).sum(-1), s2
# real-case check of the invariant claim
M0 = (0.2, 0.05, 0.7, -0.4)
_, s2 = VBc(M0, 0.5)
print('real check: tr M^2 spread over theta', np.ptp(s2.sum(1)))
n = 0; nd = 0; ex = []
for trial in range(120):
    ph = rng.uniform(0, 2*np.pi, 3); mag = rng.uniform(0, 1, 3)
    pars = (0.2, 0.2 * mag[0] * np.exp(1j*ph[0]), mag[1] * np.exp(1j*ph[1]), mag[2] * np.exp(1j*ph[2]))
    for rho in (0.1, 0.3, 0.6, 1.0):
        V, s2 = VBc(pars, rho); t = ang_min(V); n += 1
        if classify(t) == 'D2h' and np.ptp(V) > 1e-12:
            nd += 1
            if len(ex) < 8: ex.append((np.round(np.abs(pars[1:]), 2), np.round(np.degrees(np.angle(pars[1:]))), rho, round(np.degrees(t), 1), f'{np.ptp(V):.1e}'))
print(f'complex channel B: D2h angular minima {nd}/{n} (coupling, rho) samples')
for x in ex: print('   ', x)
