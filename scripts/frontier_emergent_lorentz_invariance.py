#!/usr/bin/env python3
"""Free cubic dispersion and angular mathematics on supplied symbols.

No physical Lorentz/CPT/SME identification or all-operator exclusion is proved.
Planck-scale numbers are conditional angular-average estimates.
"""

from __future__ import annotations

# Bind actual documentary reads/existence checks to cache identity.
AUDIT_INPUT_PATHS = ['docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md', 'docs/PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md']

import sys
import numpy as np
try:
    from scipy.special import sph_harm  # scipy < 1.15
except ImportError:
    from scipy.special import sph_harm_y as _shy  # scipy >= 1.15
    def sph_harm(m, l, phi, theta):
        return _shy(l, m, theta, phi)

np.set_printoptions(precision=10, linewidth=120, suppress=True)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name, condition, detail="", kind="EXACT"):
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


def info(name, detail="", condition=None):
    """Report non-load-bearing context without affecting PASS/FAIL status."""
    if condition is None:
        msg = f"  [INFO] {name}"
    else:
        msg = f"  [{'INFO-YES' if condition else 'INFO-NO'}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)


# =============================================================================
# Constants
# =============================================================================

L_PLANCK = 1.616255e-35   # metres
E_PLANCK = 1.220890e19    # GeV
M_PLANCK_GEV = E_PLANCK


# =============================================================================
# Part 1: Staggered dispersion relation
# =============================================================================

def staggered_energy_sq(p, a=1.0):
    """Exact staggered fermion dispersion: E² = (1/a²) Σ sin²(p_i a)."""
    return np.sum(np.sin(p * a) ** 2) / a ** 2


def continuum_energy_sq(p):
    """Continuum dispersion: E² = |p|²."""
    return np.sum(p ** 2)


def test_dispersion_isotropy():
    """Verify the dispersion relation approaches E² = p² at low momentum."""
    print("\n=== Part 1: Dispersion relation isotropy ===\n")

    a = 1.0  # lattice spacing (units where a = 1)

    # Test at various momentum magnitudes
    # Directions: [1,0,0], [1,1,0]/√2, [1,1,1]/√3
    directions = {
        "[1,0,0]": np.array([1.0, 0.0, 0.0]),
        "[1,1,0]": np.array([1.0, 1.0, 0.0]) / np.sqrt(2),
        "[1,1,1]": np.array([1.0, 1.0, 1.0]) / np.sqrt(3),
    }

    print("  p_mag   E²_[100]    E²_[110]    E²_[111]    E²_cont    max_aniso")
    print("  " + "-" * 72)

    for p_mag in [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0]:
        e2 = {}
        for name, d in directions.items():
            p = p_mag * d
            e2[name] = staggered_energy_sq(p, a)
        e2_cont = p_mag ** 2

        vals = list(e2.values())
        aniso = (max(vals) - min(vals)) / max(max(vals), 1e-30)
        print(f"  {p_mag:5.2f}   {e2['[1,0,0]']:10.6f}  {e2['[1,1,0]']:10.6f}  "
              f"{e2['[1,1,1]']:10.6f}  {e2_cont:10.6f}  {aniso:10.2e}")

    # Low-momentum isotropy check: at p = 0.01, aniso should be < 10⁻⁸
    p_low = 0.01
    e2_low = {n: staggered_energy_sq(p_low * d, a) for n, d in directions.items()}
    vals_low = list(e2_low.values())
    aniso_low = (max(vals_low) - min(vals_low)) / max(max(vals_low), 1e-30)
    # At p = 0.01 with a = 1, relative anisotropy ~ (a p)² / 3 ~ 3e-5
    check("Low-p isotropy: anisotropy ~ O(p²) at p = 0.01",
          aniso_low < 1e-3,
          f"anisotropy = {aniso_low:.2e} (expected ~ p²/3 ≈ 3e-5)")

    # Mid-momentum check: at p = 0.5, aniso should be visible but small
    p_mid = 0.5
    e2_mid = {n: staggered_energy_sq(p_mid * d, a) for n, d in directions.items()}
    vals_mid = list(e2_mid.values())
    aniso_mid = (max(vals_mid) - min(vals_mid)) / max(max(vals_mid), 1e-30)
    check("Mid-p anisotropy visible at p = 0.5",
          aniso_mid > 1e-4,
          f"anisotropy = {aniso_mid:.4f} (lattice effects at p ~ 1/a)")

    # Continuum agreement at low p
    # Expected deviation ~ (ap)²/3 ~ 8e-4 at p = 0.05
    p_test = 0.05
    for name, d in directions.items():
        p = p_test * d
        e2_lat = staggered_energy_sq(p, a)
        e2_con = continuum_energy_sq(p)
        dev = abs(e2_lat - e2_con) / e2_con
        check(f"E²_lattice ≈ E²_continuum at p = 0.05 along {name}",
              dev < 0.01,
              f"deviation = {dev:.2e} (expected ~ (ap)²/3)")

    return True


# =============================================================================
# Part 2: Leading Lorentz-violating coefficient
# =============================================================================

def test_lv_coefficient():
    """Extract and verify the leading O(a²) LV correction coefficient."""
    print("\n=== Part 2: Leading Lorentz-violating coefficient ===\n")

    a = 1.0

    # The staggered dispersion: E² = (1/a²) Σ sin²(p_i a)
    # Taylor: sin²(x) = x² − x⁴/3 + 2x⁶/45 − ...
    # So E² = Σ p_i² − (a²/3) Σ p_i⁴ + O(a⁴)
    # The LV coefficient for the fermion is c₄ = −a²/3

    # Numerical extraction: compare exact vs continuum along [1,0,0]
    # At small p along [1,0,0]: E² = p² − (a²/3) p⁴
    # So (E² − p²)/p⁴ → −a²/3 as p → 0

    ps = np.logspace(-4, -1, 50)
    ratios = []
    for p in ps:
        pvec = np.array([p, 0.0, 0.0])
        e2 = staggered_energy_sq(pvec, a)
        p2 = p ** 2
        if abs(p ** 4) > 1e-30:
            ratios.append((e2 - p2) / p ** 4)

    c4_numerical = np.mean(ratios[-10:])  # average at smallest p values
    c4_exact = -a ** 2 / 3.0

    check("LV coefficient c₄ = −a²/3 (fermion dispersion)",
          abs(c4_numerical - c4_exact) / abs(c4_exact) < 0.01,
          f"c₄_numerical = {c4_numerical:.6f}, c₄_exact = {c4_exact:.6f}")

    # Also check the bosonic (Laplacian) coefficient
    # Laplacian: K_i = (4/a²) sin²(p_i a/2) → p² − (a²/12) p⁴
    def laplacian_energy_sq(p, a=1.0):
        return np.sum(4.0 / a ** 2 * np.sin(p * a / 2) ** 2)

    ratios_bos = []
    for p in ps:
        pvec = np.array([p, 0.0, 0.0])
        e2 = laplacian_energy_sq(pvec, a)
        p2 = p ** 2
        if abs(p ** 4) > 1e-30:
            ratios_bos.append((e2 - p2) / p ** 4)

    c4_bos_num = np.mean(ratios_bos[-10:])
    c4_bos_exact = -a ** 2 / 12.0

    check("LV coefficient c₄ = −a²/12 (bosonic/Laplacian dispersion)",
          abs(c4_bos_num - c4_bos_exact) / abs(c4_bos_exact) < 0.01,
          f"c₄_numerical = {c4_bos_num:.6f}, c₄_exact = {c4_bos_exact:.6f}")

    # Both displayed corrections are a² p⁴ terms (dimension-six type in power counting)
    info("Dimension-six-type label for the displayed a²p⁴ terms is power counting only; "
         "no operator classification is checked.")

    # These symbols are even in each p_i (checked in Part 6c)
    info("No odd-power term appears in these symbols; a physical dimension-five exclusion "
         "is not checked.")

    return True


# =============================================================================
# Part 3: Cubic harmonic angular structure
# =============================================================================

def test_cubic_harmonic():
    """Verify the angular structure of the LV operator is the cubic harmonic."""
    print("\n=== Part 3: Cubic harmonic angular structure ===\n")

    # The LV operator is Σ_i n_i⁴ where n̂ = p̂ (unit direction)
    # Decomposition in NORMALIZED real spherical harmonics Y_lm (the
    # scipy.special.sph_harm convention used throughout this runner):
    #     Σ n_i⁴ = 3/5 + (4√π/15) K₄(θ,φ),  K₄ = Y₄₀ + √(5/14)(Y₄₄ + Y₄,₋₄)
    # The coefficient on K₄ is 4√π/15 ≈ 0.4727 with normalized Y_lm, NOT 4/5
    # (an earlier revision wrote 4/5, which is only correct under an
    # unnormalized angular convention; corrected 2026-05-29 to match the
    # normalized K₄ and the sph_harm projections below).

    # Verify at specific directions
    def sum_n4(theta, phi):
        """Compute Σ n_i⁴ for direction (θ, φ)."""
        nx = np.sin(theta) * np.cos(phi)
        ny = np.sin(theta) * np.sin(phi)
        nz = np.cos(theta)
        return nx ** 4 + ny ** 4 + nz ** 4

    # [1,0,0]: θ=π/2, φ=0 → n₁⁴ = 1, rest = 0 → Σ = 1
    check("Σn_i⁴ along [1,0,0] = 1",
          abs(sum_n4(np.pi / 2, 0) - 1.0) < 1e-12,
          f"Σn_i⁴ = {sum_n4(np.pi / 2, 0):.6f}")

    # [1,1,0]/√2: θ=π/2, φ=π/4 → each n = 1/√2 → n⁴ = 1/4 → Σ = 1/2
    check("Σn_i⁴ along [1,1,0] = 1/2",
          abs(sum_n4(np.pi / 2, np.pi / 4) - 0.5) < 1e-12,
          f"Σn_i⁴ = {sum_n4(np.pi / 2, np.pi / 4):.6f}")

    # [1,1,1]/√3: each n = 1/√3 → n⁴ = 1/9 → Σ = 1/3
    theta_111 = np.arccos(1 / np.sqrt(3))
    phi_111 = np.pi / 4
    check("Σn_i⁴ along [1,1,1] = 1/3",
          abs(sum_n4(theta_111, phi_111) - 1.0 / 3) < 1e-12,
          f"Σn_i⁴ = {sum_n4(theta_111, phi_111):.6f}")

    # Anisotropy factor: axis/diagonal ratio of the evaluated angular factor
    ratio_axis_diag = sum_n4(np.pi / 2, 0) / sum_n4(theta_111, phi_111)
    check("Anisotropy factor: [100]/[111] = 3 (factor-of-3 cubic signature)",
          abs(ratio_axis_diag - 3.0) < 1e-12,
          f"Σn_i⁴[100]/Σn_i⁴[111] = {ratio_axis_diag:.12f}; geometric ratio, "
          "not a unique microscopic identifier")

    # Verify decomposition: Σ n_i⁴ = 3/5 + (4√π/15) K₄ (normalized Y_lm)
    # Isotropic part: average of Σ n_i⁴ over the sphere = 3/5
    # (because <n_i⁴> = 1/5 for each direction, and there are 3)
    n_samples = 10000
    rng = np.random.default_rng(42)
    # Random directions on the sphere
    z = rng.uniform(-1, 1, n_samples)
    phi = rng.uniform(0, 2 * np.pi, n_samples)
    theta = np.arccos(z)
    sn4 = np.array([sum_n4(t, p) for t, p in zip(theta, phi)])
    avg_sn4 = np.mean(sn4)

    check("Spherical average ⟨Σn_i⁴⟩ = 3/5",
          abs(avg_sn4 - 0.6) < 0.01,
          f"⟨Σn_i⁴⟩ = {avg_sn4:.4f} (expected 0.6000)")

    # Verify the anisotropic part K₄ has only ℓ=4 content
    # The anisotropic part: f₄(θ,φ) = Σn_i⁴ − 3/5
    # This should project entirely onto ℓ=4 spherical harmonics
    f4_samples = sn4 - 3.0 / 5.0

    # Project onto Y₀₀ (ℓ=0): should be ~0
    y00 = np.real(sph_harm(0, 0, phi, theta))
    proj_00 = np.mean(f4_samples * y00) * 4 * np.pi
    check("No ℓ=0 content in anisotropic part",
          abs(proj_00) < 0.05,
          f"|⟨f₄|Y₀₀⟩| = {abs(proj_00):.4f}")

    # Project onto Y₂₀ (ℓ=2): should be ~0
    y20 = np.real(sph_harm(0, 2, phi, theta))
    proj_20 = np.mean(f4_samples * y20) * 4 * np.pi
    check("No ℓ=2 content in anisotropic part",
          abs(proj_20) < 0.05,
          f"|⟨f₄|Y₂₀⟩| = {abs(proj_20):.4f}")

    # Project onto Y₄₀ (ℓ=4): should be nonzero
    y40 = np.real(sph_harm(0, 4, phi, theta))
    proj_40 = np.mean(f4_samples * y40) * 4 * np.pi
    check("Nonzero ℓ=4 content in anisotropic part",
          abs(proj_40) > 0.1,
          f"|⟨f₄|Y₄₀⟩| = {abs(proj_40):.4f}")

    # Project onto Y₆₀ (ℓ=6): should be ~0
    y60 = np.real(sph_harm(0, 6, phi, theta))
    proj_60 = np.mean(f4_samples * y60) * 4 * np.pi
    check("No ℓ=6 content in Σn_i⁴ anisotropic part",
          abs(proj_60) < 0.05,
          f"|⟨f₄|Y₆₀⟩| = {abs(proj_60):.4f}")

    # -------------------------------------------------------------------
    # Exact cubic-harmonic identity with NORMALIZED Y_lm (2026-05-29 fix).
    # Verify Σn_i⁴ = 3/5 + (4√π/15) K₄ pointwise to machine precision over
    # many random directions, with K₄ = Y₄₀ + √(5/14)(Y₄₄ + Y₄,₋₄) built
    # from the same normalized sph_harm used above. Also confirm the OLD
    # coefficient 4/5 fails, so the runner pins the correct normalization.
    # -------------------------------------------------------------------
    rng2 = np.random.default_rng(2026)
    Nv = 50000
    zv = rng2.uniform(-1, 1, Nv)
    phiv = rng2.uniform(0, 2 * np.pi, Nv)
    thetav = np.arccos(zv)
    nxv = np.sin(thetav) * np.cos(phiv)
    nyv = np.sin(thetav) * np.sin(phiv)
    nzv = np.cos(thetav)
    lhs_v = nxv ** 4 + nyv ** 4 + nzv ** 4

    Y40v = sph_harm(0, 4, phiv, thetav)
    Y44v = sph_harm(4, 4, phiv, thetav)
    Y4m4v = sph_harm(-4, 4, phiv, thetav)
    K4v = np.real(Y40v + np.sqrt(5.0 / 14.0) * (Y44v + Y4m4v))

    coef_correct = 4.0 * np.sqrt(np.pi) / 15.0   # ≈ 0.472654
    coef_old = 4.0 / 5.0
    err_correct = float(np.max(np.abs(lhs_v - (3.0 / 5.0 + coef_correct * K4v))))
    err_old = float(np.max(np.abs(lhs_v - (3.0 / 5.0 + coef_old * K4v))))

    check("Exact identity Σn_i⁴ = 3/5 + (4√π/15)K₄ (normalized Y_lm)",
          err_correct < 1e-12,
          f"max|LHS-RHS| = {err_correct:.2e} over {Nv} random directions "
          f"(coef = 4√π/15 ≈ {coef_correct:.6f})")
    check("Old coefficient 4/5 is refuted under normalized Y_lm",
          err_old > 1e-3,
          f"max|LHS-RHS| = {err_old:.2e} with the discarded 4/5 coefficient")

    # Symbolic confirmation (optional: only if sympy is importable). Confirms
    # trigsimp(Σn_i⁴ − [3/5 + (4√π/15)K₄]) = 0 and that the coefficient is the
    # exact projection ⟨f|K₄⟩/⟨K₄|K₄⟩ = 4√π/15, not a numeric coincidence.
    try:
        import sympy as sp
        th, ph = sp.symbols('theta phi', real=True)
        nx_s = sp.sin(th) * sp.cos(ph)
        ny_s = sp.sin(th) * sp.sin(ph)
        nz_s = sp.cos(th)
        f_s = nx_s ** 4 + ny_s ** 4 + nz_s ** 4
        Y40_s = sp.Ynm(4, 0, th, ph).expand(func=True)
        Y44_s = sp.Ynm(4, 4, th, ph).expand(func=True)
        Y4m4_s = sp.Ynm(4, -4, th, ph).expand(func=True)
        K4_s = Y40_s + sp.sqrt(sp.Rational(5, 14)) * (Y44_s + Y4m4_s)
        rhs_s = sp.Rational(3, 5) + (4 * sp.sqrt(sp.pi) / 15) * K4_s
        residual = sp.trigsimp(sp.simplify((f_s - rhs_s).rewrite(sp.cos)))
        check("Sympy: trigsimp(Σn_i⁴ − [3/5 + (4√π/15)K₄]) = 0 identically",
              residual == 0,
              f"symbolic residual = {residual}")

        # Coefficient as exact spherical projection ⟨f|K₄⟩/⟨K₄|K₄⟩.
        def _inner(A, B):
            integ = A * sp.conjugate(B) * sp.sin(th)
            return sp.integrate(sp.integrate(integ, (ph, 0, 2 * sp.pi)),
                                (th, 0, sp.pi))
        coef_sym = sp.simplify(_inner(f_s, K4_s) / _inner(K4_s, K4_s))
        check("Sympy: ⟨f|K₄⟩/⟨K₄|K₄⟩ = 4√π/15 (exact projection)",
              sp.simplify(coef_sym - 4 * sp.sqrt(sp.pi) / 15) == 0,
              f"projected coefficient = {coef_sym}")
    except ImportError:
        info("Sympy not available — symbolic identity check skipped",
             "numeric pointwise check above already pins coef = 4√π/15")

    return True


# =============================================================================
# Part 4: Operator-classification boundary (no CPT/SME exclusion is checked)
# =============================================================================

def test_cpt_protection():
    info("No physical CPT or SME operator-basis exclusion is proved by this free-symbol runner.")
    return True


# =============================================================================
# Part 5: Planck suppression under the package pin premise
# =============================================================================

def test_planck_suppression():
    """Compute the LV magnitude under the supplied Planck-pin premise.

    This runner does not derive the pin. It computes the consequence of
    using the package-surface premise a ~ 1/M_Planck.
    """
    print("\n=== Part 5: Planck suppression under package pin premise ===\n")

    # Fermion LV coefficient: c₄ = a²/3
    # At a = l_Planck (in natural units: a = 1/M_Planck):
    # |δE²|/E² = (a²/3) × Σ p_i⁴ / E²
    # For isotropic p: Σ p_i⁴ = (3/5) p⁴ (spherical average)
    # |δE²|/E² = (a²/3) × (3/5) × p⁴/E² ≈ (1/5) × (E/M_Planck)²
    #
    # The lattice spacing a is supplied by the package pin:
    #   a ~ 1/M_Planck
    # So the Planck suppression is conditional on that pin.

    for energy_gev in (1.0, 1000.0, 1e11):
        estimate = (energy_gev/E_PLANCK)**2/5
        print(f"INFO: conditional dimensionless dispersion estimate at {energy_gev:g} GeV: {estimate:.6e}")
    check("conditional quadratic scaling over factor 1000 in energy",
          np.isclose(((1000/E_PLANCK)**2/5)/((1/E_PLANCK)**2/5), 1e6))
    print("INFO: no matched experimental operator/sector/unit map; no safety margin inferred.")

    return True


# =============================================================================
# Part 6: Finite-lattice numerical verification
# =============================================================================

def build_staggered_hamiltonian_momentum(L):
    """Build the real anti-Hermitian staggered hopping D; Hermitian lift is iD."""
    N = L ** 3

    def idx(x, y, z):
        return ((x % L) * L + (y % L)) * L + (z % L)

    def eta(mu, site):
        return (-1) ** sum(site[nu] for nu in range(mu))

    H = np.zeros((N, N), dtype=float)
    for ix in range(L):
        for iy in range(L):
            for iz in range(L):
                site = (ix, iy, iz)
                s = idx(ix, iy, iz)
                for mu in range(3):
                    e = eta(mu, site)
                    fwd = list(site)
                    fwd[mu] = (fwd[mu] + 1) % L
                    bwd = list(site)
                    bwd[mu] = (bwd[mu] - 1) % L
                    H[s, idx(*fwd)] += 0.5 * e
                    H[s, idx(*bwd)] -= 0.5 * e

    return H


def test_finite_lattice():
    """Verify dispersion isotropy on a finite lattice."""
    print("\n=== Part 6: Finite-lattice dispersion verification ===\n")

    L = 8  # even, for CPT compatibility

    # Build Hamiltonian
    H = build_staggered_hamiltonian_momentum(L)

    # H is anti-Hermitian (real antisymmetric)
    check(f"L={L}: D (legacy local variable H) is antisymmetric",
          np.allclose(H, -H.T, atol=1e-14),
          f"max |H + Hᵀ| = {np.max(np.abs(H + H.T)):.2e}")

    # Eigenvalues of iH are real (H is anti-symmetric → iH is Hermitian)
    iH = 1j * H
    eigs = np.linalg.eigvalsh(iH.astype(complex))
    eigs_sorted = np.sort(eigs)

    # The spectrum is symmetric under E -> -E (C H C = -H)
    n_zero = int(np.sum(np.abs(eigs_sorted) < 1e-10))
    pm_err = float(np.max(np.abs(eigs_sorted + eigs_sorted[::-1])))
    check(f"L={L}: spectrum is symmetric under E -> -E",
          pm_err < 1e-10,
          f"max |E_k + E_(N-1-k)| = {pm_err:.2e}, zero modes = {n_zero}")

    # Positive eigenvalues give the dispersion E(p)
    pos_eigs = np.sort(eigs_sorted[eigs_sorted > 1e-10])

    # Compare with analytical dispersion
    # On L³ with periodic BCs, momenta are p_i = 2πn_i/L for n_i = 0,...,L-1
    analytical_eigs = []
    for nx in range(L):
        for ny in range(L):
            for nz in range(L):
                px = 2 * np.pi * nx / L
                py = 2 * np.pi * ny / L
                pz = 2 * np.pi * nz / L
                e2 = np.sin(px) ** 2 + np.sin(py) ** 2 + np.sin(pz) ** 2
                if e2 > 1e-10:
                    analytical_eigs.append(np.sqrt(e2))

    analytical_sorted = np.sort(analytical_eigs)

    check(f"L={L}: lowest eigenvalue matches analytical dispersion",
          abs(pos_eigs[0] - analytical_sorted[0]) < 0.01,
          f"E_min_num = {pos_eigs[0]:.6f}, E_min_ana = {analytical_sorted[0]:.6f}")

    # Exact multiset comparison (zero modes included): the L³ absolute
    # eigenvalues of iD equal sqrt(Σ_i sin² p_i) over all L³ momenta
    # p_i = 2πn_i/L.  Each reduced-zone level occurs 8 times in the full zone
    # and 4 + 4 times (both signs) in the finite spectrum.
    analytical_all = np.sort(np.array([
        np.sqrt(np.sin(2 * np.pi * nx / L) ** 2 + np.sin(2 * np.pi * ny / L) ** 2
                + np.sin(2 * np.pi * nz / L) ** 2)
        for nx in range(L) for ny in range(L) for nz in range(L)]))
    abs_num = np.sort(np.abs(eigs_sorted))
    mult_err = float(np.max(np.abs(abs_num - analytical_all)))
    check(f"L={L}: sorted |eigenvalues| of iD equal sqrt(Σ_i sin² p_i) over all L³ momenta",
          mult_err < 1e-10,
          f"max multiset deviation = {mult_err:.2e}")

    return True


# =============================================================================
# Part 6b: Direct CPT and parity verification on the runner's own H
# =============================================================================
#
# Parts 6b and 6c check finite antiunitary matrix identities on the
# Hermitian lift H = iD of the hopping D built in Part 6, and the evenness of
# the scalar symbol.  They do not identify physical CPT or establish parity
# protection of an operator basis.  The Planck pin is read as context only
# (Part 6d).
# =============================================================================

def build_charge_conjugation(L):
    """Sublattice parity charge conjugation on the staggered Z^3 lattice.

    For single-component staggered fermions on the bipartite even-L torus,
    C_{xy} = epsilon(x) delta_{xy} where epsilon(x) = (-1)^{x_1+x_2+x_3}.
    This is real, diagonal, involutory, and satisfies C H_0 C = -H_0
    on the free staggered hopping operator (the standard sublattice-parity
    spectral flip used in CPT_EXACT_NOTE.md).
    """
    N = L ** 3
    C = np.zeros((N, N), dtype=float)
    for ix in range(L):
        for iy in range(L):
            for iz in range(L):
                idx = ((ix % L) * L + (iy % L)) * L + (iz % L)
                C[idx, idx] = (-1.0) ** (ix + iy + iz)
    return C


def build_spatial_parity(L):
    """Spatial inversion P_inv: x -> (-x) mod L on the even periodic torus.

    P_inv is an involution on the periodic torus.  Even L is used here
    to match the runner's bipartite staggered setup.  This is the parity used in
    PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md.
    """
    N = L ** 3
    P = np.zeros((N, N), dtype=float)

    def site_to_idx(x, y, z):
        return ((x % L) * L + (y % L)) * L + (z % L)

    for ix in range(L):
        for iy in range(L):
            for iz in range(L):
                idx = site_to_idx(ix, iy, iz)
                j = site_to_idx((-ix) % L, (-iy) % L, (-iz) % L)
                P[idx, j] = 1.0
    return P


def test_cpt_bridge_on_runner_H():
    """Check finite antiunitary algebra, without a physical CPT identification."""
    print("\n=== Part 6b: Finite antiunitary matrix algebra on H = iD ===\n")
    L=8
    D=build_staggered_hamiltonian_momentum(L)
    H=1j*D
    C=build_charge_conjugation(L)
    P=build_spatial_parity(L)
    CP=C@P
    check("D real antisymmetric", np.max(np.abs(D+D.T)) < 1e-14)
    check("H=iD Hermitian", np.max(np.abs(H-H.conj().T)) < 1e-14)
    check("C squared identity",np.max(np.abs(C@C-np.eye(L**3))) < 1e-14)
    check("P squared identity",np.max(np.abs(P@P-np.eye(L**3))) < 1e-14)
    check("C H C = -H",np.max(np.abs(C@H@C+H)) < 1e-14)
    check("P H P = -H",np.max(np.abs(P@H@P+H)) < 1e-14)
    check("PK preserves H=iD",np.max(np.abs(P@H.conj()@P-H)) < 1e-14)
    check("CPK flips H=iD",np.max(np.abs(CP@H.conj()@CP+H)) < 1e-14)
    check("CPK is not a symmetry of this nonzero H",np.max(np.abs(CP@H.conj()@CP-H)) > .1)
    info("C, P and PK are declared matrices; no physical charge/CPT or SME identification follows.")
    return True


def test_parity_protection_bridge():
    """Check even momentum dependence; no general EFT operator classification."""
    print("\n=== Part 6c: Parity bridge — direct verification on dispersion ===\n")

    a = 1.0

    # Direct check: E^2(-p) = E^2(p) for the staggered dispersion
    rng = np.random.default_rng(7)
    n_samples = 50
    p_mags = np.linspace(1e-3, 0.5, n_samples)
    max_asym = 0.0
    for p_mag in p_mags:
        # Random direction
        d = rng.normal(size=3)
        d /= np.linalg.norm(d)
        p = p_mag * d
        e2_pos = staggered_energy_sq(p, a)
        e2_neg = staggered_energy_sq(-p, a)
        asym = abs(e2_pos - e2_neg)
        if asym > max_asym:
            max_asym = asym
    check("E^2(-p) = E^2(p) (P-symmetric staggered dispersion)",
          max_asym < 1e-14,
          f"max |E^2(p) - E^2(-p)| = {max_asym:.2e} over 50 random (|p|,direction) pairs")

    # Equivalent statement: Taylor expansion of E^2(p) has no odd-power term
    # The odd-power coefficient is (E^2(p) - E^2(-p)) / 2; we verify it = 0.
    # No dimension-5 contribution exists (a^1 * p^3 would be odd in p).
    # Numerical extraction of any potential dim-5 coefficient.
    ps = np.logspace(-3, -1, 30)
    odd_coefs = []
    for p in ps:
        pvec = np.array([p, 0.5 * p, 0.0])
        d = pvec / np.linalg.norm(pvec)
        e2_p = staggered_energy_sq(np.linalg.norm(pvec) * d, a)
        e2_m = staggered_energy_sq(-np.linalg.norm(pvec) * d, a)
        odd_part = (e2_p - e2_m) / 2.0
        # Normalize by a*p^3 (the dim-5 magnitude)
        if np.linalg.norm(pvec) > 0:
            odd_coefs.append(abs(odd_part) / (a * np.linalg.norm(pvec) ** 3 + 1e-30))
    check("Odd a p^3 contribution to this E^2 vanishes",
          max(odd_coefs) < 1e-10,
          f"max |odd_coef| = {max(odd_coefs):.2e}")

    info("Evenness of this scalar dispersion does not classify all dimension-five fermion bilinears.")

    return True


def report_planck_pin_bridge_context():
    """Planck-pin bridge context: report the upstream lane without promoting it.

    This section is deliberately non-fatal for the runner. The structural
    surface of this note is the free-symbol dispersion, finite antiunitary
    matrix algebra, scalar-symbol evenness and cubic-harmonic calculation
    above. Any Planck-scale physical estimate remains conditional.

    What this runner asserts as fatal checks: nothing in the structural
    dispersion proof depends on deriving a/l_P = 1 here.
    """
    print("\n=== Part 6d: Planck-pin bridge context — non-load-bearing ===\n")

    from pathlib import Path

    planck_note = Path("docs/PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md")
    bridge_note = Path("docs/PLANCK_TARGET3_CLIFFORD_PHASE_BRIDGE_THEOREM_NOTE_2026-04-25.md")
    planck_text = planck_note.read_text(encoding="utf-8") if planck_note.exists() else ""
    bridge_text = bridge_note.read_text(encoding="utf-8") if bridge_note.exists() else ""

    info("Planck package note present",
         "PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md",
         planck_note.exists())
    info("Planck package surface mentions a^{-1} and M_Pl",
         "context only; not a structural premise of this runner",
         ("a^{-1}" in planck_text or "a^(-1)" in planck_text) and "M_Pl" in planck_text)
    info("Separate unit-map bridge mentions a/l_P",
         "context only; not promoted by this runner",
         "a/l_P" in bridge_text or "a / l_P" in bridge_text)

    info("The structural checks above neither derive nor require a/l_P = 1.")

    print("\n  --- Bridge citation ---")
    print("  The Planck-pin bridge is non-load-bearing context in this note.")
    print("  Its authority must come from the upstream package/unit-map lane.")
    return True


# =============================================================================
# Part 7: Scope summary
# =============================================================================

def test_combined():
    info("Supplied free symbols: isotropic quadratic term, quartic cubic correction and even momentum dependence.")
    info("Physical operator selection, Lorentz symmetry, SME matching and experimental reach remain open.")
    return True


# =============================================================================
# Main
# =============================================================================

def main():
    print("=" * 72)
    print("Emergent Lorentz Invariance note: free cubic-lattice dispersion checks")
    print("=" * 72)
    print()
    print("CONDITIONAL SCOPE: supplied free symbols only. Physical Lorentz/CPT/SME")
    print("                   identification, operator selection and the unit map")
    print("                   are separate premises; Planck-scale sizes are estimates.")
    print()

    test_dispersion_isotropy()
    test_lv_coefficient()
    test_cubic_harmonic()
    test_cpt_protection()
    test_planck_suppression()
    test_finite_lattice()
    # --- Bridge-derivation block: directly verify CPT and parity on the
    # runner's own staggered Hamiltonian; cite the upstream Planck pin. ---
    test_cpt_bridge_on_runner_H()
    test_parity_protection_bridge()
    report_planck_pin_bridge_context()
    test_combined()

    print()
    print("=" * 72)
    print(f"SUMMARY: PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    print("=" * 72)

    if FAIL_COUNT > 0:
        print("\n*** FAILURES DETECTED ***")
        sys.exit(1)
    else:
        print("\nAll bounded checks passed for the conditional support surface.")
        print("Checked free-symbol quartic correction and l=4 angular component; physical mapping remains supplied.")
        sys.exit(0)


if __name__ == "__main__":
    main()
