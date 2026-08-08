# The conflict has a name — source, finalizer, and the phase that will not close — Cycle 811

Date: 2026-07-30

Authority: none

Audit: unset

Status: bounded worked result (the W2 boundary-0 mechanism derived from
the rules; necessity and the exact sufficiency split)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle811_w2_mechanism_2026_07_28.py`](../scripts/frontier_cycle811_w2_mechanism_2026_07_28.py)
- [`frontier_cycle811_mechanism_independent_check_2026_07_28.py`](../scripts/frontier_cycle811_mechanism_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Result up front

Cycle 810 found the separator (a source-kind left row) and the failure
point (boundary 0, all ten dead starts). This cycle derives the
MECHANISM from the transition rules:

- **the named conflict: `SOURCE_FINALIZER_PHASE_CLOSURE_CONFLICT`** —
  for starts 1-9, the rule chain forces `source_compute_word` to
  execute at boundary (11 - start), AFTER the last finalizer has run,
  leaving emission registers uncleared — the cleanliness phase cannot
  close; for start 10, `source_finalizer_word` at boundary 10 leaves
  every continuation non-clean. Each step of the trace carries rule
  provenance;
- **verified 20/20**: all ten dead starts, both boundary-0 orders —
  exact traces to the dead end, zero completions; start 0 passes
  exactly at the viability point (512 successes);
- **the sufficiency split is exact**: the source row is NECESSARY and
  existentially sufficient on this battery (start 0 succeeds), but
  NOT pathwise sufficient — 1,536 of start 0's 2,048 assignments
  still fail, and the checker localized every one of those failures
  to boundaries 0 and 10 (the downstream order conditions, now
  named);
- **the checker confirmed everything** (0.04 s, five certificates):
  independent rule implementation, all 20 traces, the 512 count, the
  failure localization — and a diagnostic counterfactual surgery
  (clearing the emission registers at the conflict point) removes the
  immediate obstruction, validating the mechanism's naming.

**What this does to W2**: the wall's full story is now
ceiling → discriminator → mechanism, all rule-derived: the battery
demands a source-kind left row because only a source can run its
compute word before the finalizer phase closes; everything else about
ordering is either free (the 512) or dies at two named boundaries.

## Supplied / derived / open

### Supplied

- the Cycle-752 fixture battery and rules (reimplemented,
  provenance-cited); everything the 752/783/806/810 packages declare.

### Derived

- the traced rule chains with the boundary formula; the 20/20
  verification; the sufficiency split with failure localization; the
  counterfactual diagnostic.

### Open

- what the source/finalizer phase structure means beyond this fixture
  family (the physical reading feeds the eventual W2 resolution);
  fixture families beyond 752.

## Negative-claim discipline

The mechanism is scoped to the Cycle-752 battery under its landed
rules; the counterfactual surgery is a checker diagnostic, not a
physics claim; no claim attaches to other fixture families.

## Verdict

The wall that began as "no order works" ends as one sentence about
the rules: the source must speak before the finalizer closes the
phase, and at ten of eleven starts it cannot. Independent audit still
required.
