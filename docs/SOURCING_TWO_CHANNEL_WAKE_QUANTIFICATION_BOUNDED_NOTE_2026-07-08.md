# Seeded Moving-Zone Record-Wake Measurements In A Supplied Stochastic Comparator

**Date:** 2026-07-08
**Type:** bounded_theorem
**Primary runner:**
[`scripts/sourcing_correlation_wake_quantification_2026_07_08.py`](../scripts/sourcing_correlation_wake_quantification_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/sourcing_correlation_wake_quantification_2026_07_08.txt`](../logs/runner-cache/sourcing_correlation_wake_quantification_2026_07_08.txt)

## Supplied Comparator

The runner supplies a one-dimensional stochastic ring with:

- a fixed linear availability table
  `A(0), A(1), A(2) = 2.1, 1.1, 0.1`;
- a supplied linear attempt law `F(A) = A`;
- a resettable background with reset rate `mu = 0.02`;
- a moving width-20 attempt-boost zone;
- a supplied in-zone permanence probability `p`; and
- fixed seeds, sizes, speeds, boosts, batch lengths, and normalizations printed
  by the runner.

The resettable background is a stationarity device. The separate saturation
leg turns background formation off and makes every in-zone deposit permanent.
Neither protocol is a framework formation law.

## Seeded Measurements

On the declared resettable protocol, the runner measures:

- the attempt-boost-normalized event density in the trailing and leading halves
  of the moving zone;
- the post-passage suppression relative to the seeded baseline;
- the dependence of that post-passage quantity on the supplied permanence
  probability `p`; and
- the two-speed finite-difference comparison summarized by the printed
  effective exponents.

On the declared permanent, background-off protocol, the runner measures:

- at most one deposit per site by construction;
- the six printed per-transit deposit counts and coverages;
- the corresponding non-invasive probe-field mean suppression and spatial
  standard deviation; and
- a separately reported high-boost one-transit saturation corner.

The gates certify only these seeded finite-protocol observations. The two-speed
exponents are summaries of the two simulated speeds, not an asymptotic law.

## Explicit Interpretation Boundary

The elevated activity zone is a supplied proxy for the optional
record-opportunity interpretation discussed in
[`ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md`](ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md),
which explicitly supplies rather than derives its `AO` interpretation
premise. This runner does not derive `AO`, a formation rule, or an
identification of the event-density field with a physical clock.

The measurements do not establish that a wake gravitates, that a source must
be deposition-sparse, or that a spatially uniform late-wake offset is a unit
convention. Those require separate physical bridges and are omitted.

## Boundaries

- One-dimensional supplied comparator; no continuum or infinite-time limit.
- One availability table and one attempt law.
- Seeded finite samples with standard errors computed across four independent
  replicate means; wake/front contrasts are paired within each seed.
- Resettable-background and background-off protocols answer different
  comparator questions and are not combined into a physical dynamics claim.
- No gravity, convention, or realized-source conclusion.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — context
  for permanent, site-locked records; it does not supply the comparator.
- [`ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md`](ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md)
  — the explicitly supplied `AO` activity-to-record-opportunity
  interpretation represented by the supplied moving zone.
