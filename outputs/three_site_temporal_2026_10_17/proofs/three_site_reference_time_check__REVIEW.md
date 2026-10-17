# Three-site scalar reference time bounds: distinct check

## Disposition and exact target

**Conditional support; no necessary correction found.** The source provides the stated outgoing halfline concentration and conjugate incoming bound for the exact scalar packet, with the auxiliary cutoff condition r<1. The outgoing H-bound requires t>=2/lambda; the incoming bound is stated for t>0. The error E(t) grows with |t|, so the result is a finite-time comparison, not a uniform all-late-time claim. It supplies neither installed local/source escape nor actual full-device performance.

Read complete `three_site_reference_time/PROPOSAL.md`, SHA256 `d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f`, and verified all four cited outgoing/scalar source/check identities. Reused the unchanged completely read scalar normalization/moment proof and outgoing phase/Jacobian interface. The new residue, periodization, comparison constants and halfline sums were reconstructed directly below.

## Physical coefficient, cutoff and central error

Starting from F_s=t_f sqrt(dq/dk) F3 and kappa²a1²a2²=(8/3)jlambda^5 gives the prefactor sqrt(2g) C in (1). Its remaining modulus is sqrt(sin q sin k)|t_f| and its phase is the stated zeta exp(i phi), with the complete complex q3 still in the denominator. Thus (1) is exactly the outgoing source's packet; no flux/Jacobian factor, phase of the determinant, connector phase or first-site shift is missing. The comparison fixes phi0 once, independent of time and input.

The physical hard interval in x is centered and has endpoint 2g asin(d/(2g))>=d. Hence |x|<=D is inside the actual hard band whenever 0<D<=d. On that interval delta(x) has the same sign as x, |delta|<=|x| and |delta−x|<=D^3/(24g²). Also |delta+i lambda|<=|x+i lambda|. Combining the finite-band relative determinant estimate with the elementary difference of cubes proves the given r=3eta+3v(1+v)^2 bound. The denominator margin 1−r is therefore valid without replacing q3 by its modulus.

For the amplitude numerator, 1−sqrt(sin q sin k) is bounded by (1−sin q)+(1−sin k); the transmission deficit is bounded by |r_L|². Their sum gives A exactly as quoted. The phase discrepancy contributes at most Phi. Writing the central ratio as N exp[i(phi−phi0)](x+i lambda)^3/q3 gives the combined relative error at most (A+Phi+r)/(1−r). Integrating against the unit-mass cubic reference density yields Ecent with no additional normalization factor.

Replacing exp(−it delta) by exp(−it x) only in the rational comparison costs |t|D^3/(24g²). It does not analytically continue the actual packet or approximate its physical Hamiltonian globally. The actual raw tail outside |x|<=D has |delta|>=delta_D on its support; exact scalar moments and flux contraction give U. The full rational two-sided density tail is at most 16 lambda^5/(15pi D^5), whose square root is V. These are distinct actual-comparator and rational-reference cutoff costs, both retained.

## Periodization and cubic residue

For clarity one may choose the length-2pi Fourier cell centered at k=pi/2, i.e. x in [−2pi g,2pi g]. This is the central cell implicit in the periodization argument and represents the same integer lattice Fourier transform as any translated cell. The physical packet vanishes off its hard band in that cell. A 4pi g translate in x shifts k by 2pi, so exp(ikm) is unchanged for integer m.

After the dk-to-dx change, each alias term has its L2 norm measured by C²/(x²+lambda²)^3. The translate indexed by nonzero ell is supported at |x|>=(4|ell|−2)pi g. Bounding each translate by the full two-sided tail is conservative. Both signs of ell give the factor 2, and the odd-denominator sum is at most 4/3. Thus Z=(8/3)sqrt(16/(15pi))(lambda/(2pi g))^(5/2) is correct. Triangle inequality yields a convergent L2 series, uniformly in t. Absolute integrability of the amplitude tails also permits termwise Fourier integration. No alias orthogonality or sampled unit normalization is assumed.

For s=t−m/(2g), the continuum integral is

    integral_R exp(−ixs)/(x+i lambda)^3 dx
       = pi i s² exp(−lambda s) 1_{s>=0}.

For positive s the lower contour is clockwise; its residue is (−is)^2 exp(−lambda s)/2, giving the displayed positive i. The Fourier and variable-change prefactor is C/(2sqrt(pi g)), so the coefficient becomes i C sqrt(pi)/(2sqrt(g)) times s² exp(−lambda s), with the unchanged zeta exp(i phi0) exp(i pi m/2). This reproduces (5), including its phase, support and normalization. At s=0 the value is zero, so the boundary convention is harmless.

The central comparison, two tails and alias allowance therefore bound the raw Fourier-sequence discrepancy. The exact normalization cost from raw F to F/sqrt(p) is 1−sqrt(p). Adding it once proves (6). The sampled rational comparator is not presumed to have unit norm; the alias comparison already pays its discrepancy.

## Halfline sums, incoming partner and time scope

Squaring (5) gives coefficient 2lambda^5/(3g). On m<=0, put n=−m and s=t+n/(2g). The function s^4 exp(−2lambda s) is decreasing for s>=t when t>=2/lambda. Its lattice sum is bounded by its first summand plus 2g times its tail integral. Direct integration yields the polynomial

    exp(−2z)[(2lambda/(3g))z^4
           +(2/3)z^4+(4/3)z^3+2z²+2z+1].

Thus all terms in H² are correct. In particular the first summand retains m=0; omitting it would lose the lambda/g term. The m<=0 exclusion is deliberately stronger than the physical complement m<0. Its bound implies (9) because the actual normalized full Fourier sequence has norm one and the smaller physical excluded set has no greater norm. When epsilon_left<1, normalization of the physical restriction costs exactly 1 minus its norm, bounded as stated. This is normalization of a scalar comparator, not actual postselection.

For the conjugate packet the rational pole is at +i lambda. With incoming exponent the contour variable is s=t+m/(2g), and its Fourier sample vanishes when s>0. Therefore it vanishes for every m>=0 and t>0. Conjugating the coefficient preserves the central, tail and alias majorants; the time factor remains exp(−it delta). Equation (10) follows with the same E(t), including m=0 and both cutoff sides. There is no arbitrary change of the physical phase or replacement of the actual incoming row by this scalar without a separate Stone identification.

Equations (8)–(9) retain t>=2/lambda and r<1. On a finite interval in that domain, a supremum of H+E is a valid uniform ceiling. No smallness follows automatically for every admissible D or every time, and the growing dispersion term precludes a uniform all-late-time consequence from this proof. Keeping exact p is valid even when the optional Xi bound is uninformative. No operating point is assumed or evaluated here.

## Source exposure and verification limits

Exact unchanged premises:

- Outgoing source `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`; outgoing review `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- Scalar source `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823`; scalar review `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b`.

The target author authored the scalar source and checked the outgoing synthesis. I did not author this target or that scalar source; I previously authored narrower scalar/reference and traveling-interface work and reviewed shared attachment, inverse and composition ancestors. My recent traveling proposal specifies precisely the conjugate scalar functional used here, but is not evidence for the new residue/alias inequalities. Root exposed the cubic-impulse research direction. This is an exposed distinct same-model analytical check, not blind/model-diverse independence or wholesale recalibration.

Only scalar assertions have been supported. Actual incoming-coefficient identification, installed source/core escape, all-output aggregation, global actual omitted state, finite cut and any useful-time device theorem remain separate obligations. No scientific computation, quadrature, dynamics, sweep, optimization, external search, W/canonical/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this review file was created.

## Separate root-authored tail refinement

Also read and distinctly checked complete `three_site_reference_tail/PROPOSAL.md`, SHA256 `92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1`, after completing the frozen reference-time argument. **Conditional support; no correction required.** This is a new root-authored refinement, not a change to target d21632c8 or an assertion that its original moment U was invalid.

The exact open-channel determinant identity holds throughout the physical scalar band, not merely at the selected center. With eta<=1/16 it gives |q3|²>=(1−3eta)(delta²+lambda²)^3. Combining this with the exact density and sin(q)<=1 bounds the density by 8lambda^5/[3pi(1−3eta)|delta|^6]. Integrating the two tails from positive Delta gives the stated factor 16/(15pi), and extending beyond the physical band only enlarges the nonnegative bound. Absence of other scalar spectral mass is the checked isolated-source premise; this step would not bound unaccounted bound-state mass in an arbitrary attached apparatus.

On the retained slow interval, delta(x) is odd and strictly increasing. Thus the omitted raw transmitted packet has |delta|>delta_D, and flux contraction makes the same measure-tail estimate applicable. Taking its square root, together with the independently valid unit, second-moment and sixth-moment ceilings, gives precisely Usharp. Replacing U by this minimum in E(t) and the derived outgoing/incoming scalar bounds changes no central, phase, alias, dispersion or normalization term. The monotonic map and delta_D, not D itself in the energy tail, are essential.

The refinement uses the full-band polynomial identity from the already checked loaded inverse `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672` / my review `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`, as well as the scalar density/no-atom source pinned above. Root authored that inverse and this refinement; I checked the inverse and now this new tail integration with explicit shared exposure. This is solely a reference-packet improvement, not an actual installed omitted-state estimate, chosen operating point or complete performance certificate. Both source revisions remain unchanged.
