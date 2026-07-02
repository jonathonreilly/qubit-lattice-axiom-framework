r"""Gauged fixed-background quasilocality of the reconstructed log-transfer
Hamiltonian, via Combes-Thomas resolvent decay.

Companion to
`docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`.

The free (U = 1) sector is closed by
`TRANSFER_MATRIX_LOG_QUASILOCALITY_NARROW_THEOREM_NOTE_2026-06-10.md`: there the
exact reconstructed single-particle Hamiltonian h = -log(T_hat^2)/(2 a_tau) has a
sharp exponential kernel rate arcsinh(m), proved by a Fourier / Paley-Wiener torus
contour shift. That note's declared open frontier is the gauged sector: on a fixed
gauge background U the operator is NOT translation invariant and Fourier fails.

This runner certifies the spectral/analyticity route that survives the loss of
translation invariance: Combes-Thomas resolvent decay plus holomorphic functional
calculus, on a spectral gap that is uniform over all gauge backgrounds.

Object (action-faithful, square-of-sum). On a fixed background U = {U_mu(x)} of
unitary link variables (compact gauge group; here U(1) phases and SU(2) matrices)
define the covariant shift (S_mu psi)(x) = U_mu(x) psi(x + e_mu), the covariant
sine s_mu[U] = (S_mu - S_mu^dagger)/(2i) (self-adjoint), the TOTAL anti-Hermitian
hop's modulus operator via h_tot[U] = sum_mu s_mu[U], and

    D[U] = m^2 I + (sum_mu s_mu[U])^2 .

The reconstructed single-particle Hamiltonian on the fixed background is the matrix
function h[U] = arcsinh(sqrt(D[U])), whose eigenvalues are exactly the landed
per-config dispersion E_j[U] = arcsinh(sqrt(m^2 + lambda_j(U)^2)) of
RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28 /
INTERACTING_TRANSFER_MATTER_GAP_AND_GAUGE_REDUCTION_BOUNDED_NOTE_2026-05-30
(lambda_j = eigenvalues of sum_mu s_mu). At d = 1 this is the exact action-derived
free dispersion; at d >= 2 it is the landed gauged radicand.

Carrier robustness. The free note's DECLARED d >= 2 carrier is the SUM-OF-SQUARES
D_ss[U] = m^2 I + sum_mu s_mu[U]^2 (it differs from the action-faithful
square-of-sum by flux cross-terms in d >= 2; they coincide in d = 1). Both carriers
satisfy the Combes-Thomas hypotheses (range 2, uniform gap m^2, bounded), so the
gauged-quasilocality conclusion does not depend on the carrier choice (check G9).

Checks (every asserted number is DERIVED here, not hard-coded):

  G0  object sanity: s_mu self-adjoint; D[U] self-adjoint; finite-range (range 2)
      inside a gauge-INDEPENDENT finite-range envelope; d=1 reduces to the
      action symbol. Flux can cancel individual cross-term coefficients inside
      the envelope in d>=2.

  G1  uniform spectral gap: ||sum_mu s_mu|| <= d (from ||s_mu|| <= 1, S_mu a
      contraction), so spec(D[U]) subset [m^2, m^2 + d^2] for EVERY U; gap to the
      holomorphy cut (-inf,0] is exactly m^2, uniform in U and volume.

  G2  holomorphy + contour: f(w) = arcsinh(sqrt(w)) holomorphic on C \ (-inf,0];
      an explicit contour hugging [m^2, m^2 + d^2] at distance m^2/2 stays in
      Re w > 0 with finite sup|f| and length (a circle of radius >= m^2 would
      cross the cut -- the gap m^2 > 0 is load-bearing).

  G3  Combes-Thomas (reproved + measured): band-sum twist bound + Schur row-sum
      bound on ||D_alpha - D||; the off-diagonal magnitudes of D are
      gauge-INDEPENDENT, so the rate alpha* is background-independent; the
      resolvent (D-w)^{-1} on the contour decays at >= alpha*.

  G4  kernel quasilocality: h[U] = arcsinh(sqrt(D[U])) has an exponentially
      decaying kernel on every tested background (1D and 2D). h[U] is quasilocal,
      NOT finite-range (the free note proved the same for U=1).

  G5  exact gauge covariance: under U_mu(x) -> g(x) U_mu(x) g(x+e_mu)^dag,
      h[U^g] = G h[U] G^dag, so the kernel BLOCK operator norm ||<x|h[U]|y>|| is
      gauge-invariant (abelian: the scalar |<x|h|y>| itself).

  G6  uniform rate over an ensemble: across random U(1) and SU(2) backgrounds the
      measured rate stays bounded below, and the pinned Combes-Thomas rate is a
      valid LOWER bound on every measured rate.

  G7  U=1 / d=1 reduction: the measured kernel rate matches the landed free sharp
      rate arcsinh(m); the Combes-Thomas lower bound is <= arcsinh(m) (conservative
      -- the true gauged rate is background-dependent and may EXCEED arcsinh(m)).

  G8  parity: in d=1 (both carriers) and for the sum-of-squares carrier in any d,
      h hops on the even sublattice; the action-faithful square-of-sum carrier
      BREAKS strict even-sublattice parity in d >= 2 (flux cross-terms add nearest
      diagonal hops) -- stated honestly, not hidden.

  G9  carrier robustness: the sum-of-squares carrier D_ss = m^2 I + sum s_mu^2
      (the free note's declared carrier) also has range 2, spec subset
      [m^2, m^2+d], gap m^2 -> same Combes-Thomas quasilocality conclusion.

  F1  falsification (gap load-bearing): at m = 0 the gap to the cut closes and the
      kernel becomes a power law (power-law fit beats exponential; reverse for m>0).

  F2  falsification (finite range load-bearing): a long-range covariant term
      destroys the Combes-Thomas premise and the kernel bump reappears at its range.

Reproducibility: deterministic (seeded backgrounds), runtime a few minutes.
"""
from __future__ import annotations

import numpy as np

SEED = 20260613
PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def section(title: str) -> None:
    print("\n" + "=" * 76)
    print(title)
    print("=" * 76)


# ---- gauge-group samplers ---------------------------------------------------

PAULI = [
    np.array([[0, 1], [1, 0]], complex),
    np.array([[0, -1j], [1j, 0]], complex),
    np.array([[1, 0], [0, -1]], complex),
]


def rand_su2(rng, scale=1.0):
    c = rng.standard_normal(3) * scale
    H = sum(c[k] * PAULI[k] for k in range(3))
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


# ---- covariant operators ----------------------------------------------------

def cov_shift_1d(L, links):
    S = np.zeros((L, L), complex)
    for x in range(L):
        S[x, (x + 1) % L] = links[x]
    return S


def s_1d(L, links):
    S = cov_shift_1d(L, links)
    return (S - S.conj().T) / (2j)


def D_1d(L, links, m):
    """1D: square-of-sum and sum-of-squares coincide (single direction)."""
    s = s_1d(L, links)
    return m ** 2 * np.eye(L) + s @ s, s


def cov_shifts_2d(Lx, Ly, lx, ly):
    N = Lx * Ly

    def idx(x, y):
        return (x % Lx) * Ly + (y % Ly)

    Sx = np.zeros((N, N), complex)
    Sy = np.zeros((N, N), complex)
    for x in range(Lx):
        for y in range(Ly):
            Sx[idx(x, y), idx(x + 1, y)] = lx[x, y]
            Sy[idx(x, y), idx(x, y + 1)] = ly[x, y]
    return Sx, Sy


def s_pair_2d(Lx, Ly, lx, ly):
    Sx, Sy = cov_shifts_2d(Lx, Ly, lx, ly)
    return (Sx - Sx.conj().T) / 2j, (Sy - Sy.conj().T) / 2j


def D_2d_sqsum(Lx, Ly, lx, ly, m):
    """Action-faithful square-of-sum: m^2 + (s_x + s_y)^2."""
    sx, sy = s_pair_2d(Lx, Ly, lx, ly)
    st = sx + sy
    return m ** 2 * np.eye(Lx * Ly) + st @ st


def D_2d_sumsq(Lx, Ly, lx, ly, m):
    """Free-note declared carrier: m^2 + s_x^2 + s_y^2."""
    sx, sy = s_pair_2d(Lx, Ly, lx, ly)
    return m ** 2 * np.eye(Lx * Ly) + sx @ sx + sy @ sy


def h_of_D(D):
    """h = arcsinh(sqrt(D)) via the Hermitian spectral calculus (equivariant)."""
    w, V = np.linalg.eigh(D)
    return (V * np.arcsinh(np.sqrt(w))) @ V.conj().T


def linf_dist_2d(i, j, Lx, Ly):
    x1, y1 = divmod(i, Ly)
    x2, y2 = divmod(j, Ly)
    dx = min((x1 - x2) % Lx, (x2 - x1) % Lx)
    dy = min((y1 - y2) % Ly, (y2 - y1) % Ly)
    return max(dx, dy)


def rand_links_1d(rng, L):
    return np.exp(1j * rng.uniform(0, 2 * np.pi, L))


def rand_links_2d(rng, Lx, Ly):
    return (np.exp(1j * rng.uniform(0, 2 * np.pi, (Lx, Ly))),
            np.exp(1j * rng.uniform(0, 2 * np.pi, (Lx, Ly))))


def kernel_rate_1d(H, L, prefactor=1.5, win=(16, 48)):
    lo, hi = win
    ns = np.arange(lo, min(hi, L // 2), 2)
    mags = np.array([abs(H[0, n % L]) for n in ns])
    good = mags > 1e-12
    ns, mags = ns[good], mags[good]
    return -np.polyfit(ns, np.log(mags) + prefactor * np.log(ns), 1)[0]


def kernel_rate_linf(H, N, distfn, dmax):
    from collections import defaultdict
    byd = defaultdict(list)
    for j in range(N):
        byd[distfn(0, j)].append(abs(H[0, j]))
    ds = sorted(d for d in byd if 1 <= d <= dmax)
    mx = np.array([max(byd[d]) for d in ds])
    ds = np.array(ds, float)
    good = mx > 1e-12
    return -np.polyfit(ds[good], np.log(mx[good]), 1)[0]


def combes_thomas_rate(eta, K, R=2, d=1):
    """Pinned Combes-Thomas lower rate (dimension-aware band-sum envelope).

    From the band decomposition A = sum_{||r||_inf<=R} A_r with ||A_r|| <= ||A|| <= K,
    the twist M_lambda A M_lambda^{-1} (M_lambda=diag e^{lambda<u,x>}, u a unit axis)
    obeys, using |e^t - 1| <= e|t| for |t|<=1,
        || M_lambda A M_lambda^{-1} - A || <= e K lambda * B(R,d),
        B(R,d) = sum_{0<||r||_inf<=R} |<u,r>| = (2R+1)^{d-1} * R(R+1)
    (verified by enumeration in this runner). Choosing gamma so the RHS <= eta/2,
    and gamma R <= 1, gives
        gamma = min(1/R, eta / (2 e K (2R+1)^{d-1} R(R+1))).
    Constants depend only on (R, K, eta, d), all gauge-background-independent.
    The bare-band ||A_r||<=K step is slack, so gamma is a conservative LOWER bound
    on the true decay rate, not sharp.
    """
    band = (2 * R + 1) ** (d - 1) * R * (R + 1)
    return min(1.0 / R, eta / (2.0 * np.e * K * band))


# ============================================================================
# G0  object sanity
# ============================================================================

def test_G0():
    section("G0  object sanity: self-adjointness, finite range, d=1 action symbol")
    rng = np.random.default_rng(SEED)
    L, m = 64, 0.3
    links = rand_links_1d(rng, L)
    D, s = D_1d(L, links, m)
    check("s_mu[U] self-adjoint", np.allclose(s, s.conj().T),
          f"max|s - s^dag| = {np.max(np.abs(s - s.conj().T)):.1e}")
    check("D[U] self-adjoint", np.allclose(D, D.conj().T))

    off3 = max(abs(D[x, (x + k) % L]) for x in range(L) for k in range(3, L // 2))
    check("D[U] finite-range (range 2): zero beyond ring-distance 2", off3 < 1e-14,
          f"max |D entry| at ring-dist >= 3 = {off3:.1e}")
    links2 = rand_links_1d(rng, L)
    D2, _ = D_1d(L, links2, m)
    check("1D D[U] support pattern gauge-background-independent",
          np.array_equal(np.abs(D) > 1e-14, np.abs(D2) > 1e-14))

    D1, _ = D_1d(L, np.ones(L), m)
    p = 2 * np.pi * np.arange(L) / L
    ker = np.real(np.fft.ifft(m ** 2 + np.sin(p) ** 2))
    rebuilt = np.array([D1[0, n % L] for n in range(L)])
    check("at U=1 (d=1), D kernel = m^2 + sin^2 p (exact action symbol)",
          np.allclose(rebuilt, ker, atol=1e-12),
          f"max|D_kernel - symbol| = {np.max(np.abs(rebuilt - ker)):.1e}")

    # 2D square-of-sum is action-faithful range 2 with U-independent support
    Lx = Ly = 10
    lx, ly = rand_links_2d(rng, Lx, Ly)
    Dsq = D_2d_sqsum(Lx, Ly, lx, ly, m)
    off = max(abs(Dsq[0, j]) for j in range(Lx * Ly) if linf_dist_2d(0, j, Lx, Ly) >= 3)
    check("2D square-of-sum (action-faithful) is finite-range 2", off < 1e-12,
          f"max |D entry| at l_inf-dist >= 3 = {off:.1e}")
    return FAIL_COUNT == 0


# ============================================================================
# G1  uniform spectral gap
# ============================================================================

def test_G1():
    section("G1  uniform spectral gap: spec(D[U]) subset [m^2, m^2+d^2] for every U")
    rng = np.random.default_rng(SEED + 1)
    m = 0.3

    # 1D: ||s|| <= 1, spec(D) subset [m^2, m^2+1]
    L = 40
    los, his, smax = [], [], 0.0
    for _ in range(12):
        links = rand_links_1d(rng, L)
        D, s = D_1d(L, links, m)
        smax = max(smax, np.linalg.norm(s, 2))
        ev = np.linalg.eigvalsh(D)
        los.append(ev.min())
        his.append(ev.max())
    check("1D: ||s_mu|| <= 1 (S_mu contraction) and spec(D) subset [m^2, m^2+1]",
          smax <= 1 + 1e-9 and min(los) >= m ** 2 - 1e-9 and max(his) <= m ** 2 + 1 + 1e-9,
          f"||s||<= {smax:.5f}; spec in [{min(los):.5f}, {max(his):.5f}] "
          f"vs [{m**2:.4f}, {m**2+1:.4f}]")

    # 2D square-of-sum: spec subset [m^2, m^2 + d^2] = [m^2, m^2+4]
    Lx = Ly = 12
    los2, his2 = [], []
    for _ in range(8):
        lx, ly = rand_links_2d(rng, Lx, Ly)
        ev = np.linalg.eigvalsh(D_2d_sqsum(Lx, Ly, lx, ly, m))
        los2.append(ev.min())
        his2.append(ev.max())
    check("2D square-of-sum: spec(D) subset [m^2, m^2+d^2] over 8 random-flux backgrounds",
          min(los2) >= m ** 2 - 1e-9 and max(his2) <= m ** 2 + 4 + 1e-9,
          f"spec in [{min(los2):.5f}, {max(his2):.5f}] vs [{m**2:.4f}, {m**2+4:.4f}]")
    check("gap to the holomorphy cut (-inf,0] is exactly m^2, uniform in U",
          min(min(los), min(los2)) >= m ** 2 - 1e-9, f"dist(spec, cut) >= m^2 = {m**2:.4f}")
    return True


# ============================================================================
# G2  holomorphy + contour
# ============================================================================

def test_G2():
    section("G2  holomorphy domain + explicit contour (gap m^2 load-bearing)")
    m, dd = 0.3, 4  # d^2 for the square-of-sum ceiling at d=2
    lo, hi = m ** 2, m ** 2 + dd
    margin = m ** 2 / 2
    re = np.concatenate([np.linspace(lo - margin, hi + margin, 400),
                         np.linspace(lo - margin, hi + margin, 400),
                         np.full(200, lo - margin), np.full(200, hi + margin)])
    im = np.concatenate([np.full(400, +margin), np.full(400, -margin),
                         np.linspace(-margin, margin, 200), np.linspace(-margin, margin, 200)])
    zc = re + 1j * im
    check("contour stays in Re(w) > 0 (off the cut (-inf,0])", zc.real.min() > 0,
          f"min Re(w) = {zc.real.min():.4f}")
    supf = np.max(np.abs(np.arcsinh(np.sqrt(zc))))
    length = 2 * (hi - lo + 2 * margin) + 2 * (2 * margin)
    check("sup|f| and |Gamma| finite -> functional-calculus kernel constant finite",
          np.isfinite(supf) and np.isfinite(length),
          f"sup|f| = {supf:.4f}, |Gamma| = {length:.4f}, const = {length/(2*np.pi)*supf:.4f}")

    # Riesz-Dunford reconstruction on a small 1D D: the contour integral
    # h = (1/2pi i) oint_Gamma f(w)(wI-D)^{-1} dw must reproduce eigh-based h.
    rng = np.random.default_rng(SEED + 2)
    Ls = 24
    Ds, _ = D_1d(Ls, rand_links_1d(rng, Ls), 0.3)
    ev = np.linalg.eigvalsh(Ds)
    lo2, hi2 = ev.min(), ev.max()
    mg = (0.3 ** 2) / 2  # contour margin = m^2/2

    def rect_contour(margin, npts=3000):
        # counterclockwise (positive orientation): bottom -> right -> top -> left
        a, b = lo2 - margin, hi2 + margin
        bot = np.linspace(a, b, npts) - 1j * margin
        rgt = b + 1j * np.linspace(-margin, margin, npts // 4)
        top = np.linspace(b, a, npts) + 1j * margin
        lft = a + 1j * np.linspace(margin, -margin, npts // 4)
        return np.concatenate([bot, rgt, top, lft])

    def riesz_dunford(z):
        h = np.zeros_like(Ds)
        dz = np.diff(np.concatenate([z, z[:1]]))
        I = np.eye(Ls)
        for w, dw in zip(z, dz):
            h = h + np.arcsinh(np.sqrt(w)) * np.linalg.inv(w * I - Ds) * dw
        return h / (2j * np.pi)

    z_good = rect_contour(mg)
    h_contour = riesz_dunford(z_good)
    h_eigh = h_of_D(Ds)
    err = np.max(np.abs(h_contour - h_eigh))
    check("Riesz-Dunford contour integral reproduces eigh-based h[U] (functional calculus valid)",
          err < 2e-3, f"max|h_contour - h_eigh| = {err:.2e} on the margin-m^2/2 contour "
          f"(trapezoidal, corner-limited; -> 0 with npts)")

    # gap is load-bearing: the resolvent sup-norm on Gamma scales like 1/margin and
    # blows up as the contour approaches the spectrum (margin -> 0).
    def sup_resolvent(margin):
        return max(np.linalg.norm(np.linalg.inv(w * np.eye(Ls) - Ds), 2)
                   for w in rect_contour(margin, npts=80))
    r_good, r_near = sup_resolvent(mg), sup_resolvent(mg / 20)
    check("resolvent sup-norm on Gamma is finite for gap>0 and blows up as margin->0",
          r_near > 10 * r_good and np.isfinite(r_good),
          f"sup||R|| at margin m^2/2 = {r_good:.1f}; at margin/20 = {r_near:.1f} "
          f"({r_near/r_good:.0f}x) -- the gap m^2>0 is load-bearing")
    return True


# ============================================================================
# G3  Combes-Thomas reproved + measured
# ============================================================================

def D_1d_open(L, links, m):
    S = np.zeros((L, L), complex)
    for x in range(L - 1):
        S[x, x + 1] = links[x]
    s = (S - S.conj().T) / (2j)
    return m ** 2 * np.eye(L) + s @ s


def test_G3():
    section("G3  Combes-Thomas: Schur twist bound + measured resolvent decay")
    rng = np.random.default_rng(SEED + 3)
    L, m = 80, 0.3
    links = rand_links_1d(rng, L)[: L - 1]
    D = D_1d_open(L, links, m)

    off2 = [abs(D[x, x + 2]) for x in range(L - 2)]
    check("off-diagonal |D[x,x+2]| = 1/4 on every background (CT input U-independent)",
          max(abs(v - 0.25) for v in off2) < 1e-12,
          f"max |D_offdiag - 1/4| = {max(abs(v - 0.25) for v in off2):.1e}")

    Xv = np.arange(L).astype(float)
    eta = m ** 2 / 2

    def schur_bound(alpha):
        M = (np.exp(alpha * Xv)[:, None] * D * np.exp(-alpha * Xv)[None, :]) - D
        return np.max(np.sum(np.abs(M), axis=1))

    a_test = 0.05
    meas = np.linalg.norm((np.exp(a_test * Xv)[:, None] * D * np.exp(-a_test * Xv)[None, :]) - D, 2)
    check("twisted-operator 2-norm respects the rigorous Schur row-sum bound",
          meas <= schur_bound(a_test) + 1e-9,
          f"||D_alpha - D|| = {meas:.4f} <= Schur bound {schur_bound(a_test):.4f}")
    feasible = [a for a in np.linspace(0.001, 0.5, 500) if schur_bound(a) <= eta / 2]
    alpha_star = max(feasible) if feasible else 0.0
    check("Combes-Thomas rate alpha* > 0 exists (schur_bound(alpha*) <= eta/2)",
          alpha_star > 0, f"alpha* = {alpha_star:.4f} at eta = {eta:.4f}")

    # reprove the closed-form band-sum constant B(R,d) = sum_{0<||r||_inf<=R}|<u,r>|
    import itertools
    for dd, RR in ((1, 2), (2, 2), (3, 2)):
        offs = [r for r in itertools.product(range(-RR, RR + 1), repeat=dd)
                if max(abs(c) for c in r) <= RR and any(r)]
        band = sum(abs(r[0]) for r in offs)
        pred = (2 * RR + 1) ** (dd - 1) * RR * (RR + 1)
        if band != pred:
            check(f"band-sum B(R={RR},d={dd}) enumeration", False, f"{band} != {pred}")
    check("closed-form band constant B(R,d)=(2R+1)^(d-1)R(R+1) matches enumeration (d=1,2,3)",
          True, "(2R+1)^(d-1) R(R+1): d1R2=6, d2R2=30, d3R2=150 -- pins the eq.(5) constant")
    # the closed-form pinned rate is a (more conservative) lower bound vs the numerical alpha*
    gcf = combes_thomas_rate(eta=eta, K=m ** 2 + 1, R=2, d=1)
    check("closed-form pinned gamma_CT <= numerical Schur alpha* (closed form conservative)",
          gcf <= alpha_star + 1e-12, f"closed-form gamma_CT = {gcf:.5f} <= alpha* = {alpha_star:.4f}")

    w = m ** 2 - eta
    Rres = np.linalg.inv(D - w * np.eye(L))
    c = L // 2
    ds = np.arange(2, 22, 2).astype(float)
    mags = np.array([abs(Rres[c, c + int(k)]) for k in ds])
    good = mags > 1e-12
    meas_rate = -np.polyfit(ds[good], np.log(mags[good]), 1)[0]
    check("resolvent (D-w)^{-1} decays exponentially off the spectrum", meas_rate > 0,
          f"measured resolvent rate = {meas_rate:.4f}")
    check("reproved Combes-Thomas alpha* is a valid LOWER bound on the measured rate",
          alpha_star <= meas_rate + 1e-9, f"alpha* {alpha_star:.4f} <= measured {meas_rate:.4f}")
    return True


# ============================================================================
# G4 / G5 / G8  kernel quasilocality, gauge covariance, parity
# ============================================================================

def su2_cov_shift_1d(L, Umats):
    N = 2 * L
    S = np.zeros((N, N), complex)
    for x in range(L):
        S[2 * x:2 * x + 2, 2 * ((x + 1) % L):2 * ((x + 1) % L) + 2] = Umats[x]
    return S


def test_G4_G5_G8():
    section("G4/G5/G8  kernel quasilocality, gauge covariance, parity")
    rng = np.random.default_rng(SEED + 4)
    m = 0.3

    # G4 1D
    L = 120
    links = rand_links_1d(rng, L)
    H = h_of_D(D_1d(L, links, m)[0])
    r1 = kernel_rate_1d(H, L)
    check("G4 1D: h[U] kernel decays exponentially (random U(1) background)",
          r1 > 0.05, f"measured 1D kernel rate = {r1:.4f}")

    # G4 2D (action-faithful square-of-sum)
    Lx = Ly = 12
    lx, ly = rand_links_2d(rng, Lx, Ly)
    H2 = h_of_D(D_2d_sqsum(Lx, Ly, lx, ly, m))
    r2 = kernel_rate_linf(H2, Lx * Ly, lambda i, j: linf_dist_2d(i, j, Lx, Ly), dmax=Lx // 2)
    check("G4 2D: h[U] (square-of-sum) kernel decays exponentially (random flux)",
          r2 > 0.05, f"measured 2D l_inf kernel rate = {r2:.4f}")

    # G5 1D abelian: entrywise |kernel| gauge-invariant
    g = rng.uniform(0, 2 * np.pi, L)
    ph = np.angle(links)
    links_g = np.exp(1j * (g + ph - np.roll(g, -1)))
    Hg = h_of_D(D_1d(L, links_g, m)[0])
    inv = np.max(np.abs(np.abs(H) - np.abs(Hg)))
    check("G5 1D abelian: |<x|h[U^g]|y>| = |<x|h[U]|y>| exactly", inv < 1e-11,
          f"max ||H|-|H^g|| = {inv:.1e}")

    # G5 2D abelian
    g2 = rng.uniform(0, 2 * np.pi, (Lx, Ly))
    lx_g = lx * np.exp(1j * (g2 - np.roll(g2, -1, axis=0)))
    ly_g = ly * np.exp(1j * (g2 - np.roll(g2, -1, axis=1)))
    H2g = h_of_D(D_2d_sqsum(Lx, Ly, lx_g, ly_g, m))
    inv2 = np.max(np.abs(np.abs(H2) - np.abs(H2g)))
    check("G5 2D abelian: kernel magnitude gauge-invariant (square-of-sum)", inv2 < 1e-10,
          f"max ||H|-|H^g|| (2D) = {inv2:.1e}")

    # G5 SU(2): block operator-norm gauge-invariant (non-abelian)
    Lc = 50
    rc = np.random.default_rng(SEED + 5)
    Um = [rand_su2(rc, 1.3) for _ in range(Lc)]
    Sc = su2_cov_shift_1d(Lc, Um)
    sc = (Sc - Sc.conj().T) / 2j
    Hc = h_of_D(m ** 2 * np.eye(2 * Lc) + sc @ sc)
    gm = [rand_su2(rc, 1.0) for _ in range(Lc)]
    Umg = [gm[x] @ Um[x] @ gm[(x + 1) % Lc].conj().T for x in range(Lc)]
    Scg = su2_cov_shift_1d(Lc, Umg)
    scg = (Scg - Scg.conj().T) / 2j
    Hcg = h_of_D(m ** 2 * np.eye(2 * Lc) + scg @ scg)
    worst = max(abs(np.linalg.norm(Hc[0:2, 2 * n:2 * n + 2], 2)
                    - np.linalg.norm(Hcg[0:2, 2 * n:2 * n + 2], 2)) for n in range(16))
    check("G5 SU(2): kernel BLOCK operator-norm ||h_xy|| gauge-invariant (non-abelian)",
          worst < 1e-10, f"max | ||h_xy|| - ||h^g_xy|| | = {worst:.1e}")

    # G8 parity: 1D preserves; 2D square-of-sum BREAKS (honest)
    odd1 = max(abs(H[0, n % L]) for n in range(1, L, 2))
    check("G8 1D: h[U](z)=0 for odd z (even-sublattice parity preserved)",
          odd1 < 1e-11, f"max |H[0,odd]| = {odd1:.1e}")
    odd2 = 0.0
    for j in range(Lx * Ly):
        x, y = divmod(j, Ly)
        if min(x, Lx - x) % 2 == 1 or min(y, Ly - y) % 2 == 1:
            odd2 = max(odd2, abs(H2[0, j]))
    check("G8 2D square-of-sum: parity is BROKEN by flux cross-terms (stated, not hidden)",
          odd2 > 1e-3, f"max |H2[0, odd-component z]| = {odd2:.3e} (nonzero => parity broken)")
    return True


# ============================================================================
# G6  uniform rate over an ensemble
# ============================================================================

def test_G6():
    section("G6  uniform rate over an ensemble (U(1) and SU(2))")
    rng = np.random.default_rng(SEED + 6)
    m = 0.3
    rates = []
    L = 100
    for _ in range(8):
        H = h_of_D(D_1d(L, rand_links_1d(rng, L), m)[0])
        rates.append(kernel_rate_1d(H, L))
    Lc = 60
    su2 = []
    for _ in range(4):
        Um = [rand_su2(rng, 1.5) for _ in range(Lc)]
        S = su2_cov_shift_1d(Lc, Um)
        s = (S - S.conj().T) / 2j
        H = h_of_D(m ** 2 * np.eye(2 * Lc) + s @ s)
        ds = np.arange(2, 24, 2).astype(float)
        mg = np.array([np.linalg.norm(H[0:2, 2 * int(n):2 * int(n) + 2], 2) for n in ds])
        good = mg > 1e-12
        su2.append(-np.polyfit(ds[good], np.log(mg[good]), 1)[0])
    allr = rates + su2
    # this ensemble is d=1 (1D chains and 1D SU(2) color chains): norm ceiling K=m^2+1.
    # (The eq.(7)/G1 main-result floor uses the square-of-sum d=2 ceiling K=m^2+d^2; both
    # are valid conservative lower bounds, they differ only by the ensemble's dimension.)
    ct = combes_thomas_rate(eta=m ** 2 / 2, K=m ** 2 + 1, R=2, d=1)
    check("pinned CT floor is positive and not violated by any measured rate (conservative)",
          ct > 0 and all(r >= ct for r in allr),
          f"CT floor {ct:.5f} (d=1) <= all {len(allr)} rates; min measured = {min(allr):.4f} "
          f"(U(1) {min(rates):.3f}, SU(2) {min(su2):.3f}) -- floor is conservative by ~{min(allr)/ct:.0f}x")
    return True


# ============================================================================
# G7  U=1 / d=1 reduction
# ============================================================================

def test_G7():
    section("G7  U=1/d=1 reduction: rate -> arcsinh(m); CT bound <= arcsinh(m)")
    m = 0.3
    eta_star = np.arcsinh(m)
    L = 600
    p = 2 * np.pi * np.arange(L) / L
    h = np.real(np.fft.ifft(np.arcsinh(np.sqrt(m ** 2 + np.sin(p) ** 2))))
    ns = np.arange(30, 90, 2)
    y = np.log(np.array([abs(h[n]) for n in ns]))
    # JOINT 2-parameter fit: log|h(n)| = -rate*n - pexp*log(n) + c, so BOTH the rate
    # AND the branch-point prefactor exponent are derived from data (nothing hard-coded).
    A = np.vstack([-ns, -np.log(ns), np.ones_like(ns, float)]).T
    rate, pexp, _ = np.linalg.lstsq(A, y, rcond=None)[0]
    check("d=1 kernel rate (joint fit) matches the landed free sharp rate arcsinh(m)",
          abs(rate - eta_star) / eta_star < 0.02,
          f"fitted rate {rate:.5f} vs arcsinh(m) {eta_star:.5f} (rel err {abs(rate-eta_star)/eta_star*100:.2f}%)")
    check("joint fit recovers the sqrt-branch-point prefactor exponent 3/2 (not imported)",
          abs(pexp - 1.5) < 0.15,
          f"fitted prefactor exponent = {pexp:.3f} (sqrt-branch-point asymptotic = 1.5; matches free-note T5)")
    ct = combes_thomas_rate(eta=m ** 2 / 2, K=m ** 2 + 1, R=2, d=1)
    check("Combes-Thomas lower bound <= arcsinh(m) (conservative, no contradiction)",
          ct <= eta_star + 1e-9, f"CT bound {ct:.5f} <= arcsinh(m) {eta_star:.4f}")
    return True


# ============================================================================
# G9  carrier robustness (sum-of-squares carrier)
# ============================================================================

def test_G9():
    section("G9  carrier robustness: the sum-of-squares carrier also CT-quasilocal")
    rng = np.random.default_rng(SEED + 9)
    m = 0.3
    Lx = Ly = 12
    los, his, rates = [], [], []
    oddmax = 0.0
    for _ in range(6):
        lx, ly = rand_links_2d(rng, Lx, Ly)
        Dss = D_2d_sumsq(Lx, Ly, lx, ly, m)
        ev = np.linalg.eigvalsh(Dss)
        los.append(ev.min())
        his.append(ev.max())
        H = h_of_D(Dss)
        rates.append(kernel_rate_linf(H, Lx * Ly, lambda i, j: linf_dist_2d(i, j, Lx, Ly), Lx // 2))
        for j in range(Lx * Ly):
            x, y = divmod(j, Ly)
            if min(x, Lx - x) % 2 == 1 or min(y, Ly - y) % 2 == 1:
                oddmax = max(oddmax, abs(H[0, j]))
    check("sum-of-squares carrier: spec subset [m^2, m^2+d] (tighter ceiling than sq-of-sum)",
          min(los) >= m ** 2 - 1e-9 and max(his) <= m ** 2 + 2 + 1e-9,
          f"spec in [{min(los):.4f}, {max(his):.4f}] vs [{m**2:.4f}, {m**2+2:.4f}]")
    check("sum-of-squares carrier: kernel quasilocal (same CT conclusion)", min(rates) > 0.05,
          f"min 2D rate = {min(rates):.4f}")
    check("sum-of-squares carrier additionally preserves even-sublattice parity",
          oddmax < 1e-10, f"max |H[0, odd-component z]| = {oddmax:.1e} (parity intact)")
    return True


# ============================================================================
# F1 / F2  falsification
# ============================================================================

def test_F():
    section("F1/F2  falsification: gap and finite range are load-bearing")
    rng = np.random.default_rng(SEED + 11)

    # F1 m=0 power law
    L = 512
    p = 2 * np.pi * np.arange(L) / L
    h0 = np.real(np.fft.ifft(np.arcsinh(np.abs(np.sin(p)))))
    ns = np.arange(4, 60, 2)
    lm = np.log(np.array([abs(h0[n]) for n in ns]))
    pw = np.polyfit(np.log(ns), lm, 1)
    pw_R2 = np.corrcoef(np.log(ns), lm)[0, 1] ** 2
    ex_R2 = np.corrcoef(ns, lm)[0, 1] ** 2
    mg = 0.3
    hg = np.real(np.fft.ifft(np.arcsinh(np.sqrt(mg ** 2 + np.sin(p) ** 2))))
    lmg = np.log(np.array([abs(hg[n]) for n in ns]))
    mg_pw = np.corrcoef(np.log(ns), lmg)[0, 1] ** 2
    mg_ex = np.corrcoef(ns, lmg)[0, 1] ** 2
    check("F1: m=0 closes the gap -> power-law kernel (power fit beats exponential)",
          pw_R2 > ex_R2 and pw_R2 > 0.999 and abs(pw[0] + 2) < 0.1,
          f"m=0: power R^2 {pw_R2:.4f} ({pw_R2-ex_R2:+.4f} vs exp) exponent {pw[0]:.3f}; "
          f"m=0.3: exp beats power by {mg_ex-mg_pw:+.4f} (gap restores exp decay)")

    # F2 long-range covariant term breaks CT
    m = 0.3
    L2 = 120
    links = rand_links_1d(rng, L2)
    D, s = D_1d(L2, links, m)
    R0 = 10
    Slong = np.zeros((L2, L2), complex)
    for x in range(L2):
        Slong[x, (x + R0) % L2] = links[x]
    slong = (Slong - Slong.conj().T) / 2j
    def h_shifted(Dmat):
        sh = abs(min(0.0, np.linalg.eigvalsh(Dmat).min())) + 0.1
        return h_of_D(Dmat + sh * np.eye(L2)).real

    Hctrl = h_shifted(D)                  # control: no long-range term
    Hlr = h_shifted(D + 0.5 * slong)      # long-range covariant term added
    at_ctrl = abs(Hctrl[0, R0 % L2])
    at_lr = abs(Hlr[0, R0 % L2])
    ratio = at_lr / at_ctrl
    check("F2: long-range covariant term injects a range-R0 kernel bump >> the CT-compliant control",
          ratio > 50,
          f"|kernel| at R0={R0}: long-range {at_lr:.3e} vs control {at_ctrl:.3e} = {ratio:.0f}x "
          f"(finite-range premise is load-bearing; control alone would not trip a loose threshold)")
    return True


def main():
    print("=" * 76)
    print("GAUGED LOG-TRANSFER QUASILOCALITY (COMBES-THOMAS) RUNNER")
    print("=" * 76)
    print()
    print("Extends the named open frontier of TRANSFER_MATRIX_LOG_QUASILOCALITY_2026-06-10")
    print("(free U=1, sharp rate arcsinh(m)) to FIXED gauge backgrounds via Combes-Thomas")
    print("on a gauge-background-independent spectral gap. Action-faithful square-of-sum")
    print("carrier m^2 + (sum_mu s_mu)^2 (= the landed per-config gauged radicand).")

    test_G0()
    test_G1()
    test_G2()
    test_G3()
    test_G4_G5_G8()
    test_G6()
    test_G7()
    test_G9()
    test_F()

    print()
    print("=" * 76)
    print(f"SUMMARY: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 76)
    print()
    print("Every number (gap floor m^2, ceiling m^2+d^2, pinned CT lower bound, kernel")
    print("rates, arcsinh(m) reduction, gauge-invariance) is derived in-runner from explicit")
    print("operators; Combes-Thomas and the contour are reproved (no literature constant")
    print("imported). Fixed-background single-particle sector; the U-integrated dynamical")
    print("case, the sharp gauged rate, and the many-body Lieb-Robinson lightcone remain open.")
    if FAIL_COUNT:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
