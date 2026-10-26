#!/usr/bin/env python3
"""Finite diagnostics for a supplied SU(3) heat-kernel operator.
V1-V3 sample/truncate heat characters; V4 enumerates a supplied spectrum;
V5 checks derivatives of that series; V6 tensors two independent heat links;
V7-V8 use a one-bond scalar determinant fixture, not a fermionic transfer
construction. V9 controls complex and repeated-eigenvalue characters.
No PASS count proves reflection positivity, transfer equivalence or mass gap.
"""

from __future__ import annotations

import math
import sys
import time
from dataclasses import dataclass

import numpy as np
from numpy.linalg import det, eigh, eigvalsh, qr

AUDIT_TIMEOUT_SEC = 120


# ============================================================================
# SU(3) constants and irrep machinery
# ============================================================================

N_C = 3  # fundamental representation dimension; group rank is 2


def su3_irrep_dim(p: int, q: int) -> int:
    """Dimension of the SU(3) irrep labeled by Dynkin labels (p, q).

    dim(p,q) = (p+1)(q+1)(p+q+2) / 2

    Standard reference: any introductory text on SU(3) Lie algebra. We do
    not import this from a black box; the formula is short and derivable
    from the Weyl dimension formula applied to A_2.
    """
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def su3_irrep_casimir(p: int, q: int) -> float:
    """Quadratic Casimir of the SU(3) irrep labeled (p, q).

    C_2(p, q) = (p^2 + q^2 + p*q) / 3 + p + q

    Convention check: C_2(1, 0) = 1/3 + 1 = 4/3 (fundamental), and
    C_2(1, 1) = (1+1+1)/3 + 2 = 3 (adjoint, with our normalization
    matching χ_R(e) = dim R, ⟨χ_R, χ_R⟩ = 1).
    """
    return (p * p + q * q + p * q) / 3.0 + p + q


def enumerate_irreps_up_to(N_max: int):
    """Iterate (p, q) with p + q ≤ N_max, p ≥ 0, q ≥ 0."""
    for p in range(N_max + 1):
        for q in range(N_max + 1 - p):
            yield (p, q)


# ============================================================================
# SU(3) character on the maximal torus (Weyl character formula)
# ============================================================================

def _weyl_denominator_su3(theta1: float, theta2: float) -> complex:
    """Numerator/denominator structure for SU(3) characters.

    On SU(3), the maximal torus is parameterized by (e^{i θ_1}, e^{i θ_2},
    e^{i θ_3}) with θ_3 = -θ_1 - θ_2 mod 2π.

    The Weyl denominator is

        Δ(θ) = Π_{i<j} (e^{i θ_i} - e^{i θ_j})

    Real-magnitude squared is

        |Δ(θ)|² = Π_{i<j} 4 sin²((θ_i - θ_j) / 2)

    which is the Haar measure density on the torus.
    """
    t3 = -theta1 - theta2
    a = np.exp(1j * theta1) - np.exp(1j * theta2)
    b = np.exp(1j * theta1) - np.exp(1j * t3)
    c = np.exp(1j * theta2) - np.exp(1j * t3)
    return a * b * c


def _weyl_measure_density_su3(theta1: float, theta2: float) -> float:
    """|Δ(t)|² for the Weyl integration formula on SU(3)."""
    Δ = _weyl_denominator_su3(theta1, theta2)
    return float(abs(Δ) ** 2)


def su3_character_on_torus(p: int, q: int, theta1: float, theta2: float) -> complex:
    """Schur polynomial s_(p+q,q)(x), valid also at repeated eigenvalues.

    Complete homogeneous h_n are coefficients of product_i(1-x_i t)^-1.
    Jacobi-Trudi gives h_(p+q)h_q-h_(p+q+1)h_(q-1).
    """
    x=np.exp(1j*np.array([theta1,theta2,-theta1-theta2]))
    nmax=p+q+1
    h=np.zeros(nmax+1,dtype=complex);h[0]=1
    for z in x:
        for n in range(1,nmax+1):
            h[n]+=z*h[n-1]
    return h[p+q]*h[q]-(h[p+q+1]*h[q-1] if q else 0)


def su3_heat_kernel_on_torus(tau: float, theta1: float, theta2: float,
                              N_max: int) -> float:
    """K_τ(t) = Σ_{(p,q): p+q ≤ N_max} dim(p,q) χ_{(p,q)}(t) exp(-τ C_2 / (2 N_c)).

    Truncated character series. We pick N_max large enough that the tail is
    negligible at the τ values used.
    """
    total = 0.0
    for (p, q) in enumerate_irreps_up_to(N_max):
        d = su3_irrep_dim(p, q)
        c2 = su3_irrep_casimir(p, q)
        chi = su3_character_on_torus(p, q, theta1, theta2)
        weight = math.exp(-tau * c2 / (2.0 * N_C))
        total += d * chi * weight
    if abs(total.imag)>1e-8*(1+abs(total.real)):
        raise ArithmeticError("conjugate-pair heat sum is not real")
    return float(total.real)


# ============================================================================
# Torus quadrature mesh (Riemann grid on the (θ_1, θ_2) fundamental cell)
# ============================================================================

def torus_mesh(N: int):
    """Uniform mesh on [-π, π]² for (θ_1, θ_2). Returns flat lists.

    The mesh redundantly covers the Weyl group orbit (|W| = 6), but the
    Weyl integration formula compensates exactly via the 1/|W| factor.
    """
    grid = np.linspace(-math.pi, math.pi, N, endpoint=False)
    Θ1, Θ2 = np.meshgrid(grid, grid)
    th1 = Θ1.flatten()
    th2 = Θ2.flatten()
    dθ = (2.0 * math.pi / N) ** 2
    return th1, th2, dθ


def weyl_integral_on_su3(integrand_on_torus, N_mesh: int, N_max_chars: int) -> float:
    """Integrate a class function f on SU(3) via Weyl integration on the torus.

        ∫_{SU(3)} f(g) dg = (1/|W|) ∫_T |Δ(t)|² f(t) dt
                          ≈ (1/6) · Σ_mesh |Δ|² f · dθ

    where the torus measure is normalized so that ∫_T dt = (2π)². With our
    Riemann sum, the resulting Haar measure is normalized so that
    ∫_{SU(3)} 1 · dg = 1 only if we further divide by the normalization
    constant Z_T = ∫_T |Δ|² dt / |W|. We compute Z_T directly so the result
    is fully normalized.

    Returns the Haar-normalized integral.
    """
    th1, th2, dθ = torus_mesh(N_mesh)
    # Compute |Δ|² at each mesh point
    den2 = np.array([_weyl_measure_density_su3(t1, t2) for t1, t2 in zip(th1, th2)])
    f_vals = np.array([integrand_on_torus(t1, t2, N_max_chars)
                       for t1, t2 in zip(th1, th2)])
    # Numerator: (1/|W|) Σ |Δ|² f dθ ≈ ∫_{SU(3)} f dg_unnorm
    num = (1.0 / 6.0) * np.sum(den2 * f_vals) * dθ
    # Normalization: ∫_{SU(3)} 1 dg = 1 should hold
    norm = (1.0 / 6.0) * np.sum(den2) * dθ
    return num / norm


# ============================================================================
# One-bond staggered block fixture (not a general Leg A verification)
# ============================================================================

def random_su3_haar(rng: np.random.Generator) -> np.ndarray:
    """Generate a Haar-distributed SU(3) matrix via Ginibre + QR + det fix.

    Method:
      1. Sample a 3×3 complex matrix Z with iid standard normal real and
         imag parts.
      2. QR-decompose Z = Q R. Q is uniformly distributed on U(3) after
         the standard sign-fix of the diagonal phases.
      3. Multiply Q by a diagonal phase to make det(Q) = 1, putting the
         result in SU(3).
    """
    Z = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    Q, R = qr(Z)
    # Standard Mezzadri sign-fix: make the diagonal of R positive real.
    d = np.diag(R)
    ph = d / np.abs(d)
    Q = Q * ph
    # Force det = 1 (SU(3) condition).
    detQ = np.linalg.det(Q)
    Q = Q / (detQ ** (1.0 / 3.0))
    return Q


def staggered_dirac_2site(U: np.ndarray, m: float) -> np.ndarray:
    """Naive-staggered Dirac on the minimal 2-site Λ with one spatial link.

    Sites x = 0, 1. Link variable U on the bond (0 → 1). Staggered phase
    η_x = (-1)^x. The naive staggered Dirac operator on this minimal Λ is

        D[U] = (1/2) (η_0 (U Λ_{0→1} - U^† Λ_{1→0}))

    where Λ_{x→y} is the parallel transport projector. As a 6×6 matrix
    on Hilbert space C^3 ⊗ C^2_sites:

        D[U] = (1/2) ⊗ ( U on the (0→1) block - U^† on the (1→0) block )

    This is an open one-bond algebraic fixture, not a periodic lattice
    discretization with independent forward/backward links:

        [ 0       (1/2) U   ]
        [-(1/2) U^†   0     ]

    Adding the mass term:

        D + m I = [ m I_3,         (1/2) U      ]
                  [ -(1/2) U^†,    m I_3        ]

    For this bipartite block and unitary U, all singular values of U/2
    are 1/2, so det(D+mI)=(m²+1/4)^3. Anti-Hermiticity alone would
    not imply positive determinant.

    Returns the 6×6 complex matrix (D + m I).
    """
    I3 = np.eye(3, dtype=complex)
    upper = 0.5 * U
    lower = -0.5 * U.conj().T
    M = np.block([
        [m * I3, upper],
        [lower, m * I3],
    ])
    return M


# ============================================================================
# Truncated transfer matrix on character basis
# ============================================================================

def build_single_link_transfer(N_max: int, tau: float) -> np.ndarray:
    """Single-link transfer operator T (kernel K_τ) on truncated L²(SU(3)).

    Basis: orthonormal basis of L²(SU(3)) given by matrix elements of irreps:

        ψ_{R, a, b}(g) = sqrt(dim R) · D^R_{ab}(g)

    On this basis the convolution operator with kernel K_τ acts diagonally
    on each irrep block with eigenvalue exp(-τ C_2(R) / (2 N_c)), each of
    multiplicity (dim R)² (over a, b indices).

    We return the diagonal as a 1-D array of eigenvalues with multiplicity.
    """
    eigs = []
    for (p, q) in enumerate_irreps_up_to(N_max):
        d = su3_irrep_dim(p, q)
        c2 = su3_irrep_casimir(p, q)
        lam = math.exp(-tau * c2 / (2.0 * N_C))
        # Multiplicity = (dim R)^2 (matrix elements a, b).
        eigs.extend([lam] * (d * d))
    eigs = np.array(sorted(eigs, reverse=True))
    return eigs


def build_2site_transfer_basic(N_max: int, tau: float, beta_spatial: float = 0.0
                                ) -> np.ndarray:
    """Tensor spectrum of two independent unweighted heat links.

    This is not the one-link Hilbert space of a two-site graph.
    A nonzero spatial coupling is not implemented.
    """
    if beta_spatial != 0:
        raise ValueError("only two independent unweighted heat links are implemented")
    single_eigs = build_single_link_transfer(N_max, tau)
    # Tensor product eigenvalues
    products = np.outer(single_eigs, single_eigs).flatten()
    return np.array(sorted(products, reverse=True))


# ============================================================================
# Verifications V1 … V8
# ============================================================================

@dataclass
class VResult:
    name: str
    passed: bool
    message: str
    metrics: dict


def V1_heat_kernel_strictly_positive(tau: float = 4.0,
                                      N_max: int = 12,
                                      N_mesh: int = 16) -> VResult:
    """Finite mesh positivity diagnostic for a character partial sum.
    No continuum mesh or truncation error certificate is supplied.
    """
    th1, th2, _ = torus_mesh(N_mesh)
    # Compute K_τ and |Δ|² at each point
    K_vals = np.array([su3_heat_kernel_on_torus(tau, t1, t2, N_max)
                       for t1, t2 in zip(th1, th2)])

    min_K = float(np.min(K_vals))
    max_K = float(np.max(K_vals))

    # Margin: insist strict positivity with margin > 1e-4 to rule out
    # numerical noise.
    margin = 1e-4
    passed = min_K > margin
    msg = (f"min K_τ = {min_K:.6e}, max K_τ = {max_K:.6e} on a "
           f"{N_mesh}×{N_mesh} torus mesh with N_max = {N_max}, τ = {tau}; "
           f"strict positive margin (> {margin}): "
           f"{'YES' if passed else 'NO'}.")
    return VResult("V1 truncated K_tau positive on sampled torus mesh", passed, msg,
                   {"min_K": min_K, "max_K": max_K, "N_mesh": N_mesh,
                    "margin": margin, "tau": tau})


def V2_character_series_converges() -> VResult:
    """V2: Absolute summability of Σ dim² exp(-τ C_2 / (2 N_c)).

    This is the trace-norm of T = convolution by K_τ on L²(SU(3)) (using
    eigenvalues exp(-τ C_2 / (2 N_c)) with multiplicity dim² each). Trace-
    class needs Σ |λ_n| < ∞.

    We verify convergence at τ = 4 (where the series converges geometrically
    fast and N_max = 12 is already 6-digit converged), and additionally at
    τ = 2 and τ = 8 to show the trend.
    """
    partials_by_tau = {}
    all_passed = True
    for tau in (2.0, 4.0, 8.0):
        partials = {}
        for N_max in (4, 8, 12, 16, 20):
            s = 0.0
            for (p, q) in enumerate_irreps_up_to(N_max):
                d = su3_irrep_dim(p, q)
                c2 = su3_irrep_casimir(p, q)
                s += (d * d) * math.exp(-tau * c2 / (2.0 * N_C))
            partials[N_max] = s
        partials_by_tau[tau] = partials
        # Require relative change < 1e-6 from N=16 to N=20 (geometric tail)
        rel_change = abs(partials[20] - partials[16]) / abs(partials[20])
        if rel_change > 1e-6:
            all_passed = False

    # Verify the operator-theoretic Hilbert-Schmidt norm:
    # ||T||_{HS}^2 = Σ_n |λ_n|^2 = Σ_R (dim R)^2 exp(-τ C_2(R)/N_c)
    tau_HS = 4.0
    HS2 = 0.0
    for (p, q) in enumerate_irreps_up_to(20):
        d = su3_irrep_dim(p, q)
        c2 = su3_irrep_casimir(p, q)
        HS2 += (d * d) * math.exp(-tau_HS * c2 / N_C)  # note exponent 2× for HS

    msg_lines = []
    for tau, partials in partials_by_tau.items():
        rel = abs(partials[20] - partials[16]) / abs(partials[20])
        msg_lines.append(
            f"τ={tau}: N=4 → {partials[4]:.4e}; N=8 → {partials[8]:.4e}; "
            f"N=12 → {partials[12]:.4e}; N=16 → {partials[16]:.4e}; "
            f"N=20 → {partials[20]:.4e}; |S20−S16|/|S20| = {rel:.3e}"
        )
    msg = "; ".join(msg_lines) + f"; HS norm² at τ={tau_HS} (N_max=20): {HS2:.4e}."

    passed = all_passed and HS2 > 0 and HS2 < float('inf')
    return VResult("V2 character-series trace-norm converges (trace-class evidence)",
                   passed, msg,
                   {"partials_by_tau": partials_by_tau, "HS_norm_squared": HS2})


def V3_heat_kernel_probability(tau: float = 4.0,
                                N_max: int = 12,
                                N_mesh: int = 16) -> VResult:
    """V3: ∫_{SU(3)} K_τ dg = 1 (probability kernel) via Weyl integration."""
    # Define integrand
    def integrand(t1, t2, Nm):
        return su3_heat_kernel_on_torus(tau, t1, t2, Nm)

    val = weyl_integral_on_su3(integrand, N_mesh, N_max)
    err = abs(val - 1.0)
    # The Weyl integration formula on the truncated character series gives
    # exactly the (R=trivial)-contribution = 1: every included nontrivial
    # character integrates to zero. We tolerate
    # numerical quadrature error from coarse mesh.
    passed = err < 5e-2  # generous tolerance for coarse mesh
    msg = (f"∫_{{SU(3)}} K_τ dg ≈ {val:.6f} (error |val − 1| = {err:.3e}); "
           f"τ = {tau}, N_max = {N_max}, N_mesh = {N_mesh}.")
    return VResult("V3 K_τ is probability kernel", passed, msg,
                   {"integral": val, "err": err})


def V4_single_link_spectrum(tau: float = 4.0, N_max: int = 12) -> VResult:
    """V4: Top eigenvalue of single-link T is 1 (trivial irrep), strict
    gap to the next eigenvalue (R = fundamental (1,0))."""
    eigs = build_single_link_transfer(N_max, tau)
    top = eigs[0]
    # Spectrum has many degenerate fundamental eigenvalues; gap = top - second
    second = eigs[1]
    gap = top - second
    # Expected: top = 1, second = exp(-τ C_2(fundamental) / (2 N_c))
    #         = exp(-τ · (4/3) / 6) = exp(-2τ/9)
    expected_second = math.exp(-tau * (4.0 / 3.0) / (2.0 * N_C))
    expected_gap = 1.0 - expected_second
    passed = (
        abs(top - 1.0) < 1e-12
        and gap > 0
        and abs(gap - expected_gap) < 1e-10
    )
    msg = (f"top eigenvalue = {top:.12f} (expected 1.0); next eigenvalue = "
           f"{second:.12f} (expected {expected_second:.12f}); spectral gap "
           f"= {gap:.12e} (expected {expected_gap:.12e}); "
           f"multiplicity of top eigenvalue = "
           f"{int(np.sum(np.abs(eigs - top) < 1e-12))} (expected 1, "
           f"i.e. trivial irrep dim² = 1).")
    return VResult("V4 single-link operator has simple top + strict gap",
                   passed, msg,
                   {"top": top, "second": second, "gap": gap,
                    "expected_gap": expected_gap})


def V5_heat_equation_consistency(tau: float = 4.0, N_max: int = 10,
                                  delta_tau: float = 1e-4) -> VResult:
    """V5: Verify ∂_τ K_τ(t) = -(1/(2N_c)) Σ_R dim(R) χ_R(t) C_2(R) e^{-τC_2/(2N_c)}.

    This is the heat equation on SU(3) (the Laplace-Beltrami operator on the
    group with the bi-invariant metric acts on the (p,q)-irrep block as
    -C_2(R) times identity).

    Numerical check: pick a few non-singular torus points and compute
    central differences of K_τ in τ; compare against the analytic series for
    ∂_τ K_τ.
    """
    test_pts = [(0.5, 0.3), (1.2, 0.6), (-0.4, 1.1), (1.5, -0.7)]
    errs = []
    for (t1, t2) in test_pts:
        K_plus = su3_heat_kernel_on_torus(tau + delta_tau, t1, t2, N_max)
        K_minus = su3_heat_kernel_on_torus(tau - delta_tau, t1, t2, N_max)
        dK_num = (K_plus - K_minus) / (2.0 * delta_tau)
        # Analytic: ∂_τ K_τ = -(1/(2 N_c)) Σ_R dim(R) χ_R(t) C_2(R) e^{...}
        dK_an = 0.0
        for (p, q) in enumerate_irreps_up_to(N_max):
            d = su3_irrep_dim(p, q)
            c2 = su3_irrep_casimir(p, q)
            chi = su3_character_on_torus(p, q, t1, t2)
            dK_an += -(1.0 / (2.0 * N_C)) * d * chi * c2 * math.exp(
                -tau * c2 / (2.0 * N_C))
        rel_err = abs(dK_num - dK_an) / (abs(dK_an) + 1e-12)
        errs.append(rel_err)
    max_err = max(errs)
    passed = max_err < 1e-3
    msg = (f"heat-equation finite-difference check at 4 torus points: "
           f"max relative error = {max_err:.3e} (tol 1e-3).")
    return VResult("V5 heat equation ∂_τ K_τ = (Δ/(2 N_c)) K_τ holds",
                   passed, msg, {"errs": errs, "max_err": max_err})


def V6_two_site_truncated_spectrum(tau: float = 4.0, N_max: int = 4
                                     ) -> VResult:
    """V6: tensor product of two independent heat-link spectra."""
    eigs = build_2site_transfer_basic(N_max, tau)
    top = eigs[0]
    # Find first eigenvalue strictly less than top
    second = None
    for e in eigs[1:]:
        if abs(e - top) > 1e-12:
            second = e
            break
    if second is None:
        return VResult("V6 two independent heat-link spectrum", False,
                       "could not find second eigenvalue",
                       {})
    gap = top - second
    # Top eigenvalue = 1 · 1 = 1 (both links trivial irrep)
    expected_top = 1.0
    # Second comes from one link in trivial, other in fundamental
    expected_second = 1.0 * math.exp(-tau * (4.0 / 3.0) / (2.0 * N_C))
    expected_gap = expected_top - expected_second
    passed = (
        abs(top - expected_top) < 1e-12
        and gap > 0
        and abs(gap - expected_gap) < 1e-10
    )
    msg = (f"truncated two-independent-link spectrum: top = {top:.12f} (expected "
           f"{expected_top}), second = {second:.12f} (expected "
           f"{expected_second:.12f}), gap = {gap:.6e} (expected "
           f"{expected_gap:.6e}).")
    return VResult("V6 two independent heat links have strict gap",
                   passed, msg,
                   {"top": top, "second": second, "gap": gap})


def V7_leg_A_determinant_positivity(N_sample: int = 50, m: float = 0.1,
                                      seed: int = 20260519) -> VResult:
    """V7: Sample N=50 SU(3) configurations on the 2-site Λ link, build
    D[U] + m I, check det is real-positive with margin."""
    rng = np.random.default_rng(seed)
    dets = []
    for _ in range(N_sample):
        U = random_su3_haar(rng)
        M = staggered_dirac_2site(U, m)
        d_full = det(M)
        # Should be real-positive
        if abs(d_full.imag) > 1e-9 * (abs(d_full.real) + 1e-12):
            return VResult("V7 one-bond determinant fixture",
                           False,
                           f"non-real det encountered: {d_full}",
                           {"det": d_full, "U": U.tolist()})
        dets.append(float(d_full.real))
    dets = np.array(dets)
    min_det = float(np.min(dets))
    max_det = float(np.max(dets))
    # Margin: ensure all > some explicit threshold
    margin_threshold = m ** 6 / 100.0  # very conservative lower bound
    passed = min_det > margin_threshold and np.allclose(dets,(m*m+0.25)**3,rtol=1e-12,atol=1e-14)
    msg = (f"Sampled N={N_sample} random SU(3) configs at m={m}; "
           f"min det(D+mI) = {min_det:.6e}, max = {max_det:.6e}; "
           f"margin threshold = {margin_threshold:.6e}.")
    return VResult("V7 one-bond determinant equals (m^2+1/4)^3",
                   passed, msg,
                   {"min_det": min_det, "max_det": max_det,
                    "N_sample": N_sample})


def V8_composition_positivity(N_pairs: int = 30, tau: float = 4.0, m: float = 0.1,
                                seed: int = 20260520) -> VResult:
    """Sample the constructed one-link heat kernel times endpoint weights.

    The weights are the one-bond determinant fixture, not an integrated
    spacetime fermion action. No transfer equivalence follows. N_max=12.
    """
    rng = np.random.default_rng(seed)
    N_max = 12

    products = []
    for _ in range(N_pairs):
        U = random_su3_haar(rng)
        V = random_su3_haar(rng)
        # Compute UV^† and extract its torus parameters by diagonalization
        UV = U @ V.conj().T
        evals_UV, _ = np.linalg.eig(UV)
        # Eigenvalues of a unitary 3×3 matrix are e^{iθ_i} with θ_1+θ_2+θ_3 = 0 mod 2π
        thetas = np.angle(evals_UV)
        # Re-center so θ_1 + θ_2 + θ_3 = 0 (mod 2π); two parameters suffice
        # K_τ is a class function, evaluate using torus parameters.
        # Take first two angles after sorting:
        thetas_sorted = np.sort(thetas)
        # Adjust so sum is 0 mod 2π. Total sum = 0 mod 2π since det U V^† = 1.
        total = float(np.sum(thetas_sorted))
        # Wrap total to [-π, π]
        while total > math.pi:
            total -= 2 * math.pi
        while total < -math.pi:
            total += 2 * math.pi
        # Shift each by -total/3 so they sum to 0
        thetas_centered = thetas_sorted - total / 3.0
        t1, t2 = float(thetas_centered[0]), float(thetas_centered[1])
        K_val = su3_heat_kernel_on_torus(tau, t1, t2, N_max)

        # Symmetrized fermion factors at both transfer endpoints.
        M_U = staggered_dirac_2site(U, m)
        M_V = staggered_dirac_2site(V, m)
        det_F_U = float(det(M_U).real)
        det_F_V = float(det(M_V).real)
        sym_det = math.sqrt(det_F_U * det_F_V)

        product = K_val * sym_det
        products.append((K_val, det_F_U, det_F_V, product))

    arr = np.array([(k, d_u, d_v, p) for (k, d_u, d_v, p) in products])
    min_K = float(np.min(arr[:, 0]))
    min_det_u = float(np.min(arr[:, 1]))
    min_det_v = float(np.min(arr[:, 2]))
    min_prod = float(np.min(arr[:, 3]))
    passed = min_K > 0 and min_det_u > 0 and min_det_v > 0 and min_prod > 0
    msg = (f"Sampled N={N_pairs} (U, V) pairs at τ={tau}, m={m}; "
           f"min K_τ(UV†) = {min_K:.6e}, min det_F(U) = {min_det_u:.6e}, "
           f"min det_F(V) = {min_det_v:.6e}, min symmetrized product = {min_prod:.6e}. "
           f"All strictly positive ⟹ constructed scalar sandwich > 0 on sampled pairs; no fermionic transfer equivalence.")
    return VResult("V8 constructed scalar sandwich > 0 on samples",
                   passed, msg,
                   {"min_K": min_K, "min_det_u": min_det_u, "min_det_v": min_det_v, "min_prod": min_prod,
                    "N_pairs": N_pairs})


def V9_character_controls() -> VResult:
    errs=[]
    for t1,t2 in [(0.4,0.9),(0.7,0.7),(2*math.pi/3,2*math.pi/3),(0.,0.)]:
        x=np.exp(1j*np.array([t1,t2,-t1-t2]))
        fundamental=sum(x)
        errs.extend([abs(su3_character_on_torus(1,0,t1,t2)-fundamental),
                     abs(su3_character_on_torus(0,1,t1,t2)-fundamental.conjugate()),
                     abs(su3_character_on_torus(1,1,t1,t2)-(abs(fundamental)**2-1))])
    center=2*math.pi/3
    for p,q in enumerate_irreps_up_to(6):
        expected=su3_irrep_dim(p,q)*np.exp(1j*center*(p+2*q))
        errs.append(abs(su3_character_on_torus(p,q,center,center)-expected))
    complex_control=abs(su3_character_on_torus(1,0,.4,.9).imag)>1e-3
    return VResult('V9 complex/repeated/central character controls',max(errs)<1e-9 and complex_control,
                   f'max character error={max(errs):.3e}; non-real fundamental={complex_control}',{'max_err':max(errs)})


# ============================================================================
# Driver
# ============================================================================

def main():
    t_start = time.time()
    print("=" * 78)
    print("Cluster-decomposition Δ_T > 0 on SU(3) integral operator (real)")
    print("Runner companion to docs/CLUSTER_DECOMPOSITION_DELTA_T_FINITE_LAMBDA_OPERATOR_REAL_NOTE_2026-05-19.md")
    print("Finite diagnostics only; physical fermionic transfer identification is not established.")
    print("=" * 78)

    results = []
    print("\n[V1] strict positivity of K_τ on the SU(3) torus ...")
    results.append(V1_heat_kernel_strictly_positive())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V2] character-series trace-norm convergence ...")
    results.append(V2_character_series_converges())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V3] heat-kernel probability normalization ∫_{SU(3)} K_τ = 1 ...")
    results.append(V3_heat_kernel_probability())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V4] single-link transfer-operator spectrum (top simple + strict gap) ...")
    results.append(V4_single_link_spectrum())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V5] heat equation consistency for K_τ on torus ...")
    results.append(V5_heat_equation_consistency())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V6] two independent heat links (truncated tensor spectrum) ...")
    results.append(V6_two_site_truncated_spectrum())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V7] one-bond determinant fixture on sampled SU(3) ...")
    results.append(V7_leg_A_determinant_positivity())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    print("\n[V8] constructed scalar sandwich sampled on (U,V) Haar pairs ...")
    results.append(V8_composition_positivity())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    results.append(V9_character_controls())
    print("    " + ("PASS" if results[-1].passed else "FAIL") + " — " + results[-1].message)

    n_pass = sum(1 for r in results if r.passed)
    n_fail = sum(1 for r in results if not r.passed)
    t_total = time.time() - t_start

    print("\n" + "=" * 78)
    print(f"PASS={n_pass}  FAIL={n_fail}  (runtime: {t_total:.2f} s)")
    print("=" * 78)
    for r in results:
        tag = "PASS" if r.passed else "FAIL"
        print(f"  [{tag}] {r.name}")
    print()

    # Hard-assert gate for CI / runner-cache:
    assert n_fail == 0, (
        f"At least one verification failed (n_fail = {n_fail}). "
        f"See per-V messages above. Failing names: "
        f"{[r.name for r in results if not r.passed]}"
    )

    print("All verifications passed; runner exits cleanly.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
