## Summary

Block100 prunes the shortcut that generic source-measure Pcal/Mobius support
already supplies the Route-2 raw/one-point product registry needed after
Block99.

Pcal/Mobius gives the abstract identity
`D_A D_B log Z = D_A D_B Z - D_A Z D_B Z`. It does not identify Route-2
physical record variables, raw `P_R/E-T` moment slots, or the one-point product
that makes the symmetric singlet line pure disconnected.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 Pcal product-instantiation theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_measure_product_registry_transfer_no_go_2026_06_22.py
     TOTAL: PASS=72, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.py
     TOTAL: PASS=88, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_integrability_gate_no_go_2026_06_22.py
     TOTAL: PASS=53, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS python3 scripts/frontier_source_measure_pcal_cumulant_mobius.py
     SUMMARY: PASS=33 FAIL=0
PASS python3 scripts/frontier_source_measure_pcal_rn_cocycle.py
     SUMMARY: PASS=56 FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_measure_color_ensemble_transfer_no_go_2026_06_22.py
     TOTAL: PASS=58, FAIL=0
PASS git diff --check
PASS YAML parse for STATE.yaml
PASS ASCII scan
PASS banned overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block99 and does not push to main.

## PR Identity

```text
PENDING
```
