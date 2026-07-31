# Two dead wires and the even-toggle mechanism — Cycle 853

Date: 2026-07-31

Authority: none

Audit: unset

Status: bounded worked result (the violating-pattern usage census; the
single-wire blocking localization; the checker-closed even-toggle
mechanism with its boundary-granularity scope)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle853_generator_usage_census_2026_07_28.py`](../scripts/frontier_cycle853_generator_usage_census_2026_07_28.py)
- [`frontier_cycle853_usage_independent_check_2026_07_28.py`](../scripts/frontier_cycle853_usage_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 851 left a mystery: the family conserves four parities the rule
does not force. This cycle explains it, level by level, down to the
rule structure:

- **the usage census is exact**: the 4 parity-violating generator
  patterns (extracted independently from the 851-v2 counterexamples
  by both runners) occurred **0 times** across all 891,486 landed
  transitions;
- **blocking localizes at single-wire granularity** (the smallest
  declared level): P1/P2/P3 require `x[56]=1`, P4 requires
  `x[58]=1` — and the full reachable census (**891,513 states**,
  rebuilt independently by the checker) contains **no state with
  wire 56 or 58 lit**;
- **the recursion closes** (the checker's probe): every generator
  touching wires 56/58 toggles each an EVEN number of times — four
  cancelling X toggles per wire — so from the initial value 0 the
  wires return to 0 at every generator boundary, forever;
- **the honest scope limit**: primitive microstates INSIDE a
  generator's execution do light the wires transiently; the dead-wire
  law, and therefore the whole chain, is a generator-BOUNDARY law —
  exactly the granularity at which the family's transitions, records,
  and censuses are defined.

**The closed chain**: initial condition (wires 56/58 at 0) + even
toggle structure of the generators → dead wires at all boundaries →
violating patterns never enabled → HEAD[1]⊕HEAD[j] conserved
(j = 2..5) → S0' unreachable. The Cycle-851 "spontaneous"
conservation is not spontaneous: it is initial-condition-inherited,
with the inheritance mechanism now derived and certified. The rule's
abstract counterexamples live precisely in the states the initial
condition can never hand to a boundary.

## Supplied / derived / open

### Supplied

- the 851 package (sha-pinned; its counterexamples are the pattern
  source); the 719 core; everything the cited packages declare.

### Derived

- the pattern family and its precondition structure (both runners,
  independently); the zero-usage census; the full reachable census
  with the two dead wires; the even-toggle closure at generator
  boundaries with its scope limit.

### Open

- the braid's why (the merged why proper — untouched by this face);
  whether other landed "spontaneous" regularities (the braid clauses,
  the cohort synchrony) admit the same initial-condition-inheritance
  shape — a named candidate mechanism now exists.

## Negative-claim discipline

Zero-usage and dead-wire claims are exhaustive over the landed
family's boundary-level census (891,513 states / 891,486
transitions), never sampled; the even-toggle closure is per-generator
structural; the microstate flicker is disclosed as an explicit scope
limit, not hidden.

## Verdict

The family is not more lawful than its rules after all — it is
exactly as lawful as its birth. Two wires started dark; every move
the universe can make puts them back before anyone can look; and
four conservation laws and one forbidden state follow as bookkeeping.
This is the campaign's cleanest complete mechanism: a why answered
all the way down, with its one honest boundary drawn. Independent
audit still required.
