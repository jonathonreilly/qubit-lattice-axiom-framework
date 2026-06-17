# Assumptions And Imports

## Framework Inputs Used

- The retained sigma set used by the source runner:
  `{(2,1,0), (2,0,1), (0,1,2), (1,2,0)}`.
- The five-basin chart already encoded in the runner:
  `{Basin 1, Basin N, Basin P, Basin X, Basin 2}`.
- The active chamber condition `q_+ + delta >= sqrt(8/3)`.
- The Hermitian pencil and NuFit central-value chi^2 map already implemented in
  the source runner.

## Imported Or External Inputs

- `numpy` and `scipy.optimize.minimize` are computational tools for replaying
  the finite multistart scan.
- The runner does not import a theorem of completeness from these numerical
  tools.

## Boundary

The repair explicitly leaves these as missing:

- interval/branch-and-bound proof over `R = 50`,
- computer-algebra/root-isolation enumeration,
- certified worst-case Lipschitz or eigenvalue-gap bound,
- deterministic far-field asymptotic exclusion.
