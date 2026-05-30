# Central-Band Removal + Layernorm Note

Date: 2026-04-02

## Purpose

This note records the direct comparison between the simplest hard-geometry
rule from the gap thread and the current best Born-clean regulated propagator:

- remove post-barrier nodes with `|y - center| < y_cut`
- propagate on the same graph with per-layer normalization

The goal was to answer:

1. what `|y|` threshold works best?
2. how does the joint gravity/decoherence card scale from `N=25` to `N=100`?
3. how does this compare to the modular-gap + layernorm lane?

## Script

- [central_band_layernorm_combo.py](/Users/jonreilly/Projects/Physics/scripts/central_band_layernorm_combo.py)

## Main table

Settings:
- `nodes_per_layer = 25`
- `y_range = 12`
- `connect_radius = 3.0`
- `16 seeds`
- `N = 25, 40, 60, 80, 100`
- `y_cut = 1, 2, 3`

### Layernorm `pur_min`

Base layernorm row:
- `N=25`: `0.811`
- `N=40`: `0.801`
- `N=60`: `0.875`
- `N=80`: `0.948`
- `N=100`: `0.961`

Best pruned rows:
- `N=25`: `y_cut=2 -> 0.668`
- `N=40`: `y_cut=1 or 2 -> 0.734/0.736`
- `N=60`: `y_cut=2 -> 0.816`
- `N=80`: `y_cut=3 -> 0.881`
- `N=100`: `y_cut=2 -> 0.876`

So the strongest overall threshold on the decoherence side is:
- **`|y-center| < 2`**

## Joint gravity read

The threshold tradeoff is not identical on the gravity side.

### Strongest gravity-retaining pockets

- `N=40`, `y_cut=2`
  - layernorm gravity: `+1.664 ± 0.821`
  - about `2.0 SE`
- `N=80`, `y_cut=1`
  - layernorm gravity: `+1.668 ± 0.637`
  - about `2.6 SE`
- `N=80`, `y_cut=2`
  - layernorm gravity: `+1.440 ± 0.644`
  - about `2.2 SE`
- `N=100`, `y_cut=1`
  - layernorm gravity: `+1.022 ± 0.890`
  - positive but weaker

So the strongest gravity-preserving threshold at large `N` is usually:
- **`|y-center| < 1`**

## Scaling fit for the best overall threshold

Using the decoherence-optimal `y_cut = 2` layernorm row:

- `N=25`: `pur_min = 0.668`
- `N=40`: `0.736`
- `N=60`: `0.816`
- `N=80`: `0.887`
- `N=100`: `0.876`

Fit:

- `(1 - pur_min) = 4.81 × N^(-0.813)`
- `R^2 = 0.932`

Derived range estimates:
- `pur_min = 0.90` at about `N ≈ 117`
- `pur_min = 0.99` at about `N ≈ 1993`

## Modular gap=2 + layernorm fit (load-bearing, inlined 2026-05-18)

The comparison below requires the modular-gap=2 + layernorm row values and
the fit derived from them. Both sources are inlined here so the restricted
packet does not have to chase the dependency edge.

### Source — `geometry_lane_head_to_head.py` runner cache

The retained authority for the modular-gap=2 + layernorm row on the same
`16 seeds`, `npl=25`, `y_range=12`, `r=3.0`, `N=25..100` matched-seed grid is
the runner [`scripts/geometry_lane_head_to_head.py`](/Users/jonreilly/Projects/Physics/scripts/geometry_lane_head_to_head.py)
(which delegates to `scripts/combined_gravity_scaling.py:run_joint` with
`use_ln=True` on a `topology_families.generate_modular_dag(gap=2.0)` graph).
The cached stdout is at
[`logs/runner-cache/geometry_lane_head_to_head.txt`](/Users/jonreilly/Projects/Physics/logs/runner-cache/geometry_lane_head_to_head.txt).

Modular gap=2 + layernorm `pur_min` row from that cache (matched 16 seeds):

- `N=25`: `pur_min = 0.619 ± 0.024`  →  `1 - pur_min = 0.381`
- `N=40`: `pur_min = 0.769 ± 0.039`  →  `1 - pur_min = 0.231`
- `N=60`: `pur_min = 0.866 ± 0.029`  →  `1 - pur_min = 0.134`
- `N=80`: `pur_min = 0.852 ± 0.031`  →  `1 - pur_min = 0.148`
- `N=100`: `pur_min = 0.913 ± 0.025`  →  `1 - pur_min = 0.087`

### Fit (log-linear regression on the canonical row)

Fitting `log(1 - pur_min) = log A + β log N` on the five canonical points:

- `(1 - pur_min) = 8.75 × N^(-0.982)`
- `R^2 = 0.970`
- `pur_min = 0.90` at about `N ≈ 95`
- `pur_min = 0.99` at about `N ≈ 988`

(For reproducibility: the regression closed form on the five `(log N, log(1-pm))`
pairs above gives slope β = -0.982 and intercept log A = 2.169.)

### Provenance of an earlier (slightly different) fit in this note

The original 2026-04-02 comparison section quoted
`(1 - pur_min) = 6.94 × N^(-0.916)`, `R^2 = 0.957`, `N≈103`, `N≈1269`.
That fit pre-dates the canonical `geometry_lane_head_to_head.py` cache and
appears to have been performed against an earlier modular-gap=2 + layernorm
pilot row from `layernorm_modular_combined.py` (which sweeps `nl ∈ {25, 40,
60, 80}` only) plus a separate N=100 extension; matched-seed alignment with
the central-band `y_cut=2` row was only re-established under the head-to-head
runner. The two fits agree qualitatively (steeper exponent than central-band
`y_cut=2`, deeper extrapolation), and the comparative conclusion below holds
under either fit.

## Comparison to modular gap=2 + layernorm

The modular-gap row remains cleaner under both the 2026-04-02 and the
canonical 2026-05-18 fits:

| Fit source | A | β | R² | N at pur=0.90 | N at pur=0.99 |
|---|---|---|---|---|---|
| 2026-04-02 (this note, pilot data) | 6.94 | -0.916 | 0.957 | ≈103 | ≈1269 |
| 2026-05-18 canonical (geometry-lane head-to-head cache) | 8.75 | -0.982 | 0.970 | ≈95 | ≈988 |
| Central-band `y_cut=2` (canonical, this note) | 4.81 | -0.813 | 0.932 | ≈117 | ≈1993 |

Comparison (against the canonical modular-gap=2 row above):

- central-band `|y|<2` is **worse** at small `N=25` (`0.668` vs `0.619`)
- **better** around `N=40`, `N=60` (`0.736` vs `0.769`, `0.816` vs `0.866`)
- **better** at `N=80` (`0.887` vs `0.852`)
- **worse** at `N=100` (`0.876` vs `0.913`)
- has a **shallower exponent** (`-0.813` vs `-0.982`) but a longer
  extrapolated tail; modular-gap=2 reaches `pur_min = 0.90` faster (`N ≈ 95`
  vs `N ≈ 117`) but central-band's shallower exponent means the tail does
  not close as quickly at `pur = 0.99`.

Safe conclusion:
- the simple `|y|`-removal rule is **competitive** with the imposed modular
  gap once combined with layernorm
- but it does **not** clearly dominate modular gap=2 across the whole range

## Best supported wording

- `|y-center| < 2` is the best overall **decoherence** threshold
- `|y-center| < 1` is the best **gravity-preserving** threshold at larger `N`
- the lane is real and scales through `N=100`
- it is competitive with modular gap=2 + layernorm, but not an outright winner

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/combined_gravity_scaling.py`
- `scripts/generative_causal_dag_interference.py`
- `scripts/topology_families.py`

## Audit Repair Note (2026-05-18)

Adds the inline "Modular gap=2 + layernorm fit (load-bearing, inlined
2026-05-18)" section above. This addresses the 2026-05-17
`audited_conditional` verdict on `central_band_layernorm_note`, repair class
`missing_dependency_edge`: the comparative conclusion now has the
modular-gap=2 + layernorm row values and the fit calculation visible inside
the restricted packet, without requiring the reader to follow an external
dependency to the geometry-lane head-to-head row.

Additional dependency-edge runner / cached output for the modular-gap=2 + LN
fit:

- `scripts/geometry_lane_head_to_head.py`
- `logs/runner-cache/geometry_lane_head_to_head.txt`

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [geometry_lane_head_to_head_note](GEOMETRY_LANE_HEAD_TO_HEAD_NOTE.md)
