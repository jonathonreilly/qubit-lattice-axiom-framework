---
claim_id: vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_bounded_theorem_note_2026-10-21
claim_type: open_gate
claim_scope: "Open universal Ward/Jacobi classification target with finite sampled numerical support at N=3,4 and selected four-point examples; complex derivations, their real star-preserving restriction and stabilizers refer to explicitly supplied algebraic actions, not physical charges or dynamics."
upstream_dependencies:
  - minimal_axioms
  - candidate_laws
runner: scripts/vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_2026_10_21.py
---

# Sampled vector-response Ward checks and supplied internal actions

Claim type: open_gate. The historical theorem filename and claim identifier are retained for recovery; they do not assert theorem status.
Primary runner: `scripts/vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_2026_10_21.py`.

The [candidate-law register](CANDIDATE_LAWS.md) has zero premise weight. A relay transporting its scalar value unchanged motivates a conserved current. A free Maxwell response is separately supplied: current conservation alone does not select vector dynamics. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) choose neither that response nor the internal label dimension N.

## Finite cubic evidence

In supplied 3+1 Minkowski space with metric diag(1,-1,-1,-1), take the six parity-even metric/momentum tensor structures implemented by `vertex_general`, with free label tensors. This is a chosen one-derivative ansatz, not a demonstrated classification of every covariant vertex: epsilon structures, parity assumptions and equivalence under total derivatives require separate treatment. The runner samples Bose constraints at three off-shell momentum pairs and free gauge constraints at eight pairs (transverse null or pure-gauge legs). For N=3,4 the floating-point kernel dimensions are 1,4; at one further momentum pair, their evaluated spans match the antisymmetric Yang-Mills spans. This supports the candidate within these sampled constraints, without proving all-momenta equivalence or excluding symmetric couplings universally.

## Finite four-point evidence and open obligations

For the supplied Yang-Mills vertex, Feynman-gauge propagator and three momentum-independent parity-even contact structures, use K=12 sampled kinematic configurations per example. Fit three coefficients independently for every external label quadruple. For su(2), su(2)+u(1) and su(3), the maximum residual divided by the maximum exchange norm across quadruples is approximately 6.9e-15, 8.0e-16 and 2.2e-16. This is a sampled fit; Bose consistency of a single contact interaction is not imposed.

For the seeded random antisymmetric N=5 tensor, 120 of 625 quadruples exceed the Jacobi threshold. Their minimum normalized contact-fit residual is approximately 6.6e-3; the maximum elsewhere is 5.4e-15. The correlation with Jacobi magnitude rounds to 1.000. These are finite numerical observations, not a universal impossibility theorem. The all-N/all-momenta Ward-to-Jacobi implication, the converse, and a Bose-consistent local contact construction remain open proof obligations in this packet.

For N=4, every antisymmetric three-tensor is eps_abcd v_d. An orthogonal basis change puts nonzero v on one axis, giving su(2)+u(1) after rescaling the three noncentral generators; v=0 instead gives the abelian R^4 (compact algebra u(1)^4). Both satisfy Jacobi. The runner includes the zero-bracket control.

Conditional algebraic fact: once a real finite-dimensional Lie bracket with positive invariant metric is established, it is compact reductive. Indeed ad_x is skew, the orthogonal complement of the derived algebra is the center, and the center-free complement has Killing form tr(ad_x^2)=-||ad_x||^2<0. This does not establish the missing Ward implication. The dimension inventory gives 8 compact reductive types in dimension 12, 4 in dimension 8 and 2 in dimension 3; it selects no physical algebra.

## Derivations and explicitly supplied actions

Der_C(M_2(C)) is sl_2(C), complex dimension 3 and real dimension 6. Inner derivations ad_H have scalar kernel; the matrix-unit Leibniz system has complex kernel dimension 3. The real star-preserving restriction is su(2), represented by traceless anti-Hermitian generators. The runner separately imposes star preservation as real-linear constraints and obtains real dimension 3, and checks the Pauli generator brackets and Killing eigenvalues (-2,-2,-2). The exact integer negative control H=diag(1,-1) satisfies Leibniz but D(E21)=-2E21 differs from D(E12)*=2E21. Thus the unrestricted complex derivation kernel must not be identified with su(2).

Under the supplied SU(2) conjugation action, a rank-one projector has stabilizer U(1); under U(2) it has U(1)^2. For eight labelled rank-one projectors preserved individually under a supplied U(8) action, the stabilizer is U(1)^8, since commuting with every projector forces a unitary to be diagonal. The computed complex commutant has complex dimension 8. The common scalar phase acts trivially by conjugation on M_8(C), so the effective conjugation action quotients that phase. None of these statements supplies physical charge assignments, a gauge group, a tensor-product block or tick evolution. Independent abelian Maxwell fields are a possible supplied model, not a consequence about necessary internal dynamics.

## Reproduction and limits

The runner uses NumPy default_rng(7), in its original sequential call order. Cubic Gram eigenvalues below 1e-9 times the largest define the numerical kernel; evaluated span rank uses tolerance 1e-8. Four-point checks use Jacobi tolerance 1e-12 for Lie examples, 1e-8 for the random sample, normalized residual tolerance 1e-10 and violating-sample lower threshold 1e-3. Algebraic rank checks use 1e-10. These original predicates and tolerances are unchanged. New exact controls use integer equality. No empirical calibration occurs.

Run `python3 scripts/vector_response_to_labelled_relay_values_forces_lie_algebra_self_coupling_2026_10_21.py` (aggregate cap 300 seconds). Supplied conditions remain the continuum vector ansatz, kinetic metric, label dimension, propagator, chosen contact structures and internal actions. No gauge group, coupling, matter assignment, lattice link dynamics, physical identification or general classification theorem is established. Original assertions and the original run remain recoverable at Git head 9b8c2d6fc98297c88c3eb49f4bdb198d3a716509; this repair narrows those assertions while preserving the numerical experiment and its counterexample.
