# Artifact Plan

## Block12 Artifacts

- Note:
  `docs/QUARK_ROUTE2_RANK_ONE_CARRIER_LEG_FACTORIZATION_BOUNDARY_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_rank_one_carrier_leg_factorization_boundary_2026_06_21.py`
- Cache:
  `logs/runner-cache/frontier_quark_route2_rank_one_carrier_leg_factorization_boundary_2026_06_21.txt`
- Loop pack:
  `.claude/science/physics-loops/s3-route2-readout-endpoint/`

## Required Verification Before PR

- Run the new runner and cache output.
- Compile the new runner.
- Re-run focused upstream Route-2 checks:
  - exact readout map
  - theta-to-slice coupling
  - bilinear tensor primitive
- Run `git diff --check`.
- Run a wording/status scan for branch-local overclaim hazards.

## Repo-Weaving

No repo-wide authority surfaces are edited in this science block.
