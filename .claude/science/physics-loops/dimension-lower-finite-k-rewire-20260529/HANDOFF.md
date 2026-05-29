# Handoff

This branch does not audit the row and does not retag the ledger by hand. It
queues the lower-bound V2 packet for re-audit by changing the note itself and
running the standard pipeline.

What changed:

- The packet now cites the retained bounded finite-k bridge as load-bearing
  authority for the runner's normalized centroid sign.
- The old WKB/eikonal bridge is explicitly removed from load-bearing status.
- The false `phi < 0 for M > 0 in all cases` prose is corrected for the
  `d = 2`, `0 < r < 1` case.
- The alpha prose is narrowed so the displayed runner exponents are not
  claimed as precision matches to ideal Green-function falloff.

Audit surface after pipeline:

```text
claim_id: dimension_selection_lower_bound_bridge_v2_2026-05-20
audit_status: unaudited
effective_status: unaudited
ready: true
deps:
  - dimension_selection_finite_k_centroid_sign_bridge_note_2026-05-25
  - dimensional_gravity_table
open_dependency_paths: []
runner_path: scripts/frontier_dimension_selection.py
```

Remaining boundaries:

- No full D=3 retained theorem.
- No axiom rewrite.
- No upper-bound closure.
- No uniform all-parameter theorem beyond the retained finite runner bridge.
