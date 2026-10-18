"""Lemma F (single commuting layer bounded light cone) and the 'layer must be commuting' remark."""
import numpy as np, scipy.linalg as sl, itertools
from rv_common import check, total
rng = np.random.default_rng(5)
L = 8
def op(site_ops):
    M = np.array([[1.0+0j]])
    for i in range(L): M = np.kron(M, site_ops.get(i, np.eye(2)))
    return M
def gate(g, i):   # 2-site gate on (i, i+1) (i < L-1) as full matrix
    return np.kron(np.kron(np.eye(2**i), g), np.eye(2**(L-i-2)))
def supp(A):
    s = []
    for i in range(L):
        T = A.reshape([2]*(2*L)); # check whether A acts trivially at site i
        Tm = np.moveaxis(T, [i, L+i], [0, 1]).reshape(2, 2, -1)
        tr = (Tm[0, 0] + Tm[1, 1]) / 2
        if np.linalg.norm(Tm[0, 1]) + np.linalg.norm(Tm[1, 0]) + np.linalg.norm(Tm[0, 0] - tr) > 1e-8: s.append(i)
    return s
# commuting non-diagonal layer: V^{(x)} diag(random CZ-phase) V^dag, open chain (all translates commute)
V = sl.expm(1j * (0.7 * np.array([[0, 1], [1, 0]]) + 0.4 * np.diag([1, -1])))
Vt = op({i: V for i in range(L)})
D = np.eye(1)
ph = np.exp(1j * rng.normal(size=4))
Dg = np.diag(ph)
U = np.eye(2**L, dtype=complex)
for i in range(L - 1): U = gate(Dg, i) @ U
U = Vt @ U @ Vt.conj().T
X3 = op({3: np.array([[0, 1], [1, 0]])})
A = X3.copy(); sizes = []
for n in range(1, 9):
    A = U @ A @ U.conj().T; sizes.append(len(supp(A)))
check("Lemma F: commuting (non-diagonal) layer, |supp alpha^n(X_3)| <= |S-S| = 3 for n=1..8", max(sizes) <= 3, sizes)
# ordered staircase of non-commuting SWAPs on a ring = cyclic shift (TI, well defined, U(1)-conserving)
SW = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]], complex)
S = np.eye(2**L, dtype=complex)
for i in range(L - 1): S = gate(SW, i) @ S
Z0 = op({0: np.diag([1, -1])})
img = S @ Z0 @ S.conj().T
tgt = [i for i in range(L) if np.allclose(img, op({i: np.diag([1, -1])}))]
check("staircase of non-commuting SWAP translates acts as a translation (sigma^z_0 -> single site)", len(tgt) == 1, tgt)
check("SWAP translates do not commute", not np.allclose(gate(SW,0)@gate(SW,1), gate(SW,1)@gate(SW,0)))
total()
