# Handoff

## What Changed

This PR changes the distance-law packet from a closure-style source surface to a
bounded finite-table diagnostic:

- note title/status and conclusion narrowed;
- runner stdout narrowed from "definitive closure" / "safe claims" to bounded
  diagnostic claims;
- heavy runner cache refreshed;
- fast firewall added and cached.

## Why It Matters

The audit row was not blocked by missing compute after the earlier cache fix.
It was blocked because the selected weighted mean was presented as more than a
selected diagnostic. This PR removes that overclaim and leaves the real science
blocker explicit.

## Reviewer / Auditor Boundary

No audit verdicts, generated audit data, publication effective-status files, or
front-door status files were edited. The reviewer should run review-loop and
extract/land as appropriate. Independent audit remains responsible for any
effective status change.

## Checks

```bash
python3 scripts/cached_runner_output.py --refresh scripts/frontier_distance_law_definitive.py --timeout-sec 1800 --tail-chars 2500
python3 scripts/distance_law_finite_table_diagnostic_firewall_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/distance_law_finite_table_diagnostic_firewall_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/frontier_distance_law_definitive.py
python3 scripts/cached_runner_output.py --check-only scripts/distance_law_finite_table_diagnostic_firewall_2026_06_17.py
```

## Remaining Science

A positive distance-law upgrade still requires an independent estimator-selection
theorem or a legitimate pre-registered protocol for the selected scaled-window
weighted mean.
