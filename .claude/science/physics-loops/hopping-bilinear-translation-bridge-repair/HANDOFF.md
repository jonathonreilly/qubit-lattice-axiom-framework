# Handoff

This branch repairs `hopping_bilinear_hermiticity_theorem_note_2026-05-02`
after its audit found a missing tensor-product translation bridge.

Changes:

- Source note now cites the retained
  `tensor_product_translation_fermion_operator_bridge_narrow_theorem_note_2026-05-25`
  as the sole load-bearing authority.
- Runner now checks that bridge's `effective_status` is retained-grade
  before checking Hermiticity, translation covariance, number conservation,
  real spectrum, and occupation-swap action.
- Paired output records all checks passing.

Independent audit is still required before the row can regain retained
effective status.

PR opened: https://github.com/jonathonreilly/cl3-lattice-framework/pull/1863
