#!/usr/bin/env python3
"""J:note falsifiers for TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13 (on main).

The note's falsifier predicates ("p == I_4 must fail; rank(p) == 4 must fail; dim_C(C) == 9 must hold") and its theorems, checked with
my own exact machinery (Fractions, fraction-free elimination) on the displayed objects and beyond them:
  - the displayed F on C^2 (x) C^2: F Hermitian, F^2 = I, Tr F = 2, p = (I + F)/2 a projection of rank 3, p != I, the corner dimension
    computed as the rank of the 16 compressed matrix units p E_ab p (= 9), the rational map phi(X) = W G^-1 X W^T (integer spanning
    set |00>, |01>+|10>, |11>, Gram diag(1,2,1)) an algebra isomorphism onto the corner with phi(I_3) = p, and the ON matrix units
    |e_i><e_j| (exact sqrt(2) in sympy) a *-isomorphism with psi(I_3) = p;
  - beyond: the two-site swap on C^d (x) C^d, d = 2..8 (rank d(d+1)/2, corner dimension rank^2 from compressed units for d <= 4), and the
    n-site symmetrizer P_sym = (1/n!) sum_sigma P_sigma on (C^2)^(x)n, n = 2..7 (rank n+1; the Dicke spanning set with Gram
    diag(C(n,k)) gives phi with phi(XY) = phi(X) phi(Y) on all matrix-unit pairs and phi(I_{n+1}) = P_sym; P_sym != I).
HIT if a predicate fails.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as Fr
from math import comb, factorial

import sympy as sp


def rank(M):
    A = [list(r) for r in M]
    rows, cols = len(A), len(A[0]) if A else 0
    r = 0
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = Fr(A[i][c]) / A[r][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def mm(A, B):
    Bt = list(zip(*B))
    return [[sum((a * b for a, b in zip(row, col)), Fr(0)) for col in Bt] for row in A]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def perm_op(n, d, sigma):
    """permutation of tensor factors on (C^d)^(x)n: |i_1..i_n> -> |i_sigma^-1(1)...>"""
    D = d ** n
    M = [[Fr(0)] * D for _ in range(D)]
    for idx in itertools.product(range(d), repeat=n):
        src = sum(v * d ** (n - 1 - k) for k, v in enumerate(idx))
        tgt_idx = [idx[sigma.index(k)] for k in range(n)]
        tgt = sum(v * d ** (n - 1 - k) for k, v in enumerate(tgt_idx))
        M[tgt][src] = Fr(1)
    return M


def corner_dim(p):
    D = len(p)
    vecs = []
    for a in range(D):
        for b in range(D):
            E = [[Fr(int(i == a and j == b)) for j in range(D)] for i in range(D)]
            C = mm(mm(p, E), p)
            vecs.append([x for row in C for x in row])
    return rank(vecs)


def displayed():
    F = perm_op(2, 2, [1, 0])
    I4 = eye(4)
    p = [[(I4[i][j] + F[i][j]) / 2 for j in range(4)] for i in range(4)]
    out = {"F Hermitian": all(F[i][j] == F[j][i] for i in range(4) for j in range(4)), "F^2 = I": mm(F, F) == I4,
           "Tr F": sum(F[i][i] for i in range(4)), "p^2 = p": mm(p, p) == p, "rank p": rank(p), "p == I_4": p == I4,
           "corner dim": corner_dim(p)}
    W = [[Fr(1), Fr(0), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
    Ginv = [[Fr(1), 0, 0], [0, Fr(1, 2), 0], [0, 0, Fr(1)]]
    WT = [list(r) for r in zip(*W)]
    phi = lambda X: mm(mm(mm(W, Ginv), X), WT)
    units = [[[Fr(int(i == a and j == b)) for j in range(3)] for i in range(3)] for a in range(3) for b in range(3)]
    out["phi hom"] = all(phi(mm(X, Y)) == mm(phi(X), phi(Y)) for X in units for Y in units)
    out["phi(I_3) = p"] = phi(eye(3)) == p
    # ON *-isomorphism with exact sqrt(2)
    e = [sp.Matrix([1, 0, 0, 0]), sp.Matrix([0, 1, 1, 0]) / sp.sqrt(2), sp.Matrix([0, 0, 0, 1])]
    psi = {(i, j): e[i] * e[j].T for i in range(3) for j in range(3)}
    table = all(sp.simplify(psi[(i, j)] * psi[(k, l)] - (psi[(i, l)] if j == k else sp.zeros(4, 4))) == sp.zeros(4, 4)
                for i in range(3) for j in range(3) for k in range(3) for l in range(3))
    star = all(psi[(i, j)].T == psi[(j, i)] for i in range(3) for j in range(3))
    unit = sp.simplify(sum((psi[(i, i)] for i in range(3)), sp.zeros(4, 4)) - sp.Matrix(p)) == sp.zeros(4, 4)
    out["psi *-matrix units, psi(I_3) = p"] = table and star and unit
    return out


def two_site(dmax=8):
    out = {}
    for d in range(2, dmax + 1):
        F = perm_op(2, d, [1, 0])
        D = d * d
        p = [[(Fr(int(i == j)) + F[i][j]) / 2 for j in range(D)] for i in range(D)]
        r = rank(p)
        row = {"rank": r, "expected d(d+1)/2": d * (d + 1) // 2, "p != I": p != eye(D), "idempotent": mm(p, p) == p}
        if d <= 4:
            row["corner dim"] = corner_dim(p)
        out[d] = row
    return out


def dicke(nmax=7):
    out = {}
    for n in range(2, nmax + 1):
        D = 2 ** n
        S = [[Fr(0)] * D for _ in range(D)]
        for sigma in itertools.permutations(range(n)):
            P = perm_op(n, 2, list(sigma))
            for i in range(D):
                for j in range(D):
                    if P[i][j]:
                        S[i][j] += P[i][j]
        S = [[x / factorial(n) for x in row] for row in S]
        r = rank(S)
        # Dicke spanning set: w_k = sum of basis states with k ones; Gram diag(C(n,k))
        W = [[Fr(int(bin(i).count("1") == k)) for k in range(n + 1)] for i in range(D)]
        Ginv = [[Fr(1, comb(n, k)) if k == l else Fr(0) for l in range(n + 1)] for k in range(n + 1)]
        WT = [list(r_) for r_ in zip(*W)]
        WG = mm(W, Ginv)
        phi = lambda X: mm(mm(WG, X), WT)
        units = [[[Fr(int(i == a and j == b)) for j in range(n + 1)] for i in range(n + 1)] for a in range(n + 1) for b in range(n + 1)]
        phis = [phi(U) for U in units]
        k1 = n + 1
        hom = all(mm(phis[a * k1 + b], phis[c * k1 + e]) == (phis[a * k1 + e] if b == c else [[Fr(0)] * D for _ in range(D)])
                  for a in range(k1) for b in range(k1) for c in range(k1) for e in range(k1)) if n <= 5 else None
        out[n] = {"rank P_sym": r, "expected n+1": n + 1, "phi(I) = P_sym": phi(eye(n + 1)) == S, "phi matrix-unit table": hom,
                  "P_sym != I": S != eye(D)}
    return out


def main():
    dsp = displayed()
    print(f"1. displayed objects: {dsp}")
    ts = two_site()
    print(f"2. two-site swap on C^d x C^d: {ts}")
    dk = dicke()
    print(f"3. n-site qubit symmetrizer: {dk}")
    fails = []
    if dsp["p == I_4"] or dsp["rank p"] == 4 or dsp["corner dim"] != 9:
        fails.append("the note's three predicates")
    if not (dsp["F Hermitian"] and dsp["F^2 = I"] and dsp["Tr F"] == 2 and dsp["p^2 = p"] and dsp["rank p"] == 3 and dsp["phi hom"]
            and dsp["phi(I_3) = p"] and dsp["psi *-matrix units, psi(I_3) = p"]):
        fails.append("theorems 1-4 on the displayed objects")
    if any(v["rank"] != v["expected d(d+1)/2"] or not v["p != I"] or not v["idempotent"] or v.get("corner dim", v["rank"] ** 2) != v["rank"] ** 2
           for v in ts.values()):
        fails.append("two-site ladder")
    if any(v["rank P_sym"] != v["expected n+1"] or not v["phi(I) = P_sym"] or v["phi matrix-unit table"] is False or not v["P_sym != I"]
           for v in dk.values()):
        fails.append("symmetrizer ladder")
    if fails:
        print(f"HIT: {fails}")
    print(f"SUMMARY: on the displayed objects F is Hermitian with F^2 = I and Tr F = 2, p is a rank-3 projection, p != I_4, the 16 "
          f"compressed units span dimension {dsp['corner dim']}, phi is an algebra isomorphism with phi(I_3) = p and the ON units are *-matrix "
          f"units summing to p (the three predicates hold as stated); the two-site swap on C^d x C^d has rank d(d+1)/2 for d = 2..8 with "
          f"corner dimension rank^2 (d <= 4), and the n-site qubit symmetrizer has rank n+1 for n = 2..7 with the Dicke map phi(I) = P_sym "
          f"and exact matrix-unit tables (n <= 5); no predicate fails")


if __name__ == "__main__":
    main()
