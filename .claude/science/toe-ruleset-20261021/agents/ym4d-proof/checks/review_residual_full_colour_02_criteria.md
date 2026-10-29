# Additional actual-lattice control criteria

Declared before script 02 and before its execution. Construct the complete
periodic four-dimensional L=3, T=2 lattice (1296 fine sites and 16 roots),
enumerate all 24*81 contours per coarse link, and use the actual SU(2)
commuting normalized density. No author implementation is imported.

- Check the exact-incidence covariance Qd=d_c ev and the nonlinear neutral
  center derivative Md=d_c ev at three small nonflat backgrounds, including
  both constant harmonic maps. Numerical residual tolerance is 2e-10.
- Construct the full periodic harmonic lift and scalar Schur complement,
  check Q_per and its omitted-root-mean control, and compare scalar
  pseudodeterminants by independent cofactor and Schur routes. Logarithmic
  determinant tolerance is 2e-8, operator tolerance 2e-9.
- Check completed Fbar_1 d, both fixed constant kernels, its cofactor
  determinant, and the retained ell^4 factor at these actual backgrounds.
  Omission of either the scalar Gram or root-mean completion must fail.
- Solve the actual one-step quadratic stationary problem by a sparse
  iterative solve; require a relative equation residual <=2e-10. Derive the
  quartic from its Wilson curvature and all actual contour moments. Compare
  against fourth-order coefficients extracted from the exact normalized
  SU(2) action, on both the linear stationary chain and a chain with an
  arbitrary cubic correction. Use epsilon=.15,.075,.0375 and two-level
  Richardson elimination of the sixth-order error; tolerance 2e-7*(1+|E4|).
  Record the unextrapolated values and all residuals.
- Check exact-action invariance when each neutral fine link is shifted by a
  constant one-form and each coarse link by three times that constant, at a
  nonzero residual. Check the actual harmonic graph norms 1+1/9 and 1+9;
  tolerance 2e-10.

These are finite floating-point falsifiers/support, not general proofs,
interval certificates, uniform estimates, or a nonlinear existence argument.
All attempts and outputs remain preserved.
