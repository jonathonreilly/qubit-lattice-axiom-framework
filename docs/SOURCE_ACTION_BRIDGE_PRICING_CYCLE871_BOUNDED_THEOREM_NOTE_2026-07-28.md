# Source-action bridge pricing at a declared finite ansatz — a conditional one-scalar reduction — Cycle 871

Date: 2026-08-03 (revised 2026-08-08, review loop iteration 1)

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed gravity axiom-up
ladder, campaign 5 wave 2; no axiom surface touched). All results in
this note are CONDITIONAL on a declared action-functional ansatz; the
readout-to-action identification is an OPEN bridge (see Review record).

Claim type: bounded_theorem (conditional on the declared ansatz)

Runners:

- [`frontier_cycle871_source_action_bridge_pricing_2026_07_28.py`](../scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py)
- [`frontier_cycle871_bridge_independent_check_2026_07_28.py`](../scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py)

Receipt:

- [`source_action_bridge_pricing_cycle871_receipt_2026_07_28.json`](../outputs/source_action_bridge_pricing_cycle871_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Review record (review loop iteration 1, Sol reviewer, 2026-08-08)

The original headline — "the source-action bridge priced: one scalar,
exactly" — silently promoted the Record axiom's additivity of the scalar
**readout** `I` into additivity of a scalar **action** functional `A`.
The canonical axiom text ([MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md))
supplies additivity for the readout `I` only and expressly keeps
source/action identification outside the axioms (its Qualification and
Open Gates sections list "source/action and physical-observable
identification" as an open gate). No theorem or premise here identifies
action with readout. The claim is therefore NARROWED to conditional
finite algebra at a declared ansatz; the physical reduction of the
source-action bridge to one scalar is NOT established. The obligation
map's former "weaker/equivalent/stronger" labels were parameter-count
comparisons without implication maps and are demoted to modeled
dimension counts; the signed-term row previously added a discrete sign
cardinality to a continuous dimension (a category error) and is
corrected. The old framing must not be cited as a passed gate.

## What the bridge is, in the repo's own words

Nine obligation lines across seven sha-pinned notes name the
source-action bridge as open — gravity (6), mass (2), readout (1) —
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

## Result 1 — a conditional one-dimensional solution space at the declared ansatz

**Statement (declared ansatz; conditional).** Consider scalar
set-functionals `A` on record configurations of a finite lattice patch
(weak-field linear order) satisfying three DECLARED clauses:

- **empty-record vanishing** (declared; modeled on the Record axiom's
  `I(empty)=0` readout sentence): `A(∅) = 0`;
- **disjoint finite additivity** (declared; modeled on the Record
  axiom's count-once readout additivity for `I` — the readout-to-action
  identification is an OPEN bridge, not supplied by any axiom or landed
  theorem): `A(a ∪ b) = A(a) + A(b)` for disjoint `a, b`;
- **translation invariance** (declared; modeled on the Lattice axiom).

Then the solution space is exactly one-dimensional: additivity
triangularly eliminates every multi-site configuration down to
singletons (machine-verified per mask), and the transitive translation
action leaves exactly one singleton orbit. Free dimension = **1** on
all 16 patches tested (1D/2D/3D, up to 27 sites), by two independent
exact routes (full Fraction-arithmetic Gaussian elimination and a
structural triangular route), agreeing wherever both ran. Ablation
prices each declared clause on the 4-site chain: additivity removes 4
free parameters, translation invariance 3, empty-record 1, leaving 1.

**What this does and does not show.** IF the physical source-to-action
map satisfies the declared clauses, THEN its finite-patch residue at
this order is one real scalar. The axioms alone do NOT force the
declared clauses for an action functional: additivity, locality and
the uniform linear shape of the physical source-to-action map are not
derived here, and the physical bridge is NOT reduced to one scalar.
The missing link — a readout-to-action / source-action identification —
is exactly the object this note prices, and it remains OPEN.

## Result 2 — the Gate B normalization residual, exact at the same ansatz

The landed Gate-B runner checked its normalization at one float point
at 1e-15. Here the whole rescaling stabilizer of
`L(1 − λσ/(r+ε))` is determined in exact rationals: it is exactly the
product-one one-parameter family `{(λ,σ) → (tλ, σ/t)}`, it is a group
(closure, identity, inverses machine-verified on a 100-pair grid), and
**zero** in-scope observables (values, pairwise differences, ratios)
separate λ from σ. Shape-after-scale-quotient has free dimension 0.
The stabilizer result is exact because the observable depends only on
the product `λσ`. Whether this gauge freedom is "the same scalar" as
Result 1's is a modeling identification, not a proven identity.

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

The checker replays quotes byte-for-byte against pins, re-derives the
dimension tables by brute force over F_p and union-find orbit counting,
and its mutation harness is live: mutating the window count, the
action's σ-dependence, the brute-force constraint set, or the quote
comparison each makes the corresponding hunt fire and the checker FAIL.

## Scope and honesty

The dimension-1 theorem is at the declared ansatz: scalar functionals
on record configurations of finite torus patches at weak-field linear
order, under the DECLARED action clauses (not under the axioms
directly). The larger-model rows are exactly the places where that
ansatz's boundary lives (kernels, windows, connectivity, readout);
nothing here claims them. The TOE retention-map artifacts (the
#5592–#5598 push) are NOT in-tree on this branch; the bridge was
priced against sha-pinned landed notes only, and no retention rows
were fabricated. Authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed). Independent audit still required.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "still a new source-action premise until derived from retained APS/Wald/Gauss structure (SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md:205); classified as an open_gate proposed-extension boundary (SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md:247)"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "conditional pricing only: IF an action functional satisfies the declared additivity/empty/translation clauses THEN its finite-patch residue is one scalar; the readout-to-action identification that would make this a physical bridge reduction is OPEN and is the object to derive or import next; the larger-model obligations (kernel/window/connectivity/readout) keep their computed model sizes"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "every Result-1/Result-3 statement is conditional on the DECLARED action-functional clauses (disjoint finite additivity, empty-record vanishing, translation invariance); the readout-to-action / source-action identification is an OPEN bridge not supplied by the axioms or any landed theorem; obligation-map rows are modeled dimension counts with no implication maps"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-patch linear algebra in Fraction arithmetic, two agreeing routes, ablation-priced clauses; the stabilizer group determined exactly; classifications replayed as pure functions of computed integers"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the three DECLARED action-functional clauses (disjoint finite
  additivity, empty-record vanishing, translation invariance) — model
  stipulations patterned on the Record/Lattice readout sentences, not
  consequences of them;
- the eight author-declared finite obligation models on the `3 x 3`
  torus.

### Imports

- the seven sha-pinned obligation-bearing notes (quotes only; the
  readout-obligation row is unaudited/open on the current ledger);
- the Gate-B landed action form (AST-verified present);
- nothing numerical: all dimensions derived in-run.

### Derived (conditional on the stipulations)

- the free-dimension-1 solution space with clause ablation;
- the product-one stabilizer group and the observable quotient;
- the eight-clause obligation map with computed model sizes.

### Open

- the readout-to-action / source-action identification (the bridge
  itself — unpriced by this note beyond the conditional reduction);
- the provenance of the one scalar, if the declared clauses are ever
  derived or imported;
- implication maps (if any) between the eight obligation models;
- re-run against the retention-map artifacts when they land in-tree.

## Verdict

At a declared ansatz — additivity, empty-record vanishing, translation
invariance, stipulated for the action functional — the finite-patch
algebra leaves exactly one free scalar, and the Gate-B normalization
residual is an exact one-parameter gauge freedom of the same declared
kind. What stands between the axioms and gravity is unchanged by this
note except in bookkeeping: the source-action identification is still
open, and the remaining obligations now carry computed model sizes
instead of adjectives. Independent audit still required.
