---
claim_id: record_reset_sink_entropy_ledger_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Reset Sink Entropy Ledger

**Date:** 2026-06-05
**Claim type:** meta — bounded support map and finite information ledger.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_reset_sink_entropy_ledger_2026_06_05.py`](../scripts/frontier_record_reset_sink_entropy_ledger_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_reset_sink_entropy_ledger_2026_06_05.txt`](../logs/runner-cache/frontier_record_reset_sink_entropy_ledger_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md`](RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md)
- [`RECORD_BLANK_BOUNDARY_RESET_NO_GO_2026-06-05.md`](RECORD_BLANK_BOUNDARY_RESET_NO_GO_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)

## Purpose

The reset-with-sink construction restores reversibility by exporting old
fragment memory into explicit sink bits. This note records the finite
information ledger of that move. It answers a narrower question than
thermodynamics:

```text
How many finite record labels must the sink carry if arbitrary old fragments
are reset into a clean pointer broadcast?
```

It does not derive a heat bath, temperature, physical reset dynamics, rate,
clock, or a cost law.

## Finite Ledger

For one pointer bit `s`, `k` old fragment bits `e`, and `k` sink bits `g`, use
the reversible map

```text
(s, e, g) -> (s, g xor s, e).
```

On the blank-sink boundary `g=00...0`, the visible fragments become the clean
broadcast `ss...s`, while the sink stores the old fragment word `e`.

For a uniform finite label ensemble over `(s, e)` with blank sink:

| surface | support size | entropy in bits |
|---|---:|---:|
| full input `(s, e, g=0)` | `2^(k+1)` | `k + 1` |
| full output `(s, clean fragments, sink=e)` | `2^(k+1)` | `k + 1` |
| visible clean record after ignoring sink | `2` | `1` |
| hidden sink memory conditional on pointer | `2^k` | `k` |

Thus clean reset has not destroyed the old fragment information in the
reversible construction. It has moved `k` bits into the sink. If a later step
discards or reblanks the sink while keeping only the visible clean broadcast,
that later step is a many-to-one erasure of the old fragment labels.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| sink construction erases old memory | pruned | the sink stores the old fragment word exactly |
| ignoring the sink is a reversible reset | pruned | the visible clean record has only two labels |
| reblanking the sink is free in finite labels | pruned | reblanking maps `2^(k+1)` labels to `2` |
| entropy ledger derives thermodynamic cost | pruned | it is only finite label accounting |
| entropy ledger fixes clock/rate/dial | pruned | no dynamics selector or time normalization is supplied |

## What This Unlocks

- Reset proposals can separate three different steps:
  1. reversible export of old memory into a sink,
  2. optional discard or reblanking of the sink,
  3. any physical thermodynamic implementation.
- The reset stack now has a precise finite-accounting target for future
  open-system dynamics: explain how sink blankness is prepared and how exported
  memory is handled.
- Audit lanes can reject any "clean reset" claim that drops the sink without
  declaring the many-to-one erasure step.

## Boundaries

- Does not derive sink blankness, thermodynamic cost, physical reset dynamics,
  rates, clock, probabilities, or a dial setting.
- Does not identify finite support entropy with heat or action.
- Does not apply audit verdicts.

## Runner Summary

The runner checks the ledger for `k = 1..5`, including the `k = 3` witness used
in the reset-with-sink note. It verifies full reversible support preservation,
clean visible broadcast from blank sink, exact recovery of the old fragment word
from the sink, the `k`-bit hidden-memory ledger, and the many-to-one collapse
created by sink discard/reblanking.

Expected result:

```text
SCORECARD PASS=70 FAIL=0
```

```yaml
claim_id: record_reset_sink_entropy_ledger_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "finite sink-memory ledger for reset-with-sink; no thermodynamic cost law"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
