# y_t Lane: Zero-Import Authority

**Date:** 2026-04-17
**Type:** positive_theorem
**Status:** supported canonical-bare Ward-ratio core (no fitted or observational
SM inputs) + conditional Planck-surface and low-energy package
**Primary runner:** `scripts/frontier_yt_ward_identity_derivation.py` ([scripts/frontier_yt_ward_identity_derivation.py](../scripts/frontier_yt_ward_identity_derivation.py))
**Additional primary runner:** `scripts/frontier_yt_color_projection_correction.py`
**Supporting runners:** `scripts/frontier_yt_explicit_systematic_budget.py`,
`scripts/frontier_yt_exact_interacting_bridge_transport.py`,
`scripts/frontier_yt_boundary_consistency.py`
**Diagnostic context only:** `scripts/frontier_direct_yt_extraction.py`
(direct-bypass feasibility study; not authority for the bare-to-Planck lift or
the physical low-energy package)

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
  note carries the supported canonical-bare core and conditional physical
  package; the
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

These are the current strongest central values with no fitted or observational
SM inputs on the framework side. They are conditional central values: the
Planck-surface ratio requires the shared-dressing and physical-readout bridge,
and each low-energy value also uses the connected-trace factor `sqrt(8/9)`
under the selector condition stated below.

## Safe claim

The current package can safely say:

- the canonical-bare matrix-element ratio is exact on the bounded Ward
  surface: `y_t_bare / g_bare = 1 / sqrt(6)`
- conditional on an accepted shared-tadpole-dressing and physical-readout
  bridge, that bare ratio lifts to the Planck-surface statement
  `y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)`
- conditional also on the underived Yukawa-side selector `kappa_Y = 0`, the
  physical low-energy Yukawa is the Ward value times the connected-trace
  color-projection factor `sqrt(8/9)` — a conditional connected-trace
  specialization, not an unconditionally derived selector
- conditional on both named bridges, the low-energy `y_t` endpoint and the
  current `m_t` values are conditional central values with no fitted or
  observational SM inputs on the framework side
- the current precision caveat on the primary path is a standard-method
  residual budget, dominated by lattice-to-continuum 1-loop matching at the
  Planck interface plus standard SM RGE truncation, of order `~1.95%`
- the older Schur-coarse-bridge budget
  `1.2147511%` conservative / `0.75500635%` support-tight remains valid as an
  independent bridge-path cross-check, not as the load-bearing package
  qualifier on the primary lane

The package still cannot say that the renormalized `y_t` lane is a fully
framework-internal retained theorem from `M_Pl` to `v`.

## Conditionality of the Planck-surface and low-energy package

The exact unconditional Ward core carried by the primary runner is the
canonical-bare matrix-element ratio
`y_t_bare / g_bare = 1 / sqrt(6)`. Per the sibling Ward theorem, the
Planck-surface notation `y_t(M_Pl) / g_s(M_Pl) = 1 / sqrt(6)` additionally
requires an accepted shared-tadpole-dressing and physical-readout bridge. The
current primary runner records that lift as conditional context and attaches
no PASS/FAIL line to it.

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

- the canonical-bare Ward ratio `y_t_bare / g_bare = 1 / sqrt(6)` is the
  supported core of this note and depends on neither conditional bridge
- the Planck-surface ratio is conditional on the shared-dressing and
  physical-readout bridge, independently of the `kappa_Y` selector
- every low-energy quantity in this note that multiplies by `sqrt(8/9)` — the
  `y_t(v)` endpoint and both `m_t(pole)` central values — is conditional on
  both the Planck-surface bridge and `kappa_Y = 0`
- deriving `kappa_Y = 0` on the framework side remains an open target; this
  section records the current condition, not a closure of that derivation

## Why the lane is no longer carried by a framework-native explicit systematic

The live primary path is now:

1. exact canonical-bare Ward matrix-element ratio `1/sqrt(6)` on the bounded
   Ward surface
2. conditional lift of that ratio to the Planck surface (shared tadpole
   dressing plus physical readout)
3. conditional connected-trace color projection `sqrt(8/9)` (conditional on
   the underived selector `kappa_Y = 0`; see the conditionality section above)
4. standard lattice-to-continuum matching at the `M_Pl` interface
5. standard SM RGE running from `M_Pl` to `v`
6. standard pole-mass conversion

The remaining quantitative limitation is therefore not a framework-native
bridge systematic. It is the ordinary residual one would quote on any lattice
gauge-theory route that matches a lattice boundary condition onto the
continuum:

- sub-permille input precision on `g_s(M_Pl)` from the same-surface plaquette
  chain
- standard SM RGE truncation at the few-per-mille level
- standard lattice 1-loop matching at the `M_Pl` interface, which dominates
  the current budget

That leaves the lane as an exact canonical-bare Ward-ratio core plus a
**conditional Planck-surface and quantitative low-energy package** rather than
a retained theorem-grade UV-to-IR closure.

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
- an unconditional Planck-surface lift of the canonical-bare Ward ratio
- an unconditional derivation of the Yukawa-side selector `kappa_Y = 0` (the
  low-energy package is conditional on it)

So the right read is:

> the canonical-bare Ward ratio `y_t_bare/g_bare = 1/sqrt(6)` is the supported
> core; its Planck-surface lift is conditional on shared dressing and physical
> readout, and the renormalized low-energy `y_t` / `m_t` package is additionally
> conditional on the underived Yukawa-side selector `kappa_Y = 0`. No fitted or
> observational SM input is used on the framework side. The current primary
> precision caveat is a standard-method residual budget of order `~1.95%`, and
> the older Schur bridge survives as an independent cross-check with its own
> tighter but route-specific budget.
