"""Probe B1 (readout weights): does a block-rung (two-qubit) consistency
condition force the site-rung (one-qubit) Born form?

Exploratory probe, not a theorem. Finite direction alphabet D = 26 cubic
directions (6 axes, 12 edge midpoints, 8 diagonals), closed under negation and
the proper cubic group.

Unknown: a frame function f on a finite set S of two-qubit pure states (up to
phase), with sum_{psi in B} f(psi) = 1 for every orthonormal basis B in a
supplied family. We compare
  dim(affine solution space)  vs  dim(Born forms psi -> <psi|A|psi>, tr A = 1)
and the dimension of the induced site marginal g(a) = f(a,b)+f(a,-b)
(Born: affine in a, 3 dims; generic: odd function on D, 13 dims).

Families:
  P  : product bases {a b, a -b, -a c, -a -c} and the qubit-swapped form
       (what sequential site-local records with neighbour conditioning give).
  P+U: P plus U.B for B in P, for each entangling 'apparatus' unitary U.
"""
import itertools
import numpy as np

rng = np.random.default_rng(0)

def dirs26():
    out = []
    for v in itertools.product([-1, 0, 1], repeat=3):
        if v != (0, 0, 0):
            v = np.array(v, float)
            out.append(v / np.linalg.norm(v))
    return out

D = dirs26()
SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)
PAULI = [I2, SX, SY, SZ]

def ket(n):
    P = (I2 + n[0] * SX + n[1] * SY + n[2] * SZ) / 2
    w, v = np.linalg.eigh(P)
    return v[:, np.argmax(w)]

K = [ket(n) for n in D]
idx_neg = [min(range(len(D)), key=lambda j: np.linalg.norm(D[j] + D[i])) for i in range(len(D))]

class StateBank:
    def __init__(self):
        self.keys = {}
        self.vecs = []
    def key(self, psi):
        P = np.outer(psi, psi.conj())
        return tuple(np.round(np.concatenate([P.real.ravel(), P.imag.ravel()]), 9))
    def get(self, psi):
        k = self.key(psi)
        if k not in self.keys:
            self.keys[k] = len(self.vecs)
            self.vecs.append(psi)
        return self.keys[k]

def product_bases():
    bases = []
    n = len(D)
    for a in range(n):
        na = idx_neg[a]
        for b in range(n):
            nb = idx_neg[b]
            for c in range(n):
                nc = idx_neg[c]
                B1 = [np.kron(K[a], K[b]), np.kron(K[a], K[nb]), np.kron(K[na], K[c]), np.kron(K[na], K[nc])]
                B2 = [np.kron(K[b], K[a]), np.kron(K[nb], K[a]), np.kron(K[c], K[na]), np.kron(K[nc], K[na])]
                bases.append(B1)
                bases.append(B2)
    return bases

def analyse(bases, label, bank=None):
    bank = StateBank() if bank is None else bank
    rowset = set()
    for B in bases:
        rowset.add(tuple(sorted(bank.get(psi) for psi in B)))
    rows = list(rowset)
    nS = len(bank.vecs)
    M = np.zeros((nS, nS))
    for ids in rows:
        ids = np.array(ids)
        M[np.ix_(ids, ids)] += 1.0
    w, V = np.linalg.eigh(M)
    tol = 1e-8 * max(1.0, w.max())
    rA = int((w > tol).sum())
    sol_dim = nS - rA
    null = V[:, w <= tol]
    class _A: pass
    A = _A(); A.shape = (len(rows),)
    # Born forms restricted to S
    Ppx = np.array([[np.real(np.vdot(psi, np.kron(p, q) @ psi)) for p in PAULI for q in PAULI] for psi in bank.vecs])
    born_dim = np.linalg.matrix_rank(Ppx) - 1
    # induced site marginal g(a) = f(a,b0) + f(a,-b0), b0 = first direction
    b0 = 0
    prod_ids = []
    ok = True
    for a in range(len(D)):
        k1 = bank.keys.get(bank.key(np.kron(K[a], K[b0])))
        k2 = bank.keys.get(bank.key(np.kron(K[a], K[idx_neg[b0]])))
        if k1 is None or k2 is None:
            ok = False
            break
        prod_ids.append((k1, k2))
    if ok:
        G = np.array([null[k1] + null[k2] for k1, k2 in prod_ids])  # 26 x sol_dim
        g_dim = np.linalg.matrix_rank(G, tol=1e-8)
    else:
        g_dim = None
    print(f"[{label}] states={nS} bases={len(rows)} uniqueRows={A.shape[0]} rank={rA} "
          f"solution_dim(homog)={sol_dim} born_dim={born_dim} excess={sol_dim - born_dim} "
          f"site_marginal_free_dim={g_dim} (Born site marginal dim = 3)")
    return bank

CZ = np.diag([1, 1, 1, -1]).astype(complex)
CNOT = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]], complex)
def zz(theta):
    return np.diag(np.exp(-1j * theta * np.array([1, -1, -1, 1])))
def xx_yy(theta):  # partial iSWAP-like exchange
    H = (np.kron(SX, SX) + np.kron(SY, SY)) / 2
    w, v = np.linalg.eigh(H)
    return v @ np.diag(np.exp(-1j * theta * w)) @ v.conj().T

if __name__ == "__main__":
    PB = product_bases()
    analyse(PB, "P product-only")
    for name, Us in [("P+CZ", [CZ]),
                     ("P+CZ+CNOT", [CZ, CNOT]),
                     ("P+ZZ(pi/8)", [zz(np.pi / 8)]),
                     ("P+exchange(pi/4)", [xx_yy(np.pi / 4)]),
                     ("P+CZ+ZZ(pi/8)+exchange(pi/4)+exchange(0.3)", [CZ, zz(np.pi / 8), xx_yy(np.pi / 4), xx_yy(0.3)])]:
        bases = list(PB)
        for U in Us:
            bases += [[U @ psi for psi in B] for B in PB]
        analyse(bases, name)
