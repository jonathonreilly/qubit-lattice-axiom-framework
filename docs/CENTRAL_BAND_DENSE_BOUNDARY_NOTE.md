# Central-Band Dense Boundary Note

**Date:** 2026-04-03 (regenerated 2026-05-23)
**Status authority:** independent audit lane only
**Type:** bounded_theorem
**Scope:** Finite computational boundary sweep for the dense central-band
pocket at `N = 80, 100`, `npl = 60`, `y_cut = 2.0`, and
`connect_radius = 2.8..3.4`.

This note records a narrow radius sweep around the dense central-band
same-graph pocket and pins quantitative pass/fail criteria for the
"sharp boundary" claim against the runner stdout.

Script:
[`scripts/central_band_dense_boundary_sweep.py`](../scripts/central_band_dense_boundary_sweep.py)

## Runner Configuration

The reported tables are produced by the default invocation
`python3 scripts/central_band_dense_boundary_sweep.py`:

- `N = 80, 100`
- `npl = 60`
- `connect_radius = 2.8, 3.0, 3.2, 3.4`
- `y_cut = 2.0`, `yz_range = 12.0`
- `4` seeds (`seeds = [3, 10, 17, 24]`), `8` Monte Carlo realizations
- `p_collapse = 0.2`, `K_BAND = [3.0, 5.0, 7.0]`

The runner is deterministic at this configuration: two consecutive
invocations on 2026-05-23 produced byte-identical tables.

## Tables (regenerated 2026-05-23)

### `N = 80`

|  r   | mode | Born `|I3|/P` | `pur_min` / purity | gravity | g/SE | ok |
|-----:|------|--------------:|-------------------:|--------:|-----:|---:|
| 2.8 | `LN+|y|`            | `0.000±0.000` | `1.000±0.000` | `-0.020±0.000` |   FAIL | 1 |
| 2.8 | `LN+|y|+collapse`   | `0.000±0.000` | `0.928±0.000` | `-0.020±0.000` |   FAIL | 1 |
| 3.0 | `LN+|y|`            | `0.000±0.000` | `1.000±0.000` | `-0.458±0.137` |   -3.3 | 2 |
| 3.0 | `LN+|y|+collapse`   | `0.000±0.000` | `0.698±0.206` | `-0.498±0.072` |   -6.9 | 2 |
| 3.2 | `LN+|y|`            | `0.000±0.000` | `1.000±0.000` | `-0.685±0.465` |   -1.5 | 4 |
| 3.2 | `LN+|y|+collapse`   | `0.000±0.000` | `0.724±0.083` | `-0.641±0.443` |   -1.4 | 4 |
| 3.4 | `LN+|y|`            | `0.000±0.000` | `1.000±0.000` | `-0.010±0.313` |   -0.0 | 4 |
| 3.4 | `LN+|y|+collapse`   | `0.000±0.000` | `0.581±0.076` | `-0.119±0.400` |   -0.3 | 4 |

### `N = 100`

|  r   | mode | Born `|I3|/P` | `pur_min` / purity | gravity | g/SE | ok |
|-----:|------|--------------:|-------------------:|--------:|-----:|---:|
| 2.8 | `LN+|y|`            | `0.000±0.000` | `1.000±0.000` | `-0.007±0.000` |   FAIL | 1 |
| 2.8 | `LN+|y|+collapse`   | `0.000±0.000` | `0.496±0.000` | `-0.008±0.000` |   FAIL | 1 |
| 3.0 | `LN+|y|`            | `0.000±0.000` | `1.000±0.000` | `-0.044±0.000` |   FAIL | 1 |
| 3.0 | `LN+|y|+collapse`   | `0.000±0.000` | `0.732±0.000` | `-0.005±0.000` |   FAIL | 1 |
| 3.2 | `LN+|y|`            | `0.000±0.000` | `0.750±0.250` | `+5.210±5.218` |   +1.0 | 2 |
| 3.2 | `LN+|y|+collapse`   | `0.000±0.000` | `0.657±0.305` | `+5.087±5.095` |   +1.0 | 2 |
| 3.4 | `LN+|y|`            | `0.250±0.044` | `0.833±0.167` | `+0.056±0.246` |   +0.2 | 3 |
| 3.4 | `LN+|y|+collapse`   | `0.250±0.044` | `0.720±0.181` | `+0.058±0.244` |   +0.2 | 3 |

## Pass / Fail Criteria for "Sharp Boundary"

The "boundary is sharp" claim is decomposed into two operational predicates
that are pinned against the regenerated tables above:

### (P1) Mean-gravity sign flip across Δr ≤ 0.2

PASS at fixed `N` if the same-graph `LN+|y|` mean gravity changes sign
between two adjacent swept radii (`Δr = 0.2`), where both endpoints have
`ok ≥ 1`.

- `N = 100`: PASS. `LN+|y|` gravity goes from `-0.044` at `r = 3.0` to
  `+5.210` at `r = 3.2` — sign flip across `Δr = 0.2`.
- `N = 80`: FAIL. `LN+|y|` gravity stays negative across the full sweep
  (`-0.020`, `-0.458`, `-0.685`, `-0.010`). No sign flip in `2.8..3.4`.

### (P2) Concurrent Born-cleanliness degradation

PASS at fixed `N` if the radius at which P1 fires also exhibits a drop
of `pur_min/purity` by ≥ 0.15 relative to `r = 3.0` in the `LN+|y|` row.

- `N = 100`: PASS. `LN+|y|` purity goes from `1.000` at `r = 3.0` to
  `0.750±0.250` at `r = 3.2` — drop of `0.25`, exceeds 0.15 threshold.
  By `r = 3.4` the Born metric itself degrades to `0.250±0.044`.
- `N = 80`: not evaluated (P1 did not fire).

### Overall boundary verdict

- The sharp-boundary claim is supported **only at `N = 100`** by the
  current sweep, where both P1 and P2 fire at `r = 3.2`.
- At `N = 80` the sweep does not reach a sign flip in the probed window;
  gravity remains negative across `r = 2.8..3.4` and Born stays clean.
  The "sharp boundary" predicate is not satisfied at `N = 80` in the
  sampled radius range.

## Narrow Conclusions

- The dense central-band pocket is not broadly extendable by tweaking
  `connect_radius` at `N = 100`: a single `Δr = 0.2` step away from
  `r = 3.0` flips gravity sign and degrades Born cleanliness (P1+P2 fire).
- At `N = 80` the same radius window stays in the negative-gravity,
  Born-clean basin; the boundary is not visible inside `2.8..3.4`.
- The `r = 3.0` family remains the most Born-stable across both `N`
  values, but its gravity magnitude at `N = 100` is small
  (`-0.044±0.000` from a single retained seed) — too thin to declare a
  gravity winner at `N = 100`.
- All quantitative claims here are bounded to the specific finite
  configuration listed under "Runner Configuration" and do not generalize
  beyond it.

## Reproducibility

To regenerate:

```
python3 scripts/central_band_dense_boundary_sweep.py
```

Expected wall time on 2026-05 reference hardware: ~52 seconds.
