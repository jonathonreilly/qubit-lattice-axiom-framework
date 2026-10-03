"""GNVW index of small 1D QCAs on a qubit ring via the Choi state (comparator
formula, Gong-Suenderhauf-Schuch-Cirac style):
    log2 ind = [ I(A':B) - I(A:B') ] / 2      (mutual informations in bits)
A, B adjacent system intervals, primes = ancilla copies.  Expected:
right shift -> +1, left shift -> -1, any circuit -> 0, independent of the
random gates.  N = 10 qubits (20-qubit Choi vector, 16 MB)."""
import numpy as np

rng = np.random.default_rng(3)
N = 10


def haar(d):
    z = (rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))


def bell_state():
    psi = np.zeros([2] * (2 * N), complex)
    for bits in range(2 ** N):
        idx = [(bits >> i) & 1 for i in range(N)]
        psi[tuple(idx + idx)] = 1.0
    return psi / np.sqrt(2 ** N)


def gate(psi, G, i, j):
    G = G.reshape(2, 2, 2, 2)
    psi = np.tensordot(G, psi, axes=([2, 3], [i, j]))
    return np.moveaxis(psi, [0, 1], [i, j])


def shift(psi, s):  # content of system site x moves to x+s
    perm = list(range(2 * N))
    for x in range(N):
        perm[(x + s) % N] = x
    return np.transpose(psi, perm)


def S(psi, keep):
    rest = [i for i in range(2 * N) if i not in keep]
    M = np.transpose(psi, keep + rest).reshape(2 ** len(keep), -1)
    ev = np.linalg.eigvalsh(M @ M.conj().T)
    ev = ev[ev > 1e-14]
    return float(-np.sum(ev * np.log2(ev)))


def index_bits(psi, A, B):
    Ap = [a + N for a in A]
    Bp = [b + N for b in B]
    I1 = S(psi, Ap) + S(psi, B) - S(psi, Ap + B)
    I2 = S(psi, A) + S(psi, Bp) - S(psi, A + Bp)
    return (I1 - I2) / 2


def circuit(psi, layers):
    for L in range(layers):
        for x in range(L % 2, N, 2):
            psi = gate(psi, haar(4), x, (x + 1) % N)
    return psi


A, B = [0, 1, 2], [3, 4, 5]
for name, s, layers in [("right shift", 1, 0), ("left shift", -1, 0), ("1-layer circuit", 0, 1),
                        ("right shift o 1-layer circuit", 1, 1), ("left shift o 1-layer circuit", -1, 1),
                        ("2-layer circuit", 0, 2)]:
    psi = circuit(bell_state(), layers)
    psi = shift(psi, s)
    print(f"{name:32s}: log2 ind = {index_bits(psi, A, B):+.10f}")
# two-slot counter-conveyor: 5 cells x 2 slots; slot a (even qubits) moves +1 cell,
# slot b (odd qubits) moves -1 cell, after a random 1-layer circuit
psi = circuit(bell_state(), 1)
perm = list(range(2 * N))
for cell in range(N // 2):
    a, b = 2 * cell, 2 * cell + 1
    perm[(a + 2) % N] = a       # slot a content -> next cell
    perm[(b - 2) % N] = b       # slot b content -> previous cell
psi = np.transpose(psi, perm)
print(f"{'two-slot counter-conveyor':32s}: log2 ind = {index_bits(psi, [0, 1, 2, 3], [4, 5, 6, 7]):+.10f}")
