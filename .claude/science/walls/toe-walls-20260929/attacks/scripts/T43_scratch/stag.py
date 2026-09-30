"""Staggered lattice helpers for T43: D, eps, note's Gamma_f (2D), spin-taste singlet (any d)."""
import itertools
import numpy as np
import scipy.sparse as sp

SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]], complex), np.array([[1, 0], [0, -1]], complex)]


def gammas(d):
    if d == 2:
        return [SIG[0], SIG[1]]
    if d == 4:
        z = np.zeros((2, 2), complex)
        g = []
        for k in range(3):
            g.append(np.block([[z, -1j * SIG[k]], [1j * SIG[k], z]]))
        g.append(np.block([[z, np.eye(2)], [np.eye(2), z]]))
        return g
    raise ValueError


class Lat:
    def __init__(self, L, d):
        self.L, self.d = L, d
        self.V = L ** d
        self.coords = np.array(list(itertools.product(range(L), repeat=d)))
        self.eps = (-1.0) ** self.coords.sum(1)

    def idx(self, x):
        i = 0
        for c in x:
            i = i * self.L + (c % self.L)
        return i

    def shift(self, i, mu, s):
        x = list(self.coords[i])
        x[mu] = (x[mu] + s) % self.L
        return self.idx(x)


def eta(lat, mu):
    return (-1.0) ** (lat.coords[:, :mu].sum(1))


def fwd_shift(lat, U, mu):
    """T_mu with (T chi)(x) = U_mu(x) chi(x+mu); U shape (V,d,Nc,Nc). Returns sparse (V*Nc)^2."""
    V = lat.V
    Nc = U.shape[-1]
    rows, cols, vals = [], [], []
    for i in range(V):
        j = lat.shift(i, mu, +1)
        for a in range(Nc):
            for b in range(Nc):
                v = U[i, mu, a, b]
                if v != 0:
                    rows.append(i * Nc + a)
                    cols.append(j * Nc + b)
                    vals.append(v)
    return sp.csr_matrix((vals, (rows, cols)), shape=(V * Nc, V * Nc))


def diag_site(lat, vec, Nc):
    return sp.diags(np.repeat(vec, Nc)).tocsr()


def stag_D(lat, U):
    Nc = U.shape[-1]
    D = None
    for mu in range(lat.d):
        T = fwd_shift(lat, U, mu)
        term = 0.5 * diag_site(lat, eta(lat, mu), Nc) @ (T - T.conj().T)
        D = term if D is None else D + term
    return D.tocsr()


def gamma_f_2d(lat, U):
    """Note 2026-07-02: Gamma_f = i eta_2 (C1 C2 + C2 C1)/2, C_mu=(T+T^dag)/2, eta_2=(-1)^{x_1} (first coord)."""
    Nc = U.shape[-1]
    C = []
    for mu in range(2):
        T = fwd_shift(lat, U, mu)
        C.append(0.5 * (T + T.conj().T))
    S = 0.5 * (C[0] @ C[1] + C[1] @ C[0])
    eta2 = (-1.0) ** lat.coords[:, 0]
    return (1j * diag_site(lat, eta2, Nc) @ S).tocsr()


def clifford_elems(d):
    g = gammas(d)
    G = {}
    for A in itertools.product((0, 1), repeat=d):
        M = np.eye(g[0].shape[0], dtype=complex)
        for mu in range(d):
            if A[mu]:
                M = M @ g[mu]
        G[A] = M
    return g, G


def spintaste_op(lat, U, S_mat, xi_mat, offset, G, path_avg=True):
    """Gauge-covariant hypercube operator chi-bar (S x xi) chi with hypercube corners at offset + 2Z^d."""
    d, L = lat.d, lat.L
    Nc = U.shape[-1]
    dim = G[tuple([0] * d)].shape[0]
    c2 = 2.0 ** (-d / 2.0)
    V = lat.V
    rows, cols, vals = [], [], []
    blocks = [tuple(2 * np.array(y) + np.array(offset)) for y in itertools.product(range(L // 2), repeat=d)]
    coefs = {}
    # KS phases eta_mu(x) at an odd hypercube corner c differ from eta_mu(A) by (-1)^{sum_{nu<mu} c_nu}: this is the same as
    # flipping gamma_mu -> (-1)^{sum_{nu<mu} s_nu} gamma_mu, i.e. Gamma_A -> (-1)^{rho_s(A)} Gamma_A with rho_s(A)=sum_mu A_mu sum_{nu<mu} s_nu.
    def rho(A):
        return sum(A[mu] * sum(offset[:mu]) for mu in range(d)) % 2
    for A in G:
        for B in G:
            c = c2 * np.trace(G[A].conj().T @ S_mat @ G[B] @ xi_mat) * ((-1) ** (rho(A) + rho(B)))
            if abs(c) > 1e-12:
                coefs[(A, B)] = c
    for corner in blocks:
        for (A, B), c in coefs.items():
            xa = [(corner[m] + A[m]) % L for m in range(d)]
            xb = [(corner[m] + B[m]) % L for m in range(d)]
            ia, ib = lat.idx(xa), lat.idx(xb)
            diffs = [m for m in range(d) if A[m] != B[m]]
            if not diffs:
                W = np.eye(Nc, dtype=complex)
            else:
                perms = list(itertools.permutations(diffs)) if path_avg else [tuple(diffs)]
                W = np.zeros((Nc, Nc), complex)
                for perm in perms:
                    P = np.eye(Nc, dtype=complex)
                    pos = list(xa)
                    for m in perm:
                        if A[m] == 0:  # forward
                            P = P @ U[lat.idx(pos), m]
                            pos[m] = (pos[m] + 1) % L
                        else:  # backward
                            pos[m] = (pos[m] - 1) % L
                            P = P @ U[lat.idx(pos), m].conj().T
                    W += P
                W /= len(perms)
            for a in range(Nc):
                for b in range(Nc):
                    if W[a, b] != 0:
                        rows.append(ia * Nc + a)
                        cols.append(ib * Nc + b)
                        vals.append(c * W[a, b])
    return sp.csr_matrix((vals, (rows, cols)), shape=(V * Nc, V * Nc))


def singlet_op(lat, U, avg_offsets=True):
    d = lat.d
    g, G = clifford_elems(d)
    if d == 2:
        g5 = SIG[2]
    else:
        g5 = g[0] @ g[1] @ g[2] @ g[3]
    dim = g5.shape[0]
    offs = list(itertools.product((0, 1), repeat=d)) if avg_offsets else [tuple([0] * d)]
    O = None
    for s in offs:
        Os = spintaste_op(lat, U, g5, np.eye(dim, dtype=complex), s, G)
        O = Os if O is None else O + Os
    return (O / len(offs)).tocsr()


def taste55_op(lat, U):
    d = lat.d
    g, G = clifford_elems(d)
    g5 = SIG[2] if d == 2 else g[0] @ g[1] @ g[2] @ g[3]
    return spintaste_op(lat, U, g5, g5, tuple([0] * d), G)


def ident_op(lat, U):
    d = lat.d
    g, G = clifford_elems(d)
    dim = G[tuple([0] * d)].shape[0]
    return spintaste_op(lat, U, np.eye(dim, dtype=complex), np.eye(dim, dtype=complex), tuple([0] * d), G)


def u1_flux_links_2d(lat, Q):
    L = lat.L
    phi = 2 * np.pi * Q / L ** 2
    U = np.ones((lat.V, 2, 1, 1), complex)
    for i in range(lat.V):
        x1, x2 = lat.coords[i]
        U[i, 1, 0, 0] = np.exp(1j * phi * x1)
        U[i, 0, 0, 0] = np.exp(-1j * phi * L * x2) if x1 == L - 1 else 1.0
    return U


def u1_flux_links_4d(lat, Q1, Q2):
    """F12 = 2 pi Q1/L^2 (dims 0,1), F34 = 2 pi Q2/L^2 (dims 2,3)."""
    L = lat.L
    p1, p2 = 2 * np.pi * Q1 / L ** 2, 2 * np.pi * Q2 / L ** 2
    U = np.ones((lat.V, 4, 1, 1), complex)
    for i in range(lat.V):
        x = lat.coords[i]
        U[i, 1, 0, 0] = np.exp(1j * p1 * x[0])
        U[i, 0, 0, 0] = np.exp(-1j * p1 * L * x[1]) if x[0] == L - 1 else 1.0
        U[i, 3, 0, 0] = np.exp(1j * p2 * x[2])
        U[i, 2, 0, 0] = np.exp(-1j * p2 * L * x[3]) if x[2] == L - 1 else 1.0
    return U


def total_flux_plane(lat, U, mu, nu):
    tot = 0.0
    for i in range(lat.V):
        a = U[i, mu, 0, 0] * U[lat.shift(i, mu, 1), nu, 0, 0] * np.conj(U[lat.shift(i, nu, 1), mu, 0, 0]) * np.conj(U[i, nu, 0, 0])
        tot += np.angle(a)
    return tot


def rand_su3(rng, n):
    A = rng.normal(size=(n, 3, 3)) + 1j * rng.normal(size=(n, 3, 3))
    Q, R = np.linalg.qr(A)
    ph = np.diagonal(R, axis1=1, axis2=2)
    Q = Q * (ph / np.abs(ph))[:, None, :]
    det = np.linalg.det(Q)
    Q = Q / (det ** (1 / 3))[:, None, None]
    return Q


def hot_su3_links(lat, rng):
    U = rand_su3(rng, lat.V * lat.d).reshape(lat.V, lat.d, 3, 3)
    return U


def argdet(M):
    s, ld = np.linalg.slogdet(M)
    return np.angle(s), ld
