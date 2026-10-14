# Finite-range scalar gravity through orbital motion and coherent radio phase

**Date:** 2026-10-14
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [exponential_scalar_orbit_light_time_check.py](../scripts/exponential_scalar_orbit_light_time_check.py)

This is a conditional mathematical reconstruction and observation operator.
It uses synthetic controls and an exposed observational comparator. It is
neither a Cassini likelihood nor an empirical acceptance of the supplied scalar
action. Source-profile selection cancels from the ideal single-mode range
inverse; the physical source, background and observation model still need to
satisfy the hypotheses.

## Observational question and exact target

Cassini measured radio frequency shifts and fitted a PPN coefficient jointly with a spacecraft/solar-system model. The published gamma summary is already exposed development data. The candidate's local metric ratio is not thereby a fitted parameter. Reconstruct the leading forward operator and its calibration explicitly. The supplied scalar channel follows the normalization of the [local-response note](EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md) and uses the complete-source stress of the [composite-charge note](EXPONENTIAL_SCALAR_COMPOSITE_CHARGE_BOUNDED_THEOREM_NOTE_2026-10-14.md). The equations needed here are restated below; these links do not confer unconditional framework status.

**Exact target:** for the stated single-mode, stationary spherical weak-source response, derive the orbit/photon normalization and an injective positive-range reconstruction from three ideal circular-force coefficients, then derive the coherent finite-count observation operator for prescribed exterior worldlines.

## Domain and source normalization

Use a canonical scalar channel with kinetic term -Q(partial chi)^2, conformal matter metric A(chi)^2 g_E, beta=d ln A/d chi and q=beta^2. Use the source-generated solution with regular interior and a decaying exterior scalar perturbation, excluding or independently bounding incoming/homogeneous fields. In the local source equations use c=1 and Jordan physical coordinates. If Q is the original Einstein-action coefficient, define Q_J=Q/A_inf^2, Gbare=1/(8 pi Q_J), and mu=mu_E/A_inf. Work on the locally frozen stable operator (Delta-mu^2)delta chi=beta(rho_J-S_J)/(2Q_J)=4 pi beta Gbare(rho_J-S_J). Below rho,S and source radius refer to these physical coordinates; E=M_J in these units. Factors of c are restored in the metric, optical and dimensional mass formulas below. The complete source stress is stationary, isolated and spherical, radius R, total energy E>0, conserved at the unperturbed order. Backreaction/self-binding, ambient response, nonstationarity and higher weak-field orders require separate bounds. Here S=sum_i Tii and Trr is radial stress. No particular microscopic equilibrium state, density profile or vacuum mass is selected; stationarity itself remains a supplied class condition.

Set f_mu(s)=sinh(mu s)/(mu s), with f_0(s)=1 by continuity. The exterior scalar charge ratio is
F(mu)=E^-1 integral f_mu(s)[rho-S]dV
     =E^-1 integral [f_mu rho+s f_mu' Trr]dV.
The integrated stress vanishes at mu=0 by conservation; F(0)=1. This uses the complete supports and binding stress. At finite mu, F need not be positive without a condition. When rho>=0 and |Trr|<=rho,
2sinh(mu R)/(mu R)-cosh(mu R) <= F <= cosh(mu R).
No pressure-free material law has been inserted.

To check the charge formula directly, the Green kernel of Delta-mu^2 is
-exp(-mu|x-xprime|)/(4 pi |x-xprime|). Its angular integral outside the
source gives -exp(-mu r) f_mu(s)/r. Weighted stress conservation with test
vector f_mu(r)x_i gives integral[f_mu S+r f_mu' Trr]=0, proving the second
charge expression. If |Trr|<=rho, its integrand lies between
(2f_mu-cosh(mu s))rho and cosh(mu s)rho. The upper weight increases in s;
the lower decreases. For the latter, (2+x^2)sinh(x)-2x cosh(x) has derivative
x^2 cosh(x)>=0 and vanishes at zero. Normalization by E then yields the
stated endpoint bounds. At mu=0 these reduce to F=1.

Let M0=Gbare M_J>0 (units length^3/time^2), B=M0 q F(mu), and a_s=B/M0. The inherited leading exterior solution gives
Psi(r)=-[M0+B exp(-mu r)]/r,
Phi(r)=-[M0-B exp(-mu r)]/r,
ds_J^2=-(1+2Psi/c^2)c^2dt^2+(1-2Phi/c^2)dx^2.
Scalar stress is second weak-field order in this stipulated regime. Spherical exterior Einstein potentials have mass M0. This is not a full stellar solution or global asymptotically flat vacuum of the positive-vacuum-energy action.

## Light and orbit are different operators

Along the unperturbed exterior straight segment between x_A,x_B,
dt=dl/c [1-(Psi+Phi)/c^2]+O(weak^2).
Therefore the first-order one-way excess coordinate time is
Delta t=2 M0/c^3 L,
L=ln[(r_A+r_B+D)/(r_A+r_B-D)], D=|x_B-x_A|.
The entire segment must stay outside R. Null paths and this coordinate integrand are conformally invariant. A real endpoint clock, motion and orbit fit require additional conversion and nuisance terms; subtracting an arbitrary flat comparison does not establish an observed delay. For a prescribed varying geometry, y_coord=-d(Delta t)/dt defines a delay-rate contribution. Each uplink/downlink has its own retarded geometry; the full observed frequency follows the coherent phase operator below.

For a circular slow orbit with K(r)>0 of a pointlike unscreened weak test body in the same background, with Omega referred to the shared background coordinate time,
K(r)=r^3 Omega^2=r^2 dPsi/dr=M0+B h(mu r),
h(x)=(1+x)exp(-x).
Thus ideal light determination of M0 and ideal circular-orbit K give
z(r)=K(r)/M0-1=a_s h(mu r).
An ideal PPN-style delay template normalized by K(rc) has
1+gamma_c=2M0/K(rc),
gamma_c-1=-2 a_s h(mu rc)/(1+a_s h(mu rc)).
The local metric ratio instead is
Phi/Psi=[1-a_s exp(-mu r)]/[1+a_s exp(-mu r)].
At r=rc, put x=mu rc. Their exact difference, where both denominators are defined, is
(Phi/Psi)-gamma_c=2 a_s x exp(-x)/[(1+a_s exp(-x))(1+a_s(1+x)exp(-x))].
For finite rc>0 and mu>=0, exact equality requires x=0 or a_s=0. Approximate equality can occur both at long range and when the finite-range signal is strongly suppressed; its accuracy needs a stated tolerance. The force derivative supplies the factor 1+mu rc. These definitions do not assert Cassini's joint ephemeris fit is a single ideal circular-orbit calibration.

## Range reconstruction with light normalization

For r2>r1>R and a_s>0,mu>0,
0<z2/z1=h(mu r2)/h(mu r1)<1.
Its logarithmic derivative is
mu[r1^2/(1+mu r1)-r2^2/(1+mu r2)]<0.
The ratio continuously decreases from1 to0, so it determines a unique positive mu. Then a_s=z1/h(mu r1). F cancels from the range inference; q still needs F. A measured zero amplitude does not identify mu. The mu=0 boundary gives equal nonzero z at every radius and cannot be inferred from equality within finite errors without a precision statement.

## Three force radii without mass or source-profile calibration

Let R<r1<r2<r3 and K_i=M0+B h(mu r_i), with M0>0,B>0,mu>0.
D12=K1-K2>0, D23=K2-K3>0. Their ratio is
mathcal R(mu)=D12/D23
 =integral_r1^r2 s exp(-mu s)ds / integral_r2^r3 s exp(-mu s)ds.
The factor mu^2 cancels because h(mu a)-h(mu b)=mu^2 integral_a^b s exp(-mu s)ds.
Let mean12 and mean23 be means of s in the two positive normalized integrals.
d ln mathcal R/dmu=mean23-mean12>0.
The separated interval interiors make the inequality strict. Thus mathcal R is continuous and strictly increasing from
mathcal R0=(r2^2-r1^2)/(r3^2-r2^2)
to infinity. The large-mu limit follows, for example, from endpoint Laplace asymptotics; r1,r2>0.

Conversely any D12,D23>0 with ratio>mathcal R0 has exactly one positive solution mu. Set
B=D12/[h(mu r1)-h(mu r2)], M0=K1-B h(mu r1).
It is a physical member of this stated model only if M0>0 and if the inferred a_s=B/M0 can be supplied by q F(mu) in the candidate's domain. Passing the ratio test alone is insufficient. A fourth-radius value and/or the light coefficient is an overdetermining test. Source-profile cancellation identifies range for this one-mode operator, not the fundamental potential or ambient state. Multimode and environmental alternatives can fit some or all finite data and require separate tests.

For finite absolute errors |Khat_i-K_i|<=eps_i, define e12=eps1+eps2,e23=eps2+eps3. If Dhat12-e12>0,Dhat23-e23>0, every allowed ratio lies in
[(Dhat12-e12)/(Dhat23+e23),(Dhat12+e12)/(Dhat23-e23)].
If this whole interval is above mathcal R0, monotone inversion encloses mu. If its upper end is <=mathcal R0, no positive-mu/B model satisfying these error bounds exists. If the interval straddles mathcal R0, this ratio-only enclosure touches the zero-mass boundary; the ratio test alone is inconclusive. The M0>0 and a_s=q F domain checks remain mandatory and can exclude the entire box or impose a stronger lower bound. Finite errors must not be inverted into a spurious precise mass. These conservative bounds do not assume independent errors; they discard their shared-K2 correlation. Radius and common-time calibration errors are not included unless added to the forward/error model.

## Conditional exposed benchmark only

Using the previously exposed Cassini central value2.1e-5 and quoted error2.3e-5, the arithmetic central-minus-two-errors lower edge is -2.5e-5. This is not a new confidence interval or a likelihood fit. If a separately established error budget makes that edge applicable to gamma_c above, then for a_s>=0,
a_s h(mu rc)<=2.5e-5/(2-2.5e-5).
For an absolute bridge error eps_gamma>=0, set delta_eff=2.5e-5+eps_gamma. If delta_eff<2, the corresponding conditional bound is a_s h(mu rc)<=delta_eff/(2-delta_eff). The bridge error has not been derived; setting it to zero below is an ideal benchmark, not an observational exclusion. No q(k,u) parameter bound follows without a source/environment/range bridge.

## Physical application still to be established

The single-mode stable frozen weak-source response is supplied. The source profile need not be chosen to infer mu in the ideal inverse, but the actual body, stress, environment and instrument must be shown to satisfy the operator domain. Self-gravity, radiative and homogeneous modes, post-Newtonian terms, endpoint clocks, motion, plasma, data covariance and calibration require explicit control. No independent empirical holdout or raw Cassini likelihood has been analyzed. This derivation selects neither action/potential nor initial state nor absolute scale.

## Finite-error counterexample from the focused independent check

The checker supplied a counterexample to the earlier v2 wording, not to the monotone inverse. With radii(1,2,3), Khat=(101.6,101,100), and eps_i=1/500, the conservative ratio interval is [149/251,151/249], straddling R0=3/5. Nevertheless every exact positive-amplitude fit in the box has M0<0. Here is its exact rational proof, personally checked after the independent report.

For 0<=mu<=1/50, the mean in [1,2] is at most its mu=0 value14/9. The mean in [2,3] is at least e^(-mu)*38/15 >=(49/50)*38/15. Thus d ln R/dmu >=1043/1125 and
R(1/50)>=(3/5)[1+1043/56250]=57293/93750>151/249.
Every ratio-admissible fit must therefore have mu<1/50. Since h(x)=1-integral_0^x t exp(-t)dt, h(mu)>=4999/5000>2499/2500, while
h(mu)-h(2mu)<=mu^2 integral_1^2 s ds<=3/5000.
Using D12>=149/250 and K1<=50801/500 yields
M0=K1-D12 h(mu)/[h(mu)-h(2mu)]
   <=50801/500-(149/250)(2499/2500)/(3/5000)
   =-445667/500<0.
The conservative ratio box is thus only a necessary reconstruction step. This synthetic example is a numerical-domain control, not an astronomical measurement.

## Coherent radio phase and finite compression

Assume geometric optics in vacuum, known timelike emitter/transponder/receiver worldlines, a deterministic emitter phase Theta_e(tau_e) measured in cycles of emitter proper time, and an ideal instantaneous coherent transponder with fixed known phase multiplication ratio k. There is no independent onboard oscillator or stochastic phase slip. A calibrated finite onboard delay would require a separate bounce map. No station delay, medium or instrumental bias is silently set to its observational value.

Let t1 be emission, t2 bounce and t3 reception in shared coordinates. For time transfer T_ij(ti,tj), they obey

    t2-t1 = T_12(t1,t2),
    t3-t2 = T_23(t2,t3).

Phase constancy along each geometric-optics ray and the coherent bounce imply

    Theta_r(tau_r(t3)) = k Theta_e(tau_e(t1(t3))) + constant.

Writing w_i=d tau_i/dt_i>0 and differentiating the two implicit equations gives

    J12=dt1/dt2=(1-partial_2 T12)/(1+partial_1 T12),
    J23=dt2/dt3=(1-partial_3 T23)/(1+partial_2 T23),
    nu_r(t3)=k nu_e(tau_e(t1)) [w1(t1)/w3(t3)] J12 J23.      (1)

The denominators must be nonzero and the retarded solution unique in the chosen domain. Weak gravity and sufficiently slow separated exterior worldlines are one useful domain, not a proof of uniqueness for arbitrary geometry or lensing. This phase relation is exact for a stipulated transfer function and bounce law. Approximating the transfer function remains a separate physical approximation.

For reception endpoints t3_minus,t3_plus, with actual receiver proper compression time T_r=tau_r(t3_plus)-tau_r(t3_minus)>0, the average received count rate is

    nubar_r = k[Theta_e(tau_e(t1_plus))-Theta_e(tau_e(t1_minus))]/T_r.   (2)

Equation(2) derives the finite interval operation and permits an arbitrary calibrated frequency ramp. It does not replace it with the midpoint derivative. For one-way records, replace the coherent bounce by a specified transmitter phase model. Three-way links use distinct emitter and receiver station clocks/worldlines.

### Transfer function and endpoint clock

Use the source-generated exterior metric above, common Jordan coordinates, c restored, fixed M0, B and mu on the link interval. The prescribed worldline geometry is x_i(t_i), r_i=|x_i|, D_ij=|x_j-x_i| and S_ij=r_i+r_j. To first order in weak gravity, with the straight segment exterior to the source,

    T_ij=D_ij/c + 2M0/c^3 log[(S_ij+D_ij)/(S_ij-D_ij)].       (3)

The scalar perturbation cancels from this coordinate photon kernel. It need not cancel from the observed phase: the clock rates are

    w_i=sqrt[1+2Psi_i/c^2 -(1-2Phi_i/c^2)|v_i|^2/c^2]

for the displayed linear metric, with Psi_i=-(M0+B exp(-mu r_i))/r_i and Phi_i=-(M0-B exp(-mu r_i))/r_i. This square root defines a diagnostic resummation of that linear metric, not a complete second-order field solution. At nonrelativistic leading order,

    w_i=1+Psi_i/c^2-|v_i|^2/(2c^2)+higher orders.

Moreover a dynamically predicted x_i changes with the scalar force. Equations(1)-(3) hold positions/velocities supplied when evaluating the transfer operator; using a GR-fitted ephemeris as fixed truth would import a theory-dependent trajectory. In a perfectly circular same-station idealization the stationary scalar clock term at emission and reception agrees; a real time-dependent station trajectory requires evaluating both events. No zero endpoint-error budget has been inferred for Cassini.

For implementation, n=(x_j-x_i)/D, so dD/dt_i=-n.v_i and dD/dt_j=n.v_j. Since dr_i/dt_i=x_i.v_i/r_i, either endpoint derivative obeys

    partial L = 2[S partial D-D partial S]/(S^2-D^2).        (4)

This supplies the exact derivative of the stipulated first-order transfer function. Directly solving the retarded equations and differentiating their solutions gives an implementation-independent check of(1). Integrating received phase rate with receiver proper time checks(2).


## Inputs, derivations and observation roles

| Item | Role and provenance | Application still required |
| --- | --- | --- |
| Canonical scalar, universal conformal metric, stable frozen Helmholtz operator | Supplied candidate model, with normalization restated here and in the two linked source notes | Derive its action, select or reconstruct its background, and control omitted local terms |
| Complete weak stationary spherical stress; regular interior and decaying/source-generated exterior | Explicit local-model hypotheses; weighted conservation gives the displayed charge | Demonstrate the relevant real source and environment satisfy the domain |
| Pointlike unscreened probes, ideal circular force coefficients, common physical coordinates/time | Definitions of the inverse data model | Jointly determine or bound orbital and timing calibration; a GR-fitted ephemeris is not an independent scalar-theory observable |
| Geometric optics, coherent instantaneous bounce, known emitter phase and worldlines | Explicit measurement hypotheses | Hardware phase/ramp and delay conversion, media, trajectory and clock modeling |
| Cassini gamma summary | Exposed comparator from Bertotti, Iess and Tortora (2003); not a premise in the inverse proof | A likelihood and controlled mapping to the actual measurement would be required for a statistical bound |
| Source profile and amplitude | Removed algebraically from the ideal range ratio, then amplitude reconstructed | q still requires a source charge; the inverse does not select a potential or prove a single physical mode |

The [primary Cassini paper](https://www.nature.com/articles/nature01997)
reports gamma-1=(2.1+/-2.3)10^-5. This note uses only its already exposed
summary for the explicitly idealized arithmetic benchmark. The
[NASA PDS data-set description](https://pds.nasa.gov/ds-view/pds/viewProfile.jsp?dsid=CO-SS-RSS-1-SCE1-V1.0)
and the [format-2 orbit-data label](https://atmos.nmsu.edu/pdsd/archive/data/co-ss-rss-1-sce1-v10/cors_0024/sce1_169/odf/c32easc2002_169_0000xmmmv0.lbl)
identify a finite count/ramp/reference observable. Equation (2) in the
coherent-phase section supplies its vacuum phase-count component, not the
complete ODF receiver conversion. The source label's receiver bias and band
conversion symbols must be kept distinct from this note's scalar amplitude
and total coherent multiplication ratio. Station delays, solar plasma,
Earth orientation, other gravitational sources, thermal forces, covariance,
and higher-order propagation remain part of a prospective forward analysis.
The companion campaign registers raw-track data roles before measurement
access; no such raw values enter this theorem runner or its proof.

The role of mass calibration in massive scalar-tensor Shapiro delay also
appears in [Dyadina and Labazova (2021)](https://arxiv.org/abs/2111.13900).
Our K is explicitly the circular-force coefficient r^2 dPsi/dr; it is not
identified with a potential coefficient. No novelty claim about mass
calibration or the elementary null conformal invariance is made. The
[finite-endpoint treatment by Ashby and Bertotti](https://arxiv.org/abs/0912.2705)
identifies enhanced higher-order time-transfer terms relevant to Cassini;
the first-order kernel here is not a derived precision error budget.

## Obligation graph and boundaries

1. The supplied local operator and complete stress domain imply the exterior
   charge, by the Green-function and weighted-conservation calculation above.
2. The leading Einstein mass and conformal scalar perturbation imply the two
   displayed metric potentials within this weak-field model.
3. The null condition and circular test-body equation give two distinct
   operators; their derivatives and finite-endpoint integral are explicit.
4. Positive separated-interval Laplace integrals give strict monotonicity,
   endpoint limits and the three-radius inverse. Positivity of the reconstructed
   bare mass and admissible source coupling are separately checked.
5. Conservative difference-error boxes give an enclosure for the ratio;
   the exact rational example exhibits the extra positivity restriction.
6. Phase conservation and the specified bounce law give the retarded Jacobian
   and finite-count identity. Direct root differentiation and count integration
   independently check their numerical realization.

The algebraic target is proved under the stated hypotheses. There is no
open terminal lemma equivalent to that target. The strongest application
obligation is to obtain a joint orbital/clock/radio forward model and its
controlled errors from the candidate dynamics on the actual source and
trajectory. The action, potential, initial history and absolute scales remain
supplied or open; no parameter is selected by naming that obligation.

At zero scalar amplitude the data lose range sensitivity; at mu=0 the
positive-difference inverse has a boundary value. Negative finite-source
charge, multimode response, nonstationary or radiative backgrounds, screened
extended probes and noncircular data are different inverse problems. The
supplied two-mode numerical example illustrates additional data discrimination;
it does not exclude all multimode extensions. No theorem of impossibility,
independent wall count or exhaustion of alternative theories is asserted.

## Reproduction and focused review

Run from the repository root:

    python3 scripts/exponential_scalar_orbit_light_time_check.py

The runner compares direct angular Green integrals with exterior force/charge,
direct null-segment quadrature with the endpoint logarithm, root solutions
with inverse formulas, correlated finite-error corners with enclosures, and
retarded phase differences with proper-count integration. Its output is
`outputs/exponential_scalar_orbit_light_time_results.json`. This is a synthetic
operator check, not exhaustive numerical coverage or observational data.
The source proof supplies the universal quantifiers. Cached execution uses
`scripts/runner_cache.py` and its declared 120-second timeout.

Focused independent source confirmation and mutation results are recorded in
the campaign `REVIEW_HISTORY.md`; final evidence will be bound to the delivered
source bytes. The independent draft check corrected source-generated boundary
conditions, the test-body domain, physical-unit normalization and the wording
of the finite-error ratio test. The rational witness is retained above with
its exact derivation. No formal audit verdict or effective status is supplied.

## Claim-status record

```yaml
target_claim_id: exponential_scalar_orbit_light_time_reconstruction
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: "Exact inverse and coherent phase identities for the supplied local model"
hypothetical_axiom_status: null
admitted_observation_status: "Published gamma is exposed comparator only; no observation enters the inverse proof"
claim_type_reason: "The positive reconstruction and phase operator preserve explicit model and measurement hypotheses"
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: upstream_support
target_blocker_text: "Derive the remaining measured-gravity and environment bridge from observations rather than supplying it"
source_of_blocker_text: user_goal
reachability_to_target: "Separates the orbital force, photon transfer and coherent clock/count operators and reconstructs the ideal scalar range"
artifact_role: "Conditional analytic reconstruction with independent numerical operators"
next_trace_action: "Constrain the actual finite-source environment and joint orbital/radio forward model with registered calibration and validation data"
```
