# Sharper scalar halfline bounds by combining weighted and exact-dispersion estimates

Author lemma requiring distinct checking. This is the SAME critical-reference packet, with its full physical phase, exact nonlinear slow dispersion, hard cutoff, integer lattice and first slow coordinate m=0. Combining two previously checked estimates yields a much smaller explicit all-late allowance on the existing mediated baseline's scalar tuple. It also gives a sharper finite-window estimate. This is not a new actual-device performance certificate or a new hardware point.

## Exact packet and hypotheses

Use the packet F and domains of all-late7044 and weighted d41e: 0<lambda<=1e-8, lambda/j<=1/16, original calibrated .0027<j<.003, 0<g<=1e-6, 0<h<=4e-6, d=2j sin h, d/g<=1/2. Write

 delta(k)=-2g cos k,
 q(k)=pi/2+asin(delta(k)/(2j)),
 k_old(q)=2asin(sqrt(j/J)sin(q/2)), J=.030021107107032,
 phi(k)=61.5q(k)+.5k+172k_old(q(k)),
 C=sqrt(8lambda^5/(3pi)),
 F(k)=zeta exp(i phi(k)) sqrt(2g) C
          *[sin q sin k/sin((q+k)/2)]/q3(delta(k)),

on |delta|<=d, and zero elsewhere in one length-2pi Fourier cell. The exact physical critical denominator q3 and original fixed unit phase zeta are unchanged. The transmitted reference mass is p=integral|F|²dk, 0<p<=1. The two normalized integer sequences are

 a_m(t)=(2pi p)^(-1/2) integral F(k) exp(imk-it delta(k))dk,
 i_m(t)=(2pi p)^(-1/2) integral conjugate(F(k))
                                           exp(-imk-it delta(k))dk.

The incoming formula conjugates the coefficient, not physical time or arbitrary input. Restore the common carrier exp[-it(c_att+2j)], old aging and W/W-star in an actual interface; none is fitted or altered here. The normalized physical outgoing halfline is a_+(t)/||a_+(t)|| when nonzero. The open coordinate m=0 is the first slow site, not the old gate port.

The general lemma below needs exactly the checked weighted constants, recalled explicitly. Choose any fixed proof cutoff 0<D<=d. Let

 alpha_D=sin(D/(2g))/(D/(2g)), delta_D=2g sin(D/(2g)),
 s=sqrt(1-3lambda/j), m_D=s alpha_D³,
 P=1/(4g)+102.78/(2j cos h),
 E_c=[3lambda/j+P lambda/sqrt(3)
                 +lambda²(1/(4j²)+11/(8g²))]/m_D,
 a_D=sqrt(16lambda^5 D/(3pi))/(24g²),
 U=min{1,lambda/(sqrt(3)delta_D),
       sqrt(3lambda^6+(8/3)jlambda^5)/delta_D³,
       sqrt(16/(15pi(1-3lambda/j)))(lambda/delta_D)^(5/2)},
 V_D=sqrt(16/(15pi))(lambda/D)^(5/2),
 Z_alias=(8/3)sqrt(16/(15pi))(lambda/(2pi g))^(5/2),
 E_0=E_c+U+V_D+Z_alias+1-sqrt(p).

All are nonnegative and a_D>0. In particular the checked weighted bound is E_w(t)=E_0+a_D|t|. Its exact complex amplitude comparison uses cubic second/fourth moments; only the truncated sixth moment bounds dispersion. The full sixth moment of the rational comparison is not used. Both physical/rational hard tails and both-sign lattice aliases remain in E_0. No assumption D³/(g²lambda)<<1 or actual-source complex strip is introduced.

For all-late constants put alpha=asin(d/(2g)), v=2g cos alpha and

 Q1=g/(j cos h), Pphi=.5+102.78Q1,
 PN=tan(h)Q1+tan(alpha)+.5tan((h+alpha)/2)(Q1+1),
 Aref=3+9(lambda/j)/(2cos h), K0=sqrt(2g)C,
 I0=2K0/(s v lambda²),
 I1=(Pphi+PN)I0+K0 Aref*pi/(2s²lambda³),
 B=2K0/[s(d²+lambda²)^(3/2)]+I1+(d/v)I0,
 b=B/sqrt(pi p v).

These are exact physical-coefficient variation and hard-endpoint ceilings, not derivatives of a value envelope. The original energy-margin proof supplies k_old'<.24 on this full band before the phase derivative is used.

## New combination lemma

Let

 h_in(t)=||1_(m>=0) i(t)||,
 h_left(t)=||1_(m<=0) a(t)||.

For t>=1/v, the all-late theorem gives BOTH h_in(t),h_left(t)<=min(1,b/sqrt(t)). It charges outgoing m=0 as well as the physical excluded m<0, by using the same n>=0 sum as incoming. Indeed its raw bound is B/sqrt(2pi)*sqrt((vt)^(-2)+(vt)^(-1)); vt>=1 gives B/sqrt(pi vt), then normalization divides by sqrt(p).

The weighted theorem gives h_in(t)<=min(1,E_0+a_D t) for t>0. For t>=2/lambda it gives h_left(t)<=min(1,H(lambda t)+E_0+a_D t), where

 H(z)²=exp(-2z)[(2lambda/(3g))z^4+(2/3)z^4
                                      +(4/3)z^3+2z²+2z+1].

These statements concern identical sequences, not nearby packets. We may therefore take the minimum of their bounds. Define

 t_cross=(b/a_D)^(2/3), R_cross=(a_D b²)^(1/3).

For every t>0,

 min(E_0+a_D t,b/sqrt(t))<=E_0+R_cross.               (1)

If t<=t_cross, use the first expression and a_D t<=R_cross. If t>=t_cross, use the second and b/sqrt(t)<=R_cross. This proves (1) without evaluating a new waveform, changing D in time, or extrapolating dispersion error to infinity. The growing estimate is used only where useful and the independently exact-dispersion estimate controls the rest.

Consequently, for every T>=max(1/v,2/lambda) and ALL t>=T,

 h_in(t)<=min(1,E_0+R_cross,b/sqrt(t)),
 h_left(t)<=min(1,H(lambda T)+E_0+R_cross,b/sqrt(t)).   (2)

To prove the second inequality use min(H+E,q)<=H+min(E,q). H is decreasing for z>=2: each positive monomial z^k exp(-2z),0<=k<=4, has nonpositive derivative there. Taking H(lambda t)<=H(lambda T) then gives (2). The separate b/sqrt(t) option retains actual decay to zero; the constant crossover allowance is a useful uniform ceiling, not a nonzero asymptotic obstruction.

For a finite window [T,T1] with T>=2/lambda, the often stronger alternatives remain

 h_in(t)<=min(1,E_0+a_D T1),
 h_left(t)<=min(1,H(lambda T)+E_0+a_D T1).            (3)

Thus the method does not discard the especially accurate weighted approximation at earlier times. No finite-window comparison error growing with t is used on all future times by itself.

## Raw norm and physical-halfline normalization

The exact raw sequences have norm sqrt(p). Multiply (2) or (3) by sqrt(p) for their raw wrong-halfline norms; multiplying again by1/sqrt(Z0) is owed in the mediated reference interface. If h is any ceiling for h_left<1, then

 ||beta_+(t)||²>=p(1-h²),
 ||beta_+/sqrt(p)||>=sqrt(1-h²).

The normalized physical scalar state differs from the raw halfline vector beta_+ by exactly1-||beta_+||, bounded by1-sqrt(p(1-h²)). For a mediated raw reference beta_+/sqrt(Z0), its cost is1-sqrt(p(1-h²)/Z0). This is ONE normalization cost. Do not add1-sqrt(p) separately in a complete comparison after using this expression. The1-sqrt(p) inside E_0 is only part of proving a bound on normalized scalar functionals, not another independently omitted physical state. The actual omitted spectral vector and actual two raw coefficient errors remain separate obligations and are not established by this scalar lemma.

Both hard edges survive in E_0 and B; no soft cutoff or zero boundary term is assumed. The weighted comparator's cubic residue is zero on the incoming m>=0 halfline for positive time, and H includes its m=0 outgoing sample. Aliases use the exact4pi g period in x=2g(k-pi/2), while the all-late estimate uses the exact integer sum directly. These are alternative checked estimates for one packet; no alias charge is lost when taking their minimum.

## Conservative evaluation on the EXISTING mediated baseline scalar tuple

This section changes no supplier, source length, g, calibration or physical cutoff. Use the already certified scalar enclosures of finitepoint243c1722/check080266c4:

 3.09e-18<lambda<3.10e-18,
 3.93e-11<rho<3.94e-11,
 g=5e-8, .0027<j<.003,
 p>1-2.065e-15,
 B<780135, v>9.9999992e-8.

Here the hard scalar halfwidth is d=rho and h in the above formulas means h_rho=asin(rho/(2j)), not a new original source calibration. The B,v bounds were certified for precisely that restriction. For E_c one can conservatively use the original h=4e-6 in P. Choose the single simple proof cutoff D=rho. It lies within the physical x-band because its endpoint is2g asin(rho/(2g))>=rho. This is not a new hardware parameter or an optimized cutoff search.

The following estimates are analytical inequalities using these enclosing constants, not a new dynamics calculation or rerun of the point script:

- D/(2g)<.000394, so alpha_D>=1-(.000394)²/6>.999999974 and m_D>.99999992.
- 2j cos(4e-6)>.0053 gives P<5.02e6. Therefore E_c<9.21e-12, using sqrt(3)>1.7, lambda<3.10e-18 and3lambda/j<3.45e-15; the lambda² term is below5.4e-21 before division by m_D.
- lambda/delta_D<8e-8. The square-root prefactors in U's sharp alternative and V_D are below1. Each corresponding tail is below(8e-8)^(5/2)<1.82e-18. The alias term is below1e-27. The normalization term1-sqrt(p)<=1-p<2.065e-15. Hence E_0<9.3e-12.
- a_D<2.37e-36: its squared numerator is at most16(3.10e-18)^5(3.94e-11)/(3pi)<2.006e-98, while24g²=6e-14.
- b²=B²/(pi p v)<1.94e18, using pi>3.14 and the certified p,v lower bounds. Thus a_D b²<4.5978e-18<(1.67e-6)^3, so R_cross<1.67e-6.

Take the scalar onset T_s=20/lambda, not the baseline1e24. It is above both2/lambda and1/v. For z=20, the bracket in H² is below344²: lambda/g<6.2e-11 and its additional discrete m=0 term is below6.7e-6. The elementary finite sum sum_(k=0)^12 5^k/k!>148 proves exp(20)>148^4=479785216. Therefore H(20)<344/479785216<7.18e-7. Combining these strict bounds gives, for ALL t>=20/lambda,

 h_in(t)<1.7e-6,
 h_left(t)<2.4e-6.                                   (4)

The exact scalar onset lies below6.473e18 in the same physical time units. This is substantially earlier than the generic-variation scalar threshold used in the baseline, while certifying much smaller scalar wrong-halfline norms. It does not by itself replace the baseline complete-device onset.

On the explicit finite scalar window20/lambda<=t<=40/lambda, t<=1.295e19 and a_D t<3.07e-17. Equations(3) therefore sharpen (4) to

 h_in(t)<1e-11,
 h_left(t)<7.2e-7.                                   (5)

For reference, the scalar raw-to-normalized physical-halfline cost is then at most1-sqrt(p(1-h_left²))<=1-p+h_left²<5.21e-13 on that window. For the all-late ceilings(4), the same scalar cost is below5.763e-12. These estimates do not include the mediated physical seed factor1/sqrt(Z0), and they must not be misreported as an actual apparatus error or actual omitted mass. The mediated normalization formula above retains that factor explicitly.

The finite-window estimate(5) is a scoped use of the previously checked weighted theorem; the all-late stitching(1)-(2) is the new elementary lemma. Neither is a new contour or actual-source analyticity result. The only evaluated hardware tuple is the already certified baseline, with no parameter sweep, favorable target requirement or optimization claim.

## Premises, exposure and remaining checks

The exact same-packet identification, residue/alias proof, physical coefficient derivative and original calibrated map are load-bearing. I refreshed the complete weighted proposal/check and reused the exact all-late proposal/check and finite-point arithmetic read in the immediately preceding coherent tasks. I authored weighted/all-late/traveling antecedents and checked other scalar and finite-point sources. This is source-exposed author composition, not independent validation of my own work. Root requested a sharper scalar certificate, not its conclusion.

A distinct check must reconstruct (1), the normalized/raw conversion and every conservative substitution in(4)-(5). Actual local/source/mediator/background error, actual full-input incoming/outgoing identification, one actual omitted state, normalized complete target and a new finite read-window cut must be separately composed before claiming an earlier apparatus point. No such complete point, resource inventory, native supply, physical robustness, repeated read or finite permanent halt is supplied here. The existing baseline certificate stays unchanged.

Exact identities:

- `three_site_all_late_reference/PROPOSAL.md`: `7044e77bcf2d944a3f1b4286b885691fd9f88e733a6ab49514111af5acbc5966`.
- `three_site_all_late_reference_check/REVIEW.md`: `4ba80afbbc2301fbb4e23aafe59f85b3a85ebdab160101f970774d0383139247`.
- `three_site_weighted_reference_time/PROPOSAL.md`: `d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36`.
- `three_site_weighted_reference_time_check/REVIEW.md`: `809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac`.
- `mediated_finite_point_candidate/PROPOSAL.md`: `243c172226f2a509ce9ba11686763ebc2e754f52a8b5a4e98d6ab4424c0ca20d`.
- `mediated_finite_point_check/REVIEW.md`: `080266c4b4f7d0b26ef2d366582961221a91294ed207f615bc29d7fbf4d1223d`.
- `three_site_outgoing/PROPOSAL.md`: `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac`.
- `three_site_outgoing_check/REVIEW.md`: `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`.
- `three_site_traveling_interface/PROPOSAL.md`: `75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3`.
- `three_site_reference_time/PROPOSAL.md`: `d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f`.
- `three_site_reference_tail/PROPOSAL.md`: `92a14fa12ccb489bfe311278683b6aa12b67b6549449273ba181383f5f779fb1`.
- `three_site_reference_time_check/REVIEW.md`: `0439d990a12b51561257038b1ef14aeb88302adf12bb546de0f00571ac44a553`.

Only this proposal was written. No new scientific execution, root solve, numerical integration, dynamics, sweep, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Deterministic source hashing was provenance bookkeeping, not scientific validation.
