# Z3 doublet-block center: finite search diagnostic

**Type:** open_gate
**Scope:** finite numerical diagnostics, not an exact or global no-go.
**Primary runner:** [center search](../scripts/frontier_dm_pmns_z3_doublet_block_center_positive_sheet_no_go_2026_04_20.py)
**Cache:** [captured output](../logs/runner-cache/frontier_dm_pmns_z3_doublet_block_center_positive_sheet_no_go_2026_04_20.txt)

The supplied five-coordinate seed chart and doublet-block readout define
residuals `(delta_db-1,q_+)`. Seeded least-squares searches retain numerical
representatives at residual norm at most 1e-8 and computed `I_src>0`.
Separate component checks use 1e-10; chart deduplication uses 1e-3. The
runner reports sampled angle ranges against the original 0.5, 0.4, 0.8
thresholds. These finite observations do not certify exact roots.

A centered finite difference with step 1e-6 estimates the two-constraint
Jacobian; numerical rank uses threshold 1e-5 at sampled points. Rank two
at those samples does not prove rank on a neighborhood, hence does not
establish a local three-real manifold.

A separate finite search also imposes the supplied target
`(0.307,0.0218,0.545)`. Its test asks whether this run returns two
representatives, with matching x/y and opposite source signs to tolerance.
The number found is not an exhaustive global solution count. Positive sign
is supplied, not a derived physical sheet selector. I5/I12 physical
selection and any exact no-go remain open.

## Recovery and limits

The historical exact/global/manifold/no-go claims are withdrawn. Full
original note, runner, cache and failed paths remain recoverable at
`96009ff66e877c6e0fc9f16f00e7c9b61d2d5c68` and in the PR9847 evidence map.
The current search preserves the original starts, solver modes, thresholds,
RNG and numeric predicates; documentary text checks do not supply proofs.
PR9844 remains held. Its local-selector note is not a numerical dependency
and is not imported as authority. The computational helpers are pinned
from the approved base solely for their supplied chart/readout arithmetic.
No helper's filename or historical theorem wording certifies physical
selection. No N5 global-resolution certificate is claimed.
