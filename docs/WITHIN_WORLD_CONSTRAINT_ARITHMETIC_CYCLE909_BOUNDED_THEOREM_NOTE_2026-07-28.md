# Within-world constraint arithmetic at a stipulated carrier table: an exact denominator filter and a two-layer representation ambiguity — Cycle 909

Date: 2026-08-04 (revised 2026-08-08, review loop iteration 1)

Authority: none

Audit: unset

Status: bounded worked result, SELF-CONTAINED after review. Every
quantity is an in-file stipulated definition; the census substrate the
original block consumed is not landed on origin/main and is carried
below as provenance context only. No universal negative is claimed.

Claim type: bounded_theorem (conditional on the stipulated table)

Runners:

- [`frontier_cycle909_within_world_pricing_2026_07_28.py`](../scripts/frontier_cycle909_within_world_pricing_2026_07_28.py)
- [`frontier_cycle909_within_world_independent_check_2026_07_28.py`](../scripts/frontier_cycle909_within_world_independent_check_2026_07_28.py)

Receipt:

- [`within_world_pricing_cycle909_receipt_2026_07_28.json`](../outputs/within_world_pricing_cycle909_receipt_2026_07_28.json)
- [`within_world_independent_check_cycle909_receipt_2026_07_28.json`](../outputs/within_world_independent_check_cycle909_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Review record (review loop iteration 1, Sol reviewer, 2026-08-08)

The original note claimed a priced no-go: "nothing native reaches 613",
"future selection must come from a NEW constraint", "more search is
provably useless", and "the degree-2 carrier is two independent
purchases". Review found: (i) the valid lemma is conditional on a
candidate's already-chosen world sums and eliminates only profiles with
those sums — not every function of a census and not future constraints;
(ii) the finite recipe inventory and the four degree-0-to-degree-2
transform tests were author-declared samples, not exhaustive function
classes; (iii) the runner's degree-2-carrier certificate was forced
green unconditionally (`cert_g["pass"] = True`); (iv) the entire
computation consumed a census substrate absent from this tree and
unlanded on origin/main, so none of it was reproducible here. No
no-go-discipline packet accompanied the negative. The negative claims
are WITHDRAWN, the demoted note retains only the bounded arithmetic
cores below, and the old checklist-free negative must not be cited as a
passed gate. Both runners were replaced by self-contained programs whose
certificates bind `pass` to the predicates they name.

## Stipulated scope inputs (declared definitions, not landed facts)

- degree-0 column `[15600, 2910, 492, 1]` over the four atoms
  (everything-else and three designated positions), total `19003`;
- degree-2 column `[1728, 264, 108, 0]`;
- atom site counts `[12, 6, 6, 1]`;
- recorded layer pairs `(36,2), (22,1), (9,1), (1,0)`.

These values are stipulations of a finite table. Their historical
source is an unlanded census stack (see Provenance context); nothing
below asserts that the table is derived, retained, or audited.

## Result 1 — the factorization and the necessary denominator filter

`19003 = 31 x 613` (both factors independently confirmed prime by the
checker), and the degree-2 column's reduced orbit-profile denominator
is `175 = 5^2 x 7`.

**World-sum denominator lemma (exact, filter only).** For integers
`a_w >= 0` and positive world sums `S_w`, the reduced denominator of
`sum_w a_w / S_w` divides `lcm(S_w)`. Hence a candidate profile on
FIXED world sums whose target value is `c/19003` in lowest terms
requires `19003 | lcm(S_w)`. This is a necessary condition on the
already-chosen sums. It does not eliminate other functions of a
census, other sums, or future constraints, and this note claims no
such elimination. Verified on 4,000 randomized instances (primary) and
3,000 on an independent seed with a multiplicative test (checker),
with planted pass/fail controls behaving.

## Result 2 — exact per-site sum-of-two-squares identities

Dividing each column by the atom site counts gives integral per-site
amplitudes satisfying `c0/s = p^2 + q^2` and `c2/s = 2pq` exactly at
`(p, q) = (36, 2), (22, 1), (9, 1), (1, 0)`. Whether these amplitudes
are "the gravity walk's two-layer interference spectrum" is an
INTERPRETATION of the stipulated table, not a theorem of this note;
the per-site reading itself was licensed in the original block only by
a named premise (site-uniform reading), which remains an undischarged
stipulation here.

## Result 3 — the degree-2 ambiguity, representation-scoped

Within the declared two-layer arithmetic representation
(`c0 = s(p^2+q^2)`, `c2 = 2spq`), the degree-0 column does not
determine the degree-2 column: `1300` has three `(p, q)`
representations and `485` has two, so the representation admits
`3 x 2 x 1 x 1 = 6` distinct degree-2 columns over the same degree-0
column. **Scope:** this is non-uniqueness inside one declared
representation. It is NOT a theorem that no operation of any census
carries the first object to the second, and no "two purchases" claim
is made.

## Provenance context (non-load-bearing)

The original Cycle-909 block computed on the full realized record-write
census of the Cycle-863/878 construction, with the Cycle-902/905/906/907
artifacts as inputs. That stack is not landed on origin/main and is
absent from this tree; its recorded outputs (the 1,404-recipe census,
the 3,220 out-of-closure hunts, the zero-realizer tally, the
1,406-dimensional residual-freedom count, the orbit-inhomogeneity
finding, and the named premises P-SITE-UNIFORM / P-WITHIN-WORLD) are
recorded history from that uncertified computation. They certify
nothing here and are cited only so the lineage is not laundered. If
that stack lands, the census-scoped statements can be re-run and
re-scoped in their own package.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "the within-world distribution question and the degree-2 carrier question (lane shorthands BL9/BL10 in the historical handoff): what does the stipulated carrier table force?"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "carry the world-sum denominator filter as a necessary-condition instrument for any FUTURE proposed profile on fixed world sums; carry the six-fold representation ambiguity as the exact size of the degree-2 freedom inside the two-layer representation; everything census-scoped waits on the unlanded substrate landing"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: "all results are conditional on the stipulated four-atom table and, for Result 3, on the declared two-layer arithmetic representation; the historical per-site reading premise (site-uniform) is an undischarged stipulation; no census-scoped or universal claim survives in this note"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact integer/Fraction arithmetic on an explicit in-file table; the lemma is verified with randomized instances and planted controls on two independent seeds and test styles; the two-squares enumeration is confirmed by two enumeration orders"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, stipulated definitions, open

### Stipulated definitions (declared scope inputs)

- the four-atom carrier table and site counts listed above;
- the two-layer arithmetic representation `c0 = s(p^2+q^2)`,
  `c2 = 2spq`.

### Imports

- none. The input closure is empty; no repository file is read.

### Derived (conditional on the stipulations)

- `19003 = 31 x 613` and `175 = 5^2 x 7`;
- the necessary world-sum denominator filter;
- the exact per-site two-square identities;
- the six-fold degree-2 ambiguity within the representation.

### Open

- everything the original block claimed beyond these cores: the recipe
  census and its zero-realizer tally, the residual-freedom count, the
  spectrum interpretation, the site-uniform reading premise, and the
  within-world selection question itself — all census-scoped, all
  waiting on the unlanded substrate;
- any implication from the denominator filter to a search-closure
  statement (none exists in this note).

## Verdict

What survives review is small and exact: a prime factorization, a
necessary denominator condition that any future fixed-sum profile must
clear, four clean sum-of-two-squares identities, and a counted
six-fold ambiguity inside one declared representation. The larger
claims — that the census can never pronounce 613, that search is
provably useless, that the second carrier is a second purchase — were
scoped to inputs this tree does not contain and are withdrawn.
Independent audit still required.
