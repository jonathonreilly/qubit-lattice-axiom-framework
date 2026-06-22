# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Route-2 endpoint algebra | Converts row ratio into `q_E`, `rho_E`, and `c_TE` | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already exact algebra; physical selector still open | used |
| S3 readout-to-slice blocker | Downstream consumer and target residual | open gate | `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md` | yes | yes | derive endpoint triple upstream | used |
| O_h weights `w_E=1/3`, `w_T=1/2` | Positive weight coordinates for E/T row ratio | exact support input | prior O_h seven-site support notes cited by parent stack | yes | yes | keep as parent input | used |
| T-side stretch inputs `q_T=5/6`, `s_TE=-2` | Converts E/T row ratio into endpoint consequences | conditional stretch input | parent Route-2 endpoint algebra | yes | yes | prove T-side entries or keep scoped | open |
| Regular positive-ray cocycle | Selects `A(w)=K log w` | exact support/open | Block110 and source-measure/log-readout notes | yes | yes | prove physical Route-2 source action has this semantics | open |
| Finite-jet derivative order | Determines row degree `d=-k` | unsupported import if used physically | Block111 finite-jet analysis | yes | yes | prove physical response principle selects `k=2` | open |
| Affine Hessian-gauge equivalence | Prunes value and first-derivative readouts | conditional support premise | Block111 finite-jet lemma | yes | yes | derive action gauge freedom from Route-2 source/readout semantics | open |
| Constant source-unit/no-scale coefficient | Prevents `g(w) Phi''(w)` prefactors from shifting degree | unsupported import | Block111 prefactor boundary and counterterm parents | yes | yes | no-scale, dilation, quotient, or variational theorem | open |
| Observed endpoint/mass values | Forbidden comparator | observational comparator | none used | no | no | excluded | not used |

## Import Movement

Block111 retires the overread:

```text
regular log-action cocycle alone selects Hessian source row.
```

It exposes the sharper remaining import:

```text
Route-2 source/readout must supply affine-gauge-invariant lowest-order local
curvature response in w, with a constant source unit / no-scale coefficient.
```
