# Assumptions And Imports

No new axioms are introduced.

Inputs retained by the repair:

- exact-grid reference row
- no-restore grown rows at drifts `0.0`, `0.2`, and `0.5`
- seed `0`
- existing finite one-seed package implementation in
  `scripts/gate_b_no_restore_joint_package.py`

New source-side artifact:

- `outputs/gate_b_no_restore_recompute_certificate_2026_06_07.json`

Open import after this repair: none for the recompute-artifact blocker. The
row remains bounded/support scoped; this PR does not claim audit-retained
status.
