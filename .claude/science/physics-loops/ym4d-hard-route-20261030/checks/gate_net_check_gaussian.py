#!/usr/bin/env python3
"""Sampling check of the Gaussian algebra in Theorem 10.7, plus the T_1 sign control."""
import numpy as np
from net_check_lemma101 import build, slab_op
rng = np.random.default_rng(11)
n = 4_000_000
for P, Q in [(0.5, 0.3), (0.5, -0.2), (0.5, 0.05)]:
    C = 4 * np.array([[P, Q], [Q, P]])
    A = np.linalg.cholesky(C)
    z = rng.standard_normal((n, 2, 3))
    b = np.einsum('ij,njc->nic', A, z)
    X1 = (b[:, 0]**2).sum(1) / 8
    X2 = (b[:, 1]**2).sum(1) / 8
    cross = np.cross(b[:, 0], b[:, 1])
    print("P=%.2f Q=%+.2f  <X>=%.4f (3/2 P=%.4f)  Cov=%.5f ((3/2)Q^2=%.5f)  (1/8)E|b1xb2|^2=%.4f (12(P^2-Q^2)=%.4f)"
          % (P, Q, X1.mean(), 1.5*P, np.cov(X1, X2)[0, 1], 1.5*Q*Q, (cross**2).sum(1).mean()/8, 12*(P*P-Q*Q)))
# three-term split with an independent lift: total P^inf = P^fib + delta
Pf, df, Pd, dd = 0.5, 0.1, 0.03, 0.01  # P^fib_pp, delta_pp, P^fib_pq, delta_pq
Cb = 4*np.array([[Pf, Pd], [Pd, Pf]])
Cp = 4*np.array([[df, dd], [dd, df]])
bb = np.einsum('ij,njc->nic', np.linalg.cholesky(Cb), rng.standard_normal((n, 2, 3)))
pp = np.einsum('ij,njc->nic', np.linalg.cholesky(Cp), rng.standard_normal((n, 2, 3)))
tot = bb + pp
X1 = (tot[:, 0]**2).sum(1)/8
X2 = (tot[:, 1]**2).sum(1)/8
print("split: Cov=%.6f, (3/2)(Pfib+delta)^2=%.6f, terms %.6f %.6f %.6f" %
      (np.cov(X1, X2)[0, 1], 1.5*(Pd+dd)**2, 1.5*Pd**2, 3*Pd*dd, 1.5*dd**2))
for beta in [-0.5, -0.1, 0.1, 0.5]:
    h, B = build(beta)
    T1 = slab_op(h, B)
    ev = np.linalg.eigvalsh(0.5*(T1+T1.T))
    print("T_1 control beta=%+.1f: min eig / max eig = %.3e" % (beta, ev.min()/np.abs(ev).max()))
