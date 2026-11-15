# Frozen mathematical findings before author metadata

Target: POSITIVE_READER_COVARIANCE_ASTRA.md, complete lines 1–543,
SHA256 68bb7798bfcc0806c65531ab894e3e7f67ef1c155afd6da2f20f1b9dc2bb8da8.
Target hash was verified before the read and again before this freeze.
Preliminary independent reconstruction: review_positive_reader_covariance_preliminary.md,
SHA256 e2dab61993862c46d9ad4959db09a395299fa571c229dee4826dcda61f93b2aa.

No checks/positive_reader_covariance_* file has been opened. Target headers,
self-description, provenance summary and bibliography were necessarily exposed
in the complete source read; none supplies mathematical evidence. No predecessor
review or author numerical result is used as a premise. No numerical test was
necessary or run. This file freezes mathematics; it is not the final review
verdict or an audit certification.

## Conclusion at the mathematical freeze

No material mathematical defect was found in the stated covariance construction.
Under its actual CB local-analytic and real-gap inputs, the source establishes
its narrow finite-u, all-mode covariance result. The support rate is the tiny
explicit beta=(16R)^(-4), positive local components must be weakened as whole
matrices with real nonnegative coefficients, and the new precision constant
is a_C/U^2. The source explicitly excludes all-order interacting/tree/trace
summation and the full original-cut/continuum claims. This conclusion is
subject only to final source and metadata identity checks, not unseen author
checks supplying the proof.

## Independent checks against exact source ranges

1. **Actual matrix, lines 34–118.** PC1/PC2 is K=F_0''(0;V), with the actual
   normalized kernel, finite-u path-spread term and Haar Hessian. It is not the
   shifted Hessian. CB 153–267 provides the real curvature error, gap and local
   centered analytic vertices. Scalar absolute conversion b=DB is safe;
   compressions retain gamma I<=K_A<=B I. Range two in sup distance costs at
   most eight in l1. All n0=D(3L^4+1) degrees per coarse cell remain. PC4's
   finite Cauchy count dominates 15 q^2 third-derivative contributions; its
   coarse HS bound dominates each scalar displacement. CB's centered local
   estimate is uniform for u>=1. IC6's additional large-u amplitude hypotheses
   are not imported: this source repeats only the elementary derivative count.

2. **Principal inverse, lines 120–155.** Weighted conjugation changes K_A by
   at most b_c(exp(m r0)-1)=gamma/4 in BOTH absolute endpoint sums. The
   unweighted principal matrix has Hermitian part >=3gamma/4, hence the
   conjugate has Hermitian part >=gamma/2 and inverse norm <=2/gamma. Undoing
   the weight gives PC6. The periodic distance representatives inject into
   Z^4 (choose one sign at antipodes), so the coth sum with n0 is valid for
   all T and every principal patch. PC7 separately pays sum-of-entry-suprema
   with vK=n0 5^4; it does not interchange a supremum with an endpoint sum.

3. **Geometry, lines 157–204.** For T<16R the sole label is the entire torus
   and has <(16R)^4 cells. For T>=16R the integer interval construction works;
   psi has enough transition length to satisfy its stated derivative bound.
   Its plateau removes the distance nonsmoothness at interval endpoints;
   its zero region removes the circular cut locus. h>=1. Support lies inside
   N_(R+1)(Q); a range-two neighbor lies in A=N_(2R)(Q) for R>=4. The further
   four-cell collar includes radius-three coefficient readers and both ends
   of original coarse links. The loose side and overlap bounds s_R,J cover
   wrapping. Reverse triangle inequality proves the stated Lipschitz constant
   also when one cutoff value is zero. Nothing depends on data or parameters.

4. **Zero extension and positivity, lines 206–233.** With G_A extended by
   zero, chi_A K G_A chi_A=chi_A^2 because chi_A kills exterior rows. This
   proves KP=I+sum[K,chi_A]G_A chi_A, so R=I-KP has exactly the displayed minus
   sign and K^-1=P(I-R)^-1 has the displayed multiplication order. Every
   nonzero residual endpoint is in A by the collar just checked. For real V,
   G_A>=B^-1=2c0 gives D_A>=c0 chi_A^2. The permitted parameter acts on the
   entire positive matrix; independent entrywise weakening is correctly excluded.

5. **Absolute and marked bounds, lines 235–269.** Fix a residual row i and
   summation index k: only <=2J cutoffs can have nonzero difference. Sum final
   j through the inverse envelope g, then k through b_abs, obtaining r.
   For a residual column j, only <=J cutoffs have chi_A(j)!=0; sum i first in
   K's column and then k in G_A's column. This is <=r/2 with the same weight.
   For marked incidence use the per-patch row bound times <=n_R rows and <=J
   patches. It is <=n_R r, not an unbounded-volume sum. The analogous bounds
   for P,D are exactly the displayed p,d_core. Thus PC15 bounds the atom
   family itself, including signs, not merely its cancellation sum.

6. **Tail and rates, lines 271–322.** p and C_R are fixed before R because
   beta=1/s_R makes w=e. The explicit R choice is possible. Every nonzero
   matrix product has successive supports intersecting at a summed scalar
   index, making its full-reader union connected. Absolute multiplication and
   marking give PC18. The n-th tail term has M<=p r^n and B<=n_R p(n+1)r^n.
   Summing n>=1 gives PC19. Transpose symmetrization preserves the same
   full-reader labels and averages the two endpoint norms; it does not add a
   dimension factor or require each tail atom to be positive. Since
   r<=1/4 and pr<=c0/32, e_res<=c0/24, so the stated c0/16 is safe. No
   fixed support rate independent of R is established.

7. **Complex stability, lines 324–380.** The exact principal resolvent
   identity and entrywise envelopes give PC21, including J and J_abs. Its
   radius makes the sum of core changes <c0/8 in two-sided absolute norm.
   At the real center the nonnegatively weakened core is >=c0 I; arbitrary
   complex unit-disc residual coefficients cost <=c0/16. Hence the claimed
   Hermitian part >=13c0/16 follows. Projected-domain inverses are well-defined
   because all their coefficient readers are inside the label and an admitted
   completion exists. Matrix formulas do not depend on the center/completion.
   The operator upper bound U is conservative. The identity
   Re(C^-1)=C^{-*}(Re C)C^-1 implies precision >=a_C/U^2, not >=gamma.
   Lines 375–380 correctly prohibit copying the PS gamma regulator unchanged.

8. **Complete-reader disconnection and Gaussian normalization, lines 382–432.**
   A connected full label meeting two partition parts has a crossing edge in
   every spanning tree, so its entire atom vanishes when crossing bonds are
   zero. This removes remote-reader diagonal entries too. The surviving
   covariance block depends only on original data in that component. PC28's
   principal matrix Log is analytic on the accretive cone; its determinant
   factor and quadratic form factor by direct sum. Normalization to one
   follows first on the real SPD slice and then by holomorphic continuation
   on the convex complex symmetric accretive domain with local dominated
   convergence from PC25. All d modes are counted. Product link-ball
   integration factorizes only for product test factors; the source expressly
   does not infer that property for the unchanged white cube or arbitrary history.

9. **Derivative and downstream limits, lines 434–505.** Differentiating one
   bond differentiates all atoms containing it in their chosen tree. The sum
   over ordered k-tuples is <=|S|^k; reserving delta=beta-beta'>0 yields
   |S|^k exp(-delta|S|)<=k!/delta^k, proving PC30 for endpoint and marked norms.
   PC31 retains (1/2) sum over every ordered scalar covariance pair, including
   diagonal pairs, plus the independent coefficient/test-factor derivative.
   It does not replace a forest chain rule with one endpoint pair. Chart
   integration by parts still gives PS15's two boundary terms, and higher
   corner traces remain. The exact PC32 prefactor is PS5's full determinant,
   Haar, sigma and source-vacuum identity. No interacting reference ratio is
   cancelled by Gaussian normalization.

10. **Claim boundary, lines 1–32 and 507–543.** The stated result is bounded
    covariance support in the supplied model. No new physical axiom,
    independent-review authority, audit verdict, all-order interacting theorem,
    continuum existence or physical mass gap is asserted. The literature
    references are background attribution only, not proof inputs. Both full
    physical targets remain open.

## Dependency and consumer accounting

Full actual producer sources, with hashes in the preliminary record:
CB 1–568; SA 1–722; PS 1–544. Necessary new contextual reads:

* INTERACTING_SELECTED_CORE_ASTRA.md 22–84,129–206, SHA256
  b6c875ccc83eb455e12e729ccbd29851d782c63b26e978381927de1e058bfb61.
  Used only to check IC2's actual phase and IC6's local derivative counting;
  its stronger interacting conclusions and its cited reviews are not premises.
* RD.md 708–891, SHA256
  a60232a648e9832d0223cc0fa06ef84d8dbfe54fa91f875a8c96c3f89140aba5.
  The actual input weight is mu_0+2, with one unit used at each tree stage.
  R15–R17 require one common product reference and actual integrated defect
  masses. They are not an unchanged consumer of this beta<2 covariance result.

FIXED_SOURCE_RADIUS_ASTRA.md was searched for labels and hash-identified but
its theorem is not consumed by the target. No FR or CS result was silently
used. No target author evidence was read to reach these findings.

## Explicitly unproved consequences

A usable smaller-margin cluster consumer; all-order Gaussian derivative-tree
and boundary/corner trace summation; exact interacting/component normalization;
the unchanged selected-sector complement and arbitrary retained histories;
original-cut complex nonvanishing; effective iteration; full continuum
existence; positive physical continuum mass gap. These are limits of this
proof, not impossibility theorems or an exhausted-route claim.

Mathematical freeze UTC: 2026-10-30T01:43:36.239494+00:00
