# The Two Sourcing Channels Quantified -- Co-Moving Clock Dip, Permanent Wake, And The Deposition-Sparsity Constraint

**Date:** 2026-07-08
**Type:** bounded_theorem (seeded stochastic comparator measurements;
the wake corollary itself is axiom-forced)
**Claim type:** bounded_theorem
**Claim scope:** Record permanence forces a structural consequence the
sourcing story must own: activity that deposits permanent records
leaves a permanent crowding trail. This note measures both sourcing
channels in the campaign-5 stochastic comparator with a moving
elevated-activity zone: (1) the co-moving channel -- the
availability-normalized clock dips under and behind the zone (crowding
builds on the trailing side, `5.8-9.3` sigma); (2) the cumulative
channel -- after passage, the permanent trail suppresses the clock
along the path, with strength lawful in exactly the two parameters it
should have: monotone in deposition-per-transit (`R_wake` from `~0` at
zero permanence through `0.07-0.29` at 10 percent to `0.36-1.0` at 50
percent) and decaying with zone speed on the dwell-time scaling
(`S_after ~ v^-alpha`, `alpha = 0.64-1.09`); the zero-deposition
control shows no wake (sub-sigma). CONSEQUENCE (the constraint this
buys): Newtonian-shaped phenomenology -- gravity that follows its
source -- requires the realized formation rule to be
DEPOSITION-SPARSE (records rare per unit activity); a
deposition-heavy rule predicts gravitational-memory-like permanent
trails instead. Either branch is falsifiable in-framework; no branch
is chosen here. Comparator devices declared; sets no audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/sourcing_correlation_wake_quantification_2026_07_08.py`](../scripts/sourcing_correlation_wake_quantification_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/sourcing_correlation_wake_quantification_2026_07_08.txt`](../logs/runner-cache/sourcing_correlation_wake_quantification_2026_07_08.txt)

## Boundaries

- The moving elevated-activity zone models "formation opportunity is
  elevated where energy acts" (licensed by the support-half note); the
  permanent-fraction parameter `p` is the comparator's handle on
  deposition-per-transit; the resetting background is the declared
  stationarity device (campaign-5 conventions, seed fixed).
- The availability-normalized clock (events per open site per nominal
  time, divided by the imposed attempt boost) isolates the crowding
  channel by construction; declared loudly in the runner.
- `d = 1`, one availability profile and rate law (the class reduction
  note licenses the law-independence of weak-field statements).
- No statement is made about the realized formation rule's actual
  deposition rate -- that is the named follow-up; both phenomenology
  branches are stated.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`FORMATION_RATE_LAW_CLASS_REDUCTION_BOUNDED_NOTE_2026-07-08.md`](FORMATION_RATE_LAW_CLASS_REDUCTION_BOUNDED_NOTE_2026-07-08.md)
  (comparator conventions; law-independence).
- [`RECORD_SATURATION_AVAILABILITY_CENSUS_BOUNDED_NOTE_2026-07-08.md`](RECORD_SATURATION_AVAILABILITY_CENSUS_BOUNDED_NOTE_2026-07-08.md)
  (crowding mechanism and sign).
- [`ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md`](ACTIVITY_ENERGY_BOUND_WITNESSES_BOUNDED_NOTE_2026-07-08.md)
  (the support half licensing the zone model).

## Runner And Cache

Supervisor-executed result:

```text
TOTAL: TWO-CHANNEL-QUANTIFIED (+ flags R_wake_range=-0.005..1.000, wake_monotone_in_p=True, dwell_alpha=0.85)
```

Load-bearing residuals: zero-deposition control sub-sigma; trailing
vs leading co-moving dip `5.8-9.3` sigma; `S_after` monotone in `p` at
every `(v, b)`; dwell scaling `alpha = 0.64-1.09` with slow-vs-fast
separation `5.4-25.5` sigma; saturation guard max window density
`0.90` (weak-crowding regime held).

## Changelog

- **2026-07-08.** Initial note, single iteration; worker-drafted,
  supervisor-reviewed and supervisor-executed.
