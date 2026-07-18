# Mixed Cycle-72 Zero-Site Repair — Cycle 77

**Date:** 2026-07-14  
**Authority:** none  
**Status:** exact mixed-transient scoped closure  
**Constitutional effect:** none

Companion runner:

```text
scripts/mixed_cycle72_guide_repair_cycle77_2026_07_14.py
```

## Result

Cycle 72 is exact when launched only after the completed Cycle-67 terminal,
but one of its downstream inputs is already live during a valid partial
Cycle-67 history:

```text
X_B -> D1.
```

If `OPEN_C` is delayed, the future `Z_C=(3,0,0)` site has exactly that input.
The row writes `D1` there permanently. The full mixed scan finds one causally
feasible wrong class and no other feasible defect:

```text
target       (3,0,0)
source       downstream table
written      D1
expected     Z_C
```

Cycle 77 removes the row by changing the local order on the y side:

```text
base H1 pair + Z_A -> B_y
X_B + B_y          -> D_y.
```

No site, guide record, or axiom is added. The same 31 downstream records are
written, but `D_y` now has a physical B neighbour rather than the bare `X_B`
input that aliases `Z_C`.

## Exact terminal certificate

```text
new canonical rows             27
new proper-cubic raw rows     630
full C60/C67/C77 rows         147
full proper-cubic rows      3,224
append-only additions          31
conditional conditions         50
conditional states            475
conditional edges           1,339
conditional terminals           1 complete
parasites/conflicts              0
```

## Exact mixed audit

The scanner retains every 242,033 reachable Cycle-60 state, all 67 exact
Cycle-67 availability masks, arbitrary subsets of each locally available
downstream continuation, and every relevant interface site.

Both the baseline and repair scan the same strong local over-approximation:

```text
interface candidates                 433
retained candidates                  203
mixed local contexts              19,240
apparent wrong contexts              203
apparent wrong target/output classes  48
```

For Cycle 72, one context remains causally feasible: the `D1` theft of `Z_C`.
For Cycle 77, all 203 apparent wrong contexts have a first-bad ancestry
contradiction. The repaired result is:

```text
feasible wrong writes                  0
feasible raw conflicts                 0
feasible Cycle-60 blockers             0
feasible Cycle-67 blockers             0
```

## Scope relative to the joint-endpoint route

This is the smallest tested mixed-safe repair by additions, but it does not
retain Cycle 63's stronger ancestry condition. `B_y` can form after `Z_A` and
before `Z_C`; therefore not every B descends from both endpoints.

Cycle 79's 35-addition caged guide has the same scope distinction. Cycle 78's
47-addition construction pays for a third join layer plus a post-join export
cable and proves both that every B has `Z_A` and `Z_C` as mandatory ancestors
and that B5 is the final B.

## Boundary

This is a finite candidate-law composition result. It does not select the
universal law, establish recurrence or renewal, derive occurrence weights or
duration calibration, or supply axiom content.
