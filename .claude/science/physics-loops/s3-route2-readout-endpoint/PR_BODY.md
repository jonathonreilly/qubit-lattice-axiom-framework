## Summary

Block20 adds an exact support/boundary split for the S3/Route-2 readout endpoint campaign.

New artifact:

- `docs/S3_TIME_FACTOR_RIGIDITY_READOUT_PRIMITIVE_SPLIT_NOTE_2026-06-21.md`
- `scripts/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.py`
- `outputs/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.txt`

Also includes a narrow tolerance repair in
`scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py`
for the floating live `t_balance` comparator. This does not change the bridge
claim boundary.

Main result:

```text
(P(rho_b)-P(rho_a))(u_E,u_T,delta_E,delta_T)
  = ((rho_b-rho_a) delta_E, 0).
```

So factor-rigidity is safe for `Lambda_R`, `V_R(t)`, norm-ratio cancellation,
semigroup propagation, and rank-one localization, but it does not select the
readout primitive. The unresolved entry is exactly the E-center / `delta_E`
spatial prefactor wall.

## Claim Boundary

Actual current-surface status: `exact-support`.

This PR does not select a unique `P_R`, does not close the endpoint triple
`(-1, -2, 21/4)`, and is not a derivation of the readout primitive.

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.py`
  - `TOTAL: PASS=49, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py`
  - `PASS=64 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py`
  - `TOTAL: PASS=14, FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py`
  - `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  - `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `python3 -m py_compile scripts/frontier_s3_time_factor_rigidity_readout_primitive_split_2026_06_21.py scripts/frontier_s3_time_readout_primitive_bridge_assessment_2026_06_12.py`
  - pass
- `git diff --check`
  - pass
- overclaim wording scan
  - clean

## Handoff

- Loop pack: `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- Claim certificate: `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`
