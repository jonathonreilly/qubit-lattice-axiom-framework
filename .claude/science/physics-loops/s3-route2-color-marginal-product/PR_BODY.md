## Summary

Block108 tests a narrow non-binary product route. SU(3) rank-one color
marginals have one-point value `1/3`, hence disconnected product `1/9`.

That is exact upstream support for Block107, but Route-2 still needs a
same-source color-marginal transfer and raw moment theorem.

## Trace

Trace class: `upstream_support`.

Remaining primitive:

```text
Route-2 same-source color-marginal product theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_color_marginal_product_support_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_marginal_product_support_no_go_2026_06_22.py
     TOTAL: PASS=56, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_nonbinary_product_normal_form_support_2026_06_22.py
     TOTAL: PASS=70, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_su3_record_ensemble_transfer_no_go_2026_06_22.py
     TOTAL: PASS=64, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_trace_one_color_record_transfer_no_go_2026_06_22.py
     TOTAL: PASS=52, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
     PASS=11 FAIL=0
PASS python3 scripts/frontier_yukawa_color_projection_boundary.py
     PASS=40 FAIL=0
PASS python3 scripts/uv_gauge_to_yukawa_bridge_sc_vs_pert_scope_check.py
     SUMMARY: PASS=21 FAIL=0
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block107 and does not push to main.

## PR Identity

```text
number: 4695
url: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4695
title: [physics-loop] s3-route2 color marginal product block108 support
base: physics-loop/s3-route2-nonbinary-product-normal-form-block107-20260622
head: physics-loop/s3-route2-color-marginal-product-block108-20260622
science_commit: e88852585
```
