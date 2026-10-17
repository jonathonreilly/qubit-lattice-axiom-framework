# Slow-lead scalar reference: exact transmission measure and two directional bounds

Status: new authored scalar-reference derivation, requiring a distinct check. It does not identify the actual coefficient, seed mass, feedback, local recovery or runtime of the modified attached apparatus. Fix kappa=1e-8, g=1e-6 and .0027<j<.003. The first slow site is m=0, a NEW vertex distinct from the old gate port. The physical slow halfline is m>=0 throughout this note.

For the transmitted hard-band reference defined below, its full-lattice mass is exactly p_s=p0-R, where R is the reflected reference mass and

    0<=R<4.356e-11,
    1-1.100044e-6<p_s<=p0<=1.                       (1)

For its normalized outgoing packet b_out and normalized conjugate incoming packet b_in, the proposed conclusions are

    ||b_out(t)||_(m<=-1)<1e-6, for every t>=1e15,
    ||b_in(t)||_(m>=0)<.0016, for every t>=0.        (2)

Thus the normalized outgoing squared norm on m>=0 exceeds 1-1e-12 at the displayed sufficient onset. Its unnormalized counterpart has full mass p_s and right-halfline mass exceeding p_s(1-1e-12). These are reference bounds only, with no actual-device theorem inferred.

## Sources, exposure and unchanged definitions

Read the complete checked scalar interface `../same_carrier_slow_lead/PROPOSAL.md`, SHA256 `a9795085bd36acbdaee9de8e46709f1a61c5065d5c6f0dadc37f8bb151f962e4`, and its review `ecec86951cdb2f36011e196fe8266bffec29f55a6d0ec8f67e4bfe5684a578fb`. I authored that review, not the interface; this new derivation requires its own checker.

Reuse the previously completely read actual attached comparator definition in `record_attached_outgoing_profile/PROPOSAL.md`, SHA256 `52bd25106f95d06b1d06b741f1183a492d169e5a4c6e85aa40ebca88404d1788`, and its check `44c697a5169b5cdb665e44c8b62787c2164f72537e082523e492ad535a29f026`. Only the scalar reference formula and unnormalized moment are used, not actual attached error conclusions. The exact reference measure and hard-band tail are pinned by `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae` and wider-band source `d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2`.

The earlier incoming source `1def426f0919789b6a1a8c4048756c3a95a6a2b9ed4b5223c90e0ca321db8bf7` and outgoing onset source `3a554c4edf266a8e53cd43b57bb03c280dcf601b4eb3da502fa6a3d33bfc5fe0` motivate contour methods; their time or spatial constants are not transferred. I authored the latter and reviewed the former. Root supplied the transmission/Jacobian algebra suggestion and candidate shallow depth. Branch, denominator, normalization and spatial bounds below are new exposed author work.

Applicable unchanged workflow is reused. No numerical sweep, scientific execution, dynamics run, delegation, W/Git, model, prompt, audit or publication change occurred. Only this proposal was written; no editable prompt file changed.

Put h_q=4e-6, q in I_q=pi/2+[-h_q,h_q], delta=-2j cos q, E=2j+delta, gamma=kappa^2/j and

    D(q)=delta+gamma exp(iq),
    F(q)=kappa E'_q zeta exp(i61q+i172k_old(q))
                                      /(sqrt(2pi)jD(q)),
    k_old(q)=2 asin(a sin(q/2)), a=sqrt(j/J)<1/3.

The fixed zeta is unchanged and unimodular. It is not fitted anew. On the full real old lead 0<q<pi, this explicit scalar F has mass one; on I_q it has mass p0>1-1.1e-6 and unnormalized second moment M2<1.9e-17. The extra attachment phase has already been included in the 61q carrier.

## 1. Exact slow coefficient and lost reflection

Let epsilon=g/j, and relate the slow momentum k by cos q=epsilon cos k. Define

    q(k)=pi/2-asin(epsilon cos k),
    H=asin((j/g)sin h_q)<.01201,
    I_k=[pi/2-H,pi/2+H].

This maps I_k bijectively to I_q, with dq/dk=g sin k/(j sin q)>0. The exact interface transmission gives

    t_flux=exp(i(q+k)/2)*sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_flux(q(k)) F(q(k)) sqrt(dq/dk)
          =sqrt(g/j)*sin k/sin((q+k)/2)
                            *exp(i(q+k)/2) F(q(k)). (3)

Equivalently F_s=t F dq/dk, with t the physical amplitude at first slow site m=0. Equation (3), including its phase, therefore matches that site convention without identifying it with the old port. The expression without square roots of sine ratios supplies the analytic continuation used below.

The exact slow phase is

    Phi_s(k)=61.5 q(k)+.5 k+172k_old(q(k))+arg zeta.

It is not 61k. Flux conservation and the Jacobian give

    p_s=integral_Ik |F_s|^2 dk
       =integral_Iq (1-|r(q)|^2)|F(q)|^2 dq=p0-R.

The checked reference-only reflection norm <6.6e-6 yields R<(6.6e-6)^2=4.356e-11, proving (1). No actual seed mass has been substituted. This remains an unnormalized transmitted reference; multiplying by 1/sqrt(p_s) is an explicitly separate normalization.

Define the full integer-lattice packets

    b_out(t,m)=1/sqrt(2pi p_s) integral_Ik
                     F_s(k)exp(ikm-itE_s(k))dk,
    b_in(t,m)=1/sqrt(2pi p_s) integral_Ik
              conjugate(F_s(k))exp(-ikm-itE_s(k))dk,
    E_s(k)=2j-2g cos k.

Fourier isometry gives full-lattice norm one for each. The physical output is m>=0; old gate coordinates are excluded. Common old-energy phases and the common physical scalar have unit modulus and do not change these scalar norms. No factorization through an actual interacting Hamiltonian is asserted.

## 2. Outgoing shallow strip: branches and pole margin

Take h_s=kappa^2/(4jg), so 8.333e-9<h_s<9.26e-9, and z=x-iy with x in I_k, 0<=y<=h_s. The principal q(z)=pi/2-asin(epsilon cos z) is analytic. On this rectangle |epsilon cos z|<5e-6, |sin z|<1.000001 and

    q'(z)=epsilon sin z/sqrt(1-epsilon^2 cos^2 z),
    |q'|<.000371.

The old scalar k_old(q) branch remains near the original center and |k_old'|<.25 by the same explicit arcsin derivative estimate on this tiny image. Consequently |Phi_s'|<.5+104.5*.000371<.55. Its outgoing growth is at most exp(.55y), which is retained below. The slow dispersion obeys

    Im E_s(x-iy)=-2g sin x sinh y<=-v_s y,
    v_s=1.99e-6,

because H<.01201. This slow velocity is not the old .0053 velocity.

For a direct pole margin put

    S(z)=sqrt(1-epsilon^2 cos^2 z)=sin q(z),
    A=2g-gamma epsilon>0,
    D_s(z)=D(q(z))=-A cos z+i gamma S(z).

The real S(x)>.99999999, since |epsilon cos x|<5e-6. On the rectangle |S'(z)|<2e-7, so |S(z)-S(x)|<2e-15. Write

    D_tilde=-A cos x cosh y
                +i[gamma S(x)-A sin x sinh y].

Since A<=2g, 2g h_s=gamma/2 and sinh h_s/h_s<1.00000001, the subtracted imaginary term is less than .500001 times gamma S(x). Its remaining factor is therefore >.499. The real part has magnitude at least A|cos x|. Hence

    |D_tilde|>=.499 sqrt(A^2 cos^2 x+gamma^2 S(x)^2)
              =.499|D_s(x)|.

The difference from D_s(z) has modulus <2e-15 gamma. Since |D_s(x)|>=.999999 gamma, this gives the convenient uniform bound

    |D_s(x-iy)|>.49|D_s(x)|.                       (4)

This proves a pole-free strip throughout the rectangle, including the center and both cutoff sides. It does not assume the old q-strip depth transfers unchanged.

## 3. Outgoing L2 bottom and both sides

Apart from its phase and denominator, the explicit numerator in (3) is

    2kappa sqrt(epsilon) S(z)sin z/
                               [sqrt(2pi)sin((q(z)+z)/2)].

On this shallow rectangle, ratios to the corresponding nonzero real numerator factors are each bounded by 1.000001: S by its derivative bound, sin z since sin x>.9999, and the sine denominator by its derivative and real margin >.9999. The phase ratio is at most exp(.55h_s)<1.000001. With (4) this implies

    ||F_s(.-ih_s)||_L2(Ik)<2.05 sqrt(p_s).

For the horizontal contour contribution on m=-l, l>=1, multiply the integer Fourier coefficients of the shifted function by exp(-l h_s). This is a contraction on the selected negative integers. Parseval for that shifted coefficient and temporal decay therefore give bottom norm

    <2.1 exp(-v_s t h_s).                          (5)

No peak-times-bandwidth estimate is used; the phase growth is already paid in the 2.05 comparison. The hard cutoff itself is not analytically continued.

For each cutoff x=pi/2±H, the real energy distance is d=2j sin h_q>2.15e-8. The real part of D_tilde has magnitude (1-gamma/(2j))d cosh y, and the tiny gamma(S(z)-S(x)) correction leaves |D_s|>2.14e-8. Using sqrt(epsilon)<.02, |S|,|sin z|<1.000001, sqrt(2pi)>2.5, the sine denominator >.9999 and p_s>1-1.100044e-6 gives

    |F_s(x-iy)|/sqrt(p_s)<.008 exp(.55y).

Each side for m=-l consequently has an integral with decay exp[-(v_s t-.55+l)y]. Paying both sides and the outer Fourier factor <.4 gives amplitude <=.0064/(s_t+l), where s_t=v_s t-.55. For s_t>=1,

    sum_(l>=1)(s_t+l)^-2<=s_t^-1,
    ||both sides||<.01/sqrt(s_t).

The looser .01 coefficient also covers including l=0 by the bound s_t^-2+s_t^-1<=2/s_t. Thus the desired physical complement m<=-1 has the rigorous curve

    ||b_out(t)||_(m<=-1)
       <2.1 exp(-v_s t h_s)+.01/sqrt(v_s t-.55),
    v_s t-.55>=1.                                (6)

Choose just T=1e15. Then v_s T h_s>16 and v_s T-.55>44000^2. The elementary inequalities e>8/3 and (8/3)^5>130 give e^16>130^3*(8/3)>4e6. Therefore the right side of (6) is below 2.1/(4e6)+.01/44000<1e-6. Both terms decrease for t>=T. This proves the outgoing assertion in (2) from new scalar bounds, not by importing an old actual onset.

## 4. Incoming all-time bound via a scalar-only full slow-band extension

Extend exactly (3) to 0<k<pi using q(k)=pi/2-asin(epsilon cos k). This covers an old momentum subinterval around pi/2 containing I_q. All its real phase factors remain unimodular, and |t_flux|<=1. Consequently the auxiliary full-slow-band coefficient has mass at most one, while its part outside I_k has mass at most

    integral_(q outside Iq)|F(q)|^2 dq=1-p0<1.1e-6. (7)

This is a scalar extension only, not continuation of actual calibration or device response. No interacting kernel is used away from the certified band.

For this scalar extension use the rectangle 0<=Re z<=pi, -1<=Im z<=0. Since epsilon<1/2700 and cosh1<1.55, |epsilon cos z|<.000575. Thus q(z)=pi/2-asin(epsilon cos z) is analytic, with |q-pi/2|<.001 and Re q in (pi/2-.001,pi/2+.001). Moreover Im cos(x-iy)=sin x sinh y>=0, so Im q<=0 by the principal-arcsin sign property. The old k_old(q) branch is likewise analytic with Im k_old<=0: its argument has imaginary part a cos(Re q/2)sinh(Im q/2)<=0 and remains inside the unit disk. Finally

    |sin((q(z)+z)/2)|>=sin(pi/4-.0005)>.7.

The lower-halfplane continuation of the CONJUGATE coefficient uses Dbar(q)=delta+gamma exp(-iq) and phase exp(-iPhi_s). The phase modulus is at most exp(-y/2), since the q and k_old imaginary parts are nonpositive. The temporal multiplier has modulus <=1 for every t>=0, including t=0. At both vertical sides the energy is real.

There are no Dbar poles in the rectangle. To see this, write q=alpha-i beta with beta>=0 and alpha near pi/2. Then

    Im Dbar=-sin alpha[2j sinh beta+gamma exp(-beta)]<0.

At the bottom a stronger modulus bound follows from delta=-2g cos z:

    |Dbar|>=2g|cos(x-i)|-gamma|exp(-iq)|
             >=2g sinh1-gamma>2g.

Here |exp(-iq)|<=1, sinh1>1.1 and gamma/g<4e-8 suffice. The conjugate numerator with its phase removed obeys |S|<1.001, |sin z|<=cosh1<1.55 and sine denominator >.7. Thus its full coefficient modulus on the bottom is less than

    [2*1.001*1.55/(2.5*.7*2)] kappa/sqrt(jg)
       <kappa/sqrt(jg).

The outer Fourier factor, interval length and geometric sequence for m>=0 give bottom norm less than 1.6 kappa/sqrt(jg): use pi/sqrt(2pi)<1.3 and (1-exp(-2))^(-1/2)<1.2. Dropping the additional exp(-1/2) phase decay is safe.

At a vertical edge q is real, so S=sin q<=1 and the only phase decay needed is exp(-y/2). The real part of Dbar has modulus 2g cosh y*(1-gamma/(2j))>1.99g cosh y. Therefore the coefficient excluding its phase is bounded by

    [2/(2.5*.7*1.99)] kappa/sqrt(jg)*tanh y
       <kappa/sqrt(jg)*y.

Paying both sides and outer Fourier normalization gives, for m>=0, amplitude at most .8 kappa/sqrt(jg) times integral_0^1 y exp(-(m+.5)y)dy. For m=0 bound this integral by 1/2; for m>=1 bound it by 1/(m+.5)^2<=1/m^2. Since sum_(m>=1)m^-4<=1+1/3, the squared sum of these integral bounds is at most 1/4+4/3=19/12. Hence the complete side norm is less than 1.1 kappa/sqrt(jg).

The unnormalized auxiliary incoming halfline thus has norm below 2.7 kappa/sqrt(jg) for every t>=0. Since sqrt(jg)>5e-5, this is below .00054. Fourier isometry and halfline contraction charge the hard-cutoff tail in (7) by sqrt(1.1e-6)<.001049. Finally p_s>1-1.100044e-6 gives 1/sqrt(p_s)<1.000001. Therefore

    ||b_in(t)||_(m>=0)
       <(.00054+.001049)*1.000001<.0016, t>=0.      (8)

Both vertical sides, m=0, transmission factors, Jacobian and sharp-cutoff loss are included. The argument does not import the old incoming .00105 constant or replace the slow phase by its modulus before continuation.

## Scope and check targets

This packet has a norm deficit R from single-interface reference reflection in addition to the old hard-band deficit; it is not assigned mass p0 without that correction. Its unnormalized directional bounds are no larger than the normalized ones. A later common old/reference comparator may tensor these scalar packets with the literal operation and old aging, retaining all physical phases. Actual wrong-window matrix coefficients, repeated source/gate reflections, closed channels, finite local recovery, seed mass, spectral synthesis and any storage theorem remain to be proved for the changed Hamiltonian.

The independent check should reconstruct (3), the shallow-strip denominator comparison (4), shifted Parseval with the physical complement m<=-1, both outgoing cutoff sides, and the separate full-slow-band conjugate rectangle including its m=0 side estimate. Neither scalar auxiliary extension enlarges the original source-calibration domain. No optimized onset, permanent latch, reset, reuse or actual modified-device transfer is claimed.
