# Goal

Repair the audited-failed grown-transfer targeted packet without editing
audit verdicts or ledgers.

Target row:

- `grown_transfer_basin_targeted_repair_note_2026-06-04`

Audit issue addressed:

- Source note declared `PW = 8`, while the retained helper geometry
  actually computed `PW = 10`.
- Complex-action predicate at `gamma = 0.5` needed an actual away-sign
  check, not just a zero toward-count check.

Repair strategy:

- Use the audit-suggested low-blast-radius path: rescope the finite
  packet to the actually computed helper geometry `PW = 10`.
- Leave retained helper `scripts/gate_b_grown_joint_package.py`
  untouched.
- Strengthen the grown-transfer predicate to require `away_count == 3/3`
  and negative mean deflection at `gamma = 0.5`.
