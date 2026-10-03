"""Symbol calculus for translation-invariant Clifford QCAs (mod 2).
Polynomial over F2 in z1,z2,z3 (Laurent): frozenset of exponent tuples.
M = [[fx, hx],[fz, hz]]: columns = alpha(X_0), alpha(Z_0).
"""
import numpy as np


def padd(a, b):
    return a ^ b


def pmul(a, b):
    out = set()
    for u in a:
        for v in b:
            w = (u[0] + v[0], u[1] + v[1], u[2] + v[2])
            if w in out:
                out.remove(w)
            else:
                out.add(w)
    return frozenset(out)


def mmul(A, B):
    return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def from_vecs(fvec, hvec, pts):
    fx = frozenset(v for i, v in enumerate(pts) if fvec[2 * i])
    fz = frozenset(v for i, v in enumerate(pts) if fvec[2 * i + 1])
    hx = frozenset(v for i, v in enumerate(pts) if hvec[2 * i])
    hz = frozenset(v for i, v in enumerate(pts) if hvec[2 * i + 1])
    return [[fx, hx], [fz, hz]]


def radius(M):
    r = 0
    for row in M:
        for p in row:
            for v in p:
                r = max(r, max(abs(c) for c in v))
    return r


def is_identity(M):
    one = frozenset([(0, 0, 0)])
    return M[0][0] == one and M[1][1] == one and not M[0][1] and not M[1][0]


def trace(M):
    return padd(M[0][0], M[1][1])


def orbit_stats(M, tmax=12):
    P = M
    radii = []
    order = None
    for t in range(1, tmax + 1):
        radii.append(radius(P))
        if is_identity(P):
            order = t
            break
        P = mmul(P, M)
    return order, radii
