# Assumptions And Imports

- Input selector: `docs/audit/data/runner_breakage_inventory.json`.
- Evidence surface: SHA-pinned runner caches under `logs/runner-cache/`.
- Policy surface: `scripts/runner_cache.py` cache freshness and header parsing.

No textbook theorem, physical comparator, fitted value, or new axiom is used.
The branch does not claim any science result is retained. It only establishes
that the current runtime-failure inventory entries are not live cache failures.
