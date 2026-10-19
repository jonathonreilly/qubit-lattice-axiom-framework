# Explicit baseline resource family: distinct bounded check

No required mathematical correction was found in the pinned source. Its concrete cutoff, conservative derivative bounds, parameter family and nine ideal-error allocations establish uniform isometry error below epsilon for 0<epsilon<=1. The stated qubit, duration and coefficient exponents are correct for this prescribed family. They are sufficient resource exponents, not optimized exponents or lower bounds.

## Source identities and exposure

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

New complete source read and SHA-256 verified:

* `common_product_finite_seed_scaling/PROPOSAL.md`: `0e21dae83a8449f03276b4099ea6a6ae23e08afa5b4a1297122e67e7b9095f6e`.

Previously complete source reads and checks in this same coherent checking session, reused after refreshing their matching hashes:

* `common_product_finite_seed_router/PROPOSAL.md`: `3a195efcf8d5196ed54a74228033d0888e7f18c864e481ce61b2efea6c67992b`.
* `common_product_finite_window/PROPOSAL.md`: `1ea1943e162c1ab7f0da057a1343b95b859e394c25420d5577830a838d116b1b`.
* `common_product_finite_seed_router_check/REVIEW.md`: `5f5b1727a31df17facb9232e902c1d6985cd175058d66e54862ae614fef148a9`.
* `common_product_finite_window_check/REVIEW.md`: `1337df4d94e3d6b555a88167945e5e8490e9df978b1fbc3e140db17622e36cbb`.

I authored the two reused check reports. They support their own source scopes and are shared exposure, not prior verification of this explicit resource certificate. ROOT requested quantitative checking; I read the proposed constants before reconstructing the inequalities below. This is source-exposed same-model checking with the inherited effort, not blind discovery or model-diverse replication. No proposed sharper derivative result or other worker's result was read or used. Existing workflow snapshots are reused; no remote-main freshness, formal audit or retained status is asserted.

## Exact amplitude and concrete cutoff

Dividing the pinned source formula by j and rationalizing gives

    u sqrt(w) = sqrt(2/pi) rho exp(ik) sin(k)
                 /[rho² sin(k)+i(2-rho²)cos(k)].

This is an equality of complex amplitudes, not only densities. The incoming amplitude is its conjugate because sqrt(w) is real. Thus the phase used by the composition is preserved.

For Q(s)=1-10s³+15s⁴-6s⁵, Q(0)=1, Q(1)=0, and Q',Q'' vanish at both endpoints. Q'=-30s²(1-s)²<=0, so the cutoff lies in [0,1]. The absolute-value coordinate causes no cusp at the band center because the cutoff is constant in a neighborhood there. The transition ends at pi/24+pi/12=pi/8, strictly within pi/6. Hence this is a valid fixed C_c² cutoff.

Using s(1-s)<=1/4 gives |Q'|<=30/16=15/8 and |Q''|<=60/4=15. Scaling by h yields exactly 45/(2pi) and 2160/pi²; pi>3 proves the displayed loose ceilings 7.5 and 240. No unsupported sharper derivative maximum is needed.

With A=2-rho²>=1, tan(pi/24)>=pi/24 and pi>3, the hard-band allowance is at most `(96/pi²)rho²<11rho²`. Since the cutoff equals one on that band, p_chi>=1-P. For rho<=1/8, 11rho²<=11/64<1/2, proving the strict positive normalization and its sqrt(2) upper factor. There is no surrogate spectrum or normalization fitted to a desired answer.

## Derivative and source constants

Write z=delta sin k+iA cos k and n=exp(ik)sin k. Orthogonal real/imaginary parts give |z|>=delta; the same trigonometric norm gives |z'|<=A<=2 and |z''|=|z|<=2. Also |n|<=1, |n'|<=2 and |n''|<=4. Differentiating gives

    (n/z)'' = n''/z - 2n'z'/z² - nz''/z²
                         +2n(z')²/z³.

The four terms have bounds 4/delta, 8/delta², 2/delta² and 8/delta³. Multiplication by c rho and rho<=1 yields the source constants 4c rho^-3 and 22c rho^-5, with no missing derivative term.

For the cutoff product, the first derivative is bounded by `(7.5+4)c rho^-3`. The second derivative is bounded by `(240+2*7.5*4+22)c rho^-5`. Integrating over a length at most pi, dividing by sqrt(p_chi), and using c<1 and sqrt(2)pi<6 gives constants below 69 and 1932, respectively. Therefore the claimed 100 and 2000 are safe. The L1 bound G0<=sqrt(pi)<2 follows independently by Cauchy–Schwarz from exact L2 normalization.

Because chi is real, chi g_- is the conjugate of chi g_+. Its derivative L1 norm is sqrt(p_chi)G1<=G1, and its L1 norm is <=sqrt(pi). Thus B_minus<=100rho^-3+4<=200rho^-3. Its 2/cmin factor is dimensionless, consistent with the launch expression 2j/vmin. These are deliberately global denominator bounds and do not claim optimal rho dependence.

## Integer family, gaps and tails

For the final family rho=epsilon/256<=1/256, so all preliminary rho restrictions hold. Set u=u0 and ell=ceil(100u). Then ell>=100u, while u is already much greater than one throughout 0<epsilon<=1. The alpha choices 3/4 and 7/8 lie in (1/sqrt(3),1), since sqrt(3)>5/3. The late gap exceeds ell/4; the boundary return gap at the right endpoint is ell/4; the outgoing discarded-tail gap is ell/4+2. The early gap ell+1-2u exceeds ell/2, with u/A_early<=1/50. All strict time-ordering, pre-return and positive-gap hypotheses follow.

For A>=1, `(A^-2+A^-1)/(2pi)<=1/A`, validating (8). Inserting G0<2 and G1<=100rho^-3 gives the following safe constants:

* Right early tail: numerator at most 100rho^-3+4<=104rho^-3 and A>=u.
* Early matching tail with its sqrt(2) multiplier: at most `2(100rho^-3+4/50)/sqrt(ell)`, below the stated 300rho^-3/sqrt(ell).
* Late left-endpoint tail: numerator at most 100rho^-3+12<=112rho^-3 and 1/sqrt(A)<2/sqrt(ell), giving 224.
* Outgoing right-endpoint tail: numerator at most 100rho^-3+14<=114rho^-3 and 1/sqrt(A)<2/sqrt(ell), giving 228.

The normalization quotient is handled by mixed endpoints, as required: d_L<=230epsilon/10^7<1/2, so d_O<=2n_O<=460epsilon/10^7<1. No monotonicity of the quotient is assumed. Source launch normalization is justified below, and the finite target remains exactly the pinned phased beta_F(t).

## Every ideal-error allocation

The identity sqrt(u)=10^6rho^-3/epsilon and inequality sqrt(ell)>=10sqrt(u) imply explicit upper bounds for the square-root terms:

    2L0 <= 400 epsilon/10^6,
    2d_right <= 208 epsilon/10^6,
    sqrt(2)T_early <= 300 epsilon/10^7,
    2d_L <= 460 epsilon/10^7,
    2d_O <= 920 epsilon/10^7.

Each is strictly below epsilon/16. The source residual bound gives `2R0<=2rho^4 epsilon²/10^12`, also below epsilon/16. The spectral contribution satisfies `4sqrt(P)<=4sqrt(11)epsilon/256<epsilon/16`, since sqrt(11)<4. Hence 2delta_launch<=2R0+2L0+4sqrt(P)<3epsilon/16, proving delta_launch<1 without circularly invoking its normalization.

For d=ell+2, consecutive factorial-tail terms have ratio at most 1/25. The elementary factorial bound d!>=(d/e)^d gives `(4eu/d)^d<(1/8)^d`, using d>=100u and e<3. Thus e_early<3*8^-d<=3/d<=3/(100u). Substitution of u proves this below epsilon/16. This argument includes the correct first unequal power ell+2 from the composition.

For the boundary constants, coefficients at most 12 and 52 in A_i give `2000+1200+104=3304<4000` after factoring rho^-5. At the right endpoint uplus/qo=7/2; the A_o coefficients become 21 for G1 and 154 for G0, giving `2000+2100+308=4408<5000`. Thus both displayed constants hold.

The combined prefactor sqrt(3)d_hop/sqrt(2pi)<=sqrt(3/pi)j<j. Dropping the favorable terminal subtractions in B_window leaves an incoming bound 8000rho^-5/u and outgoing bound 10000rho^-5/ell, using cmin>1, qi(t0)>=u/2, cmax=2 and qo(tplus)=ell/4. Since ell>=100u, their sum is <=8100rho^-5/u=`8100rho epsilon²/10^12`, below epsilon/16.

These calculations account individually for exactly the nine listed nonnegative terms. Their sum is below 9epsilon/16 with no cancellation or omitted normalization cost. The estimates are uniform on the observation interval through the checked window theorem.

## Cell cost, physical cap and exponents

For eta=zeta=epsilon/[64(1+splus)], both ratios are positive and <=1/64. The whole-time cell envelope becomes

    epsilon * [(2+8splus)sqrt(2)+2splus]/[64(1+splus)]
       <= epsilon(8sqrt(2)+2)/64 < epsilon/4.

The last strict inequality follows, for example, from sqrt(2)<7/4. Consequently the complete error is below 13epsilon/16. The cell duration is splus/j from the actual seed; launch time has not been omitted. The channel factor two is correct, and substituting accuracy epsilon/2 preserves the asymptotic exponents.

D1=Lambda/2, D0=eta Lambda/2, b=eta²Lambda/2 and j=eta³Lambda/2 follow exactly because eta=zeta. These choices lie strictly within the previously checked incident-cap domain. They preserve the combined source-block convention; no full-block norm is replaced by a smaller summand convention. The construction has 8+2ell qubits and 9+2ell combined positive blocks, with no new resources added by this certificate.

At fixed Lambda, u and ell are Theta(epsilon^-8), despite the ceiling. Then splus is Theta(epsilon^-8), eta is Theta(epsilon^9), and the successive D0,b,j powers are 9,18,27. Multiplying j by rho adds one exponent, so gamma is Theta(Lambda epsilon^28). Dividing dimensionless duration by j gives Theta(Lambda^-1 epsilon^-35). The exact relative observation width is `(7/8-3/4)/(3/4)=1/6`.

For the displayed positive-term decomposition gamma is indeed the smallest positive supplied coefficient: gamma=rho j<j<a, b/j=1/eta>1, and j-gamma>gamma because rho<1/2. The same holds for 2j-gamma. Moreover `(D0-2b)/j=(1-2eta)/eta²>1` in this domain, and D1-2b is larger still. This comparison concerns scalar coefficients, including the subterms defining the combined B block. It is not a lower bound on all eigenvalues, an absolute-error tolerance, or a cost of generating exact coefficient correlations.

## Limits and record

The certificate establishes one extremely conservative conditional resource family. Exact supplied interactions, input/program preparation, coefficient correlations and native physical identifications remain premises. No sharper derivative estimate, optimality claim, permanent output, capture/reset, practical runtime, old apparatus constant or precision certificate follows. Large fixed constants are not concealed by the exponent notation.

Only this report was written. No scientific executable, parameter sweep, symbolic solver, source edit, W/Git/PR/canonical/checkpoint/editable-prompt change, model override or delegation occurred. All arithmetic above was reconstructed analytically; hashing and directory creation were bookkeeping. No retained or audit status is assigned.
