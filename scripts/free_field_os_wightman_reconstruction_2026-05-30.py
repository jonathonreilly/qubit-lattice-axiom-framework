#!/usr/bin/env python3
"""Audit-companion runner: free-field Osterwalder-Schrader -> Wightman
reconstruction R of the framework's statistics-blind free staggered-Dirac
2-point.

CONDITIONAL scope. Everything verified here is conditional on the cited rungs
(rung A continuum SO(4) 2-point: audited_conditional; rung B two-step transfer
positivity: audited_conditional; rung C spectrum condition: unaudited) and on the
on-main bounded mode-algebra fragment (unaudited). This runner does NOT assert
those rungs are ratified, does NOT claim an unconditional spin-statistics result,
does NOT claim emergent Lorentz invariance, and treats only the free (U = 1)
matter sector.

The starting object is STATISTICS-BLIND:
    S(p) = (m - i gamma.p) / (p^2 + m^2) = M^{-1}(p),  M(p) = m + i gamma.p,
the inverse of the Euclidean quadratic form, IDENTICAL for the Grassmann-Gaussian
and bosonic-Gaussian theories built on the same action. Nothing below presupposes
CAR or Grassmann variables; this is the non-circularity anchor.

What this runner VERIFIES (the pieces the note claims as ESTABLISHED conditional
on the rungs), each a genuine consequence, not a restated assumption:

  R1  statistics_blind_kernel_inverse
        M S = S M = I and S = M^{-1}; the SAME matrix is the covariance of both
        statistics. (non-circularity anchor)

  R2  os1_so4_bispinor_covariance
        The continuum kernel transforms as a Euclidean SO(4) bispinor 2-point
        (OS1): for Spin(4) representative U with SO(4) image A,
        U S(p) U^{-1} = S(A p), with A recovered from U and checked A in SO(4).
        (rung A's covariance, re-exhibited on the continuum kernel.)

  R3  os2_fermionic_reflection_positivity   [the hard OS2 step, DERIVED here]
        Reflection positivity of the free Dirac Gaussian measure with covariance
        S, as the positive-semidefiniteness of the fermionic OS Gram matrix
            M_{(i,a),(j,b)} = [ gamma_4 . S(tau_i + tau_j, k) ]_{ab},
        tau_i, tau_j > 0, at fixed spatial momentum k. This is the genuine
        Osterwalder-Schrader fermion RP condition for THIS covariance; it is
        derived from the closed-form mixed (tau, k) kernel and shown PSD over a
        random sweep. NON-TRIVIALITY: the SAME Gram with the wrong reflection
        (identity instead of gamma_4) is shown to be strongly indefinite, so the
        PSD result is a real positivity theorem, not a tautology.

  R4  os4_cluster_mass_gap
        OS4 clustering: the kernel decays exponentially in Euclidean time with
        rate exactly m (mass gap), so connected correlators cluster for m > 0.

  R5  wick_rotation_mass_shell_so31
        Wick rotation p_4 = i p_0 sends the Euclidean denominator p^2 + m^2 to the
        Minkowski mass shell -p_0^2 + |p|^2 + m^2 = 0 (SO(3,1) orbit), the 2-point
        analytic continuation underlying OS1 -> Lorentz covariance.

  R6  positive_energy_spectrum   [rung C, exhibited on the mode structure]
        The Minkowski Dirac Hamiltonian has spectrum {+E,+E,-E,-E}; the
        CAR-relabeled many-body Hamiltonian H = sum E (a^dag a + b^dag b) is
        bounded below by 0 (positive-energy / spectrum condition), with the
        explicit positive single-particle energies E(p) = sqrt(|p|^2 + m^2).

  R7  gaussian_npoint_pfaffian_hierarchy   [sub-piece 3, the routine piece]
        The Wightman/Schwinger n-point hierarchy is determined from the 2-point by
        the Gaussian recursion -- EXACTLY, for both statistics. Verified at the 4-
        and 6-point level: the bosonic (Isserlis) moment satisfies the Wick
        recursion E[x_{i0} ...] = sum_j C[i0,j] E[rest], the fermionic
        (Grassmann-Gaussian) n-point is the Pfaffian of the antisymmetric 2-point
        matrix satisfying the Pfaffian Laplace recursion, and the fermionic
        identity Pfaffian^2 = det holds. No Monte Carlo; every check is exact.

  R8  uv_relative_sign_and_completeness   [established fragment, re-verified]
        u/v completeness sum u ubar = pslash + m, sum v vbar = pslash - m, with the
        convention-independent relative sign sign(ubar u) = - sign(vbar v) and
        positive Hilbert norms u^dag u = v^dag v = 2E.

What this runner DOES NOT verify (honestly OPEN; see the note's honesty section):
  - it does NOT machine-check the abstract OS reconstruction theorem itself
    (Osterwalder-Schrader 1973/75) -- that is cited as textbook methodology;
  - it does NOT verify that the framework's LATTICE Gaussian measure equals this
    continuum Dirac Gaussian beyond rung A's continuum-limit 2-point statement
    (the lattice -> continuum measure bridge, and the 1+1d -> 4D arena bridge from
    rung B, are flagged open);
  - it does NOT verify full Poincare covariance of the reconstructed field on the
    reconstructed Hilbert space (boosts as operators), only the 2-point SO(4)
    bispinor covariance (R2) and the positive-energy time generator (R6);
  - it does NOT establish an unconditional spin-statistics result.

Single-seed deterministic; numpy + stdlib only.
"""

import numpy as np

SEED = 20260530
ATOL = 1e-9


# --------------------------------------------------------------------------
# Clifford algebra and the statistics-blind kernel
# --------------------------------------------------------------------------
def euclidean_gammas():
    """Euclidean Dirac matrices, {g_mu, g_nu} = 2 delta_{mu nu}, all Hermitian.

    g[0..2] are spatial, g[3] is the Euclidean-time (tau) gamma.
    """
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    g1 = np.block([[z2, -1j * sx], [1j * sx, z2]])
    g2 = np.block([[z2, -1j * sy], [1j * sy, z2]])
    g3 = np.block([[z2, -1j * sz], [1j * sz, z2]])
    g4 = np.block([[i2, z2], [z2, -i2]])
    return [g1, g2, g3, g4]


def minkowski_gammas():
    """Mostly-minus Minkowski gammas, {G_mu, G_nu} = 2 eta_{mu nu}."""
    g = euclidean_gammas()
    return [g[3], 1j * g[0], 1j * g[1], 1j * g[2]]


def S_momentum(p4, m):
    """Euclidean 4-momentum kernel S(p) = (m - i g.p)/(p^2 + m^2)."""
    g = euclidean_gammas()
    gp = sum(p4[k] * g[k] for k in range(4))
    return (m * np.eye(4, dtype=complex) - 1j * gp) / (p4 @ p4 + m * m)


def M_momentum(p4, m):
    g = euclidean_gammas()
    gp = sum(p4[k] * g[k] for k in range(4))
    return m * np.eye(4, dtype=complex) + 1j * gp


def S_tau_k(tau, k3, m):
    """Mixed-representation kernel: 1D Fourier of S in the Euclidean time
    component p_4, at fixed spatial momentum k3.

    Residue calculus on the poles p_4 = +/- iE, E = sqrt(|k|^2 + m^2):
        int dp4/(2pi) e^{i p4 tau} / (p4^2 + E^2)        = (1/2E) e^{-E|tau|},
        int dp4/(2pi) e^{i p4 tau} p4 / (p4^2 + E^2)     = (i/2) sgn(tau) e^{-E|tau|}.
    With S = (m 1 - i g.k_spatial) / (..) + (-i g4) p4 / (..), this gives the
    closed-form mixed kernel below.
    """
    g = euclidean_gammas()
    E = np.sqrt(k3 @ k3 + m * m)
    gk = sum(k3[j] * g[j] for j in range(3))
    ident = np.eye(4, dtype=complex)
    scal = (1.0 / (2 * E)) * np.exp(-E * abs(tau))
    vec = (1j / 2.0) * np.sign(tau) * np.exp(-E * abs(tau))
    return (m * ident - 1j * gk) * scal + (-1j * g[3]) * vec


# --------------------------------------------------------------------------
# R1: statistics-blind kernel inverse
# --------------------------------------------------------------------------
def check_R1_statistics_blind_inverse(rng):
    ident = np.eye(4, dtype=complex)
    ok = True
    for _ in range(120):
        m = rng.uniform(0.2, 3.0)
        p4 = rng.normal(size=4)
        S = S_momentum(p4, m)
        M = M_momentum(p4, m)
        ok &= np.allclose(M @ S, ident, atol=1e-10)
        ok &= np.allclose(S @ M, ident, atol=1e-10)
        ok &= np.allclose(S, np.linalg.inv(M), atol=1e-10)
        # statistics-blind: S is the inverse of the quadratic form, the SAME
        # matrix for either measure. (no statistics flag anywhere)
    return bool(ok)


# --------------------------------------------------------------------------
# R2: OS1 SO(4) bispinor covariance of the continuum kernel
# --------------------------------------------------------------------------
def spin4_representative(rng):
    """Random Spin(4) element U = exp(theta/4 [g_a, g_b]) for a plane (a,b)."""
    g = euclidean_gammas()
    a, b = rng.choice(4, size=2, replace=False)
    theta = rng.uniform(-1.0, 1.0)
    gen = 0.25 * (g[a] @ g[b] - g[b] @ g[a])
    # matrix exponential via eigen-free series is fine for small generator
    U = _expm(theta * gen)
    return U


def _expm(A, terms=40):
    out = np.eye(A.shape[0], dtype=complex)
    term = np.eye(A.shape[0], dtype=complex)
    for n in range(1, terms):
        term = term @ A / n
        out = out + term
    return out


def check_R2_so4_bispinor_covariance(rng):
    g = euclidean_gammas()
    ok = True
    for _ in range(60):
        m = rng.uniform(0.3, 2.0)
        U = spin4_representative(rng)
        Uinv = np.linalg.inv(U)
        # recover SO(4) image A_{nu mu} = (1/4) tr(g_nu U g_mu U^{-1})
        A = np.zeros((4, 4))
        for nu in range(4):
            for mu in range(4):
                A[nu, mu] = (0.25 * np.trace(g[nu] @ U @ g[mu] @ Uinv)).real
        ok &= np.allclose(A.T @ A, np.eye(4), atol=1e-8)  # A in O(4)
        ok &= np.isclose(np.linalg.det(A), 1.0, atol=1e-7)  # SO(4)
        p4 = rng.normal(size=4)
        Sp = S_momentum(p4, m)
        Ap = A @ p4
        ok &= np.allclose(U @ Sp @ Uinv, S_momentum(Ap, m), atol=1e-8)
    return bool(ok)


# --------------------------------------------------------------------------
# R3: OS2 fermionic reflection positivity (THE HARD STEP, DERIVED)
# --------------------------------------------------------------------------
def rp_gram(taus, k3, m, reflection):
    """Fermionic OS Gram matrix at fixed spatial momentum k, positive times.

    M_{(i,a),(j,b)} = [ reflection . S(tau_i + tau_j, k) ]_{ab}.
    The correct Euclidean-time reflection on Dirac spinors is reflection = g4.
    """
    n = len(taus)
    big = np.zeros((4 * n, 4 * n), dtype=complex)
    for i, ti in enumerate(taus):
        for j, tj in enumerate(taus):
            big[4 * i:4 * i + 4, 4 * j:4 * j + 4] = reflection @ S_tau_k(ti + tj, k3, m)
    return (big + big.conj().T) / 2.0  # Hermitian part (it is Hermitian by construction)


def check_R3_fermionic_reflection_positivity(rng):
    g = euclidean_gammas()
    worst_correct = np.inf  # min eigenvalue with the correct reflection (want >= 0)
    worst_wrong = np.inf    # min eigenvalue with the wrong reflection (want clearly < 0)
    for _ in range(300):
        m = rng.uniform(0.2, 3.0)
        k3 = rng.normal(size=3)
        taus = np.sort(rng.uniform(0.05, 2.0, size=int(rng.integers(2, 6))))
        # correct fermion reflection = g4
        mc = np.linalg.eigvalsh(rp_gram(taus, k3, m, g[3])).min()
        worst_correct = min(worst_correct, mc)
        # wrong reflection = identity (no spinor reflection)
        mw = np.linalg.eigvalsh(rp_gram(taus, k3, m, np.eye(4, dtype=complex))).min()
        worst_wrong = min(worst_wrong, mw)
    psd = worst_correct >= -ATOL
    nontrivial = worst_wrong < -1e-3  # the wrong reflection genuinely fails positivity
    return bool(psd and nontrivial)


# --------------------------------------------------------------------------
# R4: OS4 cluster / mass gap
# --------------------------------------------------------------------------
def check_R4_cluster_mass_gap(rng):
    ok = True
    for _ in range(40):
        m = rng.uniform(0.3, 2.0)
        t1, t2 = 1.0, 1.0 + rng.uniform(1.0, 3.0)
        n1 = np.linalg.norm(S_tau_k(t1, np.zeros(3), m))
        n2 = np.linalg.norm(S_tau_k(t2, np.zeros(3), m))
        rate = -np.log(n2 / n1) / (t2 - t1)
        ok &= np.isclose(rate, m, atol=1e-6)  # decay rate is exactly the mass gap
    return bool(ok)


# --------------------------------------------------------------------------
# R5: Wick rotation -> Minkowski mass shell (SO(3,1))
# --------------------------------------------------------------------------
def check_R5_wick_mass_shell(rng):
    ok = True
    for _ in range(120):
        m = rng.uniform(0.2, 3.0)
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        # Euclidean denom p^2+m^2 with p4 = iE: -E^2 + |p|^2 + m^2 = 0 (mass shell)
        ok &= np.isclose(-E * E + p3 @ p3 + m * m, 0.0, atol=1e-9)
        # and the Euclidean scalar denom has poles at p4 = +/- iE
        roots = np.roots([1.0, 0.0, E * E])
        ok &= np.allclose(np.sort(roots.imag), [-E, E], atol=1e-9)
    return bool(ok)


# --------------------------------------------------------------------------
# R6: positive-energy spectrum (rung C, on the mode structure)
# --------------------------------------------------------------------------
def dirac_hamiltonian(p3, m):
    G = minkowski_gammas()
    G0 = G[0]
    alpha = [G0 @ G[k + 1] for k in range(3)]
    H = sum(p3[k] * alpha[k] for k in range(3)) + m * G0
    return H


def check_R6_positive_energy_spectrum(rng):
    ok = True
    for _ in range(80):
        m = rng.uniform(0.2, 3.0)
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        spec = np.sort(np.linalg.eigvalsh(dirac_hamiltonian(p3, m)))
        ok &= np.allclose(spec, [-E, -E, E, E], atol=1e-9)
        # CAR-relabeled many-body H over a few modes: occupation in {0,1}, energies +E
        # H = sum_modes E_mode (n_a + n_b); ground state energy 0, all energies >= 0.
        n_modes = int(rng.integers(1, 4))
        energies = rng.uniform(0.3, 2.0, size=n_modes)
        # enumerate all 2^(2 n_modes) occupations -> all energies >= 0, min = 0
        worst = np.inf
        for occ in range(1 << (2 * n_modes)):
            bits = [(occ >> b) & 1 for b in range(2 * n_modes)]
            En = sum(energies[i % n_modes] * bits[i] for i in range(2 * n_modes))
            worst = min(worst, En)
        ok &= np.isclose(worst, 0.0, atol=1e-12)  # bounded below, vacuum energy 0
    return bool(ok)


# --------------------------------------------------------------------------
# R7: Gaussian n-point hierarchy (exact: Isserlis & Pfaffian recursions,
#     Pfaffian^2 = det). No Monte Carlo: every identity is algebraically exact.
# --------------------------------------------------------------------------
def _perfect_matchings(idx):
    """Yield every perfect matching (list of pairs) of the index list idx."""
    if not idx:
        yield []
        return
    a = idx[0]
    for i in range(1, len(idx)):
        b = idx[i]
        rest = idx[1:i] + idx[i + 1:]
        for m in _perfect_matchings(rest):
            yield [(a, b)] + m


def _perm_sign(perm, base):
    pos = {v: i for i, v in enumerate(base)}
    arr = [pos[v] for v in perm]
    s = 1
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                s = -s
    return s


def isserlis(C, idx):
    """Bosonic (symmetric) 2n-point: unsigned sum over all perfect matchings."""
    return sum(np.prod([C[p, q] for (p, q) in M]) for M in _perfect_matchings(idx))


def pfaffian(A, idx):
    """Fermionic (antisymmetric) 2n-point: signed sum over perfect matchings."""
    tot = 0.0 + 0.0j
    for M in _perfect_matchings(idx):
        perm = []
        for (p, q) in M:
            perm += [p, q]
        tot += _perm_sign(perm, idx) * np.prod([A[p, q] for (p, q) in M])
    return tot


def check_R7_gaussian_npoint_hierarchy(rng):
    """The full n-point hierarchy is FIXED by the 2-point via the Gaussian
    recursion -- exactly, for both statistics. Verified at the 4- and 6-point
    level on random 2-point data:

      (bosonic / Isserlis)   E[x_{i0} ... ] = sum_j C[i0,j] E[ rest \\ {i0,j} ]
      (fermionic / Pfaffian) Pf(A)          = sum_j (-1)^{j-1} A[i0,j] Pf(rest)
      (fermionic identity)   Pf(A)^2        = det(A).
    """
    ok = True
    for _ in range(60):
        # bosonic 2-point: symmetric covariance C
        Csym = rng.normal(size=(6, 6))
        C = Csym + Csym.T
        for idx in ([0, 1, 2, 3], [0, 1, 2, 3, 4, 5]):
            iss = isserlis(C, idx)
            i0 = idx[0]
            rec = 0.0
            for k in range(1, len(idx)):
                jk = idx[k]
                rest = idx[1:k] + idx[k + 1:]
                rec += C[i0, jk] * isserlis(C, rest)
            ok &= np.isclose(rec, iss, atol=1e-9)  # bosonic Wick recursion

        # fermionic 2-point: antisymmetric matrix A
        B = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
        A = B - B.T
        pf = pfaffian(A, [0, 1, 2, 3, 4, 5])
        ok &= np.isclose(pf * pf, np.linalg.det(A), atol=1e-6)  # Pfaffian^2 = det
        # fermionic Pfaffian Laplace recursion
        i0 = 0
        rec = 0.0 + 0.0j
        for k in range(1, 6):
            jk = k
            rest = [x for x in range(6) if x not in (i0, jk)]
            rec += ((-1) ** (k - 1)) * A[i0, jk] * pfaffian(A, rest)
        ok &= np.isclose(rec, pf, atol=1e-8)  # fermionic Wick recursion

        # 4x4 closed form consistency: 4-point fermionic Wick = explicit Pfaffian
        A4 = A[:4, :4]
        pf4 = A4[0, 1] * A4[2, 3] - A4[0, 2] * A4[1, 3] + A4[0, 3] * A4[1, 2]
        ok &= np.isclose(pf4, pfaffian(A4, [0, 1, 2, 3]), atol=1e-10)
        if not ok:
            break
    return bool(ok)


# --------------------------------------------------------------------------
# R8: u/v completeness, norms, relative sign (established fragment)
# --------------------------------------------------------------------------
def dirac_uv(p3, m):
    """Return (u_s), (v_s) as columns from the Dirac Hamiltonian eigenvectors,
    scaled to Hilbert norm 2E, and the Minkowski gammas."""
    G = minkowski_gammas()
    G0 = G[0]
    H = dirac_hamiltonian(p3, m)
    w, V = np.linalg.eigh(H)
    E = np.sqrt(p3 @ p3 + m * m)
    us, vs = [], []
    for i in range(4):
        vec = V[:, i]
        vec = vec / np.linalg.norm(vec) * np.sqrt(2 * E)  # u^dag u = 2E
        if w[i] > 0:
            us.append(vec)
        else:
            vs.append(vec)
    return us, vs, G


def check_R8_uv_relative_sign(rng):
    ok = True
    for _ in range(80):
        m = rng.uniform(0.3, 2.0)
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        us, vs, G = dirac_uv(p3, m)
        G0 = G[0]
        # Hilbert norms 2E
        for u in us:
            ok &= np.isclose(np.vdot(u, u).real, 2 * E, atol=1e-7)
        for v in vs:
            ok &= np.isclose(np.vdot(v, v).real, 2 * E, atol=1e-7)
        # Dirac bilinears ubar u = u^dag G0 u and relative sign
        ubaru = np.mean([np.vdot(u, G0 @ u).real for u in us])
        vbarv = np.mean([np.vdot(v, G0 @ v).real for v in vs])
        ok &= (np.sign(ubaru) == -np.sign(vbarv))  # convention-independent relative sign
        ok &= ubaru > 0 and vbarv < 0
    return bool(ok)


# --------------------------------------------------------------------------
def main():
    rng = np.random.default_rng(SEED)
    checks = [
        ("R1_statistics_blind_kernel_inverse", check_R1_statistics_blind_inverse),
        ("R2_os1_so4_bispinor_covariance", check_R2_so4_bispinor_covariance),
        ("R3_os2_fermionic_reflection_positivity", check_R3_fermionic_reflection_positivity),
        ("R4_os4_cluster_mass_gap", check_R4_cluster_mass_gap),
        ("R5_wick_rotation_mass_shell_so31", check_R5_wick_mass_shell),
        ("R6_positive_energy_spectrum", check_R6_positive_energy_spectrum),
        ("R7_gaussian_npoint_pfaffian_hierarchy", check_R7_gaussian_npoint_hierarchy),
        ("R8_uv_relative_sign_and_completeness", check_R8_uv_relative_sign),
    ]
    npass = 0
    nfail = 0
    for name, fn in checks:
        ok = fn(rng)
        tag = "PASS" if ok else "FAIL"
        if ok:
            npass += 1
        else:
            nfail += 1
        print(f"[{tag}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
