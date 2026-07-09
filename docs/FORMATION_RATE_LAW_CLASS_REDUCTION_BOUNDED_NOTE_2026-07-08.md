# The Formation-Rate Law Reduces To One Constant In The Weak Field -- Class Reduction, Measured Clock Contrast, And The Frozen-Pocket Exhibit

**Date:** 2026-07-08
**Type:** bounded_theorem (exact class reduction + seeded stochastic
comparator measurements)
**Claim type:** bounded_theorem
**Claim scope:** The axioms say records form and deliberately leave the
formation rate downstream. This note shows the downstream freedom is
one number in the weak field. For EVERY local covariant monotone rate
law `F(availability)` with the forced endpoint `F(0) = 0` (nothing
forms where nothing is admissible): (1) the normalized linear response
of the local event rate to crowding factorizes so that the law enters
only through the single dimensionless number `gF = F'(A0) A0 / F(A0)`
-- five representative laws collapse to `3e-11` after rescaling, and
differ only at second order; (2) in a seeded stochastic formation
process with a measured clock field, a pinned crowded region ticks
slower than an uncrowded one for every law (21 to 146 sigma), with the
one-constant collapse holding at 12-14 percent at finite contrast
(second-order-limited, as it must be); (3) in the axiom-faithful
permanent-record run, the event rate chokes monotonically to exactly
zero at saturation, and for a freezing-capable availability profile the
process TERMINATES AT 65 PERCENT OCCUPANCY with 70 sites frozen while
still open -- crowded pockets where formation has stopped before space
is full. The stochastic process and its resetting variant are declared
comparator devices, not a time metric or dynamics claim; no gravity
claim; sets no audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/formation_rate_law_class_reduction_2026_07_08.py`](../scripts/formation_rate_law_class_reduction_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/formation_rate_law_class_reduction_2026_07_08.txt`](../logs/runner-cache/formation_rate_law_class_reduction_2026_07_08.txt)

## Why This Note Exists

If the record-formation rate is to be the framework's clock-rate field,
the deliberately-open formation-rate slot must not smuggle in arbitrary
physics. This note shows it cannot: within the lawful class (local,
covariant, monotone, zero at zero availability -- the endpoint is
forced by one-record-per-site, not chosen), all weak-field content is
one constant. That is exactly the freedom a Newton constant occupies.

## Results

**T1 -- forced endpoint and exact collapse.** `F(0) = 0` for the class
by construction (zero availability means no formable record). For five
laws (linear, sqrt, quadratic, saturating, exponential) and three
availability profiles (linear, convex, freezing-capable): the
normalized crowding response `L = (d rate / d r) / rate` factorizes as
`gF x [A'(r0)/A0]`; after dividing by `gF` the five laws agree to
`3.1e-11` (machine-exact collapse, Richardson-checked). Second
derivatives genuinely differ (spreads `0.09` to `2.3`): the laws are
distinguishable, but only beyond the weak field.

**T2 -- measured clock contrast (seeded Gillespie comparator).** A ring
with a pinned crowded block versus an unpinned region, in the
stationary resetting variant (reset declared as the comparator device
that makes a stationary event rate measurable; the axioms' permanence
physics lives in T3): the crowded region's event rate per open site is
lower than the uncrowded region's for every law and both profiles, at
`21` to `146` sigma; the relative contrast divided by each law's `gF`
collapses across laws to `12-14` percent relative spread (gate 15;
finite-contrast second-order effects set the honest floor). The
measured version of T1.

**T3 -- saturation choke and the frozen-pocket exhibit (permanent
records, axiom-faithful).** With no reset, from 30 percent random
occupancy: the total event rate decreases monotonically as occupancy
grows and is exactly zero at saturation (linear profile: terminal
occupancy `1.000`). For the freezing-capable profile (availability
empty once both neighbors are recorded): the process TERMINATES at
occupancy `0.650` with `70` sites permanently frozen while still open
-- pockets whose neighborhoods are crowded enough that nothing can
ever register there again, although the sites themselves are
unrecorded. Formation time ends locally before space fills. This is
the owner's saturation mechanism running live, with the strong-crowding
endpoint arriving BEFORE full occupancy exactly when the availability
profile is of the census's freezing-capable class.

## Boundaries

- `d = 1` toy crowding model (two neighbors; availability profiles
  imported conceptually from the census note's classes); the process
  clock is a comparator device; the resetting variant is explicitly
  not axiom content.
- No specific rate law is chosen anywhere; every gated statement is
  class-wide. The identification of the event-rate field with a
  physical clock rate is block03's bridge, not made here.
- Statistical gates carry printed batch-mean errors; the seed is
  fixed (deterministic reproduction).
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) --
  the formation sentence and the open rate slot this note reduces.
- [`RECORD_SATURATION_AVAILABILITY_CENSUS_BOUNDED_NOTE_2026-07-08.md`](RECORD_SATURATION_AVAILABILITY_CENSUS_BOUNDED_NOTE_2026-07-08.md)
  -- the availability profiles and the constraint-class sign theorem.

## Runner And Cache

Supervisor-executed result:

```text
TOTAL: CLASS-REDUCED
```

Load-bearing residuals: exact collapse `3.1e-11`; clock contrasts at
`21-146` sigma with `gF`-collapse spread `12-14` percent; terminal
occupancies `1.000` (linear) and `0.650` with `70` frozen-open sites
(freezing-capable); monotone choke exact to zero at termination.

## Changelog

- **2026-07-08.** Initial note, single iteration; worker-drafted,
  supervisor-reviewed and supervisor-executed.
