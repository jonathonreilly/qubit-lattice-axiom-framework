# Handoff

Branch: `physics-loop/post-record-source-trace-count-repair-20260606`
Base: `physics-loop/post-record-selector-tangent-row7-20260606` / PR #2966

This stacked PR repairs
`post_record_source_measure_trace_normalization_prototype_2026-06-06`.

What changed:

- `docs/POST_RECORD_SOURCE_MEASURE_TRACE_NORMALIZATION_PROTOTYPE_2026-06-06.md`
  now reports the current 14+7=21 source/trace snapshot.
- `scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
  now expects `trace_normalization_reference = 7` and total row count `21`.
- The corresponding runner cache is refreshed to zero failures.

Verification:

- `python3 scripts/frontier_post_record_source_measure_trace_normalization_prototype_2026_06_06.py`
  reports `SUMMARY: PASS=49 FAIL=0`.

Boundaries:

- No audit-data edits.
- No new ledger rows.
- No physical measure, Born law, selector, dial, production dynamics, or arrow
  is derived by this branch.
