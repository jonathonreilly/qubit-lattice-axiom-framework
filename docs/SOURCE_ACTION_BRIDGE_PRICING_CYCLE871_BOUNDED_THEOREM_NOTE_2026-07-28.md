# The source-action bridge priced: one scalar, exactly — Cycle 871

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed gravity axiom-up
ladder, campaign 5 wave 2; no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle871_source_action_bridge_pricing_2026_07_28.py`](../scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py)
- [`frontier_cycle871_bridge_independent_check_2026_07_28.py`](../scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py)

Receipt:

- [`source_action_bridge_pricing_cycle871_receipt_2026_07_28.json`](../outputs/source_action_bridge_pricing_cycle871_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted 2026-08-03; substitution disclosed in the
campaign STATE); supervisor review including independent verification
of the structural route (triangular count-once elimination + orbit
identification). Scope disclosure: the TOE retention-map artifacts
(the #5592–#5598 push) are NOT in-tree on this branch; the bridge was
priced against sha-pinned gravity-lane primaries instead, and no
retention rows were fabricated. Independent audit still required.

## What the bridge is, in the repo's own words

Nine obligation lines across seven sha-pinned notes name the
source-action bridge as open — gravity (6), mass (2), readout (1) —
byte-recovered quotes, including:

- "still a new source-action premise until derived from retained
  APS/Wald/Gauss structure"
  (`SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md:205`);
- "classified as an `open_gate` proposed-extension boundary"
  (`SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md:247`);
- "The projective measurement theorem alone does not supply that
  source-action premise" (`YT_LSP` lineage);
- "must provide a physical carrier/source-action bridge and either a
  native eta/holonomy identity or a genuinely inhomogeneous
  Record-facing normalization theorem"
  (`AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md:21`).

## Result 1 — the bridge's free dimension is exactly 1

**Statement (declared ansatz).** Over scalar action functionals on
record configurations of a finite lattice patch (weak-field linear
order), the four-axiom surface forces everything but one number:

- **empty record** (Record): `A(∅) = 0`;
- **count-once additivity** (Record): `A(a ∪ b) = A(a) + A(b)` for
  disjoint `a, b` — this is the supplied additive-readout clause, and
  it triangularly eliminates every multi-site configuration down to
  singletons (every mask splits off its lowest bit into a genuine
  disjoint pair — machine-verified per mask);
- **translation covariance** (Lattice): identifies all singleton
  values along the translation generators — on a torus patch the
  action is transitive, so exactly ONE orbit survives.

Free dimension = singleton orbit count = **1**, on all 16 patches
tested (1D/2D/3D, up to 27 sites), by two independent exact routes —
full Fraction-arithmetic Gaussian elimination on the complete
constraint family, and the structural triangular route that never
enumerates it — agreeing wherever both ran. Ablation prices each
clause on the 4-site chain: count-once removes 4 free parameters,
translation covariance 3, empty-record 1, leaving 1.

**Consequence.** Additivity, locality, and the uniform linear shape of
the source→action map are FORCED, not imported. The bridge's entire
import at this order is **one real scalar** (the overall coupling /
normalization). "Derive the source-action bridge" means, exactly:
supply one number's provenance.

## Result 2 — the Gate B normalization residual closed

The landed Gate-B runner checked its normalization at one float point
at 1e-15. Here the whole rescaling stabilizer of
`L(1 − λσ/(r+ε))` is determined in exact rationals: it is exactly the
product-one one-parameter family `{(λ,σ) → (tλ, σ/t)}`, it is a group
(closure, identity, inverses machine-verified on a 100-pair grid), and
**zero** in-scope observables (values, pairwise differences, ratios)
separate λ from σ. Shape-after-scale-quotient has free dimension 0.
Upgrade: "still a runner convention" is now an exact one-dimensional
gauge freedom — the same scalar as Result 1's — not a missing
derivation.

## Result 3 — the obligation map (why the bridge alone is not enough)

Eight clauses classified by computed free dimension against the
bridge's 1:

- **weaker (1)**: GB-S1a shape — dimension 0, forced;
- **equivalent (2)**: GB-S1b source-strength normalization;
  G_Newton/SI normalization — both dimension 1, the SAME
  uniform-scale generator;
- **stronger (5)**: finite-core vs Green kernel (5); GB-S2
  kernel+window (8); GB-S3 connectivity (4); the signed-gravity
  locked term (2); the h-class→angle readout identity (2).

**Campaign consequence:** discharging the bridge does NOT unblock
gravity by itself — the kernel/window, connectivity, and readout
obligations are each strictly stronger than the bridge. The axiom-up
ladder's next rungs are named with their exact sizes.

## Checker teeth

The checker replays quotes byte-for-byte against pins, re-derives the
dimension tables, and its mutation harness is live: mutating the
window count, the action's σ-dependence, the brute-force constraint
set, or the quote comparison each makes the corresponding hunt fire
and the checker FAIL. Clean run: primary 8/8 PASS (0.2 s), checker
8/8 PASS, 0 refutations (0.3 s).

## Scope and honesty

The dimension-1 theorem is at the declared ansatz: scalar functionals
on record configurations of finite torus patches at weak-field linear
order, under the quoted axiom clauses. The five stronger obligations
are exactly the places where that ansatz's boundary lives (kernels,
windows, connectivity, readout); nothing here claims them. The
retention-map absence on this branch is disclosed above; the quoted
obligations came from pinned in-tree notes only.

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "still a new source-action premise until derived from retained APS/Wald/Gauss structure (SIGNED_GRAVITY_APS_WALD_GAUSS_BRIDGE_AUDIT_NOTE.md:205); classified as an open_gate proposed-extension boundary (SIGNED_GRAVITY_APS_LOCKED_SOURCE_ACTION_PROPOSAL_NOTE.md:247)"
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "the bridge premise is reduced to one scalar's provenance; the remaining gravity blockers are the five stronger clauses (kernel/window/connectivity/readout), each with computed size — target GB-S2 or the readout identity next"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite-patch linear algebra in Fraction arithmetic, two agreeing routes, ablation-priced clauses; the stabilizer group determined exactly; classifications replayed as pure functions"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the seven sha-pinned obligation-bearing notes (quotes only);
- the Gate-B landed action form (AST-verified present);
- nothing numerical: all dimensions derived in-run.

### Derived

- the free-dimension-1 theorem with clause ablation;
- the product-one stabilizer group and the observable quotient;
- the eight-clause obligation map with computed sizes.

### Open

- the one scalar's provenance (the bridge's entire residue);
- the five stronger obligations, now with exact dimensions;
- re-run against the retention-map artifacts when they land in-tree.

## Verdict

The bridge that blocks three lanes turns out to be thin: at linear
order the axioms already force every structural feature of the
source→action map, leaving a single scalar — and the Gate-B residual
is that same scalar wearing a runner convention. What actually stands
between the axioms and gravity is now itemized: five named obligations,
each strictly bigger than the bridge, each with its size computed.
Independent audit still required.
