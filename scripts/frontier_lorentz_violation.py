#!/usr/bin/env python3
"""Fixed-action cubic-anisotropy diagnostic.

This script evaluates a supplied nearest-neighbor second-order
finite-difference spatial kinetic symbol on a cubic lattice. It does not derive
that action, the lattice spacing, a relativistic carrier, CPT, or an SME-sector
identification from the four axioms. Its phenomenology tables are historical
scale illustrations, not validated experimental exclusions or framework
predictions. The robust checks are the Taylor coefficients and normalized
cubic-harmonic identity for the selected symbol.

The key result: the lattice correction to the dispersion relation is

    E^2 = m^2 + sum_i (4/a^2) sin^2(p_i a/2)

(the standard second-order finite-difference Laplacian eigenvalue;
matches LORENTZ_VIOLATION_DERIVED_NOTE.md Step 2). Expanding at low
momentum:

    E^2 = m^2 + p^2 - (a^2/12) sum_i p_i^4 + O(a^4)

The `p_i^4` term is spatially anisotropic with cubic group `O_h`. A later
SME-style parameterization is conditional on additional carrier and matching
assumptions that this runner does not verify.

If `a = l_Planck` is supplied externally, the scale factor is
`(E/E_Planck)^2`; this identification is not an axiom consequence.

The angular decomposition sum_i n_i^4 = 3/5 + (4*sqrt(pi)/15) K_4 uses the
standard NORMALIZED real spherical harmonics Y_lm (the
scipy.special.sph_harm / sympy.Ynm convention); the l=4 cubic-harmonic
coefficient is 4*sqrt(pi)/15, not 4/5 (corrected 2026-05-29). Section 2b
(verify_cubic_harmonic_identity) checks this numerically and, when sympy
is available, symbolically; the script exits non-zero if the check fails.
scipy/sympy are used only for that optional cross-check and degrade
gracefully (a closed-form numpy K_4 backs the numeric check if scipy is
absent).

PStack experiment: lorentz-violation-sme
"""

from __future__ import annotations

import math
import sys
import time

import numpy as np

np.set_printoptions(precision=10, linewidth=120, suppress=True)


# ============================================================
# Physical constants
# ============================================================
HBAR = 1.054571817e-34       # J s
C_LIGHT = 2.99792458e8       # m/s
G_NEWTON = 6.67430e-11       # m^3 kg^-1 s^-2
L_PLANCK = 1.616255e-35      # m
E_PLANCK_GEV = 1.2209e19     # GeV
E_PLANCK_J = 1.956e9         # J
GEV_TO_INVMETER = 5.076e15   # 1 GeV = 5.076e15 m^-1

# Particle masses in GeV
M_ELECTRON_GEV = 0.000511
M_PROTON_GEV = 0.938
M_NEUTRON_GEV = 0.940
M_NEUTRINO_GEV = 1e-10       # upper bound, ~0.1 eV


# ============================================================
# Section 1: Lattice dispersion relation
# ============================================================

def lattice_dispersion_1d(p: np.ndarray, a: float, m: float) -> np.ndarray:
    """Single-component lattice dispersion: (4/a^2) sin^2(p*a/2).

    On a cubic lattice with spacing a, the standard second-order
    finite-difference Laplacian eigenvalue is
        K_i = (4/a^2) sin^2(p_i a/2) = (2/a^2) (1 - cos(p_i a))

    rather than the continuum p_i^2. This is the canonical normalization
    that matches LORENTZ_VIOLATION_DERIVED_NOTE.md Step 2.

    Note (2026-05-02 audit fix): the previous version used (2/a^2)
    sin^2(p_i a/2), which is half-normalized: it gives leading
    p_i^2 / 2 rather than p_i^2 in the small-p_i limit, and the
    runner's printed expansion was inconsistent with its actual kinetic
    function. The (4/a^2) form below is the correct standard
    normalization for which sin^2(pa/2) -> (pa/2)^2 - (pa/2)^4/3 + ...
    multiplied by 4/a^2 yields p^2 - a^2 p^4/12 + ... .

    E^2 = m^2 + sum_i (4/a^2) sin^2(p_i a/2)

    Args:
        p: momentum array (GeV, in natural units with c=hbar=1)
        a: lattice spacing (in natural-unit length = 1/GeV)
        m: mass (GeV)

    Returns:
        E^2 array
    """
    return m**2 + (4.0 / a**2) * np.sin(p * a / 2.0)**2


def lattice_dispersion_3d(px: float, py: float, pz: float,
                          a: float, m: float) -> float:
    """3D lattice dispersion relation (standard (4/a^2) normalization)."""
    K = sum((4.0 / a**2) * math.sin(pi * a / 2.0)**2
            for pi in [px, py, pz])
    return m**2 + K


def continuum_dispersion(p: np.ndarray, m: float) -> np.ndarray:
    """Standard relativistic dispersion: E^2 = m^2 + p^2."""
    return m**2 + p**2


def lorentz_violation_coefficient(a: float) -> float:
    """The coefficient of the p_i^4 Lorentz-violating term.

    Expanding sin^2(p_i a/2) = (p_i a/2)^2 - (p_i a/2)^4/3 + ...
    gives (4/a^2) sin^2(p_i a/2) = p_i^2 - a^2 p_i^4/12 + ...

    The LV correction to E^2 is:
        delta(E^2) = -(a^2/12) sum_i p_i^4

    Returns the coefficient a^2/12.
    """
    return a**2 / 12.0


def sixth_order_coefficient(a: float) -> float:
    """The coefficient of the p_i^6 term (next Lorentz-violating order).

    sin^2(x) = x^2 - x^4/3 + 2x^6/45 - ...
    (4/a^2) sin^2(pa/2) = p^2 - a^2 p^4/12 + a^4 p^6/360 + ...

    Returns a^4/360.
    """
    return a**4 / 360.0


# ============================================================
# Section 2: SME (Standard Model Extension) mapping
# ============================================================

def compute_sme_coefficients(a_meters: float) -> dict:
    """Map the lattice dispersion correction onto SME coefficients.

    The Standard Model Extension (Kostelecky, 2004) parameterizes
    Lorentz violation in terms of tensor coefficients that modify
    the free-particle dispersion relation.

    For a spin-1/2 fermion in the SME, the modified dispersion is:
        E^2 = m^2 + p^2 + sum_{d,jm} k^(d)_{jm} |p|^{d-2}

    where d is the mass dimension of the operator, and k^(d)_{jm}
    are spherical-harmonic coefficients.

    The cubic lattice correction -(a^2/12) sum_i p_i^4 has:
    - Mass dimension d = 6 (the p^4 term modifies a dimension-6 operator)
    - It is a sum of p_i^4 terms, which decomposes in NORMALIZED real
      spherical harmonics Y_lm (scipy.special.sph_harm / sympy.Ynm
      convention) as:
      sum_i p_i^4 = (3/5)|p|^4 + (4*sqrt(pi)/15)|p|^4 [Y_{40} + sqrt(5/14)(Y_{44}+Y_{4-4})]
      (the coefficient on the l=4 cubic harmonic is 4*sqrt(pi)/15 ~= 0.4727
      with normalized Y_lm, NOT 4/5; see verify_cubic_harmonic_identity())
    - The isotropic part (j=0) gives: k^(6)_{00} ~ -(a^2/12)(3/5)
    - The anisotropic part (j=4) gives: k^(6)_{40} ~ -(a^2/12)(4*sqrt(pi)/15) etc.

    For comparison with experiment:
    - The coefficients have dimension [length]^2 = [energy]^{-2}
    - Convert a from meters to natural units: a_nat = a * (GeV / (hbar c))

    Args:
        a_meters: lattice spacing in meters

    Returns:
        Dictionary of SME coefficients
    """
    # Convert lattice spacing to natural units (1/GeV)
    a_nat = a_meters * GEV_TO_INVMETER  # in 1/GeV

    # The LV correction coefficient in natural units
    c4_coeff = a_nat**2 / 12.0  # dimension [1/GeV^2]

    # Decompose sum_i p_i^4 into NORMALIZED real spherical harmonics Y_lm
    # (the scipy.special.sph_harm / sympy.Ynm convention):
    #   x^4 + y^4 + z^4 = (3/5)r^4 + (4*sqrt(pi)/15) r^4 * K_4,
    #   K_4 = Y_40 + sqrt(5/14)(Y_44 + Y_{4,-4})
    # The coefficient on K_4 is 4*sqrt(pi)/15 ~= 0.4727 with normalized Y_lm,
    # NOT 4/5 (an earlier revision wrote 4/5, which is only correct for an
    # unnormalized angular convention; corrected 2026-05-29 to match the
    # normalized K_4 and the verify_cubic_harmonic_identity() projection).

    # Isotropic part: modifies the effective mass or the p^4 coefficient
    # in the rotationally-invariant sector
    iso_fraction = 3.0 / 5.0
    aniso_fraction = 4.0 * math.sqrt(math.pi) / 15.0  # coeff on normalized K_4

    # SME dimension-6 coefficients (c-type, CPT-even)
    # These modify the fermion dispersion as:
    # delta(E^2) = -c4_coeff * sum_i p_i^4
    #            = -c4_coeff * p^4 * [iso + aniso * cubic_harmonics]

    # For the electron sector (dimension-6, CPT-even):
    # c^(6)_{(I)jm} with j=0 and j=4
    c6_iso = -c4_coeff * iso_fraction        # j=0 coefficient
    c6_j4_m0 = -c4_coeff * aniso_fraction    # j=4, m=0 component

    # For dimension-8 (from the p^6 term):
    c6_coeff = a_nat**4 / 360.0
    c8_iso = c6_coeff * iso_fraction

    # The key SME coefficients commonly quoted:
    # For fermion sector, the dimension-6 operator c^(6)_{\mu\nu\rho\sigma}
    # contracted with p gives corrections proportional to a^2 p^4 / E_Planck^2.
    #
    # In the notation of Kostelecky & Mewes (2009, 2012):
    # The nonminimal coefficients are c^(d)_{(I)jm} for CPT-even
    # and a^(d)_{(V)jm} for CPT-odd.
    #
    # This selected even scalar symbol contributes only to the even sector of
    # this parameterization. It does not prove that a complete action has no
    # independent CPT-odd operators.

    return {
        # Dimension-6 CPT-even coefficients (units: GeV^-2)
        "c6_iso_j0": c6_iso,
        "c6_aniso_j4_m0": c6_j4_m0,
        "c6_total": -c4_coeff,

        # Dimension-8 CPT-even (units: GeV^-4)
        "c8_iso_j0": c8_iso,

        # Raw coefficient
        "a_natural_units": a_nat,
        "c4_coefficient": c4_coeff,

        # For comparison: express as (a/l_compton)^2 for each particle
        "electron_c6": c4_coeff * M_ELECTRON_GEV**2,  # dimensionless
        "proton_c6": c4_coeff * M_PROTON_GEV**2,
        "photon_c6": c4_coeff,  # for photons, no mass suppression
    }


# ============================================================
# Section 3: Experimental bounds (Kostelecky data tables)
# ============================================================

EXPERIMENTAL_BOUNDS = {
    "photon_birefringence": {
        "description": "GRB polarization (vacuum birefringence)",
        "sector": "photon",
        "dimension": 6,
        "bound_gev_minus2": 1e-32,
        "reference": "Kostelecky & Mewes, PRL 110 (2013) 201601",
        "notes": "Bound on k^(6)_F from GRB 061122 polarimetry",
    },
    "photon_dispersion_fermi": {
        "description": "Fermi LAT time-of-flight",
        "sector": "photon",
        "dimension": 6,
        "bound_gev_minus2": 1.0 / (6.3e10)**2,  # E_QG > 6.3e10 GeV for n=2
        "reference": "Vasileiou et al., PRD 87 (2013) 122001",
        "notes": "GRB 090510 photon speed, n=2 (dimension-6 LV)",
    },
    "electron_hughes_drever": {
        "description": "Hughes-Drever (electron sector)",
        "sector": "electron",
        "dimension": 4,
        "bound_gev": 1e-27,
        "reference": "Kostelecky & Lane, PRD 60 (1999) 116010",
        "notes": "Bound on c_{mu nu} for electrons, clock comparisons",
    },
    "proton_clock": {
        "description": "Atomic clock comparisons (proton sector)",
        "sector": "proton",
        "dimension": 4,
        "bound_gev": 1e-27,
        "reference": "Kostelecky & Vargas, PRD 98 (2018) 036003",
        "notes": "Bound on c_{mu nu} for protons",
    },
    "neutron_spin_precession": {
        "description": "Neutron spin precession",
        "sector": "neutron",
        "dimension": 4,
        "bound_gev": 1e-31,
        "reference": "Altarev et al., EPL 92 (2010) 51001",
        "notes": "Bound on b_mu for neutrons (CPT-odd, dimension 3)",
    },
    "neutrino_oscillation": {
        "description": "Neutrino oscillation (MINOS/IceCube)",
        "sector": "neutrino",
        "dimension": 4,
        "bound_gev": 1e-23,
        "reference": "Kostelecky & Mewes, PRD 85 (2012) 096005",
        "notes": "Bound on (a_L)_mu for neutrinos",
    },
    "muon_g_minus_2": {
        "description": "Muon anomalous magnetic moment",
        "sector": "muon",
        "dimension": 4,
        "bound_gev": 1e-24,
        "reference": "Bluhm et al., PRL 84 (2000) 1098",
        "notes": "Bound on c_{mu nu} for muons",
    },
    "gravity_sector_cbar": {
        "description": "Gravity sector (lunar laser ranging)",
        "sector": "gravity",
        "dimension": 4,
        "bound_dimensionless": 1e-9,
        "reference": "Battat et al., PRL 99 (2007) 241103",
        "notes": "Bound on s_bar^{mu nu} in pure gravity sector",
    },
}


# ============================================================
# Section 4: Staggered fermion taste-breaking
# ============================================================

def staggered_taste_breaking(a_nat: float) -> dict:
    """Compute taste-breaking Lorentz violation from staggered fermions.

    Staggered fermions on a cubic lattice have 2^d = 8 (in 3D) or 16 (in 4D)
    degenerate species (tastes). The taste symmetry is broken by
    lattice artifacts proportional to a^2.

    The taste-breaking interactions have the form (Lepage, 1999):
        delta_S = a^2 * sum_{mu<nu} (psi_bar gamma_mu x xi_nu psi)^2

    where xi_nu are taste matrices. These introduce ADDITIONAL dimension-6
    Lorentz-violating operators beyond the naive lattice dispersion.

    The taste-dependent dispersion becomes:
        E^2_taste = m^2 + p^2 - (a^2/12) sum_i p_i^4
                    + a^2 * Delta_taste(p)

    where Delta_taste depends on the taste quantum number and has
    a DIFFERENT angular structure than the naive p_i^4 term.

    For the physical (lightest) taste, Delta_taste is suppressed by
    an additional factor relative to the naive term. For heavy tastes,
    it can be comparable or larger.

    In the continuum limit a -> 0, both contributions vanish as a^2.
    But at finite a, the taste-breaking can double the effective
    Lorentz violation for some taste channels.

    Args:
        a_nat: lattice spacing in natural units (1/GeV)

    Returns:
        Dictionary of taste-breaking coefficients
    """
    # Naive lattice LV coefficient
    naive_c4 = a_nat**2 / 12.0

    # Taste-breaking correction factors (from lattice QCD studies)
    # The taste splitting goes as:
    #   delta_m^2_taste ~ C_taste * alpha_s^2 * a^2 * Lambda_QCD^2
    # For this selected illustrative parameterization (no running coupling),
    # the analogous splitting is:
    #   delta_LV_taste ~ C_taste * a^2 * p^4
    # where C_taste depends on the taste representation.

    # Taste representations and their approximate splitting factors
    # (from Aubin & Bernard, PRD 68 (2003) 034014):
    # Pseudoscalar (PS): C = 1 (reference)
    # Axial vector (AV): C ~ 1.2
    # Tensor (T): C ~ 1.5
    # Vector (V): C ~ 2.0
    # Scalar (S): C ~ 2.5
    # Identity (I): C ~ 3.0

    taste_factors = {
        "pseudoscalar": 1.0,
        "axial_vector": 1.2,
        "tensor": 1.5,
        "vector": 2.0,
        "scalar": 2.5,
        "identity": 3.0,
    }

    results = {}
    for taste, factor in taste_factors.items():
        # Total LV for this taste: naive + taste-breaking
        total_c4 = naive_c4 * (1.0 + factor)
        results[taste] = {
            "naive_c4": naive_c4,
            "taste_factor": factor,
            "total_c4": total_c4,
            "enhancement_ratio": 1.0 + factor,
        }

    return results


# ============================================================
# Section 5: discrete-symmetry scope
# ============================================================

def discrete_symmetry_scope() -> dict:
    """Report which symmetry statements the selected scalar symbol supports.

    The even momentum dependence verifies spatial inversion of this one
    symbol. A complete C, T, or CPT theorem would require a supplied matter
    action and explicit symmetry operators, none of which are tested here.
    """
    return {
        "selected_symbol_even_in_momentum": True,
        "complete_action_supplied": False,
        "cpt_established": False,
        "cpt_odd_coefficients_fixed": False,
        "scope": (
            "No Greenberg-theorem or CPT conclusion is drawn: the runner "
            "does not specify or test the complete QFT assumptions, matter "
            "action, or C/P/T operators required for that inference."
        ),
    }


# ============================================================
# Section 6: Numerical computation
# ============================================================

def compute_suppression_factor(E_gev: float, E_planck_gev: float) -> float:
    """Compute the natural Planck-scale suppression (E/E_Planck)^2.

    For dimension-6 operators (p^4 correction), the suppression is:
        (E/E_Planck)^2

    This is the factor by which lattice effects are suppressed at energy E.
    """
    return (E_gev / E_planck_gev)**2


def lattice_dispersion_correction_isotropic(p_gev: float,
                                            a_meters: float) -> float:
    """Fractional correction to E^2 from the isotropic p^4 term.

    delta(E^2) / E^2 ~ -(a^2/12)(3/5) p^4 / p^2 = -(a^2/20) p^2

    In natural units: a_nat = a_meters * GEV_TO_INVMETER.

    Args:
        p_gev: momentum in GeV
        a_meters: lattice spacing in meters

    Returns:
        Fractional correction (dimensionless)
    """
    a_nat = a_meters * GEV_TO_INVMETER
    return (a_nat**2 / 20.0) * p_gev**2


def direction_dependent_correction(p_gev: float, theta: float,
                                   phi: float, a_meters: float) -> float:
    """Direction-dependent (anisotropic) correction from cubic symmetry.

    For momentum along direction (theta, phi) in the lattice frame:
    sum_i p_i^4 = p^4 * f(theta, phi)

    where f(theta, phi) = sin^4(theta)cos^4(phi) + sin^4(theta)sin^4(phi)
                          + cos^4(theta)

    The isotropic average is <f> = 3/5.
    The anisotropic part is delta_f = f - 3/5.

    Maximum anisotropy: along axis (f=1) vs diagonal (f=1/3).

    Args:
        p_gev: momentum magnitude in GeV
        theta, phi: direction angles in lattice frame
        a_meters: lattice spacing in meters

    Returns:
        Fractional anisotropic correction to E^2
    """
    a_nat = a_meters * GEV_TO_INVMETER

    # Cubic angular factor
    sx = math.sin(theta) * math.cos(phi)
    sy = math.sin(theta) * math.sin(phi)
    sz = math.cos(theta)
    f_cubic = sx**4 + sy**4 + sz**4

    # The correction
    return (a_nat**2 / 12.0) * f_cubic * p_gev**2


# ============================================================
# Section 6b: Cubic-harmonic identity verification (normalized Y_lm)
# ============================================================

def _real_cubic_harmonic_k4(theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """K_4 = Y_40 + sqrt(5/14)(Y_44 + Y_{4,-4}) with NORMALIZED real Y_lm.

    Uses scipy.special.sph_harm when available (with a version-robust
    fallback for scipy >= 1.15, where the routine was renamed sph_harm_y).
    If scipy is unavailable, falls back to the exact closed form

        K_4 = (1/(16 sqrt(pi))) [ 3 (35 c^4 - 30 c^2 + 3) + 15 s^4 cos(4 phi) ]

    (c = cos theta, s = sin theta), so the numeric identity check never
    silently skips. Both routes use the same normalized Condon-Shortley
    convention, in which Y_44 + Y_{4,-4} is real and proportional to
    cos(4 phi).
    """
    try:
        try:
            from scipy.special import sph_harm  # scipy < 1.15
        except ImportError:
            from scipy.special import sph_harm_y as _shy  # scipy >= 1.15

            def sph_harm(m, l, az, pol):
                return _shy(l, m, pol, az)

        y40 = sph_harm(0, 4, phi, theta)
        y44 = sph_harm(4, 4, phi, theta)
        y4m4 = sph_harm(-4, 4, phi, theta)
        return np.real(y40 + math.sqrt(5.0 / 14.0) * (y44 + y4m4))
    except Exception:
        c = np.cos(theta)
        s = np.sin(theta)
        return (1.0 / (16.0 * math.sqrt(math.pi))) * (
            3.0 * (35.0 * c ** 4 - 30.0 * c ** 2 + 3.0)
            + 15.0 * s ** 4 * np.cos(4.0 * phi)
        )


def verify_cubic_harmonic_identity() -> bool:
    """Verify the corrected cubic-harmonic decomposition identity.

    With STANDARD NORMALIZED real spherical harmonics Y_lm (the
    scipy.special.sph_harm / sympy.Ynm convention), the exact identity is

        sum_i n_i^4 = 3/5 + (4*sqrt(pi)/15) K_4,
        K_4 = Y_40 + sqrt(5/14) (Y_44 + Y_{4,-4})

    The coefficient on K_4 is 4*sqrt(pi)/15 ~= 0.4727, NOT 4/5; the old
    4/5 value is only correct for an unnormalized angular convention and
    is refuted here. Checks: (1) numeric pointwise identity over 2x10^5
    random directions, (2) refutation of the discarded 4/5 coefficient,
    (3) the 3/5 isotropic average, and (4) optionally (if sympy imports)
    the symbolic trigsimp(f - rhs) = 0 plus the exact spherical projection
    <f|K_4>/<K_4|K_4> = 4*sqrt(pi)/15.

    Returns True iff every check passes.
    """
    print(f"\n{'=' * 78}")
    print("2b. CUBIC-HARMONIC IDENTITY VERIFICATION (normalized Y_lm)")
    print(f"{'=' * 78}\n")

    n_pass = 0
    n_fail = 0

    def _check(name: str, cond: bool, detail: str) -> None:
        nonlocal n_pass, n_fail
        tag = "PASS" if cond else "FAIL"
        if cond:
            n_pass += 1
        else:
            n_fail += 1
        print(f"  [{tag}] {name}")
        print(f"         {detail}")

    coef_correct = 4.0 * math.sqrt(math.pi) / 15.0   # ~= 0.472654
    coef_old = 4.0 / 5.0

    rng = np.random.default_rng(2026)
    n_dir = 200000
    z = rng.uniform(-1.0, 1.0, n_dir)
    phi = rng.uniform(0.0, 2.0 * np.pi, n_dir)
    theta = np.arccos(z)
    nx = np.sin(theta) * np.cos(phi)
    ny = np.sin(theta) * np.sin(phi)
    nz = np.cos(theta)
    lhs = nx ** 4 + ny ** 4 + nz ** 4

    k4 = _real_cubic_harmonic_k4(theta, phi)
    err_correct = float(np.max(np.abs(lhs - (3.0 / 5.0 + coef_correct * k4))))
    err_old = float(np.max(np.abs(lhs - (3.0 / 5.0 + coef_old * k4))))
    iso_avg = float(np.mean(lhs))

    _check(
        "Exact identity sum_i n_i^4 = 3/5 + (4*sqrt(pi)/15) K_4 (normalized Y_lm)",
        err_correct < 1e-12,
        f"max|LHS-RHS| = {err_correct:.2e} over {n_dir} random directions "
        f"(coef = 4*sqrt(pi)/15 = {coef_correct:.6f})",
    )
    _check(
        "Old coefficient 4/5 is refuted under normalized Y_lm",
        err_old > 1e-3,
        f"max|LHS-RHS| = {err_old:.2e} with the discarded 4/5 coefficient",
    )
    _check(
        "Isotropic average <sum_i n_i^4> = 3/5 (unchanged by the correction)",
        abs(iso_avg - 3.0 / 5.0) < 1e-3,
        f"<f> = {iso_avg:.6f} (expect 0.600000)",
    )

    # Optional exact symbolic confirmation (only if sympy is importable).
    try:
        import sympy as sp

        th, ph = sp.symbols("theta phi", real=True)
        nx_s = sp.sin(th) * sp.cos(ph)
        ny_s = sp.sin(th) * sp.sin(ph)
        nz_s = sp.cos(th)
        f_s = nx_s ** 4 + ny_s ** 4 + nz_s ** 4
        y40_s = sp.Ynm(4, 0, th, ph).expand(func=True)
        y44_s = sp.Ynm(4, 4, th, ph).expand(func=True)
        y4m4_s = sp.Ynm(4, -4, th, ph).expand(func=True)
        k4_s = y40_s + sp.sqrt(sp.Rational(5, 14)) * (y44_s + y4m4_s)
        rhs_s = sp.Rational(3, 5) + (4 * sp.sqrt(sp.pi) / 15) * k4_s
        residual = sp.trigsimp(sp.simplify((f_s - rhs_s).rewrite(sp.cos)))
        _check(
            "Sympy: trigsimp(sum_i n_i^4 - [3/5 + (4*sqrt(pi)/15) K_4]) = 0 identically",
            residual == 0,
            f"symbolic residual = {residual}",
        )

        def _inner(a, b):
            integrand = a * sp.conjugate(b) * sp.sin(th)
            return sp.integrate(
                sp.integrate(integrand, (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)
            )

        coef_sym = sp.simplify(_inner(f_s, k4_s) / _inner(k4_s, k4_s))
        _check(
            "Sympy: <f|K_4>/<K_4|K_4> = 4*sqrt(pi)/15 (exact spherical projection)",
            sp.simplify(coef_sym - 4 * sp.sqrt(sp.pi) / 15) == 0,
            f"projected coefficient = {coef_sym}",
        )
    except ImportError:
        print("  [skip] sympy not available -- symbolic identity check skipped")
        print("         (numeric pointwise check above already pins coef = 4*sqrt(pi)/15)")

    verdict = "PASS" if n_fail == 0 else "FAIL"
    print(f"\n  CUBIC-HARMONIC IDENTITY VERIFICATION: {verdict} "
          f"({n_pass}/{n_pass + n_fail} checks)")
    return n_fail == 0


# ============================================================
# Main experiment
# ============================================================

def run_experiment():
    t0 = time.time()

    print("=" * 78)
    print("FIXED-ACTION CUBIC-ANISOTROPY DIAGNOSTIC")
    print("Conditional SME-style scale parameterization")
    print("=" * 78)

    # ── Section 1: Lattice dispersion relation ────────────────────
    print(f"\n{'=' * 78}")
    print("1. LATTICE DISPERSION RELATION")
    print(f"{'=' * 78}")

    print("""
  On a cubic lattice with spacing a, the dispersion relation is:

    E^2 = m^2 + sum_i (4/a^2) sin^2(p_i a/2)

  (Standard second-order finite-difference Laplacian eigenvalue;
  see LORENTZ_VIOLATION_DERIVED_NOTE.md Step 2.)

  Taylor expanding for p_i a << 1:

    sin^2(p_i a/2) = (p_i a/2)^2 - (p_i a/2)^4/3 + (p_i a/2)^6*2/45 - ...

    (4/a^2) sin^2(p_i a/2) = p_i^2 - a^2 p_i^4/12 + a^4 p_i^6/360 - ...

  Therefore:
    E^2 = m^2 + p^2 - (a^2/12) sum_i p_i^4 + (a^4/360) sum_i p_i^6 - ...
                       ^^^^^^^^^^^^^^^^^^^^^^^^
                       LORENTZ-VIOLATING TERM

  The p_i^4 term is spatially anisotropic with cubic symmetry O_h.
  Its coefficient is a^2/12 for this supplied kinetic symbol. This runner
  does not derive the symbol, spacing, or a full spacetime representation.
""")

    # Numerical verification of the expansion
    a_test = 0.1  # lattice spacing in arbitrary units
    p_test = np.linspace(0, 0.5 / a_test, 200)
    m_test = 0.1

    E2_lattice = np.array([
        m_test**2 + (4.0/a_test**2) * math.sin(p * a_test / 2)**2
        for p in p_test
    ])
    E2_continuum = m_test**2 + p_test**2
    E2_corrected = m_test**2 + p_test**2 - (a_test**2 / 12.0) * p_test**4
    E2_order6 = (m_test**2 + p_test**2 - (a_test**2 / 12.0) * p_test**4
                 + (a_test**4 / 360.0) * p_test**6)

    # Check at p*a = 0.5 (moderately low momentum)
    idx_check = len(p_test) // 4
    p_c = p_test[idx_check]
    pa = p_c * a_test
    print(f"  Numerical verification (1D, a={a_test}, m={m_test}):")
    print(f"    At p*a = {pa:.4f}:")
    print(f"      E^2 (exact lattice) = {E2_lattice[idx_check]:.10f}")
    print(f"      E^2 (continuum)     = {E2_continuum[idx_check]:.10f}")
    print(f"      E^2 (p^4 corrected) = {E2_corrected[idx_check]:.10f}")
    print(f"      E^2 (p^6 corrected) = {E2_order6[idx_check]:.10f}")
    print(f"      Residual (lattice - p^4): "
          f"{abs(E2_lattice[idx_check] - E2_corrected[idx_check]):.4e}")
    print(f"      Residual (lattice - p^6): "
          f"{abs(E2_lattice[idx_check] - E2_order6[idx_check]):.4e}")

    # ── Section 2: SME coefficient mapping ────────────────────────
    print(f"\n{'=' * 78}")
    print("2. CONDITIONAL SME-STYLE COEFFICIENT PARAMETERIZATION")
    print(f"{'=' * 78}")

    print("""
  The Lorentz-violating correction decomposes in NORMALIZED real spherical
  harmonics Y_lm (scipy.special.sph_harm / sympy.Ynm convention):

    sum_i p_i^4 = p^4 * [3/5 + (4*sqrt(pi)/15) * K_4(theta, phi)]

  where K_4 is the cubic harmonic of order 4:
    K_4 = Y_{40} + sqrt(5/14) (Y_{44} + Y_{4,-4})

  The coefficient on K_4 is 4*sqrt(pi)/15 ~= 0.4727 with normalized Y_lm,
  NOT 4/5 (corrected 2026-05-29; verify_cubic_harmonic_identity() pins it).

  If a compatible carrier and sector matching are supplied, an SME-style
  parameterization would assign:
  - The correction is a dimension-6 operator (d=6, n=4 in p)
  - CPT-even (see Section 5 below)
  - The nonminimal SME coefficients are:

    c^(6)_{(I)00}   = -(a^2/12)(3/5) / sqrt(4 pi)        [isotropic, j=0]
    c^(6)_{(I)40}   = -(a^2/12)(4*sqrt(pi)/15) * (...)    [anisotropic, j=4, m=0]
    c^(6)_{(I)44}   = -(a^2/12)(4*sqrt(pi)/15) * (...)    [anisotropic, j=4, m=4]
    c^(6)_{(I)4,-4} = -(a^2/12)(4*sqrt(pi)/15) * (...)    [anisotropic, j=4, m=-4]

  The selected scalar symbol has no j=1,2,3 component. This does not set
  independent coefficients of a complete action to zero.
""")

    a_planck = L_PLANCK  # meters
    sme = compute_sme_coefficients(a_planck)

    print(f"  For a = l_Planck = {a_planck:.4e} m:")
    print(f"    a in natural units:    {sme['a_natural_units']:.4e} GeV^-1")
    print(f"    c4 coefficient (a^2/12): {sme['c4_coefficient']:.4e} GeV^-2")
    print(f"    c^(6) isotropic (j=0): {sme['c6_iso_j0']:.4e} GeV^-2")
    print(f"    c^(6) aniso (j=4,m=0): {sme['c6_aniso_j4_m0']:.4e} GeV^-2")

    print(f"\n  Dimensionless SME coefficients (c^(6) * m^2):")
    print(f"    Electron: c^(6) * m_e^2 = {sme['electron_c6']:.4e}")
    print(f"    Proton:   c^(6) * m_p^2 = {sme['proton_c6']:.4e}")
    print(f"    Photon:   c^(6) (dim-less) = {sme['photon_c6']:.4e} GeV^-2")

    # ── Section 2b: Cubic-harmonic identity verification ──────────
    # Pin the angular decomposition coefficient (normalized Y_lm): the
    # l=4 cubic-harmonic coefficient is 4*sqrt(pi)/15, not 4/5.
    identity_ok = verify_cubic_harmonic_identity()

    # ── Section 3: Experimental bounds comparison ─────────────────
    print(f"\n{'=' * 78}")
    print("3. HISTORICAL SCALE COMPARISON (NOT A VALIDATED EXCLUSION)")
    print(f"{'=' * 78}")

    print(f"\n  Natural suppression at E = 1 GeV:")
    E_test = 1.0  # GeV
    suppression = compute_suppression_factor(E_test, E_PLANCK_GEV)
    print(f"    (E/E_Planck)^2 = ({E_test} / {E_PLANCK_GEV:.4e})^2 "
          f"= {suppression:.4e}")

    print(f"\n  Conditional p^4 coefficient when a = l_Planck is supplied:")
    print(f"    a^2/12 = ({a_planck:.4e} m)^2 / 12")
    a_nat = a_planck * GEV_TO_INVMETER
    c4_pred = a_nat**2 / 12.0
    print(f"           = {c4_pred:.4e} GeV^-2")
    print(f"           = {c4_pred * E_PLANCK_GEV**2:.4e} (in E_Planck^-2 units)")

    print(f"\n  {'Experiment':<35} {'Sector':<10} {'Bound':<18} "
          f"{'Conditional':<18} {'Ratio':<12} {'Role'}")
    print(f"  {'─'*35} {'─'*10} {'─'*18} {'─'*18} {'─'*12} {'─'*20}")

    for name, info in EXPERIMENTAL_BOUNDS.items():
        sector = info["sector"]

        if "bound_gev_minus2" in info:
            bound = info["bound_gev_minus2"]
            prediction = c4_pred
            ratio = prediction / bound if bound > 0 else float('inf')
            bound_str = f"{bound:.2e} GeV^-2"
            pred_str = f"{prediction:.2e} GeV^-2"
        elif "bound_gev" in info:
            bound = info["bound_gev"]
            # For dimension-4 bounds, compare a^2/12 * E_typical^2
            E_typical = 1.0  # GeV for most experiments
            prediction = c4_pred * E_typical**2
            ratio = prediction / bound if bound > 0 else float('inf')
            bound_str = f"{bound:.2e} GeV"
            pred_str = f"{prediction * 1:.2e} GeV"
        elif "bound_dimensionless" in info:
            bound = info["bound_dimensionless"]
            # For gravity sector: s_bar is a dimension-4 (minimal SME) coeff.
            # Our dimension-6 coefficient contributes as c^(6) * E_char^2
            # where E_char ~ m_earth * v_orbit^2 ~ 10^-10 GeV for LLR.
            # More precisely: effective s_bar ~ c^(6) * p_char^2
            # For lunar laser ranging, p_char ~ m_photon_eff ~ 1 eV ~ 10^-9 GeV
            E_char_gravity = 1e-9  # GeV, characteristic energy for LLR
            prediction = c4_pred * E_char_gravity**2
            ratio = prediction / bound if bound > 0 else float('inf')
            bound_str = f"{bound:.2e}"
            pred_str = f"{prediction:.2e}"
        else:
            continue

        if ratio < 1e-6:
            status = "illustrative only"
        elif ratio < 1e-3:
            status = "illustrative only"
        elif ratio < 1:
            status = "illustrative only"
        else:
            status = "mapping unresolved"

        desc = info["description"][:34]
        print(f"  {desc:<35} {sector:<10} {bound_str:<18} "
              f"{pred_str:<18} {ratio:<12.2e} {status}")

    # ── Section 4: Staggered fermion taste-breaking ───────────────
    print(f"\n{'=' * 78}")
    print("4. STAGGERED FERMION TASTE-BREAKING CONTRIBUTIONS")
    print(f"{'=' * 78}")

    print("""
  Staggered fermions on a cubic lattice have 2^d degenerate tastes.
  Taste symmetry is broken at O(a^2), introducing ADDITIONAL Lorentz
  violation beyond the naive lattice dispersion.

  The taste-dependent LV has the form:
    delta(E^2)_taste = a^2 * C_taste * p^4

  where C_taste depends on the taste representation. The total LV
  for each taste is:
    (a^2/12)(1 + C_taste) * sum_i p_i^4

  Enhancement factors by taste (from lattice QCD):
""")

    taste_results = staggered_taste_breaking(a_nat)

    print(f"  {'Taste':<18} {'C_taste':<10} {'Enhancement':<14} "
          f"{'Total c^(6) (GeV^-2)':<22}")
    print(f"  {'─'*18} {'─'*10} {'─'*14} {'─'*22}")

    for taste, data in taste_results.items():
        print(f"  {taste:<18} {data['taste_factor']:<10.1f} "
              f"{data['enhancement_ratio']:<14.1f} "
              f"{data['total_c4']:<22.4e}")

    print(f"""
  These imported taste factors illustrate sensitivity of the selected model
  calculation only. The runner does not derive them for this framework or
  identify tastes with physical fermion species, so it makes no
  flavor-dependent Lorentz-violation prediction.
""")

    # ── Section 5: discrete-symmetry scope ────────────────────────
    print(f"\n{'=' * 78}")
    print("5. DISCRETE-SYMMETRY SCOPE")
    print(f"{'=' * 78}")

    symmetry_scope = discrete_symmetry_scope()

    print(f"""
  Verified here: the selected scalar kinetic symbol is even in momentum.

  Not supplied or verified here: a complete matter action and explicit C, T,
  or CPT operators. Therefore no exact-CPT theorem follows and no CPT-odd SME
  coefficient is fixed to zero by this calculation.

  {symmetry_scope['scope']}
""")

    # ── Section 6: conditional propagation diagnostic ─────────────
    print(f"\n{'=' * 78}")
    print("6. CONDITIONAL PROPAGATION DIAGNOSTIC")
    print(f"{'=' * 78}")

    print(f"""
  For a massless relativistic carrier governed by the supplied kinetic symbol,
  the leading finite-a anisotropy is governed by K_4(theta, phi). Neither that
  carrier identification nor a = l_Planck is derived here.

  1. DIRECTION-DEPENDENT PROPAGATION SPEED

     For a massless particle (photon, graviton):
       v(theta, phi) = c * [1 - (a^2/24) p^2 * f_4(theta, phi)]

     where f_4 = sin^4(theta)cos^4(phi) + sin^4(theta)sin^4(phi)
                 + cos^4(theta)

     The speed varies with direction by:
       delta_v / v ~ (a^2/24) * p^2 * (f_4_max - f_4_min)
                   = (a^2/24) * p^2 * (1 - 1/3)
                   = (a^2/36) * p^2

     For a = l_Planck, p = 10 GeV (Fermi LAT photon):
""")

    p_fermi = 10.0  # GeV
    a_nat_planck = L_PLANCK * GEV_TO_INVMETER
    aniso_correction = (a_nat_planck**2 / 36.0) * p_fermi**2
    print(f"       delta_v / v = (a^2/36) * p^2")
    print(f"                   = ({a_nat_planck:.4e})^2 / 36 * ({p_fermi})^2")
    print(f"                   = {aniso_correction:.4e}")

    print(f"""
     This is {aniso_correction:.1e}, approximately 10^-38.

  2. COMPARISON WITH EXPERIMENT

     Best photon birefringence bound:     ~10^-32    [GRB polarimetry]
     Best photon dispersion bound:        ~10^-21    [Fermi LAT at 10 GeV]
     Best electron anisotropy bound:      ~10^-27    [Hughes-Drever]
     Best gravity sector bound:           ~10^-9     [lunar laser ranging]

     The conditional value ({aniso_correction:.1e}) is shown only as a scale
     comparison; the runner has not established the sector mapping needed for
     an experimental exclusion.

  3. SCALING WITH ENERGY

     The suppression factor is (E/E_Planck)^2. To reach experimental
     sensitivity, we would need:

     (E/E_Planck)^2 > 10^-32  (photon birefringence bound)
     E > E_Planck * 10^-16 ~ 10^3 GeV ~ 1 TeV

     But at 1 TeV, the lattice correction for a Planck-scale lattice is:
     (1000 / 1.22e19)^2 / 12 = {(1000/E_PLANCK_GEV)**2 / 12:.4e}

     This is ~10^-32, which JUST touches the photon birefringence bound.
     At the LHC energy scale (14 TeV):
     (14000 / 1.22e19)^2 / 12 = {(14000/E_PLANCK_GEV)**2 / 12:.4e}

     Still below the birefringence bound by a factor of ~100.
""")

    # ── Section 7: Summary table ──────────────────────────────────
    print(f"\n{'=' * 78}")
    print("7. CONDITIONAL SCALE TABLE")
    print(f"{'=' * 78}")

    energies = [1e-3, 1e-1, 1.0, 10.0, 100.0, 1e3, 1e4, 1e7, 1e10]

    print(f"\n  Lattice: a = l_Planck = {L_PLANCK:.4e} m")
    print(f"  Leading LV coefficient: a^2/12 = {c4_pred:.4e} GeV^-2\n")

    print(f"  {'E (GeV)':<12} {'(E/E_Pl)^2':<14} {'|delta E^2/E^2|':<18} "
          f"{'|delta v/v|':<14} {'Best bound':<14} {'Margin':<14}")
    print(f"  {'─'*12} {'─'*14} {'─'*18} {'─'*14} {'─'*14} {'─'*14}")

    for E in energies:
        supp = compute_suppression_factor(E, E_PLANCK_GEV)
        delta_E2 = c4_pred * E**2  # fractional correction to E^2
        delta_v = delta_E2 / 2.0   # fractional velocity correction

        # Best applicable bound
        if E < 1:
            best_bound = 1e-27  # low-energy atomic physics
            bound_name = "atomic"
        elif E < 100:
            best_bound = 1e-23  # neutrino oscillations
            bound_name = "neutrino"
        elif E < 1e5:
            best_bound = 2.5e-22  # Fermi LAT (dim-6)
            bound_name = "Fermi LAT"
        else:
            best_bound = 1e-20  # generic astrophysical
            bound_name = "astro"

        margin = delta_v / best_bound if best_bound > 0 else float('inf')

        print(f"  {E:<12.1e} {supp:<14.2e} {delta_E2:<18.2e} "
              f"{delta_v:<14.2e} {best_bound:<14.2e} {margin:<14.2e}")

    # ── Section 8: Direction dependence (anisotropy) ──────────────
    print(f"\n{'=' * 78}")
    print("8. DIRECTIONAL ANISOTROPY (CUBIC LATTICE FINGERPRINT)")
    print(f"{'=' * 78}")

    print(f"\n  The cubic symmetry creates direction-dependent propagation.")
    print(f"  f_4(theta, phi) = sum_i (n_i)^4 for unit vector n.\n")

    directions = {
        "axis [100]":     (0.0, 0.0),
        "face diag [110]": (math.pi/4, 0.0),
        "body diag [111]": (math.acos(1/math.sqrt(3)), math.pi/4),
    }

    print(f"  {'Direction':<20} {'theta':<10} {'phi':<10} "
          f"{'f_4':<10} {'deviation from 3/5'}")
    print(f"  {'─'*20} {'─'*10} {'─'*10} {'─'*10} {'─'*20}")

    for name, (theta, phi) in directions.items():
        sx = math.sin(theta) * math.cos(phi)
        sy = math.sin(theta) * math.sin(phi)
        sz = math.cos(theta)
        f4 = sx**4 + sy**4 + sz**4
        dev = f4 - 3.0/5.0
        print(f"  {name:<20} {theta:<10.4f} {phi:<10.4f} "
              f"{f4:<10.4f} {dev:+.4f}")

    print(f"""
  The ratio f_4(axis) / f_4(diagonal) = {1.0 / (1.0/3.0):.1f}

  The factor-of-3 anisotropy is an exact property of this selected cubic
  momentum symbol. It is not a unique microscopic fingerprint: other models
  with the same cubic symmetry can share the angular pattern.
""")

    # ── Section 9: Hypothesis verdict ─────────────────────────────
    print(f"\n{'=' * 78}")
    print("SCOPE VERDICT")
    print(f"{'=' * 78}")

    print(f"""
  VERIFIED FOR THE SUPPLIED FIXED-ACTION MODEL:

  1. Spatial finite-a anisotropy
     - The selected momentum symbol has cubic group O_h
     - Leading correction: -(a^2/12) sum_i p_i^4
     - Dimension-6 p^4 term in the conditional parameterization

  2. CPT
     - Not established: the complete action and C/P/T operators are absent
     - No CPT-odd coefficient is fixed by this runner

  3. Conditional coefficient values if a = l_Planck and matching is supplied:
     - c^(6)_{{(I)00}} ~ {sme['c6_iso_j0']:.2e} GeV^-2 (isotropic)
     - c^(6)_{{(I)40}} ~ {sme['c6_aniso_j4_m0']:.2e} GeV^-2 (anisotropic)

  4. Natural suppression:
     - (E/E_Planck)^2 ~ 10^-38 at E = 1 GeV
     - Historical scale comparison only; no experimental verdict

  5. Staggered fermion taste-breaking:
     - Enhances LV by factor 2-4 depending on taste channel
     - Still far below experimental bounds
     - Imported illustration; no physical flavor identification established

  6. Characteristic angular signature:
     - Cubic harmonics (j=4 with m=0, +4, -4)
     - Factor of 3 anisotropy between lattice axis and body diagonal
     - Shared by models with the same cubic symmetry; not unique

  BOTTOM LINE:
    This runner validates the selected symbol's Taylor expansion and cubic
    harmonic identity. It does not promote the calculation to a four-axiom,
    CPT, SME-matching, or experimental-consistency result.
""")

    elapsed = time.time() - t0
    print(f"  Elapsed: {elapsed:.1f} s")
    print(f"\n{'=' * 78}")
    print("EXPERIMENT COMPLETE")
    print(f"  Cubic-harmonic identity check: "
          f"{'PASS' if identity_ok else 'FAIL'}")
    print(f"{'=' * 78}")

    return identity_ok


if __name__ == "__main__":
    ok = run_experiment()
    sys.exit(0 if ok else 1)
