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
4. the real-positive determinant branch supplied by the det-positivity lemma.

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

Expected runner result: `TOTAL: PASS=19 FAIL=0`.
