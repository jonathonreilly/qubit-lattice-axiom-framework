"""C1 library: fibre representation of the dressed rotations, the eight-node step, node doublets,
and Nambu (BdG) constructions.  Built on chk_model.py (a verbatim copy of B18_check/chk_model.py,
which copies the scale-ladder runner's construction code).  Conventions are fixed numerically here
and verified in c1_reps.py (no convention is assumed without a test)."""
import itertools
import numpy as np
from chk_model import *          # noqa: F401,F403  (C, L, VERTS, VID, CORN, ROTS, rots, invs, trans, Ws, kst, ...)

I12 = np.eye(12)
UU = UH @ UL
def W(k): return SKc(k) @ RLk(k) @ UU          # the eight-node step S.R_L.U_H.U_L (unitary)
def Hbl(k, bl):
    return Hk(bl, k)

# ---------- fibre matrices U_g of the dressed rotations ----------
def fibre_matrix(P, s):
    """12x12 signed permutation: site-0 corner c -> image corner (the rotations fix site 0)."""
    U = np.zeros((12, 12))
    for ci, a in enumerate(loc0):
        v2, c2 = VERTS[P[a]]
        assert tuple(v2) == (0, 0, 0)
        U[CI[c2], ci] = (-1.0) ** int(s[a])
    return U

def find_kmap(U, M, fun, ks):
    """theta in pi Z^3 with U fun(k) U^T = fun(M k + theta) for all test k (None if absent)."""
    for th in itertools.product((0, 1), repeat=3):
        th = np.pi * np.array(th)
        if all(np.allclose(U @ fun(k) @ U.T, fun(M @ k + th), atol=1e-10) for k in ks):
            return th
    return None

_rng = np.random.default_rng(2026)
_KT = _rng.uniform(-np.pi, np.pi, (4, 3))
ROT = []   # list of dicts: M (3x3 int), U (12x12), th (pi-vector), name
for R, (P, s) in zip(ROTS, rots):
    U = fibre_matrix(P, s)
    th = find_kmap(U, R.astype(float), W, _KT)
    ROT.append(dict(M=R.astype(int), U=U, th=th))

def gk(g, k): return g['M'] @ k + g['th']
def same_k(a, b): return np.allclose(np.exp(1j * (np.asarray(a) - np.asarray(b))), 1, atol=1e-9)
def stab(k): return [i for i, g in enumerate(ROT) if same_k(gk(g, k), k)]

# conjugacy class labels for O (proper rotations) from the 3x3 matrix
def cls(M):
    t = int(round(np.trace(M)))
    if t == 3: return 'E'
    if t == 0: return 'C3'
    if t == 1: return 'C4'
    # t == -1: C2 (axis) or C2' (face diagonal)
    return 'C2' if np.count_nonzero(M) == 3 and all(abs(M[i, i]) == 1 for i in range(3)) else "C2'"
A2_O = {'E': 1, 'C3': 1, 'C2': 1, 'C4': -1, "C2'": -1}

# ---------- nodes ----------
Q_R = np.pi * np.ones(3)                       # pair momentum R = pi(1,1,1) = 2k* mod 2pi
NODES = {'k*': kst, '-k*': -kst}
for i, ax in enumerate('xyz'):
    NODES[f'k*+pi e{ax}'] = kst + np.pi * np.eye(3)[i]
    NODES[f'-k*+pi e{ax}'] = -kst + np.pi * np.eye(3)[i]
NVEC = {nm: tuple(int(x) for x in np.round(np.mod((k - kst) / np.pi, 2)).astype(int) % 2) for nm, k in NODES.items()}

def level(k, E, tol=1e-7):
    """orthonormal basis of the eigenspace of W(k) at eigenphase E."""
    e, V = np.linalg.eig(W(k)); ph = np.angle(e)
    sel = np.abs(wrap(ph - E)) < tol
    Qm, _ = np.linalg.qr(V[:, sel]); return Qm

def dHk(bl, k, j):
    H = np.zeros((12, 12), complex)
    for sh, Mx in bl.items(): H += 1j * sh[j] * Mx * np.exp(1j * np.dot(k, sh))
    return H
def dW(k, j): return (dHk(blS, k, j) @ RLk(k) + SKc(k) @ dHk(blL, k, j)) @ UU
PAU = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
def weyl_data(k, Qm):
    """first-order degenerate PT on a 2-fold level of W: velocity matrix B, tilt a, chirality sign det B."""
    Wk = W(k); A = [-1j * Qm.conj().T @ Wk.conj().T @ dW(k, j) @ Qm for j in range(3)]
    a = np.array([np.trace(x).real / 2 for x in A])
    B = np.array([[np.trace(A[j] @ PAU[b]).real / 2 for b in range(3)] for j in range(3)])
    return a, B

# ---------- Nambu / BdG step ----------
def nambu_step(k, Q=Q_R, mu=np.pi / 2):
    """Nambu form of exp(-i mu N) W acting on (c_k, c^dag_{Q-k}): diag(e^{-i mu} W(k), e^{i mu} W(Q-k)^*)."""
    Z = np.zeros((24, 24), complex)
    Z[:12, :12] = np.exp(-1j * mu) * W(k); Z[12:, 12:] = np.exp(1j * mu) * W(Q - k).conj()
    return Z
def pair_layer(Dk, tau=1.0):
    """exp(-i tau [[0, D],[D^dag, 0]]) for a 12x12 pairing matrix D(k)."""
    h = np.zeros((24, 24), complex); h[:12, 12:] = Dk; h[12:, :12] = Dk.conj().T
    w_, V_ = np.linalg.eigh(h); return (V_ * np.exp(-1j * tau * w_)) @ V_.conj().T
def bdg_quasienergies(k, Dfun, tau=1.0, Q=Q_R, mu=np.pi / 2):
    Wb = pair_layer(Dfun(k), tau) @ nambu_step(k, Q, mu)
    return np.angle(np.linalg.eigvals(Wb))

# Wilson-type scalar: w(k) = 3 - sum_{i<j} cos q_i cos q_j with q = k - k*;  w = 0 only at +-k*, w = 4 at the six doublers
SG = np.array([1, -1, 1])
def wfun(k):
    s = np.sin(k) * SG
    return 3.0 - (s[0] * s[1] + s[1] * s[2] + s[2] * s[0])
