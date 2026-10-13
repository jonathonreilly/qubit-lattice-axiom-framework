"""R18-9 library. Imports the archived R18-5 runners UNMODIFIED from ../arch18 (copied from
P/scripts/C5/R18-5/). Adds: (i) photon Xi as an exact quadratic in the VWa stencil weight a
(the vertex is affine in a, so sum_pol|amp|^2 and hence Xi are quadratic in a; three evaluations fix it);
(ii) Dirac rows under UD; (iii) the mu_T2 = 0 curve r*(b_f) on D1."""
import os, sys, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
import dfam
from content3 import D1q
from content4 import scalw
from r1712_lib import xi, photonGw
from zz import mu_E
from smud_lib import dirac, NS, ND, NV
from scipy.optimize import brentq

def phot_quad(bg, fw, N=48):
    """per vector: coefficients (c0, c1, c2) of Xi_T2g(a) and Xi_Eg(a) = c0 + c1 a + c2 a^2, and mu_E^gamma."""
    law = photonGw(bg, fw*(np.pi - bg))
    out = {}
    for pol in ('T2g', 'Eg'):
        v = np.array([xi(law, N, pol, 'VWa', lam=a)[0] for a in (0.0, 1.0, -1.0)])
        c0 = v[0]; c1 = 0.5*(v[1] - v[2]); c2 = 0.5*(v[1] + v[2]) - v[0]
        out[pol] = np.array([c0, c1, c2])
    g, f = law.samples(1 << 14)
    out['muE'] = 2*mu_E(g, f, 1e-3)
    return out

def phot_at(bg, fw, a, N=48):
    law = photonGw(bg, fw*(np.pi - bg))
    T = xi(law, N, 'T2g', 'VWa', lam=a)[0]; E = xi(law, N, 'Eg', 'VWa', lam=a)[0]
    g, f = law.samples(1 << 14)
    return np.array([T, E, 2*mu_E(g, f, 1e-3), 0.0])

def muT2(bf, r, m=0.01, q=(3, 8)):
    return dfam.evaluate(D1q(bf, r), m, *q)['muT2']

def rstar(bf, m=0.01, lo=0.2, hi=1/np.sqrt(3), q=(3, 8)):
    f = lambda r: muT2(bf, r, m, q)
    flo, fhi = f(lo), f(hi)
    if flo*fhi > 0: return None
    return brentq(f, lo, hi, xtol=1e-12)

def scal(bs, fr, m=0.01):
    return scalw(bs, fr, m, vert='U')[0]
