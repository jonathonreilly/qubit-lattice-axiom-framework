# Primitive Registry Check

Use this check before classifying any dependency, premise, import, wall,
conditional input, or bounded-status source.

1. Read `docs/audit/data/axiom_premise_nodes.json`.
2. For each registered primitive node relevant to the claim, read the node's
   `current_path` source note. Do not rely on memory or prose elsewhere.
3. Treat registered primitives as approved premise nodes. They chain-satisfy
   dependencies without making downstream rows `retained_bounded`.
4. Do not classify a registered primitive as an axiom,
   imported value, missing premise, no-go wall, or source of bounded status.
5. Do not grant more than the primitive source note declares. Any
   dimensionless quantity, selector, weighting rule, normalization rule,
   probability rule, readout bridge, dynamics, source/action, or empirical
   match remains separate unless independently derived.
6. Treat any proposed primitive absent from the registry as unapproved. It
   requires explicit owner approval and a reviewed registry/policy update
   before a worker may use it as an accepted premise.

Current approved primitives:

- `scale_reference_primitive`:
  `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`. This grants the single
  dimensionful scale reference `a^{-1} = M_Pl` as a units conversion only.
  It is not a Planck import and not a bounded-status
  source. It does not assert `a/l_P = 1` as a derived theorem or supply any
  dimensionless physics.
- `kinetic_isotropy_primitive`:
  `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`. This grants only the
  structural OS0 kinetic-form isotropy `c_t = c_s`: the emergent tick is
  grained on the same footing as the spatial edge. It is not an axiom and not
  a bounded-status source. It does not supply an
  absolute scale, spacing-ratio theorem, dynamics, Lorentz-closure theorem,
  mass ratio, coupling, mixing angle, phase, selector, readout bridge,
  probability rule, normalization rule, or empirical match.
- `realized_state_primitive`:
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`. This grants only
  pointwise evaluation at a supplied law-admissible realized state
  (the axioms select no state; a history fixes one). It is not an axiom and
  not a bounded-status source. It does not supply a
  state, state-selection rule, measure, typicality or genericity assumption,
  weighting, normalization, probability rule, preferred or default state, or
  any state-contingent value; a quoted number that would differ had another
  permitted state been realized is registered data, not derivation output.
  The past hypothesis is explicitly not housed by this primitive.
