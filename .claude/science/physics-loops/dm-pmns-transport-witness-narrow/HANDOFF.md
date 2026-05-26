# Handoff

PR: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1932

## What Changed

The row now claims only a bounded interval witness: the imported transport
functional evaluates below `eta/eta_obs = 1` at the aligned seed endpoint,
above `1` at a sampled off-seed endpoint, and exactly `1` at an interpolated
witness.  Physical selector and full-stack closure language was removed.

## Verification

- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py --allow-non-main`
- `python3 scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `python3 scripts/render_controlled_vocabulary.py --check`
- `python3 scripts/vocab_lint.py --report-only docs/DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md .claude/science/physics-loops/dm-pmns-transport-witness-narrow/*.md`
- `python3 -m py_compile scripts/frontier_dm_leptogenesis_pmns_transport_extremal_source_candidate.py`
- `git diff --check`
