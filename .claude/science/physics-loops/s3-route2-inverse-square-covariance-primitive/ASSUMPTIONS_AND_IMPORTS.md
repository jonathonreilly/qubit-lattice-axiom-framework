# Assumptions And Imports

## Allowed Current-Surface Inputs

- `O_h` six-arm channel dimensions:
  - `dim(E)=2`
  - `dim(T1)=3`
  - `N_arm=6`
- Per-arm projector weights:
  - `w_E=1/3`
  - `w_T=1/2`
  - `kappa=w_T/w_E=3/2`
- Granted T-side Route-2 endpoint value:
  - `q_T=5/6`
- Granted time-side coupling input used by the endpoint arithmetic:
  - `S_TE=-2`
- Prior same-domain firewall notes:
  - `QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md`
  - `QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md`
  - `ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md`
  - `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md`

## Forbidden Imports

- No observed quark masses, CKM/J values, or target endpoint fitting.
- No fitted selector for `rho_E`.
- No cross-domain color-ray/source-line identification.
- No assumption that equivariance alone supplies the `E:T1` reduced matrix
  element ratio.
- No adoption of the inverse-square primitive as a new axiom.

## Newly Isolated Missing Primitive

The exact candidate primitive is:

```text
q_X proportional to w_X^-2.
```

If supplied, it gives

```text
q_E/q_T = (w_T/w_E)^2 = (3/2)^2 = 9/4.
```

This block only characterizes that primitive and checks its endpoint
consequences. It does not derive the primitive from the current source/readout
surface.
