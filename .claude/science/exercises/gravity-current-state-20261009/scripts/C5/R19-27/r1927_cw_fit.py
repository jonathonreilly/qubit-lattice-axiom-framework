"""R19-27 (a), check (3) refined: the per-site remainder R(mu) = e(mu) - e0 - eps1 mu - eps2 mu^2 - eps3 mu^3 on the D1 root edge,
fitted as R/mu^4 = A log mu + B + C mu (a mu^5 term allowed). Continuum CW comparator (RECALLED): A = -1/(8 pi^2) = -0.012665.
The mu^4 log mu term has n-scaling n^0 up to the log: W_4 = n d/dn[A m^4 log(m l)] = -(A/3) m^4 (EW-scale; zero under full LCP)."""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'recheck', 'arch', 'R18-5'))
from dirac import D1, kgrid
law = D1(0.915438682, 0.568280847); out = []
def bz(N, f):
    k = kgrid(N); s, w = law.S(k), law.W(k); tot = 0.0
    S23 = s[None, :, None]**2 + s[None, None, :]**2; W23 = w[None, :, None] + w[None, None, :]
    for i in range(N): tot += f(s[i]**2 + S23, w[i] + W23).sum()
    return tot/N**3
for N in (128, 192, 256):
    c = (bz(N, lambda X, W: -2*np.sqrt(X + W**2)), bz(N, lambda X, W: -2*W/np.sqrt(X + W**2)),
         bz(N, lambda X, W: -X/(X + W**2)**1.5), bz(N, lambda X, W: X*W/(X + W**2)**2.5))
    mus = np.array([0.12, 0.16, 0.2, 0.25, 0.3, 0.35, 0.4])
    R = np.array([bz(N, lambda X, W, mu=mu: -2*np.sqrt(X + (mu + W)**2)) - c[0] - c[1]*mu - c[2]*mu**2 - c[3]*mu**3 for mu in mus])
    M = np.vstack([np.log(mus), np.ones_like(mus), mus]).T
    A, B, C = np.linalg.lstsq(M, R/mus**4, rcond=None)[0]
    s = 'N=%3d: fit R/mu^4 = A log mu + B + C mu: A = %+.5f (CW -0.01267), B = %+.4f, C = %+.4f; eps2 = %+.6f' % (N, A, B, C, c[2])
    print(s, flush=True); out.append(s)
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
