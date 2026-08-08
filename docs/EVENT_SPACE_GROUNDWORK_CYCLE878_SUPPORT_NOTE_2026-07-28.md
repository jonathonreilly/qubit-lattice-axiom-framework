# The composed-record event space, measured for structure and nothing else — Cycle 878

Date: 2026-08-03 (revised 2026-08-08, review iteration 1)

Authority: none

Audit: unset

Status: conditional bounded theorem (exact finite combinatorics on a
stipulated in-file model; one primary and one independent checker
spec'd to refute; no axiom surface touched; NO probability postulate,
NO Born-rule claim, NO measure selected, NO framework-compatibility
claim)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle878_event_space_groundwork_2026_07_28.py`](../scripts/frontier_cycle878_event_space_groundwork_2026_07_28.py)
- [`frontier_cycle878_event_space_independent_check_2026_07_28.py`](../scripts/frontier_cycle878_event_space_independent_check_2026_07_28.py)

Receipt:

- [`event_space_groundwork_cycle878_receipt_2026_07_28.json`](../outputs/event_space_groundwork_cycle878_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (substitution disclosed 2026-08-03); revised under review-loop
direction 2026-08-08. Independent audit still required.

## What the claim is, exactly

A conditional finite-combinatorics result. Both runners are
SELF-CONTAINED: their only input is the landed Cycle-719 controller core
([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
sha/blob-pinned, present on `origin/main` at the pinned blob). The
composed record-write model — census, seeds, initial states, dirty
partition, schedules, dead-wire register, slot allocation, occupation
replay — is stipulated IN-FILE in the primary and rebuilt independently
in the checker. Everything below is conditional on that stipulated model
and its declared scope inputs; nothing below is a statement about the
axiom surface, about probability, or about physical occurrence.

## The event space, exactly

From the stipulated composed record-write model at horizon 16,384:
**92,260 realized record-write events** — 164 formation (F), 47,872
B0-edge, 44,224 B1-edge — spread over ALL 748 census worlds (64–129
events each; only 164 worlds ever form). The atoms are the
(world, tag, ordinal) cells and are singletons, so the generated
sigma-algebra is the full power set 2^E. The (bank-tag, ordinal)
family REFINES the global-tag family; 17 of the 28 declared family
pairs cross. Cap disclosed at event-space level: 3,856,705 bank-edge
events beyond the 64-ordinal register cap are not wire-visible.
Internal consistency: the 24 F-events at moment 0 equal the globally
clean lanes at boundary 0, and the occupation ledger and formation
moments match a second in-file replay path exactly.

## The measure-candidate inventory (no selection made)

Five record-native weightings are FINITE-MEASURE CANDIDATES —
nonnegative event-level weights, finitely additive over the certified
disjoint families, normalizable: counting, per-world uniform,
occupation-weighted, formation-lifetime, formation-moment. This is an
algebraic bookkeeping predicate and nothing more; it is deliberately
NOT called "admissible", because framework Admissibility is an
axiom-level notion and no lemma maps the framework's local conditional
distribution through Record onto these event atoms (see Open). The
declared negative control (content diversity) FAILS additivity with an
exhibited witness — the candidacy test is non-vacuous.

Marginal-invariance diagnostics, certified but not acted on (these are
facts about selected coarse marginals, NOT event-space symmetry
statements — the monitor map has no well-defined action on atoms, and
the unequal B0/B1 tag populations obstruct any atom permutation):

- the in-file monitor-phase Z_11 world relabelling is a free census
  bijection (68 orbits of size 11) but is NOT well-defined on atoms;
- only per-world uniform has F_WORLD cell masses constant on those
  world orbits — a structural fact (uniform world mass), not a
  dynamical one;
- NO candidate has equal (tag, ordinal) cell masses under bank-label
  swap (B0/B1 counts differ);
- occupation- and formation-weighted candidates fail support
  faithfulness (73,088 / 73,088 / 76,184 zero-weight events): they
  assign zero mass to realized events of never-forming worlds.

## The fraction ledger

Exact rational event-fraction tables for the certified atom families
under each finite-measure candidate — every table labelled
**"bookkeeping fraction, not probability."** All 10 candidate pairs
DISCRIMINATE, most on all 92,260 atoms; no two candidates are
indistinguishable. The discriminating atoms are a mathematical
discriminator surface — witness cells only; no bridge to preparations,
observables, or sampling frequencies exists, so nothing here is an
experiment.

## Checker

Independent rebuild of the event extraction (reversed lane bit-layout,
independently derived census, seeds, dirty partition, dead-wire
register and slot allocation), the disjointness/refinement lattice by
set containment, and every fraction table (exact). The additivity
implementation is exercised with REAL identities: disjoint-subset
unions not copied from any precomputed partition (index-residue subsets
that slice across every declared family), a three-part disjoint cover,
inclusion-exclusion on genuinely overlapping sets, a complement
identity for a non-covering subfamily, and a separate normalization
check. The marginal-constancy predicate is fed a deterministic
non-symmetry that must break it wherever world masses are not already
constant. Verdict CORROBORATES, 5/5. A narrow banned-phrase scan of the
committed cache is reported as hygiene only — it is an exact-substring
check, not a semantic boundary check, and it gates nothing.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "measure-selection groundwork: the composed-record event space as a sample space; selection requires the values of the framework's local conditional distribution and a derived local-to-event lift, both open"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "any future measure-selection work starts from this inventory: the five finite-measure candidates, their exact disagreement atlas, the marginal-invariance facts, and the support-faithfulness failures; selection itself remains the open gate"
```

## Status fields

```yaml
actual_current_surface_status: bounded_theorem (conditional finite combinatorics on the stipulated in-file model; unaudited)
target_claim_type: bounded_theorem
conditional_surface_status: conditional on the stipulated in-file model and its declared scope inputs
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite certificates of the event space, the refinement lattice, the finite-measure candidate table with a non-vacuous negative control, and the rational fraction ledger; nothing selected, nothing postulated, no framework-compatibility claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (load-bearing; stipulated definitions and scope inputs only)

- the landed Cycle-719 controller core
  ([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
  sha256 `0c041791…`, blob `c123b8d6…`) — the only file input of either
  runner;
- the stipulated in-file composed record-write model definition
  (census construction, event seeds, initial states, dirty partition,
  dead-wire register, slot allocation, formation/bank tagging,
  occupation replay);
- explicit scope inputs, all stipulated computational boundary
  conditions that materially determine the event set and every count:
  B=2 banks; source counts 2–5 over 11 stations with cyclic isolation
  (748 census worlds); horizon 16,384 orbits; dead-wire observation
  windows 512 (chunk granularity) and 4,096 (orbit granularity);
  register cap 64 wire-visible ordinals per (bank-tag, world); one
  formation slot per world.

### Provenance context (non-load-bearing)

- the model's Cycle-852/856/863/867 lineage is provenance only: those
  files are absent from `origin/main`, are not read, pinned, or
  imported by either runner (the legacy module names are
  import-blocklisted), and the identification of the stipulated
  in-file model with any landed substrate is an OPEN bridge;
- no axiom text is in either runner's input closure; the earlier
  draft's byte-pinned quotation of the 2026-06-29 axiom snapshot was
  removed because that snapshot is superseded on current `origin/main`
  ([`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md),
  current sha256 `53175250…`), whose revised Admissibility supplies a
  nearest-neighbor-conditioned probability distribution on the local
  possibility domain with availability as its support.

### Derived (conditional on the stipulated model)

- the event space with its atoms and refinement lattice;
- the five-candidate finite-measure table and the negative control;
- the marginal-invariance and support-faithfulness facts;
- the exact fraction ledger with its disagreement atlas.

### Open

- measure selection among the five candidates (the named open gate;
  this block selects none and derives no constraint that would);
- the values of the framework's local conditional probability
  distribution, and a derived lift of that local law through Record to
  these composed event atoms (the framework-compatibility bridge);
- an operational bridge from the discriminating atoms to preparations,
  observables, and outcome statistics;
- the identification of the stipulated in-file model with any landed
  substrate.

## Review record

Review-loop iteration 1 (Sol, 2026-08-08, FIX_THEN_PROCEED) demoted
this package on every live surface. What changed and why:

- the invalid claim class `support` was replaced by a narrowly scoped
  `bounded_theorem` (conditional finite combinatorics);
- "admissible"/"lawful" candidate language was demoted to
  finite-measure candidacy: the additive-plus-normalizable predicate is
  not framework Admissibility, and no local-to-event bridge exists;
- "covariance" claims were demoted to coarse-marginal invariance
  diagnostics: no action on event atoms exists for the monitor map;
- the "future experiment surface" wording was demoted to a mathematical
  discriminator surface: no operational bridge exists;
- the checker's overlapping/non-covering "must break additivity" gates
  were a category error and were replaced by real disjoint-union,
  inclusion-exclusion, complement, and normalization identities; its
  three-string "no smuggled probability claim" check was demoted to a
  non-load-bearing hygiene scan;
- both runners were made self-contained: the unlanded Cycle-863/867
  files and the stale axiom snapshot were removed from the input
  closures entirely; the model is stipulated in-file;
- the earlier draft's blanket negative boundary ("the foundation
  supplies no probability", "the axioms say plainly that they do not
  choose") was WITHDRAWN as stale and unestablished: current
  `origin/main` Admissibility supplies a local conditional probability
  distribution; what is open is its values and the local-to-event
  lift, not probability content altogether. That withdrawn boundary
  and the earlier draft's checker banner must NOT be cited as passed
  gates.

## Verdict

Before anyone can ask which weighting is true, someone has to say
exactly what is being weighed; on this stipulated model, that is now
done. The sample space is finite and certified twice over; five
finite-measure candidates exist and disagree almost everywhere; and
this block neither selects among them nor shows that anything else
does. What selection will require is stated precisely in Open — no
more, no less. Independent audit still required.
