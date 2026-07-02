## Summary

Adds exact support for the Route-2 bridge-equivalence boundary:

- `docs/QUARK_ROUTE2_COLOR_COVARIANCE_BRIDGE_EQUIVALENCE_SUPPORT_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.py`
- paired runner cache under `logs/runner-cache/`
- physics-loop handoff/certificate under `.claude/science/physics-loops/s3-route2-readout-endpoint/`

The result: under the granted T-side orientation `s_TE=-2`, the two live
positive bridge targets are algebraically equivalent:

```text
lambda = q_E/q_T = kappa^2
<=> c_TE = s_TE/kappa^2
<=> c_TE = -F_adj.
```

So the typed color bridge and typed covariance bridge are not independent
missing primitives on the current Route-2 surface. A future positive route
still needs typed source/readout semantics for this compressed bridge.

## Claim Boundary

This PR does not derive `lambda=kappa^2`, does not derive `c_TE=-F_adj`, does
not derive `rho_E=21/4`, and does not apply any audit verdict. It is exact
support for bridge targeting, not endpoint closure.

## Trace Gate

- Trace class: upstream_support
- Target claim: `s3_time_theta_to_slice_coupling_note`
- Reachability: supports by compressing the two remaining positive bridge
  routes into one typed edge target
- Handoff: `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- Certificate: `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.py
  TOTAL: PASS=23, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_qe_kappa_squared_covariance_sharper_no_go_2026_06_10.py
  TOTAL: PASS=7 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py
  TOTAL: PASS=62, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
  PASS=11 FAIL=0
python3 -m py_compile scripts/frontier_quark_route2_color_covariance_bridge_equivalence_2026_06_21.py
  pass
```

Focused local review disposition: PASS WITH EXACT SUPPORT BOUNDARY. Audit
pipeline and audit verdict scripts were not run under the no-audit campaign
boundary.
