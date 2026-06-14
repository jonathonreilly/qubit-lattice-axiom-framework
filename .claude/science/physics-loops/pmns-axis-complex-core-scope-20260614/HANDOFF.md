# Handoff

This PR repairs `pmns_graph_first_axis_alignment_note`.

The theorem previously claimed that residual `P_23` invariance forced the
real-symmetric four-parameter aligned core. The audit correctly identified that
as too narrow: for a general Hermitian `3 x 3` matrix, the invariant family is
`[[a,z,z],[z*,c,r],[z*,r,c]]` with `a,c,r in R` and `z in C`.

This branch makes that five-real-parameter complex normal form the theorem,
keeps the old real-only subfamily outside the derived claim, updates the
runner to exercise a genuinely complex sample, and refreshes the runner cache.

No audit ledger rows, publication matrices, lane registries, or status boards
are edited here. Independent audit owns any status change.
