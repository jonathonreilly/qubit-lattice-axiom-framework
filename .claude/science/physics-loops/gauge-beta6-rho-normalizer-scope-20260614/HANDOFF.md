# Handoff

This PR repairs the gauge beta=6 seam-reduction conditional.

The note previously defined normalized `rho_(p,q) = z_(p,q)/z_(0,0)` for
arbitrary abstract data. The repair adds the necessary nonzero-normalizer
domain condition: unnormalized `z` and `v` remain arbitrary-data linear
algebra, while normalized `rho` statements live on `z_(0,0) != 0`.

The runner now refuses zero-normalizer witness normalization, checks that the
source note states the nonzero-normalizer scope, verifies the finite witnesses
have nonzero `z00`, and refreshes the cache to `TOTAL: PASS=15, FAIL=0`.

No audit ledger rows, publication matrices, lane registries, or status boards
are edited here. Independent audit owns any status change.
