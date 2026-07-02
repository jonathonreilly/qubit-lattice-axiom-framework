# [physics-loop] s3-route2-center-excess-source-target block66 bounded-support

## Summary

This PR adds a bounded-support science block for the S3/Route-2 endpoint
campaign. It isolates the exact endpoint-normalized source-excess theorem
needed after a one-power Schur readout premise.

Outcome: if the readout side supplies `rho_E=3/2` and the source side is
endpoint-normalized, then the source map must supply:

```text
a_T/a_E = 1
b_T/a_T = 1
b_E/a_E = 7/2.
```

That condition is sufficient and necessary in the normalized class to reach
`rho_E=21/4`, `q_E=15/8`, and center T/E `=-8/9`. The PR does not claim the
current source bank derives this map.

## Trace

- `TRACE_GATE.md`: `.claude/science/physics-loops/s3-route2-center-excess-source-target/TRACE_GATE.md`
- `HANDOFF.md`: `.claude/science/physics-loops/s3-route2-center-excess-source-target/HANDOFF.md`
- Note: `docs/QUARK_ROUTE2_CENTER_EXCESS_SOURCE_TARGET_NOTE_2026-06-21.md`
- Runner: `scripts/frontier_quark_route2_center_excess_source_target_2026_06_21.py`
- Output: `outputs/frontier_quark_route2_center_excess_source_target_2026_06_21.txt`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_center_excess_source_target_2026_06_21.py
TOTAL: PASS=43, FAIL=0

python3 -m py_compile scripts/frontier_quark_route2_center_excess_source_target_2026_06_21.py
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

Actual current-surface status: bounded-support for the normalized
center-excess source target. This is not an audit verdict and does not resolve
the parent gate.
