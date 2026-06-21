## Summary

Regenerates audit control-plane surfaces from current source notes. This
unblocks the audit lane by making strict lint error-free, registering
source-exposed runner paths, and moving stale retained-note snapshots back
into generated re-audit queue state through existing pipeline logic.

Generated movement:

- ledger rows: `3474`
- newly seeded rows: `32`
- source-exposed runner paths attached where previously missing: `47`
- audit queue: `1694` pending, `112` ready
- dispatch queue: `5` live, `2` ready, `18` resolved post-manifest targets,
  `19` retired
- strict audit lint: no errors

## Boundary

- No audit-loop run.
- No `apply_audit.py` run.
- No audit verdicts applied.
- No source theorem note or runner source changed.
- Effective-status changes are generated invalidation/propagation from the
  existing audit pipeline, not hand-authored status changes.

## Verification

- `bash docs/audit/scripts/run_pipeline.sh` -> complete; strict lint step OK
- `python3 docs/audit/scripts/audit_lint.py --strict` -> OK, no errors
- `python3 -m py_compile docs/audit/scripts/build_citation_graph.py docs/audit/scripts/seed_audit_ledger.py docs/audit/scripts/compute_effective_status.py docs/audit/scripts/audit_lint.py` -> OK
- `git diff --check` -> OK
- `python3 scripts/precompute_audit_runners.py --pr-diff origin/main --check-only --push-mode none --allow-non-main` -> all relevant caches fresh

## External Residual

`python3 scripts/precompute_audit_runners.py --all --check-only --push-mode none --allow-non-main`
still reports ten stale/corrupt full-ledger caches. This PR does not duplicate
that work; it is already covered by the existing full-ledger runner-cache
freshness PR path.
