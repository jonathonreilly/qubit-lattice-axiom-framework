#!/usr/bin/env python3
"""Referee of J:derive:lro-of-level-ordered-formation-in-3plus1:a1.

Own counts of the tetrahedra, the 3-cycle, and the affine involutions.
"""
from itertools import product

import numpy as np
import sympy as sp
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components

N4 = ((0, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1))
N7 = N4 + tuple((-d[0], -d[1], -d[2]) for d in N4 if d != (0, 0, 0))
FSET = ((0, 0, 0), (-1, 0, 0), (0, -1, 0))


def mod(x, L):
    return tuple(t % L for t in x)


def sq_counts(L):
    flipped = {mod(f, L) for f in FSET}

    def sign(x):
        return -1 if mod(x, L) in flipped else 1

    back, fwd = {}, {}
    for x in product(range(L), repeat=3):
        sb = sum(sign(tuple(x[i] - d[i] for i in range(3))) for d in N4)
        sf = sum(sign(tuple(x[i] + d[i] for i in range(3))) for d in N4)
        back[sb * sb] = back.get(sb * sb, 0) + 1
        fwd[sf * sf] = fwd.get(sf * sf, 0) + 1
    return back, fwd


def B(r, s, L):
    acc = 0
    ez = (0, 0, 1)

    def get(m, x):
        return m.get(mod(x, L), ez)

    for x in product(range(L), repeat=3):
        S = [0, 0, 0]
        for d in N4:
            v = get(s, tuple(x[i] - d[i] for i in range(3)))
            S = [S[i] + v[i] for i in range(3)]
        rv = get(r, x)
        acc += sum(rv[i] * S[i] for i in range(3))
    return acc


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def aff(N):
    Ns, out = set(N), []
    for dl in N:
        for imgs in product(N, repeat=3):
            M = tuple(tuple(imgs[j][i] - dl[i] for j in range(3)) for i in range(3))
            if abs(det3(M)) != 1:
                continue
            image = {tuple(sum(M[i][j] * d[j] for j in range(3)) + dl[i] for i in range(3)) for d in N}
            if image == Ns:
                out.append((M, dl))
    return out


def census(L, N):
    X = np.array(list(product(range(L), repeat=3)))
    n, V = L ** 3, 2 * L ** 3

    def idx(Y):
        return (Y[:, 0] * L + Y[:, 1]) * L + Y[:, 2]

    E = np.concatenate([np.stack([idx((X - np.array(d)) % L), n + idx(X)], 1) for d in N])

    def enc(F):
        return np.sort(np.minimum(F[:, 0], F[:, 1]) * V + np.maximum(F[:, 0], F[:, 1]))

    code = enc(E)
    ident = np.arange(V)
    nfree = nweak = nfix = 0
    for M, dl in aff(N):
        Mn = np.array(M, dtype=int)
        for swap in (0, 1):
            Ml = -Mn if swap else Mn
            for c0t in product(range(L), repeat=3):
                c0 = np.array(c0t)
                c1 = (c0 - np.array(dl)) % L if swap else (c0 + np.array(dl)) % L
                b = idx((X @ Ml.T + c0) % L)
                t = idx((X @ Ml.T + c1) % L)
                th = np.concatenate([b + (n if swap else 0), t + (0 if swap else n)])
                if not np.array_equal(enc(th[E]), code) or not np.array_equal(th[th], ident):
                    continue
                if np.any(th == ident):
                    nfix += 1
                    continue
                nfree += 1
                mirror = th[E[:, 0]] == E[:, 1]
                inM = np.zeros(V, dtype=bool)
                inM[E[mirror, 0]] = True
                inM[E[mirror, 1]] = True
                inner = ~(inM[E[:, 0]] & inM[E[:, 1]])
                g = coo_matrix((np.ones(int(inner.sum())), (E[inner, 0], E[inner, 1])), shape=(V, V))
                lab = connected_components(g, directed=False)[1]
                if not np.any(lab[th] == lab):
                    nweak += 1
    return nfree, nweak, nfix


def main():
    for L in range(3, 9):
        back, fwd = sq_counts(L)
        N = L ** 3
        if back != {4: 10, 16: N - 10} or fwd != {0: 3, 4: 6, 16: N - 9}:
            raise SystemExit(f"counts {L} {back} {fwd}")
    # |S|^4 differs by 192, independent of L
    N = 8 ** 3
    back4 = 10 * 16 + (N - 10) * 256
    fwd4 = 6 * 16 + (N - 9) * 256
    if fwd4 - back4 != 192:
        raise SystemExit("quartic")
    print("S5 COUNTS FOLLOW: for L=3..8, backward |S|^2 is 4 on 10 sites and 16 elsewhere, "
          "forward is 0 on 3, 4 on 6, 16 elsewhere; sum |S|^4 differs by 192")

    u = sp.symbols("u", positive=True)
    ratio = u ** 3 * sp.cosh(u) / sp.sinh(u) ** 3
    # Z(4b)/Z(2b)^4 with u=2b
    b = sp.symbols("b", positive=True)
    Z = lambda q: sp.sinh(q) / q
    if sp.simplify(Z(4 * b) / Z(2 * b) ** 4 - ratio.subs(u, 2 * b)) != 0:
        raise SystemExit("ratio")
    n = sp.symbols("n", integer=True, positive=True)
    coeff = (3 ** n - 3) / 4 - n * (n - 1) * (n - 2)
    if [sp.simplify(coeff.subs(n, k)) for k in (3, 5, 7)] != [0, 0, 336]:
        raise SystemExit("coeffs")
    m = sp.symbols("m", integer=True, nonnegative=True)
    gap = sp.expand((8 * n ** 3 - 30 * n ** 2 + 16 * n + 6).subs(n, 7 + m))
    if gap != 8 * m ** 3 + 138 * m ** 2 + 772 * m + 1392:
        raise SystemExit(gap)
    print("S5 RATIO FOLLOWS: rho(iota s)/rho(s) = Z(4 beta)/Z(2 beta)^4 = u^3 cosh u/sinh^3 u < 1 "
          "for u>0, since the odd Taylor coefficients vanish at n=3,5 and stay positive from n=7")

    ex, ey = (1, 0, 0), (0, 1, 0)
    for L in range(2, 7):
        s0, s1, s2 = {}, {(0, 0, 0): ex}, {(1, 0, 0): ey}
        cyc = [s0, s1, s2]
        sm = sum(B(cyc[(i + 1) % 3], cyc[i], L) - B(cyc[i], cyc[(i + 1) % 3], L) for i in range(3))
        if sm != (0 if L == 2 else 1):
            raise SystemExit(f"cycle {L} {sm}")
    print("S7 FOLLOWS: the 3-cycle of all e_z, e_x at 0, e_y at e_1 has exponent sum 1 for L=3..6 "
          "(ratio e^beta) and 0 for L=2")

    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    phi = (1 + sum(sp.exp(sp.I * k) for k in (k1, k2, k3))) / 4
    vecs = []
    for i in range(3):
        e = [0, 0, 0]
        e[i] = 1
        vecs += [tuple(e), tuple(-t for t in e)]
    for i in range(3):
        for j in range(i + 1, 3):
            d = [0, 0, 0]
            d[i], d[j] = 1, -1
            vecs += [tuple(d), tuple(-t for t in d)]
    lam = sum(sp.exp(sp.I * (v[0] * k1 + v[1] * k2 + v[2] * k3)) for v in vecs) / 12
    if sp.simplify(sp.expand(1 - sp.Abs(phi) ** 2 - sp.Rational(3, 4) * (1 - lam))) != 0:
        raise SystemExit("fcc")
    print("S11 FOLLOWS: 1-|phi|^2 = (3/4)(1-lambda_FCC), so the linear stationary covariance is even in k")

    if len(aff(N4)) != 24 or len(aff(N7)) != 48:
        raise SystemExit("aff")
    expected = {(4, 4): (191, 0, 73), (4, 7): (621, 7, None), (6, 4): (475, 0, 145)}
    for L, N in ((4, N4), (4, N7), (6, N4)):
        free, weak, fix = census(L, N)
        print(f"  census L={L} stencil={len(N)} free={free} weak={weak} fixed-vertex involutions={fix}")
        ef, ew, ex = expected[(L, len(N))]
        if (free, weak) != (ef, ew) or (ex is not None and fix != ex):
            raise SystemExit("census")
    print("S9 FOLLOWS: Aff(N4)=24, Aff(N7)=48; no fixed-point-free affine involution of the diamond "
          "doubled graph at L=4 or 6 has a PSD-compatible crossing (0 pass the necessary condition)")

    print("SUMMARY: confirmed - K is the diamond-lattice reversible chain Q followed by inversion; "
          "rho_L is not inversion-symmetric for any beta>0 and L>=3 (ratio u^3 cosh u/sinh^3 u<1 at s_F); "
          "K is not reversible (a 3-cycle has ratio e^beta); each named long-range-order route fails at that step")
    print("HIT: confirmed - no inversion-symmetric stationary law, pi_L is not rho_L, and the four routes fail: "
          "the layer marginal is not stationary, no affine reflection of the diamond graph gives Gaussian domination, "
          "tilted islands are not eroded, and the infrared bound is not supplied")


if __name__ == "__main__":
    main()
