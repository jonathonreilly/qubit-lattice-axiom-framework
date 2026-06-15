# Claim Status Certificate

## What Changed

Added a source-side Wilson readout-boundary certificate:

- `docs/WILSON_EXTREMUM_CURVATURE_READOUT_BOUNDARY_CERTIFICATE_2026-06-15.md`
- `scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py`

Updated the audited conditional source note:

- `docs/WILSON_M_H_TREE_AT_EXTREMUM_LEADING_ORDER_IN_R_BOUNDED_NOTE_2026-05-08.md`
- `scripts/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.py`

## Scientific Boundary

Closed source-side support:

- Wilson staircase normalization is explicitly `W(hw) = 2 r hw`.
- The leading curvature-scale formula follows from the shifted-extremum
  curvature divided by the declared diagnostic count `N_taste = 16`.
- The square-root Taylor truncation is checked against the closed form.
- The leading square-form approximation is checked against the
  all-orders Wilson closed form with `O(r^4)` residual scaling.

Still outside scope:

- physical Higgs-pole readout;
- channel-selection principle that would derive a physical uniform
  all-corners Higgs channel;
- a nonzero numerical Wilson coefficient;
- any audit status change.

## Verification

Commands run:

```bash
PYTHONPATH=scripts python3 scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py
PYTHONPATH=scripts python3 scripts/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.py
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py,scripts/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.py --force --push-mode=none
python3 -m py_compile scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py scripts/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.py
PYTHONPATH=scripts python3 scripts/precompute_audit_runners.py --runners scripts/wilson_extremum_curvature_readout_boundary_2026_06_15.py,scripts/frontier_wilson_m_h_tree_at_extremum_leading_order_in_r.py --check-only --push-mode=none
python3 docs/audit/scripts/audit_lint.py --strict
git diff --check
```

Results:

- New certificate runner: `TOTAL: PASS=28, FAIL=0`
- Updated Wilson leading-order runner: `TOTAL: PASS=89, FAIL=0`
- Cache freshness: all relevant caches fresh
- Strict lint: OK, no errors; expected non-retained row hash-drift
  notice for the edited Wilson note
- Diff whitespace check: OK
