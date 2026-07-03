# Post-Record Expectation/Concentration Firewall

**Date:** 2026-06-06
**Type:** exact no-go / audit-calibration firewall
**Claim type:** no_go
**Status:** no-go branch-local for deriving concentration, tail p-values, or
audit calibration from expected post-record counts alone;
audit_required_before_effective_retained=true; bare_retained_allowed=false.
**Primary runner:**
[`scripts/frontier_post_record_expectation_concentration_firewall_2026_06_06.py`](../scripts/frontier_post_record_expectation_concentration_firewall_2026_06_06.py)
**Cached log:**
[`logs/runner-cache/frontier_post_record_expectation_concentration_firewall_2026_06_06.txt`](../logs/runner-cache/frontier_post_record_expectation_concentration_firewall_2026_06_06.txt)

## Result

Expected empirical frequencies do not determine finite tail probabilities.

On the two-letter alphabet and horizon `N=4`, compare two supplied laws:

1. iid fair law: every word has probability `1/16`;
2. perfectly correlated fair law: `AAAA` has probability `1/2`, `BBBB` has
   probability `1/2`, and all other words have probability `0`.

Both laws have:

```text
E[count_A] = 2,     E[count_B] = 2,
E[f_N] = (1/2, 1/2),
```

and both have fair one-time marginals at every event index. But the extreme
imbalance probability differs:

```text
P(|count_A-count_B| = 4) = 1/8      under iid fair,
P(|count_A-count_B| = 4) = 1        under correlated fair.
```

Therefore expected frequencies, and even all one-time marginals, do not imply
concentration or p-values. Audit calibration needs the supplied finite law, a
mixing/correlation assumption, or an explicit concentration theorem.

## What this prunes

This prunes the route:

```text
expected post-record frequency
  => concentration / p-value / audit verdict.
```

The valid route is conditional:

```text
supplied finite law or supplied concentration theorem
  + supplied statistic and threshold
  => calibrated p-value or audit flag under those assumptions.
```

## What remains useful

Expected-frequency interfaces remain useful for ensemble bookkeeping. They just
do not replace finite-null calibration, dynamic programming, exact enumeration,
or concentration assumptions.

## Status certificate

```yaml
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: concentration and p-values remain conditional on supplied finite law or concentration assumptions
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This branch prunes expectation-to-concentration overclaims; it does not propose retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Runner certificate

The runner verifies:

- source-anchor boundaries in landed post-record count/dynamics notes;
- both finite laws normalize exactly;
- both laws have the same expected count vector;
- both laws have the same fair one-time marginals;
- tail probabilities differ exactly;
- the same observed word receives different exact p-values;
- Record does not derive concentration, p-values, kernels, clocks, Born laws,
  Hamiltonians, or generation/Koide dials.

Run:

```text
python3 scripts/frontier_post_record_expectation_concentration_firewall_2026_06_06.py
```
