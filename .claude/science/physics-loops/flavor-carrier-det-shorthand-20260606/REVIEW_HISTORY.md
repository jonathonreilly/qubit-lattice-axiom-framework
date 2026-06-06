Verification commands run:

```text
python3 -m py_compile scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py
python3 scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py
python3 scripts/precompute_audit_runners.py --runners scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py --force --allow-non-main --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py --check-only --allow-non-main --push-mode none
```

Observed result:

- runner scorecard: `PASS=7 FAIL=0`
- runner cache refreshed and then reported fresh
