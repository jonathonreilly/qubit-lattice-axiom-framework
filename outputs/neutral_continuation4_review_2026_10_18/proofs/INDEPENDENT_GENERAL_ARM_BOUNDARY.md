<!-- Owning original: PR9750; source SHA256 0ab3394a450e492a8388362f84ce90ee552ac03da0a3e07a01ba8ec276e67d65. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# General near-nearest arm: boundary steps4–5

Disposition: PASS for steps4–5 of neutral_general_band_strip_root.md, conditional on the separately established algebra, bounded remainder, and domain claims in steps1–3. This closes the growing-segment/source-tail argument; it does not independently certify every earlier reduction step or any full native pole.

## Uniform kernel throughout the initial segment

Use R0=(L-i kappa)^-1 with kappa=eta/2>0 and L=T-A. Its diagonal imaginary part is positive. On the first M=floor(c/f) sites, choose c small enough to retain a fixed ellipticity margin. The potential increments are O(f), and kappa/f stays in a positive compact interval. The usual moving-basis transfer estimate bounds every forward and inverse prefix product by a constant independent of M, f and volume.

The original endpoint forcing argument therefore gives |u1|<=C and Im(u1)>=c>0 for u=R0 delta1. The homogeneous recurrence away from the source, with ghost value u0=-1, bounds every u_j for j<=M. Define the left regular solution p0=0,p1=1, propagated by the same homogeneous recurrence. It too is uniformly bounded throughout the segment. At the first site,

    u2=(A1+i kappa)u1+1,   p2=A1+i kappa,

so the Wronskian p1*u2-p2*u1 is exactly1. The Green kernel is consequently

    R0(i,j)=p_min(i,j) u_max(i,j).

There is no complex conjugation in this complex-symmetric Jacobi kernel formula. It proves the claimed uniform bound for ALL i,j<=M, not merely for each fixed pair with a constant that might grow with the indices. This step is valid regardless of the detailed self-adjoint tail. Finite sections must contain the entire controlled segment.

For any source v supported in that segment,

    ||R0 v||²=Im<v,R0 v>/kappa <= C ||v||_1²/eta.

The same norm estimate holds for R0* v. Thus a perturbation Q of norm O(lambda*eta), with ||Q R0||<1/2, changes local matrix elements by O(lambda)||v||_1||w||_1 via the resolvent identity. The constant is independent of the growing segment size. This is the required replacement for the inadequate global1/eta estimate.

## Weighted Schur bound

Let ||K||_p be the maximum of the weighted row and column sums with weight (1+|i-j|)^p. This is a Banach-algebra norm because that weight is submultiplicative under matrix multiplication. The diagonal unitary exp(isA) has norm1 in this algebra, even though A is unbounded.

For exp(itT), repeated commutators with the position operator have uniformly bounded finite-range coefficients. Equivalently, the weighted l2 moment of its jth column of order k is bounded by C_k(1+|t|)^k, uniformly in j and finite-section size. Cauchy–Schwarz with a summable inverse-square weight gives a weighted l1 column bound of order C_p(1+|t|)^(p+1); the row estimate follows by taking the adjoint. Thus no exponential-in-|t| estimate is needed.

In the Fourier-Duhamel expression for B, the time integral adds at most one further polynomial factor. The compact smooth cutoff g_lambda has every Fourier moment bounded by C_p lambda. Therefore ||B||_p<=C_p lambda for any fixed p. The same holds for its Hermitian part. The analytic power series for C^-1/2=(2I-B_s)^-1/2 converges in this weighted Schur algebra when lambda is sufficiently small depending on p. It follows that

    ||C^-1/2-(1/sqrt2)I||_p <= C_p lambda.

For a fixed endpoint j, the transformed source therefore has l1 tail outside the first M sites bounded by C_p lambda M^-p (adjusting a fixed factor for j). Its finite part has bounded l1 norm and differs from delta_j/sqrt2 by O(lambda) in l1. The normalization is delta_j/sqrt2, not delta_j.

## Tail and perturbation combination

The global perturbed resolvent remains O(1/eta) by the Neumann estimate from step3. Replacing a transformed source by its first-M truncation changes a boundary quadratic form by at most

    C_p lambda M^-p/eta <= C_p lambda f^(p-1).

For any fixed p>1 this tends to zero as f tends to zero; for f bounded above by a small fixed constant it is also O(lambda). No assumption lambda<<eta is used. The finite parts are controlled by the all-indices Green-kernel bound above, and their l1 source differences contribute O(lambda). The O(lambda*eta) comparison perturbation contributes another O(lambda) locally.

Hence the physical endpoint matrix is uniformly bounded, and its first diagonal imaginary part is one half of the positive base value plus O(lambda)+O(lambda f^(p-1)). It retains a uniform positive lower bound for sufficiently smalllambda and f in the prescribed strip. A fixed-supported vector approaching a nonzero multiple of delta1 inherits the corresponding directional lower bound. No positive-definite lower bound for every endpoint vector is implied.

Finally a Hermitian perturbation F_lambda with fixed endpoint support and norm O(lambda) is handled by the finite-dimensional resolvent identity. The bounded endpoint matrix makes its denominator matrix uniformly invertible for smalllambda; it changes the local Green matrix by O(lambda). This preserves the stated positive directional bound.

## Qualifications

Polynomial degree, endpoint support, and the chosen weighted moment order are fixed before taking limits. Constants can depend on those choices and the ellipticity/strip margins. The result concerns the ordinary self-adjoint arm resolvent in the specified nonreal strip. It neither provides a real-axis pointwise limit nor locates a resonance in that strip. The outgoing host continuation and omitted native interactions remain separate obligations. No repository edits or formal audit were performed.
