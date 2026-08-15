# Source-action bridge pricing at a declared finite ansatz — a conditional one-scalar reduction — Cycle 871

Date: 2026-08-03 (revised 2026-08-15, review loop iteration 2)

Authority: none

Audit: unset

Status: proposed_retained

This is a bounded, conditional worked result from one worker-authored primary
and one independent checker specified to refute; no axiom surface is touched.
All results are conditional on the declared action-functional ansatz. The
readout-to-action identification remains an open bridge (see Review record).

Claim type: bounded_theorem (conditional on the declared ansatz)

Runners:

- [`frontier_cycle871_source_action_bridge_pricing_2026_07_28.py`](../scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py)
- [`frontier_cycle871_bridge_independent_check_2026_07_28.py`](../scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Review record

The original headline — "the source-action bridge priced: one scalar,
exactly" — treated empty-set vanishing and finite additivity of a scalar
set-functional as consequences of the Record axiom and then promoted that
functional to an action. Neither step is licensed. The current canonical
axiom text
([MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md)) deliberately
does not introduce a scalar `I`, `I(empty)=0`, or finite additivity, and it
keeps source/action identification outside the axioms. The earlier
2026-08-08 review narrowed the action/readout identification but still
described the removed scalar-Record clauses as canonical. This iteration
removes that residual attribution: empty-set vanishing, additivity for two
nonempty disjoint subsets,
the Boolean configuration domain, and action translation invariance are all
independent stipulations of the finite model below.

The physical source-action bridge therefore remains OPEN. The conditional finite result
is only conditional finite algebra. The obligation map's original
"weaker/equivalent/stronger" labels were parameter-count comparisons without
implication maps and remain demoted to modeled dimension counts; a discrete
sign cardinality is kept separate from continuous dimension. The original
framing must not be cited as a passed gate.

## What the bridge is, in the repo's own words

Eight obligation lines across seven sha-pinned notes name the
source-action bridge as open — gravity (6), mass (1), readout (1) —
byte-recovered quotes, including:

- "still a new source-action premise until derived from retained
  APS/Wald/Gauss structure"
  ([SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md](SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md), line 205);
- "classified as an `open_gate` proposed-extension boundary"
  ([SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md](SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md), line 247);
- "The projective measurement theorem alone does not supply that
  source-action premise"
  ([YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md](YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md));
- "must provide a physical carrier/source-action bridge and either a
  native eta/holonomy identity or a genuinely inhomogeneous
  Record-facing normalization theorem"
  ([AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md), line 21 —
  that obligation row is unaudited/open on the current ledger).

The complete pinned text scope is the
[Gate-B interface note](GATE_B_WEAK_FIELD_SOURCE_ACTION_INTERFACE_NOTE_2026-06-16.md),
[locked source-action proposal](SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md),
[Wald/Gauss bridge note](SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md),
[gravity response backlog](SIGNED_GRAVITY_RESPONSE_BACKLOG_2026-04-25.md),
[gravity lane status note](SIGNED_GRAVITY_RESPONSE_LANE_STATUS_NOTE_2026-04-26.md),
[source-scale boundary note](YT_LSP_SOURCE_SCALE_BOUNDARY_AND_STRICT_RESPONSE_CONTRACT_NOTE_2026-05-26.md),
and the
[readout obligation](AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md).
The [Gate-B runner](../scripts/gate_b_weak_field_source_action_interface_2026_06_16.py)
is inspected as pinned text/AST only.

## Result 1 — a conditional one-dimensional solution space at the declared ansatz

**Statement (declared ansatz; conditional).** Consider rational-valued
set-functionals `A` on the Boolean subsets of sites of a nonempty finite
rectangular periodic product patch whose declared translation group acts
transitively on sites, satisfying three DECLARED clauses:

- **empty-set vanishing** (declared): `A(∅) = 0`;
- **nonempty-disjoint additivity** (declared):
  `A(a ∪ b) = A(a) + A(b)` for disjoint nonempty `a, b`;
- **translation invariance** under the patch translations (declared).

Then the solution space over the rationals is exactly one-dimensional:
triangularly eliminates every multi-site configuration down to
singletons, and the transitive translation action leaves exactly one
singleton orbit. Free dimension = **1** on all 16 declared patches tested
(1D/2D/3D, up to 27 sites). Full Fraction-arithmetic Gaussian elimination
and an independent structural route agree on the seven patches where the
full route runs; the structural split identity is exhaustively checked through
14 sites and deterministically sampled on larger patches. Ablation on the
4-site cycle gives: holding the other two clauses fixed, dropping
nonempty-disjoint additivity raises the free dimension by 4, dropping
translation invariance raises it by 3, and dropping empty-set vanishing raises
it by 1; all three clauses together leave dimension 1.

**What this does and does not show.** IF the physical source-to-action
map has exactly this Boolean domain and satisfies the declared clauses, THEN
its finite-patch solution space is one-dimensional. The axioms do NOT force
that domain or those action clauses: additivity, empty-set vanishing,
translation invariance, locality, and the uniform linear shape of the physical
source-to-action map are not derived here. The physical bridge is NOT reduced
to one scalar.

## Result 2 — the Gate B normalization residual, exact at the same ansatz

The landed Gate-B runner checked its normalization at one float point
at 1e-15. For nonzero `L`, `λ`, and `σ`, away from the pole
`r + ε = 0`, direct substitution into `L(1 − λσ/(r+ε))` gives the
rescaling stabilizer `{(λ,σ) → (tλ, σ/t) | t ∈ Q*}`. This product-one
family is a group by multiplication of nonzero rationals. The runner also
checks all 100 pairs from a finite rational sample and finds exactly the
sampled product-one pairs; that finite sample is evidence, not itself a group.
No tested observable built from the in-scope values, pairwise differences, or
ratios separates `λ` from `σ`, because every such value depends on the product
`λσ`. This one-dimensional rescaling parameter is not identified with the
one-dimensional solution space in Result 1.

## Result 3 — the obligation map: modeled dimension counts only

Eight clauses, each given an author-declared finite model on one `3 x 3`
torus, with the model's computed free dimension compared to the bridge
model's 1. **These are model-size comparisons. Equal modeled dimension
does not establish mutual implication; larger modeled dimension does
not establish that one obligation is logically stronger. No implication
maps between the heterogeneous physical obligations are constructed.**

- smaller-model-dim (1): GB-S1a shape — dimension 0 in its model;
- equal-model-dim (3): GB-S1b source-strength normalization; the
  Newton-constant/SI normalization (declared as the same one-parameter
  uniform-scale model — identity not proven); the signed-gravity locked
  term (one continuous scale; its orientation is a two-point discrete
  set the lane LOCKS — zero residual sign choices, reported separately
  and never added to the continuous dimension);
- larger-model-dim (4): finite-core vs Green kernel (5); GB-S2
  kernel+window (8); GB-S3 connectivity (4); the h-class→angle readout
  identity (2).

**Campaign consequence (conditional):** within these declared models,
discharging the bridge clause alone leaves the kernel/window,
connectivity, and readout models with more free parameters than the
bridge model's one. Whether any of those obligations logically implies
or is implied by another remains unestablished.

## Checker teeth

The checker executes the current primary in a subprocess, parses that fresh
stdout, replays quotes byte-for-byte against pinned sources, and re-derives the
dimension tables by brute force over `F_p` and union-find orbit counting. Its
hostile controls alter a claimed dimension, an obligation-model count, the
action's product dependence, one quoted byte, required-row presence, row
uniqueness, a large-patch claim, and the stabilizer headlines; all eight
mutations must be killed for the checker to pass. The primary is never
imported.

## Scope and honesty

The dimension-1 theorem is about a stipulated Boolean set-functional on finite
periodic patches, not about a physical weak-field action derived from the
axioms. The larger-model rows merely locate the boundary of that ansatz
(kernels, windows, connectivity, readout); nothing here claims those models
describe the physical obligations. The bridge was compared only with pinned,
landed notes, and no retention or audit row was fabricated. Authored by a
Claude Opus 5 worker under supervisor spec (substitution disclosed).
Independent audit still required.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: signed_gravity_aps_wald_gauss_bridge_audit_note
target_blocker_text: "still a new source-action premise until derived from retained APS/Wald/Gauss structure (SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md:205); classified as an open_gate proposed-extension boundary (SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md:247)"
source_of_blocker_text: null
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "derive or explicitly import a physical source-action domain, a nonempty transitive patch geometry, and the three action-functional clauses before this conditional finite lemma can support the target; do not treat modeled dimension counts as implication maps"
```

The quoted boundary is unaudited source-note context. The named ledger target
does not supply blocker text or retained authority.

## Status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "every Result-1/Result-3 statement is conditional on a DECLARED Boolean configuration domain, a nonempty rectangular periodic product patch with transitive site translations, rational codomain, and action-functional clauses (additivity for two nonempty disjoint subsets, empty-set vanishing, translation invariance); none is supplied by the axioms or a landed source-action theorem; obligation-map rows are modeled dimension counts with no implication maps"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-patch linear algebra under explicit stipulations, independently checked on bounded patches; exact product-form rescaling algebra; modeled dimension counts only"
audit_required_before_effective_retained: true
bare_retained_allowed: false
packet_helper_runner: scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py
```

Hard landing condition: the citation topology must contain this exact
claim-scoped helper edge and the generated ledger row must expose the same
helper path:

```yaml
source_action_bridge_pricing_cycle871_bounded_theorem_note_2026-07-28:
  - scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the rational codomain, Boolean subset domain, nonempty rectangular periodic
  product-patch family, and transitive site-translation action;
- the three DECLARED action-functional clauses (additivity for two nonempty
  disjoint subsets, empty-set vanishing, translation invariance) — model
  stipulations, not consequences of the axioms;
- the eight author-declared finite obligation models on the `3 x 3`
  torus.

### Imports

- the seven sha-pinned obligation-bearing notes (quotes only; the
  readout-obligation row is unaudited/open on the current ledger);
- the Gate-B runner as pinned text with only the names `gate_b_action` and
  `gate_b_phi` AST-verified present; the product-form expression is an explicit
  local stipulation, not a semantically AST-verified import;
- nothing numerical: all dimensions derived in-run.

### Derived (conditional on the stipulations)

- the free-dimension-1 solution space with clause ablation;
- the product-one stabilizer group of the declared Gate-B expression and the
  sampled observable quotient;
- the eight-clause obligation map with computed model sizes.

### Open

- the readout-to-action / source-action identification (the bridge
  itself — unpriced by this note beyond the conditional reduction);
- the provenance of the one scalar, if the declared clauses are ever
  derived or imported;
- implication maps (if any) between the eight obligation models;
- re-run against the retention-map artifacts when they land in-tree.

## Verdict

At the declared Boolean set-functional ansatz, nonempty-disjoint additivity, empty-set
vanishing, and translation invariance leave a one-dimensional solution space.
Separately, the declared Gate-B expression has an exact one-parameter
product-preserving rescaling freedom. No identity between those parameter
spaces is derived. What stands between the axioms and gravity is unchanged:
the physical source-action domain and clauses remain open, and the other
obligations carry only author-declared model sizes. Independent audit still
required.
