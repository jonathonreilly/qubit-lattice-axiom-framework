"""Lane R probe R2: common machinery for linearized rank-2 symmetric-tensor U(1)
gauge theories on Z^3 (symbols at small k; lattice via k -> q = 2 sin(k/2)).

Symmetric tensors use an orthonormal 6-basis: xx, yy, zz, (xy), (yz), (xz) with
off-diagonal unit tensors (e_ij+e_ji)/sqrt2.  The cubic group O (24 proper
rotations, as the Lattice axiom supplies) acts by A -> R A R^T.
"""
import itertools
import numpy as np

S2 = np.sqrt(2.0)
PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (0, 2)]


def _basis():
    out = []
    for (i, j) in PAIRS:
        M = np.zeros((3, 3))
        if i == j:
            M[i, i] = 1.0
        else:
            M[i, j] = M[j, i] = 1.0 / S2
        out.append(M)
    return out


BS = _basis()


def vec(M):
    return np.array([np.sum(B * M) for B in BS])


def mat(v):
    return sum(v[a] * BS[a] for a in range(6))


def Drep(R):
    return np.array([[np.sum(BS[a] * (R @ BS[b] @ R.T)) for b in range(6)] for a in range(6)])


C4Z = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]], float)
C3D = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)


def cubic_group():
    G = [np.eye(3)]
    frontier = [np.eye(3)]
    while frontier:
        new = []
        for g in frontier:
            for h in (C4Z, C3D):
                x = np.round(h @ g)
                if not any(np.allclose(x, y) for y in G):
                    G.append(x)
                    new.append(x)
        frontier = new
    return G


GROUP = cubic_group()
assert len(GROUP) == 24

EPS = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    EPS[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])

# ---- cubic irreps of Sym^2 (projectors in the 6-basis)
P_A1 = np.outer(vec(np.eye(3)), vec(np.eye(3))) / 3.0
P_DIAG = np.diag([1, 1, 1, 0, 0, 0]).astype(float)
P_E = P_DIAG - P_A1
P_T2 = np.diag([0, 0, 0, 1, 1, 1]).astype(float)


# ---- gauge generators (columns span the gauge orbit at momentum k)
def V_scalar(k):
    return vec(np.outer(k, k))[:, None]


def V_vector(k):
    cols = []
    for j in range(3):
        e = np.zeros(3); e[j] = 1
        cols.append(vec(np.outer(k, e) + np.outer(e, k)))
    return np.array(cols).T


def V_trace(k):
    return vec(np.eye(3))[:, None]


VERSIONS = {
    'S': lambda k: V_scalar(k),
    'S-tl': lambda k: np.hstack([V_scalar(k), V_trace(k)]),
    'V': lambda k: V_vector(k),
    'V-tl': lambda k: np.hstack([V_vector(k), V_trace(k)]),
}


def monos(n):
    return [m for m in itertools.product(range(n + 1), repeat=3) if sum(m) == n]


def mono_vals(ks, n):
    ms = monos(n)
    return np.array([[np.prod(k ** np.array(m)) for m in ms] for k in ks]), ms


def Q_param_basis(n):
    """Hermitian, real-space-real symbols of homogeneous degree n:
    even n -> real symmetric; odd n -> i * real antisymmetric."""
    ms = monos(n)
    mats = []
    if n % 2 == 0:
        for a in range(6):
            for b in range(a, 6):
                S = np.zeros((6, 6)); S[a, b] = S[b, a] = 1.0
                mats.append(S)
    else:
        for a in range(6):
            for b in range(a + 1, 6):
                S = np.zeros((6, 6), complex); S[a, b] = 1j; S[b, a] = -1j
                mats.append(S)
    basis = [(mi, S) for mi in range(len(ms)) for S in mats]
    return basis, ms


def eval_Q(coeffs, basis, mv):
    """mv: monomial values at one k (vector)."""
    Q = np.zeros((6, 6), complex)
    for c, (mi, S) in zip(coeffs, basis):
        if c != 0:
            Q = Q + c * mv[mi] * S
    return Q


def nullspace(A, rtol=1e-9):
    if A.shape[0] == 0:
        return np.eye(A.shape[1])
    u, s, vh = np.linalg.svd(A, full_matrices=True)
    tol = rtol * max(1.0, s[0] if len(s) else 1.0)
    r = int(np.sum(s > tol))
    return vh[r:].conj().T


def rand_dirs(n, rng):
    x = rng.normal(size=(n, 3))
    return x / np.linalg.norm(x, axis=1)[:, None]


def helicity_sq(Avec, n):
    """<m^2> of a symmetric tensor about axis n (continuum SO(2) little group)."""
    L = -np.einsum('abc,c->ab', EPS, n)  # so(3) generator about n
    def act(v):
        M = mat(v)
        return vec(L @ M - M @ L)
    LA = act(Avec)
    num = np.real(np.vdot(LA, LA))
    den = np.real(np.vdot(Avec, Avec))
    return num / den


def phys_projector(Vk, extra=None):
    """Orthonormal basis of the complement of span(V) (and extra) in C^6."""
    cols = Vk if extra is None else np.hstack([Vk, extra])
    q, r = np.linalg.qr(cols)
    rank = int(np.sum(np.abs(np.diag(r)) > 1e-12 * max(1, np.abs(r).max())))
    u, s, vh = np.linalg.svd(cols)
    rank = int(np.sum(s > 1e-10 * s[0]))
    return u[:, rank:]


def frequencies(K, Q, P, X=None):
    """Reduced symplectic spectrum. H = 1/2 E^+ K E + 1/2 A^+ Q A + Re(E^+ X A).
    Returns sorted real frequencies (positive branch) and eigvecs (A-part).
    Imaginary parts signal instability."""
    Kp = P.conj().T @ K @ P
    Qp = P.conj().T @ Q @ P
    d = P.shape[1]
    Xp = np.zeros((d, d), complex) if X is None else P.conj().T @ X @ P
    H = np.block([[Qp, Xp.conj().T], [Xp, Kp]])
    J = np.block([[np.zeros((d, d)), np.eye(d)], [-np.eye(d), np.zeros((d, d))]])
    w, v = np.linalg.eig(J @ H)
    om = 1j * w  # dpsi/dt = -i om psi  => eig = -i om
    return om, v[:d, :], P
