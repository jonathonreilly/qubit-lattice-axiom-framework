Verification commands run:

```text
python3 -m py_compile scripts/flavor_idempotent_u1_collapses_2026_05_30.py
python3 scripts/flavor_idempotent_u1_collapses_2026_05_30.py
python3 scripts/precompute_audit_runners.py --runners scripts/flavor_idempotent_u1_collapses_2026_05_30.py --force --allow-non-main --push-mode none
python3 scripts/precompute_audit_runners.py --runners scripts/flavor_idempotent_u1_collapses_2026_05_30.py --check-only --allow-non-main --push-mode none
```

Observed result:

- runner scorecard: `PASS=5 FAIL=0`
- runner cache refreshed and then reported fresh
