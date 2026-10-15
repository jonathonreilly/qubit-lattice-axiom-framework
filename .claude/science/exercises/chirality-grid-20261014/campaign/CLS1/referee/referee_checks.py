"""Independent small checks for the CLS-1 referee report."""

from itertools import product

import numpy as np


corners = list(product((0, 1), repeat=3))
momenta = [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

# A translation residue survives all three condensates iff K.n is even.
residual = [
    n
    for n in corners
    if all(sum(k[i] * n[i] for i in range(3)) % 2 == 0 for k in momenta)
]
print("residual residues:", residual)

sectors = {}
for q in corners:
    character = tuple((-1) ** sum(q[i] * n[i] for i in range(3)) for n in residual)
    chirality = (-1) ** sum(q)
    sectors.setdefault(character, []).append((q, chirality))
for character, entries in sectors.items():
    print("sector", character, "entries", entries, "index", sum(x[1] for x in entries))

# At order-two corners Q=-Q, so Yukawa sums and hopping differences coincide.
for q, qp in product(corners, repeat=2):
    yukawa = tuple((q[i] + qp[i]) % 2 for i in range(3))
    hopping = tuple((qp[i] - q[i]) % 2 for i in range(3))
    assert yukawa == hopping
print("sum/difference charge identity: PASS for all 64 ordered corner pairs")

# Cubic-symmetric light-light density matrix and its energy levels.
adjacency = np.ones((3, 3)) - np.eye(3)
print("light adjacency eigenvalues:", np.linalg.eigvalsh(adjacency))

# Odd-fold filter: three light entries have f=0 and hw3 has f=2.
def phi(kappa):
    matrix = np.diag([0.0, 2.0, 0.0, 0.0])
    return matrix + kappa * (np.ones((4, 4)) - np.eye(4))


for kappa in (0.0, 0.33, 4.0 / 3.0):
    matrix = phi(kappa)
    print(
        "kappa", kappa,
        "rank", np.linalg.matrix_rank(matrix, tol=1e-10),
        "det", np.linalg.det(matrix),
        "singular", np.linalg.svd(matrix, compute_uv=False),
    )
print("analytic det Phi(P) = kappa^3 * (4 - 3*kappa)")

# The Table-1 SME numbers are coefficient limits.  A two-flavour purely
# off-diagonal coefficient x has eigenvalue spread 2|x|.
planck = 1.22e19
a_bound = 2.9e-24
c_bound = 3.9e-28
epsilon = eta = 0.33
print("dimension-3 coefficient ratio epsilon/a_bound:", epsilon * planck / a_bound)
print("dimension-3 three-flavour spread ratio 3epsilon/a_bound:", 3 * epsilon * planck / a_bound)
print("dimension-4 coefficient ratio eta/c_bound:", eta / c_bound)
print("dimension-4 two-flavour spread ratio 2eta/c_bound:", 2 * eta / c_bound)
