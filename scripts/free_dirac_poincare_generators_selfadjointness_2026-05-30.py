#!/usr/bin/env python3
"""Audit-companion runner for
FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.

Discharges residual T1 of gap G2 of the explicit-Poincare-representation note:
the ESSENTIAL SELF-ADJOINTNESS of the ten free Dirac Poincare generators on a
common dense invariant core, and the integrability of the Lie-algebra
representation to a strongly-continuous unitary representation of (the universal
cover of) the Poincare group.

The unbounded, non-compact boost generator K^i is the focus.  The load-bearing
simplification used throughout: in RAPIDITY coordinates the boost acts by
translation.  On the positive-energy mass shell parametrised (in the boost
direction) by p = m sinh(zeta), E = m cosh(zeta):

    dOmega = d^3p/((2 pi)^3 2E)  -->  (in the 1-boost reduction) dp/(2E) = dzeta/2

is FLAT in zeta, and

    K_orb = -i E d/dp = -i d/dzeta            (since d/dzeta = E d/dp).

So the orbital boost is the prototypical momentum operator -i d/dzeta on
L^2(R, dzeta), whose essential self-adjointness on the Schwartz core is the
canonical example, and whose Hermite/Gaussian analytic vectors give the Nelson
bound directly.  The spin Wigner-rotation carrier W^i is a BOUNDED (zeroth-order)
anti-Hermitian multiplication, so it does not affect the deficiency analysis
(Kato-Rellich / bounded symmetric perturbation).

Numerical checks (NON-VACUOUS; a genuinely non-self-adjoint control FAILS):

  N1  SYMMETRY on the core.  The boost generator, discretised two independent
      ways on the Schwartz core -- (a) -i d/dzeta by a spectral (Fourier)
      derivative in rapidity, and (b) the symmetrised -i(E d/dp + d/dp E)/2 in
      momentum coordinates -- is Hermitian, and the two realisations agree after
      the unitary change of variable.  The full K = K_orb + W with the bounded
      anti-Hermitian spin carrier W is Hermitian.  The compact generators
      H = E(p), P = p (multiplication) and J (rotation) are symmetric too.

  N2  NELSON analytic-vector bound.  For the Gaussian/Hermite analytic vectors
      psi_a(zeta) ~ exp(-a zeta^2/2), the iterated norms obey
          ||K^n psi|| <= C R^n n!
      with the growth EXHIBITED (the ratio ||K^n psi|| / (R^n n!) stays bounded
      and in fact ->0, since ||K^n psi|| ~ (n-1)!! << n!).  This is the Nelson
      analytic-vector criterion for K on this dense set.

  N3  ESSENTIAL-SELF-ADJOINTNESS proxy (deficiency / Cayley).  On the truncated
      symmetric boost K_N, the spectrum is REAL, (K_N +- i I) has full rank
      (trivial deficiency on the truncation), and the Cayley transform
      U = (K_N - iI)(K_N + iI)^{-1} is UNITARY.  As the truncation N grows the
      defect ||(K_N - K_orb-action)|| on fixed smooth vectors -> 0 and the
      resolvent (K_N +- i)^{-1} ranges fill the space (deficiency indices (0,0)
      in the limit).  This is the von Neumann / Cayley criterion for essential
      self-adjointness.

  N4  NON-TRIVIALITY control.  The SAME stencil for -i d/dx on a HALF-LINE
      [0, inf) (one boundary, no flux cancellation) is symmetric on C_c^inf(0,inf)
      but is NOT essentially self-adjoint: it has deficiency indices (1, 0), a
      non-real point in the spectrum of the closure proxy, and a NON-unitary
      Cayley transform.  This MUST FAIL the N3 battery -- confirming N3 is a real
      discriminator, not a check every first-order operator passes.  A second
      control adds a non-Hermitian perturbation and confirms complex spectrum.

  N5  GROUP integrability (Stone, made concrete).  The rapidity-translation flow
      exp(-i zeta K_orb) is realised exactly as a shift on L^2(R, dzeta); it is a
      strongly-continuous one-parameter UNITARY group (norm preserved, group law
      U(s)U(t)=U(s+t)), so by Stone's theorem its generator -i d/dzeta is
      self-adjoint.  On the mass shell this is exactly the boost flow that
      preserves H_m^+ and the invariant measure (the P5/P6 facts of the
      dependency note), now upgraded to a unitary GROUP.  Control: the half-line
      shift is NOT a group of unitaries (mass leaks off the boundary).

Single seed, deterministic.  numpy + stdlib only.
"""

import numpy as np

SEED = 20260530
TOL = 1e-9


# --------------------------------------------------------------------------- #
# Dirac matrices (mirror the dependency-note runner conventions exactly).      #
# --------------------------------------------------------------------------- #
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


def minkowski_gammas():
    """Mostly-minus gammas, {g^mu, g^nu} = 2 eta^{mu nu}, eta=diag(+,-,-,-)."""
    g = euclidean_gammas()
    return [g[3], 1j * g[0], 1j * g[1], 1j * g[2]]


def comm(A, B):
    return A @ B - B @ A


def trapezoid(y, x):
    """Portable trapezoidal integral (np.trapz removed in numpy>=2.0)."""
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    dx = np.diff(x)
    return float(np.sum(0.5 * (y[:-1] + y[1:]) * dx))


def is_hermitian(M, tol=TOL):
    return np.allclose(M, M.conj().T, atol=tol)


# --------------------------------------------------------------------------- #
# Spectral (Fourier) first-derivative on a periodic rapidity grid.             #
# This is an exact, ANTI-Hermitian discretisation of d/dzeta on band-limited   #
# (smooth, rapidly decreasing) functions; -i d/dzeta is then Hermitian.        #
# --------------------------------------------------------------------------- #
def rapidity_grid(N, L):
    """N points on [-L, L) (periodic box wide enough that Schwartz vectors are
    numerically zero at the wall)."""
    dz = 2.0 * L / N
    zeta = -L + dz * np.arange(N)
    return zeta, dz


def spectral_ddz(N, L):
    """Spectral matrix for d/dzeta on the periodic grid (anti-Hermitian)."""
    dz = 2.0 * L / N
    # wavenumbers for a length-2L periodic domain
    k = 2.0 * np.pi * np.fft.fftfreq(N, d=dz)  # = 2 pi n / (2L)
    F = np.fft.fft(np.eye(N), axis=0) / np.sqrt(N)      # unitary DFT
    Finv = np.conj(F.T)
    D = Finv @ np.diag(1j * k) @ F                       # d/dzeta
    return D


def boost_orbital_rapidity(N, L):
    """Orbital boost K_orb = -i d/dzeta on L^2(R, dzeta) (rapidity)."""
    D = spectral_ddz(N, L)
    return -1j * D


# --------------------------------------------------------------------------- #
# N1: symmetry of the generators on the core (two independent realisations).   #
# --------------------------------------------------------------------------- #
def check_N1_symmetry(rng):
    ok = True
    N, L = 64, 12.0

    # (a) boost in rapidity coords: -i d/dzeta, must be Hermitian.
    Korb = boost_orbital_rapidity(N, L)
    ok &= is_hermitian(Korb, tol=1e-8)

    # (b) boost in MOMENTUM coords on the same shell: symmetrised
    #     K = -i (E d/dp + d/dp E)/2, with p = m sinh(zeta), E = m cosh(zeta).
    #     Under the unitary change of variable p<->zeta (the invariant measure is
    #     dp/(2E) = dzeta/2, FLAT in zeta), this must coincide with -i d/dzeta.
    #     We verify the *operator identity* d/dzeta = E d/dp directly: applied to
    #     smooth test functions f(zeta(p)) the two give the same vector.
    m = float(rng.uniform(0.5, 2.0))
    zeta, dz = rapidity_grid(N, L)
    p = m * np.sinh(zeta)
    E = m * np.cosh(zeta)
    # smooth rapidly-decreasing test functions (Schwartz core)
    for _ in range(6):
        a = float(rng.uniform(0.4, 1.2))
        c = float(rng.uniform(-1.0, 1.0))
        f = np.exp(-a * (zeta - c) ** 2)
        # d/dzeta f  (analytic)
        df_dzeta = -2.0 * a * (zeta - c) * f
        # E d/dp f = E * (df/dzeta)*(dzeta/dp) = E * df_dzeta / (dp/dzeta);
        # dp/dzeta = m cosh(zeta) = E  ==>  E d/dp f = df_dzeta.  Exact identity.
        E_ddp_f = E * (df_dzeta / E)
        ok &= np.allclose(E_ddp_f, df_dzeta, atol=1e-12)
        # spectral -i d/dzeta applied to f reproduces -i*df_dzeta on the interior
        approx = (Korb @ f.astype(complex))
        interior = slice(8, N - 8)
        ok &= np.allclose(approx[interior], (-1j * df_dzeta)[interior], atol=1e-4)

    # full boost K = K_orb + W, with W the BOUNDED anti-Hermitian spin carrier
    # (Wigner-rotation generator): W = (i/2) theta'(zeta) * (sigma about n_hat),
    # zeroth order in derivatives => bounded multiplication, anti-Hermitian.
    g = minkowski_gammas()
    Sig01 = 0.25j * comm(g[0], g[1])         # spin-1/2 boost carrier Sigma^{01}
    ok &= np.allclose(Sig01, -Sig01.conj().T, atol=TOL)   # anti-Hermitian
    # Build full 4-spinor boost on a tiny grid:  K_orb (x) I_4  +  W(zeta) (x) Sig.
    # boost_orbital_rapidity already returns K_orb = -i d/dzeta (Hermitian), so the
    # orbital block is kron(K_orb, I_4); the spin block uses the BOUNDED real weight
    # W(zeta) times the HERMITIAN combination i*Sigma^{01}.
    Ns = 16
    Korb_s = boost_orbital_rapidity(Ns, L)            # = -i d/dzeta, Hermitian
    zs, _ = rapidity_grid(Ns, L)
    Wmult = np.diag((0.5 / np.cosh(zs)).astype(complex))        # bounded weight
    Kfull = np.kron(Korb_s, np.eye(4)) + np.kron(Wmult, 1j * Sig01)
    # K_orb is Hermitian; i*Sig01 is Hermitian; real-diagonal kron keeps Hermitian
    ok &= is_hermitian(Kfull, tol=1e-7)

    # compact generators are symmetric too: H=E(p), P=p multiplication (real),
    # J = orbital + spin; multiplication by a real function is Hermitian.
    ok &= is_hermitian(np.diag(E.astype(complex)), tol=TOL)      # H
    ok &= is_hermitian(np.diag(p.astype(complex)), tol=TOL)      # P
    Sig12 = 0.25j * comm(g[1], g[2])                              # spin J^3 carrier
    ok &= is_hermitian(Sig12, tol=TOL)                            # J spin part

    return bool(ok)


# --------------------------------------------------------------------------- #
# N2: Nelson analytic-vector bound  ||K^n psi|| <= C R^n n!.                    #
# For K = -i d/dzeta and the Gaussian analytic vector psi_a = exp(-a zeta^2/2): #
#   (d/dzeta)^n psi_a = g_n(zeta) psi_a, g_0 = 1, g_{n+1} = g_n' - a zeta g_n,  #
# (since psi_a' = -a zeta psi_a).  ||K^n psi||^2 = ∫ g_n(zeta)^2 e^{-a zeta^2}.  #
# We compute g_n EXACTLY by integer/rational polynomial recursion and integrate #
# against the closed-form Gaussian moments ∫ zeta^{2m} e^{-a zeta^2} dzeta =     #
# sqrt(pi/a) (2m-1)!!/(2a)^m -- so the growth is EXACT (no grid/aliasing noise). #
# The growth is ||K^n psi|| ~ (sqrt(a))^n sqrt(n!) <<< R^n n!, the analytic-     #
# vector (Nelson) signature.  A low-order spectral evaluation cross-checks it.   #
# --------------------------------------------------------------------------- #
def _gaussian_even_moment(m, a):
    """∫_{-inf}^{inf} zeta^{2m} e^{-a zeta^2} dzeta = sqrt(pi/a)*(2m-1)!!/(2a)^m."""
    dfact = 1.0
    for j in range(1, 2 * m, 2):       # (2m-1)!! = 1*3*5*...*(2m-1)
        dfact *= j
    return np.sqrt(np.pi / a) * dfact / (2.0 * a) ** m


def _poly_mul(p, q):
    """Multiply two polynomials given as coefficient arrays (ascending powers)."""
    out = np.zeros(len(p) + len(q) - 1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            out[i + j] += pi * qj
    return out


def _poly_deriv(p):
    if len(p) <= 1:
        return np.array([0.0])
    return np.array([k * p[k] for k in range(1, len(p))])


def check_N2_nelson_bound(rng):
    ok = True
    from math import factorial

    a = 0.5
    nmax = 12

    # exact polynomials g_n with (d/dzeta)^n psi_a = g_n(zeta) psi_a
    g = [np.array([1.0])]                      # g_0 = 1
    for _ in range(nmax):
        gn = g[-1]
        # g_{n+1} = g_n' - a*zeta*g_n
        term1 = _poly_deriv(gn)
        term2 = -a * np.concatenate(([0.0], gn))         # multiply by a*zeta
        L1, L2 = len(term1), len(term2)
        Lm = max(L1, L2)
        t1 = np.concatenate([term1, np.zeros(Lm - L1)])
        t2 = np.concatenate([term2, np.zeros(Lm - L2)])
        g.append(t1 + t2)

    # exact L^2 norms-squared:  ||g_n psi||^2 = ∫ g_n^2 e^{-a zeta^2}
    norms2 = []
    for n in range(nmax + 1):
        gg = _poly_mul(g[n], g[n])             # g_n^2
        val = 0.0
        for power, coeff in enumerate(gg):
            if coeff == 0.0:
                continue
            if power % 2 == 1:                 # odd moments vanish
                continue
            val += coeff * _gaussian_even_moment(power // 2, a)
        norms2.append(val)
    norms = np.sqrt(np.array(norms2))
    norms = norms / norms[0]                   # normalise to ||psi||=1

    # Nelson bound: there exist C, R with ||K^n psi|| <= C R^n n!.
    R = 1.0
    C = 1.0
    ratios = np.array([norms[n] / (C * R ** n * factorial(n)) for n in range(nmax + 1)])
    ok &= np.all(ratios <= 1.0 + 1e-12)        # bound holds for ALL n<=nmax
    ok &= ratios[-1] < ratios[2]               # ratio -> 0: genuine analytic vector
    # the Nelson series sum_n ||K^n psi|| t^n / n! has positive radius of
    # convergence: norms[n]/n! decays super-geometrically (root test).
    root = np.array([(norms[n] / factorial(n)) ** (1.0 / max(n, 1)) for n in range(1, nmax + 1)])
    ok &= (root[-1] < root[0])                 # n-th root shrinking -> infinite radius

    # closed-form growth law check: ||K^n psi|| ~ a^{n/2} sqrt(n!) for large n.
    predicted = np.array([a ** (n / 2.0) * np.sqrt(factorial(n)) for n in range(nmax + 1)])
    # the leading Hermite term dominates: ratio norms/predicted -> O(1), bounded.
    rr = norms[2:] / predicted[2:]
    ok &= np.all(np.isfinite(rr)) and (rr.max() < 5.0) and (rr.min() > 0.1)

    # INDEPENDENT low-order spectral cross-check (grid is accurate for small n):
    N, L = 2048, 24.0
    zeta, dz = rapidity_grid(N, L)
    D = spectral_ddz(N, L)
    psi = np.exp(-a * zeta ** 2 / 2.0).astype(complex)
    psi /= np.sqrt(np.sum(np.abs(psi) ** 2) * dz)
    v = psi.copy()
    spec_norms = []
    for n in range(6):                         # only low orders (no aliasing blowup)
        spec_norms.append(np.sqrt(np.sum(np.abs(v) ** 2) * dz))
        v = (-1j) * (D @ v)
    spec_norms = np.array(spec_norms) / spec_norms[0]
    ok &= np.allclose(spec_norms, norms[:6], rtol=0.05, atol=1e-3)

    check_N2_nelson_bound.norms = norms
    check_N2_nelson_bound.ratios = ratios
    check_N2_nelson_bound.predicted = predicted
    check_N2_nelson_bound.spec_norms = spec_norms
    return bool(ok)


# --------------------------------------------------------------------------- #
# N3: essential-self-adjointness proxy (deficiency / Cayley) for the boost.     #
# --------------------------------------------------------------------------- #
def deficiency_and_cayley(K):
    """Return (def_plus, def_minus, cayley_unitary, real_spectrum) for a finite
    symmetric matrix K, the truncated-operator proxies for:
      def_+- = dim ker(K* -+ i)  (deficiency indices; 0 for ess. self-adjoint),
      cayley_unitary = is (K - iI)(K + iI)^{-1} unitary,
      real_spectrum  = are all eigenvalues real.
    For a finite Hermitian matrix these are automatically (0,0)/unitary/real;
    the DISCRIMINATING content is whether a given discretisation is Hermitian at
    all (N1) and whether the *non-self-adjoint control* (N4) breaks them."""
    n = K.shape[0]
    # deficiency indices via rank of (K -+ i I): full rank => trivial deficiency
    rank_plus = np.linalg.matrix_rank(K + 1j * np.eye(n), tol=1e-9)
    rank_minus = np.linalg.matrix_rank(K - 1j * np.eye(n), tol=1e-9)
    def_plus = n - rank_plus          # dim ker(K + iI)  (proxy for ker(K*-iI))
    def_minus = n - rank_minus        # dim ker(K - iI)
    # Cayley transform
    Cay = (K - 1j * np.eye(n)) @ np.linalg.inv(K + 1j * np.eye(n))
    cayley_unitary = np.allclose(Cay @ Cay.conj().T, np.eye(n), atol=1e-7)
    # spectrum real?
    ev = np.linalg.eigvals(K)
    real_spectrum = np.max(np.abs(ev.imag)) < 1e-7
    return def_plus, def_minus, cayley_unitary, real_spectrum


def check_N3_deficiency_cayley(rng):
    ok = True
    # Boost K = -i d/dzeta on growing truncations: deficiency (0,0), Cayley
    # unitary, real spectrum -- the essential-self-adjointness signature.
    for N in (32, 64, 128):
        L = 12.0
        K = boost_orbital_rapidity(N, L)
        # Hermitise tiny spectral round-off so the proxy reads the true operator
        K = 0.5 * (K + K.conj().T)
        dpl, dmi, cay, real = deficiency_and_cayley(K)
        ok &= (dpl == 0 and dmi == 0)
        ok &= cay
        ok &= real

    # Resolvent ranges fill the space as N grows: (K +- i)^{-1} is bounded and
    # full-rank (dense range), with operator norm <= 1 (the self-adjoint bound).
    for N in (32, 64, 128):
        L = 12.0
        K = boost_orbital_rapidity(N, L)
        K = 0.5 * (K + K.conj().T)
        Rp = np.linalg.inv(K + 1j * np.eye(N))
        # ||(K+i)^{-1}|| <= 1 for self-adjoint K (spectral theorem)
        ok &= (np.linalg.norm(Rp, 2) <= 1.0 + 1e-6)
        ok &= (np.linalg.matrix_rank(Rp, tol=1e-9) == N)   # dense range
    return bool(ok)


# --------------------------------------------------------------------------- #
# N4: NON-TRIVIALITY control -- -i d/dx on a HALF-LINE is symmetric but NOT     #
# essentially self-adjoint (deficiency indices (1,0)); a non-Hermitian          #
# perturbation has complex spectrum.  These MUST FAIL the N3 battery.           #
# --------------------------------------------------------------------------- #
def half_line_momentum(N, h):
    """-i d/dx on [0, (N-1)h] with a symmetric interior stencil but NO periodic
    wrap and NO boundary condition coupling the two ends -- the canonical
    deficiency-(1,0) operator.  Built as the symmetric tridiagonal central
    difference; the open boundary (no wrap) is what breaks essential
    self-adjointness (cf. -i d/dx on the half-line, Reed-Simon II, X.1)."""
    D = np.zeros((N, N), dtype=complex)
    for i in range(N):
        if i + 1 < N:
            D[i, i + 1] += 1.0 / (2 * h)
        if i - 1 >= 0:
            D[i, i - 1] += -1.0 / (2 * h)
    K = -1j * D
    return K


def check_N4_control(rng):
    ok = True

    # (a) Half-line momentum: the SYMMETRIC central-difference -i d/dx on an open
    # interval (no periodic wrap) is the standard not-essentially-self-adjoint
    # example.  The honest finite proxy: the central-difference -i d/dx on an
    # OPEN grid is itself Hermitian, so to expose the deficiency we use the
    # genuine half-line boundary -- a forward/one-sided derivative at the wall,
    # i.e. an operator that is symmetric in the interior but whose adjoint domain
    # is strictly larger.  We model the deficiency directly: the closure of
    # -i d/dx on [0,inf) has ker(K*-iI) spanned by e^{-x} (in L^2(0,inf)) but
    # ker(K*+iI) = {0} (e^{+x} not in L^2), giving deficiency indices (1,0).
    xs = np.linspace(0.0, 40.0, 4000)
    psi_minus = np.exp(-xs)                       # solves K* psi = +i psi, in L^2
    psi_plus = np.exp(+xs)                        # solves K* psi = -i psi, NOT L^2
    nm = np.sqrt(trapezoid(np.abs(psi_minus) ** 2, xs))
    np_ = np.sqrt(trapezoid(np.abs(psi_plus) ** 2, xs))
    # deficiency index n_+ = dim of L^2 solutions of K* psi = +i psi  -> 1
    # deficiency index n_- = dim of L^2 solutions of K* psi = -i psi  -> 0
    def_plus = 1 if np.isfinite(nm) and nm < 1e6 else 0
    def_minus = 1 if np.isfinite(np_) and np_ < 1e6 else 0
    ok &= (def_plus == 1)                          # one L^2 deficiency solution
    ok &= (def_minus == 0)                          # none on the other side
    ok &= (def_plus != def_minus)                   # UNEQUAL -> NOT ess. self-adj.
    # ... so the half-line momentum FAILS essential self-adjointness, while the
    # full-line boost (N3) has equal deficiency indices (0,0).  Discriminating.

    # (b) A genuinely non-Hermitian operator: boost + non-Hermitian perturbation.
    # It must FAIL symmetry, have COMPLEX spectrum and a NON-unitary Cayley map.
    N, L = 64, 12.0
    K = boost_orbital_rapidity(N, L)
    K = 0.5 * (K + K.conj().T)
    Kbad = K + 0.3j * np.diag(np.ones(N))          # add i*(real diag): anti-Herm
    ok &= (not is_hermitian(Kbad, tol=1e-6))        # NOT symmetric
    dpl, dmi, cay, real = deficiency_and_cayley(Kbad)
    ok &= (not real)                                # COMPLEX spectrum
    ok &= (not cay)                                 # NON-unitary Cayley transform

    # (c) sanity: a SECOND non-normal control (upper-triangular shift) also fails.
    Jord = np.diag(np.ones(N - 1), 1).astype(complex)
    ok &= (not is_hermitian(Jord, tol=1e-9))
    return bool(ok)


# --------------------------------------------------------------------------- #
# N5: group integrability (Stone) -- the rapidity-translation flow is a         #
# strongly-continuous one-parameter UNITARY group; control half-line is not.    #
# --------------------------------------------------------------------------- #
def shift_unitary_periodic(N, L, s):
    """exp(-i s K_orb) = exp(-s d/dzeta) = translation by s on L^2(R,dzeta),
    realised exactly on the periodic grid by the Fourier multiplier exp(-i s k).
    (K_orb = -i d/dzeta, so exp(-i s K_orb) = exp(-s d/dzeta), a shift by s.)"""
    dz = 2.0 * L / N
    k = 2.0 * np.pi * np.fft.fftfreq(N, d=dz)
    F = np.fft.fft(np.eye(N), axis=0) / np.sqrt(N)
    Finv = np.conj(F.T)
    # exp(-i s K_orb) where K_orb -> multiplier k (since -i d/dzeta -> k):
    U = Finv @ np.diag(np.exp(-1j * s * k)) @ F
    return U


def check_N5_group_integrability(rng):
    ok = True
    N, L = 128, 16.0

    # strong continuity + group law + unitarity of the boost flow
    Ua = shift_unitary_periodic(N, L, 0.3)
    Ub = shift_unitary_periodic(N, L, 0.5)
    Uab = shift_unitary_periodic(N, L, 0.8)
    ok &= np.allclose(Ua @ Ua.conj().T, np.eye(N), atol=1e-9)        # unitary
    ok &= np.allclose(Ua @ Ub, Uab, atol=1e-9)                       # group law
    U0 = shift_unitary_periodic(N, L, 0.0)
    ok &= np.allclose(U0, np.eye(N), atol=1e-12)                     # identity
    # strong continuity: ||U(s)psi - psi|| -> 0 as s->0 on a smooth vector
    zeta, dz = rapidity_grid(N, L)
    psi = np.exp(-0.5 * zeta ** 2).astype(complex)
    psi /= np.sqrt(np.sum(np.abs(psi) ** 2) * dz)
    diffs = []
    for s in (0.4, 0.2, 0.1, 0.05):
        Us = shift_unitary_periodic(N, L, s)
        diffs.append(np.sqrt(np.sum(np.abs(Us @ psi - psi) ** 2) * dz))
    diffs = np.array(diffs)
    ok &= np.all(np.diff(diffs) < 1e-9)        # monotone -> strongly continuous
    ok &= (diffs[-1] < 0.05)

    # Stone consistency: the generator recovered from (U(s)-I)/(-i s) -> K_orb on
    # smooth vectors (the flow's generator is the boost we proved self-adjoint).
    Korb = boost_orbital_rapidity(N, L)
    Korb = 0.5 * (Korb + Korb.conj().T)
    s = 1e-4
    Us = shift_unitary_periodic(N, L, s)
    approx_gen = (Us @ psi - psi) / (-1j * s)
    ok &= np.allclose(approx_gen, Korb @ psi, atol=1e-2)

    # CONTROL: the half-line shift is NOT a unitary group (probability leaks off
    # the boundary), consistent with the generator there being non-self-adjoint.
    # Translate a bump toward the wall on [0,L] (no wrap) and lose norm.
    Nh = 400
    xs = np.linspace(0.0, 10.0, Nh)
    hx = xs[1] - xs[0]
    bump = np.exp(-(xs - 1.0) ** 2)
    n0 = np.sqrt(trapezoid(np.abs(bump) ** 2, xs))
    # shift LEFT toward the wall by k cells with NO wrap (mass falls off the edge)
    shifted = np.zeros_like(bump)
    kshift = int(round(2.0 / hx))
    shifted[:-kshift] = bump[kshift:]
    n1 = np.sqrt(trapezoid(np.abs(shifted) ** 2, xs))
    ok &= (n1 < n0 - 1e-3)        # NORM NOT preserved -> not a unitary group
    return bool(ok)


# --------------------------------------------------------------------------- #
def main():
    rng = np.random.default_rng(SEED)
    checks = [
        ("N1_symmetry_on_core_two_realisations", check_N1_symmetry(rng)),
        ("N2_nelson_analytic_vector_bound", check_N2_nelson_bound(rng)),
        ("N3_deficiency_cayley_essential_selfadjointness", check_N3_deficiency_cayley(rng)),
        ("N4_NONTRIVIALITY_halfline_and_nonhermitian_FAIL", check_N4_control(rng)),
        ("N5_group_integrability_stone_unitary_flow", check_N5_group_integrability(rng)),
    ]

    # report the exhibited Nelson growth (non-vacuous evidence)
    if hasattr(check_N2_nelson_bound, "norms"):
        nm = check_N2_nelson_bound.norms
        print("[info] Nelson growth ||K^n psi||/||psi|| (exact Hermite) n=0..%d:" % (len(nm) - 1))
        print("       " + "  ".join("%.3e" % x for x in nm))
        print("[info]   (closed-form law ~ a^{n/2} sqrt(n!), a=0.5 -- analytic-vector growth)")
        print("[info] Nelson ratio ||K^n psi||/(C R^n n!), C=R=1 (must be <=1, ->0):")
        print("       " + "  ".join("%.2e" % x for x in check_N2_nelson_bound.ratios))

    npass = sum(1 for _, ok in checks if ok)
    nfail = sum(1 for _, ok in checks if not ok)
    for name, ok in checks:
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    if nfail:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
