# DM Full Closure Same-Surface Thermal Monotonicity Theorem

**Type:** bounded_theorem
**Status:** bounded thermal-kernel derivative/positivity certificate; the
live-DM-slice 64:1 channel-weighted ratio conclusion is conditional on an
unsupplied channel-weight authority (see 2026-05-28 repair header).
**Date:** 2026-04-17 (2026-05-28: monotonicity conclusion split from the
unsupplied 64:1 channel-weight bridge).
**Audit status:** assigned only by the independent audit lane.
**Script:** `scripts/frontier_dm_full_closure_same_surface_thermal_monotonicity_theorem.py`

## 2026-05-28 Review Repair (thermal-kernel core split from channel-weight bridge)

This note is narrowed to the thermal-kernel derivative identities and
positivity proof it directly verifies. Supplying a 64:1 channel-weight
authority is substantive DM-lane work outside this note:

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

What thermal-kernel monotonicity content can already be closed exactly, before
the live same-surface channel-weight bridge is supplied?

## Answer

The attractive and repulsive Sommerfeld thermal kernels have exact
derivative/sign bounds in the selected coupling variable.

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

If a retained 64:1 same-surface channel-weight authority is supplied, these
kernel bounds yield the pointwise derivative bound

- `64 f_att'(8y) + f_rep'(y) > 63/2`

and therefore that weighted same-surface expression is strictly increasing in
`alpha`. Without that channel-weight authority, this note does not close the
live-DM ratio monotonicity theorem.

## Consequence

This closes one exact kernel-level part of the DM-side selector problem:

- the thermal-kernel derivative identities and sign bounds are exact;
- the 64:1 weighted live-DM monotonicity conclusion remains conditional on
  the channel-weight bridge;
- exact evaluation or exact bounding of the thermal integral remains separate
  DM-lane work.

So on any admitted one-scalar `alpha` family with a supplied 64:1
same-surface channel-weight authority:

- there can be at most one closure root

Absent that authority, root uniqueness is support-only context rather than a
closed theorem of this row.

## Command

```bash
python3 scripts/frontier_dm_full_closure_same_surface_thermal_monotonicity_theorem.py
```

## Upstream authority

- [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md) — exact same-surface thermal integral form `<S> = (2/sqrt(pi)) ∫_0^∞ S(...) sqrt(t) e^{-t} dt` on the freeze-out slice `a = x_f / 4 = 25 / 4` whose `alpha` dependence is the load-bearing input for the monotonicity argument below.
- [DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md](DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md) — framework-applied normalization certificate for the underlying Maxwell-Boltzmann thermal-velocity average algebra and Sommerfeld argument normalization that the integral form descends from. The `64 : 1` same-surface channel-weight assignment is documented separately in the channel-weight authority on the DM same-surface lane.
