---
claim_id: record_born_frequency_boundary_2026-06-05
claim_type_author_hint: exact_negative_boundary
---

# Record Born-Frequency Boundary

**Date:** 2026-06-05
**Claim type:** no_go — exact negative boundary and finite counting support.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_born_frequency_boundary_2026_06_05.py`](../scripts/frontier_record_born_frequency_boundary_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_born_frequency_boundary_2026_06_05.txt`](../logs/runner-cache/frontier_record_born_frequency_boundary_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_SELECTIVE_INSTRUMENT_ATOM_CRITERION_2026-06-05.md`](RECORD_SELECTIVE_INSTRUMENT_ATOM_CRITERION_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)
- [`RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md`](RECORD_DEPHASING_BROADCAST_INTERFACE_2026-06-05.md)

## Purpose

Selective record atoms give histories and counts. They do not, by themselves,
derive a Born-frequency law or a finite-history convergence theorem.

## Result

For binary record atoms, a finite history word

```text
w in {0,1}^N
```

has exact post-record counts:

```text
n_1(w), n_0(w), f_1(w) = n_1(w)/N.
```

Those counts are information after realization. They are not a derivation of
the pre-record probability `p`, nor a guarantee that finite frequency equals
`p`. For `N = 4`, possible frequencies are `0, 1/4, 1/2, 3/4, 1`; no single
probability value is forced by the history grammar.

If an IID probability model is supplied, binomial weights can be assigned to
histories and ordinary convergence statements can be discussed. That model is
an extra probability input, not a consequence of record append/count alone.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| finite record counts derive Born probabilities | pruned | many finite histories have different frequencies |
| one finite history proves convergence | pruned | convergence is a model-level statement |
| history grammar supplies IID trials | pruned | independence/model assumptions are extra |
| selective atom criterion derives Born frequencies | pruned | it only normalizes supplied branches |
| frequency boundary fixes clock/rate/dial | pruned | no time normalization or selector is supplied |

## What This Unlocks

- Audit lanes can use record histories for exact empirical counts without
  pretending counts derive the probability law.
- Born/frequency work now has a precise missing gate: a probability model or
  theorem linking pre-record weights to long-run record frequencies.
- The pre-record probability and post-record information split remains intact.

## Boundaries

- Does not derive Born frequencies, IID structure, convergence, outcome
  selection, physical collapse, clock/rate, reset cost, or a dial setting.
- Does not apply audit verdicts or edit repo-wide authority surfaces.

## Runner Summary

The runner enumerates finite binary histories, checks append/count/frequency
facts, verifies many-to-one count classes, and confirms that a supplied
probability model is separate from record-history grammar.

Expected result:

```text
SCORECARD PASS=35 FAIL=0
```

```yaml
claim_id: record_born_frequency_boundary_2026-06-05
actual_current_surface_status: no-go
trace_class: negative_route_pruning
reachability_to_target: prunes
conditional_surface_status: "record histories count realized atoms; Born-frequency law remains a separate probability-model gate"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
