# R1 Graviton-Mass Gate: the Emergent Graviton Is Massless — the "Graviton Mass" Is the de Sitter Curvature Gap (→0 Flat), So the Spin-2 Uniqueness Chain Applies

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** reconciliation + gate (resolves R1 of the graviton-diffeomorphism exercise portfolio)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set or predict an audit outcome.
**Primary runner:** [`scripts/r1_graviton_mass_gate_massless_2026_06_08.py`](../scripts/r1_graviton_mass_gate_massless_2026_06_08.py) (PASS=4).

## The gate

The /exercise on the deepest gravity atom (the λ=1 / diffeomorphism-invariant graviton) found that the
gravity sign reduces to a chain of **spin-2 uniqueness theorems** (Fierz–Pauli / Barnich–Henneaux /
Weinberg) that all require the graviton to be **massless**. The exercise's first gate (R1): *is the
emergent graviton massless (the chain applies) or does it carry a fundamental Fierz–Pauli mass (the chain
collapses)?* The concern: `GRAVITON_MASS_SPECTRAL_GAP_IDENTITY` and `GRAVITON_SPECTRAL_TOWER` appear to
give the graviton a mass. This note resolves it.

## The reconciliation (R1 PASSES)

The "graviton mass" of
[`GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE`](GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md) is
`m_g² = 2ℏ²Λ_vac/c² = 6ℏ²/(c²R²)`, `m_g = √6 ℏH₀/c² ≈ 3.5×10⁻³³ eV` — the **de Sitter / S³ curvature gap**
of the Lichnerowicz TT spectrum on the spatial 3-sphere of radius `R = c/H₀` (the Hubble radius). It is
**not** a fundamental Fierz–Pauli mass:

- **(R1a) Curvature gap, not a fundamental mass.** `m_g ∝ 1/R → 0` as `R → ∞` (the flat limit). The mass
  is a curvature effect (the lowest TT eigenvalue on a sphere), vanishing in flat space — the standard GR
  situation (a massless graviton whose lowest mode on de Sitter sits at the curvature scale `~H₀`).
- **(R1b) Massless where tested; only an IR de Sitter deviation.** The graviton Compton wavelength
  `λ_C = ℏ/(m_g c) = R/√6 ≈` the Hubble radius. The deviation from massless propagation is `~ r/R_Hubble`:
  `~10⁻²⁶` at the lab, `~10⁻¹⁵` at solar-system scales (where GR is *precisely* tested), `~10⁻⁵` at galaxy
  scales, `~10⁻³` at cluster scales, reaching `O(1)` only at the Hubble radius. This linear-in-`r/R_Hubble`
  IR effect is the **expected de Sitter / Λ modification**, tied to `H₀` — **not** a scale-independent
  fundamental mass.
- **(R1c) The derived 1/r independently requires masslessness.** The framework's weak-field linear-response
  closure ([`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE`](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md),
  `retained_bounded`) derives the point-source potential `G₀(r) → 1/(4πr)` — the **massless** Green's
  function. A fundamental mass `m` would replace it with the Yukawa `e^{−mr}/(4πr)`. This leg is
  **matter-route** and does **not** assume the Lichnerowicz / λ=1 structure, so it is an *independent*
  confirmation of a massless mediator.

**Verdict:** the emergent graviton is **massless** — no fundamental Fierz–Pauli mass; the only "mass" is
the de Sitter/S³ curvature gap (`~H₀`, `→0` flat, effectively massless on all sub-cosmological scales) and
it is consistent with the derived massless `1/r`. So the **massless hypothesis of the spin-2 uniqueness
theorems is satisfied** → **R1 PASSES, the chain applies** → proceed to R2 (does the lattice stress tensor
become exactly conserved in the continuum, forcing the spin-2 gauge invariance?).

## What is and is not claimed

- **Is:** the emergent graviton is massless (no scale-independent Fierz–Pauli mass); the
  `GRAVITON_MASS_SPECTRAL_GAP` value is the de Sitter/S³ curvature gap (`∝1/R`, `→0` flat, `~H₀`); the
  derived `1/r` independently requires a massless mediator; so the spin-2 uniqueness chain's masslessness
  hypothesis holds (R1 gate PASS).
- **Is not:** does **not** derive the de Sitter background or `H₀`; does **not** close the deeper λ=1 /
  diffeomorphism atom (that is R2–R4); does **not** claim the IR de Sitter deviation is observed; adds no
  axiom or fitted value. The `m_g` numeric inherits the cosmology-scale bound of its source note.

## Boundaries (honest)

- **The de Sitter-gap leg imports the Lichnerowicz TT spectrum** (the λ=1 / healthy-graviton structure —
  the very atom under investigation), so *that* leg is conditional on the structure being healthy. The
  **unconditional** leg is R1c (the derived `1/r` massless Green's function, matter-route). Both say
  massless; the gate passes on either reading.
- **The "spectral tower"** (`GRAVITON_SPECTRAL_TOWER`) is the discrete S³ TT harmonic tower (`∝1/R²`),
  which becomes the continuous massless flat-space spectrum as `R→∞`; it does not introduce a fundamental
  mass.

## Load-bearing inputs

- [`GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`](GRAVITON_MASS_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md)
  — the `m_g² = 6ℏ²/(c²R²)` de Sitter/S³ curvature-gap identity (the "graviton mass").
- [`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md`](GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md)
  — the derived massless `1/r` (the independent masslessness leg).

## Forbidden-imports check

No PDG / fitted value is derived. `ℏ`, `c`, `H₀` are standard constants used only to evaluate the cited
de Sitter-gap identity's magnitude and the Yukawa suppression; the `1/r` vs Yukawa contrast is standard
Green's-function physics. The Lichnerowicz TT spectrum is named as the comparator the source identity uses.
