"""R17-12 (b): C2 covariance of each placement. For a pair (k1, k2), k1 + k2 = q z^ (no wrap), compare
N(R k1, R k2) with s_e R N(k1, k2) R^T for the proper rotations C2x: (x,y,z)->(x,-y,-z), C2y: (x,y,z)->(-x,y,-z)
(s_e = -1 for T2g under both, +1 for Eg).  Also C4z (x->y, y->-x): T2g -> -T2g, Eg -> -Eg (q unchanged).
N is the pair matrix in A-polarization space (projectors applied), so the test is basis-independent."""
import numpy as np
from r1712_lib import *
from photon import crossmat
def Nmat(law, k1, k2, pol, var):
    s1, s2 = law.sig(k1), law.sig(k2); c1, c2 = law.c(k1), law.c(k2)
    ME, MB = vertex(var, pol, c1[None], c2[None], np.array([k1[2] + k2[2]]))
    ME, MB = ME[0], MB[0]
    w1, w2 = np.linalg.norm(s1), np.linalg.norm(s2); rw = np.sqrt(w1*w2)
    Nm = 0.5*(rw*ME + crossmat(s1).T @ MB @ crossmat(s2)/rw)
    P1 = np.eye(3) - np.outer(s1, s1)/w1**2; P2 = np.eye(3) - np.outer(s2, s2)/w2**2
    return P1 @ Nm @ P2
rng = np.random.default_rng(3)
R = {'C2x': np.diag([1., -1, -1]), 'C2y': np.diag([-1., 1, -1]), 'C4z': np.array([[0., -1, 0], [1, 0, 0], [0, 0, 1]])}
sgn = {('T2g', 'C2x'): -1, ('T2g', 'C2y'): -1, ('T2g', 'C4z'): -1, ('Eg', 'C2x'): 1, ('Eg', 'C2y'): 1, ('Eg', 'C4z'): -1}
for law in (photonNN(), photonG(1.4), photonGw(0.25133, 1.01946)):
    for q in (0.0, 0.3):
        for var in ('VU', 'VMone', 'VMsym', 'VW0'):
            out = []
            for pol in ('T2g', 'Eg'):
                for rn, Rm in R.items():
                    worst = 0.0; scale = 0.0
                    for _ in range(300):
                        k1 = rng.uniform(-2.5, 2.5, 3); k1[2] = rng.uniform(-1.2, 1.2)
                        k2 = np.array([-k1[0], -k1[1], q - k1[2]])
                        N0 = Nmat(law, k1, k2, pol, var); N1 = Nmat(law, Rm @ k1, Rm @ k2, pol, var)
                        worst = max(worst, np.abs(N1 - sgn[(pol, rn)]*Rm @ N0 @ Rm.T).max()); scale = max(scale, np.abs(N0).max())
                    out.append('%s/%s %.1e' % (pol, rn, worst/scale))
            print('%-24s q=%.1f %-6s rel. covariance defect: %s' % (law.name, q, var, '  '.join(out)))
