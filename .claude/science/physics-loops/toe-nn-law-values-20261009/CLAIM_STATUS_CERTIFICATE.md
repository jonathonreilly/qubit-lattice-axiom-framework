# Claim status certificate — cycle 9

- Intended audit claim type: `bounded_theorem`
- Author surface: bounded-support, conditional on one factor
  `1 + (1 - 2 t) B^X + (t^2 - t + 1) B^Y` on the two odd cap lines, on
  partial neighbour conditions, and on the proper cubic orbit of `(0, 1, 2)`
- Current ledger status of this new note: none yet; do not invent one
- Audit remains required. This file is not a verdict.
- Open imports: the factor, partial neighbour conditions, and the uniform
  weight; formation site, probability, and rate
- Route pruned: the unique root `t = 1/2` of this factor is a selected interaction
- The root is the root of the supplied polynomial `1 - 2 t`. At that value
  the factor is `1 + (3/4) B^Y`, with strictly positive bond values
- No-go packet in the source note is scoped to this one factor. It does
  not classify every shifted factor, and it does not queue another pencil
- The odd cap alphabet stops. The following block's supplier is the
  formation rule, not a bond factor
- Runner: `TOTAL: PASS=28 FAIL=0` at the worktree copy, re-run by the author
  through `runner_cache.py`
- Independent review has not been requested

# Claim status certificate — cycle 8

- Intended audit claim type: `bounded_theorem`
- Author surface: bounded-support, conditional on quadratic pencils
  `1 + t (a X + b Y) + t^2 (c X + d Y)` with coefficients in
  `{-2,-1,0,1,2}`, on the two odd cap lines, on partial neighbour
  conditions, and on the proper cubic orbit of `(0, 1, 2)`
- Current ledger status of this new note: none yet; do not invent one
- Audit remains required. This file is not a verdict.
- Open imports: the pencil, the coefficient box, partial neighbour
  conditions, and the uniform weight; formation site, probability, and rate
- Route pruned: an independent pencil in this box isolates a unique nonzero `t`
- The constant rule `t = 0` is normalised for every independent pencil.
  That is not a selected interaction
- The balance value `1/2` is a second root of one supplied pencil, and
  strict positivity keeps `0` as well
- No-go packet in the source note is scoped to this box and these two
  lines. It does not classify a factor that is not `1` at `t = 0`
- Runner: `TOTAL: PASS=31 FAIL=0` at the worktree copy, re-run by the author
  through `runner_cache.py`
- Independent review has not been requested
