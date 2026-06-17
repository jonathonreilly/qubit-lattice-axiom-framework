# Goal

Unlock the audit pipeline by separating stale runtime-runner breakage labels
from live source/cache failures.

The target is not an audit verdict and not a ledger retag. The branch supplies a
deterministic source-side guard proving that current `timeout` and
`nonzero_exit` entries in `docs/audit/data/runner_breakage_inventory.json` no
longer correspond to failing SHA-pinned runner caches.
