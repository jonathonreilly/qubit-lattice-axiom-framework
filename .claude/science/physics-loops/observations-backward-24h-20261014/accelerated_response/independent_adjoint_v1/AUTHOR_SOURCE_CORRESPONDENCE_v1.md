# Scoped correspondence: augmented clock/trajectory adjoint

Reviewer `/root/force_energy_bridge_check`; root remains author. This is a
source correspondence after the independent derivation/control freeze, not a
formal audit. No author numerical count implementation was opened or executed.
No raw observations were read. The joint field Gram in section 3 is assigned
to another focused checker and is not independently certified here.

## Exact compared sources

* `JOINT_CLOCK_FORCE_WORKING_v2.md`, SHA-256
  `7ac81b681804460dfb277b4e2fa369b69ed138b68f833d103a9e547f81de7f7c`.
* Historical precursor `ACCELERATED_RESPONSE_WORKING_v1.md`, SHA-256
  `80d40337d01210ff51847fd56b32fb4b6332e286ac1461a1c10f9e16d0e3ed04`.

Exact copies are preserved in this review directory. Independent precheck,
controls and full report remain unchanged under the earlier identity manifest
`d293b3adb505105ecdb36014b97bdf3322796887c2b914fa1e560a3624ea12cf`.

## Augmented state and readout rows

For each body, the new note uses z=(xi,delta u,eta), with eta the proper-time
perturbation at fixed coordinate time. For the supplied constant conformal
background A_b and reference velocity u,

    ell=A_b sqrt(1-|u|^2),
    delta ell=ell alpha h-A_b gamma u dot delta u.

This gives exactly the proper-clock row in equation (3). In block form the
single-body supplied matrix and field injections are

    L = [[0,I,0], [J_x,J_u,0], [0,-A_b gamma u^T,0]],
    P_force = [0; alpha I; 0],
    P_clock = [0; 0; alpha ell].

Thus the backward adjoint gives W=alpha lambda_v and
c=alpha ell lambda_eta, with no extra factor of alpha in the separately
defined a_h. The clock-velocity coupling is retained: between readout atoms,

    -lambda_v' = lambda_x + J_u^T lambda_v
                  - A_b gamma u lambda_eta + o_v.

Consequently a jump in lambda_eta changes the derivative of lambda_v, but
does not itself make lambda_v jump. This is the relevant difference between
clock endpoint rows and velocity endpoint rows.

At one receiver proper-time endpoint with count sign sigma=+1 or -1 and count
normalization Delta tau, equation (1) supplies the state rows

    emitter at E(s):
      q_x = sigma ell_e n/(D_e Delta tau),
      q_v = 0,
      q_eta = sigma/Delta tau;
    receiver at s:
      q_x = -sigma ell_e n/(D_e Delta tau),
      q_v = 0,
      q_eta = -sigma R/Delta tau.

The distinct emitter/receiver times must remain distinct atoms. The note does
so. These rows follow from the stated phase variation and touch only position
and proper-clock components. They do not contain a hidden velocity impulse.
The coefficients depend on the supplied reference and retarded map; deriving
these rows is not an empirical calibration or a derivation of that reference.

## Initial state, jumps and regularity

The convention s0 strictly before every emitter and receiver endpoint means
there is no initial readout atom, so N_i=lambda_i(s0) is correct. The stated
fallback if an atom is exactly at s0, N_i=lambda_i(s0+)+q_i0, matches the
independent endpoint derivation. The terminal convention lambda(T+)=0 followed
by all specified backward jumps correctly retains a terminal observation atom.

Full initial-state elimination requires sum_i t_i lambda_i(s0)=0, including
positions, velocities and proper-clock offsets for every body; X^T t=0 is an
additional nuisance condition. The rank qualification is appropriate: enough
formal observations do not by themselves establish a nonzero useful contrast.

For the stated finite endpoint-only observations and bounded L on the compact
interval, the adjoint is piecewise absolutely continuous with bounded pieces.
Position/clock atoms have zero velocity components, hence lambda_v and W are
continuous. The terminal velocity trace is zero. After full initial-state
cancellation, the initial velocity trace is zero as well. The zero extension
of W is therefore H1. The clock coefficient c is bounded piecewise, so L2 is
enough for its separate direct field readout. No H1 condition on c is implied
or needed by this adjoint calculation.

**Narrow missing premise for the general distributed-readout extension:** the
current wording permits arbitrary distributed o_i but does not state its
regularity. Bounded L and finite separated atoms alone do not ensure H1 W for
arbitrary o_i. A sufficient clean repair is to require o_i in L2 on the compact
interval, or to restrict the automatic H1 conclusion to the actual finite
endpoint-count rows. For example, in a scalar velocity channel with L=0, an
integrable distributed density o(s)=|s-s_star|^(-3/4) near an interior point gives a
continuous adjoint whose derivative is not L2. Finite readout integrability
alone does not cure that failure. This omission does not affect the endpoint-
only count model actually specified by equations (1)-(2).

Velocity endpoint readouts would jump W by alpha times the velocity coefficient
and require projected cancellation or a different trace argument. The new note
correctly calls this out instead of applying the position/clock result to them.

## Historical precursor distinctions

The older note's variation-of-constants formula for distributed readouts and
its explicit addition from state atoms agree with the independent derivation.
Its endpoint atom term includes the propagated initial response and the
indicator-weighted force response. Its notation lambda(T)=0 is less explicit
than the new T+ convention when an atom lies at the final endpoint, but the
stated jumps and variation-of-constants formula retain that contribution.

The precursor is force-only and uses generic P. Continuous bounded P by itself
does not imply H1 P^T lambda, but the older text does not assert that implication;
it explicitly requires a separate regularity check including endpoints. In
the new augmented model, the force injection into velocity is constant alpha,
which removes that generic P-regularity issue for W. The new proper-clock
injection ell(s) belongs to c and its L2 condition.

The precursor has no explicit proper-clock field channel. It must not be read
as already verifying the new joint count functional, its clock-force Gram or
its background-domain requirement. Likewise, the independent 163-control
synthetic trajectory suite validates the general adjoint mechanism and endpoint
logic; it is not a run of the author's forthcoming actual-count code.

## Scope of this correspondence

The augmented state, equation (4), alpha placement, endpoint state rows,
initial-state contrast, and finite endpoint-count H1 reasoning correspond to
the frozen independent derivation. The distributed-readout regularity premise
above is the only discrepancy found in this scoped comparison. No numerical
actual-count direct/adjoint implementation has yet been checked, and no claim
about real Cassini observations, physical calibration, massive propagation or
new field Gram verification is made here.
