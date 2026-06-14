# Goal

Repair the audited conditional row `pmns_graph_first_axis_alignment_note`.

The audit blocker was local and algebraic: `P_23 H P_23 = H` on a general
Hermitian `3 x 3` core does not force the old real-symmetric four-parameter
matrix. It forces the five-real-parameter complex normal form
`[[a,z,z],[z*,c,r],[z*,r,c]]` with `a,c,r in R` and `z in C`.

This branch adopts the auditor's repair option: restate the theorem with the
complex off-axis parameter and conjugates, then update the runner to check that
scope.
