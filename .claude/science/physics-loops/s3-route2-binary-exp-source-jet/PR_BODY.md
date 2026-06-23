# Summary

Block143 packages exact support for the source-jet route:

```text
Z_CR[J] = (2/3) exp(J) + (1/3) exp(-J)
```

At zero source, `D Z_CR=1/3`, `D^2 Z_CR=1`, and `D^2 log Z_CR=8/9`, so the
formal source-cumulant selector is `kappa=0`.

This is not an audit verdict. No audit worker was run and no audit verdict was
applied.

## Trace

```yaml
trace_class: upstream_support
reachability_to_target: supports
artifact_role: theorem
```

## Boundary

The packet does not prove the physical Route-2 source typing, same-source
Riesz/unit-isometry, or orientation sign. Those remain the exact open imports.

## Files

- `docs/QUARK_ROUTE2_BINARY_EXP_SOURCE_JET_SUPPORT_2026-06-22.md`
- `scripts/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.py`
- `outputs/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.txt`
- `.claude/science/physics-loops/s3-route2-binary-exp-source-jet/`

## Verification

```text
python3 -m py_compile scripts/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.py
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.py | tee outputs/frontier_quark_route2_binary_exp_source_jet_support_2026_06_22.txt
  TOTAL: PASS=95, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_hessian_cumulant_selector_support_2026_06_22.py
  TOTAL: PASS=49, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_jet_lift_no_go_2026_06_22.py
  TOTAL: PASS=63, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_readout_isometry_sufficient_support_2026_06_22.py
  TOTAL: PASS=81, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_factorization_no_go_2026_06_22.py
  TOTAL: PASS=35, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_pr_row_ocr_functor_no_go_2026_06_22.py
  TOTAL: PASS=72, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_covariant_scalarization_collapse_no_go_2026_06_22.py
  TOTAL: PASS=50, FAIL=0
STATE.yaml parse OK
git diff --check: pass
ASCII scan: no hits
overclaim marker scan: no hits
```

## PR Identity

```text
PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4730
head: physics-loop/s3-route2-source-jet-exponential-family-support-block143-20260622
base: physics-loop/s3-route2-pr-row-ocr-functor-no-go-block142-20260622
science commit: 9d7f550a3
```
