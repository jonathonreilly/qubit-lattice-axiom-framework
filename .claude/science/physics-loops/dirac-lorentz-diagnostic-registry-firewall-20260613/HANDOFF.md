# Handoff

This PR addresses the audit row caveat by making the primitive-registry check executable.

The runner now loads `docs/audit/data/axiom_premise_nodes.json`, verifies the current canonical premise ids, and asserts that the row's load-bearing premise set is only `minimal_axioms`. The three approved primitives are checked for their limited registry caps and are not used to supply the rejected Lorentz repairs.

The source note adds the same firewall in prose. The row remains diagnostic/open-gate: no Nelson comparison theorem, no unitary Poincare representation, no self-adjoint Hamiltonian surface, and no interacting Lorentz naturalness theorem is asserted.
