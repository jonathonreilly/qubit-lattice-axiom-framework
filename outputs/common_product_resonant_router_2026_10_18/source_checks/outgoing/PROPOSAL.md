# Outgoing boundary cost from the exact source pole

New bounded author derivation, requiring distinct review. For the actual quintic cutoff and the full biased-network outgoing matrix, the outgoing part of the finite boundary integral admits a sufficient bound proportional to rho/(h^2 ell), with an explicit coefficient depending on network derivatives through order three. No complex continuation of the network, contour shift or phase inverse is assumed. The proof uses the exact lower-pole Laplace representation and three real integrations by parts. The specified C2 quintic cutoff is also W^{3,1}; an arbitrary C2 cutoff is not covered by that extra regularity premise.

This replaces only an outgoing boundary estimate. It does not improve incoming, internal, preparation or truncation costs by assertion, and does not re-optimize any frozen finite resource family.

## 1. Exact physical amplitude and domains

Retain the actual network and packet cf080, including its common record and ordinary program fiber. Use

    |k-pi/2|<=h<=10^-3, 0<=r<=10^-3,
    eta<=1/8, 0<zeta<1/2,
    e=13eta^2+5zeta, w=33h+480r, den=1-ew>0.

The incoming record is0. The outgoing record-a phase at radius n is

    Phi_a(k)=n k_a(k)+(ell+57)k-t E(k),
    k_0=k, k_1=q=acos(cos k+r/2), E(k)=2j(1-cos k).

Set ell>=1000, n in {ell,ell+1,ell+2}, and 0<=t<=T=7ell/(8j). Let

    M_a(k)=P_a J(k)^(-1/2) exp(-57ik) S(k)
                         sqrt(sin k) V_0,
    J=diag(sin k,sin q).                                (1)

Here V_0 injects arbitrary program/path input into I,record0; P_a projects the outgoing record channel while retaining ALL outgoing ports and logical/reference fibers. Thus the actual outgoing field at n is the sum of

    Y_a(n,t)=(2pi)^(-1/2) integral exp(iPhi_a(k))
                                      M_a(k)g(k) dk.    (2)

The physical scalar exp(-ict) is common and does not affect the norms. It is not removed from the actual solution. In particular (1) contains the correct sqrt(q') conversion on record1 and the ordinary conversion on record0. Replacing it by the flux matrix S alone would be incorrect.

Use precisely the finite source's g=chi F/sqrt(p), where p=||chi F||_2^2>=1/2,

    F(k)=-i sqrt(2/pi)rho exp(ik)
                         /[(2-rho^2)cot k-i rho^2],
    0<rho<=1/2, rho^2<=h.                               (3)

The real cutoff equals1 for |k-pi/2|<=h/2, is zero beyond3h/4, and on each width-h/4 transition is the quintic 1-10s^3+15s^4-6s^5. It has continuous derivatives through order two, zero first/second endpoint derivatives, and an integrable piecewise third derivative. No analytic cutoff is substituted. All coefficient/normalization phases in (2),(3) remain exact.

## 2. Remove the resonance on the real axis

Put x=tan(k-pi/2), k(x)=pi/2+atan x, A=2-rho^2, b=rho^2/A>0, and c0=sqrt(2/pi). Direct substitution gives

    F(k(x))=i c0 rho exp(ik(x))/[A(x+i b)].             (4)

The lower pole is x=-ib. For REAL x,

    1/(x+i b)=-i integral_0^infinity exp(ixv-bv) dv.      (5)

Define the compactly supported operator amplitude

    a_a(x)=chi(k(x)) exp(ik(x)) k'(x) M_a(k(x)),
    phi_a(x)=Phi_a(k(x)).

Equations (2)--(5) give the exact identity

    Y_a= rho/(pi A sqrt(p)) integral_0^infinity exp(-bv)
                  [integral exp(i(phi_a(x)+vx))a_a(x)dx]dv. (6)

Fubini is legitimate for each rho>0: the absolute integral before cancellation is bounded by ||a_a||_1/b. Uniform small-rho estimates are obtained after integration by parts, not by dropping this dependence in the Fubini justification. Crucially v>=0 ADDS to the positive outgoing phase derivative. No residue term crosses a contour, and no extension to the unphysical half-circle has been made.

## 3. Explicit phase ceilings

The packet's real-domain bounds are sin k,sin q>.99, |cos k|<=.001, |cos q|<=.0015, .99<=q'<=100/99, |q''|<.003 and |q'''|<3. Differentiating cos q=cos k+r/2 once more gives

    sin q q'''' = -cos k+cos q(q')^4
             +6 sin q(q')^2 q''-3 cos q(q'')^2
             -4 cos q q' q'''.                          (7)

Its absolute value divided by sin q is less than .04 using those displayed bounds, so the much looser ceiling |q''''|<=10 is safe. No differentiation of physical r is performed.

On the present three boundary levels, ell>=1000 and t<=T imply

    Phi_a'>=.24ell,
    |Phi_a''|<=2ell, |Phi_a'''|<=5ell,
    |Phi_a''''|<=20ell, |Phi_a'|<=4ell.                 (8)

For example the lower derivative is .99ell+ell-2jt>=.24ell; the positive +57 only helps. The upper bound uses n<=1.002ell and ell+57<=1.057ell. The E derivatives of every positive order used here have magnitude at most2j. These estimates include the elastic a=0 channel as well.

On the cutoff support |x|<.001, k'>=.999, |k''|<=.002, |k'''|<=3 and |k''''|<=.1. Chain differentiation of (8) therefore gives the convenient common ceilings

    phi_a'>=a_* ell, a_*=.23,
    |phi_a''|<=b2 ell, b2=4,
    |phi_a'''|<=b3 ell, b3=32,
    |phi_a''''|<=b4 ell, b4=128.                         (9)

For the fourth derivative the terms are Phi'''' k'^4+6Phi''' k'^2 k''+3Phi'' k''^2+4Phi'' k' k'''+Phi' k''''; even replacing |k''| by .004 gives a bound below45ell, hence (9). The actual phi_a+vx has derivative at least d_v=a_*ell+v; its higher derivatives are unchanged.

## 4. Three integrations by parts and auxiliary-frequency integration

Let A_s=||a_a^{(s)}||_1, s=0,...,3, with the highest derivative weak. Compact W^{3,1} amplitudes with the stated vanishing boundary traces allow three integrations by parts. For p_v=(phi_a+vx)', the differentiated integrand has terms with norm ceiling

    A3/d_v^3 +6b2 ell A2/d_v^4
      +(4b3 ell/d_v^4+15b2^2 ell^2/d_v^5)A1
      +(b4 ell/d_v^4+10b2 b3 ell^2/d_v^5
                                +15b2^3 ell^3/d_v^6)A0. (10)

This follows by applying d/dx(a/p_v) three times with the appropriate additional divisions by p_v. More explicitly the resulting absolute coefficient list is a'''/p_v^3, -6a''p_v'/p_v^4, -4a'p_v''/p_v^4, 15a'(p_v')^2/p_v^5, -a p_v'''/p_v^4, 10a p_v'p_v''/p_v^5, -15a(p_v')^3/p_v^6. Overall powers of i do not affect the norm. The argument applies to operator amplitudes in norm and has no logical/reference dimension factor.

In (6), bound exp(-bv)<=1 AFTER (10), and use integral_0^infinity (a_*ell+v)^(-m)dv=(a_*ell)^(1-m)/(m-1). Because 1/(pi A sqrt(p))<=sqrt(2)/(pi(7/4))<1, the result is

    ||Y_a(n,t)|| <=rho/ell^2 * B(A0,A1,A2,A3),          (11)
    B = A3/(2a_*^2)+2b2 A2/a_*^3
       +[4b3/(3a_*^3)+15b2^2/(4a_*^4)]A1
       +[b4/(3a_*^3)+10b2 b3/(4a_*^4)
                                  +3b2^3/a_*^5]A0.

This is uniform as rho decreases. It neither estimates F'' in absolute value nor loses the one-sided pole cancellation. With only two integrations by parts the v integral would leave one less power of ell; the third real derivative is essential to this route.

## 5. Cutoff and coefficient norms with no hidden rho cost

Suppose ||M_a^{(s)}(k)||<=M_s for s=0,...,3, uniformly in both records. An explicit construction of these constants for the actual network is given next. Extend the star rule to four entries by

    (u star v)_s=sum_(l=0)^s binomial(s,l)u_l v_(s-l).

All entries are nonnegative norm bounds; this does not commute the actual operator factors. A bound for C_a(x)=exp(ik(x))k'(x)M_a(k(x)) is the four-entry vector

    C=(1,1,2,5) star (1,1,3,10)
                  star (M0,M1,M2+M1,M3+3M2+3M1).       (12)

These constants follow from the displayed atan derivatives and chain rule. They have no rho or ell dependence from the source.

For chi_x(x)=chi(k(x)), the cutoff's weak derivative L1 bounds are

    ||chi_x||_1<=2h, ||chi_x'||_1<=20,
    ||chi_x''||_1<=300/h, ||chi_x'''||_1<=4000/h^2.     (13)

For clarity, in k coordinates the sup bounds are 8/h,100/h^2,3840/h^3; the third follows from |d^3(1-10s^3+15s^4-6s^5)/ds^3|<=60. Its two transitions have total width h/2, so the third L1 bound there is1920/h^2. The x-coordinate Jacobian sec^2(k-pi/2)<1.000002 and the chain formula chi_x'''=chi'''k'^3+3chi''k'k''+chi'k''' give (13) with ample margin. Continuous chi,chi',chi'' ensure that their distributional derivatives through order three introduce no atoms at the joins.

By Leibniz, (13) gives

    A0<=2h C0,
    A1<=20C0+2h C1,
    A2<=300C0/h+40C1+2h C2,
    A3<=4000C0/h^2+900C1/h+60C2+2h C3.                (14)

Since h<=1, a simple common bound is A_s<=Cbar_s/h^2 with

    Cbar0=2C0,
    Cbar1=20C0+2C1,
    Cbar2=300C0+40C1+2C2,
    Cbar3=4000C0+900C1+60C2+2C3.

Define the explicitly evaluable constant B_net=B(Cbar0,Cbar1,Cbar2,Cbar3) using (11). Then

    ||Y_a(n,t)||<=rho B_net/(h^2 ell^2).                (15)

It is harmless to use (14) directly for a smaller coefficient. The coarse B_net is used only to expose the dependence on rho,h,ell; it is not a practical estimate.

## 6. Actual network third derivatives: a real inverse certificate

The following four-entry arithmetic extends the exact packet formulas and verifies the M_s premise in (12). It needs only real-domain inverse margins already present in cf080, not an unproved complex neighborhood. Constants can be large and depend on eta,zeta,r,h through the stated margins.

Use D=(1,2,8,100) for J^{1/2} and also for sqrt(sin k), R=(2,4,40,200) for J^{-1/2}, and P=(1,68,4828,10^6) for Z^{34}. Indeed J',J'',J''' have ceilings2,10,5; ordinary scalar square-root derivative formulas with J>=.99 give the third ceilings100 and200. For Z^34, differentiating exp(34ik_a) three times and using |k_a'|<=2, |k_a''|<=6, |k_a'''|<=3 gives less than 10^6. Lower entries are the frozen packet bounds.

For the full48-dimensional biased writer, use B=11, ||L'||<=4, ||L''||<=12, ||L'''||<=10. The last follows from |(E/j)'''|<=2 and ||Z'''||<=5. The checked real inverse ||G||<=B therefore gives

    Gjet=(B,4B^2,32B^3+12B^2,
                         384B^4+288B^3+10B^2).         (16)

The general inverse third bound is 6B^4 L1^3+6B^3 L1 L2+B^2 L3, valid also for noncommuting matrices by triangle inequality over all ordered terms. Let W have zeroth entry1 and entries s=1,2,3 equal to (2 D star Gjet star D)_s. This bounds the full writer flux scattering -I-2iD E_P^*G E_P D. It retains the shared record and makes no X_R decomposition.

For the core, let lambda=1-3eta^2 and lambda_b=1-3eta^2 zeta. Define

    alpha1=2eta^2/lambda^2,
    alpha2=2eta^2/lambda^2+8eta^4/lambda^3,
    alpha3=2eta^2/lambda^2+24eta^4/lambda^3+48eta^6/lambda^4,
    beta1=2eta^2 zeta^2/lambda_b^2,
    beta2=2eta^2 zeta^2/lambda_b^2+8eta^4 zeta^3/lambda_b^3,
    beta3=2eta^2 zeta^2/lambda_b^2+24eta^4 zeta^3/lambda_b^3
                                      +48eta^6 zeta^4/lambda_b^4,
    l_s=1+2(alpha_s+beta_s), s=1,2,3.

These follow by three real derivatives of D0/(D0-E_0(s)) and D0/(D1-E_0(s)) on s in[pi/3,2pi/3]. The frozen outgoing core inverse has norm<=2. Thus its inverse derivatives are bounded by

    Ic=(2,4l1,16l1^2+4l2,96l1^3+48l1 l2+4l3).

Set Rraw=(2,2,2,2) star Ic, and take the composed record-diagonal core scattering ceiling

    Cs=(1,2Rraw1,4Rraw2+6Rraw1,
                              8Rraw3+36Rraw2+3Rraw1).  (17)

The numerator exp(-is)-exp(is) has all derivatives bounded by2; the constant -I contributes no positive-order derivative. The chain rule with q',q'',q''' gives (17). Both momenta remain in that real core band.

Replace the order0 entries of Cs,W by e,w to form Cr,Wr; their other entries are unchanged. Put

    Fjet=Wr star P star Cr star P,
    Kjet=(den^-1, den^-2 Fjet1,
           2den^-3 Fjet1^2+den^-2 Fjet2,
           6den^-4 Fjet1^3+6den^-3 Fjet1 Fjet2+den^-2 Fjet3),
    Ujet=Kjet star (Wr star P star Cs+W),
    Vjet=Cs+Cr star P star Ujet,
    Sbound=Cr+Cs star P star Ujet+Wr+W star P star Vjet.

These are exactly the ordered feedback maps of cf080 with the product rule extended through order three. Fjet0=ew, and the inverse margin den supplies every denominator. Set Sjet=(1,Sbound1,Sbound2,Sbound3), using exact flux unitarity only for order0, and finally

    Mjet=R star (1,57,57^2,57^3) star Sjet star D.       (18)

Its entries supply M0,...,M3 in (12); projection P_a and injection V_0 have norm1. Equations (16)--(18) prove finite real third-derivative ceilings for the entire demodulated ordinary outgoing map, with its correct two threshold conversions. No inference that unitarity prevents a complex pole is made. As den tends to zero these sufficient coefficients can diverge, as they should. At the finite family's h=eta^2=zeta=r=epsilon/10^6, every entry remains bounded as epsilon tends to zero, since all displayed real margins stay bounded away from zero. This last observation concerns only these coefficients, not a complete resource exponent.

## 7. Integrated outgoing contribution and restricted substitution

The fixed-diagonal cut perturbation of finite532866 has norm at most sqrt(2)j on its three radial contact levels, acting identically on the logical fibers. Combining all contact levels costs sqrt(3); using a conservative sum over the two record channels costs2. Since (15) applies on each level to the whole port vector, for any subinterval of [0,T] the outgoing Duhamel contribution obeys

    E_boundary,out <=2sqrt(6) jT rho B_net/(h^2 ell^2)
                    <5 rho B_net/(h^2 ell).             (19)

This includes wrong outgoing I/F ports and both record channels, not just the ideal record1 target. The common physical phase is unchanged. Matrix bounds tensor with arbitrary passive references without multiplicity. The cut geometry and norm are the frozen finite source's actual hopping-only perturbation; no diagonal or record threshold is altered here.

Consequently the specific estimate 5 A_o/ell in finite532866 may be supplemented by the smaller of itself and (19), provided this new third-derivative derivation and pole argument receive their own check. The unchanged incoming contribution is still 2 A_i/u; the full boundary allowance can be bounded by

    2 A_i/u + min{5 A_o/ell, 5rho B_net/(h^2 ell)}.      (20)

No claim about changing the twelve simultaneous allocations, late internal amplitudes, branch truncation or runtime follows without rebuilding those budgets. In particular removing the outgoing rho^-3 ceiling does not remove that power from a different incoming estimate. Another author is examining that distinct incoming problem; no result from it is used here.

## 8. Failed shortcuts, evidence and review status

The initially suggested analytic phase inverse is not needed and has not been established for the full network. No holomorphic radius, pole displacement after that inverse, or analytic continuation of the nonanalytic cutoff is asserted. Simply applying the old two-real-derivative bound to F would retain the resonance cost and would not prove (19). An arbitrary C2 cutoff need not have an integrable third derivative, so the current route explicitly uses the actual specified quintic. The positive-frequency sign in (5) and the positive boundary phase gap are essential; reversing either sign would invalidate the uniform v integration. This is a directional bound, not a global bound on every launch component.

N=/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934. Exact changed premises:

- common_product_biased_record_packet/PROPOSAL.md: cf080f0dae5bf71021fe91533fc97355ceaaadb5db6f3d3145e3a911c8f3ffcf. Full relevant argument reread and hash refreshed here; the truncated combined read was repaired by a separate complete ending read. Its prior distinct check315a618f389598fe8443a8ed3cdf8c39180b65ba223c4de2a359be4e218ea916 was fully read in the earlier preparation task and retains its infinite-packet scope, not these new third derivatives.
- common_product_biased_record_finite_seed/PROPOSAL.md: 532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123. Full argument reread across the combined output and a separate opening read repairing truncation; hash refreshed. Only its exact outgoing amplitude, actual cutoff and cut interface are used. Its existing twelve-budget prescription is not edited.
- common_product_endpoint_launch/PROPOSAL.md: fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4; common_product_launch_derivative_bounds/PROPOSAL.md:378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8. Their complete exact F/source arguments were read in the preceding geometric task and reused unchanged. The new real-axis substitution is shown directly in (4).

ROOT proposed exploiting the outgoing lower pole and asked for verified matrix/normalization hypotheses. This author wrote the packet and several ancestors and has full source/design exposure. The Laplace representation, weak third-derivative cutoff use, complete network third-jet certificate and integrated estimate are new author calculations requiring a distinct check. They are not independent validation of the reused network. All sources remain frozen.

Only this proposal was created. No scientific executable, numerical sweep, contour computation, delegation, W/Git/checkpoint/axiom/editable-prompt/model change or publication occurred. No native realization, preparation mechanism, finite runtime improvement, old processor transfer, normalized rare-branch guarantee or permanent halt is claimed.
