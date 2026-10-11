"""RL3 (D): sharp CHECK of Theorem 1 (exact eps-power series with eps-independent coefficients, interior/grouped
insertions included).  Observable: the realization kernel H_P(x, y0) between two added points, tau(y0,x) = T.
Theorem 1 => Var_eps[H_P(x,y0)] = eps a_1(T) + eps^2 a_2(T) + ...,  a_1(T) = int_{I(y0,x)} Gamma(z)^2 dz,
Gamma(z) = N + Id + IH + Gd + GH  (the one-insertion chaos kernel; the same vertex function as script B with
z_prev = x, z_next = y0).  (1) a_1(T) by MC quadrature (product of two independent inner estimates: unbiased).
(2) Monte Carlo of Var_eps[Hhat]/eps, Hhat = H_P/eps (E Hhat = H_k exactly; for the kernel the chaos kernels are
eps^(k+1) F_k, so Var Hhat = sum_k eps^k a_k): must tend to a_1(T) linearly in eps.  Also prints a_1^nn = int N^2.
"""
import numpy as np, sys, time
from scipy.special import gammaln
from scipy.linalg import solve_triangular
from rl2_core import OPS
op = 0; C = OPS[op]; L = len(C)
dC = np.array([C[j+1]-C[j] for j in range(L-1)] + [-C[L-1]])
def fpoly(c, m):
    m = np.asarray(m, float); return np.exp(-m)*sum(c[j]*m**j/np.exp(gammaln(j+1)) for j in range(len(c)))
mof = lambda t2: np.pi*np.maximum(t2, 0)**2/24
d = np.load("rl3_H_op0.npz"); TT, HH = d["taus"], d["H"]
Hf = lambda tau: np.interp(tau, TT, HH, right=0.0)
rng = np.random.default_rng(11)
mink2 = lambda a: a[..., 0]**2 - (a[..., 1:]**2).sum(-1)
def diamond_pts(bot, top, n):
    """uniform points in I(bot, top) (top - bot timelike), via rest-frame sampling + boost."""
    w = top - bot; tau = np.sqrt(mink2(w)); out = np.empty((0, 4))
    while len(out) < n:
        k = 3*n; t = rng.uniform(0, tau, k); x = rng.uniform(-tau/2, tau/2, (k, 3))
        ok = np.sqrt((x**2).sum(1)) < np.minimum(t, tau-t); out = np.vstack([out, np.column_stack([t[ok], x[ok]])])
    p = out[:n]
    # Lorentz boost taking (tau,0,0,0) to w
    u = w/tau; g = u[0]; vv = u[1:]; q = p.copy()
    if np.linalg.norm(vv) > 0:
        nhat = vv/np.linalg.norm(vv); par = p[:, 1:] @ nhat
        q[:, 0] = g*p[:, 0] + np.linalg.norm(vv)*par
        q[:, 1:] = p[:, 1:] + np.outer((g-1)*par + np.linalg.norm(vv)*p[:, 0], nhat)
    return bot + q, np.pi/24*tau**4
def Gamma(xp, z, yn, n):
    """one-insertion chaos kernel at z between fixed top xp and bottom yn (two independent estimates)."""
    t1 = np.sqrt(max(mink2(xp-z), 0)); t2 = np.sqrt(max(mink2(z-yn), 0))
    N = Hf(t1)*Hf(t2); ests = []
    for rep in range(2):
        u, V1 = diamond_pts(z, xp, n); v, V2 = diamond_pts(yn, z, n)
        hu = Hf(np.sqrt(np.maximum(mink2(xp-u), 0))); hv = Hf(np.sqrt(np.maximum(mink2(v-yn), 0)))
        Id = np.mean(fpoly(dC, mof(mink2(xp-v)))*hv)*V2
        IH = np.mean(hu*fpoly(dC, mof(mink2(u-v)))*hv)*V1*V2
        GH = np.mean(hu*fpoly(dC, mof(mink2(u-yn))))*V1
        Gd = float(fpoly(dC, mof(mink2(xp-yn))))
        ests.append(N + Id + IH + Gd + GH)
    return N, ests
def a1(T, nz=3000, n=4000):
    xp = np.array([T, 0, 0, 0.]); yn = np.zeros(4)
    zs, V = diamond_pts(yn, xp, nz)
    G2 = np.empty(nz); N2 = np.empty(nz)
    for i, z in enumerate(zs):
        N, e = Gamma(xp, z, yn, n); G2[i] = e[0]*e[1]; N2[i] = N*N
    return V*G2.mean(), V*G2.std()/np.sqrt(nz), V*N2.mean()
def gtable(eps, nmax):
    n = np.arange(nmax+1); g = np.zeros(nmax+1)
    for j in range(L):
        ok = n >= j
        lb = gammaln(n[ok]+1) - gammaln(j+1) - gammaln(n[ok]-j+1) + j*np.log(eps) + (n[ok]-j)*np.log1p(-eps)
        g[ok] += C[j]*np.exp(lb)
    return g
def mc(T, eps, R):
    rho = 1.0/eps; out = np.empty(R); G = gtable(eps, 400)
    for r in range(R):
        Np = rng.poisson(rho*np.pi/24*T**4)
        pts = np.empty((0, 4))
        while len(pts) < Np:
            k = 4*Np+20; t = rng.uniform(0, T, k); x = rng.uniform(-T/2, T/2, (k, 3))
            ok = np.sqrt((x**2).sum(1)) < np.minimum(t, T-t); pts = np.vstack([pts, np.column_stack([t[ok], x[ok]])])
        P = np.vstack([np.zeros((1, 4)), pts[:Np][np.argsort(pts[:Np, 0])], np.array([[T, 0, 0, 0.]])])
        n = len(P); dt = P[None, :, 0] - P[:, None, 0]; dx2 = ((P[None, :, 1:] - P[:, None, 1:])**2).sum(-1)
        Cm = (dt > 0) & (dt*dt > dx2); Cf = Cm.astype(float); cnt = np.rint(Cf @ Cf).astype(int)
        Nm = np.where(Cm, eps*G[cnt], 0.0)          # Nm[i,j]: hop i -> j (j later), weight eps g(n)
        A = np.eye(n) - Nm                           # chain sums: (I - Nm)^{-1}[0, n-1]
        e = np.zeros(n); e[-1] = 1.0
        col = solve_triangular(A, e, lower=False)    # upper triangular (time-sorted)
        out[r] = col[0]/eps                         # normalised kernel  Hhat = H_P/eps  (E Hhat = H_k, exact)
    return out
t0 = time.time()
for T in [1.0, 1.5]:
    A1, eA1, A1nn = a1(T)
    print("T=%.1f: a_1 (quadrature, node+interior+grouped) = %.5f +- %.5f ; node-only a_1^nn = %.5f ; Volterra mean H(T) = %.5f  (%.0fs)"
          % (T, A1, eA1, A1nn, Hf(T), time.time()-t0), flush=True)
    xs = []; ys = []; es = []
    for eps, R in [(0.5, 40000), (0.25, 40000), (0.125, 30000), (0.0625, 20000), (0.03125, 12000), (0.015625, 6000)]:
        h = mc(T, eps, R); v = h.var(ddof=1)
        # sd of the variance estimate via 4th moment
        m4 = np.mean((h-h.mean())**4); ev = np.sqrt(max(m4 - v*v, 0)/R)
        print("   eps=%-8g R=%6d mean Hhat = %+.5f +- %.5f   Var[Hhat]/eps = %.4f +- %.4f  (%.0fs)" % (eps, R, h.mean(), h.std()/np.sqrt(R), v/eps, ev/eps, time.time()-t0), flush=True)
        xs.append(eps); ys.append(v/eps); es.append(ev/eps)
    xs, ys, es = map(np.array, (xs, ys, es))
    for k0 in [3, 4]:
        sel = slice(len(xs)-k0, len(xs)); w = 1/es[sel]**2
        cf = np.polyfit(xs[sel], ys[sel], 1, w=np.sqrt(w)); cq = np.polyfit(xs[sel], ys[sel], 2, w=np.sqrt(w)) if k0 >= 4 else None
        print("   fit over the %d smallest eps: linear intercept %.4f%s   [compare a_1 = %.4f +- %.4f]" % (k0, cf[-1], ("" if cq is None else " ; quadratic intercept %.4f" % cq[-1]), A1, eA1))
