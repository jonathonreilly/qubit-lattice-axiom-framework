"""Independent dyadic certificate for the K3a 3D Yee-Maxwell feasibility claim.

The worker used a large radius-1 sparse LSMR solve.  Here a smaller radius-1/2
ansatz is solved densely, rounded to sixteenths, and checked against the exact
integer-valued equation matrices.  Binary floating point represents all of
these dyadic numbers exactly, so literal zero residuals are exact identities
for the finite local stencil encoded by maxwell3d.build.
"""

import numpy as np

from maxwell3d import build


A, N, target, _ = build(
    L=8,
    RP=0.5,
    RT=0.5,
    Rl=0.5,
    ry=0.75,
    verbose=False,
)

system = np.vstack((A.toarray(), N.toarray()))
rhs = np.concatenate((np.zeros(A.shape[0]), target))
solution, _, rank, singular_values = np.linalg.lstsq(
    system, rhs, rcond=1e-12
)
dyadic_solution = np.rint(16.0 * solution) / 16.0

continuity_residual = A @ dyadic_solution
normalisation_residual = N @ dyadic_solution - target

print("system shape:", system.shape)
print("rank/nullity:", rank, system.shape[1] - rank)
print("smallest retained singular value:", singular_values[rank - 1])
print("nonzero dyadic coefficients:", np.count_nonzero(dyadic_solution))
print("max |continuity residual|:", np.max(np.abs(continuity_residual)))
print("max |normalisation residual|:", np.max(np.abs(normalisation_residual)))

assert np.array_equal(continuity_residual, np.zeros_like(continuity_residual))
assert np.array_equal(normalisation_residual, np.zeros_like(normalisation_residual))
