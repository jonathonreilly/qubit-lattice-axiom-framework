import sys
sys.path.insert(0, ".")
import numpy as np, sympy as sp, mpmath as mpm
import k3_lib as K
from sympy.polys.matrices import DomainMatrix
z1, z2, w, kk, JJ = sp.symbols("z1 z2 w k J")
S = 2


def Dsym():
    T = K.terms((1.0, 1.0, 1.5), 0.3); T1 = K.terms((1.0, 1.0, 1.0), 0.3)
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, t), (a1, b1, n1, t1) in zip(T, T1):
        tt = (sp.Integer(2) if abs(t - 2.0) < 1e-12 else 2 * JJ) if abs(t1 - 2.0) < 1e-12 else 2 * kk
        e = [int(x) for x in n]
        Ms[a][b] += tt * z1 ** (S + e[0]) * z2 ** (S + e[1]) * w ** (S + e[2])
        Ms[b][a] -= tt * z1 ** (S - e[0]) * z2 ** (S - e[1]) * w ** (S - e[2])
    R = sp.QQ[kk, JJ, z1, z2, w]
    return sp.expand(R.to_sympy(DomainMatrix([[R.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), R).det()) / (z1 * z2 * w) ** (4 * S)), Ms
