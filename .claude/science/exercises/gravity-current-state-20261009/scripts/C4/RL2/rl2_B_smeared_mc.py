"""RL2 (B): realization-inverse Monte Carlo of the eps-SMEARED stable layer operator in flat 4D, FIXED source.
Units l_k = 1 (density rho = 1/eps).  N(x,y) = eps * g_eps(n(y,x)),  g_eps(n) = sum_j C_j binom(n,j) eps^j (1-eps)^(n-j)
(the expected value of C at the eps-thinned count; RL1/E1 smearing), so E N = eps f_C(eps rho V) = eps f_C(V): the MEAN operator,
and hence the mean inverse, is eps-independent in l_k units (exact, Poisson thinning).
Observables: H(x,y) tip-to-tip (tau = T) and phi(x) = sum_z H(x,z) J(z), J a FIXED Gaussian (width 0.4) centred at (0.8,0,0,0)
near the bottom tip -- source size and position do not scale with T.  sd over realizations vs T -> growth rate per unit proper time.
Usage: python rl2_B_smeared_mc.py op eps T1,T2,.. R1,R2,..
"""
import numpy as np, sys, time
from scipy.linalg import solve_triangular
from scipy.special import gammaln
from rl2_core import OPS
op = int(sys.argv[1]); eps = float(sys.argv[2])
Ts = [float(a) for a in sys.argv[3].split(",")]; Rs = [int(a) for a in sys.argv[4].split(",")]
C = OPS[op]; rho = 1.0/eps
rng = np.random.default_rng(int(1e6*eps) + 17*op + 20261011)
def gtable(nmax):
    n = np.arange(nmax+1); g = np.zeros(nmax+1)
    if eps == 1.0:
        g[:len(C)] = C; return g
    for j in range(len(C)):
        ok = n >= j
        lb = gammaln(n[ok]+1) - gammaln(j+1) - gammaln(n[ok]-j+1) + j*np.log(eps) + (n[ok]-j)*np.log1p(-eps)
        g[ok] += C[j]*np.exp(lb)
    return g
def sprinkle(T):
    vol = rho*np.pi/24*T**4; N = rng.poisson(vol); out = []; got = 0
    while got < N:
        m = int((N-got)*1.7)+100
        t = rng.uniform(0, T, m); xyz = rng.uniform(-T/2, T/2, (m, 3))
        ok = np.sqrt((xyz**2).sum(1)) < np.minimum(t, T-t)
        out.append(np.column_stack([t[ok], xyz[ok]])); got += ok.sum()
    P = np.vstack(out)[:N] if N > 0 else np.empty((0, 4))
    P = P[np.argsort(P[:, 0])]
    return np.vstack([np.zeros((1, 4)), P, np.array([[T, 0, 0, 0.]])])
def run(T, R):
    Hs = []; phis = []; Ns = []
    for r in range(R):
        P = sprinkle(T); n = P.shape[0]; Ns.append(n-2)
        dt = P[None, :, 0] - P[:, None, 0]; dx2 = ((P[None, :, 1:] - P[:, None, 1:])**2).sum(-1)
        Cm = (dt > 0) & (dt*dt > dx2); Cf = Cm.astype(np.float32)
        cnt = np.rint(Cf @ Cf).astype(np.int64)
        g = gtable(int(cnt.max())+1)
        Nm = np.where(Cm, eps*g[cnt], 0.0)
        M = np.eye(n) - Nm.T
        ex = np.zeros(n); ex[-1] = 1.0
        z = solve_triangular(M.T, ex, lower=False); hrow = z.copy(); hrow[-1] -= 1.0
        J = np.exp(-((P - np.array([0.8, 0, 0, 0]))**2).sum(1)/(2*0.4**2)); J[0] = 0; J[-1] = 0
        Hs.append(hrow[0]); phis.append(hrow @ J)
    return np.array(Hs), np.array(phis), np.mean(Ns)
t0 = time.time()
print("op%d eps=%g (rho=%g per l_k^4)" % (op, eps, rho))
for T, R in zip(Ts, Rs):
    H, phi, Nm = run(T, R)
    print("  T=%4.1f <N>=%7.1f R=%3d  H: mean=%+.3e sd=%.4e | phi: mean=%+.4e +- %.1e sd=%.4e  (%.0fs)" %
          (T, Nm, R, H.mean(), H.std(ddof=1), phi.mean(), phi.std(ddof=1)/np.sqrt(R), phi.std(ddof=1), time.time()-t0), flush=True)
