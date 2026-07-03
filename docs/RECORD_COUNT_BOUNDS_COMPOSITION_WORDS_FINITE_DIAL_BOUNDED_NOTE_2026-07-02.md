---
claim_id: record_count_bounds_composition_words_finite_dial_bounded_note_2026-07-02
claim_type: bounded_theorem
claim_scope: "Bounded support: under named unadopted pure-letter, record-production, record-persistence, finite-collection-containment, and chart-mix premises, a pure single-chart composition word has length bounded by the supplied finite record collection, pure single-chart fixed points stay {1/2} or {1} for all word lengths, and the length-<=2 mixed-word dial points are exactly the two chart-mix roots 2^(-1/3) and 2^(-2/3). This does not adopt the premises, select the realized word, fix r, import an empirical modulus, or close/retire any wall."
upstream_dependencies:
  - minimal_axioms
  - occupancy_atom_is_the_outcome_dictionary_flow_selects_equipartition_bounded_note_2026-06-12
runner: scripts/frontier_record_count_bounds_composition_words_2026_07_02.py
---

# Record Count Bounds Composition Words; Pure Single-Chart Dials Stay Fixed (Bounded Note)

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Audit-status authority:** independent audit lane only. This note does not set,
predict, or estimate any audit verdict, and it edits no audit-lane-owned registry
or audit data file.
**Actual current surface status:** open bounded support. No wall is closed and
nothing is adjudicated. The moduli / word-supplier lane stays live, now carrying
named, unadopted premises instead of an open-ended pure single-chart densification
claim.
**Primary runner:**
[`scripts/frontier_record_count_bounds_composition_words_2026_07_02.py`](../scripts/frontier_record_count_bounds_composition_words_2026_07_02.py)
**Cached runner output:**
[`logs/runner-cache/frontier_record_count_bounds_composition_words_2026_07_02.txt`](../logs/runner-cache/frontier_record_count_bounds_composition_words_2026_07_02.txt)

## Firewall

- The bound rests on named premises, none derived and none adopted here:
  pure-letter event, record production, record persistence, finite-collection
  containment, and chart-mix for mixed words.
- Record production and record persistence are dynamics-shaped. The axiom memo
  disclaims any record-production process and lists physical persistence dynamics
  among the open gates outside the axioms.
- Finite-collection containment is a scoping premise. The axiom set does not
  bound a configuration's total number of records; it only states additivity for a
  supplied finite pairwise-disjoint collection.
- Chart-mix is an extra per-step dictionary-supply premise for mixed words. It is
  not needed for pure single-chart iterates.
- Former PR #4843 is now banked on main as docs-only/provenance with no adopted
  premise status. The record-composition bridge is on main as bounded support; it
  does not adopt the composition premise. These are context only.
- No selector is proposed, no empirical modulus is imported, no `r` is fixed, no
  word is selected, and no wall is closed or retired.

## Purpose

For a single supplied dictionary, the composition-word dial set is fixed for all
word lengths: the component chart has only the positive fixed point `1/2`, and
the slot chart has only the positive fixed point `1`. The mixed points
`2^(-1/3)` and `2^(-2/3)` arise only after adding chart-mix, because a mixed word
is not an iterate of either single supplied flow.

The note also records the exact record-count bound: under the pure-letter event,
record-production, record-persistence, and finite-collection-containment premises,
a pure word with `k` letters has `k <= N_rec` for the supplied finite collection.
For a finite maximum length, the mixed-word dial set is finite by a degree bound;
the length-`<=2` mixed-word surface is enumerated completely below.

## Supplied Surface

From [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

- "A state is a configuration of records."
- "For any finite collection of pairwise-disjoint records, scalar readout `I` is
  additive, with `I(empty)=0`."
- Admissibility "does not choose a Hamiltonian or transfer operator, supply
  transition probabilities or weights, select a scalar or nonzero kinetic branch,
  assert a Dirac-square carrier, define a time metric, or provide a
  record-production process."
- Open gates include "arrow, record-production dynamics, physical persistence
  dynamics, time metric, and local observability of records."

From
[`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md):

- the agreement-conditioned double-registration update squares registered weights
  and renormalizes;
- the component chart gives `f(r)=2r^2`;
- the slot chart gives `g(r)=r^2`;
- the chart descriptions form "the same binary, not three independent binaries."

## Named Premises

**Pure-letter event premise.** Each letter of a realized single-chart word is one
agreement-conditioned double-registration event of the occupancy flow read in
that chart. A component word is an iterate of `f`; a slot word is an iterate of
`g`. Since `f` and `g` are two charts of the same binary, a mixed word is not an
iterate of either single supplied flow: `f.f = 8r^4`, `g.g = r^4`,
`f.g = 2r^4`, and `g.f = 4r^4`.

**Chart-mix premise.** A mixed word additionally requires per-step dictionary
supply. This premise is named and not adopted.

**Record-production premise.** Each event registers at least one new record. This
is dynamics-shaped content and is not supplied by the axioms. A zero-production
history can advance the word while registering no records.

**Record-persistence premise.** Records persist across events. The Record
sentence that a locked possibility is invariant under repeated readout gives only
within-readout stability of an already-present record; it is not persistence
across events. A produce-then-vanish history registers records that later vanish,
so the final count need not bound the event total.

**Finite-collection-containment premise.** A supplied finite readout collection
contains the realized history's registered records, and `N_rec` is that
collection's count. The axiom set does not bound a configuration's record total:
an all-sites-recorded configuration on `Z^3` is compatible with the quoted
axiom text.

## Record-Count Bound

Under the pure-letter event, record-production, record-persistence, and
finite-collection-containment premises, induction on a pure single-chart word
gives `k <= N_rec`. Record production gives at least one new record per event;
record persistence keeps each registered record; finite-collection containment
places them in the supplied counted collection.

The bound is exact and tight: a unit persistent contained history achieves
`k = N_rec`. Each premise is load-bearing:

- without record production, events can advance while no new records appear;
- without record persistence, records can vanish before the count is read;
- without finite-collection containment, registrations can land outside the
  counted collection.

## Finite Dial Enumeration

For words over `{f,g}` of length at most `k`, the word count is
`2^(k+1)-2`. A length-`m` word has fixed-point polynomial degree `2^m`, so any
finite maximum word length gives a finite dial set by the sum-of-degrees bound.

The length-`<=2` surface is exact:

- `f`: `2r^2-r = r(2r-1)`, positive fixed point `1/2`.
- `g`: `r^2-r = r(r-1)`, positive fixed point `1`.
- `f.g`: `2r^4-r = r(2r^3-1)`, mixed word, positive root `2^(-1/3)`,
  conditional on chart-mix.
- `g.f`: `4r^4-r = r(4r^3-1)`, mixed word, positive root `2^(-2/3)`,
  conditional on chart-mix.
- `f.f`: `8r^4-r = r(2r-1)(4r^2+2r+1)`; the cofactor has negative
  discriminant and positive leading coefficient, so it adds no positive root.
- `g.g`: `r^4-r = r(r-1)(r^2+r+1)`; the cofactor has negative discriminant and
  positive leading coefficient, so it adds no positive root.

Thus length `<=2` gives `{1/2,1}` on pure single-chart words and, only with
chart-mix, the additional distinct roots `2^(-1/3)` and `2^(-2/3)`.
The boundary `>= 1/2` for the mixed roots follows from strict monotonicity of
`a r^3 - 1` on `r>0`, not from a generic cubic sign shortcut.

## Pure Single-Chart Corollary

For every `m >= 1`,
`f^m(r)=2^(2^m-1) r^(2^m)`, so
`f^m(r)-r = r(2^(2^m-1) r^(2^m-1)-1)` and the unique positive fixed point is
`1/2`.

For every `m >= 1`, `g^m(r)=r^(2^m)`, so
`g^m(r)-r = r(r^(2^m-1)-1)` and the unique positive fixed point is `1`.

Therefore pure single-chart iteration does not densify the dial: the component
chart stays at `{1/2}` and the slot chart stays at `{1}` for all word lengths.

## Residue Map

The remaining content is not resolved by this note:

1. record production and record persistence;
2. supplied finite-collection containment;
3. chart-mix and per-step dictionary supply;
4. the realized history: which word is realized, and the realized step count;
5. related campaign context, including the banked Dynamics proposal and the
   record-composition bridge, with no adopted premise status imported here.

Choosing whether to admit or derive any of these inputs is an owner/science
decision, not a review-loop or audit-loop verdict.

## Does NOT

- Does not derive or adopt the pure-letter event, record-production,
  record-persistence, finite-collection-containment, or chart-mix premises.
- Does not select which word is realized, propose a selector, fix `r`, or import
  an empirical modulus.
- Does not close, retire, or contradict any wall.
- Does not set any audit status or effective status.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
- [`OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md`](OCCUPANCY_ATOM_IS_THE_OUTCOME_DICTIONARY_FLOW_SELECTS_EQUIPARTITION_BOUNDED_NOTE_2026-06-12.md)

Context-only surfaces are intentionally not dependency links.

## No-Promotion Statement

This note promotes nothing. The named premises remain unadopted, and the
independent audit lane owns all statuses. The landed claim is a bounded-support
record of the exact word-count and finite-dial arithmetic.
