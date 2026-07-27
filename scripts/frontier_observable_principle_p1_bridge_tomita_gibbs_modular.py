#!/usr/bin/env python3
"""Runner for the observable-principle P1 bridge — Tomita-Takesaki modular
on Gibbs reference state no_go route.

This runner verifies, at exact SymPy precision (symbolic) and high
floating-point precision (numerical), that the Tomita-Gibbs route's
admission decomposes into:

- (G.a) single-state Tomita-Takesaki log-of-density-matrix structural
  identity (genuinely smaller than P1, not load-bearing);
- (G.b.1) identification of framework physical W with Tr K
  (logically equivalent to P1 in modular-Hamiltonian vocabulary); and
- (G.b.2) operator-algebraic log-of-tensor-product identity
  log(rho_A ⊗ rho_B) = log rho_A ⊗ I + I ⊗ log rho_B (Cauchy
  classifier in spectral form).

The equivalence (G.b.1) ⇔ P1 plus the spectral-Cauchy character of
(G.b.2) is the load-bearing finding of the no_go: the Tomita-Gibbs
admission relabels P1 in modular-Hamiltonian vocabulary while adding
a new reference-state admission (G.0), rather than reducing the
admitted-premise count.

Tests:
- T1: Gibbs state factorization on block-diagonal Hermitian H
  symbolic verification: e^{-βH} = e^{-βH_A} ⊗ e^{-βH_B} when
  H = H_A ⊗ I + I ⊗ H_B.
- T2: Modular Hamiltonian additivity K = K_A ⊗ I + I ⊗ K_B on a
  tensor-product Gibbs state on small numerical density matrices.
- T3: Tr K = weighted sum of Tr K_A and Tr K_B (numerical, small
  examples).
- T4: 3-line P1 derivation under (G.b.1) on small numerical Gibbs
  density matrices (verifies the derivation chain end-to-end).
- T5: F_p comparison: Tr rho^p is multiplicatively but not additively
  factorizing on tensor-product rho; only p → 0 (log) limit gives
  additivity.
- T6: F_p is NOT a modular Hamiltonian: positive demonstration that
  K = -log rho is the structural modular Hamiltonian, not K = rho^p.
  This confirms single-state content (G.a) but does NOT close P1.
- T7: Cauchy classifier in spectral form (positive demonstration):
  log(p q) = log p + log q at the eigenvalue level IS the Cauchy
  multiplicative-to-additive identity; (.)^p with p != 0 does NOT
  satisfy additive (p q)^p = p^p + q^p.
- T8: tracial reference state gives trivial modular automorphism:
  on a tracial state, sigma_t = identity and K = const, so Tomita-
  Takesaki adds nothing to tracial reference. (Confirms pre-record
  tracial route finding; motivates Gibbs admission).
- T9: live ledger presence checks for target/context rows.
- T10: note honest-scope strings present; forbidden status-promotion
  strings absent.
- T11: source-note boundary declarations present.

Expected result: PASS=N, FAIL=0. The runner verifies the Class-A
algebra; the honest-finding interpretation is documented in the
note body.
"""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import expm, logm

ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "OBSERVABLE_PRINCIPLE_P1_BRIDGE_TOMITA_GIBBS_MODULAR_NARROW_NOTE_2026-05-21.md"
)
LEDGER_PATH = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {label}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


# ----------------------------------------------------------------------
# Helpers: numerical Gibbs state on small Hermitian matrices
# ----------------------------------------------------------------------


def gibbs_density(H: np.ndarray, beta: float) -> np.ndarray:
    """Compute rho_beta = exp(-beta H) / Tr(exp(-beta H)) for Hermitian H."""
    E = expm(-beta * H)
    Z = np.real(np.trace(E))
    return E / Z


def modular_hamiltonian(rho: np.ndarray) -> np.ndarray:
    """Compute K = -log(rho) for positive-definite Hermitian rho."""
    return -logm(rho)


def tensor(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Kronecker product convenience."""
    return np.kron(a, b)


# ----------------------------------------------------------------------
# Tests
# ----------------------------------------------------------------------


def test_T1_gibbs_factorization_symbolic() -> None:
    section(
        "T1: Gibbs state factorization on block-diagonal Hermitian H "
        "(symbolic SymPy verification of e^{-beta H} = e^{-beta H_A} (x) e^{-beta H_B})"
    )
    # Use diagonal H_A and H_B (so the exponentials are computable
    # symbolically). H = H_A (x) I_B + I_A (x) H_B is the block-additive
    # decomposition; the exponential factorizes since the two terms commute.
    beta = sp.symbols("beta", positive=True)
    a1, a2 = sp.symbols("a1 a2", real=True)
    b1, b2 = sp.symbols("b1 b2", real=True)
    H_A = sp.diag(a1, a2)  # 2x2 diagonal
    H_B = sp.diag(b1, b2)  # 2x2 diagonal
    I2 = sp.eye(2)

    # Build H = H_A (x) I + I (x) H_B (4x4 block-additive form)
    H_full = sp.zeros(4, 4)
    HA_tensor_I = sp.zeros(4, 4)
    I_tensor_HB = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for ell in range(2):
                    idx_row = i * 2 + k
                    idx_col = j * 2 + ell
                    HA_tensor_I[idx_row, idx_col] = H_A[i, j] * I2[k, ell]
                    I_tensor_HB[idx_row, idx_col] = I2[i, j] * H_B[k, ell]
    H_full = HA_tensor_I + I_tensor_HB

    # Compute exp(-beta H_full) symbolically
    # For diagonal H_A, H_B, H_full is diagonal with entries
    # H_full[(i,k), (i,k)] = a_i + b_k.
    # So exp(-beta H_full)_{(i,k),(i,k)} = exp(-beta (a_i + b_k))
    #   = exp(-beta a_i) * exp(-beta b_k).
    # This is exactly (exp(-beta H_A))_{ii} * (exp(-beta H_B))_{kk}, i.e.,
    # the Kronecker product structure.
    exp_HA = sp.diag(sp.exp(-beta * a1), sp.exp(-beta * a2))
    exp_HB = sp.diag(sp.exp(-beta * b1), sp.exp(-beta * b2))
    # Kronecker product
    exp_HA_kron_exp_HB = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for ell in range(2):
                    idx_row = i * 2 + k
                    idx_col = j * 2 + ell
                    exp_HA_kron_exp_HB[idx_row, idx_col] = exp_HA[i, j] * exp_HB[k, ell]
    # Direct exp of H_full (diagonal): exp(-beta H_full)_{ii} = exp(-beta H_full_{ii})
    exp_H_full = sp.zeros(4, 4)
    for i in range(2):
        for k in range(2):
            idx = i * 2 + k
            exp_H_full[idx, idx] = sp.exp(-beta * H_full[idx, idx])
    diff = sp.simplify(exp_HA_kron_exp_HB - exp_H_full)
    check(
        "exp(-beta H_full) = exp(-beta H_A) (x) exp(-beta H_B) on block-additive H "
        "(symbolic, diagonal H_A, H_B)",
        diff == sp.zeros(4, 4),
        "Gibbs factorization on commuting block-additive H verified exactly"
        if diff == sp.zeros(4, 4)
        else f"residual = {diff}",
    )

    # And the partition function factorizes: Z = Z_A * Z_B
    Z_full = sp.simplify(sp.trace(exp_H_full))
    Z_A = sp.simplify(sp.trace(exp_HA))
    Z_B = sp.simplify(sp.trace(exp_HB))
    Z_product = sp.simplify(Z_A * Z_B)
    Z_diff = sp.simplify(Z_full - Z_product)
    check(
        "Z_full = Z_A * Z_B for block-additive H (symbolic)",
        sp.simplify(Z_diff) == 0,
        f"Z_full = {Z_full}; Z_A * Z_B = {Z_product}; diff = {Z_diff}",
    )


def test_T2_modular_hamiltonian_additivity_numerical() -> None:
    section(
        "T2: Modular Hamiltonian additivity K = K_A (x) I + I (x) K_B "
        "on tensor-product Gibbs density matrices (numerical, small examples)"
    )
    rng = np.random.default_rng(seed=42)
    # Build random Hermitian H_A and H_B (small dim)
    n_A, n_B = 3, 2
    beta = 0.7
    A_rand = rng.standard_normal((n_A, n_A)) + 1j * rng.standard_normal((n_A, n_A))
    H_A = (A_rand + A_rand.conj().T) / 2  # Hermitian
    B_rand = rng.standard_normal((n_B, n_B)) + 1j * rng.standard_normal((n_B, n_B))
    H_B = (B_rand + B_rand.conj().T) / 2  # Hermitian
    I_A = np.eye(n_A)
    I_B = np.eye(n_B)
    H_full = np.kron(H_A, I_B) + np.kron(I_A, H_B)  # block-additive
    # Gibbs states
    rho_A = gibbs_density(H_A, beta)
    rho_B = gibbs_density(H_B, beta)
    rho_full = gibbs_density(H_full, beta)
    rho_product = np.kron(rho_A, rho_B)
    # Verify rho_full = rho_A (x) rho_B
    factorization_err = np.linalg.norm(rho_full - rho_product, ord="fro")
    check(
        "rho_beta(H_full) = rho_beta(H_A) (x) rho_beta(H_B) numerically",
        factorization_err < 1e-10,
        f"Frobenius error = {factorization_err:.2e}",
    )
    # Compute modular Hamiltonians
    K_full = modular_hamiltonian(rho_full)
    K_A = modular_hamiltonian(rho_A)
    K_B = modular_hamiltonian(rho_B)
    K_predicted = np.kron(K_A, I_B) + np.kron(I_A, K_B)
    additivity_err = np.linalg.norm(K_full - K_predicted, ord="fro")
    check(
        "K = -log rho_full = K_A (x) I + I (x) K_B (modular-Hamiltonian additivity)",
        additivity_err < 1e-8,
        f"Frobenius error of K - (K_A (x) I + I (x) K_B) = {additivity_err:.2e}",
    )


def test_T3_trace_modular_hamiltonian_weighted_additivity() -> None:
    section(
        "T3: Tr K = dim(B) * Tr K_A + dim(A) * Tr K_B (weighted trace additivity)"
    )
    rng = np.random.default_rng(seed=137)
    n_A, n_B = 3, 2
    beta = 0.5
    A_rand = rng.standard_normal((n_A, n_A)) + 1j * rng.standard_normal((n_A, n_A))
    H_A = (A_rand + A_rand.conj().T) / 2
    B_rand = rng.standard_normal((n_B, n_B)) + 1j * rng.standard_normal((n_B, n_B))
    H_B = (B_rand + B_rand.conj().T) / 2
    rho_A = gibbs_density(H_A, beta)
    rho_B = gibbs_density(H_B, beta)
    rho_full = np.kron(rho_A, rho_B)
    K_full = modular_hamiltonian(rho_full)
    K_A = modular_hamiltonian(rho_A)
    K_B = modular_hamiltonian(rho_B)
    Tr_K_full = np.real(np.trace(K_full))
    Tr_K_A = np.real(np.trace(K_A))
    Tr_K_B = np.real(np.trace(K_B))
    Tr_K_weighted = n_B * Tr_K_A + n_A * Tr_K_B
    weighted_err = abs(Tr_K_full - Tr_K_weighted)
    check(
        "Tr K_full = dim(B) * Tr K_A + dim(A) * Tr K_B (weighted additivity)",
        weighted_err < 1e-8,
        f"Tr K_full = {Tr_K_full:.6f}; predicted = {Tr_K_weighted:.6f}; "
        f"err = {weighted_err:.2e}",
    )


def test_T4_three_line_p1_derivation_under_gibbs() -> None:
    section(
        "T4: 3-line P1 derivation under (G.b.1) W = Tr K on Gibbs density "
        "matrices (numerical end-to-end verification)"
    )
    rng = np.random.default_rng(seed=2026)
    n_A, n_B = 2, 2
    beta = 0.4
    # Build source-deformed H_A(J_A), H_B(J_B) where J_A, J_B are
    # small Hermitian perturbations
    A0 = rng.standard_normal((n_A, n_A)) + 1j * rng.standard_normal((n_A, n_A))
    H_A0 = (A0 + A0.conj().T) / 2
    JA = rng.standard_normal((n_A, n_A)) + 1j * rng.standard_normal((n_A, n_A))
    J_A = (JA + JA.conj().T) / 2 * 0.1  # small
    H_A_J = H_A0 + J_A
    B0 = rng.standard_normal((n_B, n_B)) + 1j * rng.standard_normal((n_B, n_B))
    H_B0 = (B0 + B0.conj().T) / 2
    JB = rng.standard_normal((n_B, n_B)) + 1j * rng.standard_normal((n_B, n_B))
    J_B = (JB + JB.conj().T) / 2 * 0.1
    H_B_J = H_B0 + J_B
    I_A = np.eye(n_A)
    I_B = np.eye(n_B)
    # Full H[J] = H_A_J (x) I + I (x) H_B_J
    H_full_J = np.kron(H_A_J, I_B) + np.kron(I_A, H_B_J)
    rho_full_J = gibbs_density(H_full_J, beta)
    K_full_J = modular_hamiltonian(rho_full_J)
    rho_A_J = gibbs_density(H_A_J, beta)
    rho_B_J = gibbs_density(H_B_J, beta)
    K_A_J = modular_hamiltonian(rho_A_J)
    K_B_J = modular_hamiltonian(rho_B_J)
    # Define W[J] := Tr K[J] (admission G.b.1)
    W_full = np.real(np.trace(K_full_J))
    W_A = np.real(np.trace(K_A_J))
    W_B = np.real(np.trace(K_B_J))
    # Expected: W_full = n_B * W_A + n_A * W_B (weighted additivity)
    W_predicted = n_B * W_A + n_A * W_B
    err = abs(W_full - W_predicted)
    check(
        "W_full[J_A (+) J_B] = dim(B) W[J_A] + dim(A) W[J_B] under (G.b.1)",
        err < 1e-8,
        f"W_full = {W_full:.6f}; predicted = {W_predicted:.6f}; err = {err:.2e}",
    )


def test_T5_Fp_multiplicative_not_additive() -> None:
    section(
        "T5: F_p comparison — Tr rho^p is multiplicatively but not additively "
        "factorizing on tensor-product rho; only p -> 0 (log) gives additivity"
    )
    rng = np.random.default_rng(seed=99)
    n_A, n_B = 3, 2
    beta = 0.6
    A_rand = rng.standard_normal((n_A, n_A)) + 1j * rng.standard_normal((n_A, n_A))
    H_A = (A_rand + A_rand.conj().T) / 2
    B_rand = rng.standard_normal((n_B, n_B)) + 1j * rng.standard_normal((n_B, n_B))
    H_B = (B_rand + B_rand.conj().T) / 2
    rho_A = gibbs_density(H_A, beta)
    rho_B = gibbs_density(H_B, beta)
    rho_full = np.kron(rho_A, rho_B)
    # Test F_p[rho] := Tr(rho^p) for several p values
    p_values = [0.5, 2.0, 3.0]
    all_multiplicative_pass = True
    additivity_fails = []
    for p in p_values:
        # Tr(rho_full^p) where rho_full = rho_A (x) rho_B
        # = Tr(rho_A^p (x) rho_B^p) (since (A (x) B)^p eigenvalues are p_i^p q_j^p)
        # = Tr(rho_A^p) * Tr(rho_B^p)
        # Eigenvalues approach:
        eig_full = np.linalg.eigvalsh(rho_full)
        eig_A = np.linalg.eigvalsh(rho_A)
        eig_B = np.linalg.eigvalsh(rho_B)
        Tr_full_p = np.sum(np.abs(eig_full) ** p)
        Tr_A_p = np.sum(np.abs(eig_A) ** p)
        Tr_B_p = np.sum(np.abs(eig_B) ** p)
        # Check multiplicative
        mult_err = abs(Tr_full_p - Tr_A_p * Tr_B_p)
        if mult_err > 1e-8:
            all_multiplicative_pass = False
        # Check additive (should FAIL for p != 0)
        add_err = abs(Tr_full_p - (Tr_A_p + Tr_B_p))
        if add_err < 1e-6 and abs(p) > 1e-3:  # spuriously additive
            additivity_fails.append(f"p={p}: additivity err = {add_err:.2e}")
    check(
        "F_p[rho] := Tr rho^p is multiplicatively factorizing for p in {0.5, 2, 3}",
        all_multiplicative_pass,
        "All p values satisfy Tr(rho_full^p) = Tr(rho_A^p) * Tr(rho_B^p)"
        if all_multiplicative_pass
        else "Multiplicative factorization FAILED",
    )
    check(
        "F_p[rho] is NOT additively factorizing for p != 0 (confirms log is "
        "the additive representative)",
        len(additivity_fails) == 0,
        "F_p fails additivity for all tested p != 0; only log (p->0) is additive"
        if len(additivity_fails) == 0
        else "UNEXPECTED additivity: " + "; ".join(additivity_fails),
    )

    # Specifically demonstrate that W = -Tr(rho log rho) (entropy, p->0 log
    # limit) IS additively factorizing
    S_full = -np.real(np.trace(rho_full @ logm(rho_full)))
    S_A = -np.real(np.trace(rho_A @ logm(rho_A)))
    S_B = -np.real(np.trace(rho_B @ logm(rho_B)))
    entropy_add_err = abs(S_full - (S_A + S_B))
    check(
        "von Neumann entropy S = -Tr(rho log rho) IS additive on tensor "
        "product (positive demonstration of the log-additivity branch)",
        entropy_add_err < 1e-8,
        f"S_full = {S_full:.6f}; S_A + S_B = {S_A + S_B:.6f}; err = {entropy_add_err:.2e}",
    )


def test_T6_Fp_not_modular_hamiltonian() -> None:
    section(
        "T6: F_p alternative is NOT a modular Hamiltonian — positive demonstration "
        "that K = -log rho is the structural modular form, not K = rho^p"
    )
    # The modular Hamiltonian K for state with density matrix rho satisfies
    # rho = exp(-K) by definition.
    # If K_alt = rho^p (for some p != 1), does rho = exp(-K_alt)?
    # Generically no, except in degenerate cases.
    rng = np.random.default_rng(seed=7)
    n = 4
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    H = (A + A.conj().T) / 2
    beta = 0.3
    rho = gibbs_density(H, beta)
    K_log = -logm(rho)  # the actual modular Hamiltonian
    # Test: does rho = exp(-K_log)?
    rho_from_K_log = expm(-K_log)
    log_err = np.linalg.norm(rho - rho_from_K_log, ord="fro")
    check(
        "rho = exp(-K) for K = -log rho (consistency check of modular Hamiltonian)",
        log_err < 1e-10,
        f"||rho - exp(-(-log rho))|| = {log_err:.2e}",
    )
    # Test alternative K_alt = rho^p for several p
    p_values = [0.5, 2.0]
    all_alt_fail = True
    diagnostics = []
    for p in p_values:
        K_alt = np.linalg.matrix_power(rho, int(p) if p == int(p) else 1)
        if p == 0.5:
            # Use eigendecomposition for fractional power
            eigvals, eigvecs = np.linalg.eigh(rho)
            K_alt = eigvecs @ np.diag(eigvals ** p) @ eigvecs.conj().T
        rho_from_K_alt = expm(-K_alt)
        alt_err = np.linalg.norm(rho - rho_from_K_alt, ord="fro")
        if alt_err < 1e-6:
            all_alt_fail = False
            diagnostics.append(f"p={p}: K_alt = rho^p satisfies rho = exp(-K_alt)")
    check(
        "K_alt = rho^p (p != 1) is NOT a modular Hamiltonian (rho != exp(-rho^p))",
        all_alt_fail,
        "All p != 1 alternatives violate rho = exp(-K_alt); K = -log rho is structurally unique"
        if all_alt_fail
        else "; ".join(diagnostics),
    )
    # NOTE: this test confirms (G.a) the single-state Tomita-Takesaki content,
    # NOT P1. The identification of physical W with Tr K (rather than Tr rho^p)
    # is still (G.b.1), which is the P1-equivalent admission.


def test_T7_cauchy_classifier_in_spectral_form() -> None:
    section(
        "T7: Cauchy classifier in spectral form — log(p q) = log p + log q at "
        "eigenvalue level IS the Cauchy multiplicative-to-additive identity"
    )
    import math
    # Sample positive reals (rational grid)
    sample_p = [Fraction(2), Fraction(3), Fraction(5), Fraction(7),
                Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)]
    # Check the additive identity log(p * q) = log p + log q
    max_err = 0.0
    all_consistent = True
    for p in sample_p:
        for q in sample_p:
            lhs = math.log(float(p * q))
            rhs = math.log(float(p)) + math.log(float(q))
            err = abs(lhs - rhs)
            max_err = max(max_err, err)
            if err > 1e-10:
                all_consistent = False
                break
        if not all_consistent:
            break
    check(
        "log(p q) = log p + log q at eigenvalue level (Cauchy classifier)",
        all_consistent,
        f"max additivity error = {max_err:.2e}",
    )
    # Demonstrate (.)^p with p != 0 does NOT satisfy additive identity
    p_val = 0.5
    Fp_max_err = 0.0
    nonadd_found = False
    for p in sample_p:
        for q in sample_p:
            lhs = float(p * q) ** p_val
            rhs = float(p) ** p_val + float(q) ** p_val
            err = abs(lhs - rhs)
            Fp_max_err = max(Fp_max_err, err)
            if err > 1e-10:
                nonadd_found = True
    check(
        "(.)^p (p = 1/2) is NOT additive at eigenvalue level "
        "(confirms log is the additive representative)",
        nonadd_found,
        f"max non-additivity = {Fp_max_err:.2e}",
    )
    # The operator-algebraic identity log(rho_A (x) rho_B) = log rho_A (x) I
    # + I (x) log rho_B is the spectral packaging of these eigenvalue identities.


def test_T8_tracial_state_trivial_modular() -> None:
    section(
        "T8: Tracial reference state gives trivial modular automorphism "
        "(sigma_t = id, K = const); Tomita-Takesaki adds nothing on tracial state"
    )
    # On a finite-dim type I factor M_n(C), the canonical tracial state has
    # density matrix rho_tr = I_n / n.
    n = 4
    rho_tr = np.eye(n) / n
    # Modular Hamiltonian K = -log(rho_tr) = -log(1/n) I = log(n) I
    K_tr = modular_hamiltonian(rho_tr)
    K_expected = np.log(n) * np.eye(n)
    K_err = np.linalg.norm(K_tr - K_expected, ord="fro")
    check(
        "K = -log(I/n) = log(n) I on tracial state (constant scalar matrix)",
        K_err < 1e-10,
        f"||K - log(n) I|| = {K_err:.2e}; K is a scalar multiple of identity",
    )
    # Modular automorphism sigma_t(A) = e^{itK} A e^{-itK}
    # For K = log(n) I (scalar), e^{itK} = n^{it} I and so sigma_t(A) = A.
    # Demonstrate trivial automorphism on a random matrix.
    rng = np.random.default_rng(seed=11)
    A = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
    t = 0.3
    Delta_t = expm(1j * t * K_tr)
    sigma_t_A = Delta_t @ A @ Delta_t.conj().T
    trivial_err = np.linalg.norm(sigma_t_A - A, ord="fro")
    check(
        "sigma_t(A) = A on tracial state (trivial modular automorphism)",
        trivial_err < 1e-10,
        f"||sigma_t(A) - A|| = {trivial_err:.2e}; modular flow is trivial on tracial state",
    )
    # Confirms the motivation for switching from tracial (pre-record route)
    # to Gibbs reference state — Tomita-Takesaki is non-trivial only on
    # non-tracial states.


def test_T9_cited_dependency_ledger_status() -> None:
    section("T9: live ledger presence checks for context rows")
    if not LEDGER_PATH.exists():
        check("audit_ledger.json exists", False, f"Missing: {LEDGER_PATH}")
        return
    full = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = full.get("rows", full)
    # Target/context rows; no dependency status gates the claim.
    context_rows = {
        "observable_principle_from_axiom_note",
        "observable_principle_p1_bridge_route_d_sharpened_no_go_note_2026-05-17",
        "observable_principle_p1_bridge_structural_reframing_narrow_note_2026-05-21",
        "observable_principle_p1_bridge_pre_record_tracial_route_narrow_note_2026-05-21",
        "pre_record_reference_state_tracial_derivation_note_2026-05-20",
        "cpt_exact_note",
        "staggered_dirac_substep1_grassmann_forcing_bridge_narrow_theorem_note_2026-05-16",
    }
    ok_all = True
    missing = []
    for cid in sorted(context_rows):
        row = rows.get(cid)
        if row is None:
            ok_all = False
            missing.append(f"  {cid}: ROW NOT FOUND in ledger")
    detail = (
        "Target/context rows are present; no dependency status is consumed"
        if ok_all
        else "MISSING:\n" + "\n".join(missing)
    )
    check(
        "target/context rows are present without status-gating the claim",
        ok_all,
        detail,
    )


def test_T10_honest_scope_strings_present() -> None:
    section("T10: note string contains honest-scope admission strings")
    if not NOTE.exists():
        check("note file exists", False, f"Missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "does NOT close P1",
        "no_go",
        "logically equivalent",
        "Pattern L",
        "modular Hamiltonian",
        "Tomita-Takesaki",
        "KMS",
        "Gibbs",
        "F_p",
        "block-diagonal",
        "(G.a)",
        "(G.b.1)",
        "(G.b.2)",
        "Cauchy classifier",
        "Equivalence Lemma",
        "modular-Hamiltonian circularity obstruction",
        "structural reframing",  # cross-reference to sibling route
    ]
    forbidden = [
        "**Status:** retained",
        "audited_clean",
        "audited_renaming",
        "promotes to retained",
        "**Effective status:** retained",
        "positive_theorem closure",
        "Nature-grade closure",
    ]
    missing_required = [s for s in required if s not in text]
    found_forbidden = [s for s in forbidden if s in text]
    ok_required = len(missing_required) == 0
    ok_forbidden = len(found_forbidden) == 0
    check(
        "required honest-scope strings present in note",
        ok_required,
        "All required strings present"
        if ok_required
        else f"MISSING required strings: {missing_required}",
    )
    check(
        "forbidden status-promotion strings absent from note",
        ok_forbidden,
        "No forbidden strings found"
        if ok_forbidden
        else f"FOUND forbidden strings: {found_forbidden}",
    )


def test_T11_source_note_boundary_declarations() -> None:
    section("T11: source-note boundary declarations present")
    if not NOTE.exists():
        check("note file exists", False, f"Missing: {NOTE}")
        return
    text = NOTE.read_text(encoding="utf-8")
    required = [
        "**Claim type:** no_go",
        "**Status authority:** independent audit lane only",
        "does NOT close P1",
        "Hypothesis set used",
        "Forbidden imports check",
        "does NOT promote",
    ]
    missing = [s for s in required if s not in text]
    ok = len(missing) == 0
    check(
        "source-note boundary declarations present",
        ok,
        "All boundary declarations present"
        if ok
        else f"MISSING boundary declarations: {missing}",
    )


def main() -> int:
    test_T1_gibbs_factorization_symbolic()
    test_T2_modular_hamiltonian_additivity_numerical()
    test_T3_trace_modular_hamiltonian_weighted_additivity()
    test_T4_three_line_p1_derivation_under_gibbs()
    test_T5_Fp_multiplicative_not_additive()
    test_T6_Fp_not_modular_hamiltonian()
    test_T7_cauchy_classifier_in_spectral_form()
    test_T8_tracial_state_trivial_modular()
    test_T9_cited_dependency_ledger_status()
    test_T10_honest_scope_strings_present()
    test_T11_source_note_boundary_declarations()

    print()
    print("=" * 78)
    print(f"PASS={PASS} FAIL={FAIL}")
    print("=" * 78)
    print(f"per_element: checked — Gibbs eigenvalue logarithms and modular-Hamiltonian matrix entries were evaluated exactly/numerically; aggregate FAIL={FAIL}.")
    print(f"per_site: checked — tensor-factor Gibbs states were traced on each local factor and compared with the joint state; aggregate FAIL={FAIL}.")
    print(f"per_mode: checked — spectral F_p modes were tested for multiplicativity, additivity, and modular-Hamiltonian compatibility; aggregate FAIL={FAIL}.")
    print(f"per_block: checked — two-block and tracial-state modular factorizations were executed, including the weighted-trace identity; aggregate FAIL={FAIL}.")
    print(f"lattice_wide: checked and not executed — no lattice law derives the required Gibbs/product hypothesis; the executed modular certificate leaves that bridge open with PASS={PASS}, FAIL={FAIL}.")

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
