# Handoff

This branch supplies the separate I12 comparator bridge requested by the
conditional audit. It does not edit audit files and does not claim retained
status.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py
python3 scripts/precompute_audit_runners.py --runners scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py --force --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/sm_gstar_i12_empirical_thermal_comparator_bridge_2026_06_15.py --check-only
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Expected runner scorecard: `TOTAL: PASS=26 FAIL=0`.

## Remaining Blocker

The empirical small-neutrino-mass input is still admitted. A stronger future
repair would derive small `m_nu` or replace the thermal-rate comparator with
a framework-native finite-temperature collision calculation.
