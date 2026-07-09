# Saturation Stops Formation, And Constraint-Type Admissibility Makes Crowding Slow It -- The Exact Availability Census

**Date:** 2026-07-08
**Type:** bounded_theorem (exact corollary of the axiom text + exhaustive
finite censuses over declared rule spaces)
**Claim type:** bounded_theorem
**Claim scope:** Three exact results on the record-crowding mechanism.
(1) SATURATION COROLLARY: from the Record axiom text alone
(one-record-per-site + permanence), a fully recorded region admits zero
further record formation, forever -- rule-independent, verified
exhaustively (27,012 configurations). (2) RAW CENSUS: over the exact
covariant nearest-neighbor availability-rule spaces (subset-valued rules
on the classification note's condition-alphabet models; counted exactly
by orbit generating functions), crowding-monotone rules are NON-GENERIC
(0.06-1.8 percent) -- arbitrary covariance alone does not fix the sign
of the mechanism. (3) CONSTRAINT-CLASS THEOREM: under the constraint
reading of Admissibility -- each recorded neighbor contributes a
restriction and availability is the intersection (records restrict,
never enable; an open neighbor imposes nothing) -- monotonicity is
AUTOMATIC (proved by intersection, verified exhaustively) and 100
percent of axiom-compatible factorized rules are attraction-compatible.
An explicit covariant enablement witness shows what the complement
looks like: a rule where a recorded neighbor CREATES possibilities its
absence forbade. No rate law, no time metric, no gravity claim; sets no
audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/record_saturation_availability_census_2026_07_08.py`](../scripts/record_saturation_availability_census_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/record_saturation_availability_census_2026_07_08.txt`](../logs/runner-cache/record_saturation_availability_census_2026_07_08.txt)

## Why This Note Exists

The owner's mechanism proposal: record crowding should slow record
formation, and full saturation should stop it -- making the local
record-formation rate the framework's clock-rate field. This note
grounds the two structural halves exactly: the stop is an axiom
corollary; the slow-down's SIGN is located precisely -- not in
covariance (raw census: non-generic), but in the constraint character
of the Admissibility axiom itself (factorized class: universal).

## Results

**T1 -- saturation corollary (axiom-forced, rule-independent).** With
"a site never carries more than one record; records are permanent"
(MINIMAL_AXIOMS_2026-06-29), a configuration with every site recorded
has zero formable records at every subsequent step. Verified
exhaustively on 2x2x2 and 3x3x1 blocks (27,012 configurations, 770
fully-occupied; the zero at full occupancy holds for EVERY rule in the
model spaces -- the if-direction never consults the rule). Formation
sequences respect permanence (52,707 sequence nodes checked).

**T2 -- raw census: covariance does not fix the sign.** Availability
rules modeled as covariant assignments of a record-value subset to each
proper-cubic orbit of neighbor-condition patterns (the classification
note's models; a neighbor's condition is its record content or
openness). Exact counts by orbit generating functions (`k = 2`: 1,024
rules over 10 orbits; `k = 3`: 2.08e34 rules over 57 orbits; totals
verified against the imported orbit machinery). Census of the
crowding profile `Abar(r)` (mean availability at `r` recorded
neighbors): monotone-nonincreasing rules are 1.8 percent (`k = 2`) and
0.11 percent (`k = 3`) of axiom-compatible rules; non-monotone rules
dominate. Flag ATTRACTION-NONGENERIC: an arbitrary covariant rule has
no preferred crowding sign.

**T3 -- constraint-class theorem (the sign, located).** Call a rule
FACTORIZED (constraint-type) if availability(pattern) =
intersection over directions of per-neighbor constraints `C_d(v)`,
with an open neighbor imposing no constraint. Then: adding a recorded
neighbor intersects one more constraint, so availability can only
shrink or stay -- monotone nonincreasing along every crowding chain,
BY CONSTRUCTION (verified exhaustively over the full factorized class:
`k = 2` and `k = 3`, every member lands in the
strictly/weakly-decreasing or constant classes; none increasing or
non-monotone). Excluding the axiom's set-constant rules, 100 percent
of factorized rules are attraction-compatible (16/16 at `k = 3`), and
9 of 15 at `k = 3` can empty a site's availability below full
saturation (freezing-capable). The complement is exhibited: an
explicit covariant, non-factorized, INCREASING rule -- availability
empty at zero recorded neighbors and full otherwise -- an enablement
rule, in which a record's presence creates possibilities its absence
forbade. That is the shape antigravity would require.

## The Sentence This Buys (plain)

Records restrict -- that is what "admissibility" and "locking" mean in
the axiom's own vocabulary. T3 says that under exactly that reading,
crowding slows formation automatically, in every covariant realization,
with no tuning; and T2 says the reading is doing real work (arbitrary
covariant rules do not have this property). The sign of the
record-crowding mechanism is the constraint character of Admissibility.

## Boundaries

- Rule spaces are the classification note's finite condition-alphabet
  models (`k = 2, 3` readings of {open, recorded[, value]}); the
  framework's physical rule is not determined here (the classification
  note says so explicitly), and the factorized covariance condition
  implemented is stated in the runner's SPEC-NOTE.
- Availability counts are the crowding statistic; no rate law is
  chosen (that is block02's class reduction), no time identification
  is made (block03).
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) -- the
  axiom text T1 is a corollary of.
- [`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md)
  -- the rule-space models and orbit machinery (reused via import).
- [`FORMATION_RATE_LAW_CLASS_REDUCTION_BOUNDED_NOTE_2026-07-08.md`](FORMATION_RATE_LAW_CLASS_REDUCTION_BOUNDED_NOTE_2026-07-08.md)
  -- the campaign sibling consuming T3's profiles.

## Runner And Cache

Supervisor-executed result:

```text
TOTAL: CENSUS-COMPLETE ATTRACTION-NONGENERIC HORIZON-CLASS-COUNT=k2:512,k3:1.98e28 CONSTANT-COUNT-EXCLUDED-BY-AXIOM=no CONSTRAINT-CLASS-ATTRACTION=16/16=100% FACTORIZED-MONOTONE-THEOREM=ok
```

## Changelog

- **2026-07-08.** Initial note. Run 1 established T1/T2 and fired the
  pre-registered ATTRACTION-NONGENERIC flag; the supervisor identified
  the constraint-class repair (monotone-by-intersection under the plain
  reading of admissibility); run 2 added T3 and the enablement witness.
  Both supervisor-executed.
