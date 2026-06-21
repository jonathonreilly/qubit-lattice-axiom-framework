# Artifact Plan

## Block10 Artifacts

- Note:
  `docs/QUARK_ROUTE2_DUAL_NORMALIZED_SOURCE_READOUT_TWO_FACTOR_BRIDGE_CONDITIONAL_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.py`
- Cache:
  `logs/runner-cache/frontier_quark_route2_dual_normalized_source_readout_two_factor_bridge_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-readout-endpoint/`

## Required Verification Before PR

- Run the new runner and cache output.
- Compile the new runner.
- Re-run focused upstream Route-2 checks:
  - exact readout map
  - exact time coupling
  - theta-to-slice coupling
  - quadratic covariance no-go
- Run `git diff --check`.
- Run a wording/status scan for branch-local overclaim hazards.

## Repo-Weaving

No repo-wide authority surfaces are edited in this science block. Later review
may decide how to weave the result into lane status, indexes, or audit queues.
