## Summary

Block92 prunes the shortcut that a neutral same-source scalar normalization
can fix the antisymmetric `E/T` Hessian coefficient scale left open by
Block91.

In the coefficient space

```text
(lambda_E, lambda_T) = s(1,-1) + t(1,1),
```

an E/T-invariant normalization annihilates the antisymmetric line. A
normalization that sees `s` must have an anti-invariant component, which is
already typed E/T orientation data and still does not prove `t=0`.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 anti-invariant same-source E/T normalization and purity theorem.
```

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.py
PASS=55 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_antisymmetric_coeff_scale_no_go_2026_06_22.py
PASS=47 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_carrier_antisymmetric_hessian_coeff_no_go_2026_06_22.py
PASS=48 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_et_coefficient_normalization_no_go_2026_06_22.py
PASS=49 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
PASS=49 FAIL=0

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
- This is stacked on Block91 and does not push to main.

## PR Identity

```text
PR #4679
URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4679
State: OPEN
Base: physics-loop/s3-route2-antisymmetric-coeff-scale-block91-20260622
Head: physics-loop/s3-route2-normalization-functional-parity-block92-20260622
```
