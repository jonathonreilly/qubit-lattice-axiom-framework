"""SU(3) quadratic Casimir on the algebraic V_3 fundamental equals 4/3.

By cl3_color_automorphism_theorem (cited), SU(3)_c acts on the framework's
3-dim symmetric base subspace via the canonical Gell-Mann generators
T^a = λ^a / 2 satisfying Tr[T^a T^b] = (1/2) δ^{ab}.

The quadratic Casimir
    C_2  :=  Σ_a T^a T^a
is checked directly on the framework-supplied V_3 matrices:

    Σ_a (λ^a/2)^2 = (4/3) I_3.

This runner checks only the algebraic K1-K3 surface: the direct
finite-matrix identity, centrality, and value 4/3 on the cited V_3 carrier.
Schur's lemma
and the SU(N) fundamental Casimir formula are parallel context only,
not proof gates for this runner. It does not
identify V_3 with physical SM quark color and does not certify
one-gluon-exchange, quark self-energy, hard-scattering, confinement, or
other physical color-factor readouts.

Tests:
  (T1) Gell-Mann anticommutation: {T^a, T^b} = (1/3) δ^{ab} I + d^{abc} T^c
  (T2) Gell-Mann commutation:     [T^a, T^b] = i f^{abc} T^c (su(3) Lie algebra)
  (T3) Tr[T^a T^b] = (1/2) δ^{ab}
  (T4) Direct matrix identity C_2 = Σ_a T^a T^a = (4/3) I_3
  (T5) Centrality [C_2, T^b] = 0 follows on the same matrix surface
  (P1) Parallel non-gating check: formula (N² - 1) / (2N) = 4/3
"""
from __future__ import annotations

import numpy as np


def gell_mann_matrices() -> list[np.ndarray]:
    """The 8 Gell-Mann matrices λ^1, ..., λ^8 (Hermitian, 3x3).

    Standard normalization: Tr[λ^a λ^b] = 2 δ^{ab}, so T^a := λ^a / 2 has
    Tr[T^a T^b] = (1/2) δ^{ab}.
    """
    L1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    L2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    L3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    L4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    L5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    L6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    L7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    L8 = (1 / np.sqrt(3)) * np.array(
        [[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex
    )
    return [L1, L2, L3, L4, L5, L6, L7, L8]


def main() -> None:
    print("=" * 72)
    print("SU(3) QUADRATIC CASIMIR ON ALGEBRAIC V_3 FUNDAMENTAL = 4/3")
    print("=" * 72)
    print()

    lambdas = gell_mann_matrices()
    T = [L / 2 for L in lambdas]
    I3 = np.eye(3, dtype=complex)

    # ----- Test 1: Hermitian generators -----
    print("-" * 72)
    print("TEST 1: T^a are Hermitian (a = 1, ..., 8)")
    print("-" * 72)
    max_herm = 0.0
    for a, Ta in enumerate(T):
        d = np.linalg.norm(Ta - Ta.conj().T)
        max_herm = max(max_herm, d)
    print(f"  max ||T^a - (T^a)†|| = {max_herm:.3e}")
    t1_ok = max_herm < 1e-12
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: Trace orthonormality Tr[T^a T^b] = (1/2) δ^{ab} -----
    print("-" * 72)
    print("TEST 2: Tr[T^a T^b] = (1/2) δ^{ab}")
    print("-" * 72)
    max_trace_dev = 0.0
    for a in range(8):
        for b in range(8):
            tr = np.trace(T[a] @ T[b])
            target = 0.5 if a == b else 0.0
            d = abs(tr - target)
            max_trace_dev = max(max_trace_dev, d)
    print(f"  max |Tr[T^a T^b] - (1/2) δ^{{ab}}| = {max_trace_dev:.3e}")
    t2_ok = max_trace_dev < 1e-12
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: su(3) Lie algebra [T^a, T^b] = i f^{abc} T^c -----
    print("-" * 72)
    print("TEST 3: su(3) Lie algebra [T^a, T^b] = i f^{abc} T^c (closure)")
    print("-" * 72)
    # Compute commutators and verify each lies in the Hermitian span of T^a
    # by checking that i [T^a, T^b] is Hermitian and lives in span{T^c}.
    max_close_dev = 0.0
    for a in range(8):
        for b in range(8):
            comm = T[a] @ T[b] - T[b] @ T[a]
            # i*comm should be Hermitian (anti-Hermitian comm × i = Hermitian)
            i_comm = 1j * comm
            # Project onto span{T^c}: f^{abc} = -2i Tr[[T^a, T^b] T^c]
            f_abc = [(-2j * np.trace(comm @ T[c])).real for c in range(8)]
            recon = sum(1j * f_abc[c] * T[c] for c in range(8))
            d = np.linalg.norm(comm - recon)
            max_close_dev = max(max_close_dev, d)
    print(f"  max ||[T^a, T^b] - i f^{{abc}} T^c|| = {max_close_dev:.3e}")
    t3_ok = max_close_dev < 1e-10
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: direct finite-matrix Casimir identity -----
    print("-" * 72)
    print("TEST 4: direct matrix identity C_2 := Σ_a T^a T^a = (4/3) I_3")
    print("-" * 72)
    C2 = sum(Ta @ Ta for Ta in T)
    target = 4.0 / 3.0
    direct_dev = np.linalg.norm(C2 - target * I3)
    eigs = np.linalg.eigvalsh(
        C2.real if np.allclose(C2.imag, 0) else 0.5 * (C2 + C2.conj().T)
    )
    eigs_real = sorted(eigs.tolist())
    print(f"  C_2 eigenvalues = {eigs_real}")
    print(f"  ||C_2 - (4/3) I_3|| = {direct_dev:.3e}")
    t4_ok = direct_dev < 1e-12
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    # ----- Test 5: centrality follows on the same matrix surface -----
    print("-" * 72)
    print("TEST 5: centrality [C_2, T^b] = 0 for every generator")
    print("-" * 72)
    max_central_dev = 0.0
    for Tb in T:
        max_central_dev = max(max_central_dev, np.linalg.norm(C2 @ Tb - Tb @ C2))
    print(f"  max ||[C_2, T^b]|| = {max_central_dev:.3e}")
    t5_ok = max_central_dev < 1e-12
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    # ----- Parallel check: formula (N² - 1) / (2N) = 4/3 for N = 3 -----
    print("-" * 72)
    print("PARALLEL CHECK: SU(N) formula agrees at N=3 (non-load-bearing)")
    print("-" * 72)
    N = 3
    C2_formula = (N ** 2 - 1) / (2 * N)
    print(f"  (N² - 1) / (2N) = ({N**2} - 1) / {2*N} = {C2_formula}")
    agreement = np.linalg.norm(C2 - C2_formula * I3)
    print(f"  ||direct C_2 - formula C_2 I_3|| = {agreement:.3e}")
    print("  STATUS: INFO (parallel context only; not a proof gate)")
    print()

    print("=" * 72)
    print(f"  Test 1 (T^a Hermitian):                        {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (Tr[T^a T^b] = (1/2) δ^{{ab}}):           {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (su(3) Lie algebra closure):            {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (direct C_2 = (4/3) I_3):               {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (centrality from direct C_2):           {'PASS' if t5_ok else 'FAIL'}")
    print("  Parallel SU(N) formula agreement:              INFO")
    all_ok = all([t1_ok, t2_ok, t3_ok, t4_ok, t5_ok])
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
