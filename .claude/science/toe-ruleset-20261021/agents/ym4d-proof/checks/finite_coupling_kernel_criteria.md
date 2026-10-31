# Prospective numerical criteria: finite-coupling SU(N) kernel

Written before the checker. These finite controls can falsify conventions and
normalizations; they cannot prove the uniform analytic theorem.

1. SU(2), independent complex matrix pair: direct full S3 Haar quadrature of
   the original phase and of its complex-saddle-translated phase agree with
   the repaired quaternion/Bessel formula to relative 2e-8, at t=3,12,40.
   The saddle determinant is one and the traceless stationary residual is
   below 2e-12. Include a nonunitary saddle and noncommuting pair.
2. SU(2) identity: for t=40,80,160 the determinant-extracted remainder obeys
   |t E_t+3/8|<0.03. The exact mean obeys
   |t^2[(1-c_2(t))-3/(2t)]+3/8|<0.05.
3. SU(3): normalized two-angle Weyl Haar quadrature integrates 1 to 1
   within 2e-12. The 256 and 384 point-per-angle grids agree relatively to
   2e-8 at t=40,80,160, for S=I and for an independent scalar complex pair
   S=sI,E-F=2lambda I. At S=I, |t E_t+1|<0.12. The Gaussian prefactor is
   27 sqrt(3)/pi in the original exponent t Re tr(U)/3 convention.
4. SU(3), a constructed noncommuting doubled matrix pair in the proved
   parameter domain: the iterative SL saddle matches its constructed value
   within 2e-12, and the full eight-colour Hessian matches a centered
   second-difference Hessian within 3e-6. A separate wider-parameter algebra
   probe must exhibit the nonzero scalar/tr(X^3) odd term and its exact
   cancellation between X and -X to 2e-12; it is not a domain certificate.
5. Actual L=3, d=4 paired S4-prime mean: exactly 1944 contours, maximum
   length <=11; the arbitrary-holonomy brick lift gives each contour G to
   2e-12. Complex noncommuting link displacements inside the declared radius
   put both independent means in the proved matrix domain. A separate
   wider algebra probe must distinguish average(path^-1) from mean(path)^-1
   and from mean(path)^* by >1e-6.

Intentional mutations must be detected: wrong dual-quaternion sign (>1e-5
relative normalizer change); discarded SU(3) Haar/Vandermonde factor (>0.1
relative prefactor-normalized error); wrong Gaussian determinant power
(>0.05 relative error for a scalar S=1.1 diagnostic); U(N) polar substitution
for a genuinely SU(3) scalar-phase saddle (determinant defect >1e-3 on the
wider algebra probe); wrong S4 divisor 6 L^4 (>0.5 matrix error).

No criterion will be loosened after execution. Any failure remains in the
record; a later diagnostic must be labelled post hoc. Use the coordinator's
live lock, free memory >=50%, load < half the logical cores, nice 15, one
thread, 90-second wall/CPU and 300 MiB RSS watchdog limits. No lock writes.
