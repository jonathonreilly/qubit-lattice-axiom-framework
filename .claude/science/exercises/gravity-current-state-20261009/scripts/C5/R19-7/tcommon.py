"""R19-7: general-torus (period lattice in Hermite normal form) version of R18-1/R19-1 common.py.
Periods a1=(h1,0,0), a2=(r,h2,0), a3=(p,q,h3). Sites: x in [0,h1), y in [0,h2), z in [0,h3).
At (h1,h2,h3)=(L,L,L), r=p=q=0 it must reproduce common.G_matrix / pattern_vectors (checked in s0b)."""
import numpy as np, itertools, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
class Torus:
    def __init__(s, h1, h2, h3, r=0, p=0, q=0):
        s.h = (h1, h2, h3); s.r, s.p, s.q = r, p, q
        s.A = np.array([[h1, r, p], [0, h2, q], [0, 0, h3]])   # columns = periods
        s.V = h1*h2*h3
    def red(s, x):
        x = [int(v) for v in x]; h1, h2, h3 = s.h
        n3 = x[2] // h3; x = [x[0] - n3*s.p, x[1] - n3*s.q, x[2] - n3*h3]
        n2 = x[1] // h2; x = [x[0] - n2*s.r, x[1] - n2*h2, x[2]]
        n1 = x[0] // h1; x = [x[0] - n1*h1, x[1], x[2]]
        return tuple(x)
    def sidx(s, x):
        x = s.red(x); return (x[0]*s.h[1] + x[1])*s.h[2] + x[2]
    def sites(s):
        return list(itertools.product(range(s.h[0]), range(s.h[1]), range(s.h[2])))
    def G(s):
        V = s.V; G = np.zeros((3*V, 6*V), dtype=np.int64)
        for x in s.sites():
            s0 = s.sidx(x)
            for t in range(6):
                for (e, j), c in G_entries(x, t):
                    G[j*V + s.sidx(e), t*V + s0] += c
        return G
    def P(s):
        V = s.V; vecs = []
        for pat in PATTERNS:
            for x in s.sites():
                v = np.zeros(6*V, dtype=np.int64)
                for (d, t) in pat:
                    v[t*V + s.sidx(np.array(x) + np.array(d))] ^= 1
                vecs.append(v)
        return np.array(vecs)
    def kgrid(s):
        """reciprocal lattice: k with k.a_i in 2pi Z; returns all distinct k in first BZ-ish rep (as floats)"""
        B = 2*np.pi*np.linalg.inv(s.A).T   # columns b_j with a_i.b_j = 2pi delta
        ks = []
        for m in itertools.product(range(s.h[0]*s.h[1]*s.h[2]), repeat=1):
            pass
        return B
