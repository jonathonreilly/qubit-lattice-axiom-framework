# Separated Recurrent-Tube Collision Control — Cycle 84

**Date:** 2026-07-14
**Authority:** none
**Status:** exact positive separation control
**Constitutional effect:** none

Companion runner:

```text
scripts/separated_recurrent_tube_collision_control_cycle84_2026_07_14.py
```

## Result

Two copies of the Cycle-80 recurrent append tube coexist exactly when their
occupied supports have one empty lattice row between them.  Equivalently, the
minimum Manhattan distance between the two supports is two, so no site in one
tube is a nearest neighbor of a site in the other.

For two independent transverse offsets and horizons of three, six, and nine
layers, the joint asynchronous graph is the exact Cartesian product of the
two one-tube graphs.  The condition count is additive, the reachable-state
count is multiplicative, and the append-edge count obeys the product-graph
identity.  Every joint schedule reaches the two exposed correct next-layer
seeds, with no wrong append, output conflict, or hidden dead terminal.

At the three-layer horizon the pinned joint counts are:

```text
conditions                 144
reachable states         2,704 = 52^2
append edges             5,408
exposed next seeds           2
output conflicts             0
```

All 24 proper-cubic images preserve those counts.  The separation is carried
by the record geometry, not by a coordinate label or an exception in the
rule.

## Exact scope

This is a positive separation control.  It proves that the selected recurrent
mechanism admits arbitrarily long parallel histories without cross-talk at a
one-row safety margin.  It does not resolve adjacent collisions, choose what
two fronts should do when they touch, prove multi-front confluence at contact,
or nucleate either tube from the official terminal.

Those are separate law-design questions.  No axiom addition follows from
collision-free factorization or from the untested contact cases.

## Verification

```text
python3 scripts/separated_recurrent_tube_collision_control_cycle84_2026_07_14.py
```
