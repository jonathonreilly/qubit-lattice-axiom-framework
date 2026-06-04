# Handoff

## What Changed

- Parent theorem now defines `J_* = max_z sum_{X contains z} ||h_X||`
  and `D_int`, replacing the old single-term `J` velocity.
- Parent Step 4 no longer uses the false equation (8) imaginary-time
  commutator identity.
- L2 is explicitly conditional on transfer-gap or spatial slab
  authorities; LR alone is not promoted to static clustering.
- Primary runner now reports the corrected `J_*` velocity and adds E5
  for the strict `J < J_*` nearest-neighbour case.

## Verification

- Parent runner: PASS 5/5.
- Existing companion verifier: PASS 27/27.
- Runner cache refreshed for `scripts/axiom_first_cluster_decomposition_check.py`.

## Reviewer Notes

This PR is source repair only. It should not be treated as an audit
verdict or direct status lift. The best extraction is likely to land
the parent source and runner updates, then send the row back through
independent audit.
