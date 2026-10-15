# Conditional reconstruction of the revised scalar action from cosmological histories

**Date:** 2026-10-15
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_cosmological_inverse_check.py](../scripts/scalar_cosmological_inverse_check.py)


```yaml
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: revised_scalar_action_potential_scale
target_blocker_text: Derive or eliminate the remaining scalar action, state, scale and measurement assumptions
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
conditional_surface_status: Candidate metric/scalar solution membership under ideal calibrated physical histories and the supplied action class
hypothetical_axiom_status: none proposed
admitted_observation_status: Published event summaries exposed for route development; no continuous F history admitted and no independent empirical test
claim_type_reason: Exact conditional reconstruction and domain witnesses with physical suppliers still open
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: Derive a physical tensor-coefficient history or complementary growth/lensing map with explicit environment and error control
```

The exact target is a necessary-and-sufficient characterization of the coupled
FLRW metric/scalar solution within the supplied candidate, from ideal smooth
physical histories on a monotone field interval with the stated domain gates.
The supplied matter solution is a separate premise for complete matter-theory
membership.

Direct author /root. Conditional mathematical reconstruction.
This is not a reconstructed observed action, a selected state, or a new general
scalar-tensor reconstruction principle. The general method is established in
the literature; the task here is to derive specific discriminators for the
supplied revised candidate and identify exactly which observations are missing.

## Observation and input boundary

Expansion and gravitational-wave amplitude are different physical channels.
They could in principle give a physical expansion history and a tensor kinetic
coefficient history. Published GW170817 and host-galaxy distance summaries were
exposed while choosing this route. A single distance pair is not a twice
differentiable cosmological coefficient history. Wave generation, local endpoint
environments, stellar luminosity calibration, propagation, matter density and
clock/curvature reconstruction must all be controlled before making that
identification. No raw GW data or posterior has been accessed, no likelihood has
been fitted, and no independent empirical test is available in this block.

Natural units, signature (-+++). Use Jordan proper time t, a(t)>0, H=adot/a,
constant spatial curvature parameter kappa, and conserved matter with
rho_dot=-3H(rho+p). The ideal input functions are H,F,rho,p and kappa/a^2 in
common physical units, with F>0 and sufficient smoothness. F is the coefficient
of R_J/2, not a force-calibrated Newton constant. Distinguish this F from the
candidate's auxiliary 1+s exp(2 alpha u). No value of F, its derivatives, or
rho/F has yet been inferred from an actual observation.

## 1. Metric reconstruction without a chosen potential or initial trajectory

In a single-field Jordan chart use the action class

    S = integral sqrt(-g)[F R/2 - omega(F)(partial F)^2/(2F) - V(F)]
        + S_m[g,psi].

The use of F as a field chart is an action-class premise. It is not an assumption
that F(t) is monotone in every possible solution. For the inverse restrict to a
connected time interval with F_dot nowhere zero, so its time history is a chart.
The FLRW metric equations are

    3F(H^2+kappa/a^2) = rho + D/2 + V - 3H F_dot,
    -2F(H_dot-kappa/a^2) = rho+p+D+F_ddot-H F_dot,
    D = omega F_dot^2/F.

Consequently the observed-side combinations would determine

    D = -2F(H_dot-kappa/a^2) - (rho+p) - F_ddot + H F_dot,       (1)
    V = F(3H^2+H_dot+2kappa/a^2) - (rho-p)/2
        + F_ddot/2 + (5/2)H F_dot,                             (2)
    omega = F D/F_dot^2,
    q_rec = 1/(2omega+3) = F_dot^2/(2F D+3F_dot^2).                (3)

These statements can be checked by substitution into both metric equations.
The time derivative of the first metric equation, the second, and matter
conservation give the scalar equation multiplied by F_dot. Thus for F_dot!=0
the reconstructed functions along F also satisfy the scalar equation. This is
a local existence construction within the declared class, not uniqueness off
the sampled interval or in extra field directions. Smooth continuation through
isolated turning points needs its own compatibility; a constant-F plateau
cannot use the division or the Bianchi implication.

For D>0 the reconstructed Jordan kinetic coefficient is positive and 0<q_rec<1/3.
More generally positive Einstein kinetic energy only requires 2omega+3>0;
the revised candidate imposes the stronger D>0 for a changing coupled field.
The dimensionless Einstein K-metric distance obeys
dchi=+/-d ln F/(2 sqrt(q_rec)), with kinetic convention -Q(partial chi)^2
and its usual orientation and additive freedom. A dimensionful canonically
normalized varphi with kinetic term -(partial varphi)^2/2 is
varphi=sqrt(2Q)chi, for a fixed positive Einstein tensor normalization Q. This reconstructs a sampled single-field trajectory in a
coordinate, rather than choosing an initial physical state or ensemble.

Equation (2) includes the rolling derivative terms. Unlike a stationary density
inverse, it fixes the potential value on the trajectory including its additive
Einstein vacuum-energy contribution, provided the physical input functions and
absolute normalization are known. A reconstructed value is a calibration result,
not a first-principles explanation of the vacuum hierarchy.

## 2. A candidate-specific kinetic discriminator

The inherited Einstein action has kinetic convention -Q K_AB partial phi^A
partial phi^B (no factor one-half), physical metric C g_E and

    0<k<1/3, a_c=(1-k)(1+3k)/4, alpha=sqrt(a_c),
    s=(1+k)/(k(1-3k)), E=exp(2alpha u),
    W=1+sE, J=1+(1-3a_c)sE,
    K_uu=J/W^2, C=(1+s)E/W, Q=Q0(1+k).

The remaining diagonal entries and full potential are

    R_perp=1+2(1+k)(x^2+y^2)/3,
    K_xx=(1+s)4k/(9W R_perp), K_yy=(1+s)k/(3W R_perp),
    U=3/2+3s(E-1)^2/(2W^2)+nu(1+s)u^2/(2W^2)
      +(k/2)x^2 exp(-(1-k)u/alpha)
      +(k/3)y^2 exp(-(1+k)u/alpha).

Assume Q0,Hv,nu>0 and finite fields. The full supplied action is

    S=Q integral sqrt(-g_E)[R_E/2-K_AB partial phi^A partial phi^B-2Hv^2 U]
       + S_m[C g_E,psi].

K has no u/transverse cross term, K_uu is independent of x,y, and its transverse
diagonal entries are positive. Let A=sqrt(C), F=Q/C and

    F_c=Q s/(1+s)=Q0(1+k)^2/(4a_c)>0,
    c=(1-3a_c)/(2a_c),       0<c<1/2.

Here c is a dimensionless kinetic-shape parameter, not the speed of light.
Then F=F_c+[Q/(1+s)]exp(-2alpha u)>F_c. Directly,

    q_geom=|d ln A|_K^2=a_c/J
      =a_c(F-F_c)/(F-3a_c F_c).

The conformal transformation gives

    D=2F[K_AB phi_dot^A phi_dot^B-3(d ln A/dt)^2]
     =c F_dot^2/(F-F_c) + 2F(K_xx x_dot^2+K_yy y_dot^2).       (4)

This identity requires no supplied potential shape, initial scalar amplitudes,
or stationary-density solution. It retains the specified kinetic metric and
conformal matter coupling as premises. A general positive Einstein kinetic
metric alone does not imply this specific formula or Jordan positivity.
Do not identify the geometric coupling with a one-field background inverse
when transverse fields move. With T_perp=K_xx x_dot^2+K_yy y_dot^2 and
F_dot nonzero, the exact relation is

    1/q_rec = 1/q_geom + 4F^2 T_perp/F_dot^2,
    q_rec <= q_geom.

The two quantities coincide only for zero transverse velocity. The numerical
q control below uses the coupled synthetic branch and makes no full-field
identification.

For the exact x=y=0 truncation, (4) gives the undivided kinetic identity

    D(F-F_c)=c F_dot^2.                                      (5)

At points with D>0 define Y=F_dot^2/D. The candidate requires

    Y=(F-F_c)/c.

Two distinct F values give

    c=(F2-F1)/(Y2-Y1),  F_c=F1-c Y1,
    a_c=1/(2c+3),  k=(1-2sqrt(2c/(2c+3)))/3.                 (6)

Check all gates: D_i>0, distinct F_i, nonzero Y2-Y1, 0<c<1/2,
F_c>0, and F(t)>F_c over the tested interval. A third point tests the affine
shape only when it has not chosen the model or fitted c,F_c. No synthetic
third point constitutes an independent observational test.

For the full three-field candidate one has only

    D >= c F_dot^2/(F-F_c),                                 (7)

with equality iff x_dot=y_dot=0 at the instant, by transverse positivity.
At one instant equality does not imply x=y=0. However, equality throughout an
open interval of a full candidate solution forces x=y=0. Positivity first forces
x_dot=y_dot=0 throughout the interval, hence x,y are constant. The metric is
diagonal and K_uu is independent of x,y, so Gamma^x_uu=Gamma^y_uu=0. The
matter coupling has no transverse derivative. The transverse field equations
therefore reduce to Hv^2 U_x=Hv^2 U_y=0, where

    U_x=k x exp(-(1-k)u/alpha),
    U_y=(2k/3)y exp(-(1+k)u/alpha).

Because k,Hv are positive, x=y=0. This derives the truncation conditionally
from a whole-interval kinetic equality and the complete supplied field equations;
it does not infer it from a pair of fitted epochs or from an approximate equality.
A constant nonzero transverse coordinate can carry potential energy at an instant
but cannot solve those transverse equations throughout an equality interval. Thus
the exact two-point inverse (6) is not automatically an inverse for the full
three-field theory. A violation of (7), with a justified measured map and
uncertainty budget, would challenge the full candidate at those parameters;
failure of equality alone would not. This is one joint model test, not several
independent impossibility walls.

## 3. Potential and scale reconstruction within the coupled truncation

After the kinetic parameters are conditionally inferred, derive

    Q0=4a_c F_c/(1+k)^2,       Q=4a_c F_c/(1+k),
    E=F_c/[s(F-F_c)],         u=ln(E)/(2alpha).

On x=y=0 the candidate potential is

    U=B0+nu B1,
    B0=3/2+3s(E-1)^2/(2W^2),
    B1=(1+s)u^2/(2W^2),     W=1+sE.

Since V_E=2Q Hv^2 U and V=V_E/A^4,

    Z:=V/F^2 = L B0 + T B1,
    L=2Hv^2/Q>0,            T=L nu>0.                       (8)

Two times with nonzero determinant B0_1 B1_2-B0_2 B1_1 determine L,T.
Then Hv^2=L Q/2 and nu=T/L. The determinant, positivity, previous kinetic
gates and all subsequent residuals are mandatory. A single vacuum point
u=0 has B1=0 and cannot determine nu. Two fitted values alone do not test
the two-basis potential. Additional times, perturbations or other regimes
provide prospective discriminators, not already completed empirical tests.

Together (1)-(8) turn the candidate's supplied action functions and scales into
an overdetermined reconstruction problem if their physical input functions are
measured. They do not select this action among all conformal theories or derive
parameter values before calibration. General field reparametrization freedoms
and unsampled transverse potentials remain. Conversely, suppose a smooth ideal
history passes all domain gates, the kinetic identity (5) throughout the interval,
and the potential identity (8) throughout the interval, with conserved matter
and the prescribed FLRW curvature. Reconstruct u(F), set x=y=0, and use the
positive parameters (6)-(8). Both metric equations then hold by construction.
The nonzero F_dot Bianchi implication supplies the coupled scalar equation,
and U_x=U_y=0 supplies both transverse equations. Thus the tuple is a solution of the candidate FLRW metric/scalar system
with the stated conserved physical fluid on the interval. Membership of a
complete matter theory additionally presumes a supplied matter solution
psi of S_m[g,psi]; conservation alone does not construct it. With two nondegenerate calibration pairs the
parameters are unique inside this specified candidate chart. This is conditional
solution membership, not unique selection among all theories or a physical
initial-state principle. Observed precision, derivative
errors, curvature and matter calibration cannot be supplied by these equations.

If only f=F/F_ref and rho/F_ref,p/F_ref are known, the same inverse gives
c and f_c=F_c/F_ref, and Q0/F_ref. Use d=D/F_ref and v=V/F_ref. The potential
relation becomes v/f^2 = (2Hv^2 F_ref/Q)(B0+nu B1): thus Hv is inferable in
the supplied physical time units, but the absolute gravitational normalization
F_ref and dimensionless quantum hierarchy Hv^2/Q0 remain undetermined.
Rescaling F,rho,p,Q0 by the same positive factor preserves all dimensionless
readouts and H,Hv,k,nu. This is a different source/normalization assignment,
not a claim that independently calibrated matter masses also rescale.

## 4. What a gravitational-wave amplitude can supply

For a decoupled high-frequency tensor polarization with quadratic action
proportional to integral sqrt(-g) F g^{mu nu}partial_mu h partial_nu h,
geometric optics gives k^2=0 and

    nabla_mu(F A_h^2 k^mu)=0.

The same ray/beam expansion in electromagnetic propagation has no F factor.
For fixed source-normalized emission and a calibrated detector, their tensor
amplitude transfer ratio has the endpoint factor sqrt(F_source/F_observer).
Equivalently the propagation-only distance ratio is

    R=d_L^GW/d_L^EM=sqrt(F_observer/F_source).                (9)

This assumes tensor-scalar mode conversion, reflection, absorption and generation
changes are negligible or separately bounded; it is a transport theorem, not
a full compact-binary source theorem. In a homogeneous cosmology with endpoint
F equal to the cosmological values, f(z)=R(z)^(-2) for F_ref=F_observer.
Under those additional identifications, (1)-(8) are a route from two physical
channels to candidate reconstruction.

For smooth local transitions the endpoint factors telescope. Equal local
source and observer F makes (9) unity even when the intervening cosmological F
varies. This is a prescribed transport-coefficient witness, not a proof that
the revised action dynamically screens a neutron star or the detector. A
single observed distance ratio cannot choose between those environmental
maps. Smoothness relative to the wavelength matters: a sharp planar jump from
F1 to F2 has r=(F1-F2)/(F1+F2), t=2F1/(F1+F2) and
r^2+(F2/F1)t^2=1. At F1=1,F2=4 the transmitted amplitude is0.4, whereas
the adiabatic endpoint expression gives0.5. This is a transport-domain
counterexample, not a scattering solution of the revised scalar action. Neither a GR waveform distance posterior nor a stellar luminosity-based
distance is silently reinterpreted as a calibrated F measurement here.

## 5. Concrete failures and tests to preserve

The positive construction uses complete ideal functions, not one event. The
literal attempt to plug the published GW170817 distance pair into (1) fails
the input-domain gate: no F(t), F_dot, F_ddot, H_dot or controlled endpoint
map has been supplied. It would be false to quote k,nu,Q0,Hv inferred from
that pair. This is a route-local admission failure, not impossibility of
standard-siren reconstruction or the full campaign.

Another domain failure is the constant-F plateau. For exact dust-plus-Lambda
expansion normalized with that F, (1) has D=0 and (2) V=constant. In the
positive three-field kinetic metric (4), constant F and D=0 imply all field
velocities vanish. A constant scalar in the coupled candidate with q_geom>0 would
then require a fixed potential gradient to balance a changing dust trace,
which cannot hold over an interval with changing nonzero rho. The metric
identity by itself missed this scalar equation because F_dot=0. This exact
counterexample illustrates why the inverse refuses that domain; it is not an
exclusion using noisy observed LambdaCDM fits.

Before executable results: check general metric/Bianchi identities, conformal
normalization, exact candidate kinetic/potential transformations, all inverse
domains, the full-field inequality, time/normalization scaling and endpoint
telescoping. Generate synthetic histories from the original supplied Einstein
equations and reconstruct parameters from Jordan readouts; reserve later
synthetic times for residual controls, explicitly not empirical holdouts.
Retain ill-conditioning and failed inverse attempts. Deliberately alter the
curvature sign, kinetic factor, friction coefficient, Jordan time conversion,
candidate root branch and wave endpoint orientation to test the controls.

The focused independent checks are narrow: derive metric/conformal inverse
mathematics independently, then compare complete authored source; inspect
primary papers and the actual source-data claims without creating a fitted
observation. Parent authorship, original deadline and older campaign stops
remain unchanged.

## 6. Executed controls and preserved numerical failure

The frozen v1 protocol uses twelve supplied-action synthetic histories, fixed
epochs0 and6 for parameter calibration and epochs7 through16 for later
synthetic residuals. These are computational controls, not empirical holdouts.
The first double-precision run passed90 of91 controls. Case9
(k=.29,nu=.2,Q0=12,Hv=.19) failed the original5e-7 relative parameter
threshold: nu error2.6967536e-6. All original source, protocol, inputs,
outputs and execution receipt remain unchanged.

The case9 kinetic-stress subtraction has maximum cancellation ratio2.962906e6;
the case9 potential design has condition number6.323335e5. Merely evaluating
the stored rounded physical inputs with50 or80-digit arithmetic still fails
the original threshold. Reassembling physical inputs from the same saved
synthetic states at50 and80 digits recovers all twelve cases below the
unchanged threshold. This establishes an algebraic rounding diagnosis for
model-generated inputs; it neither certifies the double-precision trajectory
nor supplies high-precision measurements. Ill-conditioned derivative inference
remains a physical obstacle. No cases, epochs or tolerances were changed.

The focused source conclusions were frozen before the author note was exposed.
Their complete report was read. Mathematical/source execution and final evidence
identities are recorded separately in the campaign review record. Scoped checks
are not a formal claim audit or integrated-main validation.

## 7. Literature, import ledger and limits

The general scalar-tensor reconstruction method predates this campaign;
[Boisseau et al. (2000)](https://arxiv.org/pdf/gr-qc/0001066v1) reconstruct
functions with continuous cosmological inputs and distinguish the cosmological
coefficient from effective force coupling. Equations (1)-(8) specialize the
inverse to this supplied revised action and prove its solution-membership gates.
They are not a discovery of general cosmological reconstruction.

[Dalang and Lombriser (2019)](https://arxiv.org/pdf/1906.12333v2), equation5.20,
and [Dalang, Fleury and Lombriser (2021)](https://arxiv.org/pdf/2009.11827v3),
equations95-97, support the local-endpoint distinction in transport under their
stated premises. They do not provide the actual environmental solution for this
candidate. Equal local endpoint values are a conditional cancellation example,
not a theorem that every screening mechanism hides every tensor observable.

The [GW170817 detection paper](https://arxiv.org/pdf/1710.05832v1) and
[standard-siren analysis](https://arxiv.org/pdf/1710.05835v1) use distinct
inference setups and interval conventions. Their distance summaries depend on
GR waveforms, calibration and priors. The
[Cantiello et al. SBF measurement](https://arxiv.org/pdf/1801.06080v2) has a
Cepheid-based absolute calibration. It is independent of GW amplitude, not
independent of all stellar-physics and distance assumptions. Their quoted
summaries were exposed for route development. No joint likelihood, measurement
covariance, fit, F-history or independent empirical test was constructed here.
Exact source versions, hashes and actual read scope are preserved in the
campaign's independent source evidence; extraction is not equated with full reading.

| Input or premise | What this block derives | What remains open |
|---|---|---|
| Smooth physical H,F,rho,p and curvature; conservation; Fdot nonzero | Unique sampled Jordan D,V,omega; scalar equation from Bianchi | Actual functions, errors, clocks, matter and gravity normalization |
| Supplied revised kinetic geometry and conformal coupling | Affine kinetic discriminator and candidate parameter inverse | Why this action class is physically selected |
| Whole-interval equality inside a full candidate solution | x=y=0 from transverse equations | No observed equality; approximate equality needs separate quantitative controls |
| Coupled potential basis and nondegenerate epochs | Conditional Hv,nu,Q0 calibration and metric/scalar solution membership | No first-principles value, hierarchy or unique action selection |
| Relative coefficient and density histories | k,nu,Hv,Q0/Fref in the supplied time units | Absolute Fref and Hv^2/Q0 |
| Tensor transport, generation/detection and local endpoint map | Conditional propagation-distance relation | Actual environmental matching and source/detector/EM calibration |
| Fixed synthetic cases | Exact identities, numerical readout and inverse checks | No selected cosmological initial state or empirical confirmation |

Registered unit, kinetic-isotropy and realized-state primitives supply only
those registered statements. They provide no observed history, scalar action,
parameter, measure, typicality, noise law or physical initial condition here.
The hypothetical new premise would be a physical input map supplying those
histories with controlled errors; it has not been adopted as an accomplished
derivation. This unit is upstream conditional support. Independent audit is
still required before any effective retained-grade claim. No bare retained,
audit-cleared, complete theory of everything, or empirical success is asserted.

## 8. Proof obligations and review record

The acyclic construction is: physical FLRW conventions and conserved source
(explicit inputs) -> the two metric combinations (proved in section1) -> the
nonzero-velocity Bianchi implication (proved there) -> the supplied candidate
kinetic identity and domain inverse (proved in section2) -> exact interval
truncation from the transverse equations (proved there) -> potential basis and
parameter inversion (proved in section3) -> the conditional converse for the
metric/scalar system (proved there). No measured input history is claimed to
emerge from this graph. The actual physical observation-to-history map with
controlled errors is the strongest missing supplier for applying this result;
it remains open rather than a terminal lemma called proved.

The source-review corrections distinguish background and geometric coupling,
define the dimensionful versus dimensionless field normalization, qualify
matter-theory membership and identify the quoted cancellation ratio as case9.
Original source versions, failed numeric recovery and reviewer findings remain
immutable in the campaign evidence. The current102 author controls are separate
from42 independently derived mathematical controls and a separate12-case ODE.
The fourteen deliberately altered sources produced seven assertion failures,
six domain refusals and one complex-ordering exception. The latter is not
counted as an independently decisive mathematical rejection. A mutation
selector setup failure occurred before any variant execution and is retained.
A separate five-variant supplement tests the Bianchi matter trace, tensor
endpoint orientation, sharp-interface transmission, transverse potential force
and transverse kinetic normalization; all five fail their exact-identity
assertions. The combined nineteen variants therefore comprise twelve assertion
rejections, six domain refusals and one arithmetic exception. No scientific
source, synthetic case, calibration epoch or tolerance changed for this supplement.

The complete scoped review and exact source/cache identities are in the
[campaign review record](../.claude/science/physics-loops/observations-backward-24h-20261014/action_selection/REVIEW_RECORD_v1.md).
The [N1-N8 scope checklist](../.claude/science/physics-loops/observations-backward-24h-20261014/action_selection/NO_GO_DISCIPLINE_CHECKLIST.md)
records the tested routes and restrictions; it does not declare a theory-wide
no-go. The primary imports the sole scientific helper, so no external packet
helper registration or dependency-policy change is proposed. Its paired
[source-bound log](../logs/runner-cache/scalar_cosmological_inverse_check.txt)
is numerical/source evidence, not an audit verdict. Final integrated-main
validation and any independent audit remain later work; no merge is performed.
