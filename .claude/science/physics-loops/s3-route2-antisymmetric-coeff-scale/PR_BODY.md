## Summary

Block91 prunes the shortcut that an exact antisymmetric `E/T` direction alone
fixes the connected-Hessian coefficient vector.

The direction `(1,-1)` fixes a line, not the scale-normalized vector. The
coefficient family is:

```text
(lambda_E, lambda_T) = s(1,-1) + t(1,1).
```

The missing theorem must fix `s` from same-source normalization and exclude or
fix symmetric contamination `t`.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 scale-normalized pure-antisymmetric Hessian coefficient theorem.
```

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.py
PASS=47 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.py
PASS=48 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_et_coefficient_normalization_no_go_2026_06_22.py
PASS=49 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py
PASS=50 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
PASS=49 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

git diff --check
PASS

STATE.yaml parse
PASS

ASCII scan
PASS

overclaim scan
PASS
```

## Notes

- No audit workers were run.
- No audit verdicts were applied.
- No review-loop worker was run during this block; reviewer/cherry-pick
  handling is left to the PR review path.
- No endpoint value was used.
- This is stacked on Block90 and does not push to main.

## PR Identity

```text
PR #4678
URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4678
State: OPEN
Base: physics-loop/s3-route2-carrier-antisymmetric-hessian-coeff-block90-20260622
Head: physics-loop/s3-route2-antisymmetric-coeff-scale-block91-20260622
```
