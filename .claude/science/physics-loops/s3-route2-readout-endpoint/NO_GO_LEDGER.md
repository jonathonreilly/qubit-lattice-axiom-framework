# No-Go Ledger

- **Equivariance-only covariance route.**
  `Hom_Oh(E,T1)=0`; `O_h` leaves independent channel scalars and does not
  force `lambda = kappa^2`.

- **Quadratic-invariant route.**
  `Sym^2(perm6)` has trivial multiplicity `3`, so the `E:T1` quadratic ratio
  is free. The missing rule is inverse-square projector weight scaling.

- **Current block14: pure channel-metric route.**
  Positive `O_h` channel metrics on `E (+) T1` are
  `c_E P_E + c_T P_T1`; `c_E/c_T` is free. Ambient gives `lambda=1`, one
  reciprocal gives `lambda=3/2`, and inverse-square gives `lambda=9/4` only
  because that ratio was supplied.

- **Pending prior PR context, not required by current-main branch.**
  Blocks 8-13 further narrow exact carrier firewall, reciprocal degree,
  finite-frame one-factor, source/readout split, rank-one carrier
  factorization, and source-side Gram/tensor-power routes.
