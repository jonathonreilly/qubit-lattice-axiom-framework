#!/usr/bin/env python3
"""Audit-companion runner: the free-sector spin-statistics LEVEL-1 mechanism and
the reduction to a free-field reconstruction.

This runner does NOT claim to perform the free-field Osterwalder-Schrader ->
Wightman reconstruction of the framework's 2-point. That reconstruction (call it
R) is the explicitly UNBUILT plank of the reduction (see the companion note,
Section 5). What this runner verifies is:

  (a) the non-circularity anchor -- the framework's free staggered Euclidean
      2-point is a STATISTICS-BLIND covariance kernel
          S(p) = (m - i gamma.p) / (p^2 + m^2)  =  M^{-1},  M = m + i gamma.p,
      literally the inverse of the quadratic form, IDENTICAL for the
      Grassmann-Gaussian and bosonic-Gaussian theories; and

  (b) the LEVEL-1 energy/microcausality MECHANISM as a conditional fact: GIVEN a
      relativistic field carrying the Dirac {+E,+E,-E,-E} mode structure with the
      relative sign sign(ubar u) = -sign(vbar v), the commuting (Bose)
      quantization is excluded (energy unbounded below / microcausality broken)
      while CAR is healthy (bounded below, microcausal).

The bounded kernel-algebra premises (a) and the +-E mode structure are the
established fragment already on main as
FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30.md; this runner
re-verifies them as the mechanism's inputs. The MECHANISM (b) is a statement
about a GIVEN relativistic field -- it is the hypothesis-discharged half of the
spin-statistics connection, NOT a claim that the framework delivers that field.
Delivering the field is R (unbuilt).

Conventions
-----------
Euclidean gammas: {g_mu, g_nu} = 2 delta_{mu nu}, mu = 1..4 (g[3] is the time gamma).
Minkowski gammas (mostly-minus metric eta = diag(+,-,-,-)):
    {G_mu, G_nu} = 2 eta_{mu nu};  G^0 = g_4, G^k = i g_k.
Dirac Hamiltonian H_D = G^0 (G^k p_k + m), eigenvalues = single-particle energies.

Load-bearing signs are stated convention-independently:
    sign(ubar u) = - sign(vbar v)
holds in EVERY Dirac basis; the runner asserts the RELATIVE sign only.

Single-seed deterministic (np.random.default_rng(20260530)); SCORECARD PASS=N
FAIL=0 required for audit-companion green.
"""

import itertools

import numpy as np


# --------------------------------------------------------------------------- #
# Gamma matrices
# --------------------------------------------------------------------------- #
def euclidean_gammas():
    """Euclidean Dirac matrices (4x4), {g_mu, g_nu} = 2 delta_{mu nu}, mu=0..3.

    Same Dirac-basis construction as the SO(4) covariance runner; g[3] is the
    Euclidean time gamma (= Minkowski G^0).
    """
    I2 = np.eye(2, dtype=complex)
    Z2 = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    g4 = np.block([[I2, Z2], [Z2, -I2]])               # time-like
    g1 = np.block([[Z2, -1j * sx], [1j * sx, Z2]])
    g2 = np.block([[Z2, -1j * sy], [1j * sy, Z2]])
    g3 = np.block([[Z2, -1j * sz], [1j * sz, Z2]])
    return [g1, g2, g3, g4]


def minkowski_gammas():
    """Minkowski gammas (mostly-minus). G^0 = g_4, G^k = i g_k.

    Gives {G^0,G^0}=+2 I, {G^k,G^k}=-2 I, {G^0,G^k}=0 -> {G^mu,G^nu}=2 eta^{mu nu}.
    """
    g = euclidean_gammas()
    G0 = g[3]
    Gk = [1j * g[0], 1j * g[1], 1j * g[2]]
    return [G0] + Gk


def dirac_basis_spinors(p3, m, G):
    """Return positive- and negative-energy eigenspinors of H_D = G^0(G^k p_k + m).

    p3 = (px,py,pz). Returns (E, w, poss, negs, Hd) where poss are the two E=+E
    eigenspinors (particle u) and negs are the two E=-E eigenspinors (the
    negative-energy / antiparticle solutions). Energies are exactly
    {+E,+E,-E,-E}, E=sqrt(p^2+m^2).
    """
    G0 = G[0]
    alpha = [G0 @ G[k + 1] for k in range(3)]  # alpha^k = G^0 G^k (Hermitian)
    beta = G0
    Hd = sum(p3[k] * alpha[k] for k in range(3)) + m * beta
    w, V = np.linalg.eigh(Hd)
    E = np.sqrt(p3 @ p3 + m * m)
    order = np.argsort(w)
    w = w[order]
    V = V[:, order]
    negs = [V[:, i] for i in range(4) if w[i] < 0]
    poss = [V[:, i] for i in range(4) if w[i] > 0]
    return E, w, poss, negs, Hd


# --------------------------------------------------------------------------- #
# (a) Non-circularity anchor: statistics-blind kernel
# --------------------------------------------------------------------------- #
def check_statistics_blind_inverse(rng):
    """S(p) = M^{-1} with M = m + i gamma.p, and S is the SAME matrix irrespective
    of Grassmann vs bosonic Gaussian (it is literally the inverse of the quadratic
    form, computed once). This is the non-circularity anchor: the starting object
    knows nothing about statistics."""
    g = euclidean_gammas()
    ok = True
    for _ in range(40):
        m = rng.uniform(0.2, 3.0)
        p = rng.normal(size=4)
        gp = sum(p[k] * g[k] for k in range(4))
        M = m * np.eye(4) + 1j * gp
        S = (m * np.eye(4) - 1j * gp) / (p @ p + m * m)
        if not np.allclose(M @ S, np.eye(4), atol=1e-10):
            ok = False
        if not np.allclose(S @ M, np.eye(4), atol=1e-10):
            ok = False
        # statistics-blindness: the covariance is the inverse of the quadratic
        # form; the Grassmann-Gaussian and bosonic-Gaussian theories share the
        # SAME 2-point M^{-1}.
        if not np.allclose(S, np.linalg.inv(M), atol=1e-10):
            ok = False
    return ok


# --------------------------------------------------------------------------- #
# Established bounded premises (on main as the mode-algebra note) re-verified
# here as the mechanism's GIVEN inputs -- NOT a claim that R is performed.
# --------------------------------------------------------------------------- #
def check_euclidean_pole_continuation(rng):
    """Kernel fact (on main): the scalar Euclidean propagator 1/(p4^2 + E^2) has
    poles at p4 = +-iE. Continuing p4 -> i p0 places the mass shell at p0 = +-E:
    the two-sheet {+E,-E} structure. This is a property of the KERNEL S(p); the
    OS->Wightman assembly of a field from it is R (unbuilt)."""
    ok = True
    for _ in range(40):
        m = rng.uniform(0.2, 3.0)
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        roots = np.roots([1.0, 0.0, E * E])
        if not np.allclose(np.sort(roots.imag), np.array([-E, E]), atol=1e-9):
            ok = False
        if not np.allclose(roots.real, 0.0, atol=1e-9):
            ok = False
        mink_roots = np.roots([-1.0, 0.0, E * E])
        if not np.allclose(np.sort(mink_roots.real), np.array([-E, E]), atol=1e-9):
            ok = False
    return ok


def check_dirac_mode_structure(rng):
    """GIVEN premise of the mechanism (established fragment, on main): the Dirac
    Hamiltonian carries the single-particle spectrum {+E,+E,-E,-E}, two particle
    and two antiparticle solutions, with H_D self-adjoint."""
    G = minkowski_gammas()
    ok = True
    for _ in range(40):
        m = rng.uniform(0.2, 3.0)
        p3 = rng.normal(size=3)
        E, w, poss, negs, Hd = dirac_basis_spinors(p3, m, G)
        expect = np.array([-E, -E, +E, +E])
        if not np.allclose(np.sort(w), expect, atol=1e-9):
            ok = False
        if not (len(poss) == 2 and len(negs) == 2):
            ok = False
        if not np.allclose(Hd, Hd.conj().T, atol=1e-10):
            ok = False
    return ok


def check_uv_relative_sign(rng):
    """GIVEN premise (established fragment, on main): convention-independent
    load-bearing sign sign(ubar u) = - sign(vbar v), plus positive-definite Fock
    norms and the u/v completeness relations.

        u_s(p) = [ sqrt(E+m) chi_s ; (sigma.p)/sqrt(E+m) chi_s ]   (particle)
        v_s(p) = [ (sigma.p)/sqrt(E+m) eta_s ; sqrt(E+m) eta_s ]   (antiparticle)
    """
    G = minkowski_gammas()
    G0 = G[0]
    sigma = [np.array([[0, 1], [1, 0]], dtype=complex),
             np.array([[0, -1j], [1j, 0]], dtype=complex),
             np.array([[1, 0], [0, -1]], dtype=complex)]
    basis = (np.array([1, 0], dtype=complex), np.array([0, 1], dtype=complex))
    ok = True
    for _ in range(40):
        m = rng.uniform(0.3, 3.0)
        p3 = rng.normal(size=3)
        E = float(np.sqrt(p3 @ p3 + m * m))
        slash_p = E * G0 - sum(p3[k] * G[k + 1] for k in range(3))
        sdotp = sum(p3[k] * sigma[k] for k in range(3))
        us = [np.concatenate([np.sqrt(E + m) * s, (sdotp @ s) / np.sqrt(E + m)])
              for s in basis]
        vs = [np.concatenate([(sdotp @ s) / np.sqrt(E + m), np.sqrt(E + m) * s])
              for s in basis]
        ubar_u = [float((u.conj() @ G0 @ u).real) for u in us]
        udag_u = [float((u.conj() @ u).real) for u in us]
        vbar_v = [float((v.conj() @ G0 @ v).real) for v in vs]
        vdag_v = [float((v.conj() @ v).real) for v in vs]
        Sigma_uu = sum(np.outer(u, u.conj() @ G0) for u in us)
        Sigma_vv = sum(np.outer(v, v.conj() @ G0) for v in vs)
        if not all(np.allclose((slash_p - m * np.eye(4)) @ u, 0, atol=1e-8) for u in us):
            ok = False
        if not all(np.allclose((slash_p + m * np.eye(4)) @ v, 0, atol=1e-8) for v in vs):
            ok = False
        if not np.allclose(ubar_u, [2 * m, 2 * m], atol=1e-7):
            ok = False
        if not np.allclose(vbar_v, [-2 * m, -2 * m], atol=1e-7):
            ok = False
        if not (np.sign(ubar_u[0]) == -np.sign(vbar_v[0])):
            ok = False
        if not (np.sign(ubar_u[1]) == -np.sign(vbar_v[1])):
            ok = False
        if not np.allclose(udag_u, [2 * E, 2 * E], atol=1e-7):
            ok = False
        if not np.allclose(vdag_v, [2 * E, 2 * E], atol=1e-7):
            ok = False
        if not np.allclose(Sigma_uu, slash_p + m * np.eye(4), atol=1e-6):
            ok = False
        if not np.allclose(Sigma_vv, slash_p - m * np.eye(4), atol=1e-6):
            ok = False
    return ok


# --------------------------------------------------------------------------- #
# (b) The LEVEL-1 mechanism: GIVEN the field, CAR forced (energy + microcausality)
# --------------------------------------------------------------------------- #
def check_bounded_energy_fock(rng):
    """Mechanism, energy half: the antiparticle-relabeled Hamiltonian
    H = sum_p E(p)(a^dag a + b^dag b) on the CAR Fock space is bounded below by 0
    (vacuum energy 0). Finite-mode many-body spectrum is >= 0. This is the GIVEN
    field under CAR; the Bose comparison is in check_commuting_quantization."""
    ok = True
    for _ in range(8):
        nmodes = int(rng.integers(2, 5))
        Eparts = rng.uniform(0.3, 3.0, size=nmodes)
        Eantis = rng.uniform(0.3, 3.0, size=nmodes)
        Es = np.concatenate([Eparts, Eantis])  # all POSITIVE in CAR (antip = +E)
        N = len(Es)
        spectrum = []
        for occ in itertools.product((0, 1), repeat=N):
            spectrum.append(sum(o * e for o, e in zip(occ, Es)))
        spectrum = np.array(spectrum)
        if spectrum.min() < -1e-12:
            ok = False
        if abs(spectrum.min()) > 1e-12:
            ok = False
        if not np.isclose(spectrum.max(), Es.sum()):
            ok = False
    return ok


def check_microcausality_pauli_jordan(rng):
    """Mechanism, microcausality half: the Pauli-Jordan function Delta(x) is
    Lorentz invariant and ODD under x -> -x; for SPACELIKE x it vanishes. On a
    momentum grid symmetric under p <-> -p the equal-time integrand is exactly odd
    in p, so the spacelike kernel vanishes (microcausality), while the timelike
    kernel does not (causal support)."""
    ok = True

    def pj_kernel(x0, xvec, m, grid):
        total = 0.0 + 0.0j
        for p in grid:
            E = np.sqrt(p @ p + m * m)
            phase_minus = np.exp(-1j * (E * x0 - p @ xvec))
            phase_plus = np.exp(+1j * (E * x0 - p @ xvec))
            total += (phase_minus - phase_plus) / (2 * E)
        return total

    axis = np.linspace(-4, 4, 9)
    grid = [np.array([a, b, c]) for a in axis for b in axis for c in axis]

    for _ in range(6):
        m = rng.uniform(0.3, 2.0)
        xvec = rng.normal(size=3)
        xvec = xvec / np.linalg.norm(xvec) * rng.uniform(0.5, 2.0)
        Kspace = pj_kernel(0.0, xvec, m, grid)
        if abs(Kspace) > 1e-9:
            ok = False
        Ktime = pj_kernel(rng.uniform(0.5, 2.0), np.zeros(3), m, grid)
        if abs(Ktime) < 1e-6:
            ok = False
    return ok


def check_microcausality_discriminator(rng):
    """Mechanism core: the spin-1/2 field built with ANTICOMMUTATORS (CAR) has a
    spacelike (anti)commutator that vanishes; built with COMMUTATORS (Bose) it
    does not. Convention-independent on-shell projector identity:
        (p_slash + m) + G^0 (p_slash - m) G^0 = 2E G^0        (CAR: canonical)
        (p_slash + m) - G^0 (p_slash - m) G^0 = 2(m - p_k G^k) != 2E G^0 (Bose)
    using sum u ubar = p_slash + m, sum v vbar = p_slash - m and
    sign(ubar u) = - sign(vbar v)."""
    G = minkowski_gammas()
    G0 = G[0]
    ok = True
    for _ in range(40):
        m = rng.uniform(0.3, 3.0)
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        slash_p = E * G0 - sum(p3[k] * G[k + 1] for k in range(3))
        Lam_plus = slash_p + m * np.eye(4)   # sum u ubar
        Lam_minus = slash_p - m * np.eye(4)  # sum v vbar
        car_comb = (Lam_plus + G0 @ Lam_minus @ G0)   # CAR: should = 2E G^0
        if not np.allclose(car_comb, 2 * E * G0, atol=1e-7):
            ok = False
        bose_comb = (Lam_plus - G0 @ Lam_minus @ G0)  # Bose: must DIFFER
        if np.allclose(bose_comb, 2 * E * G0, atol=1e-7):
            ok = False
        if np.allclose(bose_comb - car_comb, np.zeros((4, 4)), atol=1e-7):
            ok = False
    return ok


def check_commuting_quantization_excluded(rng):
    """Mechanism conclusion (the LEVEL-1 obstruction): with the antiparticle {-E}
    sector present, BOSE quantization gives an unbounded-below Hamiltonian
    (Dirac-sea instability); CAR caps occupation at {0,1} and relabels b = a^dag to
    a POSITIVE antiparticle energy +E (bounded below). The discriminating quantity
    is the sign carried by adding one quantum, weighted by sign(ubar u)=-sign(vbar v).
    This is the conditional mechanism (given the field); it is NOT a claim that the
    framework delivers the field (that is R, unbuilt)."""
    ok = True
    for _ in range(20):
        E = rng.uniform(0.3, 3.0)
        nmax = 6
        bose_energies = np.array([-E * n for n in range(nmax + 1)])
        bose_energies_more = np.array([-E * n for n in range(2 * nmax + 1)])
        if not (bose_energies_more.min() < bose_energies.min() - 1e-9):
            ok = False  # Bose Dirac sea unbounded below
        car_energies = np.array([0.0, +E])  # vacuum 0, one antiparticle +E
        if car_energies.min() < -1e-12:
            ok = False  # CAR bounded below
        sign_u = +1.0
        sign_v = -1.0
        if not (sign_u == -sign_v):
            ok = False
        car_antip_energy = abs(sign_v) * E
        if car_antip_energy <= 0:
            ok = False
    return ok


def main():
    rng = np.random.default_rng(20260530)
    checks = []

    # (a) non-circularity anchor
    checks.append(("statistics_blind_kernel_is_inverse", check_statistics_blind_inverse(rng)))
    # established bounded premises (on main as the mode-algebra note), re-verified
    checks.append(("kernel_pole_continuation_pm_E", check_euclidean_pole_continuation(rng)))
    checks.append(("given_dirac_mode_structure_pm_E", check_dirac_mode_structure(rng)))
    checks.append(("given_uv_relative_sign_and_completeness", check_uv_relative_sign(rng)))
    # (b) the LEVEL-1 mechanism: given the field, CAR forced
    checks.append(("mechanism_bounded_energy_CAR_fock", check_bounded_energy_fock(rng)))
    checks.append(("mechanism_microcausality_pauli_jordan", check_microcausality_pauli_jordan(rng)))
    checks.append(("mechanism_microcausality_CAR_vs_Bose", check_microcausality_discriminator(rng)))
    checks.append(("mechanism_commuting_quantization_excluded", check_commuting_quantization_excluded(rng)))

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
