# Distinct check: resonance-weighted scalar reference time

Disposition: **conditional support; no correction requested.** The new weighted central and dispersion estimates imply the stated E_w and scalar halfline bounds. They do not require the old cutoff-displacement smallness condition. Useful numerical smallness is not automatic, and no actual-device performance follows without the separate traveling/local/background/omitted-state composition.

Read complete changed proposal at SHA256 `d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36`. Also fully read the root tail refinement and distinct joint time/tail review. I authored the original scalar source and original reference-time proposal, and checked the outgoing/traveling interfaces. I did not author this weighted refinement. This is a distinct check of its new inequalities with shared ancestry disclosed. For the unchanged periodization, residue and halfline argument I use the separate completed review, not a claim of independent checking of my own original proof.

## Exact packet and admissible cutoff

The coefficient is literally F_s3. The numerator sqrt(2g) C sqrt(sin q sin k)|t_f|, phase zeta exp[i(61.5q+.5k+172k_old)] and complete q3 denominator agree with the checked slow Jacobian/flux identity. No phase of q3 or connector factor is absorbed into a free fitted phase. The carrier and old factor remain owed in the actual target.

The exact selected x endpoint is 2g asin(d/(2g))>=d. Hence every 0<D<=d lies within the physical hard band. On this interval |x|/(2g)<=1/4, delta has the sign of x, and sinc monotonicity gives alpha_D |x|<=|delta|<=|x|. In particular no hidden requirement D/lambda small or D^3/(g^2 lambda) small is needed. The suggested D=min(d,g/4) is positive and admissible but not required.

The exact full-band scalar polynomial lower bound is |q3(delta)|>=sqrt(1-3eta)(delta^2+lambda^2)^(3/2). Since alpha_D<=1, delta^2+lambda^2>=alpha_D^2(x^2+lambda^2). This proves the denominator margin m_D=sqrt(1-3eta)*alpha_D^3 without a displacement Neumann expansion. It is a scalar denominator bound; it says nothing by itself about an attached full-fiber inverse.

## New central ratio and moments

Factoring the difference of cubes gives

    |(delta+i lambda)^3-(x+i lambda)^3|
       <=3|delta-x| |x+i lambda|^2.

With |delta-x|<=|x|^3/(24g^2), division by |x+i lambda|^3 bounds this by x^2/(8g^2). Combining it with the checked lattice-versus-cubic determinant error proves |z_q-1|<=3eta+x^2/(8g^2), while the preceding exact margin gives |z_q|>=m_D. These are compatible even when the first upper bound exceeds one; inversion uses the independent lower bound, not 1-|z_q-1|.

The numerator N lies in [0,1]. Its deficit is bounded by the two sine deficits and the transmission deficit, the latter at most |r_L|^2<=delta^2/g^2. This yields x^2[1/(4j^2)+5/(4g^2)]. Adding the displacement coefficient 1/(8g^2) gives exactly 11/(8g^2), as in E_c.

The phase derivative is correctly taken in the linear slow-energy variable x. Differentiating the actual k_old formula gives a cos(q/2)/sqrt(1-a^2 sin^2(q/2)); monotonic numerator/denominator bounds on q in [pi/2-h,pi/2+h] give K_h. The stated square roots stay positive because j/J<.1. Together with |q'(x)|<=1/(2j cos h), this proves P_h. Independently the previously checked energy-margin inclusion first puts the whole band inside the original calibrated interval, after which k_old'<.24 proves P_safe with 61.5+172*.24=102.78. Thus neither phase choice is circular or removes the nominal j/J correlation.

For rho_M=C^2/(x^2+lambda^2)^3 the exact integrals are mass one, second moment lambda^2/3 and fourth moment lambda^4. They follow directly by rescaling x=lambda*y and integrating the even rational functions. The central ratio error is bounded pointwise by

    [3eta+P|x|+x^2(1/(4j^2)+11/(8g^2))]/m_D.

Minkowski in L2(rho_M dx) then gives precisely E_c. The phase term uses the second moment and the quadratic term uses the fourth moment. Extending these nonnegative integrals to the whole real line is legitimate. The exact complex ratio, not a density-only estimate, is being controlled.

## Truncated dispersion and remaining tails

After comparing the actual and rational amplitudes with the SAME actual time factor, only the rational amplitude needs its dispersion changed from delta to x. Consequently this step does not require another 1/m_D multiplier. Its squared weighted error is bounded by t^2/(24g^2)^2 times the central sixth-moment integral. The full sixth moment diverges, but on [-D,D], x^6/(x^2+lambda^2)^3<=1. Thus that integral is at most 2D C^2=16lambda^5 D/(3pi), proving the stated E_disp. The simplified expression and the D=cg scaling in the proposal follow algebraically. No divergent moment is silently extended to infinity.

The actual raw comparator tail U_sharp uses the energy threshold delta_D, not x threshold D. Its four alternatives are separately valid: total mass, exact second moment, exact sixth moment, and the checked scalar full-band rational-envelope tail with denominator 1-3eta. Flux contraction makes them valid for the transmitted raw packet. V_D instead pays the full cubic reference's energy tail. These are distinct charges and neither can replace the installed seed's omitted spectral mass.

The inherited alias series is unchanged by this refinement. The exact period is 4pi g in x; both-sign aliases and the odd-integer sum give the displayed Z_alias. Real time factors have modulus one, so its bound is uniform in t. The completed distinct joint time/tail review reconstructed this lattice periodization, the cubic residue and its prefactors. The present change alters none of those definitions or conventions. In particular the sampled comparator b is not presumed normalized as a lattice vector.

## Normalization, halfline and incoming scope

The preceding charges compare the raw physical Fourier sequence to b. Paying ||F/sqrt(p)-F||=1-sqrt(p) once proves (3). Positive exact p is sufficient; an optional lower bound using Xi can be used only where valid. This is comparator normalization, not actual postselection.

The inherited sum-integral bound on b requires t>=2/lambda and retains its m=0 summand, including the 2lambda/(3g) term in H^2. The proposal preserves this domain. The excluded set m<=0 is stronger than the physical complement m<0; therefore its estimate implies the stated physical-halfline lower norm bound without an indexing equality. For t>0 the conjugate rational packet has upper pole and samples supported on t+m/(2g)<=0, so it vanishes on m>=0. The same new central/dispersion majorants, with conjugated phase but unchanged physical time factor, give (5).

These are exactly the normalized scalar functionals used by the traveling interface. Its raw alpha and beta carry an additional sqrt(p) and common exp(-i2jt), so later synthesis must restore those factors and pay physical-halfline normalization only once. Actual incoming identification uses real rectangular Stone conjugation and the complete coefficient error, not the scalar estimate alone. No complete source/core escape, actual omitted-state bound or finite receiver theorem is established here. The growth of E_disp with |t| still prevents a uniform all-late-time conclusion from this comparison.

## Evidence and limits

The exact moment and scalar polynomial premises are reused at their separately checked identities. The calibrated energy-map argument was fully refreshed in the immediately preceding coherent dwell review. Complete changed arguments and the new time/tail review were read; no scientific computation, quadrature, sweep, dynamics, optimization, original calibration rerun or ancestral blanket certification occurred. Only this review was created; no W/Git/PR/checkpoint/prompt/model edit or delegation occurred.

Exact refreshed identities:

- `three_site_weighted_reference_time/PROPOSAL.md`: `d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36`.
- `three_site_reference_time/PROPOSAL.md`: `d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f`.
- `three_site_reference_tail/PROPOSAL.md`: `92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1`.
- `three_site_reference_time_check/REVIEW.md`: `0439d990a12b51561257038b1ef14aeb88302adf12bb546de0f00571ac44a553`.
- `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`.
- `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.
