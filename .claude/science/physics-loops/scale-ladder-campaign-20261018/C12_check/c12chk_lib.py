"""C12 checker library.  Model = C11_check/c11model.py (independent build, Bloch X(k) = sum X_a e^{-ik.a}).
Own T1 frame (nullspace solve, not tau_frames.npy), own batched W3 (central differences), own D_b letter."""
import os, sys, itertools
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'C11_check'))
import numpy as np
from c11model import GRP, DOUB, KST, bl, RLX, RTX, A0, SDIAG, FC, avg, sym_onsite, wrapk, HON

PAULI = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
EPS = np.zeros((3, 3, 3))
for p in itertools.permutations(range(3)): EPS[p] = np.linalg.det(np.eye(3)[list(p)])


def t1_frame(D):
    """Solve U_g T_l U_g^T = sum_j M_jl T_j with T_l = D y_l D^dag (the condition needed for covariance of D_b)."""
    rows = []
    for g in GRP:
        u = D.conj().T @ g['U'] @ D           # 2x2 rep on D (D invariant)
        M = g['M']
        # linear map on (y_0,y_1,y_2) in C^{12}
        L = np.zeros((12, 12), complex)
        for l in range(3):
            for e in range(4):
                y = np.zeros((3, 2, 2), complex); y[l].flat[e] = 1
                out = np.zeros((3, 2, 2), complex)
                for ll in range(3):
                    out[ll] = u @ y[ll] @ u.conj().T - sum(M[j, ll] * y[j] for j in range(3))
                L[:, l * 4 + e] = out.flatten()
        rows.append(L)
    A = np.concatenate(rows, 0)
    _, s, Vh = np.linalg.svd(A)
    null = Vh[np.abs(s) < 1e-9] if len(s) == 12 else None
    ns = int(np.sum(s < 1e-9))
    y = Vh[-1].conj().reshape(3, 2, 2)
    # make Hermitian: y_l -> phase so that y_0 Hermitian
    ph = np.trace(y[0] @ y[0]); y = y / np.sqrt(ph / 2)
    if not np.allclose(y[0], y[0].conj().T): y = 1j * y
    if np.allclose(y[0] @ y[1], -1j * y[2]): y = -y
    return y, ns, s


def nvec(Q, m):
    """Q: (N,3). returns n (N,4) unnormalised and nhat."""
    n = np.concatenate([np.sin(Q), (m + np.cos(Q).sum(1))[:, None]], 1)
    return n, n / np.linalg.norm(n, axis=1)[:, None]


def make_Db(b, m=2.0, center=None, frame=None, inv=False):
    D = DOUB[b]; P = D @ D.conj().T
    y = frame if frame is not None else t1_frame(D)[0]
    T = [D @ y[i] @ D.conj().T for i in range(3)]
    c = KST if center is None else center
    s = -1 if inv else 1
    def f(K):
        K = np.atleast_2d(K); _, nh = nvec(K - c, m)
        out = np.eye(12)[None] - P[None] + nh[:, 3, None, None] * P[None]
        out = out + 1j * s * sum(nh[:, i, None, None] * T[i][None] for i in range(3))
        return out
    return f


def bl_batch(X, K):
    K = np.atleast_2d(K); out = np.zeros((len(K),) + next(iter(X.values())).shape, complex)
    for a, B in X.items(): out += np.exp(-1j * K @ np.array(a, float))[:, None, None] * B[None]
    return out


def expiH_batch(X, K, theta=1.0):
    H = theta * bl_batch(X, K); H = (H + np.conj(np.swapaxes(H, 1, 2))) / 2
    w, V = np.linalg.eigh(H)
    return np.einsum('nij,nj,nkj->nik', V, np.exp(1j * w), V.conj())


def S_batch(K, p=1):
    K = np.atleast_2d(K)
    d = SDIAG[None] ** p * np.exp(-1j * p * K @ FC.T.astype(float))
    return np.einsum('ni,ij->nij', d, np.eye(12))


def word(fs):
    def f(K):
        out = None
        for g in fs:
            X = g(K); out = X if out is None else out @ X
        return out
    return f


def W3(f, N, h=1e-5, shift=0.5, batch=4096):
    """(1/24 pi^2) int eps_ijk tr(A_i A_j A_k), A_i = U^{-1} d_i U, midpoint N^3 grid, central differences.
    Uses U^{-1} (inverse), so it also applies to GL maps."""
    ks = (np.arange(N) + shift) * 2 * np.pi / N - np.pi
    K = np.array(list(itertools.product(ks, ks, ks)))
    tot = 0.0 + 0j
    for s0 in range(0, len(K), batch):
        Kb = K[s0:s0 + batch]; U = f(Kb); Ui = np.linalg.inv(U)
        A = []
        for i in range(3):
            e = np.zeros(3); e[i] = h
            A.append(Ui @ ((f(Kb + e) - f(Kb - e)) / (2 * h)))
        # eps_ijk tr(A_i A_j A_k) = 3 tr(A0[A1,A2])
        tot += np.sum(3 * np.einsum('nij,nji->n', A[0], A[1] @ A[2] - A[2] @ A[1]))
    return tot * (2 * np.pi / N) ** 3 / (24 * np.pi ** 2)


def pauli_ctrl(m=2.0, center=np.zeros(3)):
    def f(K):
        K = np.atleast_2d(K); _, nh = nvec(K - center, m)
        return nh[:, 3, None, None] * np.eye(2)[None] + 1j * sum(nh[:, i, None, None] * PAULI[i][None] for i in range(3))
    return f
