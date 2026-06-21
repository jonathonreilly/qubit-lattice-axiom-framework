# [physics-loop] s3-route2-source-scalar-prep-gate block65 no-go

## Summary

This PR adds a science block for the S3/Route-2 endpoint campaign. It tests
whether a channel-scalar source-preparation map
`S(a_E,a_T)=diag(a_E,a_T,a_E,a_T)` can provide the missing source-side
inverse-Schur endpoint factor.

Outcome: no-go for that shortcut. A channel-scalar source map rescales shell
T/E through `a_T/a_E`, but it leaves `q_E` and `q_T` unchanged. It therefore
cannot move the missing `beta_E/alpha_E` factor to `21/4` unless that factor is
already supplied by the readout map.

## Trace

- `TRACE_GATE.md`: `.claude/science/physics-loops/s3-route2-source-scalar-prep-gate/TRACE_GATE.md`
- `HANDOFF.md`: `.claude/science/physics-loops/s3-route2-source-scalar-prep-gate/HANDOFF.md`
- Note: `docs/QUARK_ROUTE2_SOURCE_SCALAR_PREP_GATE_NO_GO_NOTE_2026-06-21.md`
- Runner: `scripts/frontier_quark_route2_source_scalar_prep_gate_no_go_2026_06_21.py`
- Output: `outputs/frontier_quark_route2_source_scalar_prep_gate_no_go_2026_06_21.txt`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_scalar_prep_gate_no_go_2026_06_21.py
TOTAL: PASS=66, FAIL=0

python3 -m py_compile scripts/frontier_quark_route2_source_scalar_prep_gate_no_go_2026_06_21.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_blindness_no_go.py
TOTAL: PASS=14, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
TOTAL: PASS=103, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_route2_readout_record_positivity_no_go.py
TOTAL: PASS=8 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py
PASS=12 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py
PASS=64 FAIL=0

git diff --check
PASS

overclaim scan over changed files
PASS

ASCII scan over changed files
PASS
```

## Status

Actual current-surface status: no-go for channel-scalar source preparation as
the missing Route-2 source-side endpoint theorem. This is not an audit verdict
and does not resolve the parent gate.
