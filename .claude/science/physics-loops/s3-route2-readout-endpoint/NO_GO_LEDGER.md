# No-Go Ledger

| Route | Status | Source | Residual left |
|---|---|---|---|
| Exact current readout-map reduction alone fixes `rho_E` | no-go | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | `beta_E / alpha_E` remains free after T-side entries are granted |
| `O_h` equivariance forces E/T covariance | no-go | `QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md` | E/T scales remain independent |
| Quadratic invariant forces `lambda=kappa^2` | no-go | `QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md` | invariant quadratic has free E/T ratio |
| Zero or one reciprocal projector-weight factor closes endpoint | no-go | branch-local block09 packet | endpoint needs total degree two |
| Two-factor mechanism closes on current surface | conditional only | branch-local block10 packet | current surface does not license two independent legs |
| Product-level endpoint/readout algebra certifies independent source/readout legs | no-go | branch-local block11 packet | source/readout factorization gauge remains unfixed |
| Current `K_R` carrier factorization supplies the two reciprocal factors | no-go | branch-local block12 packet | `K_R` factorization is rank-one, channel-blind, and degree zero |
| Source-side Gram/tensor powers of current `K_R` supply inverse-square covariance | no-go | block13 | channel-blind contractions give `lambda=1`; channel metric would be extra |

## Block13 Addition

The nonseparable `K_R` Gram route fails exactly:

```text
K_R^T M K_R = (a^T M a) b b^T.
```

Unit `E` and `T1` probes see the same scalar.
