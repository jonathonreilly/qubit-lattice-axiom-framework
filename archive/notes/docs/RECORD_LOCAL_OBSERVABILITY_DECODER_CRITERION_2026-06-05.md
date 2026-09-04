---
claim_id: record_local_observability_decoder_criterion_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Local-Observability Decoder Criterion

**Date:** 2026-06-05
**Claim type:** bounded_theorem — bounded support map and exact finite decoder criterion.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_local_observability_decoder_criterion_2026_06_05.py`](../scripts/frontier_record_local_observability_decoder_criterion_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_local_observability_decoder_criterion_2026_06_05.txt`](../logs/runner-cache/frontier_record_local_observability_decoder_criterion_2026_06_05.txt).

**Local support inputs:**

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md`](DARWINISM_BRIDGE_RESIDUAL_LOCAL_OBSERVABILITY_OPEN_GATE_NOTE_2026-06-05.md)
- [`RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md`](RECORD_PRODUCTION_RESIDUAL_CHECKLIST_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)
- [`RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md`](RECORD_INSTRUMENT_KERNEL_INTERFACE_2026-06-05.md)

## Purpose

The Darwinism bridge residual says local observability is open. This note gives
the finite audit criterion for that bridge:

```text
for every disjoint fragment F_i, there is a local decoder d_i
such that d_i(F_i(record value o)) = o for every produced value o,
and all decoders agree.
```

That is the finite meaning of "each local observer can recover the same
determined record value." It is stronger than global determinacy and weaker
than a physical derivation of the broadcast dynamics.

## Result

For a finite produced-record alphabet `O` encoded into disjoint fragment labels,
local observability is exactly the existence of a compatible family of local
decoders:

```text
d_i : fragment_i_labels -> O
```

for all fragments `i`, with `d_i(label_i(o)) = o` for every `o in O`.

The runner verifies:

- broadcast codewords such as `{0000, 1111}` have local decoders on every
  fragment;
- single-register storage has a global decoder but fails all non-register
  fragments;
- parity/global encodings can have a determined global value while every single
  fragment is ambiguous;
- if fine local decoders exist, coarse local decoders are obtained by composing
  with the coarse-graining map.

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| determined global value implies local observability | pruned | global decoder can exist while local decoders fail |
| single durable register implies objective broadcast | pruned | non-register fragments have no value decoder |
| parity record implies local observability | pruned | each single fragment is ambiguous |
| local observability fixes probability weights | pruned | decoder existence is a support/readability fact, not a weight law |
| local observability supplies rates | pruned | clock/rate normalization remains separate |

These are route-specific prunings. They do not block a future theorem from
supplying the local decoder family.

## What remains open

- A physical mechanism that writes a produced record into locally decodable
  disjoint fragments.
- A proof that the framework dynamics supplies such decoders.
- Probabilities/weights over values.
- Clock/rate normalization.
- Measurement Hamiltonian and production law.

## What this unlocks

- Audit rows can require an explicit local-decoder family when claiming
  local/objective records.
- Darwinism-style arguments can separate global determinacy from local
  readability.
- Coarse-grained record claims can inherit local observability from a finer
  locally observable code without re-proving the physical production step.

## Boundaries

- Does not derive local observability from the three axioms.
- Does not derive broadcast dynamics, production, probabilities, rates, a clock,
  or a measurement Hamiltonian.
- Does not select a generation/Koide dial setting.
- Does not apply audit verdicts.

## Runner summary

The runner verifies finite decoder existence/nonexistence for broadcast,
single-register, and parity/global encodings; checks agreement of all local
decoders in the broadcast case; and verifies coarse-graining composition for a
fine locally observable code.

Expected result:

```text
SCORECARD PASS=37 FAIL=0
```

```yaml
claim_id: record_local_observability_decoder_criterion_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact finite decoder criterion; no physical broadcast derivation"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
