# Assumptions And Imports

- The upstream `nonlabel_grown_basin_note` remains the retained bounded anchor.
- The new recompute runner uses the same finite drift/seed grid as the source
  note: drifts `0.15`, `0.20`, `0.25`, seeds `0`, `1`, `2`, and fixed
  `restore = 0.70`.
- The branch does not add a continuum theorem, family-wide theorem, or new
  axiom.
- `scripts/gate_b_grown_joint_package.py` remains the local grown-geometry
  helper imported by the original runner family.
