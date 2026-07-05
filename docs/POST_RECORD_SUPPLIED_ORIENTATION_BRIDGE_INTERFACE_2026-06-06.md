# Post-Record Supplied Orientation Bridge Interface

**Date:** 2026-06-06
**Type:** exact support / conditional dynamics interface
**Claim type:** bounded_theorem
**Status:** bounded-support interface for supplied orientation bridge semantics;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Status authority:** source-side type boundary only; this packet does not apply
or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.py`](../scripts/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.txt)

## Result

The arrow-orientation no-go has a positive interface:

```text
supplied finite law on post-record words
  + supplied orientation bridge
  + supplied directed event/statistic
  + exact enumeration
  => law-scoped directed certificate under that supplied bridge
```

The physical forward order is a supplied bridge. Record and count data do not
derive that orientation.

A supplied orientation bridge must name:

- the law id;
- the orientation convention (`forward` or `reverse` on the word order);
- the clock or ordering id;
- the production-kernel, Hamiltonian, transfer, or instrument id when a row
  wants dynamics language rather than only oriented word language.

This branch does not derive an orientation, clock, or kernel. It defines the
finite certificate interface once those data are supplied.

## Why the interface matters

The no-go proves:

```text
count(w) = count(reverse(w))
count_* P = count_* P^R
```

So count-only events cannot orient the arrow. But directed events can depend on
the supplied orientation. For example, an endpoint event such as:

```text
first atom is A and last atom is B
```

can have different probability under the same finite word law depending on
whether the supplied physical order is the word order or the reversed word
order. That is useful only because the orientation bridge is explicit.

## Audit use

This gives the `arrow_or_dynamics_bridge` rows a reusable interface:

1. If a row supplies only counts, it remains count-level and cannot orient a
   physical arrow.
2. If a row supplies a finite law plus an orientation bridge, exact enumeration
   can certify directed word events.
3. If a row wants production dynamics, it must also name the supplied kernel,
   Hamiltonian, transfer operator, instrument, clock, or rate bridge.
4. The bridge is law-scoped. Directed certificates do not transport across
   laws or orientation conventions without rechecking.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "directed post-record certificates are available only under supplied orientation/law/clock/kernel bridges"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch defines a supplied-bridge interface and does not derive or select the bridge."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not derive a physical arrow from Record.
- Does not derive or select a production kernel.
- Does not derive a clock, rate, Hamiltonian, transfer operator, or instrument.
- Does not select or force a generation/Koide dial location.
- Does not turn stable settings into selected dials.

## Runner certificate

The runner verifies:

- source anchors in this note, the arrow-orientation no-go, and supplied
  concentration interface;
- supplied orientation bridges validate directed endpoint certificates by
  exact enumeration;
- missing orientation is rejected for directed certificates;
- wrong law scope is rejected;
- reversed orientation changes directed endpoint probabilities while preserving
  count-only probabilities;
- supplied forward/reversed empirical kernels are valid but not selected by
  counts;
- no audit verdict, audit-data write, retained/promoted claim,
  Record-derived physical arrow, production-kernel selection, stable-setting
  dial selection, or generation/Koide selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_supplied_orientation_bridge_interface_2026_06_06.py
```
