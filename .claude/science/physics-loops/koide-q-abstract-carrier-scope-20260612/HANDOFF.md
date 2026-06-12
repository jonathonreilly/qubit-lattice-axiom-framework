# Handoff

## What Changed

This branch repairs the Koide `Q` selector row by making the load-bearing theorem explicitly abstract:

```text
x = (u, v, w), with cyclic C_3 action.
```

On that carrier, there is no nontrivial scale-free invariant at linear order, and at quadratic order there is exactly one nontrivial scale-free ratio, represented by `E_perp/E_+`, `2/kappa`, or `Q`.

The physical identification with the staggered-Dirac second-order returned mass carrier remains future/open context. The source note no longer links that open gate as a markdown dependency.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_koide_q_minimal_scale_free_selector.py`
  - `TOTAL: PASS=13 FAIL=0`
- `python3 scripts/precompute_audit_runners.py --runners scripts/frontier_koide_q_minimal_scale_free_selector.py --force --concurrency 1 --push-mode none --allow-non-main`
  - `ok 1`, `nonzero_exit 0`

## Boundaries

- No ledger edits.
- No audit verdict/status assertion.
- Does not derive the physical staggered-Dirac carrier.
- Does not close native Koide `Q`.
- Does not select the physical value law.
- Does not add or change axioms.
