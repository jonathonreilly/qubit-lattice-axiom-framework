# Handoff

This PR repairs the Higgs effective `N_taste` conditional.

The audited algebra already supported the narrower boundary: the single-class
assignments are all distinct from uniform-16, but they are not five
pairwise-distinct values. The corrected claim is five assignments yielding
three distinct values, with `k=0,4` and `k=1,3` paired by binomial symmetry.

The note, runner intro, runner source-structure checks, terminal verdict, and
runner cache now all use the corrected scope.

No audit ledger rows, publication matrices, lane registries, or status boards
are edited here. Independent audit owns any status change.
