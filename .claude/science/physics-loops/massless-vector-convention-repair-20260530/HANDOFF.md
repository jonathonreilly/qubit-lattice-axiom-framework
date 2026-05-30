# Handoff

This branch fixes the audit-failed convention issue:

```text
constraint row: k_mu
polarization: epsilon^mu
gauge shift: epsilon^mu -> epsilon^mu + c k^mu
kernel check: k_mu k^mu = 0
```

Verification:

```text
python3 -m py_compile scripts/audit_companion_massless_vector_polarization_count_from_lorentz_and_gauge_2026_05_28.py
PYTHONPATH=scripts python3 scripts/audit_companion_massless_vector_polarization_count_from_lorentz_and_gauge_2026_05_28.py
python3 scripts/precompute_audit_runners.py --runners scripts/audit_companion_massless_vector_polarization_count_from_lorentz_and_gauge_2026_05_28.py --force --push-mode none --allow-non-main --concurrency 1
bash docs/audit/scripts/run_pipeline.sh
```

Result: `unaudited`, `ready: true`, `open_dependency_paths: []`.
