# Opportunity Queue

1. `plaquette_beta6_perturbative_derivation_bounded_obstruction_note_2026-05-27`
   - Status: packaged for review.
   - Move: conditional imported-value blocker converted into explicit supplied-input scope.
   - Remaining: independent audit must decide whether the scoped runner-local obstruction is acceptable.

2. Search the current audit ledger for uncovered audited conditional rows after this PR is opened.
   - Prefer rows not already covered by open PRs.
   - Prefer rows with executable runners and narrow imported-value blockers.
   - Avoid narrowing where a genuine framework-native proof route is available.
