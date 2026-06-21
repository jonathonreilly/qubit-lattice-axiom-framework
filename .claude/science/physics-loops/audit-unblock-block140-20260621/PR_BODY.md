## Summary

Registers the existing runner for the high-priority unaudited S3 time
factor-rigidity note.

Before this PR, the note referenced
`frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py` in prose, but
the audit graph/ledger had `runner_path: null`. This PR adds a standard
`Runner` metadata line and regenerates the small affected audit surfaces.

Result:

- target claim: `s3_time_theta_to_slice_coupling_factor_rigidity_note_2026-05-17`
- runner path: `scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py`
- audit status remains `unaudited`
- effective status remains `unaudited`
- runner classifier: `dominant_class: C`, with `C=9`, `D=4`

## Boundary

- No audit-loop run.
- No `apply_audit.py` run.
- No audit verdicts applied.
- No effective-status promotion.
- Parent `s3_time_theta_to_slice_coupling_note` remains open.
- Runner source unchanged.

## Verification

- `python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py` -> `PASS=64 FAIL=0`
- `bash docs/audit/scripts/run_pipeline.sh` -> complete, no invalidations
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors
- `python3 -m py_compile scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py` -> OK
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh
- `git diff --check` -> OK
