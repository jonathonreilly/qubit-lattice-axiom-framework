# Artifact Plan

Primary artifacts:

- `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py`
  contains the self-contained compatibility layer and no longer imports the stale
  PMNS helper stack.
- `docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md`
  records the narrowed bounded status and the diagnostic boundary for the
  interpolated equality.
- `logs/runner-cache/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.txt`
  is refreshed against the repaired runner.
- Audit pipeline artifacts queue the row as `unaudited`, `ready: true`.

Verification artifacts:

- runner refresh with `PASS=12 FAIL=0`
- audit pipeline
- strict audit lint
- controlled vocabulary checks
- pre-commit audit check
