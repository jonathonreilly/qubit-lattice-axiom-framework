"""Q1 (E): how strongly does a propagated field (a 'matter/light probe') record the sprinkling inside a small region R?
Same model and code path as probe Z2 (RL2_B smeared weights, exact binomial thinning; op0; carrier source with a past
edge at t = 0 centred at (d,0,0); observer worldline x = 0).  For each realization P we also build P' = P with the points
inside a 4D Euclidean ball R (centre c_R, radius r_R) deleted and freshly resampled at the same density, and compute
   s_R(t) = E|phi_P(t) - phi_P'(t)|^2 / (2 Var phi(t))
(= 1 if resampling R were as good as an independent sprinkling, = 0 if the field ignored R).
For a coherent probe with nbar photons in its mean mode, |<alpha_P|alpha_P'>| = exp(-nbar |phi_P - phi_P'|^2/(2|Psi|^2)),
so the which-region decoherence exponent is ~ nbar * (V/|Psi|^2) * s_R(t)  (V/|Psi|^2 grows like e^{gamma tau}).
Usage: python q1_E_region_sensitivity.py eps T npairs"""
import numpy as np, sys, time
from scipy.linalg import solve_triangular
from scipy.special import gammaln
from rl2_core import OPS
eps = float(sys.argv[1]); T = float(sys.argv[2]); NP = int(sys.argv[3])
op = 0; d = 2.0; dt = 0.25; ta = d + 0.5; w0 = 1.0
C = OPS[op]; rho = 1.0/eps; sig = 0.4; R0 = 1.2; xs = np.array([d, 0, 0.])
rng = np.random.default_rng(424242 + int(100*eps))
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
def in_omega(P):
    t = P[:, 0]; z = P[:, 1:]
    ok = (t >= 0) & (np.linalg.norm(z, axis=1) <= T - t) & (np.linalg.norm(z - xs, axis=1) <= R0 + t)
    return ok
def sprinkle():
    Ncand = rng.poisson(rho*np.pi*T**4/3)
    u = rng.uniform(size=Ncand); t = T*(1 - (1-u)**0.25)
    r = (T-t)*rng.uniform(size=Ncand)**(1/3); v = rng.normal(size=(Ncand, 3)); v /= np.linalg.norm(v, axis=1)[:, None]
    P = np.column_stack([t, v*r[:, None]]); return P[in_omega(P)]
def resample_ball(P, c, rr):
    inside = np.linalg.norm(P - c, axis=1) <= rr
    lo = c - rr; Nc = rng.poisson(rho*(2*rr)**4)
    Q = lo + 2*rr*rng.uniform(size=(Nc, 4)); Q = Q[(np.linalg.norm(Q - c, axis=1) <= rr)]; Q = Q[in_omega(Q)]
    return np.vstack([P[~inside], Q]), inside.sum(), len(Q)
def field(P):
    P = P[np.argsort(P[:, 0])]; n = P.shape[0]
    dtm = P[None, :, 0] - P[:, None, 0]; dx2 = ((P[None, :, 1:] - P[:, None, 1:])**2).sum(-1)
    Cm = (dtm > 0) & (dtm*dtm > dx2); Cf = Cm.astype(np.float32)
    cnt = np.rint(Cf @ Cf).astype(np.int64); Nm = np.where(Cm, eps*G[cnt], 0.0)
    dist = np.linalg.norm(P[:, 1:] - xs, axis=1); w = np.where(dist <= R0, np.exp(-dist**2/(2*sig**2)), 0.0)
    Jm = np.column_stack([w*np.cos(w0*P[:, 0]), w*np.sin(w0*P[:, 0])])
    U = solve_triangular(np.eye(n) - Nm.T, Jm, lower=True)
    rr = np.linalg.norm(P[:, 1:], axis=1); Cob = (tobs[None, :] - P[:, 0:1]) > rr[:, None]
    cob = np.rint(Cf @ Cob.astype(np.float32)).astype(np.int64); Nob = np.where(Cob, eps*G[cob], 0.0)
    PH = Nob.T @ U; return PH[:, 0] + 1j*PH[:, 1]
regions = [("mid, r=0.5", np.array([T/2, 1.0, 0, 0]), 0.5), ("mid, r=1.0", np.array([T/2, 1.0, 0, 0]), 1.0),
           ("near source, r=0.5", np.array([1.0, 1.8, 0, 0]), 0.5), ("off-axis, r=0.5", np.array([T/2, 0.0, 2.0, 0]), 0.5)]
t0 = time.time(); base = []; diffs = {lab: [] for lab, _, _ in regions}; moved = {lab: [] for lab, _, _ in regions}
for ip in range(NP):
    P = sprinkle(); ph = field(P); base.append(ph)
    for lab, c, rr in regions:
        P2, nin, nnew = resample_ball(P, c, rr); diffs[lab].append(ph - field(P2)); moved[lab].append((nin, nnew))
    if time.time() - t0 > 420: break
base = np.array(base); R = base.shape[0]; V = base.var(0); m = base.mean(0)
vol_diamond = np.pi*T**4/3
print("eps=%g T=%g op0 w0=1: %d realizations (%.0f s); <n> per sprinkling ~ %.0f" % (eps, T, R, time.time()-t0, rho*vol_diamond*0.45))
print(" t:          " + " ".join("%7.2f" % x for x in tobs[::2]))
print(" V/|mean|^2: " + " ".join("%7.3g" % x for x in (V/np.maximum(np.abs(m)**2, 1e-300))[::2]))
for lab, c, rr in regions:
    D = np.array(diffs[lab]); sR = (np.abs(D)**2).mean(0)/(2*V)
    mv = np.array(moved[lab]).mean(0)
    print(" %-20s (4-vol %.3g, pts removed/added %.1f/%.1f): s_R(t) = %s" %
          (lab, np.pi**2/2*rr**4, mv[0], mv[1], " ".join("%7.3f" % x for x in sR[::2])))
