## Summary

This PR adds the Block70 Route-2 current-projector idempotence support packet.

Block69 left the connected-current selector as a free two-channel coefficient:

```text
R_phys(kappa) = F_adj + kappa F_singlet.
```

This block imposes exact current-projector idempotence and proves the resulting
dichotomy:

```text
kappa^2 = kappa => kappa in {0,1}.
```

Claim-state movement: `upstream_support`.  This is bounded support, not endpoint
closure: idempotence narrows the continuous selector to connected versus full
trace, but does not exclude the full-trace endpoint.

## Artifacts

- Handoff: `.claude/science/physics-loops/s3-route2-current-projector-idempotence/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-current-projector-idempotence/TRACE_GATE.md`
- Certificate: `.claude/science/physics-loops/s3-route2-current-projector-idempotence/CLAIM_STATUS_CERTIFICATE.md`
- Note: `docs/QUARK_ROUTE2_CURRENT_PROJECTOR_IDEMPOTENCE_SUPPORT_NOTE_2026-06-22.md`
- Runner: `scripts/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.py`
- Output: `outputs/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.txt`

## Verification

Branch-local review passed. Audit pipeline intentionally not run; no audit
verdict applied.

- `python3 -m py_compile scripts/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.py` - PASS.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_current_projector_idempotence_support_2026_06_22.py` - PASS, `TOTAL: PASS=36, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_connected_current_selector_no_go_2026_06_22.py` - PASS, `TOTAL: PASS=53, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/rconn_matching_rule_nogo_certificate.py` - PASS, `PASS=30 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py` - PASS, `TOTAL: PASS=38, FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py` - PASS, `PASS=11 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py` - PASS, `PASS=12 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py` - PASS, `PASS=64 FAIL=0`.
- `PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py` - PASS, `TOTAL: PASS=103, FAIL=0`.

## Remaining Blocker

The next exact theorem target is full-trace exclusion, equivalently
singlet-annihilation, selecting `kappa=0` over `kappa=1`.
