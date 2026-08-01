# The stabilization threshold — not derivable, and neither reading is "settled" — Cycle 862

Date: 2026-08-01

Authority: none

Audit: unset

Status: bounded worked result (the content-stabilization census; the
conditional forcing argument; the corrected coincidence decomposition;
the tick-vacuity negative)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle862_stabilization_threshold_2026_07_28.py`](../scripts/frontier_cycle862_stabilization_threshold_2026_07_28.py)
- [`frontier_cycle862_stabilization_independent_check_2026_07_28.py`](../scripts/frontier_cycle862_stabilization_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status. Owner-directed exercise route (threshold derivability inside
the confirmation-ladder model); no axiom surface touched.

## Result up front

Can the record threshold be DERIVED inside the ladder model from the
Record axiom's own clauses? The attempt ran under one declared plain
reading and the answer is no — with exact structure:

- **the machinery regression is exact** (independently rebuilt from
  the 719 core in this stack: 182/114 stamps, the 34/49/31 split, 68
  E1-only, the landed content digest);
- **the stabilization census** (first rung whose content every later
  clean confirmation repeats, horizon 51,115): 56 keys stabilize at
  the set itself, 126 at scattered later rungs, and the rest are
  never certified within horizon — verdict
  `STABILIZATION_INCOMPLETE_AT_HORIZON`;
- **the corrected coincidence decomposition (reversal thirty)**: of
  the 114 both-stamped keys, **27 stabilize before their E2 stamp, 14
  exactly at it, and 73 change content after it**. v1 reported zero
  at-E2 coincidences; the checker refuted it; the v1 defect was a
  first-bucket-wins ordering (rung==1 tested before E2 equality) plus
  a missing change-after bucket — diagnosed and repaired in v2;
- **the conditional forcing argument is internally valid**: under
  reading R ("the locked content is the content the admissible
  dynamics sustains"), every threshold below a key's stabilization
  rung has its exact contradicting witness (2,223,285/2,223,285), and
  in particular **73 of E2's own stamps are below-threshold** — under
  R, most E2 records lock content the universe later revises. Under
  fiat-permanence (the record keeps its content regardless), nothing
  is forced. Both readings printed;
- **the tick-restricted rescue fails**: "stable across later on-tick
  confirmations" is vacuity-dominated (every key's final on-tick
  event is trivially stable over an empty tail); the 43 non-vacuous
  at-E2 cases are data, not a reading;
- verdict: **THRESHOLD-NOT-DERIVED** — stabilization is a third
  structure, scattered relative to both landed clocks, uniform with
  nothing.

**What this settles for the pending decision**: the "records mark
settled facts" philosophy selects NEITHER landed reading — under the
sustained-content reading it indicts most E2 stamps as premature and
E1's even more so. The two landed readings are cadence choices (the
fine clock and the tick, per Cycle 861); content-stability is
independent of both; and the threshold inside the ladder model
remains a dial, now with the exact map of what each setting commits
to.

## Supplied / derived / open

### Supplied

- the 719 core; the certified 860 regression targets (as pinned
  verification constants); everything the cited packages declare.

### Derived

- the content sequences and stabilization census; the corrected
  decomposition; the witness count; the tick-vacuity negative.

### Open

- stabilization beyond the horizon (the incomplete tail); whether any
  physically-motivated reading selects the stabilization structure
  itself as the record set (a third-candidate question, now with its
  census in hand).

## Negative-claim discipline

The non-derivability verdict is conditional structure, exactly
scoped: reading R's forcing is machine-checked with full witnesses;
fiat-permanence's non-forcing is stated; the coincidence numbers are
the checker-corrected ones; the horizon censoring is explicit.

## Checker disclosure

The checker refuted v1's zero-at-E2 claim (reversal thirty) and
exposed the tick-probe vacuity; v2 adopts both. Only the checker's
pinned expectation constants were re-frozen; its attack logic is
byte-identical and v1-era labels are retained by design — disclosed
here and in the receipt, not edited away.

## Verdict

We asked whether the axiom's own words could choose the moment a fact
becomes a fact, and the answer is that the words permit three
different clocks and privilege none: the first glimpse, the tick, and
the settling — and the universe files different paperwork under each.
The threshold stays in the owner's hands, but for the first time
every setting comes with its receipts. Independent audit still
required.
