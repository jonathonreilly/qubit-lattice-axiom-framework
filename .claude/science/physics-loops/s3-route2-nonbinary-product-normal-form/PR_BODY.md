## Summary

Block107 gives a non-binary normal form for the connected-cumulant route.
If the same Route-2 source has `E[XY]=1` and `E[X]E[Y]=1/9`, then P-cal
connected subtraction gives `kappa=0`.

This avoids making the binary/log-odds selector load-bearing. That selector is
one subcase, not the whole product theorem.

## Trace

Trace class: `upstream_support`.

Remaining primitive:

```text
Route-2 same-source one-point product theorem E[X]E[Y]=1/9.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.py
     TOTAL: PASS=70, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_log_odds_selector_stretch_no_go_2026_06_22.py
     TOTAL: PASS=80, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.py
     TOTAL: PASS=67, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_signed_quotient_classification_no_go_2026_06_22.py
     TOTAL: PASS=67, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py
     TOTAL: PASS=72, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py
     TOTAL: PASS=75, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
     PASS=11 FAIL=0
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block106 and does not push to main.

## PR Identity

```text
PENDING
```
