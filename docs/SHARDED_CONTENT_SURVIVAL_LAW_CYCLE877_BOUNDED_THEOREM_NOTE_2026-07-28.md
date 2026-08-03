# The survival law is one wire: sharded record content and its exact cost — Cycle 877

Date: 2026-08-04

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed campaign-5, the
blockF1 successor; no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle877_sharded_content_2026_07_28.py`](../scripts/frontier_cycle877_sharded_content_2026_07_28.py)
- [`frontier_cycle877_sharding_independent_check_2026_07_28.py`](../scripts/frontier_cycle877_sharding_independent_check_2026_07_28.py)

Receipt:

- [`sharded_content_survival_cycle877_receipt_2026_07_28.json`](../outputs/sharded_content_survival_cycle877_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted 2026-08-03; substitution disclosed).
Independent audit still required.

## The instrument

The live payload projection is 147 wires of the 5,815-wire state
(5,668 dead); S shard groups (S in {2, 4, 8}, blocks derived from the
state layout and disclosed) digest into 577 disjoint structurally
inert slots of the 5,270-wire safe pool; register readback matches the
independently walked trajectory 448/448; every 867/874 pool,
annotation, and locality cell reproduces before extension.

## Result 1 — the survival law is maximally local

On EVERY direct-flip class, the damage set at the formation edge is
EXACTLY ONE WIRE — the flipped wire itself (mean = min = max = 1.0) —
although the monotone structural forward cone would permit up to 295.
Exactly one shard dies at every S, and it is always the flip's own
shard: confined-to-flip-shard = 1.0 across all 18 direct cells, zero
no-survivor cells. Verdict: LOCAL. **The "content hypersensitivity"
of Cycles 867/874 was a one-wire difference amplified by a whole-state
digest** — the damage was always minimal; the instrument made it look
global.

## Result 2 — reconstruction and its exact curve

Full content is never reconstructible under a direct flip at any S
(the flipped shard always dies): 0.0 everywhere, honestly reported.
The RECOVERED payload fraction climbs 0.50 → 0.75 → 0.877 for
S = 2 → 4 → 8, with no saturation at 8 — each doubling halves the
loss toward 1 − 1/147 = 0.9932, reached only at S = 147 (one shard
per wire).

## Result 3 — the trade, exactly

S = 8 costs 385 slots (7.3% of the safe pool); saturation costs 4,833
(91.7%). The pool admits S ≤ 160, so PAYLOAD GRANULARITY binds before
the slot budget does.

## Result 4 — the boundary tail, and a design rule

The checker's exhaustive 768-probe boundary sweep (all 16
block-boundary wires included) found 719 of 720 firing flips damage
exactly one wire. The single outlier is a 10-wire-damage flip where
allocation rules split: SCATTERED shard boundaries let it reach every
shard, while CONTIGUOUS blocks confine it to 3 of 8 shards and never
lose all — **contiguity buys tail protection that scattering
destroys.** Adjacent adversarial fact: defeating sharding requires k
placed flips in k distinct shards, which fire only 0.306 of the time
and then kill exactly k shards — the attack pays a 70%
formation-suppression penalty.

## Checker

Different allocator (far-end reversed), arithmetic rank-map
boundaries, plus two shard rules the primary never builds (strided,
hash-scattered); the entire incidence matrix reproduces cell-for-cell;
cone-containment, cone-prediction, and digest-vs-bits failures all
zero; the boundary attack could not break the one-wire law on any
rule. 5/5 PASS, zero refutations.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "content fragility is a property of digesting the WHOLE state at formation, not of the formation event (blockF1's diagnosis); certify shard survival and reconstruction"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the record-locality story is closed at this scope: one-wire damage, shard-local death, exact recovery curve, contiguity design rule; the formation lane's remaining opens are the firing-gap path-dependence at scale and the B=4 legs"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact incidence matrices at declared classes and shard counts; the one-wire law checked against the structural cone and an exhaustive boundary sweep; recovery and cost curves exact; checker reproduces cell-for-cell under different allocators and rules"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel, 863 machinery, and the 867-v3/874 instruments
  (sha-pinned, reproduced before extension).

### Derived

- the one-wire survival law and its shard-locality;
- the reconstruction curve and the 1 − 1/147 asymptote;
- the cost curve and the S ≤ 160 pool bound;
- the boundary outlier and the contiguity design rule;
- the k-flip adversarial cost with its formation-suppression penalty.

### Open

- the firing-gap path-dependence at scale (B=4);
- shard-aware readout conventions, if the lane ever wants them — a
  design question, not a physics gap.

## Verdict

Chased through three blocks, the fragility of record content turns out
to have been one wire the whole time — the one that was flipped — made
to look catastrophic by an instrument that digested everything at
once. Sharding does not defeat perturbation; it prices it: lose
exactly the shard you touched, keep the rest, and the curve to
near-perfect recovery is a halving law with its endpoint at one shard
per wire. Even the exception obeys a rule worth keeping: keep your
blocks contiguous. Independent audit still required.
