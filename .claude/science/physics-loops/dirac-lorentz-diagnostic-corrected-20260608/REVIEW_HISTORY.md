## Local Review

- Verified the original blocker by inspecting the runner import:
  `hermegauss` uses the `exp(-x^2/2)` weight, but the squared rapidity
  Gaussian norm requires `exp(-x^2)` after the `x=sqrt(a) zeta` substitution.
- Replaced the quadrature with `hermgauss`.
- Added an analytic lower-bound assertion for `H^n psi` to prevent a purely
  empirical finite-table certificate.
- Checked that the packet still claims only an open-gate diagnostic boundary.

