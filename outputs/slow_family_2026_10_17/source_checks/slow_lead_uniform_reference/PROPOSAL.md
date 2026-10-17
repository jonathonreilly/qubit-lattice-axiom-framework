# Uniform scalar slow reference: incoming bound and outgoing concentration

Status: new authored scalar-reference family lemma, requiring a distinct check. No actual-device temporal or finite theorem is inferred. The normalized transmitted reference obeys the explicit bounds (12) and (17) below. Their parameter dependence is in resonance units, with all cutoffs, phases and normalization retained.

## 1. Domain, sources and exact reference

Fix the supplied .0027<j<.003, the original old-arm phase and its fixed J. Use

    0<kappa<=10^-8, 0<g<=10^-6, 0<h<=4e-6,
    gamma=kappa^2/j, d=2j sin h,
    H=d/gamma>=100, L=g/gamma>=100, d/g=H/L<=.024. (1)

The last condition together with H>=100 actually forces L>4000; the weaker displayed L>=100 suffices for the strip estimates. No optimality is claimed. Put epsilon=g/j<1/2700 and define

    q(k)=pi/2-asin(epsilon cos k),
    K_h=asin(d/(2g))<=asin(.012)<.012001,
    I_k=[pi/2-K_h,pi/2+K_h], I_q=pi/2+[-h,h].

These intervals map bijectively. The same scalar reference as in the fixed proof is

    F(q)=kappa E'_q zeta exp(i61q+i172k_old(q))
                                      /[sqrt(2pi)jD(q)],
    D(q)=-2j cos q+gamma exp(iq),
    k_old(q)=2asin(a sin(q/2)), a=sqrt(j/J)<1/3,
    F_s(k)=sqrt(epsilon) sin k/sin((q(k)+k)/2)
                                      *exp(i(q(k)+k)/2) F(q(k)). (2)

zeta is the unchanged fixed unimodular phase. The first slow site is m=0, distinct from the retained old gate port. The phase is Phi_s=61.5q+.5k+172k_old(q)+arg zeta. It is not61k.

Read/reuse complete fixed scalar source `../slow_lead_reference_packet/PROPOSAL.md` e6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e and its check6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5. Reuse my uniform endpoint source c8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887 and read COMPLETE its new root check `../slow_lead_uniform_endpoint_check/REVIEW.md`, f3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0. Only exact scalar measure/moment and interface identities are imported here, not actual endpoint or mass conclusions. Root exposed the proposed strip and scaling route. I authored uniform endpoint and slow gate/recovery arguments, but not the fixed scalar contour source. This is exposed author derivation, not independent review.

Applicable unchanged instructions are reused. No scientific execution, sweep, solver, delegation, Git/W, PR/publication, checkpoint, prompt or model change occurred. This is the sole deliverable. The original supplied phase/coefficient relations remain premises.

## 2. Normalization and useful explicit lower bounds

Exactly F_s=t_flux sqrt(dq/dk) F, with |t_flux|^2=1-|r|^2 and dq/dk=g sin k/(j sin q). Thus

    p_s=integral_Ik |F_s|^2 dk=p0-R,
    R=integral_Iq |r|^2 |F|^2 dq.                 (3)

The full0<q<pi reference has mass one. With A=2j-gamma and alpha=gamma/A, its exact y=tan(q-pi/2) measure is

    2kappa^2/[pi A^2] *dy/[(y^2+alpha^2)(1+y^2)].

The hard-band mass p0 is the exact expression (9) in uniform endpoint; it is not the former fixed numerical p0 value. Bounding the outside integrand by y^-2 and using tan h>=sin h yields

    1-p0 <=8j^2/(pi A^2 H)<.68/H.                (4)

Here gamma/j<1.4e-11, so A/j>1.9999 and pi>3 suffice for the relaxed coefficient. The exact second-energy moment bound gives

    integral_Iq delta^2 |F|^2 dq
       <=16kappa^2 j^2 h/(pi A^2)<.68 gamma^2 H,  (5)

using h/sin h<1.000001. The uniform reflection estimate |r|<=.251|delta|/g then gives

    0<=R<.043 H/L^2,
    p_s>1-.68/H-.043 H/L^2>.9931.                (6)

The last inequality uses H>=100 and H/L<=.024. Thus every normalization below is well defined, with1/sqrt(p_s)<1.004. Retaining p_s explicitly is preferable to paying this loose ceiling.

Define the full integer-lattice normalized packets

    b_out(t,m)=[2pi p_s]^-1/2 integral_Ik
                                  F_s(k)exp(ikm-itE_s(k))dk,
    b_in(t,m)=[2pi p_s]^-1/2 integral_Ik
                         conjugate(F_s(k))exp(-ikm-itE_s(k))dk,
    E_s(k)=2j-2g cos k.

Both full-lattice norms are one by Fourier isometry. The physical slow ray is m>=0, so the outgoing complement is m<=-1 and the incoming physical restriction INCLUDES m=0. Their raw counterparts have norm sqrt(p_s); all bounds below multiply by sqrt(p_s) when unnormalized.

## 3. Uniform outgoing strip and denominator

Set y0=gamma/(4g)=1/(4L)<=.0025. Use z=x-iy with x in I_k,0<=y<=y0. On this rectangle |epsilon cos z|<5e-6. The principal q(z) and k_old(q(z)) are analytic, with

    |q'|<.000371, |k_old'|<.25,
    |Phi_s'|<=.5+104.5*.000371<.55.

The old arcsin argument remains near its fixed interior value, so this is the same explicit branch derivative estimate as the scalar ancestor, on the stated tiny q image. The outgoing phase ratio is <=exp(.55y). Temporal decay obeys

    Im E_s(x-iy)=-2g sin x sinh y<=-1.99g y.

Put S(z)=sqrt(1-epsilon^2 cos^2 z)=sin q(z) and A_s=2g-gamma epsilon>0. Then

    D_s(z)=D(q(z))=-A_s cos z+i gamma S(z).

For real x, S(x)>.99999999. Throughout the rectangle |S'|<2e-7, so |S(z)-S(x)|<5e-10. The comparison

    D_tilde=-A_s cos x cosh y
                   +i[gamma S(x)-A_s sin x sinh y]

retains more than .499 of its real-line imaginary part: A_s<=2g,2g y0=gamma/2 and sinh(y0)/y0<1.000002. Its real part does not decrease in magnitude. Therefore |D_tilde|>=.499|D_s(x)|. The correction is <5e-10 gamma, whereas |D_s(x)|>=.999999 gamma. A safe uniform result is

    |D_s(x-iy)|>.49|D_s(x)|.                    (7)

This proves absence of poles through the full rectangle, including the center and cutoff sides; it is not a center-only denominator estimate.

Apart from phase and denominator, F_s has numerator

    2kappa sqrt(epsilon) S(z) sin z /
                                     [sqrt(2pi)sin((q(z)+z)/2)].

Relative to the corresponding real factors, S costs <1.000001 and |sin(x-iy)|/sin x<1.000004. The real part of (q(z)+z)/2 stays within .006004 of pi/2, since the q displacement is <=.000371*.0025. Thus its sine modulus is >.99998; the ratio of the real denominator to its complex modulus is <1.000021. The phase costs exp(.55*.0025)<1.0014. Their product divided by .49 is <2.05. Consequently

    ||F_s(.-iy0)||_L2(Ik)<2.05 sqrt(p_s).         (8)

The larger strip relative to the fixed proof has been paid explicitly; its old1.000001 phase estimate was not copied.

## 4. Bottom and both hard-cutoff sides

Extend the shifted integrand by zero to one2pi interval and apply Parseval. For m=-l,l>=1, the additional spatial factor exp(-l y0) is contractive. Equations (7)–(8) give normalized bottom norm

    <2.1 exp[-1.99g t/(4L)]
     =2.1 exp[-.4975 gamma t].                   (9)

This uses L2 control, not a peak-times-bandwidth estimate. The cutoff indicator itself is not analytically continued.

At x=pi/2±K_h, |2g cos x|=d. The real part of D_tilde has modulus (1-gamma/(2j))d cosh y. Its correction is <5e-10 gamma<=5e-12 d since H>=100. Hence |D_s|>.99d on either side. The numerator bounds |S|<1.001, |sin z|<1.001, sine denominator>.9999 and sqrt(2pi)>2.5 imply

    |F_s(x-iy)|/sqrt(p_s)
      <sqrt(L)/(H sqrt(p_s)) exp(.55y).          (10)

Indeed kappa sqrt(g/j)/d=sqrt(L)/H and the remaining coefficient is <1. Both vertical sides and the outer Fourier factor <.4 yield pointwise side amplitude at m=-l at most

    .8 sqrt(L)/[H sqrt(p_s)(s_t+l)],
    s_t=1.99g t-.55.

For s_t>0, summing l>=1 gives squared reciprocal sum<=1/s_t. If sigma=gamma t satisfies L sigma>=1, then s_t>=1.44L sigma>1. Therefore the normalized total side norm is bounded by

    .8/[H sqrt(p_s) sqrt(sigma)].                (11)

Combining (9) and (11), with the trivial norm ceiling, proves

    ||b_out(t)||_(m<=-1)
      <=min{1,2.1 exp(-.4975 sigma)
                    +.8/[H sqrt(p_s sigma)]},
    sigma=gamma t, L sigma>=1.                   (12)

For earlier times the bound one applies. Equation (12) is an explicit uniform scalar concentration curve, not a selected onset or an actual apparatus success statement.

## 5. Incoming auxiliary extension and pole-free depth-one rectangle

Extend the EXACT scalar expression (2) to0<k<pi. Its q image is an interior subinterval of(0,pi) containing I_q. Flux contractivity bounds its mass by one. Its omitted part outside I_k has squared coefficient norm at most1-p0. This is an auxiliary scalar extension, not an expansion of the calibrated interacting-source energy domain.

For0<=Re z<=pi,-1<=Im z<=0, |epsilon cos z|<.000575. The principal q branch satisfies |q-pi/2|<.001 and Im q<=0. The old k_old branch is analytic and has Im k_old<=0. Also

    |sin((q(z)+z)/2)|>=sin(pi/4-.0005)>.7.

The analytic continuation of conjugate(F_s) uses exp(-iPhi_s) and Dbar(q)=-2j cos q+gamma exp(-iq). The phase modulus is at most exp(-y/2); the temporal modulus is at most one for every t>=0, and exactly one on vertical sides. For q=alpha-i beta with beta>=0,

    Im Dbar=-sin alpha[2j sinh beta+gamma exp(-beta)]<0.

Thus there are no poles on the full rectangle. On its bottom,

    |Dbar|>=2g sinh1-gamma>2g,                    (13)

using sinh1>1.1 and gamma/g=1/L<=.01. This replaces the former fixed tiny gamma/g estimate by an explicit uniform margin.

With |S|<1.001, |sin z|<=cosh1<1.55 and the denominator>.7, the phase-free bottom coefficient is <kappa/sqrt(jg)=1/sqrt(L). Paying the outer Fourier factor, interval length and geometric sum over m>=0 gives bottom norm

    <1.6/sqrt(L).                                (14)

For clarity pi/sqrt(2pi)<1.3 and (1-exp(-2))^-1/2<1.2 suffice. Dropping the beneficial exp(-1/2) phase factor is safe.

On either vertical side q is real, S<=1, and the real denominator has modulus2g cosh y(1-gamma/(2j))>1.99g cosh y. The phase-free coefficient is <[kappa/sqrt(jg)] y. Paying both sides and Fourier normalization bounds its mth amplitude by

    .8/sqrt(L) integral_0^1 y exp(-(m+.5)y)dy.

For m=0 this integral is <=1/2; for m>=1 it is <=1/m^2. Since sum_(m>=1)m^-4<=4/3, their squared sum is <=19/12. Thus both sides together have norm

    <1.1/sqrt(L).                                (15)

The complete auxiliary incoming physical-halfline norm is therefore <2.7/sqrt(L), uniformly for every t>=0. All endpoint contributions, including m=0, are paid.

## 6. Hard-band restriction and final incoming estimate

Fourier isometry, followed by halfline contraction, charges the auxiliary-to-hard-band difference by sqrt(1-p0). Divide by the actual transmitted normalization sqrt(p_s), not sqrt(p0). The result is

    ||b_in(t)||_(m>=0)
      <=min{1,[2.7/sqrt(L)+sqrt(1-p0)]/sqrt(p_s)},
    t>=0.                                       (16)

Using (4) gives the optional entirely explicit relaxation

    ||b_in(t)||_(m>=0)
      <=min{1,[2.7/sqrt(L)+sqrt(.68/H)]/sqrt(p_s)}. (17)

For the raw packet, multiply (12), (16), or (17) by sqrt(p_s). The exact p_s is given by (3), with safe lower bound (6). Its norm deficit includes BOTH hard-band loss and interface reflection; no renormalization is hidden in the formulas.

## Scope and remaining work

The proved candidate statements are scalar transmitted-reference mass bounds, all-time incoming restriction and the outgoing concentration curve on the explicit positive domain. Their constants are uniform in that domain; the physical waiting time remains t=sigma/gamma. No value of sigma, g, kappa or finite length is selected.

An actual-device family theorem still needs the complete two-lip coefficient synthesis, the real-band operator and omitted-mass interfaces, all finite/local and closed-tail contributions, literal K/W and physical scalar, and a separate finite-cap application. Those obligations cannot be replaced by the scalar auxiliary extension. This proposal supplies no actual success probability, uniform complex strip for the interacting device, native coefficient/seed supply, precision robustness or permanent storage claim. A distinct checker should reconstruct the widened outgoing strip constants, both side sequences, exact p_s and the incoming m=0 contribution before use.
