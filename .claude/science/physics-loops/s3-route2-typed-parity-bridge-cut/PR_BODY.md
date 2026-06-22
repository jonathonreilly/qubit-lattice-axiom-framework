## Summary

Block96 synthesizes Blocks 92-95 into a minimal typed parity bridge cut.

For `kappa=0`, the route needs three same-source premises: physical E/T source
Hessian, symmetric pure-disconnected typing, and anti-invariant adjoint-line
typing. The scalar E/T coefficient bridge additionally needs the
anti-invariant normalizer from framework primitives.

## Trace

Trace class: `upstream_support`.

Remaining primitive:

```text
Route-2 same-source typed parity source-Hessian theorem on the physical E/T readout.
```

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py
PASS=60 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.py
PASS=67 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.py
PASS=67 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.py
PASS=70 FAIL=0

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
- This is stacked on Block95 and does not push to main.

## PR Identity

```text
PENDING
```
