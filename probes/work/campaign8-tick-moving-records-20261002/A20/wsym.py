"""w-coordinate construction of S3-equivariant SL2(F2[w]) symbols and conversion to z (Laurent) form.
w_i = z_i + 1/z_i. Label basis (bx,bz): X=(1,0), Z=(0,1). M columns = alpha(X_0), alpha(Z_0).
"""
import itertools
from math import comb
import sympy as sp

w1, w2, w3 = sp.symbols("w1 w2 w3")
W = (w1, w2, w3)
GF2 = dict(modulus=2)


def P2(e):
    return sp.Poly(sp.expand(e), *W, modulus=2)


def mat2(Mx):
    return [[P2(Mx[i][j]) for j in range(2)] for i in range(2)]


def construct(N0):
    u0 = (w1 + w2, w2 + w3)
    P = [[u0[0], u0[0] ** 2], [u0[1], u0[1] ** 2]]
    Delta = sp.expand(P[0][0] * P[1][1] + P[0][1] * P[1][0])
    adj = [[P[1][1], P[0][1]], [P[1][0], P[0][0]]]   # char 2: no signs
    N = [[N0[i][j].subs("D", Delta) if hasattr(N0[i][j], "subs") else N0[i][j] for j in range(2)] for i in range(2)]
    PN = [[sum(P[i][k] * N[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    PNA = [[sum(PN[i][k] * adj[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    M = [[(1 if i == j else 0) + PNA[i][j] for j in range(2)] for i in range(2)]
    return mat2(M), P2(Delta)


def permute(poly, p):
    e = poly.as_expr().subs({W[0]: W[p[0]], W[1]: W[p[1]], W[2]: W[p[2]]}, simultaneous=True)
    return P2(e)


G_TAU = ((1, 1), (0, 1))   # axes y<->z, labels Y<->Z : (a,b)->(a+b,b)
G_C = ((1, 1), (1, 0))     # axes x->y->z, labels X->Y->Z : (a,b)->(a+b,a)


def equivariant(M):
    """check M(w) = g M(sigma^{-1} w) g^{-1} for tau=(23) and the 3-cycle (w->(w2,w3,w1) substitution)."""
    ok = True
    for g, p in [(G_TAU, (0, 2, 1)), (G_C, (1, 2, 0))]:
        Mp = [[permute(M[i][j], p) for j in range(2)] for i in range(2)]
        # g^{-1}: for tau g^{-1}=g; for c, g^{-1} = g^2 = ((0,1),(1,1))
        gi = g if g == G_TAU else ((0, 1), (1, 1))
        prod = [[None] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                acc = P2(0)
                for k in range(2):
                    for l in range(2):
                        if g[i][k] and gi[l][j]:
                            acc = acc + Mp[k][l]
                prod[i][j] = acc
        ok &= all((prod[i][j] - M[i][j]).is_zero for i in range(2) for j in range(2))
    return ok


def to_z(poly):
    """F2[w] -> set of z-exponents (Laurent), w_i^k = sum_j C(k,j) z_i^{k-2j}."""
    out = set()
    for mon, c in poly.terms():
        if int(c) % 2 == 0:
            continue
        factors = []
        for k in mon:
            factors.append([k - 2 * j for j in range(k + 1) if comb(k, j) % 2 == 1])
        for v in itertools.product(*factors):
            if v in out:
                out.remove(v)
            else:
                out.add(v)
    return frozenset(out)


def Mz(M):
    return [[to_z(M[i][j]) for j in range(2)] for i in range(2)]
