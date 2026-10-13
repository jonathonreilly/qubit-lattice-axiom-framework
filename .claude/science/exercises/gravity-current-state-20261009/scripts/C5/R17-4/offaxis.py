"""R17-4 (a): off-axis one-loop TT cone coefficient for separable laws in S, E1 extension.
E1 (stated extension): the pair (k + q/2, k - q/2) has TT vertex V_e(k) = sum_ij e_ij tau_ij(k), with k the relative momentum,
  M: tau_ij = sigma_i sigma_j,  U: tau_ij = f_i f_j  (f = sigma sigma'),  q-independent at fixed relative momentum.
  On the axis (e transverse to z) V_e depends on (k_x, k_y) only, so E1 = R9-9's class V there.
Closed form (derived in the report):  Xi(n,e) = (5/32)<W S^2/eps^7> - (1/32)<W/eps^5> - (3/64)<(n.grad W) S/eps^5>,
  W = V_e^2, S = sum_i n_i f_i (so S/eps = n.grad eps).  Equivalently (1/32)<W A_nn/eps^5> - (1/192)<(n.grad)^2 W/eps^3>.
Laplace-separable evaluation: 1/eps^p = Gamma(p/2)^-1 int t^{p/2-1} e^{-t eps^2} dt; integrand monomials factorize per axis."""
import numpy as np, sympy as sp
from math import gamma
sx = sp.symbols('s0:3'); fx = sp.symbols('f0:3'); spx = sp.symbols('sp0:3'); fpx = sp.symbols('fp0:3')

def _expr(n, e, vtx):
    n = [sp.nsimplify(x) if isinstance(x, (int,)) else x for x in n]
    if vtx == 'M':
        tau = [[sx[i]*sx[j] for j in range(3)] for i in range(3)]
        dtau = lambda k: [[(spx[k]*sx[j] if i == k else 0) + (spx[k]*sx[i] if j == k else 0) for j in range(3)] for i in range(3)]
    else:
        tau = [[fx[i]*fx[j] for j in range(3)] for i in range(3)]
        dtau = lambda k: [[(fpx[k]*fx[j] if i == k else 0) + (fpx[k]*fx[i] if j == k else 0) for j in range(3)] for i in range(3)]
    V = sum(e[i][j]*tau[i][j] for i in range(3) for j in range(3))
    DV = sum(n[k]*sum(e[i][j]*dtau(k)[i][j] for i in range(3) for j in range(3)) for k in range(3))
    W = sp.expand(V*V); DW = sp.expand(2*V*DV); S = sum(n[i]*fx[i] for i in range(3))
    # three pieces with their eps powers
    return [(sp.expand(sp.Rational(5, 32)*W*S*S), 7), (sp.expand(-sp.Rational(1, 32)*W), 5), (sp.expand(-sp.Rational(3, 64)*DW*S), 5)]

def _terms(n, e, vtx):
    out = []
    for ex, p in _expr(n, e, vtx):
        poly = sp.Poly(ex, *(sx + fx + spx + fpx))
        for mon, c in poly.terms():
            exps = tuple((mon[i], mon[3+i], mon[6+i], mon[9+i]) for i in range(3))
            if any((a + b) % 2 for (a, b, c_, d) in exps):  # sigma, f odd per axis -> zero mean
                continue
            out.append((float(c), p, exps))
    return out

class Moments:
    """1D zone moments <sigma^a f^b sigma'^c f'^d e^{-t g}> on a t grid."""
    def __init__(self, law, m, n1=1 << 14, nu=1500, umin=-16.0, chunk=150):
        kk = 2*np.pi*(np.arange(n1)+0.5)/n1 - np.pi; a = np.abs(kk); sg = np.sign(kk)
        s = sg*np.interp(a, law.k, law.sig); spv = np.interp(a, law.k, law.sp)
        spp = sg*np.interp(a, law.k, np.gradient(law.sp, law.k))   # sigma'' (odd)
        self.s, self.sp, self.f = s, spv, s*spv; self.fp = spv*spv + s*spp; self.g = s*s
        umax = np.log(80.0/min(m*m, 1.0)) + 2
        u = np.linspace(umin, umax, nu); self.t = np.exp(u); self.du = u[1]-u[0]; self.m = m
        self.chunk = chunk; self.cache = {}
    def mom(self, key):
        if key not in self.cache:
            a, b, c, d = key
            w = self.s**a * self.f**b * self.sp**c * self.fp**d
            out = np.empty(len(self.t))
            for i0 in range(0, len(self.t), self.chunk):
                E = np.exp(-np.outer(self.t[i0:i0+self.chunk], self.g))
                out[i0:i0+self.chunk] = E @ w / len(self.g)
            self.cache[key] = out
        return self.cache[key]
    def eps_avg(self, terms):
        """sum_terms c <prod_i mono_i / eps^p>"""
        t, m = self.t, self.m; tot = 0.0
        for c, p, exps in terms:
            prod = np.ones_like(t)
            for ex in exps: prod = prod*self.mom(ex)
            tot += c*np.sum(t*self.du * t**(p/2-1)*np.exp(-t*m*m)*prod)/gamma(p/2)
        return tot

r2, r3, r6 = np.sqrt(2), np.sqrt(3), np.sqrt(6)
def _pols():
    z = [0, 0, 1]; fd = [1/r2, 1/r2, 0]; bd = [1/r3]*3
    Eg = np.diag([1., -1, 0]); T2 = np.zeros((3, 3)); T2[0, 1] = T2[1, 0] = 1
    a = np.array([1, -1, 0])/r2; bz = np.array([0, 0, 1.]); bb = np.array([1, 1, -2])/r6
    F1 = np.outer(a, a)-np.outer(bz, bz); F2 = np.outer(a, bz)+np.outer(bz, a)
    B1 = np.outer(a, a)-np.outer(bb, bb)
    return {'Eg': (z, Eg), 'T2g': (z, T2), 'face1': (fd, F1), 'face2': (fd, F2), 'body': (bd, B1)}
POLS = _pols()
_TERMS = {}
def terms(name, vtx):
    if (name, vtx) not in _TERMS:
        n, e = POLS[name]
        _TERMS[(name, vtx)] = _terms(list(n), [[float(e[i, j]) for j in range(3)] for i in range(3)], vtx)
    return _TERMS[(name, vtx)]

def xi_off(law, m, vtx='M', names=('Eg', 'T2g', 'face1', 'face2', 'body'), mom=None, **kw):
    mom = mom or Moments(law, m, **kw)
    return {nm: mom.eps_avg(terms(nm, vtx)) for nm in names}, mom

def relation(X):
    """O_h on-shell TT identity (basis.py): body = (8 face1 + 4 face2 - 3 Eg)/9."""
    return X['body'] - (8*X['face1'] + 4*X['face2'] - 3*X['Eg'])/9
