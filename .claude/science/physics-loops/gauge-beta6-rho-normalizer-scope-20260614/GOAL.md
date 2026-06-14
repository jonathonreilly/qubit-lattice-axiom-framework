# Goal

Repair `gauge_vacuum_plaquette_beta6_evaluation_seam_reduction_science_only_note_2026-04-17`.

The audit blocker was that normalized `rho` was defined for arbitrary abstract
`(S, eta, K)` without requiring the normalizer `z_(0,0)` to be nonzero. This
branch adds the nonzero-normalizer hypothesis exactly where normalized `rho`
is used.
