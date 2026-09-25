---
claim_id: dynamics_clause_the_compression_update_is_the_one_distant_update_consistent_with_locality_of_marginals_and_affine_joint_laws_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional-state uniqueness from positive joint effects and sharp marginals. Conditional finite quantum mathematics under the explicit premises in this note; no native law, framework premise or retained grade is adopted.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_compression_is_the_consistent_distant_update_2026_09_24.py
---
# Conditional-state uniqueness from positive joint effects and sharp marginals

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** conditional-support; unaudited.

## Supplied setting

Take finite ordinary complex quantum systems, positive affine joint record
effects and sharp Born marginal laws. These are explicit premises, not a
collapse or Born derivation from the lock. In particular the general steering
route to joint affinity already supplies ensemble weights and conditional
updates; using it to derive those same updates would be circular.

## Joint effects

For two binary rank-one qubit PVMs, let E_qr>=0 with
sum_r E_qr=P_q tensor I and sum_q E_qr=I tensor P_r.
Then E_qr lies below both projectors. Positivity makes its support lie in
the intersection, the one-dimensional span of |q> tensor |r>.
Thus E_qr=c_qr P_q tensor P_r, c_qr>=0. The marginal equations, with
linearly independent P_r, force every c_qr=1. This is a proof for every
state and both menus, not an inference from sampled intersections.

## Conditional partner and rest

For p_q=Tr((P_q tensor I)rho)>0, consistency of sequential observations
with this joint law requires, for every partner projector P_r,

    Tr(P_r tau_q)=Tr((P_q tensor P_r)rho)/p_q.

An informationally complete partner repertoire uniquely fixes

    tau_q=Tr_i[(P_q tensor I)rho(P_q tensor I)]/p_q.

For a larger rest system the same conclusion requires informationally complete
product measurements and the corresponding joint Born law on that supplied
tensor product. Qubit two-party affinity alone does not furnish that premise.
For p_q=0 the conditional state is undefined and no uniqueness is claimed.
If the recorded site's global post-state is also required to have rank-one
marginal P_q, positivity restricts its support to P_q tensor H_rest,
so the global post-state is P_q tensor tau_q. Without that lock only the rest's
marginal is fixed; no unrestricted uniqueness of the entire instrument follows.

Leaving the partner unchanged instead gives p_q p_r. On a singlet its
absolute difference from the required joint probability is |a dot b|/4,
attaining 1/4 at parallel axes. This refutes that reset under the stated
joint-law premise, not under the lock and no-signalling alone.

## Two supported outcomes

For two nonzero rank-one supported effects e_1 P_1,e_2 P_2, completeness
requires e_1 P_1+e_2 P_2=I. In the basis with first vector spanning P_1,
the off-diagonal entry and the positive complementary diagonal force P_2
to be its orthogonal complement, then e_1=e_2=1. Equivalently the
rank-one matrix I-e_1 P_1 has eigenvalues 1,1-e_1 and must have determinant
zero. More outcomes evade this: three coplanar trine projectors with
weights 2/3 sum to I. No classification of larger menus is asserted.

## Corrected evidence

The primary reconstructs partner/rest states and verifies the marginal
linear system and singlet formula. Its original rest contraction summed
two independent site indices. After rank-one compression a spurious scalar
usually canceled on normalization, hiding the defect in random tests.
The correct partial trace identifies the two site indices. A deterministic
minus-X projector with positive outcome probability exposes the old 0/0
case; the corrected contraction agrees with an independent diagonal-block sum.
Impossible-outcome branches now raise explicitly instead of dividing by zero.
Historical independent-check narratives remain on the frozen original branch;
they are not current execution evidence.

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
Require positive outcome probability for a conditional state. Correct the rest partial trace by identifying site indices. Specify complete partner tomography and joint Born premises. Separate partner uniqueness from global instrument uniqueness. Retain larger supported menus as a counterroute. The primary reports these five scope resolutions.

### N6
Native realization and every wider original claim not proved above remain deferred, recoverable from the original PR head.

### N7
The explicit positive routes and counterexamples above delimit the obstruction. Failure of a sampled route does not exclude untested alternatives.

### N8
This is bounded conditional progress, not a Born/composition/dynamics derivation from the four axioms or a physical completion.

## Sources and execution

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_A_DISTANT_RECORD_IS_A_RECORDED_RANDOMIZER_LOCALITY_OF_MARGINALS_FORCES_PREPARATION_AFFINITY_AND_THE_TRACE_RULE_BOUNDED_THEOREM_NOTE_2026-09-24.md)

[Primary](../scripts/dynamics_clause_compression_is_the_consistent_distant_update_2026_09_24.py) and [fresh output](../logs/runner-cache/dynamics_clause_compression_is_the_consistent_distant_update_2026_09_24.txt).
