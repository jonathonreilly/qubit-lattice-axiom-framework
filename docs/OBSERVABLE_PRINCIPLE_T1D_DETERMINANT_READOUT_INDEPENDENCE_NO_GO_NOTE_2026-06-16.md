# Observable-Principle T1-d Determinant-Readout Independence No-Go

**Date:** 2026-06-16
**Claim type:** no_go
**Actual current-surface status:** no-go source proposal; independent audit
lane owns any effective status.
**Trace class:** direct_blocker_closure
**Target blocker:** `observable_principle_from_axiom_note` was audited
conditional because "the restricted packet does not derive T1-d from the
cited inputs"; T1-d is the readout-identification bridge asserting that the
scalar record readout `W` is a continuous function of `Z = det(D+J)` alone on
all of `R_{>0}` and that disjoint source blocks register as disjoint records.
**Primary runner:**
[`scripts/frontier_observable_principle_t1d_determinant_readout_independence_2026_06_16.py`](../scripts/frontier_observable_principle_t1d_determinant_readout_independence_2026_06_16.py)

## Result

T1-d is independent of the current framework axioms. It cannot be derived
from:

1. finite scalar Record additivity for already supplied disjoint records;
2. determinant multiplicativity on direct sums;
3. continuity of a scalar source readout on finite positive source data; and
4. the real-positive determinant branch supplied by
   [`REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md`](REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md).

The axiom input is
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md): Record supplies
finite scalar additivity for supplied disjoint record collections, while
withholding source/action, arbitrary observable identification, readout
contexts, sector-generation rules, weighting, normalization, and dynamics.

The obstruction is exact. There are continuous, block-additive scalar readouts
on finite positive source blocks that satisfy `W(A + B) = W(A) + W(B)` under
direct sum but are not functions of `det(D+J)` alone. For example, on real
positive diagonal source blocks with `D = 0`,

```text
W_epsilon(S) = log det(S) + epsilon Tr(S)
```

is continuous and direct-sum additive because both `log det` and `Tr` are
additive under block direct sums. But it is not determinant-only: the two
positive source blocks

```text
S_1 = diag(4, 1),     S_2 = diag(2, 2)
```

have the same determinant `4` and different traces `5` and `4`, hence
`W_epsilon(S_1) != W_epsilon(S_2)` for any nonzero `epsilon`.

So Record additivity plus determinant multiplicativity can select the
logarithmic family only after the determinant-only readout quotient is already
imposed. That quotient is precisely T1-d's missing bridge. It is not a
consequence of Record.

## Disjoint-Source To Disjoint-Record Clause

The second half of T1-d is independent for the same reason. The Record axiom
states finite additivity for pairwise-disjoint records once a readout context
is supplied. It does not say that two disjoint source blocks must be assigned
to disjoint records.

A source-to-record assignment can map two disjoint source block labels to the
same realized record label without contradicting Record, because the premise
needed for additivity over two records has not been met. Therefore the
blocks-to-records clause is a genuine bridge premise. It may be supplied by a
future readout-context theorem or approved primitive, but it is not derivable
from the present Lattice, Quantum, and Record axioms.

## Boundary

This note is not a no-go against the observable principle itself. It is only a
no-go against deriving T1-d from the currently approved axioms and the existing
determinant algebra. The conditional chain in
`docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` remains meaningful when T1-d
is supplied as an explicit bridge premise. This parent row is named as plain
context rather than as a graph-visible dependency.

Nor does this note add a new axiom, primitive, or Tier-A admission. The only
allowed downstream use is negative: consumers must not treat T1-d as
Record-derived or silently framework-native on the current surface.

Guardrail sentence for verifiers: consumers must not treat T1-d as Record-derived, and this note does not add a new axiom.

## No-Go Discipline Gate

**N1 -- Alternative route enumeration.** Five routes were checked. (1) Record
additivity plus determinant block factorization could force determinant-only
readout; the `W_epsilon = log det + epsilon Tr` countermodel refutes it. (2) A
fixed-dimension quotient could remove the trace freedom; `diag(4,1)` and
`diag(2,2)` are both two-dimensional and have the same determinant, so it does
not. (3) Continuity or smoothness on the positive source cone could force
`log det`; `W_epsilon` is smooth there. (4) Source-disjoint blocks could be
automatically record-disjoint; the non-injective source-to-record assignment
refutes that pure-logic implication. (5) Lattice, Quantum, or Record could
supply the missing source/action or observable-identification bridge; the
minimal axiom note explicitly withholds those structures.

**N2 -- Wall independence.** The determinant-only quotient and the
source-blocks-to-records clause are independent. A determinant-only scalar
readout would not make a non-injective source-to-record map injective, and an
injective source-to-record bridge would not make every additive scalar source
readout a function of determinant alone.

**N3 -- Hidden-wall scan.** The used inputs are explicit: minimal axioms,
finite determinant/direct-sum algebra, continuity on the positive source cone,
and the retained positive-branch determinant lemma. Future readout-context
theorems or approved primitives are named as future import-retirement paths,
not consumed here.

**N4 -- Residual matching.** The residual attacked here is exactly the parent
T1-d residual: deriving the determinant-only scalar readout quotient and
source-blocks-to-records clause from Record plus determinant algebra. No broader
observable-principle closure is claimed.

**N5 -- Rhetoric audit.** The negative statement is only finite and local to
T1-d. The determinant-only failure is tested on finite positive diagonal source
blocks; the blocks-to-records failure is tested at the source-label to
record-label assignment level. No lattice-wide, dynamical, empirical, or
physical-measure no-go is asserted.

**N6 -- Partial-closure path scan.** The wall can still be retired by a future
readout-context theorem, approved primitive, or explicit bounded bridge that
supplies determinant-only readout and source-blocks-to-records injectivity.
This note does not classify that future path as a new axiom requirement.

**N7 -- Steelman.** The strongest counterargument is that a richer readout
context might identify central-sector record labels with determinant data and
thereby rule out trace-sensitive additive source readouts. That would be a real
positive bridge if supplied, but it is not in the current Lattice, Quantum, and
Record axioms or the determinant algebra used by the parent packet.

**N8 -- Cross-cycle echo.** Similar Record-derived source/action, selection,
and target-vector walls elsewhere in the repo are handled by explicit supplied
interfaces, bounded bridges, or future primitive/theorem paths rather than by
treating Record as arbitrary observable authority. This note follows that
pattern and leaves the positive bridge route open.

## Verification

The runner checks:

- exact direct-sum additivity of `log det`, `Tr`, and
  `W_epsilon = log det + epsilon Tr`;
- the same-determinant/different-trace witness showing
  `W_epsilon` is not determinant-only;
- exact determinant multiplicativity on direct sums, showing the countermodel
  preserves the determinant algebra consumed by the parent note;
- independence of the source-disjoint to record-disjoint clause by an explicit
  non-injective source-to-record assignment;
- parent-note guardrails: T1-d remains declared as a boundary, is stated as
  not derivable from `minimal_axioms`, and cites this no-go.

Expected runner result: `TOTAL: PASS=20 FAIL=0`.
