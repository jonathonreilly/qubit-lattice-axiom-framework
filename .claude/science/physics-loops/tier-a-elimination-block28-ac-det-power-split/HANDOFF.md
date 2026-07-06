# Handoff

## Current Block

Block 28 is exact support for the AC_phi_lambda(i) determinant-power split:
holomorphic/orbit count-once is `det_C(K)`, while realified/sector-tied
count-twice is `det_R R(K) = |det_C(K)|^2`.

Branch: `physics-loop/tier-a-elimination-block28-ac-det-power-split-20260704`
Base: `physics-loop/tier-a-elimination-block27-ac-reta-record-nonsupply-20260704`
Source commit: `87f50b6a8`
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4969

## Expected Claim Movement

The block should not edit the Tier-A registry. Its movement is:

```text
The AC(i) survivor is sharpened to an exact determinant-power fork:
complex determinant counted once versus realified determinant counted twice.
```

## Boundaries

- No AC_phi_lambda retirement.
- No AC_phi_lambda(i) retirement.
- No r = 1/2 derivation.
- No orbit-occupancy premise adoption.
- No K-real primitive introduction.
- No physical generation coupling theorem.
- No registry, audit verdict, primitive, axiom, or publication edit.
- R-eta and theta untouched.

## Verification

- `PYTHONPATH=scripts python3 scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py` -> PASS (`PASS=52 FAIL=0`)
- `python3 -m py_compile scripts/acphilambda_occupancy_determinant_power_split_exact_support_2026_07_04.py` -> PASS
- `bash docs/audit/scripts/run_pipeline.sh` -> PASS; newly seeded rows=1
- `python3 docs/audit/scripts/audit_lint.py --strict` -> PASS; existing 23 warnings / 178 notices, no errors
- `git diff --check` -> PASS
- New audit row -> `acphilambda_occupancy_determinant_power_split_exact_support_note_2026-07-04`, `claim_type=bounded_theorem`, `audit_status=unaudited`, `effective_status=unaudited`, `criticality=leaf`

## Next Exact Action

Watch the hosted `audit_pipeline`, then continue toward a real physical
horn-selection theorem or the remaining R-eta route.
