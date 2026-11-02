# Prospective numerical criteria for the one-loop unit

Written before either new check program or its execution. Written proof is
not preregistered under PROCESS_LIGHT. These finite checks cannot establish
depth-uniformity, an infrared limiting theorem or physical existence.

Use the genuine d=4 SU(2) gauge-action family

`S_alpha=(1-8 alpha) S_W+alpha S_rect`, alpha=0 and 1/32,

where S_rect contains the twelve ordered 2-by-1 rectangular loops per site
(long direction mu, short direction nu, mu!=nu), each with normalized
`1-Re tr U_loop/2`. Construct loop paths and their linear Fourier rows
explicitly. At a constant Cartan background H=i sigma3 the charged quantum
root has q=2. Gauge covariance identifies its exact flat-background Bloch
Hessian with the zero-background symbol at shifted momentum. This gives an
actual charged Gaussian-block control, not a model of the whole stationary
chain. Its nonzero-alpha member independently tests the common-J
normalization used by the finite-part comparison.

Before looking at outputs require:

1. Actual loop incidence annihilates every Fourier gradient. Wilson plus
   gauge completion equals lambda I. Exact arithmetic is required for these
   identities and the point matrices below.
2. The normalized rectangle combination has quadratic marginal coefficient
   one. Its difference from Wilson starts at degree four. Verify this from
   the loop rows, not a hardcoded continuum coefficient. The intentional
   replacement `1-8alpha -> 1-4alpha` must change that marginal coefficient.
3. At K=(pi/2,pi/2,pi/2,pi/2), compute the epsilon-squared phase-averaged
   log determinant coefficient in two ways: derivatives of the explicit
   determinant, and tadpole minus the complete bubble. They must agree
   exactly. Include the real root pair and vector/half-ghost weights.
   Replacing the inside bubble coefficient 1/2 by 1/4, or retaining only
   one real root component, must disagree by more than 10^-6.
4. Direct finite-epsilon phase quadrature of that same log determinant,
   at epsilon=0.001 and 0.0005 with 64 uniform phases, must agree with the
   exact coefficient to within 5e-6. No precision or tolerance is to be
   changed after looking at results without labeling the change.
5. Independently build the periodic 3^4 incidence matrices and the neutral
   Wilson cosine-Hessian vertex for P=2pi/3. The gauge-completed inverse
   is zero on its four exact harmonic modes. Its two-form projector
   diagonal must be 40/81 within 1e-11. The neutral determinant coefficient
   divided by the actual phase-averaged Wilson wave density 3/4 must equal
   -20/81 within 1e-11. Deleting the neutral vertex, replacing its finite
   projector diagonal by 1/2, or omitting the Wilson wave divisor must
   fail this comparison by more than 10^-4.

Print exact matrices/coefficient values, quantitative errors and every
predicate, including intentional mutations. Keep complete outputs. A
failed check stays recorded, whether mathematical or an implementation
defect. Use one BLAS/OpenMP thread, bounded matrices and nice execution.
No old author or reviewer program is modified or rerun for these checks.
