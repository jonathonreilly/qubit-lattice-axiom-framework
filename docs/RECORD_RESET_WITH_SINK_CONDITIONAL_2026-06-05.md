---
claim_id: record_reset_with_sink_conditional_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Reset With Explicit Sink Conditional

**Date:** 2026-06-05
**Claim type:** bounded support map and conditional finite construction.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_reset_with_sink_conditional_2026_06_05.py`](../scripts/frontier_record_reset_with_sink_conditional_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_reset_with_sink_conditional_2026_06_05.txt`](../logs/runner-cache/frontier_record_reset_with_sink_conditional_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_BLANK_BOUNDARY_RESET_NO_GO_2026-06-05.md`](RECORD_BLANK_BOUNDARY_RESET_NO_GO_2026-06-05.md)
- [`RECORD_POINTER_BROADCAST_HAMILTONIAN_CONDITIONAL_2026-06-05.md`](RECORD_POINTER_BROADCAST_HAMILTONIAN_CONDITIONAL_2026-06-05.md)
- [`RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md`](RECORD_POINTER_BROADCAST_CIRCUIT_INTERFACE_2026-06-05.md)

## Purpose

The blank-boundary no-go shows that closed clean reset without a sink is
many-to-one. This note gives the finite escape route: add explicit sink bits,
move the old fragment memory into the sink, and then write the clean pointer
record into the fragments.

## Result

On one pointer bit `s`, three fragment bits `e_i`, and three sink bits `g_i`,
the reversible label map

```text
(s, e, g) -> (s, g xor s, e)
```

is a permutation. If the sink starts blank (`g=000`), the output fragments are
the clean local broadcast `sss`, while the old fragment state `e` is preserved
in the sink.

Thus the reset no-go is not "reset is impossible." It is:

```text
clean reset requires either a blank boundary or an explicit sink/erasure
resource that carries the old memory.
```

## Negative route pruning

| route | verdict | reason |
|---|---|---|
| sink construction makes reset free | pruned | sink blankness and cost remain inputs |
| sink construction derives production dynamics | pruned | it is a supplied reversible map |
| sink construction removes thermodynamic accounting | pruned | old memory is exported, not destroyed |
| sink construction fixes clock/rate | pruned | no time or rate normalization is supplied |
| sink construction selects a dial location | pruned | it is only a record-production interface |

## What remains open

- Preparing blank sink degrees of freedom.
- Accounting for sink entropy / thermodynamic cost.
- Deriving the reversible reset map from physical dynamics.
- Clock/rate normalization.
- Probabilities before realization.

## What this unlocks

- The production stack now has both sides of the reset boundary: a no-go without
  a sink and an exact conditional construction with a sink.
- Future dynamics work can target the real residual: sink preparation,
  thermodynamic cost, and physical implementation.

## Boundaries

- Does not derive sink blankness, thermodynamic cost, physical reset dynamics,
  rates, clock, probabilities, or a dial setting.
- Does not apply audit verdicts.

## Runner summary

The runner verifies the sink map is a permutation; preserves the pointer; gives
clean broadcast from arbitrary old fragments when the sink is blank; stores the
old fragment state in the sink; and fails clean broadcast when the sink is not
blank.

Expected result:

```text
SCORECARD PASS=29 FAIL=0
```

```yaml
claim_id: record_reset_with_sink_conditional_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact reversible reset construction given blank sink bits"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
