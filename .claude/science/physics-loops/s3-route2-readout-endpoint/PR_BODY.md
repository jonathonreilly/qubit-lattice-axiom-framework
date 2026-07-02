## Summary

Adds a branch-local S3/Route-2 direct-consumer packet:

- `docs/S3_TIME_THETA_TO_SLICE_READOUT_WITNESS_CRITERION_NOTE_2026-06-21.md`
- `scripts/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.py`
- paired runner cache under `logs/runner-cache/`
- physics-loop handoff/certificate under `.claude/science/physics-loops/s3-route2-readout-endpoint/`

The science result is bounded support / negative route pruning. Inside the
existing conditional family `Xi_P(t; c) = (P_R c) tensor V_R(t)`, a downstream
linear witness can distinguish `rho_E` only through overlap with the exact
E-center ambiguity vector. Shell-only, T-row-only, and time-ratio-only
consumers are blind to the missing `rho_E = 21/4` direction.

## Claim Boundary

This PR does not derive the endpoint triple `(-1, -2, 21/4)`, does not close
`s3_time_theta_to_slice_coupling_note`, and does not apply any audit verdict.
It narrows the next positive target to a typed E-center source/readout
primitive supplying `q_E = 15/8` or equivalently `c_TE = -8/9`.

## Trace Gate

- Trace class: negative_route_pruning
- Target claim: `s3_time_theta_to_slice_coupling_note`
- Reachability: prunes blind downstream consumers and sharpens the remaining
  E-center witness primitive
- Handoff: `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- Certificate: `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.py
  TOTAL: PASS=16, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py
  PASS=12 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py
  PASS=64 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
  PASS=11 FAIL=0
python3 -m py_compile scripts/frontier_s3_time_theta_to_slice_readout_witness_criterion_2026_06_21.py
  pass
```

Focused local review disposition: PASS WITH BOUNDED CLAIMS. Audit pipeline and
audit verdict scripts were not run under the no-audit campaign boundary.
