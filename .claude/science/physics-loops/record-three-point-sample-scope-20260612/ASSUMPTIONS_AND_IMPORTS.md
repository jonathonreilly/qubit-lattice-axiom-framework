# Assumptions And Imports

## Inputs Kept

- The finite L=3, L=4, and L=5 ring events, occupancies, seeds, and depth
  choices named in the source note.
- The exact finite Born-weighted tree and sparse `expm_multiply` evolution.
- The fixed sampled-null protocol:
  `null_p95(Theta, w, kpref=3, n_draws=300, seed=7777)`.

## Imports Still Open

- Inherited Born/record-conditioning chain from #3554/#3555.
- Named instrument, carrier, hopping, and selector protocol authorities.

## Imports Retired Or Exposed

- No exhaustive permutation-null p95 is claimed.
- No certified finite-sample upper confidence bound is claimed.
- No MC-free null theorem is claimed.
