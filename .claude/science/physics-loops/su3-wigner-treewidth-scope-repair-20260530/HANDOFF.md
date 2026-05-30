# Handoff

This PR repairs `su3_wigner_l3_treewidth_infeasible_2026-05-04`.

The audit blocker was not the graph computation; it was scope and formula
inventory:

- heuristic upper bounds were written as if they were lower bounds;
- global "regardless of heuristic" infeasibility language exceeded the runner;
- `8^30` was displayed as roughly `10^28` entries instead of
  `1.2379 x 10^27`.

The repaired note is scoped to the two implemented heuristics, min-degree and
min-fill. It explicitly does not prove a treewidth lower bound and does not rule
out all path optimizers.

After pipeline:

- `audit_status: unaudited`
- `effective_status: unaudited`
- queue `ready: true`
- `open_dependency_paths: []`

Independent audit remains required before any verdict is applied.
