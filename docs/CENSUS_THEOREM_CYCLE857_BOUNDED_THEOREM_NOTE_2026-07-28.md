# Conditional `C11` census theorem — Cycle 857

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded conditional result (closed-form counting law with
structural certification, conditional information accounting, and a
declared one-at-a-time sensitivity table)

Claim type: bounded_theorem

**Primary runner:**
[`frontier_cycle857_census_theorem_2026_07_28.py`](../scripts/frontier_cycle857_census_theorem_2026_07_28.py)

**Independent helper runner:**
[`frontier_cycle857_census_independent_check_2026_07_28.py`](../scripts/frontier_cycle857_census_independent_check_2026_07_28.py)

Load-bearing supplied boundary:
[`RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).
That note has `Authority: none` and `Audit: unset`; it supplies one controller
token and leaves separated multi-source composition open.

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Conditional result up front

Define the bounded generator to contain tuples `(phase, S)` where the carrier
is a labelled oriented `C11`, `phase` is one global label in a four-element
set, and `S` is an unlabeled simple subset of `k=2..5` sites with cyclic pair
distance at least two. For this declared generator, the following are exact
theorems rather than empirical enumeration claims:

- **the counting law**: for k = 2..5 sources,
  **N_k = C(10-k, k-1) x 4 x 11 / k**, giving exactly
  176 + 308 + 220 + 44 = **748 = 68 x 11**;
- **certified structurally, not just numerically** (the checker's
  verdict `STRUCTURE_CERTIFIED`): C(10-k, k-1) counts the
  separation-admissible spacing patterns via an explicit bijection,
  4 the phases, 11 the origins, and /k the source-label quotient —
  each factor mapped to its census axis, with integrality of the
  quotient certified per stratum;
- **the conditional information accounting is exact**:
  log2(748) = log2(68) + log2(11), or about 6.09 ideal uniform family-index
  bits plus 3.46 ideal uniform within-family index bits; a dense fixed-width
  index uses 10 bits, and neither statement includes the supplied generator
  description, a probability law, or a physical selector;
- **the declared sensitivity table is exact** in the 7,425-member ambient of
  all `(k, phase, simple-site-subset)` tuples with `k=1..6`, formal phases
  `0..4`, and `C11` sites. Removing one predicate while holding the other
  three fixed gives counts 792 / 748 / 4048 / 935; replacing one predicate
  by the stated one-notch tightening gives 572 / 704 / 220 / 561. These are
  one-at-a-time marginal counts, not intrinsic or additive contributions;
- **the packing implication is exact**: `k<=5` follows from distance-two
  separation on `C11`, so relaxing that redundant predicate changes nothing.

Thus 748 is exactly the cardinality of the declared finite generator. This
result does not claim that the framework derives that generator as its full
physical possibility space.

## Supplied / derived / open

### Supplied

- `bank_count=2`;
- the interpretation of the resulting eleven controller-program stations as
  a labelled oriented placement cycle;
- one global four-valued event label, rather than per-source phases;
- indistinguishable source atoms represented by unlabeled simple subsets;
- the `k>=2` multi-source sector, cyclic distance-two separation, and Cartesian
  independence of the phase and placement axes;
- the SHA-pinned Cycle719 core bytes and the one-token/open-multi-source status
  stated in the linked Cycle719 note.

### Derived

- conditional on the supplied generator: the `k<=5` packing endpoint, the
  counting law with per-factor bijections, the stratum and free-orbit totals,
  the ideal uniform and fixed-width index accounting, and the eight-entry
  one-at-a-time sensitivity table with the implied-constraint identification.

### Open

- the counting law at general ring size n (the natural
  generalization: is C(n-1-k, k-1) x phases x n / k the law wherever
  the separation rule holds?); composite-n behavior (ties to the
  free-action scope question of Cycle 852).
- derivation of `bank_count=2`, a physical placement carrier and phase
  observable, separated multi-source composition/dynamics, and an exhaustive
  map from physical initial states to this finite generator;
- a probability law or physical selector over the 748 generator members.

## Negative-claim discipline

The finite law is declared and runner-checked at the `k=2..5`, ring-11,
four-label scope. The physical-generator bridge and the general/composite-`n`
forms are named as open, not claimed.

## Verdict

The declared finite generator contains exactly 748 tuples and 68 free
translation orbits. Conditional on that fixed generator, an ideal uniform
index carries about 9.55 bits of information and a dense fixed-width index
uses 10 bits. No exhaustiveness, probability, selector, or physical-input
claim follows from this arithmetic. Independent audit still required.
