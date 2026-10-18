"""COL-1 check 2: ownership lemma illustrations (class M, qubits).

Attempt: SU(3)_x acts on qubits S_x (as 3 + singlets, random basis); SU(3)_{x+1} must act on the
translate S_x + 1 and commute.  Compute the commutant of A_x inside the operators supported on
S_x + 1 and decide whether that commutant can host any nontrivial su(3) (needs a simple block M_n, n >= 3).
"""
import numpy as np
from scipy.linalg import null_space
from su3common import T

rng = np.random.default_rng(20261014)

def haar(n):
    z = (rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / np.abs(np.diag(r)))

def kron(*ms):
    out = np.array([[1.0 + 0j]])
    for m in ms:
        out = np.kron(out, m)
    return out

def commutant_in(gens_big, k_left, k_right, nq):
    """Operators 1_{k_left qubits} (x) B (x) 1_{k_right} with B on nq qubits commuting with gens_big."""
    dB = 2 ** nq
    basis = []
    for i in range(dB):
        for j in range(dB):
            E = np.zeros((dB, dB), complex); E[i, j] = 1
            basis.append(kron(np.eye(2 ** k_left), E, np.eye(2 ** k_right)))
    rows = []
    for g in gens_big:
        rows.append(np.stack([(g @ b - b @ g).ravel() for b in basis], axis=1))
    M = np.concatenate(rows, axis=0)
    ns = null_space(M)
    ops = [sum(ns[k, c] * basis[k] for k in range(len(basis))) for c in range(ns.shape[1])]
    return ops

def block_sizes(ops):
    """Structure of the *-algebra spanned by ops (assumed closed): sizes n_j of its simple blocks."""
    d = len(ops)
    if d == 0:
        return []
    # orthonormal basis of the algebra (as vectors)
    V = np.stack([o.ravel() for o in ops], axis=1)
    Q, _ = np.linalg.qr(V)
    alg = [Q[:, c].reshape(ops[0].shape) for c in range(Q.shape[1])]
    # centre: elements of alg commuting with all of alg
    rows = [np.stack([(a @ b - b @ a).ravel() for a in alg], axis=1) for b in alg]
    ns = null_space(np.concatenate(rows, axis=0))
    centre = [sum(ns[k, c] * alg[k] for k in range(d)) for c in range(ns.shape[1])]
    # random hermitian central element -> minimal central projections
    h = sum(rng.normal() * (z + z.conj().T) for z in centre)
    w, U = np.linalg.eigh(h)
    vals = []
    for v in w:
        if not any(abs(v - u) < 1e-8 for u in vals):
            vals.append(v)
    sizes = []
    for v in vals:
        Pv = U[:, np.abs(w - v) < 1e-8]
        P = Pv @ Pv.conj().T
        sub = [P @ a @ P for a in alg]
        S = np.stack([s.ravel() for s in sub], axis=1)
        r = np.linalg.matrix_rank(S, tol=1e-8)
        if r > 0:
            sizes.append(int(round(np.sqrt(r))))
    return sorted(sizes)

print("=== ownership illustrations (class M)")
for trial in range(3):
    # (1) S_x = {x, x+1} (2 qubits, C^4 = 3 + 1 in a random basis); candidate partner on {x+1, x+2}
    V = haar(4)
    gens = [kron(V @ np.pad(T[a], ((0, 1), (0, 1))) @ V.conj().T, np.eye(2)) for a in range(8)]
    C = commutant_in(gens, 1, 0, 2)
    bs = block_sizes(C)
    print("(1) trial %d: S_x={x,x+1}; commutant inside ops on {x+1,x+2}: dim %d, simple blocks %s, hosts su(3): %s"
          % (trial, len(C), bs, any(b >= 3 for b in bs)))
# product-singlet basis (singlet = |11>)
perm = np.eye(4)[:, [0, 1, 2, 3]]
gens = [kron(np.pad(T[a], ((0, 1), (0, 1))), np.eye(2)) for a in range(8)]
C = commutant_in(gens, 1, 0, 2)
bs = block_sizes(C)
print("(1') singlet |11>, triplet {|00>,|01>,|10>}: commutant dim %d, blocks %s, hosts su(3): %s" % (len(C), bs, any(b >= 3 for b in bs)))

for trial in range(3):
    # (2) S_x = {x,x+1,x+2} (C^8 = 3 + 5 singlets, random basis); partner on {x+1,x+2,x+3}
    V = haar(8)
    gens = [kron(V @ np.pad(T[a], ((0, 5), (0, 5))) @ V.conj().T, np.eye(2)) for a in range(8)]
    C = commutant_in(gens, 1, 0, 3)
    bs = block_sizes(C)
    print("(2) trial %d: S_x={x..x+2} (3+5x1 random); commutant inside ops on {x+1..x+3}: dim %d, blocks %s, hosts su(3): %s"
          % (trial, len(C), bs, any(b >= 3 for b in bs)))
# (2') 3 + 3bar + 1 + 1 on three qubits, random basis
for trial in range(2):
    V = haar(8)
    Z = np.zeros((8, 8), complex)
    gens = []
    for a in range(8):
        g = Z.copy(); g[:3, :3] = T[a]; g[3:6, 3:6] = -np.conj(T[a])
        gens.append(kron(V @ g @ V.conj().T, np.eye(2)))
    C = commutant_in(gens, 1, 0, 3)
    bs = block_sizes(C)
    print("(2') trial %d: 3+3bar+1+1 random on {x..x+2}: commutant dim %d, blocks %s, hosts su(3): %s"
          % (trial, len(C), bs, any(b >= 3 for b in bs)))
print("Reading: generic overlapping placements leave no room; any successful overlap must split the shared")
print("qubits into sectors owned by one side at a time (Bravyi-Vyalyi form), which the token construction does.")
