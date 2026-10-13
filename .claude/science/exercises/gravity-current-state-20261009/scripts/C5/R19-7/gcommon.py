"""R19-7: anisotropic-torus generalisation of R18-1/R19-1 common.py (G_matrix, pattern_vectors) for Lx x Ly x Lz.
At Lx=Ly=Lz=L it must reproduce common.G_matrix(L) and common.pattern_vectors(L) exactly (checked in s0)."""
import numpy as np, itertools, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from common import *
def sidx(x, Ls):
    return (x[0]*Ls[1] + x[1])*Ls[2] + x[2]
def G_matrix_a(Ls):
    Ls = tuple(Ls); V = Ls[0]*Ls[1]*Ls[2]; G = np.zeros((3*V, 6*V), dtype=np.int64)
    for x in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])):
        s0 = sidx(x, Ls)
        for t in range(6):
            for (e, j), c in G_entries(x, t):
                e = tuple(int(v) % Ls[a] for a, v in enumerate(e)); ei = j*V + sidx(e, Ls)
                G[ei, t*V + s0] += c
    return G
def pattern_vectors_a(Ls):
    Ls = tuple(Ls); V = Ls[0]*Ls[1]*Ls[2]; vecs = []
    for p in PATTERNS:
        for x in itertools.product(range(Ls[0]), range(Ls[1]), range(Ls[2])):
            v = np.zeros(6*V, dtype=np.int64)
            for (d, t) in p:
                y = [(x[a] + d[a]) % Ls[a] for a in range(3)]
                v[t*V + sidx(y, Ls)] ^= 1
            vecs.append(v)
    return np.array(vecs)
