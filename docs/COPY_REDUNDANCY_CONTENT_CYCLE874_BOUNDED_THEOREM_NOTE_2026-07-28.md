# Copy redundancy does not protect record content — and the contrast was firing all along — Cycle 874

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked result (one worker-authored primary and one
independent checker spec'd to refute; owner-directed campaign-5 wave 2,
queue item 2b as reframed by the blockP25 finale; no axiom surface
touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle874_copy_redundancy_content_2026_07_28.py`](../scripts/frontier_cycle874_copy_redundancy_content_2026_07_28.py)
- [`frontier_cycle874_redundancy_independent_check_2026_07_28.py`](../scripts/frontier_cycle874_redundancy_independent_check_2026_07_28.py)

Receipt:

- [`copy_redundancy_content_cycle874_receipt_2026_07_28.json`](../outputs/copy_redundancy_content_cycle874_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

Worker disclosure: authored by a Claude Opus 5 worker under supervisor
spec (codex quota exhausted 2026-08-03; substitution disclosed).
Independent audit still required.

## The instrument

Record CONTENT becomes a real 32-bit word over the live payload
projection, written into R disjoint structurally-dead slot groups
(R in {1,2,3}; 321 slots, zero pairwise overlaps, zero gate
inputs/targets, zero dead-activation conflicts) and READ BACK from the
mutated state (0 readback-vs-host mismatches). Every pinned 867-v3
number reproduces exactly (pool 5,668/5,270; moment-exact 164/164;
748 existence lanes; all four locality cells) — the extension is
conservative over the landed model.

## Result 1 — the scoped negative: R does nothing

Across R = 1 → 3, in BOTH declared modes (replicated copies;
staggered copies written at different clean edges — a genuine second
channel, register agreement only 115/157 lanes at R=3): **zero of
eight majority-readback cells change**, and the restore-class near/far
contrast is FLAT in R (0.09375 replicated, 0.107143 staggered, at
every R). Under perturbation, all copies corrupt together. The
checker attacked the null with a deliberately different slot
allocation and a 4x-wider deep-staggered scheme (clean edges 1/5/9):
still no R-gain. Copy redundancy, as whole-state content replication,
is priced out.

## Result 2 — the decomposition: the contrast is firing, not content

The blockP25 finale reported the restore-class cells
(near 32/32/32 vs far 32/29/29) as a near/far content-preservation
contrast. The cells are exact and unchanged; their READING sharpens
here: `content_gap_given_fired = 0.0` exactly, both modes — **whenever
a restore fires, content always survives, near and far alike**. The
entire contrast is a FIRING gap (0.09375 / 0.107143): three far
restores fail to fire (a transient far perturbation can leave a
permanent trace in the dynamics), and no fired restore ever corrupts
content. Locality in this model lives in whether formation happens,
never in what gets written once it does.

## Result 3 — the lever, found constructively

The checker's harder-redundancy attack included projection-SHARDED
content — each copy digesting a DIFFERENT state block rather than the
whole state. Sharding does not change the majority-readback verdict
(the negative above stands), but it leaves **a surviving shard under
every direct-flip class**: `any_copy_survives_at_R3 = 1.0` for
one_flip, late_acting, and untouched_in_chunk, both sides. Content
fragility is therefore a property of digesting the WHOLE state at
formation, not of the formation event: block-local record content is
the lever that whole-state copy redundancy is not. Named successor:
the sharded-content block (certify shard survival and reconstruction
as the primary object).

## Negative-claim discipline (compact)

The negative is scoped to: majority readback of whole-state content
digests, R <= 3, the two declared modes plus the checker's
deep-staggered scheme, the declared perturbation classes and sample.
The live route out (sharding) was FOUND by this block's own checker
and is named as the successor, not suppressed. Thin cells and caps
are disclosed in the emitted payloads.

## Trace gate

```yaml
trace_class: negative_route_pruning
target_claim_id: null
target_blocker_text: "robust formation via copy redundancy (867's hypersensitivity names the suspect) — campaign GOAL queue 2b, as reframed by blockP25 to content robustness"
source_of_blocker_text: user_goal
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "whole-state copy redundancy is priced out; the successor is sharded (block-local) record content — certify shard survival and reconstruction; separately, the firing/content decomposition feeds the B-AXIS and formation lanes"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite certificates; the R-invariance and the firing/content decomposition are emitted as computed cells; the checker replicated with a different allocator and wider schemes, zero refutations"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel and 863 machinery (as the landed model imports them);
- the 867-v3 composed model and its locality cells (sha-pinned,
  reproduced exactly before extension).

### Derived

- the R-invariance of majority readback (both modes, plus the
  checker's harder schemes);
- the firing-not-content decomposition of the restore contrast;
- the shard-survival finding and the whole-state-digestion diagnosis.

### Open

- the sharded-content successor block (survival + reconstruction);
- whether the firing-gap path-dependence scales with B.

## Verdict

Redundancy was the named suspect for rescuing fragile records, and the
toy dismissed it: copies of the whole state die together, at every R,
in every mode tried. What the block found instead is better — content
never dies in a record that forms (the contrast was firing all along),
and content survives even direct flips the moment each copy stops
trying to remember everything. The record wants to be local.
Independent audit still required.
