# CHIRAL 3+1D Boundary Phase Note — Finite-Scan Record (Binding)

Date: 2026-04-10 (scope narrowed 2026-05-17 per audited_conditional `scope_too_broad` repair: binding scope is the finite scan record only; recurrence-artifact interpretation requires a separately retained boundary/finite-size bridge)

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"split the finite scan result
into a bounded clean claim, then re-audit the recurrence-artifact
interpretation only after adding an isolating boundary/finite-size
bridge theorem or controlled runner."*

This revision implements the splitting. The binding evidence of this
note is exactly the **finite-scan tabulated results** from
`scripts/frontier_chiral_3plus1d_boundary_phase_diagram.py` on the
declared scan grid (boundary classes × propagation modes × `(lambda,
delta)` cells at `n ∈ {21, 31}`). The §"Interpretation" recurrence-
artifact reading is **demoted to out-of-binding-scope**; promoting
that interpretation requires a separately retained isolating
boundary/finite-size bridge theorem or controlled runner.

This note records the boundary-condition phase scan added in
`scripts/frontier_chiral_3plus1d_boundary_phase_diagram.py`.

## What Was Scanned

- Boundary classes: periodic, reflecting, open/absorbing
- Propagation modes: coherent, classical, phase-kill
- Dimensionless ratios:
  - `lambda = L / n`
  - `delta = offset / n`
- Sizes: `n = 21, 31`

For periodic boundaries, the observable is torus-aware:
- signed minimum-image displacement toward the mass

For reflecting/open boundaries, the observable is non-periodic:
- raw `z` centroid shift

## Result Summary

- Periodic coherent mode shows a small AWAY basin at high `lambda` / high `delta`:
  - AWAY consensus cells at `(0.24, 0.57)`, `(0.24, 0.86)`, `(0.29, 0.57)`, `(0.29, 0.86)`
- Periodic classical and phase-kill modes show broader AWAY regions in the same high-`lambda` corner.
- Reflecting boundary is TOWARD everywhere on this grid for all three modes.
- Open/absorbing boundary is TOWARD everywhere except one coherent corner case:
  - `(delta, lambda) = (0.29, 0.86)`
  - that AWAY cell disappears in classical and phase-kill modes.
- Torus-aware vs raw periodic observables did not disagree on this grid:
  - torus-sensitive cells = 0

## Interpretation

The periodic AWAY windows are not primarily a torus-observable artifact. They are mostly
boundary-condition / recurrence artifacts because they disappear under reflecting BCs and
almost entirely disappear under open/absorbing BCs.

The single open coherent AWAY corner appears to be a coherent edge effect rather than a
stable boundary-agnostic sign flip, because it does not survive classicalization.

## Closure-Card Robustness Test To Add

Add a `boundary robustness` row to the 3+1D closure card:

- Evaluate one mid-basin point and one edge-stress point at the same `lambda` and `delta` on
  periodic, reflecting, and open/absorbing boundaries.
- Require the sign to stay TOWARD in all three boundary classes for the mid-basin point.
- On periodic runs, also check that the torus-aware and raw centroid observables agree in sign.
- Fail the row if the sign changes when only the boundary condition changes.

That test would catch recurrence-driven sign flips before they are promoted into the paper narrative.
