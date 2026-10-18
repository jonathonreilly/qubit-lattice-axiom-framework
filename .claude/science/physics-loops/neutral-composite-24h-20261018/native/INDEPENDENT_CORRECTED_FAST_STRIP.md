# Corrected fast-arm strip: focused proof-gap check

Disposition: NOT YET PROVED by the supplied NN strip argument. No contradiction to the proposed directional estimate was found, but a new center/stable transfer estimate is required. This is a focused mathematical obstacle report, not a formal audit. No repository files were changed.

The operator under consideration has diagonal v_n=f(n+1)-5lambda/2, nearest hopping-2, next-nearest hopping-epsilon with epsilon=lambda/4, and f=lambda^3/16. Its ordinary self-adjoint lower-half-plane resolvent is evaluated at z=x-i eta, eta/f in a fixed positive compact interval. The proposed x=-6lambda+O(lambda^(7/3)) stays inside the propagating local band throughout an initial segment of length proportional to1/f. The diagonal shift therefore does not remove the interior ellipticity margin used in the NN argument.

## Why the old transfer proof cannot simply be reused

The scalar fourth-order homogeneous recurrence is

    epsilon u_(n+2)+2u_(n+1)+(z-v_n)u_n+2u_(n-1)+epsilon u_(n-2)=0.

At locally constant real v, its characteristic polynomial is

    epsilon r^4+2r^3+(x-v)r²+2r+epsilon=0.

For small lambda it has an elliptic pair near the NN roots and an additional reciprocal real pair of sizes approximately lambda/8 and8/lambda, with negative signs. Thus the full4×4 transfer product and its inverse cannot have the NN proof's uniform boundedness: one channel grows exponentially and another decays. Diagonalizing the full transfer and asserting all factors have norm1+O(f+eta) would be false.

Grouping two sites into a block does not immediately solve this. The interblock hopping is [[-epsilon,0],[-2,-epsilon]], with one singular value near2 and the other of order epsilon²/2. Bounds using its inverse lose powers oflambda. Likewise the global resolvent identity comparing NNN and NN operators has perturbation ratio lambda/eta of orderlambda^-2, so it gives no small correction in this strip. Neither route proves the needed uniform estimate.

## What remains valid and what is actually needed

For the2×2 boundary Green matrix g=P(z-H)^-1P*, self-adjointness gives

    Im(w* g w)=eta ||(z-H)^-1 P*w||² >=0,

with w=(-2,-lambda/4). The sign is positive in the lower half-plane. The needed result is a uniform upper bound on the boundary matrix and a positive lower bound specifically on this directional dissipative quadratic form. A uniform positive-definite lower bound on Im(g) is too strong: already at lambda=0 and band-center energy0, the two-site spectral-density matrix has rank one (the second-site sine wave vanishes). The nonvanishing w projection is the appropriate target.

A viable extension would separate the two-dimensional propagating center bundle from the one-dimensional stable and unstable bundles, uniformly in smalllambda. It must then prove all of the following:

1. Center evolution across M proportional to1/f retains two-sided bounds, using slow variation O(f) and eta=O(f), without constants diverging withlambda.
2. The forced half-line boundary equations for source P*w inject a center amplitude bounded below, uniformly inlambda; an evanescent boundary layer cannot absorb the entire source.
3. The admissible resolvent solution has no uncontrolled growing component on the initial segment. The global1/eta norm bound and self-adjoint tail can help exclude it, but this step must be carried through quantitatively.
4. Summed physical norm on that segment controls the injected center amplitude, giving the directional dissipative lower bound. Boundary matching must also bound both columns of g; positivity alone does not give a full matrix upper bound.

These statements are plausible given the fixed propagating-band margin and the strong evanescent separation, but they are additional lemmas, not consequences of the supplied2×2 transfer proof. I have not completed those lemmas here and therefore do not certify the uniform strip estimate for the corrected operator.

## Numerical and scope observations

The root's block continued fraction uses the correct two-site onsite indices f(2m)-5lambda/2 and f(2m+1)-5lambda/2, intra-block hopping-2, and the corresponding NNN/NN interblock matrix. Increasing the far cutoff is a useful numerical convergence control, but finitely many lambda values and stable cutoff comparisons do not establish a uniform lower bound or rule out narrow exceptional parameter sequences.

Even if the corrected strip estimate is proved, it would be a bound on this specified self-adjoint arm and prescribed eta/f strip. It would not establish existence of a resonance in that strip, identify the outgoing host sheet, or control additional omitted native operators. Those remain separate requirements.

## Follow-up: a preconditioning route that avoids lambda/eta

There is a more promising reduction than the naive4×4 transfer estimate. Write epsilon=lambda/4, T=S+S†, and remove the small boundary term temporarily:

    H0=-2T-epsilon T²+f(n+1)-2lambda,
    H=H0-epsilon |1><1|.

Fix the real part x of z and define the real diagonal operator

    A_n=[sqrt(1+epsilon*(f(n+1)-2lambda-x))-1]/epsilon,
    L=T-A,
    C=2+epsilon*(T+A).

For sufficiently smalllambda in the stated x range, C is uniformly positive. Direct multiplication gives the EXACT identity

    H0-x=-(CL+LC)/2.

The apparently dangerous O(lambda) change has therefore been absorbed into a positive metric and an NN difference operator. Moreover

    [C,L]=-2epsilon[T,A].

Adjacent differences of A are O(f), uniformly on the whole half-line (they decrease at large n). Thus this commutator is O(epsilon*f), not O(epsilon). The second commutator [C,[C,L]] is O(epsilon²*f); the half-line endpoint contribution to [T,[T,A]] must be included, so it should not be silently estimated as O(f²) everywhere.

Formally,

    H0-x=-sqrt(C) L sqrt(C) - (1/2)[sqrt(C),[sqrt(C),L]].

A suitable bounded double-commutator estimate would make the last term O(epsilon²*f), small compared with eta~f. Unlike the naive resolvent perturbation, its ratio toeta is then O(epsilon²). This is the useful structural gain.

For D=2+epsilon A, one also has C=D+epsilon T and

    ||D^(1/2)(C^-1-D^-1)D^(1/2)||=O(epsilon).

Thus after congruence, the difference between imaginary metrics eta*C^-1 and eta*D^-1 is O(epsilon*eta) in the natural weighted norm. The diagonal-metric problem corresponds to a self-adjoint weighted NN Jacobi operator. On the controlled initial segment n<=const/f its weights, local band margin, and step variation are uniformly bounded, so an adaptation of the original NN strip proof is plausible. This route does not requirelambda<<eta.

### Exact remaining gap

I have not completed the operator-domain/double-commutator estimate for the unbounded C and L, nor the transfer-to-boundary-source estimate after the nonlocal sqrt(C) congruence. In particular, a global1/eta resolvent bound is insufficient to control the small nonlocal tail of the transformed boundary vector: a bare O(epsilon) source-norm error could again lose1/eta. One needs a localized/weighted endpoint Green estimate, or a graph-transform boundary matching argument, showing that this tail is harmless and that w still injects a uniformly nonzero propagating component. Only after that step can the small boundary perturbation -epsilon P1 be handled by a uniformly controlled finite-rank resolvent formula.

The exact preconditioning identities substantially narrow the obstacle: the bulk NNN perturbation can be organized at O(epsilon*f) or smaller relative scales, rather than O(epsilon). However, without the transformed-source/boundary estimate it is not yet a proof of the uniform2×2 bound or of Im(w*gw)>=c>0. The initial NOT YET PROVED disposition therefore remains in force.

## Final review of root completion: scoped PASS

Reviewed `/private/tmp/neutral_corrected_strip_root.md`, including its variable-Jacobi transfer and finite-tail truncation additions. These close the previously identified gaps for the specified corrected self-adjoint arm and prescribed eta/f strip. The earlier NOT YET PROVED disposition is superseded by this scoped PASS, with the harmless first-step correction below.

1. **Algebra and bounded remainder.** The identities H0-x=-(CL+LC)/2 and H0-x=-sqrt(C)Lsqrt(C)+R are correct. On finite sections, the two square-root commutator formulas give ||R||<=||[C,[C,L]]||/(8c). Adjacent differences of A are globally O(f), so both nested commutators are bounded uniformly in section length; the far finite-section endpoint contributes the same bounded type as the near endpoint. The bound is O(epsilon² f). Applying the integral formulas first in finite sections avoids assuming unbounded commutators are defined everywhere.

2. **Jacobi comparison and domains.** D A=2A+epsilon A²=v-x exactly, so J has diagonal -(v-x), linear in n, and positive offdiagonal sqrt(D_n D_(n+1)) growing at most as sqrt(n). Carleman's reciprocal sum diverges, giving the unique self-adjoint Jacobi closure. The original finite-range arm is likewise essentially self-adjoint with its confining diagonal and bounded hopping. C,D have a common positive lower bound, C-D=epsilon T is bounded, and the square-root difference is O(epsilon) in norm. Consequently U=sqrt(C)D^-1/2 and its inverse are bounded I+O(epsilon). Uniform finite-section bounds pass to the unique half-line resolvents; this supplies a domain-safe interpretation rather than a merely formal product of unbounded operators.

3. **Signs.** Congruencing z-H0 gives J-i eta M-E, with E=U^-1 R U^-* and M=U^-1 U^-*=sqrt(D)C^-1sqrt(D). Thus the lower physical resolvent corresponds to (J-i eta)^-1, which has POSITIVE imaginary part. The norm identity and subsequent positive dissipative bound use the correct sign. The boundary correction H=H0-epsilon P1 gives denominator1+epsilon*g11, as stated.

4. **Small perturbation after congruence.** M-I=O(epsilon), E=O(epsilon² f), and eta is bounded above/below by positive multiples of f. The comparison perturbation is therefore O(epsilon*eta), not O(epsilon). Its product with the global base resolvent is O(epsilon). For fixed-supported endpoint sources the NN bound gives resolvent-vector norms O(eta^-1/2). Sandwiching the resolvent identity then yields O(epsilon) LOCAL Green corrections. This step does not use a false globally O(1) resolvent bound.

5. **Weighted source tail.** Expanding (C+t)^-1 around diagonal D+t in C^-1/2 is justified uniformly because ||epsilon T(D+t)^-1||<=2epsilon/(c+t)<1. The kth term moves at most k sites. After multiplication by sqrt(D), its integral is bounded by a constant times epsilon^k integral[t^-1/2(c+t)^(-k-1/2)]dt, finite for k>=1. The tail beyond a fixed K sites is therefore O(epsilon^K), uniformly despite unbounded D. Truncation changes a Green quadratic form by O(epsilon^K/eta), which vanishes for fixed K>=8 and eta comparable tolambda³. The retained finite-supported vector differs from its original endpoint vector by O(epsilon); bounded fixed-endpoint Green matrices then control that difference locally. This correctly closes the previous nonlocal-source gap.

6. **Variable-Jacobi strip.** On the initial segment of length proportional to1/f the coefficients have a fixed ellipticity margin, and the moving real transfer bases vary O(f). Determinants telescope, so inverse products have the same type of uniform bound as forward products. The norm sum and exact imaginary-part identity give the positive endpoint bound. Fixed-endpoint Green entries follow from finitely many recurrence identities. There is one minor literal correction: if the artificial boundary coefficient is chosen a0=2, its difference from a1 is generally O(lambda²), not O(f). Choose a0=a1 instead, with ghost forcing -1/a0, or isolate this first uniformly bounded transfer step. Either choice restores the written estimates and leaves all conclusions unchanged.

Finally, the transformed coupling vector tends to -2delta1. Its positive imaginary quadratic form therefore survives the O(epsilon)+o(1) local corrections. The small rank-one boundary term is harmless because1+epsilon*g11 remains bounded away from zero. This proves a uniformly bounded boundary2×2 Green matrix and a uniformly positive Im(w*gw) for w=(-2,-epsilon), on the stated strip. It does NOT prove a positive-definite lower bound for the full2×2 imaginary part.

The conclusion remains strictly the corrected-arm lemma. It proves neither a native pole nor that a pole lies in this strip, and gives no real-axis pointwise limit. The outgoing host continuation, omitted native operators, and full resonance/source assertions remain separate obligations.
