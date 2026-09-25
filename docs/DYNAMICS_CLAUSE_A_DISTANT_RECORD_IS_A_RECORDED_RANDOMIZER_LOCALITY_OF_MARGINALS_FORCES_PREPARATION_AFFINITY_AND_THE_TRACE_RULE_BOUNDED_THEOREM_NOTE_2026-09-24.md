---
claim_id: dynamics_clause_a_distant_record_is_a_recorded_randomizer_locality_of_marginals_forces_preparation_affinity_and_the_trace_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Steering affinity and support orientation under explicit ensemble premises. Conditional finite quantum mathematics under the explicit premises in this note; no native law, framework premise or retained grade is adopted.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_a_distant_record_is_a_recorded_randomizer_2026_09_24.py
---
# Steering affinity and support orientation under explicit ensemble premises

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** conditional-support; unaudited.

## Supplied setting

Use finite complex density matrices, ordinary tensor composition, purifications,
controlled preparation and projective conditional compression. These structures
are conditional models, not consequences of the Record text. A local record
law depends only on its reduced state and chosen binary menu. Equal-time
no-signalling means averaging over a remote record does not change that law.
For the general affinity argument below, the remote ensemble weights are
explicitly Born weights. Their availability is a premise of that argument.

A controlled Heisenberg bond at Jt=pi implements SWAP up to phase. On |01>,
a partial swap cos(theta)I-i sin(theta)SWAP gives reduced Bloch length
|cos(2 theta)|. With supplied local rotations this prepares purifications
of every qubit density matrix; controlled swaps can move the partner.
Switchable bonds, input preparation, measurement menus and timing are supplied.
This is a controlled protocol, not an autonomous recorded randomizer.

## Conditional affinity

For rho=p|u><u|+(1-p)|v><v|, choose the purification with columns
sqrt(p)u,sqrt(1-p)v. Its coefficient matrix A obeys AA*=rho. Any other
minimal purification has coefficient matrix sqrt(rho)U on its support,
so a suitable orthonormal partner measurement realizes these columns.
The outcome weights p,1-p follow from the Born preparation premise.
No-signalling then requires F(rho)=pF(u)+(1-p)F(v).

For the full affine extension on mixed-state ensembles, explicitly assume
availability of arbitrary finite ensemble refinements with their density-matrix
weights and a sufficiently large purifying ancilla. For rho=sum p_j rho_j,
refine each rho_j into pure states and apply ensemble independence twice.
This proves F(sum p_j rho_j)=sum p_j F(rho_j). Finite-dimensional affinity
and 0<=F<=1 give F(rho)=Tr(E rho), 0<=E<=I. The qubit binary-chord
experiments alone do not certify that general operational refinement premise.

For a covariant binary qubit law with no extra directional input and
antipodal menu normalization, an already affine law has form
f_lambda(r dot q)=(1+lambda r dot q)/2, |lambda|<=1.
The compression support requirement says an outcome cannot occur when its
normalizing Born overlap vanishes. At r=-q this forces lambda=1.
More generally 0<=E<=I, <q_perp|E|q_perp>=0 and
<q|(I-E)|q>=0 imply E|q_perp>=0 and (I-E)|q>=0:
a positive operator with zero quadratic form annihilates that vector.
Thus E=|q><q|. The lock alone does not supply this support requirement.

## Self-consistent weights: the exact limited conclusion

Now assume the affine covariant family above and let both parties use it
for their outcome weights. For the Schmidt state with reduced z-coordinate
0<r<1, a partner z record prepares site states +z,-z with weights
(1+lambda r)/2,(1-lambda r)/2. The averaged site +z law is
(1+lambda^2 r)/2, whereas its direct law is (1+lambda r)/2.
Equality gives lambda(lambda-1)=0. Born (lambda=1) and the constant law
(lambda=0) satisfy the averaging condition throughout this family; the
support requirement excludes the constant law. This argument classifies the
already affine family. Tests of five chosen laws do not prove that every
nonlinear self-weighted law is affine. That wider closure remains deferred;
the preceding general affinity proof does import Born ensemble weights.

## Countermodels and finite diagnostics

A replacement rule setting the recorded site to its selected pure possibility
and leaving the other site's reduced state unchanged obeys the lock and
no-signalling for every normalized binary law depending on that reduced state.
It need not be an affine quantum instrument. Anti-Born and tanh examples
therefore refute a derivation from the lock and no-signalling alone.

The primary retains controlled-swap, chord and sampled nonlinear-law checks.
The finite four-site chain diagnostic distinguishes equal-time marginal
invariance from later dynamical influence. Its sampled cubic short-time growth
is not an exact finite-speed theorem. Frequency convergence is a separate
question: vanishing averaged covariance is the relevant mean-square criterion;
clustering is sufficient, not necessary. No preparation, time law, Born rule
or frequency law is adopted for the framework here.

A random effect's distance/support-violation ratio is not uniformly bounded.
For a rotated rank-one projector the distance is sqrt(2)|sin(theta)| and
the summed support violation is 2 sin(theta)^2; their ratio diverges as
theta tends to zero. Exact zero support, not a sampled ratio bound, supplies
the orientation proof.

## Scope discipline

### N1
The alternatives actually examined are the explicit constructions, maps and counterexamples above. No exhaustive framework route classification is claimed.

### N2
Preparation, probability, composition, dynamics and operational readout have distinct premises; the displayed implications do not establish pairwise independence.

### N3
Finite complex matrices, specified tensor products, available effects and any ensemble/update assumptions are supplied mathematical setting.

### N4
The linked sources supply only their stated conditional algebra and current axiom boundary, never an inherited audit grade.

### N5
Supply ensemble weights in the general affinity argument. Restrict self-weighted classification to the affine covariant family. Separate controlled preparation from an autonomous randomizer. Use exact positive-effect support instead of a sampled ratio bound. Keep frequency and finite-time propagation obligations separate. The primary reports these five scope resolutions.

### N6
Native realization and every wider original claim not proved above remain deferred, recoverable from the original PR head.

### N7
The explicit positive routes and counterexamples above delimit the obstruction. Failure of a sampled route does not exclude untested alternatives.

### N8
This is bounded conditional progress, not a Born/composition/dynamics derivation from the four axioms or a physical completion.

## Sources and execution

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

[Primary](../scripts/dynamics_clause_a_distant_record_is_a_recorded_randomizer_2026_09_24.py) and [fresh output](../logs/runner-cache/dynamics_clause_a_distant_record_is_a_recorded_randomizer_2026_09_24.txt).
