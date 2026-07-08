# Two-Band Mass-Energy Equivalence Identity Test -- Operator-Tagged Bands, Measured Zone-Origin Migration, And A Bounded Methods No-Go At Reachable Sizes

**Date:** 2026-07-08
**Type:** no_go (bounded methods negative) with one measured structural
exhibit and the tagging method's positive legs recorded
**Claim type:** no_go
**Claim scope:** On the `d = 1` staggered Schwinger comparator (import
I-GAUGE) at ring sizes `N <= 16`, the tautology-free two-band
mass-energy-equivalence identity test -- gate
`(M_2 / M_1)(E_{0,1} / E_{0,2}) = 1` with each band fit in its own rest
frame -- is NOT executable as a gated multi-coupling measurement: the
validity window is squeezed shut from both sides, with at most one
transitional grid point surviving per species. This is a negative about
the INSTRUMENT at reachable sizes, not about the identity: nothing here
contradicts the gated separation and universality results of the
predecessor note. Alongside the negative, one structural fact is
measured and volume-stable: the second meson's band minimum migrates
from `P = 0` to the staggered zone edge `P = pi/2` as coupling grows,
with a mass-dependent flip point. Escapes are named. No audit status is
set.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/gauged_two_band_identity_operator_tagged_2026_07_08.py`](../scripts/gauged_two_band_identity_operator_tagged_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/gauged_two_band_identity_operator_tagged_2026_07_08.txt`](../logs/runner-cache/gauged_two_band_identity_operator_tagged_2026_07_08.txt)

## Why This Note Exists

The gauged separation note gated static-channel separation and
cross-species metric universality but deferred the identity-grade test:
band-2 could not be tracked by energy ordering (level crossings). This
block built the named repair -- operator-tagged band identification --
and ran the identity test through three disciplined iterations. The
tagging repair works; the identity test still does not gate at these
sizes, for measured reasons recorded here.

## Method (final form after three iterations)

- **Operator tagging:** band-1 identified by overlap with a
  momentum-projected covariant-current probe, band-2 by a staggered
  scalar-density probe, both computed against the global ground state;
  validity by third-party dominance (a band's tag weight must dominate
  every state OTHER than the two tagged bands by `2x`), with
  tag-collision and ambiguity self-exclusion.
- **Own-frame fitting:** each band's rest frame is discovered from the
  data (`k* = argmin` of the tagged band energy over all momentum
  sectors, clean-interior-minimum required); dispersion fits use four
  own-frame momenta `P' = pi d / n_cells`, `d = 0..3`, overdetermined
  least squares with printed residuals.
- **Validity discipline:** per-band tag validity in the sectors
  actually used; `N = 12` vs `N = 16` stability of the identity ratio
  (`<= 0.05`) with origin-location agreement across sizes (by momentum
  fraction); two-meson-threshold inclusion; fit-residual bounds;
  Wilson-rotor spot drift `3.7e-13`.
- Regression against the predecessor cache: exact sector energies to
  `0.0`, cache prints to `4.6e-06` (CHECK-01 ok).

## The Measured Squeeze (the negative's content)

**Side 1 -- weak coupling (`g <= 0.6`): continuum pollution.** Band-2
approaches the two-meson continuum; on the finite ring its tag weight
spreads over near-threshold scattering states and its energy is shifted
by avoided crossings. Symptoms, printed: tag validity fails, and the
identity ratio drifts between `N = 12` and `N = 16` by up to `1.9`
(true bound states converge exponentially; continuum-polluted states
shift like `1/L` -- the stability gate is doing exactly its job).

**Side 2 -- strong coupling (`g >= 0.8..1.0`): zone-origin migration
and narrow bands.** The measured exhibit: the tagged band-2 minimum
sits at `P = 0` at weak coupling and at the staggered zone edge
`P = pi/2` at strong coupling:

```text
    ORIGIN-SPLIT (band-1, band-2 origins per point, N = 16):
    m = 0.2:  g = 0.4, 0.5, 0.6, 0.8 -> (0, 0);  g = 1.0, 1.4 -> (0, 4)
    m = 0.4:  g = 0.4, 0.5, 0.6      -> (0, 0);  g = 0.8..1.4 -> (0, 4)
```

The flip point is mass-dependent, and the origin location agrees
between `N = 12` and `N = 16` at every point (`k* = 4` of 8 cells and
`k* = 3` of 6 cells are the same momentum fraction `1/2`). The
full-zone scans at `(m = 0.2, g = 1.4)` show a clean, reflection-
symmetric band with minimum `1.939` at the zone edge versus `2.116` at
`P = 0` (asymmetry `<= 1.1e-13`). Past the flip, band-2 fit in its own
frame is NARROW (strong quartic terms, own-frame fit residuals
`1e-2`-class versus band-1's `1e-4`-class), and its fitted inverse
curvature drifts across volumes by `0.2` to `1.5` -- a heavy,
tightly-bound lattice state that is not in the relativistic regime at
these spacings.

**The survivor count:** exactly one grid point per species sits between
the two failure modes, and even it fails cross-size band-2 tag validity
at `N = 12`. A trend gate needs at least two clean couplings per
species; the window at `N <= 16` contains at most one.

**Honest context, not claimable:** two isolated points land near the
identity (`ratio_I = 0.985` at `(m = 0.2, g = 1.0)` own-frame;
`0.983` at the continuum-polluted `(m = 0.2, g = 0.4)`), but the
across-coupling spread of the same diagnostic is order one
(`c21` series for `m = 0.2`: `0.94, 0.80, 0.57, 1.00, 1.81` across
`g = 0.4..1.4`), so near-1 values at scattered points carry no
evidential weight -- the instrument's systematic spread dominates.

## What The Block Did Establish (positive legs of the method)

- Operator tagging identifies both bands unambiguously wherever the
  states are discrete: 100 percent agreement with energy ordering
  in-window, band-2 scalar-tag separation up to `0.98` vs `0.002`,
  clean third-party dominance once the two tagged bands are allowed to
  share vector strength (the run-1 validity criterion punished
  form-factor physics; the repair is recorded in the changelog).
- The zone-origin migration of the second meson is a measured,
  volume-stable structural fact of the staggered comparator, and it
  retro-diagnoses the predecessor's level-crossing failure: band-2 was
  being tracked around the wrong momentum origin.
- The reported (ungated) cross-species band-2 own-frame metric ratios
  sit within `24` percent everywhere and within `6` percent at
  `g = 1.4`.

## No-Go Discipline

- **Routes enumerated and attempted:** (1) energy-ordered
  identification (predecessor; fails to level crossings); (2)
  operator-tagged identification at the `P = 0` frame with
  strict dominance (fails: validity criterion punished shared vector
  strength); (3) window-shifted grid with third-party dominance
  (fails: two-sided squeeze first measured); (4) own-frame fitting
  with data-discovered origins (final; fails: squeeze persists --
  continuum below, narrow-band fit fragility above).
- **Steelman:** "a smarter tag operator would fix it at `N = 16`."
  Response: tag ambiguity is not the binding constraint on either
  side -- at weak coupling the two-meson continuum is physically
  present at band-2's energy (no operator removes it from the
  spectrum), and at strong coupling the tagging already succeeds while
  the OWN-FRAME FIT drifts across volumes. The wall is spectral
  density and band narrowness, not identification.
- **Escapes (named, in decreasing directness):** (a) larger `N` --
  with the honest caveat that the continuum near band-2 gets DENSER
  with `N` while individual mixings weaken, so improvement must be
  measured, not assumed; (b) a Wilson-kernel comparator, where the
  scalar partner sits at `P = 0` and the zone split is absent by
  construction; (c) variational/smeared tag operators to sharpen
  band-2 against the continuum at weak coupling; (d) identity-grade
  observables that avoid dispersion fits entirely (form-factor or
  boost-matrix-element mass extractions).
- **Boundedness:** the negative is scoped to the INSTRUMENT (this
  comparator, these sizes, dispersion-fit methodology). It does not
  assert the identity fails; it does not touch the gated separation,
  metric-universality, or classification results of #5067/#5068.

## Boundaries

- `d = 1` staggered comparator; `N <= 16`; `W_MAX = 4` (spot-checked
  at 5); I-GAUGE inherited by citation.
- The zone-migration exhibit is a lattice-structure statement about
  this staggered realization, not a continuum claim.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`GAUGED_MESON_MASS_ENERGY_EQUIVALENCE_SEPARATION_NOTE_2026-07-08.md`](GAUGED_MESON_MASS_ENERGY_EQUIVALENCE_SEPARATION_NOTE_2026-07-08.md)
  -- the deferral this block attacked; its gated results are unaffected.
- [`GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- machinery.
- [`NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md`](NOETHER_SOURCE_CURRENT_CLASSIFICATION_BOUNDED_NOTE_2026-07-08.md)
  -- campaign sibling; unaffected by this negative.

## Runner And Cache

Primary runner:
[`scripts/gauged_two_band_identity_operator_tagged_2026_07_08.py`](../scripts/gauged_two_band_identity_operator_tagged_2026_07_08.py)

Runner cache:
[`logs/runner-cache/gauged_two_band_identity_operator_tagged_2026_07_08.txt`](../logs/runner-cache/gauged_two_band_identity_operator_tagged_2026_07_08.txt)

Supervisor-executed runner result (final iteration):

```text
TOTAL FAIL TAGGING-FAILED elapsed=1140.20s
```

with CHECK-01 (regression) and CHECK-05 (fit honesty) ok, and the
validity gates failing exactly as the squeeze anatomy above describes
(`own_frame_tag_origin_valid = 1/8`, `stable = 0/8`). The FAIL line IS
the deliverable: the gates were pre-committed and the instrument
reported its own limits.

## Changelog

- **2026-07-08.** Three iterations, each catching a real error or
  structure: (run 1) supervisor validity criterion punished the two
  mesons for sharing vector strength -- 0/6 despite 100 percent
  identification agreement; (run 2) window shifted weak, third-party
  dominance fixed; the two-sided squeeze first measured, and the
  all-sector zone exhibit revealed the band-2 origin at the zone edge;
  (run 3, final, pre-committed) own-frame fitting with discovered
  origins; origin migration confirmed volume-stable; squeeze persists;
  the bounded methods negative filed per the pack's pre-registered
  shape.
