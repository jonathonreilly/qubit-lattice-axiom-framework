# Handoff

This PR repairs the dimension upper-bound conditional row by adding a durable
source repair note plus paired runner.

## What changed

- Added `DIMENSION_UPPER_BOUND_DEPENDENCY_EDGE_REPAIR_NOTE_2026-06-08.md`.
- Added `scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py`
  and a SHA-pinned cache.
- Updated the old upper-bound wrapper to cite the repair note and the one-hop
  support packets.

## Verification

```bash
python3 scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py
python3 scripts/frontier_d3_upper_bound_import_scope_gate_2026_06_06.py
git diff --check
```

## Boundaries

- No `docs/audit/**` files changed.
- No audit verdict is applied.
- Bertrand and atomic-stability remain bounded support / import-supported
  routes unless future framework-native proofs land.
