# Artifact Plan

## Block11 Artifacts

- Note:
  `docs/QUARK_ROUTE2_SOURCE_READOUT_FACTORIZATION_GAUGE_NO_GO_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_source_readout_factorization_gauge_no_go_2026_06_21.py`
- Cache:
  `logs/runner-cache/frontier_quark_route2_source_readout_factorization_gauge_no_go_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-readout-endpoint/`

## Required Verification Before PR

- Run the new runner and cache output.
- Compile the new runner.
- Re-run focused upstream Route-2 checks:
  - exact readout map
  - theta-to-slice coupling
  - source-domain bridge no-go
- Run `git diff --check`.
- Run a wording/status scan for branch-local overclaim hazards.

## Repo-Weaving

No repo-wide authority surfaces are edited in this science block.
