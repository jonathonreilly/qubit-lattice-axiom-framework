# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Exact restricted readout family | Defines `P_R` and endpoint algebra | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | derive unique endpoint triple | imported as open support |
| S3-time parent row | Direct consumer of endpoint triple | open gate | `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` | yes | yes | upstream endpoint theorem | parent remains open |
| Factor rigidity | Localizes ambiguity to spatial prefactor | exact support | `S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md` | yes | no | not a selector | support only |
| Route2/s3-time/rconn candidate bank | Finite target-near search surface | computed lattice input | runner sweep | yes | no | replace with derived selector if found | bounded residual map |
| T-side row selector | Needed for full triple | unsupported import | `QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md` | yes | yes | theorem selecting `P_R` row | open selector |
| E-center lift `q_E=15/8` | Direct equivalent of `rho_E=21/4` | unsupported import | `QUARK_ROUTE2_E_CENTER_LIFT_DERIVATION_ATTEMPT_BOUNDED_NOTE_2026-06-12.md` | yes | yes | E-center source/readout theorem | open selector |
| Signed `R_conn` center bridge | Equivalent color/support route | unsupported import | `QUARK_ROUTE2_RCONN_TYPED_BRIDGE_DERIVATION_BOUNDED_NOTE_2026-06-12.md` | yes | yes | typed source-domain theorem | open selector |
| Inverse-square coefficient law | Would promote `9/4` to readout law | unsupported import | `QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md` | yes | yes | nonlinear/readout-covariance theorem | open selector |
| Physical/admissible readout primitive | Would choose a unique `P_R` for S3 gate | unsupported import | `S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md` | yes | yes | unique gate-readout theorem or explicit convention | open selector |
