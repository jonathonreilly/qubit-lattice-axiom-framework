# Handoff

## Summary

This PR repairs the audited-conditional Koide Dirac-mass bounded no-go row by narrowing it to the
algebraic facts the source proves: sign-blind singular-value readout, Berry-flat L-R coupling, and
the signed-vs-singular residual.

## Changed

- Corrected the odd-block determinant sign: `det D = -|det M|^2`.
- Removed "forced physical mass" language from the live claim.
- Removed the non-retained staggered-gate markdown dependency from the note.
- Updated the runner to assert the correct determinant sign.
- Refreshed runner cache.

## Verification

```bash
python3 scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_koide_dirac_mass_forces_r_one_exact.py --force --concurrency 1 --push-mode none --allow-non-main
```

Results:

- `6 PASS, 0 FAIL`
- cache refresh `ok=1`

## Boundaries

- No audit ledger edits.
- No retained-status claim.
- No physical charged-lepton mass bridge.
- No hard universal no-go.

PR: pending
