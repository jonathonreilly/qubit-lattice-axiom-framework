# Realized-State Primitive

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-11
**Type:** meta
**Status:** framework primitive declaration. Registered in
`docs/audit/data/axiom_premise_nodes.json` as
`realized_state_primitive`. Explicit owner approval is recorded in
`docs/audit/AXIOM_MINIMALITY_POLICY.md` section 6.
**Status authority:** independent audit lane only. This source note does not
set, predict, or estimate any audit verdict.
**Support runner:**
[`scripts/realized_state_primitive_irreducibility_support_2026_06_11.py`](../scripts/realized_state_primitive_irreducibility_support_2026_06_11.py)
**Cached log:**
[`logs/runner-cache/realized_state_primitive_irreducibility_support_2026_06_11.txt`](../logs/runner-cache/realized_state_primitive_irreducibility_support_2026_06_11.txt)

## The Primitive

> The laws don't pick the state; the world does — among the states the laws
> permit. Derivations may evaluate at the realized state — pointwise, nothing
> more: no averaging over alternatives, no "typical" or "generic", and no
> quoting a number that would differ had another state been realized. The past
> hypothesis is a separate, stronger input.

## What This Declares

The framework takes one interface fact: the three axioms (Lattice, Quantum,
Record) fix the carrier, the adjacency, and the registration structure — they
supply **no rule selecting which state is realized**. A physical history
additionally fixes one realized state: a single constraint-admissible
configuration ("among the states the laws permit"). A derivation may
**specialize** to it — evaluate an already-derived state functional at that one
configuration, **pointwise**. Pointwise evaluation is function application: it
presupposes no measure, no sigma-algebra, and no disintegration.

This primitive supplies the **slot**, never the **content**. It carries no
specific state, no value, and no dimensionless physics.

## The Policing Clauses (what "nothing more" means)

1. **No averaging over alternatives.** No aggregation or quantification over
   the states the realized one could have been. Averaging requires a choice of
   how much each alternative counts; that choice is physics this primitive does
   not supply.
2. **No "typical" or "generic".** Typicality and genericity are measure-one /
   comeager claims with respect to *some* measure or topology choice;
   ensemble-quantified predicates ("for almost every state", "the generic
   configuration") are not admissible specialization predicates under this
   primitive.
3. **The counterfactual test.** No quoting a number that would differ had
   another permitted state been realized. Any quantity extracted under
   specialization must be invariant as the realized state ranges over the
   entire conditioned family; if it varies, it depended on a representative
   choice — it is registered data about our world, to be matched like the
   masses, and may not cite this primitive as derivation support.
4. **Constraint admissibility.** "Among the states the laws permit": the
   supplied state must satisfy the framework's own derived consistency
   structure. The primitive licenses no evaluation at configurations the
   axioms' retained theorems exclude.

## Why It Is A Primitive

The framework baseline, Lattice + Quantum + Record, is state-blind: the axioms
fix an operator algebra and a registration structure, and a state is an
additional datum (a positive normalized functional on that algebra). That the
axioms cannot supply it is not a temporary gap but a structural fact,
exhibited case by case on exact finite-dimensional instances:

- the dynamics is state-blind while registered outcomes are state-contingent
  (the same operator set produces growing, shrinking, flat, or fluctuating
  record counts depending solely on the supplied state — see the arrow note
  below and check S1/S4 of the support runner);
- no derived selector picks a point of a degenerate invariant manifold
  (`docs/OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md`);
- candidate "natural" references are reconstructions, not selections: the
  maximal-symmetry reference is one invariant state among a continuum of
  invariant states on a degenerate manifold (support runner, check S2), and
  identifying it as "the natural input" is exactly the move the record
  ontology demotes (a realist slip).

A primitive (rather than a per-note disclaimer) because the alternative is
each note ad-hoc wording its own conditioning — which is precisely how a
measure, a typicality assumption, or a representative choice gets smuggled.
One governed object with fixed policing clauses replaces scattered prose.

## What This Does Not Do

- It does not add or amend an axiom. The minimal framework baseline remains
  the three named axioms in `docs/MINIMAL_AXIOMS_2026-06-05.md`.
- It does not supply a state, a state-selection rule, a measure or
  distribution over states, a typicality or genericity assumption, a
  weighting, a normalization, a probability rule, a preferred or default
  state, or the value of any state-contingent quantity.
- It does not permit identifying the realized state with the maximal-symmetry
  reference (`I/d`-type reconstructions) "as the natural input".
- It does not house the **past hypothesis**. The past hypothesis — the
  existence of a low-record (low-entropy) end of the realized history — is a
  strictly stronger claim: it asserts the realized state is *special*, which
  is a typicality-class claim of exactly the kind clauses 1-2 forbid. It
  remains a separate named input, anchored as the residual of
  `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`
  (which derives the arrow's *direction* from record formation and pins the
  *existence* of the low-record boundary as the open input; statuses are
  pipeline-derived). The two inputs are distinct axes; the support runner
  (check S4) exhibits the separation on an explicit instance.
- It does not convert state-contingent content into axiom-derived content.
  Registry semantics: as an approved premise node this primitive
  chain-satisfies dependencies without bounding downstream rows — but the
  primitive itself carries no contingent content, so a row that *quotes data
  of a particular realized state* (a registered pattern, a locus choice, a
  holonomy class) remains conditional on that supplied data exactly as
  supplied inputs always are. Nothing about this primitive lifts such a row
  into the unconditional column; effective statuses remain audit-lane-only.

## The State-Contingency Register (initial entries)

Entries below are the data this primitive's slot is currently known to carry —
each backed by a landed exact-runner result establishing that the datum is
underdetermined by Lattice + Quantum + Record + retained structure. Future
entries require the same: a runner-backed underdetermination result, not a
convenience reclassification. (Statuses are pipeline-derived and set by the
independent audit lane; paths below are source notes, not status claims.)

1. **Which point of the open-shell degenerate ground manifold is realized**
   (invariant locus vs symmetry-broken complement) —
   `docs/OPEN_SHELL_INVARIANT_LOCUS_CONDITIONAL_NEUTRALITY_NO_DERIVED_SELECTOR_BOUNDED_THEOREM_NOTE_2026-06-10.md`.
2. **Which induced holonomy content the matter state carries** (the derived
   curvature functional is exactly flat on the sea and state-dependently
   non-flat off it) —
   `docs/INDUCED_HOLONOMY_MATTER_STATE_FUNCTIONAL_DERIVED_CURVATURE_TRAJECTORY_BOUNDED_THEOREM_NOTE_2026-06-10.md`.
3. **Initial-state dependence of record-dressed relaxation data** —
   `docs/INTERLEAVED_MEAN_MAP_PERIPHERAL_COUNT_COLLAPSE_ALMOST_PERIODICITY_REMOVAL_BOUNDED_THEOREM_NOTE_2026-06-10.md`.
4. **Per-sector registered weight patterns** (e.g. the charged-lepton block
   weight `r`) — registered patterns of the realized state, matched like the
   masses; canonical statement in
   `docs/RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`
   (guardrail G3). This primitive is the registry-level home of that
   discipline: dial settings (`r = 0, 1/2, 1`) are sector data, never forced.

**Explicitly not an entry:** the past hypothesis (see above — separate,
stronger input).

## Review Trail

Wording was stress-tested by a two-round, ten-persona adversarial physics
panel (lattice gauge theory, operator algebras/axiomatic QFT, quantum
foundations, cosmology/initial conditions, particle phenomenology, general
relativity, statistical mechanics, precision flavor experiment, condensed
matter, sceptical senior theory). Round 1 (a "conditioning ONLY" wording)
drew 9 reservations + 1 objection: the decisive defects were the
measure-presupposition of the word "conditioning" (and its Borel-Kolmogorov
ill-posedness at measure-zero specializations), an unbanned "generic", an
unpinned value-extraction seam, and the past-hypothesis bundling
contradiction. Round 2 (the present wording: pointwise evaluation; "typical"
and "generic" banned by name; the counterfactual test; constraint
admissibility in-clause; the past hypothesis carved out) passed 10/10 with no
objections. The corpus motivates the named ban: "generic/generically" appears
~800 times across ~356 notes versus ~57 for "typical" — the named ban covers
the workhorse term, and the counterfactual test independently forecloses the
substance.

## Enforcement

Mechanical, not honor-system: workers apply
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (do not grant more
than this note declares); a specialization citing this primitive for a datum
absent from the register above is a misuse (the correct move is to land the
underdetermination runner first); the audit lane alone sets effective
statuses, and nothing in this primitive's semantics promotes state-contingent
rows.
