# Post-Record Directed Certificate Examples

**Date:** 2026-06-06
**Type:** exact support / supplied dynamics examples
**Claim type:** methodology / positive examples
**Status:** exact-support branch-local for supplied directed-certificate
examples; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py`](../scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_directed_certificate_examples_2026_06_06.txt)
**Load-bearing row-bucket helper:**
[`scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py`](../scripts/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.py)
with cache
[`logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_stability_dynamics_selector_subdivision_2026_06_06.txt)

## Result

The supplied-orientation bridge interface admits concrete finite examples:

```text
supplied finite law plus supplied orientation bridge
  + supplied clock/order id
  + supplied kernel/transfer/instrument id when dynamics language is used
  + supplied directed statistic
  + exact enumeration
  => law-scoped directed finite certificate
```

The law carries probability; the post-record words carry realized markers and
counts. This matches the pre-record/post-record split: probability lives in the
supplied law or production model, while a post-record site is a realized
information object.

The examples do not derive an arrow, clock, kernel, or selected dial. They show
what becomes exactly checkable after those bridge data are supplied.

## Examples

The runner instantiates three exact finite examples:

| Example | Supplied directed statistic | Exact check |
|---|---|---:|
| Signed transition drift | antisymmetric edge score along oriented words | forward expectation `-1/2`, reverse expectation `1/2` |
| Realized marker lag | first index of a realized marker `M` | forward expectation `7/6`, reverse expectation `11/6` |
| Low-to-high boundary event | first atom `L` and last atom `H` | forward probability `1/2`, reverse probability `1/6` |

In all three cases, the count pushforward is invariant under reversal while
the directed statistic changes under the supplied orientation.

## Dynamics meaning

This is a positive companion to the arrow-orientation firewall. Counts alone
cannot orient a physical arrow, but directed certificates are available after a
row supplies the missing bridge data:

- finite law id;
- orientation convention;
- clock/order id;
- kernel, transfer, Hamiltonian, instrument, rate, or boundary bridge when the
  row uses dynamics language;
- directed statistic or event.

The certificate is scoped to those inputs. It does not transport across laws,
bridges, or statistics without rechecking.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "directed finite certificates are exactly checkable under supplied law/orientation/clock/kernel bridges"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch gives supplied-bridge examples and does not derive or select the bridge data."
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
- Does not derive a Born law from Record.
- Does not select or force a generation/Koide dial location.
- Does not turn stable settings into selected dials.

## Runner certificate

The runner verifies:

- source anchors in this note, the supplied orientation bridge, the
  arrow-orientation firewall, and the stability/dynamics subdivision;
- the stability/dynamics helper source used to obtain the
  `arrow_or_dynamics_bridge` bucket is included in the packet;
- the current `arrow_or_dynamics_bridge` bucket remains `34` rows;
- signed transition drift has exact orientation-sensitive expectations and
  tails;
- realized marker lag keeps probabilities in the law and markers in
  post-record tuples;
- low-to-high boundary events are exact under supplied forward/reverse
  bridges;
- missing orientation, wrong law scope, wrong values, and missing dynamics
  kernel inputs are rejected;
- count pushforwards remain invariant under reversal in all examples;
- no audit verdict, audit-data write, retained/promoted claim,
  Record-derived physical arrow, production-kernel selection, clock/rate
  derivation, Born-law derivation, stable-setting dial selection, or
  generation/Koide selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_directed_certificate_examples_2026_06_06.py
```
