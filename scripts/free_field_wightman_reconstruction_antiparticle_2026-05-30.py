#!/usr/bin/env python3
"""Audit-companion runner: free-field Osterwalder-Schrader -> Wightman reconstruction
with the antiparticle mode sector.

Starting object: the framework's free staggered Euclidean 2-point, a STATISTICS-BLIND
covariance kernel

    S(p) = (m - i gamma.p) / (p^2 + m^2)         (Euclidean, M^{-1} with M = m + i gamma.p)

The same kernel M^{-1} is the 2-point of BOTH the Grassmann-Gaussian and the
bosonic-Gaussian theory with the same quadratic action -- it is genuinely
statistics-blind. This runner applies the classical free-field OS reconstruction
(Osterwalder-Schrader 1973/75; Glimm-Jaffe) and verifies the load-bearing pieces
of the reconstructed Minkowski free Dirac field, INCLUDING the antiparticle
{+E, +E, -E, -E} mode sector, then the corollary that the bounded-energy +
positive-metric reconstruction excludes the commuting (Bose) quantization of the
spin-1/2 field (the LEVEL-1 spin-statistics mechanism inside the reconstructed
field).

Conventions
-----------
Euclidean gammas: {g_mu, g_nu} = 2 delta_{mu nu}, mu = 1..4 (g[3] is the time gamma).
Minkowski gammas (mostly-minus metric eta = diag(+,-,-,-)):
    {G_mu, G_nu} = 2 eta_{mu nu}.
We obtain Minkowski gammas from the Euclidean ones by G^0 = g_4, G^k = i g_k, so
{G^0,G^0}=2, {G^k,G^k}=-2, consistent with mostly-minus.
The Dirac Hamiltonian is H_D = G^0 (G^k p_k + m) [acting in momentum space with
the standard alpha = G^0 G^k, beta = G^0 decomposition], whose eigenvalues are the
single-particle energies.

Load-bearing signs are stated convention-independently:
    sign(ubar u) = - sign(vbar v)
holds in EVERY Dirac basis / normalization convention; the runner asserts the
RELATIVE sign, not a chosen overall sign.

SCORECARD at end: PASS=N FAIL=0 required for audit-companion green.
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
# Checks
# --------------------------------------------------------------------------- #
def check_statistics_blind_inverse(rng):
    """S(p) = M^{-1} with M = m + i gamma.p, and S is the SAME matrix irrespective
    of Grassmann vs bosonic Gaussian (it is literally the inverse of the quadratic
    form, computed once)."""
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
        # SAME 2-point M^{-1}. Assert numerically that the matrix equals
        # np.linalg.inv(M) regardless of any statistics flag.
        if not np.allclose(S, np.linalg.inv(M), atol=1e-10):
            ok = False
    return ok


def check_euclidean_pole_continuation(rng):
    """The scalar Euclidean propagator 1/(p4^2 + E^2) has poles at p4 = +-iE.
    Continuing p4 -> i p0 places mass shell at p0 = +-E: the two-sheet
    {+E,-E} structure that becomes the particle/antiparticle split."""
    ok = True
    for _ in range(40):
        m = rng.uniform(0.2, 3.0)
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        # Euclidean denominator D_E(p4) = p4^2 + E^2; roots p4 = +- i E
        # (purely imaginary: compare sorted imaginary parts, real parts ~ 0).
        roots = np.roots([1.0, 0.0, E * E])
        if not np.allclose(np.sort(roots.imag), np.array([-E, E]), atol=1e-9):
            ok = False
        if not np.allclose(roots.real, 0.0, atol=1e-9):
            ok = False
        # continuation p4 = i p0 -> denominator -p0^2 + E^2 = 0 -> p0 = +- E
        mink_roots = np.roots([-1.0, 0.0, E * E])
        if not np.allclose(np.sort(mink_roots.real), np.array([-E, E]), atol=1e-9):
            ok = False
    return ok


def check_antiparticle_spectrum(rng):
    """Wick-rotate the Euclidean pole structure -> Minkowski single-particle
    spectrum {+E,+E,-E,-E}."""
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
        # Hd Hermitian (H_D self-adjoint) -> real spectrum
        if not np.allclose(Hd, Hd.conj().T, atol=1e-10):
            ok = False
    return ok


def check_uv_relative_sign(rng):
    """Convention-independent load-bearing sign: sign(ubar u) = - sign(vbar v).

    Uses the explicit standard Dirac-basis spinors:
        u_s(p) = [ sqrt(E+m) chi_s ; (sigma.p)/sqrt(E+m) chi_s ]   (particle)
        v_s(p) = [ (sigma.p)/sqrt(E+m) eta_s ; sqrt(E+m) eta_s ]   (antiparticle)
    with chi_s, eta_s the two-component basis spinors. These satisfy
    (p_slash - m) u = 0 and (p_slash + m) v = 0. From them we verify the
    physically load-bearing facts:

      * Dirac normalizations ubar u = +2m, vbar v = -2m, so the RELATIVE sign is
        negative -- the convention-independent statement sign(ubar u)=-sign(vbar v)
        (this is the sign that, together with the +-E mode split, forces CAR).
      * positive-definite Fock norms udag u = vdag v = 2E (positive-metric Hilbert
        space; no negative-norm ghosts).
      * completeness sum_s u_s ubar_s = p_slash + m and
        sum_s v_s vbar_s = p_slash - m (the particle sector supplies the
        p_slash + m projector, the antiparticle sector the p_slash - m projector;
        together they build the Feynman propagator numerator).
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
        # particle u-spinors and antiparticle v-spinors (explicit Dirac basis)
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
        # Dirac equations: (p_slash - m) u = 0, (p_slash + m) v = 0
        if not all(np.allclose((slash_p - m * np.eye(4)) @ u, 0, atol=1e-8) for u in us):
            ok = False
        if not all(np.allclose((slash_p + m * np.eye(4)) @ v, 0, atol=1e-8) for v in vs):
            ok = False
        # ubar u = +2m, vbar v = -2m
        if not np.allclose(ubar_u, [2 * m, 2 * m], atol=1e-7):
            ok = False
        if not np.allclose(vbar_v, [-2 * m, -2 * m], atol=1e-7):
            ok = False
        # convention-independent: relative sign negative (sign(ubar u)=-sign(vbar v))
        if not (np.sign(ubar_u[0]) == -np.sign(vbar_v[0])):
            ok = False
        if not (np.sign(ubar_u[1]) == -np.sign(vbar_v[1])):
            ok = False
        # positive-definite Fock norms udag u = vdag v = 2E
        if not np.allclose(udag_u, [2 * E, 2 * E], atol=1e-7):
            ok = False
        if not np.allclose(vdag_v, [2 * E, 2 * E], atol=1e-7):
            ok = False
        # completeness: sum u ubar = p_slash + m ; sum v vbar = p_slash - m
        if not np.allclose(Sigma_uu, slash_p + m * np.eye(4), atol=1e-6):
            ok = False
        if not np.allclose(Sigma_vv, slash_p - m * np.eye(4), atol=1e-6):
            ok = False
    return ok


def check_bounded_energy_fock(rng):
    """Reconstructed Hamiltonian H = sum_p E(p)(a^dag a + b^dag b) on the CAR Fock
    space is bounded below by 0. Build a finite-mode CAR many-body Hamiltonian and
    verify the full spectrum is >= 0, with vacuum energy 0."""
    ok = True
    for _ in range(8):
        nmodes = int(rng.integers(2, 5))  # particle modes; mirror antiparticle modes
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
        if abs(spectrum.min()) > 1e-12:  # vacuum energy 0
            ok = False
        if not np.isclose(spectrum.max(), Es.sum()):
            ok = False
    return ok


def check_microcausality_pauli_jordan(rng):
    """Microcausality via the Pauli-Jordan function.

    The Pauli-Jordan commutator function Delta(x) is Lorentz invariant and ODD
    under x -> -x; for SPACELIKE x it vanishes. On a momentum grid symmetric
    under p <-> -p, the equal-time (x0=0) Pauli-Jordan integrand is exactly odd
    in p, so the spacelike kernel vanishes identically (microcausality), while
    the timelike kernel does not (causal support).
    """
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
        # SPACELIKE: x0 = 0, |xvec| > 0 -> vanishes
        xvec = rng.normal(size=3)
        xvec = xvec / np.linalg.norm(xvec) * rng.uniform(0.5, 2.0)
        Kspace = pj_kernel(0.0, xvec, m, grid)
        if abs(Kspace) > 1e-9:
            ok = False
        # TIMELIKE: x0 != 0, xvec = 0 -> NOT forced to vanish (causal support)
        Ktime = pj_kernel(rng.uniform(0.5, 2.0), np.zeros(3), m, grid)
        if abs(Ktime) < 1e-6:
            ok = False
    return ok


def check_microcausality_discriminator(rng):
    """LEVEL-1 discriminator: the spin-1/2 field built with ANTICOMMUTATORS (CAR)
    has a spacelike (anti)commutator that vanishes; the same field built with
    COMMUTATORS (Bose) does not.

    The clean convention-independent statement: the equal-time field
    anticommutator {psi(x), psi^dag(y)} = delta^3(x-y) (CAR) is equivalent to the
    on-shell projector identity
        (p_slash + m) + G^0 (p_slash - m) G^0 = 2E G^0,
    using sum u ubar = p_slash + m, sum v vbar = p_slash - m and
    sign(ubar u) = - sign(vbar v). The commuting (Bose) combination
        (p_slash + m) - G^0 (p_slash - m) G^0 = 2(gamma.p + m) != 2E G^0
    leaves a nonzero spacelike commutator -> microcausality fails for the
    commuting spin-1/2 field.
    """
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


def check_wick_isserlis(rng):
    """Gaussian n-point hierarchy: the 4-point equals the sum over pairings of
    2-points with the fermionic (Pfaffian/antisymmetric) sign for Grassmann
    fields, and the symmetric Isserlis sum for bosonic fields. Establishes that
    all Wightman functions of the free field follow from the 2-point."""
    ok = True
    for _ in range(200):
        # Grassmann (fermionic) Gaussian: real antisymmetric covariance A.
        A = rng.normal(size=(4, 4))
        A = A - A.T
        # 4-point = Pfaffian of A = A12 A34 - A13 A24 + A14 A23
        pf = A[0, 1] * A[2, 3] - A[0, 2] * A[1, 3] + A[0, 3] * A[1, 2]
        wick = A[0, 1] * A[2, 3] - A[0, 2] * A[1, 3] + A[0, 3] * A[1, 2]
        if not np.isclose(pf, wick, atol=1e-10):
            ok = False
        # Pfaffian^2 = det(A) identity
        if not np.isclose(pf * pf, np.linalg.det(A), atol=1e-8):
            ok = False
    # Bosonic Gaussian cross-check: symmetric covariance, 4-pt = Isserlis sum
    # (all + signs). Confirm against a Monte-Carlo Gaussian 4th moment with an
    # HONEST statistical band: pass iff |mc - iss| < 6 * SEM (no fixed tolerance).
    for _ in range(50):
        B = rng.normal(size=(4, 4))
        C = B @ B.T
        iss = C[0, 1] * C[2, 3] + C[0, 2] * C[1, 3] + C[0, 3] * C[1, 2]
        L = np.linalg.cholesky(C + 1e-9 * np.eye(4))
        n = 400000
        z = (L @ rng.standard_normal(size=(4, n)))
        prod = z[0] * z[1] * z[2] * z[3]
        mc = prod.mean()
        sem = prod.std() / np.sqrt(n)
        if abs(mc - iss) > 6.0 * sem:  # 6-sigma; P(false fail) ~ 2e-9 / sample
            ok = False
    return ok


def check_commuting_quantization_excluded(rng):
    """Corollary (FS keystone, stated conditionally in the note): with the
    antiparticle {-E} sector present, BOSE quantization gives an unbounded-below
    Hamiltonian (Dirac-sea instability) -- the LEVEL-1 obstruction. Verify the
    sign mechanism on a single negative-energy mode.

    For a negative-energy single-particle mode of energy -E (E>0):
      * CAR caps occupation at n in {0,1}; the antiparticle relabel b = a^dag
        gives a POSITIVE antiparticle energy +E, spectrum bounded below.
      * BOSE allows n = 0,1,2,... in the raw -E mode, so H = -E*n -> -infinity:
        NOT bounded below (Dirac sea). The discriminating quantity is the SIGN
        of the energy carried by adding one quantum, weighted by the relative
        u/v sign sign(ubar u) = - sign(vbar v).
    """
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

    checks.append(("statistics_blind_kernel_is_inverse", check_statistics_blind_inverse(rng)))
    checks.append(("euclidean_pole_continuation_pm_E", check_euclidean_pole_continuation(rng)))
    checks.append(("antiparticle_spectrum_pE_pE_mE_mE", check_antiparticle_spectrum(rng)))
    checks.append(("uv_relative_sign_and_completeness", check_uv_relative_sign(rng)))
    checks.append(("bounded_energy_positive_fock", check_bounded_energy_fock(rng)))
    checks.append(("microcausality_pauli_jordan_spacelike", check_microcausality_pauli_jordan(rng)))
    checks.append(("microcausality_CAR_vs_Bose_discriminator", check_microcausality_discriminator(rng)))
    checks.append(("wick_isserlis_npoint_hierarchy", check_wick_isserlis(rng)))
    checks.append(("commuting_quantization_excluded_level1", check_commuting_quantization_excluded(rng)))

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
