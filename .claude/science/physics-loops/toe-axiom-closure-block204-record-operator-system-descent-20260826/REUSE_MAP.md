# Reuse Map

- Import Block 190 only for the exact exterior generators and carrier labels.
- Reconstruct Block 191/194 projectors and detector blocks from source; do not
  reuse cached `1/8` values as evidence.
- Import Block 192 action/OS identities, but independently form the two-sector
  marginal and leave its relative sector normalization symbolic.
- Import Block 203's exact per-copy periodic CAR functional and carrier type;
  do not extrapolate it to a full `C32` state without a declared functor.
- Use exact ranks, binomial coefficients, and generating functions instead of
  dense many-body matrices.
- Do not reuse failed event amplitudes, fitted normalizations, or gravity
  intermediates.
