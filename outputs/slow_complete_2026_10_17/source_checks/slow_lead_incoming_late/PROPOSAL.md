# Late incoming slow reference: centered hard-band contour

Status: authored conditional scalar derivation requiring a distinct check. A depth-one lower contour on the ORIGINAL centered hard slow band gives a quantitative incoming bound with no auxiliary full-band subtraction. At the current fixed parameters the raw scalar incoming norm is<2.2e-7 for every t>=1e15. The already checked actual coefficient interface then gives actual incoming norm<4.122e-5. This supplies neither a complete-state onset by itself nor a complex strip for the interacting apparatus.

## Domain, sources and exposure

Fix the original supplied j,J and calibration phase, with .0027<j<.003. Use the uniform-reference domain

    0<kappa<=1e-8, 0<g<=1e-6, 0<h<=4e-6,
    gamma=kappa^2/j, d=2j sin h,
    H=d/gamma>=100, L=g/gamma>=100, H/L<=.024.

Here H is a dimensionless band ratio, not the Hamiltonian. Set epsilon=g/j<1/2700 and K_h=asin(d/(2g))<.012001. The physical first slow site is m=0, distinct from the old finite gate port. The real slow interval is I_k=[pi/2-K_h,pi/2+K_h].

Read/reused full uniform scalar source5f2026dc3f63a757f13cf58bc468f05de10cfca9f04fda9c6615b816c9b94907 and its check338e554834f994741982842c555589db5e62dba9ad121233989ce60068f26c93; fixed scalar sourcee6a9706d497d7c6abb5590d2baae0940efdf628e81101f5f4cfd91885e93ea8e/rootcheck6fb89d66d0a79e5c66c6dabd00c030ddb603308485f60c857b95f0e791b1a5f5. The actual outgoing/coefficient interface is fixed source6f9ebabb3405b124e52582c313c342889c9146e0040306d0ec7b72e8e8371b17/checkaeb147ff7d430562ff27ab7cbfc276e8066b48199ed6c9a163ee281357ecf528 or uniform endpointc8d2b7681f2059ec986bc3e41bf0a3eea8fefbc43c86addc17539b2f258bb887/checkf3e449109bc4bac6b4e4692d0db5f40c4d282d663b32f3b89a7ff1065ded28e0. Their unchanged complete-input and two-lip scope is carried by fixed synthesisab552c4002af8388d5e223cf81390cdcbaa74685affda5c263048cbea73cdb2a/checkc6d82eaf1e4789f6b4f6b6f5c0fe97a0201fce1dbe7e99b294995d76e516a628 and uniform synthesis8cd26edcb7941d8254494480455d17c137652ec779e37e78901de5a04e71ac9e/checkb873ac37d8a327f27491f36e80dfe5e8aeef7eb0d7b405bba6b70a6ffb9e71a7. These full arguments/checks were read in the coherent prior tasks; the exact scalar continuation passages and source identities were refreshed here.

Root proposed lowering the centered hard-band conjugate coefficient rather than extending first to(0,pi). I authored the fixed reference and synthesis and checked the uniform reference; this is exposed author work, not independent recertification. The depth-one denominator comparison below is newly derived here. No numerical computation, sweep, solver, delegation, W/Git/PR/checkpoint/publication, model or prompt change occurred. This proposal is the sole deliverable. Original exact coefficient/phase and source premises remain conditional.

## 1. Exact coefficient, normalization and phases

The real matching map and old converter branch are

    q(k)=pi/2-asin(epsilon cos k),
    k_old(q)=2asin(sqrt(j/J) sin(q/2)).

Write E_s(k)=2j-2g cos k and D(q)=-2j cos q+gamma exp(iq). The coefficient at firstslow m=0 is exactly

    Fs(k)=2kappa sqrt(epsilon) sin q(k) sin k
       *zeta exp[i61.5q(k)+i k/2+i172k_old(q(k))]
       /[sqrt(2pi) sin((q(k)+k)/2) D(q(k))].            (1)

This is tf sqrt(dq/dk)F(q), with tf the unit-flux interface transmission. It is not the physical transmission amplitude multiplied by an unchanged momentum measure. The same fixed unimodular zeta and phase61.5q+.5k+172k_old are retained. No61-site translation in the slow coordinate is made.

Let ps=integral_Ik|Fs|^2dk=p0-R, with R the actual scalar reflected reference mass. The checked normalization gives ps>1-.68/H-.043H/L^2>.9931. Define the normalized incoming sequence on the full integer lattice by

    b_in(t,m)=[2pi ps]^-1/2 integral_Ik
                     conjugate(Fs(k)) exp[-ikm-itE_s(k)] dk.

Its full-lattice norm is one. The requested physical restriction is m>=0, INCLUDING m=0. The raw packet is sqrt(ps)b_in. All bounds below preserve this distinction.

## 2. Analytic continuation on the original hard band

Use the rectangle z=x-iy with x in I_k and0<=y<=1. This is a scalar-reference continuation only. Since |epsilon cos z|<=epsilon cosh1<.000575, the principal q(z) is analytic and |q-pi/2|<.001. Because Im cos(x-iy)=sin x sinh y>=0, its principal-arcsin image gives Im q<=0. The old k_old branch remains analytic: its argument has modulus<1, positive real neighborhood near the old carrier and nonpositive imaginary part. Thus Im k_old<=0 as well.

Set S(z)=sqrt(1-epsilon^2 cos^2 z)=sin q(z), using the positive real branch on I_k. Its real part is positive throughout the rectangle. The sine denominator in(1) has

    |sin((q(z)+z)/2)|
       >=cos((.012001+.001)/2)>.9999.                  (2)

Indeed the real part of its argument stays within(.012001+.001)/2 of pi/2; an imaginary part cannot decrease the squared sine modulus below sin^2 of its real part.

The analytic continuation of conjugate(Fs) uses conjugate(zeta), negative phase and

    Dbar_s(z)=Dbar(q(z))=-A cos z-i gamma S(z),
    A=2g-gamma epsilon=2g(1-gamma/(2j))>0.             (3)

It does NOT use the outgoing D_s=-A cos z+i gamma S. The negative phase has modulus

    |exp[-i61.5q-i z/2-i172k_old]|<=exp(-y/2).         (4)

The temporal factor obeys

    Im E_s(x-iy)=-2g sin x sinh y<=-1.99g y,
    |exp[-itE_s(x-iy)]|<=exp(-1.99g t y), t>=0.        (5)

These estimates hold on BOTH cutoff verticals as well as the bottom. Unlike verticals at0 and pi of an auxiliary full interval, the present verticals have sin x near1 and supply temporal damping.

## 3. Exact lower-contour denominator improvement

Write S=u+iv with u>0. Since x is in the centered interval, cos(2x)<0. Therefore

    Re(S(z)^2)=1-epsilon^2 cos^2 x
                         -epsilon^2 cos(2x)sinh^2 y
                >=S(x)^2.

As u^2=Re(S^2)+v^2, this proves u>=S(x). Taking the imaginary part of S^2 gives

    v=-epsilon^2 cos x sin x cosh y sinh y/u.

Substitute into(3):

    Re Dbar_s=-cos x cosh y
                 [A+gamma epsilon^2 sin x sinh y/u],
    Im Dbar_s=-A sin x sinh y-gamma u.

All bracketed quantities are nonnegative, with A,u positive. Thus neither component cancels its real-line counterpart, and

    |Dbar_s(x-iy)|>=|Dbar_s(x)|, 0<=y<=1.              (6)

In particular there are no poles anywhere in this rectangle. On either vertical cutoff, |2g cos x|=d, and the real part supplies the stronger bound

    |Dbar_s(x-iy)|
       >=(1-gamma/(2j))d cosh y>.9999d cosh y.         (7)

This is a genuine modulus comparison across the whole rectangle, not an assumed actual-source strip or center-only pole argument. Its sign is special to the conjugate incoming denominator. The outgoing denominator has the opposite imaginary sign and may have a lower pole; this deep deformation is not valid for it by the same proof.

## 4. Bottom: an L2 estimate on the shifted original interval

Let C(z) denote the analytic conjugate coefficient from(1). Relative to its real-line magnitude, its phase-free numerator changes by at most

    |S(z)|/S(x) <1.001/.99999999,
    |sin(x-iy)|/sin x <=cosh1/.9999<1.55/.9999,
    sin((q(x)+x)/2)/|sin((q(z)+z)/2)| <1/.9999.

The product is<1.56. Equation(6) does not enlarge the inverse denominator, and the phase in(4) is contractive. Hence

    |C(x-i)|<1.6 |Fs(x)|,
    ||C(.-i)||_L2(Ik)<1.6 sqrt(ps).                    (8)

Extend the bottom integrand by zero to a2pi interval and apply Parseval. For the physical m>=0 its extra spatial factor is exp(-m), hence contractive, including m=0. Equation(5) at depth1 yields normalized bottom contribution

    <1.6 exp(-1.99g t).                                (9)

No peak-times-width replacement is used. The hard cutoff indicator itself is not analytically continued; its two edges are handled next.

## 5. Both hard-cutoff sides, including m=0

On either side, |S|<1.001, |sin(x-iy)|<=cosh y and(7) cancels the latter cosh factor. By(2), sqrt(2pi)>2.5 and gamma/j<1.4e-11, the coefficient without its phase satisfies

    |C(x-iy)|/sqrt(ps)
       <=[2*1.001/(2.5*.9999*.9999)]
                         kappa sqrt(epsilon)/(d sqrt(ps))
       <sqrt(L)/(H sqrt(ps)).                          (10)

The last identity uses kappa sqrt(g/j)/d=sqrt(L)/H. The negative phase contributes exp(-y/2). Paying BOTH sides and the outer Fourier factor1/sqrt(2pi)<.4 gives, at each m>=0,

    |side amplitude|
       <=.8 sqrt(L)/(H sqrt(ps))
                integral_0^1 exp[-(m+.5+1.99g t)y]dy
       <=.8 sqrt(L)/(H sqrt(ps)(m+s)),
    s=.5+1.99g t.                                     (11)

For s>0,

    sum_(m>=0)(m+s)^-2<=s^-2+s^-1.

The s^-2 term explicitly pays m=0. Let sigma=gamma t and u_t=L sigma=g t. For u_t>=1, s>=1.99u_t and therefore

    u_t(s^-1+s^-2)
       <=1/1.99+1/(1.99^2 u_t)
       <=1/1.99+1/1.99^2.

Since .8^2(1/1.99+1/1.99^2)<.7^2, the normalized side norm is

    <.7/[H sqrt(ps sigma)], L sigma>=1.                (12)

The bound would be wrong if the m=0 term were silently dropped. No endpoint oscillation or cancellation between the two sides is assumed.

## 6. Quantitative late incoming result

Adding(9) and(12) and using the full normalized norm ceiling gives

    ||b_in(t)||_(m>=0)
      <=min{1,1.6 exp(-1.99L sigma)
                            +.7/[H sqrt(ps sigma)]},
    sigma=gamma t, L sigma>=1.                         (13)

Equivalently the RAW reference incoming norm is at most

    Jref_late(t)=min{sqrt(ps),
           1.6sqrt(ps)exp(-1.99g t)+.7/(H sqrt(gamma t))}.
                                                               (14)

For earlier times use the existing all-time incoming bound or the norm ceiling. One can take the minimum with that previous bound at any time where(14) applies. The depth-one proof is uniform over the stated positive domain, and has no new parameter restriction. The time dependence is explicit; decreasing gamma still changes the physical waiting time required for a given sigma.

This directly deforms the centered hard-band coefficient. There is NO sqrt(1-p0) auxiliary-to-hard-band penalty. Both hard edges are instead paid by their temporally damped side integrals. The reflected normalization deficit remains in ps and is not removed. The phase, flux factor and momentum Jacobian have not been changed to obtain the rate.

At the current fixed point, t>=1e15 gives g t>=1e9, gamma t>100/3 and H=2j^2 sin(4e-6)/1e-16>580000. Thus the second term in(14) is below .7/(580000*5.7)<2.12e-7. The exponential term is<1e-12 (already the weaker exponent42 and exp42>2^42 suffice). Therefore

    raw scalar incoming norm <2.2e-7, t>=1e15.          (15)

This is an elementary sufficient enclosure, not a numerical Fourier integration or optimized constant.

## 7. Transfer to actual incoming and complete-state implications

The checked physical coefficient interface gives norm error<=Eout in EACH record-X sector for complete prepared input on the common physical union, including wrong-window rows. Fixed-basis conjugation preserves that coefficient bound for the incoming term. Fourier isometry and physical-halfline restriction therefore give

    ||incoming_actual(t)||<=Jref_late(t)+Eout,          (16)

with the same common scalar, physical output-window energy phases, literal old W* for the ideal incoming comparator, all old inputs and arbitrary passive references. Different ideal old channels are orthogonal; sector errors average in orthogonal record-X ranges. No extra scalar-column or record factor is inserted. The actual coefficients themselves have not been analytically continued; only their real-band L2 difference from the scalar reference is used.

At the fixed point Eout<4.1e-5, so(15) gives actual incoming norm<4.122e-5 for every t>=1e15. This replaces the former all-time actual ceiling .001641 at late times. It is a quantitative bound for the represented incoming contribution, not the complete actual state or its omitted spectral remainder.

In a future complete-state bound, use(16) alongside the single actual omitted amplitude, represented full emitter, finite/closed background and outgoing coefficient error. In particular this route costs up to TWO copies of Eout: one outgoing and one incoming comparison. It does not itself attain the sharper asymptotic floor epsilon_sp+Eout. Approaching that floor requires either actual incoming decay beyond its coefficient-error ceiling or a sharper comparison. The separate background derivative/inverse obligation in slow_lead_complete_onset_frontier/PROPOSAL.md (c590e093e7a4ca6abc1e147414f5ee5b08e725fa1a881b266fae7271b56e0d46) remains unresolved; no complete onset is asserted by combining unproved derivative assumptions here.

The result addresses only a supplied mathematical reference and its already checked actual coefficient comparison. It establishes no native preparation, coefficient tolerance, observation protocol, repeated measurement, irreversible latch, permanent halt or practical-time claim. A distinct checker should inspect the signs in(3), the exact componentwise denominator comparison(6), both cutoff factors, the m=0 sequence sum and the full-input transfer(16) before use.
