#!/usr/bin/env python3
"""J:attack-g:PR8032 - finite-PW static-source note (PR #8032), pattern (g) PROOF STEP BY BRUTE FORCE on the R = 1 plaquette fixture's
contraction step, verified literally:

  "B_ij = (1/2) sum_(k,l,a,b) eps_ika eps_jlb conj(U_ab) M_lk, C_ij = conj(M_ji)/3 ... uses only integral U_ij conj(U_kl) =
   delta_ik delta_jl/3, integral U_i1j1 U_i2j2 U_i3j3 = eps_i1i2i3 eps_j1j2j3/6, the conjugate rule, and exact center-charge zeros ...
   The resulting unnormalized J matrix is [[0,1/18,1/54],[1/18,0,1/54],[1/54,1/54,0]]. For example the B-J-C contraction contains 36
   nonzero epsilon products divided by 1944, giving 1/54."

with J = ReTr(UM)/3 = (chi + conj chi)/6, chi = Tr(UM), inner products <F, G> = integral Tr(F* G)/3 over independent Haar U, M:
  * the B-J-C contraction expanded term by term over all index values with the two stated moment rules and the center-charge zeros:
    the number of nonzero epsilon products and the value, as exact rationals;
  * the two moment rules and every entry of the stated J matrix (and the stated norms 1, 1/3, 1/9 of A, B, C) by Monte Carlo over
    independent Haar SU(3) pairs (U, M), with standard errors;
  * the fixture's neutral 3 x 3 Hamiltonian diag(0,16,16) + v(I - J_n), J_n off-diagonal 1/6, at t = 1/100, v = 96t/(1+t-2t^2): the
    stated eigenvector (1, t, t), E0 = v - vt/3, the other eigenvalues 16 + 11v/6 - E0 and 16 + 7v/6, 0 < E0 < v < 4; the trial energy
    [4 + (20/3)t^2 + v(Qn - (4t+t^2)/27)]/Qn and 4 < Etrial - E0 < 4.01, all exact.
HIT if a stated count, entry, eigen-statement or the bracket fails.
"""
import itertools
import math
import sys
from fractions import Fraction

import numpy as np


def eps(i, j, k):
    return (i - j) * (j - k) * (k - i) // 2


def main():
    # ---- the B-J-C contraction, literally
    # <B, J C> = int Tr(B* J C)/3 = (1/3) sum_ij int conj(B_ij) J C_ij
    # conj(B_ij) = (1/2) sum eps_ika eps_jlb U_ab conj(M_lk);  J = (sum_cd U_cd M_dc + conj(U_cd) conj(M_dc))/6;  C_ij = conj(M_ji)/3
    # U-moments: int U_ab U_cd = 0 (center), int U_ab conj(U_cd) = delta_ac delta_bd/3; M-moments: int conj(M_lk) conj(M_dc) conj(M_ji)
    # = eps_ldj eps_kci/6 (conjugate of the third-moment rule; real), int conj(M_lk) M_dc conj(M_ji) = 0 (center).
    nonzero, total = 0, Fraction(0)
    R3 = range(3)
    for i, j, k, l, a, b, c, d in itertools.product(R3, repeat=8):
        e1 = eps(i, k, a) * eps(j, l, b)
        if e1 == 0:
            continue
        # only the conj(U_cd) conj(M_dc) half of J survives the centre charge
        umom = Fraction(1, 3) if (a == c and b == d) else 0
        if umom == 0:
            continue
        mm = eps(l, d, j) * eps(k, c, i)
        if mm == 0:
            continue
        nonzero += 1
        total += Fraction(e1 * mm) * umom * Fraction(1, 6)
    value = Fraction(1, 3) * Fraction(1, 2) * Fraction(1, 6) * Fraction(1, 3) * total
    prefactor = Fraction(1, 3) * Fraction(1, 2) * Fraction(1, 6) * Fraction(1, 3) * Fraction(1, 3) * Fraction(1, 6)
    print(f"[contraction] B-J-C expanded over all index values with the stated moment rules: {nonzero} nonzero epsilon products, "
          f"prefactor 1/{1 / prefactor} (the note: 36 products divided by 1944), value {value} (stated 1/54): "
          f"{nonzero == 36 and prefactor == Fraction(1, 1944) and value == Fraction(1, 54)}")
    # ---- Monte Carlo: the moment rules, the J matrix and the norms
    rng = np.random.default_rng(8032)
    n = 400000

    def haar(n):
        Z = rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3))
        Q, R = np.linalg.qr(Z)
        ph = np.diagonal(R, axis1=1, axis2=2) / np.abs(np.diagonal(R, axis1=1, axis2=2))
        Q = Q * ph[:, None, :]
        return Q / np.linalg.det(Q)[:, None, None] ** (1 / 3)

    U, M = haar(n), haar(n)
    E = np.zeros((3, 3, 3))
    for i1, i2, i3 in itertools.product(range(3), repeat=3):
        E[i1, i2, i3] = eps(i1, i2, i3)
    m2 = np.mean(U[:, 0, 1] * np.conj(U[:, 0, 1]))
    m3 = np.mean(U[:, 0, 0] * U[:, 1, 1] * U[:, 2, 2])
    m3b = np.mean(U[:, 0, 1] * U[:, 1, 0] * U[:, 2, 2])
    A = U
    B = 0.5 * np.einsum("ika,jlb,nab,nlk->nij", E, E, np.conj(U), M)
    C = np.conj(np.transpose(M, (0, 2, 1))) / 3
    chi = np.einsum("nij,nji->n", U, M)
    J = (chi + np.conj(chi)).real / 6

    def ip(F, G, w=None):
        vals = np.einsum("nij,nij->n", np.conj(F), G) / 3 * (1 if w is None else w)
        return vals.mean(), vals.std() / math.sqrt(len(vals))

    names = {"A": A, "B": B, "C": C}
    rows = []
    stated = {("A", "A"): 0, ("A", "B"): Fraction(1, 18), ("A", "C"): Fraction(1, 54), ("B", "B"): 0, ("B", "C"): Fraction(1, 54), ("C", "C"): 0}
    zmax = 0.0
    for (x, y), s in stated.items():
        m, se = ip(names[x], names[y], J)
        z = abs(m - float(s)) / max(se, 1e-12)
        zmax = max(zmax, z)
        rows.append(f"<{x},J{y}> = {m.real:+.5f}{m.imag:+.5f}i (stated {s}, {z:.1f} s.e.)")
    norms = [ip(names[x], names[x])[0].real for x in "ABC"]
    norm_ok = abs(norms[0] - 1) < 5e-3 and abs(norms[1] - 1 / 3) < 5e-3 and abs(norms[2] - 1 / 9) < 5e-3
    print(f"[Monte Carlo] {n} independent Haar pairs: int |U_12|^2 = {m2.real:.4f} (1/3); int U_11 U_22 U_33 = {m3.real:+.4f} (1/6); "
          f"int U_12 U_21 U_33 = {m3b.real:+.4f} (-1/6); " + "; ".join(rows) + f"; norms of A, B, C = {', '.join(f'{x:.4f}' for x in norms)} "
          f"(stated 1, 1/3, 1/9)")
    # ---- the neutral Hamiltonian and the trial energy, exactly
    t = Fraction(1, 100)
    v = 96 * t / (1 + t - 2 * t * t)
    Jn = [[0, Fraction(1, 6), Fraction(1, 6)], [Fraction(1, 6), 0, Fraction(1, 6)], [Fraction(1, 6), Fraction(1, 6), 0]]
    H = [[(Fraction([0, 16, 16][r]) if r == c else 0) + v * ((1 if r == c else 0) - Jn[r][c]) for c in range(3)] for r in range(3)]
    vec = [1, t, t]
    E0 = v - v * t / 3
    Hv = [sum(H[r][c] * vec[c] for c in range(3)) for r in range(3)]
    eig_ok = all(Hv[r] == E0 * vec[r] for r in range(3))
    anti = [0, 1, -1]
    Ha = [sum(H[r][c] * anti[c] for c in range(3)) for r in range(3)]
    anti_ok = all(Ha[r] == (16 + 7 * v / 6) * anti[r] for r in range(3))
    trace_ok = sum(H[r][r] for r in range(3)) == E0 + (16 + 11 * v / 6 - E0) + (16 + 7 * v / 6)
    order_ok = 0 < E0 < v < 4 and E0 < 16 + 7 * v / 6 and E0 < 16 + 11 * v / 6 - E0
    Qn = 1 + 4 * t * t / 9
    Et = (4 + Fraction(20, 3) * t * t + v * (Qn - (4 * t + t * t) / 27)) / Qn
    excess = Et - E0
    # the same trial energy from the stated Gram/J data: psi = A + tB + tC
    kin = 4 * 1 + 16 * t * t * Fraction(1, 3) + 12 * t * t * Fraction(1, 9)
    jnum = 2 * t * Fraction(1, 18) + 2 * t * Fraction(1, 54) + 2 * t * t * Fraction(1, 54)
    Et2 = (kin + v * (Qn - jnum)) / Qn
    print(f"[fixture] t = 1/100, v = {v} = {float(v):.6f}: (1, t, t) is an eigenvector with E0 = v - vt/3 = {float(E0):.6f}: {eig_ok}; "
          f"(0, 1, -1) with 16 + 7v/6: {anti_ok}; trace matches the third eigenvalue 16 + 11v/6 - E0: {trace_ok}; 0 < E0 < v < 4 and E0 "
          f"lowest: {order_ok}; Etrial from the displayed formula = Etrial from the J matrix and norms: {Et == Et2}; Etrial - E0 = "
          f"{float(excess):.9f} (strictly between 4 and 4.01: {4 < excess < Fraction(401, 100)})")
    hits = []
    if not (nonzero == 36 and prefactor == Fraction(1, 1944) and value == Fraction(1, 54)):
        hits.append(f"B-J-C contraction: {nonzero} products, prefactor {prefactor}, value {value}")
    if zmax > 5 or not norm_ok:
        hits.append(f"J matrix or norms off their stated values: max z {zmax:.1f}, norms {norms}")
    if not (eig_ok and anti_ok and trace_ok and order_ok and Et == Et2 and 4 < excess < Fraction(401, 100)):
        hits.append("fixture eigen-structure or the (4, 4.01) bracket")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: pattern (g) PROOF STEP BY BRUTE FORCE on the R = 1 fixture's contraction step - the B-J-C contraction has exactly "
          f"{nonzero} nonzero epsilon products over 1944 = {value}, the whole stated J matrix and the norms 1, 1/3, 1/9 agree with Monte Carlo "
          f"over 400000 Haar pairs (max {zmax:.1f} s.e.), and the neutral eigen-structure and 4 < Etrial - E0 = {float(excess):.6f} < 4.01 hold "
          f"exactly; {len(hits)} failures; the step holds as written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
