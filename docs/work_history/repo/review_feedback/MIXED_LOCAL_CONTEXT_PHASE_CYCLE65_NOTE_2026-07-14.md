# Mixed Local-Context Phase Audit — Cycle 65

**Date:** 2026-07-14
**Authority:** none
**Status:** exact bounded rejection of the frozen Cycle-64 candidate; no global no-go
**Constitutional effect:** none

Companion runner:

```text
scripts/mixed_local_context_phase_cycle65_2026_07_14.py
```

## Result

The frozen Cycle-64 transducer is not live-composable with Cycle 60 as
written.  This is already visible in Cycle 64's own completed-comb condition
compiler, and a stronger mixed-context scan exposes additional transient
cross-fire.

The stronger scan fixes only the 38-record completed Cycle-57 builder.  It
treats all 52 Cycle-60 additions and all 152 Cycle-64 additions as independent
local presence/absence variables.  For each open target adjacent to that
204-site footprint, it exhausts all subsets of the target's at-most-six
variable neighbours.  This is a complete radius-one scan:

```text
union canonical rows        163
union raw rotated inputs  3,370
candidate targets           461
local subsets             6,297
matching contexts         2,215
bad contexts                371
bad target/output triples    95
```

The canonical and raw rule tables are single-valued by **input**.  That does
not make them single-valued by **target during construction**.  Cycle-64 rows
produce 254 wrong-content footprint matches and 89 off-footprint matches.
Cycle-60 rows contribute 28 more arbitrary-subset footprint mismatches; those
are separately known to be unreachable inside Cycle 60's exact 242,033-state
graph, so this note does not relabel Cycle 60 itself as defective.

## Minimal witnesses

All of the following are exact one- or two-neighbour local contexts over the
completed Cycle-57 base:

```text
P at (-2,-3,-3)
  makes intended A target (-1,-3,-3) match output P.

A at (-1,-3,-3)
  makes outside target (-1,-3,-2) match output T.

A at (-1,-3,-3)
  makes intended F target (0,-3,-3) match output T.

OPEN_B at (0,-2,-1) plus PHASE_E at (1,-2,0)
  makes intended L2 target (0,-2,0) match output X_B.
```

The first and fourth defects do not depend on removing an unfinished Cycle-60
record.  Cycle 64's own completed-Cycle-60 `compile_conditions()` reports 16
competing-output targets: all fifteen `A` sites admit both `A` and `P`, while
`L2=(0,-2,0)` admits both `L2` and `X_B`.  The frozen Cycle-64 runner therefore
ends `20 PASS / 1 FAIL` at its target-single-output check.

## What failed

The monotone-parent idea proves a progress property only after type safety is
available.  It does not itself provide type safety.  Under proper-cubic
rotation, a rule whose only live discriminator is “has a lower-rank parent”
can occur at a target assigned a different rank.  Later-shell rows then write
earlier-shell sites, and terminal-snapshot signatures hide the transient
aliases.

The exact residual is:

```text
MIXED_LOCAL_CONTEXT_CLOSURE
TARGET_OUTPUT_RACE
```

It is not an impossibility result for homogeneous nearest-neighbour laws, the
phase instrument, Cycle 60, or the framework.

## Fresh N1–N8 gate

### N1 — Alternative routes

Five live repair routes remain: enumerate only actually reachable mixed
states; add role-distinct local cages; redesign the rank shells so rotated
parent signatures are disjoint; absorb benign same-output cross-fire into a
larger footprint; or introduce a genuinely local completion token before the
phase shell.  None is silently ruled out here.

### N2 — Wall independence

Two walls were tested independently.  The fifteen `A/P` and one `L2/X_B`
target races occur with the completed Cycle-60 base.  The 89 outside matches
arise only in the stronger mixed-variable scan.  Removing the latter does not
repair the former.

### N3 — Hidden-wall scan

An arbitrary local subset need not extend to a globally reachable state.  The
mixed scan therefore rejects the requested static composability criterion; by
itself it does not prove all 371 contexts dynamically reachable.  A positive
replacement still needs either an exact reachable-state proof or a static
closure strong enough to make reachability irrelevant.

### N4 — Residual matching

The evidence matches only mixed local-context closure and target-output race.
It does not match axiom insufficiency, failure of the `C/X/Z` instrument, or a
no-go for strict nearest-neighbour compilation.

### N5 — Rhetoric audit

“Cycle 64 is rejected as written” is licensed.  “The route is impossible,”
“the framework cannot form records,” and “an axiom must be added” are not.

### N6 — Partial-closure paths

Cycle 60's exact comb, the six-site `F` seed, the finite shell geometry, the
152-site official-support avoidance, and the intended `C_Q/X_B/Z_A/Z_C`
locations remain useful construction data.  The 142-row output table and its
rank-confluence conclusion do not survive this audit.

### N7 — Steelman

The strongest defense is that causal-parent preservation guarantees some
lower-rank support before each write and avoids preferred schedules.  The
counterexample accepts that premise: the support is present, but the same
rotated support is legal at a differently typed target.  Progress and typing
are independent obligations.

### N8 — Cross-cycle echo

This is the same failure genus as the rejected `K3=N2-only` relay: a completed
snapshot has a clean signature class, while a partial subset exposes extra
aliases before the intended cages arrive.  The recurrence makes a mixed
local-subset or exact reachable-state composition check mandatory for the next
candidate; it does not enlarge the negative scope.

## Authority boundary

This note changes no axiom, primitive, registry, policy, queue, retained
status, or audit verdict.  It does not commit, push, merge, or select a law.
