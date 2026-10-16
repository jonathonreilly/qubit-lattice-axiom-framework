# Focused independent one-way proper-count review

Reviewer `/root/localized_history_check`; direct scientific authorship remains
with `/root`. This checks the supplied one-way conformal reference model. It is
not a formal audit, combined landing verdict, spacecraft calibration or empirical
validation. No scientific source, campaign state, lock, branch or index was edited.

## Independent work and exact scope

Before opening any accelerated_response author source, I derived the finite
proper-endpoint response and froze PROPER_COUNT_PRECHECK_v1.md and
PROPER_COUNT_NUMERICAL_PROTOCOL_v1.md. I then implemented and executed the frozen
protocol: 179 independent synthetic controls passed. Only afterward did I read
the complete 127-line JOINT_CLOCK_FORCE_WORKING_v3.md, all 144 lines of
proper_count_endpoint_controls_v2.py, all 255 lines of
proper_count_adjoint_controls_v2.py, AUTHOR_FREEZE_v1.json and both full proper-
count result files. Their exact hashes match the supplied freeze. I did not run
or import the author scripts. The author results remain 9 endpoint controls and
22 augmented-adjoint controls, not independent executions by this reviewer.

The precheck used general smooth scalar conformal perturbations. Some independent
profiles are not free massless KG solutions; they test the kinematic count mapping
and supplied conformal force/clock equations, not a field equation or energy Gram.
The author uses massless plane waves and explicitly does not claim their global
energy is finite. The joint clock/force energy Gram and its sufficient norm bound
in sections 3 and 5 were read for context but are a separate focused review scope.
No claim that these 179 controls independently establish that Gram is made.

## Checked response and correspondence

In c=1 coordinates set f_A=A_b sqrt(1-|v_A|^2), with proper clocks tau_A.
The retarded emission time u(t) obeys t-u=|x_R(t)-x_E(u)|. For n pointing from
emitter to receiver, D_A=1-n.v_A and K=f_E D_R/(f_R D_E). Let xi_A be the
fixed-coordinate path perturbation, eta_v,A=xi_A', and chi_A the fixed-coordinate
proper-clock perturbation. At fixed receiver proper labels,

    delta t=-chi_R/f_R,
    delta u=[D_R delta t-n.(xi_R-xi_E)]/D_E,
    delta N=nu_e Delta[chi_E-K chi_R-(f_E/D_E)n.(xi_R-xi_E)].

The author's eta_A denotes this review's chi_A, and its R denotes K. Equations
(1)-(2) therefore agree in every sign and factor. Its normalized count is
(delta N/nu_e)/Delta tau_R, whereas the independent program retains nu_e for
absolute cycle counts. The proper-time denominator is fixed. Retarded emitter
positions must be evaluated at u, not at receiver time t. The null rays are
unchanged as unparameterized paths in the supplied conformal metric; an extra
scalar propagation integral is not present in this model.

The reference proper-clock derivative is

    chi_A'=f_A[alpha h-gamma_A^2 v_A.eta_v,A],

for constant A_b. This is precisely the direct clock term plus velocity-dependent
lapse row in the author's augmented system. The additional gradient-of-background
term in my precheck applies only if log A_b is allowed to vary, which this author
note explicitly freezes. No discrepancy follows from its absence here.

A supplied conformal geodesic force has coordinate acceleration
-(1-|v|^2)(grad log A+v partial_t log A). Its first variation at constant A_b
matches the author's a_h. It is partial_t at fixed position, not a convective
field derivative. The linear external coefficients J_x,J_u and any external
force response remain supplied dynamics. Knowledge of a path alone cannot
justify setting an unknown scalar-dependent external force to zero. The note
states this limitation, and the nonlinear synthetic source in the author code
implements exactly its declared coordinate-force prescription.

## Independent numerical evidence

The independent full path fixture combines rotating line of sight, smooth
coordinate trajectory perturbations, direct metric lapse perturbations and both
initial clock offsets. Its derivative is 0.10828058002000411; the final central-
difference error at epsilon=0.00125 is 1.96e-10. Successive coarser errors decrease
by approximately four as the step halves. A separate calculation differentiates
K at fixed proper time, including delta n and acceleration times endpoint shifts,
and integrates delta K over the receiver proper interval. It agrees with the
finite endpoint formula without deriving its integrand by differencing that formula.

Controls individually compare receiver and emission times, total event positions,
line direction, both total clocks and instantaneous frequency. They isolate field,
path and clock effects, verify their first-order sum, test common translation and
consistent rotation, and reject omission of the receiver clock term. The field-
only derivative is 0.08351084665065325 and the path-only derivative is
0.025146837028722648. The remaining clock-only derivative is
-0.0003771036593718191. The emitter offset alone cancels. The receiver offset
matches -nu_e kappa_R(K_b-K_a) and is nonzero in the changing-Doppler fixture.

Static time-dependent and static spatial-gradient conformal profiles have the
exact count N_epsilon=nu_e exp(-epsilon b L) Delta tau_R for the supplied held
paths. Their independent derivatives are -0.6612319999999997; final finite-
difference errors are at most 1.34e-9. A constant conformal perturbation on static
paths gives zero count derivative. These discriminate clocks from a path-only
force account and do not identify an actual radio instrument.

The distinct conditional dynamics fixture integrates nonlinear trajectories and
proper clocks jointly under the conformal geodesic term plus an explicitly
supplied damped coordinate acceleration. It separately integrates the augmented
tangent system, retaining nonzero initial position, velocity and clock variations.
Its count derivative is 0.6663152445067285, with final nonlinear finite-difference
error 9.99e-9 and second-order convergence. State/clock samples and implicit
receiver/emitter event sensitivities also agree. No interval certification or
uniform nonlinear remainder estimate is claimed from these floating computations.

## Initial-state and constant-background qualification

Additive emitter phase/clock offsets cancel from a finite count for the supplied
constant proper source frequency. Receiver clock offsets generally do not cancel,
because fixed proper labels select displaced coordinate epochs. Initial orbital
perturbations survive unless modeled or projected out. The author appropriately
uses the full augmented initial-state row rather than only constant velocity.

My independent counterexample keeps an accelerating receiver coordinate path
fixed while applying a constant conformal perturbation. Its nonzero count
derivative is 0.03082392888537673 (final finite-difference error 6.67e-11).
Thus universal cancellation cannot be assumed for this family. The author instead
derives b0_i=sum_A integral c_i,A from its actual adjoint and requires b0^T t=0
alongside the initial-state and instrument columns. For a constant h=k, a_h=0
and the joint field response is exactly k b0_i. This is the correct first-order
response column for the supplied model and resolves the caveat by an observable
contrast, without selecting a background value.

The author's example has seven floating nullspace directions before b0 and six
after it. Its stored old-contrast response is 3.241919514954966e-8; this does not
vanish just because it is small. The working note says approximately 3.4e-8;
the exact result should be used in any quantitative packaging. This rounding
summary does not affect a theorem or control. The rank tolerance and lack of an
exact-rank certificate are disclosed. Removing the column can consume a channel,
and no nonzero channel is promised for actual data. It does not determine A_b,
alpha, a physical field background or an energy budget.

## Augmented-adjoint source correspondence

The author endpoint rows place +f_E n/D_E and +1 on emitter position/clock, and
-f_E n/D_E and -K on receiver position/clock, at their respective distinct null
events. Adjacent count endpoints have opposite signs divided by their actual
proper-clock span. These match the checked kinematics. No direct velocity row
is introduced. The backward rule lambda'=-L^T lambda, with positive row jumps
when crossing an observation backward, gives the stated initial-state row and
integrated source by differentiating lambda^T z.

The code independently propagates a forward fundamental matrix and integrates
the adjoint piecewise across all retarded/receiver atoms. It evaluates force and
direct-clock contributions separately before combining them. The stored mismatch
between forward counts and initial-plus-source response is 1.04e-11; omitting the
direct clock gives an error 0.34882265344135777. Its nonlinear clock/null/orbit
comparison has final error 4.36e-7 and ratios about four. I checked the source
and recorded result correspondence rather than rerunning these author controls.
My 179 controls do not include an independently implemented adjoint solver.

Because the atoms touch only position and clock, the force adjoint component
lambda_v has no observation jump. Under the note's bounded linear coefficients
and L2 distributed sources it is continuous piecewise H1. Terminal zero and the
full initial-state contrast give zero outer traces, so extension by zero is H1.
The direct clock weight can jump and stays L2. Velocity-readout atoms or an
initial-epoch atom would need the separate boundary treatment already stated in
the note. This regularity is conditional on the specified observation rows and
is not a property of every possible radio readout.

## Preserved reviewer failure and limits

The first independent run reached final serialization but failed because the
reviewer geometry dataclass named Path shadowed pathlib.Path. Its source and
stderr remain intact. Immutable v2 aliases the filesystem class as FilePath and
uses a new result filename; no formula, fixture, threshold or numerical parameter
changed. The successful rerun produced the 179-control record. The exact repair
diff is preserved in INDEPENDENT_PROPER_COUNT_FAILURE_REPAIR_v1.json. This was a
reviewer implementation failure, not a scientific discrepancy or author failure.

No additional discrepancy was found in the one-way endpoint/augmented-clock
scope. Actual transmitter/receiver calibration, oscillator response, clock
synchronization, coherent turnaround or delay, media, tensor/source corrections,
external-force identification, field dynamics and physical error/resource budgets
remain outside this calculation. No raw observations were accessed. No PR,
formal audit verdict or broader theory exclusion is produced by this report.

Exact source and evidence identities are bound by PROPER_COUNT_REVIEW_IDENTITY_v1.json.
The precheck and numerical protocol remain unchanged; their complete formulas
and fixtures are available alongside this report.
