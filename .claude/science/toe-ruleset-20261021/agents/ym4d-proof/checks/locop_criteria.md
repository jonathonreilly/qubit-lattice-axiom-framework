# LOCOP numerical criteria

Registered before writing or running the LOCOP check script, 2026-10-30.
These are finite algebraic regressions, not estimates for the interacting
RG map, its uniform coefficient bounds, or the continuum theory.

1. **Covariance.** Deterministic SU(2) contour products and their arithmetic
   mean transform by their endpoint matrices, and the soft-kernel numerator
   exponent is invariant, with maximum absolute error < 1e-12. A deliberate
   independent transformation of the coarse field with the fine field frozen
   must change the exponent by > 1e-4. This negative control tests the scope
   of joint covariance, not gauge breaking in the model.
2. **Localization.** Exact rational constant-curvature tests of a plaquette
   and rectangular loop reproduce their oriented areas squared, tensor
   extraction is idempotent, and the 384 signed permutations of four axes
   send a symmetric 6 by 6 matrix to (trace/6) times the identity after
   averaging. All rational residuals must be exactly zero. A trace-free
   anisotropic quadratic must survive scalar extraction and scale by one.
3. **Real Taylor benchmark.** For every two-variable monomial F^a Z^b of
   field degree <= 6 surviving removal of degrees zero, one and F^2,
   the ideal dilation L^4 G(L^-2 F,L^-3 Z) has full coordinate Taylor norm
   ratio <= 4/L+8/L^2, for L = 3, 5, 7. For b=0 and a>=3 the ratio is
   <= 8/L^2. Rational inequalities must hold exactly. The first bound is
   required to be < 1 only at L=7; L=3 and L=5 are not contraction claims.
4. **Coupling sign and bracket.** A finite synthetic recurrence with a
   bounded one-loop partial-sum defect and |rho_j|<=C/u_j must satisfy the
   derived two-sided bracket for every pair of its 41 levels (820 pairs),
   using exact rational arithmetic. The returned-term sign must agree with
   u'=u-b+beta(R), rho=-beta(R). This tests arithmetic only.
5. **Haar/relative-field diagnostic.** The SU(2) chart-Jacobian quadratic
   coefficient must converge to -1/3 in log[(sin z/z)^2]/z^2 at z=1e-3,
   with error < 1e-6. The soft exponent's quadratic coefficient at fixed
   fine identity must equal t/2 in FLOW's unit colour direction, with
   error < 1e-6 at z=1e-3 and t=2. These terms must not be labelled a
   gauge-breaking physical gluon mass.

Run serially under a numeric lock, nice >= 10, every BLAS/OpenMP thread
variable = 1, peak RSS < 1,000,000,000 bytes, all three load averages < 8,
and macOS memory_pressure free percentage >= 30. Check resources before
and after each group. Refuse the numerical run if any guard fails; do not
relax a guard. No pools and no RLIMIT_AS. Record every failure explicitly.
