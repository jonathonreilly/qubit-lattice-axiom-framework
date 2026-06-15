# Assumptions And Imports

## Quark Route-2

- The current typed-edge bank is the finite configured bank checked by
  `scripts/frontier_quark_route2_source_domain_bridge_no_go.py`.
- The named authority packet is exactly the union of configured edge
  authorities plus dependency-linked Route-2 authorities:
  `S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md`,
  `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`,
  `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md`,
  `QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md`,
  and `RCONN_DERIVED_NOTE.md`.
- The bridge `R_conn = 8/9 -> c_TE = -8/9` remains missing. This PR does not
  supply it.

## YT BC Transfer

- Plaquette constants, Ward target, RGE coefficients, threshold scales, and EW
  initial conditions are accepted-premise implementation inputs for the finite
  runner diagnostic.
- No continuum monotonicity theorem, exact continuum unique-root theorem, or
  physical SM-at-Planck closure is supplied here.

## New Axioms

No new axiom is introduced.
