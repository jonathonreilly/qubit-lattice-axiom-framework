# A bounded-rate alternative and the response it still needs

Personal derivation, 2026-09-15. Keep the same actual filtered clock measure
and the same exact-fiber diffusion as in BLOCK1_POSITIVE_HYBRID_GENERATOR.md.
Only the auxiliary proof dynamics changes. No physical law is changed.

For an oriented move v, put Delta S_v=v.Az+v.Av/2 and define

 b_v(z)=1/(1+exp(Delta S_v))=c_v(z)^2/(1+c_v(z)^2).

Then b_-v(z+v)=1-b_v(z), and

 exp[-S(z)]b_v(z)=exp[-S(z+v)]b_-v(z+v).

Thus L_b=L_c+sum_v b_v Delta_v is another reversible generator for the
same measure. In finite volume, its jump rate is bounded by the number
of oriented moves, so standard Poisson thinning and the Lipschitz fiber
SDE give a conservative construction directly.

The elementary inequality c/(1+c^2)<=1/2 implies b_v<=c_v/2. Therefore

 E b_v^p <= E b_v <= (1/2)exp[-q_v/8], p>=1.          (1)

The second-moment anomaly of the square-root rates is absent. If a=A v,
then the first three derivatives are

 D b_v[t]=-b_v(1-b_v)(a.t),
 D^2 b_v[t,u]=b_v(1-b_v)(1-2b_v)(a.t)(a.u),
 D^3 b_v[t,u,w]=-b_v(1-b_v)(1-6b_v+6b_v^2)
                         (a.t)(a.u)(a.w).

The absolute scalar coefficient in each line is at most b_v. Thus these
derivatives, when measured along specified directions, inherit (1) after
multiplication by the displayed deterministic factors. Their pointwise
suprema need not be small in beta: Delta S_v=0 is allowed.

For exp(i t.z), the expected absolute cubic remainder in the jump
generator is at most

 (h^3/6)exp[-pi^2 beta(1+4tau)/2] ||t||_3^3.          (2)

This again vanishes for four-dimensional diffuse tests, but is only a
generator Taylor remainder. The drift correlations and the fluctuation of
the quadratic intensity still need a volume-uniform response argument.

The two Dirichlet forms obey E_b(f,f)<=E_c(f,f)/2 for their jump parts.
There is no positive uniform reverse comparison: b_v/c_v tends to zero
both at very small and at very large c_v. Therefore a future gap proof
for the original rates would not automatically transfer by this comparison.

The mean jump drift has derivative

 D[sum_v v b_v(z)] = -sum_v b_v(1-b_v) v v^T A.

Its quadratic form is nonpositive in the A metric. This fact controls the
mean drift, not sample-path separation: unmatched jumps in a coupling also
contribute to the distance. No pathwise contraction, source differentiability
of jump paths, or stationary Gaussianity follows from this sign alone.

This is a concrete alternative that removes one identified obstacle. The
remaining weighted response problem is substantial; repeatedly introducing
rates without proving such an estimate would not advance the field target.
