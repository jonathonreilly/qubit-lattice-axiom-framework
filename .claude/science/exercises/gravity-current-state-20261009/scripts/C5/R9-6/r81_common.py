"""R8-1 common pieces: smooth steps, the lattice one-body box law (R7-1), and the exact
smooth Bakamjian-Thomas (BT) difference kernel w(P; q', q) of sqrt(M^2+P^2) - sqrt(M0^2+P^2)
for M = M0 + V, V = lam * sum_a |g_a><g_a| (d = 1: one odd g; d = 2: the p-wave doublet
g_a(q) = q_a b(|q|^2), a rotational scalar channel).

Kernel formula (Woodbury, exact):  A = M^2 + P^2 = A0 + U C U^T, A0 = M0^2 + P^2,
  U = [g, M0 g] (per channel), C = [[lam^2 n, lam], [lam, 0]], n = <g_a|g_a>,
  sqrt(A) - sqrt(A0) = (1/pi) int_0^inf t^{1/2} (A+t)^{-1} (A-A0) (A0+t)^{-1} dt
                     = (1/pi) int_0^inf t^{1/2} R_t U (C^{-1} + U^T R_t U)^{-1} U^T R_t dt,  R_t = (A0+t)^{-1}.
So w(P; q', q) = G1(q') G1(q) * Omega(P; |q'|, |q|), with G1 = g (d=1) or the pair factor
(q'.q) b' b (d=2), and Omega = (1/pi) int t^{1/2} R_t(q') R_t(q) [Gam11 + Gam12 (M0'+M0) + Gam22 M0' M0] dt.
"""
import numpy as np

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

class BoxLaw:
    """one-body lattice symbols: s(k) = k on |k| <= B (C^inf, periodic), eps = sqrt(m^2 + sum s^2)."""
    def __init__(self, m, B=2.6, B2=3.0):
        self.m, self.B, self.B2 = m, B, B2
    def s(self, k):
        k = wrap(k); r = sstep((self.B2 - np.abs(k))/(self.B2 - self.B))
        return r*k + (1-r)*np.sin(k)
    def eps(self, *ks):
        return np.sqrt(self.m**2 + sum(self.s(k)**2 for k in ks))

class BTKernel:
    """exact smooth BT difference kernel for the rank-one (d=1) or p-wave doublet (d=2) channel."""
    def __init__(self, m, kappa, lam, d, ns=(-36.0, 56.0, 0.12), nq=6001):
        self.m, self.kappa, self.lam, self.d = m, kappa, lam, d
        s0, s1, ds = ns
        self.svals = np.arange(s0, s1 + ds/2, ds)
        self.tvals = np.exp(self.svals)
        # trapezoid weights in s, with dt = t ds and the t^{1/2}/pi prefactor
        self.cw = ds*self.tvals*np.sqrt(self.tvals)/np.pi
        # quadrature grid for G (radial in d = 2)
        if d == 1:
            self.qg = np.linspace(-kappa, kappa, nq); self.wq = np.full(nq, self.qg[1]-self.qg[0])
            self.gg2 = self.g1(self.qg)**2                     # g^2
        else:
            r = np.linspace(0.0, kappa, nq); w = np.full(nq, r[1]-r[0]); w[0] = w[-1] = 0.5*w[0]
            self.qg = r; self.wq = w
            # <g_x|f|g_x> = int q_x^2 b^2 f d^2q = pi int r^3 b(r^2)^2 f(r) dr
            self.gg2 = np.pi*r**3*self.b(r**2)**2
        self.ng = np.sum(self.gg2*self.wq)                     # n = <g|g> (per channel)
        self.M0g = self.M0(self.qg)

    def b(self, r2):
        return sstep(1.0 - r2/self.kappa**2)/self.kappa
    def g1(self, q):                                           # d = 1 odd form factor
        return (q/self.kappa)*sstep(1.0 - (q/self.kappa)**2)
    def M0(self, q):                                           # q: |q| or q (d=1); M0 depends on q^2
        return 2*np.sqrt(self.m**2 + q**2)

    def Gamma(self, P2):
        """Gam_s = (C^{-1} + G(t_s))^{-1} for all s, as arrays (a11, a12, a22)."""
        lam, n = self.lam, self.ng
        A0 = self.M0g**2 + P2
        R = 1.0/(A0[None, :] + self.tvals[:, None])           # (ns, nq)
        G11 = (R*self.gg2*self.wq).sum(1)
        G12 = (R*self.gg2*self.M0g*self.wq).sum(1)
        G22 = (R*self.gg2*self.M0g**2*self.wq).sum(1)
        # C^{-1} for C = [[lam^2 n, lam],[lam, 0]]: det = -lam^2 ; C^{-1} = [[0, 1/lam],[1/lam, -n]]
        a, bb, c = G11 + 0.0, G12 + 1.0/lam, G22 - n
        det = a*c - bb*bb
        return c/det, -bb/det, a/det

    def Omega(self, P2, qa, qb):
        """Omega(P; q', q) on all pairs (qa[i], qb[j]); qa, qb are |q| (d=2) or q (d=1)."""
        g11, g12, g22 = self.Gamma(P2)
        Ma, Mb = self.M0(qa), self.M0(qb)
        Ra = 1.0/((Ma**2 + P2)[None, :] + self.tvals[:, None])    # (ns, na)
        Rb = 1.0/((Mb**2 + P2)[None, :] + self.tvals[:, None])
        cw = self.cw
        # sum_s cw R_a R_b [g11 + g12 (Ma + Mb) + g22 Ma Mb]
        Ya0 = Ra*cw[:, None]; Ya1 = Ya0*Ma[None, :]
        out = (Ya0*g11[:, None]).T @ Rb + (Ya1*g12[:, None]).T @ Rb \
            + (Ya0*g12[:, None]).T @ (Rb*Mb[None, :]) + (Ya1*g22[:, None]).T @ (Rb*Mb[None, :])
        return out

    def bound_mass(self):
        """mu_b solving 1 + lam <g|(M0 - mu)^{-1}|g> = 0 below 2m (bisection)."""
        f = lambda mu: 1.0 + self.lam*np.sum(self.gg2*self.wq/(self.M0g - mu))
        lo, hi = 1e-6, 2*self.m - 1e-12
        if f(lo)*f(hi) > 0: return None
        for _ in range(200):
            mid = 0.5*(lo+hi)
            if f(lo)*f(mid) <= 0: hi = mid
            else: lo = mid
        return 0.5*(lo+hi)

def lam_for_mass(m, kappa, d, mu_b, nq=6001):
    K = BTKernel(m, kappa, -1.0, d, nq=nq)
    return -1.0/np.sum(K.gg2*K.wq/(K.M0g - mu_b))
