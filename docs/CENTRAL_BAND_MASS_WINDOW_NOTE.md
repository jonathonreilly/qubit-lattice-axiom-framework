# Central-Band Mass Window Note

This note records the gravity-side follow-up to the central-band hard-geometry
lane. The question is narrower than the full joint card:

- does the best retained hard-geometry row give a cleaner mass-response window
  than the plain baseline?

The summary script is:

- [`scripts/central_band_mass_window_summary.py`](/Users/jonreilly/Projects/Physics/scripts/central_band_mass_window_summary.py)

The intended comparison is on the same graphs and matched seeds:

- plain baseline
- baseline layernorm
- central-band pruned linear
- central-band pruned layernorm

The script keeps the comparison review-safe by:

- using fixed-graph matched seeds
- fixing one mass anchor on the gravity layer
- varying only the mass count `M`
- fitting only the declared positive window

This is a gravity-side summary only. Collapse is handled elsewhere by the
joint card, because including it here would mix a stochastic control into the
mass-law fit.

## What The Summary Shows

The bounded sweep was run at `N = 60`, `N = 80`, and `N = 100` with `16`
matched seeds, `npl = 25`, `y_range = 12.0`, `r = 3.0`, `y_cut = 2.0`,
`anchor_b = 5.0`, and the mass counts `M = 1, 2, 3, 5, 8, 12`. The fit window
is the declared positive subset `M in {2, 3, 5, 8}`.

The per-mode power-law fits on the declared fit window, taken directly from
the current runner stdout, are:

- `N = 60`
  - linear: not enough positive points for a stable fit
  - LN: not enough positive points for a stable fit
  - pruned linear: `delta ~= 0.8073 * M^-0.324` with `R^2 = 0.209`
  - pruned LN: `delta ~= 0.1320 * M^0.456` with `R^2 = 0.485`
- `N = 80`
  - linear: `delta ~= 0.3114 * M^-0.219` with `R^2 = 0.027`
  - LN: `delta ~= 0.2723 * M^0.186` with `R^2 = 0.121`
  - pruned linear: not enough positive points for a stable fit
  - pruned LN: `delta ~= 0.7859 * M^-0.220` with `R^2 = 0.602`
- `N = 100`
  - linear: `delta ~= 0.6096 * M^-1.175` with `R^2 = 0.634`
  - LN: `delta ~= 0.3198 * M^0.297` with `R^2 = 0.248`
  - pruned linear: `delta ~= 0.3802 * M^0.553` with `R^2 = 0.825`
  - pruned LN: `delta ~= 0.2207 * M^0.638` with `R^2 = 0.994`

The removed fraction on the pruned rows is `17.1%`-`17.2%` across the three
`N` values.

## Narrow Conclusion

The gravity-side answer is mixed but useful:

- on the densest slice `N = 100`, both pruned rows fit cleaner power laws
  than either plain mode: pruned LN reaches `R^2 = 0.994` and pruned linear
  reaches `R^2 = 0.825`, against `R^2 = 0.634` for plain linear and
  `R^2 = 0.248` for plain LN
- the cleanest retained mass fit in this sweep is the pruned LN row at
  `N = 100`, which has the best `R^2` of the four modes
- at `N = 60` and `N = 80` the picture is mixed: pruned LN at `N = 80` is
  cleaner than either plain mode, but neither pruned row is uniformly
  better than baseline across all three `N` slices
- this is still a bounded window, not a full gravity-law rescue

