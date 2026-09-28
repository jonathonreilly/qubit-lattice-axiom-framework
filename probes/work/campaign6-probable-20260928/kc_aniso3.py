"""Symbolic Bloch determinant for J = (Jx, Jy, Jz) and kappa."""
import sys
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import sympy as sp
import k3_lib as K
from sympy.polys.matrices import DomainMatrix
z1, z2, w, kk, Jx, Jy, Jz = sp.symbols("z1 z2 w k Jx Jy Jz")
S = 2
_T0 = K.terms((1.0, 1.0, 1.0), 0.3); _Tx = K.terms((1.5, 1.0, 1.0), 0.3); _Ty = K.terms((1.0, 1.5, 1.0), 0.3); _Tz = K.terms((1.0, 1.0, 1.5), 0.3)
KIND = []
for t0, tx, ty, tz in zip(_T0, _Tx, _Ty, _Tz):
    if abs(t0[3] - 2) > 1e-12:
        KIND.append("odd")
    elif abs(tx[3] - 2) > 1e-12:
        KIND.append("x")
    elif abs(ty[3] - 2) > 1e-12:
        KIND.append("y")
    else:
        KIND.append("z")
TERMS = [(a, b, n, kd) for (a, b, n, _), kd in zip(_T0, KIND)]
AMP = {"x": 2 * Jx, "y": 2 * Jy, "z": 2 * Jz, "odd": 2 * kk}


def Dsym(sub=None):
    sub = sub or {}
    Ms = [[sp.Integer(0)] * 4 for _ in range(4)]
    for (a, b, n, kd) in TERMS:
        tt = sp.sympify(AMP[kd]).subs(sub)
        e = [int(x) for x in n]
        Ms[int(a)][int(b)] += tt * z1 ** (S + e[0]) * z2 ** (S + e[1]) * w ** (S + e[2])
        Ms[int(b)][int(a)] -= tt * z1 ** (S - e[0]) * z2 ** (S - e[1]) * w ** (S - e[2])
    gens = [g for g in (kk, Jx, Jy, Jz) if g not in sub] + [z1, z2, w]
    R = sp.QQ[gens]
    return sp.expand(R.to_sympy(DomainMatrix([[R.from_sympy(sp.expand(x)) for x in r] for r in Ms], (4, 4), R).det()) / (z1 * z2 * w) ** (4 * S))
