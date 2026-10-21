---
claim_id: vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_bounded_theorem_note_2026-10-21
claim_type: bounded_theorem
claim_scope: "For N supplied local, covariant vector fields with a positive kinetic metric and at most one derivative in the cubic vertex, consistency with the free gauge symmetry leaves exactly the Yang-Mills cubic vertex with totally antisymmetric structure constants, and the tree-level four-point Ward identity then requires the Jacobi identity; which compact reductive algebra occurs, any gauge group, coupling, matter assignment or physical identification is not established."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_2026_10_21.py
---

# A vector response to labelled relay values forces a Lie-algebra self-coupling

Claim type: bounded_theorem.
Primary runner: `scripts/vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. With a relay carrying its value unchanged and stepping one block per tick, a single scalar value current is conserved, and a vector response to it is the Maxwell field. This note asks what a supplied vector response allows when the value carries one of N labels. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither the response nor N.

## The cubic vertex

Take the most general cubic vertex of N vector fields that is covariant, Bose symmetric and linear in momenta: six tensor structures, each with a free label tensor. Require that contracting one leg with its momentum gives zero whenever the other two legs solve the free equation, as transverse null waves or as pure gauge. For N = 3 the solution space has dimension 1, and for N = 4 it has dimension 4. Both equal C(N,3), and in both cases the space is exactly the span of the Yang-Mills vertex with totally antisymmetric f. Symmetric couplings are excluded.

## The four-point Ward identity

Fix that vertex, use a Feynman-gauge propagator, and allow the most general momentum-independent contact term. Replace one leg by its momentum and require the tree amplitude to vanish. For su(2), su(2)+u(1) and su(3) a contact term achieves this, with largest relative residual 6.9e-15, 8.0e-16 and 2.2e-16. For a random totally antisymmetric f on N = 5, no contact term achieves it on the 120 of 625 label quadruples where the Jacobi tensor is nonzero; the smallest relative residual there is 6.6e-3, the largest elsewhere is 5.4e-15, and the residual tracks the size of the Jacobi violation with correlation 1.000. On N = 4 this control cannot fail, because every totally antisymmetric f there is eps_abcd v_d, which is su(2)+u(1). The self-coupling must therefore be the structure constants of a Lie algebra, and the positive kinetic metric makes it compact reductive.

The algebra is not fixed. There are 8 compact reductive algebras of dimension 12, su(3)+su(2)+u(1) among them, 4 of dimension 8 and 2 of dimension 3.

## What the site domain supplies

The derivations of the site possibility domain M_2(C) form a three-dimensional algebra. It is su(2), with Killing eigenvalues -2, -2, -2. A locked record projector keeps a u(1). A block value recorded in a locked basis of 8 labels is preserved only by the abelian u(1)^8, of dimension 8. In this supplied setting the record layer gives a torus of charges, and a non-abelian response needs the odds to carry a degenerate multiplet that the tick rotates. If the links never act on the internal value, N decoupled abelian fields are consistent.

## Scope

Supplied: the vector-response ansatz (local, covariant, at most one derivative, positive kinetic metric), the label dimension N, whether links act on internal values, and the tree-level Feynman-gauge test. No gauge group, coupling, matter assignment, lattice link dynamics or physical identification is established.
