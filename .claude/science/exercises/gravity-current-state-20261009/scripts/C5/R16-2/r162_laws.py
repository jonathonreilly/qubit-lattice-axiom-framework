"""R16-2: law adapters.
D1Law: R14-1's subluminal Wilson-box Dirac D1(r) (r141_wilson.make, copied verbatim below), in the interface of
R8-5/R13-7 (methods S, W, d and attribute m), so that r137_onshell.dE_onshell and r101 moment() run unchanged.
  h(k) = sum_j s(k_j) alpha_j + (m + sum_j W(k_j)) beta,  s = SymS(b) (|s'| <= 1),  W' = r sqrt(1 - s'^2) on [b, pi-b].
  Box |k_j| <= b: s = k, W = 0 -> E = sqrt(m^2 + k^2) exactly (tree c = 1 for every m).
  Whole-zone v_max <= 1 for r <= 1/sqrt(3) (R14-1 theorem, Cauchy-Schwarz).
Photon: R8-5's box photon d = rho_g q + (1 - rho_g) 2 sin(q/2), plateau (c1, c2); c1 = None -> naive 2 sin(q/2).
LitLaw: R8-5's BQ literal edge (r = 0) is r85_box_qed_copy.Law(b1, b2, 0, c1, c2, m).
GScal: R14-1's gapped even scalar G(b): eps^2 = m^2 + sum u(k_j), u = h^2, h' = 1 - sstep((|k| - b)/(pi - b)).
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from sublum import sstep, wrap, SymS, SymG
from r85_box_qed_copy import plateau

xg, wg = np.polynomial.legendre.leggauss(8)

def make(b, r):
    """verbatim logic of r141_wilson.make (R14-1)."""
    A = SymS(b); w = A.w
    edges = np.linspace(0, 1, 20001); mid = 0.5*(edges[1:]+edges[:-1]); half = 0.5*(edges[1]-edges[0])
    sig = lambda x: 1 - 2*sstep(x)
    cell = (np.sqrt(np.maximum(0, 1 - sig(mid[:, None] + half*xg[None, :])**2))*wg).sum(1)*half
    tab = np.concatenate([[0.0], np.cumsum(cell)])*w*r
    def W(k):
        a = np.abs(wrap(k)); x = np.clip((a - b)/w, 0, 1); return np.interp(x, edges, tab)
    def dW(k):
        k = wrap(k); a = np.abs(k); x = (a - b)/w
        return np.sign(k)*r*np.sqrt(np.maximum(0, 1 - (1 - 2*sstep(x))**2))
    return A, W, dW, tab[-1]

def photon_d(c1, c2):
    if c1 is None:
        return lambda q: 2*np.sin(np.asarray(q, float)/2)
    def d(q):
        q = np.asarray(q, float); rg = plateau(q, c1, c2)
        return rg*q + (1 - rg)*2*np.sin(q/2)
    return d

class D1Law:
    def __init__(self, b, r, c1, c2, m):
        self.b, self.r, self.c1, self.c2, self.m = b, r, c1, c2, m
        self.A, self._W, self._dW, self.Wpi = make(b, r)
        self._d = photon_d(c1, c2)
        self.naive_photon = c1 is None
    def S(self, k):
        return self.A.s(np.asarray(k, float))
    def W(self, k):
        return self._W(np.asarray(k, float))
    def d(self, q):
        return self._d(q)

class GScal:
    def __init__(self, b, c1, c2, m):
        self.b, self.c1, self.c2, self.m = b, c1, c2, m
        self.G = SymG(b)
        self._d = photon_d(c1, c2)
    def u(self, k):
        return self.G.g(np.asarray(k, float))
    def up(self, k):
        return self.G.dg(np.asarray(k, float))
    def upp(self, k):
        return self.G.d2g(np.asarray(k, float))
    def d(self, q):
        return self._d(q)
