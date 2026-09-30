"""R2 test: is psi = sqrt(mu) the exact ground state of a local frustration-free projector Hamiltonian?
Open 2x2x2 cube, static law of the (3,1,2) product rule. H = sum_x (1 - A_x), A_x = projector onto the
site-x conditional state given its window neighbours (a NN-local operator)."""
import itertools, time
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh

t0 = time.time()
P_, Q_, R_ = 3.0, 1.0, 2.0
PHI = np.zeros((6, 6))
for s in range(6):
    for t in range(6):
        PHI[s, t] = P_ if s == t else (Q_ if s // 2 == t // 2 else R_)
sites = list(itertools.product((0, 1), repeat=3))
sid = {c: i for i, c in enumerate(sites)}
nbrs = [[sid[tuple(c[k] ^ (1 if k == j else 0) for k in range(3))] for j in range(3)] for c in sites]
edges = sorted({tuple(sorted((i, j))) for i in range(8) for j in nbrs[i]})
assert len(edges) == 12
letters = "abcdefgh"

# mu(v) proportional to prod_edges phi(v_i, v_j)
mu = np.ones((6,) * 8)
for (i, j) in edges:
    shape = [1] * 8; shape[i] = 6; shape[j] = 6
    T = PHI if i < j else PHI.T
    mu = mu * T.reshape(shape)
mu /= mu.sum()
psi = np.sqrt(mu)

# sqrt of conditional r(s | nbrs) for each site; tensor with axes [x, n1, n2, n3]
sqR = []
for x in range(8):
    w = np.ones((6, 6, 6, 6))
    for k, y in enumerate(nbrs[x]):
        shape = [1] * 4; shape[0] = 6; shape[1 + k] = 6
        w = w * PHI.reshape(shape)  # phi(s, eta_k): axis0=s, axis(1+k)=eta_k
    w = w / w.sum(axis=0, keepdims=True)
    sqR.append(np.sqrt(w))

def apply_A(x, v):
    sub = letters[x] + "".join(letters[y] for y in nbrs[x])
    rest = letters.replace(letters[x], "")
    c = np.einsum(f"{letters},{sub}->{rest}", v, sqR[x], optimize=True)
    return np.einsum(f"{sub},{rest}->{letters}", sqR[x], c, optimize=True)

# 1. A_x psi = psi
err = max(np.abs(apply_A(x, psi) - psi).max() for x in range(8))
print(f"max_x ||A_x psi - psi||_inf = {err:.2e}")
# 2. A_x is a projector (spot check on a random vector)
rv = np.random.default_rng(0).normal(size=(6,) * 8)
Ar = apply_A(3, rv)
print(f"projector check ||A(A v) - A v||_inf = {np.abs(apply_A(3, Ar) - Ar).max():.2e}")

def matvec(v):
    v = v.reshape((6,) * 8)
    out = 8 * v
    for x in range(8):
        out = out - apply_A(x, v)
    return out.reshape(-1)

dim = 6 ** 8
Hop = LinearOperator((dim, dim), matvec=matvec, dtype=np.float64)
Hpsi = matvec(psi.reshape(-1))
print(f"||H psi||_inf = {np.abs(Hpsi).max():.2e}   [{time.time()-t0:.0f}s]")
w = eigsh(Hop, k=3, which="SA", return_eigenvectors=False, tol=1e-10, ncv=30)
w = np.sort(w)
print("lowest three eigenvalues of H:", w, f"  [{time.time()-t0:.0f}s]")
ok = err < 1e-12 and w[0] < 1e-9 and w[1] > 0.05
print("R2 TEST:", "PASS (unique gapped frustration-free local parent)" if ok else ("FAIL" if err > 1e-12 or w[1] < 1e-6 else "in between; report as measured"))
