## Summary

Block94 prunes the shortcut that E/T symmetry alone makes the symmetric
source-Hessian line pure disconnected.

Both disconnected and connected singlet terms are E/T-symmetric. `D^2 log Z`
subtracts only the factorizable disconnected piece, so a connected symmetric
residue survives as `kappa` unless a same-source factorization theorem proves
`eta=0`.

## Trace

Trace class: `negative_route_pruning`.

Remaining primitive:

```text
Route-2 symmetric-line pure-disconnected same-source typing theorem.
```

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_symmetric_line_purity_no_go_2026_06_22.py
PASS=67 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_parity_source_hessian_sufficient_2026_06_22.py
PASS=70 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
PASS=49 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_color_source_transfer_no_go_2026_06_22.py
PASS=51 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_normalization_functional_parity_no_go_2026_06_22.py
PASS=55 FAIL=0

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
- This is stacked on Block93 and does not push to main.

## PR Identity

```text
PENDING
```
