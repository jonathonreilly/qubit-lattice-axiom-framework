# Assumptions And Imports

Closed in this block:

- The primary runner no longer imports
  `frontier_dm_leptogenesis_flavor_column_functional_theorem.py`.
- The primary runner no longer imports
  `frontier_dm_leptogenesis_pmns_active_projector_reduction.py`.
- The primary runner no longer imports
  `frontier_dm_leptogenesis_pmns_projector_interface.py`.
- The canonical cycle matrix, `canonical_h`, active packet diagonalization, and
  one-column transport functional used by the interval witness are local to the
  primary runner.

Still imported or open:

- `scripts/dm_leptogenesis_exact_common.py` supplies the exact-package constants,
  normalized transport grid, expansion profile, and washout profile.
- `ETA_OBS` is used as a diagnostic normalization for the root location.  This
  block does not claim an independent physical prediction of the observed
  baryon ratio.
- The physical off-seed selector law remains open.
- Full-stack PMNS/DM closure remains open.

No new repo-wide axiom is introduced.
