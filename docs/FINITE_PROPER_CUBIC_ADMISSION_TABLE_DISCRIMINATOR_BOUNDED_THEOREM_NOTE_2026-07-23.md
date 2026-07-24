# Finite Proper-Cubic Admission-Table Discriminator

**Type:** bounded_theorem

Date: 2026-07-23

Authority: none

Audit: unset

Runner: [`scripts/finite_proper_cubic_admission_table_discriminator_2026_07_23.py`](../scripts/finite_proper_cubic_admission_table_discriminator_2026_07_23.py)

Runner cache: [`logs/runner-cache/finite_proper_cubic_admission_table_discriminator_2026_07_23.txt`](../logs/runner-cache/finite_proper_cubic_admission_table_discriminator_2026_07_23.txt)

Receipt: [`outputs/finite_proper_cubic_admission_table_discriminator_receipt_2026_07_23.json`](../outputs/finite_proper_cubic_admission_table_discriminator_receipt_2026_07_23.json)

Independent checker: [`scripts/finite_proper_cubic_admission_table_discriminator_independent_check_2026_07_23.py`](../scripts/finite_proper_cubic_admission_table_discriminator_independent_check_2026_07_23.py)

Independent grid: [`outputs/finite_proper_cubic_admission_table_discriminator_independent_grid_2026_07_23.json`](../outputs/finite_proper_cubic_admission_table_discriminator_independent_grid_2026_07_23.json)

## Claim

On the complete set of 64 Boolean six-neighbor words, supply the five shell
tables

```text
unique_quorum = {1}
odd_shells    = {1,3,5}
nonempty      = {1,2,3,4,5,6}
low_density   = {1,2}
even_nonzero  = {2,4,6}
```

and the finite lane-zero port grammar encoded in the runner.  The implemented
four-tier discriminator is total on grammar-valid finite streams.  It either
identifies the unique table consistent with the observations or returns an
explicit ambiguity, off-family, covariance, contradiction, or malformed-port
witness.  For the frozen blinded corpus it identifies all five supplied tables
on full coverage and on the weight-at-most-three training prefix.  A supplied
imposter that agrees with `odd_shells` on every training word is rejected when
the held weight-five words are added.

This is a finite classifier theorem for supplied inputs.  It is not a physical
formation or admission law.

## Exact finite results

- Accepted rows over all 64 words are `6, 32, 63, 21, 31` in the table order
  above.  Training counts are `6, 26, 41, 21, 15`; held counts are
  `0, 6, 22, 0, 16`.
- Every pair of supplied tables has an explicit separating word.  The minimum
  separating shell-set size is three, with six minimum sets.
- The proper-cubic action has 24 frames and ten orbits on the 64 words.  Every
  supplied shell table is invariant under that action.
- A proper-cubic-covariant antipodal-pair table is correctly reported as
  off-family, demonstrating that the supplied five-table family is not assumed
  to exhaust covariant tables.
- A preferred-axis imposter, a contradictory repeated word, and eight distinct
  malformed-port streams are refused with their named witnesses.
- Whole-stream reorientation preserves the verdict for all 24 frames in the
  tested in-family and off-family cases.

## Supplied structure

The five shell tables, the lane-zero port grammar, the lowest-index synthetic
emitter convention, the train/held split, blind seed, stream roster, imposter
catalog, and malformed catalog are supplied.  The emitter is a self-test
fixture, not a physical formation route.  The field names `occurrence`,
`MEMBER`, and `LAW_RECEIPT` are grammar labels and carry no framework semantics
in this theorem.

## Scope and open bridges

The result does not identify nature's fixed Admissibility rule, select an
actual outcome, form or preserve a framework Record, derive a Born weight or
sampling law, construct the supplied streams from physical M2 dynamics, or
touch time, gravity, source, energy, or stress.  Other proper-cubic local laws
are allowed; the antipodal control supplies one explicit example.

The independent audit lane assigns any audit or effective status.
