# Handoff

## Current Block

Block 14 attacks AC_phi_lambda sub-admission (i)'s determinant-order /
physical chiral L-R coupling route.

Branch: `physics-loop/tier-a-elimination-block14-aci-detorder-20260704`
Base: `physics-loop/tier-a-elimination-block13-aci-index-20260704`
PR: pending
Source commit: pending

## Expected Claim Movement

The block should not edit the Tier-A registry. Its movement is:

```text
current determinant-order support does not derive AC(i)'s physical chiral
L-R coupling/readout bridge; non-SUSY index availability and separate-factor
algebra remain support/open-gate material rather than retirement.
```

## Boundaries

- No AC_phi_lambda retirement.
- No `r = 1/2` or `r = 1` derivation or selection.
- No primitive or axiom registration.
- No audit-status change.
- No theta or R-eta movement.
- No exclusion of future physical L-R coupling, readout-rule, or Pfaffian/Weyl
  quotient routes.

## Verification

- `PYTHONPATH=scripts python3 scripts/acphilambda_determinant_order_chiral_lr_current_surface_no_go_2026_07_04.py` -> PASS (`PASS=158 FAIL=0`)
- `python3 -m py_compile scripts/acphilambda_determinant_order_chiral_lr_current_surface_no_go_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS with pre-existing warnings/notices only
- `git diff --check` -> PASS

## Next Exact Action

Commit, push, open a stacked PR, then monitor audit.
