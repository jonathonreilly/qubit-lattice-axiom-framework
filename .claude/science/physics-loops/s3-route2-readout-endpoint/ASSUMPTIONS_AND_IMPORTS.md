# Assumptions And Imports

## Minimal Allowed Premises

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Six-arm `O_h` star decomposition | Supplies `A1 (+) E (+) T1` and weights `w_E=1/3`, `w_T=1/2` | zero-input structural / computed lattice input | runner recomputation plus Route-2 covariance notes | yes | yes | exact runner/log route | Recomputed in block17 runner |
| Granted T-side algebra | Converts `lambda=9/4` into `rho_E=21/4` | support-only comparison | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | theorem route for T-side remains external | Used only as the named endpoint compression |
| Target rationals | Comparison target for the open residual | observational comparator / named target only | exact readout map note | yes as target, not proof | yes | derive from structural theorem | Not used as a proof input |
| Unit-normalized projected-arm analysis | One reciprocal frame-bound factor | conditional primitive | block17 runner | yes | yes | derive source/readout theorem selecting this normalization | Conditional only |
| Two independent analysis legs | Squares the reciprocal factor to `9/4` | unsupported import on current surface | block17 boundary | yes | yes | derive leg-count/source-readout split theorem | Open blocker |

## Forbidden Inputs

- Observed quark masses, CKM/J target minimization, or PDG data.
- Nearest-rational selection from live endpoint values.
- Treating `rho_E=21/4` or `lambda=9/4` as adopted.
- Treating canonical Riesz reconstruction as a source of reciprocal factors
  after its inverse cancels the frame bound.
- Claiming the exact readout map selects a source/readout split when it only
  sees the product.

## Newly Isolated Dependency

The finite-frame route reaches the target only if the current surface gains a
new theorem selecting exactly two reciprocal unit-frame analysis legs:

```text
lambda_n = ((1/w_E)/(1/w_T))^n.
```

`n=2` gives `lambda=9/4`; `n=0` and `n=1` are exact falsifiers for endpoint
closure.
