# Koide Q=1 Q-Side Objectivity Premise Audit

**Date:** 2026-05-31
**Claim type:** exact support / negative route pruning.
**Actual current-surface status:** exact support.  Bare quotient atom-anonymity
is sufficient for `Q=2/3`, but the physical rank-erasing premise is not
derived here.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_koide_q1_q_side_objectivity_premise_audit.py`](../scripts/frontier_koide_q1_q_side_objectivity_premise_audit.py)

## Question

The record-quotient fork isolated the Q-side gap:

```text
full Hilbert trace / Born rank      -> Q = 1
rank-erased quotient record count   -> Q = 2/3
```

This note asks whether the missing rank-erased quotient count can be obtained
from objectivity, source-measure, or max-entropy structure already present in
the repo.

## Answer

Not on the current surface.

There is a clean sufficient principle:

```text
erase Hilbert rank first, then impose atom-anonymity on the bare two-atom
record quotient.
```

On the bare quotient algebra `C^2`, the two atoms can be swapped.  Invariance
under that swap forces

```text
tau_count(e0) = tau_count(e1) = 1/2,
```

and therefore gives

```text
r = 1/2
Q = 2/3.
```

But that is already the missing physical premise.  It is not forced by the
actual `S`-labeled record.

## Why Objectivity Does Not Close It

The embedded sharp record has

```text
S = C + C^2 = 2 P0 - P1
rank(P0), rank(P1) = (1,2).
```

The bare quotient has an atom-swap symmetry, but the `S`-labeled record does
not.  Swapping the atoms sends the `S` eigenvalue pair

```text
(2, -1)
```

to

```text
(-1, 2).
```

So the atom swap is not an automorphism of the labeled physical record.  The
automorphism group preserving `S` is just the identity, and the identity
imposes no probability constraint.  Both

```text
(1/3, 2/3)
```

and

```text
(1/2, 1/2)
```

are invariant under the identity.

Thus objectivity of the `S`-record is too weak.  Uniform count follows only
after an additional move that discards the rank and `S`-label structure before
reference selection.

## Why Max Entropy Does Not Close It

The order of operations matters:

```text
count full Hilbert microstates, then erase rank:
  (1/3, 1/3, 1/3) -> (1/3, 2/3) -> Q = 1

erase rank first, then count quotient atoms:
  (e0, e1) -> (1/2, 1/2) -> Q = 2/3
```

These operations do not commute because the atom ranks are unequal.

Equivalently, quotient-uniform weights pulled back to the three Hilbert
microstates give

```text
(1/2, 1/4, 1/4),
```

not the full Hilbert max-entropy law

```text
(1/3, 1/3, 1/3).
```

So "max entropy" alone does not choose the Q-side premise.  It gives different
answers depending on whether the selected algebra is the full Hilbert algebra
or the rank-erased quotient record algebra.

## Source-Measure Boundary

The existing source-measure / record-intervention theorem is still useful: it
says a record-facing source is a probability law on finite sharp-record
histories.

But it keeps a full-support reference `P0` as input.  The sharp-record tangent
theorem similarly gives the primitive signed tangent after choosing
`P0=(1/2,1/2)`.  It does not derive that reference from the `S` record.

The strict onsite source-domain route remains a separate Q-side route:

```text
physical source-domain uses strict onsite descent
  -> reduced Z erased
  -> Q = 2/3.
```

That route is still open as a physical source-domain theorem.

## What Remains

The Q-side premise has now been reduced to an exact choice between two possible
physical theorems:

```text
P_MEASURE:
  physical charged-lepton readout erases Hilbert rank before reference
  selection, leaving an atom-anonymous two-record quotient.

P_SOURCE:
  physical charged-lepton source-domain law uses strict onsite descent or
  otherwise excludes projected Z as undeformed source data.
```

Either one would give the Q side:

```text
Q = 2/3.
```

Neither one is derived by this note.

## Closeout Flags

```text
KOIDE_Q1_Q_SIDE_OBJECTIVITY_PREMISE_AUDIT=TRUE
BARE_QUOTIENT_ATOM_ANONYMITY_IMPLIES_Q23=TRUE
S_LABELED_RECORD_OBJECTIVITY_IMPLIES_Q23=FALSE
FULL_TRACE_NATURALITY_IMPLIES_Q1=TRUE
MAX_ENTROPY_ALONE_SELECTS_Q23=FALSE
SOURCE_MEASURE_SELECTS_QUOTIENT_REFERENCE=FALSE
P_SOURCE_STRICT_ONSITE_REMAINS_OPEN=TRUE
Q_SIDE_PREMISE_DERIVED_CURRENT_SURFACE=FALSE
MINIMAL_EXTRA_PRINCIPLE=rank_erasure_before_reference_selection_or_strict_onsite_source_domain
NEXT_THEOREM=derive_physical_rank_erasure_before_measure_or_P_SOURCE
```

## Verification

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/frontier_koide_q1_q_side_objectivity_premise_audit.py
```

Expected closeout:

```text
PASSED: 20/20
KOIDE_Q1_Q_SIDE_OBJECTIVITY_PREMISE_AUDIT=TRUE
BARE_QUOTIENT_ATOM_ANONYMITY_IMPLIES_Q23=TRUE
S_LABELED_RECORD_OBJECTIVITY_IMPLIES_Q23=FALSE
FULL_TRACE_NATURALITY_IMPLIES_Q1=TRUE
MAX_ENTROPY_ALONE_SELECTS_Q23=FALSE
SOURCE_MEASURE_SELECTS_QUOTIENT_REFERENCE=FALSE
Q_SIDE_PREMISE_DERIVED_CURRENT_SURFACE=FALSE
```

## Cross-References

- [`KOIDE_Q1_RECORD_QUOTIENT_MEASURE_FORK_NOTE_2026-05-31.md`](KOIDE_Q1_RECORD_QUOTIENT_MEASURE_FORK_NOTE_2026-05-31.md)
  - exact fork between Hilbert-rank `Q=1` and quotient-count conditional
    `Q=2/3`.
- [`SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md`](SOURCE_MEASURE_RECORD_INTERVENTION_THEOREM_NOTE_2026-05-30.md)
  - record-facing sources are probability laws on finite sharp-record
    histories, with a reference law as input.
- [`KOIDE_Q_SOURCE_DOMAIN_CANONICAL_DESCENT_THEOREM_NOTE_2026-04-25.md`](KOIDE_Q_SOURCE_DOMAIN_CANONICAL_DESCENT_THEOREM_NOTE_2026-04-25.md)
  - strict onsite descent erases the reduced `Z` coordinate conditionally.
- [`KOIDE_Q_BACKGROUND_ZERO_Z_ERASURE_CRITERION_THEOREM_NOTE_2026-04-25.md`](KOIDE_Q_BACKGROUND_ZERO_Z_ERASURE_CRITERION_THEOREM_NOTE_2026-04-25.md)
  - source-free / `Z`-erasure is equivalent to `Q=2/3` inside the admitted
    reduced route.
