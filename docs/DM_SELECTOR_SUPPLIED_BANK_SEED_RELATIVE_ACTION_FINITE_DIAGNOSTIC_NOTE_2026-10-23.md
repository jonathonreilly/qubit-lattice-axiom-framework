# Supplied-bank seed-relative-action finite diagnostic

**Date:** 2026-10-23
**Type:** bounded_theorem
**Status:** finite numerical comparison under supplied inputs; independent review pending.
**Primary runner:** `scripts/frontier_dm_selector_supplied_bank_seed_relative_action_finite_diagnostic.py`
**Primary runner cache:** `logs/runner-cache/frontier_dm_selector_supplied_bank_seed_relative_action_finite_diagnostic.txt`

This diagnostic compares the five supplied recovered lifts returned by
`dm_selector_branch_support.recovered_bank()` against the fixed `H_SEED`
from `frontier_dm_leptogenesis_pmns_observable_relative_action_law.py`.
The lifts, affine Hermitian matrices, positivity repairs, comparison seed and
scalar functional are inputs. Their physical derivation, bank completeness,
normalization uniqueness and physical selection authority are not established.

For the supplied matrices, the computation evaluates

```text
A_mu(H) = H + mu I
S_mu(H || H_seed) = Re[Tr(A_mu(H_seed)^(-1) A_mu(H))
                       - logdet(A_mu(H_seed)^(-1) A_mu(H)) - 3].
```

The implementation uses the existing `slogdet` expression, singular-branch
guard, `np.argsort` ordering and runner thresholds unchanged. It returns the
first sorted score index and the gap to the second; a tie gives zero margin
and fails the positive-margin predicates. No new tie-breaking physical law
is supplied.

Set `mu_floor` to the maximum of the supplied bank's positivity repairs.
The comparisons cover the original 20 `SHIFT_OFFSETS`, three 20-entry
linspace grids from `mu_floor+1e-6` through `mu_floor+20`, and one additional
sample at `mu_floor+1e6`. The grids share boundary entries; they are sampled
entries, not a covering proof for a continuous interval. For the first two
groups the test requires lift0 and margin greater than1e-9; for the far
sample it requires lift0 and margin greater than1e-18. The sign check uses
the imaginary `[1,2]` entry of the directly imported pure `kz_from_h` map,
with zero as the original comparison threshold, over these same five lifts.

A successful capture means these floating-point predicates pass for this
supplied finite bank and these sampled shifts. It does not certify rigorous
roundoff bounds, exact root/rank statements, positivity for every shift,
a physical selector, or a globally unique minimizer over other banks or
all shifts. In particular the far-shift sample is not an asymptotic proof.

The numerical functions, candidate list, seed, grids and threshold predicates
are reused from the previously reviewed selector computation. This separate
owner does not import that primary or the broad shifted-sign module, and
performs no summary-file/documentary authority checks. The existing selector's
input declarations and the standalone documentary mains remain intact; this
new numerical owner does not discharge their independent consistency duties.
