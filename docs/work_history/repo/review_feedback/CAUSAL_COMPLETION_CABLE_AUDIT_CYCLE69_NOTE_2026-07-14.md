# Causal Completion-Cable Audit — Cycle 69

**Date:** 2026-07-14  
**Authority:** none  
**Status:** exact conditional causal-safety audit of the Cycle-67 candidate  
**Constitutional effect:** none

Companion runner:

```text
scripts/causal_completion_cable_audit_cycle69_2026_07_14.py
```

## Result

The Cycle-67 completion detector and return cable survive the causal audit.
The four red lines in the Cycle-67 scratch runner are static-alias false
positives, not reachable writes.

An independent compiler reproduces exactly:

```text
355 compiled local conditions
308 intended target/type conditions
47 apparently bad conditions
34 apparently bad target/output classes
  - 15 off-footprint classes
  - 19 wrong-role classes on the footprint
```

All 47 apparently bad conditions are impossible in a correct append-only
history. This result does **not** reject the cable table, and it gives no basis
for rejecting the geometric route.

The 308 same-target/same-output conditions were also checked one by one. Each
contains the intended causal parents of that particular target; none is an
early same-content alias that could evade the induction below.

## Why the static failures are not physical failures

The static compiler asks whether a rotated row matches a declared finite
neighbour pattern. It does not ask whether the records in that pattern can
coexist in causal order.

For the causal audit, suppose a bad write is the first bad write. Every record
already present around it must then have been written correctly. The intended
dependency graph is strictly rank-lowering:

```text
F6 -> FP3 -> I1_3 -> I2_3 -> DONE1
    -> L1 -> ... -> L12 -> C_Q -> P0 -> P1 -> P2 -> P3
    -> X_B -> {Z_A, Z_C}.
```

The two endpoint records are nonadjacent peers; neither is a parent of the
other. Every other non-base parent has strictly lower rank.

A fixed-point calculation therefore gives the records that must already exist
before each correctly written record. Every one of the 47 bad signatures says
that at least one such mandatory ancestor is absent while one of its
descendants is present. Permanence makes that local context impossible. For
example, a row which appears able to write `L7` over a delayed `L5` also
requires a neighbouring `L6`; that `L6` itself cannot exist unless the same
`L5` already exists.

This is not the only certificate. A second calculation blocks each bad
condition's required-absent sites, discards the exact signature table, and
generously allows **every** site whose named causal parents exist. This is an
over-approximation of every correct Cycle-67 history. None of the 47 bad
conditions can assemble even in that larger process. The two independent
checks return `47/47` and `47/47` respectively.

## Completion detector

The detector boundary can be separated from the cable and exhausted exactly:

| quantity | result |
|---|---:|
| records | 16 |
| role census | `F6 / FP3 / I1_3 / I2_3 / DONE1` |
| canonical rows | 9 |
| compiled conditions | 31 |
| reachable asynchronous states | 344 |
| edges | 1,030 |
| terminals | 1 |
| complete terminals | 1 |
| wrong/off-footprint conditions | 0 |
| output conflicts | 0 |

`DONE` has exactly the other fifteen detector records as mandatory ancestors.
It is therefore a genuine local completion fact for this finite detector, not
a premature clock or a global read.

## Return and phase endpoint

Using the completed causal prefix, each of these eight target signatures is a
singleton open-site class:

```text
C_Q, P0, P1, P2, P3, X_B, Z_A, Z_C.
```

The `L12` record breaks the pre-existing two-site `W6/Z0` ambiguity and makes
`C_Q` unique. The later cable records similarly cage each phase relay. `Z_A`
and `Z_C` are distance two apart and commute after `X_B`.

Cycle 67's check `A05` is mechanically mis-specified: it defines every
non-official addition as an "auxiliary" and then asks whether `P0..P3`, which
are themselves declared non-official additions, are not auxiliaries. The
correct freshness question is whether those four sites are absent from the
completed base, detector, cable, and `C_Q` prefix. They are all fresh.

An explicit exact-table schedule writes all 91 declared records and encounters
zero enabled bad condition. More generally, the strict causal DAG and the
complete set of 308 parent-valid local-subset rows give the first-bad-write
induction above; the result is not tied to that displayed schedule.

## Boundary

This is conditional on the completed Cycle-60 comb, exactly as Cycle 67 was.
It does not yet prove safe composition through every transient Cycle-60 state,
renewal, recurrence, route minimality, or any axiom/formation law. Cycle 68's
mixed-transient method remains the required next interface audit.

The engineering lesson is narrower: one-parent-looking wave rows cannot be
rejected by static aliases alone when their possible records carry staged
pair/completion ancestry. Causal feasibility must be checked before changing
the route or adding record roles.
