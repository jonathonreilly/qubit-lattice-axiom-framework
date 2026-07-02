## Summary

Adds an exact support / selector-boundary packet for the Route-2 readout edge:

- `docs/QUARK_ROUTE2_SOURCE_COUNT_SELECTOR_BRIDGE_BOUNDARY_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py`
- paired runner cache under `logs/runner-cache/`
- physics-loop handoff/certificate under `.claude/science/physics-loops/s3-route2-readout-endpoint/`

The result sharpens the compressed bridge target:

```text
kappa = N_color/N_pair = 3/2
s_TE = -N_pair = -2
c_TE = s_TE/kappa^2 = -N_pair^3/N_color^2 = -8/9 = -F_adj
```

It also maps the physical color selector family
`R_phys(xi)=F_adj+xi(1-F_adj)` into exact Route-2 endpoint outputs. Only the
connected specialization `xi=0` gives `rho_E=21/4`; full trace gives
`rho_E=4`.

## Claim Boundary

This PR does not derive `c_TE=-F_adj`, does not derive the connected selector
`xi=0`, does not derive `rho_E=21/4`, and does not apply any audit verdict. It
is exact support for the typed bridge target and a selector-boundary map.

## Trace Gate

- Trace class: upstream_support
- Target claim: `s3_time_theta_to_slice_coupling_note`
- Reachability: supports by sharpening the missing typed bridge into
  `c_TE=-R_phys(0)` / `s_TE/(N_color/N_pair)^2`
- Handoff: `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- Certificate: `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py
  TOTAL: PASS=44, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
  PASS=11 FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_lift_derivation_attempt_bounded_2026_06_12.py
  TOTAL: PASS=46, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_source_domain_bridge_no_go.py
  TOTAL: PASS=103, FAIL=0
python3 scripts/rconn_matching_rule_nogo_certificate.py
  RUNNER STATUS: PASS (PASS=30 FAIL=0)
python3 -m py_compile scripts/frontier_quark_route2_source_count_selector_bridge_boundary_2026_06_21.py
  pass
```

Focused local review disposition: PASS WITH EXACT SUPPORT / SELECTOR
BOUNDARY. Audit pipeline and audit verdict scripts were not run under the
no-audit campaign boundary.
