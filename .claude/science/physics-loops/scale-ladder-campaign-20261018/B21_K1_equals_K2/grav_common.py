"""gravity objects, built fresh with sympy Functions."""
from __future__ import annotations
import sympy as sp
from fourier_core import X, Fn, vd, I

COMP = [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]
HF = {ab: Fn(f"h{ab[0]}{ab[1]}") for ab in COMP}
PF = {ab: Fn(f"P{ab[0]}{ab[1]}") for ab in COMP}
NF = Fn("N")
XIF = [Fn(f"xi{k}") for k in range(3)]
e = sp.Symbol("e")
D = lambda f, k: sp.diff(f, X[k])


def h(i, j):
    return HF[(min(i, j), max(i, j))]


def series2(expr, n=2):
    expr = sp.expand(expr)
    return sum(expr.coeff(e, k) * e ** k for k in range(n + 1))


def sqrtgR():
    H = sp.Matrix(3, 3, lambda i, j: h(i, j))
    g = sp.eye(3) + e * H
    gi = sp.eye(3) - e * H + e ** 2 * H * H
    trh = H.trace()
    sg = 1 + e * trh / 2 + e ** 2 * (trh ** 2 / 8 - (H * H).trace() / 4)
    dg = [[[sp.diff(g[i, j], X[k]) for k in range(3)] for j in range(3)] for i in range(3)]
    # Gamma^k_ij
    Gam = [[[series2(sum(gi[k, l] * (dg[l][i][j] + dg[l][j][i] - dg[i][j][l]) for l in range(3)) / 2)
             for j in range(3)] for i in range(3)] for k in range(3)]
    R = 0
    for i in range(3):
        for j in range(3):
            Rij = sum(sp.diff(Gam[k][i][j], X[k]) - sp.diff(Gam[k][i][k], X[j]) for k in range(3))
            Rij += sum(Gam[k][k][l] * Gam[l][i][j] - Gam[k][j][l] * Gam[l][i][k] for k in range(3) for l in range(3))
            R += gi[i, j] * series2(Rij)
    out = series2(sg * series2(R))
    return sp.expand(out.coeff(e, 1)), sp.expand(out.coeff(e, 2))


def kin(al):
    pd = [PF[(j, j)] for j in range(3)]
    tr = sum(pd)
    return (sum(p ** 2 for p in pd) - tr ** 2 / 2) / (4 * al) + sum(PF[ab] ** 2 for ab in COMP[3:]) / (8 * al)


def ft(expr, mom):
    """plane-wave substitution: mom maps function-name -> (amplitude symbol, k triple). Linear-in-each-slot use only."""
    def rep_der(d):
        f = d.expr
        a, k = mom[f.func.__name__]
        fac = a
        for v, n in d.variable_count:
            fac *= (I * k[X.index(v)]) ** n
        return fac
    ex = sp.expand(expr).replace(lambda a: isinstance(a, sp.Derivative), rep_der)
    ex = ex.replace(lambda a: isinstance(a, sp.core.function.AppliedUndef) and a.func.__name__ in mom,
                    lambda a: mom[a.func.__name__][0])
    return sp.expand(ex)


def load_R12(path="R12.pkl"):
    """[sqrt g R]^(1), ^(2): cached pickle, rebuilt (~4 s) if absent."""
    import os, pickle
    if os.path.exists(path):
        return pickle.load(open(path, "rb"))
    R = sqrtgR()
    pickle.dump(R, open(path, "wb"))
    return R
