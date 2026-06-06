# Post-Record Arrow Orientation Firewall

**Date:** 2026-06-06
**Type:** exact no-go / dynamics firewall
**Claim type:** no-go
**Status:** no-go branch-local for deriving a physical arrow or production
kernel from post-record counts alone; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_arrow_orientation_firewall_2026_06_06.py`](../scripts/frontier_post_record_arrow_orientation_firewall_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_arrow_orientation_firewall_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_arrow_orientation_firewall_2026_06_06.txt)

## Result

Post-record counts do not orient a physical arrow.

The finite record-history theorem gives append/count information dynamics once
atoms are realized:

```text
w -> wv
count(wv) = count(w) + count(v)
```

That is a stable post-record information surface. It is not a physical arrow,
not a production kernel, not a clock, and not a law for which atom appears
next.

The exact obstruction is reversal symmetry of count information:

```text
count(w) = count(reverse(w)).
```

More generally, for any finite law `P` on record words and its reversed law
`P^R(w) = P(reverse(w))`, the count pushforward is invariant under reversal:

```text
count_* P = count_* P^R.
```

Therefore any audit event, p-value, or concentration certificate that depends
only on counts cannot decide which orientation is the physical arrow.

## What survives reversal

Count data and scalar additive readouts survive reversal:

```text
I(count(w)) = I(count(reverse(w))).
```

This is why post-record append/count dynamics is useful: it gives stable,
durable information and unbounded finite retention without keeping the whole
history as one coherent qubit state.

## What reversal changes

Oriented transition data changes:

```text
transitions(reverse(w)) = transpose(transitions(w)).
```

For asymmetric histories, the forward empirical transition counts and the
reversed empirical transition counts are different while the post-record count
state is identical. A supplied orientation can choose one. The count state does
not.

## Dynamics implication

The practical implication for the `arrow_or_dynamics_bridge` bucket is:

- post-record words/counts supply realized information;
- count laws and concentration certificates can calibrate count events under a
  supplied law;
- physical arrow, production kernel, Hamiltonian, transfer operator,
  instrument, clock, rate, or low-record boundary condition must still be
  supplied by a separate bridge.

This is consistent with the existing arrow result: record formation can point
away from a supplied low-record boundary, but the low-record boundary is the
open past-hypothesis input. This note proves the count-only obstruction: if the
bridge supplies no orientation/boundary/law, post-record information does not
create one.

An oriented law, boundary condition, clock, or production kernel is a separate
bridge input.

post-record counts do not orient a physical arrow.

## Status certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "post-record counts can support realized information and count certificates; they cannot orient a physical arrow or select a production kernel without a supplied bridge"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch proves a no-go/firewall, not a positive retained-grade theorem."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not derive a physical arrow from Record.
- Does not derive a production kernel, Hamiltonian, transfer operator,
  instrument, clock, or rate.
- Does not select or force a generation/Koide dial location.
- Does not turn stable settings into selected dials.

## Runner certificate

The runner verifies:

- source anchors in this note and the upstream post-record/dynamics notes;
- count states are invariant under word reversal;
- count scalar readouts are invariant under word reversal;
- finite count-law pushforwards are invariant under law reversal;
- count-only event probabilities are invariant under law reversal;
- oriented transition counts reverse by transposition;
- asymmetric histories have different oriented transition data with identical
  count states;
- empirical forward/reversed kernels are both valid supplied kernels and are
  not selected by the count state;
- no audit verdict, audit-data write, retained/promoted claim,
  Record-derived physical arrow, production-kernel selection, stable-setting
  dial selection, or generation/Koide selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_arrow_orientation_firewall_2026_06_06.py
```
