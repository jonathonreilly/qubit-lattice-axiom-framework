"""Coordinator check of A10 S1/S4, written from the statements.
S1: 2-qubit unitaries commuting with u(x)u for all u in SU(2) are phase*exp(-i th SWAP) (check: commutant dimension 2).
S4: 1D brickwork of partial swaps exp(-i th SWAP) on even then odd bonds, one excitation, 2-site cell (cell momentum K):
    cos(omega) = cos(th_e) cos(th_o) - sin(th_e) sin(th_o) cos(K)  (eigenphases measured relative to the |00> phase)."""
import numpy as np
from scipy.linalg import expm
rng = np.random.default_rng(3)
SW = np.eye(4)[[0, 2, 1, 3]]
# S1: commutant of {u (x) u}: solve [X, u(x)u] = 0 for random u's
from scipy.stats import unitary_group
A = []
for _ in range(6):
    u = unitary_group.rvs(2, random_state=rng); U2 = np.kron(u, u)
    A.append(np.kron(np.eye(4), U2) - np.kron(U2.T, np.eye(4)))   # vec(XU - UX) = (I(x)U ... ) form
M = np.vstack(A)
sv = np.linalg.svd(M, compute_uv=False)
print("S1: commutant dimension of {u(x)u} =", int(np.sum(sv < 1e-9)), "(expected 2: span{1, SWAP})")
# S4: single excitation on a ring of 2N sites; even bonds (0,1),(2,3)..., odd bonds (1,2),(3,4)...
N = 40; L = 2 * N
def layer(theta, offset):
    U = np.eye(L, dtype=complex)
    g = expm(-1j * theta * SW)          # one-excitation block of the gate in basis {|10>,|01>}: rows/cols 1,2 of SW basis
    blk = g[np.ix_([1, 2], [1, 2])] / g[0, 0]   # relative to |00> phase
    for p in range(N):
        a, b = (2 * p + offset) % L, (2 * p + 1 + offset) % L
        U[np.ix_([a, b], [a, b])] = blk
    return U
worst = 0.0
for te, to in [(0.3, 0.3), (0.3, 0.7), (1.1, 0.4), (np.pi/4, np.pi/4)]:
    W = layer(to, 1) @ layer(te, 0)
    ev = np.angle(np.linalg.eigvals(W) * np.exp(-1j * (te + to)))   # remove the overall gate phase e^{i(th_e+th_o)}
    Ks = 2 * np.pi * np.arange(N) / N
    pred = np.array([np.arccos(np.clip(np.cos(te)*np.cos(to) - np.sin(te)*np.sin(to)*np.cos(K), -1, 1)) for K in Ks])
    meas = np.sort(np.abs(ev)); predicted = np.sort(np.concatenate([pred, pred]))
    err = np.max(np.abs(meas - predicted)); worst = max(worst, err)
    print("th_e=%.3f th_o=%.3f: max |measured - formula| eigenphase = %.2e" % (te, to, err))
print("worst:", "%.2e" % worst)
