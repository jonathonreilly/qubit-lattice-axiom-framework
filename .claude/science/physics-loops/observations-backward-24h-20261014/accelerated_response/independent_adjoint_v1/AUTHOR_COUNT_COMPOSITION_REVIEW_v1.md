# Post-source check: physical count composition and constant offset

Reviewer `/root/force_energy_bridge_check`; root remains author. This focused
comparison follows the independently frozen adjoint derivation and 163-control
suite. The new checks here are explicitly **post-author-source exposure**.
They are not a formal audit, a new independent derivation of the null geometry,
or a broad rerun of the author's program. No raw observations were accessed.

## Frozen sources

| Source | SHA-256 |
|---|---|
| JOINT_CLOCK_FORCE_WORKING_v3.md | c90af86ca2008d4d31e857bf4f7b6a7fe5b73b7ad0c307f65ac08eb3bff62605 |
| proper_count_adjoint_controls_v2.py | 89521be38bf9859653b7e3bdd8fc8af9d99b805a4672f1ddde82144bf5510d13 |
| proper_count_endpoint_controls_v2.py | 00c0b049351cbc366da89fe78831a9c48677fee08026b455562385c87022b5e6 |
| PROPER_COUNT_ADJOINT_RESULTS_v2.json | 7c5ff21c236a809de240b3e5fdcae084ae6ff4e267979a180c75a3f514e6b2f1 |
| PROPER_COUNT_ENDPOINT_RESULTS_v2.json | 540927a3e285db53e01cfc6f2e66620a095a54afdceedfcf6f4ebdb5f3ebc500 |
| AUTHOR_FREEZE_v1.json | 1fbf8ce5a789e45c5c31de4d487e6d76eb0ff1562b15bf1995ab5b57aad78caf |

Exact source copies and a manifest are saved in this directory. Earlier
independent precheck, failed controls, repaired controls and reports remain
unchanged. The new note includes the requested o_i in L2 premise, resolving
the distributed-readout qualification in the previous scoped report.

## Actual finite-count composition within the supplied model

The author program uses two bodies, each with a seven-component state
(xi,delta u,eta). The 14-dimensional matrix has the proper blocks: xi'=delta u,
external response J_x=-k and J_u=-d, and the proper-clock velocity coefficient
-A_b u/sqrt(1-u^2). The direct field injections are alpha a_h in velocity and
alpha A_b sqrt(1-u^2) h in the clock. No second alpha is inserted when the
adjoint contractions are taken.

The external reference acceleration is the time derivative of the supplied
reference velocity. Its nonlinear test model is explicitly time-dependent
external acceleration plus -k(x-x_ref)-d(u-u_ref), with the scalar force added.
Its first variation therefore gives the displayed matrix. This is a valid
synthetic supplied dynamics, not a derivation of an astronomical force law.

`observations` forms each count as the difference of the two endpoint phase
rows divided by the fixed receiver proper-time span. The emitter and receiver
position/clock rows and their distinct coordinate times match the frozen
independent row derivation. No velocity row is inserted. Shared endpoints are
collected as common atoms, preserving their algebraic signs. Every observation
atom is strictly after START=-4 and before END=7.2, so no initial atom is being
discarded. The backward loop adds the atom at the right edge before integrating
to the previous knot; this matches the minus/plus jump convention.

`forward` separately propagates the initial-state transition; `adjoint` returns
the initial adjoint and all piecewise solutions. `by_body` contracts velocity
adjoints with the already-alpha-weighted force and clock adjoints with the
already-alpha-weighted direct clock forcing. Thus the forward, initial-state,
and joint adjoint response compared by the author are the same operator.

The nonlinear test solves perturbed orbits and proper clocks, then finds the
receiver coordinate event at fixed proper time and the corresponding emitted
null event. This source structure corresponds to the specified finite-count
observable; the other checker owns the full null/clock geometry verification.
The frozen author output reports 22 controls, direct-versus-adjoint discrepancy
1.04e-11, and central nonlinear count errors 6.98e-6, 1.75e-6, 4.36e-7 for
epsilon .004,.002,.001. Those results were read and source-bound here, **not
rerun**. The helper's nine-control output was likewise read, not rerun.

## Initial-state and force-weight regularity correspondence

Full [N,X] contrasts remove arbitrary initial position, velocity and clock
components plus the two declared instrument columns. The program checks the
initial coefficient from both propagated transitions and backward adjoints.
This is stronger than removing a constant velocity alone.

The pure position/clock endpoint rows have zero velocity projections, so they
do not jump lambda_v. Their clock projection may jump lambda_eta, which changes
lambda_v' through the clock-velocity coupling but not lambda_v itself. The
force injection is constant alpha, hence W=alpha lambda_v is continuous.
The post-final-atom segment has zero terminal velocity trace, and full initial-
state contrasts remove the initial trace. Bounded supplied coefficients and
the finite atom set therefore give the required compact H1 W. The direct
clock weight c=alpha ell lambda_eta is piecewise bounded and in L2. Adding the
b0 condition only narrows this already qualifying contrast space.

The initial emitter-clock column is identically zero in every finite count:
a constant source phase cancels under endpoint differencing. The initial
receiver-clock column is -Delta R/Delta tau. These facts explain why fourteen
listed initial components need not give fourteen independent observable
columns. They were checked directly from the count rows without a transition
or adjoint solve.

## Independent closed response for the constant-offset column

Within the supplied model, a spacetime constant scalar perturbation h=k has
no gradient or time-derivative force. Starting with zero initial perturbations,
xi=delta u=0 and

    eta_A(s)=alpha k [tau_A(s)-tau_A(s0)].

Consequently its phase response divided by k is

    chi_0(s)=alpha {tau_e(E(s))-tau_e(s0)
                    -R(s)[tau_r(s)-tau_r(s0)]},

and its finite-count response is

    b0_i=[chi_0(s_{i+1})-chi_0(s_i)]/Delta tau_i.

This closed formula was derived during the post-source check independently of
the author's adjoint integral and constant-forcing ODE. It reuses the supplied
reference clock and retarded geometry, which are separately being checked.
It agrees with all 22 frozen adjoint b0 entries to **5.15e-15**.

The formula supports section 4: b0 is a derived response column under the
supplied observation/dynamics model, and b0^T t=0 removes the otherwise
zero-energy constant contribution. This removes observable sensitivity;
it does not derive a field state, select the constant, or determine A_b,
alpha, the action, environmental boundary conditions or an energy budget.

The exact mathematical statement uses exact nullspace conditions. In finite
precision, a merely small residual b0^T t is not sufficient to bound the
response to an arbitrarily large constant. The author note explicitly limits
the computed nullspaces to a floating experiment and keeps exact contrast
conditions in the theorem; that distinction must remain in any later package.

## Targeted post-source controls actually executed

`postsource_count_composition_check_v1.py` imports the guarded author module
without running either main routine. Bytecode output is disabled to keep all
review writes in the assigned directory. It performs 53 targeted checks, all
passing, and preserves the author input hashes before and after execution.

* Closed constant-clock response versus stored b0: maximum error 5.15e-15.
* Exact initial emitter/receiver clock columns, event-epoch ordering and zero
  endpoint velocity rows.
* Finite differences of the helper's scalar field versus the force injection
  used by the augmented ODE: maximum error 5.60e-12.
* Direct clock source, sign of the proper-clock velocity Jacobian, and absence
  of feedback from an initial clock offset into the supplied orbit/rate law.
* Reference acceleration versus differentiated reference velocity: maximum
  error 2.84e-12.
* Saved singular spectra versus declared floating nullities: ranks 15 and 16,
  leaving seven and six contrasts. The smallest retained post-b0 singular
  value is 5.77e-9 against the stated threshold 4.37e-12. This is an internal
  numerical consistency check, not a certified exact rank calculation.

No new discrepancy was found in this scoped code/source comparison. The
generic adjoint and endpoint controls remain the earlier independently frozen
work; these new controls test their composition in the exposed author example.
Plane waves here test local response and have infinite global energy, so these
programs alone cannot verify a finite-energy empirical bound. No raw data,
astronomical orbit, calibration, positive-mass generalization, nonlinear
uniform remainder or complete joint Gram was independently validated here.
