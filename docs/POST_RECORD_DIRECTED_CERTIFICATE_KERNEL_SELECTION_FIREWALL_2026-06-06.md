# Post-Record Directed Certificate Kernel Selection Firewall

**Date:** 2026-06-06
**Type:** exact no-go / dynamics firewall
**Claim type:** no-go
**Status:** no-go branch-local for selecting a production kernel from directed
certificates alone; audit_required_before_effective_retained=true;
bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.py`](../scripts/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.txt)

## Result

Directed certificates do not select a production kernel.

The positive examples show what can be verified after a law, orientation,
clock, kernel id, and directed statistic are supplied. This firewall keeps the
converse out:

```text
exact directed certificate data
  != selected production kernel
```

The kernel remains a supplied bridge input.

## Exact witnesses

The runner gives two finite witnesses.

1. **Identical finite law, different unvisited rows.** With source mass only
   on `A`, two row-stochastic kernels can agree on the `A` row and differ on
   the unvisited `B` row. They induce the same length-2 law and the same
   directed certificates, but they are different kernels.
2. **Same scalar certificate, different laws and kernels.** With full support,
   two different kernels can agree on one directed certificate value such as
   endpoint `A -> B` while disagreeing on other directed statistics.

So same directed certificate data can admit distinct candidate kernels unless
the kernel, estimator, or model-selection rule is supplied separately.

## Dynamics meaning

Directed certificates are useful for auditing a supplied dynamics bridge. They
are not a selector for the bridge. If a row wants production dynamics language,
it must name the kernel, Hamiltonian, transfer operator, instrument, clock,
rate, boundary condition, or model-selection rule it is using.

This preserves the pre-record/post-record split. Probability lives in the
supplied law or production model; post-record sites carry realized information.
The realized records can test a supplied model, but do not by themselves choose
the model.

## Status certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "directed certificates can validate supplied kernel bridges but cannot select production kernels without a supplied selection rule"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch is a firewall/no-go and not a retained-grade positive proposal."
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

- source anchors in this note, directed-certificate examples, the supplied
  orientation bridge, and the arrow-orientation firewall;
- two distinct row-stochastic kernels can induce the same finite law and same
  directed certificate values when rows are unvisited;
- one scalar directed certificate can admit distinct full-support candidate
  kernels;
- supplied kernel id gates dynamics-language certificates;
- wrong law scope, missing orientation, missing kernel, and wrong value are
  rejected;
- no audit verdict, audit-data write, retained/promoted claim,
  Record-derived physical arrow, production-kernel selection, clock/rate
  derivation, Born-law derivation, stable-setting dial selection, or
  generation/Koide selection flag is set.

Run:

```text
python3 scripts/frontier_post_record_directed_certificate_kernel_selection_firewall_2026_06_06.py
```
