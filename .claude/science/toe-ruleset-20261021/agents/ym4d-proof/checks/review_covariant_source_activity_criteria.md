# SA affected-review numerical criteria

These statements and thresholds precede the new review code and inspection of
the author's scientific code. The frozen source, including its reported test
results, and the coordinator's summaries have already been read.

1. Exact set/word comparisons on T=2 and T=3 must show that every paired
   kernel reads only its two coarse endpoint blocks, and every fine Wilson
   plaquette reads a coarse set within graph distance 2 of either of its
   coordinate indices. Include wrapping anchors and all fine plaquettes.
   The selected crossing fibre must occur in exactly 72 of its 1,944 paired
   words and in no distinct endpoint kernel. Deleting a genuine remote
   coefficient read must change an actual SU(2) plaquette Hessian entry by
   more than 1e-10 on the diagnostic configuration.
2. A three-colour covariant matrix with noncommuting transports and distinct
   local colour coefficients must satisfy the actual patch identity
   (K+a)P=I-R and the resolvent reconstruction within 5e-12 in maximum-entry
   error. Check a=0,0.3,2,20, both absolute endpoint sums, and the marked
   support-incidence product estimate. Use the computed labelled norm at
   beta=4.5; it must give residual r<1/2. Verify the finite truncation's
   proved remainder bound with only 5e-12 rounding allowance. Wrong residual
   sign or noncommuting product order must cause error greater than 1e-10
   in a diagnostic case. The Stieltjes square root and full determinant
   must agree with independent spectral calculations to 2e-10.
3. An explicit overlapping-support matrix family must distinguish incoming
   column sums from outgoing row sums in the marked-product calculation.
   Exact sums must reject omission of the remote mark or its column factor.
   Support size must count every filled connector vertex, not just diameter
   or two endpoints; omitted original-data dependence must be detected.
4. In three scalar dimensions, a complex affine cube homotopy with
   noncommuting maps and a mixed polynomial density must obey the exact
   integrated divergence identity. Every oriented face is included. Missing
   a face, the determinant derivative, or the linear part of boundary
   velocity must give a nonzero exact algebraic discrepancy.
5. For the actual SU(2) crossing-link conditional fibre with alpha=0.43,
   b=0.07, u=17, kappa=1.1, p=1.15 and epsilon=0.014+0.009i, direct matrix
   plaquettes, direct normalized Haar tilt integration and the analytic
   density must agree. At >=55 decimal working precision require errors
   <=1e-25 for Haar/Bessel normalization, fixed-real-sector factorization,
   and integrated normalized contour flux versus the endpoint logarithm.
   Scalar critical residuals must be <=1e-30. Keep the full three-colour Haar
   Jacobian restricted to the fibre, its HS-to-a Jacobian, all source vacuum
   and canonical linear terms. Omitting normalizer, Haar or source terms
   must change their evaluated derivative/factor by more than 1e-10.
6. An actual coarse plaquette with positive curvature must violate the
   necessary good-event inequality under the displayed too-small thresholds.
   A moving hard plaquette threshold must exhibit unit uniform-norm change
   for arbitrarily small nonzero displacement. These diagnose excluded
   inferences; they do not price a complementary history or certify SA12.
7. All new numerical runs use niceness >=10, the five recorded thread
   variables equal to 1, RSS <2,000,000,000 bytes, all load averages <20,
   macOS free memory >=50%, no pools, and a 60-second per-program deadline.
   Resource refusal is neither a counterexample nor successful validation.
   Failed attempts are preserved; changed fixtures/probes are identified,
   and no threshold is silently relaxed.
