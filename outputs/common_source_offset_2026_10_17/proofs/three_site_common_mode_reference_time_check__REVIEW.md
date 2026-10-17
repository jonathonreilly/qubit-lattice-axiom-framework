# Distinct check of the shifted scalar reference-time estimate

Verdict: conditional support; no necessary correction found. The changed carrier, velocity, quadratic dispersion, physical coefficient, hard-band tails, periodized aliases and halfline estimates follow with the displayed constants. This is a scalar functional theorem, not an actual-device escape or performance certificate. No numerical point is selected.

Complete reviewed source: three_site_common_mode_reference_time/PROPOSAL.md, SHA256 646f26bdb76fbb0b5c8144d492f094c6ffd191fd7312a6c77373fdc069b9d4de. The complete common-mode traveling source and its check were read for the new exact coefficient scope. The common-mode scalar and unchanged outgoing/reference premises are reused at the identities below, with necessary outgoing coefficient equations refreshed directly.

## Physical coefficient, carrier and domain

At kD=acos(-Delta/(2g)), delta(kD)=Delta and v=2g sin kD>0. Direct trigonometric expansion gives

    delta(kD+x/v)-Delta
      =v sin(x/v)+Delta[cos(x/v)-1].

Differentiation gives vphys=v cos(x/v)-Delta sin(x/v). These retain the sign of Delta, including the negative curvature when Delta>0. The physical load in q_Delta remains m_j(delta), not m_j(delta-Delta). The scalar determinant margin is a previously checked same-offset statement, not a shifted processor calibration.

The raw Fourier coefficient follows from the inherited identity t_L(dq/dk)=t_f sqrt(dq/dk). The nominal source numerator kappa a1a2/sqrt(pi j) equals C=sqrt(8lambda^5/(3pi)). Squaring the displayed coefficient gives the scalar energy density times physical ddelta/dk and |t_f|², so p is the retained transmitted mass, 0<p<=1. The phase of t_f is already in 61.5q+.5k+172k_old; it must not appear a second time. The fixed zeta and complex denominator phase are preserved.

The chosen cell contains the physical hard band because both kD and its endpoints lie within asin(1/4) of pi/2. The proof cutoff exists for every strict |Delta|<d. From v²>=15g²/4 and D<=g/4, the stated maxima etaD<=7/360 and omegaD<=1/24 follow. Thus alphaD>0, and the central interval remains inside the ORIGINAL physical band: |delta|<=|Delta|+(1+etaD)D<|Delta|+2D<d. The original k_old derivative and phase hypotheses are applicable there.

## Weighted determinant, numerator and dispersion

Taylor bounds yield

    |y-x|<=|Delta|x²/(2v²)+|x|³/(6v²).

Consequently sqrt(y²+lambda²)>=alphaD sqrt(x²+lambda²), proving the denominator floor mD. For the cubic difference, factor the difference of two cubes and bound each factor by (1+etaD)sqrt(x²+lambda²). This gives exactly the coefficient3(1+etaD)² in Qerr. The scalar finite-band discrepancy contributes beta(1+etaD)³. No assumption that D²/(v lambda) is small is needed.

The numerator contains sqrt(vphys/v); omitting it would change the packet normalization. Since its square differs from one by at most omegaD<1, its difference from one is bounded by the same pointwise allowance. Both other positive factors are contractive: 1-sqrt(sin q)<=delta²/(4j²), and 1-|t_f|<=|r_L|²<=delta²/g². The latter bound is valid on the physical retained band by the exact scalar interface formula, with g/j<1e-6/.0027. These facts prove the displayed pointwise bound for N-1.

The normalized cubic density has second moment lambda²/3 and fourth moment lambda⁴. Minkowski applied to delta²<=Delta²+2|Delta|(1+etaD)|x|+(1+etaD)²x² gives precisely J2. Weighted L2 bounds then give Nerr. The phase chain rule is

    dphi/dx=.5/v+(61.5+172 k_old'(q))
                         (vphys/v)/(2j sin q),

so 102.78=61.5+172*.24 yields the stated P. Splitting the complex numerator/phase and denominator ratios, then dividing by mD, gives Ecentral with no extra numerator multiplier on its phase term.

The exact-versus-linear time comparison keeps exp[-it(2j+Delta)] on both sides. The quadratic displacement costs |t||Delta|lambda²/(2v²) by the finite fourth moment. The cubic displacement costs the displayed truncated-sixth-moment term because int_-D^D x⁶ rho(x)dx<=2D C². The untruncated cubic sixth moment diverges and is neither used nor silently bounded. The dispersion estimate grows with |t|; it does not support an all-late-time guarantee.

## Scalar mass, hard tails and aliases

The shifted nominal scalar first/third-power calculations give centered second moment lambda²/3 and sixth moment mu6=3lambda⁶+(8/3)jlambda⁵. The common source offset drops out of those local moments about its source center; it does not drop out of the physical lead load. Outside the original physical band, |delta-Delta|>=d-|Delta|, proving the first term in (2). Reflection loss is bounded by the full physical second moment Delta²+lambda²/3 divided by g². Thus (2) is a valid optional bound; it need not be informative and is not assumed positive.

Monotonicity of delta(k) on the physical band and the central endpoint estimates imply |delta-Delta|>=bD outside the proof cutoff. Scalar second/sixth moments, or the same-offset density bound C²/[(1-beta)²(y²+lambda²)³], give the stated U alternatives. Transmission is contractive. These are RAW physical tail bounds; there is no unaccounted 1/sqrt(p) factor because raw comparison precedes normalization. The rational tail is V by direct integration of C²/x⁶.

For period2pi v and central cell |x|<=pi v, a nonzero alias has distance at least (2|n|-1)pi v. Its norm is bounded by C sqrt(2pi v)/[(2|n|-1)³(pi v)³]. Summing both signs with 2sum(2n-1)^-3<=8/3 gives exactly

    Z=(8/3)sqrt(16/(3pi))*(lambda/(pi v))^(5/2).

No old centered alias constant is substituted. The linear time factors have modulus one in this real-line comparison, and the alias series converges in L2. Periodizing that complete time-dependent coefficient yields its full-line Fourier samples. Central error, dispersion and both tails compare the raw physical packet to the central-cell cubic; Z pays its periodization. Finally normalizing the physical packet costs exactly 1-sqrt(p). This establishes the full E(t) budget without twice charging either physical normalization or tails.

## Residue, physical m=0 and conjugate incoming wave

The lower-pole integral gives pi i s² exp(-lambda s) for s=t-m/v>=0. After the Fourier/Jacobian factor C/sqrt(2pi v), this is the source's i C sqrt(pi/(2v)). Both exp(i kD m) and exp[-it(2j+Delta)] remain, so equation (3) has the correct carrier, phase and velocity. The sampled comparator is not presumed normalized.

Its squared modulus is [4lambda⁵/(3v)]s⁴exp(-2lambda s). For t>=2/lambda this decreases along m<=0. Paying the m=0 endpoint and the integral over the rest gives the stated H_v polynomial, including the 4lambda/(3v) z⁴ term. The outgoing excluded set m<=0 is a conservative superset of the true complement m<0 of the physical ray m>=0. Thus both inequalities in (4) are valid even though the displayed sets overlap at zero.

Conjugating the FIXED incoming coefficient moves its cubic pole to the upper half-plane while the time factor remains exp(-itE). Its Fourier delay is t+m/v, so its comparison samples vanish for t>0 and m>=0, including m=0. The same norm budget proves (5). This is not time reversal of the actual dynamics and does not conjugate old/reference input vectors. In an actual traveling composition it accompanies W*, as the source explicitly states.

For raw packets, multiplication by sqrt(p) gives the displayed incoming bound and outgoing lower norm. The inequality 1-r<=1-sqrt(p)+C_out² follows from sqrt(1-C_out²)>=1-C_out². This is a single target normalization cost. If its lower bound is zero, the formula does not assert positivity; exact r>0 or another positive bound remains required before normalizing a physical-halfline target.

## Exposure, pins and limits

I authored the common-mode scalar source and actual inverse/moment interface, as well as the original scalar reference-time ancestor, and reviewed several outgoing/weighted ancestors. I did not author this new shifted weighted-time calculation. The author has shared attachment/reference ancestry. This is a distinct check of the changed calculation with prior exposure disclosed, not blind independence or a recertification of my own scalar premises. Those premises have the separate checks recorded below.

Verified identities:

- three_site_common_mode_reference_time/PROPOSAL.md: 646f26bdb76fbb0b5c8144d492f094c6ffd191fd7312a6c77373fdc069b9d4de.
- three_site_common_mode_source/PROPOSAL.md: 5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb; distinct check af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb.
- three_site_common_mode_traveling/PROPOSAL.md: 0abafe7b46fe6c93df110df8bc1e7a9dbc3a4eca30d38dbdea619337ca75940d; check4ac2571d63c5c6b4e7d7ea4e490a224b1e3d9d0a34b7ca4d82bce7fcc5038bdd.
- three_site_weighted_reference_time/PROPOSAL.md: d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36, with my earlier check809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac reused only within its unchanged conventions.
- three_site_outgoing/PROPOSAL.md: af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac, with my earlier check721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02; exact physical coefficient and transmission equations refreshed.

The result does not establish actual local escape, a full-device time/error point, unknown-offset closeness to a zero-offset packet, arbitrary coefficient tolerance, permanent storage or native implementation. In particular scalar no-hidden-mass does not exclude outside mass in an attached processor. The direct-core and converter-derivative tasks are not premises here.

Only this review was written. No numerical integration, dynamics, sweep, spectrum, scientific runner, solver, source/canonical/W/Git/PR/checkpoint/prompt/model modification or delegation occurred. Analytical reconstruction and deterministic identity inspection are the verification performed; this is not retained-status certification.
