# Route Portfolio

## Selected Route: Generated Pipeline Refresh

Run the repo audit pipeline generator path from current source notes. Keep the
result as generated control-plane state and record the boundary in the PR.

Expected movement:

- attach source-exposed runner paths to graph and ledger rows;
- move stale retained rows into re-audit state through existing invalidation
  logic;
- regenerate queue, dispatch, reliability, and publication effective-status
  views;
- make strict lint clean without applying verdicts.

## Rejected Route: Duplicate Runner-Cache Refresh

`precompute_audit_runners.py --all --check-only` still reports ten stale or
corrupt full-ledger caches. Those are already covered by the existing
full-ledger runner-cache freshness PR path, so block139 does not duplicate
that work.

## Rejected Route: Decoration Parent Promotion

The CKM decoration-parent notice is not fixed here. The parent remains
unaudited, and the pipeline correctly keeps the decoration dependent on parent
status rather than promoting it.
