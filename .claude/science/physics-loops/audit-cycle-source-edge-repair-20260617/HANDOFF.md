# Handoff

This branch repairs current source-cycle blockers without touching
`docs/audit/data`, publication matrices, or front-door status files.

Changed source edges:

- `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md` no longer presents the
  spacetime tensor primitive as a markdown one-hop dependency.
- `S3_TIME_SPACETIME_TENSOR_PRIMITIVE_NOTE.md` no longer presents the
  theta-to-slice survey as a one-hop authority.
- `QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28.md` no longer
  presents peer/downstream bridge and taste-staircase rows as dependencies of
  the negative boundary.
- `CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE.md` no longer presents GST support and
  down-type extraction rows as dependencies of the `5/6` bridge support note.
- `DOWN_TYPE_MASS_RATIO_CKM_DUAL_NOTE.md` no longer presents the later
  taste-staircase support follow-up as a dependency of the earlier bounded
  lane row.

Run:

```bash
python3 scripts/source_cycle_false_edge_hygiene_2026_06_17.py
python3 scripts/cached_runner_output.py --refresh scripts/source_cycle_false_edge_hygiene_2026_06_17.py
python3 scripts/cached_runner_output.py --check-only scripts/source_cycle_false_edge_hygiene_2026_06_17.py
```

Next audit action: rebuild dependency graph from source and confirm these
cycle edges are absent.
