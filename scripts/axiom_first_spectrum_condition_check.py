#!/usr/bin/env python3
"""
axiom_first_spectrum_condition_check.py
----------------------------------------

Numerical exhibits for the axiom-first spectrum condition lattice
theorem on Cl(3) ⊗ Z^3 (loop axiom-first-foundations-block02,
Cycle 1 / Route R7).

Theorem note:
  docs/AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md

What this runner exhibits, on a small free-staggered lattice (the
staggered-only surface; representative finite carrier of the two-step
blocked transfer matrix T := T_hat^2 whose positivity the note imports
from the staggered-only sector authorities):

  E1.  Construct T = exp(-2 a_τ H_lat) on a small spatial slice,
       representing the two-step blocked object T := T_hat^2;
       verify spectrum of T is real and positive with M_T = max
       eigenvalue.

  E2.  Build the normalised transfer matrix T_norm = T / M_T;
       verify spectrum is in (0, 1].

  E3.  Compute H := -(1/(2 a_τ)) log(T_norm); verify H is self-adjoint
       with non-negative spectrum (E_0 = 0, all E_n ≥ 0).

  E4.  Compute the mass gap m_gap = E_1 - E_0 = -log(λ_1 / M_T) /
       (2 a_τ); report it as a positive number on this finite carrier.

E1-E4 exhibit the content of (SC1)-(SC3) of the note. (SC4) is a
*conditional* temporal-decay corollary (given the gap, via the
temporal bridge note) and is NOT exhibited by this
runner; the verdict line therefore does not claim it. The exhibited gap in
E4 is non-degeneracy on this finite carrier, not a closed-form gap claim
for every canonical configuration.
"""

from __future__ import annotations

import sys
import math
import numpy as np
from numpy.linalg import eigh
from scipy.linalg import expm, logm


def free_staggered_1d_hamiltonian(L_s, mass=0.3):
    """1D free staggered Hamiltonian (no Wilson term, minimal axiom setup)."""
    h = np.zeros((L_s, L_s), dtype=complex)
    for x in range(L_s):
        eps = (-1) ** x
        h[x, x] += mass * eps
        xp = (x + 1) % L_s
        # symmetric staggered hop +i/2 forward, -i/2 backward (Hamiltonian convention)
        h[x, xp] += 0.5j
        h[xp, x] += -0.5j
    h = 0.5 * (h + h.conj().T)

    # Many-body Hamiltonian H = Σ_xy h_xy (c_x^† c_y - ½ δ_xy)
    I2 = np.eye(2, dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    SP = np.array([[0, 1], [0, 0]], dtype=complex)

    def kron_chain(ops):
        out = ops[0]
        for op in ops[1:]:
            out = np.kron(out, op)
        return out

    c, cdag = [], []
    for i in range(L_s):
        chain = []
        for j in range(L_s):
            if j < i:
                chain.append(Z)
            elif j == i:
                chain.append(SP)
            else:
                chain.append(I2)
        c_i = kron_chain(chain)
        c.append(c_i)
        cdag.append(c_i.conj().T)

    dim = 2 ** L_s
    H = np.zeros((dim, dim), dtype=complex)
    I_full = np.eye(dim, dtype=complex)
    for x in range(L_s):
        for y in range(L_s):
            if abs(h[x, y]) > 1e-15:
                H += h[x, y] * (cdag[x] @ c[y] - 0.5 * (I_full if x == y else 0))
    H = 0.5 * (H + H.conj().T)
    return H


def main():
    print("=" * 72)
    print(" axiom_first_spectrum_condition_check.py")
    print(" Loop: axiom-first-foundations-block02, Cycle 1 / R7")
    print(" Spectrum condition: H = -log(T/M_T)/(2 a_τ) is self-adjoint, H ≥ 0")
    print("=" * 72)

    a_tau = 1.0
    L_s = 4
    mass = 0.3

    H_lat = free_staggered_1d_hamiltonian(L_s, mass=mass)
    T = expm(-2.0 * a_tau * H_lat)
    print(f"\n  L_s = {L_s}, mass = {mass}, a_τ = {a_tau}, dim = {2**L_s}")

    # E1: spectrum of T
    evals_T = np.linalg.eigvalsh(0.5 * (T + T.conj().T))
    M_T = float(evals_T.max())
    print(f"\n--- E1: spectrum of T ---")
    print(f"  min eigval = {evals_T.min():.6e}, max eigval (M_T) = {M_T:.6e}")
    print(f"  all positive? {np.all(evals_T > 0)}")
    e1 = (evals_T.min() > 0) and (M_T > 0)
    print(f"  E1 verdict: {'PASS' if e1 else 'FAIL'}")

    # E2: T / M_T spectrum in (0, 1]
    T_norm = T / M_T
    evals_Tn = np.linalg.eigvalsh(0.5 * (T_norm + T_norm.conj().T))
    print(f"\n--- E2: spectrum of T_norm = T / M_T ---")
    print(f"  min eigval = {evals_Tn.min():.6e}, max eigval = {evals_Tn.max():.6e}")
    e2 = (evals_Tn.min() > 0) and (evals_Tn.max() <= 1.0 + 1e-12)
    print(f"  spectrum in (0, 1]? {e2}")
    print(f"  E2 verdict: {'PASS' if e2 else 'FAIL'}")

    # E3: H = -(1/(2 a_τ)) log(T_norm) self-adjoint, H ≥ 0
    H_phys = -(1.0 / (2.0 * a_tau)) * logm(T_norm)
    H_phys_herm = 0.5 * (H_phys + H_phys.conj().T)
    H_old = -(1.0 / a_tau) * logm(T_norm)
    H_old_herm = 0.5 * (H_old + H_old.conj().T)
    old_ratio_err = float(np.max(np.abs(H_old_herm - 2.0 * H_phys_herm)))
    H_err = float(np.max(np.abs(H_phys - H_phys_herm)))
    evals_H = np.linalg.eigvalsh(H_phys_herm)
    print(f"\n--- E3: H = -(1/(2 a_τ)) log(T_norm) ---")
    print(f"  Hermiticity err (||H - H†||_max) = {H_err:.3e}")
    print(f"  old 1/a_τ normalization gives exactly 2H? err = {old_ratio_err:.3e}")
    print(f"  spectrum of H: min = {evals_H.min():.6e}, max = {evals_H.max():.6e}")
    print(f"  ground state E_0 = {evals_H.min():.6e} (target: 0)")
    e3 = (H_err < 1e-9) and (old_ratio_err < 1e-9) and (evals_H.min() > -1e-10)
    print(f"  E3 verdict: {'PASS' if e3 else 'FAIL'}")

    # E4: mass gap
    evals_H_sorted = np.sort(evals_H)
    E0 = evals_H_sorted[0]
    E1 = evals_H_sorted[1]
    m_gap = E1 - E0
    print(f"\n--- E4: mass gap m_gap = E_1 - E_0 ---")
    print(f"  E_0 = {E0:.6e}, E_1 = {E1:.6e}")
    print(f"  m_gap = {m_gap:.6e}")
    e4 = m_gap > 1e-6
    print(f"  m_gap > 0? {e4}")
    print(f"  E4 verdict: {'PASS' if e4 else 'FAIL'}")

    # Summary
    print()
    print("=" * 72)
    print(" SUMMARY")
    print("=" * 72)
    results = {"E1 (T spectrum positive)": e1,
               "E2 (T/M_T spectrum in (0,1])": e2,
               "E3 (H ≥ 0)": e3,
               "E4 (m_gap > 0)": e4}
    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    n_fail = n_total - n_pass
    for k, v in results.items():
        print(f"   {k}: {'PASS' if v else 'FAIL'}")
    print(f"\n   PASSED: {n_pass}/{n_total}")
    print(f"\nSCORECARD: PASS={n_pass} FAIL={n_fail}")
    print()
    if n_pass == n_total:
        # E1-E4 exhibit the content of SC1-SC3 (T positive Hermitian, H
        # self-adjoint and >= 0, and a positive gap on this finite carrier)
        # on the free-staggered surface. SC4 (the conditional temporal-decay
        # corollary on the gap) is NOT exhibited by this runner; it is a
        # downstream corollary in the note conditioned on the temporal bridge
        # note, so the verdict deliberately does not claim it.
        print(" verdict: SC1-SC3 content (T positive Hermitian; H self-adjoint,")
        print("          H >= 0, E_0 = 0; positive gap on this finite carrier)")
        print("          exhibited on the finite free-staggered surface.")
        print("          SC4 is a conditional corollary in the note, not exhibited here.")
        return 0
    else:
        print(" verdict: at least one structural exhibit failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
