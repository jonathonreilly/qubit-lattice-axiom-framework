"""R16-3 module (independent code; R14-3's formulas re-derived).
Separable one-band law eps^2 = m^2 + sum_i g(k_i), g = sigma^2, sigma(0)=0, |sigma'|<=1.
sigma' piecewise constant (values v_j on [k_j, k_{j+1}]) blended by a C^inf step of width wt at each breakpoint.
Xi_v = (1/32) <|V|^2 (5 f_z^2 - eps^2)/eps^7>  (R9-9 Thm T after IBP; R14-3 (R2))
     = (1/(32 Gamma(5/2))) int dt t^{3/2} e^{-t m^2} W_v(t) J(t),  J = 2 t F2 - E0
W: M,T2g 4 G1^2; M,Eg 2(G2 E0 - G1^2); U,T2g 4 F2^2; U,Eg 2(F4 E0 - F2^2)
(E0,F2,F4,G1,G2)(t) = 1D zone means of (1, f^2, f^4, g, g^2) e^{-t g}."""
import numpy as np
from math import gamma

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

class ZLaw:
    def __init__(self, vals, bks, wt, name='', nf=1 << 18):
        # vals[0] = 1 on [0, bks[0]); vals[j] after breakpoint bks[j-1]; last value should be 0 (flat end) 
        self.vals, self.bks, self.wt, self.name = list(vals), list(bks), wt, name
        k = np.linspace(0, np.pi, nf+1); self.k = k
        sp = np.full_like(k, vals[0])
        for j, a in enumerate(bks):
            w = wt if np.isscalar(wt) else wt[j]
            sp = sp + (vals[j+1]-vals[j])*sstep((k - a + w/2)/w)
        dk = k[1]-k[0]
        sig = np.concatenate([[0.0], np.cumsum(0.5*(sp[1:]+sp[:-1])*dk)])
        self.sp, self.sig = sp, sig
        self.b = bks[0] - (wt if np.isscalar(wt) else wt[0])/2
    def samples(self, n):
        # midpoint grid on [-pi, pi]; even g, odd f
        kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
        a = np.abs(kk)
        s = np.interp(a, self.k, self.sig); sp = np.interp(a, self.k, self.sp)
        return s*s, np.sign(kk)*s*sp
    def info(self):
        s, sp = self.sig, self.sp
        g = s*s
        i = np.where((g[1:-1] < g[:-2]) & (g[1:-1] <= g[2:]))[0]+1
        return dict(maxabs=np.abs(sp).max(), sig_pi=s[-1], valleys=[(round(self.k[j],3), round(g[j],4)) for j in i])
    def vmax(self, m, d=3, n=200001):
        g, f = self.samples(n)
        phi = lambda lam: np.max(f*f - lam*g)
        lo, hi = 0.0, 1.0
        while d*phi(hi) > hi*m*m: hi *= 2
        for _ in range(70):
            mid = 0.5*(lo+hi)
            if d*phi(mid) > mid*m*m: lo = mid
            else: hi = mid
        return np.sqrt(0.5*(lo+hi))

def moments_from(g, f, t):
    W = np.exp(-np.outer(t, g))
    f2 = f*f
    return dict(E0=W.mean(1), F2=W@f2/len(g), F4=W@(f2*f2)/len(g), G1=W@g/len(g), G2=W@(g*g)/len(g))

def xi_all(g, f, m, nu=1500, umin=-16.0, chunk=200):
    umax = np.log(80.0/min(m*m, 1.0)) + 2
    u = np.linspace(umin, umax, nu); t = np.exp(u); du = u[1]-u[0]
    M = {kk: np.empty(nu) for kk in ['E0','F2','F4','G1','G2']}
    for i0 in range(0, nu, chunk):
        mm = moments_from(g, f, t[i0:i0+chunk])
        for kk in M: M[kk][i0:i0+chunk] = mm[kk]
    E0, F2, F4, G1, G2 = (M[x] for x in ['E0','F2','F4','G1','G2'])
    J = 2*t*F2 - E0
    base = t*du * t**1.5*np.exp(-t*m*m)*J/(32*gamma(2.5))
    W = {'M,T2g': 4*G1**2, 'M,Eg': 2*(G2*E0 - G1**2), 'U,T2g': 4*F2**2, 'U,Eg': 2*(F4*E0 - F2**2)}
    return {v: float(np.sum(base*Wv)) for v, Wv in W.items()}

def Icurve(g, f, Bs):
    return np.array([2*np.pi*np.mean((5*f*f-(B+g))/(B+g)**3.5) for B in Bs])

def xi_grid(g1, f1, m, which=('M,T2g','U,T2g','M,Eg','U,Eg')):
    """Direct 3D zone grid, IBP form; g1, f1 sampled on N-point midpoint grid."""
    N = len(g1)
    gx = g1[:, None, None]; gy = g1[None, :, None]; gz = g1[None, None, :]
    fx2 = (f1*f1)[:, None, None]; fy2 = (f1*f1)[None, :, None]; fz2 = (f1*f1)[None, None, :]
    e2 = m*m + gx + gy + gz
    core = (5*fz2 - e2)/e2**3.5
    out = {}
    V = {'M,T2g': 4*gx*gy, 'M,Eg': (gx-gy)**2, 'U,T2g': 4*fx2*fy2, 'U,Eg': (fx2-fy2)**2}
    for v in which:
        out[v] = float(np.mean(V[v]*core)/32)
    return out

def mu_E(g, f, m, nu=1500, umin=-16.0):
    """R14-3 (R1) kurtosis form: mu_E = [12 Gamma(3/2)]^-1 int dt t^{1/2} e^{-t m^2} E0 [3 F2^2 - F4 E0]."""
    umax = np.log(80.0/min(m*m, 1.0)) + 2
    u = np.linspace(umin, umax, nu); t = np.exp(u); du = u[1]-u[0]
    mm = moments_from(g, f, t)
    return float(np.sum(t*du*t**0.5*np.exp(-t*m*m)*mm['E0']*(3*mm['F2']**2 - mm['F4']*mm['E0']))/(12*gamma(1.5)))

class Mix:
    """Convex mixture of sigma' profiles (same k grid): stays in |sigma'| <= 1; sigma'(pi) = 0 if all are."""
    def __init__(self, laws, w, name='mix'):
        self.k = laws[0].k; self.sp = sum(wi*L.sp for wi, L in zip(w, laws))
        dk = self.k[1]-self.k[0]
        self.sig = np.concatenate([[0.0], np.cumsum(0.5*(self.sp[1:]+self.sp[:-1])*dk)]); self.name = name
    samples = ZLaw.samples; info = ZLaw.info; vmax = ZLaw.vmax
