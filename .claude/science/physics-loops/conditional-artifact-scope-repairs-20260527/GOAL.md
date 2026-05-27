# Goal

Repair current `audited_conditional` rows by changing only source/audit-derived
artifacts, leaving final audit status to the independent audit lane.

Targets:

- `gate_b_grown_joint_package_note`: reconcile the source note to the current
  SHA-pinned runner cache and retained-bounded dependency metadata.
- `gravity_clean_derivation_note`: narrow the source to the auditor's bounded
  IF-chain and supersede the prior single-axiom / zero-free-parameter wording.
