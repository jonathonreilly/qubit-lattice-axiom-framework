# Wave-Retardation Schedule-Rate Sweep — Controlled Finite-Carrier Negative

**Date:** 2026-07-18 (source repair of the 2026-04-07 packet)
**Type:** bounded_theorem
**Status:** source-repaired bounded finite-carrier result; this note does not assert an audit disposition

## Claim

For the finite carrier and schedules defined below, the computed moving-field
versus instantaneous-comparator difference does **not** identify a single
monotone schedule-rate-only power law or a laboratory prediction card.

This is a statement about the named finite computations, not about every
possible discretization, a continuum limit, a universal retardation law, or a
physical laboratory observable.  One of the two controlled relative-gap
curves is monotone; that fact is reported rather than hidden.  Its raw
difference is non-monotone, and matched finite counterchecks show dependence
on trajectory location and post-motion buffer at fixed schedule rate/trajectory.

## Artifact chain

- primary runner:
  [`scripts/wave_retardation_velocity_sweep.py`](../scripts/wave_retardation_velocity_sweep.py)
- finite wave/comparator/beam helper:
  [`scripts/wave_retarded_gravity.py`](../scripts/wave_retarded_gravity.py)
- exact runner/helper-SHA cache:
  [`logs/runner-cache/wave_retardation_velocity_sweep.txt`](../logs/runner-cache/wave_retardation_velocity_sweep.txt)

Run all evidence classes with:

```bash
python3 scripts/wave_retardation_velocity_sweep.py --mode all
```

The `normal`, `independent`, and `hostile` modes are also separately
executable.  The tables below are live output from the repaired code.

**Controlled-result fingerprint:** `73717ea7d1cf5a8c8e88d3d19259d9b9d0b7b7948e0341a6593c4dbed95c53c8`

## Why the old packet failed

The pre-repair runner was replayed before editing.  With the corrected
discrete-Poisson helper already present on `main`, its first relative-gap
sweep was

`19.22%, 13.49%, 7.19%, 0.79%, 5.92%, 13.75%, 37.16%`,

and its second was

`35.74%, 42.22%, 33.41%, 36.82%, 44.46%, 44.15%, 77.08%`.

Those live values contradicted both old note tables and their printed slopes,
zero, sign flip, minimum, and equal-rate comparison.  More importantly, the
old alleged fixed-trajectory loop changed `NL`, recomputed onset as `NL//3`,
changed the final measurement layer, and continued moving beyond its nominal
endpoint.  Some runs overshot cell 0.  Thus it did not hold the advertised
controls fixed.  The old dated stdout is historical evidence only and is not
the source for any result below.

## Explicit finite carrier

The carrier is a numerical test object, not a new framework primitive or an
observable map.

| Quantity | Fixed value |
| --- | ---: |
| lattice layers `NL` | 78 (`t = 0,...,77`) |
| transverse spacing `H` | 0.5 |
| transverse half-width `PW` | 8 (source-cell boundary at `±16`) |
| maximum physical hop / angular weight | `MAX_D_PHYS=3`, `BETA=0.8` |
| source onset | `t = 10` |
| source start / endpoint | cell `6` / cell `0` |
| family / geometry seed | Fam1-like `seed=0`, `drift=0.20`, `restore=0.70` |
| field strength / beam number | `S=0.004`, `K=5.0` |
| moving field | the helper's finite leapfrog update |
| instantaneous comparator | discrete Dirichlet Poisson solve at each occupied source cell |
| SOR controls | `omega=1.8`, tolerance `1e-11`, maximum `20000` iterations |
| beam detector | intensity centroid on the explicitly named layer |
| relative-gap denominator | `max(abs(dM), abs(dI))`; undefined if both are at most `1e-10` |

The wave update used here has plane-wave dispersion

```text
sin^2(omega/2) = H^2 [sin^2(k_y/2) + sin^2(k_z/2)].
```

Its long-wavelength numerical propagation rate is therefore `H=0.5`
transverse cells per layer.  The source entries below are schedule rates in
cells per layer, not fractions of a physical light speed.  They range from
`0.2` to `1.5` times this numerical long-wavelength rate; the two fastest
schedules exceed it.  No continuum or laboratory normalization is supplied.

Before onset the schedule returns cell 6 but the source is off.  Let `D` be
the number of elapsed motion intervals.  The source is on at cell 6 on
`t=10`, reaches cell 0 on `t=10+D`, and is clamped at cell 0 on every later
layer.  At an intermediate layer `t`, the cell is

```text
6 + int(round((-6) * (t - 10) / D))
```

with elapsed time clamped to `[0,D]`; Python's ties-to-even `round` is part of
this finite schedule.  There are `D+1` on-trajectory samples, including both
endpoints.  The source stays strictly inside the `±16` boundary in every run.
No source boundary crossing occurs.

### Exact trajectory map

Run-length encoding `cell × number-of-sampled-layers` gives every sampled
position from onset through the endpoint:

| `D` | schedule rate (cells/layer) | endpoint layer | sampled positions | fixed-final buffer | fixed-buffer detector |
| ---: | ---: | ---: | --- | ---: | ---: |
| 60 | 0.100 | 70 | `6×6,5×9,4×11,3×9,2×11,1×9,0×6` | 7 | 77 |
| 30 | 0.200 | 40 | `6×3,5×5,4×5,3×5,2×5,1×5,0×3` | 37 | 47 |
| 20 | 0.300 | 30 | `6×2,5×3,4×4,3×3,2×4,1×3,0×2` | 47 | 37 |
| 15 | 0.400 | 25 | `6×2,5×2,4×3,3×2,2×3,1×2,0×2` | 52 | 32 |
| 12 | 0.500 | 22 | `6×2,5×1,4×3,3×1,2×3,1×1,0×2` | 55 | 29 |
| 10 | 0.600 | 20 | `6×1,5×2,4×2,3×1,2×2,1×2,0×1` | 57 | 27 |
| 8 | 0.750 | 18 | `6×1,5×1,4×2,3×1,2×2,1×1,0×1` | 59 | 25 |

This table also exposes a residual discretization change: the dwell counts
at integer cells necessarily change with `D`.  The realized displacement on
every elapsed layer is exactly the difference between successive RLE samples,
so each step is either 0 or -1 cell; no multi-cell jump occurs.

## Constraint fact: what cannot all be fixed

For fixed geometric endpoints,

```text
D = abs(end - start) / schedule_rate
measurement_layer = onset + D + post_motion_buffer.
```

Consequently, varying schedule rate while holding onset and endpoints fixed forces
`D` to vary.  If the measurement layer is fixed, the propagation buffer must
vary.  If the buffer is fixed, the measurement layer must vary.  A
one-dimensional sweep cannot simultaneously hold endpoints, onset, duration,
buffer, measurement time, and schedule rate fixed while changing schedule rate.  This is a
narrow parameter-constraint fact, not a statement that no redesigned or
higher-dimensional experiment can isolate a schedule-rate effect.

## Controlled results

`dM` and `dI` are detector-centroid changes relative to the same free beam.
`M-I` is signed.  Within every displayed row `dM` and `dI` have the same
nonzero sign, so no relative-gap denominator is near zero.  Sign reversals
*between* sweep rows are retained and disclosed below; absolute-value slopes
must not be read through those reversals as physical exponents.

### A. Fixed final detector layer 77

Onset, endpoints, lattice, carrier geometry, solver controls, and measurement
layer are fixed.  Schedule rate and duration vary together, and the buffer varies as
required by the identity above.

| `D` | schedule rate | endpoint | buffer | `dM` | `dI` | `M-I` | relative gap |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 | 0.100 | 70 | 7 | -0.007349 | -0.002555 | -0.004794 | 65.24% |
| 30 | 0.200 | 40 | 37 | -0.009959 | -0.004078 | -0.005881 | 59.05% |
| 20 | 0.300 | 30 | 47 | -0.009399 | -0.004345 | -0.005054 | 53.77% |
| 15 | 0.400 | 25 | 52 | -0.008722 | -0.004906 | -0.003816 | 43.75% |
| 12 | 0.500 | 22 | 55 | -0.009290 | -0.005610 | -0.003680 | 39.61% |
| 10 | 0.600 | 20 | 57 | -0.009658 | -0.005779 | -0.003880 | 40.17% |
| 8 | 0.750 | 18 | 59 | -0.010013 | -0.006321 | -0.003691 | 36.87% |

Both `abs(M-I)` and the relative gap are non-monotone.  Their log-log
diagnostic slopes are respectively `-0.198` and `-0.308`.  Because the data
are non-monotone and the buffer co-varies, these are shape diagnostics, not
scaling exponents.

### B. Fixed seven-layer post-motion buffer

Onset, endpoints, lattice, carrier geometry, solver controls, and buffer are
fixed.  Schedule rate and duration vary together, and the detector layer varies as
required.

| `D` | schedule rate | endpoint | detector | `dM` | `dI` | `M-I` | relative gap |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 | 0.100 | 70 | 77 | -0.007349 | -0.002555 | -0.004794 | 65.24% |
| 30 | 0.200 | 40 | 47 | +0.010738 | +0.004870 | +0.005868 | 54.65% |
| 20 | 0.300 | 30 | 37 | +0.011365 | +0.006249 | +0.005115 | 45.01% |
| 15 | 0.400 | 25 | 32 | +0.008619 | +0.004965 | +0.003654 | 42.40% |
| 12 | 0.500 | 22 | 29 | +0.006517 | +0.004068 | +0.002448 | 37.57% |
| 10 | 0.600 | 20 | 27 | +0.005160 | +0.003638 | +0.001523 | 29.51% |
| 8 | 0.750 | 18 | 25 | +0.003945 | +0.003134 | +0.000811 | 20.55% |

Here `abs(M-I)` is non-monotone while the relative gap is strictly
decreasing.  Their log-log diagnostic slopes are `-0.844` and `-0.512`.
The signed response reverses between schedule rates 0.100 and 0.200; no intervening
zero was located by this sample set.
The monotone relative-gap curve alone is not a schedule-rate-only scaling law:
measurement layer/duration still co-vary, the raw difference is non-monotone,
and the matched counterchecks below show dependence on other finite controls.

### C. Same trajectory and schedule rate, varied buffer

For `D=20`, schedule rate 0.300 cells/layer, onset 10, and trajectory 6 to 0, only the detector
layer/post-motion buffer changes:

| buffer | detector | `dM` | `dI` | `M-I` | relative gap |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 34 | +0.010995 | +0.006776 | +0.004219 | 38.37% |
| 7 | 37 | +0.011365 | +0.006249 | +0.005115 | 45.01% |
| 12 | 42 | +0.010451 | +0.005398 | +0.005053 | 48.35% |
| 20 | 50 | +0.004773 | +0.002336 | +0.002437 | 51.06% |
| 47 | 77 | -0.009399 | -0.004345 | -0.005054 | 53.77% |

The output therefore depends on the measurement/buffer choice even with the
source schedule and schedule rate fixed.  The signed response also reverses somewhere
between the sampled buffers 20 and 47; this scan does not locate a zero.

### D. Same schedule rate and timing, shifted trajectory geometry

At schedule rate 0.300 cells/layer, `D=20`, onset 10, detector 37, and buffer 7:

| source path | `dM` | `dI` | `M-I` | relative gap |
| --- | ---: | ---: | ---: | ---: |
| cell 6 to cell 0 | +0.011365 | +0.006249 | +0.005115 | 45.01% |
| cell 8 to cell 2 | +0.015095 | +0.010550 | +0.004545 | 30.11% |

The same displacement, schedule rate, duration, buffer, and measurement layer do not
give the same output after shifting the path in the finite transverse grid.
This is a finite geometry counterexample to a schedule-rate-only reading.

## Independent and hostile evidence

The independent mode reconstructs the seeded carrier, schedules, leapfrog
history, beam propagation, and detector readout as array operations without
calling the helper implementation.  It uses a factorized sparse-direct
Dirichlet Poisson solve instead of the normal SOR route.  It recomputes the
fixed-buffer `D=60,20,8` subset without importing result tables and agrees
within `3e-8` in `dM` and `dI`.

The hostile mode contains eight executable evidence objects.  It requires
fail-closed detection of continued post-endpoint motion, moving onset,
changing lattice size, and changing a purportedly fixed detector layer.  It
also compares every formatted table row and the live numerical fingerprint to
this note, verifies the exact runner and helper SHAs, cache status, and cached fingerprint,
rejects the superseded table fragments, exercises zero and opposite-sign
denominators, guards against power-law/lab-observable rhetoric, and mutates
the load-bearing equal-rate geometry comparison.  During cache creation the
guard recognizes the cache tool's in-progress log; a mandatory post-refresh
hostile replay then requires the completed exact-SHA cache.

Evidence counts emitted by `--mode all` are:

- normal: 21 displayed finite measurement rows, representing 20 unique
  measurements because the `D=20`, buffer-7 row appears in two controlled
  surfaces;
- independent: 3 separately reconstructed numerical records;
- hostile: 8 mutation or prose/data guards.

## Current-cycle N1-N8 evidence

### N1 — normalized real alternative routes

The current cycle marks the following routes `ATTEMPTED`: fixed-final detector
(`R3`), fixed post-motion buffer (`R4`), fixed-trajectory buffer scan (`R5`),
equal-rate shifted path (`R6`), and a separate array/sparse-direct numerical
implementation (`R7`).  Each route has a printed numerical outcome and a
named residual control.  The historical replays `R1` and `R2` are no-go
memory, not support for the current result.  Continuum refinement and an
independent laboratory-observable bridge are `UNTESTED` and excluded from the
bounded conclusion.

### N2 — independently shown walls only

The exact timing identity proves only the necessary duration/buffer/measurement
coupling.  The buffer scan independently shows finite readout-time dependence;
the shifted pair independently shows finite absolute-geometry dependence.
Neither wall implies the other.  A broader physical conclusion would also
require a controlled continuum construction and an observable bridge, but
those are open routes rather than inflated conclusions from these finite
walls.

### N3 — hidden-assumption scan

The result imports the finite leapfrog stencil, Dirichlet transverse boundary,
point-source coupling, integer-cell rounding, stationary endpoint clamp,
Fam1-like grown-DAG realization, path-sum beam propagation, centroid readout,
discrete Poisson comparator, SOR tolerance, sparse-direct residual threshold,
and the chosen source/detector schedule.  None is derived from the minimal
axioms in this packet.  There is no empirical calibration, physical speed,
physical phase map, continuum selector, or universal observable map.

### N4 — residual matching

The stale legacy tables and the old confounded schedule attack source
integrity and experimental design; they do not prove the repaired bounded
conclusion and are dropped as support.  The bounded conclusion instead rests
on the fresh controlled rows, exact timing identity, matched finite pairs, and
independent reconstruction.  It remains lattice- and schedule-specific and
does not rule out a continuum scaling, another discretization, a factorial
design with more independent degrees of freedom, or a physical model with a
supplied observable map.

### N5 — five resolution surfaces

- per-element: the rounded cell at every source layer is specified;
- per-site: all source cells are interior to the `±16` boundary;
- per-mode: no Fourier/mode-resolved scaling was computed, so no mode claim is
  made;
- per-block: the named moving-field/comparator/beam block is evaluated in the
  four controlled surfaces;
- lattice-wide: only the stated detector-layer centroid is read out.

### N6 — partial controlled closures and primitive check

Fixed final time closes measurement-time drift but leaves buffer coupled to
duration.  Fixed buffer closes buffer drift but leaves measurement time
coupled.  Equal-rate shifted geometry closes schedule rate/timing but changes
absolute path location.  The buffer scan closes the full source schedule but
changes readout time.  Their intersection supports the bounded conclusion and
nothing stronger.  The approved primitives do not supply a wave carrier,
continuum selector, or observable map, and this packet requires no new axiom;
redesigned factorial, continuum, and observable-bridge routes remain open.

### N7 — strongest steelman

The strongest live counterargument is that the fixed-buffer relative gap is
monotone across all seven schedule rates and might become part of a physical
model after measurement time is controlled independently.  That observation
does not defeat the narrower result here: measurement time co-varies in this
surface, the raw difference is non-monotone, and the matched buffer and
geometry routes show that the current residual-coupled rows do not identify a
schedule-rate-only law.  A preregistered factorial design remains an open
discriminator rather than a result of this packet.

### N8 — retired-wall and cross-cycle check

The prior version of this row was retired after its replay exposed stale
tables, moving controls, and an unclamped endpoint.  This cycle does not reuse
that failed wall as support: it repairs the controls and narrows the claim to
fresh common finite facts.  Similar finite-surrogate and missing-observable
walls elsewhere in the repository remain open; the already named reopening
mechanisms are a redesigned factorial harness, controlled continuum
refinement, and an independently validated observable bridge.  No approved
primitive or convention reviewed in this cycle retires those mechanisms.

## Boundary and dependency disposition

This row does not inherit or certify finite-c propagation, retarded gravity,
the old single-point magnitude, or any other wave lane.  Such claims require
their own sources.  Conversely, this packet supplies no premise to the
continuum-limit or retarded-gravity notes; their independent science must
stand on their own runners and sources.

The numerical carrier is not promoted to an axiom, admission, primitive,
physical input, empirical value, dependency authority, selector, or observable
map.  The table entries are only source schedule rates in cells per layer.
They are not normalized to a physical propagation constant or calibrated to a
laboratory speed.

An immutable generated front-door file may continue to list this claim until
publication governance is refreshed by its own process.  That listing is not
a conclusion of this note and was not edited in this repair.

## Strongest honest conclusion

The named finite computations fail to supply one monotone schedule-rate-only power
law or a unique laboratory card.  The fixed-final surface is non-monotone, the
fixed-buffer raw difference is non-monotone, and finite matched pairs establish
dependence on buffer/readout time and absolute trajectory location.  A
monotone relative-gap curve on one residual-coupling surface is reported as a
diagnostic, not promoted into a scaling exponent.

No statement is made about a continuum limit, a redesigned harness, a
universal retardation mechanism, or any laboratory observable.
