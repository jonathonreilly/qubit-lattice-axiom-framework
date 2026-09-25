---
claim_id: admissibility_rule_waves_need_signed_weights_a_formation_rule_with_nonnegative_weights_keeps_an_undamped_branch_only_by_rigid_transport_and_the_amplitude_step_is_a_signed_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Finite-memory, finite-component, translation-invariant linear recursions with finitely supported entrywise
  nonnegative weights whose total is row-stochastic have all multipliers in the unit disk. Within each recurrent
  irreducible companion class, a locally unimodular branch on an open momentum set has affine phase fixed by cycle
  displacement divided by cycle length; distinct classes may have different velocities. A signed two-level recurrence
  has unimodular roots iff |aP(k)|<=1, but repeated endpoint roots allow linear growth for arbitrary initial data.
  A separately supplied unitary coin step obeys that recurrence with compatible initial data. No universal no-wave
  theorem for nonlinear rules, infinite memory, probability laws or the continuous-time parent walk.
upstream_dependencies:
- admissibility_rule_a_phase_timed_by_the_local_clock_every_packet_falls_towards_slow_clocks_force_is_energy_times_gradient_weight_and_inertia_tied_by_the_walk_bounded_theorem_note_2026-09-21
- admissibility_rule_directed_gaussian_propagator_overlap_covariance_gain_bounds_bounded_theorem_note_2026-09-15
- admissibility_rule_waves_among_moving_records_need_a_coupling_that_time_reversal_flips_clocked_record_motion_never_oscillates_bounded_theorem_note_2026-09-23
- minimal_axioms
runner: scripts/admissibility_rule_waves_need_signed_weights_nonnegative_rules_keep_an_undamped_branch_only_by_rigid_transport_2026_09_24.py
---

# Linear averaging multipliers, classwise transport and a signed recurrence

**Type:** bounded_theorem
**Status:** bounded-support; supplied finite linear models, unaudited.

This note studies a supplied finite-memory linear averaging recursion and a separately supplied discrete unitary coin step. Nonnegative gain-one branches have the stated spectral bound and classwise transport restriction; signed recurrences require endpoint stability qualifications. Nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Premises and declared objects

Supply theta_(t+1)(x)=sum_(0<=j<J,y) w_j(y) theta_(t-j)(x-y), with J,M finite, M-vector values, finite displacement support, entrywise nonnegative matrices w_j, and sum w_j row-stochastic. These weights are an extra linear-model assumption; the fact that probabilities are nonnegative does not make every formation law a linear averaging rule. The Gaussian parent supplies a one-level scalar example, not this whole classification. Noise is omitted from the homogeneous dispersion problem.

The augmented JM-vector consists of the present value and J-1 past values. Its companion symbol B(k) has top blocks W_j(k)=sum_y w_j(y)exp(-ik.y), and identity subdiagonal blocks. Its eigenvalues are the roots of det[lambda^J I-sum_j W_j(k)lambda^(J-1-j)]. C=B(0) is nonnegative row-stochastic; |B(k)|<=C. Decompose the finite directed support graph into strongly connected classes. A recurrent class means a closed row-stochastic block, not merely irreducibility of sum w_j. Empty or unused memory slots can make the full companion reducible.

Separately supply U(k)=R(theta)diag(exp(-ik),exp(ik)), with R(theta)=[[cos theta,-sin theta],[sin theta,cos theta]]. This is a discrete unitary step, not a derived discretization or exact exponential of the continuous-time generator in the parent walk. The current clocked-motion parent states a finite detailed-balance autocorrelation theorem; it does not say all record motion never oscillates.

## Theorem T1 — spectral bound

The induced maximum-row-sum norm of B(k) is at most1, hence every eigenvalue has |lambda|<=1. More strongly all powers have that norm at most1: this nonnegative gain-one recursion has no growing defective unit-circle modes. The five exact rational-angle fixtures in the runner test an average, a persistent walk, two memory levels and a two-component rule. Their listed nontransport partners are strictly inside the disk at those angles, not necessarily at every isolated angle. The half-step rule has roots +/-exp(-ik/2), allowing temporal period and rational velocity.

The parent's persistent-walk example has polynomial lambda^2-2p cos(k)lambda+2p-1 at p=9/25. Discrete negative or complex damped multipliers are not excluded by the separate continuous-time detailed-balance result.

## Theorem T2 — classwise affine phase on an open set

On any recurrent irreducible companion class, suppose a continuous local eigenvalue branch has |lambda(k)|=1 on a connected open neighborhood. Then its phase is affine there: lambda(k)=zeta exp(-ik.v), with v equal to displacement divided by length of any directed cycle of that class. This is a statement about an undamped branch and its supporting class. It does not assert that the whole rule, all components or all decaying branches move at a single velocity.

Proof of the equality step: for Bx=lambda x, let r=|x|. Then r<=|B|r<=Cr. A strictly positive stationary left vector of the irreducible stochastic C makes the sum of nonnegative slacks zero. Thus Cr=r; irreducibility implies r is strictly positive and constant up to scale. Every edge attains its modulus bound and every triangle inequality is equality. Writing x_i=r_i exp(i alpha_i), each positive displacement contribution on edge i to j has

    exp(-ik.y) exp(i alpha_j)=lambda exp(i alpha_i).

If an edge contains two distinct displacements, their phases must agree throughout the open neighborhood, forcing y=y'. Thus each supported edge carries one displacement. Multiplying the edge relation around a directed cycle of length L and total displacement Y gives lambda^L=exp(-ik.Y). Choose a local continuous root to obtain lambda=zeta exp(-ik.Y/L), zeta^L=1. Every other cycle must give the same velocity because equality of their exponential affine functions on an open set forces equality of slopes. The edge displacements minus v therefore have zero cycle sums and are vertex-potential differences. This is precisely the component phase gauge version of rigid transport for that class. It supplies the analytic step that was only attributed to earlier attempts.

For a reducible finite C, transient irreducible blocks have spectral radius below1: there is leakage along a path to a closed class, so some finite power has maximum row sum strictly below1 on the block. They cannot supply a unimodular eigenvalue. Apply the proof to each recurrent block. Different blocks can transport at different velocities; diag(exp(-ik),exp(ik)) is a nonnegative two-stream counterexample to a single velocity for the full rule. Decaying eigenbranches can be dispersive. The exclusion concerns undamped branches with non-affine phase on open sets, not arbitrary waves, fronts, isolated momenta or nonlinear laws.

## Theorem T3 — signed recurrence and endpoint exception

For real a and P(k)=(1/d)sum_j cos k_j, the scalar recurrence

    theta_(t+1)=2aP theta_t-theta_(t-1)

has polynomial lambda^2-2aP(k)lambda+1. Its two roots are on the unit circle iff |aP(k)|<=1. If the inequality is strict they are distinct and every solution at that fixed momentum is bounded. At aP=+/-1 the companion is defective: solutions (A+Bt)(+/-1)^t generally grow linearly. Thus unimodular roots are not unrestricted losslessness or power boundedness. If |a|<1, the strict inequality is uniform over k and the finite-memory evolution has a uniform bound. At |a|=1, exceptional momenta remain.

At a=1 choose omega=acos P in [0,pi]. On the one-dimensional Brillouin interval [-pi,pi], omega=|k|, including nonpropagating/repeated endpoint cases. For general small k, P=1-|k|^2/(2d)+O(|k|^4), so omega^2=|k|^2/d+O(|k|^4); the leading cone is round, while finite-wavelength corrections need not be. At a=5/4,k=0 one root is2, an exponential instability.

## Theorem T4 — discrete unitary step and restricted initial data

The separately supplied U satisfies U dagger U=I, det U=1, tr U=2 cos(theta)cos(k). Its characteristic identity gives U^2-(tr U)U+I=0, hence each component of psi_t=U^t psi_0 satisfies the signed recurrence with a=cos(theta). Unitarity makes this amplitude evolution bounded at every k. The converse is false for arbitrary two-level data: the unitary history requires psi_1=U psi_0. In particular at repeated roots this condition removes the recurrence's growing solutions. The negative coefficient is an elimination identity for amplitudes, not negative probabilities or a theorem that an amplitude layer is the only possible mechanism.

## No-Go Discipline Gate

### N1 — Alternatives
Nonlinear or time-dependent rules, infinite memory, infinitely many internal components, non-stochastic gains, other state variables and isolated momenta are outside the classification. Multiple recurrent velocities are allowed. A gain condition outside the theorem does not by itself prove every mode grows.
### N2 — Wall independence
No repository no-go wall is used.
### N3 — Inputs
Finite memory, nonnegative constant coefficients, row-stochastic total and translation invariance are explicit extra assumptions.
### N4 — Sources
Parents supply conditional examples only. The graph-cycle proof above replaces the unprovided analytic argument from historical attempts.
### N5 — Resolution
Five rational-angle fixtures and a 3x3 gauge/non-gauge example supplement the general norm and cycle proofs. Signed dispersion and the 2x2 matrix identity are symbolic. Tests alone do not classify every rule.
### N6 — Primitive boundary
No negative probability, new physical primitive or mandatory amplitude realization is adopted.
### N7 — Strongest objection
A unimodular root can be defective. T3 explicitly keeps the linear-growth exception, and T4 uses unitary-compatible initial data.
### N8 — Historical scope
Original propagators, additional stability regions and author referee reports remain recovery material only.

## Falsifiers

A multiplier outside the disk under the exact T1 assumptions, or a non-affine unimodular branch on an open set in a finite recurrent class, refutes the respective statement. Defective signed endpoints are an explicit exception, not a falsifier.

## Imports

The finite nonnegative irreducible matrix theorem supplies a strictly positive stationary left vector; its equality consequence and the graph-cycle argument are proved above. The runner uses the Schur-Cohn root-disk recursion, exact rational arithmetic and the Cayley-Hamilton identity. These are mathematical tools, not physical authority.
- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Current conditional example](ADMISSIBILITY_RULE_DIRECTED_GAUSSIAN_PROPAGATOR_OVERLAP_COVARIANCE_GAIN_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md)
- [Current conditional example](ADMISSIBILITY_RULE_WAVES_AMONG_MOVING_RECORDS_NEED_A_COUPLING_THAT_TIME_REVERSAL_FLIPS_CLOCKED_RECORD_MOTION_NEVER_OSCILLATES_BOUNDED_THEOREM_NOTE_2026-09-23.md)
- [Current conditional example](ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md)

## Review record

PR9176 harvests five author-reported probes attempts. This scope replaces the whole-rule transport inference and unrestricted losslessness claim; no audit verdict is conferred.

## Verification

Run `python3 scripts/admissibility_rule_waves_need_signed_weights_nonnegative_rules_keep_an_undamped_branch_only_by_rigid_transport_2026_09_24.py`. Expected TOTAL: PASS=11 FAIL=0.
