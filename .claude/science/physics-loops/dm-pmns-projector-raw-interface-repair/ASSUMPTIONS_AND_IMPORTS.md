# Assumptions and Imports

## Load-bearing inputs

- Finite `3 x 3` positive-definite Hermitian matrices.
- Standard spectral theorem for Hermitian matrices.
- Unitary matrix arithmetic.

## Removed imports

- No `dm_leptogenesis_exact_common.py` helper.
- No transport diagnostic machinery.
- No carrier authority from the PMNS lane.
- No physical N1 column-selection theorem.
- No eta/eta_obs value.

## Audit boundary

The row is reset to `unaudited`; independent audit owns any retained
status.
