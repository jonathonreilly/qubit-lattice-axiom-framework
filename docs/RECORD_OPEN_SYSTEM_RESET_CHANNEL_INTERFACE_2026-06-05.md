---
claim_id: record_open_system_reset_channel_interface_2026-06-05
claim_type_author_hint: bounded_support_map
---

# Record Open-System Reset Channel Interface

**Date:** 2026-06-05
**Claim type:** bounded_theorem — bounded support map and open-system interface.
**Status authority:** independent audit lane only. This source note does not
set an audit verdict, edit audit data, or assert package-status promotion.
**Primary runner:**
[`scripts/frontier_record_open_system_reset_channel_interface_2026_06_05.py`](../scripts/frontier_record_open_system_reset_channel_interface_2026_06_05.py)
with cache
[`logs/runner-cache/frontier_record_open_system_reset_channel_interface_2026_06_05.txt`](../logs/runner-cache/frontier_record_open_system_reset_channel_interface_2026_06_05.txt).

**Local support inputs:**

- [`RECORD_BLANK_SINK_PREPARATION_REGRESS_NO_GO_2026-06-05.md`](RECORD_BLANK_SINK_PREPARATION_REGRESS_NO_GO_2026-06-05.md)
- [`RECORD_RESET_SINK_ENTROPY_LEDGER_2026-06-05.md`](RECORD_RESET_SINK_ENTROPY_LEDGER_2026-06-05.md)
- [`RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md`](RECORD_RESET_WITH_SINK_CONDITIONAL_2026-06-05.md)
- [`RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md`](RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md)

## Purpose

The blank-sink regress no-go blocks internal closed finite blanking from an
arbitrary prior sink state. This note supplies the exact open-system interface
that escapes the no-go without hiding information loss:

```text
V |x>_S = |0...0>_S |x>_E.
```

Tracing out `E` gives a reset channel on `S`. Keeping `E` shows the old state
has been exported, not destroyed.

## Result

For a `d = 2^k` dimensional sink register, define the isometry

```text
V : H_S -> H_S tensor H_E
V |x> = |0> |x>.
```

Then:

1. `V* V = I`, so the joint system-plus-environment evolution is reversible at
   the dilation level.
2. The reduced system channel is exact reset:

   ```text
   Tr_E[V rho V*] = |0><0|
   ```

   for every normalized input state `rho`.
3. The environment carries the input state:

   ```text
   Tr_S[V rho V*] = rho.
   ```

So the open-system reset channel is an exact interface for sink preparation,
but its dilation makes the exported-memory residual explicit.

Equivalently, the Kraus operators

```text
K_x = |0><x|
```

satisfy `sum_x K_x* K_x = I` and implement the same reset channel.

## Rate Boundary

A one-qubit amplitude-damping channel with parameter `p` resets `|1>` exactly
only at `p = 1`. For a finite-rate semigroup parametrization
`p(t) = 1 - exp(-gamma t)`, finite `gamma` and finite `t` give `p(t) < 1`.
Thus this block supplies an exact open-system channel interface, not a derived
finite-time physical rate or clock normalization.

## Negative Route Pruning

| route | verdict | reason |
|---|---|---|
| open reset destroys old memory for free | pruned | Stinespring environment carries `rho` |
| reset channel derives thermodynamic cost | pruned | no bath, temperature, or cost law is supplied |
| exact reset channel derives finite-time rate | pruned | damping semigroup reaches exact endpoint only at `p=1` |
| fixed finite environment supports arbitrary repeated reset | pruned | environment dimension grows with exported histories |
| reset interface fixes a dial | pruned | no selector is supplied |

## What This Unlocks

- Future dynamics proposals can cite a precise reset-channel interface instead
  of alternating between closed-unitary no-go and informal erase language.
- Audit lanes can ask whether a proposed record-production dynamics supplies
  the dilation/environment, the trace-out step, and the physical rate/cost
  layer separately.
- The next hard route is now narrower: derive a physical implementation of this
  channel, or state the boundary/open-system premise explicitly.

## Boundaries

- Does not derive a Hamiltonian, bath, temperature, thermodynamic cost,
  finite-time rate, clock, low-record boundary, probabilities, or a dial
  setting.
- Does not say the environment may be discarded for free.
- Does not apply audit verdicts.

## Runner Summary

The runner verifies Stinespring isometry, Kraus completeness, system reset,
environment state preservation, repeated-cycle environment growth, and the
amplitude-damping endpoint/rate boundary.

Expected result:

```text
SCORECARD PASS=49 FAIL=0
```

```yaml
claim_id: record_open_system_reset_channel_interface_2026-06-05
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "exact open-system reset channel interface; physical implementation and rates remain open"
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
