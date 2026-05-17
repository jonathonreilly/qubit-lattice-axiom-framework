#!/usr/bin/env python3
"""
staggered_only_det_positivity_case_a_2026-05-17.py
---------------------------------------------------

Runner companion to
    docs/STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md

Numerical verification of the closed-form sub-theorem

    det(M_KS + m * I)  =  prod_{i=1}^{n/2}  ( m^2 + sigma_i^2 )  >  0

on the canonical staggered-Dirac Kogut-Susskind operator on a balanced
lattice block, for arbitrary SU(3) gauge background and any m > 0.

The runner verifies four load-bearing identities of the note's proof:

  V1.  Block decomposition (4) of M_KS in the eps-sorted basis:
       in that basis the diagonal blocks of M_KS are exactly zero,
       and the off-diagonal blocks satisfy lower-left = -upper-right^†.

  V2.  Hermiticity of gamma_5 * M from equation (7):
       (gamma_5 * M)^† = gamma_5 * M.

  V3.  Sign reconciliation (equations (12)-(15)):
       det(gamma_5 * M)  =  (-1)^{n/2}  ·  prod ( m^2 + sigma_i^2 ),
       det(gamma_5)       =  (-1)^{n/2},
       det(M)             =  prod ( m^2 + sigma_i^2 ).

  V4.  Strict positivity (18):
       det(M) > 0 across a range of m > 0 values and lattice sizes,
       and the lower bound det(M) >= m^n.

The runner is a verification of the load-bearing identities; the
closed-form derivation in the note is the load-bearing argument.

Conventions match the parent note
    docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md
and its parent runner
    scripts/axiom_first_reflection_positivity_check.py
(Exhibit E5 for {eps, M_KS} = 0; Exhibit E6 for det(M) >= 0 across the
canonical staggered+Wilson surface).
"""

from __future__ import annotations

import sys
import numpy as np
from numpy.linalg import det, svd, eigvalsh, matrix_rank


# ---------------------------------------------------------------------------
# Build the canonical Kogut-Susskind staggered-Dirac hop M_KS on (1+1)D
# with arbitrary SU(3) gauge background. Lattice sites are indexed
# (t, x) with t in {0, ..., L_t-1}, x in {0, ..., L_s-1}; both L_t and
# L_s are even (balanced staggered chirality).
# ---------------------------------------------------------------------------

def staggered_eps_1plus1d(L_t, L_s):
    """eps(t, x) = (-1)^(t + x) on a (1+1)D lattice."""
    eps = np.zeros(L_t * L_s, dtype=float)
    for t in range(L_t):
        for x in range(L_s):
            eps[t * L_s + x] = (-1) ** (t + x)
    return eps


def staggered_phases_1plus1d(L_t, L_s):
    """eta_t(x) = +1 (time direction first); eta_x(t) = (-1)^t."""
    return {
        "eta_t": lambda t, x: +1.0,
        "eta_x": lambda t, x: (-1.0) ** t,
    }


def random_su3_link():
    """Sample a random SU(3) matrix uniformly w.r.t. Haar measure (Ginibre + QR)."""
    z = np.random.randn(3, 3) + 1j * np.random.randn(3, 3)
    q, r = np.linalg.qr(z)
    # Fix the sign of det
    d = np.diag(np.diag(r) / np.abs(np.diag(r)))
    q = q @ d
    # Make det = 1
    q = q / np.linalg.det(q) ** (1.0 / 3.0)
    # Numerical safety: project onto SU(3)
    u, _, vh = np.linalg.svd(q)
    q = u @ vh
    q = q / np.linalg.det(q) ** (1.0 / 3.0)
    return q


def build_M_KS_su3_1plus1d(L_t, L_s, rng=None):
    """
    Build M_KS on (1+1)D with random SU(3) gauge links on every link.
    Returns the full matrix as a complex array of size (3 * L_t * L_s) x ...
    """
    if rng is None:
        rng = np.random.default_rng(0)
    eta = staggered_phases_1plus1d(L_t, L_s)
    N = L_t * L_s
    N_color = 3
    dim = N * N_color
    # gauge links: U_mu(t, x) for mu in {t, x}
    U_t = {}
    U_x = {}
    for t in range(L_t):
        for x in range(L_s):
            U_t[(t, x)] = sample_su3(rng)
            U_x[(t, x)] = sample_su3(rng)

    M = np.zeros((dim, dim), dtype=complex)

    def site_idx(t, x):
        return (t % L_t) * L_s + (x % L_s)

    def color_slice(s):
        return slice(s * N_color, (s + 1) * N_color)

    # M_KS = sum_{x, mu} (1/2) [
    #   eta_mu(x) * U_mu(x) * delta(x+mu, y) - eta_mu(x) * U_mu(x-mu)^† * delta(x-mu, y)
    # ]
    # Standard canonical Kogut-Susskind.
    for t in range(L_t):
        for x in range(L_s):
            s = site_idx(t, x)
            # mu = t
            tp = (t + 1) % L_t
            s_tp = site_idx(tp, x)
            sign_t = eta["eta_t"](t, x)
            M[color_slice(s), color_slice(s_tp)] += 0.5 * sign_t * U_t[(t, x)]
            M[color_slice(s_tp), color_slice(s)] += (
                -0.5 * sign_t * U_t[(t, x)].conj().T
            )
            # mu = x
            xp = (x + 1) % L_s
            s_xp = site_idx(t, xp)
            sign_x = eta["eta_x"](t, x)
            M[color_slice(s), color_slice(s_xp)] += 0.5 * sign_x * U_x[(t, x)]
            M[color_slice(s_xp), color_slice(s)] += (
                -0.5 * sign_x * U_x[(t, x)].conj().T
            )
    return M


def sample_su3(rng):
    """Sample SU(3) matrix from the Haar measure using QR of Ginibre."""
    z = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    q, r = np.linalg.qr(z)
    d = np.diag(np.diag(r) / np.abs(np.diag(r)))
    q = q @ d
    # Normalize det to 1
    det_q = np.linalg.det(q)
    q = q / det_q ** (1.0 / 3.0)
    # SVD project (numerical safety)
    u, _, vh = np.linalg.svd(q)
    q = u @ vh
    det_q = np.linalg.det(q)
    q = q / det_q ** (1.0 / 3.0)
    return q


def eps_diagonal_with_color(L_t, L_s, N_color=3):
    """Block eps to include color; eps acts trivially on color."""
    eps_site = staggered_eps_1plus1d(L_t, L_s)
    return np.repeat(eps_site, N_color)


def reorder_by_eps(M, eps_diag):
    """
    Permute the basis so that all +1 eps states come first, then all -1.
    Returns (M_perm, perm, n_plus, n_minus).
    """
    plus = np.where(eps_diag > 0)[0]
    minus = np.where(eps_diag < 0)[0]
    perm = np.concatenate([plus, minus])
    M_perm = M[np.ix_(perm, perm)]
    return M_perm, perm, len(plus), len(minus)


# ---------------------------------------------------------------------------
# V1: block decomposition of M_KS in the eps-sorted basis
# ---------------------------------------------------------------------------

def check_V1_block_decomposition(L_t=4, L_s=4, rng=None, tol=1e-10):
    print("\n--- V1: M_KS is purely off-diagonal in the eps-sorted basis ---")
    print(f"  L_t = {L_t}, L_s = {L_s}, N_color = 3")
    if rng is None:
        rng = np.random.default_rng(7)
    M_KS = build_M_KS_su3_1plus1d(L_t, L_s, rng=rng)
    eps = eps_diagonal_with_color(L_t, L_s)
    M_perm, perm, n_plus, n_minus = reorder_by_eps(M_KS, eps)
    assert n_plus == n_minus, f"Lattice not balanced: {n_plus} vs {n_minus}"
    # Diagonal blocks in eps-sorted basis must be zero
    upper_left = M_perm[:n_plus, :n_plus]
    lower_right = M_perm[n_plus:, n_plus:]
    ul_norm = float(np.max(np.abs(upper_left)))
    lr_norm = float(np.max(np.abs(lower_right)))
    # Off-diagonal: lower-left should equal -upper-right^†
    upper_right = M_perm[:n_plus, n_plus:]
    lower_left = M_perm[n_plus:, :n_plus]
    skew_err = float(np.max(np.abs(lower_left + upper_right.conj().T)))
    print(f"  ||upper_left||_max  = {ul_norm:.3e}")
    print(f"  ||lower_right||_max = {lr_norm:.3e}")
    print(f"  ||lower_left + upper_right^†||_max = {skew_err:.3e}")
    pass_diag = (ul_norm < tol) and (lr_norm < tol)
    pass_skew = skew_err < tol
    ok = pass_diag and pass_skew
    print(f"  V1 verdict: {'PASS' if ok else 'FAIL'}")
    return ok, M_KS, eps, M_perm, n_plus


# ---------------------------------------------------------------------------
# V2: gamma_5 * M is Hermitian (eq. 7)
# ---------------------------------------------------------------------------

def check_V2_gamma5_hermiticity(M_KS, eps, mass=0.5, tol=1e-10):
    print("\n--- V2: gamma_5 * M is Hermitian ---")
    print(f"  mass m = {mass}")
    dim = M_KS.shape[0]
    M = M_KS + mass * np.eye(dim, dtype=complex)
    eps_mat = np.diag(eps).astype(complex)
    g5M = eps_mat @ M
    err = float(np.max(np.abs(g5M - g5M.conj().T)))
    print(f"  ||gamma_5 M - (gamma_5 M)^†||_max = {err:.3e}")
    ok = err < tol
    print(f"  V2 verdict: {'PASS' if ok else 'FAIL'}")
    return ok, M


# ---------------------------------------------------------------------------
# V3: sign reconciliation eqs (12)-(15)
# ---------------------------------------------------------------------------

def check_V3_sign_reconciliation(M_KS, eps, M_perm, n_plus, mass=0.5, tol=1e-8):
    print("\n--- V3: sign reconciliation det(gamma_5 M) = (-1)^{n/2} * prod (m^2 + sigma^2) ---")
    print(f"  mass m = {mass}, n_plus = {n_plus}, n/2 = {n_plus}")
    dim = M_KS.shape[0]
    # Use the eps-sorted basis directly
    eps_perm = np.concatenate([
        np.ones(n_plus), -np.ones(n_plus)
    ]).astype(complex)
    # K = upper-right block of M_KS in eps-sorted basis
    K = M_perm[:n_plus, n_plus:]
    # Singular values of K
    sigma = svd(K, compute_uv=False)
    # m^2 + sigma_i^2
    factors = mass ** 2 + sigma ** 2
    prod_factors = float(np.prod(factors))
    # det(gamma_5 M) directly
    M_full_perm = M_perm + mass * np.eye(dim, dtype=complex)
    eps_mat_perm = np.diag(eps_perm)
    g5M = eps_mat_perm @ M_full_perm
    det_g5M = complex(det(g5M))
    sign = (-1) ** n_plus
    expected_det_g5M = sign * prod_factors
    err_g5M = abs(det_g5M.real - expected_det_g5M) / max(abs(expected_det_g5M), 1.0)
    im_ratio = abs(det_g5M.imag) / max(abs(det_g5M), 1.0)
    print(f"  det(gamma_5 M) computed:  {det_g5M.real:+.6e} + {det_g5M.imag:+.2e}i")
    print(f"  (-1)^(n/2) * prod (m^2 + sigma^2): {expected_det_g5M:+.6e}")
    print(f"  relative error: {err_g5M:.3e}, Im/|det| = {im_ratio:.2e}")
    pass_g5M = err_g5M < tol and im_ratio < tol

    # det(gamma_5) = (-1)^{n/2}
    det_eps = float(np.prod(eps_perm.real))
    expected_det_eps = sign
    print(f"  det(gamma_5) = det(eps) computed: {det_eps:+.0f}")
    print(f"  (-1)^(n/2) expected:               {expected_det_eps:+.0f}")
    pass_eps = abs(det_eps - expected_det_eps) < tol

    # det(M) = prod (m^2 + sigma_i^2)
    det_M = complex(det(M_full_perm))
    err_M = abs(det_M.real - prod_factors) / max(prod_factors, 1.0)
    im_ratio_M = abs(det_M.imag) / max(abs(det_M), 1.0)
    print(f"  det(M) computed:        {det_M.real:+.6e} + {det_M.imag:+.2e}i")
    print(f"  prod (m^2 + sigma^2):   {prod_factors:+.6e}")
    print(f"  relative error: {err_M:.3e}, Im/|det| = {im_ratio_M:.2e}")
    pass_M = err_M < tol and im_ratio_M < tol

    ok = pass_g5M and pass_eps and pass_M
    print(f"  V3 verdict: {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------------------
# V4: strict positivity det(M) > 0 across a parameter scan
# ---------------------------------------------------------------------------

def check_V4_strict_positivity(tol=1e-9):
    print("\n--- V4: det(M) > 0 across SU(3) gauge backgrounds and m > 0 ---")
    rng = np.random.default_rng(42)
    cases = []
    n_pass = 0
    n_total = 0
    for L_t in (4, 6):
        for L_s in (4, 6):
            for mass in (0.1, 0.3, 0.5, 1.0, 2.0):
                for seed in range(3):
                    sub_rng = np.random.default_rng(seed * 1000 + L_t * 100 + L_s * 10 + int(mass * 10))
                    M_KS = build_M_KS_su3_1plus1d(L_t, L_s, rng=sub_rng)
                    dim = M_KS.shape[0]
                    M = M_KS + mass * np.eye(dim, dtype=complex)
                    d = complex(det(M))
                    # Check eq. (16): det(M) = prod (m^2 + sigma_i^2)
                    eps = eps_diagonal_with_color(L_t, L_s)
                    M_perm, perm, n_plus, _ = reorder_by_eps(M_KS, eps)
                    K = M_perm[:n_plus, n_plus:]
                    sigma = svd(K, compute_uv=False)
                    expected = float(np.prod(mass ** 2 + sigma ** 2))
                    rel_err = abs(d.real - expected) / max(expected, 1.0)
                    im_ratio = abs(d.imag) / max(abs(d), 1.0)
                    # Strict positivity
                    strictly_positive = d.real > 0
                    # Lower bound det(M) >= m^n (Corollary C2)
                    n_sites = L_t * L_s * 3  # include color
                    lower_bound = mass ** n_sites
                    above_bound = d.real >= lower_bound - 1e-9 * lower_bound
                    n_total += 1
                    if rel_err < 1e-6 and im_ratio < 1e-6 and strictly_positive and above_bound:
                        n_pass += 1
                    cases.append((
                        L_t, L_s, mass, seed, d.real, expected,
                        rel_err, im_ratio, strictly_positive, lower_bound,
                        above_bound,
                    ))
    # Show first 8 cases for the log
    print(f"  Configurations checked: {n_total}")
    print(f"  {'L_t':>3} {'L_s':>3} {'m':>5} {'seed':>4}  det(M)         prod(m^2+sig^2)  rel_err  pos  >= m^n")
    for c in cases[:8]:
        L_t, L_s, mass, seed, d_real, expected, rel_err, im_ratio, sp, lb, ab = c
        print(
            f"  {L_t:3d} {L_s:3d} {mass:5.2f} {seed:4d}  "
            f"{d_real:+.4e}   {expected:+.4e}  {rel_err:.2e}   "
            f"{'+' if sp else '-'}    {'+' if ab else '-'}"
        )
    if len(cases) > 8:
        print(f"  ... ({len(cases) - 8} more cases checked)")
    print(f"  pass rate: {n_pass} / {n_total}")
    ok = n_pass == n_total
    print(f"  V4 verdict: {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main():
    print("=" * 72)
    print(" staggered_only_det_positivity_case_a_2026-05-17.py")
    print(" Companion runner to")
    print("   docs/STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md")
    print(" Verifies the closed-form factorisation")
    print("   det(M_KS + m * I) = prod_{i=1}^{n/2} (m^2 + sigma_i^2) > 0")
    print(" on the canonical staggered-Dirac with SU(3) gauge background.")
    print("=" * 72)

    np.random.seed(0)
    rng = np.random.default_rng(7)

    v1_pass, M_KS, eps, M_perm, n_plus = check_V1_block_decomposition(L_t=4, L_s=4, rng=rng)
    v2_pass, M_full = check_V2_gamma5_hermiticity(M_KS, eps, mass=0.5)
    v3_pass = check_V3_sign_reconciliation(M_KS, eps, M_perm, n_plus, mass=0.5)
    v4_pass = check_V4_strict_positivity()

    print()
    print("=" * 72)
    print(" SUMMARY")
    print("=" * 72)
    results = {
        "V1 (block decomp: M_KS purely off-diagonal in eps-sorted basis)": v1_pass,
        "V2 (gamma_5 M Hermitian)": v2_pass,
        "V3 (sign reconciliation det(g5 M) = (-1)^(n/2) * prod (m^2+sigma^2))": v3_pass,
        "V4 (strict positivity det(M) > 0 with lower bound m^n)": v4_pass,
    }
    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    for k, v in results.items():
        print(f"   {k}: {'PASS' if v else 'FAIL'}")
    print(f"\n   PASSED: {n_pass}/{n_total}")
    print()
    if n_pass == n_total:
        print(" verdict: closed-form sub-theorem identities reproduced numerically.")
        return 0
    else:
        print(" verdict: at least one identity failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
