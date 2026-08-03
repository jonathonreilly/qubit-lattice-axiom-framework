# The local-clock relation: no within-key dictionary, an exact cross-key time translation — Cycle 869

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute, which forced three real
corrections mid-cycle; owner-directed campaign-5 wave 1; no axiom
surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle869_clock_relation_2026_07_28.py`](../scripts/frontier_cycle869_clock_relation_2026_07_28.py)
- [`frontier_cycle869_relation_independent_check_2026_07_28.py`](../scripts/frontier_cycle869_relation_independent_check_2026_07_28.py)

Receipt:

- [`local_clock_relation_cycle869_receipt_2026_07_28.json`](../outputs/local_clock_relation_cycle869_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted 2026-08-03; substitution disclosed in the
campaign STATE); supervisor review of the family grammar, the
substantive/identity-like discriminators, the across-key edge
construction, and both caches. Checker independence is cross-context,
not cross-model. Independent audit still required.

## The question and the two-sided answer

Cycle 866 found that at B=3 the bank-pair sync cadences fully fragment
— every pair its own signature — and no global record-time exists. The
question here: is there a LAWFUL RELATION between the local pair-clocks
— an exact dictionary mapping one cadence to another?

**Within a key, across bank pairs: the declared family is exhausted —
a priced negative.** Over the declared transformation family
(F1 constant offset; F1W windowed offset; F2A tick-affine; F2B
index-affine; F3 index-lag-plus-offset; F3P partial-lag with a 1/2
coverage floor; F4 periodic tiling), searched to declared caps with
every witness re-verified exactly: of 646 comparable pairs-of-pair-
clocks, 13/480 substantive comparisons admit any whole-cadence
dictionary, and exactly **1** moves the tick values — the rest are
c=0 / d=0 / s=1 containments (one clock a literal sub-run of the
other at the same absolute times), classified as coincidence, not
transformation law. Single-bank clocks: 1/831. The negative is priced
to F and its caps, stated as such in the emitted closure line.

**Across keys at a fixed bank pair: an exact time-translation
dictionary.** Bucketing clocks by their gap word: **632 of 632**
constant-offset edges to class representatives carry a nonzero offset
(79/63/16 distinct offsets per bank pair, range −910…+1215; per-pair
edges 140/258/234, checker-replicated). Same cadence, different
origin. The toy's "relativity" at this scope is a symmetry between
STARTING CONDITIONS, not between local clocks: within one world the
clocks are mutually untranslatable, while the same clock across worlds
is a pure time translation.

**Structure found on the way:** 713/912 pair clocks are strictly joint
(gated by neither bank alone); 62 are one bank's clock outright; 135
silent. Every nondegenerate period found (19, 114, 1444 ticks) is a
whole number of 19-station orbits — 1444 = 4·19².

## The checker's teeth (three corrections forced mid-cycle)

The checker (own substrate rebuild — corpus sha equal; full-horizon
replay through the 719 controller on 12 keys, zero mismatches; claim
replication; wider-parameter refutation search) forced three repairs,
preserved in the commit trail:

1. saturation was being inferred from a transient ladder — now exact
   and cap-free;
2. the period search's tail window hid the 19- and 114-tick periods —
   now a 3/4 ladder;
3. partial-overlap matches had no declared family member — now F3P
   with a 1/2 coverage floor, reported as partial, never as a
   dictionary.

After hardening, the checker's wider search finds exactly the 32
substantive non-identity relations the primary publishes, and every
period claim survives direct membership adjudication.

## Negative-claim discipline

The within-key negative is scoped to the declared family F, its
declared parameter ranges, and its declared caps (all emitted); the
closure line states it is "a negative priced to F and its caps, not a
claim about all conceivable transformations." Thin comparisons (shorter
clock < 8 events) are excluded from the headline and reported
separately. No claim is made beyond the B=3 probe scope (events {0,1},
k=2, horizon 8,192, store caps declared).

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "is there a lawful inter-clock relation at B=3/4? (campaign GOAL queue 2a; the fragmented cadences of Cycle 866)"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "the cross-key time-translation law is the found structure — feed it to the B-AXIS second leg (record-time laws across worlds) and test whether it survives B=4; the within-key negative prices the local-clocks route"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact witness-verified searches over a declared closed family at declared caps; the positive law replicated edge-for-edge by an independent rebuild; the negative priced to the family"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel (sha-pinned; the only declared repo input);
- the 866-lineage probe scope (declared, re-derived, not imported).

### Derived

- the within-key family exhaustion with the substantive/identity-like
  split;
- the cross-key time-translation dictionary (632/632 nonzero);
- the joint-clock census and the orbit-multiple period law.

### Open

- does the cross-key translation law survive B=4?
- is the orbit-multiple period law (all periods = multiples of 19)
  forced, or a B=3 accident?
- the B-AXIS second leg (this block supplies its cross-world leg).

## Verdict

Asked for relativity between its local clocks, the toy refused — and
then volunteered a better symmetry: within a world the fragmented
clocks share no dictionary at all, but across worlds every clock is
the same clock started at a different moment. Time translation between
initial conditions is exactly the lawful relation the fragmentation
left room for, and every period the substrate exhibits is a whole
number of its own orbits. Independent audit still required.
