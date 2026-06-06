---
claim_id: record_asymptotic_reset_convergence_ledger_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Asymptotic Reset Convergence Ledger

**Date:** 2026-06-05
**Claim type:** bounded support map and convergence ledger.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_asymptotic_reset_convergence_ledger_2026_06_05.py`](../scripts/frontier_record_asymptotic_reset_convergence_ledger_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_asymptotic_reset_convergence_ledger_2026_06_05.txt`](../logs/runner-cache/frontier_record_asymptotic_reset_convergence_ledger_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_FINITE_TIME_RESET_SEMIGROUP_NO_GO_2026-06-05.md`](RECORD_FINITE_TIME_RESET_SEMIGROUP_NO_GO_2026-06-05.md)
- [`RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md`](RECORD_OPEN_SYSTEM_RESET_CHANNEL_INTERFACE_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)

## Purpose

The finite-time semigroup no-go blocks exact reset at finite bounded-generator
time. This note records the compatible positive route: finite-step damping can
approach blanking with an explicit residual ledger.

## Result

For a one-bit damping step with reset probability `p` and residual factor
`q = 1 - p`, an initially excited bit has residual excited weight

```text
r_n = q^n
```

after `n` supplied steps. For `0 < p < 1`, `r_n` is strictly decreasing and
converges to zero as `n` grows, but remains positive at every finite `n`.

To reach residual at most `epsilon`, the step count must satisfy

```text
n >= ceil(log(epsilon) / log(q)).
```

For `k` independent sink bits, the union-bound ledger gives

```text
Pr(any bit not blank) <= k q^n.
```

This supplies an epsilon-reset accounting surface, not exact finite-time reset.
It also supplies step counts, not physical time: converting `n` into a rate or
clocked duration remains a separate dynamics input.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| asymptotic convergence gives exact finite reset | pruned | residual `q^n` stays positive for finite `n` |
| epsilon ledger gives physical time | pruned | step count is not a clock map |
| epsilon ledger derives thermodynamic cost | pruned | no bath or cost law is supplied |
| multi-bit reset is free of scaling | pruned | union-bound threshold depends on `k` |
| convergence ledger fixes a dial | pruned | no selector is supplied |

## What This Unlocks

- Dynamics proposals can state epsilon-reset quality with explicit residuals
  instead of claiming exact finite reset.
- The reset stack now separates exact channel interface, finite-time endpoint
  no-go, and asymptotic approximation.
- Future physical routes can focus on deriving `p`, a clock map, or a bath/cost
  model.

## Boundaries

- Does not derive exact finite-time reset, a Hamiltonian, bath, thermodynamic
  cost, finite-time rate, clock, low-record boundary, probabilities from
  pre-record dynamics, or a dial setting.
- Does not apply audit verdicts.

## Runner Summary

The runner verifies residual monotonicity and positivity for finite steps,
epsilon-threshold arithmetic, the multi-bit union-bound ledger, and source-note
wording markers.

Expected result:

```text
SCORECARD PASS=36 FAIL=0
```

```yaml
claim_id: record_asymptotic_reset_convergence_ledger_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "epsilon-reset convergence ledger; no exact finite-time reset or physical rate"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
