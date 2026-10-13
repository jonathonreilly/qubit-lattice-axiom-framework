"""C5 R18-12: shared law definitions (lattice units, a = 1).

Matter (registered setting, TESTS R18-12):
  S(b)  scalar: eps^2 = m^2 + sum s(k_i)^2           (R13-4/R14-1 odd symbol; mirror boxes at the corners)
  G(b)  scalar: eps^2 = m^2 + sum g(k_i)             (R14-1 gapped even form; no light corners)
  D1(b, r) Dirac: E^2 = (m + sum W(k_i))^2 + sum s(k_i)^2   (R14-1 sec. 6, copied construction; doublers m + n W_pi)
Photon (transverse), omega^2 = sum d(q_j)^2 (R8-5 form):
  'R85'  d = rho q + (1 - rho) 2 sin(q/2), rho = 1 on |q| <= c1, 0 on |q| >= c2 (Gevrey step), c1 = 1, c2 = 2
  'std'  d = 2 sin(q/2)                     (plain plaquette photon)
  'max'  d = |q| (wrapped)                  pointwise UPPER envelope of the subluminal nondecreasing class (d' in [0,1], d(0)=0)
  'min1' d = min(|q|, 1)                    pointwise LOWER envelope of that class with box |q| <= 1
Separable pieces are returned per component so that sums over a 3D grid can be broadcast.
Defect (R16-8/R18-8): Delta_cc = eps * (d_c^2 (eps^2/2) - 1).
"""
import os, sys
os.environ.setdefault("OMP_NUM_THREADS", "2")
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sublum_copy import SymS, SymG, sstep, wrap

B = 1.4
S14, G14 = SymS(B), SymG(B)

# ---- D1(b, r) Wilson piece, copied from R14-1 r141_wilson.py make() ----
def make_W(b=B, r=1/np.sqrt(3)):
    A = SymS(b); w = A.w
    xg, wg = np.polynomial.legendre.leggauss(8)
    edges = np.linspace(0, 1, 20001); mid = 0.5*(edges[1:]+edges[:-1]); half = 0.5*(edges[1]-edges[0])
    sig = lambda x: 1 - 2*sstep(x)
    cell = (np.sqrt(np.maximum(0, 1 - sig(mid[:, None] + half*xg[None, :])**2))*wg).sum(1)*half
    tab = np.concatenate([[0.0], np.cumsum(cell)])*w*r
    def W(k):
        a = np.abs(wrap(np.asarray(k, float))); x = np.clip((a - b)/w, 0, 1); return np.interp(x, edges, tab)
    return W, tab[-1]
W14, WPI = make_W()

def num_d2(f, k, h=1e-4):
    return (f(k + h) - 2*f(k) + f(k - h))/h**2
def num_d1(f, k, h=1e-5):
    return (f(k + h) - f(k - h))/(2*h)

class Matter:
    """name in {'S','G','D1'}; methods give per-component pieces and full eps, Delta diag."""
    def __init__(self, name, m):
        self.name, self.m = name, m
    def eps(self, K):
        K = np.atleast_2d(K)
        if self.name == 'S':
            return np.sqrt(self.m**2 + (S14.s(K)**2).sum(-1))
        if self.name == 'G':
            return np.sqrt(self.m**2 + G14.g(K).sum(-1))
        if self.name == 'D1':
            return np.sqrt((self.m + W14(K).sum(-1))**2 + (S14.s(K)**2).sum(-1))
    def grid_eps(self, kg):
        """eps on the N^3 product grid kg x kg x kg."""
        if self.name == 'S':
            u = S14.s(kg)**2; return np.sqrt(self.m**2 + u[:, None, None] + u[None, :, None] + u[None, None, :])
        if self.name == 'G':
            u = G14.g(kg); return np.sqrt(self.m**2 + u[:, None, None] + u[None, :, None] + u[None, None, :])
        if self.name == 'D1':
            u = S14.s(kg)**2; w = W14(kg)
            return np.sqrt((self.m + w[:, None, None] + w[None, :, None] + w[None, None, :])**2
                           + u[:, None, None] + u[None, :, None] + u[None, None, :])
    def shifted_eps(self, Q, kg):
        """eps(Q - p) for p on the product grid (Q a 3-vector)."""
        cs = [wrap(Q[j] - kg) for j in range(3)]
        if self.name in ('S', 'D1'):
            u = [S14.s(c)**2 for c in cs]
        else:
            u = [G14.g(c) for c in cs]
        U = u[0][:, None, None] + u[1][None, :, None] + u[2][None, None, :]
        if self.name == 'D1':
            w = [W14(c) for c in cs]; Wt = w[0][:, None, None] + w[1][None, :, None] + w[2][None, None, :]
            return np.sqrt((self.m + Wt)**2 + U)
        return np.sqrt(self.m**2 + U)
    def delta(self, K):
        """diagonal of Delta_cb (separable bands -> diagonal), shape (n,3)."""
        K = np.atleast_2d(np.asarray(K, float)); e = self.eps(K)
        f = lambda kk: 0.5*self.eps(kk)**2
        out = np.zeros_like(K)
        for c in range(3):
            def fc(x, c=c):
                KK = K.copy(); KK[:, c] = x; return f(KK)
            out[:, c] = num_d2(fc, K[:, c])
        return e[:, None]*(out - 1.0)
    def is_edge(self, K):
        return (np.abs(wrap(np.atleast_2d(K))) > B + 1e-12).any(-1)

def rho(q, c1=1.0, c2=2.0):
    a = np.abs(wrap(np.asarray(q, float)))
    return 1 - sstep((a - c1)/(c2 - c1))

PHOTONS = {
    'R85':  lambda q: rho(q)*np.abs(wrap(q)) + (1 - rho(q))*2*np.abs(np.sin(wrap(q)/2)),
    'std':  lambda q: 2*np.abs(np.sin(np.asarray(q, float)/2)),
    'max':  lambda q: np.abs(wrap(np.asarray(q, float))),
    'min1': lambda q: np.minimum(np.abs(wrap(np.asarray(q, float))), 1.0),
}
PHOTON_BOX = {'R85': 1.0, 'std': 0.0, 'max': np.pi, 'min1': 1.0}

def omega(name, Q):
    d = PHOTONS[name]; Q = np.atleast_2d(np.asarray(Q, float))
    return np.sqrt((d(Q)**2).sum(-1))

def omega_shift(name, Q, kg):
    """omega(Q - p), p on the product grid."""
    d = PHOTONS[name]; u = [d(wrap(Q[j] - kg))**2 for j in range(3)]
    return np.sqrt(u[0][:, None, None] + u[1][None, :, None] + u[2][None, None, :])

def photon_delta(name, Q):
    Q = np.atleast_2d(np.asarray(Q, float)); w = omega(name, Q)
    out = np.zeros_like(Q)
    for c in range(3):
        def fc(x, c=c):
            QQ = Q.copy(); QQ[:, c] = x; return 0.5*omega(name, QQ)**2
        out[:, c] = num_d2(fc, Q[:, c])
    return w[:, None]*(out - 1.0)
