# Assumptions And Imports

No new axioms are introduced.

Inputs retained by the repair:

- fixed drift `0.2`
- restore grid `0.60, 0.70, 0.80`
- seed `0`
- existing finite propagation implementation in
  `scripts/NONLABEL_GROWN_BASIN_TARGETED.py`
- existing grown-row geometry constructor imported from
  `scripts/gate_b_grown_joint_package.py`

New source-side artifact:

- `outputs/nonlabel_grown_basin_recompute_certificate_2026_06_07.json`

Open import after this repair: none for the runner-artifact blocker. The row
remains bounded/support scoped; this PR does not claim audit-retained status.
