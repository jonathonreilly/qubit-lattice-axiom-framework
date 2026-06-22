# Assumptions And Imports

## Allowed

- Exact restricted Route-2 carrier columns from
  `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`.
- Exact slice/time obstruction context from
  `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md` and
  `S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md`.
- Conditional T-side stretch values:
  `beta_T/alpha_T = -1`, `alpha_T/alpha_E = -2`.
- Exact rational arithmetic over the fixed source vectors
  `S=(1,-2)` and `C(q_E)=(q_E,-5/3)`.

## Forbidden

- Observed quark masses.
- Fitted Yukawa values.
- CKM or `J` target minimization.
- Nearest-rational selection from the live E endpoint.
- Treating `c_TE=-8/9`, `q_E=15/8`, `rho_E=21/4`, or metric ratio
  `1449/704` as supplied proof inputs.
- Audit verdicts or repo-wide status movement.

## Newly Exposed Imports

- A positive route must derive a typed E-center source/readout primitive,
  such as `c_TE=-8/9`, or derive an equivalent selector metric/source rule.
