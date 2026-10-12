"""C5 R14-3 shared module: separable one-band box laws eps^2 = m^2 + sum_i g(k_i), g = sigma^2,
sigma(0) = 0, sigma' = 1 on [0, b] (box: g = k^2), sigma' built from Gevrey (sstep) transitions on [b, pi].
Even g; f = g'/2 = sigma sigma' (odd), f' = g''/2 = sigma'^2 + sigma sigma'' = 1 + A  (A = Theorem E anomaly, axis comp.)
Odd-symbol laws (eps^2 = m^2 + sum s^2, s odd) are the case sigma(pi) = 0.
Quantities (all per scalar species, lattice units, <.> = zone mean over d^3k/(2pi)^3):
  mu_E (R9-2 closed form, zero-point eps/2, RN-L1 norm):  mu_E = -(1/8) <(f'_x - f'_y)(f_x^2 - f_y^2)/eps>
        = (1/12) <(3 f_x^2 f_y^2 - f_x^4)/eps^3>      (integration by parts in k_x; proved here)
  Xi (R9-9 Theorem T): Xi = (1/32) <|V|^2 A_zz / eps^5> = (1/32) <|V|^2 (5 f_z^2 - eps^2)/eps^7>  (IBP in k_z)
  vertices (R9-9 class V): M: T2g 4 g_x g_y, Eg (g_x - g_y)^2 ; U: T2g 4 f_x^2 f_y^2, Eg (f_x^2 - f_y^2)^2
  v_max (d=3, exact for separable laws): v^2 = lam solves d * max_k (f^2 - lam g) = lam m^2 (bisection).
"""
import numpy as np
from scipy.interpolate import CubicSpline

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

class Law:
    """sigma' = v0 + sum_j (v_{j+1}-v_j) sstep((k - a_j)/w_j) on [0, pi]; v0 = 1 and first a_0 >= b."""
    def __init__(self, vals, starts, widths, name='', nfine=400001):
        self.vals, self.starts, self.widths, self.name = list(vals), list(starts), list(widths), name
        self.b = starts[0] if starts else np.pi
        kf = np.linspace(0, np.pi, nfine); self.kf = kf
        sp = self.dsig(kf)
        hh = 1e-6
        spp = (self.dsig(kf + hh) - self.dsig(kf - hh))/(2*hh)
        spp[0] = 0.0
        # sigma by cumulative Simpson-like (trapezoid + endpoint correction via spline integral)
        cs = CubicSpline(kf, sp)
        sig = cs.antiderivative()(kf)
        self._s, self._sp, self._spp = CubicSpline(kf, sig), CubicSpline(kf, sp), CubicSpline(kf, spp)
        self.sig_pi = sig[-1]; self.sp_pi = sp[-1]
    def dsig(self, k):
        k = np.asarray(k, float); out = np.full_like(k, self.vals[0])
        for j, (a, w) in enumerate(zip(self.starts, self.widths)):
            out = out + (self.vals[j+1] - self.vals[j])*sstep((k - a)/w)
        return out
    def gff(self, k):
        """g, f, f' at arbitrary k (periodic, even g)."""
        kw = wrap(np.asarray(k, float)); a = np.abs(kw); sg = np.sign(kw)
        s, sp, spp = self._s(a), self._sp(a), self._spp(a)
        return s*s, sg*s*sp, sp*sp + s*spp
    def vmax(self, m, d=3, n=200001):
        k = np.linspace(0, np.pi, n); g, f, fp = self.gff(k)
        phi = lambda lam: np.max(f*f - lam*g)
        lo, hi = 0.0, 1.0
        while d*phi(hi) > hi*m*m: hi *= 2
        for _ in range(80):
            mid = 0.5*(lo+hi)
            if d*phi(mid) > mid*m*m: lo = mid
            else: hi = mid
        return np.sqrt(0.5*(lo+hi))
    def Amax(self, n=200001):
        k = np.linspace(0, np.pi, n); g, f, fp = self.gff(k); return (fp-1).max(), (fp-1).min()
    def sig_minmax_edge(self, n=200001):
        k = np.linspace(self.b, np.pi, n); s = self._s(k); return s.min(), s.max()

def grid(N):
    return 2*np.pi*(np.arange(N)+0.5)/N - np.pi

def mu_E(law, m, N=240):
    k = grid(N); g, f, fp = law.gff(k)
    GX, GY = g[:, None], g[None, :]; FX, FY = f[:, None], f[None, :]; PX, PY = fp[:, None], fp[None, :]
    t1 = t2 = 0.0
    for gz in g:
        e = np.sqrt(m*m + GX + GY + gz)
        t1 += ((PX - PY)*(FX**2 - FY**2)/e).sum()
        t2 += ((3*FX**2*FY**2 - FX**4)/e**3).sum()
    return -t1/8/N**3, t2/12/N**3

def Xi(law, m, N=240):
    k = grid(N); g, f, fp = law.gff(k); A = fp - 1
    GX, GY = g[:, None], g[None, :]; FX, FY = f[:, None], f[None, :]
    verts = {'M,T2g': 4*GX*GY, 'M,Eg': (GX-GY)**2, 'U,T2g': 4*FX**2*FY**2, 'U,Eg': (FX**2-FY**2)**2}
    out = {v: [0.0, 0.0] for v in verts}
    for gz, fz, az in zip(g, f, A):
        e2 = m*m + GX + GY + gz; e = np.sqrt(e2)
        wA = az/e**5; wI = (5*fz*fz - e2)/e**7
        for v, V2 in verts.items():
            out[v][0] += (V2*wA).sum(); out[v][1] += (V2*wI).sum()
    return {v: (a/32/N**3, b/32/N**3) for v, (a, b) in out.items()}

def IB(law, B, n=40001):
    k = np.linspace(-np.pi, np.pi, n)[:-1]; g, f, fp = law.gff(k)
    return np.sum((fp-1)/(B+g)**2.5)*(2*np.pi/len(k)), np.sum((5*f*f-(B+g))/(B+g)**3.5)*(2*np.pi/len(k))

# ---- standard families
def G_law(b):       # R14-1 G(b): sigma' = 1 - sstep((k-b)/(pi-b))
    return Law([1.0, 0.0], [b], [np.pi-b], 'G(%.2f)' % b)
def S_law(b):       # R13-4 S(b): sigma' 1 -> -1 over [b, pi-b]
    return Law([1.0, -1.0], [b], [np.pi-2*b], 'S(%.2f)' % b)
