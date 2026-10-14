# Thermal charge bounds and a conditional scalar bounce test

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_thermal_bounce_check.py](../scripts/exponential_scalar_thermal_bounce_check.py)

The complete supplied scalar action is in the
[future-confinement note](EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md).
The [physical-past and calibration note](EXPONENTIAL_SCALAR_PHYSICAL_PAST_BOUNDED_THEOREM_NOTE_2026-10-14.md)
supplies the conditional local-gravity ceiling and negative-u energy monotonicity.
Neither dependency derives the action, particle content, state or measured environment.

Massive particles and thermal transitions challenge a perfectly conserved
radiation-fluid charge. The result below derives what universal metric coupling
actually conserves, then replaces the traceless-fluid assumption with continuous
finite-mass thermodynamics for a specified ideal electromagnetic bath. Its
maximum charge-growth factor is too small to evade the stated Einstein-bounce
bare target. Positive measured-gravity calibration must be kept explicit. Part IV links
bounce pressure to the thermal entropy and strengthens the calibrated bound
within its stated same-background regime. No observed abundance, spectrum or likelihood is fitted.

The four proof parts have separate equation numbering. Radiation charge means
rho*a^4 for the explicitly chosen component; it is conserved only under the
conditions derived below. The source-normalization conversion, matter content,
equilibrium/isolation and any entropy production remain distinct premises.

## I. Conformal conservation and the thermal endpoint budget

Direct derivation by /root. The past-history theorems explicitly assume a
positive separately conserved radiation charge. This block asks how much of
that premise follows from the supplied universal matter action. The observed
existence of massive particles and thermal transitions makes this a real
applicability question; a one-component w=1/3 fluid is not automatically the
whole early-universe matter sector.

### What the universal metric coupling fixes

Let g_J=A^2g_E, C=A^2, dt_J=A dt_E, a_J=A a_E,
L=dot(A)/A=b.dot(phi), H=H_E, Z=H+L and H_J=Z/A.
For an isotropic component i, define a Jordan energy-exchange density Q_i,J by

    d rho_i,J/dt_J + 3 H_J(rho_i,J+p_i,J)=Q_i,J.

Total on-shell matter diffeomorphism invariance gives sum_i Q_i,J=0 when the
split includes all interacting matter components and no external source.
It does not individually set every Q_i,J to zero. With
rho_i,E=A^4rho_i,J, p_i,E=A^4p_i,J, direct differentiation gives

    dot rho_i,E+3H(rho_i,E+p_i,E)
      =L(rho_i,E-3p_i,E)+A^5 Q_i,J.                  (1)

The trace term is fixed by the conformal coupling. Internal transfer is a
property of the specified matter interactions and state, not fixed by A
alone. The factor A^5 matters: Q_i,J is per physical proper time and volume.
For an exactly traceless component, p_r=rho_r/3, define the frame-invariant
radiation charge

    D_r=rho_r,E a_E^4=rho_r,J a_J^4.

Then

    dot D_r=a_E^4 A^5 Q_r,J,
    d D_r/dt_J=a_J^4 Q_r,J.                          (2)

For a component or whole bath that is not exactly traceless, the same charge
expression D_i=rho_i,J a_J^4 instead obeys the exact general identity

    dD_i/dt_J=a_J^4[H_J(rho_i,J-3p_i,J)+Q_i,J].       (2a)

This follows by differentiating D_i and inserting the component continuity
equation. At a massive threshold the total bath may have Q_total,J=0 but
rho_total-3p_total!=0, so its charge can grow. That is consistent with (2),
whose absence of a trace term required p_r=rho_r/3. It is not a direct
scalar-to-photon production rate. The focused independent check highlighted
this distinction; the author added this explicit derivation to make the
endpoint thermodynamic calculation's intermediate assumptions visible.

An isolated classical tracefree sector has Q_r,J=0, so D_r is conserved.
This is a derived consequence conditional on isolation and tracelessness.
The bare gravitational action does not derive a thermal distribution,
radiation abundance, entropy constant, particle masses or the separate
absence of transfer. Quantum anomalies, nonrelativistic thresholds and
interactions require their actual stress tensors and microscopic inputs.

For a decoupled massive component Q_i,J=0, equation (1) still has a trace
source in Einstein time. That source is a frame conversion, not by itself
creation of photons. A scalar force sourced by a thermal trace must not be
counted as a radiation-production rate without a component exchange model.

### Inverse bookkeeping is not an interaction law

In a Jordan dust/radiation split with rho_d,rho_r>=0, choose an actual
interaction rate J(t_J) and let Q_r,J=J,Q_d,J=-J. Then

    dot_J rho_r+4H_J rho_r=J,
    dot_J rho_d+3H_J rho_d=-J.

The sum always obeys total conservation. Conservation alone allows an
infinite family of such transfer histories and does not determine J or its
sign. A nonnegative J can be sustained only while the source reservoir and
its dynamics support it. Specifying J=Gamma rho_d introduces Gamma and a
microscopic interaction assumption; it is not a derivation from diffeomorphism
invariance. Inferring J from a supplied history is a reconstruction, not a
prediction of that history.

If a positive radiation charge changes between two events, let
zeta=D_r,f/D_r,b. In an Einstein-bounce setting with fixed positive curvature
and f_b=rho_r,b/(3Q kappa_b)<1/2, the endpoint identity becomes

    d_J,f F_bare,f=(a_E,f/a_E,b)^2/(f_b zeta).         (3)

A target d_J,f<=epsilon, F_bare,f<=1+delta therefore requires

    zeta >= exp(2N)/[f_b epsilon(1+delta)],
    N=log(a_E,f/a_E,b).                              (4)

This uses the initial bounce bound and endpoint identities, not conserved
radiation in between. It supplies a necessary charge budget, not a source.
If other energy conditions, the target calibration or radius ordering change,
they must be checked explicitly. Here N>=0 for the radius-growing use case.

### Equilibrium entropy supplies a conditional endpoint budget

Adopt a thermal endpoint definition in physical units, zero chemical potentials,
and a comoving entropy S=s_J a_J^3 for a specified bath:

    rho_J=(pi^2/30)g_* T^4,
    s_J=(2pi^2/45)g_*s T^3.

Eliminating T and a_J shows

    D=rho_J a_J^4
      =(pi^2/30)(45/(2pi^2))^(4/3)
        [g_*/g_*s^(4/3)] S^(4/3).

Thus between endpoint thermal states

    zeta=(g_*,f/g_*,b)(g_*s,b/g_*s,f)^(4/3)
          (S_f/S_b)^(4/3).                          (5)

If both endpoints have all bath species ultrarelativistic at one common
 temperature, g_*=g_*s=g, and

    zeta=(g_b/g_f)^(1/3)(S_f/S_b)^(4/3).             (6)

An adiabatic transition with S_f=S_b can increase D even though total
matter conservation holds; assuming D constant across a change in degrees
of freedom would silently strengthen the model. Conversely, a large required
zeta cannot be supplied by an arbitrarily small change in g. Combining
(4) and (6) gives the necessary entropy condition

    S_f/S_b >= [exp(2N)/(f_b epsilon(1+delta))]^(3/4)
                (g_f/g_b)^(1/4).                   (7)

Endpoint chemical potentials, species out of equilibrium, different bath
temperatures and conserved charges require the corresponding thermodynamic
relations; (5)–(7) are not universal entropy theorems.

### Ideal electron-positron/photon illustration and a split-sector warning

For a supplied isolated equilibrium electromagnetic bath well above the
electron mass, photon spin states contribute2 and electron/positron states
contribute(7/8)*4, so g_b=11/2. Well below the mass, g_f=2. With ideal adiabatic
annihilation and negligible remnant pair abundance,

    zeta_total_bath=(11/4)^(1/3).                     (8)

If instead D refers only to the photon component at both ends, the same
entropy calculation yields

    zeta_photon=(11/4)^(4/3).                         (9)

The degrees-of-freedom values are ideal ultrarelativistic/nonrelativistic
endpoint limits, not exact finite-temperature values at a specified T/m.
Finite-mass endpoint corrections require their actual distributions.

These are different charges. The initial bounce fraction f_b in (3) must
refer to the same component used for zeta; one cannot combine a total initial
radiation fraction with the larger photon-only factor. Massive pairs near
threshold are not exactly traceless radiation; the endpoint construction and
energy transfer explicitly replace that intermediate assumption.

This illustration does not model neutrino decoupling, QED corrections, nuclear
reactions, a complete standard-model species history, a scalar-induced decay,
or measured light-element abundances. It introduces the specified observed
particle sector and a chosen thermal state as inputs; neither is selected by
the candidate gravity action. The fixed charge budget makes a proposed repair
checkable without declaring a freely supplied production law to be derived.

## II. Continuous finite-mass bath and Einstein bounce

Direct scientific author: /root. This addresses a specific physical loophole in
the separately conserved radiation assumption: observed massive pairs are not
traceless through annihilation. No microscopic matter theory, equilibrium state,
interaction rate, entropy abundance or initial history is selected here.

### Adopted matter sector and exact thermodynamics

Use the same supplied universal physical metric g_J=A^2 g_E. Adopt an ideal
isotropic photon plus electron/positron bath, common positive physical T,
zero chemical potentials, two photon and four fermion spin states, fixed
physical pair mass m>0, and distributions f_gamma=(exp(p/T)-1)^-1 and
f_e=(exp(sqrt(p^2+m^2)/T)+1)^-1. The particle content, mass and distributions
are matter inputs. The gravity action by itself does not imply equilibration.
The standard distribution, stress and entropy definitions are given in PDG's
2025 Big-Bang Cosmology review, Eqs22.35–22.42; the distinct equilibrium-rate
condition is discussed in Eq22.45. This source is exposed development context,
not a likelihood or evidence that this candidate satisfies the rate condition.
https://pdg.lbl.gov/2025/reviews/rpp2025-rev-bbang-cosmology.pdf

For x=m/T, y=p/T, Ehat=sqrt(y^2+x^2), and f=(exp(Ehat)+1)^-1, write

    rho_J=T^4 r(x),       p_J=T^4 P(x),
    r=pi^2/15 + (2/pi^2) integral_0^infinity y^2 Ehat f dy,
    P=pi^2/45 + (2/(3pi^2)) integral_0^infinity y^4 f/Ehat dy.

Positive integrands give 0<p_J<=rho_J/3. The exact trace is

    rho_J-3p_J = (2m^2/pi^2) integral_0^infinity p^2 f_e/E dp >0

at any finite m,T>0. Differentiating at fixed physical momentum gives

    rho_T = 4pi^2 T^3/15
       +(2/(pi^2 T^2)) integral_0^infinity p^2 E^2 f_e(1-f_e) dp >0.

Integration by parts, with vanishing endpoint terms, yields p_T=(rho+p)/T.
Let s=(rho+p)/T. Differentiating this relation gives s_T=rho_T/T. These
identities include the continuous finite-mass transition; no step in g is used.
All derivatives here vary physical T at fixed m and fixed matter definitions.

### Isolation derives entropy conservation within equilibrium

For a bath with Q_total,J=0, physical continuity is
rho_T dot_J T+3H_J(rho+p)=0. Therefore

    dot_J(s a_J^3)=a_J^3[rho_T dot_J T/T+3H_J s]=0.

The positive constant S is an unselected integration constant. Isolation and
reversible local equilibrium imply its conservation, not its value. Departure
from equilibrium, chemical potentials, dissipative entropy, changing masses or
external transfers require new equations. No collision-rate check has been
performed to establish equilibrium for a candidate bouncing trajectory.

Define D=rho_J a_J^4=rho_E a_E^4 and G(T)=rho/s^(4/3). With fixed S,
D=S^(4/3)G(T). Exact differentiation gives

    d ln G/dT = rho_T (3p-rho)/[3rho(rho+p)] <=0.       (1)

The asymptotic ideal gas integrals give effective weights g_hot=11/2 and
g_cold=2. Thus G is between its hot and cold limits, whose ratio is

    R=G_cold/G_hot=(11/4)^(1/3).                      (2)

For any two finite positive temperatures on one fixed-entropy history,

    1/R <= zeta=D_f/D_b <= R.                        (3)

The weak endpoint inequalities suffice; neither a temperature ordering nor
monotone physical expansion is needed. A nonmonotone scalar conformal factor
does not defeat (3), because the charge is exactly frame invariant. For this
ideal m>0 gas finite endpoint bounds are strict, but the proof below only uses
weak bounds. The numerical integral grid checks the formulas; monotonicity
and the analytic limiting integrals establish the uniform statement.

### Einstein-bounce inequality with a traceful bath

Let Q>0 be the gravitational coefficient, w_phi=|dot phi|_K^2>=0,
kappa=Kc/a_E^2, and let other nonbath matter satisfy rho_o+p_o>=0 at a strict
Einstein bounce H_E,b=0, dot H_E,b>0. The action has scalar kinetic energy
Q w_phi, without a 1/2 in its kinetic Lagrangian. Raychaudhuri is

    dot H_E=kappa-w_phi-[rho_B,E+p_B,E+rho_o+p_o]/(2Q).

All bath stresses transform with the same positive A^4, so w_B=p_B/rho_B
is frame invariant and nonnegative. At the bounce,

    kappa_b > rho_B,b(1+w_B,b)/(2Q),
    f_B,b=rho_B,b/(3Q kappa_b) < 2/[3(1+w_B,b)] <=2/3. (4)

This derives positive Kc directly from Raychaudhuri and the positive bath.
Unlike the traceless radiation bound, no p_B=rho_B/3 assumption is made.
No special form or height of the scalar potential is used in this step.

At a later event with Z_f=H_E,f+dot A_f/A_f nonzero, define

    d_J,f=kappa_f/Z_f^2,
    F_bare,B,f=3Q Z_f^2/rho_B,E,f,
    N=ln(a_E,f/a_E,b).

The same total bath must be used in f_B and zeta. Endpoint kinematics gives

    d_J,f F_bare,B,f = exp(2N)/(f_B,b zeta)
      > [3(1+w_B,b)/(2R)] exp(2N)
      >= [3/(2R)] exp(2N).                           (5)

For this bath, (3/(2R))^3=27/22>1. Consequently every such Einstein bounce
and later event with a_E,f>=a_E,b obeys d_J,f F_bare,B,f>1. It cannot reach
a target d_J,f<=epsilon and F_bare,B,f<=1+delta with epsilon>0, delta>=0
and epsilon(1+delta)<=1.
The ideal pair threshold alone therefore cannot remove this specific bound.
This is a conditional mathematical obstruction, not a likelihood exclusion.
It concerns the bare cosmological normalization and a total-bath diagnostic;
it is not automatically a bound on a photon-only or measured-G radiation law.

For a finite set of ideal equilibrium species at fixed masses and zero chemical
potentials, the same positive-trace/heat-capacity argument gives R=(g_hot/g_cold)^(1/3),
provided some massless species remain and the same bath is isolated. The coarse
bounce obstruction with N>=0 is guaranteed whenever R<=3/2. For a larger
ratio it is not guaranteed by this estimate; that does not construct a repair.
An externally allowed entropy increase sigma=S_f/S_b multiplies the maximum
charge ratio by sigma^(4/3). A necessary escape budget becomes

    sigma > [3 exp(2N)/(2R epsilon(1+delta))]^(3/4),   (6)

using the strict bounce inequality and the positive target product
epsilon(1+delta)>0. If that product is nonpositive, the positive diagnostic
product already makes the target impossible; no finite budget expression is
asserted there. Specifying sigma is not a production law.
For different measured-gravity normalizations the additional calibration factor
must be inserted before any observational assertion.

### Scope of the progress

Within a stated matter sector, constant D has been replaced by the derived
finite-mass charge range, and the restricted Einstein-bounce obstruction still
holds. The result removes the need for exact tracelessness throughout this
particular argument. It retains, and does not derive, isolation, reversible
equilibrium, the particle theory, positive kinetic/enthalpy conditions, radius
ordering and the target epoch/calibration. No full bouncing thermal solution,
reaction network, observed abundance, independent empirical test, general
Jordan-bounce theorem, perturbation stability or quantum origin is established.

## III. Measured calibration and entropy escape budgets

Direct author /root. This is an integration of the finite-mass thermodynamic
bound with the separately checked conditional calibration formulas. It is not
a new local-body solution, a measured calibration, or an empirical likelihood.

Let P_bare=d_J F_bare,B and let G_bare,c=C_c/(8pi Q)>0 at the final
cosmological event. For an actually chosen positive measured normalization
G_cal, define gamma=G_cal/G_bare,c. Then

    F_cal,B=F_bare,B/gamma,      P_cal=P_bare/gamma.        (1)

The finite-mass proof gives P_bare>3 exp(2N)/(2R) at fixed bath entropy,
R=(11/4)^(1/3), with the same total-bath diagnostic at all endpoints.
For different positive entropy constants at the two equilibrium endpoints,
let sigma=S_f/S_b. The endpoint thermodynamic bounds instead give

    zeta<=R sigma^(4/3),
    P_cal>3 exp(2N)/[2R sigma^(4/3) gamma].               (2)

No process that changes sigma is derived. At sigma=1 the original isolated
reversible model is recovered. Eq2 uses the actual bounce cap and thermal
endpoint definitions; it does not require equilibrium throughout an entropy
producing interval, but the interval must still be an actual gravitational
history before this becomes an applicability statement.

### Same-background weak-source calibration

In the previously derived instantaneous weak-source principal limit,
G_pr=G_bare,c(1+q_c), 0<q_c<1/3. The additional nonnegative self-adjoint
constant-mass Yukawa model gives 1<=gamma<=1+q_c for its radial force.
These are specified response regimes, not a theorem for arbitrary bodies,
tachyonic modes, a changing environment, or nonlinear screening.

If an independently justified relative-error ceiling eta>=0 gives
G_cal<=(1+eta)G_pr, then gamma<(4/3)(1+eta) and

    P_cal>9 exp(2N)/[8R sigma^(4/3)(1+eta)].             (3)

The same-background eta=0,sigma=1 coefficient 9/(8R) is below one.
Thus the bare statement P_bare>1 does not by itself imply P_cal>1.
A positive target L=epsilon(1+delta), epsilon>0, delta>=0, requires

    exp(2N) < (8/9) R sigma^(4/3)(1+eta)L.              (4)

When N>=0 and the right-hand side is <=1, the target is impossible under
these explicit calibration assumptions. Otherwise Eq4 is a necessary radius
budget, not evidence that a background solution or an observational fit exists.

### Arbitrary finite calibration background under the principal ceiling

The supplied action's checked coupling identity gives, at any finite local
field point, C_l(1+q_l)<=1+k with 0<k<1/3. If the local measurement is in the
same principal regime with the stated error ceiling, then

    gamma<=(1+eta)(1+k)/C_c.

Combining with Eq2 gives a necessary small-C condition for the positive target:

    C_c<Ccrit,
    Ccrit=2R sigma^(4/3)(1+eta)(1+k)L exp(-2N)/3.        (5)

Neither the relation between local and cosmological states nor the history
that produces either state has been supplied by this inequality. If 0<Ccrit<1,
the previously proved negative-u monotonicity of the scalar potential gives

    rho_phi,E/(2Q Hv^2)>U0(Ccrit),
    U0(C)=3/2+(3s/2)(1-C)^2
       +nu(1+s-sC)^2 log^2[C/(1+s-sC)]/[8a(1+s)].      (6)

Here a=(1-k)(1+3k)/4, s=(1+k)/[k(1-3k)], nu>0 and the full potential has
nonnegative x,y additions. Eq6 is a required scalar-energy cost, not a measured
upper bound or a contradiction. If Ccrit=1, the strict C_c<1 still gives
energy strictly above3/2, but no uniform positive excess above the vacuum
floor is supplied. If Ccrit>1, this argument forces neither C_c<1 nor that
negative-u threshold floor. The choice of k,nu,Hv and an entropy source remains
unselected. The positive-target condition excludes division by a nonpositive
L; a nonpositive target is already impossible because P_cal>0.

All endpoint budgets refer to the specified total electromagnetic bath.
Additional decoupled species, chemical potentials, QED corrections and finite
body measurement effects require their own energy and calibration equations.
The numerical constants below are synthetic evaluations of these exact
coefficients; no data values or fitted errors have been substituted.

## IV. Joint pressure and entropy close the coarse bound gap

Author /root. Conditional derivation frozen before new execution. This uses the existing ideal equilibrium photon/electron/positron bath as an explicit matter premise, not a derived particle theory or observed fit. It improves the earlier separately maximized bounce and charge bounds. All earlier bounds remain valid but need not be sharp.

### Inputs and observation-facing target

On a strict Einstein-frame bounce, positive scalar kinetic energy and nonnegative other-component enthalpy give f_b < 2/[3(1+w_b)] for the selected total bath. The same component is used at the final regular physical event. Write N=ln(a_E,f/a_E,b), D=rho_E a_E^4=rho_J a_J^4, zeta=D_f/D_b, d_J=kappa_E/Z^2 and F_bare=3Q Z^2/rho_B,E. Then P_bare=d_J F_bare=exp(2N)/(f_b zeta). The product target is necessary, not sufficient, for individual observational limits. Positive target Ltar, measured calibration and its error budget are supplied quantities; no data likelihood has been acquired.

The supplied bath has photons (g=2) and massive electron/positron fermions (g=4), zero chemical potential, common positive physical temperature, fixed positive mass, ideal statistics and equilibrium at both endpoints. In the reversible isolated case sigma=S_f/S_b=1, with S=s a_J^3. A separately supplied sigma>0 is an algebraic allowance, not a derived entropy source. The previous finite-mass proof establishes rho_T>0, p_T=(rho+p)/T, s=(rho+p)/T, G=rho/s^(4/3), and G_hot <= G(T) <= G_cold, with R=G_cold/G_hot=(11/4)^(1/3).

### Entropy density bound derived from occupations

Let x=m/T, y=p/T, Ehat=sqrt(y^2+x^2), f=1/(exp(Ehat)+1) and h_F(f)=-f ln(f)-(1-f)ln(1-f). For 0<f<=1/2,

 dh_F/df=ln[(1-f)/f]=Ehat >=0,
 df/dEhat=-f(1-f)<0.

At every y>0, increasing x lowers h_F(f). The dimensionless fermion entropy density is

 s_f/T^3 = g/(2 pi^2) integral_0^infinity y^2 h_F(f) dy.

This equals (rho_f+p_f)/T^4 by integration by parts using h_F(f)=Ehat f+ln(1+exp(-Ehat)); the boundary y^3 ln(1+exp(-Ehat)) vanishes at both limits. Thus h(T)=s/T^3 is bounded above by its massless hot value h_hot=11 pi^2/45. Photon entropy gives the positive cold floor h_cold=4 pi^2/45. Finite x>0 gives h(T)<h_hot. These are inequalities for the assumed equilibrium distribution, not a reason the actual early universe must be in that distribution.

### Joint bound

The Gibbs identity links the two previously separate terms exactly:

 (1+w_b) G_b = T_b/s_b^(1/3) = h_b^(-1/3).

Since zeta=sigma^(4/3) G_f/G_b,

 f_b zeta < (2/3) sigma^(4/3) G_f h_b^(1/3)
             <= (2/3) sigma^(4/3) G_cold h_hot^(1/3)
             = (R/2) sigma^(4/3).

The final equality uses G_hot=(3/4)h_hot^(-1/3). No ordering of endpoint temperatures, no monotonic A, and no fitted scalar initial point is required. The strict bounce gives strictness. The endpoint bounds alone do not establish a full history approaching equality.

Therefore

 P_bare > [2/(R sigma^(4/3))] exp(2N).                      (1)

This improves the previous coarse coefficient 3/(2R). The improved bare coefficient has cube 32/11 and is about 1.4275. For N>=0 and sigma=1 it forbids a bare target Ltar<=1. This is a conditional Einstein-bounce obstruction, not every Jordan bounce or a full cosmological exclusion.

### Measured weak-source calibration

Let gamma=G_cal/G_bare,c>0, so P_cal=P_bare/gamma. In the explicitly adopted same-background weak frozen principal regime, or its stated stable Yukawa completion, gamma<=(1+eta)(1+q_c), with eta>=0 and q_c<1/3. Hence

 P_cal > [3/(2R sigma^(4/3)(1+eta))] exp(2N).               (2)

Its eta=0,sigma=1 coefficient has cube 27/22 and is approximately 1.0706487833. Consequently, for N>=0 a positive target Ltar requires

 exp(2N) < (2R/3) sigma^(4/3)(1+eta) Ltar.                 (3)

With sigma=1 and eta=0, Ltar<=1 is impossible under these hypotheses. A necessary entropy allowance is sigma>[3 exp(2N)/(2R(1+eta)Ltar)]^(3/4). This does not prove an entropy production mechanism. Nor does it justify same-background calibration for an actual body or measurement. Different finite calibration backgrounds retain gamma<=(1+eta)(1+k)/C_c and require

 C_c < (R/2) sigma^(4/3)(1+eta)(1+k)Ltar exp(-2N).         (4)

For thresholds below one the previously proved negative-u energy floor applies with this tighter threshold. At threshold one there is no uniform positive gap above vacuum; above one the threshold supplies no negative-u restriction.

For a more general ideal bath with common equilibrium temperature, zero chemical potentials, fixed masses, positive massless species at low temperature, and analogous entropy and G bounds, replace R by (g_hot/g_cold)^(1/3). Equations (1)-(4) follow only when those constituent assumptions hold. R<=2 obstructs the bare unit target at N>=0, sigma=1; R<=3/2 obstructs the same-background eta=0 measured unit target. R above these thresholds is absence of this obstruction, not a constructed solution.

### What was eliminated and what survives

The coarse independent maximization of bounce pressure and thermal charge is eliminated algebraically. The apparent coefficient-below-one loophole from that coarse integration is closed within the stated same-background ideal-bath domain. Particle content, equilibrium, zero chemical potentials, isolation or supplied sigma, a strict Einstein bounce, positive kinetic/nonnegative other enthalpy, and the measured response regime all remain explicit. No initial history, action/potential, physical scale, laboratory environment, collision rate or abundance likelihood is derived. All thermal numerical checks are synthetic development calculations.

## Computational scope and assumption accounting

The canonical runner repeats five explicit mathematical blocks:27 conformal
and endpoint controls,8 general trace-charge identities,229 finite-mass checks
(including61 quadrature nodes and7 alternate energy-coordinate comparisons),
14 calibration-integration controls, and276 joint entropy/bounce controls.
The joint block includes postprocessing of the newly recomputed61-node bath
array plus seven fresh occupation-entropy integrals and six derivative checks.
It is the canonical rerun of the source development calculation, not an
independent empirical test. Counts mix exact identities and
numerical implementation checks; they are not counts of observed tests.
All grid profiles, numerical error estimates and synthetic calibration examples
are serialized. The uniform bounds are proved in the text, not extrapolated
from the grid. The integral derivative checks keep the physical mass fixed.

Actual altered implementations are retained with their failures:four original
thermal changes, four finite-mass changes, three calibration changes and four
joint-entropy changes. The
original wrapper NameError before the general-trace execution is preserved.
Focused independent checks retain their own first failures and exact repairs;
source qualifications preserve the original versions. A recovery archive holds
original notes, programs, numerical profiles, full reports and command records.

This result derives entropy conservation only within a specified reversible
isolated equilibrium matter model; the entropy value and equilibration are not
selected. It does not create a microscopic source for an allowed entropy budget.
The action, fields, parameters, vacuum hierarchy and initial state remain open.
The finite-mass bound concerns a strict Einstein bounce, nonnegative remaining
enthalpy, the stated radius ordering and the same total bath at the endpoints.
It does not transfer the earlier physical-stationary/slow-past theorem unchanged
to traceful matter, prove a nonlinear environment solution, or establish a
cosmological fit. These are proposed conditional results without a formal audit
verdict, effective retained grade, merge or theory-of-everything conclusion.
