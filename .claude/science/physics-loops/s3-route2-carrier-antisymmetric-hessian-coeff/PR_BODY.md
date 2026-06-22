## Summary

Block90 tests whether the current carrier-orbit invariance support supplies
the exact antisymmetric `E/T` coefficient primitive needed by Block89.

It does not. The carrier-orbit work gives useful `Z_2` operator
classification, but it leaves registry closure open and treats
`Theta_R^(0)` / `Xi_R^(0)` as bounded candidates, not exact connected-Hessian
coefficient-normalization theorems.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 exact antisymmetric E/T Hessian-coefficient primitive.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.py
     TOTAL: PASS=48, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_et_coefficient_normalization_no_go_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py
     TOTAL: PASS=50, FAIL=0
PASS python3 scripts/frontier_carrier_orbit_invariance.py
     PASS=65 FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
     PASS=11 FAIL=0
PASS git diff --check
PASS STATE.yaml parse
PASS ASCII scan
PASS overclaim marker scan
```

## Notes

- No audit workers were run.
- No registry audit was performed.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block89 and does not push to main.

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4677
Number: 4677
Base: physics-loop/s3-route2-hessian-et-coefficient-normalization-block89-20260622
Head: physics-loop/s3-route2-carrier-antisymmetric-hessian-coeff-block90-20260622
Science commit: b2c00fd29
```
