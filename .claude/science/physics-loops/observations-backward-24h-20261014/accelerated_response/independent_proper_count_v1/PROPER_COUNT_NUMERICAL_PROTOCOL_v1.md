# Frozen independent numerical protocol: proper-endpoint count response

This protocol is frozen with PROPER_COUNT_PRECHECK_v1.md before author-source
access. The numerical fixtures below are synthetic conditional models, with no
fit parameters, raw data, empirical clock budget or measured acceleration.

## Independent representations

1. Solve the exact receiver clock integrals and invert them at fixed proper labels
   for each epsilon. Solve the exact retarded null equation, then evaluate the
   emitter clock difference. Use nested scalar bracketing/root solves and adaptive
   quadrature. This is the nonlinear finite-count reference.
2. Independently integrate the linear clock-rate perturbations and use the
   analytic receiver-time/null-time sensitivities and endpoint S expression.
3. Compute the total-event delta K, including delta n and endpoint acceleration
   terms, and integrate it over the fixed receiver proper interval. It must match
   the endpoint expression. Do not implement this as a disguised finite difference
   of S or omit the changing-line-of-sight terms.
4. Where dynamics are tested, integrate the nonlinear perturbed trajectory plus
   both clocks and compare with an independently augmented tangent ODE. Keep
   prescribed-path tests separate from this additional force-model assumption.

Use central finite differences at epsilon=0.01,0.005,0.0025 and, when useful,
0.00125. Check second-order convergence until quadrature/root roundoff dominates;
state the observed error and floor rather than forcing a convergence ratio at
roundoff. Verify all velocity magnitudes stay below one, null residuals and clock
endpoint residuals are small, and retarded emission precedes reception. Exact
parameter choices may be narrowed for numerical conditioning only with the
change and reason preserved; do not silently discard a failing fixture.

## Closed-form clock-only fixtures

For A=A_0 exp(epsilon b t), static paths at separation L and constant proper
emitter frequency nu_e give exactly
N_epsilon=nu_e exp(-epsilon b L)(T_b-T_a). Compare the full nonlinear numerical
count and its derivative to this expression. Choose A_0=1.3, b=0.08, L=1.1,
nu_e=1.7 and receiver coordinate reference endpoints 1.2,4.6 (proper endpoints
are computed from the epsilon=0 clock). An additive clock anchor cancels from
the exact count difference. This fixture detects omission of direct clocks.

Repeat with a constant a=b: count derivative is zero for static paths. Repeat
with A=A_0 exp(epsilon b x_1), emitter at x_1=0 and receiver at x_1=L held fixed:
the same exponential endpoint frequency ratio results. Explicitly label the
external support holding these paths rather than treating them as geodesics.

## Moving and rotating-line-of-sight prescribed paths

Use coordinate anchor t_*=-4, A_0=1.3 and proper frequency nu_e=1.7. Baseline paths:

    x_E(t)=(0.1 sin(0.3t), 0.04t, 0),
    x_R(t)=(2+0.1t+0.05 sin(0.2t),
            0.4+0.08 cos(0.25t), 0.03 sin(0.4t)).

Explicit fixed-coordinate variations:

    xi_E(t)=(0.03 cos(0.4t), 0.02 sin(0.3t), 0.01t),
    xi_R(t)=(-0.02 sin(0.35t), 0.025 cos(0.3t), 0.015 sin(0.2t)).

Set x_A,epsilon=x_A+epsilon xi_A and

    a(t,x)=0.04 sin(0.6t-0.7x_1+0.2x_2)+0.015 cos(0.4t+0.3x_3),
    A_epsilon=1.3 exp(epsilon a),
    tau_E,epsilon(t_*)=0.07 epsilon,
    tau_R,epsilon(t_*)=-0.05 epsilon.

Fix T_a=tau_R,0(1.2), T_b=tau_R,0(4.6). Derive eta and accelerations analytically.
Test the full fixture and separately isolate field-only, path-only and clock-
offset-only perturbations. Compare receiver and emitter time derivatives, total
positions, total event clock readings, line direction, local frequency and count.
Check linear superposition of first variations. Use the full retarded position
x_E(u), not x_E(t), and verify that dropping the receiver clock or either path
motion generally fails these nondegenerate fixtures.

## Initial-state and constant-background discriminators

A nonzero emitter proper-clock offset alone must cancel from the finite count.
A receiver offset alone must produce -nu_e kappa_R(K_b-K_a) for nonconstant K.
The moving fixture above supplies that nonconstant response. A common constant
spatial translation of both paths in a homogeneous conformal background, with
identical clock anchors, must leave the count unchanged; this checks positional
signs. A rotation of the entire geometry/perturbations should leave scalar counts
unchanged when the scalar profile is rotated consistently.

To reject an unjustified general constant-background cancellation, use A_0=1,
stationary emitter x_E=0, receiver x_R=0.5+0.025t^2, t_a=1,t_b=3, coordinate anchor
zero, a=b=0.1, xi=0 and kappa=0. Keep the coordinate paths fixed and receiver
proper labels fixed. Compare exact clock-inversion counts with the nonzero
closed derivative in the precheck. The full paths remain safely subluminal on
the required interval. Record why this family differs from a universal units
rescaling of all physical inputs.

## Conditional augmented dynamics

As a separate supplied model, take constant A_0 and a smooth external coordinate
acceleration F_ext(t,x,v) that leaves the tested interval subluminal. It may be
zero for the first fixture. Add the exact conformal geodesic coordinate term
-(1-|v|^2)(grad ell+v partial_t ell), retaining the reference external force.
Integrate x,v,tau jointly. Compare with the precheck's xi,eta,chi tangent system,
including nonzero initial xi,eta and kappa in at least one fixture. Vary endpoint
proper labels only through implicit inversion. Do not infer this force law from
the radio observation model or silently assume an external proper-unit force
has zero variation. Report this additional dynamical assumption separately.

## Evidence and failure handling

Save source hash, result identities, parameters, integration/root tolerances,
finite-difference errors, true/false controls and all attempted failures. Numerical
quadrature is not interval-certified. The test count is bookkeeping, not a claim
of empirical independent validation. Compare author sources only after these
precheck/protocol bytes and their SHA-256 hashes have been sent to root.
