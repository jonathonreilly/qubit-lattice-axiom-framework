#!/usr/bin/env python3
"""Referee of J:derive:the-travelling-disturbances-source-by-species:a1.

Exact Gaussian rationals on the 4^3 torus. Does not import the author's check.
"""
from fractions import Fraction as F
from itertools import product

import sympy as sp

L = 4
SITES = list(product(range(L), repeat=3))
IDX = {s: i for i, s in enumerate(SITES)}
# Pauli matrices over Gaussian rationals (re, im)
SX = [[(F(0), F(0)), (F(1), F(0))], [(F(1), F(0)), (F(0), F(0))]]
SY = [[(F(0), F(0)), (F(0), F(-1))], [(F(0), F(1)), (F(0), F(0))]]
SZ = [[(F(1), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(-1), F(0))]]
SG = [SX, SY, SZ]
Z = (F(0), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def smul(a, s):
    return (a[0] * s, a[1] * s)


def conj(a):
    return (a[0], -a[1])


def re(a):
    return a[0]


def dot(u, v):
    return add(mul(conj(u[0]), v[0]), mul(conj(u[1]), v[1]))


def apply_sigma(M, spin):
    return [add(mul(M[a][0], spin[0]), mul(M[a][1], spin[1])) for a in range(2)]


def shift(x, a, s):
    y = list(x)
    y[a] = (y[a] + s) % L
    return tuple(y)


def apply_S(psi, j):
    out = [None] * len(SITES)
    for x in SITES:
        # (psi(x+e) - psi(x-e)) / (2i) = -i/2 * (psi(x+e) - psi(x-e))
        d = [add(psi[IDX[shift(x, j, 1)]][a], smul(psi[IDX[shift(x, j, -1)]][a], F(-1))) for a in range(2)]
        out[IDX[x]] = [smul(mul((F(0), F(-1)), d[a]), F(1, 2)) for a in range(2)]
    return out


def apply_C(psi, j):
    out = [None] * len(SITES)
    for x in SITES:
        d = [add(psi[IDX[shift(x, j, 1)]][a], psi[IDX[shift(x, j, -1)]][a]) for a in range(2)]
        out[IDX[x]] = [smul(d[a], F(1, 2)) for a in range(2)]
    return out


def apply_H(psi):
    out = [[Z, Z] for _ in SITES]
    for j in range(3):
        sj = apply_S(psi, j)
        for i, spin in enumerate(sj):
            got = apply_sigma(SG[j], spin)
            out[i] = [add(out[i][a], got[a]) for a in range(2)]
    return out


def responses(psi):
    th, J, K, pi, P = {}, {}, {}, {}, {}
    Spsi = [apply_S(psi, j) for j in range(3)]
    Ppsi = []
    for j in range(3):
        sj = Spsi[j]
        cj = apply_C(sj, j)  # C_j S_j , since P = S C = C S on Fourier modes; use S then C
        # P_j = S_j C_j. Apply C first then S.
        Ppsi.append(apply_S(apply_C(psi, j), j))
    for a in range(3):
        for j in range(3):
            th[(a, j)] = []
            J[(a, j)] = []
            K[(a, j)] = []
            for i, x in enumerate(SITES):
                th[(a, j)].append(re(dot(psi[i], apply_sigma(SG[a], Spsi[j][i]))))
                y = IDX[shift(x, a, 1)]
                J[(a, j)].append(F(1, 2) * (
                    re(dot(psi[y], apply_sigma(SG[a], Spsi[j][i])))
                    + re(dot(Spsi[j][y], apply_sigma(SG[a], psi[i])))))
                K[(a, j)].append(F(1, 2) * (
                    re(dot(psi[y], apply_sigma(SG[a], Ppsi[j][i])))
                    + re(dot(Ppsi[j][y], apply_sigma(SG[a], psi[i])))))
    for j in range(3):
        pi[j] = [re(dot(psi[i], Spsi[j][i])) for i in range(len(SITES))]
        P[j] = [re(dot(psi[i], Ppsi[j][i])) for i in range(len(SITES))]
    He = apply_H(psi)
    e = [re(dot(psi[i], He[i])) for i in range(len(SITES))]
    return th, J, K, pi, P, e


def main():
    # one deterministic Gaussian-integer state
    psi = []
    for i, x in enumerate(SITES):
        psi.append([((F(1 + x[0] - x[1]), F(x[2] - 1)), (F(x[1] - 2), F(1 - x[0])))])
        psi[-1] = psi[-1][0]
    th0, J0, K0, pi0, P0, e0 = responses(psi)
    for nv in product((0, 1), repeat=3):
        D = [(-1) ** t for t in nv]
        s_n = D[0] * D[1] * D[2]
        rho = [s_n * d for d in D]
        # R with R sigma R^dag = rho sigma
        if rho == [1, 1, 1]:
            R = [[(F(1), F(0)), Z], [Z, (F(1), F(0))]]
        else:
            a = rho.index(1)
            R = [[mul((F(0), F(1)), SG[a][r][c]) for c in range(2)] for r in range(2)]
        for a in range(3):
            got = [[Z, Z], [Z, Z]]
            # R sigma R^dag. R^dag = conj transpose
            Rd = [[conj(R[c][r]) for c in range(2)] for r in range(2)]
            mid = [[Z, Z], [Z, Z]]
            for r in range(2):
                for c in range(2):
                    mid[r][c] = add(mul(SG[a][r][0], Rd[0][c]), mul(SG[a][r][1], Rd[1][c]))
            for r in range(2):
                for c in range(2):
                    got[r][c] = add(mul(R[r][0], mid[0][c]), mul(R[r][1], mid[1][c]))
            if got != [[smul(SG[a][r][c], rho[a]) for c in range(2)] for r in range(2)]:
                raise SystemExit(f"coin map {nv} {a}")
        mapped = []
        for i, x in enumerate(SITES):
            sign = (-1) ** (nv[0] * x[0] + nv[1] * x[1] + nv[2] * x[2])
            mapped.append([smul(apply_sigma(R, psi[i])[a], sign) for a in range(2)])
        th, J, K, pi, P, e = responses(mapped)
        for a in range(3):
            for j in range(3):
                if th[(a, j)] != [s_n * D[a] * D[j] * v for v in th0[(a, j)]]:
                    raise SystemExit("theta")
                if J[(a, j)] != [s_n * D[j] * v for v in J0[(a, j)]]:
                    raise SystemExit("J")
                if K[(a, j)] != [s_n * v for v in K0[(a, j)]]:
                    raise SystemExit("K")
        for j in range(3):
            if pi[j] != [D[j] * v for v in pi0[j]]:
                raise SystemExit("pi")
            if P[j] != P0[j]:
                raise SystemExit("P")
        if e != [s_n * v for v in e0]:
            raise SystemExit("energy")
    print("S1 FOLLOWS: on one Gaussian-integer state of the 4^3 torus, all eight species maps send "
          "Theta to s_n D_a D_j Theta, J to s_n D_j J, K to s_n K, e to s_n e, pi_j to D_j pi_j, and P_j to itself")

    Kc = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"K{min(i,j)}{max(i,j)}"))
    for nv in product((0, 1), repeat=3):
        D = [(-1) ** t for t in nv]
        Dm = sp.diag(*D)
        Th = sp.simplify(Dm * Kc * Dm)
        Js = sp.simplify((Kc * Dm + (Kc * Dm).T) / 2)
        for c in range(3):
            a, b = [x for x in range(3) if x != c]
            plus = (Kc[a, a] - Kc[b, b]) / 2
            cross = Kc[a, b]
            Da, Db = D[a], D[b]
            frame_p = sp.simplify((Th[a, a] - Th[b, b]) / 2 / plus)
            frame_x = sp.simplify(Th[a, b] / cross)
            if frame_p != 1 or frame_x != Da * Db:
                raise SystemExit("frame table")
            two_p = sp.simplify((Js[a, a] - Js[b, b]) / 2)
            two_x = sp.simplify(Js[a, b] / cross)
            if Da == Db:
                if sp.simplify(two_p / plus - Da) != 0 or two_x != Da:
                    raise SystemExit("reach two equal")
            else:
                trace = Da * (Kc[a, a] + Kc[b, b]) / 2
                if sp.simplify(two_p - trace) != 0 or two_x != 0:
                    raise SystemExit("reach two unequal")
    print("S2 FOLLOWS: relative to the species' own K, frame + is 1 and x is (-1)^(n_a+n_b); "
          "reach two is D_a for both polarisations when n_a=n_b, and when n_a!=n_b the x source is 0 "
          "and the + source is the transverse trace; reach three is +1 because K and e pick up the same s_n")

    k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
    ks = (k1, k2, k3)
    Hk = sum((sp.Matrix([[0, 1], [1, 0]]) * sp.sin(ks[0]),
              sp.Matrix([[0, -sp.I], [sp.I, 0]]) * sp.sin(ks[1]),
              sp.Matrix([[1, 0], [0, -1]]) * sp.sin(ks[2])), sp.zeros(2))
    # rebuild cleanly
    Ssym = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    Hk = sum((Ssym[a] * sp.sin(ks[a]) for a in range(3)), sp.zeros(2))
    E2 = sum(sp.sin(k) ** 2 for k in ks)
    if sp.simplify(Hk * Hk - E2 * sp.eye(2)) != sp.zeros(2):
        raise SystemExit("H^2")
    E = sp.sqrt(E2)
    Proj = (sp.eye(2) + Hk / E) / 2
    for a in range(3):
        if sp.simplify(sp.trace(Proj * Ssym[a]) - sp.sin(ks[a]) / E) != 0:
            raise SystemExit("hellmann")
    q1, q2 = sp.symbols("q1 q2", real=True)
    for n1, n2 in product((0, 1), repeat=2):
        ka, kj = sp.pi * n1 + q1, sp.pi * n2 + q2
        Kaj = sp.sin(ka) * sp.cos(ka) * sp.sin(kj) * sp.cos(kj)
        if sp.simplify(Kaj - sp.sin(2 * q1) * sp.sin(2 * q2) / 4) != 0:
            raise SystemExit("K species")
        Thaj = sp.sin(ka) * sp.sin(kj)
        if sp.simplify(Thaj - (-1) ** (n1 + n2) * sp.sin(q1) * sp.sin(q2)) != 0:
            raise SystemExit("theta sign")
    ser = sp.series(sp.sin(2 * q1) * sp.sin(2 * q2) / 4, q1, 0, 4).removeO()
    ser = sp.series(ser, q2, 0, 4).removeO()
    lead = sp.expand((q1 - sp.Rational(2, 3) * q1 ** 3) * (q2 - sp.Rational(2, 3) * q2 ** 3))
    if sp.expand(ser - lead) != 0:
        raise SystemExit("series")
    print("S3 FOLLOWS: K_a^j = sin(2q_a) sin(2q_j)/(4E) with no species sign, and Theta keeps D_a D_j; "
          "the first lattice correction is -(2/3)(q_a^2+q_j^2)")

    p3, Kf, wb = sp.symbols("p3 K wbar", positive=True)
    hp, h12 = sp.symbols("hp h12", real=True)
    h = sp.Matrix([[hp, h12, 0], [h12, -hp, 0], [0, 0, 0]])
    pv = sp.Matrix([0, 0, p3])
    p2 = p3 ** 2
    R1 = -((pv.T * h * pv)[0] - p2 * h.trace())
    ph = h * pv
    R2 = (-sp.Rational(1, 4) * p2 * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
          + sp.Rational(1, 2) * (ph.T * ph)[0]
          - sp.Rational(1, 2) * (pv.T * h * pv)[0] * h.trace()
          + sp.Rational(1, 4) * p2 * h.trace() ** 2)
    F2 = -Kf * wb * R2
    want = Kf * wb * p3 ** 2 * (hp ** 2 + h12 ** 2) / 2
    if sp.simplify(R1) != 0 or sp.simplify(F2 - want) != 0:
        raise SystemExit("TT energy")
    print("S4 FOLLOWS: a TT disturbance along e_3 has R1=0 and F2=(K wbar/4) p^2 h_ij h_ij >= 0, "
          "so with alpha>0 the free TT energy is positive and a species sign squares away in the radiated energy")
    print("SUMMARY: confirmed - the TT source per unit of a species' own stress is species-blind for + under the "
          "frame and (-1)^(n_a+n_b) for x; under reach two it is D_a for both polarisations when n_a=n_b, and when "
          "n_a!=n_b the x source vanishes and + becomes the transverse trace; reach three is +1 for all eight, with "
          "K=sin(2q_a)sin(2q_j)/(4E); pi_j flips with D_j and P_j does not; for alpha>0 no species gains energy by radiating")
    print("HIT: confirmed - frame, reach-two and reach-three TT source tables, the two momentum books, and the "
          "positive TT energy (K wbar/4) p^2 h^2, so a reflected species does not gain energy by emitting when alpha>0")


if __name__ == "__main__":
    main()
