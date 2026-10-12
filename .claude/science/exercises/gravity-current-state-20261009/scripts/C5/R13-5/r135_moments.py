"""C5 R13-5 Lemma B2 check: the pair channel of the W1-complete stress drops out of the Poincare moments.
H = int T^00 and P = int T^0j need F^{0nu}_pair at q = 0; K = int x T^00 needs d/dq F^{00}_pair at q = 0.
Claim: F^{0j}_pair = O(|q|), F^{00}_pair = O(|q|^2) (two factors of D(q), D(0) = 0, omega_pair >= 2m), so K, P, H are
number-conserving and R8-2's Theorem E ([K_i, P_j] = i dGamma(eps (delta_ij + A_ij))) holds verbatim, whatever the pair kernel.
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r135_w1_pair import pair_kernel, wrap
rng = np.random.default_rng(7)
for name in ['G', 'L']:
    for member in ['U', 'M']:
        r0, rj = [], []
        for delta in [1e-2, 1e-3, 1e-4]:
            kk = rng.uniform(-np.pi, np.pi, (4000, 3)); qq = delta*rng.normal(size=(4000, 3))
            F, *_ = pair_kernel(member, name, 0.3, kk, wrap(-kk + qq))
            r0.append(np.max(np.abs(F[:, 0, 0])/np.sum(qq**2, -1))); rj.append(np.max(np.abs(F[:, 0, 1:]).max(-1)/np.sqrt(np.sum(qq**2, -1))))
        print('%s %s m=0.3: max |F^00_pair|/|q|^2 at |q|~1e-2,1e-3,1e-4: %.3f %.3f %.3f | max |F^0j_pair|/|q|: %.3f %.3f %.3f' % (name, member, *r0, *rj))
