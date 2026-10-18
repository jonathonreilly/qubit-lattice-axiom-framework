"""Shared tools for block C5: three-winding W3 of maps T^3 -> U(n) or GL(n).

Convention (fixed here, used everywhere):
    W3[U] = (1/24 pi^2) * int_{[0,2pi)^3} sum_{abc} eps_{abc} tr(A_a A_b A_c) d^3k,
    A_a = U^{-1} d_a U.
Since tr is cyclic, sum eps tr(A_a A_b A_c) = 3 [tr(A1 A2 A3) - tr(A1 A3 A2)].

Laurent polynomial walks are stored as dicts {(n1,n2,n3): ndarray (n x n)} with
U(k) = sum_n A_n exp(i k.n).

Exactness lemma used by the certificates (proved in NOTE.md, Lemma Q): if U is a Laurent
polynomial unitary of Chebyshev range r per axis, then U^{-1} = U^dagger has range r and
the integrand is a trigonometric polynomial of degree <= 6r per axis. The uniform grid
rule with N points per axis integrates exp(i m k) exactly for |m| < N, so for N >= 6r+1
the grid sum equals the integral up to floating-point rounding.
"""
import itertools
import numpy as np

PAULI = [np.eye(2, dtype=complex),
         np.array([[0, 1], [1, 0]], dtype=complex),
         np.array([[0, -1j], [1j, 0]], dtype=complex),
         np.array([[1, 0], [0, -1]], dtype=complex)]


class Checker:
    def __init__(self):
        self.p = 0
        self.f = 0

    def check(self, name, ok):
        ok = bool(ok)
        if ok:
            self.p += 1
        else:
            self.f += 1
        print(('PASS' if ok else 'FAIL') + ': ' + name, flush=True)

    def total(self):
        print(f'TOTAL: PASS={self.p} FAIL={self.f}')
        return 0 if self.f == 0 else 1


# ---------------- Laurent polynomial arithmetic ----------------
def lp_mul(A, B):
    out = {}
    for na, Ma in A.items():
        for nb, Mb in B.items():
            n = tuple(x + y for x, y in zip(na, nb))
            out[n] = out.get(n, 0) + Ma @ Mb
    return {n: M for n, M in out.items() if np.abs(M).max() > 1e-15}


def lp_const(M):
    return {(0, 0, 0): np.asarray(M, dtype=complex)}


def lp_dagger(A):
    return {tuple(-x for x in n): M.conj().T for n, M in A.items()}


def lp_range(A):
    return max(max(abs(x) for x in n) for n in A)


def lp_cond_shift(P, a):
    """Generalized conditional shift S(k) = P e^{ik.a} + (1-P), P a constant projector."""
    d = P.shape[0]
    out = {tuple(a): P.astype(complex)}
    out[(0, 0, 0)] = out.get((0, 0, 0), 0) + (np.eye(d) - P)
    return out


def lp_eval_grid(A, N):
    """Return U and dU/dk_a on an N^3 grid (exact derivatives), shapes (N,N,N,d,d)."""
    k = 2 * np.pi * np.arange(N) / N
    d = next(iter(A.values())).shape[0]
    U = np.zeros((N, N, N, d, d), complex)
    dU = [np.zeros_like(U) for _ in range(3)]
    for n, M in A.items():
        ph = np.exp(1j * (n[0] * k[:, None, None] + n[1] * k[None, :, None] + n[2] * k[None, None, :]))
        U += ph[..., None, None] * M
        for a in range(3):
            dU[a] += (1j * n[a]) * ph[..., None, None] * M
    return U, dU


def w3_from_fields(U, dU, unitary=True):
    """Grid-average three-winding from U and its derivatives on a uniform N^3 grid."""
    Ui = np.conj(np.swapaxes(U, -1, -2)) if unitary else np.linalg.inv(U)
    A = [Ui @ d for d in dU]
    t = np.trace(A[0] @ A[1] @ A[2], axis1=-2, axis2=-1) - np.trace(A[0] @ A[2] @ A[1], axis1=-2, axis2=-1)
    # integral = (2pi)^3 * mean; W3 = 3 * integral / (24 pi^2)
    val = 3 * (2 * np.pi) ** 3 * t.mean() / (24 * np.pi ** 2)
    return val


def w3_laurent(A, N=None):
    r = lp_range(A)
    if N is None:
        N = 6 * r + 2
    U, dU = lp_eval_grid(A, N)
    return w3_from_fields(U, dU), N


def unitarity_error(A, N=9):
    U, _ = lp_eval_grid(A, N)
    d = U.shape[-1]
    return np.abs(U @ np.conj(np.swapaxes(U, -1, -2)) - np.eye(d)).max()


# ---------------- random unitaries / projectors ----------------
def haar(d, rng):
    z = (rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))


def rand_projector(d, rank, rng):
    V = haar(d, rng)
    return V[:, :rank] @ V[:, :rank].conj().T


# ---------------- smooth (non-finite-range) maps ----------------
def smooth_grid(func, N):
    """func(k1,k2,k3 arrays) -> (U, [dU1,dU2,dU3]) with analytic derivatives."""
    k = 2 * np.pi * (np.arange(N) + 0.5) / N   # offset grid avoids exact TRIM points
    K1, K2, K3 = np.meshgrid(k, k, k, indexing='ij')
    return func(K1, K2, K3)


def wilson_weyl_map(M):
    """O-covariant analytic map V_M = (f + i g.sigma)/|d|, f = M - sum cos, g = sin k."""
    def func(K1, K2, K3):
        Ks = [K1, K2, K3]
        f = M - np.cos(K1) - np.cos(K2) - np.cos(K3)
        g = [np.sin(x) for x in Ks]
        df = [np.sin(x) for x in Ks]
        dg = [[(np.cos(Ks[a]) if a == b else 0 * K1) for b in range(3)] for a in range(3)]  # dg[a][b] = d_b g_a
        nrm2 = f ** 2 + g[0] ** 2 + g[1] ** 2 + g[2] ** 2
        nrm = np.sqrt(nrm2)
        Wm = f[..., None, None] * PAULI[0] + 1j * sum(g[a][..., None, None] * PAULI[a + 1] for a in range(3))
        U = Wm / nrm[..., None, None]
        dU = []
        for b in range(3):
            dW = df[b][..., None, None] * PAULI[0] + 1j * sum(dg[a][b][..., None, None] * PAULI[a + 1] for a in range(3))
            dn = (f * df[b] + sum(g[a] * dg[a][b] for a in range(3))) / nrm
            dU.append(dW / nrm[..., None, None] - Wm * (dn / nrm2)[..., None, None])
        return U, dU
    return func
