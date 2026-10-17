# Resonance-weighted three-site scalar reference time comparison

Status: new authored conditional refinement requiring a distinct check. This keeps exactly the scalar coefficient and physical phase of the checked three-site reference-time source. It replaces its central cutoff suprema by cubic-reference L2 moments, retains both tails and lattice aliases, and gives an explicit general finite-time inequality. No hardware point, installed escape or complete performance is selected.

## Fixed packet and domain

Retain the exact calibrated J=.030021107107032 and .0027<j<.003 with the original relation j=J(1−C0), not a freely retuned j. Use the three-site domain 0<lambda<=1e−8, eta=lambda/j<=1/16, 0<g<=1e−6, 0<h<=4e−6, d=2j sin h, d/g<=1/2. Put

    x=2g(k−pi/2), delta(x)=2g sin(x/(2g)),
    q(x)=pi/2+asin(delta(x)/(2j)), k(x)=pi/2+x/(2g),
    k_old(q)=2asin(sqrt(j/J)sin(q/2)),
    phi(x)=61.5q(x)+.5k(x)+172k_old(q(x)), phi0=phi(0),
    C=sqrt(8lambda^5/(3pi)),
    q3(delta)=(delta²−lambda²/3)(delta−3jlambda m_j(delta+i0))
                                           −(8lambda²/3)delta.

On the exact selected hard band, the raw coefficient is

    F(k)=zeta exp(i phi(x)) sqrt(2g) C
           sqrt(sin q sin k)|t_f| / q3(delta(x)),
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2).

It vanishes elsewhere in a length-2pi Fourier cell. Its exact transmitted mass is p=int|F|²dk, 0<p<=1. This is precisely F_s3 of the outgoing source. All detector/reference planes, the phase of q3 and the first slow coordinate m=0 are unchanged. No time-dependent phase is fitted.

Define the normalized outgoing and conjugate incoming sequences on all integer m by

    a_m(t)=1/sqrt(2pi) int F(k)/sqrt(p) exp[ikm−it delta(k)]dk,
    a_in,m(t)=1/sqrt(2pi) int conjugate(F(k))/sqrt(p)
                                         exp[−ikm−it delta(k)]dk.

The carrier exp[−it(c_att+2j)] and literal old aging/W remain outside these scalar definitions as in the actual traveling interface. Norm estimates do not remove them from a physical target.

## Explicit bound

Choose any auxiliary 0<D<=d; D changes no hardware. Define

    alpha_D=sin(D/(2g))/(D/(2g)),
    s_eta=sqrt(1−3eta), m_D=s_eta alpha_D^3,
    delta_D=2g sin(D/(2g)), mu6=3lambda^6+(8/3)jlambda^5.

Since D/(2g)<=1/4, alpha_D>0 and m_D>0. No condition of the old form D^3/(g²lambda)<<1 is required.

For an exact explicit physical phase constant put a=sqrt(j/J), q_-=pi/2−h, q_+=pi/2+h and

    K_h = a cos(q_-/2)/sqrt(1−a² sin²(q_+/2)),
    P_h = 1/(4g) + (61.5+172K_h)/(2j cos h).

All square roots are positive on the supplied domain. Alternatively, the already checked energy-map enclosure k_old'(q)<.24 permits the simpler ceiling

    P_safe = 1/(4g)+102.78/(2j cos h).

One may directly use P_safe without comparing the loose K_h expression numerically. Let P be either P_h or P_safe, each independently a valid bound on |phi'(x)|.

Set

    E_c = [3eta + P lambda/sqrt(3)
                    +lambda²(1/(4j²)+11/(8g²))]/m_D,
    E_disp(t)=|t|/(24g²)*sqrt(16lambda^5 D/(3pi)),
    U_sharp=min{1,lambda/(sqrt(3)delta_D),sqrt(mu6)/delta_D^3,
              sqrt(16/(15pi(1−3eta)))(lambda/delta_D)^(5/2)},
    V_D=sqrt(16/(15pi))(lambda/D)^(5/2),
    Z_alias=(8/3)sqrt(16/(15pi))(lambda/(2pi g))^(5/2),
    E_w(t)=E_c+E_disp(t)+U_sharp+V_D+Z_alias+1−sqrt(p).       (1)

One may simply use D=min{d,g/4}, which is always positive and admissible. This is a proof-cutoff convention, not an optimized or new hardware point. Keeping exact p is always valid; the outgoing source's Xi bound may replace it only in its stated domain.

Let b_m(t) be the SAME periodized cubic comparator as in the checked time source:

    b_m(t)=zeta exp(i phi0) exp(i pi m/2)
       i C sqrt(pi)/(2sqrt(g)) [t−m/(2g)]²
       exp[−lambda(t−m/(2g))] 1_{t−m/(2g)>=0}.             (2)

Then for every real t,

    ||a(t)−b(t)||_{ell2(Z)} <= E_w(t).                       (3)

For z=lambda t and t>=2/lambda define

    H(z)²=exp(−2z)[(2lambda/(3g))z^4
                   +(2/3)z^4+(4/3)z^3+2z²+2z+1].

The scalar consequences are

    ||1_{m<=0}a(t)|| <= min{1,H(lambda t)+E_w(t)},            (4)
    ||1_{m>=0}a(t)|| >= sqrt(1−min{1,H(lambda t)+E_w(t)}²).

For the conjugate incoming sequence, every t>0 obeys

    ||1_{m>=0}a_in(t)|| <= min{1,E_w(t)}.                    (5)

The physical outgoing complement is m<0; (4) deliberately also charges m=0. These bounds can be made uniform on a specified finite interval by taking their supremum, but E_disp grows with |t| and gives no uniform all-late-time theorem.

## Weighted central comparison

The normalized cubic density in the real variable x is

    rho_M(x)=C²/(x²+lambda²)^3,
    int rho_M=1, int x²rho_M=lambda²/3,
    int x^4rho_M=lambda^4.                                (6)

These are exact scalar integrals. On |x|<=D, sinc monotonicity gives |delta(x)|>=alpha_D |x|. The physical scalar determinant identity, valid on the entire j band, gives

    |q3(delta)|>=s_eta (delta²+lambda²)^(3/2)
                >=m_D (x²+lambda²)^(3/2).                 (7)

This is a positive exact-reference margin, not a small-displacement Neumann assumption. It is why the old supremum r<1 can be removed from this new comparison. No actual operator-valued source inverse is asserted by (7).

The checked lattice-to-cubic estimate is

    |q3(delta)−(delta+i lambda)^3|<=3eta|delta+i lambda|³.

Also |delta−x|<=|x|³/(24g²), and both |delta+i lambda| and |x+i lambda| are bounded by the latter. Factoring the difference of cubes therefore gives

    |(delta+i lambda)^3−(x+i lambda)^3|/|x+i lambda|³
       <=3|delta−x|/sqrt(x²+lambda²) <=x²/(8g²).

Thus for z_q=q3(delta)/(x+i lambda)^3,

    |z_q−1|<=3eta+x²/(8g²),  |z_q|>=m_D.                  (8)

Write N=sqrt(sin q sin k)|t_f|. The same physical reflection/flux bounds as in the outgoing proof imply

    0<=N<=1,
    1−N <= x²[1/(4j²)+5/(4g²)].                           (9)

No sin/flux factor is silently replaced by one in the coefficient; (9) pays for the replacement in norm.

The derivative of the fixed physical phase is

    phi'(x)=(61.5+172 k_old'(q)) q'(x)+1/(4g),
    q'(x)=cos(x/(2g))/(2j sin q),
    k_old'(q)=a cos(q/2)/sqrt(1−a²sin²(q/2)).

On this interval |q'|<=1/(2j cos h), and the exact last expression is at most K_h, proving |phi'|<=P_h. The alternative .24 bound follows from the original energy margins first placing this q-band inside the original calibrated k-band, then k_old'=2j sin q/E'_old<.24; it is not a circular derivative-domain argument. Hence |phi(x)−phi0|<=P|x| with either stated P.

Relative to F_M=zeta exp(i phi0)sqrt(2g)C/(x+i lambda)^3, the exact amplitude ratio is N exp[i(phi−phi0)]/z_q. Equations (8)–(9) bound its deviation from one by

    [P|x|+3eta+x²(1/(4j²)+11/(8g²))]/m_D.

Taking the L2 norm against rho_M on the central interval, applying Minkowski, and extending only nonnegative moment integrals to R gives exactly E_c by (6). This pays the fixed phase by its resonance-weighted second moment and the displacement/numerator by the finite fourth moment. There is no input- or time-dependent phase adjustment.

## Weighted dispersion, tails and integer lattice

After the central amplitude comparison, the remaining rational time-factor error obeys |exp(−it delta)−exp(−itx)|<=|t||x|³/(24g²). The full sixth moment of rho_M is infinite and is NOT used. Instead

    int_{−D}^D x^6 rho_M(x) dx <= 2D C²
                                  =16lambda^5 D/(3pi).

Its square root gives E_disp(t) in (1). This step preserves the actual nonlinear dispersion outside the estimate, and crucially truncates the sixth moment at D.

Outside the central interval the raw physical packet is bounded by U_sharp from the separately checked exact finite-band scalar tail. The full rational tail is V_D. The periodization argument is unchanged: period 4pi g in x corresponds to 2pi in k, the central cell is [−2pi g,2pi g], and the sum of both-sign aliases is bounded by Z_alias. Time multiplication has unit modulus on the real line, so this alias bound is uniform in t. The cubic residue gives exactly (2); its normalization and support were checked separately. The comparator is not presumed to be a unit lattice vector.

Adding central, dispersion, raw and rational tails and aliases gives the raw Fourier comparison. Normalizing the exact physical coefficient costs 1−sqrt(p) once, proving (3). The checked sum-integral bound on m<=0 gives H and then (4). For the conjugate rational coefficient the pole is upper and the sample is supported on t+m/(2g)<=0. It vanishes for t>0,m>=0; the same moment, tail and alias comparison proves (5). This retains the conjugated physical phase, both hard sides and m=0.

## What improves and what remains

The old central phase cost could be bounded by P D; it is now P lambda/sqrt(3), without changing the actual phase. The former denominator comparison used a cutoff displacement D^3/(g²lambda); (7)–(8) replace it by a rigorous margin and a weighted O(lambda²/g²) contribution. Dispersion is bounded by |t|lambda^(5/2)sqrt(D)/(6sqrt(3pi)g²), rather than a time times D³ supremum. These are improvements in the sufficient comparison method when the central cutoff is broad relative to lambda; they do not ensure every total bound or chosen cutoff is smaller in every regime.

For example, when an admissible D=cg is used with fixed 0<c<=1/2, the dispersion scale is (lambda|t|)(lambda/g)^(3/2)sqrt(c)/(6sqrt(3pi)); the rational tails scale as (lambda/g)^(5/2), and the phase includes O(lambda/g)+O(lambda/j). Smaller g/lambda still increases these costs. No useful threshold, operating point or hardware improvement is assumed. Other cutoffs or the old bound may remain preferable in some regimes; both frozen sources remain intact.

This is a scalar reference theorem only. Actual incoming identification requires the real Stone conjugation and full-input error allowance of the separate traveling interface; actual source/core escape, one global omitted seed state, normalization of a physical target and finite receiver transfer remain separate. The raw quantities for later synthesis are sqrt(p) times the normalized norms in (4)–(5). A later complete composition must not charge spectral normalization twice or replace actual omitted mass by this scalar tail.

## Exact sources and exposure

- Fixed time comparison `three_site_reference_time/PROPOSAL.md`: `d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f`.
- Tail refinement `three_site_reference_tail/PROPOSAL.md`: `92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1`; joint distinct review `three_site_reference_time_check/REVIEW.md`: `0439d990a12b51561257038b1ef14aeb88302adf12bb546de0f00571ac44a553`.
- Exact outgoing coefficient `three_site_outgoing/PROPOSAL.md`: `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`; review `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- Scalar density/moments `three_site_product_source/PROPOSAL.md`: `a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823`; review `c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b`.
- Full-band reference polynomial `three_site_loaded_inverse/PROPOSAL.md`: `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672`; review `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`.
- Original calibrated energy-map domain `bandcenter_bandwidth_extension/PROPOSAL.md`: `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`; scalar branch conventions also in `slow_lead_wide_reference/PROPOSAL.md`, `c2d7a0cbc06e2669b6e42fca50f3c902dc889b5fb02bc891aaf7d94ab6eff4fd`.

I authored this refinement, checked the fixed time/tail argument and reviewed or authored related scalar, inverse and traveling ancestors. Root suggested weighted moments and the possible smaller-g direction, not a proven conclusion. Complete unchanged time/tail, scalar and outgoing arguments were read in the coherent preceding tasks; the needed exact phase-map/domain passages were refreshed here. This is exposed author work, not independent review of itself or blind recertification of ancestry. A distinct check is required for the new central margin, moment constants, truncated-sixth-moment step and all normalization/alias bookkeeping. No scalar numerical integration, dynamics, sweep, optimization, scientific runner, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this proposal was created.
