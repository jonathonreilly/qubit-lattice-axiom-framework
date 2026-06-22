# Summary

Block68 attacks the endpoint orientation sign `sigma=-1` exposed by Block67.
The result is conditional support: under the Route-2 endpoint algebra,
conditional shell `T/E=-2`, `q_T>0`, and positive `q_E`, the sign is forced:

```text
sign(c_TE)=sign(shell T/E)=-1.
```

This narrows the bridge.  The sign is not the remaining hard magnitude
problem under those premises; the connected selector `kappa=0`, or an
equivalent theorem forcing `|c_TE|=8/9`, remains open.

# Trace

- Trace class: `upstream_support`
- Target blocker: `underlying readout-map endpoint triple is not yet derived`
- Parent consumer: `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`
- Handoff: `.claude/science/physics-loops/s3-route2-endpoint-orientation-sign/HANDOFF.md`
- Trace gate: `.claude/science/physics-loops/s3-route2-endpoint-orientation-sign/TRACE_GATE.md`

# Artifacts

- `docs/QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md`
- `scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py`
- `outputs/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.txt`
- `.claude/science/physics-loops/s3-route2-endpoint-orientation-sign/`

# Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py
TOTAL: PASS=38, FAIL=0

python3 -m py_compile scripts/frontier_quark_route2_endpoint_orientation_sign_support_2026_06_22.py
PASS

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_factorization_no_go_2026_06_22.py
TOTAL: PASS=35, FAIL=0

PYTHONPATH=scripts python3 scripts/rconn_matching_rule_nogo_certificate.py
RUNNER STATUS: PASS (PASS=30 FAIL=0)

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
TOTAL: PASS=103, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
PASS=11 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_quark_route2_direct_e_center_readout_family_no_go_2026_06_22.py
TOTAL: PASS=49, FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling.py
PASS=12 FAIL=0

PYTHONPATH=scripts python3 scripts/frontier_s3_time_theta_to_slice_coupling_factor_rigidity.py
PASS=64 FAIL=0
```

Branch-local review passed.  Audit pipeline intentionally not run; no audit
verdict applied.

# Remaining Blocker

The next direct target is the connected-current selector theorem `kappa=0`.
