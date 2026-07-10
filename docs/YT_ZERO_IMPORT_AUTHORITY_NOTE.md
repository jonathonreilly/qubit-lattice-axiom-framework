# y_t Lane: Zero-Import Authority

**Date:** 2026-04-17
**Status:** derived lattice-scale Ward-ratio core (zero external observables) + conditional low-energy package (conditional on the underived Yukawa-side selector `kappa_Y = 0`)
**Primary runner:** `scripts/frontier_yt_ward_identity_derivation.py` ([scripts/frontier_yt_ward_identity_derivation.py](../scripts/frontier_yt_ward_identity_derivation.py))
**Additional primary runner:** `scripts/frontier_yt_color_projection_correction.py`
**Supporting runners:** `scripts/frontier_yt_explicit_systematic_budget.py`,
`scripts/frontier_yt_exact_interacting_bridge_transport.py`,
`scripts/frontier_yt_boundary_consistency.py`,
`scripts/frontier_direct_yt_extraction.py`

## Authority role

This is the canonical authority note for the zero-import renormalized `y_t`
lane on `main`.

Use this note together with:

- `YT_WARD_IDENTITY_DERIVATION_THEOREM.md` (sibling/companion derivation;
  cross-reference only — not a one-hop dep of this note. The Ward theorem
  cites this note's vertex-power line, not vice versa.)
- [ALPHA_S_DERIVED_NOTE.md](./ALPHA_S_DERIVED_NOTE.md)
- [YT_COLOR_PROJECTION_CORRECTION_NOTE.md](./YT_COLOR_PROJECTION_CORRECTION_NOTE.md)
- `YT_FLAGSHIP_BOUNDARY_NOTE.md`
- `YT_EXPLICIT_SYSTEMATIC_BUDGET_NOTE.md` (see-also cross-reference;
  backticked to break cycle-0011 (length-8 yt-cluster ring through
  zero_import -> explicit_budget -> exact_schur -> coarse_grained ->
  uv_class_uniqueness -> constructive_uv -> interacting_locality ->
  boundary_theorem -> zero_import) in the citation graph. This authority
  note is the canonical retained zero-import endpoint surface; the
  explicit-systematic-budget note is a downstream cross-check whose own
  dependency-repair list already foreswears citing this authority note as
  upstream (see its trailing cycle-break comment). The load-bearing
  citation direction runs from the cross-check back to this authority,
  not vice versa.)

Do not treat older backward-Ward / route-history notes as competing authority.

## Current strongest package read

| Observable | Framework result | Comparator | Deviation |
|---|---|---|---|
| `y_t(v)` | `0.9176` | `~0.917` | `+0.06%` |
| `m_t(pole)` 2-loop | `172.57 GeV` | `172.69 GeV` | `-0.07%` |
| `m_t(pole)` 3-loop | `173.10 GeV` | `172.69 GeV` | `+0.24%` |

These are the current strongest zero-external-observable central values on the
renormalized `y_t` lane. They are conditional central values: each one
multiplies the exact Ward core by the connected-trace factor `sqrt(8/9)`,
whose selector condition is stated below.

## Safe claim

The current package can safely say:

- the lattice-scale Yukawa-to-gauge ratio is exact on the canonical surface:
  `y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)`
- conditional on the underived Yukawa-side selector `kappa_Y = 0`, the
  physical low-energy Yukawa is the Ward value times the connected-trace
  color-projection factor `sqrt(8/9)` — a conditional connected-trace
  specialization, not an unconditionally derived selector
- conditional on that same selector, the low-energy `y_t` endpoint and the
  current `m_t` values are conditional central values with zero external SM
  observables on the framework side
- the current precision caveat on the primary path is a standard-method
  residual budget, dominated by lattice-to-continuum 1-loop matching at the
  Planck interface plus standard SM RGE truncation, of order `~1.95%`
- the older Schur-coarse-bridge budget
  `1.2147511%` conservative / `0.75500635%` support-tight remains valid as an
  independent bridge-path cross-check, not as the load-bearing package
  qualifier on the primary lane

The package still cannot say that the renormalized `y_t` lane is a fully
framework-internal retained theorem from `M_Pl` to `v`.

## Conditionality of the low-energy package

The color-projection factor `sqrt(8/9)` enters the low-energy package as a
conditional connected-trace specialization, not as an unconditionally derived
selector. Per
[YT_COLOR_PROJECTION_CORRECTION_NOTE.md](./YT_COLOR_PROJECTION_CORRECTION_NOTE.md),
the connected-trace value `K_Y(0) = 8/9` is the specialization of the color
projection to the Yukawa-side selector `kappa_Y = 0`, and that selector is not
derived in this packet: the cited SU(3) Fierz/channel-count authority plus
color-blind scaling do not by themselves fix `kappa_Y = 0` or an unconditional
`sqrt(8/9)` correction.

Consequently:

- the lattice-scale Ward ratio `y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)` is the
  supported core of this note and does not depend on the selector
- every low-energy quantity in this note that multiplies by `sqrt(8/9)` — the
  `y_t(v)` endpoint and both `m_t(pole)` central values — is conditional on
  `kappa_Y = 0`
- deriving `kappa_Y = 0` on the framework side remains an open target; this
  section records the current condition, not a closure of that derivation

## Why the lane is no longer carried by a framework-native explicit systematic

The live primary path is now:

1. exact lattice-scale Ward theorem on the retained theory
2. conditional connected-trace color projection `sqrt(8/9)` (conditional on
   the underived selector `kappa_Y = 0`; see the conditionality section above)
3. standard lattice-to-continuum matching at the `M_Pl` interface
4. standard SM RGE running from `M_Pl` to `v`
5. standard pole-mass conversion

The remaining quantitative limitation is therefore not a framework-native
bridge systematic. It is the ordinary residual one would quote on any lattice
gauge-theory route that matches a lattice boundary condition onto the
continuum:

- sub-permille input precision on `g_s(M_Pl)` from the same-surface plaquette
  chain
- standard SM RGE truncation at the few-per-mille level
- standard lattice 1-loop matching at the `M_Pl` interface, which dominates
  the current budget

That leaves the lane as an exact Ward-ratio core plus a **conditional
quantitative low-energy package** rather than a retained theorem-grade
UV-to-IR closure.

## What the Schur-bridge stack becomes

The Schur-coarse-bridge program is not retracted. It remains useful and
nontrivial:

- it gives an independent route from the lattice Ward boundary toward the same
  low-energy endpoint
- its higher-order and nonlocal tails remain a real quantified bridge-path
  budget
- agreement of that bridge path with the Ward-primary path is a meaningful
  cross-check on the framework

But those bridge tails are no longer the package's load-bearing reason to mark
the primary YT lane as explicit-systematic.

## Honest boundary

The current package does **not** claim:

- a fully framework-internal continuum-limit theorem on this specific
  composite-Higgs Wilson-staggered surface
- a theorem-grade elimination of all UV-to-IR transport residuals
- a practical direct-lattice bypass that measures `y_t(v)` on accessible
  lattices
- an unconditional derivation of the Yukawa-side selector `kappa_Y = 0` (the
  low-energy package is conditional on it)

So the right read is:

> the exact lattice-scale Yukawa/gauge normalization is retained, the
> renormalized low-energy `y_t` / `m_t` lane is a conditional package —
> conditional on the underived Yukawa-side selector `kappa_Y = 0` — with zero
> external SM observables on the framework side, the current primary precision
> caveat is a standard-method residual budget of order `~1.95%`, and the older
> Schur bridge survives as an independent cross-check with its own tighter but
> route-specific budget.
