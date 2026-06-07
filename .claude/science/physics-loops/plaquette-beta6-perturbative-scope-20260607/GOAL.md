# Goal

Repair the conditional audit blocker for
`plaquette_beta6_perturbative_derivation_bounded_obstruction_note_2026-05-27`.

Quoted blocker:

`missing_bridge_theorem: add retained or effective-bounded authority rows for the NSPT coefficient packet, beta=6 Wilson normalization, MC comparator, and F2 comparator, or keep this row explicitly runner-local/conditional; also fix the stale source-note expected-output count from PASS=24 to PASS=28.`

This branch fixes the stale expected-output count. The row is already scoped as
a conditional runner-local diagnostic on current `main`.
