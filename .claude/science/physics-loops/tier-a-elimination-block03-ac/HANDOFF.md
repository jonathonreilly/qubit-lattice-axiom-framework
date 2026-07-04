# Handoff

## Current Block

Block 3 makes the first AC-side partial retirement: AC_phi_lambda(i)'s value
face is no longer treated as a Tier-A derivation target. It is registered
realized-state data under the approved `realized_state_primitive`.

## Completed In Block 3

- Updated the human Tier-A registry and machine `tier_a_admissions.json`.
- Kept the genuine admitted input count at two.
- Kept AC_phi_lambda as a Tier-A target, but narrowed AC(i)'s survivor to the
  measure-side/dynamical occupancy realization binary.
- Added boundary-runner checks for the new wording and refreshed the runner
  cache.

## Verification

- `PYTHONPATH=scripts python3 scripts/admitted_input_registry_tier_a_boundary_check.py`: PASS=63 FAIL=0.
- Runner cache refreshed.
- `bash docs/audit/scripts/run_pipeline.sh`: pass; no errors, existing warnings/notices only.
- `python3 docs/audit/scripts/audit_lint.py --strict`: pass; no errors, existing warnings/notices only.

## Next Exact Action

Commit the block, push, and open one review PR. After review, attack either
AC(ii)'s R-eta atom or AC(iii)'s contentless species bridge governance call.
