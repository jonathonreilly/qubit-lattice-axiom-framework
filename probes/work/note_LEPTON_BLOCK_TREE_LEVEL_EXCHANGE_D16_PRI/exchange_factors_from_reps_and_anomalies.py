#!/usr/bin/env python3
"""J:note falsifier for LEPTON_BLOCK_TREE_LEVEL_EXCHANGE_D16_PRIME_THEOREM_NOTE_2026-05-10 (on main).

Falsifiers implemented: (1) "L_L or e_R carries a nontrivial SU(3)_c generator", (2) "e_R carries a nontrivial SU(2)_L generator",
(3) "the cited hypercharge convention or assignments change the displayed Y_EW(L_L) Y_EW(e_R) product".

The note's runner hard-codes the representation dimensions and Y_EW(L_L) = -1/2, Y_EW(e_R) = -1. Disjoint machinery here, exact:
  1. explicit generator matrices (Gell-Mann/2 on colour triplets, Pauli/2 on weak doublets, zero on singlets) for every
     one-generation field (Q_L, u_R, d_R, L_L, e_R, nu_R); the single-boson exchange factor X_G(A, B) = sum_a T^a_A (x) T^a_B for each
     gauge factor G, as an exact matrix, for the note's pair (L_L, e_R) and for all 21 field pairs (beyond the note's one pair);
  2. the hypercharges re-derived from the anomaly system (SU(Nc)^2 Y, SU(2)^2 Y, gravitational Y, Y^3) by an exact lex Groebner
     basis, with only charge normalizations as input: Q(e_L) = T_3 + Y/2 = -1, Q(nu_R) = 0, Q(u_R) > 0 (the cited uniqueness note takes
     the left-handed hypercharges as input; here SU(2)^2 Y fixes Y(Q_L) from Y(L_L));
  3. beyond the note's size: Nc = 2..7 colours (lepton product and the SU(2)_L doublet-count parity), the content without nu_R, and
     Y(nu_R) left free (the product along the anomaly-free family).
HIT only if the note's own statements fail at Nc = 3 under its cited inputs.
"""
from __future__ import annotations

import itertools

import sympy as sp

R = sp.Rational


def gell_mann():
    l = [sp.zeros(3, 3) for _ in range(8)]
    l[0][0, 1] = l[0][1, 0] = 1
    l[1][0, 1], l[1][1, 0] = -sp.I, sp.I
    l[2][0, 0], l[2][1, 1] = 1, -1
    l[3][0, 2] = l[3][2, 0] = 1
    l[4][0, 2], l[4][2, 0] = -sp.I, sp.I
    l[5][1, 2] = l[5][2, 1] = 1
    l[6][1, 2], l[6][2, 1] = -sp.I, sp.I
    l[7] = sp.diag(1, 1, -2) / sp.sqrt(3)
    return [m / 2 for m in l]


PAULI = [sp.Matrix([[0, 1], [1, 0]]) / 2, sp.Matrix([[0, -sp.I], [sp.I, 0]]) / 2, sp.Matrix([[1, 0], [0, -1]]) / 2]


def generators(color_dim, weak_dim):
    """colour and weak generators on V = C^color (x) C^weak."""
    Ic, Iw = sp.eye(color_dim), sp.eye(weak_dim)
    col = [sp.kronecker_product(t, Iw) for t in gell_mann()] if color_dim == 3 else [sp.zeros(weak_dim, weak_dim)] * 8
    wk = [sp.kronecker_product(Ic, t) for t in PAULI] if weak_dim == 2 else [sp.zeros(color_dim, color_dim)] * 3
    return col, wk


def exchange(gA, gB):
    return sum((sp.kronecker_product(a, b) for a, b in zip(gA, gB)), sp.zeros(gA[0].rows * gB[0].rows, gA[0].rows * gB[0].rows))


def anomaly_solution(Nc, with_nu=True, y_nu=sp.Integer(0)):
    """exact lex Groebner solution of the anomaly system in doubled hypercharge (Q = T_3 + Y/2), with Y(L_L) = -1 from Q(e_L) = -1."""
    yQ, yu, yd, ye = sp.symbols("yQ yu yd ye")
    yL = -1
    yn = y_nu if with_nu else 0
    nnu = 1 if with_nu else 0
    eqs = [2 * yQ - yu - yd,                                                      # SU(Nc)^2 Y
           Nc * yQ + yL,                                                          # SU(2)^2 Y
           2 * Nc * yQ + 2 * yL - Nc * yu - Nc * yd - ye - nnu * yn,              # gravitational Y (= Tr Y)
           2 * Nc * yQ ** 3 + 2 * yL ** 3 - Nc * yu ** 3 - Nc * yd ** 3 - ye ** 3 - nnu * yn ** 3]  # Y^3
    G = sp.groebner(eqs, ye, yQ, yd, yu, order="lex")
    sols = sp.solve(list(G), [yQ, yu, yd, ye], dict=True)
    return G, sols


def main():
    fields = {"Q_L": (3, 2), "u_R": (3, 1), "d_R": (3, 1), "L_L": (1, 2), "e_R": (1, 1), "nu_R": (1, 1)}
    G3, sols3 = anomaly_solution(3)
    sols3 = [s for s in sols3 if s[sp.Symbol("yu")] > 0]
    ok_unique = len(sols3) == 1
    s = sols3[0]
    Y = {"Q_L": s[sp.Symbol("yQ")], "u_R": s[sp.Symbol("yu")], "d_R": s[sp.Symbol("yd")], "L_L": sp.Integer(-1), "e_R": s[sp.Symbol("ye")],
         "nu_R": sp.Integer(0)}
    print(f"1. anomaly system at Nc = 3 (doubled Y, Q = T_3 + Y/2, Q(e_L) = -1, Q(nu_R) = 0), lex Groebner basis {list(G3)}; solutions with "
          f"Q(u_R) > 0: {sols3} (unique: {ok_unique})")
    reps = {f: generators(*d) for f, d in fields.items()}
    fails = []
    col_L, wk_L = reps["L_L"]
    col_e, wk_e = reps["e_R"]
    nz = lambda M: not M.is_zero_matrix
    print(f"   generators on L_L: colour nonzero {any(nz(t) for t in col_L)}, weak nonzero {any(nz(t) for t in wk_L)}; on e_R: colour nonzero "
          f"{any(nz(t) for t in col_e)}, weak nonzero {any(nz(t) for t in wk_e)}")
    gl = exchange(col_L, col_e)
    w = exchange(wk_L, wk_e)
    prod_doubled = Y["L_L"] * Y["e_R"]
    prod_ew = (Y["L_L"] / 2) * (Y["e_R"] / 2)
    print(f"2. note's pair (L_L, e_R): gluon exchange factor zero {gl.is_zero_matrix}; W exchange factor zero {w.is_zero_matrix}; B charge "
          f"product doubled Y(L_L)Y(e_R) = {prod_doubled}, electroweak Y_EW(L_L)Y_EW(e_R) = {prod_ew}")
    if any(nz(t) for t in col_L + col_e) or any(nz(t) for t in wk_e) or not gl.is_zero_matrix or not w.is_zero_matrix:
        fails.append("generators")
    if not (ok_unique and prod_ew == R(1, 2) and prod_doubled == 2):
        fails.append("hypercharge product")

    rows = []
    for (a, b) in itertools.combinations_with_replacement(fields, 2):
        ca, wa = reps[a]
        cb, wb = reps[b]
        g2 = sp.simplify(sum(abs(e) ** 2 for e in exchange(ca, cb)))
        w2 = sp.simplify(sum(abs(e) ** 2 for e in exchange(wa, wb)))
        rows.append((a, b, g2, w2, (Y[a] / 2) * (Y[b] / 2)))
    only_b = [f"({a},{b}) {p}" for a, b, g2, w2, p in rows if g2 == 0 and w2 == 0 and p != 0]
    print(f"3. all 21 one-generation pairs (|gluon factor|^2, |W factor|^2, Y_EW product): "
          + "; ".join(f"({a},{b}) {g2},{w2},{p}" for a, b, g2, w2, p in rows))
    print(f"   pairs whose only nonzero single-boson exchange is B: {only_b}")

    beyond = {}
    for Nc in range(2, 8):
        G, sols = anomaly_solution(Nc)
        good = [t for t in sols if t[sp.Symbol("yu")] > 0]
        Gn, soln = anomaly_solution(Nc, with_nu=False)
        goodn = [t for t in soln if t[sp.Symbol("yu")] > 0]
        prods = sorted({(sp.Integer(-1) / 2) * (t[sp.Symbol("ye")] / 2) for t in good})
        prods_n = sorted({(sp.Integer(-1) / 2) * (t[sp.Symbol("ye")] / 2) for t in goodn})
        beyond[Nc] = (len(good), prods, len(goodn), prods_n, (Nc + 1) % 2 == 0, [t[sp.Symbol("yu")] for t in good])
    print("4. beyond the note's size, Nc colours (Q_L (Nc,2), u_R, d_R (Nc,1), L_L, e_R, [nu_R]): "
          + "; ".join(f"Nc={Nc}: solutions {n1} with Y_EW(L)Y_EW(e) {p1} (Y(u_R) {yu}), without nu_R {n2} with {p2}, SU(2)_L doublet count "
                      f"Nc+1 even {ev}" for Nc, (n1, p1, n2, p2, ev, yu) in beyond.items()))
    yn = sp.Symbol("y_nu")
    Gf, solf = anomaly_solution(3, y_nu=yn)
    ye_f = sorted({sp.simplify(t[sp.Symbol("ye")]) for t in solf}, key=sp.default_sort_key)
    prod_f = sorted({sp.expand((sp.Integer(-1) / 2) * (e / 2)) for e in ye_f}, key=sp.default_sort_key)
    print(f"5. Y(nu_R) = y_nu left free at Nc = 3: Y(e_R) on the anomaly-free family {ye_f}; Y_EW(L_L)Y_EW(e_R) = {prod_f}")

    if fails:
        print(f"HIT: the note's statements fail under its cited inputs: {fails}")
        print("SUMMARY: falsifier fired; see the HIT line")
    else:
        b3 = beyond[3]
        print(f"SUMMARY: falsifiers 1-3 do not fire: from explicit generator matrices the gluon and W exchange factors between L_L and e_R are "
              f"exactly zero and the B charge product is Y_EW(L_L)Y_EW(e_R) = {prod_ew} (doubled {prod_doubled}), with the hypercharges "
              f"re-derived by a lex Groebner basis of the anomaly system (unique with Q(u_R) > 0); beyond the note: the product is 1/2 for "
              f"every Nc = 2..7 and without nu_R, the SU(2)_L doublet count Nc+1 is even only for odd Nc, and with Y(nu_R) = y_nu free the "
              f"product is {prod_f} (1/2 only at y_nu = 0, the cited neutral-singlet input); of the 21 one-generation pairs, "
              f"{len(only_b)} have B as their only single-boson exchange")


if __name__ == "__main__":
    main()
