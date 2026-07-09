# Wilson-Kernel Two-Band Identity Test -- Zone Obstruction Removed, O(a) Speed Artifact Measured, And The Volume Wall Demonstrated Directly

**Date:** 2026-07-08
**Type:** no_go (bounded methods negative, second kernel) with two
measured structural exhibits
**Claim type:** no_go
**Claim scope:** On the Wilson-kernel `d = 1` gauged comparator (import
I-GAUGE-W) at exact-diagonalization-reachable sizes (`N <= 10` Wilson
sites), the two-band mass-energy-equivalence identity test is NOT
executable as a gated measurement. The Wilson kernel removes the
staggered no-go's zone obstruction (measured: both bands' rest frames
at `P = 0` at every point, volume-stable) and the test proceeds much
further than on the staggered kernel -- four grid points pass tag,
origin, threshold, and fit validity with identity ratios `1.04-1.25` --
but the decisive volume leg refutes convergence: at the best point the
identity ratio moves from `1.04 (N = 8)` to `2.21 (N = 10)`. The
second meson's fitted dispersion is not volume-converged at reachable
sizes on EITHER kernel; near-1 identity values at single volumes are
finite-size accidents. This closes the ED route to the identity test
and names the tensor-network escape. Nothing here asserts the identity
fails; no gated predecessor result is touched. No audit status is set.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/wilson_two_band_identity_own_frame_2026_07_08.py`](../scripts/wilson_two_band_identity_own_frame_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/wilson_two_band_identity_own_frame_2026_07_08.txt`](../logs/runner-cache/wilson_two_band_identity_own_frame_2026_07_08.txt)

## Why This Note Exists

The staggered identity no-go named the Wilson kernel as its most direct
escape: no zone split, both meson bands resting at `P = 0`, doublers
gapped. This block executed that escape on the validated Wilson engine,
porting the own-frame protocol unchanged. The escape worked exactly as
far as advertised -- and exposed the deeper wall underneath.

## Measured Exhibit 1 -- The Zone Fix Worked

Band origins discovered from all-sector data: `(k*_1, k*_2) = (0, 0)`
at every gated point, both masses, all couplings `1.0-2.0`, agreeing
between `N = 8` and `N = 6` and at the `N = 10` spot. The staggered
zone-origin migration is confirmed to be a staggered-kernel artifact,
absent here by construction. (The two weak-coupling reported points
show `k*_2 = 1` with order-1 reflection asymmetry -- not zone
structure, but continuum pollution corrupting the argmin, printed.)

## Measured Exhibit 2 -- The Wilson O(a) Speed Artifact

The Wilson term is a dimension-five operator; its price is an `O(a)`
species-dependent correction to the emergent speed, visible exactly as
the textbook expansion predicts: the free-level band gives
`c^2 = 1 + m + O(p^2)`, and the measured band-1 values bracket it --
`c_1^2 = 1.12-1.19` at `m = 0.2` and `1.25-1.39` at `m = 0.4` at the
weaker couplings, relaxing toward and below `1` as the gauge
renormalization competes (`0.92 / 0.94` at `g = 1.7-2.0`). Consequence
for design: the staggered artifact-collapse gate (`1 - c^2 > 0`,
`O(a^2)` form) is structurally wrong for this kernel and was replaced
by the ungated WILSON-OA-ARTIFACT report.

## The Run (final form)

Own-frame protocol as in the staggered v3 runner: operator tags
(pseudoscalar `psi^dag sigma2 psi` for band-1, scalar
`psi^dag sigma3 psi` for band-2, role-decision at `P = 0`),
third-party dominance, all-sector origin discovery, own-frame
least-squares fits, threshold and fit-residual self-exclusion.
Grid: `m in {0.2, 0.4}`, gated `g in {1.0, 1.2, 1.4, 1.7}` (the
Wilson clean window is strong coupling -- band-2 deeply bound and
isolated), reported `g in {0.6, 2.0}`; `N = 8` main, `N = 6` stability
(printed COARSE-N6-FITS caveat), Wilson-rotor spot `3.4e-14`, engine
regression at print precision `4.8e-6`.

**How far it got.** Four of eight gated points fully pass tag +
origin + threshold + fit validity (`g in {1.4, 1.7}`, both masses) with
small band-2 fit residuals (`1.3e-3` to `6.6e-3`) and identity
diagnostics:

```text
    m = 0.2:  g = 1.4: ratio_I = 1.042, c21 = 0.863
              g = 1.7: ratio_I = 1.095, c21 = 0.840
    m = 0.4:  g = 1.4: ratio_I = 1.147, c21 = 0.809
              g = 1.7: ratio_I = 1.254, c21 = 0.750
```

This is materially further than the staggered comparator ever got (its
survivor count was one point, tag-invalid at the second size).

**Why it still fails (the decisive leg).** The `N = 6` stability
comparison cannot confirm any point (coarse-momentum fits; 0/8), and
the purpose-built `N = 10` volume spot at the best point
`(m = 0.2, g = 1.4)` REFUTES convergence outright:

```text
    ratio_I:  1.042 (N = 8)  ->  2.211 (N = 10)     drift 1.17, tol 0.10
    c21:      0.863 (N = 8)  ->  0.652 (N = 10)
```

with the `N = 10` band-2 tagged energies failing the own-frame rise
condition (`E(k=1) < E(k=0)`) and fit validity -- the same
continuum-pollution signature as the staggered weak-coupling wall, now
appearing at strong coupling as the volume grows and the two-meson
spectrum densifies around band-2. The near-1 values at `N = 8` are
finite-size accidents, exactly as the staggered note's honesty clause
anticipated for single-volume near-1 values.

## The Consolidated Negative (both kernels)

Across two kernels and five disciplined iterations: the two-band
identity test requires the second meson's DISPERSION (not just its
energy) to be volume-converged, and at every ED-reachable size the
band-2 state is within reach of the finite-volume two-meson spectrum --
below some coupling it mixes outright; above, its fitted inverse
curvature still moves at order one between adjacent volumes. The wall
is spectral density versus volume, not identification (solved by
tagging), not zone structure (solved by the Wilson kernel), not fit
methodology (own-frame, overdetermined, residual-gated).

## No-Go Discipline

- **Routes attempted:** staggered energy-ordered; staggered tagged
  (three iterations, separate note); Wilson tagged own-frame at the
  ported grid (run 1); Wilson at the physics-corrected strong-coupling
  grid with the N = 10 volume leg (run 2, final). Two spec bugs from
  run 1 (cache print tolerance; O(a^2) artifact gate on an O(a)
  kernel) fixed and documented.
- **Steelman:** "gate the four valid N = 8 points and report the
  identity as plausible." Rejected: the one point where volume
  convergence could be tested failed it by an order of magnitude over
  tolerance; gating the untested three would launder finite-size
  accidents into a claim.
- **Escapes (named):** (a) tensor-network/DMRG volumes (`d = 1`,
  `N ~ 40-100` is routine there; the two-meson density argument says
  band-2 needs volumes where its width-to-spacing ratio is resolved --
  this is THE route); (b) fit-free identity observables (form-factor /
  boost matrix elements) that need only `P = 0` states; (c) smeared
  variational tag bases to push the mixing scale down at fixed volume.
- **Boundedness:** scoped to the instrument class (ED dispersion fits,
  `N <= 10` Wilson / `N <= 16` staggered, these tags). The identity
  itself is untested, not refuted. The separation, universality,
  classification, and source-law results (#5067-#5071) are untouched.

## Boundaries

- `d = 1`; I-GAUGE-W inherited by citation; `W_MAX = 4` (spot 5).
- The O(a) artifact exhibit is a lattice-kernel statement, not a
  continuum claim; the free-level `1 + m` expectation is quoted at
  leading order only.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`GAUGED_WILSON_SCHWINGER_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_WILSON_SCHWINGER_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- the validated machinery.
- [`GAUGED_TWO_BAND_MASS_ENERGY_EQUIVALENCE_OPERATOR_TAGGED_NOTE_2026-07-08.md`](GAUGED_TWO_BAND_MASS_ENERGY_EQUIVALENCE_OPERATOR_TAGGED_NOTE_2026-07-08.md)
  -- the staggered no-go whose named escape this block executed.
- [`GAUGED_MESON_MASS_ENERGY_EQUIVALENCE_SEPARATION_NOTE_2026-07-08.md`](GAUGED_MESON_MASS_ENERGY_EQUIVALENCE_SEPARATION_NOTE_2026-07-08.md)
  -- the gated positive results this negative does not touch.

## Runner And Cache

Primary runner:
[`scripts/wilson_two_band_identity_own_frame_2026_07_08.py`](../scripts/wilson_two_band_identity_own_frame_2026_07_08.py)

Runner cache:
[`logs/runner-cache/wilson_two_band_identity_own_frame_2026_07_08.txt`](../logs/runner-cache/wilson_two_band_identity_own_frame_2026_07_08.txt)

Supervisor-executed runner result (final iteration):

```text
TOTAL FAIL TAGGING-FAILED elapsed=1874.67s
```

The pre-committed FAIL line is the deliverable: CHECK-07 (the `N = 10`
volume spot) is the load-bearing evidence, with CHECK-01/CHECK-05 ok
and the validity gates failing exactly as the anatomy above describes.

## Changelog

- **2026-07-08.** Two runs. Run 1 (ported staggered grid): zone fix
  confirmed; two supervisor spec bugs found (cache print tolerance
  1e-8 vs 6-digit cache; O(a^2) artifact gate on an O(a) kernel); the
  clean window identified at strong coupling where the ported grid had
  it reported-only. Run 2 (final, physics-corrected grid + N = 10
  volume leg, pre-committed to ship): four points fully valid at
  N = 8; the N = 10 spot refuted volume convergence at the best point;
  the bounded methods negative filed for the ED instrument class with
  the tensor-network escape named as THE route.
