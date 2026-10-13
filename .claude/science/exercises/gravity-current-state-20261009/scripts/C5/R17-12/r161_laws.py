"""R16-1: law classes with R8-5's Law interface (attributes m, b1, b2, r, c1, c2; methods S, W, d).
D1Law(b, r, m, photon): R14-1's subluminal Wilson-box Dirac D1(r):
   s = R13-4 odd symbol S(b) (s' = 1 on [0,b], Gevrey step to -1 on [b, pi-b], -1 on [pi-b, pi]);
   W' = r sqrt(1 - s'^2) = 2 r sqrt(st(1-st)) on the slab [b, pi-b], W = 0 on [0,b], W = W_pi on [pi-b, pi]; W even.
   W is tabulated by Gauss-Legendre cells + CubicSpline (C^2 interpolant; R14-1 used linear interp, which has no W'').
photon: 'naive' -> d = 2 sin(q/2) (no photon box);  (c1, c2) -> R8-5 plateau photon d = rho q + (1-rho) 2 sin(q/2).
"""
import numpy as np
from scipy.interpolate import CubicSpline
from sublum import sstep, wrap, SymS
from r85_box_qed_copy import plateau

_xg, _wg = np.polynomial.legendre.leggauss(8)

class D1Law:
    def __init__(self, b, r, m, photon='naive', ncell=20000):
        self.b, self.r, self.m = b, r, m
        self.b1, self.b2 = b, np.pi - b          # (informational)
        self.A = SymS(b); w = self.A.w
        edges = np.linspace(0, 1, ncell + 1); mid = 0.5 * (edges[1:] + edges[:-1]); half = 0.5 * (edges[1] - edges[0])
        st = sstep(mid[:, None] + half * _xg[None, :])
        cell = (2 * np.sqrt(np.maximum(0, st * (1 - st))) * _wg).sum(1) * half
        tab = np.concatenate([[0.0], np.cumsum(cell)]) * w * r
        self._Wsp = CubicSpline(edges, tab)
        self.Wpi = tab[-1]
        if photon == 'naive':
            self.c1 = self.c2 = None; self.naive_photon = True
        else:
            self.c1, self.c2 = photon; self.naive_photon = False
    def S(self, k):
        return self.A.s(np.asarray(k, float))
    def W(self, k):
        a = np.abs(wrap(np.asarray(k, float)))
        x = np.clip((a - self.b) / self.A.w, 0.0, 1.0)
        return self._Wsp(x)
    def dW(self, k):
        k = wrap(np.asarray(k, float)); x = (np.abs(k) - self.b) / self.A.w
        st = sstep(x)
        return np.sign(k) * 2 * self.r * np.sqrt(np.maximum(0, st * (1 - st)))
    def d(self, q):
        if self.naive_photon:
            return 2 * np.sin(np.asarray(q, float) / 2)
        q = wrap(np.asarray(q, float))
        rg = plateau(q, self.c1, self.c2)
        return rg * q + (1 - rg) * 2 * np.sin(q / 2)

class BQLaw:
    """R8-5's BQ law (S = rho k + (1-rho) sin k, W = r (1-rho)(1-cos k)) with a free choice of photon:
    photon = 'naive' | (c1, c2)."""
    def __init__(self, b1, b2, r, m, photon='naive'):
        self.b1, self.b2, self.r, self.m = b1, b2, r, m
        if photon == 'naive':
            self.c1 = self.c2 = None; self.naive_photon = True
        else:
            self.c1, self.c2 = photon; self.naive_photon = False
    def S(self, k):
        k = wrap(np.asarray(k, float))      # periodic extension (R8-5's Law is only valid on [-pi, pi])
        rho = plateau(k, self.b1, self.b2); return rho * k + (1 - rho) * np.sin(k)
    def W(self, k):
        k = wrap(np.asarray(k, float))
        rho = plateau(k, self.b1, self.b2); return self.r * (1 - rho) * (1 - np.cos(k))
    def d(self, q):
        if self.naive_photon:
            return 2 * np.sin(np.asarray(q, float) / 2)
        q = wrap(np.asarray(q, float))
        rg = plateau(q, self.c1, self.c2)
        return rg * q + (1 - rg) * 2 * np.sin(q / 2)

def with_mass(law, m):
    import copy
    l2 = copy.copy(law); l2.m = m; return l2
