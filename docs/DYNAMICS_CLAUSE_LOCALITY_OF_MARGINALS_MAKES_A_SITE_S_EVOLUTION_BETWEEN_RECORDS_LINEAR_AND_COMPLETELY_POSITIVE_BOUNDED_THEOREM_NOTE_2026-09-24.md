---
claim_id: dynamics_clause_locality_of_marginals_makes_a_site_s_evolution_between_records_linear_and_completely_positive_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Affine channels and reversible evolution under explicit extension premises. Conditional finite quantum mathematics under the explicit premises in this note; no native law, framework premise or retained grade is adopted.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_locality_of_marginals_makes_site_evolution_linear_and_completely_positive_2026_09_24.py
---
# Affine channels and reversible evolution under explicit extension premises

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** conditional-support; unaudited.

## Supplied assumptions and affinity

Use finite complex density matrices and ordinary tensor composition. Supply
operational availability of arbitrary finite ensembles with their density-matrix
weights, branchwise application of one deterministic local evolution, and
no-signalling of its nonselected output. The companion steering note states
why Born-weighted preparation is an extra premise. For each ensemble the output
must satisfy Phi(sum p_j rho_j)=sum p_j Phi(rho_j); tomography converts equality
of all output effects to equality of states. Thus Phi extends linearly to
Hermitian matrices, and complex-linearly to all matrices. It is positive and
trace preserving when it maps all density matrices to density matrices.
No-signalling without these ensemble and update premises does not prove this.

## Complete positivity is a separate extension requirement

Explicitly require that the evolution of a decoupled local system alongside
an idle ancillary qubit is Phi tensor id, and that this extension maps every
joint density matrix to a positive matrix. Decoupling alone does not define
that tensor extension. Applying it to a maximally entangled state makes the
Choi matrix C=sum_ij |i><j| tensor Phi(|i><j|) positive (up to a positive
normalization). Write C=sum_alpha |v_alpha><v_alpha| and reshape v_alpha into
matrices K_alpha using the displayed input/output ordering. Entry comparison
gives Phi(A)=sum K_alpha A K_alpha*. Trace preservation gives sum K_alpha*K_alpha=I.
This Kraus form is positive after tensoring any finite identity, proving CP.
A qubit ancilla suffices for a qubit input; for dimension d use an ancillary d.

The transpose is a positive map with a negative partial-transpose eigenvalue
-1/2 on a singlet. A controlled local rotation followed by a Heisenberg bond
exposes a negative product-record probability. That example excludes transpose
in this supplied experiment, not every non-CP map through the same controls.
The general CP conclusion uses the explicit extension-positivity premise.

## A channel with a channel inverse is unitary

Let Phi and Psi be CPTP maps on the same finite matrix algebra, with
Psi Phi=id, and Kraus operators A_i,B_j. The identity channel has rank-one
Choi matrix, so every composite Kraus matrix B_j A_i=c_ji I. At least one
c_ji is nonzero; its A_i and B_j are invertible because they are square.
Fix that j. For every k, B_j A_k=c_jk I, so every A_k is proportional to
the same invertible matrix V. Trace preservation makes
(sum |a_k|^2) V*V=I. Rescaling V gives a unitary U and Phi(rho)=U rho U*.
Conversely unitary conjugation has its unitary inverse. This does not apply
to unequal input/output dimensions or merely invertible linear maps.
Dephasing with off-diagonal multiplier 1/2 is linearly invertible; its inverse
maps |+><+| to a matrix with eigenvalue -1/2, so is not a channel.

A differentiable unitary family has an instantaneous Hermitian generator.
A continuous time-homogeneous one-parameter unitary group on a finite system
has a fixed Hermitian generator. The group/time-homogeneity premise is extra;
unitarity alone gives neither a fixed Hamiltonian nor its spatial support.
A nearest-neighbour two-site generator is supplied in the finite chain checks.
Heisenberg evolution spreads operators beyond one bond at nonzero time;
the displayed commuting Ising case does not. No theorem classifying every
strict-range unitary family or every permitted generator is claimed.

## Evidence scope

The primary tests two selected nonlinear maps, affine channel examples,
transpose and generic inverse witnesses, and finite chain support growth.
The proofs above, not random sampling, establish the conditional statements.
Whole-region channel evolution, native Hamiltonian selection, physical time,
entangled preparation and measurement completeness remain supplied or open.

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
Supply the tensor extension and positivity requirement for CP. Separate the transpose witness from a universal CP proof. Prove the same-dimensional channel inverse theorem using Kraus matrices. Require group time homogeneity for a fixed generator. Keep generator support independent from finite-time operator support. The primary reports these five scope resolutions.

### N6
Native realization and every wider original claim not proved above remain deferred, recoverable from the original PR head.

### N7
The explicit positive routes and counterexamples above delimit the obstruction. Failure of a sampled route does not exclude untested alternatives.

### N8
This is bounded conditional progress, not a Born/composition/dynamics derivation from the four axioms or a physical completion.

## Sources and execution

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md)

[Primary](../scripts/dynamics_clause_locality_of_marginals_makes_site_evolution_linear_and_completely_positive_2026_09_24.py) and [fresh output](../logs/runner-cache/dynamics_clause_locality_of_marginals_makes_site_evolution_linear_and_completely_positive_2026_09_24.txt).
