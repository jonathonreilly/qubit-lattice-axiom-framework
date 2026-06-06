# Handoff

Branch: `physics-loop/post-record-generation-koide-index-repair-20260606`
Base: `physics-loop/post-record-selector-tangent-row7-20260606` / PR #2966

This stacked PR repairs
`post_record_generation_koide_stable_location_index_2026-06-06`.

What changed:

- `docs/POST_RECORD_GENERATION_KOIDE_STABLE_LOCATION_INDEX_2026-06-06.md`
  now reports the current 103+3=106 row map.
- `scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py`
  now expects the current selector class split:
  47 Koide/value, 37 obstruction/open-gate, 6 generation, 5 selector-surface,
  4 readout/carrier, 2 measure/source, and 2 other.
- The corresponding runner cache is refreshed to zero failures.

Verification:

- `python3 scripts/frontier_post_record_generation_koide_stable_location_index_2026_06_06.py`
  reports `SUMMARY: PASS=60 FAIL=0`.

Boundaries:

- No audit-data edits.
- No new ledger rows.
- No selected dial, Record-derived selector, physical arrow, or Koide closure
  is claimed.
