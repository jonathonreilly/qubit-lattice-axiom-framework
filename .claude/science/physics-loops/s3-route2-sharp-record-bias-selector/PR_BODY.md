## Summary

Block105 prunes the shortcut that the generic sharp-record RN/Fisher
source-measure toolkit itself selects the Route-2 binary bias required after
Block104.

The toolkit supplies the normalized RN chart and unit tangent. In that chart,
`kappa=0` requires `h = +/- (1/2) log 2`, equivalently a `2:1` or `1:2`
signed-outcome source measure. No current Route-2 primitive selects that
nonzero displacement.

## Trace

Trace class: `negative_route_pruning`.

Refined remaining primitive:

```text
Route-2 sharp-record bias-selector theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_sharp_record_bias_selector_no_go_2026_06_22.py
     TOTAL: PASS=67, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_signed_quotient_classification_no_go_2026_06_22.py
     TOTAL: PASS=67, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_binary_same_record_transfer_no_go_2026_06_22.py
     TOTAL: PASS=60, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.py
     TOTAL: PASS=72, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py
     TOTAL: PASS=75, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
     PASS=11 FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS python3 scripts/frontier_source_measure_sharp_record_tangent_space.py
     SUMMARY: PASS=58 FAIL=0
PASS python3 scripts/frontier_source_measure_pcal_rn_cocycle.py
     SUMMARY: PASS=56 FAIL=0
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block104 and does not push to main.

## PR Identity

```text
PENDING
```
