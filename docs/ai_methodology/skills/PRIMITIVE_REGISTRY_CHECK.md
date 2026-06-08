# Primitive Registry Check

Use this check before classifying any dependency, premise, import, wall,
admission, or bounded-status source.

1. Read `docs/audit/data/axiom_premise_nodes.json`.
2. For each registered primitive node relevant to the claim, read the node's
   `current_path` source note. Do not rely on memory or prose elsewhere.
3. Treat registered primitives as approved premise nodes. They chain-satisfy
   dependencies without making downstream rows `retained_bounded`.
4. Do not classify a registered primitive as an axiom, Tier-A admission,
   imported value, missing premise, no-go wall, or source of bounded status.
5. Do not grant more than the primitive source note declares. Any
   dimensionless quantity, selector, weighting rule, normalization rule,
   probability rule, readout bridge, dynamics, source/action, or empirical
   match remains separate unless independently derived or explicitly admitted.
6. Treat any proposed primitive absent from the registry as unapproved. It
   requires explicit owner approval and a reviewed registry/policy update
   before a worker may use it as an accepted premise.

Current approved primitive:

- `scale_reference_primitive`:
  `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`. This grants the single
  dimensionful scale reference `a^{-1} = M_Pl` as a units conversion only.
  It is not a Planck import, not a Tier-A admission, and not a bounded-status
  source. It does not assert `a/l_P = 1` as a derived theorem or supply any
  dimensionless physics.
