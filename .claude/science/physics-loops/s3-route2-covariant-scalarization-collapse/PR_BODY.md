## Summary

Block88 prunes the shortcut that a covariant `sl_3` color-readout family can
be collapsed to invariant scalar orbit data and then treated as the Route-2
scalar `E/T` bridge.

`Tr(X^2)` and `Tr(X^3)` are useful invariant color scalars, but scalarization
loses the adjoint-valued source/readout typing before the Route-2 physical
readout is identified. A family `a Tr(X^2) + b Tr(X^3)` is still free unless a
same-source readout theorem fixes the coefficients and channel assignment.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 covariant-family connected-Hessian E/T readout theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py
     TOTAL: PASS=50, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.py
     TOTAL: PASS=50, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_observable_hessian_readout_identification_no_go_2026_06_22.py
     TOTAL: PASS=47, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_color_source_transfer_no_go_2026_06_22.py
     TOTAL: PASS=51, FAIL=0
PASS git diff --check
PASS STATE.yaml parse
PASS ASCII scan
PASS overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block87 and does not push to main.

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4675
Number: 4675
Base: physics-loop/s3-route2-invariant-scalar-output-coupling-block87-20260622
Head: physics-loop/s3-route2-covariant-scalarization-collapse-block88-20260622
Science commit: 7b89b45c5
```
