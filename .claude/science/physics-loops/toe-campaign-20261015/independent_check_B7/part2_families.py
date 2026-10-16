"""Part 2f: alpha,beta (h = alpha J + beta T at the k=0 G3/2 node) for simple two-layer families
qA = exp(a Qi), qB = exp(b Qj); isotropy check of loci beta=0 and beta/alpha in {10/3, -5/6}.
NUMERICAL."""
import numpy as np, sys
from part2_isotropy import alpha_beta, J, T
from part2_cone import Q, quat, eff_h, dirs
from scipy.optimize import brentq
def qexp(t, Qm): return np.cos(t)*np.eye(8) + np.sin(t)*Qm
for (i, j) in [(0, 1), (1, 0), (1, 2), (0, 0)]:
    for a, b in [(0.3, 0.5), (np.pi/4, np.pi/4), (0.7, 0.2)]:
        r = alpha_beta(qexp(a, Q[i]), qexp(b, Q[j]))
        print(f"qA=exp({a:.3f} Q{i+1}) qB=exp({b:.3f} Q{j+1}):", [(round(w,4), round(al,5), round(be,5)) for w, al, be, res in r])
def spec_spread(alpha, beta):
    sp = np.array([np.sort(np.linalg.eigvalsh(sum(n[k]*(alpha*J[k]+beta*T[k]) for k in range(3)))) for n in dirs(300)])
    return sp.max(0)-sp.min(0), sp[0]
for ratio in [0.0, 10/3, -5/6, 1.0]:
    s, e = spec_spread(1.0, ratio)
    print(f"beta/alpha={ratio:+.4f}: spread over 300 directions {np.round(s,12)}, eigenvalues {np.round(e,6)}")
