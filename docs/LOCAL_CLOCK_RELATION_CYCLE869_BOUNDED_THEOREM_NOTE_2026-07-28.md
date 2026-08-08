# The local-clock relation at B=3: a bounded finite-corpus measurement — within-key dictionaries sparse in the declared family, exact within-class cross-key time translations — Cycle 869

Date: 2026-08-03 (revised 2026-08-08, review-loop iteration 1; see Review
record)

Authority: none

Audit: unset

Status: bounded finite-corpus measurement, demoted from its original
headline by adversarial review (one worker-authored primary and one
independent checker spec'd to refute, which forced three real corrections
mid-cycle; no axiom surface touched).  Campaign/queue identifiers appear
only under Provenance context below and carry no naming weight.

Claim type: bounded_theorem (narrowed finite-corpus statements only; the
live surface is bounded-support and every claim is conditional on the
unaudited Cycle-719 substrate named under Imports)

Runners:

- [`frontier_cycle869_clock_relation_2026_07_28.py`](../scripts/frontier_cycle869_clock_relation_2026_07_28.py)
- [`frontier_cycle869_relation_independent_check_2026_07_28.py`](../scripts/frontier_cycle869_relation_independent_check_2026_07_28.py)

Both runners are co-load-bearing: the keyed-equality replication and the
period adjudication live in the independent checker, so no audit packet for
this note is complete without it (see Review record).

Receipt:

- [`local_clock_relation_cycle869_receipt_2026_07_28.json`](../outputs/local_clock_relation_cycle869_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted 2026-08-03; substitution disclosed in the
campaign state file); supervisor review of the family grammar, the
substantive/identity-like discriminators, the across-key edge
construction, and both caches. Checker independence is cross-context,
not cross-model. Independent audit still required.

## The question and the measured answer

Is there an exact dictionary, inside a declared transformation family,
carrying one bank-pair clock's cadence onto another's — within a key and
across keys — on the B=3 corpus (304 keys, 912 pair clocks, horizon 8,192)?

**Within a key, across bank pairs: the declared family is exhausted at its
declared caps — a priced, family-scoped negative with measured exceptions.**
Over the declared family (constant time offset, alias F1; windowed time
offset, F1W; tick affine, F2A; index affine, F2B; index lag plus offset,
F3; partial lag overlap, F3P, with a 1/2 coverage floor; periodic residue
law, F4), searched to declared caps with every witness re-verified against
the member's complete definition: of 646 comparable pairs-of-pair-clocks,
480 are substantive, and of those 429 admit no witness in the family;
13 admit a whole-cadence dictionary, of which 12 are identity-like
containments (c=0 / d=0 / s=1: one clock a literal sub-run of the other at
the same absolute times) and exactly **1** moves the tick values; the
partial member matches a further 38 on at least half a clock, 31 of them
non-identity. Single-bank clocks: 1/831. This is a negative priced to the
family and its caps, with the 13 dictionaries and 31 non-identity partial
witnesses stated up front — it is NOT a universal untranslatability or
"no dictionary" claim, and the emitted closure line prices it explicitly.

**Across keys at a fixed bank pair: exact time translations inside observed
equal-gap-word classes.** The runner first buckets sounding clocks by exact
gap-word equality and then verifies constant-offset edges only within those
buckets (equal finite gap words plus equal length already imply a constant
offset, by finite-list algebra). Measured occupancy: 685 of 777 sounding
pair clocks fall in a nontrivial equal-gap-word class; the 632 edges from
class members to their class representatives all carry a nonzero offset
(79/63/16 distinct offsets per bank pair, range −910…+1215; per-pair edges
140/258/234, checker-replicated); the remaining 92 sounding clocks are
singletons with no in-family translation partner anywhere in this corpus.
This is a within-class verification over the observed class occupancy —
not a universal cross-key dictionary, and no claim is made that every
cross-key clock has a translation partner.

**Structure found on the way:** of the 912 pair clocks, 713 are strictly
joint (gated by neither bank alone), 62 are one bank's clock outright, 2
are identical to both banks at once, and 135 are silent (713+62+2+135 =
912). Every detector-selected nondegenerate period (19, 114, 1444 ticks)
is a whole number of 19-station orbits — 1444 = 4·19². These are the
declared tail-ladder detector's selections, not least periods: the
review's direct-membership probe found proper-divisor support (361, 722,
19) beneath some listed rows, so only the divisibility arithmetic is
claimed, never a least-period or only-period statement.

## The checker's teeth (three corrections forced mid-cycle)

The checker (own substrate rebuild — corpus sha equal; full-horizon
replay through the Cycle-719 controller on 12 keys, zero mismatches;
claim replication; a complementary bounded loosened-cap re-search) forced
three repairs, preserved in the commit trail:

1. saturation was being inferred from a transient ladder — now exact
   and cap-free;
2. the period search's tail window hid the 19- and 114-tick periods —
   now a 3/4 ladder;
3. partial-overlap matches had no declared family member — now the
   partial-lag member with a 1/2 coverage floor, reported as partial,
   never as a dictionary.

After hardening, the checker's re-search finds substantive non-identity
relations on exactly the same 32 keyed pairs the primary publishes, and
the gate is EXACT KEYED WITNESS-SET EQUALITY (published key list against
found key list), not count equality. The re-search is complementary
bounded coverage, not a proven superset of the primary's search: its
period transient scan is capped while the primary's tail-ladder pushback
is uncapped, so period disagreements are adjudicated by direct membership
instead. Every period claim survives that direct membership adjudication.

## Negative-claim discipline

The within-key negative is scoped to the declared family, its declared
parameter ranges, and its declared caps (all emitted); the closure line
states it is "a negative priced to F and its caps, not a claim about all
conceivable transformations." The measured partial closure — 13
whole-cadence dictionaries (1 tick-moving) and 31 non-identity partial
witnesses — leads the statement rather than being suppressed. Thin
comparisons (shorter clock < 8 events) are excluded from the headline and
reported separately. No claim is made beyond the B=3 probe scope (events
{0,1}, k=2, horizon 8,192, store caps declared), and the terminal PASS
marker of the primary certifies measurement integrity only, not a theorem
outcome.

## Interpretation (meta, non-load-bearing)

One may read the within-class constant-offset identity as "the same
cadence started at a different moment," and the contrast with the sparse
within-key dictionaries as a symmetry between STARTING CONDITIONS rather
than between local clocks. This reading is labeling, not a derived
result: the runners do not derive that two keyed initial states are
physically "the same clock," nor any symmetry acting on the initial-state
space — they compare observed cadence lists. Nothing downstream may
load-bear on this paragraph, and it must not be cited as a theorem.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "is there a lawful inter-clock relation at B=3/4? (owner goal queue provenance; motivated by the unlanded fragmentation exploration referred to as Cycle 866)"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "feed the within-class cross-key time-translation measurement to the second leg of the bank-count axis (record-time laws across worlds) and test whether it survives B=4; the within-key negative prices the local-clocks route at its declared caps"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact witness-verified searches over a declared closed family at declared caps on one finite corpus; the within-class constant-offset edges gated by keyed witness-set equality against an independent rebuild; the negative priced to the family; all of it conditional on the unaudited Cycle-719 substrate"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, declared scope, provenance, derived, open

### Imports (load-bearing)

- the Cycle-719 two-rail recurrent controller core
  ([`frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py`](../scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py);
  sha-pinned by both runners; the only declared repository input), whose
  source authority is
  [`RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md`](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md).
  That note is landed byte-identical on the main line but its audit ledger
  row is currently `unaudited`; every result here is therefore CONDITIONAL
  on that upstream chain and support-only until it is independently
  retained.

### Declared scope inputs (stipulated boundary choices, not derived)

- B=3 fixture banks, 19 stations, horizon 8,192 chunks, the event-seeded
  k=2 census (304 keys), the cadence store cap, the eight-event evidence
  floor, the 1/2 partial-coverage floor, and every family/search cap
  emitted in the pricing block. These are normalizations; all claims are
  conditional on them.

### Provenance context (non-load-bearing)

- the fragmentation exploration referred to as Cycle 866: no landed
  artifact exists on origin/main; it is motivation only, carries no
  authority, and nothing here executes or inherits it;
- owner campaign/queue identifiers (goal-queue item, PR branch): work
  provenance only, never scientific names.

### Derived (on this corpus, conditional on the imports above)

- the within-key family exhaustion with the substantive/identity-like
  split (429 no-witness / 12 identity-like / 1 tick-moving of 480
  substantive; 38 partial, 31 non-identity);
- the within-class cross-key constant-offset verification (685/777
  sounding clocks in nontrivial classes; 632 representative edges, all
  nonzero; 92 singletons);
- the joint-clock census (713/62/2/135) and the orbit-multiple
  divisibility of every detector-selected period.

### Open

- does the within-class translation structure survive B=4?
- is the orbit-multiple divisibility of detected periods forced, or a
  B=3 accident? (a least-period census would need a stronger detector
  contract than either runner declares)
- do the 92 singleton clocks acquire partners on a longer horizon or a
  wider family?
- the second leg of the bank-count axis (record-time laws across worlds;
  this measurement supplies its cross-world leg).

## Review record (iteration 1, Sol, 2026-08-08 — FIX_THEN_PROCEED)

An adversarial review demoted this package from its original headline
("no within-key dictionary, an exact cross-key time translation") to the
bounded finite-corpus measurement stated above. The universal negative
contradicted the note's own 13 measured dictionaries and 1 tick-moving
witness, and the universal cross-key reading contradicted the runner's own
92 singleton clocks; the original headline and any earlier no-go-style
checklist for it must not be cited as a passed gate. Fixes applied in this
iteration: the checker now gates keyed witness-set equality instead of
count equality; the checker's search is labeled complementary bounded, not
strictly wider; the windowed-offset verifier enforces the whole-target
window and every member's verifier enforces its complete definition; all
seven family members carry positive controls; the period contract is
detector-selection, not least-period; the terminal marker is relabeled
measurement-only; the Cycle-719 authority edge is linked and the Cycle-866
lineage is provenance-only; the physical "same clock" reading is split
into the non-load-bearing interpretation section above. Outstanding at
landing (outside this PR's frozen file set): register the independent
checker as a claim-scoped helper for this note's audit packet (the
citation-graph builder's explicit packet-helper table) and co-land the
citation-graph manifest acknowledgment for this note's node; do not spend
an audit seat on this row before both are done and the Cycle-719 chain is
independently retained.

## Verdict

On this finite corpus the declared family yields almost no within-key
dictionaries (1 tick-moving of 480 substantive comparisons, priced to the
family and its caps), while inside the observed equal-gap-word classes
every representative cross-key edge is an exact nonzero time translation
(632 edges over 685 of 777 sounding clocks; 92 singletons remain
unrelated). Every detector-selected period is a whole number of the
substrate's 19-station orbits. These are bounded measurements conditional
on an unaudited upstream substrate; independent audit is still required,
and no universal or physical-symmetry claim is made.
