## Summary

Block99 prunes the shortcut that a bare formal source-coordinate registry is
enough to force `kappa=0`.

The packet shows that formal mixed-partial integrability is too weak: with
three source coordinates, the four finite Route-2 slots can be embedded in a
symmetric quadratic `W`, and the same formal registry skeleton accepts
`R_conn(kappa)=8/9+kappa/9` for multiple `kappa` values.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 typed source-action/product registry theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_formal_source_coordinate_registry_vacuity_no_go_2026_06_22.py
     TOTAL: PASS=88, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_integrability_gate_no_go_2026_06_22.py
     TOTAL: PASS=53, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py
     TOTAL: PASS=63, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py
     TOTAL: PASS=60, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.py
     TOTAL: PASS=70, FAIL=0
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
- This is stacked on Block98 and does not push to main.

## PR Identity

```text
PENDING
```
