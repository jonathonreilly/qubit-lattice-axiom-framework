#!/usr/bin/env python3
"""Audit-companion runner for FREE_STAGGERED_2POINT_SMEARED_CONVERGENCE.

Standalone lemma: the SMEARED / distributional upgrade of rung A's POINTWISE
free staggered-Dirac 2-point convergence.

    THEOREM (smeared 2-point convergence). Given rung A's pointwise convergence
    S_a(p) -> S(p) = (m - i gamma.p)/(p^2 + m^2)  (a -> 0, taste a 4-fold
    spectral multiplicity), the smeared pairing <f, S_a g> -> <f, S g> holds for
    all Schwartz test spinors f, g.

Mechanism (this runner verifies it NON-VACUOUSLY):

  * The free covariance is exactly solvable: S_a S_a^dag = (1/Delta_a) 1_4, so
    ||S_a(p)||_F = 2 / sqrt(Delta_a(p)).
  * Jordan's inequality |sin x| >= (2/pi)|x| on [0, pi/2] gives, on the
    Brillouin-zone half |p_mu a| <= pi/2,
        Delta_a(p) = m^2 + (1/a^2) sum_mu sin^2(p_mu a) >= m^2 + (2/pi)^2 |p|^2,
    hence the a-INDEPENDENT bound ||S_a(p)||_F <= Phi(p) = 2/sqrt(m^2+(2/pi)^2|p|^2).
  * KEY SUBTLETY: Phi alone is NOT L^1(R^4) (it decays like 1/|p|), but the
    DOMINATING FUNCTION FOR THE INTEGRAND |f(p)| ||S_a(p)||_F |g(p)| IS L^1 for
    Schwartz f, g (Gaussian/Schwartz decay beats 1/|p| in 4D). The dominating
    function is h(p) = |f(p)| Phi(p) |g(p)| in L^1, NOT Phi itself. Even more
    robustly the crude cap ||S_a||_F <= 2/m (since Delta_a >= m^2) times Schwartz
    f, g already gives an L^1 dominating function.
  * Dominated convergence then interchanges lim_{a->0} with the momentum
    integral -> smeared convergence. G1's residual is discharged; the
    dissolution is conditional ONLY on rung A's pointwise statement.

Scope: FREE / Gaussian only. Fixed m > 0 (Phi uses Delta_a >= m^2 > 0). The
massless / m -> 0 limit is NOT treated. No statistics selection, no
emergent-Lorentz claim, no interacting claim. Taste enters strictly as a 4-fold
spectral multiplicity in the continuum limit; NO finite-`a` taste-flat operator
is built or used. This runner consumes rung A's pointwise convergence as an
INPUT; it does not re-derive rung A.

Checks:

  C1  Exact Frobenius norm: ||S_a(p)||_F = 2/sqrt(Delta_a(p)) to machine
      precision (since S_a S_a^dag = (1/Delta_a) 1_4).

  C2  Jordan bound: on the BZ half |p_mu a| <= pi/2,
      Delta_a(p) >= m^2 + (2/pi)^2 |p|^2 (0 violations over a randomized
      sample); and the a-independent envelope ||S_a||_F <= Phi(p) holds there.

  C3  The integrand-vs-Phi L^1 distinction, exhibited BOTH ways:
        (a) int Phi(p) d^4p DIVERGES (the radial integral of r^3 / sqrt(...)
            grows without bound as the cutoff -> infinity);
        (b) int |f(p)| Phi(p) |g(p)| d^4p CONVERGES (plateaus under cutoff
            refinement) for sample Schwartz f, g; and the crude cap (2/m) too.

  C4  Smeared pairing convergence: <f, S_a g> -> <f, S g> as a -> 0 along a
      sequence a in {0.4, 0.2, 0.1, 0.05}, error decreasing monotonically at
      the O(a^2) rate rung A reports pointwise (each halving cuts error >= ~3x).

  C5  Non-triviality control: a covariance that VIOLATES the bound / does not
      converge (a fixed O(1) mass offset that does not vanish as a -> 0) has a
      smeared pairing that does NOT converge to <f, S g> (error plateaus,
      bounded away from zero; final mis-scaled error >> the correct one). So C4
      is a real theorem about THIS covariance, not a tautology.

  C6  Dominated-convergence interchange, demonstrated directly: the pointwise
      integrand fbar(p) S_a(p) g(p) is dominated uniformly in `a` by the L^1
      function h(p) = |f(p)| Phi(p) |g(p)|, and the integral of the integrand
      converges to the integral of the limit integrand (lim and int commute).

It does NOT machine-verify the abstract OS -> Wightman reconstruction, Gaussian
n-point rigidity (that is the dissolution note's job), or any statistics
selection.
"""

import numpy as np

# numpy >= 2.0 renamed trapz -> trapezoid; support both.
_trapz = getattr(np, "trapezoid", None) or np.trapz


# ---------------------------------------------------------------------------
# Dirac algebra (Euclidean, {g_mu, g_nu} = 2 delta_mu_nu), matching the in-repo
# convention used by the free-Dirac mode-algebra runner.
# ---------------------------------------------------------------------------
def euclidean_gammas():
    """Euclidean Dirac matrices, {g_mu, g_nu} = 2 delta_mu_nu."""
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
IDENT4 = np.eye(4, dtype=complex)


def lattice_momentum(p, a):
    """s_mu(p) = sin(p_mu a) / a; -> p_mu as a -> 0."""
    return np.sin(np.asarray(p) * a) / a


def delta_lattice(p, a, m):
    """Exact scalar denominator Delta_a(p) = m^2 + sum_mu s_mu(p)^2."""
    s = lattice_momentum(p, a)
    return m * m + float(s @ s)


def S_lattice(p, a, m):
    """Free staggered 2-point S_a(p) = (m 1 - i sum_mu g_mu s_mu) / Delta_a.

    Taste is a spectator 4-fold multiplicity (rung A); this 4x4 spin block is
    the irreducible object. NO finite-`a` taste-flat operator is used.
    """
    s = lattice_momentum(p, a)
    gp = sum(s[mu] * GAMMAS[mu] for mu in range(4))
    return (m * IDENT4 - 1j * gp) / delta_lattice(p, a, m)


def S_continuum(p, m):
    """Continuum free Dirac covariance S(p) = (m 1 - i g.p)/(p^2 + m^2)."""
    p = np.asarray(p)
    gp = sum(p[mu] * GAMMAS[mu] for mu in range(4))
    return (m * IDENT4 - 1j * gp) / (float(p @ p) + m * m)


# ---------------------------------------------------------------------------
# Schwartz test-spinor smearing infrastructure.
# A Schwartz test spinor f(p) = (Gaussian envelope) * (fixed 4-vector). The
# pairing is <f, K g> = int d^4p  fbar(p) K(p) g(p)  with fbar the conjugate
# transpose row spinor. We evaluate on a deterministic product grid (midpoint
# quadrature) over a cube [-P, P]^4; the Gaussian decay makes the cube finite-P
# truncation error negligible at the chosen widths.
# ---------------------------------------------------------------------------
def make_grid(n_per_axis, p_max):
    """Deterministic midpoint product grid on [-p_max, p_max]^4.

    Returns (pts, weight): pts is (N, 4); weight is the per-cell d^4p volume.
    """
    axis = np.linspace(-p_max, p_max, n_per_axis, endpoint=False)
    dx = axis[1] - axis[0]
    axis = axis + dx / 2.0  # midpoints
    grids = np.meshgrid(axis, axis, axis, axis, indexing="ij")
    pts = np.stack([g.ravel() for g in grids], axis=1)
    weight = dx ** 4
    return pts, weight


def gaussian_envelope(pts, width, center):
    """exp(-|p - center|^2 / (2 width^2)) on a (N,4) point array -> (N,)."""
    d = pts - np.asarray(center)[None, :]
    return np.exp(-np.einsum("ij,ij->i", d, d) / (2.0 * width * width))


def schwartz_spinor(pts, width, center, vec):
    """f(p): (N, 4) complex array = scalar Gaussian * fixed complex 4-vector."""
    env = gaussian_envelope(pts, width, center)
    return env[:, None] * np.asarray(vec, dtype=complex)[None, :]


def _bilinears(fvals, gvals):
    """Precompute the spinor bilinears that fully determine the pairing of any
    kernel of the form (alpha 1 + i sum_mu beta_mu gamma_mu):

        B0(p)  = fbar(p) . g(p),                     shape (N,)
        Bmu(p) = fbar(p) . gamma_mu . g(p),          shape (N, 4)

    Then  fbar . (alpha 1 + i sum_mu beta_mu gamma_mu) . g
            = alpha B0 + i sum_mu beta_mu Bmu.
    This makes the smeared pairing a pure vectorized numpy reduction (no
    Python-level 4x4 matmul per grid point).
    """
    fc = np.conjugate(fvals)                      # (N, 4)
    B0 = np.einsum("ni,ni->n", fc, gvals)         # (N,)
    Bmu = np.stack([np.einsum("ni,ij,nj->n", fc, GAMMAS[mu], gvals)
                    for mu in range(4)], axis=1)  # (N, 4)
    return B0, Bmu


def smeared_pairing_lattice(a, m, B0, Bmu, pts, weight):
    """<f, S_a g> = int d^4p fbar(p) S_a(p) g(p), fully vectorized.

    S_a(p) = (m 1 - i sum_mu gamma_mu s_mu(p)) / Delta_a(p), so
    fbar S_a g = ( m B0 - i sum_mu s_mu Bmu ) / Delta_a.
    """
    s = np.sin(pts * a) / a                        # (N, 4)
    Delta = m * m + np.einsum("ni,ni->n", s, s)    # (N,)
    num = m * B0 - 1j * np.einsum("ni,ni->n", s, Bmu)
    return complex(np.sum(num / Delta) * weight)


def smeared_pairing_continuum(m, B0, Bmu, pts, weight):
    """<f, S g> with S(p) = (m 1 - i g.p)/(p^2 + m^2), vectorized."""
    Delta = m * m + np.einsum("ni,ni->n", pts, pts)
    num = m * B0 - 1j * np.einsum("ni,ni->n", pts, Bmu)
    return complex(np.sum(num / Delta) * weight)


def envelope_Phi_grid(pts, m):
    """Phi(p) = 2/sqrt(m^2 + (2/pi)^2 |p|^2) on a (N,4) grid -> (N,)."""
    psq = np.einsum("ni,ni->n", pts, pts)
    return 2.0 / np.sqrt(m * m + (2.0 / np.pi) ** 2 * psq)


def integrand_norm_smear(norm_vals, fvals, gvals, weight):
    """int |f(p)| (norm)(p) |g(p)| d^4p, vectorized. norm_vals is (N,)."""
    fmag = np.linalg.norm(fvals, axis=1)
    gmag = np.linalg.norm(gvals, axis=1)
    return float(np.sum(fmag * norm_vals * gmag) * weight)


# ---------------------------------------------------------------------------
# C1  Exact Frobenius norm ||S_a||_F = 2/sqrt(Delta_a).
# ---------------------------------------------------------------------------
def check_c1_exact_frobenius_norm(rng):
    ok = True
    for _ in range(200):
        m = rng.uniform(0.2, 3.0)
        a = rng.uniform(0.02, 0.5)
        p = rng.uniform(-np.pi / a, np.pi / a, size=4)
        S = S_lattice(p, a, m)
        Delta = delta_lattice(p, a, m)
        # S S^dag = (1/Delta) 1_4  =>  ||S||_F^2 = 4/Delta  =>  ||S||_F = 2/sqrt(Delta)
        SSd = S @ S.conj().T
        ok &= np.allclose(SSd, IDENT4 / Delta, atol=1e-10)
        ok &= abs(np.linalg.norm(S, "fro") - 2.0 / np.sqrt(Delta)) < 1e-10
    # rung A's pointwise input, at the 4x4 matrix level: S_a(p) -> S(p) as a -> 0
    # at fixed physical p (used here as the named target, not re-derived).
    for _ in range(50):
        m = rng.uniform(0.5, 2.0)
        p = rng.uniform(-1.5, 1.5, size=4)
        d_coarse = np.linalg.norm(S_lattice(p, 0.1, m) - S_continuum(p, m), "fro")
        d_fine = np.linalg.norm(S_lattice(p, 0.05, m) - S_continuum(p, m), "fro")
        ok &= d_fine < d_coarse                  # converging pointwise (rung A)
        ok &= d_fine < 5e-2
    return bool(ok)


# ---------------------------------------------------------------------------
# C2  Jordan bound Delta_a >= m^2 + (2/pi)^2 |p|^2 on the BZ half, 0 violations;
#     and the a-independent envelope ||S_a||_F <= Phi(p) there.
# ---------------------------------------------------------------------------
def check_c2_jordan_bound(rng):
    ok = True
    N = 200000
    m = rng.uniform(0.2, 3.0, size=N)
    a = rng.uniform(0.02, 0.5, size=N)
    # sample on the BZ half |p_mu a| <= pi/2  <=>  |p_mu| <= pi/(2a), each axis.
    half = (np.pi / (2 * a))[:, None]
    p = rng.uniform(-1.0, 1.0, size=(N, 4)) * half
    s = np.sin(p * a[:, None]) / a[:, None]
    Delta = m * m + np.einsum("ni,ni->n", s, s)
    psq = np.einsum("ni,ni->n", p, p)
    bound = m * m + (2.0 / np.pi) ** 2 * psq
    # (1) Jordan: Delta_a >= m^2 + (2/pi)^2 |p|^2 on the BZ half, 0 violations.
    jordan_violations = int(np.sum(Delta < bound - 1e-9))
    # (2) a-independent envelope dominates the exact Frobenius norm on the half:
    #     ||S_a||_F = 2/sqrt(Delta_a) <= Phi(p) = 2/sqrt(bound).
    frob = 2.0 / np.sqrt(Delta)
    Phi = 2.0 / np.sqrt(bound)
    env_violations = int(np.sum(frob > Phi + 1e-9))
    ok &= (jordan_violations == 0) and (env_violations == 0)

    # (3) crude cap ||S_a||_F <= 2/m EVERYWHERE on the full BZ |p_mu| <= pi/a.
    pf = rng.uniform(-1.0, 1.0, size=(N, 4)) * (np.pi / a)[:, None]
    sf = np.sin(pf * a[:, None]) / a[:, None]
    Df = m * m + np.einsum("ni,ni->n", sf, sf)
    ok &= bool(np.all(2.0 / np.sqrt(Df) <= 2.0 / m + 1e-9))
    return bool(ok)


# ---------------------------------------------------------------------------
# C3  The integrand-vs-Phi L^1 distinction, BOTH ways.
# ---------------------------------------------------------------------------
def check_c3_integrand_vs_phi_L1(rng):
    """Exhibit:
      (a) int Phi d^4p DIVERGES: monotone increase without plateau as cutoff
          P grows (radial r^3 / sqrt(m^2 + c r^2) ~ r^2 for large r).
      (b) int |f| Phi |g| d^4p CONVERGES: plateaus as P and resolution grow.
      Also confirm the crude-cap integrand int |f| (2/m) |g| converges.
    """
    m = 1.0
    ok = True

    # (a) int Phi d^4p over a 4-ball of radius P, via the radial reduction
    #     int_{|p|<P} Phi d^4p = (vol of S^3) * int_0^P r^3 Phi(r) dr,
    #     vol(S^3) = 2 pi^2.  Phi(r) = 2/sqrt(m^2 + (2/pi)^2 r^2).
    def radial_phi_integral(P, nr=200000):
        r = np.linspace(0.0, P, nr)
        integrand = r ** 3 * 2.0 / np.sqrt(m * m + (2.0 / np.pi) ** 2 * r ** 2)
        return 2.0 * np.pi ** 2 * _trapz(integrand, r)

    cutoffs = [10.0, 20.0, 40.0, 80.0]
    Is = [radial_phi_integral(P) for P in cutoffs]
    incr = [Is[i] - Is[i - 1] for i in range(1, len(Is))]
    # divergence: the integral grows without bound and the INCREMENTS GROW
    # (integrand ~ r^2 at large r => integral ~ P^3, increments ~ P^3). A
    # convergent integral would have shrinking increments tending to 0; these
    # strictly increase, an unambiguous divergence witness.
    ok &= all(Is[i] > Is[i - 1] for i in range(1, len(Is)))
    ok &= all(incr[i] > incr[i - 1] for i in range(1, len(incr)))
    ok &= Is[-1] > 1e6                  # large and still climbing

    # (b) int |f| Phi |g| d^4p over [-P,P]^4 for sample Schwartz f, g. The
    #     Gaussian envelope decays to < 1e-9 well inside |p| = 14, so a fixed
    #     generous cutoff P = 14 captures the whole integral; we then certify
    #     the integral EXISTS / is finite by RESOLUTION refinement (the
    #     quadrature value is stable to high relative precision).
    width = 0.9
    fvec = np.array([1.0, 0.5j, -0.3, 0.2], dtype=complex)
    gvec = np.array([0.4, -0.2j, 0.7, -0.1], dtype=complex)
    fcen = np.array([0.3, -0.2, 0.1, 0.0])
    gcen = np.array([-0.1, 0.2, 0.0, 0.15])

    def phi_smear(P, n):
        pts, w = make_grid(n, P)
        f = schwartz_spinor(pts, width, fcen, fvec)
        g = schwartz_spinor(pts, width, gcen, gvec)
        return integrand_norm_smear(envelope_Phi_grid(pts, m), f, g, w)

    P0 = 14.0
    J_lo = phi_smear(P0, 28)
    J_hi = phi_smear(P0, 56)
    # finite, positive, and stable under resolution doubling (Cauchy in the
    # quadrature => the integral converges to a finite value).
    ok &= np.isfinite(J_hi) and (J_hi > 0.0)
    ok &= abs(J_hi - J_lo) / J_hi < 1e-2
    # extending the cutoff beyond P0 adds essentially nothing (tail < 1e-9):
    # contrast with Phi-without-test-function, which kept growing in part (a).
    J_ext = phi_smear(20.0, 80)
    ok &= abs(J_ext - J_hi) / J_hi < 1e-2

    # crude-cap integrand int |f| (2/m) |g| also finite (and >= the Phi one,
    # since Phi(p) <= 2/m everywhere).
    def cap_smear(P, n):
        pts, w = make_grid(n, P)
        f = schwartz_spinor(pts, width, fcen, fvec)
        g = schwartz_spinor(pts, width, gcen, gvec)
        return integrand_norm_smear(np.full(pts.shape[0], 2.0 / m), f, g, w)

    J_c = J_hi
    K_b = cap_smear(P0, 28)
    K_c = cap_smear(P0, 56)
    ok &= np.isfinite(K_c) and (abs(K_c - K_b) / K_c < 1e-2)
    ok &= K_c >= J_c - 1e-9           # cap integrand dominates the Phi integrand

    return bool(ok)


# ---------------------------------------------------------------------------
# Shared smearing setup for C4 / C5 / C6.
# ---------------------------------------------------------------------------
def _fixed_test_spinors(pts):
    width = 0.9
    fvec = np.array([1.0, 0.5j, -0.3, 0.2], dtype=complex)
    gvec = np.array([0.4, -0.2j, 0.7, -0.1], dtype=complex)
    fcen = np.array([0.3, -0.2, 0.1, 0.0])
    gcen = np.array([-0.1, 0.2, 0.0, 0.15])
    f = schwartz_spinor(pts, width, fcen, fvec)
    g = schwartz_spinor(pts, width, gcen, gvec)
    return f, g


# ---------------------------------------------------------------------------
# C4  Smeared pairing convergence <f, S_a g> -> <f, S g>, O(a^2) rate.
# ---------------------------------------------------------------------------
def check_c4_smeared_pairing_converges():
    m = 1.0
    P, n = 10.0, 40
    pts, w = make_grid(n, P)
    f, g = _fixed_test_spinors(pts)
    B0, Bmu = _bilinears(f, g)

    target = smeared_pairing_continuum(m, B0, Bmu, pts, w)

    a_seq = [0.4, 0.2, 0.1, 0.05]
    errs = []
    for a in a_seq:
        val = smeared_pairing_lattice(a, m, B0, Bmu, pts, w)
        errs.append(abs(val - target))

    ok = True
    # monotone decreasing error
    for i in range(1, len(errs)):
        ok &= errs[i] < errs[i - 1]
    # each a-halving cuts the error by >= ~3x (O(a^2) => factor ~4; allow slack)
    for i in range(1, len(errs)):
        ok &= errs[i - 1] / errs[i] >= 3.0
    # final error small
    ok &= errs[-1] < 1e-2
    return bool(ok), errs, target


# ---------------------------------------------------------------------------
# C5  Non-triviality control: a non-converging covariance -> non-converging
#     smeared pairing.
# ---------------------------------------------------------------------------
def check_c5_nonconverging_control():
    m = 1.0
    eps = 0.6  # FIXED O(1) mass offset; does NOT vanish as a -> 0
    P, n = 10.0, 40
    pts, w = make_grid(n, P)
    f, g = _fixed_test_spinors(pts)
    B0, Bmu = _bilinears(f, g)

    target = smeared_pairing_continuum(m, B0, Bmu, pts, w)

    a_seq = [0.4, 0.2, 0.1, 0.05]
    bad_errs = []
    good_errs = []
    for a in a_seq:
        # mis-scaled covariance S_a(.; m+eps): the bilinears are mass-independent,
        # so passing mass = m+eps to the lattice pairing IS S_lattice_misscaled.
        bad = smeared_pairing_lattice(a, m + eps, B0, Bmu, pts, w)
        good = smeared_pairing_lattice(a, m, B0, Bmu, pts, w)
        bad_errs.append(abs(bad - target))
        good_errs.append(abs(good - target))

    ok = True
    # bad sequence PLATEAUS (does not converge to target): per-halving ratio ~1,
    # i.e. NOT the >=3x O(a^2) decay the correct sequence shows.
    for i in range(1, len(bad_errs)):
        ratio = bad_errs[i - 1] / bad_errs[i]
        ok &= ratio < 1.5
    # bad error does NOT decay: total reduction across the whole sequence is
    # tiny (< 2x), whereas the correct sequence collapses by >> 10x.
    ok &= (bad_errs[0] / bad_errs[-1]) < 2.0
    ok &= (good_errs[0] / good_errs[-1]) > 10.0
    # bad error is bounded away from zero RELATIVE to the convergent sequence:
    # it is dramatically larger than the correct one at the finest a.
    ok &= bad_errs[-1] / good_errs[-1] > 50.0
    return bool(ok), bad_errs, good_errs


# ---------------------------------------------------------------------------
# C6  Dominated-convergence interchange, demonstrated directly.
# ---------------------------------------------------------------------------
def check_c6_dominated_convergence_interchange():
    """Show the pointwise integrand I_a(p) = fbar(p) S_a(p) g(p) is dominated
    uniformly in `a` by the L^1 function h(p) = |f(p)| Phi(p) |g(p)|, AND that
    int I_a -> int I_0 (lim and int commute). The domination is the hypothesis
    of dominated convergence; the convergence of the integrals is its
    conclusion."""
    m = 1.0
    P, n = 10.0, 40
    pts, w = make_grid(n, P)
    f, g = _fixed_test_spinors(pts)
    B0, Bmu = _bilinears(f, g)
    fmag = np.linalg.norm(f, axis=1)
    gmag = np.linalg.norm(g, axis=1)

    # The a-independent dominator h(p): |f| Phi(p) |g| on the BZ half, and the
    # crude cap |f| (2/m) |g| off it. Both are L^1 against Schwartz f, g.
    Phi = envelope_Phi_grid(pts, m)
    h_half = fmag * Phi * gmag
    h_cap = fmag * (2.0 / m) * gmag

    ok = True
    for a in [0.4, 0.2, 0.1, 0.05]:
        s = np.sin(pts * a) / a
        Delta = m * m + np.einsum("ni,ni->n", s, s)
        # pointwise integrand magnitude |fbar(p) S_a(p) g(p)|, vectorized
        num = m * B0 - 1j * np.einsum("ni,ni->n", s, Bmu)
        integrand_mag = np.abs(num / Delta)
        # Cauchy-Schwarz / submultiplicativity bound: |I_a| <= |f| ||S_a||_F |g|
        frob = 2.0 / np.sqrt(Delta)
        ub_op = fmag * frob * gmag
        ok &= bool(np.all(integrand_mag <= ub_op + 1e-9))
        # the a-independent dominator h: Phi on the half, crude cap off it
        on_half = np.all(np.abs(pts * a) <= np.pi / 2, axis=1)
        h = np.where(on_half, h_half, h_cap)
        ok &= bool(np.all(ub_op <= h + 1e-9))
        if not ok:
            break

    # conclusion: int I_a -> int I_0 (the smeared pairing converges)
    target = smeared_pairing_continuum(m, B0, Bmu, pts, w)
    val_fine = smeared_pairing_lattice(0.025, m, B0, Bmu, pts, w)
    ok &= abs(val_fine - target) < 5e-3

    # and the dominating integral int h is FINITE (L^1), using the crude cap
    # everywhere for a clean a-independent statement
    Ih = float(np.sum(h_cap) * w)
    ok &= np.isfinite(Ih) and Ih > 0.0
    return bool(ok)


def main():
    rng = np.random.default_rng(20260530)

    c4_ok, c4_errs, _ = check_c4_smeared_pairing_converges()
    c5_ok, c5_bad, c5_good = check_c5_nonconverging_control()

    checks = [
        ("C1_exact_frobenius_norm_2_over_sqrt_Delta", check_c1_exact_frobenius_norm(rng)),
        ("C2_jordan_bound_Delta_ge_m2_plus_4overpi2_psq", check_c2_jordan_bound(rng)),
        ("C3_integrand_L1_while_Phi_not_L1", check_c3_integrand_vs_phi_L1(rng)),
        ("C4_smeared_pairing_converges_Oa2", c4_ok),
        ("C5_nonconverging_covariance_control", c5_ok),
        ("C6_dominated_convergence_interchange", check_c6_dominated_convergence_interchange()),
    ]

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")

    print(f"  C4 smeared-pairing errors (a=0.4,0.2,0.1,0.05): "
          f"{', '.join(f'{e:.3e}' for e in c4_errs)}")
    print(f"  C5 control: mis-scaled errors {', '.join(f'{e:.3e}' for e in c5_bad)}; "
          f"correct {', '.join(f'{e:.3e}' for e in c5_good)}; "
          f"final ratio {c5_bad[-1]/c5_good[-1]:.1f}x")

    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
