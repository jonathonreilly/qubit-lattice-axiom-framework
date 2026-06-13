# Handoff

## What Changed

The dependency-edge repair note now has a canonical visible type
`bounded_theorem`, an explicit source role saying it is a bounded source-graph
repair only, and a not-parent-theorem firewall. The runner now checks those
scope boundaries.

## Verification

```bash
python3 scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py
python3 scripts/precompute_audit_runners.py --runners scripts/dimension_upper_bound_dependency_edge_repair_2026_06_08.py --check-only --push-mode=none
```

Expected:

- Runner: `PASS=51 FAIL=0`
- Cache: fresh

Independent audit remains responsible for any row-status or claim-type
movement.
