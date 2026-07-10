#!/usr/bin/env python3
"""Audit-companion runner for
HEAT_KERNEL_GAUGE_ACTION_NATIVE_RP_PLANE_CHARACTER_POSITIVITY_ALL_COMPACT_GROUPS_NARROW_THEOREM_NOTE_2026-07-09.

Everything below is REPROVED from finite-dimensional computation inside this
file; nothing is cited as an input. The heat-kernel (HK) plane weight is

    K_t = sum_lambda c_lambda(t) chi_lambda ,   c_lambda(t) = d_lambda * exp(-t*C2(lambda)/2)

with C2 in the retained trace-form normalization Tr(T_a T_b) = delta_ab/2 for
the Lie cases (SU(3) fundamental C2 = 4/3, so c_fund(1)/d = exp(-2/3), the
same convention as the HK candidate notes), and a nonnegative-spectrum group
Laplacian for the finite/abelian testbeds (Z_N cycle Cayley set {+-1}:
lambda_q = 2(1-cos(2*pi*q/N)); U(1): lambda_n = n^2).

Setup (mirrors the Wilson temporal-gauge RP bridge note's carrier):
  * two time slices t in {0,1}; one periodic spatial direction; L_s = 2
    spatial links per slice; temporal gauge U_0 = 1;
  * reflection theta swaps the slices; Theta is ANTILINEAR:
    Theta(F)(U) = conj(F(theta U));
  * HK weight w(c0,c1) = K_t(loop(c1)) * K_t(loop(c0)) * prod_k K_t(U_k(0) U_k(1)^dag);
  * positive-half observables: abelian character-degree<=2 monomials /
    the bridge note's 6-element matrix-element basis.

Parts:
  A (H1): manifest strict positivity of c_lambda(t) for Z_N, U(1), SU(2),
     SU(3); SU(3) dimension/Casimir spot checks incl. the exp(-2/3)
     convention alignment. These are implementation sanity checks; analytic
     coefficient positivity follows from the displayed exponential formula.
  B (H2 algebra): coefficient-level semigroup c(s)c(t)/d = c(s+t) on all
     four groups; exact Z_N kernel-level convolution; Haar normalization
     (trivial coefficient = 1; quadrature integrals = 1); realness of K_t;
     character orthonormality on trig-exact Weyl quadrature grids (validates
     the Schur-polynomial character machinery); U(1) Poisson/Jacobi-theta
     identity; Schur(identity) = dimension.
  C (H4): pointwise positivity. Z_N exact; U(1) via the term-positive
     Gaussian image sum; SU(2)/SU(3) finite-truncation grid evidence at
     printed t values (support only; H4 is not consumed by H3).
  D (H2 cut factorization): chi_lambda(A B^dag) = sum_ij pi_lambda(A)_ij *
     conj(pi_lambda(B)_ij) exactly, on seeded random pairs: Z_N all reps;
     SU(2) unitary symmetric-power reps j in {1/2,1,3/2,2}; SU(3)
     fundamental and adjoint (pi_ad(U)_ab = 2 Tr(T_a U T_b U^dag)).
  E (H3): integrated reflected Gram PSD on the two-slice carrier with the
     HK weight: Z_N exact over all configurations; dropped-conjugation
     negative control (non-PSD); manifest factorization G = W diag(kappa)
     W^dag with plane-kernel eigenvalues kappa >= 0; U(1) quadrature Gram;
     SU(2) and SU(3) seeded Monte-Carlo Grams.

Literature disclaimer: Osterwalder & Seiler, Ann. Phys. 110 (1978) 440, and
Montvay & Munster, "Quantum Fields on a Lattice" Sec. 3.4, are comparators
only; every positivity statement above is reproved here. No PDG / fitted /
measured / lattice-MC-input / beta=6 / g_bare value is used as a derivation
input. This runner is an audit companion for a bounded theorem note: not a
new claim row beyond its note, not a status promotion; audit grades are set
exclusively by the independent audit lane.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

AUDIT_TIMEOUT_SEC = 900

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  [PASS] {label}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"  [FAIL] {label}" + (f"  ({detail})" if detail else ""))


def section(title: str) -> None:
    print()
    print("-" * 88)
    print(title)
    print("-" * 88)


# ----------------------------------------------------------------------------
# Group spectral data and kernels
# ----------------------------------------------------------------------------

def zn_coeffs(N: int, t: float) -> np.ndarray:
    q = np.arange(N)
    lam = 2.0 * (1.0 - np.cos(2.0 * np.pi * q / N))
    return np.exp(-t * lam / 2.0)


def zn_kernel(N: int, t: float) -> np.ndarray:
    """K_t(n) for n = 0..N-1 (exact finite character sum; real)."""
    c = zn_coeffs(N, t)
    n = np.arange(N)
    phases = np.exp(2j * np.pi * np.outer(q_ := np.arange(N), n) / N)
    K = (c[:, None] * phases).sum(axis=0)
    assert np.abs(K.imag).max() < 1e-12
    return K.real


def u1_kernel_on_grid(theta: np.ndarray, t: float, nmax: int = 60) -> np.ndarray:
    n = np.arange(-nmax, nmax + 1)
    c = np.exp(-t * n.astype(float) ** 2 / 2.0)
    K = (c[:, None] * np.exp(1j * np.outer(n, theta))).sum(axis=0)
    return K.real


def u1_gaussian_image_sum(theta: np.ndarray, t: float, mmax: int = 8) -> np.ndarray:
    out = np.zeros_like(theta)
    for m in range(-mmax, mmax + 1):
        out += np.exp(-(theta - 2.0 * np.pi * m) ** 2 / (2.0 * t))
    return math.sqrt(2.0 * np.pi / t) * out


def su2_irreps(jmax_twice: int):
    """[(j, d, C2)] for 2j = 0..jmax_twice."""
    out = []
    for tw in range(jmax_twice + 1):
        j = tw / 2.0
        out.append((j, tw + 1, j * (j + 1.0)))
    return out


def su2_char_grid(j: float, theta: np.ndarray) -> np.ndarray:
    """chi_j(theta) = sum_m exp(2 i m theta) via the everywhere-stable m-sum."""
    ms = -j + np.arange(int(2 * j) + 1)
    return np.cos(2.0 * np.outer(ms, theta)).sum(axis=0)


def su2_kernel_grid(theta: np.ndarray, t: float, jmax_twice: int) -> np.ndarray:
    K = np.zeros_like(theta)
    for j, d, C2 in su2_irreps(jmax_twice):
        K += d * math.exp(-t * C2 / 2.0) * su2_char_grid(j, theta)
    return K


def su2_theta_of(U: np.ndarray) -> np.ndarray:
    """Conjugacy angle theta in [0, pi] from stacked SU(2) matrices."""
    tr = np.einsum("...ii->...", U).real
    return np.arccos(np.clip(tr / 2.0, -1.0, 1.0))


def su3_irreps(cut: int):
    """[(p, q, d, C2)] for p+q <= cut."""
    out = []
    for p in range(cut + 1):
        for q in range(cut + 1 - p):
            d = (p + 1) * (q + 1) * (p + q + 2) // 2
            C2 = (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0
            out.append((p, q, d, C2))
    return out


def su3_h_polys(x: np.ndarray, kmax: int) -> dict:
    """Complete homogeneous h_k(x1,x2,x3) via Newton identities, vectorized.

    x: (..., 3) complex eigenvalues. Returns {k: (...) array}, h_{-2}=h_{-1}=0.
    """
    shape = x.shape[:-1]
    p = {k: (x ** k).sum(axis=-1) for k in range(1, kmax + 1)}
    h = {-2: np.zeros(shape, dtype=complex), -1: np.zeros(shape, dtype=complex),
         0: np.ones(shape, dtype=complex)}
    for k in range(1, kmax + 1):
        acc = np.zeros(shape, dtype=complex)
        for i in range(1, k + 1):
            acc = acc + p[i] * h[k - i]
        h[k] = acc / k
    return h


def su3_schur(h: dict, p: int, q: int) -> np.ndarray:
    """s_lambda for partition (p+q, q, 0) via 3x3 Jacobi-Trudi in h."""
    l1, l2 = p + q, q
    a, b, c = h[l1], h[l1 + 1], h[l1 + 2]
    d_, e, f = h[l2 - 1], h[l2], h[l2 + 1]
    g, i_, jj = h[-2], h[-1], h[0]
    return (a * (e * jj - f * i_)
            - b * (d_ * jj - f * g)
            + c * (d_ * i_ - e * g))


def su3_kernel_from_eigs(x: np.ndarray, t: float, cut: int,
                         return_imag: bool = False):
    """K_t from eigenvalues x (..., 3), truncated at p+q <= cut."""
    irreps = su3_irreps(cut)
    h = su3_h_polys(x, cut + 2)
    K = np.zeros(x.shape[:-1], dtype=complex)
    for p, q, d, C2 in irreps:
        K = K + d * math.exp(-t * C2 / 2.0) * su3_schur(h, p, q)
    if return_imag:
        return K.real, np.abs(K.imag).max()
    return K.real


def su3_torus_eigs(t1: np.ndarray, t2: np.ndarray) -> np.ndarray:
    x = np.empty(t1.shape + (3,), dtype=complex)
    x[..., 0] = np.exp(1j * t1)
    x[..., 1] = np.exp(1j * t2)
    x[..., 2] = np.exp(-1j * (t1 + t2))
    return x


# ----------------------------------------------------------------------------
# Haar sampling
# ----------------------------------------------------------------------------

def rand_su2(rng: np.random.Generator, n: int) -> np.ndarray:
    v = rng.standard_normal((n, 4))
    v /= np.linalg.norm(v, axis=1, keepdims=True)
    a, b, c, d = v[:, 0], v[:, 1], v[:, 2], v[:, 3]
    U = np.empty((n, 2, 2), dtype=complex)
    U[:, 0, 0] = a + 1j * b
    U[:, 0, 1] = c + 1j * d
    U[:, 1, 0] = -c + 1j * d
    U[:, 1, 1] = a - 1j * b
    return U


def rand_su3(rng: np.random.Generator, n: int) -> np.ndarray:
    Z = (rng.standard_normal((n, 3, 3)) + 1j * rng.standard_normal((n, 3, 3)))
    Q, R = np.linalg.qr(Z)
    diag = np.einsum("...ii->...i", R)
    ph = diag / np.abs(diag)
    Q = Q * ph[:, None, :]
    det = np.linalg.det(Q)
    Q = Q * np.exp(-1j * np.angle(det) / 3.0)[:, None, None]
    return Q


def dagger(U: np.ndarray) -> np.ndarray:
    return np.conj(np.swapaxes(U, -1, -2))


# ----------------------------------------------------------------------------
# Abelian exact/quadrature integrated Gram (Z_N and U(1)-grid), L_s = 2
# ----------------------------------------------------------------------------

def abelian_basis(Ls: int = 2):
    qs = [(0,) * Ls]
    for q in itertools.product((-1, 0, 1), repeat=Ls):
        if 1 <= sum(abs(x) for x in q) <= 2:
            qs.append(q)
    return np.array(qs)


def abelian_gram(Kvals: np.ndarray, conj_first: bool = True, Ls: int = 2):
    """Reflected Gram over all slice configs on the N-point group/grid.

    Kvals[d] = K_t at group element d (real). Weight:
    w(c0,c1) = K(loop(c1)) K(loop(c0)) prod_k K(c0_k - c1_k).
    G_ij = (1/Z) sum_{c0,c1} w * conj(F_i(c0)) * F_j(c1)   (conj dropped when
    conj_first=False -- the negative control).
    """
    N = len(Kvals)
    idx = np.indices((N,) * Ls).reshape(Ls, -1)          # (Ls, M)
    M = idx.shape[1]
    hvec = Kvals[idx.sum(axis=0) % N]                    # (M,) half weights
    D = (idx[:, :, None] - idx[:, None, :]) % N          # (Ls, M, M)
    Kplane = Kvals[D].prod(axis=0)                       # (M, M)
    qs = abelian_basis(Ls)
    phases = (2.0 * np.pi / N) * (qs @ idx)              # (B, M)
    F = np.exp(1j * phases)
    row = (np.conj(F) if conj_first else F) * hvec
    col = F * hvec
    Gu = row @ Kplane @ col.T
    Z = float(hvec @ Kplane @ hvec)
    return Gu, Z, Kplane, hvec, F


def psd_report(G: np.ndarray):
    herm = np.abs(G - G.conj().T).max()
    ev = np.linalg.eigvalsh((G + G.conj().T) / 2.0)
    return ev.min(), herm


# ----------------------------------------------------------------------------
# SU(2) symmetric-power representation (Part D)
# ----------------------------------------------------------------------------

def su2_sym_power(U: np.ndarray, n: int) -> np.ndarray:
    """Unitary irrep of SU(2) on degree-n Bargmann monomials e_ab = z1^a z2^b /
    sqrt(a! b!), via (pi(U) f)(z) = f(U^{-1} z). Dimension n+1."""
    Minv = U.conj().T
    dim = n + 1
    pi = np.zeros((dim, dim), dtype=complex)
    fact = [math.factorial(k) for k in range(n + 1)]
    for col, (a, b) in enumerate((n - k, k) for k in range(dim)):
        # expand (M11 z1 + M12 z2)^a (M21 z1 + M22 z2)^b
        coeff = {}
        for i in range(a + 1):
            for k in range(b + 1):
                c1 = i + k
                w = (math.comb(a, i) * Minv[0, 0] ** i * Minv[0, 1] ** (a - i)
                     * math.comb(b, k) * Minv[1, 0] ** k * Minv[1, 1] ** (b - k))
                coeff[c1] = coeff.get(c1, 0.0) + w
        for c1, w in coeff.items():
            d1 = n - c1
            rowi = n - c1
            pi[rowi, col] = (w * math.sqrt(fact[c1] * fact[d1])
                             / math.sqrt(fact[a] * fact[b]))
    return pi


GELL_MANN = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
    np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / math.sqrt(3.0),
]


def su3_adjoint(U: np.ndarray) -> np.ndarray:
    """pi_ad(U)_ab = 2 Tr(T_a U T_b U^dag), T_a = lambda_a/2."""
    Ud = U.conj().T
    pi = np.empty((8, 8), dtype=complex)
    for a in range(8):
        for b in range(8):
            pi[a, b] = 0.5 * np.trace(GELL_MANN[a] @ U @ GELL_MANN[b] @ Ud)
    return pi


# ----------------------------------------------------------------------------
# Monte-Carlo integrated Gram (SU(2)/SU(3)), L_s = 2
# ----------------------------------------------------------------------------

def mc_gram(group: str, t: float, n: int, seed: int, cut: int):
    rng = np.random.default_rng(seed)
    sampler = rand_su2 if group == "su2" else rand_su3
    L = [[sampler(rng, n) for _s in (0, 1)] for _k in (0, 1)]

    loop0 = L[0][0] @ L[1][0]
    loop1 = L[0][1] @ L[1][1]
    str0 = L[0][0] @ dagger(L[0][1])
    str1 = L[1][0] @ dagger(L[1][1])

    if group == "su2":
        def kern(V):
            th = su2_theta_of(V)
            K = np.zeros(n)
            for j, d, C2 in su2_irreps(cut):
                K += d * math.exp(-t * C2 / 2.0) * su2_char_grid(j, th)
            return K, 0.0
    else:
        def kern(V):
            x = np.linalg.eigvals(V)
            return su3_kernel_from_eigs(x, t, cut, return_imag=True)

    kvals, imags = [], []
    for V in (loop0, loop1, str0, str1):
        K, im = kern(V)
        kvals.append(K)
        imags.append(im)
    w = kvals[0] * kvals[1] * kvals[2] * kvals[3]

    def obs(A, B):
        trA = np.einsum("nii->n", A)
        trB = np.einsum("nii->n", B)
        trAB = np.einsum("nij,nji->n", A, B)
        one = np.ones(n, dtype=complex)
        if group == "su2":
            fifth = A[:, 0, 0]
        else:
            fifth = np.conj(trA)
        return np.stack([one, trA, trB, trAB, fifth, B[:, 0, 1]])

    Fpos = obs(L[0][1], L[1][1])
    Fneg = obs(L[0][0], L[1][0])
    G = np.einsum("s,is,js->ij", w, np.conj(Fneg), Fpos) / w.sum()
    ess = float(w.sum() ** 2 / (w * w).sum())
    return G, w, max(imags), ess


# ----------------------------------------------------------------------------
# Parts
# ----------------------------------------------------------------------------

def part_a():
    section("Part A -- H1: manifest strict positivity of c_lambda(t)")

    ok = True
    detail = []
    for N in range(2, 7):
        for t in (0.3, 1.0, 2.5):
            c = zn_coeffs(N, t)
            ok = ok and bool(c.min() > 0.0)
    check("A1: Z_N coefficients strictly positive (N=2..6, t in {0.3,1.0,2.5})", ok)

    # |n| <= 30 keeps exp(-t n^2/2) inside float64 range at t=1.5 (exp(-675));
    # positivity of exp(real) is manifest, the check certifies the computed values.
    n = np.arange(-30, 31)
    ok = True
    for t in (0.5, 1.5):
        c = np.exp(-t * n.astype(float) ** 2 / 2.0)
        ok = ok and bool(c.min() > 0.0)
    check("A2: U(1) coefficients strictly positive (|n|<=30, t in {0.5,1.5})", ok)

    ok = True
    for t in (1.0, 1.5, 3.0, 4.0):
        cs = [d * math.exp(-t * C2 / 2.0) for _j, d, C2 in su2_irreps(30)]
        ok = ok and min(cs) > 0.0
    check("A3: SU(2) sampled coefficients strictly positive (2j<=30)", ok)

    spot = {(1, 0): (3, 4.0 / 3.0), (0, 1): (3, 4.0 / 3.0), (1, 1): (8, 3.0),
            (2, 0): (6, 10.0 / 3.0), (3, 0): (10, 6.0), (2, 1): (15, 16.0 / 3.0),
            (2, 2): (27, 8.0)}
    ok = True
    c2_fund = None
    for (p, q, d, C2) in su3_irreps(10):
        if (p, q) == (1, 0):
            c2_fund = C2
        if (p, q) in spot:
            d0, C20 = spot[(p, q)]
            ok = ok and d == d0 and abs(C2 - C20) < 1e-12
    align = abs(math.exp(-1.0 * c2_fund / 2.0) - math.exp(-2.0 / 3.0))
    check("A4: SU(3) dimension/Casimir spot checks + c_fund(1)/d = exp(-2/3) alignment",
          ok and align < 1e-15, f"|c_fund(1)/d - e^(-2/3)|={align:.1e}")

    ok = True
    for t in (1.0, 2.0, 3.0, 4.0, 6.0):
        cs = [d * math.exp(-t * C2 / 2.0) for _p, _q, d, C2 in su3_irreps(10)]
        ok = ok and min(cs) > 0.0
    check("A5: SU(3) coefficients strictly positive (p+q<=10, t in {1,2,3,4,6})", ok)

def part_b():
    section("Part B -- H2 algebra: semigroup, normalization, realness, orthonormality")

    s, t = 0.7, 1.3
    worst = 0.0
    for N in range(2, 7):
        lhs = zn_coeffs(N, s) * zn_coeffs(N, t)
        rhs = zn_coeffs(N, s + t)
        worst = max(worst, float(np.abs(lhs - rhs).max()))
    n = np.arange(-40, 41).astype(float)
    worst = max(worst, float(np.abs(np.exp(-s * n * n / 2) * np.exp(-t * n * n / 2)
                                    - np.exp(-(s + t) * n * n / 2)).max()))
    for _j, d, C2 in su2_irreps(30):
        cs_, ct_, cst = (d * math.exp(-u * C2 / 2.0) for u in (s, t, s + t))
        worst = max(worst, abs(cs_ * ct_ / d - cst))
    for _p, _q, d, C2 in su3_irreps(10):
        cs_, ct_, cst = (d * math.exp(-u * C2 / 2.0) for u in (s, t, s + t))
        worst = max(worst, abs(cs_ * ct_ / d - cst))
    check("B1: coefficient semigroup c(s)c(t)/d = c(s+t) on Z_N, U(1), SU(2), SU(3)",
          worst < 1e-12, f"max dev={worst:.1e}")

    N = 5
    Ks, Kt, Kst = zn_kernel(N, 0.4), zn_kernel(N, 0.9), zn_kernel(N, 1.3)
    conv = np.array([(Ks * np.roll(Kt[::-1], nn + 1)).sum() / N for nn in range(N)])
    dev = float(np.abs(conv - Kst).max())
    check("B2: Z_5 kernel-level convolution (K_0.4 * K_0.9) = K_1.3 exact",
          dev < 1e-12, f"max dev={dev:.1e}")

    devs = []
    devs.append(abs(zn_coeffs(4, 1.0)[0] - 1.0))
    devs.append(abs(zn_kernel(4, 1.0).mean() - 1.0))
    th = np.linspace(0.0, np.pi, 4096, endpoint=False) + np.pi / 8192
    K2 = su2_kernel_grid(th, 1.5, 24)
    devs.append(abs((2.0 / np.pi) * np.mean(np.sin(th) ** 2 * K2) * np.pi - 1.0))
    g = 72
    t1, t2 = np.meshgrid(2 * np.pi * np.arange(g) / g, 2 * np.pi * np.arange(g) / g,
                         indexing="ij")
    x = su3_torus_eigs(t1, t2)
    delta2 = (np.abs(x[..., 0] - x[..., 1]) ** 2 * np.abs(x[..., 0] - x[..., 2]) ** 2
              * np.abs(x[..., 1] - x[..., 2]) ** 2)
    K3 = su3_kernel_from_eigs(x, 2.0, 12)
    devs.append(abs(np.mean(delta2 * K3) / 6.0 - 1.0))
    check("B3: Haar normalization: c_triv=1; mean_Z4 K=1; SU(2)/SU(3) Weyl integrals = 1",
          max(devs) < 1e-10, f"max dev={max(devs):.1e}")

    im_zn = 0.0  # zn_kernel asserts internally; recompute explicitly
    c = zn_coeffs(5, 0.7)
    q = np.arange(5)
    Kc = (c[:, None] * np.exp(2j * np.pi * np.outer(q, q) / 5)).sum(axis=0)
    im_zn = float(np.abs(Kc.imag).max())
    _, im_su3 = su3_kernel_from_eigs(x, 2.0, 12, return_imag=True)
    check("B4: realness of K_t (Z_5 exact; SU(3) torus grid; SU(2) m-sum is real by construction)",
          im_zn < 1e-12 and im_su3 < 1e-9, f"Z_5 im={im_zn:.1e}, SU(3) im={im_su3:.1e}")

    thq = np.linspace(0.0, np.pi, 4096, endpoint=False) + np.pi / 8192
    worst = 0.0
    for tja in range(0, 7):
        for tjb in range(0, 7):
            ja, jb = tja / 2.0, tjb / 2.0
            val = (2.0 / np.pi) * np.mean(np.sin(thq) ** 2
                                          * su2_char_grid(ja, thq)
                                          * su2_char_grid(jb, thq)) * np.pi
            worst = max(worst, abs(val - (1.0 if tja == tjb else 0.0)))
    hh = su3_h_polys(x, 8)
    reps = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (2, 1)]
    for (pa, qa) in reps:
        for (pb, qb) in reps:
            sa = su3_schur(hh, pa, qa)
            sb = su3_schur(hh, pb, qb)
            val = np.mean(delta2 * sa * np.conj(sb)) / 6.0
            tgt = 1.0 if (pa, qa) == (pb, qb) else 0.0
            worst = max(worst, abs(val - tgt))
    check("B5: character orthonormality (SU(2) sin^2 measure; SU(3) Weyl 2-torus measure)",
          worst < 1e-9, f"max dev={worst:.1e}")

    thg = np.linspace(-np.pi, np.pi, 1001)
    worst = 0.0
    for tt in (0.5, 1.5):
        worst = max(worst, float(np.abs(u1_kernel_on_grid(thg, tt)
                                        - u1_gaussian_image_sum(thg, tt)).max()))
    check("B6: U(1) Poisson/Jacobi-theta identity (character sum = Gaussian image sum)",
          worst < 1e-10, f"max dev={worst:.1e}")

    idx = su3_torus_eigs(np.zeros(1), np.zeros(1))
    hid = su3_h_polys(idx, 8)
    worst = 0.0
    for (p, q, d, _C2) in su3_irreps(6):
        worst = max(worst, abs(complex(su3_schur(hid, p, q)[0]) - d))
    check("B7: Schur machinery at identity: s_(p,q)(1,1,1) = d_(p,q) for p+q<=6",
          worst < 1e-9, f"max dev={worst:.1e}")


def part_c():
    section("Part C -- H4: pointwise-positivity boundary at printed t")

    ok = True
    mins = []
    for N in range(2, 7):
        for t in (0.3, 1.0, 2.5):
            K = zn_kernel(N, t)
            ok = ok and bool(K.min() > 0.0)
            if N in (2, 4) and t == 0.3:
                mins.append(f"Z_{N}(t={t}):{K.min():.3e}")
    check("C1: Z_N pointwise positivity, exact (N=2..6, t in {0.3,1.0,2.5})",
          ok, "; ".join(mins))

    thg = np.linspace(-np.pi, np.pi, 2001)
    ok = True
    detail = []
    for tt in (0.5, 1.5):
        Kg = u1_gaussian_image_sum(thg, tt)
        Kc = u1_kernel_on_grid(thg, tt)
        ok = ok and bool(Kg.min() > 0.0) and bool(Kc.min() > 0.0)
        detail.append(f"t={tt}: min={Kc.min():.3e}")
    check("C2: U(1) pointwise positivity (term-positive Gaussian rep; grid min > 0)",
          ok, "; ".join(detail))

    ok = True
    detail = []
    for tt in (3.0, 4.0):
        npts = 20001
        th = np.linspace(0.0, np.pi, npts)
        cut = 24
        K = su2_kernel_grid(th, tt, cut)
        margin = float(K.min())
        ok = ok and margin > 0.0
        detail.append(f"t={tt}: truncated-grid min={margin:.4f}")
    check("C3: SU(2) finite-truncation grid is positive (support only)",
          ok, "; ".join(detail))

    ok = True
    detail = []
    for tt, cut in ((4.0, 8), (6.0, 8)):
        g = 401
        ax = np.linspace(-np.pi, np.pi, g, endpoint=False)
        t1, t2 = np.meshgrid(ax, ax, indexing="ij")
        x = su3_torus_eigs(t1, t2)
        K = su3_kernel_from_eigs(x, tt, cut)
        margin = float(K.min())
        ok = ok and margin > 0.0
        detail.append(f"t={tt}: truncated-grid min={margin:.4f}")
    check("C4: SU(3) finite-truncation torus grid is positive (support only)",
          ok, "; ".join(detail))


def part_d():
    section("Part D -- H2 cut factorization: chi(AB^dag) = sum_ij pi(A)_ij conj(pi(B)_ij)")

    N = 5
    worst = 0.0
    for qq in range(N):
        for a in range(N):
            for b in range(N):
                lhs = np.exp(2j * np.pi * qq * (a - b) / N)
                rhs = np.exp(2j * np.pi * qq * a / N) * np.conj(np.exp(2j * np.pi * qq * b / N))
                worst = max(worst, abs(lhs - rhs))
    check("D1: Z_5 factorization exact for all reps and group pairs",
          worst < 1e-14, f"max dev={worst:.1e}")

    rng = np.random.default_rng(11)
    pairs = [(rand_su2(rng, 1)[0], rand_su2(rng, 1)[0]) for _ in range(5)]
    worst_h = worst_u = worst_tr = 0.0
    for A, B in pairs:
        for tw in (1, 2, 3, 4):
            pa, pb, pab = (su2_sym_power(M, tw) for M in (A, B, A @ B))
            worst_h = max(worst_h, float(np.abs(pa @ pb - pab).max()))
            worst_u = max(worst_u, float(np.abs(pa @ pa.conj().T - np.eye(tw + 1)).max()))
            th = su2_theta_of(A[None])[0]
            worst_tr = max(worst_tr, abs(np.trace(pa)
                                         - complex(su2_char_grid(tw / 2.0, np.array([th]))[0])))
    check("D2: SU(2) symmetric-power reps: homomorphism, unitarity, trace = character",
          max(worst_h, worst_u, worst_tr) < 1e-12,
          f"hom={worst_h:.1e}, unit={worst_u:.1e}, tr={worst_tr:.1e}")

    worst = 0.0
    for A, B in pairs:
        V = A @ B.conj().T
        thv = su2_theta_of(V[None])[0]
        for tw in (1, 2, 3, 4):
            lhs = complex(su2_char_grid(tw / 2.0, np.array([thv]))[0])
            pa, pb = su2_sym_power(A, tw), su2_sym_power(B, tw)
            rhs = (pa * np.conj(pb)).sum()
            worst = max(worst, abs(lhs - rhs))
    check("D3: SU(2) factorization chi_j(AB^dag) = sum_ij pi_j(A)_ij conj(pi_j(B)_ij)",
          worst < 1e-12, f"max dev={worst:.1e}")

    rng3 = np.random.default_rng(12)
    A3, B3 = rand_su3(rng3, 1)[0], rand_su3(rng3, 1)[0]
    piA, piB, piAB = su3_adjoint(A3), su3_adjoint(B3), su3_adjoint(A3 @ B3)
    im = max(float(np.abs(piA.imag).max()), float(np.abs(piB.imag).max()))
    orth = float(np.abs(piA @ piA.conj().T - np.eye(8)).max())
    hom = float(np.abs(piA @ piB - piAB).max())
    trdev = abs(np.trace(piA) - (abs(np.trace(A3)) ** 2 - 1.0))
    hA = su3_h_polys(np.linalg.eigvals(A3)[None], 6)
    schur_dev = abs(complex(su3_schur(hA, 1, 1)[0]) - (abs(np.trace(A3)) ** 2 - 1.0))
    check("D4: SU(3) adjoint: real, orthogonal, homomorphism, trace = |TrU|^2-1 = s_(1,1)",
          max(im, orth, hom, trdev, schur_dev) < 1e-11,
          f"im={im:.1e}, orth={orth:.1e}, hom={hom:.1e}, tr={trdev:.1e}, schur={schur_dev:.1e}")

    V = A3 @ B3.conj().T
    fund = abs(np.trace(V) - (A3 * np.conj(B3)).sum())
    adj = abs((abs(np.trace(V)) ** 2 - 1.0) - (piA * np.conj(piB)).sum())
    check("D5: SU(3) factorization, fundamental and adjoint",
          max(fund, abs(adj)) < 1e-11, f"fund={fund:.1e}, adj={abs(adj):.1e}")


def part_e():
    section("Part E -- H3: integrated reflected Gram PSD with the HK weight")

    ok = True
    details = []
    for N in (2, 3, 4, 5):
        for t in (0.3, 1.0, 2.5):
            Gu, Z, _, _, _ = abelian_gram(zn_kernel(N, t))
            mineig, herm = psd_report(Gu / Z)
            ok = ok and mineig > -1e-11 and herm < 1e-11
            if N in (2, 5):
                details.append(f"Z_{N}(t={t}): min={mineig:+.1e}")
    check("E1: Z_N exact Gram PSD (N in {2,3,4,5}, t in {0.3,1.0,2.5})",
          ok, "; ".join(details[:4]) + " ...")

    worst_ctrl = 0.0
    for t in (0.3, 1.0):
        Gu, Z, _, _, _ = abelian_gram(zn_kernel(4, t), conj_first=False)
        mineig, _ = psd_report(Gu / Z)
        worst_ctrl = min(worst_ctrl, mineig)
    check("E2: dropped-conjugation control is NOT PSD (Z_4)",
          worst_ctrl < -1e-3, f"min eig={worst_ctrl:+.4f}")

    Gu, Z, Kplane, hvec, F = abelian_gram(zn_kernel(4, 1.0))
    kap, phi = np.linalg.eigh((Kplane + Kplane.T) / 2.0)
    W = (hvec * np.conj(F)) @ phi
    Gfac = (W * kap) @ W.conj().T
    dev = float(np.abs(Gfac - Gu).max())
    check("E3: manifest factorization G = W diag(kappa) W^dag, kappa >= 0 (Z_4, t=1.0)",
          dev < 1e-9 and kap.min() > -1e-12,
          f"match dev={dev:.1e}, kappa_min={kap.min():+.1e}")

    ok = True
    details = []
    for t in (0.5, 1.5):
        grid = 24
        Kvals = u1_kernel_on_grid(2.0 * np.pi * np.arange(grid) / grid, t)
        Gu, Z, _, _, _ = abelian_gram(Kvals)
        mineig, herm = psd_report(Gu / Z)
        ok = ok and mineig > -1e-9 and herm < 1e-9
        details.append(f"t={t}: min={mineig:+.1e}")
    check("E4: U(1) quadrature Gram PSD (24-point grid, t in {0.5,1.5})",
          ok, "; ".join(details))

    # The sampled Monte-Carlo weights remain positive at t=3.0. This is a
    # finite-sample diagnostic, not a full-kernel pointwise-positivity proof.
    G, w, im, ess = mc_gram("su2", 3.0, 200_000, 0, 24)
    mineig, herm = psd_report(G)
    tol = max(3.0 * herm, 5e-3)
    check("E5: SU(2) MC Gram PSD within MC tolerance (t=3.0, n=200k, seed 0)",
          mineig > -tol and w.min() > 0.0 and im < 1e-8,
          f"min eig={mineig:+.2e}, tol={tol:.1e}, herm={herm:.1e}, w_min={w.min():.2e}, ESS={ess:.0f}")

    G, w, im, ess = mc_gram("su3", 3.0, 400_000, 1, 10)
    mineig, herm = psd_report(G)
    tol = max(3.0 * herm, 5e-3)
    check("E6: SU(3) MC Gram PSD within MC tolerance (t=3.0, n=400k, seed 1)",
          mineig > -tol and w.min() > 0.0 and im < 1e-6,
          f"min eig={mineig:+.2e}, tol={tol:.1e}, herm={herm:.1e}, w_min={w.min():.2e}, ESS={ess:.0f}")


def main() -> int:
    print("=" * 88)
    print("Heat-kernel gauge action: native RP plane character positivity on specified heat semigroups")
    print("companion runner for the 2026-07-09 narrow theorem note")
    print("=" * 88)
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    print()
    print("=" * 88)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
