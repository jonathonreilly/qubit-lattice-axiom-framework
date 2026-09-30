"""Test E: node energies d0(k*) and rotation eigenvalues for the full-soldering NN law."""
import itertools, numpy as np
from common import O, rho, su2_of_rotation
from test_B_covariant import build, hop_set_nn, combo, dvec
basis, _ = build("full", hop_set_nn())
C, A = combo(basis)
E = {}
for k in itertools.product([0, np.pi], repeat=3):
    d, d0 = dvec(C, A, np.array(k))
    n = sum(1 for x in k if x > 1)
    E.setdefault(n, []).append((round(d0, 6), round(float(np.linalg.norm(d)), 12)))
for n in sorted(E): print(f"nodes with {n} coordinates = pi: count {len(E[n])}, energies {sorted(set(e[0] for e in E[n]))}, |d| = {max(e[1] for e in E[n]):.1e}")
# rotation operator on the walker coin: 90-degree turn about z, lifted (full soldering) vs trivial lift
g = next(g for g in O if np.array_equal(g, np.array([[0,-1,0],[1,0,0],[0,0,1]])))
U = su2_of_rotation(rho("full", g))
print("full soldering: U^4 =", np.round(np.linalg.matrix_power(U, 4), 6).tolist(), " eigenvalues of U:", np.round(np.linalg.eigvals(U), 4))
print("trivial soldering: U^4 = identity, eigenvalue 1")
