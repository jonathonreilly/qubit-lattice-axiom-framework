# Handoff

## Current Block

Block 8 attacks theta's mass-side determinant-readout bridge after the
2026-07-04 axiom update.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4933
Branch: `physics-loop/tier-a-elimination-block08-theta-mass-20260704`
Base: `physics-loop/tier-a-elimination-block07-aci-binary-20260704`
Source commit: `7f4642214`

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

- `PYTHONPATH=scripts python3 scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py` -> `TOTAL: PASS=110 FAIL=0`
- `python3 -m py_compile scripts/theta_mass_determinant_axiom_update_no_go_2026_07_04.py` -> pass
- `bash docs/audit/scripts/run_pipeline.sh` -> pass
- `python3 docs/audit/scripts/audit_lint.py --strict` -> pass with existing warnings/notices only
- `git diff --check` -> pass

## Next Exact Action

Monitor PR #4933 audit status, then attack the theta gauge-side winding account
as the remaining theta Tier-A residual.
