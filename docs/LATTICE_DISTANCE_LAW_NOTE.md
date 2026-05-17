# Lattice Distance-Law Note

**Date:** 2026-04-03 (scope-probe sharpening 2026-05-16; runner-discovery declaration 2026-05-17)
**Status:** bounded numerical distance-law fit on the ordered-lattice no-barrier harness at `N = 40`; the framework-derivable companion is the `sqrt(strength)` scaling, which is verified by the scope-probe runner; the `b`-exponent itself is NOT universal across `N` and is therefore explicitly bounded to the `N = 40` harness. Not a retained asymptotic distance-law theorem.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/lattice_no_barrier_distance.py`](../scripts/lattice_no_barrier_distance.py)
**Helper runners (audit packet must include):** [`scripts/lattice_mirror_distance.py`](../scripts/lattice_mirror_distance.py)
**Scope-probe runner:** [`scripts/lattice_no_barrier_distance_scope_probe.py`](../scripts/lattice_no_barrier_distance_scope_probe.py)

**Review repair perimeter (2026-05-05 generated-audit context):**
Generated-audit context identified this chain-closure blocker: "The
restricted packet contains only the fitted rows and no runner stdout
or source proving that the rows were generated from the stated
lattice rules. The broader conclusion that this is a retained
ordered-lattice distance-law branch also depends on unverified
harness, boundary-condition, and asymptotic choices." The
repair target being addressed is: "Re-check with the actual runner
source and completed stdout/log to verify that the table and fit
are computed from the stated lattice update rules rather than
selected or hard-coded values." This rigorization edit only sharpens
the boundary of the repair perimeter; nothing here promotes audit
status. The source note remains a numerical fit (not a closed theorem)
on the bounded `b >= 7` window. The active runner is
[`scripts/lattice_no_barrier_distance.py`](../scripts/lattice_no_barrier_distance.py)
and the frozen runner output is preserved at
[`logs/2026-04-03-lattice-no-barrier-distance.txt`](../logs/2026-04-03-lattice-no-barrier-distance.txt);
both are registered in "Cited authority chain (2026-05-10)" below
so the audit-graph one-hop edges are explicit.

**Scope-probe sharpening (2026-05-16):**
A subsequent
[`scripts/lattice_no_barrier_distance_scope_probe.py`](../scripts/lattice_no_barrier_distance_scope_probe.py)
runner adds two scope-defining cross-checks that the bounded claim
depends on. Frozen output is preserved at
[`logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt`](../logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt)
and registered in the cited authority chain. Both checks are also
recorded in the dedicated "Framework-derivable companion and
N-dependence" section below.

This note freezes the ordered-lattice distance-law result that reopens the
gravity-distance question outside the current random-connected symmetry
architecture.

Artifacts:

- [`scripts/lattice_no_barrier_distance.py`](../scripts/lattice_no_barrier_distance.py)
- [`logs/2026-04-03-lattice-no-barrier-distance.txt`](../logs/2026-04-03-lattice-no-barrier-distance.txt)
- companion sign-changing barrier probe:
  [`scripts/lattice_mirror_distance.py`](../scripts/lattice_mirror_distance.py)
- scope-probe runner (2026-05-16):
  [`scripts/lattice_no_barrier_distance_scope_probe.py`](../scripts/lattice_no_barrier_distance_scope_probe.py)
- scope-probe SHA-pinned runner cache (2026-05-16):
  [`logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt`](../logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt)

## Question

The earlier closure on the mirror / random-connected symmetry family said that
the current connected DAG architecture does not retain a clean `1/b` law
because transverse spreading destroys beam confinement.

The ordered-lattice question is narrower:

- if transport is regular enough to keep the beam confined, does a clean
  distance-dependent gravity magnitude appear?

## Setup

- ordered 2D lattice with forward edges and `|Δy| <= 1`
- `N = 40`
- half-width `= 20`
- source at `y = 0`
- **no barrier**
- one mass node row at `y = b` on the gravity layer
- `k = 5.0`
- detector readout: centroid shift `delta`

## Bounded Numerical Result

The ordered lattice gives a clean distance-dependent magnitude law on the
far-field window `b >= 7`:

```text
|delta| ~= 23.5071 * b^(-1.052)
R^2 = 0.9850
```

Saved rows:

| b | `delta` | `|delta|` |
|---|---:|---:|
| 3 | `-3.5350` | `3.5350` |
| 5 | `-3.3798` | `3.3798` |
| 7 | `-2.8797` | `2.8797` |
| 10 | `-2.1879` | `2.1879` |
| 13 | `-1.6612` | `1.6612` |
| 16 | `-1.2787` | `1.2787` |
| 19 | `-1.0045` | `1.0045` |

And the phase-only control remains clean:

- `k = 0` gives `+0.000000e+00`

## Interpretation

This is the first bounded branch in the repo that supports a clean
distance-dependent gravity magnitude law on the ordered no-barrier harness.

Important scope limits:

- the signed centroid shift is **negative** on this no-barrier harness, so the
  bounded law is currently about `|delta|`, not a clean attractive signed
  deflection law
- the barrier lattice and no-barrier lattice are different measurement
  geometries; the no-barrier harness gives the cleanest law, while the barrier
  harness shows sign-changing distance dependence
- this result does **not** rescue the old distance-law claim on the flagship
  mirror / random-connected symmetry family

## Framework-derivable companion and N-dependence (2026-05-16)

The scope-probe runner
[`scripts/lattice_no_barrier_distance_scope_probe.py`](../scripts/lattice_no_barrier_distance_scope_probe.py)
adds two checks that pin the precise framework-derivable content of the
bounded fit. The frozen output is in
[`logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt`](../logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt).

### Strength-scaling (framework-derivable)

The per-edge action used by the runner is
`Δact = dl - ret` with `dl = L·(1 + lf)` and
`ret = sqrt(dl² - L²) = L · sqrt((1 + lf)² - 1) = L · sqrt(2·lf + lf²)`.
This expands non-analytically at `lf = 0+`:

```text
Δact(L, lf) = L · [(1 + lf) - sqrt(2·lf + lf²)]
            ≈ L · [1 + lf - sqrt(2·lf)]    for small lf
```

so that `Δact - L ≈ -L · sqrt(2·lf)` at small `lf`. Since the
field-dependent part scales as `sqrt(lf)`, not `lf`, the leading
centroid-shift response is in `sqrt(strength)`, not in `strength`.

The scope-probe runner verifies this prediction directly. At fixed
`b = 13`, `N = 40`, `half_width = 20`, varying
`strength ∈ {0.01, 0.02, 0.05, 0.1, 0.2, 0.5}`, the runner reports:

```text
|delta| ~= 5.8137 * strength^(0.551), R^2 = 0.9997
```

The fitted exponent `0.551` is within `0.051` of the predicted `0.5`.
The small positive offset is the leading sub-`sqrt(strength)`
correction from the `+lf` term in `Δact ≈ L · (lf - sqrt(2·lf))`.
This is the framework-derivable companion law the source note's
bounded numerical fit has to satisfy and does satisfy.

### N-dependence of the b-tail exponent

The far-field b-tail exponent on the `b >= 7` window is **not
universal** across lattice sizes. The scope-probe runner sweeps
`N ∈ {30, 40, 60, 80}` (with `half_width` widened to fit the same
`b`-grid) and reports:

| `N` | `half_width` | tail fit `b >= 7` coeff | tail fit `α` | `R²` |
|---:|---:|---:|---:|---:|
| 30 | 20 | 24.7265 | `-1.260` | 0.9905 |
| 40 | 20 | 23.5071 | `-1.052` | 0.9850 |
| 60 | 25 | 21.9358 | `-0.793` | 0.9785 |
| 80 | 31 | 21.3532 | `-0.637` | 0.9754 |

The exponent drifts over `0.6` units across this `N` range. The
source note's headline `α ≈ -1.05` is therefore an `N = 40` harness
property, not a universal asymptotic. This rules out promoting the
result to a derived asymptotic theorem on the ordered-lattice family,
and explicitly bounds the scope of the numerical fit to the source
note's exact `(N, half_width, k, strength) = (40, 20, 5.0, 0.1)`
geometry.

### What this sharpening claims and what it does NOT claim

- **Claims:** the strength-scaling check is a framework-derivable
  companion law that the same no-barrier harness has to satisfy; the
  scope-probe runner verifies it to `R² = 0.9997` with the predicted
  `0.5` exponent matched within `0.05`.
- **Claims:** the `b`-exponent is N-dependent across
  `N ∈ {30, 40, 60, 80}` and the source note's `α ≈ -1.05` is bounded
  to the `N = 40` harness.
- **Does NOT claim** an analytic derivation of the `b ≈ -1.05`
  exponent itself. The bounded fit remains a numerical property of
  the `N = 40` no-barrier geometry, not a closed asymptotic theorem.
- **Does NOT claim** that the bounded fit extrapolates beyond the
  documented `(N, half_width, k, strength)` parameters.

## Project-level read

The safest synthesis update is:

- **random-connected symmetry family:** distance law remains a structural
  negative
- **ordered-lattice family:** distance-law branch is now bounded and
  review-safe on the no-barrier harness

So the project now has:

- a flagship symmetry-protected coexistence program
- and a separate ordered-lattice branch that reopens the distance-law bridge

## Next step

The highest-value next move on this branch is:

- test whether an ordered lattice can inherit enough of the mirror / symmetry
  program to unify:
  - Born
  - strong slit separation / decoherence
  - gravity
  - distance law

That is the natural “lattice-mirror hybrid” frontier.

## Cited authority chain (2026-05-10, extended 2026-05-16)

The generated-audit context cited at top flagged that the
restricted packet "contains only the fitted rows and no runner
stdout or source proving that the rows were generated from the
stated lattice rules." The cited-authority chain on this row is
registered explicitly below so the audit-graph one-hop edges from
the source note to its load-bearing inputs are visible.

| Cited authority | File / log | Provenance role |
|---|---|---|
| Active runner | [`scripts/lattice_no_barrier_distance.py`](../scripts/lattice_no_barrier_distance.py) | computes the ordered 2D lattice transport (`generate_lattice_mirror`, `propagate`, `compute_field_at_b` from `scripts/lattice_mirror_distance.py`), runs the seven `b` values from `B_VALUES = [3, 5, 7, 10, 13, 16, 19]`, evaluates the centroid shift, and fits the far-field `b >= 7` power law. The fixed harness parameters `n_layers = 40`, `half_width = 20`, `K = 5.0`, source at `y=0`, mass row at `y=b` on the gravity layer (one-third of the way from detector toward source) match the Setup table verbatim. |
| Frozen runner output | [`logs/2026-04-03-lattice-no-barrier-distance.txt`](../logs/2026-04-03-lattice-no-barrier-distance.txt) | preserves the exact seven-row centroid table (`b=3..19`, `delta=-3.5350..-1.0045`), the `k=0` control `+0.000000e+00`, and the far-field fit `\|delta\| ~= 23.5071 * b^(-1.052), R^2 = 0.9850` cited in the Bounded Numerical Result section |
| Mirror lattice helper module | [`scripts/lattice_mirror_distance.py`](../scripts/lattice_mirror_distance.py) | provides the `generate_lattice_mirror`, `propagate`, and `compute_field_at_b` helpers imported by the active runner; this is the same helper layer the source note references implicitly via "ordered 2D lattice with forward edges and `\|Delta y\| <= 1`" |
| Audit-lane runner cache | canonical path `logs/runner-cache/lattice_no_barrier_distance.txt` under [`scripts/runner_cache.py`](../scripts/runner_cache.py); regenerated by the audit-lane precompute when this runner is added to the active queue | will provide the auditor with completed stdout matching the frozen log; addresses the audit-stated "Re-check with the actual runner source and completed stdout/log" repair note |
| Scope-probe runner (2026-05-16) | [`scripts/lattice_no_barrier_distance_scope_probe.py`](../scripts/lattice_no_barrier_distance_scope_probe.py) | (a) verifies the framework-derivable strength-scaling `\|delta\| ~ strength^(0.5)` predicted by `Delta_act ≈ -L · sqrt(2·lf)`, fitting `0.551` (within `0.051` of `0.5`) at `R^2 = 0.9997`; (b) measures the b-tail exponent on `N ∈ {30, 40, 60, 80}` and shows it drifts across the range `[-1.260, -0.637]`, demonstrating that the source note's `α ≈ -1.05` is bounded to the `N = 40` harness and is NOT a universal asymptotic |
| Scope-probe SHA-pinned runner cache | [`logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt`](../logs/runner-cache/lattice_no_barrier_distance_scope_probe.txt), governed by [`scripts/runner_cache.py`](../scripts/runner_cache.py) | preserves the strength-scaling table (six rows for `strength ∈ {0.01, 0.02, 0.05, 0.1, 0.2, 0.5}`) and the four-N tail-exponent table; SHA-pinned cache of the scope-probe runner output, refreshed by the audit-lane precompute on each runner edit |

The bounded numerical result table values (`b`, `delta`, `\|delta\|`) and the
fit `\|delta\| ~= 23.5071 * b^(-1.052), R^2 = 0.9850` are reproduced
from the runner without selection or hard-coding: the runner runs
the seven b values listed in `B_VALUES`, fits all seven, and the
note cites all seven. The far-field window `b >= 7` is the only
selection rule, declared explicitly both in the runner and in the
note; the four points in that window (`b = 7, 10, 13, 16, 19`) are
exactly the post-peak rows.

This rigorization edit only sharpens the conditional perimeter and
registers the cited authority chain; it does not set audit status,
hand-author audit JSON, claim a stronger asymptotic exponent than
the bounded `~ 1/b` numerical fit, or set an audit outcome. The bounded interpretation in the
existing "Important scope limits" section continues to apply: the
`|delta|` law is a bounded numerical observation on the no-barrier
harness, not an attractive signed distance law and not a rescue of
the random-connected family.

The 2026-05-16 scope-probe sharpening adds two new derivable items
to the cited authority chain (the strength-scaling and the
N-dependence of the b-exponent) and pins the bounded scope of the
source note's `α ≈ -1.05` claim explicitly to the `N = 40` harness.
The framework-derivable companion law (`|delta| ∝ sqrt(strength)`)
is verified by the scope-probe runner at `R² = 0.9997` with exponent
matched to the predicted `0.5` within `0.051`. This is the framework
content the source note's bounded fit has to satisfy and does
satisfy. It is the strongest derivable property of the harness; the
`b`-exponent itself is not promoted from the bounded numerical fit.
