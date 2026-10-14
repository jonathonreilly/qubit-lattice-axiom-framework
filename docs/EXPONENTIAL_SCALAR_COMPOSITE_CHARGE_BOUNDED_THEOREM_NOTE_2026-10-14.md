# Deriving the scalar charge of complete matter bodies

Status: conditional support.
Claim type: bounded_theorem.
Scientific author: /root.
Primary runner: `scripts/exponential_scalar_composite_charge_check.py`.

Observed universality of weak free fall motivates checking the source trace,
rather than assigning a pressure-negligible mass or a body charge. Complete
stress conservation removes the pressure restriction for leading massless
stationary monopoles. Finite range retains a weighted stress moment. For
time-dependent conserved sources, a finite-window endpoint estimate replaces
stationarity only for a signed average of the source-generated amplitude.

The [supplied action](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md)
and [local normalization](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md)
remain premises. Universal conformal coupling is not derived from a differential
null. Local flatness, weak fields and controlled ambient response are explicit.
The formal massless operator does not select a massless candidate parameter.
The following are full personal derivations, with preserved version references.

## Composite stress and the scalar mass bridge

Scientific author: /root. This is a new personal derivation in the existing
observations-first campaign. Universal weak free fall motivates testing whether
the earlier pressure-negligible source premise is necessary. The supplied
universal conformal matter coupling is still a premise; an experimental null
does not derive exact universality or the complete action. The Laue mechanism
below is established stress-conservation physics, not a novelty claim.

### 1. Explicit local and perturbative domain

Use the supplied action's consistent scalar channel, canonical coordinate chi,
kinetic term -Q (partial chi)^2, and matter action Sm[A(chi)^2 g,matter].
At a constant ambient state write beta=d ln A/d chi, q=beta^2, Q>0,
GE=1/(8 pi Q), and mu^2=Y_chichi>=0. Freeze those coefficients. Work to leading
order in weak gravitational and scalar perturbations, on a local flat background
whose curvature, background evolution and field gradients can be neglected.
No global Minkowski vacuum for the supplied positive vacuum energy is asserted.

The unperturbed body is complete, isolated, stationary, and in its rest frame.
Its symmetric stress tensor has partial_j T^{ij}=0, rho=T^{00}, S=sum_i T^{ii},
and total energy Ebody=integral rho d^3x>0. It is compact or decays so that all
integrations by parts and multipole expansions below are valid. Containers,
support stresses and binding matter must be included. External clamps, omitted
walls, significant self-gravity/scalar binding, time dependence, quantum trace
effects not represented by the complete supplied matter stress, and a strong
ambient profile are outside this leading calculation. A stationary conserved
stress is conditional data, not a derived equation of state or realized body.

Subtract the ambient field equation before linearization: rho and S below
are the compact excess body stress. Constant or slowly changing background
terms are removed in that subtraction; neglected variations require a local
scale separation. This does not assert an arbitrary constant field solves the
full supplied action. At this order, body-induced changes in beta times its
source are of higher weak-source order. The ambient region must additionally
be matter-free, or its linear trace response must have an independently justified
negligible effect on the stated local scales. Subtraction alone does not establish
this: a retained ambient trace Tbg contributes -beta_chi Tbg/(2Q) to the squared
restoring mass, and an ambient material perturbation contributes
-beta deltaTbg/(2Q) to the linear equation. Such responses cannot in general
be replaced by the vacuum Y_chichi used here. No ambient-density selector or
response law is derived. Varying the action under this explicit scope gives

    (Delta-mu^2) delta_chi = beta (rho-S)/(2Q).

The sign and factor 2 follow from the -Q kinetic normalization, not the
more common -Q/2 convention. The leading matter trace is -rho+S.

### 2. Massless monopole from conservation

Integrating partial_k(x^i T^{kj}) gives the Laue identity

    integral T^{ij} d^3x = 0,      integral S d^3x = 0.

Consequently the scalar monopole is

    Qscalar(0)=integral(rho-S)d^3x=Ebody.

The mu=0 result is a formal massless local-operator limit; it does not select
a zero-mass member of the supplied positive-parameter potential. Its leading
long-range use for mu>0 also requires R<<r<<1/mu and the stated local/background
control. No pointwise pressure approximation or barotropic law is needed. The static
massless Green function therefore gives, at leading monopole order,

    delta_chi = - beta GE Ebody/r + higher multipoles.

The linearized Einstein equation gives its monopole from integral(rho+S)=Ebody;
the integrated spatial stresses likewise vanish. Thus, in the local asymptotic
monopole zone, the two Jordan potentials obey

    Psi_J = - GE Ebody (1+q)/r,
    Phi_J = - GE Ebody (1-q)/r,
    gamma = (1-q)/(1+q).

Here g00=-(1+2 Psi) and gij=(1-2 Phi)delta_ij in isotropic weak coordinates.
These are leading long-range potentials, not an automatically valid spacecraft
time-delay likelihood, finite-range PPN fit, or nonlinear matched Solar solution.

With ambient Ainf constant, rJ=Ainf rE and Ebody=Ainf MJ. The common potential
coefficient becomes Gbare MJ/rJ, where Gbare=Ainf^2 GE. MJ is the body's total
local inertial energy in Jordan units, not a previously assigned sum of rest
masses. This derives the leading mass conversion for this weak isolated body.

For an external scalar gradient nearly constant across a weak test body,
partial_mu T^{mu i}=beta T partial_i chi gives the integrated force
F_i=-beta Ebody partial_i chi. Thus the acceleration has the same leading beta
for complete stationary test bodies. Under these premises a massless common
scalar changes universal attraction, but produces no leading differential
acceleration between two such bodies. Weak-equivalence-principle null results
alone therefore do not bound this common q. Finite experimental precision does
not establish the premises. Finite-size tidal, self-binding, composition-specific
coupling or environmental corrections must be separately calculated.

### 3. Finite range: the surviving stress moment

For a spherically symmetric source supported in r<=R, define

    f(r)=sinh(mu r)/(mu r), with f=1 at mu r=0,
    Qscalar(mu)=integral f(r)(rho-S) d^3x.

The exact exterior solution of the frozen linear scalar problem is

    delta_chi(r)=-beta GE Qscalar(mu) exp(-mu r)/r,  r>R.

Weighted integration by parts gives

    integral f S = - integral r f'(r) Trr,
    Qscalar(mu)=integral [f rho+r f' Trr] d^3x.

Indeed partial_j(f x_i T^{ij})=f S+r f' Trr under stress conservation.
The unweighted cancellation does not imply weighted cancellation. At fixed
compact stress profile the small-mass expansion is

    Qscalar(mu)/Ebody = 1 + mu^2/(6 Ebody)
        integral r^2 (rho+2 Trr) d^3x + O(mu^4).

The equivalent weighted virial relation is integral r^2 S=-2 integral r^2 Trr.
Finite-range scalar charge therefore depends on a stress moment not determined
by total mass or the unweighted Laue identity.

If the additional pointwise inequalities rho>=0 and |Trr|<=rho hold, then

    2 sinh(x)/x-cosh(x) <= Qscalar(mu)/Ebody <= cosh(x),  x=mu R.

The proof uses f+r f'=cosh(mu r), f-r f'=2f-cosh(mu r).
The first is increasing and the second decreasing for nonnegative argument:
the latter has power coefficients (1-2n)/(2n+1)! for n>=1. This is a conditional
bound, not a derived energy condition. Its lower bound can be negative at large
x. Neither positive density nor conservation alone lets us reuse the earlier
positive-source Yukawa-kernel bounds for the signed trace source.

For a pointlike weak test body outside the sphere, the scalar/Newton force ratio
is q [Qscalar(mu)/Ebody](1+mu r)exp(-mu r), relative to the
bare metric Newton acceleration GE Ebody/r^2. A finite test body requires its own
spatial response; a published constant-gamma bound cannot simply be substituted.

### 4. Explicit conserved synthetic stress family

Take R=1, rho=rho0>0 inside, zero outside, and

    pr=p0(1-r^2)^2,
    pt=pr+(r/2)pr'=p0(1-r^2)(1-3r^2).

Radial conservation pr'+2(pr-pt)/r=0 holds, including the regular center limit.
The radial traction vanishes at the outer boundary, so no missing surface force
is introduced. The density jump has no static spatial-divergence contribution.
For p0/rho0 in {-2/5,0,2/5}, |pr| and |pt| are bounded by rho0. These examples
have the same Ebody and exactly zero integrated S, yet different finite-mu charge.
They are admissible conserved stress fixtures, not derived material equilibria.
An arbitrary overall small density scale can ensure weak self-gravity; it does
not select an observed body's density, rigidity or microscopic state.

A constant isotropic pressure inside a sharp sphere with no wall is a control
that violates isolation/conservation at its boundary. Its nonzero integral S
cannot be used as a counterexample to the complete-body theorem. The missing
boundary force is precisely the failed premise.

### 5. Remaining imports and evidence roles

Retired within the stated massless leading domain: pointwise negligible pressure
as a condition for scalar-charge/total-inertial-mass equality. Derived conditionally:
the universal leading composite-body charge, Jordan mass conversion, finite-range
weighted stress identity and a bound under an additional radial stress inequality.
Still supplied: the universal A, the action and canonical channel, background,
range, coupling/scale, a complete conserved stationary stress, weak-field/local
validity and experimental response model. No equation of state, body history,
action selector or independent observed fit is derived.

The protocol's synthetic stress cases test algebra and Green-function matching.
Any cited MICROSCOPE result is exposed observational context, not a calibration,
held-out test, new likelihood, or numerical limit on a universal scalar q.

## A finite observation window without a stationary matter state

Scientific author: /root. The static composite-body result is useful, but real
observations average over finite windows. This block asks which part of its
stationary-state premise can be replaced by exact conservation and endpoint
bounds. It derives only a source-generated massless scalar amplitude, not a
complete observed force or a selected radiative state.

### 1. Local premises and exact instantaneous identity

Use the same supplied universal conformal coupling and kinetic normalization as
the composite-stress derivation, with constant beta, GE=1/(8 pi Q), weak source
and a local flat background. The massless scalar equation is the formal mu=0
local-operator limit, not a selected massless member of the supplied potential.
Ambient matter response and metric/scalar backreaction are neglected under the
same explicit scope. This calculation does not establish their smallness.

On a finite time band, a complete symmetric matter tensor obeys
partial_mu T^{mu nu}=0 and has support in a fixed ball |x|<=R. Define
rho=T00>=0, j_i=T0i, S=sum_i Tii, E=integral rho d^3x>0 and
I(t)=integral |x|^2 rho(t,x)d^3x. Assume smoothness/decay sufficient for the
following operations and the pointwise component bounds |j|<=rho and
|Tii|<=rho for each i. These inequalities and confinement are declared physical
conditions, not consequences of scalar field dynamics or a derived body state.
Conservation and vanishing surface flux give constant E and

    I'=2 integral x dot j,
    I''=2 integral S,
    Qinstant(t)=integral(rho-S)=E-I''/2.

This is exact matter kinematics in the stated local model. Without stationarity,
the instantaneous integrated scalar trace need not equal energy. It is not yet
the retarded radiative monopole.

For any window [t0,t1] of length T>0,

    Qinstant_bar/E = 1-[I'(t1)-I'(t0)]/(2 E T),
    |Qinstant_bar/E-1| <= 2 R/T.

The bound follows from |I'|<=2RE at both endpoints. No initial phase, periodicity,
relaxation, infinite past or ergodic distribution is required. Restoring units
replaces R/T by R/(c T). This controls an integral of the source, not a direct
finite-distance instrument observable.

### 2. Retardation must be included

The retarded contribution from the specified finite-band worldtube |x|<=R has leading far-zone amplitude

    delta_chi(t,r n)=-beta GE F(u,n)/r+O(r^-2),  u=t-r,
    F(u,n)=F_R(u,n)=integral_{|x|<=R} [rho-S](u+n dot x,x) d^3x.

The large-r expansion assumes compact smooth source on the required retarded
band and sufficient temporal regularity; it is a local flat radiation problem.
The total local solution may include an arbitrary homogeneous or incoming scalar wave. Radiation generated by an earlier or outside source history can also supply this boundary data. Finite-band confinement alone does not determine that global history or the full globally retarded field. F_R denotes only the explicitly specified local-worldtube contribution. Its definition does not derive or eliminate the initial/boundary freedom.

For [u0,u1], use the extended source band [u0-R,u1+R]. The shifted window at
each x differs from the unshifted window only inside endpoint bands of width2R.
Since |rho-S|<=4rho and integral rho(t,x)d^3x=E at every common time,

    |integral_u0^u1 F du - integral_u0^u1 Qinstant du| <=16 E R.

Each of the two endpoint bands contributes at most 4E times2R. Combining the
instantaneous endpoint bound yields the conservative, not sharp, result

    |Fbar/E-1| <=18 R/T.

It holds uniformly in direction n. The bound concerns a signed time average
of the leading scalar source amplitude, not its absolute value, fluctuations,
derivative, scalar energy flux, force, gamma or differential acceleration.
In particular, averaging away an amplitude correction does not bound radiation
power. No constraint on an added homogeneous wave follows. The source need only
satisfy the conditions on the finite extended band, not for an assumed infinite
bounded history.

### 3. A fully conserved time-dependent fixture

Inside R=1 let h(r)=(1-r^2)^m, m>=3, and set it to zero outside. Choose

    rho=rho0+epsilon cos(omega t) Delta h,
    j=epsilon omega sin(omega t) grad h,
    Tij=-epsilon omega^2 cos(omega t) h delta_ij,

with rho0 constant inside the ball and zero outside. Both conservation equations
hold exactly, including absence of boundary distributions because h, its first
derivative and its needed limiting second derivatives vanish at r=1 for m>=3.
The constant base density has no spatial stress/energy flux. This is a conserved
stress fixture, not an equation of state, microscopic material, causal evolution
construction or a demonstrated stable body.

Its energy is E=4 pi rho0/3. With H0=integral h d^3x,

    I=Ibase+6 epsilon cos(omega t) H0,
    Qinstant=E+3 epsilon omega^2 cos(omega t) H0.

The retarded angular integral is spherical and uses sinc(omega r). Define
Hk=integral h(r) sinc(omega r)d^3x. Integration by parts against the regular
Helmholtz wave gives integral Delta h sinc=-omega^2 Hk. Therefore

    F(u)=E+2 epsilon omega^2 cos(omega u) Hk.

The coefficients3 and2 are different even in the small-frequency leading
nontrivial correction. Replacing retarded source time by a common instant
before calculating that correction gives the wrong result. Neither coefficient
is an empirical fit.

For the protocol m=3, rho0=1, epsilon=1/1000, omega<=2, elementary bounds give
|Delta h|<=6m+4m(m-1)=42, |grad h|<=2m=6, h<=1. Hence rho>=0.958,
|j|<=0.012, and each |Tii|<=0.004, establishing the component inequalities
uniformly in time. Finite-window integrals can be computed exactly from sine
endpoint differences, with no assumed random phase.

### 4. Assumption accounting

Conditionally replaced: stationarity for sufficiently long signed averages of
the source-generated massless far-zone amplitude, by finite-band conservation,
confinement and explicit component inequalities. The theorem supplies its own
finite-window error rather than inserting a phase or ensemble distribution.
Still supplied: the action/coupling, weak local massless approximation, source
confinement, stress inequalities and complete material tensor. An arbitrary
homogeneous wave, absolute scales, matter realization and actual measurement
response are still free. The finite-band condition does not derive a globally
bounded cosmological history. No observation likelihood or state selection is
claimed; the fixtures are mathematical development data.

## Computational evidence and physical interpretation

The canonical calculation preserves137 static and98 dynamic controls,235 total.
Static fixtures have15 source/range cases plus direct angular Green checks.
Dynamic fixtures have9 instantaneous/retarded cases and9 finite windows. All
source coefficients, pressure profiles, frequencies and observation windows are
synthetic development choices. Their complete values, results and actual damaged
programs remain in the recovery archive; they are not measurements or a fitted
material law. The analytic inequalities, not finite samples, establish the
theorem's domain. Counts are implementation assertions, not experiments.

The earlier static hand versions omitted an explicit condition on ambient linear
matter response. Subtracting an ambient equation removes its zeroth-order source,
not that response. The complete v1/v2 texts, exact diffs and v3 scope repair are
retained. No changed equation or relaxed tolerance is used to hide that premise.

[MICROSCOPE](https://arxiv.org/abs/2209.15487) is exposed observational motivation.
The archived context records the accessed source, its identity and limits.
No raw telemetry, instrument likelihood or independently reserved test is used.
The ideal massless universal response is common to complete weak test bodies;
this calculation does not convert a differential null to a bound on common q.

The stationary result concerns total inertial energy, including all supports.
The finite-range bounds require additional stress inequalities and can have an
uninformative negative lower edge. A finite-radius test body and actual apparatus
need their own response calculation. The dynamic bound concerns only a signed
source-amplitude average; it does not bound its fluctuations, derivatives,
radiation power, a measured force or an arbitrary homogeneous scalar solution.
No source realization, globally bounded cosmological history, chosen initial
state, complete action, scale or observed confidence region is derived.

Recovery: `docs/work_history/physics/revised-scalar-composite-charge-20261014/README.txt`.
