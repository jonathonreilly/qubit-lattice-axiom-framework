# Post-Record Supplied Kernel Selection Rule Interface

**Date:** 2026-06-06
**Type:** exact support / conditional dynamics interface
**Claim type:** bounded_theorem
**Status:** bounded-support interface for supplied finite kernel-selection rule
semantics; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Status authority:** source-side type boundary only; this packet does not apply
or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.py`](../scripts/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.txt)

## Result

The kernel-selection firewall has a positive supplied-rule interface:

```text
supplied finite candidate family plus supplied selection rule
  + supplied source/law scope
  + supplied orientation and clock/order bridge
  + exact rational scoring
  => unique selected candidate inside that supplied rule
```

The rule is supplied, not derived from Record. The candidate family is supplied,
not derived from Record.

This is the dynamics analogue of the dial constraint: stable setting is not
selected dial, and an exact selected candidate is only a stable location within
the supplied selection rule.

## Example

The runner uses two supplied row-stochastic candidate kernels. A supplied
quadratic rational score compares each candidate law against supplied target
values for:

- endpoint `A -> B`;
- endpoint `B -> A`;
- the event that the second atom is `B`.

That supplied rule has a unique minimum at candidate `k4`. If the rule is
weakened to only endpoint `A -> B`, the same candidates tie and kernel
selection is blocked as underselected.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "finite kernel selection is exact only inside a supplied candidate family and supplied selection rule"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch defines a supplied-rule interface and does not derive the rule, candidates, or physical production kernel."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not edit `docs/audit/data`.
- Does not apply or predict audit verdicts.
- Does not promote any row.
- Does not derive a physical arrow from Record.
- Does not derive a production kernel from Record.
- Does not derive a selection rule or candidate family from Record.
- Does not derive a Born law from Record.
- Does not select or force a generation/Koide dial location.
- Does not turn stable settings into selected dials.

## Runner certificate

The runner verifies:

- source anchors in this note, the kernel-selection firewall, and the directed
  certificate examples;
- supplied candidate kernels are row-stochastic;
- the supplied informative rule has a unique exact rational minimum;
- the selected candidate is inside the supplied candidate family;
- a weak endpoint-only rule underselects the kernel;
- missing rule, wrong rule scope, missing orientation, and zero-weight rules
  are blocked;
- no audit verdict, audit-data write, retained/promoted claim,
  Record-derived selection rule, Record-derived candidate family,
  physical-arrow derivation, Born-law derivation, stable-setting dial
  selection, or generation/Koide selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_supplied_kernel_selection_rule_interface_2026_06_06.py
```
