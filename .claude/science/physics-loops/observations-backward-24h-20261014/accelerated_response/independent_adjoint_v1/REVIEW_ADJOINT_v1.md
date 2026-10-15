# Independent finite-observation adjoint check

Reviewer: `/root/force_energy_bridge_check`. Root remains the author. This is a
focused mathematical and synthetic-control check, not a formal audit. The
derivation and executable controls below were completed before opening any
author accelerated-response draft or implementation. No raw observations,
calibration products, or new empirical values were read.

## Exact conditional response operator

For supplied coefficients on a finite interval [a,b], let

    z' = L(s) z + P(s) f(s),
    y_i = integral q_i(s)^T z(s) ds + sum_r d_ir^T z(t_r)
          + (X beta)_i + e_i.

The distributed readout q_i can encode a known pushed-forward count window,
clock, varying calibration, viewing geometry or a retarded-time change of
variables. That representation must first be justified by the actual supplied
measurement model; an archive timestamp does not establish it. A multitime
readout can be represented by multiple distributed pieces or atoms after a
valid change of variables. A history-dependent delay-differential state law
cannot silently be replaced by this finite-dimensional ordinary differential
equation.

Let Phi(s,t) be the state transition matrix. The propagated initial coefficient
is the column vector

    N_i = integral Phi(s,a)^T q_i(s) ds
          + sum_r Phi(t_r,a)^T d_ir.

Between readout atoms, the backward adjoint satisfies

    -lambda_i' = L^T lambda_i + q_i.

Across an atom,

    lambda_i(t_r^-) = lambda_i(t_r^+) + d_ir.

Use lambda_i(b^+)=0, hence lambda_i(b^-)=d_ib. At the left endpoint retain
N_i=lambda_i(a^+)+d_ia. The exact force weight is w_i=P^T lambda_i, and

    y_i - (X beta)_i - e_i = N_i^T z(a) + integral w_i^T f.

For rows N_i^T stacked as N, a contrast c removes arbitrary unknown z(a) and
beta exactly when

    N^T c=0,  X^T c=0.

The word "exactly" here refers to removing both independent unknown terms for
all their values in this supplied linear model. If only a subspace of the
initial state is unknown, use its response columns; subtract known components.
A rank-deficient nuisance design is permitted; work with its actual span.
Once those conditions hold, c^T(y-e)=integral w_c^T f with w_c=sum_i c_i w_i.
Simple sums of coefficients are not substitutes for propagated state columns.

These formulas follow independently from variation of constants and from
integrating (lambda_i^T z)'=lambda_i^T P f-q_i^T z on each interval. The jump
and two endpoint contributions reproduce the readout atoms, including the
initial atom that would be lost by setting N_i=lambda_i(a^+).

## Endpoint regularity is an additional requirement

The ODE identity holds for ordinary smooth force inputs even when w_c has
jumps. Boundedness on the fixed-spatial-point free-scalar finite-energy space
is a different question. For a compactly supported force weight, the massless
gradient identity is

    G_cd = (1/(6 pi)) integral w_c'(s) dot w_d'(s) ds.

It requires the distributional derivative of the zero-extended weights in L2.
For piecewise H1 weights this means zero outer traces, no internal jumps, and
an L2 interior derivative. Compact support then also gives L1. The same
massless Gram bounds nonnegative massive fields spectrally; it is not in
general their exact Gram. This uses the previously independently checked
stationary free-field Fourier/angular identity, and does not replace a new
moving-spatial-trace calculation.

For continuous P in W1,infinity, bounded L, and q in L2 on each segment,

    w_c' = P'^T lambda_c - P^T L^T lambda_c - P^T q_c,
    w_c(t_r^-)-w_c(t_r^+) = P(t_r)^T d_cr.

The outer conditions are

    P(b)^T d_cb=0,
    P(a)^T lambda_c(a^+)=0.

For an initial-state-free contrast, the second expression is -P(a)^T d_ca.
Thus removing the initial state does not automatically give H1 if an initial
velocity atom remains. With no atoms, full initial-state cancellation and the
zero terminal adjoint do give both zero traces. A jump in P changes the
internal matching condition to

    P_-^T (lambda_+ + d_cr) - P_+^T lambda_+ = 0.

If clocks or calibrations produce singular pushed-forward coefficients, or P
lacks the stated regularity, H1 must be checked directly. In particular, one
must not omit delta contributions at jumps and use only the smooth derivative
in the Gram formula.

## Newtonian trajectory interpretation and exact endpoint controls

For z=(delta x,delta v), a supplied linearized Newtonian trajectory has

    L = [[0,I],[K,D]],  P = [[0],[B]],
    -lambda_x' = K^T lambda_v + q_x,
    -lambda_v' = lambda_x + D^T lambda_v + q_v,
    w = B^T lambda_v.

Here K is the position Jacobian and D the velocity Jacobian of the reference
acceleration. For a Newtonian point source with acceleration -GM x/r^3,
K=GM(3 rhat rhat^T-I)/r^3 and D=0. The reference orbit, force injection B, GM,
coordinate time, count response and linearization validity remain supplied.

A position atom d=(d_x,0) jumps lambda_x but leaves w continuous. A velocity
atom d=(0,d_v) generally jumps w by B^T d_v. Outer position atoms can therefore
be compatible with an H1 force weight after initial-state cancellation; outer
velocity atoms require explicit projected cancellation. This distinction is
about the tested observable functional, not about whether positions or
velocities can ever be measured.

Two free-particle examples isolate the issue without a numerical solver:

* v(b)-v(a) removes initial velocity but generates the rectangular force weight
  1_[a,b]. It is not H1. Its massless cutoff squared norm is
  [Lambda-sin(Lambda T)/T]/(3 pi^2), T=b-a, which diverges.
* x(0)-2x(T)+x(2T) removes initial position and velocity. It generates the
  continuous triangle of height T and slopes +1,-1, with squared norm T/(3 pi).
  The Fourier cutoff tail is bounded by 8/(3 pi^2 Lambda).
* x(b)-x(a)-(b-a)v(a) also removes initial state, but its force weight b-s is
  nonzero at a. It fails the left trace condition because of the initial
  velocity atom.

These examples are restrictions on finite-energy trace bounds, not a rejection
of a scalar theory or of the ordinary finite-dimensional trajectory identity.

## Independent executable evidence

`independent_adjoint_check_v2.py` uses a planar circular Newtonian reference,
radius 1 and angular frequency 0.4, on [0,3.2]. Its tidal matrix rotates with
the reference orbit, so this is a genuinely time-varying dynamical test. Nine
synthetic readouts combine distributed finite-window velocity response with
known varying calibration and direction. Eight contain only position atoms;
one deliberately contains initial, internal and terminal velocity atoms.

The forward variational ODE, state transition ODE and backward piecewise
adjoints are separately integrated. Distributed integrals use 36-point Gaussian
quadrature on every interval cut at all readout edges and atoms. All endpoint
and internal jumps are retained. The first eight rows remove four initial
components and one additive nuisance with a three-dimensional contrast space.

The completed run has **163 controls, all passing**, in 0.139 seconds of script
time (Python 3.12.8, NumPy 2.4.1, SciPy 1.17.0). Relevant discrepancies are:

| Independent comparison | Maximum absolute discrepancy |
|---|---:|
| Initial response, adjoint versus propagated transition | 7.70e-13 |
| Direct readout versus state-plus-adjoint-force response | 8.28e-14 |
| Force variation, direct versus adjoint | 2.05e-14 |
| Initial-state perturbation versus N response | 9.43e-14 |
| Interior force-weight derivative versus finite differences | 1.11e-11 |

The qualifying synthetic contrast Gram has eigenvalues approximately
0.0148764, 0.0207012, 0.0422851. The deliberately unqualified velocity-atom row
has visible projected weight jumps and a nonzero terminal force trace; it is
not included in that H1 Gram.

A separate nonlinear Newtonian integration with +/-epsilon perturbations of
both initial state and applied force checks the variational dynamics. Maximum
central-difference errors at epsilon 0.004, 0.002, 0.001 are 4.1620e-7,
1.0405e-7, 2.6013e-8, giving the expected factor-four convergence. This is a
synthetic local linearization check, not an empirical orbit validation.

The rectangle cutoff norms at Lambda 10,50,200 are 0.326821,1.667206,6.736995.
The triangle cutoff norms are 0.127608,0.135868,0.137426, bounded below the
exact 1.3/(3 pi) and within the stated analytic tail enclosure.

## Preserved control failure and repair

Version 1 completed 161 controls: 159 passed and two nonzero-effect controls
failed because the arbitrary 0.01 threshold exceeded the chosen synthetic
signals. The exact omitted-initial-atom norm is 0.00806226, and the projected
initial-position-atom norm is 0.00539946. Version 1, its output and results
remain unchanged. `CONTROL_REPAIR_v1.json` records the issue.

Version 2 adds equality checks against the exact omitted terms and checks
nonzero magnitude above 1e-6. It does not alter the mathematical formulas,
fixtures, ODEs, adjoints or numerical integration. Both repaired controls and
all original substantive identities pass. No author source was opened before
this repair or freeze.

## Scope and remaining imports

The checked output is an exact adjoint reconstruction **conditional on** a
supplied linearized dynamics and readout map. It does not derive a spacecraft
force residual, an archive clock or calibration, a retarded two-way radio map,
the field action, a scalar coupling, a gravitational scale, an environmental
solution, or the validity of replacing a moving physical worldline by a fixed
spatial field trace. No measured data values were read. The stationary Gram
should remain explicitly separate from the trajectory adjoint identity until
their spatial and dynamical mapping is justified.

All executable controls and this report were frozen before author-source
comparison. Exact identities are in `REVIEW_IDENTITY_v1.json`.
