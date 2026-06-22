## Summary

Block95 prunes the shortcut that anti-invariant E/T output parity alone proves
the connected response is the SU(3) adjoint color bilinear.

An anti-invariant connected response can include adjoint and non-adjoint
connected residue on the same E/T line. The anti-invariant E/T normalization
sees only the sum, so a color-representation typing theorem remains required.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 anti-invariant adjoint-line same-source typing theorem.
```

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_anti_invariant_adjoint_typing_no_go_2026_06_22.py
PASS=67 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.py
PASS=67 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.py
PASS=70 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_color_source_transfer_no_go_2026_06_22.py
PASS=51 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_hessian_et_coefficient_normalization_no_go_2026_06_22.py
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
- This is stacked on Block94 and does not push to main.

## PR Identity

```text
PR #4682
URL: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4682
State: OPEN
Base: physics-loop/s3-route2-symmetric-line-purity-block94-20260622
Head: physics-loop/s3-route2-anti-invariant-adjoint-typing-block95-20260622
```
