# Observation-derived scalar response for accelerated coherent counts

**Date:** 2026-10-15
**Status:** proposed_retained
**Claim type:** bounded_theorem
**Actual current surface status:** conditional-support
**Primary runner:** [scalar_accelerated_coherent_count_check.py](../scripts/scalar_accelerated_coherent_count_check.py)

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: scalar_accelerated_coherent_count
target_blocker_text: "Derive or eliminate the scalar theory's remaining initial-state and measurement assumptions"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Establish actual trajectory, clock and link calibration with an independently supported error or energy budget"
conditional_surface_status: "Exact linear response and massless Gram under the displayed field, action and measurement premises"
hypothetical_axiom_status: null
admitted_observation_status: "No observational values enter this theorem or its synthetic controls"
claim_type_reason: "The response and energy implication are derived; their physical premises remain supplied"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The downstream consumer is the campaign's reconstruction of scalar history from
finite tracking counts. This support result does not establish that the actual
tracking residual obeys the supplied scalar model.

**Exact target:** derive the orbital and proper-clock sensitivity of finite one-way and ideal coherent radio counts, then obtain the exact joint massless energy Gram along prescribed accelerated paths. Exact observable contrasts remove specified initial-state, nuisance and constant-offset responses; they do not select a physical field state.

The starting object is a count between fixed receiver proper-time labels. The arbitrary force window used in a generic bound is replaced here by the response of that observation through supplied trajectory dynamics. This closes a named conditional construction gap, while actual calibration, action/potential, reference dynamics, field energy, absolute scales and error budgets remain open. No new archive values are opened or fitted. All controls are mathematical or synthetic development tests, with no independent empirical validation.

## Supplied action, force and energy conventions

Use c=1 and one common real free massless scalar perturbation h on a flat Einstein coordinate patch. Supply the conformal physical metric A(phi)^2 eta, with background A_b>0 and delta log A=alpha h for constant alpha. These are premises, not derivations of the user's action or potential. With the supplied massive test-body action -m integral A sqrt(1-|u|^2) ds, Euler-Lagrange gives

    d_s(A gamma u)=-grad A/gamma.

Substituting d_s log A=partial_s log A+u.grad log A and solving the rank-one velocity equation gives

    u'=-(1-|u|^2)[grad log A+u partial_s log A].

Thus its linear perturbative force at a constant background is alpha a_h with the a_h displayed below. The partial time derivative is at fixed x. If an external force is prescribed, its full perturbation must also be modeled; the synthetic additive coordinate-force examples below explicitly choose its Jacobians and zero extra scalar dependence. Proper-force specifications can differ. No tensor, matter-source or nonlinear scalar closure is inferred.

The laboratory field energy is E=1/2 integral[p0^2+|grad h0|^2] on R3; the Hilbert norm is2E. For positive plane branches h=(2pi)^(-3/2) integral[a(k) exp(i|k|s-i k.x)+conjugate] d^3k, real-energy pairing gives norm squared4 integral |k|^2 |a(k)|^2. The complex a has no extra a(-k)=conjugate(a(k)) restriction: reality is already implemented by the explicit conjugate. The background/zero-mode domain is stated in the joint norm section. These linear probes are not an assertion that all nonlinear scalar histories obey this action or energy.

| Input | Role | Provenance | Open physical obligation |
| --- | --- | --- | --- |
| Free massless field, conformal metric and test-body action | Defines field energy, force and clocks | Supplied candidate, explicitly defined and differentiated in this note | Derive or discriminate action, potential and valid linear regime |
| Reference trajectories and external linearized dynamics | Maps field forcing to body and clock perturbations | Supplied smooth timelike model; synthetic fixtures are declared choices | Jointly calibrate actual environment and scalar response |
| Proper-time labels, constant source frequency, geometric optics and ideal coherent transfer | Defines the count observable | Explicit measurement hypotheses here | Bound real clocks, media, electronics, delays and calibration errors |
| Anchored energy domain or exact constant-response cancellation | Makes the joint observable energy-controlled | Mathematical domain and response column derived below | Determine physical background and energy/error budget independently |
| Real Fourier duality, Parseval and finite-dimensional Hilbert projection | Mathematical tools | Conventional mathematics, with used normalization and proof steps restated here | No physical premise retired by these tools |

## 1. Physical reference and light-time variation

Use a frozen flat Einstein coordinate metric and a conformal physical metric A(phi)^2 eta. The scalar perturbation h is free and massless in that coordinate patch; delta log A=alpha h for a constant supplied coupling. External specified reference dynamics generate smooth emitter and receiver worldlines x_e(s),x_r(s), with |u_A|<1. Their reference proper lapse is ell_A=A_b sqrt(1-|u_A|^2), A_b>0. Conformal geometric-optics null rays have the flat coordinate light cone in this model. Tensor perturbations, media, finite transponder delays, electronics and other scalar-dependent external forces remain outside this supplied one-way model.

For receiver coordinate event s, the reference emission time t=E(s) obeys

    s-t=|x_r(s)-x_e(t)|,
    n=[x_r(s)-x_e(t)]/|x_r(s)-x_e(t)|,
    D_e=1-n.u_e(t),    D_r=1-n.u_r(s),
    E'(s)=D_r/D_e.

Require nonzero range, unique causal solution and uniform subluminal margins on the compact interval. These justify the implicit derivatives. Write xi_A(s)=delta x_A(s) at fixed coordinate time and eta_A(s)=delta tau_A(s). For an observation at fixed receiver proper time, delta s=-eta_r(s)/ell_r(s). Linearizing light time gives

    delta t=[D_r delta s+n.(xi_e(t)-xi_r(s))]/D_e.

For a source of constant proper phase frequency nu_0, with no additional link phase, the received phase variation divided by nu_0 is

    chi(s)=eta_e(t)-R(s) eta_r(s)
             +ell_e(t)/D_e * n.(xi_e(t)-xi_r(s)),
    R(s)=ell_e(t)D_r/[ell_r(s)D_e].                    (1)

No emitter proper-time or receiver-time perturbation is silently omitted. A normalized finite count over fixed receiver proper-time endpoints tau_a,tau_b is

    delta y_i=[chi(s_b)-chi(s_a)]/(tau_b-tau_a).       (2)

A reference oscillator phase at those fixed proper endpoints contributes no additional variation if its specified proper frequency is fixed. Unknown initial phases, instrumental shifts or chirps require their own explicit nuisance or additional clock/source terms. Shared endpoint covariance is not presumed diagonal.

## 2. Derive the field weights through an augmented trajectory adjoint

For each body let z_A=(xi_A,delta u_A,eta_A). Supply the linearized external background F_A and its coefficients J_x,J_u. The conformal scalar forcing and proper-clock equation give

    xi_A'=delta u_A,
    delta u_A'=J_x xi_A+J_u delta u_A+alpha a_h,A,
    eta_A'=-A_b gamma_A u_A.delta u_A+ell_A alpha h(s,x_A(s)),
    a_h,A=-(1-|u_A|^2)[grad h+u_A partial_s h](s,x_A(s)),
    gamma_A=(1-|u_A|^2)^(-1/2).                        (3)

Here external dynamics and coordinate/clock calibration are premises, while their response weights are derived. General coupled-body linear dynamics can be used as one larger state. This version omits unmodeled scalar-dependent external-force variations rather than declaring them zero in nature.

Choose s0 strictly before every emitter/receiver observation endpoint; this is a supplied initial-data epoch. If an observation atom is instead placed exactly at s0, its coefficient q_i0 must be added to lambda_i(s0+) in the initial-state row. Equation(2), using(1), is a finite sum of specified position and clock endpoint functionals. Their emitter and receiver coordinate times differ. For any such linear observation plus distributed readouts o_i(s)^T z(s), with each o_i in L2 on this finite interval, define lambda_i backward by

    lambda_i'=-L(s)^T lambda_i-o_i(s),
    lambda_i(T^+)=0,
    lambda_i(t_j^-)=lambda_i(t_j^+)+q_ij.

Then the exact first-order count is

    y_i=lambda_i(s0)^T z(s0)
       +sum_A integral [W_i,A.a_h,A+c_i,A h(s,x_A)] ds
       +(X beta)_i+e_i,
    W_i,A=alpha lambda_i,v_A,
    c_i,A=alpha ell_A lambda_i,eta_A.                  (4)

This follows by differentiating lambda^T z and retaining every endpoint jump; it is also variation of constants. A real contrast vector t annihilates arbitrary initial orbital/clock perturbations iff sum_i t_i lambda_i(s0)=0. It must separately satisfy X^T t=0 for nuisance elimination. A nonzero contrast need not exist: require a rank calculation, not a promised extra channel.

The endpoint rows in(1) touch positions and clocks, not velocities. Therefore lambda_v has no jump at those events; lambda_eta may jump. With bounded piecewise continuous L and positive finite endpoint separations, W is piecewise H1 and continuous. Its final trace is zero. After the full initial-state contrast, its initial trace is also zero, so zero extension gives compact H1 W. The direct clock weight c is only piecewise L2; that is sufficient below. Velocity endpoint readouts would generally jump lambda_v, and require a different regularity analysis. Eliminating only constant velocity is insufficient when the actual trajectory dynamics couple positions, velocities and clocks.

## 3. Joint massless clock/force energy Gram

Use the real Hilbert completion of smooth compactly supported initial data under ||(h0,p0)||_H^2=integral(|grad h0|^2+p0^2), with h0 represented by its homogeneous-H1 Sobolev representative in L6(R3). Thus the constant scalar background is fixed explicitly. Finite gradient energy alone, if an arbitrary added spatially constant h0 is also permitted, cannot bound this joint observable unless sum_A integral c_A ds=0: that added constant has zero energy/force and changes the readout by h0 sum_A integral c_A. The arbitrary constant is not an energy-controlled datum or a derived initial-state selector. No claim that actual radio contrasts automatically satisfy that cancellation is made.

For one prescribed C2 path, u=x', |u|<=beta<1, take real compact c in L2 and real compact W in H1 with zero endpoint traces. Let n be a unit spatial direction and define

    phi_n(s)=s-n.x(s),    d_n=1-n.u(s)>0,
    b_n=(1-|u|^2)(n-u)/d_n,
    R_n(tau)=b_n(s(tau)).W(s(tau)),
    S_n(tau)=c(s(tau))/d_n(s(tau)),
    H_n(tau)=S_n(tau)-partial_tau R_n(tau).            (5)

The initially smooth field observable extends continuously to this anchored energy space by the norm derived below; no pointwise trace on arbitrary finite-energy data is assumed. All are zero-extended on the corresponding phase interval; the force zero traces remove boundary deltas. The minus sign is substantive. For the real plane branch exp(i k[s-n.x]), h has amplitude1 and a_h has amplitude i k(1-|u|^2)(n-u). With the transform F[f](k)=integral f(tau) exp(i k tau) d tau,

    T(k,n)=F[S](k)+i k F[R](k)=F[S-R'](k).

Combining both real frequency branches in the full angular integral, the lab-energy dual Gram for ||h||_H^2=2E is

    G_ij=1/(8pi^2) integral_S2 integral_R H_i,n(tau) H_j,n(tau) d tau dOmega.  (6)

No clock-force independence assumption is made. In coordinate time the single-path density is

    G_ij=1/(8pi^2) integral_S2 integral
       [c_i-partial_s(b_n.W_i)] [c_j-partial_s(b_n.W_j)]/d_n ds dOmega.       (7)

For a stationary path this reduces to

    G_ij=(1/(2pi)) integral c_i c_j ds
             +(1/(6pi)) integral W_i'.W_j' ds,

because the mixed angular odd term integrates to zero. For a general moving path the mixed term remains. A static zero cross term is not a general rule.

For finitely many distinct paths A, define H_i,A,n on each path's own common phase variable tau=s-n.x_A(s), then sum H_i,n=sum_A H_i,A,n BEFORE forming the Gram. Distinct source locations shift those phase supports. Evaluating cross terms at equal coordinate time or summing separate nonnegative energies would be a different operator. Field modes with a shared normalization are handled by the joint direct-sum Hilbert space, but this working result is massless; a massive extension needs a new argument.

## 4. Eliminate a constant perturbation through the observed response

Within the same linearized observation model, calculate the response column

    b0_i=sum_A integral c_i,A(s) ds.                  (8a)

This column is derived from the count/trajectory adjoint, not supplied as an arbitrary selector. For a spatially and temporally constant perturbation h=k, a_h=0 and the field contribution is exactly k b0_i. Consequently a contrast t removes this additional zero-energy freedom precisely when b0^T t=0. Use the actual span of [N,X,b0], where N_i=lambda_i(s0)^T. Existence of a nonzero contrast requires the corresponding rank to leave a nontrivial nullspace; adding this column can consume a channel. The scalar count mapping and these columns must be known to the required accuracy; no measurement-calibration uncertainty is silently set to zero.

For contrasts satisfying all three conditions, the joint operator descends to the energy space modulo additive constants. The same Gram formula holds for the anchored representative plus any constant because the observable is unchanged. This eliminates sensitivity to an unknown first-order constant scalar offset for this specified observable. It does not determine the absolute background A_b, its coupling alpha, the action, the field energy, a massive zero mode, or an environmental boundary condition. Outside these contrasts the fixed-background premise remains necessary. A finite-dimensional projection removes information rather than deriving an actual state.

A synthetic control example with 22 finite counts, 14 initial orbit/clock components and two instrument columns has seven floating nullspace directions before b0 and six after b0. The pre-existing contrasts leave a nonzero constant-mode response of order 3.24e-8 in the chosen normalization. That small finite number is not an energy bound for an arbitrarily large zero-energy constant. The numerical rank is a controlled floating experiment, not a certified exact rank or an actual radio calibration.

## 5. A sufficient energy bound and inverse interpretation

The algebraic identity

    (1-n.u)^2-(1-|u|^2)|n-u|^2=(n.u-|u|^2)^2

gives |b_n|<=1. With a=||u'||_infinity,

    |b_n'|<=D_beta a,
    D_beta=2beta/(1-beta^2)+(1+beta)+1/(1-beta).

Therefore for a single path

    G(W,c;W,c)<= [||c||_2+||W'||_2+D_beta a ||W||_2]^2/[2pi(1-beta)].        (8b)

For multiple paths use the square of the sum of the individual norm bounds, preserving one common field-energy budget. This is only a sufficient bound. The exact finite observation Gram(6) can instead be used as follows. For the bounded finite real-Hilbert observation map B, G=BB*. A residual r is feasible iff r belongs to range(G). The minimum-norm representative is h_min=B*G^+r and E_min=r^T G^+r/2: B h_min=r and every other solution differs by an orthogonal element of ker(B). This proves feasibility and the least possible energy without selecting the actual state. Errors and unremoved nuisance terms must first be retained in r; a singular pseudoinverse alone does not make an infeasible residual possible. No upper energy/error budget follows from these operator identities.


## 6. Ideal coherent multileg transfer

### Reference and exact phase premises

Use the same constant conformal background and prescribed subluminal paths.
A signal visits ordered events (A_0,t_0),...,(A_m,t_m), with a distinct nonzero
flat coordinate null separation on every leg. A body may occur more than once;
its clock and dynamical state must then be shared, not duplicated as independent
sources. For leg j from j-1 to j define

    n_j=[x_Aj(t_j)-x_A(j-1)(t_(j-1))]/range_j,
    D_j^- = 1-n_j.u_A(j-1)(t_(j-1)),
    D_j^+ = 1-n_j.u_Aj(t_j),
    R_j = D_j^+/D_j^-.

Every root is causal and unique within the supplied histories, and every D is
bounded away from zero. An ideal instantaneous coherent transponder passes
phase with a fixed known multiplier and an additive constant. It has no
independent oscillator phase in this model. The product of its multipliers is
kappa. This electronics/zero-delay premise is explicit; real hardware,
time-dependent delays, media and phase corrections need their own operators.
For a constant proper source frequency nu_0 the received phase in cycles is

    Phi_r = kappa nu_0 tau_A0(t_0) + constant.

Consequently a count between fixed proper receiver labels T_a,T_b is the
difference of those emitted phases. No intermediate proper clock is read by
this specified ideal phase map.

### Endpoint variation by backward composition

Write xi_A and eta_A for the fixed-coordinate position and proper-clock
variations as in the one-way derivation above. At the final proper-time endpoint,

    delta t_m=-eta_Am(t_m)/ell_Am(t_m).

Each linearized null leg gives, with all terms evaluated at its own events,

    delta t_(j-1)=R_j delta t_j + B_j,
    B_j=n_j.[xi_A(j-1)(t_(j-1))-xi_Aj(t_j)]/D_j^-.

Iterating the actual leg equations, rather than replacing them by a single
equal-time range, yields

    delta t_0=(product_(j=1)^m R_j) delta t_m
               +sum_(j=1)^m (product_(l=1)^(j-1) R_l) B_j.

The empty product is one. The source clock variation at its retarded event is
eta_A0(t_0)+ell_A0(t_0) delta t_0. Therefore define

    chi_m=eta_A0(t_0)
          -[ell_A0(t_0)/ell_Am(t_m)] (product_j R_j) eta_Am(t_m)
          +ell_A0(t_0) sum_j (product_(l<j) R_l) B_j.

The normalized finite count variation is

    delta y = kappa [chi_m(T_b)-chi_m(T_a)]/(T_b-T_a),

where y is in units of nu_0. All intermediate positions occur at their separate
events. Their coefficients can add, cancel or have different directions; no
assumed static line of sight replaces them.

### Initial-state, intermediate-clock and energy consequences

These observations again have only position and proper-clock endpoint atoms,
with no velocity atoms. The augmented orbit/clock adjoint therefore derives W
and c under the same regularity conditions. For an ideal two-leg station ->
spacecraft -> same station link, both source and final clock terms belong to
one station state. No spacecraft clock endpoint row occurs. In the supplied
clock-independent external trajectory dynamics, the spacecraft clock adjoint
is identically zero, so its direct field coefficient c_spacecraft is zero.
Its force coefficient W_spacecraft need not vanish: its moving position still
affects both null legs. Thus a separate spacecraft oscillator history is absent
because of the exact phase-transfer premise. It is not legitimate to delete
spacecraft clocks in a noncoherent or delayed hardware model by the same step.

The complete initial-state columns N, explicit instrument columns X and the
constant-offset response b0=sum_A integral c_A are derived from this multileg
operator. Contrasts must annihilate their actual spans. With enough surviving
rank, the vector force weights have zero outer traces and are compact H1, while
the direct field weights are compact L2. Sum all path contributions at common
arrival phase before squaring to use the massless joint energy Gram from the
joint norm above. No independent energy allocation to uplink/downlink bodies is
assumed. Repeated visits to one body are contributions to the same field and
same physical trajectory.

This reconstruction removes a supplied arbitrary response kernel within the
stated link model; it does not determine the real link calibration, initial
field energy, external dynamics, absolute scale, environmental solution, action
or potential. It also makes no accelerated positive-mass claim. Finite numerical
perturbation tests can check the first variation; they do not give an observed
noise bound or a certified nonlinear remainder enclosure.

## 7. Exact physical-count and energy composition fixture

Use a stationary free reference station at0 and spacecraft at L e1, with
L=3/5, constant conformal background A_b=1, unit coordinate/proper count
duration, instantaneous coherent return, and alpha*kappa=1. The source proper
frequency is constant. The scalar field and perturbed test-body dynamics remain
the supplied massless/conformal model. The station's clock is shared at emission
and reception. With receiver time t, the emission/bounce times are t-2L,t-L.
The first-order source phase before turnaround multiplication, normalized by
the source proper frequency as in section 6, is

    chi(t)=eta_s(t-2L)-eta_s(t)
           +e1.[xi_s(t-2L)+xi_s(t)-2xi_b(t-L)].

For the first contrast take times t_j=7/5+j, j=0,1,2 and coefficients
beta=(1,-2,1). The bounded normalized count contrast is
kappa sum_j beta_j chi(t_i,j), the later unit-time count minus the earlier one.
The second contrast translates all three times one unit later. The displayed
weights and harmonic response below have absorbed alpha*kappa=1; alpha and
kappa need not individually equal one. Define

    F_a(s)=sum_j beta_j (t_j-a-s)_+.

Each F_a is the unit triangular force window: zero before t_0-a, slope+1 on
(t_0-a,t_1-a), slope-1 on(t_1-a,t_2-a), zero afterward. Exact zeroth/first
moments sum beta=sum beta*t=0 remove the arbitrary initial body positions and
velocities. The shared clock anchor cancels. The derived weights are

    W_s=e1(F_2L+F_0),    W_b=-2e1 F_L,
    c_s=-F_2L'+F_0',     c_b=0.

They are compact H1/L2 with exact zero outer force traces. The total direct
coefficient integrates to zero, so adding a constant scalar perturbation does
not change this observable. No scalar initial field or physical energy is
selected by these moment identities.

Let z=n.e1. The shared arrival-time amplitude is

    H_z(tau)=-(1+z) F_2L'(tau)+(1-z) F_0'(tau)
               +2z F_L'(tau+Lz).

The spacecraft term is shifted by its actual spatial position. Evaluating it
at equal coordinate time would change the operator. Hence

    G_ij=(1/(4pi)) integral_(-1)^1 integral_R H_i,z H_j,z d tau dz.

All pieces are constants in tau with coefficients linear in z. Their interval
endpoints are affine in z; their order changes only at z=-2/3,2/3. Integrating
the polynomial overlap on these three angular pieces gives exactly

    G = 1/(1620 pi) [[3064,-1871],[-1871,3064]].

Its eigenvalues1193/(1620pi) and4935/(1620pi) are positive, so the exact two
contrast observations have a nondegenerate free-field energy response. This is
a Gram statement for the supplied model, not a claim that measured residuals
are scalar or that a field energy upper budget has been inferred.

### Separate original harmonic-response calculation

Use the plane branch h=exp(ik[s-n.x]). A particular station/spacecraft response
has eta=-i alpha h/k and xi=-i alpha n h/k; arbitrary homogeneous orbit/clock
pieces vanish in the exact contrast moments above. Substitution in
kappa sum_j beta_j chi(t_i,j), with alpha*kappa=1, gives the original coherent
response

    T_i(k,z)=(-i/k) sum_j beta_j exp(ik t_i,j)
       [(1+z)exp(-2ikL)+(z-1)-2z exp(-ikL(1+z))].

Write its numerator as sum_l a_i,l(z) exp(ik q_i,l(z)); each coefficient sum
vanishes. The radial identity integral_0^infinity[1-cos(k x)]/k^2 dk=pi|x|/2
then implies

    integral_0^infinity Re[T_i conjugate(T_j)] dk
       =-(pi/2) sum_lm a_i,l a_j,m |q_i,l-q_j,m|.

It follows from integration by parts and the Dirichlet sine integral; an
exponential regulator gives the same limit without conditionally exchanging
individual divergent terms. Only the finite zero-sum combination is used.
The original real energy normalization gives

    G_ij=(1/(4pi^2)) integral_(-1)^1 integral_0^infinity
             Re[T_i conjugate(T_j)] dk dz.

The pairwise time differences are affine in z. Exact polynomial integration
over the sign partitions reproduces the displayed matrix entry by entry. The
author program implements this event-pair calculation separately from interval
overlap; neither imports the other result.

Omitting the station direct-clock response changes4piG by
[[−344,166],[166,−344]]/135. Collapsing spacecraft arrival time to station
coordinate time changes4piG by[[3848,−2557],[−2557,3848]]/405. Both are explicit
rejected variants of this controlled model. They are not rejected theories of
all possible measurements.

The general accelerated theorem remains dependent on exact response columns
and trace cancellation. A numerically small initial/constant response is not
an exact cancellation when those unknown amplitudes are unbounded. Given a
computed design C_hat and contrast t with C_hat^T t=0, the actual nuisance
leakage is t^T(C-C_hat)theta. If ||theta||<=M, its magnitude is bounded by
M||(C-C_hat)^T t||; without such a bound, a nonzero model error leaves no
uniform cancellation claim. Real calibration and initial-state/error bounds
therefore remain application work. This exact fixture avoids numerical-nullspace
ambiguity only for its stated stationary model, not for actual tracking data.


## 8. Why the inertial substitution fails

The accelerated coefficient derivative includes b_n'. This term cannot be discarded by inserting an instantaneous velocity into an inertial result. A complete counterexample uses a C2 path with u=beta sin^2(pi s)e1 on[0,1], zero outside, for0<beta<1. Choose a compact H1 vector window W=e1 w that equals1 on[0,1], rises from0 to1 on[-1,0] and falls to0 on[1,2]. Velocity and acceleration vanish on the two ramps, and W'=0 during the moving plateau. The true norm is the stationary ramp norm plus the strictly positive angular integral of |b_n'.e1|^2/d over the plateau. An instantaneous inertial W'-only expression misses exactly that positive term. This rejects this particular extension of the inertial formula, not the scalar theory or all accelerated bounds.

## 9. Proof obligations and boundary cases

| Obligation | Disposition inside this note |
| --- | --- |
| Proper-time phase/count and multileg endpoint response | Derived by implicit differentiation and exact phase composition under the supplied propagation/link model. |
| Field-to-orbit/clock response weights | Derived by the augmented-state adjoint with retained endpoint jumps. |
| Compact H1 force and L2 direct weights | Proved from position/clock atoms, L2 distributed readouts, bounded dynamics and exact initial-state cancellation. |
| Joint accelerated massless energy Gram | Derived from real energy duality, monotone phase coordinates and Parseval; direct field and force signs remain coupled. |
| Unknown constant-offset response | Derived from the same weights; an additional exact nullspace condition removes this response without selecting a background. |
| Actual-count/Gram composition | Exact stationary rational example and independently represented spectral integral; accelerated numerical controls remain finite diagnostics. |
| Actual measurement calibration and error/energy budget | Open application obligations, not terminal lemmas assumed to have been derived. |

No retained framework authority or unmerged theorem is needed for a proof step: the used action/field/readout premises and mathematical steps are restated here. Prior campaign notes are provenance. The strongest missing physical bridge is a validated mapping of actual radio counts and their uncertainties to this specified trajectory/clock/free-field operator. A physical energy upper budget is also required to turn the resulting energy requirement into an exclusion. Neither is supplied by a small residual or a projection rule.

If alpha=0, all scalar weights and their Gram vanish; a nonzero residual needs another explanation. An empty contrast space supplies no scalar constraint. A singular Gram requires the displayed range condition. Uniform timelike margin is required; the lightlike limit is excluded. Positive mass, unmodeled sources, nonconstant background corrections, arbitrary nonsmooth worldlines, velocity endpoint atoms with uncancelled jumps, independent transponder clocks or delays and uncertain calibrations require separate arguments. The stationary exact fixture does not certify a numerical rank for accelerating paths.

## 10. Verification, provenance and remaining obligations

The primary runner calls five source helpers and writes their results and a source-bound summary under outputs/scalar_accelerated_coherent_count. It reads no external scientific files or observations; its integrity reads include its own source, those helpers and this note. Every source helper declares the same180second cap; the primary cache uses its declared180seconds. Run `/usr/local/bin/python3 scripts/scalar_accelerated_coherent_count_check.py`, or the repository runner_cache envelope for a canonical cache.

The canonical author controls are15 joint Fourier/time/multipath comparisons,9 proper-endpoint finite-variation checks,22 one-way orbit/clock adjoint checks,14 coherent-link checks and15 exact composition checks. The nonlinear synthetic tests solve perturbed worldlines and clocks and then solve actual null intersections at fixed receiver proper times. Their factor-four central-difference convergence verifies a first variation in those examples, not a uniform nonlinear error enclosure. Plane-wave probes in the local ODE checks have infinite global energy and are not used as finite-energy empirical states. The exact composition fixture instead evaluates the Hilbert dual through its complete spectral integral.

The two initial author numerical failures remain preserved in the campaign pack: coarse multipath angular resolution exceeded the unchanged tolerance, and a finite perturbation step left a truncation error just above its tolerance. Increasing angular resolution or decreasing the perturbation step resolved them; no physical conclusion was hidden or tolerance relaxed. Independent checks identified the constant-background domain and L2 readout qualifications before canonical packaging. Historical versions remain distinguishable. Full report identities, source adaptation, failed attempts, and review dispositions are in the campaign accelerated_response pack. Focused checks are distinct from formal audit or integrated landing validation.

Every new result is conditional on the displayed observation and field model. Derived response columns, clock/force weights and ideal-coherence cancellations replace corresponding arbitrary measurement choices within that model. They do not derive an initial field, measured energy/error budget, absolute background or scale, actual spacecraft/station solution, scalar action/potential, real media/electronics/turnaround calibration, or a massive accelerated norm. New reference, noise, nonlinear or positive-mass routes remain open. There is no claim of a TOE, a complete literature novelty search, independent empirical confirmation, or framework-authority promotion.

## Review record

Focused independent derivations and source comparisons are preserved in the
campaign accelerated_response pack. They identified the need to state the
anchored background domain, the L2 distributed-readout premise, and the exact
fixture's turnaround normalization explicitly. Those qualifications are in
this note. The final normalization repair changes explanatory text only: the
count is kappa times the phase contrast, with alpha*kappa absorbed into the
displayed fixture. The original reports and source identities remain distinct.

This unit proposes bounded_theorem / conditional-support. Combined validation
on an integrated current-main candidate and independent audit remain landing
conditions; neither is performed or pre-stated by this author proposal. Earlier
campaign PRs remain frozen and are provenance, not missing proof suppliers.
