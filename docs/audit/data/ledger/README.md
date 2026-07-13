# Sharded audit ledger

One file per claim row at `<claim_id[:2]>/<claim_id>.json` (two-character
fanout keeps git tree objects small). This directory plus
`../ledger_meta.json` is the git-tracked source of truth for the audit
ledger. The monolithic `../audit_ledger.json` consumed by readers is an
UNTRACKED cache materialized by `docs/audit/scripts/ledger_io.py`
(`--materialize`, also pipeline step 0); writers must go through
`ledger_io.save_ledger()`. Rationale: a per-verdict rewrite of the 61 MB
monolith cost ~170 KB of packed git history per verdict (~1.5 GB total by
2026-07-13, removed in the same-day history prune); one-row fanout shards
cost a few KB.
