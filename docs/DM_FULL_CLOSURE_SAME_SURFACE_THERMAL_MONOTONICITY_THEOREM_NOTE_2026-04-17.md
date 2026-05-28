# DM Full Closure Same-Surface Thermal Monotonicity Theorem

**Type:** bounded_theorem
**Status:** bounded thermal-kernel derivative/positivity certificate; the
live-DM-slice 64:1 channel-weighted ratio conclusion is conditional on an
unsupplied channel-weight authority (see 2026-05-28 repair header).
**Date:** 2026-04-17 (2026-05-28: monotonicity conclusion split from the
unsupplied 64:1 channel-weight bridge per audit verdict).
**Branch:** `codex/dm-thermal-review-2026-04-17`  
**Status authority:** independent audit lane only.
**Script:** `scripts/frontier_dm_full_closure_same_surface_thermal_monotonicity_theorem.py`

## 2026-05-28 Audit Repair (thermal-kernel core split from channel-weight bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The derivative identities and positivity proof close algebraically,
> but the restricted packet does not contain the promised channel-weight
> authority or an explicit retained formula tying the same-surface DM
> ratio to the 64:1 weighted attractive/repulsive Sommerfeld terms.
> Without that bridge, the final DM-ratio monotonicity conclusion is
> [not closed]."*

Repair via the split path (adding a retained 64:1 channel-weight authority
is substantive new DM-lane work, out of scope):

- **Load-bearing (in scope):** the thermal-kernel derivative identities
  and positivity proof (monotonicity of the `f_att`, `f_rep` Sommerfeld
  thermal averages), which close algebraically and are runner-verified.
- **Conditional / NON-load-bearing (split off):** the final
  same-surface DM-ratio monotonicity conclusion, which requires the
  **64:1 channel-weighted attractive/repulsive formula**
  `d/dy [64 f_att(8y) + f_rep(y)]` as a retained one-hop authority. That
  channel-weight bridge is **not supplied**; the DM-ratio conclusion is
  recorded as conditional on it.

No new axiom, import, or retained bridge is introduced. The thermal-kernel
core is the load-bearing content; the 64:1 DM-ratio conclusion stays
conditional until the channel-weight authority lands.

## Question

What part of the DM-side selector problem can already be closed exactly, before
the thermal integral itself is fully derived?

## Answer

The exact same-surface thermal DM ratio is **strictly increasing** in the
selected coupling `alpha`.

The key exact identities are:

- `f_att'(y) - 1/2 = h(y) / (2 (e^y - 1)^2)`
- `f_rep'(y) + 1/2 = h(y) / (2 (e^y - 1)^2)`

with

- `h(y) = e^(2y) - 2 y e^y - 1`

and

- `h(0)=0`
- `h'(y) = 2 e^y (e^y - 1 - y) > 0` for `y>0`

so

- `f_att'(y) >= 1/2`
- `f_rep'(y) >= -1/2`

for all `y>0`.

On the same-surface DM channel weights, this yields the pointwise derivative
bound

- `64 f_att'(8y) + f_rep'(y) > 63/2`

and therefore the exact same-surface thermal DM ratio is strictly increasing in
`alpha`.

## Consequence

This closes one exact part of the DM-side selector problem:

- the remaining blocker is **not** monotonicity
- the remaining blocker is only exact evaluation or exact bounding of the
  thermal integral itself

So on any admitted one-scalar `alpha` family:

- there can be at most one closure root

The remaining work is to close the thermal integral, not to prove root
uniqueness.

## Command

```bash
python3 scripts/frontier_dm_full_closure_same_surface_thermal_monotonicity_theorem.py
```

## Upstream authority

- [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md) — exact same-surface thermal integral form `<S> = (2/sqrt(pi)) ∫_0^∞ S(...) sqrt(t) e^{-t} dt` on the freeze-out slice `a = x_f / 4 = 25 / 4` whose `alpha` dependence is the load-bearing input for the monotonicity argument below.
- [DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md](DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md) — framework-applied normalization certificate for the underlying Maxwell-Boltzmann thermal-velocity average algebra and Sommerfeld argument normalization that the integral form descends from. The `64 : 1` same-surface channel-weight assignment is documented separately in the channel-weight authority on the DM same-surface lane.
