# Assumptions And Imports

## Allowed Current-Surface Inputs

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Restricted readout family `P(rho_E)` | defines readout ambiguity | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | derive unique `rho_E` | leaves `rho_E` free |
| Schur weights `w_E=1/3`, `w_T=1/2` | supplies exact `9/4` value | exact runner support | `frontier_quark_route2_qe_covariance_schur_quadratic_no_go_2026_06_14.py` | yes | yes | coefficient theorem | value present, bridge absent |
| Registration/positivity tests | candidate readout selector | no-go support | `frontier_route2_readout_record_positivity_no_go.py` | yes | yes | new distinguishing input | leaves `rho_E` free or bounded |
| Factor rigidity | localizes ambiguity | exact support | `S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md` | yes | yes | select `P_R` | does not select `rho_E` |

## Forbidden Inputs

- Observed quark masses or fitted Yukawa entries.
- Nearest-rational selection from live endpoint data.
- Treating the structural value `9/4` as a coefficient law without a typed
  theorem.
- Treating this branch-local packet as an audit verdict.

## Open Import

The missing readout-only theorem is:

```text
inverse_square_value_9_4 -> readout_coefficient_law_p2 -> rho_E = 21/4.
```
