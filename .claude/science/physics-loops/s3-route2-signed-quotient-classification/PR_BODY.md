## Summary

Block104 prunes the shortcut that a deterministic signed quotient of the four
current `P_R` labels is enough to force the Block102 binary one-point bias.

A quotient map can assign `+/-` labels, but it does not supply the source
measure. Under the uniform four-label measure, nonconstant quotients give
means `-1/2`, `0`, or `1/2`, not `+/-1/3`. With arbitrary source measure, the
same quotient can realize multiple `kappa` values.

## Trace

Trace class: `negative_route_pruning`.

Refined remaining primitive:

```text
Route-2 typed signed quotient plus source-measure bias theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_signed_quotient_classification_no_go_2026_06_22.py
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
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block103 and does not push to main.

## PR Identity

```text
PENDING
```
