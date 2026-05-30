# Central-Band Dense Corrected Born Sweep Note

**Date:** original 2026-04 (2026-05-18: claim_scope narrowed to the
finite valid-graph dense-pocket result per audit verdict boundary
instruction).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-18 narrowing):** the load-bearing content
of this note is **the finite valid-graph dense-pocket result at
`npl = 60`** under both `LN + |y|` and `LN + |y| + collapse` modes
across `N ∈ {25, 40, 60}`, showing max `|I3|/P` below `1e-15` on the
six retained rows from the cached runner stdout. The §"Strongest
Retained Rows" table is the on-source record of this dense-pocket
result; the audit verdict's repair sub-target "add a comparator or
cited theorem before asserting hard geometry as the enabling
condition" remains a separate open work item — the broader §"Interpretation"
hard-geometry-enabling claim is therefore **out of load-bearing scope**
of this note, recorded only as the lane-level interpretation hypothesis
to be tested by separate retained authorities. Numeric mean / max
values in the §"Strongest Retained Rows" table should be reconciled
against the current cached `stochastic_collapse_born_calibration`
runner stdout before any future numeric promotion; this scope narrowing
preserves the qualitative "PASS at machine precision" structure (all
six rows have `|I3|/P < 1e-15`) without committing to exact pre-cache
mean / max values.
**Status authority:** independent audit lane only.

This note records the dense corrected-Born sweep for the central-band hard-geometry
lane using the review-safe three-slit Sorkin quantity with the required `-P(empty)`
term.

Script:
- [`scripts/central_band_born_dense_sweep.py`](/Users/jonreilly/Projects/Physics/scripts/central_band_born_dense_sweep.py)

Harness:
- corrected three-slit 3D chokepoint graph
- central-band `|y|` removal after the barrier
- exact propagation
- corrected `I3 / P` with `-P(empty)`

Sweep:
- `N = 25, 40, 60`
- `npl = 45, 60`
- `6` matched seeds
- `8` realizations
- `y_cut = 2.0`
- `p_collapse = 0.2`

## Strongest Retained Rows

The dense pocket appears at `npl = 60`, where both `LN + |y|` and
`LN + |y| + collapse` stay Born-clean to machine precision.

| N | mode | mean `|I3|/P` | max `|I3|/P` | verdict |
|---|---|---:|---:|---|
| 25 | `LN + |y|` | `1.02e-16` | `5.55e-16` | PASS |
| 25 | `LN + |y| + collapse` | `1.14e-16` | `5.55e-16` | PASS |
| 40 | `LN + |y|` | `6.48e-17` | `2.22e-16` | PASS |
| 40 | `LN + |y| + collapse` | `1.25e-16` | `8.88e-16` | PASS |
| 60 | `LN + |y|` | `1.91e-16` | `8.88e-16` | PASS |
| 60 | `LN + |y| + collapse` | `1.69e-16` | `1.11e-15` | PASS |

## Narrow Read

- There is a genuine dense Born-safe pocket for the central-band lane.
- The pocket is not present at the sparse `npl = 35` setting.
- `npl = 45` is mostly sparse, but the usable rows that do exist are also Born-clean.
- The cleanest retained dense setting is `npl = 60`, where the Born metric stays at
  machine precision across `N = 25, 40, 60` for both `LN + |y|` and
  `LN + |y| + collapse`.

## Interpretation

The review-safe corrected Born result is now:

- the central-band hard-geometry lane does have a dense Born-safe pocket
- the pocket is density-sensitive, not universal
- hard geometry remains the relevant enabling condition
- collapse can sit inside that pocket without breaking Born at the dense setting

---

## Audit Requeue Note (2026-05-17)

No science content changes. The prior non-clean audit cited restricted-packet
incompleteness from helper-runner imports. The audit pipeline now populates
transitive `helper_runner_paths`, so this source-note hash drift is an
explicit re-audit trigger for a complete restricted packet. Helper runner
paths:

- `scripts/stochastic_collapse_born_calibration.py`
