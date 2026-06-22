## Summary

Block97 prunes the shortcut that the current exact finite `K_R -> P_R` readout
surface itself proves the same-source E/T source-Hessian premise from Block96.

The finite `P_R` readout gives endpoint/readout data. A connected Hessian
requires a same-source source two-jet: source coordinates, `Z[J]`, raw second
moments, one-point products, and the identification that the physical E/T
readout is `D^2 log Z`.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 same-source source-jet lift theorem for the physical E/T readout.
```

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py
PASS=63 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_typed_parity_bridge_minimal_cut_2026_06_22.py
PASS=60 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
PASS=49 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_observable_hessian_readout_identification_no_go_2026_06_22.py
PASS=47 FAIL=0

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
- This is stacked on Block96 and does not push to main.

## PR Identity

```text
PENDING
```
