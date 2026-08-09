# Exact algebra of the five candidate weightings on the stipulated composed-record model — Cycle 905 (salvage)

Date: 2026-08-08

Authority: none

Audit: unset

Status: conditional bounded theorem (exact finite combinatorics on a
stipulated in-file model; one primary and one independent checker
spec'd to refute; no axiom surface touched; NO probability postulate,
NO Born-rule claim, NO measure selected, NO candidate eliminated, NO
interface or bridge claim, NO framework-compatibility claim)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle905_weighting_exact_algebra_2026_08_08.py`](../scripts/frontier_cycle905_weighting_exact_algebra_2026_08_08.py)
- [`frontier_cycle905_weighting_exact_algebra_independent_check_2026_08_08.py`](../scripts/frontier_cycle905_weighting_exact_algebra_independent_check_2026_08_08.py)

Receipt:

- [`weighting_exact_algebra_cycle905_receipt_2026_08_08.json`](../outputs/weighting_exact_algebra_cycle905_receipt_2026_08_08.json)
- [`weighting_exact_algebra_independent_check_cycle905_receipt_2026_08_08.json`](../outputs/weighting_exact_algebra_independent_check_cycle905_receipt_2026_08_08.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: rebuilt by the review-loop salvage pass 2026-08-08
after the original Cycle-905 package was REJECTED in review (see the
Review record below). Independent audit still required.

## What the claim is, exactly

A conditional finite-combinatorics result and nothing more. Both
runners are SELF-CONTAINED: their only pinned upstream input is the
landed Cycle-719 controller core
([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
sha/blob-pinned, present on `origin/main` at the pinned blob). The
composed record-write model — census, seeds, initial states, dirty
partition, schedules, dead-wire register, slot allocation — is
stipulated IN-FILE in the primary and rebuilt from an independent
in-file transcription in the checker. It is the same in-file
stipulation, function for function, as the current-main Cycle-878
support note's primary
([`EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md`](EVENT_SPACE_GROUNDWORK_CYCLE878_SUPPORT_NOTE_2026-07-28.md));
that note is a cross-reference for the reader, not an input of either
runner. Everything below is conditional on the stipulated model and
its declared scope inputs; nothing below is a statement about the
axiom surface, about probability, about physical occurrence, about
any interface, or about the selection of any weighting.

The five candidate weightings are the Cycle-878 finite-measure
candidates — counting, per-world uniform, occupation-weighted,
formation-lifetime, formation-moment — restated in-file. "Candidate"
is an algebraic bookkeeping predicate; framework Admissibility is an
axiom-level notion and no lemma connects it to these event atoms.
Every fraction is labelled **"bookkeeping fraction, not probability."**

## The certified calculations, exactly

On the stipulated model (92,260 realized record-write events over 748
census worlds at horizon 16,384; 164 worlds ever form; the 584
never-formed worlds carry 73,088 events, all bank-tag writes):

1. **Rank.** The 5 x 92,260 integer weighting matrix has exact rank
   **5** — the five weightings are linearly independent — by three
   agreeing routes (rational full-pivot elimination; division-free
   Gram/Laplace minors; a world-reduced cross-check with
   world-constancy VERIFIED, not assumed), with an exhibited
   nonsingular 5 x 5 minor (determinant
   138,978,185,647,720,130,150,400,000 on worlds 0, 1, 7, 8, 11). The
   three weightings with nonempty zero sets have rank 3 among
   themselves.

2. **Coefficient identity and its event-level residual.** The
   world-coefficient identity a4 + a5 = (boundaries + 1) * [formed]
   holds on all 748 world rows (0 violations). The candidate
   combination it suggests, (boundaries+1)*M2 − M4 − M5, has nonzero
   event-level residual on EXACTLY the 73,088 events of the
   never-formed block (set equality verified, not just counts), so the
   identity induces no linear dependence among the five event-level
   weightings — consistent with rank 5.

3. **Zero sets.** M1 and M2 have EMPTY zero sets, with exact minimum
   event numerators 1 and 8,320. The zero sets of M3 and M4 are
   IDENTICAL AS SETS and equal the never-formed block (73,088 events);
   the zero set of M5 strictly contains it (worlds formed at moment 0
   add 3,096 events; 76,184 total). These are bookkeeping facts about
   the stipulated model, not selection facts.

4. **Difference supports.** All ten candidate pairs differ somewhere
   (no two candidates are indistinguishable). The three pairs among
   {M3, M4, M5} differ on IDENTICALLY the same 19,172 events (the
   formed-world block) and on identically the same cells of every
   declared family, while the exact fraction VALUES at those events
   differ — witnesses retain both unequal values. Equal difference
   supports are a support/cardinality fact only; they are NOT equality
   of the weightings, which remain mathematically distinct, and no
   observational reading of any kind is attached to them.

5. **Mass lattices, as necessary filters only.** The totals are
   92,260; 802,813,440; 897,595,870,080; 29,530,480,287,360;
   2,192,349,344,640, and the exact subset-mass lattices (lcm of
   normalized event-mass denominators) are 92,260; 802,813,440;
   7,012,467,735; 230,706,877,245; 17,127,729,255, with every prime
   factorization machine-verified (deterministic Miller-Rabin plus
   recomposition). The only statement made is the NECESSARY condition:
   a subset mass p/q in lowest terms under a weighting has q dividing
   that weighting's lattice. Nothing here decides which denominators
   are achieved by actual subsets, prices any separation, or selects
   anything.

6. **One-way positivity lemma (conditional).** If a weighting's event
   masses are strictly positive on every event — as holds for M1 and
   M2 here — then every NONEMPTY subset of events carries strictly
   positive mass, so such a weighting cannot satisfy any constraint
   that would demand zero total mass on some nonempty subset. Whether
   ANY such constraint applies to this model is expressly NOT decided
   here, and the converse direction (that a weighting with a nonempty
   zero set can satisfy any particular such constraint) is expressly
   NOT claimed.

## Checker

Independent in-file rebuild of the whole model (own transcription;
chunk-granularity dead-wire accumulation across the whole window —
strictly more sampling points, so census equality is a real check),
plain Fraction weightings normalized to total mass 1 against the
primary's integer-numerator arithmetic, integer multiply-only
elimination plus modular rank over three large primes against the
primary's Fraction elimination and Gram/Laplace minors, event-level
brute-force difference supports against the primary's world-level
route, an exhaustive positivity sweep over every cell of every family
for M1/M2, and independently recomputed lattices and factorizations.
The verdict covers EVERY certified statement of the primary receipt —
15 claim-survival rows, none omitted. Verdict **CORROBORATES**, 8/8
teeth bite, exit code fail-closed (nonzero on any refutation or gate
failure). Both runners exited 0 with all certificates PASS.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "carry the durable exact finite calculations of the rejected Cycle-905 package as conditional finite-model support: rank, zero sets, residual, difference supports, factorizations"
source_of_blocker_text: review_salvage
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "any future work on these weightings starts from this exact-algebra inventory; everything the rejected package claimed beyond it (interface constraints, candidate elimination, separation pricing, symmetry tension) remains NOT ESTABLISHED and would need to be built from scratch against current-main inputs"
```

## Status fields

```yaml
actual_current_surface_status: bounded_theorem (conditional finite combinatorics on the stipulated in-file model; unaudited)
target_claim_type: bounded_theorem
conditional_surface_status: conditional on the stipulated in-file model and its declared scope inputs
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite certificates of the rank, the coefficient identity and its residual set, the zero-set lattice, the pairwise difference supports, and the verified mass-lattice factorizations; nothing selected, nothing eliminated, nothing postulated, no interface or framework-compatibility claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports (load-bearing; stipulated definitions and scope inputs only)

- the landed Cycle-719 controller core
  ([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py),
  sha256 `0c041791…`, blob `c123b8d6…`, present on `origin/main` at
  this blob) — the only pinned upstream input of either runner;
- the stipulated in-file composed record-write model definition and the
  five candidate weighting definitions (restated in-file in both
  runners);
- explicit scope inputs, all stipulated computational boundary
  conditions that materially determine the event set and every count:
  2 banks; source counts 2–5 over 11 stations with cyclic isolation
  (748 census worlds); horizon 16,384 orbits; dead-wire observation
  windows 512 (chunk granularity) and 4,096 (orbit granularity);
  register cap 64 wire-visible ordinals per (bank-tag, world); one
  formation slot per world.

### Provenance context (non-load-bearing)

- the numbers reproduced here first appeared in the rejected Cycle-905
  package; they are recomputed here from scratch on the self-contained
  stipulated model, and nothing from that package (or from the
  Cycle-863/867/902 lineage, or from any axiom file) is read, pinned,
  or imported — the legacy module names are import-blocklisted;
- the identification of the stipulated in-file model with any landed
  substrate is an OPEN bridge (as recorded on the current-main
  Cycle-878 support note).

### Derived (conditional on the stipulated model)

- the rank-5 statement with its exhibited nonsingular minor;
- the coefficient identity with its exact event-level residual set;
- the exact zero-set counts and set identities;
- the exact pairwise difference supports with retained unequal values;
- the verified total/lattice factorizations as necessary filters;
- the one-way positivity lemma.

### Open (expressly not decided here)

- measure selection among the five candidates, and any constraint that
  would narrow them;
- whether any constraint demanding zero mass on a nonempty subset of
  events applies to this model, and any interface/bridge content from
  any other lane;
- subset realizability for any demanded mass denominator (the lattice
  condition is necessary only);
- any operational bridge from difference supports to preparations,
  observables, or outcome statistics;
- the values of the framework's local conditional probability
  distribution and its lift through Record to these event atoms;
- the identification of the stipulated in-file model with any landed
  substrate.

## Review record

The original Cycle-905 package ("the Born lane opens", PR #5967) was
REJECTED by the sole combined adversarial science review
(FAIL/SALVAGE_REJECT, 2026-08-08). Grounds, compressed:

- its evidence was pinned to absent or superseded ancestor bytes
  (including a census module absent from `origin/main`), so the delta
  was not replayable on `origin/main`;
- its vendored Cycle-902 runner could not execute (exit 2 on five
  missing upstream artifacts), so the gravity-side premises had no
  runnable reproduction closure;
- it resurrected Cycle-878 conclusions that the landed review repair
  had expressly withdrawn ("admissible" candidates, an atom-level
  covariance credential, a blanket no-probability boundary);
- its zero_count>0 gate did not prove the claimed 42-cell pullback
  hosting (a one-way exclusion was presented as a two-way selection);
- divisibility was promoted from a necessary condition to an
  unproved exact separating construction;
- its checker omitted claimed ledger rows while the note said all rows
  were corroborated, and several PASS predicates did not check the
  headline claims;
- its universal negative claims carried no structured stress-test
  packet, and its naming and packaging violated the repo vocabulary.

Per the salvage disposition, ONLY the exact rank, zero-set, residual,
difference-support and factorization calculations were preserved, as
conditional finite-model support on in-file stipulated definitions —
which is exactly and only what this package contains. Every claim of
the rejected package beyond these calculations (lane opening,
candidate elimination or survival, twin-ness or observational
equivalence, separation pricing, interface tension, ledger rows) was
DROPPED, is NOT ESTABLISHED, and must not be cited from this note or
from the rejected package.

## Verdict

Five stipulated weightings on a stipulated finite model, and the exact
algebra they satisfy: a rank, an identity with its residual, three
zero sets with their lattice, ten difference supports, and five
factored totals. Nothing is selected, nothing is eliminated, and every
question that would make this physics is stated in Open. Independent
audit still required.
