# DM Full Closure Same-Surface Thermal Series/Tail Support

**Type:** bounded_theorem
**Status:** bounded pure thermal-kernel series/tail certificate; the live-DM
slice (plaquette-derived α interval, η/ω selector constants) is conditional
on unsupplied authorities (see 2026-05-28 repair header).
**Date:** 2026-04-17 (2026-05-28: pure thermal-kernel core split from the
unsupplied live-DM-slice constants).
**Audit status:** assigned only by the independent audit lane.
**Script:** `scripts/frontier_dm_full_closure_same_surface_thermal_series_tail_support.py`

## 2026-05-28 Review Repair (thermal-kernel core split from live-DM constants)

This note is narrowed to the pure thermal-kernel series/tail certificate it
directly verifies. Supplying authorities for the plaquette α interval and
η/ω selector is substantive DM-lane work outside this note:

- **Load-bearing (in scope):** the positive-series identities, tail
  inequalities, and the J1/J2 Meijer-G representations — closed
  algebraically and by independent quadrature checks (runner-verified).
  This is a **pure thermal-kernel** result, independent of any specific
  DM-slice numbers.
- **Conditional / NON-load-bearing (split off):** the **live DM slice** —
  the plaquette-derived α interval constants, the η/ω conversion target,
  and the same-surface selector sample definitions. The helper layer
  imports these **without retained one-hop authorities**; they are
  recorded as conditional inputs, not part of the load-bearing
  thermal-kernel certificate.

No new axiom, import, or retained bridge is introduced. The pure
thermal-kernel series/tail certificate is the load-bearing content; the
live-DM-slice numbers stay conditional until their authorities land.

## Question

Can the DM thermal layer be hardened beyond the old coarse-grid or opaque
adaptive-evaluator story, without pretending that the current-bank selector is
already theorem-grade closed?

## Answer

Yes, at support level.

The same-surface DM thermal factors admit exact positive-series
decompositions:

- `y/(1-e^{-y}) = sum_{n>=0} y e^{-n y}`
- `y/(e^{y}-1) = sum_{n>=1} y e^{-n y}`

The corresponding term integrals reduce exactly to:

- `J1(c) = ∫_0^∞ v e^{-a v^2 - c/v} dv`
- `J2(c) = ∫_0^∞ v^2 e^{-a v^2 - c/v} dv`

which are represented by exact Meijer-G expressions on the retained
`x_f = 25` slice.

The tails are controlled by exact inequalities:

- attractive tail: `tail_att(N) <= (1+y)e^{-N y}`
- repulsive tail: `tail_rep(N) <= (1+y)e^{-(N+1) y}`

so the remainder reduces again to exact `J1/J2` objects.

## Consequence

For the helper-defined live-DM sample points, the corrected high-precision
continuum evaluator is contained inside extremely narrow exact-series/tail
support intervals:

- `alpha_lo`
- `alpha_conv`
- `alpha_hi`

with ratio widths below `1e-9` on that slice.

On those conditional sample points the exact-series/tail intervals are:

- `alpha_lo = 0.090667836017286`
  - `R in [5.442019867867, 5.442019867931]`
- `alpha_conv = 0.090899546858439`
  - `R in [5.447934280692, 5.447934280753]`
- `alpha_hi = 0.092264992618360`
  - `R in [5.482855571890, 5.482855571936]`

So the DM thermal layer is now materially harder than before:

- the coarse selector story is gone
- the corrected continuum evaluator agrees with an exact positive-series
  decomposition plus exact tail control on the helper-defined sample points

## Honest Status

- current-bank DM selector closure: still open
- admitted DM-side selector: still support, not theorem-grade closure
- remaining blocker: supply retained authorities for the live-DM sample
  definitions and promote the thermal layer from support to a genuine
  theorem-grade evaluation/bounding result

## Command

```bash
python3 scripts/frontier_dm_full_closure_same_surface_thermal_series_tail_support.py
```

## Upstream authority

- [DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md](DM_FULL_CLOSURE_SAME_SURFACE_THERMAL_INTEGRAL_REPRESENTATION_THEOREM_NOTE_2026-04-16.md) — exact same-surface thermal integral form on the freeze-out slice `a = x_f / 4 = 25 / 4` whose positive-series decomposition is the load-bearing input for the `J1(c)`, `J2(c)` Meijer-G representations and the exact tail bounds.
- [DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md](DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md) — framework-applied normalization certificate for the underlying Maxwell-Boltzmann thermal-velocity average algebra and the Gaussian variable change `v -> sqrt(2T/m_chi) sqrt(t)` that puts the `J1/J2` integrals in canonical form. The Meijer-G bound implementation is a standard symbolic-integration evaluation on this canonical form.
