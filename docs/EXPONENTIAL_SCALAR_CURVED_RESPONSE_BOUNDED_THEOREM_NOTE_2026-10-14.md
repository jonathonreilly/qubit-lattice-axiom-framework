# Curved scalar response and the finite-energy boundary restriction

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_curved_response_check.py](../scripts/exponential_scalar_curved_response_check.py)

A scalar range inferred from a force law requires a controlled spacetime and
physical readout. For this supplied action, the range can approach the vacuum
curvature scale even at weak coupling. This note derives the exact static
linear scalar kernel on that vacuum, the acceleration of a specified physical
observer, and a condition under which the static horizon boundary follows
from finite exterior energy. It does not select the action, cosmological
initial state or observed environment. No empirical fit or audit grade is
asserted.

## Complete supplied action

Use signature (-+++), phi=(u,x,y), and

    S=Q(k) integral sqrt(-ghat) [Rhat/2
      -K_AB ghat^{mu nu} partial_mu phi^A partial_nu phi^B-2Hv^2 U]
      +S_m[C ghat,matter], Q(k)=Q0(1+k), Q0>0, Hv>0.

For fixed 0<k<1/3 and nu>0, put

    a=(1-k)(1+3k)/4, alpha=sqrt(a), s=(1+k)/(k(1-3k)),
    E=exp(2alpha u), F=1+sE, J=1+(1-3a)sE,
    D=1+2(1+k)(x^2+y^2)/3,
    K=diag(J/F^2,(1+s)4k/(9FD),(1+s)k/(3FD)),
    C=(1+s)E/F,
    U=3/2+3s(E-1)^2/(2F^2)
      +(k/2)x^2 exp(-lambda_x u)+(k/3)y^2 exp(-lambda_y u)
      +nu(1+s)u^2/(2F^2),
    lambda_x=(1-k)/alpha, lambda_y=(1+k)/alpha.

The model, three fields, universal physical metric, k, nu, Q0 and Hv are
candidate inputs. The registered scale, isotropy and realized-state premises
do not select them. Symbols x and y in this action are field coordinates;
below, x=Hv r/c is instead the dimensionless radial coordinate.

For an explicit check of the vacuum normalization, F0=1+s, J0=a/k,
K_u0=J0/(1+s)^2, partial_u log sqrt(C)|0=sqrt(a)/(1+s), and
U_uu|0=[12 a s+nu(1+s)]/(1+s)^2. Thus alpha_m^2=k and
B=U_uu|0/K_u0=4[3(1+k)+nu]/(1-3k). The first derivatives of U vanish
there. The constant part gives Lambda=3Hv^2 in natural units. The primary
runner independently differentiates the supplied expressions at the vacuum.

## Question and fixed hypotheses

The flat static Yukawa force law is a possible local approximation. In this action,
at nu=1 and small k, sensitivity to the scalar range occurs at H_v r/c near
1/4. Weak coupling does not by itself make curvature negligible there.
Derive the response and an actual local readout before interpreting that
flat-space inverse. All previous observations are exposed development context;
the calculations below use exact identities and synthetic parameters only.

Use the supplied Einstein action Q integral sqrt(-g)[R/2-K_AB dphi^A dphi^B
-2 H_v^2 U]+S_m[C g,psi], with signature -+++, Q=Q0(1+k)>0,
0<k<1/3, nu>0. At its stationary vacuum phi=0, U=3/2, C=1,
the canonical matter-coupled scalar varphi satisfies

    alpha_m^2=k,  m_u^2/H_v^2=B=4[3(1+k)+nu]/(1-3k)>12.

The other two scalar directions have zero linear matter coupling. These
identities follow from the complete supplied action above. They do
not derive that action or its constants. Write H=H_v/c, mu=m_u/c,
x=H r, beta=mu/H=sqrt(B), and m=Gstar M/c^2, Gstar=1/(8 pi Q).

The source is a prescribed, weak, static, central nonrelativistic source;
pressure/stress in its scalar trace are negligible. The point limit is used
first. Work to first order in m and the scalar amplitude, on compact exterior
domains with m/(r f)<<1 and |alpha_m delta varphi|<<1, f=1-H^2 r^2.
At a constant vacuum the scalar excitation stress starts at second order;
the nonzero constant potential already supplies the background de Sitter
curvature. The regular background-horizon boundary condition is stated,
not inferred from cosmological initial data or from a retarded evolution.
The linear metric expansion is not asserted uniform at either horizon.

## Scalar equation, source normalization and boundary

Variation gives (Box-mu^2) delta varphi=4 pi Gstar alpha_m rho/c^2
for the stated trace. In the exact vacuum static patch,

    ds_E^2=-f c^2 dt^2+dr^2/f+r^2 dOmega^2,
    (r^2 f delta varphi_r)_r/r^2-mu^2 delta varphi=0  (exterior).

Set delta varphi=-alpha_m m psi(x)/r. The radial equation reduces to

    (1-x^2) psi_xx-2x psi_x+(2-B) psi=0.                 (1)

The point source fixes psi(0)=1, equivalently the outward flux of the
positive radial kernel psi/x is -1 at the origin. It does not by itself fix
the regular additive part. A bounded solution at the background horizon
x=1 excludes the logarithmic Frobenius branch. The remaining solution is

    psi(x)=P_l(x)/P_l(0),   l(l+1)=2-B,
    l=-1/2+i sqrt(B-9/4)  for the candidate domain B>12.   (2)

Here P is equivalently DEFINED by the horizon series below, so no unproved
special-function branch convention is needed. Put v=1-x and A=B-2>0:

    P_l(x)=sum[n>=0] a_n v^n,  a_0=1,
    a_(n+1)=[n(n+1)+A] a_n/[2(n+1)^2].                 (3)

All coefficients are positive. The radius of convergence is 2, hence the
series is real, positive and differentiable on 0<=x<=1. Its x=0 sum is
finite and positive; normalization (2) exists. The local regular singular
equation at x=1 has one analytic solution and one logarithmic solution.
Equivalently, the difference of two bounded same-flux solutions has no
source; multiplying its equation by itself and integrating gives
integral[x^2 f y_x^2+B x^2 y^2]=0. Center and horizon surface terms vanish.
For B>0 the difference is zero. This proves uniqueness in the stated
bounded regular class, not uniqueness among time-dependent states.

At x=1, psi_x=(1-B/2)psi; for y=psi/x, y_x=-B y/2.
The flux equation gives

    x^2 f y_x=-B integral_x^1 t^2 y(t) dt,
    B integral_0^1 x psi(x) dx=1.

Thus y is positive and strictly decreasing. The massless exception is real:
for B=0 a unit Coulomb coefficient gives y=1/x-atanh(x)+constant,
which is unbounded at the horizon. The regular P_1=x has P_1(0)=0 and
cannot be normalized to that source. The candidate's B>12 avoids this case.
At B=2 the regular solution is psi=1, y=1/x; this is an analytic control
outside the candidate's mass range, not a new candidate parameter choice.

## Force kernel and controlled series evaluation

Define D_B(x)=psi-x psi_x. A derivative of the scalar potential alone is
proportional to D_B; it must not be equated to a physical acceleration
without a metric and readout. Its center expansion is

    psi=1+b1 x+(B-2)x^2/2+B b1 x^3/6
          +(B+4)(B-2)x^4/24+O(x^5),
    D_B=1-(B-2)x^2/2-B b1 x^3/3
          -(B+4)(B-2)x^4/8+O(x^5).

The horizon condition fixes b1=P_l'(0)/P_l(0). The flat gradient kernel is
F(beta x)=(1+beta x)exp(-beta x). The leading difference is x^2; the cubic
term depends on the boundary through b1. No finite-radius error estimate
is obtained merely by calling x small.

For rational B>2 and rational 0<=x<=1, (3) gives exact rational enclosures.
Let S_N(v)=sum_0^N a_n v^n, a=a_(N+1), and choose N with

    rho0(v)=v[1+A/(N+2)^2]/2<1,
    rho1(v)=v[1+A/((N+1)(N+2))]/2<1.

For omitted terms the respective value and derivative ratios are bounded
by rho0 and rho1. Hence

    0<=P-S_N<=a v^(N+1)/(1-rho0),
    0<=P_v-S_N'<= (N+1)a v^N/(1-rho1).                (4)

Apply the same denominator bounds at v=1 and divide positive intervals.
They enclose psi and D_B=[P+x P_v]/P(0), without floating roundoff.
Rational exponential-series bounds and rational square-root brackets can
likewise enclose F(beta x). These are pointwise computed certificates, not
a claimed uniform error theorem over all masses or distances.

## Physical metric and a specified acceleration readout

To first order, the Einstein exterior metric is Schwarzschild-de Sitter,
h(r)=1-H^2 r^2-2m/r. Write a(r)=alpha_m delta varphi=-k m psi(Hr)/r.
The physical metric is (1+2a) ds_E^2. Use the PHYSICAL areal radius
R=(1+a)r. Then, to first order at fixed R,

    ds_J^2=-F_J(R)c^2dt^2+dR^2/G_J(R)+R^2 dOmega^2,
    F_J=f-2m/R+2a,
    G_J=f-2m/R+2H^2 R^2 a+2f R a_R,                (5)
    f=1-H^2 R^2,  a=-k m psi(HR)/R.

The same time normalization as the Einstein static patch is used. The
signed outward proper acceleration needed to hold a static observer is
an invariant along that observer: a_hold=c^2 sqrt(G_J) F_J'/(2F_J).
Subtract the source-free value at the SAME physical R,
a_dS=-c^2 H^2 R/sqrt(f). The linear source-induced difference is

    Delta a_hold = c^2 m/R^2 [T(x)+k S_B(x)],       x=HR,
    T=(1-2x^2)/f^(3/2),
    S_B=[f^2 D_B-x^2(1+f)psi]/f^(3/2).             (6)

This signed difference can change sign on sufficiently large domains;
the tensor difference T vanishes at x=1/sqrt(2). A ratio divided by T is
undefined there. On a specified domain with T nonzero, the scalar excess
relative to the tensor prediction is k S_B/T, not generally k D_B or
k F(beta x). Its small-x kernel is

    S_B/T = 1-(B/2+1)x^2+O(x^3).

Consequently a coordinate scalar derivative is not the whole curved-space
measurement correction. Formula (6) assumes an independently specified
background H, common physical radius and tensor mass parameter m; it has
not eliminated their observational reconstruction or error model.

For a circular timelike geodesic, the static-observer speed instead obeys
v_circ^2/c^2=R F_J'/(2F_J), on the static exterior domain F_J>0, G_J>0 and
0<R F_J'/[2F_J]<1. Its coordinate
frequency obeys Omega^2/c^2=F_J'/(2R). In this convention

    R F_J'/2=-x^2+(m/R)[1+k D_B(x)].                (7)

A positive circular-orbit frequency is an additional restriction; bound
slow circular tracers cannot be assumed available at every range radius
of a weak source in a de Sitter background. We have not derived orbital
stability. Null paths and local angles at the SAME spacetime events are
conformally invariant; mapping those events to fixed physical areal radii
and clocks is an extra readout step. The flat infinite-ray lensing formula
is not re-used here as a de Sitter mass calibration.

## Prescribed spherical source limitation

The center-regular homogeneous scalar kernel V_B obeys

    (1-x^2)V_xx+(2/x-4x)V_x-B V=0,
    V(0)=1, V_x(0)=0,
    V=sum[n even>=0] d_n x^n,
    d_(n+2)=[n(n+3)+B]d_n/[(n+2)(n+3)].             (8)

The weighted Wronskian of V and y=psi/x is
x^2 f(V y_x-V_x y)=-1. Green's identity gives an exterior scalar charge
factor, relative to the Einstein mass integral, for a prescribed spherical
nonnegative nonrelativistic density supported at r_s<1/H:

    F_body=integral_0^rs rho(r) r^2 V_B(Hr)dr /
           integral_0^rs rho(r) r^2 dr.

The radial mass integral must be finite and strictly positive. Then
a=-k m F_body psi/r. Positive series coefficients imply
1<=F_body<=V_B(H r_s). This is a remaining profile input. It includes
neither nonlinear scalar feedback nor a derivation of static equilibrium.
The mass integral is the Einstein static radial mass integral, not an
unqualified proper-volume integral; at this linear order the background
frame has C=1. A physically supported body must also satisfy conservation
and the negligible-trace-stress hypotheses. No arbitrary source profile
is thereby proved realizable.

## What is and is not retired

The exact conditional static vacuum response can be derived without a flat
space approximation. The supplied action, positive vacuum, initial state,
stationarity, horizon regularity, physical source and observational mapping
remain explicit premises. Neither B nor k nor H_v nor Q0 is selected by
solving this boundary-value problem. The earlier flat two-radius inverse is
not automatically a curved-space inverse. No observations have been fitted,
no independent observation test has been passed, and no TOE is established.

## Deriving the stationary boundary from exterior energy

The static Green calculation used a bounded background-horizon branch. Ask
whether that restriction is independent, or follows from a physically stated
finite-energy class. The point-source ultraviolet singularity must not be
hidden: work on every fixed exterior annulus x0<=x<1 with x0>0. For a finite
body, take x0 outside it. No global finite-energy point-source claim follows.

For a real canonical scalar perturbation phi=delta varphi, its quadratic
Killing energy on the exact de Sitter static patch is, up to a positive
constant depending on the action and units,

    E_ext=1/2 integral_x0^1 x^2 [phi_tau^2/f+f phi_x^2+B phi^2] dx,
    f=1-x^2, tau=H_v t.                                  (9)

This follows by contracting the canonical scalar stress with the static
Killing field and slice normal. The lapse factor cancels the proper radial
volume factor in the static gradient/potential terms. It is Killing energy,
not a claim of a global de Sitter timelike symmetry beyond the static patch.
For static solutions the first term is zero. The constant vacuum stress is
part of the background and is excluded from this quadratic excitation energy.

Let y_R=psi/x be the positive bounded solution constructed earlier. Reduction
of order gives a second independent exterior solution

    y_Q(x)=y_R(x) integral^x dt/[t^2(1-t^2)y_R(t)^2].    (10)

Writing q=y_R(1)>0, as x tends to 1 from below,

    y_Q=-(1/(2q)) log(1-x)+O(1),
    y_Q'=1/[2q(1-x)]+O(|log(1-x)|).

Any nonzero y_Q component therefore makes the static gradient contribution
to (9) diverge logarithmically; a bounded component cannot cancel the leading
positive square. The y_R component has finite exterior energy. Thus among
stationary solutions with the specified source, FINITE EXTERIOR QUADRATIC
KILLING ENERGY implies the bounded horizon branch and the earlier unique
Green kernel. The branch need not be supplied independently after that
energy class is stipulated. Finiteness of this whole exterior energy has
not been measured by local observations; it remains an explicit condition.

This implication does not infer stationarity, the vacuum environment, source
turn-on time, retarded boundary data or our universe's six-state history.
There can be finite-energy time-dependent transients. To show a finite-time
history converges to this particular stationary kernel would require a
separate evolution and local-decay argument, not just (9) or positivity.

## Homogeneous radial dynamics and a restricted stability consequence

For source-free differences on the fixed vacuum background, set
rho=atanh(x), psi=x phi. The angular harmonic with index j=0,1,2,... obeys

    psi_tautau-psi_rhorho+V_j(rho)psi=0,
    V_j=(1-x^2)[B-2+j(j+1)/x^2].                       (11)

The action's B>12 makes V_j nonnegative. For regular-center perturbations,
psi=O(x^(j+1)), and finite-energy horizon behavior, the corresponding
positive wave energy is

    E_psi=1/2 integral_0^infinity
        [psi_tau^2+psi_rho^2+V_j psi^2] d rho.

For j=0, direct integration by parts gives

    E_phi=E_psi-1/2 [f psi^2/x]_boundaries.             (12)

The boundary term vanishes for regular-center perturbations and bounded or
logarithmic static horizon profiles. On an exterior annulus its finite
inner value does not affect the horizon finiteness test. Angular energy
adds the same positive j(j+1) term in both representations.

There is no nonzero separated homogeneous growing mode e^(s tau) w(rho)
with Re(s)>0, regular center and the outgoing/finite-energy horizon branch.
At infinity that branch behaves as exp(-s rho); at the center it is regular.
Multiplying -w''+V_j w=-s^2 w by its conjugate and integrating gives

    integral(|w'|^2+V_j|w|^2)+s^2 integral|w|^2=0.

The integrals are finite for those modes and boundary terms vanish. Its
imaginary part forces Im(s)=0 when Re(s)>0, and then its real part is a sum
of nonnegative terms including a strictly positive s^2 norm. Contradiction.
This is a linear fixed-background scalar-mode statement. It does not prove
a nonlinear cosmological attractor, a decay rate, absence of all nonmodal
effects, global metric stability or convergence after a source turns on.
It derives a useful consistency condition from the supplied positive mass,
while leaving the observed environment and initial state open.

## Executed evidence and limits of the result

The primary runner checks the supplied vacuum normalization, radial and metric
identities, positive rational kernel enclosures, a separate ODE integration,
source flux and Wronskian identities, physical-radius acceleration, energy
and wave equations, and explicit failed-formula/domain controls. Eight
comparison points have exact rational enclosures. They are mathematical
development examples, not held-out observations. At B=16,x=1/4, D is about
0.769214503893 versus the flat factor 0.735758882343; the specified physical
holding-to-tensor kernel is about 0.717012253039. The action allows B=16,
for example at k=.01,nu=.85; the nu=1 small-k limit approaches this value.
These are changes in kernel factors, not percent changes of total measured
acceleration; the scalar term also carries k.

Independent evidence uses three singular-endpoint BVPs, 21 exact rational
kernel certificates, two finite-volume source-profile sequences, 18 implicit
physical-radius metric checks and 15 negative/domain controls. Its 111
supported conditions were assembled from a preserved original 107/111 run
and targeted repairs; they are not a fresh uninterrupted 111-pass run.
The original checker errors and author comparator precision error remain in
the recoverable evidence archive. Numerical tests support the implementations;
the handwritten series, uniqueness and energy proofs carry the mathematical
claims.

Finite energy on an exterior static annulus derives the bounded horizon
branch only within that stated class. A finite-energy nonstatic scalar pulse
is an explicit control against treating it as an initial-state selector.
A negative-potential growing mode outside this action's positive-mass domain
checks that the restricted stability argument really uses its hypotheses.
No local-decay rate, retarded-source convergence, observed-state selection,
nonlinear compact-object solution or complete observational inverse is proved.
The action and scale hierarchy remain supplied. The scientific direction is
observations first, with each missing physical input kept visible.

The special-function notation agrees with the real-argument Legendre
(Ferrers) equation in [NIST DLMF 14.2](https://dlmf.nist.gov/14.2) and its
[hypergeometric representation](https://dlmf.nist.gov/14.3). The positive
series above defines the branch used here, and the physical boundary is
justified separately; the references supply no physical selection rule.
