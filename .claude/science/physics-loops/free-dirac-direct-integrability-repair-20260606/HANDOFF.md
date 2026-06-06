# Handoff

This branch repairs the free-Dirac Poincare generator row by replacing the
failed Nelson/common-Gaussian analytic-vector claim.

What changed:

- The note no longer claims rapidity Gaussians are common analytic vectors for
  `H`, `P`, `J`, `K`, or a Nelson Laplacian.
- The runner proves that the old H/P Gaussian route fails by checking moment
  growth.
- The repair uses direct unitary mass-shell action and one-parameter
  Stone/self-adjointness checks instead.
- The status remains bounded-support; audit owns any ledger movement.

Reviewer extraction target:

- Decide whether the direct unitary-action construction is an acceptable
  alternate integrability theorem for this row's bounded free-field scope.
