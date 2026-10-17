# Scalar transmitted reference on the wider slow receiver band

Status: new conditional scalar lemma requiring a distinct check. On d/g<=.5, H>=100 and L=g/gamma>=200, the exact first-slow-site reference has p_s>.993. Its normalized outgoing complement and late incoming physical restriction obey, for sigma=gamma t with L sigma>=1,

    C_out<=min{1,2.1 exp(-.4825 sigma)
                           +.8/[H sqrt(p_s sigma)]},
    C_in<=min{1,1.7 exp(-1.93 L sigma)
                           +.72/[H sqrt(p_s sigma)]}. (1)

Both cutoff sides are paid, including incoming m=0. These are scalar-reference results only. No actual-source analytic continuation, actual omitted mass or actual-device temporal theorem is asserted.

## 1. Domain, packet and exposure

Keep the supplied .0027<j<.003, original J and common fixed unimodular zeta. Let

    0<kappa<=1e-8, 0<g<=1e-6, 0<h<=4e-6,
    gamma=kappa^2/j, d=2j sin h,
    H=d/gamma>=100, d/g<=.5, L=g/gamma>=2H>=200.

Write epsilon=g/j<1/2700, K_h=asin(d/(2g))<=asin(1/4)<.252681 and I_k=[pi/2-K_h,pi/2+K_h]. The exact branches and energies are

    q(k)=pi/2-asin(epsilon cos k),
    k_old(q)=2asin(a sin(q/2)), a=sqrt(j/J)<1/3,
    E_s(k)=2j-2g cos k, delta=-2g cos k=-2j cos q,
    D(q)=delta+gamma exp(iq).

The physical first slow site has m=0. Retain the EXACT coefficient

    F(q)=kappa E'_q zeta exp[i61q+i172k_old(q)]
                                      /[sqrt(2pi)jD(q)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    dq/dk=g sin k/(j sin q),
    F_s(k)=t_f sqrt(dq/dk) F(q(k))
      =2kappa sqrt(epsilon) sin q(k) sin k
       *zeta exp[i61.5q(k)+ik/2+i172k_old(q(k))]
       /[sqrt(2pi)sin((q(k)+k)/2)D(q(k))].             (2)

The phase is61.5q+.5k+172k_old+arg zeta; it is not a translation by61 slow sites. The physical connector amplitude t_L=sqrt(j/g)exp(ik)(1+r_L) and the flux amplitude t_f are not interchangeable without the Jacobian in(2).

Root proposed the wider domain and pointed to the possible cos(2x)<0 denominator reinforcement. I read the complete narrow uniform-reference and late-incoming arguments as context, not as constants that automatically transfer. I authored the wider gate/endpoint and earlier inverse refinements and checked some original components. This is source-exposed author derivation, not an independent check. I also read the full completed wider-gate check9c32a1c9 supporting corrected source5b667173. Only its exact interface and changed-domain scalar reflection are used here; no emitter conclusion is a premise. Exact identities are listed below. No numerical integration, sweep, scientific execution, subagent, W/Git/PR/checkpoint, prompt or model change occurred.

## 2. Exact normalization, reflection and moments

The genuine equal-diagonal j-chain reference has total mass one. Its hard q-band mass p0 has, with A=2j-gamma, alpha=gamma/A and y_h=tan h, the exact formula

    p0=4kappa^2/[pi A^2(1-alpha^2)]
                           *[atan(y_h/alpha)/alpha-h]. (3)

For example it follows by integrating the cotangent measure

    [2kappa^2/(pi A^2)] dy/[(y^2+alpha^2)(1+y^2)].

Its full integral is one since gamma(A+gamma)=2kappa^2. Thus total normalization is not an assumed Lorentzian. Multiplication by the exact phase in(2) changes no mass.

The scalar interface reflection is exactly r=(exp(iq)-exp(ik))/(exp(ik)-exp(-iq)). The checked wider calculation gives |r|<.128 and |r|<=.261|delta|/g. These also follow directly from the sine ratio, sin k>=sqrt(15/16), and g/j<1/2700. Current conservation and the Jacobian yield EXACTLY

    p_s=integral_Ik |F_s|^2 dk=p0-R,
    R=integral_Iq |r(q)|^2 |F(q)|^2 dq>=0.             (4)

For transparent reusable moment ceilings put

    M_q2=integral_Iq |q-pi/2|^2 |F(q)|^2 dq,
    M_E2=integral_Iq delta^2 |F(q)|^2 dq.

The cotangent density, tan u>=u and |delta|<=2j|u| give the safe bounds

    M_q2<=4kappa^2 h/(pi A^2)*(h/sin h)^2,
    M_E2<=16kappa^2 j^2 h/(pi A^2)<.68 gamma^2 H.     (5)

The optional factor(h/sin h)^2 in the first is conservative. The tail integral similarly gives

    1-p0<=8j^2/(pi A^2 H)<.68/H.                    (6)

Here gamma/j<1.4e-11, A/j>1.9999, h/sin h<1.000001 and pi>3 suffice. No fixed numerical tail or moment from the narrow device is inserted. If a first energy moment is needed, the exact energy density

    gamma sqrt(1-delta^2/(4j^2))
       /[pi((1-gamma/j)delta^2+gamma^2)]

gives integral_Iq |delta| |F|^2 dq<=gamma log(1+(1-gamma/j)H^2)/[pi(1-gamma/j)].

Equations(4)–(6) imply the NEW reflection allowance

    R<(.261)^2*.68 H/L^2<.047 H/L^2,
    p_s>1-.68/H-.047H/L^2>.993.                     (7)

The last inequality uses L>=2H and H>=100: the maximum displayed loss is .0068+.0001175=.0069175. The old.043 coefficient is not retained. In particular the transmitted normalization is positive, and it includes both cutoff and reflected mass.

Define normalized full-integer-lattice sequences

    b_out(t,m)=[2pi p_s]^-1/2 integral_Ik
                                  F_s(k)exp[ikm-itE_s(k)]dk,
    b_in(t,m)=[2pi p_s]^-1/2 integral_Ik
                         conjugate(F_s(k))exp[-ikm-itE_s(k)]dk.

Each has full-lattice norm one. The outgoing complement is m<=-1; incoming physical restriction is m>=0, including0. Raw packets are sqrt(p_s) times these sequences.

## 3. Shallow outgoing contour on the wider interval

Set y0=1/(4L)<=.00125 and use z=x-iy, x in I_k, 0<=y<=y0. The principal q and k_old branches are analytic. The correlated band condition implies |epsilon cos x|<=sin h<=4e-6, while the imaginary displacement is at most epsilon sinh y0. Thus |epsilon cos z|<5e-6 and |q-pi/2|<6e-6. On this rectangle

    |q'|<.000371, |k_old'|<.25,
    |Phi_s'|<.5+104.5*.000371<.55.

The explicit old arcsine branch derivative follows from a<1/3 and its argument staying near a/sqrt2, strictly away from a branch point. Hence the outgoing phase grows by at most exp(.55y). Since sin x>=sqrt(15/16)>.968,

    |exp[-itE_s(x-iy)]|<=exp(-1.93g t y), t>=0.       (8)

Write S(z)=sqrt(1-epsilon^2 cos^2 z), positive on the real band, and A_s=2g-gamma epsilon. The outgoing denominator is

    D_s(z)=-A_s cos z+i gamma S(z).

On the strip S(x)>.99999999 and |S'|<2e-7, so |S(z)-S(x)|<2.5e-10. Compare with

    Dtilde=-A_s cos x cosh y
                 +i[gamma S(x)-A_s sin x sinh y].

Its real magnitude does not decrease. Since A_s<=2g and2g y0=gamma/2, with sinh(y0)/y0<1.000001, its imaginary component remains more than.499 of the real-line imaginary component. Thus |Dtilde|>=.499|D_s(x)|. The correction is<2.5e-10 gamma and |D_s(x)|>=.999999gamma, giving

    |D_s(x-iy)|>.49|D_s(x)|.                         (9)

This excludes poles over the WHOLE rectangle, not only the center.

The numerator ratios satisfy |S(z)|/S(x)<1.000001 and |sin(x-iy)|/sin x<1.000003. The real part of(q(z)+z)/2 differs from pi/2 by less than(.252681+.000006)/2; its sine modulus is>.992. The real numerator's sine denominator is<=1. Therefore the coefficient ratio, including phase, is bounded by

    1.000001*1.000003*exp(.55*.00125)/(.992*.49)<2.1.

In particular ||F_s(.-iy0)||_2<2.1sqrt(p_s). Extending the bottom integrand by zero to a2pi interval and applying Parseval gives outgoing complementary bottom norm

    <=2.1 exp[-1.93g t/(4L)]=2.1 exp(-.4825 sigma).    (10)

For m=-l,l>=1, its additional factor exp(-l y0) is contractive. No peak-times-bandwidth estimate is used.

At a cutoff x=pi/2±K_h the real part of Dtilde has magnitude(1-gamma/(2j))d cosh y. The correction is<2.5e-10 gamma<=2.5e-12 d, so |D_s|>.99d on either vertical side. Numerator bounds and sqrt(2pi)>2.5 give the phase-free coefficient ceiling

    |F_s(x-iy)|/sqrt(p_s)
         <sqrt(L)/(H sqrt(p_s))*exp(.55y).           (11)

For instance2*1.001*1.001/(2.5*.992*.99)<1 is a sufficient numerical witness. Both sides and the outer Fourier factor give at m=-l a total bound .8sqrt(L)/[H sqrt(p_s)(l+s)], s=1.93gt-.55. When gt=L sigma>=1, s>=1.38gt>0 and sum_(l>=1)(l+s)^-2<=1/s. Hence their norm is at most .8/[H sqrt(p_s sigma)], proving the outgoing part of(1). The hard cutoff itself was never analytically continued; its two boundary segments were paid.

## 4. Deep incoming contour and reinforced conjugate denominator

Now use the same ORIGINAL hard x interval but0<=y<=1. No auxiliary full-band extension is required. On this rectangle |epsilon cos z|<.000575, so |q-pi/2|<.001. Both q and k_old remain analytic, with Im q<=0 and Im k_old<=0. In particular the incoming negative phase has modulus<=exp(-y/2). Also

    |sin((q(z)+z)/2)|
       >=cos((.252681+.001)/2)>.991.                 (12)

The continuation of the conjugate coefficient uses conjugate(zeta), negative phase and the CONJUGATE denominator

    Dbar_s(z)=-A_s cos z-i gamma S(z).                (13)

Write S=u_s+i v_s, u_s>0. Throughout the centered interval cos(2x)<0. Exact algebra gives

    Re(S^2)=1-epsilon^2 cos^2 x
                         -epsilon^2 cos(2x)sinh^2 y>=S(x)^2,
    u_s>=S(x),
    v_s=-epsilon^2 cos x sin x cosh y sinh y/u_s.

Consequently

    Re Dbar_s=-cos x cosh y
                  [A_s+gamma epsilon^2 sin x sinh y/u_s],
    Im Dbar_s=-A_s sin x sinh y-gamma u_s.

Their magnitudes reinforce, rather than cancel, their real-line counterparts. Thus

    |Dbar_s(x-iy)|>=|Dbar_s(x)|,
    |Dbar_s(x_cut-iy)|>.9999 d cosh y.                (14)

There are no poles over the complete depth-one rectangle. This proof uses the sign in(13); it would be wrong to apply it to the outgoing denominator.

For the incoming coefficient C(z), relative numerator ratios are bounded by |S(z)|/S(x)<1.001/.99999999, |sin(x-i)|/sin x<1.55/.968, and the denominator ratio<1/.991. Their product is<1.63. The phase is contractive and(14) does not enlarge the inverse denominator, so a convenient bound is

    ||C(.-i)||_2<1.7sqrt(p_s).

Parseval, the factor exp(-m) for m>=0 and(8), now valid throughout depth1 with the same1.93, give normalized bottom norm<=1.7exp(-1.93gt). This includes m=0 without spatial damping at that site.

On either cutoff side, |sin(x-iy)|<=cosh y cancels the cosh factor in(14). Since2*1.001/(2.5*.991*.9999)<1, the remaining phase-free coefficient is<sqrt(L)/(H sqrt(p_s)). The negative phase contributes exp(-y/2). Paying both sides and outer Fourier normalization gives each m>=0 amplitude at most

    .8sqrt(L)/(H sqrt(p_s))
                integral_0^1 exp[-(m+.5+1.93gt)y]dy
      <=.8sqrt(L)/[H sqrt(p_s)(m+s_in)],
    s_in=.5+1.93gt.

The complete sum INCLUDING m=0 satisfies sum_(m>=0)(m+s_in)^-2<=s_in^-2+s_in^-1. For gt=L sigma>=1,

    (gt)*(s_in^-1+s_in^-2)<=1/1.93+1/1.93^2,
    .8^2*(1/1.93+1/1.93^2)<.72^2.

Hence the combined sides have norm<=.72/[H sqrt(p_s sigma)]. Adding the bottom and the trivial full-lattice ceiling proves the incoming part of(1). The old.7 coefficient is not reused. There is no sqrt(1-p0) auxiliary-to-hard-band penalty because the actual hard endpoints were integrated directly; their costs have not disappeared.

## 5. Scalar contract and limits

For gt>=1 the raw scalar bounds are

    ||raw outgoing||_(m<=-1)
      <=min{sqrt(p_s),2.1sqrt(p_s)exp(-.4825gamma t)
                                     +.8/(H sqrt(gamma t))},
    ||raw incoming||_(m>=0)
      <=min{sqrt(p_s),1.7sqrt(p_s)exp(-1.93g t)
                                     +.72/(H sqrt(gamma t))}.

For earlier nonnegative times use the norm ceiling sqrt(p_s). The exact physical outgoing raw norm is at least sqrt(p_s)*sqrt(1-C_out^2); this is a scalar Fourier decomposition only. For each fixed positive triple C_out and C_in tend to zero, while outgoing physical norm tends to sqrt(p_s). No fixed observation time, operating point or finite receiver length is selected.

These statements retain the supplied phase, both origins, flux/Jacobian, reflection mass, hard cutoffs and m=0. They concern the explicit scalar reference, not an actual emitter spectral measure. The true source must still supply a real-band full-input coefficient comparison on the enlarged domain before scalar bounds can be used for actual incoming/outgoing contributions. Full local recovery, the one actual omitted state, literal K/W aging and all output coordinates remain separate parts of a device theorem. No actual-source continuation, uniform apparatus strip, runtime, success probability, native preparation or permanent storage follows here.

The argument requires a distinct check, particularly the changed strip geometry, positive mass lower bound, conjugate denominator sign and both endpoint sequence sums. Narrow constants were recomputed rather than transferred. Source identities alone are not proof or audit certification.

## Exact source identities

- `slow_lead_wider_receiver_band/PROPOSAL.md`: `5b667173cd9ee3d8faa285e5856e8a89e8a83ae87f09207664cc5115e247ee57`.
- `slow_lead_wider_receiver_band_check/REVIEW.md`: `9c32a1c901300c32cb6d0630cfef19e9aa33b9438274b6ab8dc561ccc2a38b0d`.
- `slow_lead_uniform_reference/PROPOSAL.md`: `5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907`.
- `slow_lead_uniform_reference_check/REVIEW.md`: `338e554834f994741982842c555589db5e62dba9ad121233989ce60068f26c93`.
- `slow_lead_incoming_late/PROPOSAL.md`: `59e2786a7174d06e3d95b3c6b7c8b08dd58cf8de63b9c596d5cfb6e5c3dfe6b5`.
- `slow_lead_reference_packet/PROPOSAL.md`: `e6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e`.
- `bandcenter_reference_measure_check/REVIEW.md`: `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae`.

The narrow uniform and late incoming sources are proof context, not asserted changed-domain temporal constants. The new actual wide endpoint/emitter result is not used as a premise of this scalar lemma.
