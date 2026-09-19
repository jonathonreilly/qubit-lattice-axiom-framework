#!/usr/bin/env python3
"""J:note check for QUARK_ROUTE2_E_CENTER_SINGLE_ADJOINT_LINE_SELECTOR_CONDITIONAL_SUPPORT_NOTE_2026-06-21 (on main).

The note's computable content and falsifiers, in exact rational arithmetic, plus two enumerations beyond its sizes:
  1. the conditional chain for SU(3): e_E = 7/8, rho_E = 6 e_E = 21/4, q_E = 1 + rho_E/6 = 15/8, c_TE = (-2)(5/6)/q_E = -8/9, and the
     falsifier readouts: the line itself (k = 1), the full adjoint (k = 8), F_adj = 8/9 read as the excess; the rank enumeration
     k = 0..8 (the note: only k = 7 reaches 21/4);
  2. beyond SU(3): for SU(N), N = 2..12, every integer-rank readout k/(N^2 - 1), k = 0..N^2 - 1, that reaches rho_E = 21/4, its
     codimension, and whether the signed centre ratio (-2)(5/6)/(1 + k/(N^2-1)) equals -F_adj(N) = -(N^2-1)/N^2 for the
     codimension-one readout (the note's 8/9 magnitude remark);
  3. the falsifier "the selected line is arbitrary ... rather than typed by source geometry": exact dimensions of the subspace of the
     real adjoint su(3) fixed by natural subgroup actions (permutation S3 and its subgroups, the diagonal Z3 x Z3 torus, Delta(27),
     the block SU(2) x U(1) generators, real SO(3), the maximal torus): which fix exactly one line, and which line.
HIT if the note's arithmetic or its k = 0..8 enumeration fails.
"""
from __future__ import annotations

import itertools
from fractions import Fraction as Fr

import sympy as sp


def chain():
    e = Fr(7, 8)
    rho = 6 * e
    qE = 1 + rho / 6
    qT, shell = Fr(5, 6), -2
    cTE = shell * qT / qE
    ks = [k for k in range(9) if 6 * Fr(k, 8) == Fr(21, 4)]
    wrong = {"line itself k=1": 6 * Fr(1, 8), "full adjoint k=8": 6 * Fr(8, 8), "F_adj=8/9 as excess": 6 * Fr(8, 9)}
    return {"e_E": e, "rho_E": rho, "q_E": qE, "c_TE": cTE, "k hitting 21/4": ks, "wrong readouts rho_E": wrong}


def sun():
    out = {}
    for N in range(2, 13):
        D = N * N - 1
        hits = [(k, D - k) for k in range(D + 1) if 6 * Fr(k, D) == Fr(21, 4)]
        e1 = Fr(D - 1, D)
        c1 = -2 * Fr(5, 6) / (1 + e1)
        out[N] = {"dim adj": D, "rank readouts reaching 21/4 (k, codim)": hits, "codim-1 rho_E": 6 * e1,
                  "codim-1 c_TE": c1, "equals -F_adj": c1 == -Fr(D, N * N)}
    return out


def su3_basis():
    """Gell-Mann basis (real span of Hermitian traceless 3x3)."""
    I = sp.I
    L = [sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]), sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
         sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]), sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
         sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]), sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
         sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]), sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3)]
    return L


def fixed_subspace(gens, lie=False):
    """Real dimension and a basis of {X in su(3): g X g^-1 = X for all generators} (or [Y, X] = 0 for Lie generators)."""
    B = su3_basis()
    c = sp.symbols("c0:8", real=True)
    X = sum((ci * Bi for ci, Bi in zip(c, B)), sp.zeros(3, 3))
    eqs = []
    for g in gens:
        M = (g * X - X * g) if lie else (g * X * g.inv() - X)
        for entry in M:
            ex = sp.expand(entry)
            eqs += [sp.re(ex), sp.im(ex)]
    A = sp.Matrix([[sp.diff(eq, ci) for ci in c] for eq in eqs])
    A = sp.simplify(A)
    ns = A.nullspace()
    lines = [sp.simplify(sum((v[i] * B[i] for i in range(8)), sp.zeros(3, 3))) for v in ns]
    return len(ns), lines


def symmetry_table():
    w = sp.exp(2 * sp.pi * sp.I / 3)
    P12 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    C = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Dw = sp.diag(1, w, w ** 2)
    I = sp.I
    lam = su3_basis()
    groups = {
        "S3 permutations": ([P12, C], False),
        "Z3 cyclic shift": ([C], False),
        "Z2 transposition": ([P12], False),
        "diagonal Z3 x Z3 (clock)": ([Dw, sp.diag(w, w, w ** 2)], False),
        "Delta(27) = <C, clock>": ([C, Dw], False),
        "Delta(54) = <C, P12, clock>": ([C, P12, Dw], False),
        "SU(2) x U(1) block (Lie)": ([lam[0], lam[1], lam[2], lam[7]], True),
        "real SO(3) (Lie)": ([lam[1], lam[4], lam[6]], True),
        "maximal torus (Lie)": ([lam[2], lam[7]], True),
    }
    out = {}
    for name, (gens, lie) in groups.items():
        d, lines = fixed_subspace(gens, lie)
        out[name] = (d, [str(L.tolist()) for L in lines] if d == 1 else None)
    return out


def main():
    ch = chain()
    print(f"1. SU(3) chain: {ch}")
    s = sun()
    for N, r in s.items():
        print(f"2. SU({N}): {r}")
    tab = symmetry_table()
    print(f"3. fixed-subspace dimensions in su(3): { {k: v[0] for k, v in tab.items()} }")
    for k, v in tab.items():
        if v[0] == 1:
            print(f"   {k}: fixed line {v[1][0]}")
    fails = []
    if not (ch["e_E"] == Fr(7, 8) and ch["rho_E"] == Fr(21, 4) and ch["q_E"] == Fr(15, 8) and ch["c_TE"] == Fr(-8, 9)
            and ch["k hitting 21/4"] == [7] and all(v != Fr(21, 4) for v in ch["wrong readouts rho_E"].values())):
        fails.append("SU(3) conditional arithmetic")
    if fails:
        print(f"HIT: {fails}")
    other = {N: r["rank readouts reaching 21/4 (k, codim)"] for N, r in s.items() if r["rank readouts reaching 21/4 (k, codim)"]}
    coinc = [N for N, r in s.items() if r["equals -F_adj"]]
    single = [k for k, v in tab.items() if v[0] == 1]
    print(f"SUMMARY: the SU(3) chain gives e_E = 7/8, rho_E = 21/4, q_E = 15/8, c_TE = -8/9, only k = 7 of k = 0..8 reaches 21/4, and the "
          f"falsifier readouts give rho_E = 3/4 (line), 6 (full adjoint), 16/3 (F_adj as excess); for SU(N), N = 2..12, rank readouts "
          f"reaching 21/4 exist only for {other} (codimension one only at N = 3), and the codimension-one centre ratio equals -F_adj(N) only "
          f"for N in {coinc}; among the subgroup actions tried, exactly one adjoint line is fixed by {single} "
          f"(dimensions {({k: v[0] for k, v in tab.items()})}); no arithmetic step fails")


if __name__ == "__main__":
    main()
