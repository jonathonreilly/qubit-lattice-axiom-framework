# First-Role Differentiation — Cycle 56

**Date:** 2026-07-14

**Type:** authority-free positive append-only construction, complete mixed-table
asynchronous graph, proper-cubic covariance test, and bounded handoff

**Authority: none.** This note is not an axiom proposal, registered primitive,
retained theorem, audit verdict, or permission to change foundation, registry,
policy, queue, or audit state. **No live foundation or audit edit is
authorized.** It issues **no audit verdict**, commit, push, or PR. It makes **no
axiom need** claim.

Companion runner:

```text
scripts/first_role_differentiation_cycle56_2026_07_14.py
```

## Result Up Front

Cycle 56 positively constructs

> `SCHEDULE_SAFE_OFF_TARGET_COMPLETION_PATH`

and thereby closes the Cycle-55 residual

> `FIRST_ROLE_DIFFERENTIATION`.

The run starts from exactly the seven-record Cycle-43/47 seed plus
`(0,1,1): BACKSTOP`; neither the AUX scaffold nor `LAUNCH_A` is supplied. The
Cycle-54 AUX/JOINT rules, every new Cycle-56 rule, the launcher rule, every one
of their proper-cubic images, and the complete Cycle-52 renewal table are all
installed from state zero.

The rules first reconstruct the off-target `AUX,AUX,JOINT` scaffold. A forced
three-site safe `RING` orbit then writes two pair certificates and merges them
into one `COMPLETE` record. `COMPLETE` gates a short off-target path and a
two-site `ARM` orbit. Exactly one arm meets exactly one AUX beside the still-open
Cycle-52 target `(-1,2,1)`, so the rule `AUX+ARM -> A_1_2` has that site as its
only rotated-signature match. No final target is used as temporary storage.

The new permanent `A_1_2` record supplies the one adjacent final role that
Cycle 55 showed was sufficient to gate the launcher. Consequently
`BACKSTOP+A_1_2` uniquely writes `(-1,1,1): LAUNCH_A`. With Cycle 52 already
live, the construction then appends exactly

```text
(-2,1,1): B_1_1
(-2,2,1): B_1_2
```

and deliberately stops. Those are the first two records of the transformed
Cycle-52 `B` slice. No third `B` role is enabled because the remaining required
`A` roles have not yet been constructed.

The complete mixed asynchronous graph has exactly **78 reachable states**,
**157 directed edges**, one terminal, zero parasites, zero output conflicts,
and zero overwrite attempts. Every possible single-site interleaving joins the
same 19-write terminal. All 24 rotated/translated graphs have the identical
census and exact transformed terminal.

This is a positive result, so no negative N1–N8 gate is invoked. It is also
**not full nucleation closure**. The exact next residual is

> `REMAINING_A_SLICE_COMPLETION`.

Ten final `A`-slice roles remain open. They must be written correctly before the
Cycle-52 renewal chain can pass `B_1_2` and become the complete autonomous rail
already established in Cycle 52.

## 1. Exact State Zero

State zero is exactly:

```text
(0,0,0): Z0
(0,1,0): H1
(0,2,0): H0
(0,3,0): H1
(0,0,1): H1
(0,0,2): H0
(1,1,1): H1
(0,1,1): BACKSTOP
```

`LAUNCH_A`, both AUX records, `JOINT`, every Cycle-56 certificate, every
Cycle-52 `A` role, and every `B` role are absent. The state has eight records.

Inputs below are exact six-neighbour recorded/open signatures. A displayed
content list is shorthand; direction and every omitted open direction remain
part of the input. All 24 proper-cubic images are live simultaneously.

## 2. Exact Static Construction

The full Cycle-56 extension has these stages:

| Stage | Exact intended sites | Required local contents | Output |
|---|---|---|---|
| AUX orbit | `(0,1,2),(0,2,1)` | `BACKSTOP+H0` | common `AUX` |
| ordinary JOINT | `(0,2,2)` | `AUX+AUX` | `JOINT` |
| RING orbit | `(0,3,1),(1,1,2),(1,2,1)` | `AUX+H1` | common `RING` |
| gated pair join | `(1,2,2)` | `JOINT+RING+RING` | `JOIN` |
| bare pair join | `(1,3,1)` | `RING+RING` | `JOIN` |
| early bare-join image | `(1,2,2)` before JOINT | `RING+RING` | same `JOIN` |
| late JOINT repair | `(0,2,2)` after early JOIN | `AUX+AUX+JOIN` | same `JOINT` |
| completion merge | `(1,3,2)` | `JOIN+JOIN` | `COMPLETE` |
| path root | `(0,3,2)` | `JOINT+RING+COMPLETE` | `P0` |
| P1 orbit | `(-1,3,2),(0,3,3),(0,4,2)` | `P0` | common `P1` |
| ARM orbit | `(-1,3,1),(0,4,1)` | `RING+P1` | common `ARM` |
| first final role | `(-1,2,1)` | `AUX+ARM` | `A_1_2` |
| launcher | `(-1,1,1)` | `BACKSTOP+A_1_2` | `LAUNCH_A` |

There are twelve distinct canonical Cycle-54/56 input signatures. The table
contains two schedule-tolerance ideas that matter:

1. The two pair intersections use one common `JOIN` content. Before `JOINT`
   forms, proper-cubic symmetry can make `(1,2,2)` look like the bare
   `RING+RING` join. Writing the same final content there is safe.
2. That early `JOIN` becomes an extra neighbour of the still-open `JOINT` site.
   The added `AUX+AUX+JOIN -> JOINT` input lets JOINT form late. It changes no
   output and performs no rewrite.

Without the late-JOINT input, one legal schedule terminates early. Without the
common join content, the bare rule permanently mistypes the gated join. The
landed table absorbs both timing orders extensionally while remaining
append-only and single-valued.

## 3. Why The Completion Certificate Works

At the completed Cycle-55 AUX/JOINT scaffold, the only exact-signature class
whose whole orbit is off all final target and official-support sites is the
three-record `RING` orbit. This makes it the forced first common orbit within
the bounded local-orbit route; it is not a claim of global minimum over every
possible alphabet and geometry.

No one lattice site is nearest-neighbour adjacent to all three RING sites. Two
pair joins therefore gather the distributed evidence:

```text
JOIN at (1,2,2) certifies the two positive-side RING records;
JOIN at (1,3,1) certifies the outer and lower RING records;
COMPLETE at (1,3,2) sees both JOIN records.
```

Every RING record is an ancestor of `COMPLETE`. No partial RING schedule can
produce both joins. Downstream path rules therefore cannot suppress an
unwritten RING site, which is the schedule defect that defeated the simpler
ungated branch.

From `COMPLETE`, the path bends around the outside of the final `A` footprint:

```text
COMPLETE -> P0 -> three-site P1 orbit -> two-site ARM orbit.
```

The arm at `(-1,3,1)` is adjacent to `(-1,2,1)`; the second arm is a harmless
required orbit mate. `AUX+ARM` is unique at the intended target under the full
rotated table. The other ten still-open final `A` sites never receive any
content.

## 4. Complete Mixed Asynchronous Graph

The runner scans every open nearest-neighbour candidate after every append. It
combines the full auxiliary table with `c52.enabled_assignments` at every state;
Cycle 52 is not staged off. Each enabled write becomes a separate graph edge.

Exact census:

```text
source records:       8
declared additions:  19
reachable states:    78
directed edges:     157
terminals:            1
parasite states:      0
output conflicts:     0
overwrite attempts:   0
```

The checks quantify every state:

- no untouched final `A` site is ever occupied;
- `A_1_2` is written only at `(-1,2,1)`;
- `A_1_2` precedes `LAUNCH_A` in every state;
- `LAUNCH_A` precedes `B_1_1`;
- `B_1_1` precedes `B_1_2`; and
- the first-role rule never points at an off-target site.

The sole terminal contains exactly the declared 19 additions and nothing else.
Because the graph is finite, append-only, and has one complete terminal, every
maximal asynchronous schedule joins it; no fairness premise selects a preferred
order.

## 5. Raw Rule Table And Covariance

The twelve canonical Cycle-54/56 inputs expand to 234 distinct raw directional
proper-cubic signatures. Every raw signature has exactly one output. None is an
exact input of the Cycle-52 table, whose own mixed table remains conflict-free.
Reachable mixed outputs are likewise single-valued.

For each of the 24 rotations, the runner transforms state zero, all 19 declared
writes, and the official support by the same rotation and a fixed translation.
Every transformed graph again has exactly 78 states, 157 edges, one terminal,
zero parasites, zero conflicts, and zero overwrites. Every transformed terminal
is exactly the transformed declared map, and every footprint is disjoint from
the transformed official support.

## 6. Exact Post-Role Handoff

At the completed off-target path, the auxiliary table exposes only

```text
(-1,2,1): A_1_2.
```

Cycle 52 is still quiet. After that role forms, the auxiliary table exposes
only

```text
(-1,1,1): LAUNCH_A.
```

Cycle 52 remains quiet until the launcher forms. Its successive exact enabled
sets are then:

```text
after LAUNCH_A: {(-2,1,1): B_1_1}
after B_1_1:    {(-2,2,1): B_1_2}
after B_1_2:    {}
```

The terminal deliberately stops at `B_1_2`. This is a clean bounded handoff,
not an autonomous Cycle-52 rail yet.

## 7. Scope And Handoff

Cycle 56 closes the first-role and launcher-last problems for this exact
candidate table. It does not derive the other ten `A` roles, finish the `A`
boundary, or discharge `OFFICIAL_SEED_TO_RAIL_NUCLEATION`.

The next residual is `REMAINING_A_SLICE_COMPLETION`: use the new permanent
RING/JOIN/COMPLETE/P0/P1/ARM wake plus `A_1_2` to force the other ten correct
roles without touching the already-live Cycle-52 outputs. Acceptance must keep
the full mixed table live, preserve every schedule and all 24 rotations, and
join the complete Cycle-52 supplied-boundary state before claiming nucleation.

No constitutional inference follows. This is candidate-law synthesis inside
the current nearest-neighbour Admissibility and permanent Record semantics.

## Verification

```text
python3 scripts/first_role_differentiation_cycle56_2026_07_14.py
PASS=604 FAIL=0
```
