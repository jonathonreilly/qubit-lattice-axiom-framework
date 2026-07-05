# Post-Record Supplied Concentration Certificate Interface

**Date:** 2026-06-06
**Type:** exact support / conditional audit interface
**Claim type:** bounded_theorem
**Status:** bounded-support interface for finite law-scoped certificate semantics;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Status authority:** source-side type boundary only; this packet does not apply
or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.py`](../scripts/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.txt)

## Result

Post-record histories and counts can consume concentration information, but
Record does not create that information by itself.

The safe finite audit contract is:

```text
supplied finite law on post-record words
  + supplied statistic/event
  + verified law-scoped concentration certificate
  => conservative finite audit flag under that law
```

A concentration certificate is law-scoped data:

```text
certificate = (law id, event predicate, epsilon)
meaning: P_law(event) <= epsilon
```

For finite post-record words, the runner verifies the certificate by exact
enumeration. If the event depends only on counts, the same probability can be
computed after pushing the law forward to count states. This is the connection
to the exact post-record append/count dynamics: realized histories remain
integral, while concentration belongs to the supplied law or certificate layer.

## Why law scope matters

On the two-letter alphabet at horizon `N=4`, the iid fair law and the perfectly
correlated fair law have the same expected counts and the same one-time
marginals. But the extreme imbalance event

```text
|count_A - count_B| >= 4
```

has probability:

```text
1/8   under iid fair,
1     under correlated fair.
```

Therefore an iid concentration certificate with bound `epsilon = 1/4` is valid
for the iid law and invalid for the correlated law. A certificate cannot be
transported across laws merely because expected counts match.

## Audit use

This gives bounded and conditional audit lanes a reusable interface:

1. If a row supplies a finite null law, exact enumeration or dynamic
   programming can verify the event probability.
2. If a row supplies a concentration theorem, the certificate must name its law
   scope and hypotheses.
3. If a row only supplies expected frequencies or one-time marginals, it does
   not have a concentration certificate.
4. If a row only supplies a stable dial location, that is separate from
   calibrated p-values unless the law/score/rule/certificate are supplied.

In short, expectation-only data does not have a concentration certificate.

## Status certificate

```yaml
actual_current_surface_status: exact-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "audit flags are conditional on supplied finite laws or supplied concentration certificates"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch provides an exact finite interface, not a retained/audit verdict."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Boundaries

- Does not derive a probability law from Record.
- Does not derive concentration from expected frequency.
- Does not derive independence, mixing, martingale, or Born hypotheses.
- Does not derive a kernel, clock/rate, Hamiltonian, or record-production law.
- Does not apply audit verdicts.
- Does not select or force a generation/Koide dial location.

## Runner certificate

The runner verifies:

- source anchors in the landed Record/dynamics notes;
- exact normalization of iid and correlated finite laws;
- same expected counts and one-time marginals for the control laws;
- exact pushforward from word laws to count laws;
- exact event probability agreement before and after count pushforward;
- iid certificate validity under its own law;
- invalidity of the same certificate under the correlated law;
- conservative audit flag semantics for observed extreme words;
- Record does not derive probability, concentration, p-values, audit verdicts,
  or generation/Koide dial selection.

Run:

```text
python3 scripts/frontier_post_record_supplied_concentration_certificate_interface_2026_06_06.py
```
