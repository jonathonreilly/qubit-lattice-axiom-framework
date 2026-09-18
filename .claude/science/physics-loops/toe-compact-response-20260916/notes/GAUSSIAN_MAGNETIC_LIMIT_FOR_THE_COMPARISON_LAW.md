# Gaussian magnetic subsequences for the real comparison law

Working personal theorem proposal, 2026-09-16. This note concerns exactly
the noncompact comparison action in [the convex extension note](CONVEX_EXTENSION_OF_LIFTED_KERNEL.md).
It does not transfer that conclusion to the compact Hamiltonian. The
comparison's coincidence on a small-curl region does not imply equality
of normalized laws in a growing volume. All new statements await
independent review.

## 1. The finite periodic comparison measure

Use a periodic spatial cubic lattice of even side L>=4, a periodic chain of
M>=3 time slices of spacing T, and real normalized spatial links a_n.
The temporal difference is (a_(n+1)-a_n)/T, and C is spatial curl. Let
b_n=Ca_n and use the weighted inner product

    <u,v>_T=T sum_(n,p) u_n,p v_n,p.

The real action is S_alpha from the convex extension note. Quotient its
common temporal-constant/curl nullspace before integrating a. This is
an ordinary finite-dimensional Lebesgue integral on the orthogonal
complement, not a compact gauge integral. The interaction beyond S0
is a function of b alone, and it has a smooth extension to all ambient
plaquette coordinates:

    U(b)=sum_n g^(-2) {F_alpha(g J_n b)-Q(g J_n b)/2},
    J_n b(s)=(1-s/T)b_n+(s/T)b_(n+1).                      (1)

The constant value at b=0 may be subtracted without changing the law.
Let J combine all these interpolations. Jensen's inequality and the
positive adjoint averaging give

    ||J||_(p->p)<=1, ||J*||_(p->p)<=1, 1<=p<=infinity.     (2)

The node norm has weight T and the slab norm uses ds. For example,
J* averages the two neighboring slab functions with the affine shape
weights divided byT. Its row mass is1 on the periodic chain; its dual
column mass is1 because the two shape weights sum to1.

The positive majorant in section6 of [the bridge note](BRIDGE_CUBIC_SOURCE_BOUND.md)
therefore gives the actual ambient operator bounds

    ||U''(b)||_(p->p)<=delta_*=epsilon_alpha+delta2,
    |U'''(b)[h,k,l]|<=g m3 ||h||_(3,T)||k||_(3,T)||l||_(3,T),
    m3=sin(3alpha/2)+delta3.                               (3)

They hold for every real b, with no curl constraint needed in their
proof. In particular p=2,3,3/2 are available. This operator statement
is stronger than a bound on the Hessian quadratic form.

## 2. The exact magnetic Gaussian covariance

For the quadratic action S0, put omega_n=sqrt(T)b_n. Its covariance K
in ordinary counting coordinates is, at spatial momentum k and temporal
momentum theta,

    K(k,theta)=C(k)C(k)* / [lambda_t+b(theta)lambda_s],
    lambda_t=4 sin^2(theta/2)/T^2,
    lambda_s=sum_(i=1)^3 4 sin^2(k_i/2),
    b(theta)=(2+cos theta)/3=1-T^2 lambda_t/6.              (4)

The expression is zero when lambda_s=0, and positive on its image when
lambda_s>0. This follows by inverting the link quadratic form
lambda_t I+b(theta)C*C: on transverse links C*C=lambda_s I, while C
annihilates longitudinal links. At theta=0 its longitudinal kernel is
part of the quotient specified above. Thus no zero-mode inverse has
been inserted implicitly.

Let P_s=C C*/lambda_s on nonzero spatial modes and zero on zero modes.
It is the spatial curl projection. With

    q0=lambda_s/(lambda_t+lambda_s),
    A=(T^2/6) lambda_s lambda_t/(lambda_t+lambda_s),

all zero modes set to zero, equation(4) factors as

    K=P_s q0 (I-A)^(-1).                                  (5)

For T<1/sqrt(2), lambda_s<=12 implies
lambda_t+b(theta)lambda_s>=lambda_s, so ||K||_(2->2)<=1.
The covariance has no claim to be the compact measure's covariance.

## 3. Uniform l3 bounds, including anisotropic time spacing

We need a volume-uniform bound on K in l3 and l^(3/2), not just its
Fourier eigenvalues. The standard spatial cubic Riesz estimate gives

    ||P_s||_(p->p)<=kP_p<infinity, p=3,3/2,                (6)

uniformly in the spatial period. Self-adjointness makes the two constants
equal; write kP for a common upper bound. One proof is the periodic
Riesz argument in the main-revision source named in section7: the
multipliers delta_i delta_j*/lambda_s have uniform order-zero annular
derivative estimates; their kernels obey the discrete Calderon-Zygmund
size and difference bounds in dimension3. The l2 multiplier bound,
weak(1,1) decomposition, interpolation and duality give finite l3 and
l^(3/2) constants. Mass regularization and periodization preserve them.
The matrix P_s has only three components and a fixed finite number of
such entries, so its bound is independent of L. This is a mathematical
operator estimate, without a probabilistic phase input.

To handle arbitrary T without allowing an unknown constant to grow as
T decreases, use the dimension-independent diagonal discrete Riesz
bound of Domelevo and Petermichl, Theorem1. For product cyclic groups,
any sum of coordinate Laplacians divided by their total Laplacian has
l^p norm at most p*-1, where p*=max(p,p/(p-1)). The zero mode is assigned
zero. The theorem includes mixed cyclic factors (their section2).

Here is an explicit reduction of weighted rates to that theorem. If
T^(-2)=m/n is rational, take m copies of the temporal cyclic group and
n copies of each spatial cyclic group. Map their product to the original
four-dimensional torus by summing coordinates within each group of
copies. Pullback by this surjective homomorphism is an isometry for
normalized counting measure. The unweighted Laplacian of the larger
product, restricted to pullbacks, becomes

    m Delta_time+n sum_i Delta_i.

The sum over all spatial copies becomes n sum_i Delta_i. Applying the
published dimension-independent bound and restricting back gives

    ||q0||_(p->p)<=p*-1,
    ||lambda_t/(lambda_t+lambda_s)||_(p->p)<=p*-1.         (7)

Both are rational symbols of the finite Laplacian and intertwine under
pullback, including the constant mode. Approximate any positive T^(-2)
by rationals; on each fixed finite torus the matrices converge in every
operator norm. The same constant survives. This proves(7) for everyT>0
without treating anisotropy as an unverified extension of the paper.

At p=3 or3/2, p*-1=2. Also ||lambda_s||_(p->p)<=12, by its absolute
row sum. Hence ||A||_(p->p)<=4T^2. For0<T<1/2, (5) and its Neumann
series give

    ||K||_(3->3), ||K||_(3/2->3/2)
                         <=k3(T):=2kP/(1-4T^2).           (8)

This upper bound stays finite as T tends to0. It resolves the possible
mismatch between a small short-time interaction and an uncontrolled
anisotropic covariance norm.

## 4. A nonempty fixed-parameter regime

Choose fixed T,alpha,g satisfying

    0<T<1/2, 0<alpha<pi/3, g>0,
    delta_*<1, k3(T) delta_*<1.                           (9)

These conditions are nonempty. First make T sufficiently small: k3(T)
remains bounded while the T-dependent part ofdelta2 tends to0. Then
make alpha small, and finally take g sufficiently small but positive.
All three parameters are thereafter held fixed as L,M grow. This is an
existence statement for sufficient constants, not a numerically computed
critical coupling and not a parameter selected by framework axioms.

Write R(omega)=-U(omega/sqrt(T)). In counting coordinates its derivative
bounds are

    ||R''||_(p->p)<=delta_*, p=2,3,3/2,
    |R'''[u,v,w]|<=[g m3/sqrt(T)] ||u||_3||v||_3||w||_3. (10)

The factor1/sqrt(T) comes from converting the weighted cubic norm to
counting coordinates; it must not be dropped. The magnetic marginal is
exactly the Gaussian measure with covarianceK on Gamma=range(K), tilted
by exp(R). It is proper by(9). The evenness of the bridge action and
v_alpha makes this law centered.

## 5. Cubic log-MGF bound and Gaussian subsequences

For completeness, the finite Gaussian-perturbation lemma used here can
be proved by the preconditioned auxiliary diffusion

    d omega_tau=[-omega_tau+K grad R(omega_tau)+K h]d tau
                                                     +sqrt(2K)dB_tau.

It stays in Gamma and has the tilted Gaussian invariant law. At a finite
auxiliary horizon, source variations v_a and w_ab satisfy the integral
equations with kernels exp[-(tau-s)]K R'' and forcing K a, respectively
K R'''[v_a,v_b]. The contraction k3 delta_*<1 gives, pathwise,

    ||v_a||_3<=C3||a||_3,
    ||w_ab||_(3/2)<=[g m3/sqrt(T)] C3^3 ||a||_3||b||_3,
    C3=k3(T)/(1-k3(T)delta_*).                             (11)

The p=2 contraction gives convergence of the mean to the stationary
mean. Integrate the finite-horizon second derivative of that mean over
a source rectangle before taking the horizon to infinity. The resulting
finite-difference bound passes to the stationary mean, which is smooth
by the Gaussian tails. Dividing by the rectangle area gives the third
log-partition derivative bound. This avoids assuming that stochastic
stationary derivatives converge uniformly in dimension.

For the actual magnetic linear statistic X_h=<h,b>_T and its log-MGF
L_h(t)=log E exp(t X_h), equation(10) and the sourceh_count=sqrt(T)h
therefore give

    |L_h(t)-t^2 Var(X_h)/2|
                    <=g m3 C3^3 |t|^3 ||h||_(3,T)^3/6.  (12)

The factors ofsqrt(T) cancel as displayed. This is uniform in both
spatial volume and the number of time slices, at fixed T,alpha,g.

If a family of real tests h_V^1,...,h_V^r has bounded l2_T norms and
l3_T norms tending to0, its covariance matrices are bounded by the
convex covariance estimate. Every covariance-convergent subsequence
therefore has a joint centered Gaussian limit, by applying(12) to all
fixed linear combinations of the tests. This proves Gaussian
subsequences, not uniqueness or a particular effective covariance.
For ordinary four-dimensional smooth test scaling, the l3_T cube is
of order the square of the macroscopic lattice spacing; the exact
finite-test criterion just stated is the theorem used here.

There is also a useful lower covariance bound. On Gamma the action
Hessian is at most K_Gamma^(-1)+delta_* I. Integration by parts gives
E[(omega-E omega)(grad S)^T]=I and
E[(grad S)(grad S)^T]=E Hess S. Matrix Cauchy-Schwarz therefore yields

    Cov(omega)>=(E Hess S)^(-1)
                >=(K_Gamma^(-1)+delta_* I)^(-1).

The matching Brascamp-Lieb upper bound gives, in ambient coordinates,

    K/(1+delta_*) <= Cov(omega) <= K/(1-delta_*).          (13)

Here ||K||2<=1 was used, and both bounds vanish on Gamma-perp. Thus a
test with a positive limiting quadratic variance cannot collapse to a
point mass merely because the nonlinear comparison is taken to a large
volume. Covariance identification and homogenization remain separate.

## 6. What has and has not been connected

The chain of proposals now has a precise positive conclusion: the actual
lifted bridge supplies a smooth real comparison interaction, and that
comparison has Gaussian magnetic subsequences for diffuse tests at fixed
positive g in a nonempty sufficient parameter regime.

There is still no normalized comparison from the compact Hamiltonian to
this real measure. A field-dependent integer lift, sparse defects and
pointwise agreement on good fields do not supply it. A fixed positive
density of repaired regions may renormalize the covariance. Nor has this
note proved the physical electric source map, a unique Maxwell covariance,
reflection positivity of the modified comparison law, a reconstructed
photon Hilbert space, matter interactions, or selection of the supplied
Hamiltonian by the framework axioms. Those conclusions are not renamed
as consequences of(12).

The useful next target is an exact compact winding/region representation
with normalized weights and source derivatives. Such a representation
could make(12) relevant to the original model; its existence with the
necessary bounds is not assumed here.

## 7. Sources and proof status

- Main source at e0ef7cf4633034a8c1e6d57f5812cc4275bf1349:
  PRECONDITIONED_EXTENDED_GRADIENT_GAUSSIAN_REMAINDER_AND_FREE_CUBIC_RIESZ_BOUNDED_THEOREM_NOTE_2026-09-15.md.
  The entire source was personally reread. Its finite source-variation
  argument and periodic Riesz proof are the mathematical starting points,
  restated with the actual carrier and weights here. It remains an author
  proposal; no independent-review status is imported.
- Domelevo and Petermichl, [Sharp Lp estimates for discrete second order
  Riesz transforms](https://arxiv.org/abs/1507.03796), v1, Theorem1 and
  section2. All22 extracted PDF pages were personally read. The exact
  PDF SHA256 is3650832913fcfdc398be6d1ec32d7213a6d3122526ea9332bcc4d2400151162e.
  Its theorem concerns diagonal combinations. Off-diagonal discrete
  transforms are NOT silently included; only the two diagonal multipliers
  in(7) use this theorem. Their weighted extension is derived by replication.
- The later paper1701.04106v1 was read only at PDF pages1-8. Its stated
  discrete block is also diagonal. It supplies no additional theorem used
  here and does not license an off-diagonal sharp constant.

Completed finite checks compare the covariance with an independent matrix
inverse, verify replicated-coordinate intertwining and time weighting,
and challenge the positive bridge majorant with signed static response
equations. They cannot prove the infinite-volume statement.

## Author evidence and status

See [personal review](../review/PERSONAL_REVIEW.md), [claim status](../CLAIM_STATUS_CERTIFICATE.md), and [negative-claim discipline](../NO_GO_DISCIPLINE_CHECKLIST.md). Finite checks are challenges to the proof, not independent review or an execution of an infinite-volume theorem.
