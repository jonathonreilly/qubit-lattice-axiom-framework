# Handoff

## Repairs

- Gamma5 factor no-go: validation count now matches `PASS=20 FAIL=0`.
- SU(3) dabc: C2 cubic scalar corrected to `10/9 I_3`; runner checks it.
- Signed-gravity eta bridge: T3 narrowed to `Lambda in Z+1/2`; generic
  fractional-cutoff formula and excluded cutoffs are explicit.

## Verification

```bash
python3 scripts/frontier_koide_gamma5_factor_bridge_no_go.py
python3 scripts/su3_dabc_symmetric_check.py
python3 scripts/signed_gravity_product_grading_eta_sector_bridge_2026_06_11.py
python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_gamma5_factor_bridge_no_go.py,scripts/su3_dabc_symmetric_check.py,scripts/signed_gravity_product_grading_eta_sector_bridge_2026_06_11.py --check-only --push-mode=none
```

Expected:

- Gamma5: `PASS=20 FAIL=0`
- SU(3): `OVERALL: PASS`
- Signed gravity: `PASS=31 FAIL=0`
- Caches: fresh

Independent audit remains responsible for row-status changes.
