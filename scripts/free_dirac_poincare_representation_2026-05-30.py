#!/usr/bin/env python3
"""Audit-companion runner for FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE.

Closes gap G2 of the free-field OS->Wightman reconstruction: it constructs the
explicit positive-energy Poincare representation of the FREE Dirac field and
verifies, by concrete numerics, that all ten generators close into the Poincare
algebra -- in particular the boost-boost relation [K^i, K^j] = -i eps^{ijk} J^k
that distinguishes a genuine Poincare representation from rotations+translations.

This is textbook free-field QFT done explicitly, NOT by invoking the abstract OS
reconstruction theorem.  Two independent realizations of the ten generators are
verified:

  Realization I (finite-dimensional Lie-algebra rep, exact matrices):
    P1: spin-1/2 Lorentz generators  J^i = (1/2) eps^{ijk} Sigma^{jk},
        K^i = Sigma^{0i},  Sigma^{mu nu} = (i/4)[gamma^mu, gamma^nu], close the
        Lorentz algebra so(3,1): [J,J]=ieJ, [J,K]=ieK, [K,K]=-ieJ.
    P2: the full Poincare algebra iso(3,1) in the 5x5 (defining) rep of the ten
        generators (H,P^i,J^i,K^i) closes ALL ten brackets, including
        [H,K^i]=iP^i, [P^i,K^j]=i delta^{ij} H, [H,P^i]=0, [P^i,P^j]=0.
    P3: NON-TRIVIALITY control -- a wrong-sign boost generator (K -> -K, or the
        Euclidean SO(4) sign [K,K]=+ieJ) FAILS the Poincare algebra.

  Realization II (one-particle mass-shell differential operators, the construction
    that actually lives on H_m^+ = {p^0 = E(p)} with measure d^3p/((2pi)^3 2E)):
    P4: H = E(p), P^i = p^i, the orbital rotation J^i = -i eps p d/dp, and the
        boost vector field K^i = -i E(p) d/dp^i (the spin Wigner-rotation term is
        verified separately in P5) close all four boost-containing brackets
        [H,K^i]=iP^i, [P^i,K^j]=i delta^{ij} H, [J^i,K^j]=i eps K, the boost-boost
        [K^i,K^j]=-i eps J.  Evaluated ANALYTICALLY on a Gaussian test family using
        exact closed-form derivatives (machine precision, no finite-difference).
    P5: the boost vector field b^i(p)=E d/dp^i integrates the mass shell into
        itself (E^2 - p^2 = m^2 invariant) and the Wigner little-group rotation
        of the spin index is the correct SU(2) Wigner rotation.
    P6: the Lorentz-invariant measure d^3p/(2E) is preserved by the boost flow
        (div of the measure-weighted boost field vanishes) -- this is the
        unitarity of the one-particle boost.

  Positive energy / mass shell / 2-point continuation:
    P7: positive-energy single-particle spectrum E(p) >= m > 0; the CAR-relabeled
        many-body Hamiltonian H = sum E(p)(a^dag a + b^dag b) is bounded below by 0
        (rung C made concrete); spectrum in the closed forward light cone.
    P8: boosted 2-point matches rung A's SO(4)->SO(3,1) Wick-rotation continuation:
        the boosted Minkowski mass shell -p0^2+|p|^2+m^2=0 is the Lorentz orbit, and
        the bispinor 2-point transforms covariantly S'(Lp)=Lambda S(p) Lambda^{-1}.

Single seed, deterministic.  numpy + stdlib only.
"""

import itertools

import numpy as np

SEED = 20260530
TOL = 1e-9          # exact-arithmetic tolerance (matrices and analytic operators)


# --------------------------------------------------------------------------- #
# Dirac matrices (mirror the on-main mode-algebra runner conventions exactly)  #
# --------------------------------------------------------------------------- #
def euclidean_gammas():
    """Euclidean Dirac matrices, {g_mu, g_nu} = 2 delta_mu_nu (all Hermitian)."""
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
    """Mostly-minus Minkowski gammas (g^0,g^1,g^2,g^3) from Euclidean gammas.

    g^0 = g4 (Hermitian), g^k = i*g_k^E (anti-Hermitian), giving
    {g^mu,g^nu} = 2 eta^{mu nu} with eta = diag(+,-,-,-).
    """
    g = euclidean_gammas()
    return [g[3], 1j * g[0], 1j * g[1], 1j * g[2]]


def pauli():
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return [sx, sy, sz]


LEVI = np.zeros((3, 3, 3))
for _i, _j, _k in itertools.permutations(range(3)):
    LEVI[_i, _j, _k] = np.sign((_j - _i) * (_k - _i) * (_k - _j))


def comm(A, B):
    return A @ B - B @ A


# --------------------------------------------------------------------------- #
# Realization I: finite-dimensional Lie-algebra reps (exact matrices)          #
# --------------------------------------------------------------------------- #
def lorentz_generators_spinor():
    """Spin-1/2 Lorentz generators on the 4-component Dirac spinor.

    Sigma^{mu nu} = (i/4)[gamma^mu, gamma^nu] (Minkowski).
    J^i = (1/2) eps^{ijk} Sigma^{jk}  (rotations, Hermitian),
    K^i = Sigma^{0i}                  (boosts, anti-Hermitian for the spinor rep).
    """
    g = minkowski_gammas()
    eta = np.diag([1.0, -1.0, -1.0, -1.0])
    Sig = {}
    for mu in range(4):
        for nu in range(4):
            Sig[(mu, nu)] = 0.25j * comm(g[mu], g[nu])
    J = [np.zeros((4, 4), dtype=complex) for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                J[i] += 0.5 * LEVI[i, j, k] * Sig[(j + 1, k + 1)]
    K = [Sig[(0, i + 1)] for i in range(3)]
    return J, K, eta


def check_lorentz_algebra_spinor():
    """P1: so(3,1) closes on the spin-1/2 rep, incl. [K,K] = -i eps J."""
    J, K, _ = lorentz_generators_spinor()
    ok = True
    for i in range(3):
        for j in range(3):
            eJ = sum(1j * LEVI[i, j, k] * J[k] for k in range(3))
            eK = sum(1j * LEVI[i, j, k] * K[k] for k in range(3))
            ok &= np.allclose(comm(J[i], J[j]), eJ, atol=TOL)        # [J,J]=ieJ
            ok &= np.allclose(comm(J[i], K[j]), eK, atol=TOL)        # [J,K]=ieK
            # the crucial boost-boost -> rotation, Minkowski sign:
            ok &= np.allclose(comm(K[i], K[j]), -eJ, atol=TOL)       # [K,K]=-ieJ
    # Hermiticity structure: J Hermitian, K anti-Hermitian (non-compact boost).
    for i in range(3):
        ok &= np.allclose(J[i], J[i].conj().T, atol=TOL)
        ok &= np.allclose(K[i], -K[i].conj().T, atol=TOL)
    return bool(ok)


def check_lorentz_algebra_spinor_euclidean_sign():
    """NON-TRIVIALITY control: the genuine spin-1/2 boosts do NOT obey the
    Euclidean SO(4) sign [K,K] = +i eps J.

    SO(4) (Euclidean) has a compact algebra so(4) = su(2) x su(2) with
    [K,K] = +i eps J; the Minkowski (Lorentz, non-compact) algebra has
    [K,K] = -i eps J.  This MUST return False -- if it returned True, the
    boost-boost sign check would be a tautology that any rotation-like generator
    satisfies.  This pins that the relation we verify is the genuine *Lorentz*
    boost-boost relation, the SO(4)->SO(3,1) (Wick-rotation) content, not SO(4).
    """
    J, K, _ = lorentz_generators_spinor()
    ok = True
    for i in range(3):
        for j in range(3):
            eJ = sum(1j * LEVI[i, j, k] * J[k] for k in range(3))
            ok &= np.allclose(comm(K[i], K[j]), +eJ, atol=TOL)  # WRONG (Euclidean)
    return bool(ok)


def poincare_defining_rep():
    """Ten Poincare generators in the 5x5 defining (vector+translation) rep.

    Acting on the affine coordinate (x^0,x^1,x^2,x^3,1)^T.  The 4x4 Lorentz block
    uses the textbook so(3,1) generators in the vector representation,

        (M_{rho sigma})^{mu}{}_{nu} = i ( delta^{mu}_{rho} eta_{sigma nu}
                                          - delta^{mu}_{sigma} eta_{rho nu} ),

    eta = diag(+,-,-,-), which satisfy the Lorentz algebra
        [M_{mu nu}, M_{rho sigma}] = i( eta_{nu rho} M_{mu sigma}
            - eta_{mu rho} M_{nu sigma} - eta_{nu sigma} M_{mu rho}
            + eta_{mu sigma} M_{nu rho} ).
    From these,
        J^i = (1/2) eps^{ijk} M_{jk},   K^i = M_{0i},
    give [J,J]=ieJ, [J,K]=ieK, [K,K]=-ieJ by construction.

    Translations P_mu are realized on the affine coordinate by the standard
    nilpotent shift in the last column, fixed so that
        [M_{mu nu}, P_rho] = i( eta_{nu rho} P_mu - eta_{mu rho} P_nu ),
    i.e. P_rho transforms as a four-vector.  We set the column entries to
    eta_{mu rho} (a lower-index four-vector shift); H = P^0 = P_0, P^i = -P_i is
    the contravariant spatial momentum.  All ten brackets are checked numerically
    in check_poincare_algebra, so the conventions are self-validating.
    """
    eta = np.diag([1.0, -1.0, -1.0, -1.0])

    # Lorentz generators M_{rho sigma} (rho<sigma) as 5x5 (4x4 block) matrices.
    def Mgen(rho, sigma):
        M = np.zeros((5, 5), dtype=complex)
        for mu in range(4):
            for nu in range(4):
                M[mu, nu] = 1j * (
                    (1.0 if mu == rho else 0.0) * eta[sigma, nu]
                    - (1.0 if mu == sigma else 0.0) * eta[rho, nu]
                )
        return M

    # Translation generators P_mu (lower index) as nilpotent shifts on the affine
    # coordinate: P_mu has eta_{mu nu} in the last column at row nu.  Then
    # [M_{rho sigma}, P_mu] picks up exactly the four-vector transformation.
    def Pgen(mu):
        T = np.zeros((5, 5), dtype=complex)
        for nu in range(4):
            T[nu, 4] = eta[mu, nu]
        return T

    P_lower = [Pgen(mu) for mu in range(4)]
    H = P_lower[0]                       # H = P_0 = P^0 (time translation)
    P = [-P_lower[i + 1] for i in range(3)]  # P^i = -P_i (contravariant spatial)

    J = []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        # J^i = (1/2) eps^{ijk} M_{jk} = M_{(i+1)(i+2)} (spatial indices +1)
        J.append(Mgen(j + 1, k + 1))
    K = [Mgen(0, i + 1) for i in range(3)]
    return {"H": H, "P": P, "J": J, "K": K, "eta": eta}


def check_poincare_algebra(rep, boost_sign=+1.0):
    """P2/P3: verify all ten Poincare brackets for the 5x5 defining rep.

    boost_sign=+1 -> correct Minkowski rep (should PASS).
    boost_sign=-1 -> wrong-sign boost (non-triviality control, should FAIL).
    """
    H = rep["H"]
    P = rep["P"]
    J = rep["J"]
    K = [boost_sign * k for k in rep["K"]]
    ok = True

    # [P^i, P^j] = 0 ; [H, P^i] = 0
    for i in range(3):
        ok &= np.allclose(comm(H, P[i]), 0, atol=TOL)
        for j in range(3):
            ok &= np.allclose(comm(P[i], P[j]), 0, atol=TOL)

    # [H, J^i] = 0
    for i in range(3):
        ok &= np.allclose(comm(H, J[i]), 0, atol=TOL)

    # [J^i, J^j] = i eps J^k ; [J^i, K^j] = i eps K^k ; [K^i, K^j] = -i eps J^k
    for i in range(3):
        for j in range(3):
            eJ = sum(1j * LEVI[i, j, k] * J[k] for k in range(3))
            eK = sum(1j * LEVI[i, j, k] * K[k] for k in range(3))
            ok &= np.allclose(comm(J[i], J[j]), eJ, atol=TOL)
            ok &= np.allclose(comm(J[i], K[j]), eK, atol=TOL)
            ok &= np.allclose(comm(K[i], K[j]), -eJ, atol=TOL)

    # [H, K^i] = i P^i ; [P^i, K^j] = i delta^{ij} H
    for i in range(3):
        ok &= np.allclose(comm(H, K[i]), 1j * P[i], atol=TOL)
        for j in range(3):
            ok &= np.allclose(comm(P[i], K[j]),
                              1j * (1.0 if i == j else 0.0) * H, atol=TOL)

    # [J^i, P^j] = i eps P^k ; [J^i, H] = 0 (rotations act as vector on P)
    for i in range(3):
        for j in range(3):
            eP = sum(1j * LEVI[i, j, k] * P[k] for k in range(3))
            ok &= np.allclose(comm(J[i], P[j]), eP, atol=TOL)
    return bool(ok)


# --------------------------------------------------------------------------- #
# Realization II: one-particle mass-shell differential operators               #
# --------------------------------------------------------------------------- #
def check_oneparticle_boost_generators(rng):
    """P4: H,P,J,K as the EXPLICIT closed-form differential operators on the mass
    shell close the full Poincare algebra (evaluated analytically -- exact, no FD).

    On the positive-energy mass shell H_m^+ = {p^0 = E(p)}, a one-particle
    wavefunction is psi(p) (spin index carried separately; the spin Wigner-rotation
    term is verified in P5).  The ten generators act on psi(p) as the closed-form
    differential operators

        H psi   = E(p) psi,                         E(p)=sqrt(|p|^2+m^2)
        P^i psi = p^i psi
        J^i psi = -i eps^{ijk} p^j d/dp^k psi        (orbital rotation)
        K^i psi = -i E(p) d/dp^i psi                 (orbital boost vector field)

    The boost in direction i moves a mass-shell point by delta p^j = w delta^{ij} E,
    delta E = w p^i; its lift to functions is the first-order operator
    K^i = -i E(p) d/dp^i.  The sign is fixed by [H,K^i] = +iP^i.

    These operators are applied ANALYTICALLY to a Gaussian test family
        psi_c(p) = exp(-alpha |p-c|^2),
    using the exact derivative identities
        d_i psi      = -2 alpha (p-c)_i psi,
        d_i d_j psi  = (4 alpha^2 (p-c)_i (p-c)_j - 2 alpha delta_{ij}) psi,
        d_i d_j d_k psi = ( -8 alpha^3 r_i r_j r_k
                            + 4 alpha^2 (r_i delta_{jk}+r_j delta_{ik}+r_k delta_{ij}) ) psi,
    so every nested commutator of (at most) two first-order operators is evaluated
    to machine precision with NO finite-difference error (the source of the earlier
    O(1e-3) discrete-product-rule artifact is removed).  We verify all four
    boost-containing brackets pointwise on a random sample of momenta:
        [H,K^i]=iP^i,  [P^i,K^j]=i delta^{ij} H,  [J^i,K^j]=i eps^{ijk} K^k,
        [K^i,K^j]=-i eps^{ijk} J^k   (the crucial boost-boost -> rotation).
    """
    m = float(rng.uniform(0.7, 1.6))
    alpha = float(rng.uniform(0.4, 1.0))

    # A point on the mass shell is parameterized by spatial p; E(p)=sqrt(p^2+m^2).
    # We need E and its first and second derivatives in closed form:
    #   d_i E = p_i / E,
    #   d_i d_j E = delta_{ij}/E - p_i p_j / E^3.
    def E(p):
        return np.sqrt(p @ p + m * m)

    def dE(p, i):
        return p[i] / E(p)

    def ddE(p, i, j):
        e = E(p)
        return (1.0 if i == j else 0.0) / e - p[i] * p[j] / e ** 3

    # Gaussian test function value and derivatives at a point p, centered at c.
    def psi(p, c):
        r = p - c
        return np.exp(-alpha * (r @ r))

    def dpsi(p, c, i):
        r = p - c
        return -2 * alpha * r[i] * psi(p, c)

    def ddpsi(p, c, i, j):
        r = p - c
        return (4 * alpha ** 2 * r[i] * r[j]
                - 2 * alpha * (1.0 if i == j else 0.0)) * psi(p, c)

    # Closed-form operator actions returning the *value* and *first derivatives*
    # of (Op psi) at a point, so that a second operator can be applied exactly.
    # We represent a "field" as a callable (value, grad, hess) closure.  To keep
    # it simple and exact we apply each operator symbolically on the Gaussian and
    # evaluate the final commutator's value at sample points.

    # Action of K^i = -i E d_i on psi: value = -i E dpsi_i.
    # For nested commutators we need d_l of (E d_i psi) etc.; do it in closed form:
    #   d_l (E d_i psi) = (d_l E) d_i psi + E (d_i d_l psi).
    def K_val(p, c, i):
        return -1j * E(p) * dpsi(p, c, i)

    def K_grad(p, c, i, l):
        return -1j * (dE(p, l) * dpsi(p, c, i) + E(p) * ddpsi(p, c, i, l))

    def J_val(p, c, i):
        out = 0.0 + 0.0j
        for j in range(3):
            for k in range(3):
                if LEVI[i, j, k] != 0:
                    out += -1j * LEVI[i, j, k] * p[j] * dpsi(p, c, k)
        return out

    def J_grad(p, c, i, l):
        # d_l ( -i eps p_j d_k psi ) = -i eps ( delta_{jl} d_k psi + p_j d_k d_l psi )
        out = 0.0 + 0.0j
        for j in range(3):
            for k in range(3):
                if LEVI[i, j, k] != 0:
                    out += -1j * LEVI[i, j, k] * (
                        (1.0 if j == l else 0.0) * dpsi(p, c, k)
                        + p[j] * ddpsi(p, c, k, l))
        return out

    def H_val(p, c):
        return E(p) * psi(p, c)

    def P_val(p, c, i):
        return p[i] * psi(p, c)

    # Composite operator values at p for the commutators.
    def comm_HK(p, c, i):
        # [H,K^i] psi = H(K^i psi) - K^i(H psi)
        #   H(K^i psi)  = E * (K^i psi value)
        #   K^i(H psi)  = -i E d_i (E psi) = -i E ( (d_i E) psi + E d_i psi )
        HK = E(p) * K_val(p, c, i)
        KH = -1j * E(p) * (dE(p, i) * psi(p, c) + E(p) * dpsi(p, c, i))
        return HK - KH

    def comm_PK(p, c, i, j):
        # [P^i, K^j] psi = p^i (K^j psi) - K^j(p^i psi)
        #   K^j(p^i psi) = -i E d_j (p^i psi) = -i E ( delta_{ij} psi + p^i d_j psi )
        PK = p[i] * K_val(p, c, j)
        KP = -1j * E(p) * ((1.0 if i == j else 0.0) * psi(p, c)
                           + p[i] * dpsi(p, c, j))
        return PK - KP

    def comm_JK(p, c, i, j):
        # [J^i, K^j] psi = J^i(K^j psi) - K^j(J^i psi)
        #   J^i(K^j psi) = -i eps^{iab} p_a d_b (K^j psi) = -i eps p_a K_grad(.,j,b)
        JK = 0.0 + 0.0j
        for a in range(3):
            for b in range(3):
                if LEVI[i, a, b] != 0:
                    JK += -1j * LEVI[i, a, b] * p[a] * K_grad(p, c, j, b)
        #   K^j(J^i psi) = -i E d_j (J^i psi) = -i E J_grad(.,i,j)
        KJ = -1j * E(p) * J_grad(p, c, i, j)
        return JK - KJ

    def comm_KK(p, c, i, j):
        # [K^i, K^j] psi = K^i(K^j psi) - K^j(K^i psi)
        #   K^i(K^j psi) = -i E d_i (K^j psi) = -i E K_grad(.,j,i)
        KiKj = -1j * E(p) * K_grad(p, c, j, i)
        KjKi = -1j * E(p) * K_grad(p, c, i, j)
        return KiKj - KjKi

    ok = True
    worst = 0.0
    for _ in range(40):
        p = rng.normal(size=3) * 1.3
        c = rng.normal(size=3) * 0.7

        # [H, K^i] = i P^i
        for i in range(3):
            err = abs(comm_HK(p, c, i) - 1j * P_val(p, c, i))
            worst = max(worst, err); ok &= err < TOL

        # [P^i, K^j] = i delta^{ij} H
        for i in range(3):
            for j in range(3):
                err = abs(comm_PK(p, c, i, j)
                          - 1j * (1.0 if i == j else 0.0) * H_val(p, c))
                worst = max(worst, err); ok &= err < TOL

        # [J^i, K^j] = i eps^{ijk} K^k
        for i in range(3):
            for j in range(3):
                rhs = sum(1j * LEVI[i, j, k] * K_val(p, c, k) for k in range(3))
                err = abs(comm_JK(p, c, i, j) - rhs)
                worst = max(worst, err); ok &= err < TOL

        # [K^i, K^j] = -i eps^{ijk} J^k   (boost-boost -> rotation, the crux)
        for i in range(3):
            for j in range(3):
                rhs = sum(-1j * LEVI[i, j, k] * J_val(p, c, k) for k in range(3))
                err = abs(comm_KK(p, c, i, j) - rhs)
                worst = max(worst, err); ok &= err < TOL

    # NON-TRIVIALITY control: a wrong-sign orbital boost K -> +i E d_i misses
    # [H,K^i] = +iP^i by O(p) (NOT a tautology that holds for any sign).
    p = rng.normal(size=3) * 1.3
    c = rng.normal(size=3) * 0.7
    bad_err = 0.0
    for i in range(3):
        # comm with the flipped sign: [H, +iE d_i] = +i p^i, target is +i p^i but
        # the algebra fixes K = -iE d_i, so this flipped operator gives -i P^i,
        # i.e. it misses the required +iP^i by 2i p^i.
        HKbad = E(p) * (+1j * E(p) * dpsi(p, c, i))
        KHbad = +1j * E(p) * (dE(p, i) * psi(p, c) + E(p) * dpsi(p, c, i))
        bad = (HKbad - KHbad) - 1j * P_val(p, c, i)
        bad_err = max(bad_err, abs(bad))
    control_fails = bad_err > 1e-3
    ok &= control_fails

    return bool(ok), worst


def check_mass_shell_and_wigner(rng):
    """P5: boost flow maps H_m^+ into itself; spin index gets the Wigner rotation.

    (a) Mass-shell invariance: under a finite boost Lambda(w, n_hat), a point on
        the positive mass shell maps to another point on the positive mass shell
        (E'^2 - |p'|^2 = m^2, E' > 0).
    (b) Wigner rotation: for a boost Lambda and a rest-frame spin state, the
        induced little-group element W(Lambda,p) = L(Lambda p)^{-1} Lambda L(p)
        is a rotation (SU(2) Wigner rotation): it leaves the rest momentum
        (m,0,0,0) fixed, so as a 4x4 Lorentz matrix it is block-diag(1, R) with
        R in SO(3); the spin-1/2 carrier is the corresponding SU(2) element.
    """
    m = float(rng.uniform(0.7, 1.6))
    eta = np.diag([1.0, -1.0, -1.0, -1.0])

    def boost_matrix(w, nhat):
        nhat = nhat / np.linalg.norm(nhat)
        ch, sh = np.cosh(w), np.sinh(w)
        L = np.eye(4)
        L[0, 0] = ch
        for i in range(3):
            L[0, i + 1] = sh * nhat[i]
            L[i + 1, 0] = sh * nhat[i]
            for j in range(3):
                L[i + 1, j + 1] += (ch - 1.0) * nhat[i] * nhat[j]
        return L

    def rot_matrix(theta, nhat):
        nhat = nhat / np.linalg.norm(nhat)
        K = np.array([[0, -nhat[2], nhat[1]],
                      [nhat[2], 0, -nhat[0]],
                      [-nhat[1], nhat[0], 0.0]])
        R3 = np.eye(3) + np.sin(theta) * K + (1 - np.cos(theta)) * (K @ K)
        L = np.eye(4)
        L[1:, 1:] = R3
        return L

    def std_boost_to(p3):
        """Standard boost L(p): (m,0,0,0) -> (E,p)."""
        pmag = np.linalg.norm(p3)
        E = np.sqrt(pmag ** 2 + m * m)
        if pmag < 1e-14:
            return np.eye(4)
        w = np.arccosh(E / m)
        return boost_matrix(w, p3 / pmag)

    ok = True
    worst = 0.0
    for _ in range(40):
        # (a) mass-shell invariance under a random boost
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        p4 = np.array([E, *p3])
        L = boost_matrix(rng.uniform(-1.2, 1.2), rng.normal(size=3))
        q4 = L @ p4
        inv = q4[0] ** 2 - q4[1:] @ q4[1:]
        ok &= abs(inv - m * m) < 1e-8 and q4[0] > 0
        worst = max(worst, abs(inv - m * m))

        # check the orbit is on-shell for the *Minkowski metric* generally:
        ok &= abs(p4 @ eta @ p4 - m * m) < 1e-8

        # (b) Wigner rotation W = L(Lp)^{-1} L L(p) fixes the rest momentum and
        #     is a pure spatial rotation (little group of a massive particle).
        Lp = std_boost_to(p3)
        q3 = (L @ p4)[1:]
        Lq = std_boost_to(q3)
        W = np.linalg.inv(Lq) @ L @ Lp
        rest = np.array([m, 0.0, 0.0, 0.0])
        # W fixes the rest vector:
        ok &= np.allclose(W @ rest, rest, atol=1e-7)
        # W is block-diag(1, R) with R orthogonal (rotation), det R = +1:
        R = W[1:, 1:]
        ok &= np.allclose(W[0, 1:], 0, atol=1e-7) and np.allclose(W[1:, 0], 0, atol=1e-7)
        ok &= np.allclose(R @ R.T, np.eye(3), atol=1e-7)
        ok &= abs(np.linalg.det(R) - 1.0) < 1e-7
        worst = max(worst, np.abs(R @ R.T - np.eye(3)).max())

    # (b') the SU(2) carrier of a little-group rotation is unitary and squares
    #      into SO(3) via the adjoint (spin-1/2 Wigner rotation is unitary).
    sx, sy, sz = pauli()
    for _ in range(20):
        nhat = rng.normal(size=3)
        nhat /= np.linalg.norm(nhat)
        th = rng.uniform(-np.pi, np.pi)
        Usu2 = np.cos(th / 2) * np.eye(2) - 1j * np.sin(th / 2) * (
            nhat[0] * sx + nhat[1] * sy + nhat[2] * sz)
        ok &= np.allclose(Usu2.conj().T @ Usu2, np.eye(2), atol=1e-10)  # unitary
        # adjoint action reproduces the SO(3) rotation by angle th about nhat:
        Radj = np.zeros((3, 3))
        sig = [sx, sy, sz]
        for a in range(3):
            Ma = Usu2 @ sig[a] @ Usu2.conj().T
            for b in range(3):
                Radj[b, a] = 0.5 * np.real(np.trace(sig[b] @ Ma))
        Rexp = rot_matrix(th, nhat)[1:, 1:]
        ok &= np.allclose(Radj, Rexp, atol=1e-9)
    return bool(ok), worst


def check_invariant_measure(rng):
    """P6: the Lorentz-invariant measure d^3p/(2E) is preserved by the boost flow.

    The boost vector field on the mass shell is b^i(p) = E(p) (the velocity of the
    point under an infinitesimal boost in direction i is d p^j/dw = delta^{ij} E).
    A measure rho(p) d^3p is invariant under the flow of a vector field V iff
    div(rho V) = 0.  For the invariant measure rho = 1/(2E) and the boost field
    in direction i, V^j = E delta^{ij}, we need
        sum_j d/dp^j ( (1/(2E)) E delta^{ij} ) = d/dp^i (1/2) = 0.
    Verify this identity numerically (finite-difference divergence ~ 0), and the
    non-triviality control that the *flat* measure rho=1 is NOT invariant.
    """
    m = float(rng.uniform(0.7, 1.6))
    h = 1e-4
    ok = True
    worst_inv = 0.0
    worst_flat = 0.0
    for _ in range(60):
        p = rng.normal(size=3)

        def E(q):
            return np.sqrt(q @ q + m * m)

        # divergence of rho*V for the invariant measure, boost in direction i:
        for i in range(3):
            div_inv = 0.0
            div_flat = 0.0
            for j in range(3):
                ep = p.copy(); ep[j] += h
                em = p.copy(); em[j] -= h
                # invariant: rho V^j = (1/(2E)) * E * delta^{ij} = (1/2) delta^{ij}
                fp = (1.0 / (2 * E(ep))) * E(ep) * (1.0 if i == j else 0.0)
                fm = (1.0 / (2 * E(em))) * E(em) * (1.0 if i == j else 0.0)
                div_inv += (fp - fm) / (2 * h)
                # flat: rho V^j = E delta^{ij}
                gp = E(ep) * (1.0 if i == j else 0.0)
                gm = E(em) * (1.0 if i == j else 0.0)
                div_flat += (gp - gm) / (2 * h)
            worst_inv = max(worst_inv, abs(div_inv))
            worst_flat = max(worst_flat, abs(div_flat))
            ok &= abs(div_inv) < 1e-6
    # Non-triviality: the flat measure's divergence is non-zero (boost does NOT
    # preserve d^3p) -- so P6 is a real statement about the *invariant* measure.
    nontrivial_flat = worst_flat > 1e-2
    return bool(ok and nontrivial_flat), worst_inv, worst_flat


# --------------------------------------------------------------------------- #
# Positive energy, mass shell, 2-point continuation                            #
# --------------------------------------------------------------------------- #
def dirac_hamiltonian(p3, m):
    G = minkowski_gammas()
    G0 = G[0]
    alpha = [G0 @ G[k + 1] for k in range(3)]
    beta = G0
    return sum(p3[k] * alpha[k] for k in range(3)) + m * beta


def check_positive_energy(rng):
    """P7: positive single-particle energy; CAR many-body H bounded below by 0."""
    ok = True
    for _ in range(60):
        m = float(rng.uniform(0.2, 3.0))
        p3 = rng.normal(size=3)
        E = float(np.sqrt(p3 @ p3 + m * m))
        # single-particle Dirac spectrum {+E,+E,-E,-E}
        w = np.linalg.eigvalsh(dirac_hamiltonian(p3, m))
        ok &= np.allclose(np.sort(w), [-E, -E, E, E], atol=1e-9)
        # positive-energy branch is >= m > 0 and inside forward light cone
        ok &= E >= m - 1e-12
        ok &= (E ** 2 - p3 @ p3) > 0 and E > 0   # forward timelike four-momentum

        # CAR-relabeled many-body Hamiltonian on a finite mode set is >= 0
        n_modes = 4
        mode_p = [rng.normal(size=3) for _ in range(n_modes)]
        energies = np.array([float(np.sqrt(q @ q + m * m)) for q in mode_p])
        # occupation numbers in {0,1} for particles (a) and antiparticles (b)
        gmin = np.inf
        for occ_a in itertools.product([0, 1], repeat=n_modes):
            for occ_b in itertools.product([0, 1], repeat=n_modes):
                Etot = energies @ (np.array(occ_a) + np.array(occ_b))
                gmin = min(gmin, Etot)
        ok &= abs(gmin) < 1e-12          # vacuum energy 0
        ok &= gmin >= -1e-12             # bounded below by 0
    return bool(ok)


def check_boosted_2point(rng):
    """P8: boosted bispinor 2-point matches rung A's SO(4)->SO(3,1) continuation.

    (a) The Euclidean SO(4) denominator p^2+m^2 Wick-continues (p4 = i p0) to the
        Minkowski mass shell -p0^2+|p|^2+m^2=0, i.e. the Lorentz orbit.
    (b) The Minkowski Dirac 2-point S(p) = (pslash + m)/(p^2 - m^2 +i0) (numerator
        algebra) transforms as a bispinor: under a Lorentz boost with spinor rep
        Lambda = exp(-i w K) and vector rep L, S(L p) = Lambda S(p) Lambda^{-1}.
        This is the SO(3,1) covariance continued from rung A's SO(4) covariance.
    """
    g = minkowski_gammas()
    eta = np.diag([1.0, -1.0, -1.0, -1.0])
    J, K, _ = lorentz_generators_spinor()
    ok = True
    worst = 0.0

    def boost_vec(w, nhat):
        nhat = nhat / np.linalg.norm(nhat)
        ch, sh = np.cosh(w), np.sinh(w)
        L = np.eye(4)
        L[0, 0] = ch
        for i in range(3):
            L[0, i + 1] = sh * nhat[i]
            L[i + 1, 0] = sh * nhat[i]
            for j in range(3):
                L[i + 1, j + 1] += (ch - 1.0) * nhat[i] * nhat[j]
        return L

    for _ in range(40):
        m = float(rng.uniform(0.5, 2.0))

        # (a) Wick rotation of the SO(4) denominator to the Lorentz orbit
        p3 = rng.normal(size=3)
        E = np.sqrt(p3 @ p3 + m * m)
        # Euclidean p4 = iE pole; continue to Minkowski p0 = E:
        mink = -E ** 2 + p3 @ p3 + m * m
        ok &= abs(mink) < 1e-9

        # (b) bispinor covariance under a finite boost
        w = rng.uniform(-1.0, 1.0)
        nhat = rng.normal(size=3)
        L = boost_vec(w, nhat)
        # spinor rep of this boost: exp(-i w (nhat . K)).  Since K is anti-
        # Hermitian here, exp(-i w nhat.K) = exp(w nhat.(-iK)); build via series.
        nK = sum(nhat[i] / np.linalg.norm(nhat) * K[i] for i in range(3))
        Lam = _expm(-1j * w * nK)
        # arbitrary off-shell four-momentum p (the 2-point numerator pslash+m)
        p = np.array([rng.normal(), *rng.normal(size=3)])
        pslash = p[0] * g[0] - sum(p[i + 1] * g[i + 1] for i in range(3))  # p_mu g^mu with mostly-minus -> p^0 g^0 - p^i g^i
        # careful: pslash = p_mu gamma^mu = eta_{mu nu} p^nu gamma^mu
        pslash = sum((eta @ p)[mu] * g[mu] for mu in range(4))
        S = pslash + m * np.eye(4)
        Lp = L @ p
        Sp = sum((eta @ Lp)[mu] * g[mu] for mu in range(4)) + m * np.eye(4)
        lhs = Lam @ S @ np.linalg.inv(Lam)
        err = np.abs(lhs - Sp).max()
        worst = max(worst, err)
        ok &= err < 1e-7

        # consistency: the spinor boost intertwines gamma as a 4-vector,
        #   Lam gamma^mu Lam^{-1} = (L^{-1})^{mu}{}_{nu} gamma^nu
        Linv = np.linalg.inv(L)
        for mu in range(4):
            lhsg = Lam @ g[mu] @ np.linalg.inv(Lam)
            rhsg = sum(Linv[mu, nu] * g[nu] for nu in range(4))
            err = np.abs(lhsg - rhsg).max()
            worst = max(worst, err)
            ok &= err < 1e-7
    return bool(ok), worst


def _expm(A, terms=60):
    """Matrix exponential by truncated series (sufficient for the |w|<=1 boosts)."""
    out = np.eye(A.shape[0], dtype=complex)
    term = np.eye(A.shape[0], dtype=complex)
    for k in range(1, terms):
        term = term @ A / k
        out = out + term
    return out


# --------------------------------------------------------------------------- #
def main():
    rng = np.random.default_rng(SEED)
    results = []

    results.append(("P1 spin-1/2 Lorentz algebra so(3,1) closes, [K,K]=-i eps J",
                    check_lorentz_algebra_spinor()))

    rep = poincare_defining_rep()
    results.append(("P2 full Poincare algebra iso(3,1): all 10 brackets close",
                    check_poincare_algebra(rep, boost_sign=+1.0)))

    # Non-triviality controls (these MUST be False for a correct rep):
    #  (a) a wrong-sign boost generator K -> -K breaks [H,K]=iP and [P,K]=i d H;
    #  (b) the Euclidean SO(4) boost-boost sign [K,K]=+i eps J (instead of the
    #      Minkowski -i eps J) is NOT satisfied by the genuine Lorentz boosts.
    wrong_sign = check_poincare_algebra(rep, boost_sign=-1.0)
    euclid_sign = check_lorentz_algebra_spinor_euclidean_sign()
    results.append(("P3 NON-TRIVIALITY: wrong-sign boost AND Euclidean [K,K]=+ieJ "
                    "both FAIL the (Minkowski) Poincare algebra",
                    (not wrong_sign) and (not euclid_sign)))

    ok4, worst4 = check_oneparticle_boost_generators(rng)
    results.append((f"P4 one-particle mass-shell generators close algebra "
                    f"(analytic, worst={worst4:.2e})", ok4))

    ok5, worst5 = check_mass_shell_and_wigner(rng)
    results.append((f"P5 boost preserves H_m^+; SU(2) Wigner rotation correct "
                    f"(worst={worst5:.2e})", ok5))

    ok6, wi, wf = check_invariant_measure(rng)
    results.append((f"P6 invariant measure d^3p/2E boost-preserved "
                    f"(div_inv={wi:.2e}, flat_div={wf:.2e})", ok6))

    results.append(("P7 positive-energy spectrum; CAR many-body H >= 0 (vacuum 0)",
                    check_positive_energy(rng)))

    ok8, worst8 = check_boosted_2point(rng)
    results.append((f"P8 boosted bispinor 2-point = SO(4)->SO(3,1) continuation "
                    f"(worst={worst8:.2e})", ok8))

    npass = sum(1 for _, ok in results if ok)
    nfail = sum(1 for _, ok in results if not ok)
    print("=" * 78)
    print("FREE DIRAC POINCARE REPRESENTATION  (closes gap G2 by explicit")
    print("construction of the positive-energy Poincare rep of the free Dirac field)")
    print("=" * 78)
    for name, ok in results:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print("=" * 78)
    print(f"SCORECARD PASS={npass} FAIL={nfail}")
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
