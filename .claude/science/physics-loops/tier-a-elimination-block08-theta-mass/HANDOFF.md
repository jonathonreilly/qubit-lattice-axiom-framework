# Handoff

## Current Block

Block 8 attacks theta's mass-side determinant-readout bridge after the
2026-07-04 axiom update.

## Expected Claim Movement

The block should not edit the Tier-A registry. Its movement is:

```text
updated axioms/primitives do not supply the determinant-channel interface
or physical exhaustion bridge for arg det(M_u M_d).
```

## Boundaries

- No theta retirement.
- No `theta_bar = 0` derivation.
- No primitive or axiom registration.
- No gauge-side winding movement.
- No use of measured neutron-EDM bounds or fitted values.

## Verification

- `PYTHONPATH=scripts python3 scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py`
- `python3 -m py_compile scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py`
- `bash docs/audit/scripts/run_pipeline.sh`
- `python3 docs/audit/scripts/audit_lint.py --strict`
- `git diff --check`
