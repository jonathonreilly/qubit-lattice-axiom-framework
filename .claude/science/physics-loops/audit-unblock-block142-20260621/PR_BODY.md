## Summary

Registers the existing verifier for the unaudited tensorized Schur primitive
note.

Before this PR, `s3_time_tensorized_schur_primitive_note` had a paired
verifier in the repo, but the audit graph/ledger had `runner_path: null`.
This PR adds a standard `Runner` metadata line, refreshes the runner cache,
and regenerates the small affected audit surfaces.

Result:

- target claim: `s3_time_tensorized_schur_primitive_note`
- runner path: `scripts/frontier_s3_time_tensorized_schur_primitive_downstream_fix.py`
- audit status remains `unaudited`
- effective status remains `unaudited`
- runner cache: `38 PASS / 0 FAIL`
- runner classifier: `dominant_class: B`

## Boundary

- No audit-loop run.
- No `apply_audit.py` run.
- No audit verdicts applied.
- No effective-status promotion.
- Runner source unchanged.
- No exact tensor carrier, exact endpoint theorem, exact support-to-slice law,
  or full GR closure claimed.

## Verification

- `python3 scripts/frontier_s3_time_tensorized_schur_primitive_downstream_fix.py` -> `38 PASS / 0 FAIL`
- `bash docs/audit/scripts/run_pipeline.sh` -> complete, no invalidations
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_s3_time_tensorized_schur_primitive_downstream_fix.py --check-only --push-mode none --allow-non-main` -> fresh
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors
- `python3 -m py_compile scripts/frontier_s3_time_tensorized_schur_primitive_downstream_fix.py docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/classify_runner_passes.py` -> OK
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh
- `git diff --check` -> OK
