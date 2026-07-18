# Phase-Port-Preserving Reservation Comb — Cycle 60 Scratch

**Date:** 2026-07-14
**Authority:** none
**Status:** exact bounded construction; conditional on the completed Cycle-57 builder
**Constitutional effect:** none

## Result

Cycle 59 reserves the four official sites `q,a,b,c`, but its broad one-parent
`S8` orbit permanently occupies `(2,-1,0)`. Together with `OPEN_B` and the
official future support, that closes every nearest-neighbour exit from `b`.
No later append-only phase token can then make `X@b` depend locally on `C@q`.

This scratch replaces only that broad `S8` closure. A write-once cube
completion first certifies that all three `S7` records exist and carries that
certificate to a marker beside the two c-side `S8` sites. The resulting exact
`E+MARK -> S8` row has six images instead of twelve and leaves `(2,-1,0)`
fresh. The original q/a/b/c certificate order is retained.

The all-rotation asynchronous graph is exact:

```text
canonical rows       21
declared additions   52
compiled conditions  80
reachable states     242,033
edges                 1,650,121
complete terminals   1
incomplete terminals 0
output conflicts     0
parasites             0
ordering violations   0
```

This is a candidate-law geometry result, not an axiom consequence and not a
constitutional proposal.

## New exact rows

Coordinates are in the decoded frame `t=(0,0,0)`, `d=+x`, `e=+y`.

| role | representative | exact local parents at staged formation | exact staged orbit |
|---|---:|---|---|
| `PAIR` | `(2,-2,-2)` | two `S7` | `(1,-2,-3)`, `(2,-2,-2)`, `(2,-1,-3)` |
| `ALL` | `(2,-2,-3)` | three `PAIR` | singleton |
| `R1` | `(3,-2,-3)` | one `ALL` | `(2,-3,-3)`, `(2,-2,-4)`, `(3,-2,-3)` |
| `R2` | `(3,-2,-2)` | one `PAIR`, one `R1` | six sites |
| `MARK` | `(3,-1,-2)` | one `S7`, two `R2` | `(1,-3,-2)`, `(1,-1,-4)`, `(3,-1,-2)` |
| `S8` | `(3,0,-2)` | one `E`, one `MARK` | `(0,-3,-2)`, `(0,-1,-4)`, `(1,-3,-1)`, `(1,0,-4)`, `(3,-1,-1)`, `(3,0,-2)` |

The three `PAIR` sites are the pairwise corners opposite the `COMP6`-centred
`S7` triad. `ALL` is the remaining cube corner and therefore cannot form
until every pair certificate exists. This removes the early one-`S7` marker
leak found by the first repair attempt.

## Scope

The probe establishes a live fresh port adjacent to `b` while preserving the
four reservation certificates under every asynchronous append order. It does
not yet construct the phase continuation

```text
C@q < X@b < joint Z@(a,c) < B/D/H.
```

That continuation must start only after the `OPEN_C` commit, carry a visible
signal to `q`, return a post-`C` signal through the fresh b port, allow the two
commuting endpoint records without premature builder writes, and retain every
future official site.
