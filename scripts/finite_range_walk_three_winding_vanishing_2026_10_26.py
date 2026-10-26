#!/usr/bin/env python3
"""Three-winding of finite-range translation-invariant walks on Z^3.

Source note:
  docs/FINITE_RANGE_WALK_THREE_WINDING_VANISHING_BOUNDED_THEOREM_NOTE_2026-10-26.md

The theorem rests on one imported algebraic input, K_1(C[Z^3]) = C^* (+) Z^3
(equivalently SK_1 = 0).  No finite computation can verify that input, and this
runner does not try.  It checks the parts that can be checked:

  A. conventions and positive controls: the integrator returns the predicted
     nonzero integers for analytic infinite-range maps, including an exactly
     O-covariant one;
  B. the proof's mechanism on GL_n(C[Z^3]): products of a unit-monomial
     diagonal and elementary matrices have W3 = 0, elementary factors do not
     change W3 of a nontrivial map, and a Laurent polynomial matrix that is
     invertible on the torus but whose inverse is not a Laurent polynomial can
     carry W3 = -1 (so the hypothesis cannot be dropped);
  C. exact-grid certificates (finite integration lemma) for a battery of
     finite-range unitary walks, including walks found by solving the
     unitarity equations with no product structure imposed;
  D. the supporting Clifford-family lemma by an exact symbolic computation.

Conventions: W3[U] = (1/24 pi^2) int_{[0,2pi)^3} sum_abc eps_abc
tr(A_a A_b A_c) d^3k with A_a = U^{-1} d_a U.  Walks U(k) = sum_n A_n e^{i n.k}.
"""
from __future__ import annotations

import itertools
import os
import sys

for _var in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")

import numpy as np
import sympy as sp
from scipy.optimize import least_squares

AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/FINITE_RANGE_WALK_THREE_WINDING_VANISHING_BOUNDED_THEOREM_NOTE_2026-10-26.md",
)

PAULI = [np.eye(2, dtype=complex),
         np.array([[0, 1], [1, 0]], dtype=complex),
         np.array([[0, -1j], [1j, 0]], dtype=complex),
         np.array([[1, 0], [0, -1]], dtype=complex)]

PASSES = 0
FAILS = 0


def check(label, ok, detail=""):
    global PASSES, FAILS
    ok = bool(ok)
    if ok:
        PASSES += 1
    else:
        FAILS += 1
    print(f"{'PASS' if ok else 'FAIL'}: {label}" + (f" [{detail}]" if detail else ""), flush=True)


# ----------------------------------------------------------------- Laurent matrices
def lp_mul(A, B):
    out = {}
    for na, Ma in A.items():
        for nb, Mb in B.items():
            n = tuple(x + y for x, y in zip(na, nb))
            out[n] = out.get(n, 0) + Ma @ Mb
    return {n: M for n, M in out.items() if np.abs(M).max() > 1e-15}


def lp_const(M):
    return {(0, 0, 0): np.asarray(M, dtype=complex)}


def lp_range(A):
    return max(max(abs(x) for x in n) for n in A)


def lp_cond_shift(P, a):
    """Generalized conditional shift P e^{ik.a} + (1 - P), P a constant projector."""
    d = P.shape[0]
    out = {tuple(a): P.astype(complex)}
    out[(0, 0, 0)] = out.get((0, 0, 0), 0) + (np.eye(d) - P)
    return out


def lp_eval(A, K):
    """Evaluate U and dU/dk_a at points K (..., 3)."""
    d = next(iter(A.values())).shape[0]
    U = np.zeros(K.shape[:-1] + (d, d), complex)
    dU = [np.zeros_like(U) for _ in range(3)]
    for n, M in A.items():
        ph = np.exp(1j * (K @ np.array(n, float)))
        U += ph[..., None, None] * M
        for a in range(3):
            dU[a] += (1j * n[a] * ph)[..., None, None] * M
    return U, dU


def grid(N, offset=0.0):
    k = 2 * np.pi * (np.arange(N) + offset) / N
    return np.stack(np.meshgrid(k, k, k, indexing="ij"), -1)


def w3_density(U, dU, Uinv):
    """W3 density on the grid, normalised so that its mean is W3."""
    A = [Uinv @ d for d in dU]
    t = (np.trace(A[0] @ A[1] @ A[2], axis1=-2, axis2=-1)
         - np.trace(A[0] @ A[2] @ A[1], axis1=-2, axis2=-1))
    return 3 * (2 * np.pi) ** 3 * t / (24 * np.pi ** 2)


def w3_fields(U, dU, Uinv):
    """Grid average of the W3 density times the torus volume."""
    return w3_density(U, dU, Uinv).mean()


def w3_unitary_laurent(A, N):
    """Returns (W3, mean |density|); the second number shows the integrand is not
    identically zero, so a vanishing integral is a genuine cancellation."""
    U, dU = lp_eval(A, grid(N))
    dens = w3_density(U, dU, np.conj(np.swapaxes(U, -1, -2)))
    return dens.mean(), np.abs(dens).mean()


def w3_gl_laurent(A, Ainv, N):
    """W3 of a Laurent matrix with an explicit Laurent inverse (exact on N^3 grids
    when N > 3 (range(A) + range(Ainv))).  Returns (W3, mean |density|)."""
    K = grid(N)
    U, dU = lp_eval(A, K)
    Ui, _ = lp_eval(Ainv, K)
    dens = w3_density(U, dU, Ui)
    return dens.mean(), np.abs(dens).mean()


def unitarity_error(A, N=9):
    U, _ = lp_eval(A, grid(N, 0.37))
    d = U.shape[-1]
    return np.abs(U @ np.conj(np.swapaxes(U, -1, -2)) - np.eye(d)).max()


def det_monomial(A, N=None):
    """Fit det U(k) = c exp(i m.k) on a grid; return (m, max residual)."""
    r = lp_range(A)
    d = next(iter(A.values())).shape[0]
    N = N or (2 * d * r + 3)
    K = grid(N)
    U, _ = lp_eval(A, K)
    det = np.linalg.det(U)
    F = np.fft.fftn(det) / N ** 3
    idx = np.unravel_index(np.argmax(np.abs(F)), F.shape)
    m = tuple(int(i) if i <= N // 2 else int(i) - N for i in idx)
    c = F[idx]
    resid = np.abs(det - c * np.exp(1j * (K @ np.array(m, float)))).max()
    return m, resid


def haar(d, rng):
    z = (rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def rand_projector(d, rank, rng):
    V = haar(d, rng)
    return V[:, :rank] @ V[:, :rank].conj().T


# ----------------------------------------------------------------- analytic controls
def vm_fields(M, K):
    """V_M = (f + i g.sigma)/|(f,g)|, f = M - sum cos k_a, g = sin k (O-covariant)."""
    c = np.cos(K)
    s = np.sin(K)
    f = M - c.sum(-1)
    nrm2 = f ** 2 + (s ** 2).sum(-1)
    nrm = np.sqrt(nrm2)
    W = f[..., None, None] * PAULI[0] + 1j * sum(s[..., a, None, None] * PAULI[a + 1] for a in range(3))
    U = W / nrm[..., None, None]
    dU = []
    for b in range(3):
        dW = s[..., b, None, None] * PAULI[0] + 1j * c[..., b, None, None] * PAULI[b + 1]
        dn = (f * s[..., b] + s[..., b] * c[..., b]) / nrm
        dU.append(dW / nrm[..., None, None] - W * (dn / nrm2)[..., None, None])
    return U, dU


def w3_vm(M, N):
    U, dU = vm_fields(M, grid(N, 0.5))
    return w3_fields(U, dU, np.conj(np.swapaxes(U, -1, -2)))


def cubic_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            R = np.zeros((3, 3))
            for i, p in enumerate(perm):
                R[i, p] = signs[i]
            if np.linalg.det(R) > 0:
                mats.append(R)
    return mats


def spin_lift(R):
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if abs(ang) < 1e-12:
        return np.eye(2, dtype=complex)
    if abs(ang - np.pi) < 1e-9:
        w, v = np.linalg.eig(R)
        n = np.real(v[:, np.argmin(np.abs(w - 1))])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    n = n / np.linalg.norm(n)
    return np.cos(ang / 2) * PAULI[0] - 1j * np.sin(ang / 2) * sum(n[a] * PAULI[a + 1] for a in range(3))


def part_a_controls():
    print("== A. conventions and analytic (infinite-range) positive controls", flush=True)
    O = cubic_group()
    lift_ok = all(np.allclose(spin_lift(R) @ PAULI[a + 1] @ spin_lift(R).conj().T,
                              sum(R[b, a] * PAULI[b + 1] for b in range(3)))
                  for R in O for a in range(3))
    check("24 proper cubic rotations with spin-1/2 lifts D sigma_a D^dag = R_ba sigma_b", len(O) == 24 and lift_ok)
    rng = np.random.default_rng(1)
    dev = 0.0
    for _ in range(300):
        k = rng.uniform(-np.pi, np.pi, 3)
        R = O[rng.integers(24)]
        D = spin_lift(R)
        U1, _ = vm_fields(2.0, (R @ k)[None])
        U0, _ = vm_fields(2.0, k[None])
        dev = max(dev, np.abs(U1[0] - D @ U0[0] @ D.conj().T).max())
    check("V_2 is exactly O-covariant with the full spin-1/2 coin action", dev < 1e-13, f"max dev {dev:.1e}")
    predicted = {3.5: 0, 2.0: 1, 0.5: -2, -2.0: 1, -3.5: 0}
    vals = {M: [w3_vm(M, N) for N in (32, 64, 96)] for M in predicted}
    c = int(np.sign(vals[2.0][-1].real))
    print(f"   convention sign c = {c:+d}, fixed from M = 2 only", flush=True)
    for M, n in predicted.items():
        v = vals[M]
        print(f"   M = {M:+.1f}: W3(N=32, 64, 96) = " + ", ".join(f"{x.real:+.10f}" for x in v), flush=True)
        check(f"V_M at M = {M:+.1f}: W3 = c*({n:+d}) from an independent preimage count",
              abs(v[-1] - c * n) < 1e-6 and abs(v[-1] - v[-2]) < abs(v[1] - v[0]) + 1e-12,
              f"|W3 - c n| = {abs(v[-1] - c * n):.1e}")
    return c


# ----------------------------------------------------------------- GL_n(C[Z^3]) mechanism
def rand_laurent_scalar(rng, r=1, scale=0.6):
    out = {}
    for n in itertools.product(range(-r, r + 1), repeat=3):
        if rng.random() < 0.5:
            out[n] = scale * (rng.normal() + 1j * rng.normal())
    if not out:
        out[(1, 0, 0)] = scale
    return out


def elementary(d, i, j, p):
    """1 + p e_ij and its inverse 1 - p e_ij as Laurent matrices."""
    E = {(0, 0, 0): np.eye(d, dtype=complex)}
    Ei = {(0, 0, 0): np.eye(d, dtype=complex)}
    for n, cf in p.items():
        M = np.zeros((d, d), complex)
        M[i, j] = cf
        E[n] = E.get(n, 0) + M
        Ei[n] = Ei.get(n, 0) - M
    return E, Ei


def part_b_mechanism(c):
    print("== B. the proof mechanism on GL_n(C[Z^3])", flush=True)
    rng = np.random.default_rng(7)
    # mixed upper/lower elementary factors: a product of only upper (or only lower)
    # triangular factors has a pointwise-zero density, which would test nothing
    slots = [(0, 1), (1, 0), (1, 2), (2, 1), (0, 2), (2, 0)]
    for trial in range(4):
        d = 3
        m = tuple(int(x) for x in rng.integers(-2, 3, 3))
        cst = np.exp(1j * rng.uniform(0, 2 * np.pi)) * (0.5 + rng.random())
        D = {m: np.diag([cst, 1, 1]).astype(complex)}
        Dinv = {tuple(-x for x in m): np.diag([1 / cst, 1, 1]).astype(complex)}
        M, Minv = D, Dinv
        picks = [slots[int(o)] for o in rng.permutation(len(slots))[:4]]
        if all(i < j for i, j in picks) or all(i > j for i, j in picks):
            picks[-1] = picks[-1][::-1]
        for i, j in picks:
            E, Ei = elementary(d, i, j, rand_laurent_scalar(rng))
            M = lp_mul(M, E)
            Minv = lp_mul(Ei, Minv)
        prod = lp_mul(M, Minv)
        ident_err = max(np.abs(prod.get((0, 0, 0), 0) - np.eye(d)).max(),
                        max((np.abs(Mx).max() for n, Mx in prod.items() if n != (0, 0, 0)), default=0.0))
        N = 3 * (lp_range(M) + lp_range(Minv)) + 2
        w, l1 = w3_gl_laurent(M, Minv, N)
        print(f"   trial {trial}: factors {picks}, det monomial {m}, range(M) = {lp_range(M)},"
              f" range(M^-1) = {lp_range(Minv)}, M M^-1 - 1 = {ident_err:.1e}, exact grid N = {N}:"
              f" W3 = {w.real:+.2e}{w.imag:+.1e}i, mean |density| = {l1:.2e}", flush=True)
        check(f"GL trial {trial}: diag(c z^m,1,1) times four mixed elementary Laurent factors has W3 = 0"
              f" with a nonzero density", ident_err < 1e-12 and abs(w) < 1e-9 and l1 > 1e-3)
    # elementary factors do not change W3 of a nontrivial map; additivity
    K = grid(48, 0.5)
    V, dV = vm_fields(2.0, K)
    Z = np.zeros(K.shape[:-1] + (4, 4), complex)
    big = Z.copy(); big[..., :2, :2] = V; big[..., 2:, 2:] = np.eye(2)
    dbig = []
    for b in range(3):
        t = Z.copy(); t[..., :2, :2] = dV[b]; dbig.append(t)
    w_st = w3_fields(big, dbig, np.linalg.inv(big))
    p = rand_laurent_scalar(rng)
    E, Ei = elementary(4, 0, 3, p)
    Ev, dEv = lp_eval(E, K)
    Eiv, _ = lp_eval(Ei, K)
    prodv = big @ Ev
    dprod = [dbig[b] @ Ev + big @ dEv[b] for b in range(3)]
    w_el = w3_fields(prodv, dprod, Eiv @ np.linalg.inv(big))
    check("stabilisation and an elementary factor leave W3 unchanged: W3[V_2 (+) 1] = W3[(V_2 (+) 1) E] = c",
          abs(w_st - c) < 1e-8 and abs(w_el - c) < 1e-8, f"{w_st.real:+.10f}, {w_el.real:+.10f}")
    U2 = V @ V
    dU2 = [dV[b] @ V + V @ dV[b] for b in range(3)]
    w_sq = w3_fields(U2, dU2, np.conj(np.swapaxes(U2, -1, -2)))
    check("Polyakov-Wiegmann additivity: W3[V_2 V_2] = 2c", abs(w_sq - 2 * c) < 1e-8, f"{w_sq.real:+.10f}")
    # Fourier truncation of V_2: Laurent polynomial, invertible, inverse not Laurent, W3 = c
    Nf = 64
    Kf = grid(Nf)
    Vf, _ = vm_fields(2.0, Kf)
    coef = np.fft.fftn(Vf, axes=(0, 1, 2)) / Nf ** 3
    for r in (2, 3):
        T = {}
        for n in itertools.product(range(-r, r + 1), repeat=3):
            T[n] = coef[n[0] % Nf, n[1] % Nf, n[2] % Nf]
        ws = []
        for N in (40, 56):
            U, dU = lp_eval(T, grid(N, 0.5))
            ws.append(w3_fields(U, dU, np.linalg.inv(U)))
        Us, _ = lp_eval(T, grid(40, 0.5))
        sv = np.linalg.svd(Us, compute_uv=False)
        uerr = np.abs(Us @ np.conj(np.swapaxes(Us, -1, -2)) - np.eye(2)).max()
        _, dres = det_monomial(T)
        print(f"   truncation range {r}: min singular value {sv.min():.3f}, unitarity defect {uerr:.2e},"
              f" det minus best unit monomial {dres:.2e}, W3(N=40, 56) = {ws[0].real:+.8f}, {ws[1].real:+.8f}",
              flush=True)
        check(f"range-{r} Fourier truncation of V_2: invertible on the torus, det not a unit monomial"
              f" (so not in GL_2(C[Z^3])), W3 = c",
              sv.min() > 0.05 and uerr > 1e-4 and dres > 1e-4
              and abs(ws[1] - c) < 1e-6 and abs(ws[0] - ws[1]) < 1e-6)


# ----------------------------------------------------------------- finite-range battery
def shift_coin_walk(d, L, rng):
    """Coins alternating with conditional shifts; the shift axes cycle x, y, z so that
    the walk depends on all three momenta (otherwise the 3-form density vanishes
    pointwise and the check would be trivial)."""
    W = lp_const(haar(d, rng))
    for step in range(L):
        P = rand_projector(d, int(rng.integers(1, d)), rng)
        a = [0, 0, 0]
        a[step % 3] = int(rng.choice([-1, 1]))
        W = lp_mul(W, lp_cond_shift(P, a))
        W = lp_mul(W, lp_const(haar(d, rng)))
    return W


def d2_product_walk():
    def q(a):
        n1 = [0, 0, 0]; n1[a] = 1
        n2 = [0, 0, 0]; n2[a] = -1
        return {tuple(n1): (PAULI[0] + PAULI[a + 1]) / 2, tuple(n2): (PAULI[0] - PAULI[a + 1]) / 2}
    return lp_mul(lp_mul(q(0), q(1)), q(2))


def b_star_clifford_walk():
    """The O-covariant two-qubit Clifford walk at the parameter point b* of
    TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK (rebuilt from its Gram family)."""
    Gm = [np.kron(PAULI[1], PAULI[0]), np.kron(PAULI[2], PAULI[0]),
          np.kron(PAULI[3], PAULI[1]), np.kron(PAULI[3], PAULI[2]), np.kron(PAULI[3], PAULI[3])]
    b0, b2 = 11 / 30, 3 / 20
    co = [259200000000, -453744000000, 12644840000, 1185396800, -39225499]
    b1 = np.sqrt(min(r.real for r in np.roots(co) if abs(r.imag) < 1e-12 and r.real > 0))
    G = np.array([
        [1 - 3 * b0 ** 2, -2 * b0 * b1, b1 ** 2 - b0 ** 2 - b0 * b2, -3 * b1 * (b0 - b2)],
        [-2 * b0 * b1, b0 ** 2 - 2 * b1 ** 2, b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2],
        [b1 ** 2 - b0 ** 2 - b0 * b2, b1 * (b0 - b2), 2 * b1 ** 2 - b2 ** 2, 2 * b1 * b2],
        [-3 * b1 * (b0 - b2), b0 * b2 - b1 ** 2 + b2 ** 2, 2 * b1 * b2, 3 * b2 ** 2]])
    ev, EV = np.linalg.eigh(G)
    F = (EV[:, 1:] * np.sqrt(ev[1:])).T

    def cosmono(idx):
        out = {(0, 0, 0): 1.0}
        for a in idx:
            new = {}
            for n, cf in out.items():
                for s in (1, -1):
                    m = list(n); m[a] += s
                    new[tuple(m)] = new.get(tuple(m), 0) + cf / 2
            out = new
        return out

    def sin_times_cos(a, idx):
        out = {}
        for n, cf in cosmono(idx).items():
            for s in (1, -1):
                m = list(n); m[a] += s
                out[tuple(m)] = out.get(tuple(m), 0) + cf * s / 2j
        return out

    phi = [cosmono([]), {}, {}, cosmono([0, 1, 2])]
    for a in range(3):
        for n, cf in cosmono([a]).items():
            phi[1][n] = phi[1].get(n, 0) + cf
    for a, bb in itertools.combinations(range(3), 2):
        for n, cf in cosmono([a, bb]).items():
            phi[2][n] = phi[2].get(n, 0) + cf
    F0 = F @ np.array([1, 3, 3, 1])
    Q = np.linalg.qr(np.column_stack([F0, np.eye(3)[:, :2]]))[0]
    if Q[:, 0] @ F0 < 0:
        Q[:, 0] *= -1
    F = Q.T @ F
    A = {}

    def add(dct, M):
        for n, cf in dct.items():
            A[n] = A.get(n, 0) + cf * M

    for r, Mat in enumerate([np.eye(4), 1j * Gm[0], 1j * Gm[1]]):
        for i in range(4):
            add(phi[i], F[r, i] * Mat)
    for a in range(3):
        others = [c for c in range(3) if c != a]
        add(sin_times_cos(a, []), b0 * 1j * Gm[2 + a])
        for c in others:
            add(sin_times_cos(a, [c]), b1 * 1j * Gm[2 + a])
        add(sin_times_cos(a, others), b2 * 1j * Gm[2 + a])
    return {n: np.asarray(M, complex) for n, M in A.items() if np.abs(M).max() > 1e-15}


def generic_unitary(n, rng, r=1):
    """Solve U U^dag = 1 for all 27 range-1 hop matrices with no product structure
    imposed.  U U^dag - 1 has degree <= 2r per axis, so vanishing on the (4r+1)^3
    grid means vanishing identically (up to the solver residual).  A soft anchor
    toward a random non-unitary Laurent matrix keeps the solution moving; it is then
    removed.  The Jacobian of the residual is supplied in closed form."""
    H = np.array(list(itertools.product(range(-r, r + 1), repeat=3)))
    nh = len(H)
    Nu = 4 * r + 1
    ku = 2 * np.pi * np.array(list(itertools.product(range(Nu), repeat=3))) / Nu
    Cu = np.exp(1j * ku @ H.T)                       # (K, nh)
    nk = Cu.shape[0]
    target = 0.15 * (rng.normal(size=(nh, n, n)) + 1j * rng.normal(size=(nh, n, n)))
    target[nh // 2] += np.eye(n)
    npar = nh * n * n
    eye = np.eye(n)

    def unpack(p):
        return (p[:npar] + 1j * p[npar:]).reshape(nh, n, n)

    def res(p, aw):
        A = unpack(p)
        U = np.einsum("kh,hij->kij", Cu, A)
        R = (U @ np.conj(np.swapaxes(U, 1, 2)) - eye).ravel()
        out = [R.real, R.imag]
        if aw > 0:
            Dv = (A - target).ravel() * aw
            out += [Dv.real, Dv.imag]
        return np.concatenate(out)

    def jac(p, aw):
        A = unpack(p)
        U = np.einsum("kh,hij->kij", Cu, A)
        # d R_k[a,b] / d Re A_h[i,j] = C_kh d_ai conj(U_k[b,j]) + conj(C_kh) U_k[a,j] d_bi
        t1 = np.einsum("kh,ai,kbj->kabhij", Cu, eye, np.conj(U))
        t2 = np.einsum("kh,kaj,bi->kabhij", np.conj(Cu), U, eye)
        d_re = (t1 + t2).reshape(nk * n * n, npar)
        d_im = (1j * t1 - 1j * t2).reshape(nk * n * n, npar)
        top = np.hstack([d_re.real, d_im.real])
        bot = np.hstack([d_re.imag, d_im.imag])
        J = np.vstack([top, bot])
        if aw > 0:
            J = np.vstack([J, aw * np.eye(2 * npar)])
        return J

    p = np.concatenate([target.real.ravel(), target.imag.ravel()])
    for aw in (0.3, 0.03, 0.0):
        p = least_squares(res, p, jac=jac, args=(aw,), method="trf", max_nfev=200,
                          xtol=1e-15, ftol=1e-15, gtol=1e-15).x
    A = unpack(p)
    return {tuple(int(x) for x in h): A[i] for i, h in enumerate(H) if np.abs(A[i]).max() > 1e-14}


def part_c_battery():
    print("== C. finite-range unitary walks: exact-grid certificates", flush=True)
    rng = np.random.default_rng(3)
    # (name, walk, density expectation): "nonzero" means the W3 density is not identically
    # zero, so W3 = 0 is a genuine cancellation; "pointwise zero" marks walks whose density
    # vanishes identically for a structural reason stated in the name.
    walks = []
    for d, L, cnt in ((2, 4, 3), (3, 4, 2), (4, 5, 2)):
        for t in range(cnt):
            walks.append((f"shift-coin product n={d} depth={L} #{t}", shift_coin_walk(d, L, rng), "nonzero"))
    walks.append(("D2-covariant product walk q_x q_y q_z", d2_product_walk(), "nonzero"))
    walks.append(("D3 body-diagonal shift (depends on k1+k2+k3 only)",
                  {(1, 1, 1): (PAULI[0] + (PAULI[1] + PAULI[2] + PAULI[3]) / np.sqrt(3)) / 2,
                   (-1, -1, -1): (PAULI[0] - (PAULI[1] + PAULI[2] + PAULI[3]) / np.sqrt(3)) / 2},
                  "pointwise zero"))
    walks.append(("O-covariant two-qubit Clifford walk b* (Clifford lemma)", b_star_clifford_walk(),
                  "pointwise zero"))
    # The solver can land on degenerate solutions whose density vanishes (identically or
    # nearly); those test nothing and are reported and skipped, never counted.
    found = attempts = 0
    while found < 2 and attempts < 8:
        attempts += 1
        A = generic_unitary(2, rng)
        _, l1 = w3_unitary_laurent(A, 8)
        if l1 < 1e-3:
            print(f"   solver attempt {attempts}: mean |density| {l1:.1e}, degenerate solution not used", flush=True)
            continue
        found += 1
        walks.append((f"walk with no imposed structure n=2 #{found} ({len(A)} nonzero hops,"
                      f" solver attempt {attempts})", A, "nonzero"))
    check("two solver solutions with no imposed structure and a non-trivial density were found",
          found == 2, f"{attempts} attempts")
    allzero = True
    for name, A, expect in walks:
        r = lp_range(A)
        uerr = unitarity_error(A)
        U0, _ = lp_eval(A, grid(5, 0.21))
        motion = np.abs(U0 - U0.mean(axis=(0, 1, 2))).max()
        m, dres = det_monomial(A)
        w1, l1 = w3_unitary_laurent(A, 6 * r + 2)
        w2, _ = w3_unitary_laurent(A, 6 * r + 5)
        dens_ok = l1 > 1e-6 if expect == "nonzero" else l1 < 1e-12
        ok = (uerr < 1e-9 and motion > 1e-3 and dres < 1e-9 and abs(w1) < 1e-9 and abs(w2) < 1e-9
              and dens_ok)
        allzero &= ok
        print(f"   {name}: range {r}, unitarity err {uerr:.1e}, det = c e^(i{m}.k) (resid {dres:.1e}),"
              f" W3(N={6 * r + 2}) = {w1.real:+.1e}, W3(N={6 * r + 5}) = {w2.real:+.1e},"
              f" mean |density| = {l1:.2e} (expected {expect})", flush=True)
        check(f"{name}: unitary, moving, unit-monomial det, density {expect}, exact-grid W3 = 0", ok)
    # finite integration lemma: integrand of the D2 walk has Fourier degree <= 6r per axis
    A = d2_product_walk()
    N = 16
    U, dU = lp_eval(A, grid(N))
    Ui = np.conj(np.swapaxes(U, -1, -2))
    Aa = [Ui @ d for d in dU]
    dens = (np.trace(Aa[0] @ Aa[1] @ Aa[2], axis1=-2, axis2=-1) - np.trace(Aa[0] @ Aa[2] @ Aa[1], axis1=-2, axis2=-1))
    F = np.abs(np.fft.fftn(dens)) / N ** 3
    deg = 0
    for idx in zip(*np.nonzero(F > 1e-12)):
        deg = max(deg, max(min(i, N - i) for i in idx))
    check("finite integration lemma: the D2-walk W3 density has Fourier degree <= 6r per axis", deg <= 6, f"degree {deg}")
    return allzero


# ----------------------------------------------------------------- exact Clifford lemma
def part_d_clifford():
    print("== D. Clifford-family lemma (exact symbolic)", flush=True)
    P = [sp.Matrix(m.tolist()).applyfunc(sp.nsimplify) for m in PAULI]
    G = [sp.kronecker_product(P[1], P[0]), sp.kronecker_product(P[2], P[0]),
         sp.kronecker_product(P[3], P[1]), sp.kronecker_product(P[3], P[2]), sp.kronecker_product(P[3], P[3])]
    ok = all((G[a] * G[b] + G[b] * G[a]) == (2 * sp.eye(4) if a == b else sp.zeros(4))
             for a in range(5) for b in range(5)) and all(g.H == g for g in G)
    check("Gamma = (tau1, tau2, tau3 sx, tau3 sy, tau3 sz): Hermitian, square to 1, pairwise anticommuting", ok)
    x = sp.symbols("x0:6", real=True)
    Phi = x[0] * sp.eye(4) + sp.I * sum((x[j + 1] * G[j] for j in range(5)), sp.zeros(4))
    Phid = x[0] * sp.eye(4) - sp.I * sum((x[j + 1] * G[j] for j in range(5)), sp.zeros(4))
    r2 = sum(xi ** 2 for xi in x)
    check("Phi^dag Phi = |x|^2 * 1 exactly", sp.simplify(Phid * Phi - r2 * sp.eye(4)) == sp.zeros(4))
    th = [Phid * Phi.diff(xi) for xi in x]
    signs = (1, -1, -1, 1, 1, -1)
    allzero = True
    for i, j, l in itertools.combinations(range(6), 3):
        T = 0
        for (a, b, cc), sgn in zip(itertools.permutations((i, j, l)), signs):
            T += sgn * (th[a] * th[b] * th[cc]).trace()
        if sp.expand(T) != 0:
            allzero = False
    check("all 20 antisymmetrised components of tr(theta^3) vanish as polynomials on R^6", allzero)
    y = sp.symbols("y0:4", real=True)
    Ps = y[0] * sp.eye(2) + sp.I * sum((y[j + 1] * P[j + 1] for j in range(3)), sp.zeros(2))
    Psd = y[0] * sp.eye(2) - sp.I * sum((y[j + 1] * P[j + 1] for j in range(3)), sp.zeros(2))
    ths = [Psd * Ps.diff(yi) for yi in y]
    T = 0
    for (a, b, cc), sgn in zip(itertools.permutations((1, 2, 3)), signs):
        T += sgn * (ths[a] * ths[b] * ths[cc]).trace()
    T0 = sp.expand(T).subs({y[0]: 1, y[1]: 0, y[2]: 0, y[3]: 0})
    check("control: the same routine gives a nonzero component on SU(2) = S^3", T0 != 0, f"T_123(1,0,0,0) = {T0}")


def main():
    print("Imported input (not checked here): K_1(C[Z^3]) = C^* (+) Z^3, i.e. SK_1(C[Z^3]) = 0.")
    print("Supplied class: translation-invariant single-particle walks with finitely many hops.")
    c = part_a_controls()
    part_b_mechanism(c)
    part_c_battery()
    part_d_clifford()
    print(f"TOTAL: PASS={PASSES} FAIL={FAILS}")
    return 0 if FAILS == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
