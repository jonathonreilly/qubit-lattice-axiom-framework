"""R16-10 law adapters (matter and photon symbols as plain 1D functions).
Matter:
  scalar G(b): u = h_b^2 (R14-1 SymG; u'/2 = h h' <= h <= k: non-rising), box |k| <= b.
  Dirac D1(b, r): R14-1 / R16-2 make() (verbatim, via arch/R16-2/r162_laws.py); s = SymS(b), W Wilson, box |k| <= b.
  Dirac literal L(b1, b2): R8-5 S = rho k + (1-rho) sin k (W = 0), box |k| <= b1.
Photon (d odd, t = d^2 even periodic):
  'R85'(c1, c2, G): d = rho_g q + (1 - rho_g) G 2 sin(q/2)   (G = 1: R8-5's photon; G > 1: stiffened)
  'Gph'(c): d = h_c(q) = SymG(c).h  -- nondecreasing, d' in [0, 1] (subluminal), d = q on |q| <= c, d(pi) = (pi + c)/2
  'naive': 2 sin(q/2)
"""
import numpy as np, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'arch', 'R16-2'))
from sublum import SymG, SymS, sstep, dsstep, wrap
from r85_box_qed_copy import plateau
import r162_laws

def photon(kind, *args):
    if kind == 'naive':
        return lambda q: 2*np.sin(np.asarray(q, float)/2)
    if kind == 'R85':
        c1, c2, G = args
        def d(q):
            q = np.asarray(q, float); rg = plateau(q, c1, c2)
            return rg*q + (1 - rg)*G*2*np.sin(q/2)
        return d
    if kind == 'Gph':
        c, = args; g = SymG(c)
        def d(q):
            q = np.asarray(q, float); return np.sign(wrap(q))*g.h(q)
        return d
    if kind == 'Gstiff':          # Gph shape times a stiffening factor outside the box: d = h_c + (G-1)(h_c - h_c restricted) ...
        c, G = args; g = SymG(c)
        def d(q):
            q = np.asarray(q, float); a = np.abs(wrap(q)); hh = g.h(q)
            return np.sign(wrap(q))*(hh + (G - 1)*(hh - np.minimum(a, c)))   # = q in box; slope 1 + (G-1)(h' - 0) ... nondecreasing
        return d
    raise ValueError(kind)

def scalar_G(b):
    g = SymG(b)
    return (lambda k: g.g(np.asarray(k, float)))

def dirac_D1(b, r):
    A, W, dW, Wpi = r162_laws.make(b, r)
    return (lambda k: A.s(np.asarray(k, float))), (lambda k: W(np.asarray(k, float)))

def dirac_lit(b1, b2):
    def S(k):
        k = np.asarray(k, float); rho = plateau(k, b1, b2); return rho*k + (1 - rho)*np.sin(k)
    return S, (lambda k: 0.0*np.asarray(k, float))
