# Assumptions And Imports

- The audit-loop must remain owner of claim truth and audit verdicts.
- Source-side tooling may prove whether a runner path/cache blocker is still
  live without changing ledger verdicts.
- `runner_breakage_inventory.json` is treated as inventory evidence, not as an
  authority surface to edit in this block.
- Current SHA-pinned cache freshness is defined by `scripts/runner_cache.py`.
- Legacy runner references are canonicalized by basename to checked-in
  `scripts/<name>.py` paths when that file exists in the current checkout.

No external literature or observational values are used.
