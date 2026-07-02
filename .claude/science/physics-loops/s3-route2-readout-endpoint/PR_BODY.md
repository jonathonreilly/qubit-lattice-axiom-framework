## Summary

Adds a bounded current-bank no-go for the Route-2 E-center source/readout
primitive:

- `docs/QUARK_ROUTE2_E_CENTER_CURRENT_SOURCE_BANK_NO_GO_NOTE_2026-06-21.md`
- `scripts/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.py`
- paired runner cache under `logs/runner-cache/`
- physics-loop handoff/certificate under `.claude/science/physics-loops/s3-route2-readout-endpoint/`

The exact counter-witness is that `P(0)` and `P(21/4)` share the current
source-bank invariants (`delta_A1`, `K_R`, T-side candidates, `F_adj`,
`kappa`, positivity/sign facts), while their E-center lifts differ. Therefore
the current source bank cannot derive `rho_E=21/4` without an additional
non-blind E-center bridge.

## Claim Boundary

This PR does not derive `rho_E=21/4`, does not close
`s3_time_theta_to_slice_coupling_note`, and does not apply any audit verdict.
It prunes current-bank recombination attempts and leaves future source-domain,
typed `F_adj`, and typed covariance bridges open.

## Trace Gate

- Trace class: negative_route_pruning
- Target claim: `s3_time_theta_to_slice_coupling_note`
- Reachability: prunes current-bank-only E-center source derivations
- Handoff: `.claude/science/physics-loops/s3-route2-readout-endpoint/HANDOFF.md`
- Certificate: `.claude/science/physics-loops/s3-route2-readout-endpoint/CLAIM_STATUS_CERTIFICATE.md`

## Verification

```text
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.py
  TOTAL: PASS=21, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_rconn_typed_bridge_derivation_bounded_2026_06_12.py
  TOTAL: PASS=62, FAIL=0
PYTHONPATH=scripts python3 scripts/quark_route2_ell_e_structural_narrowing_bounded_2026_06_12.py
  TOTAL: PASS=47, FAIL=0
PYTHONPATH=scripts python3 scripts/frontier_quark_route2_exact_readout_map.py
  PASS=11 FAIL=0
python3 -m py_compile scripts/frontier_quark_route2_e_center_current_source_bank_no_go_2026_06_21.py
  pass
```

Focused local review disposition: PASS WITH BOUNDED NO-GO CLAIM. Audit
pipeline and audit verdict scripts were not run under the no-audit campaign
boundary.
