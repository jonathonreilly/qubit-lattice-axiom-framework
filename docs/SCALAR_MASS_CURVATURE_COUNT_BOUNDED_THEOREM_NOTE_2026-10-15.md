# Mass and curvature bounds for observation-derived scalar counts

**Date:** 2026-10-15
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_mass_curvature_count_check.py](../scripts/scalar_mass_curvature_count_check.py)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: scalar_mass_curvature_count
target_blocker_text: "Derive or eliminate the scalar theory's remaining initial-state and measurement assumptions"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Supply empirical reference calibration, scale constraints and independently justified errors or energy budgets"
conditional_surface_status: "Observation and propagation bounds under the displayed candidate action, vacuum and measurement premises"
hypothetical_axiom_status: null
admitted_observation_status: "No observational values enter this theorem or its synthetic controls"
claim_type_reason: "Count contrasts and propagation errors are derived; physical action, scales and calibration remain conditional"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The downstream consumer is the reconstruction of scalar history from finite
tracking counts. The previous massless calculation left an important gap:
the supplied revised scalar action has positive mass on a curved vacuum.
This note derives explicit corrections and a proper-count contrast on that
vacuum. It allows arbitrary finite-energy perturbative initial data. It
does not choose a state to make a signal fit.

**Exact target:** bound the positive-mass and time-dependent vacuum-potential
response errors, derive a four-endpoint count that cancels initial orbit and
clock terms, and compose those results into a conditional physical-energy
requirement. The latter remains an implication, not an observed energy estimate.

No new archive data are opened or fitted. Earlier Day169 radio products remain
exposed development data; their format consistency is not a gravity test.
Every numerical case below is mathematical or synthetic development evidence.
No independent empirical test or literature-priority claim is made.

## 1. Premises and the retained distinction between inference and import

Supply a linear scalar channel h with conformal coupling delta log A=alpha h,
a test-body action -m integral A ds_E, ideal geometric-optics radio transfer,
constant source proper frequency and instantaneous coherent turnaround when
used. Actual clocks, media, delays, environmental sources, tensor dynamics and
calibration errors are not established by these premises.

For the curved application supply a stationary scalar vacuum with
Einstein de Sitter metric, normalization Q>0 and mass m^2=B H^2, B>12, H>0.
The candidate action convention is -Q(partial h)^2-Q m^2 h^2 at quadratic
order. In the revised scalar candidate the supplied parameter relation is
B=4[3(1+kappa)+nu]/(1-3kappa), 0<kappa<1/3, nu>0; this makes B>12.
This note treats that relation and the vacuum as premises. It derives the
consequences for observations without selecting kappa,nu,H,Q or a potential.
The source curved-action note is provenance, not a hidden proof supplier.

| Input | Disposition here | Remaining obligation |
| --- | --- | --- |
| Action, linear regime and stationary vacuum | Explicit premises | Derive or discriminate them empirically |
| Count, clock and link model | Defines the observable; weights then derived | Validate actual instruments and environment |
| Initial orbital/clock perturbations | Exact contrast removes their linear columns in the stated fixture | Bound leakage from uncertain reference calibration |
| Initial scalar field | Arbitrary in the specified energy completion | No state, history or energy upper budget selected |
| Mass and curvature scales | Error bounds remain explicit functions | Obtain independent scale constraints |
| Stronger force-window regularity | Sufficient condition for the proved tail bound | Check it for other actual calibrated responses |

Use c=1. Coordinate times, momenta and lengths in the formulas have consistent
natural units. A numerical time unit in a synthetic example is not an SI scale
identification.

## 2. Common real energy space and the observation

First consider the homogeneous flat equation
h_tt-Delta h+mu^2 h=0. For mu>=0 define

    N_mu = integral [p0^2+|grad h0|^2+mu^2 h0^2] = 2 E_lab.
    h=(2pi)^(-3/2) integral [a(k) exp(i omega t-i k.x)+conjugate] d^3k,
    omega=sqrt(k^2+mu^2), g(k)=2 omega a(k).

Then N_mu=integral |g|^2. The real Hilbert pairing is Re integral g1* g2;
there is no additional a(-k)=a(k)* restriction. Reality already comes from
the explicit conjugate. For mu=0 use the anchored homogeneous-H1
representative, or explicitly remove the constant response column. A global
nonzero constant massive oscillation is not a finite-energy datum on R3.

Fix one common spacetime origin for all response rows. Identifying g at
different masses is an energy-space isometry, not equality of physical Cauchy
data. By contrast, the variable-potential comparison in section6 preserves
the same chi initial data. These two identifications must not be conflated.

For finitely many prescribed C3 timelike paths x_A(t), let u=x', |u|<=beta<1.
The linear observation obtained from the proper-count/orbit-clock response has
the form

    O[h]=sum_A integral [c_A h-(1-|u_A|^2)W_A.(grad h+u_A partial_t h)] dt.

Supply real compact L2 clocks c_A. Require the zero extension of W_A continuous,
compact and in W^(1,1), with W_A' in BV. Thus W is H1 as well.
All total variations below include outer and internal jumps of W'.
This is stronger than bare H1 regularity; no extension to arbitrary H1 force
weights is claimed by the following explicit tail bound.

Put v=k/omega, n=kvec/k, q=1-|u|^2. Direct substitution gives

    F_mu=sum_A integral [c_A/omega+i q_A(v n-u_A).W_A]
                         exp(i omega t-i k n.x_A) dt,
    O_mu[g]=(2pi)^(-3/2) Re integral g F_mu d^3k,
    G_mu,ij=(2pi)^(-3) integral k^2 Re(F_mu,i F_mu,j*) dk dOmega.

All paths sample the SAME field. Their amplitudes are added before the norm
is taken. No separate field-energy budget is assigned to each location.

For reference, the massless common-arrival representation is explicit:
tau=t-n.x_A(t), d=1-n.u_A>0 and b=(1-u^2)(n-u)/d. A force integration by
parts gives the arrival kernel
H_n(tau)=sum_A[c_A/d-partial_tau(b.W_A)], each evaluated at its own inverse
arrival time. One-sided Parseval for this real kernel gives

    G_0,ij=1/(8pi^2) integral_S2 integral_R H_i,n H_j,n d tau dOmega.

Compact L2 clocks and the stated weights make this finite. Summing at common
tau retains the cross terms. The normalization follows also directly from
N=4 integral k^2|a|^2. Density extends the initially smooth finite-energy
calculation to the indicated completion.

## 3. Explicit positive-mass correction

For fixed v,n put

    d_v=1-v n.u, b_v=(1-u^2)(v n-u)/d_v,
    V_F=sum_A sup_(v,n) TV{[(b_v.W_A)']/d_v}.

Two integrations by parts, the second in the BV/Stieltjes sense, give
|F_mu,force|<=V_F/omega^2. Zero outer W traces remove the first boundary
term; the second derivative measure includes every W' jump.

This constant has an analytic supplier. With delta=1-beta, a=||u'||infinity,
j=||u''||infinity, Q0=1+beta and Q1=1+2beta(1+beta), the quotient rule gives

    B0=Q0/delta,
    B1=Q1 a/delta+Q0 a/delta^2,
    B2=[(2+6beta)a^2+Q1 j]/delta
          +[2Q1 a^2+Q0 j]/delta^2+2Q0 a^2/delta^3.

These bound |b|,|b'|,|b''|. Per path a sufficient bound is

    V_F,A <= [B2||W||1+2B1||W'||1+B0 TV(W')]/delta
                   +a[B1||W||1+B0||W'||1]/delta^2.

Sum these suppliers; sampled maxima alone are not suppliers. No BV(c) is
needed because the clock difference is estimated separately.

Write Delta=omega-k and define

    C=sum integral |c|,
    D=sum integral [|t c|+(1-u^2)|W|],
    E=sum integral |t|(1-u^2)(1+|u|)|W|.

At fixed k,n the spatial phases agree at both masses. Splitting the clock
amplitude change, its temporal phase change and the force change gives
C Delta/(k omega), D Delta/omega, and E Delta. The first two terms are
globally square-integrable in the radial measure. The last is used only
below K; above K the force difference is <=2V_F/k^2. Thus

    epsilon_mu(K) <= 1/(sqrt(2)pi) [
       C sqrt((2-pi/2)mu)+D sqrt((pi/2-4/3)mu^3)
                         +(E mu^2/2)sqrt(K)+2V_F/sqrt(K)].

Here epsilon bounds the norm of the scalar observation difference on the
common g space. The exact radial identities are

    integral_0^infinity (1-k/omega)^2 dk=(2-pi/2)mu,
    integral_0^infinity k^2(Delta/omega)^2 dk=(pi/2-4/3)mu^3.

For example k=mu sinh y followed by z=exp(-y) reduces the two integrals to
2mu integral_0^1 z^2/(1+z^2) dz and
(mu^3/2) integral_0^1(1-z^2)^2/(1+z^2) dz.
The remaining low integral uses k^2 Delta^2<=mu^4/4. For E V_F>0,
K=4V_F/(E mu^2) yields

    epsilon_mu <= [C sqrt((2-pi/2)mu)+D sqrt((pi/2-4/3)mu^3)
                         +2mu sqrt(E V_F)]/(sqrt(2)pi).              (1)

Zero cases take the infimum of the all-K bound; at mu=0 the difference is
exactly zero. These are sufficient, deliberately conservative enclosures.

An exact constant-offset contrast improves the infrared term. Define

    C0=|sum integral c|, M=sum integral |c|(|t|+|x_A(t)|).

The total massless clock numerator has modulus <=C0+kM. Consequently (1)
also holds with C replaced by C0 and D by D+M. Exact C0=0 removes the
sqrt(mu) term, leaving O(mu), or O(mu^(3/2)) for a pure clock. A numerically
small C0 is not zero. A vector comparison must use one common epoch and
isometry; separately recentered scalar bounds cannot silently be combined.

For a contrast with g0=t^T G0 t,

    max(0,sqrt(g0)-epsilon_t) <= sqrt(t^T G_mu t)
                                      <=sqrt(g0)+epsilon_t.

If errors obey |t^T error|<=e_t and the measured residual is truly described
by this model, every compatible state obeys
E_lab>=max(0,|t^T r|-e_t)^2/[2(sqrt(g0)+epsilon_t)^2].
The zero-denominator case requires a separate feasibility check. Exact
vector data still require membership in the response range. A vector
epsilon_op<=sqrt(sum epsilon_i^2) gives
||G_mu-G0||op<=2sqrt(||G0||op)epsilon_op+epsilon_op^2.
None of these inequalities chooses the least-energy state as physical.

## 4. A rejected universal mass-order shortcut

A single stationary clock has positive-mass density v<=1. That does not
establish G_mu<=G0 for separated clocks. For identical real c(t) at fixed
points the exact angular integral gives

    G_mu=1/(2pi^2) integral_mu^infinity |c_hat(omega)|^2
                         v sum_AB sinc(v omega r_AB) d omega.

Take three equilateral points with side r, and omega0 r=pi. Their spatial
factor at that frequency is 3v+6sin(pi v)/pi. At v=2/3 its ratio to the
massless value3 is 2/3+sqrt(3)/pi>1. This strict reversal is realizable
with compact smooth zero-integral clocks: for any nonzero smooth compact
real bump psi, c_T=partial_t[psi(t/T)sin(omega0 t)]. Its integral is zero.
As T grows its normalized positive-frequency power concentrates at omega0;
smooth compactness supplies arbitrarily fast off-peak decay. Localization
therefore gives the stated strict ratio for sufficiently large finite T.

The helper's finite-window cos-squared examples have finite differentiability,
not C-infinity. Their ratios approach1.218 and are explicitly quadrature
diagnostics. The separate smooth-bump proof supplies existence. An independent
checker also constructed a different compact smooth three-point example;
its derivation and source identities are preserved in the campaign pack.
This counterexample concerns general separated clock responses, not the
specific two-body coherent link or the entire scalar theory.

The massive two-body coherent fixture is checked separately. With L=3/5,
endpoints1.4,2.4,3.4, coefficients(1,-2,1), and station0/body L e1,

    F=(-i/omega^2) sum_j beta_j exp(i omega t_j) [
         (1+vz)exp(-2i omega L)+(vz-1)
                         -2vz exp(-i omega L-i kLz)].

This follows from the clock particular solution eta=-i h/omega and orbital
solution xi=-i k n h/omega^2; arbitrary homogeneous pieces cancel.
Direct integration of the derived piecewise weights agrees. For a second
channel shifted by one, the massless exact Gram is
[[3064,-1871],[-1871,3064]]/(1620pi). The helper also implements the massive
angular integral separately. Each entry's tail past K is <=128/(pi^2 K),
using |F|<=16/omega^2. Finite quadrature convergence is not an interval
certificate and does not prove a general ordering.

## 5. Curvature changes both field propagation and the count weights

In the supplied spatially flat de Sitter chart, set
a(t)=1/(1-Ht), a(0)=1, 0<=t<=T<1/H and physical metric A(h)^2 a^2 eta.
The fixed-background source-free scalar equation is

    h''+2mathcalH h'-Delta h+a^2 m^2 h=0, mathcalH=a'/a.

The scalar perturbation stress is quadratic at this supplied stationary
vacuum. Set chi=a h. Direct differentiation gives

    chi''-Delta chi+V(t)chi=0,
    V=(B-2)H^2/(1-Ht)^2, mu0=sqrt(B-2)H>0.

In particular the frozen mass is mu0, not m. For the observation in section2,

    Wtilde=W/a,
    ctilde=[c+(1-u^2)mathcalH W.u]/a.                               (2)

The induced clock term matters on a moving path. The actual curved reference
lapse is ell=a sqrt(1-u^2). The test-body Euler-Lagrange equation is
u'=-(1-u^2)[mathcalH u+alpha(grad h+u h')], at first scalar order with its
corresponding reference position/velocity Jacobians. One cannot reuse flat
reference clock and orbit weights merely by renaming h as chi.

At the specified initial slice the Einstein comoving excitation energy is

    E_phys=Q integral[(chi'-Hchi)^2+|grad chi|^2+B H^2 chi^2].

Compare with N0=integral[chi'^2+|grad chi|^2+mu0^2 chi^2]. Put
rB=1/sqrt(B-2). The (chi',mu0 chi) matrix is
[[1,-rB],[-rB,1+3rB^2]], so

    lambda_- N0 <= E_phys/Q <=lambda_+ N0,
    lambda_±=1+3rB^2/2 ±sqrt(rB^2+9rB^4/4).                         (3)

Its determinant1+2rB^2 is positive; the gradient coefficient1 lies between
the eigenvalues. This is an initial-slice conversion, not a conserved global
de Sitter Killing energy. At other slices the comoving energy has an additional
1/a factor after substitution. No physical upper energy budget is inferred.

## 6. Explicit error for the varying potential

Write V=mu0^2+U(t), U C1, and use the SAME arbitrary initial chi data for the
variable and frozen equations. Set S=integral_0^T|U|, U0=||U||infinity,
U1=||U'||infinity and R=exp(S/mu0). For the displayed background,

    S=mu0^2 H T^2/(1-HT),
    U0=mu0^2[(1-HT)^(-2)-1], U1=2H mu0^2/(1-HT)^3.

At omega=sqrt(k^2+mu0^2), solve f''+(omega^2+U)f=0,
f(0)=1,f'(0)=i omega. Its variation-of-constants representation is

    f=A+ exp(i omega t)+A- exp(-i omega t),
    f'=i omega[A+ exp(i omega t)-A- exp(-i omega t)],
    A+'=iU/(2omega)[A++A- exp(-2i omega t)],
    A-'=-iU/(2omega)[A+ exp(2i omega t)+A-],
    A+(0)=1,A-(0)=0.

The l1 matrix norm is |U|/omega. Differentiating that matrix, including its
oscillating coefficients, and applying Gronwall gives

    sum|A_sigma|<=R,
    sum|A_sigma'|<=R U0/mu0,
    sum|A_sigma''|<=R[U1/mu0+U0+U0^2/mu0^2],
    |f-exp(i omega t)|<=RS/omega,
    |f'-i omega exp(i omega t)|<=RS.

Use the transformed weights (2), now denoted c,W. Define
C=sum||c||1, Wsum=sum||W||1, D=(1+beta)Wsum.
The clock difference is globally <=RS C/omega^2; the force difference
below K is <=RS D/omega. The radial integrals are bounded by
pi/(4mu0) and K respectively.

For the high-frequency force put, for sigma=+/-1,

    d_sigma=1-sigma v n.u,
    b_sigma=(1-u^2)(sigma v n-u)/d_sigma,
    j_sigma=-(b_sigma.W)',
    r_sigma=(b_sigma+(1-u^2)u).W.

One integration by parts gives the branch kernel
omega^(-1) integral[A_sigma j_sigma-A_sigma' r_sigma]
exp(i sigma omega t-i k n.x) dt. This expression uses the derivative
of the individual branch; sum A_sigma' exp(i sigma omega t)=0 ensures
equivalence with the displayed f' representation. A second BV integration
bounds it by omega^(-2) TV[(A_sigma j_sigma-A_sigma' r_sigma)/d_sigma].

Let V_F bound sum TV(j/d), G_F bound sum||j/d||1,
V_R bound sum TV(r/d), and R_L bound sum||r/d||1 uniformly in sigma,v,n.
The previous quotient constants supply

    G_F,A <=[B1||W||1+B0||W'||1]/delta,
    R0=B0+beta, R1=B1+(1+2beta^2)||u'||infinity,
    R_L,A<=R0||W||1/delta,
    V_R,A<=[R1||W||1+R0||W'||1]/delta
                            +||u'||infinity R0||W||1/delta^2.

A conservative sum for both branches is

    C_F=2R[V_F+(U0/mu0)(G_F+V_R)
                       +(U1/mu0+U0+U0^2/mu0^2)R_L].

It follows by the BV product rule; the factor2 safely permits each branch's
supremum at a different time. The difference from the frozen force has
high-k bound (C_F+V_F)/k^2. The radial low/high split therefore gives

    epsilon_U <= [RS C sqrt(pi/(4mu0))
                     +2sqrt(RS D(C_F+V_F))]/(sqrt(2)pi).             (4)

For nonzero force the minimizing cutoff is (C_F+V_F)/(RS D).
S=0 means identical operators; D=0 removes the force term. The zero cases
use the all-K infimum. These estimates prove boundedness on the frozen
positive-energy completion, not just agreement for finitely many modes.
The constants may be unhelpfully large near the chart boundary.

Add (1) at mu0 to (4) using the SAME transformed curved-reference weights
and the common initial epoch. This compares with massless propagation of
chi using those weights, not with uncorrected flat clocks or flat orbits.

## 7. Deriving an actual curved count contrast

Choose comoving station0 and spacecraft L e1, the supplied ideal coherent
link, and constant source proper frequency. Absorb the common alpha times
the coherent frequency normalization into the displayed response; it must
be restored for a physical count. At reception conformal time t the reference
emission and bounce times are t-2L,t-L. Define d(t)=1-Ht and
P(t)=t-Ht^2/2. Linearizing the original body and clock equations gives

    (a delta u)'=-alpha grad chi,
    xi(t)=xi0+v0 P(t)-alpha integral_0^t[P(t)-P(s)]grad chi(s,x)ds,
    eta(t)=eta0+alpha integral_0^t chi(s,x)ds.

Implicit differentiation of the two null events at fixed receiver proper
time gives the phase response

    Phi(t)=eta_s(t-2L)-[a(t-2L)/a(t)]eta_s(t)
       +a(t-2L)e1.[xi_s(t-2L)+xi_s(t)-2xi_b(t-L)].                    (5)

The lapse ratio and emission lapse are essential. There is no direct
spacecraft clock in ideal coherent transfer; its orbital force remains.

For four equally spaced receptions t_i=t0+i Delta, t0>2L, choose

    gamma=(-1,3,-3,1), beta_i=d(t_i-2L)gamma_i.

This follows from canceling the reference columns: gamma annihilates
polynomials of degree<=2, beta a_e=gamma, P is quadratic and
1-a_e/a_r=2HL a_e. Hence sum beta=0 and every initial longitudinal
position, velocity and shared-clock term cancels exactly. Transverse
first-order coefficients vanish in this straight-line reference.

These endpoints form an actual contrast of three proper-time-normalized
counts, not conformal-time counts. If Delta_tau_i is the receiver proper
interval and y_i=(Phi(t_(i+1))-Phi(t_i))/Delta_tau_i, then
l_i=-Delta_tau_i sum_(j<=i)beta_j gives sum l_i y_i=sum beta_i Phi(t_i).

Define F_a^H(s)=sum gamma_i[P(t_i-a)-P(s)]1_(s<t_i-a). Substitution of
the original orbit and clock integrals into (5) yields the chi weights

    W_s=e1(F_2L^H+F_0^H), W_b=-2e1 F_L^H,
    c_s=sum gamma_i[d(t_i-2L)1_(s<t_i-2L)-d(t_i)1_(s<t_i)], c_b=0.

Their zero extensions are compact; W is continuous with W' BV.
Moreover integral c_s=sum gamma_i[d(t_i-2L)(t_i-2L)-d(t_i)t_i]=0.
Thus (1) has no sqrt(mu0) term for this contrast. This exact cancellation
annihilates a constant comparison field chi. A constant physical h instead
has chi=a h and need not be annihilated. Neither is a choice of a homogeneous
physical scalar state or a claim that those constant probes solve the massive
field equation.

If an estimated operator C_hat defines a contrast through C_hat^T l=0,
actual nuisance leakage is l^T(C-C_hat)theta. Without a bound on theta or
exact C=C_hat, a small numerical difference does not give uniform elimination.
Uncertain H, trajectories, clocks and hardware therefore remain application
obligations.

## 8. Exact composition and usable error suppliers

For L=3/5,t_i=7/5+i,Delta=1,T=22/5, the reference massless-propagation Gram
of those curved-count weights is

    G0(H)=(646969H^2-454020H+98700)/(16200pi), 0<=H<5/22.              (6)

It is not the actual massive/curved Gram. To derive it, let z=n.e1 and form

    H_z(tau)=sum gamma_i {
        [d(t_i-2L)+z d(tau)]1_(tau<t_i-2L)
       +[-d(t_i)+z d(tau)]1_(tau<t_i)
       -2z d(tau+Lz)1_(tau<t_i-L-Lz)}.

Sum all three path contributions before squaring. Each coefficient is affine
in tau and every interval endpoint is affine in z. Outer pieces vanish by
the gamma moments. Their order changes only at z=+/-2/3. Exact polynomial
integration in tau and then on the three z intervals gives (6) through
G0=(4pi)^(-1) integral dz integral H_z^2 d tau.
At H=0 this is329/(54pi), the squared energy-dual norm of the difference of
the two flat channels.
Independent event/interval and original trajectory/clock checks are distinct
from inserting (6) into its own test.

Conservative analytic suppliers, all at common epoch0, are

    C0=0, C<=16L+8HL Delta=9.6+4.8H,
    Wsum<=24, Wp=sum||W'||1<=16, V_F<=32+16H.

For each F_a, its derivative is -d(s)sum gamma_i1_(s<t_i-a).
The step function has L1=4Delta and TV=8. Its support length is3Delta,
so ||F'||1<=4Delta, TV(F')<=8+4HDelta and, using both zero traces,
||F||1<=(3Delta/2)||F'||1<=6Delta^2. Summing the four copies gives
the stated force suppliers. Decomposing c_s into
sum gamma_i d(t_i)[1_(s<t_i-2L)-1_(s<t_i)]
+2HL sum gamma_i1_(s<t_i-2L) gives C. All participating times are
nonnegative and HT<1, so 0<d<=1.

The clock sits at the spatial origin. Thus D+M<=2TC+Wsum and E<=TWsum.
For the stationary reference, G_F,V_R<=Wp and R_L<=Wsum.
Equations(1),(4) become the fully explicit functions implemented by
propagation_enclosure. No quadrature or fitted field value enters them.

For B=16, the following H values are synthetic in the declared time units:

| H | sqrt(G0) | epsilon_mass | epsilon_U | Total error bound / sqrt(G0) |
| --- | --- | --- | --- | --- |
| 0.00001 | 1.39257 | 0.00098185 | 0.00001125 | 0.00071314 |
| 0.0001 | 1.39228 | 0.00987757 | 0.00035585 | 0.00735012 |
| 0.001 | 1.38940 | 0.10066077 | 0.01128624 | 0.08057237 |
| 0.01 | 1.36066 | 1.06801545 | 0.37040972 | 1.05715289 |
| 0.05 | 1.23494 | 5.93795881 | 6.13170055 | 9.77351191 |

The last two rows do not certify a small correction. Keeping that failure
visible is part of the result; the theorem does not assume HT is small.

Together with (3), any genuinely scalar contrast residual r with justified
projected error e would imply

    E_phys >= Q lambda_- max(0,|r|-e)^2 /
                       [sqrt(G0)+epsilon_mass+epsilon_U]^2.        (7)

Restore the known scalar/count coupling in the denominator when it has not
been absorbed into r. Zero coupling or zero denominator requires feasibility
handling. Actual r,e,Q,H,B, instrument coefficients and an independent upper
energy budget are not supplied by (7).

## 9. Checks, provenance and surviving gaps

The primary runner calls three helpers, declares its source inputs and writes
source-bound results below outputs/scalar_mass_curvature_count. It reads no
external scientific files or observation data. Helpers carry the same
180second cap; one primary cache binds the note, runner and helper bytes.

Controls cover real-field energy normalization, moving-path quotient
derivatives and integration by parts, massive original coherent phase versus
derived weights, exact radial constants, shared-field interference, exact
curved-field and clock transformations, energy eigenvalues, original
orbit/clock ODEs versus curved weights, initial-data cancellations, exact
Gram polynomial integration, potential-mode bounds, the Bogoliubov derivative
suppliers and the explicit conservative enclosures. Finite quadrature and
ODE results are diagnostics, not interval certificates. Plane waves used
as local probes are not claimed to have finite global energy.

The original working notes and controls remain immutable in the campaign
physical_bridge pack. Independent pre-exposure derivations, later source
comparisons and canonical adaptation records remain separate. The sharpened
clock/force split and constant-offset refinement were suggested by a focused
checker and then personally rederived and implemented by the lead author.
No author aggregate suite is counted as an independent mathematical check.
Formal audit and integrated current-main landing validation are not performed
or pre-stated by this proposal.

Derived within the supplied model: the positive-mass correction, the
curvature-shifted propagation mass, the exact clock-weight transformation,
the initial energy conversion, the count contrast and its response weights,
and the conditional energy requirement. Eliminated as a shortcut: universal
massless upper-Gram substitution for arbitrary separated clocks.

Still surviving: action/potential selection, actual vacuum/environment,
nonlinear and sourced history, absolute scales, realistic calibration and
error budgets, tensor/matter completion, and a physical field-energy upper
bound. Arbitrary finite-energy scalar initial data remain allowed rather than
selected. A unique actual scalar history and a TOE have not been derived.
