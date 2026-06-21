## Summary

Adds block19 for the S3/Route-2 readout endpoint campaign: an exact-support
inventory of direct theta-to-slice consumers independent of unresolved
`rho_E`.

The exact rule:

```text
c = (u_E, u_T, delta_E, delta_T)
P(rho_E)c = (u_E + rho_E delta_E, -2 u_T + 2 delta_T)
```

So direct consumers with `delta_E=0` are independent of `rho_E`; consumers
with `delta_E != 0` inherit the unresolved scalar source factor.

Honest status: `exact-support` for direct consumer triage. This PR does not
audit, apply verdicts, push to main, or claim the endpoint is closed.

## Artifacts

- `docs/S3_TIME_ENDPOINT_INDEPENDENT_CONSUMER_INVENTORY_NOTE_2026-06-21.md`
- `scripts/frontier_s3_time_endpoint_independent_consumer_inventory_2026_06_21.py`
- `logs/runner-cache/frontier_s3_time_endpoint_independent_consumer_inventory_2026_06_21.txt`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/TRACE_GATE.md`
- `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_endpoint_independent_consumer_inventory_2026_06_21.py`
  - `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py`
  - `PASS=11 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_time_coupling.py`
  - `PASS=8 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py`
  - `PASS=12 FAIL=0`
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_primitive_chain_reaudit.py`
  - `PASS=24 FAIL=0`
- `python3 -m py_compile scripts/frontier_s3_time_endpoint_independent_consumer_inventory_2026_06_21.py`
- `git diff --check`
- overclaim wording scan

## Review Notes

No PR conflict or mergeability check will be run. Existing physics-loop PRs are
not refreshed to main; the reviewer owns cherry-picking the science.
