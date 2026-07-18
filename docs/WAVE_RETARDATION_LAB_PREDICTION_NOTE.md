# Wave-Retardation Velocity Sweep — Controlled Finite-Carrier Negative

**Date:** 2026-07-18 (source repair of the 2026-04-07 packet)
**Type:** bounded_theorem
**Status:** source-repaired bounded finite-carrier result; this note does not assert an audit disposition

## Claim

For the finite carrier and schedules defined below, the computed moving-field
versus instantaneous-comparator difference does **not** identify a single
monotone velocity-only power law or a laboratory prediction card.

This is a statement about the named finite computations, not about every
possible discretization, a continuum limit, a universal retardation law, or a
physical laboratory observable.  One of the two controlled relative-gap
curves is monotone; that fact is reported rather than hidden.  Its raw
difference is non-monotone, and matched finite counterchecks show dependence
on trajectory location and post-motion buffer at fixed speed/trajectory.

## Artifact chain

- primary runner:
  [`scripts/wave_retardation_velocity_sweep.py`](../scripts/wave_retardation_velocity_sweep.py)
- finite wave/comparator/beam helper:
  [`scripts/wave_retarded_gravity.py`](../scripts/wave_retarded_gravity.py)
- exact-runner-SHA cache:
  [`logs/runner-cache/wave_retardation_velocity_sweep.txt`](../logs/runner-cache/wave_retardation_velocity_sweep.txt)

Run all evidence classes with:

```bash
python3 scripts/wave_retardation_velocity_sweep.py --mode all
```

The `normal`, `independent`, and `hostile` modes are also separately
executable.  The tables below are live output from the repaired code.

**Controlled-result fingerprint:** `5b212aa736207745110e303194c6fb90007d9fe08f4e32cd8bac587dd899f890`

## Why the old packet failed

The pre-repair runner was replayed before editing.  With the corrected
discrete-Poisson helper already present on `main`, its first relative-gap
sweep was

`19.22%, 13.49%, 7.19%, 0.79%, 5.92%, 13.75%, 37.16%`,

and its second was

`35.74%, 42.22%, 33.41%, 36.82%, 44.46%, 44.15%, 77.08%`.

Those live values contradicted both old note tables and their printed slopes,
zero, sign flip, minimum, and same-speed comparison.  More importantly, the
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

| `D` | speed (cells/layer) | endpoint layer | sampled positions | fixed-final buffer | fixed-buffer detector |
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
D = abs(end - start) / speed
measurement_layer = onset + D + post_motion_buffer.
```

Consequently, varying speed while holding onset and endpoints fixed forces
`D` to vary.  If the measurement layer is fixed, the propagation buffer must
vary.  If the buffer is fixed, the measurement layer must vary.  A
one-dimensional sweep cannot simultaneously hold endpoints, onset, duration,
buffer, measurement time, and speed fixed while changing speed.  This is a
narrow parameter-constraint fact, not a statement that no redesigned or
higher-dimensional experiment can isolate a speed effect.

## Controlled results

`dM` and `dI` are detector-centroid changes relative to the same free beam.
`M-I` is signed.  Within every displayed row `dM` and `dI` have the same
nonzero sign, so no relative-gap denominator is near zero.  Sign reversals
*between* sweep rows are retained and disclosed below; absolute-value slopes
must not be read through those reversals as physical exponents.

### A. Fixed final detector layer 77

Onset, endpoints, lattice, carrier geometry, solver controls, and measurement
layer are fixed.  Speed and duration vary together, and the buffer varies as
required by the identity above.

| `D` | speed | endpoint | buffer | `dM` | `dI` | `M-I` | relative gap |
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
fixed.  Speed and duration vary together, and the detector layer varies as
required.

| `D` | speed | endpoint | detector | `dM` | `dI` | `M-I` | relative gap |
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
The signed response reverses between speed 0.100 and 0.200; no intervening
zero was located by this sample set.
The monotone relative-gap curve alone is not a velocity-only scaling law:
measurement layer/duration still co-vary, the raw difference is non-monotone,
and the matched counterchecks below show non-speed dependence.

### C. Same trajectory and speed, varied buffer

For `D=20`, speed 0.300, onset 10, and trajectory 6 to 0, only the detector
layer/post-motion buffer changes:

| buffer | detector | `dM` | `dI` | `M-I` | relative gap |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 4 | 34 | +0.010995 | +0.006776 | +0.004219 | 38.37% |
| 7 | 37 | +0.011365 | +0.006249 | +0.005115 | 45.01% |
| 12 | 42 | +0.010451 | +0.005398 | +0.005053 | 48.35% |
| 20 | 50 | +0.004773 | +0.002336 | +0.002437 | 51.06% |
| 47 | 77 | -0.009399 | -0.004345 | -0.005054 | 53.77% |

The output therefore depends on the measurement/buffer choice even with the
source schedule and speed fixed.  The signed response also reverses somewhere
between the sampled buffers 20 and 47; this scan does not locate a zero.

### D. Same speed and timing, shifted trajectory geometry

At speed 0.300, `D=20`, onset 10, detector 37, and buffer 7:

| source path | `dM` | `dI` | `M-I` | relative gap |
| --- | ---: | ---: | ---: | ---: |
| cell 6 to cell 0 | +0.011365 | +0.006249 | +0.005115 | 45.01% |
| cell 8 to cell 2 | +0.015095 | +0.010550 | +0.004545 | 30.11% |

The same displacement, speed, duration, buffer, and measurement layer do not
give the same output after shifting the path in the finite transverse grid.
This is a finite geometry counterexample to a velocity-only reading.

## Independent and hostile evidence

The independent mode reconstructs the schedules without the normal schedule
class, spells the leapfrog update separately, and uses an independent
Gauss-Seidel (`omega=1`) Poisson solve instead of the normal SOR route.  It
recomputes the fixed-buffer `D=60,20,8` subset without importing result tables
and agrees within `3e-8` in `dM` and `dI`.

The hostile mode contains eight executable evidence objects.  It requires
fail-closed detection of continued post-endpoint motion, moving onset,
changing lattice size, and changing a purportedly fixed detector layer.  It
also compares every formatted table row and the live numerical fingerprint to
this note, verifies the exact-runner-SHA cache status and cached fingerprint,
rejects the superseded table fragments, exercises zero and opposite-sign
denominators, guards against power-law/lab-observable rhetoric, and mutates
the load-bearing same-speed geometry comparison.  During cache creation the
guard recognizes the cache tool's in-progress log; a mandatory post-refresh
hostile replay then requires the completed exact-SHA cache.

Evidence counts emitted by `--mode all` are:

- normal: 21 finite measurement records (two seven-row surfaces, one
  five-row buffer scan, and one two-row geometry pair);
- independent: 3 separately reconstructed numerical records;
- hostile: 8 mutation or prose/data guards.

## Current-cycle N1-N8 evidence

### N1 — real alternative routes

The cycle executes fixed-final and fixed-buffer surfaces, the buffer scan,
the shifted same-speed pair, normal SOR versus independent Gauss-Seidel, and
normal versus independently spelled leapfrog/schedule routes.  These are
numerical objects with printed values and tolerance comparisons, not route
names.  No continuum route was executed or closed.

### N2 — independently shown walls only

The exact timing identity proves only the necessary duration/buffer/measurement
coupling.  The buffer scan and shifted pair independently show finite
dependence on those two non-speed controls.  The note does not infer that all
possible controls matter or that no better carrier exists.

### N3 — hidden-assumption scan

The result imports the finite leapfrog stencil, Dirichlet transverse boundary,
point-source coupling, integer-cell rounding, stationary endpoint clamp,
Fam1-like grown-DAG realization, path-sum beam propagation, centroid readout,
discrete Poisson comparator, SOR/independent Gauss-Seidel tolerances, and the
chosen source/detector schedule.  None is derived from the minimal axioms in
this packet.  There is no empirical calibration, lab velocity, physical phase
map, continuum selector, or universal observable map.

### N4 — finite versus universal scope

The closure is lattice- and schedule-specific.  It does not rule out a
continuum scaling, another discretization, a factorial design with more
independent degrees of freedom, or a physical model with a supplied observable
map.

### N5 — five resolution surfaces

- per-element: the rounded cell at every source layer is specified;
- per-site: all source cells are interior to the `±16` boundary;
- per-mode: no Fourier/mode-resolved scaling was computed, so no mode claim is
  made;
- per-block: the named moving-field/comparator/beam block is evaluated in the
  four controlled surfaces;
- lattice-wide: only the stated detector-layer centroid is read out.

### N6 — partial controlled closures

Fixed final time closes measurement-time drift but leaves buffer coupled to
duration.  Fixed buffer closes buffer drift but leaves measurement time
coupled.  Same-speed shifted geometry closes speed/timing but changes absolute
path location.  The buffer scan closes the full source schedule but changes
readout time.  Their intersection supports the bounded conclusion and nothing
stronger.

### N7 — separate executable reconstruction

`--mode independent` neither imports normal result tables nor calls the normal
trajectory class, normal wave-history wrapper, or normal SOR comparator.  It
recomputes three discriminating rows and checks them numerically.  Shared beam
propagation/readout remains an explicitly disclosed common component.

### N8 — cross-cycle and fresh-route comparison

The pre-repair replay reproduced the latest failed-audit mismatch and the
confounded schedules above.  The repaired normal route then produced the four
current controlled surfaces and fingerprint, while the fresh independent
route reproduced the discriminating subset through separate schedule,
leapfrog, and Poisson implementations.  The conclusion was narrowed from old
mechanism and magnitude stories to the finite facts common to those routes.

## Boundary and dependency disposition

This row does not inherit or certify finite-c propagation, retarded gravity,
the old single-point magnitude, or any other wave lane.  Such claims require
their own sources.  Conversely, this packet supplies no premise to the
continuum-limit or retarded-gravity notes; their independent science must
stand on their own runners and sources.

The numerical carrier is not promoted to an axiom, admission, primitive,
physical input, empirical value, dependency authority, selector, or observable
map.  `v/c` in the tables is only the carrier speed in cells per layer under
the update convention `c=1`; it is not calibrated to a laboratory speed.

An immutable generated front-door file may continue to list this claim until
publication governance is refreshed by its own process.  That listing is not
a conclusion of this note and was not edited in this repair.

## Strongest honest conclusion

The named finite computations fail to supply one monotone velocity-only power
law or a unique laboratory card.  The fixed-final surface is non-monotone, the
fixed-buffer raw difference is non-monotone, and finite matched pairs establish
dependence on buffer/readout time and absolute trajectory location.  A
monotone relative-gap curve on one residual-coupling surface is reported as a
diagnostic, not promoted into a scaling exponent.

No statement is made about a continuum limit, a redesigned harness, a
universal retardation mechanism, or any laboratory observable.
