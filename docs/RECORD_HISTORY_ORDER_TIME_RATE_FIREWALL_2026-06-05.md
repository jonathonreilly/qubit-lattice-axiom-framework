---
claim_id: record_history_order_time_rate_firewall_2026-06-05
claim_type_author_hint: no_go
---

# Record History Order Is Not A Time/Rate Metric

**Date:** 2026-06-05
**Claim type:** no_go
**Claim boundary:** narrow negative route-pruning certificate. Independent
audit is required before any effective-status use.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_history_time_rate_firewall_2026_06_05.py`](../scripts/frontier_record_history_time_rate_firewall_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_history_time_rate_firewall_2026_06_05.txt`](../logs/runner-cache/frontier_record_history_time_rate_firewall_2026_06_05.txt).

**Local support inputs:**

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

## 2026-06-17 source-boundary repair

This row is not a positive time/rate theorem. Its source payload is negative
route pruning: post-record word/count order and any supplied per-step kernel do
not determine a physical time metric, continuous-time generator, transition
rate, or clock normalization. A later dynamics theorem may still supply those
bridges; this row only prevents downstream notes from importing them from
record-history order alone.

The abstract word and optional per-step kernel are quantified theorem inputs,
not positive conclusions imported from another row. This row is not a
production theorem and does not turn those inputs into formation dynamics.

## 2026-07-16 causal-source scope split

The object in this note is a **supplied abstract word/order**, not a causal
event set. This row does not construct a map from a site-tagged record atom to
a formation event, does not supply a formation-successor relation, and does
not identify prefix order with the causal or chronological order used by a
light-cone theorem. It must not be consumed as a positive causal-order input.

Those are separate positive bridges. The current
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) says that
records form and are permanent, but leaves the formation rule,
record-production dynamics, time metric, and dependency structure outside the
axiom content.

## Question

Given a supplied abstract finite record word/order, do its order and counts
determine physical time, rates, or a clock normalization?

No. A record history supplies ordered words and counts. A supplied instrument
kernel supplies probabilities per admitted step. A physical time metric or
transition rate requires an additional clock/production normalization.

The useful typed surface is:

```text
supplied abstract word w in O*
  -> order/length/counts
  -> optional supplied step kernel P
  -> probabilities per step
  -> requires clock map n |-> t_n for physical rates.
```

## Supplied abstract-word surface

Given the supplied word, the abstract word algebra gives:

- append one supplied word atom;
- extend a finite word;
- update integral counts;
- preserve prefix/order structure;
- allow arbitrarily long finite histories without a fixed finite cap.

It does not attach a metric to the step index. The same word and the same
per-step kernel can be embedded in many increasing time grids. Counts and word
order are unchanged, while rates per unit time change.

Likewise, a one-step transition probability `q` does not determine a unique
continuous-time rate. For a Poisson-style event,

```text
q = 1 - exp(-lambda dt)
```

only the product `lambda dt` is fixed by the one-step probability. Without
`dt`, the rate `lambda` is open.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| history length is physical time | pruned | the same word admits multiple time grids |
| record count divided by step count is a physical rate | pruned | rates per unit time depend on the clock map |
| a step kernel determines a continuous-time generator | pruned | generator estimates scale with the chosen step duration |
| unbounded retention supplies unlimited metric duration | pruned | arbitrarily long finite histories are not a metric-time theorem |
| arrow/order supplies clock normalization | pruned | record order can orient a history while leaving interval lengths open |

These are route-specific prunings. They do not say a future dynamics/clock
theorem is impossible.

## What remains open

- A physical clock map from record-step index to time values.
- A production law or measurement Hamiltonian that fixes step duration.
- A continuous-time generator or rate normalization.
- Decoherence/formation dynamics beyond the supplied instrument/kernel surface.
- Cosmological or thermodynamic boundary conditions for a global arrow.

## What this unlocks

- Audit rows can cite this row only for the negative timing/rate boundary over
  a supplied abstract word; it grants no causal-order premise.
- Dynamics rows can separate "per-step transition kernel" from
  "continuous-time generator."
- Causal-order consumers must add a typed record-atom-to-formation-event map
  and a supplied or derived dependency order on the same event set as their
  cone relation.
- Production lanes can state exactly what they must add: a formation process
  and a clocked dynamics, not another abstract word/count identity.

## Boundaries

- Does not derive physical time, rates, a clock, a generator, a measurement
  Hamiltonian, or record production.
- Does not derive record atoms as formation events, a formation-successor
  relation, spacelike incomparability, causal order, chronological order, or
  compatibility with a light-cone event set.
- Does not claim unlimited metric duration from unbounded finite histories.
- Does not select a generation/Koide dial setting.
- Does not apply audit verdicts.

## Runner summary

The runner verifies:

- append/count/prefix order on finite record words;
- arbitrary finite extension without a fixed cap;
- the same word embedded in different time grids has the same order/counts but
  different rates;
- the same per-step Markov kernel admits different step durations and different
  generator/rate normalizations;
- the same one-step event probability is compatible with different
  `(lambda, dt)` pairs;
- the source note keeps clock/rate/selector residuals explicit.
- the source note forbids positive causal-order use of this negative row.

Expected result:

```text
SCORECARD PASS=49 FAIL=0
```

## Claim boundary

- Claim id:
  `record_history_order_time_rate_firewall_2026-06-05`.
- Trace class: negative route pruning.
- Reachability: prunes imports from exact order/count/per-step-kernel facts to
  physical time, rate, generator, clock, or metric-duration closure.
- This source note makes no retained-status proposal and does not use bare
  retained language.
