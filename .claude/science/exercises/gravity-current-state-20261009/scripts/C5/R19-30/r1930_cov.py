"""R19-30: cubic covariance of the parity-resolved re-placement (scalar E1 kernel, pair channel), whole torus incl. the cut.
For a signed permutation (R k)_a = s_a k_{pi(a)}: f_i(R k) = s_i f_{pi(i)}(k), eps(R k) = eps(k), so a covariant kernel obeys
   T^{ij}(R k1, R k2) = s_i s_j T^{pi(i) pi(j)}(k1, k2)   (tilde kernels; the site-label phase e^{-i q.p} is the same rule
   up to the integer translations that relabel p under R, which do not change |amplitudes| and are tested via |G|).
Checked for 'raw' (control) and 'PR', for C4z, a mirror x -> -x, C3(111) and C2(110)."""
import numpy as np
import lib1930 as L
SC = L.Scalar(m=0.01)
rng = np.random.default_rng(193009)
n = 3000
k1 = rng.uniform(-np.pi, np.pi, (n, 3)); k2 = rng.uniform(-np.pi, np.pi, (n, 3))
qv = rng.uniform(-np.pi, np.pi, (1000, 3)); qv[:, 0] = np.pi - 1e-7*rng.uniform(0.5, 1, 1000); k2[:1000] = qv - k1[:1000]   # q_x near the cut
def tilde(k1, k2, i, j, mode):
    q = L.wrap(k1 + k2); K = k1 - q/2
    fun = lambda kb: (SC.f(kb[..., i])*SC.f(kb[..., j]))[..., None]
    return L.tilde_component(fun, K, q, i, j, mode)[..., 0]/np.sqrt(SC.eps(k1)*SC.eps(k2))
OPS = {'C4z': ((1, 0, 2), (-1, 1, 1)), 'mirror x': ((0, 1, 2), (-1, 1, 1)), 'C3(111)': ((1, 2, 0), (1, 1, 1)), 'C2(110)': ((1, 0, 2), (1, 1, -1))}
for mode in ('raw', 'PR'):
    out = []
    for name, (perm, s) in OPS.items():
        perm = np.array(perm); s = np.array(s, float)
        R = lambda k: s*k[..., perm]
        worst = 0.0
        for i in range(3):
            for j in range(i, 3):
                lhs = tilde(R(k1), R(k2), i, j, mode); rhs = s[i]*s[j]*tilde(k1, k2, perm[i], perm[j], mode)
                worst = max(worst, np.abs(lhs - rhs).max())
        out.append('%s %.1e' % (name, worst))
    print('scalar E1 tilde kernel, mode %-3s: max |T(Rk) - s_i s_j T^{pi(i)pi(j)}(k)| over 3000 pairs (1000 at the q_x cut): ' % mode + ', '.join(out))
