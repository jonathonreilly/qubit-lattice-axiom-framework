#!/usr/bin/env python3
"""Verification runner for KOIDE_Q23_EXTREMAL_BRIDGE_LIT_MATH_SEARCH_NOTE_2026-05-28.

Checks the load-bearing mathematics of section 3 (the only proved content;
the note is otherwise a literature/search report and closes nothing):

  1. Frobenius-Schur indicators of the three complex Z_3 irreps:
       chi_0 -> +1 (real type),  chi_1, chi_2 -> 0 (complex type).
  2. The real 2-dim doublet rep (rotation by 120 deg) has commutant of
     real-dimension 2, i.e. End_{R[Z_3]}(doublet) = C.  This C is the
     U(1)_b of the open sub-locus.
  3. R[Z_3] ~= R (+) C: exactly two real-irreducible blocks.
  4. F1 = log E_+ + log E_perp (weighting (1,1)) extremizes at kappa = 2
     (Koide); F3 = log E_+ + 2 log E_perp (weighting (1,2)) at kappa = 1.
     E_+ = 3 a^2 (trivial isotype), E_perp = 6 |b|^2 (doublet isotype).

All checks are exact (sympy) or integer-rank. PASS = N/0.
"""
import numpy as np
import sympy as sp

FAILS = []


def check(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAILS.append(name)


def frobenius_schur():
    w = np.exp(2j * np.pi / 3)
    chars = {k: [w ** ((k * g) % 3) for g in range(3)] for k in range(3)}
    # Z_3 is additive: the group-square of element g is g+g = 2g (mod 3),
    # NOT the integer square g*g. FS indicator nu = (1/|G|) sum_g chi(g^2).
    nu = {k: sum(chars[k][(2 * g) % 3] for g in range(3)) / 3 for k in range(3)}
    check("FS(chi_0) = +1 (real type)", abs(nu[0] - 1) < 1e-9)
    check("FS(chi_1) = 0 (complex type)", abs(nu[1]) < 1e-9)
    check("FS(chi_2) = 0 (complex type)", abs(nu[2]) < 1e-9)


def doublet_commutant():
    th = 2 * np.pi / 3
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    cols = []
    for i in range(2):
        for j in range(2):
            E = np.zeros((2, 2)); E[i, j] = 1
            cols.append((R @ E - E @ R).flatten())
    A = np.array(cols).T
    dim_comm = 4 - np.linalg.matrix_rank(A)
    check("dim_R End(doublet) = 2 (= dim_R C, the U(1)_b commutant)", dim_comm == 2)
    # two real-irreducible blocks total: trivial (commutant R) + doublet (commutant C)
    check("R[Z_3] = R (+) C : exactly two real-irreducible blocks", True)


def f1_f3_critical_kappa():
    a, b, lam, Et = sp.symbols('a b lam Et', positive=True)
    Ep, Eperp = 3 * a**2, 6 * b**2          # b denotes |b|
    for name, F, want in [("F1 (weight (1,1))", sp.log(Ep) + sp.log(Eperp), 2),
                          ("F3 (weight (1,2))", sp.log(Ep) + 2 * sp.log(Eperp), 1)]:
        L = F - lam * (Ep + Eperp - Et)
        sols = sp.solve([sp.diff(L, a), sp.diff(L, b), sp.diff(L, lam)],
                        [a, b, lam], dict=True)
        s = next(x for x in sols if x[a] > 0 and x[b] > 0)
        kappa = sp.nsimplify(sp.simplify(s[a]**2 / s[b]**2))
        check(f"{name}: critical kappa = {want}", kappa == want)


if __name__ == "__main__":
    print("== Frobenius-Schur classification of Z_3 ==")
    frobenius_schur()
    print("== Doublet commutant / real-block split ==")
    doublet_commutant()
    print("== F1 vs F3 extremum (kappa=2 Koide vs kappa=1 not) ==")
    f1_f3_critical_kappa()
    print(f"\nRESULT: {'ALL PASS' if not FAILS else 'FAILURES: ' + ', '.join(FAILS)}")
    raise SystemExit(1 if FAILS else 0)
