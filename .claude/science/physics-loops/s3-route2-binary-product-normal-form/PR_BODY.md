## Summary

Block102 gives a conditional binary product normal form for the Route-2 Pcal
product theorem.

Under the normalized binary same-record ansatz with `E[XY]=1`, Pcal connected
subtraction gives `1 - m^2`. Thus `kappa=0` is equivalent to
`|E[X]|=1/3`, i.e. a `2:1` or `1:2` binary record bias.

## Trace

Trace class: `upstream_support`.

Remaining primitive:

```text
Route-2 binary one-point bias theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_binary_product_normal_form_support_2026_06_22.py
     TOTAL: PASS=72, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_pcal_moment_realization_no_go_2026_06_22.py
     TOTAL: PASS=75, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py
     TOTAL: PASS=72, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py
     TOTAL: PASS=60, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS python3 scripts/frontier_source_measure_pcal_cumulant_mobius.py
     SUMMARY: PASS=33 FAIL=0
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block101 and does not push to main.

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4689
Number: 4689
Title: [physics-loop] s3-route2 binary product normal form block102 conditional-support
State: OPEN
Base: physics-loop/s3-route2-pcal-moment-realization-block101-20260622
Head: physics-loop/s3-route2-binary-product-normal-form-block102-20260622
Science commit: 5e6baa4a8
```
