# Mixed Cycle-76 Caged-Guide Audit — Cycle 79

**Date:** 2026-07-14
**Authority:** none
**Status:** exact Cycle-76 rejection; conditionally green local repairs
**Constitutional effect:** none

Companion runner:

```text
scripts/mixed_cycle76_caged_guide_audit_cycle79_2026_07_14.py
```

## Result

Cycle 76 really does remove Cycle 72's old race at `c=(3,0,0)`. It does not,
however, survive the full mixed history.

Its first guide row is

```text
E + L8 + L10 -> YS.
```

That same exact local signature occurs at the still-open `P1=(1,-2,0)` and
`P3=(2,-1,0)` sites after a valid 73-record Cycle-67 prefix through `L10`.
The law therefore writes `YS` permanently where `P1` or `P3` must later go.
This is not a static subset warning: the runner constructs a literal sequence
in which every earlier append is correct.

The narrow verdict is:

> The exact Cycle-76 `E+L8+L10 -> YS` packet is not live-composition safe.

The guide idea is not rejected. Moving its first layer into the already
present `W4/W6` cage removes the alias without changing the projection or
adding a new axiom.

## What happened to the old Cycle-72 race

Across all 242,033 reachable Cycle-60 states, there are exactly 24 states in
which the maximal Cycle-67 continuation contains `X_B` while the `OPEN_C`
neighbour of the future `Z_C` site is absent. Cycle 72's bare row then reads

```text
X_B -> D1
```

at `Z_C`, stealing the endpoint. Cycle 76 deletes that input row. Thus its
`YS/YG` guide succeeds at the job it was designed to do.

The defect is a new one: it moves the first-bad write from `Z_C` to the phase
return cable. Removing one local alias is not enough; every earlier mixed
prefix must be scanned.

## Static false positives versus causal schedules

The strong scan retains:

- every reachable Cycle-60 state;
- all 67 exact Cycle-67 availability masks;
- arbitrary subsets of every locally available downstream stage; and
- every interface target on which any component row can act or be blocked.

For Cycle 76 it finds:

```text
interface candidates                         434
retained candidates                          207
mixed local contexts                      27,386
ancestry-certified wrong contexts            496
ancestry-certified target/output classes      48
causally feasible wrong contexts               20
causally feasible target/output classes         2
feasible raw conflicts                          0
feasible Cycle-60 blockers                      0
feasible Cycle-67 blockers                      0
```

The 496 certified contexts are static false positives. Each contains a
present record while requiring one of that record's unavoidable ancestors
absent, so none can be the first bad append.

The remaining twenty contexts quotient to exactly two classes:

```text
P1 : expected P1, Cycle-76 row writes YS
P3 : expected P3, Cycle-76 row writes YS
```

They have no absent-ancestor witness. More decisively, one exact causal
schedule realizes both signatures: complete Cycle 60, then append the 73
Cycle-67 records in rank/site order through `L10`. Every one of those writes
is accepted by the Cycle-67 table. Before `P0` or `P2` exists, the open `P1`
and `P3` sites both see exactly `E+L8+L10`. Cycle 76 returns `YS` at each.
The correct phase writes require `P0` and `P2`, respectively, so neither can
have protected the site earlier.

## Minimum local repair tournament

The probes held the complete projection and isolation tail fixed and varied
only the first guide geometry.

| Route | Additions | Mixed contexts | Feasible wrong writes | Outcome |
|---|---:|---:|---:|---|
| Cycle 76, `E+L8+L10 -> YS` | 39 | 27,386 | 20 / 2 classes | rejects exact packet |
| add `L7+S8 -> Y0` before old YS | 39 | 27,664 | 20 / 2 classes | `Y0` writes off footprint |
| add `J6+L11 -> Y0` before old YS | 37 | 27,062 | 10 / 1 class | `Y0` steals `P2` |
| move YS to the `W4/W6` cage | 35 | 69,447 | 0 | conditionally green |
| Cycle-77 BY-first reorder | 31 | 19,240 | 0 | conditionally green |

The two failed preguide probes are informative. Another upstream guide does
not solve the problem if its own local signature is reused by the live phase
cable:

```text
L7+S8 preguide: off-footprint Y0 at (1,-3,0) and (3,-1,0)
J6+L11 preguide: Y0 at the intended P2 site
```

No global minimum is claimed. These are the closest tested variants around
the Cycle-76 geometry.

## The caged two-layer guide

The smallest tested repair that retains Cycle 76's two-layer shape is:

```text
W4 + W6      -> YS  (two-site exact class)
OPEN_B + YS  -> YG  (two-site exact class)
X_B + YG     -> D_y
X_B + L10    -> D_z
```

The exact guide classes are:

```text
YS: (0,1,-2), (1,1,-1)
YG: (0,1,-3), (2,1,-1)
```

None of those four guide sites is adjacent to a Cycle-67 target. This is the
bare-metal reason the relocation works: the first guide is keyed by two
already written cage records, not by a signature that the still-growing
phase cable must itself pass through.

Exact finite census:

```text
new records                    35
new canonical rows             29
full C60/C67/repair rows       149
full proper-cubic raw rows   3,272
conditional conditions         53
conditional states          1,455
conditional edges           5,023
conditional terminals           1 complete
parasites/conflicts              0
```

Full mixed scan:

```text
interface candidates                         435
retained candidates                          207
mixed local contexts                      69,447
ancestry-certified wrong contexts            496
ancestry-certified target/output classes      48
causally feasible wrong contexts                0
feasible raw conflicts                          0
feasible Cycle-60 blockers                      0
feasible Cycle-67 blockers                      0
```

The larger context count is not a regression. It comes from admitting more
arbitrary local subsets around the relocated pair. Every one of the 496
wrong-looking contexts has a first-bad ancestry contradiction; none has a
causal schedule.

## Which green repair is appropriate

There are now three different scoped successes, with different semantics:

1. The Cycle-77 BY-first reorder is smallest: no added guide records and no
   feasible mixed defect. It permits B records before `Z_C`.
2. The caged Cycle-76 repair keeps the two-layer guide and is also mixed-safe
   in this model. It likewise does not prove that every B record has both
   endpoint records in its mandatory ancestry.
3. Cycle 78 adds a third guide layer and has already proved the stronger
   joint-endpoint invariant: every B record descends from both `Z_A` and
   `Z_C`.

So the selection is not “which table passes?” All three can pass their scoped
mixed checks. The scientific question is whether joint-endpoint ancestry is
part of the intended record-formation mechanism. If yes, Cycle 78 is the
current relevant construction. If no, the smaller BY-first or caged route is
enough. This remains a conditional-law distinction, not an axiom ruling.

## N1–N8 no-go discipline for the Cycle-76 rejection

### N1 — alternative-route enumeration

Five nearby routes were kept explicit: the original Cycle-76 guide, two
single-preguide repairs, the `W4/W6` caged relocation, and the orthogonal
BY-first reorder. The original and both preguides fail under the same mixed
scanner; the latter two close the scoped defect. Cycle 78 is the stronger
joint-endpoint comparator.

### N2 — wall-independence audit

`P1` and `P3` are not counted as two independent walls. They realize the same
proper-cubic canonical `E+L8+L10` input and are two manifestations of one
shared signature-reuse wall. Likewise, the two `L7+S8` off-footprint targets
form one symmetry-related failure family.

### N3 — hidden-wall scan

The audit includes partial Cycle-60 histories, partial Cycle-67 availability,
arbitrary available downstream subsets, off-footprint targets, cross-table
output conflicts, and irreversible blockers of open Cycle-60 or Cycle-67
targets. The exact downstream graph separately checks terminal completion,
parasites, and conflicts. Joint-endpoint ancestry is reported separately so
that a green safety result is not mistaken for that stronger invariant.

### N4 — residual matching

The scanner's only feasible Cycle-76 classes are exactly the two targets
realized by the independent 73-append schedule. There is no unexplained
residual between the over-approximation and the constructive counterexample.

### N5 — rhetoric audit

The negative claim is only about the exact Cycle-76 `YS` input in the finite
C60/C67 composition. It is not a no-go for guides, local append-only laws,
the Cycle-67 completion barrier, or the framework.

### N6 — partial-closure path scan

Both the caged relocation and BY-first reorder reach zero feasible mixed
defects. The failure therefore closes a wording/geometry choice, not the
whole construction lane.

### N7 — strongest steelman

The strongest simple defense of Cycle 76 is that the guide only needs a more
private first signature. The `W4/W6` cage realizes precisely that defense and
passes. A broader no-guide conclusion would therefore be false.

### N8 — cross-cycle echo

This repeats the Cycle-65/68 lesson: a table that is exact on its completed
source can still alias a live intermediate role. Local role separation and a
caged signature can retire the alias, but only a mixed-history audit shows
that it did.

## Boundary

This runner does not select an exact universal law, prove recurrence or
renewal, derive probabilities or durations, or justify axiom language. It
shows only that the Cycle-76 terminal-green result was insufficient, gives an
exact counter-schedule, and identifies two conditionally green local repairs.
