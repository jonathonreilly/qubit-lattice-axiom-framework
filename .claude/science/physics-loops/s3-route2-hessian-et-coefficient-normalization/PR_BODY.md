## Summary

Block89 prunes the shortcut that a same-source connected color Hessian fixes
the Route-2 scalar `E/T` bridge by SU(3) covariance alone.

The invariant symmetric adjoint bilinear is unique up to scale, so a connected
color Hessian supplies one Killing/Hilbert-Schmidt color block. The two Route-2
scalar outputs still have free coefficients:

```text
H_E = lambda_E B,   H_T = lambda_T B.
```

Thus `kappa=0` support and E/T coefficient normalization are separate gates.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 connected-Hessian E/T coefficient normalization theorem.
```

## Verification

```text
PASS python3 -m py_compile scripts/frontier_quark_route2_hessian_et_coefficient_normalization_no_go_2026_06_22.py
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_et_coefficient_normalization_no_go_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py
     TOTAL: PASS=50, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_invariant_scalar_output_coupling_no_go_2026_06_22.py
     TOTAL: PASS=50, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
     TOTAL: PASS=49, FAIL=0
PASS PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
     PASS=11 FAIL=0
PASS git diff --check
PASS STATE.yaml parse
PASS ASCII scan
PASS overclaim marker scan
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No endpoint value was used.
- This is stacked on Block88 and does not push to main.

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4676
Number: 4676
Base: physics-loop/s3-route2-covariant-scalarization-collapse-block88-20260622
Head: physics-loop/s3-route2-hessian-et-coefficient-normalization-block89-20260622
Science commit: 2e2c75fde
```
