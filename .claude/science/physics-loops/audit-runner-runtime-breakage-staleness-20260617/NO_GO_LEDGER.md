# No-Go Ledger

No scientific no-go is introduced.

Rejected route: editing `docs/audit/data/runner_breakage_inventory.json`
directly. That would be an audit-result/data mutation, so this branch leaves the
inventory untouched and supplies only a source-side verifier.

Rejected route: changing core cache freshness policy. That would force broad
cache churn unrelated to the target and would waste effort keeping PRs current
against moving `main`.
