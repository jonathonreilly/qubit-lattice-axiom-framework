# Census-consistency arithmetic and a conditional likelihood-maximizer lemma; the recorded lock-point menu census as stipulated history — Cycle 911

Date: 2026-08-04 (revised 2026-08-08, review loop iteration 1; file renamed
from `RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_...` — the re-typing
convention is not a theorem and no longer names this note)

Authority: none

Audit: unset

Status: bounded worked result, SELF-CONTAINED after review. Every
certified quantity is an in-file stipulation or an exact lemma; the
substrate the original block computed on is not landed on origin/main
and is carried below as provenance context only.

Claim type: bounded_theorem (conditional on declared model imports)

Runners:

- [`frontier_cycle911_type_vacuity_2026_07_28.py`](../scripts/frontier_cycle911_type_vacuity_2026_07_28.py)
- [`frontier_cycle911_type_vacuity_independent_check_2026_07_28.py`](../scripts/frontier_cycle911_type_vacuity_independent_check_2026_07_28.py)

Receipt:

- [`type_vacuity_cycle911_receipt_2026_07_28.json`](../outputs/type_vacuity_cycle911_receipt_2026_07_28.json)
- [`type_vacuity_independent_check_cycle911_receipt_2026_07_28.json`](../outputs/type_vacuity_independent_check_cycle911_receipt_2026_07_28.json)

Companion (non-propositional):

- [`WORLD_SETUP_BOOKKEEPING_TERMINOLOGY_META_NOTE_2026-08-08.md`](WORLD_SETUP_BOOKKEEPING_TERMINOLOGY_META_NOTE_2026-08-08.md)
  — the recommended world/setup/bookkeeping terminology, split out as a
  convention per the review's labeling ruling.

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Review record (review loop iteration 1, Sol reviewer, 2026-08-08)

The original note bundled exact substrate computations with two
promotions review rejected: (i) "maximum likelihood selects counting
UNCONDITIONALLY" — the AM-GM calculation is correct GIVEN a declared
sample space whose atoms are the individually indexed census events and
an iid product likelihood in which every atom is observed exactly once;
those are load-bearing statistical-model choices not supplied by the
four axioms or the realized-state primitive, and making every observed
instance its own atom makes the empirical maximizer uniform BY
CONSTRUCTION; (ii) the re-typing verdict ("the worlds were setups all
along", "the census weightings were never occurrence weights", "the
interface survives as bookkeeping") — a typing/interpretation
convention, not a consequence of the zero-coupling calculation: a
separately supplied or derived ensemble measure over initial conditions
could still assign occurrence probabilities, and the realized-state
primitive supplies no such measure but does not forbid one. Per the
split ruling the convention moved to a separate meta note and is
asserted nowhere as a theorem. The substrate computations themselves
consumed the unlanded Cycle-863/878 stack absent from this tree, so
both runners were replaced by self-contained fail-closed programs. The
withdrawn wording must not be cited as a passed gate.

## Result 1 — census-consistency arithmetic (exact)

The stipulated recorded census is internally consistent:
`187 x 4 = 748` worlds; `C(748, 2) = 279,378` world pairs (verified by
two independent expressions); the recorded shared-tick-0 pair count
(5,168) and distinct-vector count (323) are within range; the recorded
branch-pair count is 0 (a recorded value, stipulated).

## Result 2 — the likelihood-maximizer lemma, conditional

UNDER the declared model — sample space = the N individually indexed
census events, likelihood `L(p) = prod_e p(e)`, every atom observed
exactly once — the unique maximizer is uniform. Verified exactly on
500 randomized rational vectors (primary), by a pairwise-smoothing
argument and an exhaustive exact grid (checker), with uniform attaining
the bound. **The declared imports are named:** the event ontology and
the iid product factorization. The merged-atom CONTROL certifies these
are load-bearing: merging two events into one atom moves the maximizer
away from event-uniformity. No unconditional selection claim survives;
the lemma cannot strengthen Nature-grade retention on its own.

## Provenance context (non-load-bearing)

The original block's substrate computations — the dual no-coupling
certification (AST sweep + runtime perturbation), the complete
279,378-pair branch matrix with 0 branch pairs, the schedule subtlety
(5,168 shared tick-0 states, 323 distinct vectors), the 164 lock
points each carrying a two-element menu under both operational
readings, the exhibited selection site, the rule-space spectrum under
the declared condition-map premise, the convergence table, and the two
audit flags (the recorded boundary-certificate misquote and the
recorded chunk-slicing artifact) — are recorded history from the
uncertified full-checkout computation on the unlanded stack. They
certify nothing here; if the stack lands they can be re-run and
certified in their own package. The named premises of that history
(sample-space and condition-map premises) are undischarged
stipulations. The realized-state primitive's actual scope is
[REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md);
the axiom baseline is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md).

## Trace gate

```yaml
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "is the recorded census an arena of alternatives, and does any recorded lock point carry a genuine menu? (historical occurrence-rule exercise routes)"
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "carry only: the census arithmetic is consistent; the likelihood lemma is CONDITIONAL on its declared event ontology and product factorization (both named imports); the world/setup terminology is a convention in the meta note, not a premise; the occurrence-weight question and any ensemble measure over initial conditions remain OPEN (underived, unforbidden); substrate-scoped claims wait on the unlanded stack"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "Result 2 is conditional on the declared sample-space and iid product-likelihood imports (named); Result 1 is arithmetic on stipulated recorded counts; the re-typing convention is non-propositional and lives in the companion meta note; no substrate-scoped certification survives in this note"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact Fraction arithmetic with randomized verification, a pairwise-smoothing independent route, an exhaustive exact grid, and a load-bearing-ontology control; recorded values explicitly stipulated"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the recorded census table (counts only, listed in the runner);
- the declared likelihood model: event-instance atoms + iid product
  factorization (LOAD-BEARING, named imports).

### Imports

- none beyond the declared model; the input closure contains no
  repository file beyond the paired runner/cache pins.

### Derived (conditional on the stipulations)

- the census-consistency arithmetic;
- the uniform-maximizer lemma for the declared likelihood, with the
  merged-atom control showing the ontology choice is load-bearing.

### Open

- the occurrence-weight question, including whether a lawful ensemble
  measure over initial conditions can be derived or must be imported
  (the realized-state primitive supplies none and forbids none);
- every substrate-scoped result of the original block (no-coupling,
  branch matrix, menus, selection site, spectrum, convergence table,
  audit flags) — waiting on the unlanded stack;
- the registration of the historical sample-space and condition-map
  premises, if their consumers ever land.

## Verdict

Two things survive review intact: arithmetic that checks, and a lemma
that says exactly what it is conditional on. The maximum-likelihood
argument selects uniform counting precisely because the declared model
atomizes every observed instance and multiplies — name those two
choices and the "unconditional" evaporates. The claim that the worlds
"were setups all along" is a useful way of talking, and it is now
filed where ways of talking belong. Independent audit still required.
