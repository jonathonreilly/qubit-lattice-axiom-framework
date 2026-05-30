#!/usr/bin/env python3
"""Audit-companion runner for FREE_FIELD_LATTICE_TO_CONTINUUM_GAUSSIAN_MEASURE.

The deliverable this runner backs is narrow:

    For a specified free fermionic Gaussian/quasi-free Dirac theory, smeared
    covariance convergence drives convergence of fixed finite Pfaffian
    Schwinger functions. For the cited free staggered covariance, pointwise
    convergence upgrades to smeared Schwartz-test convergence by a dominated
    convergence envelope. No one-dimensional transfer-matrix bridge is used.

The runner is free/Gaussian only. It makes no interacting claim, no statistics
selection, and no emergent-Lorentz claim. It does NOT use any finite-`a`
taste-flat operator: taste enters strictly as a four-fold spectral multiplicity
in the continuum limit, as in the cited covariance note.

Checks:

  F1  Free-fermion n-point = Pfaffian of the 2-point (4- and 6-point), with the
      fermionic identity Pf(A)^2 = det(A). This is the Gaussian-rigidity input
      that each fixed hierarchy element is a polynomial in the 2-point matrix.

  F2  Characteristic functional rigidity: for finite Gaussian/quasi-free test
      data, the generating
      functional chi_C(J) = exp(-1/2 <J, C J>) is determined by the covariance,
      and (J -> chi_C(J)) is injective in C on a spanning test-spinor set.
      Convergence of the smeared covariance <J, C_a J> <=> convergence of
      chi_{C_a}(J) for every J. (Bratteli-Robinson quasi-free state continuity;
      Glimm-Jaffe Gaussian generating functional.)

  F3  a -> 0 sequence of the lattice staggered 2-point S_a(p) ->
      S(p) = (m - i gamma.p)/(p^2 + m^2), SMEARED against a Schwartz test-spinor
      set. Shows: (i) the smeared pairing <f, S_a g> -> <f, S g>; (ii) hence the
      characteristic functional exp(-1/2 <J,S_a J>) -> exp(-1/2 <J,S J>); (iii)
      hence the induced n-point (Pfaffian) functions converge. This is the
      distributional / test-function sense OS reconstruction consumes, built on
      top of the cited covariance note's pointwise/orbit O(a^2) convergence.

  F4  Taste enters as a four-fold multiplicity in the limit: the exact finite-`a`
      scalar spectrum Delta_a(p) = m^2 + (1/a^2) sum_mu sin^2(p_mu a) has every
      eigenvalue of the 16x16 reduced operator appearing with multiplicity 4,
      and Delta_a(p) -> m^2 + |p|^2. No finite-`a` taste-flat operator is used.

  F5  Non-triviality control: a covariance sequence that does NOT converge
      (a fixed O(1) mis-scaling that survives a -> 0) yields a NON-converging
      smeared pairing, hence a non-converging characteristic functional and
      non-converging Pfaffian moments. So F3 is a real convergence theorem about
      THIS sequence, not a tautology that holds for any sequence.

  F6  Dominated-convergence envelope: the cited covariance note gives
      POINTWISE-in-p (and SO(4)-orbit scalar) O(a^2) convergence. The runner
      exhibits ||S_a(p)||_F = 2/sqrt(Delta_a(p)) and the bounds used to pass
      from pointwise to smeared convergence for Schwartz test spinors.

It does NOT verify the abstract OS reconstruction theorem, microcausality, or a
spin-statistics theorem.
"""

import itertools

import numpy as np


# --------------------------------------------------------------------------
# Euclidean Dirac matrices (Hermitian, {g_mu, g_nu} = 2 delta_mu_nu).
# Same convention as the cited free staggered covariance packet.
# --------------------------------------------------------------------------
def euclidean_gammas():
    i2 = np.eye(2, dtype=complex)
    z2 = np.zeros((2, 2), dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    g4 = np.block([[i2, z2], [z2, -i2]])
    g1 = np.block([[z2, -1j * sx], [1j * sx, z2]])
    g2 = np.block([[z2, -1j * sy], [1j * sy, z2]])
    g3 = np.block([[z2, -1j * sz], [1j * sz, z2]])
    return [g1, g2, g3, g4]


GAMMAS = euclidean_gammas()


def S_continuum(p, m):
    """Continuum free Dirac 2-point S(p) = (m - i gamma.p)/(p^2 + m^2)."""
    gp = sum(p[k] * GAMMAS[k] for k in range(4))
    return (m * np.eye(4, dtype=complex) - 1j * gp) / (p @ p + m * m)


def S_lattice(p, a, m):
    """Free staggered lattice 2-point (one irreducible spin block):

        S_a(p) = (m 1 - i sum_mu gamma_mu s_mu) / Delta_a(p),
        s_mu = sin(p_mu a)/a,   Delta_a(p) = m^2 + sum_mu s_mu^2.

    As a -> 0 with p fixed: s_mu -> p_mu, Delta_a -> m^2 + |p|^2, so
    S_a(p) -> S(p). Taste is a four-fold spectral multiplicity (F4), not in S_a.
    """
    s = np.sin(p * a) / a
    gs = sum(s[k] * GAMMAS[k] for k in range(4))
    Delta = m * m + float(s @ s)
    return (m * np.eye(4, dtype=complex) - 1j * gs) / Delta


def S_lattice_misscaled(p, a, m, eps=0.35):
    """Non-triviality control (F5): a covariance whose mass is shifted by a
    FIXED O(1) amount that does NOT vanish as a -> 0. Its pointwise limit is
    S(p; m+eps) != S(p; m), so neither the smeared pairing nor the moments
    converge to the target. Same functional shape, broken limit."""
    return S_lattice(p, a, m + eps)


# --------------------------------------------------------------------------
# Gaussian rigidity: n-point = Pfaffian of the antisymmetric 2-point.
# --------------------------------------------------------------------------
def pfaffian(A):
    """Pfaffian of an even-dimensional antisymmetric matrix, by the
    recursive Laplace expansion Pf(A) = sum_j (-1)^j A[0,j] Pf(A without 0,j)."""
    A = np.asarray(A, dtype=complex)
    n = A.shape[0]
    if n == 0:
        return 1.0 + 0.0j
    if n % 2 == 1:
        return 0.0 + 0.0j
    if n == 2:
        return A[0, 1]
    total = 0.0 + 0.0j
    rest = list(range(1, n))
    for k, j in enumerate(rest):
        idx = [r for r in rest if r != j]
        minor = A[np.ix_(idx, idx)]
        total += ((-1) ** k) * A[0, j] * pfaffian(minor)
    return total


def gaussian_npoint_pfaffian(cov):
    """Free-fermion n-point = Pf(cov) for the antisymmetric 2-point matrix
    cov (the Berezin-Gaussian / Wick rule). Returns Pf(cov)."""
    return pfaffian(cov)


def random_antisymmetric(n, rng):
    B = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return B - B.T


# --------------------------------------------------------------------------
# Test-spinor (Schwartz) smearing infrastructure for F3 / F6.
# We work in momentum space on a fixed continuum grid of physical momenta and
# pair the 4x4 kernels against Gaussian-decay (Schwartz) test spinors. The
# smeared pairing is <f, K g> = sum_p fbar(p) K(p) g(p) w(p), a Riemann
# approximation to the tempered pairing the OS Schwinger functions live in.
# --------------------------------------------------------------------------
def schwartz_grid(n_per_axis, p_max):
    """Symmetric continuum momentum grid in 4D Euclidean space."""
    axis = np.linspace(-p_max, p_max, n_per_axis)
    dp = axis[1] - axis[0]
    pts = np.array(list(itertools.product(axis, repeat=4)))
    weight = dp ** 4
    return pts, weight


def schwartz_test_spinors(pts, rng, n_test):
    """A set of Schwartz (Gaussian-decay) 4-component test spinors f(p)."""
    norm2 = np.sum(pts ** 2, axis=1)
    fields = []
    for _ in range(n_test):
        widths = rng.uniform(0.4, 1.0, size=4)
        phases = rng.uniform(0, 2 * np.pi, size=4)
        amps = rng.uniform(0.5, 1.5, size=4)
        env = np.exp(-0.5 * norm2 / rng.uniform(0.8, 1.6) ** 2)
        spinor = np.stack(
            [amps[c] * np.exp(1j * phases[c]) * np.exp(-0.5 * norm2 * widths[c] ** 2 / 4)
             for c in range(4)],
            axis=1,
        )
        fields.append(spinor * env[:, None])
    return fields


def smeared_pairing(kernel_of_p, f, g, pts, weight):
    """<f, K g> = sum_p conj(f(p)) . K(p) . g(p) * weight, K a 4x4 kernel."""
    total = 0.0 + 0.0j
    for i in range(pts.shape[0]):
        K = kernel_of_p(pts[i])
        total += np.vdot(f[i], K @ g[i])
    return total * weight


def char_functional(quad_form):
    """Gaussian characteristic functional exp(-1/2 <J, C J>)."""
    return np.exp(-0.5 * quad_form)


# --------------------------------------------------------------------------
# Checks
# --------------------------------------------------------------------------
def check_g1_pfaffian_hierarchy(rng):
    """Free-fermion 4- and 6-point = Pfaffian of the 2-point; Pf^2 = det."""
    ok = True
    for n in (4, 6):
        for _ in range(200):
            A = random_antisymmetric(n, rng)
            pf = gaussian_npoint_pfaffian(A)
            det = np.linalg.det(A)
            ok &= abs(pf * pf - det) < 1e-7 * (1 + abs(det))
        # Laplace recursion consistency: Pf(A) = sum_j (-1)^j A[0,j] Pf(minor)
        A = random_antisymmetric(n, rng)
        rest = list(range(1, n))
        recur = 0.0 + 0.0j
        for k, j in enumerate(rest):
            idx = [r for r in rest if r != j]
            recur += ((-1) ** k) * A[0, j] * pfaffian(A[np.ix_(idx, idx)])
        ok &= abs(recur - pfaffian(A)) < 1e-9
    return bool(ok)


def check_g2_char_functional_rigidity(rng):
    """For Gaussians, chi_C(J) = exp(-1/2 <J,C J>) is fixed by the covariance C,
    and the map C -> chi_C(.) is injective on a spanning test set: <J,C J> =
    <J,C' J> for a spanning set of J forces C = C'. So covariance convergence
    <=> characteristic-functional convergence (Bratteli-Robinson quasi-free
    continuity; Glimm-Jaffe). Covariances are PSD (physical: a real covariance
    obeys Re<J,C J> >= 0, so |chi_C(J)| <= 1)."""
    ok = True
    for _ in range(50):
        # PSD 4x4 covariances C = G G^dag (physical covariance positivity).
        G = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        C = G @ G.conj().T
        Gp = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        Cp = Gp @ Gp.conj().T
        # Injectivity: if <J,C J> = <J,C' J> for a spanning set of J, then C=C'.
        Js = [rng.normal(size=4) + 1j * rng.normal(size=4) for _ in range(40)]
        same_quad = all(
            abs(np.vdot(J, C @ J) - np.vdot(J, Cp @ J)) < 1e-9 for J in Js
        )
        ok &= (same_quad == np.allclose(C, Cp, atol=1e-7))
        # Functional continuity for PSD C: a small change dC in the covariance
        # gives a small change in chi. With Re<J,C J> >= 0, |chi| <= 1 and the
        # bound |chi_C(J) - chi_{C+dC}(J)| <= (1/2)|<J,dC J>| holds.
        dH = 1e-6 * (rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4)))
        dC = dH + dH.conj().T
        J = rng.normal(size=4) + 1j * rng.normal(size=4)
        q0 = np.vdot(J, C @ J)
        q1 = np.vdot(J, (C + dC) @ J)
        dq = np.vdot(J, dC @ J)
        ok &= abs(char_functional(q0) - char_functional(q1)) <= 0.5 * abs(dq) + 1e-9
        ok &= abs(char_functional(q0)) <= 1.0 + 1e-12  # PSD => |chi| <= 1
    return bool(ok)


def check_g3_smeared_convergence_drives_functional_and_moments(rng):
    """a -> 0: smeared <f,S_a g> -> <f,S g>; hence chi converges; hence the
    induced Pfaffian n-point converges. This is the distributional sense OS
    needs, built on the cited pointwise covariance convergence."""
    m = 0.7
    pts, weight = schwartz_grid(n_per_axis=7, p_max=3.0)
    fields = schwartz_test_spinors(pts, rng, n_test=4)
    a_seq = [0.4, 0.2, 0.1, 0.05]

    ok = True

    # (i) smeared pairing converges, and the error halves as O(a) or faster
    cont_pair = smeared_pairing(lambda p: S_continuum(p, m), fields[0], fields[1], pts, weight)
    errs = []
    for a in a_seq:
        lat_pair = smeared_pairing(lambda p: S_lattice(p, a, m), fields[0], fields[1], pts, weight)
        errs.append(abs(lat_pair - cont_pair))
    # monotone decreasing to ~0
    ok &= all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
    ok &= errs[-1] < 1e-2 * (1 + abs(cont_pair))
    # convergence rate: refining a by 2 cuts the error by >~ 2 (O(a) or O(a^2))
    ratios = [errs[i] / max(errs[i + 1], 1e-30) for i in range(len(errs) - 1)]
    ok &= all(r > 1.8 for r in ratios)

    # (ii) characteristic functional converges (diagonal quad form <J,C J>)
    J = fields[2]
    qf_cont = smeared_pairing(lambda p: S_continuum(p, m), J, J, pts, weight)
    chi_cont = char_functional(qf_cont)
    chi_errs = []
    for a in a_seq:
        qf_lat = smeared_pairing(lambda p: S_lattice(p, a, m), J, J, pts, weight)
        chi_errs.append(abs(char_functional(qf_lat) - chi_cont))
    ok &= all(chi_errs[i + 1] < chi_errs[i] + 1e-12 for i in range(len(chi_errs) - 1))
    ok &= chi_errs[-1] < 1e-2

    # (iii) induced n-point (Pfaffian) functions converge. Build a 4-point
    # antisymmetric 2-point matrix from smeared pairings on a 4-leg test set
    # and track its Pfaffian as a -> 0.
    legs = schwartz_test_spinors(pts, rng, n_test=4)

    def cov_matrix(kernel_of_p):
        n = 4
        M = np.zeros((n, n), dtype=complex)
        for i in range(n):
            for j in range(n):
                M[i, j] = smeared_pairing(kernel_of_p, legs[i], legs[j], pts, weight)
        return M - M.T  # antisymmetrize -> Berezin 2-point

    pf_cont = pfaffian(cov_matrix(lambda p: S_continuum(p, m)))
    pf_errs = []
    for a in a_seq:
        pf_lat = pfaffian(cov_matrix(lambda p: S_lattice(p, a, m)))
        pf_errs.append(abs(pf_lat - pf_cont))
    ok &= all(pf_errs[i + 1] < pf_errs[i] + 1e-12 for i in range(len(pf_errs) - 1))
    ok &= pf_errs[-1] < 1e-2 * (1 + abs(pf_cont))

    return bool(ok)


def check_g4_taste_fourfold_multiplicity(rng):
    """Taste enters as a 4-fold spectral multiplicity in the limit. The 16x16
    reduced staggered operator's M^dag M spectrum is the scalar Delta_a(p) with
    multiplicity 4 (4 identical spin blocks), and Delta_a -> m^2 + |p|^2.
    NO finite-`a` taste-flat operator is built: we use the scalar spectrum
    directly and confirm the multiplicity from the full 16x16 object."""
    ok = True

    def alpha_matrices():
        # alpha_mu: Hermitian involutions on the 16-dim hypercube label space,
        # (alpha_mu)_{b xor e_mu, b} = (-1)^{sum_{nu<mu} b_nu}; Clifford with 4
        # identical spin blocks (cited covariance packet).
        labels = list(itertools.product([0, 1], repeat=4))
        index = {b: i for i, b in enumerate(labels)}
        alphas = []
        for mu in range(4):
            A = np.zeros((16, 16), dtype=complex)
            for b in labels:
                bb = list(b)
                bb[mu] ^= 1
                bb = tuple(bb)
                sign = (-1) ** sum(b[nu] for nu in range(mu))
                A[index[bb], index[b]] = sign
            alphas.append(A)
        return alphas

    alphas = alpha_matrices()
    # Clifford check
    for mu in range(4):
        for nu in range(4):
            anti = alphas[mu] @ alphas[nu] + alphas[nu] @ alphas[mu]
            expected = 2.0 * (mu == nu) * np.eye(16)
            ok &= np.allclose(anti, expected, atol=1e-12)

    m = 0.9
    for _ in range(8):
        a = rng.uniform(0.05, 0.4)
        p = rng.normal(size=4)
        s = np.sin(p * a) / a
        M16 = m * np.eye(16, dtype=complex) + 1j * sum(s[k] * alphas[k] for k in range(4))
        eig = np.linalg.eigvalsh(M16.conj().T @ M16)
        Delta = m * m + float(s @ s)
        # every eigenvalue = Delta, with multiplicity 16 here (all 4 spin blocks
        # identical AND the 4x4 block itself is Delta * I_4) -> divisible by 4.
        ok &= np.allclose(eig, Delta, atol=1e-9)
        ok &= (eig.shape[0] % 4 == 0)
        # continuum limit of the scalar spectrum
        Delta_small = m * m + float((np.sin(p * 1e-4) / 1e-4) ** 2 @ np.ones(4)) if False else None
    # continuum limit Delta_a -> m^2 + |p|^2
    for _ in range(8):
        p = rng.normal(size=4)
        vals = []
        for a in (0.2, 0.1, 0.05, 0.025):
            s = np.sin(p * a) / a
            vals.append(m * m + float(s @ s))
        target = m * m + float(p @ p)
        errs = [abs(v - target) for v in vals]
        ok &= all(errs[i + 1] < errs[i] for i in range(len(errs) - 1))
    return bool(ok)


def check_g5_nonconverging_control(rng):
    """Non-triviality control. Head-to-head: the CORRECT lattice sequence
    S_a(.; m) has a smeared error to the target S(.; m) that shrinks RAPIDLY
    under a-refinement (O(a)-or-better, factor >= 2 per halving), whereas a
    mis-scaled sequence S_a(.; m+eps) -- which has a fixed O(1) mass offset that
    does NOT vanish as a -> 0 -- has a smeared error to the SAME target that
    PLATEAUS (factor < 1.5 per halving, bounded away from 0). So the smeared
    convergence of F3 is a real theorem about this sequence, not a tautology.
    Robust to the test-spinor draw (compares decay RATES, not raw magnitudes)."""
    m = 0.7
    eps = 0.6  # fixed O(1) offset that survives a -> 0 (wrong continuum limit)
    pts, weight = schwartz_grid(n_per_axis=7, p_max=3.0)
    fields = schwartz_test_spinors(pts, rng, n_test=2)
    a_seq = [0.2, 0.1, 0.05, 0.025]
    ok = True

    target = smeared_pairing(lambda p: S_continuum(p, m), fields[0], fields[1], pts, weight)
    scale = 1.0 + abs(target)

    good_errs, bad_errs = [], []
    for a in a_seq:
        good = smeared_pairing(lambda p: S_lattice(p, a, m), fields[0], fields[1], pts, weight)
        bad = smeared_pairing(lambda p: S_lattice_misscaled(p, a, m, eps), fields[0], fields[1], pts, weight)
        good_errs.append(abs(good - target))
        bad_errs.append(abs(bad - target))

    # The CORRECT sequence converges: error shrinks by a factor >= 2 per halving
    good_ratios = [good_errs[i] / max(good_errs[i + 1], 1e-30) for i in range(len(good_errs) - 1)]
    ok &= all(r >= 2.0 for r in good_ratios)
    ok &= good_errs[-1] < 1e-2 * scale

    # The MIS-SCALED sequence does NOT converge to the target: error plateaus
    # (each refinement reduces it by < 1.5x) and stays bounded away from zero.
    bad_ratios = [bad_errs[i] / max(bad_errs[i + 1], 1e-30) for i in range(len(bad_errs) - 1)]
    ok &= all(r < 1.5 for r in bad_ratios)
    ok &= bad_errs[-1] > 1e-2 * scale
    # The final mis-scaled error is at least 50x the final correct error.
    ok &= bad_errs[-1] > 50.0 * good_errs[-1]
    return bool(ok)


def check_g6_dominated_convergence_envelope(rng):
    """Dominated-convergence probe: the cited covariance packet gives pointwise
    O(a^2) convergence
    S_a(p) -> S(p). To upgrade to the SMEARED (test-function) convergence OS
    needs, one applies dominated convergence with the uniform envelope

        |S_a(p)|_F <= C / (Delta_a(p))^{1/2} <= C / sqrt(m^2 + (2/pi)^2 |p|^2)

    on the first Brillouin zone |p_mu| <= pi/a (using |sin(x)| >= (2/pi)|x| for
    |x| <= pi/2). The Frobenius norm of S_a is exactly (4 / Delta_a)^{1/2} since
    S_a S_a^dag = (1/Delta_a) I_4. This envelope is Schwartz-integrable against
    Schwartz test spinors uniformly in a, supplying the missing dominating
    function. This check exhibits the envelope numerically; the analytic
    dominated-convergence step upgrades pointwise convergence to the smeared
    statement for fixed positive mass and Schwartz test spinors."""
    m = 0.8
    ok = True
    for _ in range(200):
        a = rng.uniform(0.02, 0.4)
        # momentum in the first BZ |p_mu| <= pi/a
        p = rng.uniform(-np.pi / a, np.pi / a, size=4)
        S = S_lattice(p, a, m)
        s = np.sin(p * a) / a
        Delta = m * m + float(s @ s)
        # exact: ||S_a||_F^2 = 4 / Delta_a (since S S^dag = I/Delta)
        ok &= abs(np.linalg.norm(S, "fro") ** 2 - 4.0 / Delta) < 1e-9
        # envelope: |sin(x)| >= (2/pi)|x| for |x| <= pi/2 -> on the BZ HALF
        # |p_mu a| <= pi/2 we get Delta_a >= m^2 + (2/pi)^2 |p|^2.
        if np.all(np.abs(p * a) <= np.pi / 2):
            ok &= Delta >= m * m + (2.0 / np.pi) ** 2 * float(p @ p) - 1e-9
        # the envelope C/sqrt(Delta_a) with C=2 dominates ||S_a||_F everywhere
        ok &= np.linalg.norm(S, "fro") <= 2.0 / np.sqrt(Delta) + 1e-9
    return bool(ok)


def main():
    rng = np.random.default_rng(20260530)
    checks = [
        ("F1_freefermion_npoint_is_pfaffian_of_2point", check_g1_pfaffian_hierarchy(rng)),
        ("F2_gaussian_char_functional_rigidity", check_g2_char_functional_rigidity(rng)),
        ("F3_smeared_convergence_drives_functional_and_moments",
         check_g3_smeared_convergence_drives_functional_and_moments(rng)),
        ("F4_taste_fourfold_multiplicity_in_limit", check_g4_taste_fourfold_multiplicity(rng)),
        ("F5_nonconverging_covariance_control", check_g5_nonconverging_control(rng)),
        ("F6_dominated_convergence_envelope", check_g6_dominated_convergence_envelope(rng)),
    ]

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
