# Flavor — qubit-factor Berry holonomy probe: pins to a topological winding ("w pin"), does not derive 2/9 or r=1/2

**Date:** 2026-05-30
**Claim type:** bounded negative (probe result, provisional).
**Status authority:** independent audit lane only; this note sets source metadata only.
**Runner:** `scripts/flavor_qubit_berry_holonomy_probe_2026_05_30.py` (SCORECARD PASS=4).
**Source:** the off-index next-path named by `FLAVOR_EQUIVARIANT_ETA_COMPLEMENTARITY_NOTE_2026-05-30`
(a non-index invariant nonzero exactly where η vanishes). Independently corroborated by a
sister-lane runner that bottomed out at a winding pin.

## Probe
The equivariant-η complementarity showed η is silent exactly on the R³⊗C² coin sector where
C₃-breaking is possible, and named the candidate replacement: a **qubit-factor Berry / holonomy
phase** — nonzero on degenerate-block adiabatic loops where η is blind, and natively radian-valued,
so a candidate to bridge the dimensionless-2/9 → radian-2/9 wall. Concrete test: the gauge-invariant
(Wilson-loop) Berry phase of the adiabatic loop `δ: 0→2π` of the mass-embedded circulant
`H(a, |b|e^{iδ})` on R³⊗C², where the complex coupling `b=|b|e^{iδ}` acts on the coin as the
in-plane Bloch rotation `|b|(cos δ·σ_x + sin δ·σ_y)`. Does it equal `2/9` (rad) and is it `r=1/2`-selective?

## Result — honest negative
- **B1 — pure phase loop (no gap):** Berry phase `= −π` for **every** `|b|`. It pins to a topological
  half-winding (a "**w pin**"), completely r-blind. Does not give 2/9 and does not select r.
- **B2 — native gap `a·σ_z` (the physical embedding, `r=|b|²/a²`):** the phase is continuous and
  r-selective, `|γ| = π(1 − 1/√(1+r))`. **At r=1/2 it is 0.5765 rad** — `−π(1−√(2/3))` — which is
  **not 2/9 in any normalization** (`2/9 rad`, `(2/9)π`, `(2/9)·2π` all missed). The value `2/9 rad`
  corresponds to `r ≈ 0.158`, and `(2/9)·2π` to `r ≈ 2.24` — neither is `r=1/2`. The holonomy does
  **not** pin `r=1/2`.
- **B3 — value-coincidence noted and dismissed:** the loop latitude obeys `cos²θ = 1/(1+r)`, which
  equals `Q = 1/3 + (2/3)r` **only at `r=1/2`** (both `2/3`). But these are different functions of `r`
  (one decreasing, one increasing); they merely **cross** at the point we are trying to derive. This is
  a value-coincidence, **not** a derivation of `r=1/2` (per the "no coincidences" discipline: a single
  crossing of two distinct functions is not a structural identity).

## Verdict
The qubit-factor Berry holonomy does not supply `2/9` or pin `r=1/2`. The pure-phase loop quantizes to
a topological winding (the sister-lane "w pin", here `−π`); the gapped loop is continuous and
r-selective but lands `0.5765 rad` at `r=1/2`, unrelated to `2/9`, and `2/9` selects a different `r`.
The off-index Berry route converges, once again, on the irreducible `r=1/2` / generation-chiral pin —
which it does not supply.

## Standing-instruction framing (not a closing claim)
This closes neither the search nor the radian-bridge question; it records that *this* holonomy
construction does not cross the wall. The bridge would require a holonomy whose latitude is itself
fixed (e.g. a native quantization of `θ`), rather than left free — the next thing to ask is whether
any native structure *quantizes the loop latitude* `θ` to `cos²θ=2/3` (equivalently fixes `r=1/2`),
which is exactly the standing pin restated in holonomy language. No native latitude-quantizer is known;
finding (or excluding) one is the open path.
