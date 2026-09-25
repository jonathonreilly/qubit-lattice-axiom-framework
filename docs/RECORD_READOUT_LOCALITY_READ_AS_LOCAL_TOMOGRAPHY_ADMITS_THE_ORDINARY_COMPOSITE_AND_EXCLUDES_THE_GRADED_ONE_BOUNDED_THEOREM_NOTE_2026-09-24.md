---
claim_id: record_readout_locality_read_as_local_tomography_admits_the_ordinary_composite_and_excludes_the_graded_one_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Finite tomography, generated composition and a parity-superselected comparator. Conditional finite quantum mathematics under the explicit premises in this note; no native law, framework premise or retained grade is adopted.
upstream_dependencies:
- minimal_axioms
runner: scripts/record_readout_locality_as_local_tomography_selects_ordinary_composite_2026_09_24.py
---
# Finite tomography, generated composition and a parity-superselected comparator

**Date:** 2026-09-25
**Type:** bounded_theorem
**Status:** conditional-support; unaudited.

## Supplied readings

Consider local tomography as a proposed requirement that a joint state is
fixed by all available local-effect product statistics. It is not adopted
as an interpretation entailed by Record readout locality. Distinguish this
operational premise from an algebraic one: faithful commuting unital M_2(C)
copies generate the whole finite complex C*-algebra, with positive normalized
states on that algebra. The latter fixes the ordinary abstract matrix algebra;
with an available informationally complete local repertoire it already gives
tomography. These are not counted as two independent necessary costs.

## Exact ordinary reconstruction

For four tetrahedral unit Bloch vectors n_j, let P_j=(I+n_j dot sigma)/2.
Their Hilbert-Schmidt Gram matrix is

    G_jk=Tr(P_j P_k),  G=(2/3)I_4+(1/3)11^T.

It has eigenvalues 2,2/3,2/3,2/3 and determinant 16/27, hence the P_j form
a real basis of qubit Hermitian matrices. Products P_j tensor P_k have Gram
matrix G tensor G, also invertible, so all sixteen measured numbers uniquely
reconstruct every two-qubit Hermitian matrix. They are frequencies gathered
across different binary menus, not sixteen outcomes of one normalized menu:
sum P_j=2I and sum P_j tensor P_k=4I. The Pauli product basis gives the same
result, with 15 normalized-state coordinates for two sites and 63 for three.

For finite faithful commuting local copies the product map from M_(2^n)(C)
into their generated algebra is a unital *-homomorphism. Simplicity makes it
injective and generatedness makes it surjective. This reproduces the linked
category-relative theorem. Extra direct-sum sectors or spectator factors
remain possible if generatedness is dropped. Operational availability of
all required effects is a separate premise, not supplied by that abstract map.

## Exact parity-superselected counterexample

For one fermionic mode per site with parity superselection, each local readable
algebra is span{I,n_i}. The even local observable algebras commute. Odd CAR
field operators anticommute across sites; they are not the readable local
algebras in this comparison. Local readable products span
{I,n_1,n_2,n_1 n_2}, giving only three normalized coordinates, while two
2-by-2 parity blocks have seven. The odd-sector states
(|01>+|10>)/sqrt(2) and (|01>-|10>)/sqrt(2) agree on every such local product
but have trace distance 1. Global X tensor X separates them and is even,
but its two individual X factors are not allowed local even observables.
This specific superselected model fails that local tomography requirement.
It does not exclude every graded theory: larger even logical encodings,
different apparatus roles or repertoires change the question. The linked
two-mode repair is one such explicitly conditional route.

## Product positivity does not fix the quantum state cone

W=(I+X tensor X+Y tensor Y+Z tensor Z)/4=SWAP/2 has trace one and marginals I/2.
For arbitrary vectors a,b, <a,b|W|a,b>=|<a|b>|^2/2>=0. By positive spectral
decomposition this holds for every product of positive local effects.
But the singlet has expectation -1/2. Thus product coordinates and product
positivity do not imply positivity on the full matrix algebra. Requiring
positive states on that generated algebra excludes W. This is a counterexample
to that inference, not a complete alternative framework model or an empirical
state. No physical fermions, species identification, composition law or
retained science status is derived here.

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
Prove tetrahedral reconstruction with an exact invertible Gram matrix. Distinguish cross-menu frequencies from one normalized outcome menu. Keep even observable commutation separate from odd CAR relations. Restrict the graded counterexample to one parity-superselected mode per site. Separate product positivity from positivity on the generated algebra. The primary reports these five scope resolutions.

### N6
Native realization and every wider original claim not proved above remain deferred, recoverable from the original PR head.

### N7
The explicit positive routes and counterexamples above delimit the obstruction. Failure of a sampled route does not exclude untested alternatives.

### N8
This is bounded conditional progress, not a Born/composition/dynamics derivation from the four axioms or a physical completion.

## Sources and execution

- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13](GENERATED_FINITE_COMPOSITION_MINIMALITY_THEOREM_2026-07-13.md)
- [TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03](TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md)
- [MATTER_RECORD_GRADING_SAME_CARRIER_COMPATIBILITY_TWO_MODE_EVEN_REPAIR_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01](MATTER_RECORD_GRADING_SAME_CARRIER_COMPATIBILITY_TWO_MODE_EVEN_REPAIR_AXIOM_DECISION_BOUNDED_THEOREM_NOTE_2026-09-01.md)

[Primary](../scripts/record_readout_locality_as_local_tomography_selects_ordinary_composite_2026_09_24.py) and [fresh output](../logs/runner-cache/record_readout_locality_as_local_tomography_selects_ordinary_composite_2026_09_24.txt).
