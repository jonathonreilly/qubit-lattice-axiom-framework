"""Z2 (A): fixed-source smeared Monte Carlo (RL2_B, exact binomial thinning) with a CARRIER source switched on with a past edge,
and the field recorded as a TIME SERIES at an observer worldline.

Units l_k = 1, density rho = 1/eps, weights N(x,y) = eps g_eps(n(y,x)) (RL2_B; E N = eps f_C(V), mean operator eps-independent).
Source: J(y) = w(y_vec) * exp(i w0 t_y) * Theta(t_y), w = Gaussian (sigma 0.4) centred at x_s = (d,0,0), truncated at |y-x_s| <= R0 = 1.2.
  (past edge = the spacelike plane t = 0; regular nonzero turn-on patch: |J| = w is continuous and nonzero at the edge -> RL4 T' class.)
  cos and sin columns are solved separately, phi = phi_c + i phi_s  (complex carrier e^{i w0 t}).
Sprinkling region Omega = J+(supp J) cap J-(x_T): exact for this observable (every interval between points of Omega lies in Omega).
Observer: x_k = (t_k, 0,0,0), t_k on a grid in [t_a, T]; each observer is its own Palm point (not added to the sprinkling):
  phi(x_k) = sum_z N(x_k, z) u(z),  u = (I - N)^{-1} J on the sprinkled points.
Output: npz with the complex time series for every realization and every w0.
Usage: python z2_A_carrier_mc.py op eps T ta dt d Rmax tmax_seconds tag
"""
import numpy as np, sys, time
from scipy.linalg import solve_triangular
from scipy.special import gammaln
from rl2_core import OPS
op = int(sys.argv[1]); eps = float(sys.argv[2]); T = float(sys.argv[3]); ta = float(sys.argv[4]); dt = float(sys.argv[5])
d = float(sys.argv[6]); Rmax = int(sys.argv[7]); tmax = float(sys.argv[8]); tag = sys.argv[9]
W0 = np.array([0.0, 0.1, 0.3, 1.0, 2.0, 4.0])
C = OPS[op]; rho = 1.0/eps; sig = 0.4; R0 = 1.2; xs = np.array([d, 0, 0.])
rng = np.random.default_rng(int(1e6*eps) + 17*op + 7919*int(10*T) + 20261011)
tobs = np.arange(ta, T + 1e-9, dt); K = len(tobs)
def gtable(nmax):
    n = np.arange(nmax+1); g = np.zeros(nmax+1)
    if eps == 1.0:
        g[:len(C)] = C; return g
    for j in range(len(C)):
        ok = n >= j
        lb = gammaln(n[ok]+1) - gammaln(j+1) - gammaln(n[ok]-j+1) + j*np.log(eps) + (n[ok]-j)*np.log1p(-eps)
        g[ok] += C[j]*np.exp(lb)
    return g
G = gtable(200000)
def sprinkle():
    Ncand = rng.poisson(rho*np.pi*T**4/3)          # uniform in the 4D cone J-(x_T) cap {t>=0}
    u = rng.uniform(size=Ncand); t = T*(1 - (1-u)**0.25)
    r = (T-t)*rng.uniform(size=Ncand)**(1/3); v = rng.normal(size=(Ncand, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    z = v*r[:, None]
    ok = np.linalg.norm(z - xs, axis=1) <= R0 + t   # in J+(supp J) (thinning keeps it Poisson on Omega)
    P = np.column_stack([t[ok], z[ok]]); P = P[np.argsort(P[:, 0])]
    return P
def one():
    P = sprinkle(); n = P.shape[0]
    dtm = P[None, :, 0] - P[:, None, 0]; dx2 = ((P[None, :, 1:] - P[:, None, 1:])**2).sum(-1)
    Cm = (dtm > 0) & (dtm*dtm > dx2); Cf = Cm.astype(np.float32)
    cnt = np.rint(Cf @ Cf).astype(np.int64)
    Nm = np.where(Cm, eps*G[cnt], 0.0)                 # Nm[i,j] = N(x_j, x_i) for i < j (i earlier)
    dist = np.linalg.norm(P[:, 1:] - xs, axis=1)
    w = np.where(dist <= R0, np.exp(-dist**2/(2*sig**2)), 0.0)
    cols = [w*np.cos(w0*P[:, 0]) for w0 in W0] + [w*np.sin(w0*P[:, 0]) for w0 in W0]
    Jm = np.column_stack(cols)
    U = solve_triangular(np.eye(n) - Nm.T, Jm, lower=True)   # u = J + N u
    # observers
    rr = np.linalg.norm(P[:, 1:], axis=1)
    Cob = (tobs[None, :] - P[:, 0:1]) > rr[:, None]            # z < x_k (strictly timelike)
    cob = np.rint(Cf @ Cob.astype(np.float32)).astype(np.int64)  # count in open interval (z, x_k)
    Nob = np.where(Cob, eps*G[cob], 0.0)                       # n x K
    PH = Nob.T @ U                                             # K x (2*len(W0))
    nw = len(W0)
    return PH[:, :nw] + 1j*PH[:, nw:], n
t0 = time.time(); out = []; ns = []
for r in range(Rmax):
    ph, n = one(); out.append(ph); ns.append(n)
    if time.time() - t0 > tmax: break
out = np.array(out)   # R x K x nw
np.savez("z2_A_%s.npz" % tag, phi=out, tobs=tobs, W0=W0, eps=eps, op=op, T=T, d=d, ns=np.array(ns))
R = out.shape[0]
print("op%d eps=%g T=%g d=%g dt=%g: R=%d realizations, <n>=%.0f, %.0fs" % (op, eps, T, d, dt, R, np.mean(ns), time.time()-t0))
m = out.mean(0); v = out.var(0)
for j, w0 in enumerate(W0):
    print("  w0=%.1f: t, |mean|, sd:" % w0, " ".join("%.2f:%.3g/%.3g" % (tobs[k], abs(m[k, j]), np.sqrt(v[k, j]))
          for k in range(0, len(tobs), max(1, len(tobs)//8))))
