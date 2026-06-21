# No-Go Ledger

- **Equivariance-only covariance route.**
  `Hom_Oh(E,T1)=0`; equivariance leaves independent channel scalars.

- **Scalar quadratic-invariant route.**
  `Sym^2(perm6)` has trivial multiplicity `3`; scalar quadratic ratios are
  free.

- **Pure channel-metric route.**
  Pending PR #4543: channel metrics on `E (+) T1` have free `c_E/c_T`.

- **Nonseparable quadratic map route.**
  Pending PR #4544: `Hom_Oh(Sym^2(E (+) T1), E (+) T1)` has dimension `3`;
  representation content does not select the endpoint coefficient.

- **Current block16 support boundary.**
  Not a no-go: exact consumer firewall localizing `rho_E` to E-center.
