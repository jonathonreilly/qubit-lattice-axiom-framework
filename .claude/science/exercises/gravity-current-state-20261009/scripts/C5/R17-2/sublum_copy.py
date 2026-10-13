"""R14-1: subluminal one-band box symbols (b <= 1.4, Gevrey step), accurate (no 2^16 linear interpolation).
(S) R13-4's odd symbol: s' = sigma = 1 on [0,b], 1 - 2 sstep((k-b)/w) on [b, pi-b] (w = pi - 2b), -1 on [pi-b, pi];
    s(k) = k on [0,b];  k - 2 w Phi((k-b)/w) on [b, pi-b];  pi - k on [pi-b, pi];  odd, 2pi-periodic.
    Phi(x) = int_0^x sstep, tabulated by 8-point Gauss-Legendre per cell + CubicSpline (error ~1e-15).
    eps_S = sqrt(m^2 + sum s(k_i)^2).  Identity: s(pi - k) = s(k)  -> exact mirror boxes at the corners.
(G) gapped even-g form (R8-2 option (b) type): eps_G^2 = m^2 + sum g(k_i), g = h^2 on [0,pi] extended even,
    h' = 1 - sstep((k-b)/(pi-b)) on [b, pi]  (h' in [0,1], flat zero at pi), h = k on [0,b].
    |grad eps_G| <= |(h h')_i| / sqrt(m^2 + sum h^2) < 1 for every b < pi (elementary).
"""
import numpy as np
from scipy.interpolate import CubicSpline

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def dsstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
        d1 = np.where(x > 0, e1/np.where(x > 0, x, 1)**2, 0.0)
        d2 = np.where(x < 1, e2/np.where(x < 1, 1-x, 1)**2, 0.0)
    return (d1*e2 + e1*d2)/(e1+e2)**2

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def _Phi_table(n=40000):
    xg, wg = np.polynomial.legendre.leggauss(8)
    edges = np.linspace(0, 1, n+1); a, bb = edges[:-1], edges[1:]
    mid, half = 0.5*(a+bb), 0.5*(bb-a)
    cell = (sstep(mid[:, None] + half[:, None]*xg[None, :])*wg[None, :]).sum(1)*half
    Phi = np.concatenate([[0.0], np.cumsum(cell)])
    return CubicSpline(edges, Phi)
_PHI = _Phi_table()
def Phi(x):
    x = np.clip(x, 0.0, 1.0)
    return _PHI(x)

class SymS:
    """R13-4 odd subluminal symbol."""
    def __init__(self, b):
        assert b < np.pi/2
        self.b, self.w = b, np.pi - 2*b
    def s(self, k):
        k = wrap(np.asarray(k, float)); a = np.abs(k); b, w = self.b, self.w
        v = np.where(a <= b, a, np.where(a >= np.pi - b, np.pi - a, a - 2*w*Phi((a - b)/w)))
        return np.sign(k)*v
    def ds(self, k):
        a = np.abs(wrap(np.asarray(k, float)))
        return 1 - 2*sstep((a - self.b)/self.w)
    def d2s(self, k):
        k = wrap(np.asarray(k, float)); a = np.abs(k)
        return -np.sign(k)*2*dsstep((a - self.b)/self.w)/self.w

class SymG:
    """gapped even-g subluminal form: g = h^2, h' = 1 - sstep((|k|-b)/(pi-b))."""
    def __init__(self, b):
        self.b, self.w = b, np.pi - b
    def h(self, k):
        a = np.abs(wrap(np.asarray(k, float))); b, w = self.b, self.w
        return np.where(a <= b, a, a - w*Phi((a - b)/w))
    def dh(self, k):            # derivative of h(|k|) w.r.t. |k|
        a = np.abs(wrap(np.asarray(k, float)))
        return 1 - sstep((a - self.b)/self.w)
    def g(self, k):
        return self.h(k)**2
    def dg(self, k):            # g'(k), odd
        k = wrap(np.asarray(k, float))
        return np.sign(k)*2*self.h(k)*self.dh(k)
    def d2g(self, k):
        a = np.abs(wrap(np.asarray(k, float)))
        hp = self.dh(k); hpp = -dsstep((a - self.b)/self.w)/self.w
        return 2*(hp**2 + self.h(k)*hpp)
