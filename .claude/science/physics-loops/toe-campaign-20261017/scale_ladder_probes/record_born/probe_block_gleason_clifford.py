"""Probe B2: interlocking (group-closed) block-rung frames.
Alphabet D14 = 6 axes + 8 cube diagonals (cubic-covariant). Frames = images of
all product bases over D14 under sampled elements of the two-qubit Clifford
group <H_i, S_i, CZ> (local part = proper cubic rotations of the Bloch sphere).
Question: is the frame function forced to the Born form (15 dims) and the
site marginal g(a) to the affine Born form (3 dims; generic odd on D14 = 7)?
Control: same with only local Cliffords (no CZ) -> no entangling apparatus.
"""
import itertools, sys
import numpy as np
sys.path.insert(0, '.')
import probe_block_gleason as pb

rng = np.random.default_rng(1)
D = [d for d in pb.D if np.sum(np.abs(d) > 1e-9) in (1, 3)]
pb.D = D
pb.K = [pb.ket(n) for n in D]
pb.idx_neg = [min(range(len(D)), key=lambda j: np.linalg.norm(D[j] + D[i])) for i in range(len(D))]
H = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
S = np.diag([1, 1j])
I2 = np.eye(2)
gens_local = [np.kron(H, I2), np.kron(I2, H), np.kron(S, I2), np.kron(I2, S)]
gens_ent = gens_local + [np.diag([1, 1, 1, -1]).astype(complex)]

def sample(gens, n, L=40):
    out = [np.eye(4, dtype=complex)]
    for _ in range(n):
        U = np.eye(4, dtype=complex)
        for g in rng.integers(0, len(gens), L):
            U = gens[g] @ U
        out.append(U)
    return out

PB = pb.product_bases()
for label, gens, n in [("local-Clifford only (no entangler)", gens_local, 150),
                       ("Clifford with CZ, 150 elems", gens_ent, 150),
                       ("Clifford with CZ, 600 elems", gens_ent, 600)]:
    Us = sample(gens, n)
    bases = [[U @ psi for psi in B] for U in Us for B in PB]
    pb.analyse(bases, label)
