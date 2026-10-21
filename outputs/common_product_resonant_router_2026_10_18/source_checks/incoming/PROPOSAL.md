# Resonance-resolved incoming boundary integral

New bounded author derivation requiring distinct review. For the ACTUAL normalized compact-band source profile, at the three incoming cut offsets d=0,-1,-2, the integrated amplitude admits an exponential resonance term plus a cutoff remainder proportional to rho/(h^2 u0). This replaces the generic rho^-3/u0 incoming estimate in the specified scalar interface. It does not replace outgoing, internal, seed-matching or other finite-device costs, and establishes no new end-to-end resource exponent.

## 1. Exact quantity and compatibility assumptions

Use the exact phase-preserving source amplitude from fb72/378086,

    F(k)=-i sqrt(2/pi)rho exp(ik)
                     /[(2-rho^2)cot k-i rho^2], 0<k<pi.

Take the same real C2 quintic cutoff as finite532866: plateau |k-pi/2|<=h/2, transition width h/4, zero beyond3h/4, 0<=chi<=1, with |chi'|<=8/h and |chi''|<=100/h^2. Impose

    0<h<=10^-3, 0<rho^2<=h/16,
    p=||chi F||_2^2, g=chi F/sqrt(p).                    (1)

The checked physical source measure has norm one on the upper semicircle. Its hard-band bound gives P_omit<=3rho^2/h<=3/16 and hence p>=13/16>1/2. No fitted normalization is used. The finite532866 source policy satisfies (1), since rho<=epsilon sqrt(h)/1024 and 0<epsilon<=1. The present result also covers other profiles satisfying this same cutoff contract and compatibility.

For dimensionless time u=jt define exactly

    a_d(u)=1/sqrt(2pi) integral_0^pi
       exp[idk-i2u(1-cos k)]g(k)dk,
    d in {0,-1,-2}.                                     (2)

This is the incoming component at n=ell,ell+1,ell+2 of the packet whose incoming phase is (ell-n)k-tE(k). The integral uses g, not conjugate(g): reversal of the standalone lead coordinate already fixed that convention in the finite source. No full-circle replacement is made.

## 2. Exact energy-coordinate cancellation and residue

Set

    delta=rho^2, a=sqrt(1-delta), A=2-delta,
    lambda=delta/(2a), x=cos k, s(x)=sqrt(1-x^2).

On the physical interval, s=sin k>0. Put theta(x)=chi(arccos x), extended by zero off its compact support, and

    t_0(x)=x+i s(x), t_(-1)(x)=1, t_(-2)(x)=x-i s(x).

The Jacobian dk=-dx/s removes precisely the sin k in the original numerator. Reversing the integration limits, including the Fourier normalization, gives

    a_d(u)=rho exp(-i2u)/sqrt(p)
       integral_R exp(i2ux) theta(x)
          [-i t_d(x)/(pi(Ax-i delta s(x)))] dx.          (3)

Only the compact physical support of theta contributes. In particular x is a one-to-one energy coordinate on the ORIGINAL upper semicircle.

Since A^2-delta^2=4a^2, rationalization gives denominator 4a^2(x^2+lambda^2). Define s_lambda=sqrt(1+lambda^2)=A/(2a), so delta s_lambda=A lambda. Using

    s(x)-s_lambda=-(x^2+lambda^2)/(s(x)+s_lambda)

gives the exact cancellation

    Ax+i delta s(x)
      =(x+i lambda)[A-i delta(x-i lambda)/(s(x)+s_lambda)].

Thus the physical amplitude density in brackets in (3) is

    b_d(x)/(x-i lambda),
    b_d(z)=(-i)/(4pi a^2) t_d(z)
               [A-i delta(z-i lambda)/(s(z)+s_lambda)]. (4)

The pole at -i lambda has been removed analytically, not dropped by approximation. The remaining upper-energy-plane pole at +i lambda is appropriate for exp(+i2ux) at positive u. This is equivalent to a lower pole in y=-2x with phase exp(-iuy); the signs depend on this explicit energy-coordinate choice.

For complex z with |z|<1/2, take the analytic square-root branch s(z)=sqrt(1-z^2) having s(0)=1. On that disk Re s(z)>=sqrt(3/4), |s(z)|<=sqrt(5/4), and s_lambda>=1. Hence s(z)+s_lambda has no zero. Conditions (1) give a>.99 and lambda<h. Formula (4) is analytic on the disk. A simple uniform bound is

    |b_d(z)|<=1, |z|<=1/2, d=0,-1,-2.                   (5)

Indeed |t_d|<2, the bracket has norm below3 (delta<=10^-3 and |z-i lambda|<.501 suffice), and 4pi a^2>11. These loose estimates cover the closed disk without approaching a branch point.

At the remaining pole,

    b_d(i lambda)=(-i A)/(4pi a^2) t_d(i lambda),
    t_0(i lambda)=i/a, t_(-1)(i lambda)=1,
    t_(-2)(i lambda)=-ia.                                (6)

Every factor and phase in these residues is retained below.

## 3. Smooth cutoff remainder with an explicit L1 second derivative

Write b_*=b_d(i lambda) and define, on a neighborhood of the real support,

    R_d(x)=[b_d(x)-b_*]/(x-i lambda).

This quotient is analytic at i lambda. For |x|<=h it has the integral representation R_d(x)=integral_0^1 b_d'(i lambda+t(x-i lambda))dt. Cauchy estimates on radius1/4 disks about those segment points are valid inside |z|<1/2 and (5) gives

    |R_d|<=4, |R_d'|<=16, |R_d''|<=128.                 (7)

For example differentiating m times under the t integral gives an extra t^m; the bound (m+1)!4^(m+1)/(m+1)=m!4^(m+1) gives (7). These constants do not grow as rho shrinks.

The transformed cutoff is one for |x|<=sin(h/2)>=h/3 and zero for |x|>=sin(3h/4)<=h. On its support |(arccos x)'|<=2 and |(arccos x)''|<=2. Therefore safe bounds are

    |theta'|<=16/h, |theta''|<=500/h^2,
    ||theta||_1<=2h, ||theta'||_1<=32,
    ||theta''||_1<=1000/h.                              (8)

In particular theta' and theta'' vanish on |x|<h/3. Compact C2 support also removes joining boundary terms when theta R_d is extended by zero. From (7)--(8),

    ||(theta R_d)''||_1
       <=4000/h+1024+256h <=5280/h.                      (9)

Define the FULL real-line remainder

    V_d(x)=theta(x)R_d(x)
                          +b_*[theta(x)-1]/(x-i lambda). (10)

This is the exact difference between the compact physical integrand and its full-line pole comparison. For W=(theta-1)/(x-i lambda),

    W''=theta''/(x-i lambda)
           -2theta'/(x-i lambda)^2
           +2(theta-1)/(x-i lambda)^3.

Using |x-i lambda|>=|x| on real x and the support gap h/3 gives respectively the integral bounds 3000/h^2, 576/h^2, and18/h^2. For the last, integrate 2|x|^-3 on |x|>=h/3; |theta-1|<=1. Since |b_*|<=1, (9) yields

    ||V_d''||_1 <=5280/h+3594/h^2 <9000/h^2.             (11)

V_d is not absolutely integrable in general: its tail is -b_*/(x-i lambda). But V_d tends to zero, V_d' tends to zero and is integrable, and V_d'' is integrable. Its oscillatory integral is consequently well-defined for u>0 by integration by parts, and TWO integrations give

    |integral_R exp(i2ux)V_d(x)dx|
                    <=9000/(4h^2 u^2).                 (12)

This step is valid despite V_d's 1/x tail; it does not incorrectly invoke absolute integrability of V_d itself.

## 4. Exact pole transform and pointwise boundary bound

The following transform is only of the rational comparison, not of the cutoff:

    integral_R exp(i2ux)/(x-i lambda)dx
                    =2pi i exp(-2lambda u), u>0.         (13)

One direct justification closes an upper semicircle of radius R>2lambda. Its arc norm is bounded by R/(R-lambda) times integral_0^pi exp(-2uR sin theta)dtheta, which tends to zero by dominated convergence for each fixed u>0. The real improper integral exists by one integration by parts. The one enclosed pole gives (13). No essential-singularity contour or analytic continuation of chi is involved.

Pointwise on the whole real line, the exact compact integrand equals b_*/(x-i lambda)+V_d(x). Thus (3),(6),(10)--(13) prove

    a_d(u)=exp(-i2u) C_d exp(-2lambda u)+Rem_d(u),
    C_d=rho A t_d(i lambda)/(2a^2 sqrt(p)),
    |Rem_d(u)|<=4000 rho/(h^2 u^2).                     (14)

The last constant follows from p>=1/2 and 9000sqrt(2)/4<4000. Furthermore |C_d|<2rho: A<=2, a>.99, |t_d(i lambda)|<=1/a and 1/sqrt(p)<=sqrt(2)<3/2 give |C_d|/rho<=1.5/.99^3<2. Hence a convenient uniform bound for all three offsets is

    |a_d(u)| <=2rho exp[-rho^2 u/a]
                           +4000rho/(h^2 u^2), u>0.     (15)

The exact coefficients in (14) give a tighter optional first term and preserve the original source phase. Bound (15) is not a pure exponential assertion: it explicitly retains the cutoff-induced algebraic allowance.

The full-line pole and V_d cancel exactly outside the physical cutoff support, including beyond |x|=1. Artificial tails of the pole comparison have not been mistaken for physical energy density. Since the target quantity uses g, its cutoff is part of the EXACT integrand. There is no additional omitted band-edge mass in (14). If one instead asks for the UNcut F integral, the present C2 cutoff-remainder proof does not apply unchanged; the removed physical spectral component would need its own integrated estimate. A uniform-in-time L2 cutoff error multiplied by an arbitrarily long time interval would not suffice for that purpose.

## 5. Integrated estimate and finite-boundary interface

Let 0<u0<=U, with U possibly infinite. Integrating (15), writing inverse infinity and its exponential as zero, gives

    integral_(u0)^U |a_d(u)|du
       <= (2a/rho)[exp(-rho^2 u0/a)-exp(-rho^2 U/a)]
          +(4000rho/h^2)(1/u0-1/U)
       <= (2/rho)exp(-rho^2 u0/a)
                              +4000rho/(h^2 u0).         (16)

This is a genuine integrable amplitude estimate; no oscillatory cancellation AFTER taking |a_d| is assumed. It covers the same three fixed offsets with identical constants.

In finite532866 section5, the incoming packet at the cut levels has precisely d=0,-1,-2 and the original incoming record0. Its program/path input is a common Hilbert-space factor of norm one, so there is no separate path/reference count. Taking the norm across at most three levels costs sqrt(3). The actual hopping-only cut perturbation has norm at most sqrt(2)j; changing from physical time t to u=jt cancels j. Consequently the INCOMING portion of its integrated boundary Duhamel allowance may be replaced by

    E_boundary,in <= sqrt(6) * {
         (2a/rho)[exp(-rho^2 u0/a)-exp(-rho^2 U/a)]
            +(4000rho/h^2)(1/u0-1/U) }, U=jT.            (17)

The same inequality holds with any earlier upper time. This uses only the incoming part; the full perturbation acts on incoming plus outgoing fields and must retain the separate outgoing allowance. The actual record bias vanishes on the incoming R0 field and its global physical scalar is a unit phase, so neither changes (17). No outgoing record1 momentum q is substituted into this incoming calculation.

At times u0 beyond the resonance scale, the first term is exponentially small. The algebraic coefficient rho/h^2 is smaller than rho^-3 by the factor rho^4/h^2. Under rho^2<=h/16 this factor is at most1/256, and for the finite source's shrinking rho^2/h it tends to zero. The constants in (16) are conservative, so this comparison concerns coefficient dependence and useful regimes, not uniform numerical superiority to every older bound at every u0. One may retain the minimum of this allowance and the previously proved incoming allowance when both hypotheses apply.

No new finite family or runtime exponent is proved. Finite532866's Q also contains outgoing A_o, source survival and internal terms, and its source/packet match and final truncation still need their own budgets. Reducing only the incoming part of A_i does not remove those constraints. In particular this source does not prove a corresponding outgoing analytic bound, and does not change any frozen finite, resource or preparation source.

## 6. Failed shortcuts and physical limits

The k-circle rational continuation has squared norm2 whereas the physical upper-half spectrum has norm1; that failed shortcut from geometricbe2ab is not used. The successful continuation here is an explicitly subtracted real-energy pole with an exact smooth remainder, not a change of spectral domain. The C2 cutoff is transformed as a real function and never declared analytic. Its derivative and exterior-tail costs are visible in (8)--(12). The original phase and positive p are retained.

The scalar survival estimate306174 concerns the occupied emitter, not these spatial cut amplitudes. It inspired the energy coordinate but cannot replace this derivation. Conversely (16) does not certify source survival, full incoming half-line norm, outgoing far tails, localized seed weight, physical initialization, finite capture/reset, readout, native coefficients or permanent halt. The head-conserving standalone source and its exact compensation remain supplied. The result is a new scalar/vector interface requiring distinct review, not a complete operation certificate.

## 7. Exact sources, exposure and work record

N=`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

- Finite target interface `common_product_biased_record_finite_seed/PROPOSAL.md`: `532866ed3e3d9117906c4f5b6be3839fdc45c522bae727d1980e724ad11b7123`, previously authored and completely read; hash refreshed unchanged. Only its incoming phase, levels, physical cut norm and existing allowance are used here.
- Exact source `common_product_endpoint_launch/PROPOSAL.md`: `fb72f4ed4af9d6f00d6430ec4997fab3f8fbb978b140692b083ddda5e324e9e4`, and phase cancellation `common_product_launch_derivative_bounds/PROPOSAL.md`: `378086fdc6b217f9a2eb9d85fdb1ca862a54905be048d298465e0b123722fec8`, completely reread in the immediately preceding geometric review and reused at their exact standalone scopes. Measure check `1953d153c9ac8583202e7ca18bff62829bfbff2373691cc43a5ae152a2a6b0ae` was also completely reread there.
- `common_product_geometric_source_profile/PROPOSAL.md`: `be2ab9da4b62ca7f595c17fea5ec6e62849cdada2c34416154996ad15180538e`; my full distinct review `cfd880ac1dcd866fe47fd51c7b8f29764270fc028e67e540c1cb1a6b1f86dfed`. Both were completely read in that preceding task and hashes refreshed here. Their normalized free-profile theorem is not a premise of (14); their domain warning is retained.
- `common_product_resonance_tail/PROPOSAL.md`: `306174fb0a884c62d5c6de401492a742a3d8a55670ef273f9d376258e531c002`, completely reread in the preceding task; its complete check `common_product_resonance_tail_check/REVIEW.md`, `de9dbd20bf873f194d969ec6570e77224a2dfb192ba3ac4035b0933fc3d610bd`, was read here. Both hashes were refreshed. The survival theorem is not imported as a spatial result.

ROOT requested the incoming-boundary improvement and suggested a real-energy pole route during derivation. I had independently reached the equivalent x=cos k representation before receiving that additional algebra, but the subsequent constants and proof were developed with full design exposure; this is not a blind-origin claim. I authored the finite source and other components and reviewed the geometric source. This is same-model/effort author continuation requiring a distinct check of (3)--(17), especially the Jacobian, removable pole, analytic branch, transformed-cutoff constants, improper Fourier transforms and physical boundary prefactor.

Only this proposal was created. No scientific executable, numerical contour/integration, solver, parameter sweep, W/Git/checkpoint/axiom/editable-prompt/model change, delegation or publication occurred. All frozen sources remain unchanged.
