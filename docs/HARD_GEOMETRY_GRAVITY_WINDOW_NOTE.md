# Hard-Geometry Direct Gravity Window Note

**Date:** 2026-04-03 (scope narrowed 2026-05-26)
**Status:** bounded primary-runner direct-gravity maximum only
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Primary runner:** [`scripts/hard_geometry_gravity_window.py`](../scripts/hard_geometry_gravity_window.py)
**Primary runner cache:** [`logs/runner-cache/hard_geometry_gravity_window.txt`](../logs/runner-cache/hard_geometry_gravity_window.txt)

This note narrows the hard-geometry comparison to the direct evidence produced
by the primary runner. The previous version also compared mass-response fits
between central-band and generated-asymmetry sources; that mass-fit comparison
is removed from binding scope because the cited central-band mass authority has
the cleaner `R^2` value and does not support the old conclusion.

## Narrowed Claim

The bounded claim is now only:

> In the cached primary-runner sweep, the strongest Born-safe layer-normalized
> direct gravity pocket is the generated-asymmetry row
> `family=asym`, `threshold=0.05`, `scale=1.0`, `N = 100`, with
> `grav_ln = +2.297 +/- 0.486`, `grav_lin = +2.480`, `pur_min = 0.937`,
> `born_max = 6.66e-16`, and `ok = 6`.

This is a finite-runner window statement. It is not a mass-response theorem, a
universal hard-geometry law, or an asymptotic claim.

## Runner Evidence

The primary runner performs the same-window sweep over:

- `N = 60, 80, 100`
- central-band `y_cut = 1.0, 2.0, 3.0`
- generated-asymmetry thresholds `0.05, 0.10, 0.20`
- field scales `0.5, 1.0, 1.5`
- six seeds

The cached final summary reports:

```text
Best Born-safe LN gravity pocket
  family=asym, param=0.05, scale=1.0,
  grav_ln=+2.297+/-0.486, grav_lin=+2.480,
  pur_min=0.937, born_max=6.66e-16, ok=6
```

The row is kept as a bounded direct-gravity pocket because:

- the runner computes the gravity and Born controls directly
- the best row is Born-safe at the printed tolerance
- the layer-normalized gravity mean is positive with the printed finite-window
  standard error

## Removed From Binding Scope

The following are not part of this row's narrowed claim:

- central-band versus generated-asymmetry mass-response fit ranking
- any claim that generated asymmetry has the cleaner mass-response fit
- any universal hard-geometry carrier theorem
- any asymptotic gravity law
- any status upgrade of the central-band or generated-asymmetry source notes

## Plain-Text Context Pointers

These names are historical context only and are deliberately not markdown
links, so they do not become load-bearing dependency edges for this narrowed
row:

- `CENTRAL_BAND_DENSE_JOINT_NOTE.md`
- `CENTRAL_BAND_MASS_WINDOW_NOTE.md`
- `ASYMMETRY_PERSISTENCE_PILOT_NOTE.md`
- `ASYMMETRY_PERSISTENCE_MASS_WINDOW_NOTE.md`

## Citation-Graph Note

The load-bearing artifact for this narrowed row is the registered primary
runner and its SHA-pinned cache. No source-note dependency is required for the
removed mass-response comparison.
