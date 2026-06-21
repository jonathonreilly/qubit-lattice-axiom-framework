# No-Go Ledger

| Route | Status | Source | Residual left |
|---|---|---|---|
| Exact current readout-map reduction alone fixes `rho_E` | no-go | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | `beta_E / alpha_E` remains free after T-side entries are granted |
| `O_h` equivariance forces E/T covariance | no-go | `QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md` | `Hom_Oh(E,T1)=0`; E/T scales remain independent |
| Quadratic invariant forces `lambda=kappa^2` | no-go | `QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md` | invariant quadratic has free E/T ratio |
| Bulk/box-size ratio stabilizes at `9/4` | no-go | `QUARK_ROUTE2_QE_BOX_SIZE_SCAN_CLOSES_BULK_LIMIT_HATCH_NARROW_THEOREM_NOTE_2026-06-10.md` and follow-on covariance note | ratio is not stable; `N=15` is not a derivation |
| Zero or one reciprocal projector-weight factor closes endpoint | no-go | block09 branch-local factor-degree packet | degree 0 gives `lambda=1`; degree 1 gives `lambda=3/2`; endpoint needs degree 2 |
| Direct `Theta_R -> Lambda_R` consumer is independent of `rho_E` | no-go / support boundary | block08 branch-local exact consumer firewall | E-center-sensitive uniqueness still depends on `rho_E` |

## Block10 Addition

Finite-frame dual normalization supplies a plausible exact origin for one
reciprocal factor. Two independent such legs close conditionally, but the
current Route-2 surface does not license them. This converts the open problem
from "find an inverse square" to "derive two independent local Riesz-dual
source/readout legs or an equivalent total-degree-2 primitive."
