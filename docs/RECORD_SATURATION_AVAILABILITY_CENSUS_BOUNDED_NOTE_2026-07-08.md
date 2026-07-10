# Record Saturation And A Covariant Availability Census With A Supplied Factorized-Set Model

**Date:** 2026-07-08
**Type:** bounded_theorem
**Primary runner:**
[`scripts/record_saturation_availability_census_2026_07_08.py`](../scripts/record_saturation_availability_census_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/record_saturation_availability_census_2026_07_08.txt`](../logs/runner-cache/record_saturation_availability_census_2026_07_08.txt)

## Claim

This note keeps two exact results and one conditional model lemma.

**T1 — saturation.** The Record axiom says that a site never carries more
than one record and that records are permanent. Therefore a region in which
every site is recorded admits no further record formation in that region, and
that conclusion persists. The runner checks the finite bookkeeping on
`2 x 2 x 2` and `3 x 3 x 1` open-boundary blocks for the declared
`k = 2, 3` condition alphabets: 27,012 configurations, 770 fully occupied
configurations, and 52,707 depth-limited formation-sequence nodes.

**T2 — raw covariant-rule census.** In the two finite models imported from
the covariance-classification runner, a rule assigns an availability subset to
each proper-cubic orbit of neighbor-condition patterns. Exact orbit generating
functions give 1,024 rules over 10 orbits for `k = 2` and
`4^57` rules over 57 orbits for `k = 3`. After excluding set-constant
rules, crowding-monotone mean-availability profiles are a minority in both
model spaces.

**T3 — conditional factorized-set lemma.** Additionally supply all of the
following model premises:

1. each direction and recorded neighbor value carries a set constraint
   `C_d(v)`;
2. an open neighbor contributes the full available-value set; and
3. the availability for a pattern is the intersection of its six directional
   constraints;
4. proper-cubic covariance acts at the constraint level, so
   `C_d(v) = C_e(v)` whenever `d` and `e` lie in the same direction
   orbit; and
5. rotations permute directions but do not permute the supplied condition
   values.

Adding one recorded neighbor then replaces one full-set factor by
`C_d(v)`, so the new availability is a subset of the old availability. The
monotonicity is an elementary intersection lemma. The runner exhausts the
declared finite factorized classes: all 15 nonconstant `k = 3` models are
crowding-monotone, as is the one nonconstant `k = 2` model. Nine of the 15
`k = 3` models can empty availability before all six neighbors are recorded.

The factorized-set premises are not consequences of Admissibility. They are a
supplied model. A covariant non-factorized witness whose availability is empty
at zero recorded neighbors and full once any neighbor is recorded is an
explicit member of the counted increasing class.

## Boundaries

- The finite rule spaces and their condition alphabets are supplied models;
  they do not determine the framework's physical admissibility rule.
- T1 uses only one-record-per-site and permanence. The finite enumeration is a
  bookkeeping check, not the logical source of the corollary.
- T2 is an exact census of the declared finite rule spaces, not a measure over
  all possible laws.
- T3 is conditional on the five explicit factorized-set and covariance
  premises above.
- No rate law, time metric, formation dynamics, or gravity conclusion is
  supplied.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) — the
  one-record-per-site and permanence statements used by T1.
- [`ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`](ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_OPENNESS_ACHIRAL_ORIENTED_FRAME_MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md)
  — the finite condition-alphabet models and proper-cubic orbit machinery used
  by T2 and reused to parameterize the conditional T3 model.
