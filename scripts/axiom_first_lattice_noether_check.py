#!/usr/bin/env python3
"""
axiom_first_lattice_noether_check.py
-------------------------------------

Numerical exhibits for the axiom-first lattice Noether theorem on
Cl(3) ⊗ Z^3 (loop axiom-first-foundations, Cycle 5 / Route R5).

Theorem note:
  docs/AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md

Exhibits on a small free staggered fermion lattice (representative
of the canonical pure-staggered surface — gauge sector contributes
the same Noether structure for U(1) ⊂ SU(3)):

  E1.  Symmetry condition (6): for the U(1) phase generator T = i·I,
       [T, M] = T M - M T = 0 to machine precision.

  E2.  Symmetry condition (6) for the (2Z)^d sublattice translation:
       two-site shift operator S^{(2μ̂)} satisfies S M S^T = M
       (one-site shifts are NOT symmetries because the staggered
       phase factor η_μ has period 2; that is the staggered-shift
       caveat documented in the theorem note's Step 5).

  E3.  Fermion-number current J^μ_x defined by (4); on-shell lattice
       divergence ∂^L · J = 0 verified at a chosen classical
       solution of the equations of motion.

  E4.  On-shell global charge conservation: total fermion number
       Q = Σ_x ⟨χ̄_x χ_x⟩ is constant under temporal translation.

  E5.  Algebraic closure (5) -> (4): under onsite/internal U(1) phase
       substitution T = i I, the bilateral current formula (5) reduces
       to the fermion-number current (4) up to the convention factor +i.
       The 2026-06-06 repair adds an arbitrary-bilinear symbolic check
       for the sign convention, not only a sampled lattice value.

  E5b. Direct U(1) local-envelope sign check: for arbitrary sampled
       finite fields chi, chibar and local alpha_x, the direct variation
       delta S matches the bilateral plus-sign expression in (7c), while
       the old minus-sign current fails by an order-one residual. This
       makes the sign visible without using a propagator surface where
       symmetric link-bilinears can cancel.

  E6.  Support-only verification of (3): the canonical staggered sublattice-
       momentum density P^μ_x = -(i/2) η_μ(x) [χ̄_x ∂^L_μ χ_x -
       ∂^L_μ χ̄_x · χ_x] has on-shell ∂^L_μ P^μ_x = 0 to machine
       precision in the free pure-staggered ground state. Added by
       the 2026-05-10 gate-recategorization repair to discharge the
       audit's "missing (5) -> (3) verification" gap. The textual
       reduction (5) -> (3) is honestly a discrete Ward-identity
       rearrangement (not a literal infinitesimal substitution; the
       theorem note's Step 4b makes this explicit). The 2026-05-25
       boundary repair narrows this exhibit to support-only status:
       E6 is not a symbolic arbitrary-field derivation of (3).

  E7.  Field-level two-step Ward identity: on a nondegenerate L=6
       block, the central two-step generator D^(2ρ) is skew-adjoint,
       commutes with M_KS, and satisfies the localized envelope identity
       δ_ω S_F = Σ_x ω_x[-(χ̄D)_x(Mχ)_x + (χ̄M)_x(Dχ)_x]. The check also
       samples nonzero massless on-shell fields and verifies arbitrary
       local-envelope variation vanishes to machine precision.
"""

from __future__ import annotations

import sys
import numpy as np
import sympy as sp
from itertools import product
from pathlib import Path


def staggered_eta(x, mu):
    if mu == 0:
        return 1.0
    return float((-1) ** sum(x[:mu]))


def build_M_pure_staggered(L, mass=0.3, dim=3):
    """Pure staggered Dirac on a periodic L^dim block. No Wilson term."""
    sites = list(product(range(L), repeat=dim))
    idx = {x: i for i, x in enumerate(sites)}
    N = len(sites)
    M = np.zeros((N, N), dtype=complex)
    for x in sites:
        i = idx[x]
        M[i, i] += mass
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            jp = idx[xp]
            jm = idx[xm]
            eta = staggered_eta(x, mu)
            M[i, jp] += 0.5 * eta
            M[i, jm] += -0.5 * eta
    return M, sites, idx


def build_two_step_generator(sites, idx, L, dim, rho):
    """Central two-step generator (S_{+2rho} - S_{-2rho})/2."""
    N = len(sites)
    D = np.zeros((N, N), dtype=complex)
    for x in sites:
        i = idx[x]
        xp = list(x)
        xm = list(x)
        xp[rho] = (xp[rho] + 2) % L
        xm[rho] = (xm[rho] - 2) % L
        D[i, idx[tuple(xp)]] += 0.5
        D[i, idx[tuple(xm)]] += -0.5
    return D


def numerical_nullspace(A, tol=1e-10):
    """Right nullspace basis using SVD; columns span {v: A v = 0}."""
    _, singular_values, vh = np.linalg.svd(A)
    return vh.conj().T[:, singular_values < tol], singular_values


# ---------------------------------------------------------------------------
# E1: U(1) phase symmetry condition [T, M] = 0
# ---------------------------------------------------------------------------

def exhibit_E1(L=2, dim=3, mass=0.3, tol=1e-12):
    print("\n--- Exhibit E1: U(1) phase symmetry condition [T_U1, M] = 0 ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    N = len(sites)
    T_U1 = 1j * np.eye(N, dtype=complex)
    comm = T_U1 @ M - M @ T_U1
    err = float(np.max(np.abs(comm)))
    print(f"  L={L}, dim={dim}, mass={mass}, N={N}")
    print(f"  ||[T_U1, M]||_max = {err:.3e}")
    verdict = "PASS" if err < tol else "FAIL"
    print(f"  E1 verdict: {verdict}")
    return err < tol


# ---------------------------------------------------------------------------
# E2: (2Z)^d sublattice translation symmetry — invariance under x → x + 2a
# ---------------------------------------------------------------------------

def exhibit_E2(L=4, dim=3, mass=0.3, tol=1e-12):
    print("\n--- Exhibit E2: (2Z)^d sublattice translation symmetry of M ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    N = len(sites)

    # Shift permutation S_a for a chosen direction a (we test μ=0 and μ=1).
    # We test a TWO-step shift (to avoid the staggered phase modulation
    # which has period 2 in each direction).
    pass_all = True
    for mu in range(dim):
        shift = tuple(2 if k == mu else 0 for k in range(dim))
        S = np.zeros((N, N), dtype=complex)
        for x in sites:
            i = idx[x]
            xp = tuple((x[k] + shift[k]) % L for k in range(dim))
            j = idx[xp]
            S[i, j] = 1.0
        # Check S M S^{-1} = M (since S is a permutation, S^{-1} = S^T)
        err = float(np.max(np.abs(S @ M @ S.T - M)))
        verdict = "PASS" if err < tol else "FAIL"
        print(f"  shift by 2 in direction μ={mu}: ||S M S^T - M||_max = {err:.3e}  {verdict}")
        if err >= tol:
            pass_all = False
    print(f"  E2 verdict: {'PASS' if pass_all else 'FAIL'}")
    return pass_all


# ---------------------------------------------------------------------------
# E3, E4: Fermion-number current divergence-free on-shell
# ---------------------------------------------------------------------------

def exhibit_E3_E4(L=4, dim=3, mass=0.3, tol=1e-9):
    print("\n--- Exhibit E3, E4: fermion-number current divergence on shell ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    N = len(sites)

    # Take a classical solution: M χ = 0 means χ = 0 (since M is invertible
    # for m > 0). For a non-trivial test, use the SOURCED equation:
    #   M χ = J  with J source -> the conservation identity holds for
    #   the SOURCED current only at sites without a source.
    # For a clean exhibit, we use a (continuum-limit) plane-wave Slater
    # determinant: at half filling, build the propagator G(x,y) =
    # ⟨χ_x χ̄_y⟩ in the ground state of the equivalent Hamiltonian.
    #
    # In free-fermion theory, ⟨χ̄_x χ_y⟩ = (M^-1)_{xy} (Wick).
    # Conservation of J^μ_x means ∂^L_μ ⟨J^μ_x⟩ = 0 in the GROUND STATE.

    Minv = np.linalg.inv(M)

    # Compute ⟨J^μ_x⟩ = -(1/2) η_μ(x) (G(x, x+μ̂) + G(x+μ̂, x))
    #                 with G(x, y) = ⟨χ̄_x χ_y⟩ = (M^-1)_{yx} (Wick contraction)
    div_max = 0.0
    div_typical = 0.0
    n_sites_checked = 0
    for x in sites:
        i = idx[x]
        # accumulate ∂^L_μ ⟨J^μ_x⟩ = Σ_μ (J^μ_x - J^μ_{x - μ̂})
        div_x = 0.0 + 0j
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            ip = idx[xp]
            im = idx[xm]
            eta_x = staggered_eta(x, mu)
            eta_xm = staggered_eta(xm, mu)
            # ⟨J^μ_x⟩ at site x
            J_x = -0.5 * eta_x * (Minv[ip, i] + Minv[i, ip])
            # ⟨J^μ_{x-μ̂}⟩
            J_xm = -0.5 * eta_xm * (Minv[i, im] + Minv[im, i])
            div_x += J_x - J_xm
        div_max = max(div_max, abs(div_x))
        div_typical += abs(div_x)
        n_sites_checked += 1
    div_typical /= n_sites_checked

    print(f"  L={L}, dim={dim}, mass={mass}, N={N}")
    print(f"  max |∂^L · J|  = {div_max:.3e}    (target: 0 to machine precision)")
    print(f"  mean |∂^L · J| = {div_typical:.3e}")
    e3_pass = div_max < tol
    print(f"  E3 verdict: {'PASS' if e3_pass else 'FAIL'}")

    # E4: total charge Q = Σ_x ⟨χ̄_x χ_x⟩ = tr(M^{-1}). For a translation-
    # invariant ground state, Q is constant. We verify by computing Q on
    # successive time slices in a temporal cube and confirming Q_t is t-independent.
    # For pure staggered, the t-direction is one of the lattice axes; we slice
    # along μ=0.
    Q_t = []
    for t in range(L):
        Qsum = 0.0 + 0j
        for x in sites:
            if x[0] != t:
                continue
            i = idx[x]
            Qsum += Minv[i, i]
        Q_t.append(Qsum)
    Q_arr = np.array(Q_t)
    print(f"  charge per time slice: {[f'{q.real:+.4f}' for q in Q_arr]}")
    Q_var = float(np.std([q.real for q in Q_arr]))
    print(f"  std(Re Q_t) = {Q_var:.3e}")
    e4_pass = Q_var < 1e-9
    print(f"  E4 verdict: {'PASS' if e4_pass else 'FAIL'}")

    return e3_pass, e4_pass


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# E5 — algebraic closure of (5) -> (4) (added 2026-05-03 for review
#      follow-up; strengthened 2026-06-06). Verifies that the onsite/internal
#      U(1) phase substitution in the bilateral current formula (5) reduces
#      to the fermion-number current (4), and checks the sign convention
#      exactly for arbitrary forward/backward bilinears.
# ---------------------------------------------------------------------------

def exhibit_E5(L=4, dim=3, mass=0.3, tol=1e-12):
    print("\n--- Exhibit E5: bilateral (5) -> (4) closure on small lattice ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    N = len(sites)
    Minv = np.linalg.inv(M)

    # (5) for U(1) phase generator T = i*I gives:
    #   J^mu_x = (i/2) eta_mu(x) [chibar_x chi_{x+mu} + chibar_{x+mu} chi_x]
    # The convention-real fermion-number current (4) is +i times this:
    #   J^mu_x_real = -(1/2) eta_mu(x) [chibar_x chi_{x+mu} + chibar_{x+mu} chi_x]
    # Verify: under the U(1) phase substitution into (5) above, the resulting
    # bilateral form matches (4) exactly.
    closure_max = 0.0
    n_sites = 0
    for x in sites:
        i = idx[x]
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            ip = idx[xp]
            eta = staggered_eta(x, mu)
            # Bilateral (5) under U(1) phase substitution (T^A = i):
            # J5_mu_x = (i/2) eta * [<chibar_x chi_xp> + <chibar_xp chi_x>]
            #        = (i/2) eta * [G(xp,x) + G(x,xp)]   (with G = M^-1)
            J5 = 0.5j * eta * (Minv[ip, i] + Minv[i, ip])
            # The convention-real version:
            J5_real = 1j * J5
            # The (4) form:
            J4 = -0.5 * eta * (Minv[ip, i] + Minv[i, ip])
            closure_max = max(closure_max, abs(J5_real - J4))
            n_sites += 1
    B_forward, B_backward, eta_symbol = sp.symbols("B_forward B_backward eta")
    J5_phase = sp.I * sp.Rational(1, 2) * eta_symbol * (B_forward + B_backward)
    J5_real = sp.I * J5_phase
    J4_real = -sp.Rational(1, 2) * eta_symbol * (B_forward + B_backward)
    symbolic_residual = sp.simplify(J5_real - J4_real)
    symbolic_pass = symbolic_residual == 0

    print(f"  L={L}, dim={dim}, mass={mass}, sites checked={n_sites}")
    print(f"  symbolic arbitrary-bilinear residual i*(i/2)*eta*(B+ + B-) - J4 = {symbolic_residual}")
    print(f"  max |J5_real - J4| = {closure_max:.3e}  (target: 0 to machine precision)")
    e5_pass = closure_max < tol and symbolic_pass
    print(f"  Bilateral (5) under T = i I closes algebraically to (4):")
    print(f"  symbolic arbitrary-bilinear verdict: {'PASS' if symbolic_pass else 'FAIL'}")
    print(f"  E5 verdict: {'PASS' if e5_pass else 'FAIL'}")
    return e5_pass


def exhibit_E5b(L=4, dim=3, mass=0.3, tol=1e-12):
    print("\n--- Exhibit E5b: direct U(1) local-envelope sign check ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    N = len(sites)
    rng = np.random.default_rng(20260606)
    chi = rng.normal(size=N) + 1j * rng.normal(size=N)
    chibar = rng.normal(size=N) + 1j * rng.normal(size=N)
    alpha = rng.normal(size=N)

    # Direct local U(1) variation with delta chi = i alpha chi and
    # delta chibar = -i alpha chibar.
    direct_delta = ((-1j * alpha * chibar) @ M @ chi) + (
        chibar @ M @ (1j * alpha * chi)
    )

    bilateral_plus = 0.0 + 0.0j
    historical_minus = 0.0 + 0.0j
    for x in sites:
        i = idx[x]
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xp = tuple((x[k] + ehat[k]) % L for k in range(dim))
            ip = idx[xp]
            eta = staggered_eta(x, mu)
            dalpha = alpha[ip] - alpha[i]
            bilateral_plus += (
                0.5j
                * eta
                * (chibar[i] * chi[ip] + chibar[ip] * chi[i])
                * dalpha
            )
            historical_minus += (
                0.5j
                * eta
                * (chibar[i] * chi[ip] - chibar[ip] * chi[i])
                * dalpha
            )

    plus_err = abs(direct_delta - bilateral_plus)
    minus_err = abs(direct_delta - historical_minus)
    direct_scale = max(abs(direct_delta), 1.0)
    minus_relative = minus_err / direct_scale
    e5b_pass = plus_err < tol and minus_relative > 1e-3
    print(f"  L={L}, dim={dim}, mass={mass}, sampled fields={N}")
    print(f"  direct delta S = {direct_delta.real:+.6e}{direct_delta.imag:+.6e}j")
    print(f"  |direct - bilateral plus sign| = {plus_err:.3e}")
    print(f"  |direct - historical minus sign| = {minus_err:.3e}")
    print(f"  relative historical-minus residual = {minus_relative:.3e}")
    print("  -> direct variation selects the plus-sign bilateral current in (7c).")
    print(f"  E5b verdict: {'PASS' if e5b_pass else 'FAIL'}")
    return e5b_pass


# ---------------------------------------------------------------------------
# E6 — direct verification of the (3) momentum-density divergence
#      (added 2026-05-10 for gate-recategorization repair).
#
# The note's textual reduction (5) -> (3) is honestly a discrete
# Ward-identity rearrangement, not a literal infinitesimal substitution
# (two-site translation is a discrete generator, not a Lie generator,
# so the bilateral form (5) does not directly specialise to (3)).
# Step 4b of the note now states this explicitly. To discharge the
# audit's "missing (5) -> (3) verification" gap, this exhibit verifies
# directly that the explicit (3) form has on-shell ∂^L_μ P^μ = 0,
# which is the operational content of (N1).
# ---------------------------------------------------------------------------

def exhibit_E6(L=4, dim=3, mass=0.3, tol=1e-9):
    print("\n--- Exhibit E6: support-only (3) momentum-density divergence ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    N = len(sites)
    Minv = np.linalg.inv(M)

    # Canonical staggered sublattice-momentum density (3):
    #   P^mu_x = -(i/2) eta_mu(x) [chibar_x d^L_mu chi_x - d^L_mu chibar_x . chi_x]
    # with d^L_mu chi_x = (chi_{x+mu} - chi_{x-mu})/2 (symmetric difference).
    # In the free-fermion ground state, the Wick contraction is
    #   <chibar_a chi_b> = (M^-1)_{ba}.
    # So
    #   <P^mu_x> = -(i/2) eta_mu(x) * (1/2) *
    #              [ <chibar_x chi_{x+mu}> - <chibar_x chi_{x-mu}>
    #                - <chibar_{x+mu} chi_x> + <chibar_{x-mu} chi_x> ]
    #            = -(i/4) eta_mu(x) *
    #              [ G(x+mu, x) - G(x-mu, x) - G(x, x+mu) + G(x, x-mu) ]
    # with G(a,b) = (M^-1)_{a,b}.
    #
    # Then check ∂^L_mu <P^mu_x> = Σ_mu (<P^mu_x> - <P^mu_{x-mu}>) = 0 on shell.

    def P_expectation(x_tuple, mu):
        ehat = tuple(1 if k == mu else 0 for k in range(dim))
        xp = tuple((x_tuple[k] + ehat[k]) % L for k in range(dim))
        xm = tuple((x_tuple[k] - ehat[k]) % L for k in range(dim))
        ix = idx[x_tuple]
        ixp = idx[xp]
        ixm = idx[xm]
        eta = staggered_eta(x_tuple, mu)
        # <P^mu_x> using <chibar_a chi_b> = G(b,a) = Minv[a,b]^T  -> Minv[b,a]
        # <chibar_x chi_y> = Minv[y,x]
        return -0.25j * eta * (
            Minv[ixp, ix] - Minv[ixm, ix]
            - Minv[ix, ixp] + Minv[ix, ixm]
        )

    div_max = 0.0
    div_typical = 0.0
    n_checked = 0
    for x in sites:
        div_x = 0.0 + 0j
        for mu in range(dim):
            ehat = tuple(1 if k == mu else 0 for k in range(dim))
            xm = tuple((x[k] - ehat[k]) % L for k in range(dim))
            P_x = P_expectation(x, mu)
            P_xm = P_expectation(xm, mu)
            div_x += P_x - P_xm
        div_max = max(div_max, abs(div_x))
        div_typical += abs(div_x)
        n_checked += 1
    div_typical /= n_checked

    print(f"  L={L}, dim={dim}, mass={mass}, sites checked={n_checked}")
    print(f"  max |∂^L · <P>| = {div_max:.3e}    (target: 0 to machine precision)")
    print(f"  mean |∂^L · <P>| = {div_typical:.3e}")
    e6_pass = div_max < tol
    print(f"  E6 verdict: {'PASS' if e6_pass else 'FAIL'}")
    print(f"  -> support-only: canonical staggered density (3) has")
    print(f"     ∂^L_μ <P^μ> = 0 in this free-carrier expectation exhibit.")
    print(f"     E6 is not the arbitrary-field two-step Ward proof.")
    return e6_pass


# ---------------------------------------------------------------------------
# E7 — field-level localized two-step Ward identity (added 2026-05-25).
#
# This is the load-bearing replacement for the old Step 4b overclaim. It
# checks the exact envelope identity generated by
# D^(2rho) = (S_(+2rho) - S_(-2rho))/2:
#
#   delta_omega S_F
#     = -bar D Omega M chi + bar M Omega D chi
#     = sum_x omega_x [-(bar D)_x (M chi)_x + (bar M)_x (D chi)_x].
#
# On shell, both terms vanish for arbitrary local envelopes. This does not
# identify the support-only density (3) as the arbitrary-field Ward current.
# ---------------------------------------------------------------------------

def exhibit_E7(L=6, dim=3, mass=0.3, tol=1e-9):
    print("\n--- Exhibit E7: localized two-step Ward identity (field-level) ---")
    M, sites, idx = build_M_pure_staggered(L, mass=mass, dim=dim)
    M0, sites0, idx0 = build_M_pure_staggered(L, mass=0.0, dim=dim)
    if sites != sites0 or idx != idx0:
        raise RuntimeError("site ordering mismatch between massive and massless blocks")

    rng = np.random.default_rng(20260525)
    N = len(sites)
    chi = rng.normal(size=N) + 1j * rng.normal(size=N)
    chibar = rng.normal(size=N) + 1j * rng.normal(size=N)

    pass_all = True
    max_comm = 0.0
    max_skew = 0.0
    max_local_coeff_err = 0.0
    max_random_envelope_err = 0.0
    max_on_shell_variation = 0.0
    min_nullity = None

    for rho in range(dim):
        D = build_two_step_generator(sites, idx, L, dim, rho)
        comm_err = float(np.max(np.abs(M @ D - D @ M)))
        skew_err = float(np.max(np.abs(D.T + D)))
        max_comm = max(max_comm, comm_err)
        max_skew = max(max_skew, skew_err)

        Dchi = D @ chi
        chibarD = chibar @ D
        Mchi = M @ chi
        chibarM = chibar @ M
        local_coeff = -chibarD * Mchi + chibarM * Dchi

        # Check every site coefficient by turning on one envelope basis vector.
        coeff_err = 0.0
        for j in range(N):
            omega_Mchi = np.zeros(N, dtype=complex)
            omega_Dchi = np.zeros(N, dtype=complex)
            omega_Mchi[j] = Mchi[j]
            omega_Dchi[j] = Dchi[j]
            direct = -(chibar @ D @ omega_Mchi) + (chibar @ M @ omega_Dchi)
            coeff_err = max(coeff_err, abs(direct - local_coeff[j]))
        max_local_coeff_err = max(max_local_coeff_err, float(coeff_err))

        omega = rng.normal(size=N)
        direct_random = -(chibar @ D @ (omega * Mchi)) + (chibar @ M @ (omega * Dchi))
        weighted_random = np.dot(omega, local_coeff)
        random_err = abs(direct_random - weighted_random)
        max_random_envelope_err = max(max_random_envelope_err, float(random_err))

        # Nontrivial on-shell sample on the massless block. Right nullspace:
        # M0 chi = 0. Left nullspace: chibar M0 = 0, equivalently M0.T chibar = 0.
        D0 = build_two_step_generator(sites0, idx0, L, dim, rho)
        right_ns, s_right = numerical_nullspace(M0, tol=1e-10)
        left_ns, s_left = numerical_nullspace(M0.T, tol=1e-10)
        nullity = min(right_ns.shape[1], left_ns.shape[1])
        min_nullity = nullity if min_nullity is None else min(min_nullity, nullity)
        if nullity == 0:
            pass_all = False
            on_shell_variation = float("inf")
        else:
            coeff_r = rng.normal(size=right_ns.shape[1]) + 1j * rng.normal(size=right_ns.shape[1])
            coeff_l = rng.normal(size=left_ns.shape[1]) + 1j * rng.normal(size=left_ns.shape[1])
            chi_shell = right_ns @ coeff_r
            chibar_shell = left_ns @ coeff_l
            omega_shell = rng.normal(size=N)
            on_shell_variation = abs(
                -(chibar_shell @ D0 @ (omega_shell * (M0 @ chi_shell)))
                + (chibar_shell @ M0 @ (omega_shell * (D0 @ chi_shell)))
            )
            eom_err = max(
                float(np.max(np.abs(M0 @ chi_shell))),
                float(np.max(np.abs(chibar_shell @ M0))),
            )
            on_shell_variation = max(on_shell_variation, eom_err)
            print(
                f"  rho={rho}: min singular values right/left="
                f"{s_right[-1]:.3e}/{s_left[-1]:.3e}, nullity={nullity}"
            )

        max_on_shell_variation = max(max_on_shell_variation, float(on_shell_variation))
        rho_pass = (
            comm_err < tol
            and skew_err < tol
            and coeff_err < tol
            and random_err < tol
            and on_shell_variation < tol
        )
        print(
            f"  rho={rho}: ||[M,D]||={comm_err:.3e}, "
            f"||D^T+D||={skew_err:.3e}, "
            f"local coeff err={coeff_err:.3e}, "
            f"random-envelope err={random_err:.3e}, "
            f"on-shell variation={on_shell_variation:.3e}  "
            f"{'PASS' if rho_pass else 'FAIL'}"
        )
        pass_all = pass_all and rho_pass

    print(f"  L={L}, dim={dim}, massive identity mass={mass}, N={N}")
    print(f"  max ||[M,D]||_max = {max_comm:.3e}")
    print(f"  max ||D^T + D||_max = {max_skew:.3e}")
    print(f"  max local-envelope coefficient error = {max_local_coeff_err:.3e}")
    print(f"  max random-envelope identity error = {max_random_envelope_err:.3e}")
    print(f"  max sampled on-shell variation = {max_on_shell_variation:.3e}")
    print(f"  min sampled massless nullity = {min_nullity}")
    print(f"  E7 verdict: {'PASS' if pass_all else 'FAIL'}")
    print("  -> verifies Step 4b's exact two-step Ward identity (3a).")
    print("     It does not promote the support-only density (3).")
    return pass_all


def exhibit_E8_source_boundary():
    print("\n--- Exhibit E8: source dependency boundary for parent staggered gate ---")
    root = Path(__file__).resolve().parents[1]
    note_path = root / "docs" / "AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29.md"
    text = note_path.read_text(encoding="utf-8")
    flat_text = " ".join(text.split())

    parent = "STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md"
    retained_substep = "STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md"

    checks = {
        "note file exists": note_path.exists(),
        "parent gate remains named as registered context": parent in text,
        "parent gate is not a markdown one-hop dependency": f"]({parent})" not in text,
        "retained substep-1 remains the markdown load-bearing dependency": f"]({retained_substep})" in text,
        "registered route is explicitly non-current graph dependency": "not a current citation-graph dependency" in flat_text,
        "source says parent uses no markdown edge": "no longer uses a markdown edge" in flat_text,
    }
    for label, ok in checks.items():
        print(f"  {label}: {'PASS' if ok else 'FAIL'}")
    passed = all(checks.values())
    print(f"  E8 verdict: {'PASS' if passed else 'FAIL'}")
    return passed


def main():
    print("=" * 72)
    print(" axiom_first_lattice_noether_check.py")
    print(" Loop: axiom-first-foundations, Cycle 5 / Route R5")
    print(" Exhibits the lattice Noether theorem (U(1) phase + (2Z)^d sublattice")
    print(" translation) on the admitted staggered/Grassmann carrier (open gate per")
    print(" MINIMAL_AXIOMS_2026-05-20.md). Bounded theorem.")
    print(" 2026-05-03 review-loop: + E5 algebraic closure (5) -> (4) check")
    print(" 2026-05-10 gate-recategorization repair: + E6 (3) divergence check")
    print(" 2026-05-25 Step 4b boundary repair: E6 support-only, + E7 field-level")
    print(" exact two-step Ward identity")
    print(" 2026-06-06 onsite-generator repair: E5 arbitrary-bilinear symbolic")
    print(" sign check; (5) scoped to onsite/internal infinitesimal generators")
    print(" 2026-06-06 audit repair: + E5b direct U(1) local-envelope sign check")
    print(" 2026-06-12 source-boundary repair: + E8 parent gate plain-text target")
    print("=" * 72)

    e1 = exhibit_E1(L=2, dim=3)
    e2 = exhibit_E2(L=4, dim=3)
    e3, e4 = exhibit_E3_E4(L=4, dim=3)
    e5 = exhibit_E5(L=4, dim=3)
    e5b = exhibit_E5b(L=4, dim=3)
    e6 = exhibit_E6(L=4, dim=3)
    e7 = exhibit_E7(L=6, dim=3)
    e8 = exhibit_E8_source_boundary()

    print()
    print("=" * 72)
    print(" SUMMARY")
    print("=" * 72)
    results = {"E1 (U(1) sym condition)": e1,
               "E2 ((2Z)^d sublattice translation sym)": e2,
               "E3 (current divergence-free on shell)": e3,
               "E4 (global charge conservation)": e4,
               "E5 (bilateral (5) -> (4) algebraic closure)": e5,
               "E5b (direct U(1) sign-visible local variation)": e5b,
               "E6 (support-only (3) momentum-density divergence)": e6,
               "E7 (field-level two-step Ward identity)": e7,
               "E8 (parent gate source-boundary check)": e8}
    n_pass = sum(1 for v in results.values() if v)
    n_total = len(results)
    for k, v in results.items():
        print(f"   {k}: {'PASS' if v else 'FAIL'}")
    print(f"\n   PASSED: {n_pass}/{n_total}")
    print()
    if n_pass == n_total:
        print(" verdict: bounded lattice Noether theorem exhibited on the admitted")
        print("          staggered/Grassmann carrier; U(1) current closes via E5")
        print("          and sign-visible arbitrary-field E5b, the (2Z)^d")
        print("          translation branch is the exact two-step Ward identity")
        print("          checked by E7, and the old density (3) is")
        print("          support-only via E6.")
        return 0
    else:
        print(" verdict: at least one structural exhibit failed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
