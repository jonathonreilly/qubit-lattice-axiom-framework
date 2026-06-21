# No-Go Ledger

- **Equivariance-only covariance route.**
  `Hom_Oh(E,T1)=0`; equivariance leaves independent channel scalars.

- **Scalar quadratic-invariant route.**
  `Sym^2(perm6)` has trivial multiplicity `3`; scalar quadratic ratios are
  free.

- **Pure channel-metric route.**
  PR #4543: channel metrics on `E (+) T1` have free `c_E/c_T`.

- **Nonseparable quadratic map route.**
  PR #4544: `Hom_Oh(Sym^2(E (+) T1), E (+) T1)` has dimension `3`;
  representation content does not select the endpoint coefficient.

- **Theta-to-slice consumer dependency.**
  PR #4545: unresolved `rho_E` enters only through the E-center source factor;
  this supports downstream triage but does not derive the endpoint.

- **Current block17 finite-frame/Riesz boundary.**
  Parseval and canonical Riesz reconstruction give no reciprocal lift, one
  unit-frame analysis leg gives only `3/2`, and two legs reproduce the target
  only as an extra source/readout theorem not currently derived.
