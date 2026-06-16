# Handoff

This PR is a source-side compute unblock for the grown-transfer failed
audit row. It intentionally does not edit:

- `docs/audit/**`
- publication effective-status mirrors
- front-door status files
- retained helper source or note files

Review focus:

1. Confirm that rescoping to `PW = 10` is acceptable under the audit's
   stated repair alternatives.
2. Confirm that the stricter `gamma=0.5` predicate proves actual away
   sign: `away_count == 3/3` and mean deflection `< 0`.
3. Confirm the regenerated caches are fresh and correspond to the edited
   runners.

Expected audit effect:

- This should remove the concrete post-audit compute blocker for
  `grown_transfer_basin_targeted_repair_note_2026-06-04`.
- It does not by itself claim family-wide retained closure.
