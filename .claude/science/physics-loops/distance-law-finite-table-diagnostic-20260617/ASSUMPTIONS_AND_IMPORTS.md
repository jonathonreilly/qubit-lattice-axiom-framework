# Assumptions And Imports

## A_min

- Existing ordered cubic lattice and one-site qubit framework are not modified.
- Existing runner numerics are reused; no new axiom or primitive premise is
  introduced.

## Load-bearing Inputs

- `scripts/frontier_distance_law_definitive.py` computes finite ordered-cubic
  Dirichlet Poisson/path-sum data for `N = 31, 40, 48, 56, 64, 80, 96`.
- The selected weighted mean of scaled-fit values for `N >= 56` remains a
  diagnostic selector only.

## Exposed Import / Open Theorem

- Missing: independent estimator-selection theorem or pre-registered protocol
  selecting the scaled-fit `N >= 56` weighted mean before looking at the result.
- The PR does not import such a theorem and does not cite external literature as
  a proof substitute.
