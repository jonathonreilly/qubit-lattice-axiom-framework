# Assumptions And Imports

## Inputs Kept

- The finite L=3 and L=4 ring events, occupancies, seeds, and depth choices
  named in the source note.
- The exact finite Born-weighted tree and sparse fermionic evolution used by
  the runner.
- The fixed sampled-null protocol:
  `null_p95(Theta, w, kpref=3, n_draws=300, seed=7777)`.

## Imports Retired Or Exposed

- No exhaustive permutation-null p95 is claimed.
- No certified finite-sample upper confidence bound is claimed.
- No MC-free null theorem is claimed.

## Open Guardrails

- No period-law, L>=5, Z^3, convergence, CLT, or gap-universality result is
  claimed.
- Inherited Born/record-conditioning dependencies remain outside this block.
