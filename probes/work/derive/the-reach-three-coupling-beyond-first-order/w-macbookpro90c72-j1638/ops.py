"""Exact operators of blocks 54, 69, 72 on a torus of side L (Gaussian rationals via gq.V)."""
from fractions import Fraction as Fr
import itertools
import numpy as np
from gq import V, inner, sitedens

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
HALF = Fr(1, 2)


def fsh(f, m):
    """(f shifted)(x) = f(x + m)"""
    return np.roll(f, tuple(-x for x in m), axis=(0, 1, 2))


def mul(m, k): return tuple(k * x for x in m)


def S(a, p):   # (1/(2i)) [p(x+e_a) - p(x-e_a)]
    return (p.roll(E[a]) - p.roll(mul(E[a], -1))).scale((Fr(0), -HALF))


def C(a, p):
    return (p.roll(E[a]) + p.roll(mul(E[a], -1))).scale((HALF, Fr(0)))


def P(j, p):   # (1/(4i)) [p(x+2e_j) - p(x-2e_j)]
    return (p.roll(mul(E[j], 2)) - p.roll(mul(E[j], -2))).scale((Fr(0), Fr(-1, 4)))


def Cw(a, v, p):   # 1/2 [v(x) p(x+e_a) + v(x-e_a) p(x-e_a)]
    return (p.roll(E[a]).mulfield(v) + p.roll(mul(E[a], -1)).mulfield(fsh(v, mul(E[a], -1)))).scale((HALF, Fr(0)))


def C2w(j, v, p):  # 1/2 [v(x) p(x+2e_j) + v(x-2e_j) p(x-2e_j)]
    return (p.roll(mul(E[j], 2)).mulfield(v) + p.roll(mul(E[j], -2)).mulfield(fsh(v, mul(E[j], -2)))).scale((HALF, Fr(0)))


def Sw(a, w, p):   # (1/(2i)) [w(x) p(x+e_a) - w(x-e_a) p(x-e_a)]
    return (p.roll(E[a]).mulfield(w) - p.roll(mul(E[a], -1)).mulfield(fsh(w, mul(E[a], -1)))).scale((Fr(0), -HALF))


def d(a, f): return fsh(f, E[a]) - f
def d2(j, f): return fsh(f, mul(E[j], 2)) - f


def H(p):
    out = p.zero_like()
    for a in range(3):
        out = out + S(a, p).sigma(a)
    return out


def Vb(b, p):   # sum_{a,l} sigma_a 1/2 {C_a[b[a][l]], P_l}
    out = p.zero_like()
    for a in range(3):
        for l in range(3):
            t = Cw(a, b[a][l], P(l, p)) + P(l, Cw(a, b[a][l], p))
            out = out + t.scale((HALF, Fr(0))).sigma(a)
    return out


def H3(b, p): return H(p) + Vb(b, p)


def G(xi, p):   # sum_j 1/2 {xi_j, P_j}
    out = p.zero_like()
    for j in range(3):
        out = out + (P(j, p).mulfield(xi[j]) + P(j, p.mulfield(xi[j]))).scale((HALF, Fr(0)))
    return out


def icomm(X, Y, p):   # i[X, Y] p
    return (X(Y(p)) - Y(X(p))).times_i()
