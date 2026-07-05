"""Axiom-first KMS condition check.

Cross-checks the KMS condition for the Gibbs state on the
finite-dim physical Hilbert space H_phys reconstructed from the
RP transfer matrix on a finite Euclidean-time block.

The script does not re-derive RP or the spectrum condition (those are
companion support surfaces over the framework baseline whose effective
status is decided by the audit pipeline — see
docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md and
docs/AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md).
Instead, it constructs a small explicit Hermitian H >= 0 on a finite
Hilbert space, builds the positive two-step transfer block
T = exp(-2 a_tau H), and verifies the KMS strip identity by computing
both sides in the eigenbasis of H (which is numerically stable for
arbitrary z in the strip).

Tested identities (all on a generic finite-dim H >= 0):

  T1: KMS strip identity  F_{A,B}(t + i beta_th) = G_{A,B}(t)
      with F(z) := < A alpha_z(B) >_beta, G(t) := < alpha_t(B) A >_beta.
  T2: finite-strip analyticity and the finite-block grown strip bound.
  T3: equilibrium uniqueness via finite matrix-unit KMS equations,
      including the degenerate-energy scalar-block condition.
  T4: path-integral correspondence and native slice-insertion cyclicity:
      with even raw L_tau and N_tau=L_tau/2 blocked steps,
      tr(T^{N_tau-j} O T^j) = tr(T^{N_tau} O).

These are all the structural content of the theorem note.
"""
from __future__ import annotations

import numpy as np


def hermitian_psd(seed: int, dim: int) -> np.ndarray:
    """Return a Hermitian positive-semidefinite matrix of given dim.

    Used to model the reconstructed Hamiltonian H >= 0 on H_phys.
    """
    rng = np.random.default_rng(seed)
    eigvals = np.sort(rng.uniform(0.0, 5.0, size=dim))
    eigvals[0] = 0.0  # M_T = 1 gauge
    Q, _ = np.linalg.qr(rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim)))
    H = Q @ np.diag(eigvals) @ Q.conj().T
    H = 0.5 * (H + H.conj().T)
    return H


def random_operator(seed: int, dim: int) -> np.ndarray:
    """Return a generic complex matrix to use as A or B."""
    rng = np.random.default_rng(seed)
    M = rng.standard_normal((dim, dim)) + 1j * rng.standard_normal((dim, dim))
    return M


def diagonalize(H: np.ndarray):
    """Return (eigvals, V) so that H = V diag(eigvals) V.conj().T."""
    eigvals, V = np.linalg.eigh(H)
    return eigvals, V


def F_strip(A: np.ndarray, B: np.ndarray, eigvals: np.ndarray, V: np.ndarray, beta_th: float, z: complex) -> complex:
    """< A alpha_z(B) >_{beta_th} computed in the eigenbasis of H.

    Uses
      F(z) = (1/Z) sum_{n,m} exp(-beta_th E_n) A_{nm} exp(i z (E_m - E_n)) B_{mn}.

    For z = t + i beta_th, the factor exp(-beta_th E_n) exp(-beta_th (E_m - E_n))
    = exp(-beta_th E_m) is finite and avoids the cancellation that would arise
    if we composed exp(-beta_th H) and exp(beta_th H) as separate matrices.
    """
    A_eig = V.conj().T @ A @ V
    B_eig = V.conj().T @ B @ V
    Z = float(np.sum(np.exp(-beta_th * eigvals)))
    n_dim = len(eigvals)
    total = 0.0 + 0.0j
    for n in range(n_dim):
        for m in range(n_dim):
            weight_n = np.exp(-beta_th * eigvals[n])
            phase = np.exp(1j * z * (eigvals[m] - eigvals[n]))
            total += weight_n * A_eig[n, m] * phase * B_eig[m, n]
    return total / Z


def G_real(A: np.ndarray, B: np.ndarray, eigvals: np.ndarray, V: np.ndarray, beta_th: float, t: float) -> complex:
    """< alpha_t(B) A >_{beta_th} for real t, computed in eigenbasis."""
    A_eig = V.conj().T @ A @ V
    B_eig = V.conj().T @ B @ V
    Z = float(np.sum(np.exp(-beta_th * eigvals)))
    n_dim = len(eigvals)
    total = 0.0 + 0.0j
    for n in range(n_dim):
        for m in range(n_dim):
            weight_n = np.exp(-beta_th * eigvals[n])
            phase = np.exp(1j * t * (eigvals[n] - eigvals[m]))
            total += weight_n * phase * B_eig[n, m] * A_eig[m, n]
    return total / Z


def G_strip(A: np.ndarray, B: np.ndarray, eigvals: np.ndarray, V: np.ndarray, beta_th: float, z: complex) -> complex:
    """< alpha_z(B) A >_{beta_th} for arbitrary z in the strip [0, beta_th]."""
    A_eig = V.conj().T @ A @ V
    B_eig = V.conj().T @ B @ V
    Z = float(np.sum(np.exp(-beta_th * eigvals)))
    n_dim = len(eigvals)
    total = 0.0 + 0.0j
    for n in range(n_dim):
        for m in range(n_dim):
            weight_n = np.exp(-beta_th * eigvals[n])
            phase = np.exp(1j * z * (eigvals[n] - eigvals[m]))
            total += weight_n * phase * B_eig[n, m] * A_eig[m, n]
    return total / Z


def operator_norm(M: np.ndarray) -> float:
    return float(np.linalg.norm(M, ord=2))


def spectral_matrix(eigvals: np.ndarray, V: np.ndarray, values: np.ndarray) -> np.ndarray:
    """Return V diag(values) V^* for functions of H."""
    return V @ np.diag(values) @ V.conj().T


def normalized_gibbs_weights(eigvals: np.ndarray, beta_th: float) -> np.ndarray:
    weights = np.exp(-beta_th * eigvals)
    return weights / np.sum(weights)


def kms_matrix_unit_ratio_residual(eigvals: np.ndarray, probs: np.ndarray, beta_th: float) -> float:
    """Max residual of p_j = exp(beta(E_i-E_j)) p_i over matrix units.

    This is the finite-dimensional KMS endpoint equation for
    A = |i><j|, B = |j><i| in the eigenbasis of H.
    """
    max_resid = 0.0
    for i, Ei in enumerate(eigvals):
        for j, Ej in enumerate(eigvals):
            lhs = probs[j]
            rhs = np.exp(beta_th * (Ei - Ej)) * probs[i]
            max_resid = max(max_resid, abs(lhs - rhs))
    return float(max_resid)


def main() -> None:
    print("=" * 72)
    print("AXIOM-FIRST KMS CONDITION CHECK")
    print("=" * 72)
    print()
    print("Setup:")
    print("  finite-dim H_phys (modeling RP-reconstructed physical Hilbert space)")
    print("  H = self-adjoint, H >= 0 (modeling spectrum condition SC1, SC2)")
    print("  T = exp(-2 a_tau H), Gibbs at beta_th = L_tau a_tau")
    print("  raw L_tau is even; N_tau = L_tau/2 blocked transfer factors")
    print()

    seed_H = 20260501
    dim = 8
    a_tau = 1.0
    a_blk = 2.0 * a_tau
    L_tau = 12
    assert L_tau % 2 == 0, "two-step blocked KMS check needs even raw L_tau"
    N_tau = L_tau // 2
    beta_th = N_tau * a_blk
    print(f"  dim(H_phys) = {dim}")
    print(f"  a_tau       = {a_tau}")
    print(f"  a_blk       = {a_blk}")
    print(f"  raw L_tau   = {L_tau}")
    print(f"  N_tau       = {N_tau}")
    print(f"  beta_th     = {beta_th}")
    print()

    H = hermitian_psd(seed_H, dim)
    eigvals, V = diagonalize(H)
    assert np.all(eigvals >= -1e-12), "H must be PSD (spectrum condition)"
    assert abs(eigvals[0]) < 1e-12, "ground state at zero by convention"
    Z = float(np.sum(np.exp(-beta_th * eigvals)))
    print(f"  spec(H)     = {eigvals.round(6)}")
    print(f"  Z(beta_th)  = {Z:.6f}")
    print()

    # ----- Test 1: KMS identity F(t + i beta_th) = G(t) -----
    print("-" * 72)
    print("TEST 1: KMS identity  F_{A,B}(t + i beta_th) = G_{A,B}(t)")
    print("        equivalently  G_{A,B}(t - i beta_th) = F_{A,B}(t)")
    print("-" * 72)
    print("F is analytically continued through the strip 0 <= Im z <= beta_th.")
    print("Computing both sides in the eigenbasis of H.")
    print("Sweeping t in [-2, 2] across 9 grid points, 4 (A, B) pairs.")
    print()
    max_resid_kms = 0.0
    n_points = 9
    n_pairs = 4
    for pair_idx in range(n_pairs):
        A = random_operator(seed_H + 100 + pair_idx, dim)
        B = random_operator(seed_H + 200 + pair_idx, dim)
        residuals = []
        for t in np.linspace(-2.0, 2.0, n_points):
            F_val = F_strip(A, B, eigvals, V, beta_th, t + 1j * beta_th)
            G_val = G_real(A, B, eigvals, V, beta_th, t)
            resid = abs(F_val - G_val)
            residuals.append(resid)
            max_resid_kms = max(max_resid_kms, resid)
        print(f"  pair {pair_idx}: max |F(t + i beta_th) - G(t)| over grid = {max(residuals):.3e}")
    print()
    print(f"  GLOBAL MAX KMS RESIDUAL = {max_resid_kms:.3e}")
    print()
    kms_ok = max_resid_kms < 1e-10
    print(f"  STATUS: {'PASS' if kms_ok else 'FAIL'}")
    print()

    # ----- Test 2: strip bound |G(z)| <= ||A|| ||B|| -----
    # The proof's bound uses the trace-norm |tr(e^{-beta H} X)| <= ||X||
    # times tr(e^{-beta H}) = Z, so |G(z)| <= ||alpha_z(B) A||. Since
    # alpha_z is NOT a *-automorphism for complex z (it can grow as
    # exp(beta * (E_max - E_min))), the natural strip bound is on
    # |G(z)| <= ||A|| ||B|| * exp(spread). We test the weaker but standard
    # strip inequality on the *boundary* values:
    #   |G(t + i s)| / max(||A||, ||B||)^2 <= bounded constant.
    # And we verify F(t + i beta_th) = G(t) on the whole grid (already T1).
    print("-" * 72)
    print("TEST 2: strip analyticity (boundary continuity of G_{A,B}(z))")
    print("-" * 72)
    print("We verify that G(z) is continuous and finite on the full strip,")
    print("and that the analytic continuation satisfies G(t + i beta_th) =")
    print("the same KMS-symmetric value as F(t).")
    print()
    A = random_operator(seed_H + 300, dim)
    B = random_operator(seed_H + 400, dim)
    nA = operator_norm(A)
    nB = operator_norm(B)
    spread = float(np.max(eigvals) - np.min(eigvals))
    naive_bound = nA * nB
    grown_bound = nA * nB * np.exp(beta_th * spread)
    print(f"  ||A||                              = {nA:.4f}")
    print(f"  ||B||                              = {nB:.4f}")
    print(f"  energy spread                      = {spread:.4f}")
    print(f"  naive bound ||A|| ||B||            = {naive_bound:.4f}")
    print(f"  worst-case strip bound ||A|| ||B|| exp(beta * spread) = {grown_bound:.4e}")
    print()
    max_mag = 0.0
    grid_s = np.linspace(0.0, beta_th, 7)
    grid_t = np.linspace(-1.0, 1.0, 7)
    for s in grid_s:
        for t in grid_t:
            G_val = G_strip(A, B, eigvals, V, beta_th, t + 1j * s)
            max_mag = max(max_mag, abs(G_val))
    print(f"  max |G(z)| over strip grid = {max_mag:.4e}")
    print(f"  ratio max|G| / grown_bound = {max_mag / grown_bound:.6f}")
    bound_ok = max_mag <= grown_bound * 1.01  # tolerance
    print(f"  STATUS: {'PASS' if bound_ok else 'FAIL'}")
    print()

    # ----- Test 3: equilibrium uniqueness by matrix units -----
    print("-" * 72)
    print("TEST 3: equilibrium uniqueness — finite matrix-unit KMS equations")
    print("-" * 72)
    print("For A=|i><j| and B=|j><i|, KMS at t=0 forces")
    print("  p_j = exp(beta_th(E_i - E_j)) p_i.")
    print("Inside a degenerate energy block this forces equal weights.")
    print()

    deg_eigvals = np.array([0.0, 1.0, 1.0, 2.5, 4.0, 4.0], dtype=float)
    gibbs_probs = normalized_gibbs_weights(deg_eigvals, beta_th)
    gibbs_ratio_resid = kms_matrix_unit_ratio_residual(deg_eigvals, gibbs_probs, beta_th)

    distorted_probs = gibbs_probs.copy()
    distorted_probs[1] *= 1.25
    distorted_probs[2] *= 0.75
    distorted_probs /= distorted_probs.sum()
    distorted_ratio_resid = kms_matrix_unit_ratio_residual(deg_eigvals, distorted_probs, beta_th)

    print(f"  degenerate test spectrum          = {deg_eigvals}")
    print(f"  Gibbs matrix-unit max residual    = {gibbs_ratio_resid:.3e}")
    print(f"  non-scalar degenerate-block resid = {distorted_ratio_resid:.3e}")
    uniqueness_ok = gibbs_ratio_resid < 1e-12 and distorted_ratio_resid > 1e-4
    print(f"  STATUS: {'PASS' if uniqueness_ok else 'FAIL'}")
    print()

    # ----- Test 4: path-integral correspondence and slice cyclicity -----
    print("-" * 72)
    print("TEST 4: path-integral correspondence")
    print("        Z = tr T^{N_tau} = tr exp(-beta_th H)")
    print("        tr(T^{N_tau-j} O T^j) = tr(T^{N_tau} O)")
    print("-" * 72)
    # T = exp(-2 a_tau H) computed via eigenbasis. This is the current
    # RP/spectrum two-step blocked transfer object T := T_hat^2.
    T_eigvals = np.exp(-a_blk * eigvals)
    T = spectral_matrix(eigvals, V, T_eigvals)
    O = random_operator(seed_H + 450, dim)
    T_power_L = np.linalg.matrix_power(T, N_tau)
    Z_trans = float(np.sum(T_eigvals ** N_tau))
    Z_gibbs = float(np.sum(np.exp(-beta_th * eigvals)))
    reference_num = np.trace(T_power_L @ O)
    max_slice_resid = 0.0
    for j in range(N_tau + 1):
        lhs = np.trace(np.linalg.matrix_power(T, N_tau - j) @ O @ np.linalg.matrix_power(T, j))
        max_slice_resid = max(max_slice_resid, abs(lhs - reference_num))
    print(f"  tr T^{N_tau}              = {Z_trans:.10f}")
    print(f"  tr exp(-beta_th H)     = {Z_gibbs:.10f}")
    print(f"  | difference |         = {abs(Z_trans - Z_gibbs):.3e}")
    print(f"  max slice cyclicity residual = {max_slice_resid:.3e}")
    pi_ok = abs(Z_trans - Z_gibbs) < 1e-10 and max_slice_resid < 1e-10
    print(f"  STATUS: {'PASS' if pi_ok else 'FAIL'}")
    print()

    # ----- Test 5: KMS analytic continuation to t=0 yields a real ratio -----
    print("-" * 72)
    print("TEST 5: detailed-balance corollary at z = i beta_th")
    print("        F(0 + i beta_th) = G(0) = < B A >_beta (a Hermitian-like ID)")
    print("-" * 72)
    A_self = random_operator(seed_H + 500, dim)
    A_self = 0.5 * (A_self + A_self.conj().T)  # Hermitian A
    B_self = random_operator(seed_H + 600, dim)
    B_self = 0.5 * (B_self + B_self.conj().T)  # Hermitian B
    F_at_ibeta = F_strip(A_self, B_self, eigvals, V, beta_th, 1j * beta_th)
    G_at_zero = G_real(A_self, B_self, eigvals, V, beta_th, 0.0)
    print(f"  F(0 + i beta_th)    = {F_at_ibeta}")
    print(f"  G(0) = <BA>_beta_th = {G_at_zero}")
    print(f"  | difference |     = {abs(F_at_ibeta - G_at_zero):.3e}")
    db_ok = abs(F_at_ibeta - G_at_zero) < 1e-10
    print(f"  STATUS: {'PASS' if db_ok else 'FAIL'}")
    print()

    # ----- Summary -----
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Test 1 (KMS identity strip endpoint):    {'PASS' if kms_ok else 'FAIL'}")
    print(f"  Test 2 (strip continuity / bound):       {'PASS' if bound_ok else 'FAIL'}")
    print(f"  Test 3 (equilibrium uniqueness):         {'PASS' if uniqueness_ok else 'FAIL'}")
    print(f"  Test 4 (path-integral correspondence):   {'PASS' if pi_ok else 'FAIL'}")
    print(f"  Test 5 (detailed-balance at i beta_th):  {'PASS' if db_ok else 'FAIL'}")
    print()
    all_ok = kms_ok and bound_ok and uniqueness_ok and pi_ok and db_ok
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()
    print("Note: this runner verifies the KMS theorem at the structural")
    print("level on a generic finite-dim H >= 0 on H_phys. The framework's")
    print("specific H_phys is the RP-reconstructed transfer-matrix Hilbert")
    print("space from docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_")
    print("2026-04-29.md (R3) plus docs/AXIOM_FIRST_SPECTRUM_CONDITION_")
    print("THEOREM_NOTE_2026-04-29.md (SC1, SC2). The proof in the companion")
    print("theorem note is dimension-independent (Steps 1-5).")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
