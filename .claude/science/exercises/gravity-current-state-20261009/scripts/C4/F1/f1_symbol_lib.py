# shared symbol helpers (same conventions as f1_lattice_foliation_symbol.py)
import numpy as np
def _sym_basis():
    B = []
    for i in range(3):
        M = np.zeros((3, 3)); M[i, i] = 1; B.append(M)
    for (i, j) in [(0, 1), (1, 2), (0, 2)]:
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1 / np.sqrt(2); B.append(M)
    return B
BAS = _sym_basis()
def vec(M): return np.array([np.sum(M * b) for b in BAS])
def mat(v): return sum(v[a] * BAS[a] for a in range(6))
_eps = np.zeros((3, 3, 3))
for (i, j, k), s in {(0,1,2):1,(1,2,0):1,(2,0,1):1,(0,2,1):-1,(2,1,0):-1,(1,0,2):-1}.items():
    _eps[i, j, k] = s
def R_op(q):
    M = np.zeros((6, 6))
    for b in range(6):
        M[:, b] = vec(np.einsum('iab,jcd,a,c,bd->ij', _eps, _eps, q, q, BAS[b]))
    return -M   # sign fixed so h_TT:R(h_TT) = +q^2|h_TT|^2 (see f1_lattice_foliation_symbol.out)
def S_vec(q):
    return np.array([-(q @ q) * np.trace(BAS[b]) + q @ BAS[b] @ q for b in range(6)])
