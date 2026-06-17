# Handoff

This branch wires the Koide A1 fractional-topology no-go synthesis for audit.

The new primary runner imports and executes all five existing probe runners:

- O13 Cheeger-Simons `R/Z`
- O14 orbifold Chern
- O15 eta-to-radian lift
- O16 fractional QH analog
- O17 twisted K-theory

The source note now has an explicit `Primary runner` line, allowing
`build_citation_graph.py` to resolve the primary runner. The helper resolver
then includes all five probe scripts because the wrapper uses static
`import scripts...` imports.

Next action: reviewer should inspect the PR, then the independent audit lane
can decide whether the no-go synthesis row is audit-ready.

PR: https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/4260
