# Assumptions And Imports

## Current-Surface Premises

- The branch starts from `origin/main` at
  `2cdf7fcbd900648d3ded4fb08afb44051b170a01`.
- The source note is
  `docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- The paired runner is
  `scripts/frontier_quark_route2_exact_readout_map.py`.
- The existing runner-supported result is an exact carrier/readout reduction
  plus a missing-map obstruction, not a complete exact readout theorem.

## Forbidden Imports

- No observed quark masses or fitted target values are imported as proof inputs
  in this repair.
- No audit verdict, effective retained status, or expected audit result is
  asserted.
- No repo-wide authority surface is edited by hand; generated audit and
  publication surfaces come from `bash docs/audit/scripts/run_pipeline.sh`.

## Open Imports Exposed

- The unresolved theorem step remains the readout map entry
  `rho_E = beta_E / alpha_E`.
- The full triple `(rho_T, mu, rho_E)` remains unproved on the current source
  surface.
