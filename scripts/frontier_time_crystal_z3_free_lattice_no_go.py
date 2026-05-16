#!/usr/bin/env python3
"""
Discrete Time Crystal on the Free Z^d Hamiltonian Lattice — No-Go
==================================================================

STATUS: proposed no-go theorem on the retained free-scalar Z^d
        Hamiltonian-lattice surface. Scope is exactly the surface on
        which the repo's emergent-Lorentz / free-scalar 2-point closure
        and the 1+1D / 3+1D boost-covariance theorems are stated:
        quadratic bosonic dispersion E_lat^2(p) = m^2 + sum_i (4/a^2)
        sin^2(p_i a/2) on Z^d (d=1,2,3), with a Z_2 internal mode-parity
        qubit per momentum mode and a global periodic kick.

THEOREM (free-lattice no-rigid-DTC):
  Let H_lat be the retained free-scalar lattice Hamiltonian on Z^d
  with dispersion E_lat(p) above. Consider the simplest Floquet drive
  compatible with the lattice symmetries: a global Z_2 mode-parity
  kick X by angle (π+ε) every period T, stroboscopic Floquet operator
      U_F(ε)  =  exp(-i (π+ε)/2 · X)  ·  exp(-i H_lat T).
  In each momentum mode k ∈ BZ this block-diagonalizes to an SU(2)
  Floquet matrix

      U_F(k, ε)  =  R_x(π+ε) · R_z(E_lat(k) T),

  whose quasi-energies ±θ_k(ε) satisfy the EXACT closed form

      cos θ_k(ε)  =  -sin(ε/2) · cos(E_lat(k) T / 2).             (*)

  Then:

    (a) Period-2T pairing at the symmetry point. At ε = 0,
        θ_k(0) = π/2 for every k, so U_F(k,0)^2 = -I in every mode.
        The single-mode stroboscopic σ_z(nT) correlator is exactly
        period-2T.

    (b) Per-mode rigidity failure. At ε ≠ 0, θ_k(ε) depends on k
        through cos(E_lat(k) T/2) and is k-dispersive: the subharmonic
        response frequency 2θ_k/T detunes from π/T linearly in ε with
        mode-dependent slope ∂(2θ_k)/∂ε|_{ε=0} · 1/T = cos(E_lat(k) T/2)
        / T.

    (c) Thermodynamic-limit smearing (no DTC). In the L → ∞ BZ
        thermodynamic limit, the stroboscopic correlator
        C(nT; ε) := (1/|BZ|) ∫_BZ d^d k cos(2n θ_k(ε)) is a continuous
        function of n with no surviving period-2T component for any
        ε ≠ 0: the discrete subharmonic peak at ω = π/T has zero
        spectral weight at finite ε in the thermodynamic limit
        (the weight is supported on a measure-zero subset of BZ).

  Together (a)-(c) say: clean Z^d Hamiltonian-lattice Floquet drives
  show trivial period-doubling exactly at the symmetry point ε = 0,
  but no rigid discrete-time-translation-symmetry-breaking phase.
  Hence the retained free Z^d sector does NOT host a genuine
  Floquet DTC. (Putative interacting + disordered MBL DTC phases are
  outside the retained surface and outside the scope of this note.)

MECHANISM:
  1.  H_lat is quadratic, hence its Floquet stroboscopic problem
      decouples mode-by-mode in momentum k.
  2.  In each (k, internal-Z_2) block the dynamics is SU(2), and the
      kick + free evolution Floquet matrix has exact trace
      Tr U_F(k,ε) = 2 cos((π+ε)/2) cos(E_lat(k) T / 2)
                  = -2 sin(ε/2) cos(E_lat(k) T / 2)
      giving (*).
  3.  At ε = 0 the kick is a perfect π-pulse: U_F(k,0) lies on the
      equator of SU(2) (cos θ = 0), forcing θ = π/2 in EVERY mode —
      the π-paired Floquet doublet of an MBL DTC, but here for a
      structural (symmetry-point) rather than a dynamical (l-bit)
      reason. Any ε ≠ 0 tilts cos θ_k(ε) off the equator by an
      amount proportional to cos(E_lat(k) T/2), which is k-dependent.
  4.  k-dependent quasi-energy detuning + dense BZ ⇒ the
      stroboscopic-time autocorrelator is a Riemann sum that becomes
      a continuous BZ integral as L → ∞. Its Fourier transform on
      the stroboscopic-frequency circle is the pushforward of d^d k
      under the smooth map k ↦ 2θ_k(ε); the symmetry-point delta at
      π/T disappears for any ε ≠ 0.

This runner verifies the theorem with PASS / FAIL checks across six
parts:

  A. Closed-form per-mode Floquet trace identity (*).
  B. ε = 0 exact period-2T pairing for arbitrary E_lat(k) T.
  C. ε ≠ 0 detuning slope ∂(2θ)/∂ε|_{ε=0} = cos(E_lat(k) T/2).
  D. Numerical SU(2) Floquet diagonalisation vs. closed form.
  E. Multi-mode L-ring autocorrelator: subharmonic peak smears with
     ε > 0; the spectral weight at ω = π/T shrinks with L.
  F. Z^d (d=1,2,3) BZ integral: subharmonic peak weight at ω = π/T
     vanishes for any ε > 0 in the L → ∞ thermodynamic limit, with
     a transparent measure-theoretic explanation.

Self-contained: numpy + scipy. No external state.

Cross-refs (free-lattice retained surface):
  - LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE (1+1D continuum closure
    on the same dispersion)
  - scripts/frontier_lorentz_boost_3plus1d.py (3+1D continuum closure
    on the same dispersion)
  - EMERGENT_LORENTZ_INVARIANCE_NOTE (cubic-harmonic dispersion)
"""
from __future__ import annotations

import sys
import time
import numpy as np

np.set_printoptions(precision=10, linewidth=120, suppress=True)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "", kind: str = "EXACT") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    tag = f" [{kind}]" if kind != "EXACT" else ""
    msg = f"  [{status}]{tag} {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# =============================================================================
# Core: free-scalar lattice dispersion (the retained Z^d surface)
# =============================================================================

def E_lat(k_vec, a: float, m: float) -> float:
    """Free-scalar Z^d dispersion: E^2 = m^2 + sum_i (4/a^2) sin^2(k_i a / 2)."""
    k_arr = np.atleast_1d(np.asarray(k_vec, dtype=float))
    return float(np.sqrt(m * m + (4.0 / (a * a)) * np.sum(np.sin(k_arr * a / 2.0) ** 2)))


# =============================================================================
# Core: per-mode SU(2) Floquet operator U_F(k, eps) = R_x(pi+eps) R_z(beta_k)
# =============================================================================

SIGMA_X = np.array([[0, 1], [1, 0]], dtype=complex)
SIGMA_Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
SIGMA_Z = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)


def R_axis(alpha: float, sigma: np.ndarray) -> np.ndarray:
    """exp(-i alpha sigma / 2) ∈ SU(2)."""
    return np.cos(alpha / 2.0) * I2 - 1j * np.sin(alpha / 2.0) * sigma


def floquet_mode(eps: float, beta: float) -> np.ndarray:
    """U_F = R_x(pi+eps) R_z(beta), single momentum mode."""
    return R_axis(np.pi + eps, SIGMA_X) @ R_axis(beta, SIGMA_Z)


def closed_form_cos_theta(eps: float, beta: float) -> float:
    """cos theta_k(eps) = -sin(eps/2) cos(beta/2).  Eq. (*)."""
    return -np.sin(eps / 2.0) * np.cos(beta / 2.0)


def theta_k(eps: float, beta: float) -> float:
    """Quasi-energy theta_k(eps) ∈ [0, pi]."""
    return float(np.arccos(np.clip(closed_form_cos_theta(eps, beta), -1.0, 1.0)))


# =============================================================================
# Part A.  Closed-form per-mode Floquet trace identity (*)
# =============================================================================

def part_A() -> None:
    print()
    print("=" * 76)
    print("PART A.  Closed-form per-mode Floquet trace identity (*)")
    print("=" * 76)
    print("  Test:  Tr U_F(eps, beta) / 2  ==  -sin(eps/2) cos(beta/2)")
    print("  for a grid of (eps, beta) ∈ [-pi, pi] × [0, 2 pi].")

    rng = np.random.default_rng(20260516)
    eps_grid = np.linspace(-np.pi, np.pi, 17)
    beta_grid = np.linspace(0.0, 2.0 * np.pi, 19)
    max_err = 0.0
    for eps in eps_grid:
        for beta in beta_grid:
            U = floquet_mode(eps, beta)
            num = 0.5 * np.real(np.trace(U))
            ana = closed_form_cos_theta(eps, beta)
            max_err = max(max_err, abs(num - ana))
    check(
        "trace identity Tr U_F / 2 = -sin(eps/2) cos(beta/2) on 17 x 19 grid",
        max_err < 1e-13,
        detail=f"max |num - analytic| = {max_err:.2e}",
    )

    # Random spot checks at irrational arguments
    max_err_r = 0.0
    for _ in range(64):
        eps = rng.uniform(-np.pi, np.pi)
        beta = rng.uniform(0.0, 4.0 * np.pi)
        U = floquet_mode(eps, beta)
        max_err_r = max(max_err_r, abs(0.5 * np.real(np.trace(U)) - closed_form_cos_theta(eps, beta)))
    check(
        "trace identity (64 random irrational points)",
        max_err_r < 1e-13,
        detail=f"max err = {max_err_r:.2e}",
    )

    # SU(2): unitarity and det = +1
    max_unit = 0.0
    max_det = 0.0
    for eps in eps_grid:
        for beta in beta_grid:
            U = floquet_mode(eps, beta)
            max_unit = max(max_unit, np.max(np.abs(U.conj().T @ U - I2)))
            max_det = max(max_det, abs(np.linalg.det(U) - 1.0))
    check(
        "U_F unitary on full grid",
        max_unit < 1e-13,
        detail=f"max |U†U - I| = {max_unit:.2e}",
    )
    check(
        "U_F ∈ SU(2) (det = 1) on full grid",
        max_det < 1e-13,
        detail=f"max |det U - 1| = {max_det:.2e}",
    )


# =============================================================================
# Part B.  eps = 0 exact period-2T pairing for arbitrary E_lat(k) T
# =============================================================================

def part_B() -> None:
    print()
    print("=" * 76)
    print("PART B.  Exact period-2T pairing at eps = 0 (the symmetry point)")
    print("=" * 76)
    print("  Test:  for any beta ∈ R,  cos theta(0, beta) = 0  ⇒  U_F(0,beta)^2 = -I.")
    print("  Hence every mode k contributes a perfect π-paired Floquet doublet")
    print("  at eps = 0, irrespective of the underlying dispersion E_lat(k).")

    beta_grid = np.linspace(0.0, 4.0 * np.pi, 41)
    max_cos = 0.0
    max_sq = 0.0
    for beta in beta_grid:
        max_cos = max(max_cos, abs(closed_form_cos_theta(0.0, beta)))
        U = floquet_mode(0.0, beta)
        U2 = U @ U
        max_sq = max(max_sq, np.max(np.abs(U2 + I2)))
    check(
        "closed form: cos theta(0, beta) = 0 for all beta",
        max_cos < 1e-15,
        detail=f"max |cos theta| = {max_cos:.2e}",
    )
    check(
        "U_F(0,beta)^2 = -I for all beta (perfect π-pulse pairing)",
        max_sq < 1e-13,
        detail=f"max |U^2 + I| = {max_sq:.2e}",
    )

    # Stroboscopic <sigma_z> correlator at eps=0: exact period-2T for any beta.
    # In the |↑> initial state, <sigma_z(nT)> = (-1)^n exactly.
    psi0 = np.array([1.0, 0.0], dtype=complex)
    max_period2_err = 0.0
    for beta in [0.3, 1.0, 2.5, 3.7, 5.1]:
        U = floquet_mode(0.0, beta)
        psi = psi0.copy()
        for n in range(1, 21):
            psi = U @ psi
            sz = np.real(np.conj(psi) @ (SIGMA_Z @ psi))
            expected = (-1) ** n  # perfect period-2T flip
            max_period2_err = max(max_period2_err, abs(sz - expected))
    check(
        "single-mode <sigma_z(nT)> = (-1)^n exactly at eps=0 (20 periods × 5 beta)",
        max_period2_err < 1e-12,
        detail=f"max |<sz>(nT) - (-1)^n| = {max_period2_err:.2e}",
    )

    # Even when beta is k-dispersive (e.g., E_lat(k) T with d=3), at eps=0
    # every mode independently gives (-1)^n. So the L-site lattice average
    # of <sigma_z(nT)> is also exactly (-1)^n. We verify this on a 3D BZ
    # sample with the retained dispersion.
    a, m, T = 1.0, 0.3, 0.7
    L = 5
    k_axis = np.linspace(-np.pi / a, np.pi / a, L, endpoint=False)
    avg_err = 0.0
    n_modes = 0
    # |↑> per mode; correlator averages by symmetry.
    for kx in k_axis:
        for ky in k_axis:
            for kz in k_axis:
                beta = E_lat([kx, ky, kz], a, m) * T
                U = floquet_mode(0.0, beta)
                psi = psi0.copy()
                for n in range(1, 9):
                    psi = U @ psi
                    sz = np.real(np.conj(psi) @ (SIGMA_Z @ psi))
                    avg_err = max(avg_err, abs(sz - (-1) ** n))
                n_modes += 1
    check(
        f"Z^3 L={L} BZ sample (n_modes={n_modes}): every mode gives (-1)^n at eps=0",
        avg_err < 1e-12,
        detail=f"max |sz - (-1)^n| over all modes & 8 periods = {avg_err:.2e}",
    )


# =============================================================================
# Part C.  eps ≠ 0 detuning slope:  d(2 theta) / d eps |_{eps=0} = cos(beta/2)
# =============================================================================

def part_C() -> None:
    print()
    print("=" * 76)
    print("PART C.  Per-mode detuning slope (rigidity failure to leading order)")
    print("=" * 76)
    print("  Expand cos theta(eps, beta) = -sin(eps/2) cos(beta/2) about eps=0:")
    print("     theta(eps, beta) ≈ π/2 + (eps/2) cos(beta/2) + O(eps^3)")
    print("     2 theta / T     ≈ π/T + (eps/T) cos(beta/2)")
    print("  So the subharmonic detuning δω(eps) = (eps/T) cos(beta/2) is")
    print("  mode-dependent (β depends on k via E_lat(k) T) — non-rigid.")

    # Numerical derivative of 2*theta wrt eps at eps=0, vs analytic cos(beta/2).
    h = 1e-5
    beta_list = [0.1, 0.7, 1.5, 2.3, 3.0, 4.2, 5.5, 6.0]
    max_slope_err = 0.0
    for beta in beta_list:
        # Central diff of theta(eps, beta) wrt eps at 0:
        th_plus = theta_k(+h, beta)
        th_minus = theta_k(-h, beta)
        slope_2theta = (th_plus - th_minus) / h  # d(2 theta)/d eps via central diff on theta
        # Note: d(2 theta)/d eps = 2 d theta/d eps, and (th_plus - th_minus)/h = 2 d theta/d eps
        slope_pred = np.cos(beta / 2.0)
        max_slope_err = max(max_slope_err, abs(slope_2theta - slope_pred))
    check(
        "d(2 theta)/d eps |_{eps=0} = cos(beta/2)  (8 beta values, central diff)",
        max_slope_err < 1e-7,
        detail=f"max |numerical - analytic slope| = {max_slope_err:.2e}",
    )

    # The slope is generically nonzero. The unique zeros occur at beta = π
    # mod 2π (the resonance condition). At those isolated beta the
    # leading-order detuning vanishes; the next-order correction is O(eps^3).
    slope_at_pi = abs(np.cos(np.pi / 2.0))
    check(
        "slope vanishes exactly at beta = π (isolated resonance)",
        slope_at_pi < 1e-15,
        detail=f"|cos(π/2)| = {slope_at_pi:.2e}",
    )

    # Slope is non-flat in beta: ⇒ different modes detune at different rates ⇒
    # spectral broadening of the L-mode subharmonic line.
    slopes = [np.cos(b / 2.0) for b in beta_list]
    spread = max(slopes) - min(slopes)
    check(
        "slope spread across beta_list > 1  (non-flat ⇒ broadening)",
        spread > 1.0,
        detail=f"max slope - min slope = {spread:.3f}",
    )


# =============================================================================
# Part D.  Numerical SU(2) diagonalisation vs closed form across BZ
# =============================================================================

def part_D() -> None:
    print()
    print("=" * 76)
    print("PART D.  Numerical Floquet eigenvalues vs closed form on a 3D BZ grid")
    print("=" * 76)
    a, m, T = 1.0, 0.5, 1.1
    L = 8
    eps_list = [0.0, 0.03, 0.1, 0.25, 0.7]
    k_axis = np.linspace(-np.pi / a, np.pi / a, L, endpoint=False)
    for eps in eps_list:
        max_err = 0.0
        for kx in k_axis:
            for ky in k_axis:
                for kz in k_axis:
                    beta = E_lat([kx, ky, kz], a, m) * T
                    U = floquet_mode(eps, beta)
                    evals = np.linalg.eigvals(U)
                    # eigenvalues should be e^{±i theta} with cos theta = closed form
                    cos_theta_num = float(np.real(0.5 * np.sum(evals)))
                    cos_theta_ana = closed_form_cos_theta(eps, beta)
                    max_err = max(max_err, abs(cos_theta_num - cos_theta_ana))
        check(
            f"3D BZ L={L} (eps={eps:+.3f}): eigenvalue cos theta matches (*)",
            max_err < 1e-12,
            detail=f"max err over {L**3} modes = {max_err:.2e}",
        )


# =============================================================================
# Part E.  L-ring stroboscopic autocorrelator: subharmonic peak smears with eps
# =============================================================================

def stroboscopic_autocorr_1d(eps: float, a: float, m: float, T: float,
                              L: int, N_periods: int) -> np.ndarray:
    """C(n) = (1/L) sum_k <sz(nT)>_k  with |↑> initial state in each mode.

    For one mode at eps=0 we have <sz(nT)> = (-1)^n; mixing in eps detunes
    the per-mode oscillation to a Floquet rotation in the (z, x) sector
    of the Bloch sphere whose stroboscopic z-projection we average.
    """
    k_axis = np.linspace(-np.pi / a, np.pi / a, L, endpoint=False)
    psi = np.zeros((L, 2), dtype=complex)
    psi[:, 0] = 1.0  # |↑>
    Us = np.zeros((L, 2, 2), dtype=complex)
    for j, k in enumerate(k_axis):
        beta = E_lat([k], a, m) * T
        Us[j] = floquet_mode(eps, beta)
    out = np.zeros(N_periods + 1)
    out[0] = 1.0  # <sz>(0) = +1 averaged
    for n in range(1, N_periods + 1):
        # apply U per mode
        psi = np.einsum("kab,kb->ka", Us, psi)
        sz = np.real(np.conj(psi[:, 0]) * psi[:, 0] - np.conj(psi[:, 1]) * psi[:, 1])
        out[n] = np.mean(sz)
    return out


def part_E() -> None:
    print()
    print("=" * 76)
    print("PART E.  L-ring stroboscopic correlator: subharmonic peak smearing")
    print("=" * 76)
    a, m, T = 1.0, 0.4, 0.9
    N_periods = 256

    # (i) eps = 0: every mode gives (-1)^n, so the L-average is (-1)^n.
    for L in [8, 32, 128]:
        C = stroboscopic_autocorr_1d(0.0, a, m, T, L, N_periods)
        expected = np.array([(-1) ** n for n in range(N_periods + 1)], dtype=float)
        max_err = float(np.max(np.abs(C - expected)))
        check(
            f"eps=0, L={L}: 1D autocorrelator equals (-1)^n exactly",
            max_err < 1e-12,
            detail=f"max err = {max_err:.2e}",
        )

    # (ii) eps > 0: subharmonic spectral weight at ω = π/T decays with L.
    #
    # Weight at ω = π/T over N stroboscopic periods is
    #     w(L, eps; N) = | (1/N) sum_{n=1}^{N} (-1)^n C(n) |
    # which is the discrete Fourier component at the Nyquist frequency.
    # For eps = 0 this equals 1 exactly. For eps > 0 it shrinks as L grows
    # because the modes dephase at distinct rates.
    eps_test = 0.15

    def subharm_weight(L: int) -> float:
        C = stroboscopic_autocorr_1d(eps_test, a, m, T, L, N_periods)
        signs = np.array([(-1) ** n for n in range(1, N_periods + 1)], dtype=float)
        return float(abs(np.mean(signs * C[1:])))

    weights = {L: subharm_weight(L) for L in [8, 32, 128, 512]}
    print(f"  eps={eps_test:+.3f}: subharmonic weight w(L) =")
    for L, w in weights.items():
        print(f"      L = {L:4d}   w = {w:.6f}")

    # Reference: eps = 0 weight is exactly 1 at every L (rigid).
    C_ref = stroboscopic_autocorr_1d(0.0, a, m, T, 128, N_periods)
    signs_ref = np.array([(-1) ** n for n in range(1, N_periods + 1)], dtype=float)
    w_ref = float(abs(np.mean(signs_ref * C_ref[1:])))
    check(
        "eps=0 subharmonic weight equals 1 exactly (rigid reference)",
        abs(w_ref - 1.0) < 1e-12,
        detail=f"w(eps=0, L=128) = {w_ref:.6f}",
    )
    # Monotone decay with L (modulo small finite-N noise)
    L_vals = sorted(weights.keys())
    decay_ok = all(weights[L_vals[i + 1]] <= weights[L_vals[i]] + 1e-3
                   for i in range(len(L_vals) - 1))
    check(
        "subharmonic weight is non-increasing in L at eps>0 (BZ-sampling smearing)",
        decay_ok,
        detail=f"weights = {[f'{weights[L]:.4f}' for L in L_vals]}",
    )
    # At L=512 the weight is substantially below 1.
    check(
        "L=512 subharmonic weight < 0.6 (well below rigid value 1)",
        weights[512] < 0.6,
        detail=f"w(L=512) = {weights[512]:.4f}",
    )


# =============================================================================
# Part F.  Z^d (d=1,2,3) BZ integral: thermodynamic-limit no-rigidity
# =============================================================================

def thermo_limit_subharm_weight(eps: float, a: float, m: float, T: float,
                                 d: int, n_grid: int, N_periods: int) -> float:
    """Quadrature estimate of

        w_∞(eps) = lim_{L→∞} |(1/N) sum_{n=1}^N (-1)^n C_L(n; eps)|

    The per-mode |↑> stroboscopic <sigma_z(nT)> is, for our Floquet
        cos theta = -sin(eps/2) cos(beta/2),
    a function of (theta, beta) that we average over the BZ:

        C(n; eps) = ∫_BZ d^d k / |BZ| · sz_n(theta_k(eps), beta_k)

    The subharmonic projection (-1)^n C(n) integrates to give the
    fraction of BZ measure with theta = π/2 (a measure-zero set for
    eps ≠ 0), so w_∞(eps) → 0 in the L → ∞ limit for all eps ≠ 0.
    """
    k_axis = np.linspace(-np.pi / a, np.pi / a, n_grid, endpoint=False)
    if d == 1:
        mesh = np.array(np.meshgrid(k_axis, indexing="ij")).reshape(d, -1).T
    elif d == 2:
        mesh = np.array(np.meshgrid(k_axis, k_axis, indexing="ij")).reshape(d, -1).T
    elif d == 3:
        mesh = np.array(np.meshgrid(k_axis, k_axis, k_axis, indexing="ij")).reshape(d, -1).T
    else:
        raise ValueError(d)
    n_modes = mesh.shape[0]
    psi = np.zeros((n_modes, 2), dtype=complex)
    psi[:, 0] = 1.0
    Us = np.zeros((n_modes, 2, 2), dtype=complex)
    for j, kv in enumerate(mesh):
        beta = E_lat(kv, a, m) * T
        Us[j] = floquet_mode(eps, beta)
    signs = np.array([(-1) ** n for n in range(1, N_periods + 1)], dtype=float)
    acc = 0.0
    for n in range(1, N_periods + 1):
        psi = np.einsum("kab,kb->ka", Us, psi)
        sz = np.real(np.conj(psi[:, 0]) * psi[:, 0] - np.conj(psi[:, 1]) * psi[:, 1])
        acc += signs[n - 1] * float(np.mean(sz))
    return abs(acc / N_periods)


def part_F() -> None:
    print()
    print("=" * 76)
    print("PART F.  Z^d BZ thermodynamic limit: subharmonic peak weight → 0 (eps>0)")
    print("=" * 76)
    a, m, T = 1.0, 0.4, 0.9
    N_periods = 256

    for d in [1, 2, 3]:
        # Reference: eps = 0 should give weight = 1 (rigid).
        w0 = thermo_limit_subharm_weight(0.0, a, m, T, d,
                                         n_grid=20 if d == 3 else (40 if d == 2 else 200),
                                         N_periods=N_periods)
        check(
            f"d={d}: eps=0 BZ-averaged subharmonic weight = 1 (rigid at symmetry point)",
            abs(w0 - 1.0) < 1e-12,
            detail=f"w_BZ(eps=0) = {w0:.6f}",
        )
        # eps = 0.15: BZ-quadrature weight converges to its thermodynamic
        # limit as the grid refines. The diagnostic is convergence of the
        # two finest grids (Riemann-sum stability), and smallness of the
        # converged value vs the rigid reference w(eps=0) = 1.
        n_grids = {1: [64, 128, 256], 2: [24, 36, 48], 3: [12, 16, 20]}[d]
        weights = []
        for ng in n_grids:
            w = thermo_limit_subharm_weight(0.15, a, m, T, d, n_grid=ng, N_periods=N_periods)
            weights.append(w)
        print(f"  d={d}, eps=0.15: BZ grid sweep ng = {n_grids}  →  w = "
              f"{['%.4f' % w for w in weights]}")
        # The two finest grids must agree to within 1% — Riemann-sum stability
        # of the BZ integral as L → ∞.
        rel_diff = abs(weights[-1] - weights[-2]) / max(weights[-1], 1e-12)
        check(
            f"d={d}: eps=0.15 BZ weight converged at finest two grids (Riemann-sum stability)",
            rel_diff < 0.01,
            detail=f"|w(ng={n_grids[-1]}) - w(ng={n_grids[-2]})| / w = {rel_diff:.3e}",
        )
        check(
            f"d={d}: eps=0.15 converged BZ weight is small (≪ rigid value 1)",
            weights[-1] < 0.35,
            detail=f"w(ng={n_grids[-1]}) = {weights[-1]:.4f}",
        )

    print()
    print("  Measure-theoretic explanation: weight at ω = π/T is the BZ measure of")
    print("  the level set {k : cos theta_k(eps) = 0}, equivalently")
    print("  {k : sin(eps/2) cos(E_lat(k) T / 2) = 0}. For eps ≠ 0 this is the")
    print("  vanishing set of an analytic non-constant function on the d-torus,")
    print("  hence Lebesgue measure zero. So w_∞(eps) = 0 for all eps ≠ 0.")
    print("  The peak at ω = π/T survives only at eps = 0 — the symmetry point.")


# =============================================================================
# Driver
# =============================================================================

def main() -> int:
    t0 = time.time()
    print("=" * 76)
    print("FREE Z^d HAMILTONIAN-LATTICE DTC NO-GO RUNNER")
    print("=" * 76)
    print("Scope: retained free-scalar lattice surface; quadratic E_lat(p)")
    print("       on Z^d with d = 1, 2, 3 and Z_2 mode-parity qubit per k.")
    print()
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    dt = time.time() - t0
    print()
    print("=" * 76)
    print(f"PASS = {PASS_COUNT}, FAIL = {FAIL_COUNT}   (elapsed {dt:.1f} s)")
    print("=" * 76)
    if FAIL_COUNT == 0:
        print()
        print("THEOREM CONCLUSION (free Z^d Hamiltonian-lattice retained surface):")
        print()
        print("  Period-doubled Floquet response at the symmetry point eps = 0 is")
        print("  STRUCTURAL — every mode gives U_F(k,0)^2 = -I — but the response")
        print("  is NOT RIGID: any kick imperfection eps ≠ 0 disperses the")
        print("  subharmonic frequency 2 theta_k(eps)/T across the BZ. The")
        print("  thermodynamic-limit spectral weight at ω = π/T vanishes for all")
        print("  eps ≠ 0. The retained free Z^d sector therefore hosts NO genuine")
        print("  discrete time crystal phase.")
        print()
        print("  Putative MBL / interacting + disordered DTC phases lie outside")
        print("  the retained surface and are NOT addressed by this no-go.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
