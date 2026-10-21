"""C4b-01: numerical sanity checks of the recalled GNVW index properties used in the index lemma.

NOT a proof.  The index lemma (NOTE.md, Lemma 1) relies on recalled properties of the GNVW index
of 1D QCAs (Gross-Nesme-Vogts-Werner, CMP 310 (2012) 419):
  (I2) multiplicativity, (I4) ind(right shift of a d-dim cell) = d,
  (I7) ind(P a P^-1) = 1/ind(a) for the spatial reflection P,
  (I8) ind(u a u^-1) = ind(a) for an on-site unitary layer u (follows from I2 + ind(u) = 1).
Here we evaluate the index of small 1D qubit-ring QCAs by an independent formula, the Choi-state
mutual-information expression (recalled from Ranard-Walter-Witteveen, Ann. Henri Poincare 23
(2022) 3905):
    log2 ind(a) = ( I(a_in : b_out) - I(a_out : b_in) ) / 2
for adjacent intervals a (left) and b (right) of length >= range, evaluated in the Choi state
(U (x) 1)|Omega>.  Sign convention fixed by hand on the right shift: output site j = input j-1,
so b_out is correlated with a_in through one site => I(a_in:b_out)=2 bits, ind = 2.
Expected constants come from the theory statements (I4),(I7),(I2), not from this code.
"""
import numpy as np
from c4b_common import check, total

rng = np.random.default_rng(20261018)
N = 8          # ring sites
n = 2          # interval length (>= range of every test QCA)
D = 2 ** N


def perm_unitary(f):
    """unitary moving the qubit at site j to site f(j)."""
    U = np.zeros((D, D))
    for idx in range(D):
        bits = [(idx >> (N - 1 - j)) & 1 for j in range(N)]
        out = [0] * N
        for j in range(N):
            out[f(j) % N] = bits[j]
        o = 0
        for j in range(N):
            o = (o << 1) | out[j]
        U[o, idx] = 1
    return U.astype(complex)


def two_site(g, i, j):
    """embed 4x4 gate g on sites (i,j) (ordered) of the ring."""
    U = np.zeros((D, D), complex)
    for idx in range(D):
        bi = (idx >> (N - 1 - i)) & 1
        bj = (idx >> (N - 1 - j)) & 1
        col = 2 * bi + bj
        for row in range(4):
            amp = g[row, col]
            if amp == 0:
                continue
            ni, nj = row >> 1, row & 1
            o = idx
            o = (o & ~(1 << (N - 1 - i))) | (ni << (N - 1 - i))
            o = (o & ~(1 << (N - 1 - j))) | (nj << (N - 1 - j))
            U[o, idx] += amp
    return U


def haar(d):
    z = (rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))) / np.sqrt(2)
    q, r = np.linalg.qr(z)
    return q * (np.diag(r) / abs(np.diag(r)))


def onsite(us):
    U = np.array([[1.0 + 0j]])
    for u in us:
        U = np.kron(U, u)
    return U


def brick(parity):
    U = np.eye(D, dtype=complex)
    for j in range(parity, N, 2):
        U = two_site(haar(4), j, (j + 1) % N) @ U
    return U


def entropy(rho):
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-12]
    return float(-(w * np.log2(w)).sum())


def rdm(psi, keep):
    """psi over 2N qubits: qubits 0..N-1 = output, N..2N-1 = input copy."""
    t = psi.reshape([2] * (2 * N))
    rest = [q for q in range(2 * N) if q not in keep]
    t = np.transpose(t, keep + rest).reshape(2 ** len(keep), -1)
    return t @ t.conj().T


def mi(psi, A, B):
    return entropy(rdm(psi, A)) + entropy(rdm(psi, B)) - entropy(rdm(psi, A + B))


def index(U):
    # Choi state: sum_i U|i> (x) |i> / sqrt(D)
    psi = (U / np.sqrt(D)).reshape(-1)        # index (out, in) -> row-major = out (x) in
    a = list(range(0, n))
    b = list(range(n, 2 * n))
    a_in = [N + q for q in a]
    b_in = [N + q for q in b]
    return 2 ** ((mi(psi, a_in, b) - mi(psi, a, b_in)) / 2)


S = perm_unitary(lambda j: j + 1)          # right shift
Sl = perm_unitary(lambda j: j - 1)         # left shift
P = perm_unitary(lambda j: -j)             # reflection j -> -j
W = brick(1) @ brick(0)                    # depth-2 brickwork (range 2), index 1 expected
W1 = brick(0)                               # depth-1 (range 1)
u = onsite([haar(2) for _ in range(N)])

cases = [
    ("identity", np.eye(D, dtype=complex), 1.0),
    ("right shift (I4: d=2)", S, 2.0),
    ("left shift", Sl, 0.5),
    ("depth-2 random brickwork circuit", W, 1.0),
    ("shift o depth-1 circuit", S @ W1, 2.0),
    ("reflection-conjugate P(S W1)P^-1  (I7)", P @ S @ W1 @ P.conj().T, 0.5),
    ("reflection-conjugate of circuit P W P^-1", P @ W @ P.conj().T, 1.0),
    ("on-site conjugate u(S W1)u^-1  (I8)", u @ S @ W1 @ u.conj().T, 2.0),
    ("S o S (I2: 2*2)", S @ S, 4.0),
    ("S o Sl (I2: 2*(1/2))", S @ Sl, 1.0),
]
for name, U, exp in cases:
    assert np.allclose(U.conj().T @ U, np.eye(D), atol=1e-10)
    val = index(U)
    check(f"GNVW index {name} = {exp}", abs(val - exp) < 1e-8, f"computed {val:.10f}")

total()
