# Artifact Plan

## Block04 artifacts

- Source note:
  `docs/QUARK_ROUTE2_SOURCE_COUNT_SELECTOR_BRIDGE_BOUNDARY_NOTE_2026-06-21.md`
- Runner:
  `scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py`
- Runner cache:
  `logs/runner-cache/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.txt`
- Branch-local loop pack:
  `.claude/science/physics-loops/s3-route2-readout-endpoint/`

## Verification plan

- run the new verifier;
- run adjacent Route-2 readout/source bridge verifiers;
- run `py_compile` on the new script;
- run `git diff --check`;
- perform focused local review without audit pipeline or verdict scripts.
