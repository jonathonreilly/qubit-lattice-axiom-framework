"""Common tools for the T09 tick census: cubic rotation group, its double cover irreps,
covariant radius-1 (cross-support) unitary ticks on Z^3 with C^s per site."""
import itertools
import numpy as np
from scipy.linalg import expm, null_space

# ---------- the 24 proper rotations of the cube (signed permutation matrices, det +1) ----------
def rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            M = np.zeros((3, 3))
            for r, c in enumerate(perm):
                M[r, c] = signs[r]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    assert len(out) == 24
    return out

ROTS = rotations()
E = np.eye(3)
DIRS = [E[0], -E[0], E[1], -E[1], E[2], -E[2]]          # order: +x -x +y -y +z -z
DIR_LABEL = ['+x', '-x', '+y', '-y', '+z', '-z']

def dir_index(v):
    for i, d in enumerate(DIRS):
        if np.allclose(d, v):
            return i
    raise ValueError

# ---------- SU(2) lift of a rotation ----------
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
PAULI = [SX, SY, SZ]

def rot_axis_angle(R):
    # rotation vector via matrix log
    from scipy.spatial.transform import Rotation
    rv = Rotation.from_matrix(R).as_rotvec()
    return rv

def su2_lift(R):
    rv = rot_axis_angle(R)
    th = np.linalg.norm(rv)
    if th < 1e-12:
        return np.eye(2, dtype=complex)
    n = rv / th
    return expm(-1j * th / 2 * sum(n[i] * PAULI[i] for i in range(3)))

def spin_matrices(j):
    dim = int(round(2 * j + 1))
    m = np.array([j - i for i in range(dim)])
    Jz = np.diag(m).astype(complex)
    Jp = np.zeros((dim, dim), complex)
    for i in range(1, dim):
        mm = m[i]
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - mm * (mm + 1))
    Jm = Jp.conj().T
    Jx = (Jp + Jm) / 2
    Jy = (Jp - Jm) / (2j)
    return Jx, Jy, Jz

def D_j(j, R):
    rv = rot_axis_angle(R)
    th = np.linalg.norm(rv)
    Jx, Jy, Jz = spin_matrices(j)
    if th < 1e-12:
        return np.eye(Jx.shape[0], dtype=complex)
    n = rv / th
    return expm(-1j * th * (n[0] * Jx + n[1] * Jy + n[2] * Jz))

# ---------- sign character of S4 (permutation of the 4 body diagonals) ----------
DIAG = [np.array(v) for v in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1)]]
def sgn(R):
    perm = []
    for d in DIAG:
        w = R @ d
        for k, e in enumerate(DIAG):
            if np.allclose(w, e) or np.allclose(w, -e):
                perm.append(k)
    assert sorted(perm) == [0, 1, 2, 3]
    # parity
    s = 1
    p = perm[:]
    for i in range(4):
        while p[i] != i:
            j = p[i]
            p[i], p[j] = p[j], p[i]
            s = -s
    return s

# ---------- irreps of O (integer) and 2O (spinorial) as functions R -> matrix ----------
def _axis_perm(R):
    P = np.abs(R)
    return P

def irrep_matrix(name, R):
    if name == 'A1':
        return np.eye(1, dtype=complex)
    if name == 'A2':
        return np.array([[sgn(R)]], dtype=complex)
    if name == 'T1':
        return R.astype(complex)
    if name == 'T2':
        return sgn(R) * R.astype(complex)
    if name == 'E':
        P = _axis_perm(R)
        # basis of the complement of (1,1,1)
        B = np.array([[1, -1, 0], [1, 1, -2]], float)
        B = B / np.linalg.norm(B, axis=1, keepdims=True)
        return (B @ P @ B.T).astype(complex)
    if name == 'H1':      # spin-1/2 = E1/2
        return su2_lift(R)
    if name == 'H2':      # E5/2 = spin-1/2 x sign
        return sgn(R) * su2_lift(R)
    if name == 'G':       # spin-3/2 = G
        return D_j(1.5, R)
    raise ValueError(name)

IRREP_DIM = {'A1': 1, 'A2': 1, 'E': 2, 'T1': 3, 'T2': 3, 'H1': 2, 'H2': 2, 'G': 4}
INT_IRREPS = ['A1', 'A2', 'E', 'T1', 'T2']
SPIN_IRREPS = ['H1', 'H2', 'G']

def rep_matrix(names, R):
    blocks = [irrep_matrix(n, R) for n in names]
    dim = sum(b.shape[0] for b in blocks)
    M = np.zeros((dim, dim), complex)
    i = 0
    for b in blocks:
        d = b.shape[0]
        M[i:i + d, i:i + d] = b
        i += d
    return M

def check_rep(names):
    """verify homomorphism up to sign for spinorial reps, exactly for integer reps"""
    spin = names[0] in SPIN_IRREPS
    for R1 in ROTS[:8]:
        for R2 in ROTS[:8]:
            a = rep_matrix(names, R1) @ rep_matrix(names, R2)
            b = rep_matrix(names, R1 @ R2)
            if spin:
                ok = np.allclose(a, b) or np.allclose(a, -b)
            else:
                ok = np.allclose(a, b)
            if not ok:
                return False
    return True

# ---------- covariant space of the radius-1 tick ----------
def rotation_taking(v_from, v_to):
    for i, R in enumerate(ROTS):
        if np.allclose(R @ v_from, v_to):
            return i
    raise ValueError

def covariant_basis(names):
    """returns (dim, basis0 (list of s x s matrices for A_0), basisN (list of dicts dir->matrix) ) for complex coefficients"""
    s = sum(IRREP_DIM[n] for n in names)
    rho = {i: rep_matrix(names, R) for i, R in enumerate(ROTS)}
    # A_0: commutes with all rho
    cons = []
    for i in rho:
        r = rho[i]
        cons.append(np.kron(r, r.conj()) - np.eye(s * s))    # vec(r A r^dag) = (r kron conj(r)) vec(A) (row-major)
    C0 = np.vstack(cons)
    N0 = null_space(C0)
    basis0 = [N0[:, j].reshape(s, s) for j in range(N0.shape[1])]
    # A_{+z}: invariant under stabiliser of e_z
    ez = E[2]
    stab = [i for i, R in enumerate(ROTS) if np.allclose(R @ ez, ez)]
    consz = [np.kron(rho[i], rho[i].conj()) - np.eye(s * s) for i in stab]
    Nz = null_space(np.vstack(consz))
    basisN = []
    for j in range(Nz.shape[1]):
        Az = Nz[:, j].reshape(s, s)
        d = {}
        for di, v in enumerate(DIRS):
            r = rho[rotation_taking(ez, v)]
            d[di] = r @ Az @ r.conj().T
        basisN.append(d)
    return s, basis0, basisN

def build_A(s, basis0, basisN, c0, cN):
    A0 = sum(c * b for c, b in zip(c0, basis0)) if basis0 else np.zeros((s, s), complex)
    A = {di: sum(c * d[di] for c, d in zip(cN, basisN)) if basisN else np.zeros((s, s), complex) for di in range(6)}
    return A0, A

def U_of_k(A0, A, k):
    U = A0.copy()
    for di, v in enumerate(DIRS):
        U = U + A[di] * np.exp(1j * (k @ v))
    return U
