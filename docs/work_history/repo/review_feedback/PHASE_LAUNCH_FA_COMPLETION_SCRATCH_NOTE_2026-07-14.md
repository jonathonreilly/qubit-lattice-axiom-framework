# Phase-Launch F/A Completion — Scratch Note

**Date:** 2026-07-14
**Authority:** none
**Status:** exact bounded subsystem, conditional on the completed Cycle-60 terminal
**Constitutional effect:** none

## Result

The first post-comb carrier is the six-site proper-cubic orbit `F`, whose
local input is one `R2` plus one `S8`. Adding only this row to Cycle 60 is
already exact under every asynchronous order:

```text
634,613 states / 4,434,685 edges / one complete terminal / no defect.
```

The next naive row, `F -> A`, has a real transient race. Three pairs of `F`
sites share an otherwise open common neighbour. If one `F` forms first, that
corner has the one-`F` input and writes `A`; if both `F` records form first,
the same corner instead sees `F+F`. A snapshot made only after all `F` records
therefore misses three reachable writes.

The completion is finite and exact:

1. declare the three pair corners as `A`;
2. retain `F` when its normal `R2+S8` input has gained the corner `A`;
3. write the corner `A` from `F+F` if both `F` records win first.

The resulting phase-only graph from the completed Cycle-60 terminal is:

```text
canonical rows   4
F sites          6
A sites          15
conditions       33
states           117,649
edges            878,766
terminals        1 complete
parasites        0
conflicts        0
```

All 21 additions avoid both the current official block and the next block
translated by `3d`. The result is a schedule-completion component of a
candidate strict-nearest-neighbour phase compiler. It does not select an
instrument, branch weight, occurrence rate, or axiom wording.

## Exact orbits

```text
F = {
  (0,-3,-3), (0,-2,-4), (2,-3,-1),
  (2,0,-4), (3,-2,-1), (3,0,-3)
}

A exterior = {
  (-1,-3,-3), (-1,-2,-4), (0,-4,-3), (0,-2,-5),
  (2,-4,-1), (2,-3,0), (2,0,-5), (2,1,-4),
  (3,-2,0), (3,1,-3), (4,-2,-1), (4,0,-3)
}

A pair corners = {
  (0,-3,-4), (3,-3,-1), (3,0,-4)
}
```

Three additional static targets that a whole-universe compiler can list for
the one-`F` row are causally unreachable: formation of their adjacent `F`
already requires a `PAIR` and an `E` that change the local input. Full
Cycle-60 composition should nevertheless verify this structural dependency
directly after the complete phase subsystem is assembled.
