# Handoff

## What Changed

- Made `scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py`
  self-contained for its bounded interval witness.
- Added a source-note repair section explaining the stale helper import issue.
- Re-ran the primary runner and audit pipeline.
- The target row is now `unaudited`, `effective_status=unaudited`, and
  `ready=true`.

## Verification

```text
python3 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py
python3 scripts/vocab_lint.py --report-only docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md
bash docs/audit/scripts/run_pipeline.sh
git diff --check
```

## Remaining Boundary

This is still only a bounded/imported transport interval witness. It should not
be read as physical selector closure or a full DM result.
