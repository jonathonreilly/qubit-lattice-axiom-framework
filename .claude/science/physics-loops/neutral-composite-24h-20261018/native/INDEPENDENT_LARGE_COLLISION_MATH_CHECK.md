# Large-feature native contact kernel: independent check

Disposition: PASS for the specified coefficient-level Born/contact numerator and its strictly positive critical scaled limit. No exact four-body S matrix or decay claim follows. Read /tmp/neutral_large_collision_root.md and probe; used the certified critical bracket from native/LARGE_BOUND_FEATURE_PROOF.md. No shared/canonical edits.

## Contact identity and permanent convention

The general directed-contact identity remains valid: apply the exact two-body eigen-equation separately to the two factors, including BOTH native interval rays and their actual signs/phases. All internal pair hopping and ray contributions cancel 2E times the product. A forbidden cross-pair hop i->j leaves the two distinct pairings contributing 2[f(j,k)f(j,l)+f(j,l)f(j,k)], hence the same factor four. This argument does not rely on the anchor's absent x ray. The common-layer four-singleton output receives the corresponding six-spin length-two ray inputs; higher flip counts cannot reach it in one native flip.

For the full 24-term labeled permanent, fix labels a,b on 0,d. The two orders of the remaining labels c,e convert the unordered k,l sum exactly into S_c S_e-G_(c+e), with no extra factor one-half. Summing the 12 choices a!=b and the four neighbors gives the stated 48-term expression with external factor four. Repeated outgoing momenta do not remove their labeled multiplicities: this permanent is four times the six-subset convention. It is explicitly unnormalized and should remain so in comparisons.

The exclusions are correct: phi(0)=0 already, while excluding d subtracts f_d exp(-ip.d) from S and f_d^2 exp(-iq.d) from G. The latter is an analytic square, not an absolute square, because the incoming pair factors are multiplied, not conjugated. The COM phase exp(iQ.d/2) is therefore necessary. The outgoing total momentum is 2Q modulo reciprocal vectors, and its energy is exactly 2E because cos(theta)+cos(qy)=1+b+delta/4.

## Critical convolution limit

The exact cavity expression gives phi_hat/u=hreg_b+p_b with p_b=tau_b/[delta+4(A_k+bB_k)]. Here hreg_b is uniformly bounded, nonpositive, and converges almost everywhere to h. The peak p_b is nonnegative. Its mass is exactly

 integral p_b=-tau_b g00=-sqrt(2)sigma(v.D)=Astar_b,

which tends to Astar>0. Its mass outside any fixed neighborhood of zero tends to zero since tau_b=O(1/log(1/delta)). Hence it is an approximate identity in the normalized torus measure, with mass Astar. The pointwise directional discontinuity of h at zero does not matter at the nonzero external q values used here.

The regular-regular convolution converges by dominated convergence. Each peak-regular term tends to Astar h(q), uniformly on compact sets separated from q=0. For peak-peak choose disjoint small neighborhoods of 0 and q. On the first, the shifted peak is O(tau_b), so the integral is O(tau_b Astar_b); the second is identical, and the complement is O(tau_b^2). Thus it tends to zero. This proves, without multiplying weak distributions,

 Fourier[(phi/u)^2](q) -> I(q)+2Astar h(q), q!=0.

All relevant momenta (0,+/-2theta,-pi) stay away from zero. The S factors likewise converge to h at their nonzero arguments. Consequently the stated limiting finite sum is justified.

## Coefficients of the remaining integrals

At criticality, sum_d exp(-ip_b.d)=2cos(theta)+2cos(qy)=2(1+b). For remaining momenta of opposite x signs, the removed labels have opposite signs: there are eight ordered assignments (a,b), giving coefficient -4*8*2(1+b)=-64(1+b) for I(0,-pi). For remaining momenta of equal x sign, there are four assignments in total, giving -32(1+b) for the combined equal convolutions I(+2theta,-pi)=I(-2theta,-pi). Thus both coefficients are exact; a finite-delta version would replace 1+b by 1+b+delta/4 before taking the limit.

The complete limiting kernel is real: inversion pairs each d and -d, and swaps the paired outgoing x momenta. Since phi is real and inversion-even after the displayed COM factor, the corresponding finite-sum terms are complex conjugates. The convolutions are real and reflection-even as well.

## Independent interval positivity certificate

Since h<=0, integral |h|=Astar. Its pointwise bound is

 |h|<=M=-sigma/(2sqrt(2))*max(vx,vy/b).

Therefore 0<=I(q)<=integral h^2<=M Astar. I independently implemented the elementary 48-term C expression with interval arithmetic at 40 digits over the entire certified bracket [0.2347569009270,0.2347569009271], using the critical eigenvector ratio vx/vy=sigma Gxy/(1-sigma Gxx) and normalization. Interval comparison proves vy/b>vx throughout the bracket. Results:

 C in [83.7430853217274,83.7430853229552],
 Astar in [0.511039634699002,0.511039634700285],
 M in [1.33968390069267,1.33968390069495],
 C-96(1+b)M Astar in [2.5891438341152,2.5891438356907].

The lower endpoint is strictly positive. This is an independent interval certificate, not a quadrature estimate or decimal eigenvector assumption. Files: /tmp/neutral_large_collision_reviewer_interval.py and /tmp/neutral_large_collision_reviewer_interval.json. The script also checks the convolution-coefficient intervals against their exact formulas; the exact combinatorial argument above supplies the identities. Small imaginary intervals arise solely from interval enclosure; exact reality follows from reflection as noted above.

Thus K/u^2 has a strictly positive critical limit, and the actual coefficient numerator is nonzero for sufficiently near-critical bound features. It fades with u^2~constant*delta log^2(1/delta); the large feature does not imply a nonvanishing unscaled collision strength. The numerical value near 51.052 is supplemental and is not needed for the positivity proof. The result concerns native on-shell contact/Born overlap with FREE outgoing constituent plane waves, not exact distorted four-body states, an exact S amplitude, a lifetime, a rate, or empirical/cosmological coupling.
