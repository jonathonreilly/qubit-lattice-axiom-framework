# Summary

Block145 prunes the shortcut:

```text
signed quotient + ordinary source-measure controls => Route-2 2:1 bias
```

Normalization, positivity, RN absolute continuity, and sign-quotient data
leave a family of binary source measures. The missing primitive is the
Route-2 theorem proving `P(+1):P(-1)=2:1` or `1:2` from physical structure.

This is not an audit verdict. No audit worker was run and no audit verdict was
applied.

## Trace

```yaml
trace_class: negative_route_pruning
reachability_to_target: prunes
artifact_role: no_go
```

## Files

- `docs/QUARK_ROUTE2_SOURCE_MEASURE_BIAS_NO_GO_2026-06-22.md`
- `scripts/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.py`
- `outputs/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.txt`
- `.claude/science/physics-loops/s3-route2-source-measure-bias/`

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.py | tee outputs/frontier_quark_route2_source_measure_bias_no_go_2026_06_22.txt
  TOTAL: PASS=87, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_physical_jcr_typing_no_go_2026_06_22.py
  TOTAL: PASS=95, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_signed_quotient_classification_no_go_2026_06_22.py
  TOTAL: PASS=67, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.py
  TOTAL: PASS=72, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_binary_same_record_transfer_no_go_2026_06_22.py
  TOTAL: PASS=60, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
  TOTAL: PASS=49, FAIL=0
STATE.yaml parse OK
git diff --check: pass
ASCII scan: no hits
overclaim marker scan: no hits
```

## PR Identity

```text
pending_create
```
