# Handoff

This branch repairs the Gate B grown-geometry joint package conditional row
by reconciling the source note to the live runner cache.

Key movement:

- Updated Born values to current cache: exact `2.06e-15`,
  moderate-drift `2.23e-15`, stress `2.63e-15`.
- Updated farfield dependency prose to match current retained-bounded ledger
  metadata.
- Added runner replay self-checks pinned to the source-note values.
- Cache runtime passed with the replay self-check.
- Pipeline reset the target row to `audit_status=unaudited`,
  `effective_status=unaudited`, `ready=true`.

Remaining science blocker: this is still a finite bounded runner certificate,
not a physical Gate B/gravity closure theorem.
