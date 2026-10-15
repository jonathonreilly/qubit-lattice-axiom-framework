# Finite-window bounds on scalar initial-field contributions

**Date:** 2026-10-15
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_finite_window_history_check.py](../scripts/scalar_finite_window_history_check.py)

**Exact target:** derive energy bounds for time-averaged free scalar-field
contributions along prescribed subluminal observation paths, including the
full force from a supplied conformal matter action, and connect that observable
to adjacent finite velocity averages without choosing the initial field.

The observation problem comes first: finite tracking counts are averages,
while a reconstructed stationary force law leaves an initial-field remainder.
We ask which averaged force can be controlled from a quantitative energy
budget. The result derives a suitable averaging construction, its moving-path
bound and its physical normalization. It supplies no measured energy budget,
calibrated spacecraft trajectory, radio-to-force identification or scalar fit.

The free fields below denote homogeneous differences after a particular source
response has been separated in the stated linear operator. Time-dependent
source errors, background/metric changes and nonlinear remainder terms require
additional controlled contributions. They are not silently relabeled free data.
No raw observation product is read here; reserved products remain unopened.

## 1. Operator and Fourier conventions

Use s=ct, L=partial_s^2-Delta+mu^2 on R^3, mu>=0, with the supplied
stable frozen flat operator. Begin with real smooth rapidly decreasing
initial data q(x),p(x), and define

    h(s)=cos(s*Omega)q + sin(s*Omega)*p/Omega,
    Omega=sqrt(-Delta+mu^2),
    E=(1/2)*integral [|p|^2+|grad q|^2+mu^2*q^2] d^3x.

This is the mathematical energy in the displayed field normalization.
Physical scalar energy can have an additional kinetic/coupling factor;
neither its normalization nor its measured budget is silently supplied.

The spatial Fourier transform is unitary:
qhat(k)=(2*pi)^(-3/2)*integral exp(-i k.x)q(x)d^3x.
For a real time weight w in H1(R) intersect L1(R), use the nonunitary
time transform W(omega)=integral w(s) exp(i*omega*s) ds.
For fixed x0 and a fixed unit spatial vector e, define on smooth solutions

    A_w = integral w(s) e.grad h(s,x0) ds.

The bound below extends this linear functional continuously to the
energy completion. For rough finite-energy data this extension, rather
than an assumed classical pointwise trace, defines the average.

## 2. Exact dual norm and mass-independent enclosure

Put omega_k=sqrt(|k|^2+mu^2), C=Re W and S=Im W. The Fourier functional
contains (i e.k) exp(i k.x0) times [qhat C + phat S/omega_k].
Cauchy-Schwarz against the joint energy vector (omega_k*qhat,phat)
therefore yields

    |A_w| <= sqrt(2*E) * C_mu[w],

    C_mu[w]^2
      = (2*pi)^(-3)*integral (e.k)^2/omega_k^2
                                      * |W(omega_k)|^2 d^3k
      = 1/(6*pi^2)*integral_0^infinity
             k^4/(k^2+mu^2) * |W(sqrt(k^2+mu^2))|^2 dk
      = 1/(6*pi^2)*integral_mu^infinity
             (omega^2-mu^2)^(3/2)/omega * |W(omega)|^2 domega.

The angular factor is 4*pi/3. The real-data constraint is compatible
with the dual vector (imaginary odd spatial factors); smooth spectral
approximations reach the displayed operator norm. This is an energy-space
operator statement, not a count of numerical samples.

Since (omega^2-mu^2)^(3/2)/omega <= omega^2, real-weight Parseval gives

    C_mu[w]^2 <= ||w'||_2^2/(6*pi),
    |A_w| <= sqrt(E/(3*pi)) * ||w'||_2.

For mu=0 the norm enclosure is equality. No spatial support radius,
decomposition age, L1 initial norm or initial phase appears. The energy
E is still a required quantitative input. Shifting the center of w
multiplies W by a phase and changes no bound: widening an averaging
window is different from asserting that passive waiting erased history.

The same bound holds for the norm of the full vector average grad h:
apply it to each fixed unit e with the same constant and take the
supremum. This is not three independent uses of the energy budget.

## 3. The time window matters

For the normalized triangular weight

    w_T(s)=(T-|s|)/T^2 for |s|<=T, otherwise 0,

W(omega)=sinc(omega*T/2)^2, with sinc(x)=sin(x)/x, and
||w_T'||_2^2=2/T^3. Consequently

    |A_wT| <= sqrt(2*E/(3*pi*T^3)).

A normalized rectangular weight of support [-T,T] has
W=sin(omega*T)/(omega*T) and is not in H1. In the massless case
its energy dual norm with spectral cutoff Lambda obeys exactly

    C_box,Lambda^2 =
      [Lambda/2 - sin(2*Lambda*T)/(4*T)]/(6*pi^2*T^2).

The runner evaluates this formula at nine finite cutoffs. At the chosen
cutoffs 40/T, the rectangular values exceed the corresponding triangular
norm. These are explicit finite witnesses distinguishing two observables;
no claim about all instruments or alternative field theories is made.

## 4. A constructive finite-average readout

Let v be absolutely continuous on [s0-T,s0+T] with a=v', and define
bar_v_minus and bar_v_plus as its averages on the two adjacent intervals.
Fubini or integration by parts yields

    (bar_v_plus-bar_v_minus)/T
      = integral w_T(s-s0) a(s) ds.

This is exact. The triangular acceleration average is constructed from
two rectangular velocity averages; it does not demand a chosen initial
velocity or acceleration history.

For an explicitly supplied leading readout y(s)=kappa*v(s)+b+e(s),
with known nonzero constant kappa and constant b,

    (bar_y_plus-bar_y_minus)/(kappa*T)
      = integral w_T a
        + (bar_e_plus-bar_e_minus)/(kappa*T).

If the two average errors are bounded by eta_plus,eta_minus, the latter
error is at most (eta_plus+eta_minus)/(|kappa|*T).
If each average is formed as N/(f0*T) plus known constants with fixed
nonzero reference f0, nonnegative absolute count-error budgets
dN_plus,dN_minus give the bound
(dN_plus+dN_minus)/(|kappa*f0|*T^2).

These readout premises are not established by decoding an ODF record.
Real coherent links require the earlier exact phase/ramp/clock treatment,
changing lines of sight, moving worldlines, media and electronics.
All intervals here use the same s variable as the field equation;
seconds and station proper time require explicit conversion.

For the field functional above, the acceleration contribution must be
a specified constant multiple of a fixed-point field gradient. An actual
spacecraft samples a moving trajectory, and its force law and metric
response must be derived before assigning it this bound. A fixed-point
bound is not quietly claimed for arbitrary moving or accelerating paths.


## Moving-path phase estimate

Let w be real, continuous, compactly supported, with w' in L1 and w'' a
finite signed measure. Write W0=||w||_1>0, W1=||w'||_1, and
W2=||w''||_TV. A normalized triangle has W0=1, W1=2/T, W2=4/T^2;
its second derivative includes the jumps at -T,0,T.

On a neighborhood of the support let x(s) be C3 with
|x'|<=v_*<1, |x''|<=A, |x'''|<=J. Put delta=1-v_*>0.
For a spatial wave vector k and Omega=sqrt(|k|^2+mu^2)>0, take

    psi(s)=Omega*s-k.x(s),
    d(s)=psi'(s)/Omega=1-(k/Omega).x'(s).

Then d>=delta, |d'|<=A and |d''|<=J. Both frequency signs obey
the same bounds. Two integrations by parts, using distributional w'',
give

    I(k)=integral w exp(-i psi) ds
        = -Omega^(-2) integral exp(-i psi) *
          [w''/d^2 - 3*w'*d'/d^3 - w*d''/d^3
                                      + 3*w*(d')^2/d^4].

The first term is a measure integral. The jumps of w' must not be dropped.
There is no front or source singularity in this Fourier identity.
It implies

    |I(k)| <= min(W0, B/Omega^2),

    B = W2/delta^2 + 3*A*W1/delta^3
                  + J*W0/delta^3 + 3*A^2*W0/delta^4.

The isolated Omega=0 massless mode is handled by the direct W0 bound and
has zero Fourier measure. The estimate does not assume a constant velocity,
compact initial support or a prescribed phase.

## Moving-path energy envelope

For a fixed unit e and
A_w,x = integral w(s) e.grad h(s,x(s)) ds, the two-frequency energy
dual norm has integrand

    (2*pi)^(-3) * (e.k)^2/Omega^2 *
       (|I_plus(k)|^2+|I_minus(k)|^2)/2.

The two terms give equal integrated contributions by k->-k and reality.
Using the uniform phase bound, integrating (e.k)^2 over directions, and
Omega>=|k| gives

    C_path^2 <= 1/(6*pi^2) integral_0^infinity
                     k^2 min(W0^2,B^2/k^4) dk
               = 2/(9*pi^2) * B^(3/2) * W0^(1/2),

    |A_w,x| <= sqrt(2*E) * C_path.

Splitting at k=sqrt(B/W0) gives the displayed radial integral. The same
constant controls the norm of the full vector average by taking a
supremum over fixed unit e after integration; no extra sqrt(3) is needed.

For a triangle,

    B = 4/(delta^2*T^2) + 6*A/(delta^3*T)
                           + J/delta^3 + 3*A^2/delta^4.

This is a conservative bound. At a stationary path its constant need
not equal the sharper exact fixed-point norm derived above.

## Changing observation direction

Let n(s) be a real C2 vector with |n|<=1, |n'|<=N1 and |n''|<=N2.
For integral w n(s).grad h(s,x(s)) ds, use amplitude
a_k=w(s)*(n(s).k)/Omega in the two-frequency representation.
Its L1, derivative and second-derivative variation are bounded by

    L0 <= W0,
    L1 <= W1+N1*W0,
    L2 <= W2+2*N1*W1+N2*W0.

Thus define

    B_rot = (W2+2*N1*W1+N2*W0)/delta^2
             + 3*A*(W1+N1*W0)/delta^3
             + J*W0/delta^3 + 3*A^2*W0/delta^4.

Without pulling a constant spatial projection out of the time integral,
a safe angular estimate instead gives

    C_rot^2 <= 2/(3*pi^2) * B_rot^(3/2) * W0^(1/2),
    |integral w n.grad h| <= sqrt(2*E) * C_rot.

The factor three loss relative to the fixed-direction envelope is
deliberate. No claim of sharpness is made. If W0=0 the observable is zero.


## Force derived from the conformal matter action

Freeze the Einstein metric to Minkowski, use s=ct and c=1 for this
derivation, and take the supplied physical metric g_J=A(phi)^2 eta.
An ideal spinless test body of fixed Jordan mass has action

    S_p=-m integral A(phi(s,x)) sqrt(1-|v|^2) ds, v=dx/ds.

This test-body model omits self-gravity, finite-size forces, radiation
reaction and material sensitivities. For ell=log A, the Euler-Lagrange
equation is

    d_s(A gamma v)=-A gamma^(-1) grad ell,
    gamma=(1-|v|^2)^(-1/2).

The total derivative of ell along the body is
D_s ell=partial_s ell+v.grad ell. Inverting I+gamma^2 v v^T gives exactly

    a=dv/ds=-(1-|v|^2)[grad ell+v partial_s ell].             (1)

The time derivative is partial at fixed position, not D_s. Discarding
the v partial_s ell term would be an extra slow-motion/static premise.

About one constant background, use kinetic-normal scalar modes h_j,
alpha_j=partial log A/partial h_j at that background, and the leading
linear perturbation ell=ell_b+sum_j alpha_j h_j. The free operator
hypothesis is L_j h_j=0, L_j=partial_s^2-Delta+mu_j^2, mu_j>=0.
Then the free initial-field part of (1), to this stated order, is

    n.a_h=-sum_j alpha_j [P(s).grad h_j+R(s) partial_s h_j],
    P=(1-|v|^2)n, R=(1-|v|^2)(n.v).                         (2)

The evaluated trajectory and direction must be given or controlled.
This is a scalar contribution in the frozen metric. Tensor perturbations,
background gradients, source response, coupling variation and higher
orders have not disappeared from the physical acceleration.

## Energy envelope for the full scalar force

Let w have the regularity and W0,W1,W2 of the moving-path estimate above. Let x be C3, |v|<=V<1, |a|<=A2,
|d_s a|<=J3 and delta=1-V; n is C2 with |n|<=1,
|n'|<=N1, |n''|<=N2. Name L=1-|v|^2. Valid coefficient budgets are

    P0=1,
    P1=2*V*A2+N1,
    P2=2*(A2^2+V*J3)+4*V*A2*N1+N2,

    R0=V,
    R1=2*V^2*A2+N1*V+A2,
    R2=2*V*(A2^2+V*J3)
           +4*V*A2*(N1*V+A2)+N2*V+2*N1*A2+J3.

Here |P^(r)|<=Pr and |R^(r)|<=Rr for r=0,1,2.
Define Cr=Pr+Rr and

    L0=C0*W0,
    L1=C0*W1+C1*W0,
    L2=C0*W2+2*C1*W1+C2*W0,
    Bjet=L2/delta^2+3*A2*L1/delta^3
                          +J3*L0/delta^3+3*A2^2*L0/delta^4.

For each Fourier sign the normalized amplitude is
w(P.k/Omega +/- R). It has the three budgets L0,L1,L2.
The two integrations by parts from the moving-path estimate above therefore give

    Cjet^2 <= 2/(3*pi^2) Bjet^(3/2) L0^(1/2),
    |integral w [P.grad h+R partial_s h]|
                                     <= sqrt(2*E[h]) Cjet. (3)

This is conservative and uniform in nonnegative mass. The energy
completion defines the functional for rough data. If the path is
stationary and n constant, the sharper fixed-point triangular bound
can instead be used: Cjet^2<=1/(3*pi*T^3).

For finitely many kinetic-normal modes, a single joint energy budget
E_tot=sum_j E[h_j] and q=sum_j alpha_j^2 yield, by Cauchy-Schwarz
over the modes,

    |integral w n.a_h| <= sqrt(2*q*E_tot) Cjet.              (4)

Allocating the full energy independently to each field is unnecessary.
All scalar masses and coefficients remain conditional; no initial phase,
support radius or decomposition age is selected.

## Constant-velocity force control

For mu=0, triangle w_T, v=u e_z constant, and constant n, the exact
squared norms for the combination in (2) are

    C_parallel^2=(1-u^2)^2/(2*pi*T^3)
             integral_-1^1 (z-u)^2/(1-u*z)^3 dz,
    C_perpendicular^2=(1-u^2)^2/(4*pi*T^3)
             integral_-1^1 (1-z^2)/(1-u*z)^3 dz.            (5)

They follow by radial substitution Omega*(1-u*z) in the Fourier norm.
The factor z-u comes from the partial time derivative in (1).
For 0<|u|<1, put Dlog=log((1+u)/(1-u)). The change of variable
z_prime=(z-u)/(1-u*z) evaluates the two angular integrals as

    C_parallel^2=(1-u^2)^2*(Dlog-2*u)/(2*pi*T^3*u^3),
    C_perpendicular^2=(1-u^2)*(2*u-(1-u^2)*Dlog)
                                              /(4*pi*T^3*u^3).

At u=0 both continuous limits are 1/(3*pi*T^3).

These are mathematical controls of the same first-derivative functional,
not a claim that a freely accelerating spacecraft keeps constant velocity
in a nonzero field. They test the prescribed reference-path linearization.

## Physical energy and gravitational normalization

The supplied candidate has kinetic term -Q sum_j (partial h_j)^2
at the frozen point. In the Einstein units of its action the positive
quadratic physical scalar energy is therefore

    E_phi,E=2*Q*E_tot,E.

The coefficient Q is not silently set to one. At a constant background
A_b, use physical coordinates x_J=A_b*x_E, s_J=A_b*s_E.
Then E_tot,J=A_b*E_tot,E, E_phi,J=E_phi,E/A_b and
Q_J=Q/A_b^2. Thus E_phi,J=2*Q_J*E_tot,J and the physical-coordinate
version of (4) is

    |integral w_J n.a_h,J|
                 <= sqrt(q*E_phi,J/Q_J) Cjet,J
                  = sqrt(8*pi*G_bare*q*E_phi,J) Cjet,J,   (6)

where G_bare=A_b^2/(8*pi*Q) as in the existing response note.
The left side is acceleration with respect to s_J, in natural units;
a conversion to acceleration per second squared requires the c^2 factor
and consistent conversion of every right-hand-side natural-unit quantity.
No formula with SI G and joules substituted directly is asserted here.
This is the positive quadratic perturbation energy, not an absolute
cosmological vacuum energy.

For the candidate's local scalar sector, supply 0<k<1/3 and

    a=(1-k)(1+3*k)/4, sigma=(1+k)/(k*(1-3*k)),
    Z=exp(2*sqrt(a)*u), F=1+sigma*Z,
    J=1+(1-3*a)*sigma*Z,
    K_uu=J/F^2, K diagonal with positive other entries,
    A^2=(1+sigma)*Z/F, A independent of the other fields.

Then partial_u log A=sqrt(a)/F and
q=alpha_A K^{AB}alpha_B=a/J. The identity
1/3-a=(1-3*k)^2/12>0 and J>1 prove 0<q<1/3
at every finite background in this supplied scalar sector. Potential
selection, mass stability and actual background identification are separate
hypotheses, not consequences of this algebra. If, in addition, an actual
same-background gravity measurement has a valid positive-geometry weak
response G_meas=G_bare*(1+q_geom) with q_geom>=0, then
G_bare<=G_meas and

    |integral w_J n.a_h,J|
                  <= sqrt((8*pi/3)*G_meas*E_phi,J) Cjet,J. (7)

This is a conditional substitution of an experimentally calibrated
normalization; actual finite-body/environment/clock errors must be bounded.
It does not make a quoted laboratory error into a bound on response-model
error. A different environment, signed geometry or unstable response
does not meet this premise.

For the stationary triangular limiting functional, (7) reduces to
sqrt(8*G_meas*E_phi,J/(9*T_J^3)). Even there E_phi,J is still an
independently required quantitative energy budget. No value of it,
G_meas, q, A_b, Q or T_J is fitted or inferred here.


## Complete observable and empirical separation

For a supplied leading readout proportional to n(s).v(s), adjacent averages
produce a triangular average of n.a+n'.v. The geometric term obeys
|integral w_T n'.v|<=N1*V and must be removed or bounded. A changing
proportionality, retarded endpoint or station clock introduces further terms.
The exact finite-count phase convention from the earlier campaign work is
context, not a calibrated force measurement used in this proof.

The strongest checked result is the energy envelope for the specified free
field and observation functional. It replaces compact initial support, an
initial phase and a source-age selector for that functional with a quantitative
energy input. It does not infer that input or a preferred state. The physical
application still needs a common candidate-consistent trajectory/clock/ray
operator and a quantitative budget for free scalar energy, forcing and
linearization remainders. No independent observation, parameter fit or selected
fundamental constant is represented by these synthetic controls.

## Proof obligations and imports

| Step or input | Provenance and role | Disposition |
| --- | --- | --- |
| Stable constant-mass free KG operator on flat space | Supplied local physical model; not derived from observations | Fourier solution and energy norm proved under this hypothesis |
| Unitary spatial Fourier transform and ordinary real time transform | Mathematical conventions | Factors and real-data compatibility derived above |
| Fixed-point and moving temporal functionals | Defined observable and supplied path/direction regularity | Exact stationary norm and conservative moving envelopes derived here |
| Subluminal margin, acceleration, jerk and direction bounds | Quantitative kinematic inputs | Not measured or inferred by the runner |
| Universal conformal test-body action | Supplied matter model in a frozen metric | Exact coordinate acceleration derived; free-field linearization is explicit |
| Positive kinetic metric, nonnegative masses and finite mode count | Supplied local scalar regime | Joint mode energy bound derived here |
| Candidate K and A formulas, Q and background units | Explicit supplied sector above; full-action provenance is the current-main local-response note | Coupling ceiling and normalization conversion derived without choosing parameters |
| Physical scalar energy and optional same-background gravity response | Quantitative physical inputs and conditional calibration relation | Q can be expressed through G_bare; no measured budget or environment is assigned |
| Count/velocity proportionality, constant reference and errors | Optional supplied observation model | Adjacent-average identity and absolute error bound derived; actual radio calibration remains application work |

The proof graph is Fourier evolution to the energy dual norm; real-weight
Parseval to the stationary enclosure; distributional integration by parts and
a subluminal phase bound to the moving envelope; Euler-Lagrange variation to
the scalar force; the joint mode norm and constant-frame conversion to the
physical-energy bound; and ordinary integration by parts to the adjacent-average
readout. All these mathematical steps appear here. The missing empirical
calibration is an application obligation, not a premise asserting the target
theory or a claim that the theory has been validated.

The domains include mu=0, stationary paths and zero energy; the zero Fourier
mode contributes no gradient and is handled by limiting energy-space
approximation. T>0 and V<1 are explicit. Signed time weights use L1 and total
variation norms; only the geometric N1*V shortcut uses a nonnegative normalized
triangle. All frequencies, coordinates and energy units must be consistent.
A chosen minimum-energy state, an untested history probability measure and an
actual compact-support assumption are not introduced.

The supplied-action provenance is
`EXPONENTIAL_SCALAR_LOCAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-10-13.md`
and `EXPONENTIAL_SCALAR_ENVIRONMENT_BRIDGE_BOUNDED_THEOREM_NOTE_2026-10-14.md`
at main commit 92574ffe95192cc0724a27e1acad28e42d325115. The local formulas
needed here are explicitly restated and re-derived. No ancestor runner output
or retained-grade authority is assumed.

## Execution and review record

The primary runner directly imports the three temporal, moving and force-energy
helper modules, declares them and this note as inputs, and writes products only
under its requested output directory. It reads no scientific data or ancestor
output. Package-local integrity reads hash the note and its source closure.
Python, NumPy, SciPy, SymPy and mpmath are required. The declared timeout is
120 seconds. The canonical cache belongs under
`logs/runner-cache/scalar_finite_window_history_check.txt`.

The canonical runner executes 70 temporal, 133 moving and 57 force/normalization
controls, with independent derivations and separate executable checks. These
are synthetic controls, not observations or a proof of generality. Exact
inequalities rest on the displayed arguments. The temporal review clarified
that count-error symbols denote nonnegative absolute budgets. No equation or
code changed for that clarification. Source-bound final checks and mutation
records are kept in the campaign pack. Combined landing validation and formal
independent audit remain outstanding; no audit-owned status is written here.

## Claim-status record

```yaml
target_claim_id: scalar_finite_window_initial_history
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
conditional_surface_status: "Energy bounds for a specified free-field observable under an explicit local operator and measurement model"
hypothetical_axiom_status: null
admitted_observation_status: "No new observation values or empirical scalar tests"
claim_type_reason: "Positive operator norm bounds and finite-average construction with explicit physical hypotheses"
audit_required_before_effective_retained: true
bare_retained_allowed: false
trace_class: upstream_support
target_blocker_text: "Derive or eliminate remaining scalar initial-history and measured-gravity assumptions"
source_of_blocker_text: user_goal
reachability_to_target: "Supplies a finite-window bound without selecting an initial profile; actual physical energy and readout calibration remain open"
artifact_role: "Conditional scalar observation theorem and synthetic controls"
next_trace_action: "Determine an observationally justified energy or residual budget and verify the full clock/trajectory/forcing approximation before fitting scalar signatures"
```
