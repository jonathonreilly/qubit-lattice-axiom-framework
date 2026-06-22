## Summary

This PR adds the Block71 Route-2 full-trace exclusion no-go packet.

Block70 narrowed the connected-current selector to the two idempotent endpoints:

```text
kappa in {0,1}.
```

This block tests whether the current exact controls exclude `kappa=1`.  They
do not.  The full-trace endpoint survives idempotence, positivity,
channel-scalar form, positive readout domain, endpoint orientation sign, CMT
scale invariance, and bounded OZI-size control.

Claim-state movement: `negative_route_pruning`.  Excluding full trace is
equivalent to adding a singlet-annihilation or disconnected-current-zero
theorem; it is not derived here.

## Artifacts

- Handoff: `.claude/science/physics-loops/s3-route2-full-trace-exclusion/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-full-trace-exclusion/TRACE_GATE.md`
- Certificate: `.claude/science/physics-loops/s3-route2-full-trace-exclusion/CLAIM_STATUS_CERTIFICATE.md`
- Note: `docs/QUARK_ROUTE2_FULL_TRACE_EXCLUSION_NO_GO_NOTE_2026-06-22.md`
- Runner: `scripts/frontier_quark_route2_full_trace_exclusion_no_go_2026_06_22.py`
- Output: `outputs/frontier_quark_route2_full_trace_exclusion_no_go_2026_06_22.txt`

## Verification

Branch-local review passed. Audit pipeline intentionally not run; no audit
verdict applied.

- `python3 -m py_compile scripts/frontier_quark_route2_full_trace_exclusion_no_go_2026_06_22.py` - PASS.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_full_trace_exclusion_no_go_2026_06_22.py` - PASS, `TOTAL: PASS=50, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.py` - PASS, `TOTAL: PASS=36, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_current_selector_no_go_2026_06_22.py` - PASS, `TOTAL: PASS=53, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_factorization_no_go_2026_06_22.py` - PASS, `TOTAL: PASS=35, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py` - PASS, `TOTAL: PASS=38, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/rconn_matching_rule_nogo_certificate.py` - PASS, `PASS=30 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py` - PASS, `PASS=11 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py` - PASS, `TOTAL: PASS=103, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py` - PASS, `PASS=12 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py` - PASS, `PASS=64 FAIL=0`.

## Remaining Blocker

The exact connected selector still needs a singlet-annihilation theorem.  The
next queued direct consumer is the positive E-center readout domain theorem
`q_E>0`.
