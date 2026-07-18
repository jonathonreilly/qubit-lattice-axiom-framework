# Joint-Endpoint Mixed Rebind — Cycle 78

**Date:** 2026-07-14
**Authority:** none
**Status:** exact mixed-transient candidate-law closure
**Constitutional effect:** none

Companion runner:

```text
scripts/joint_endpoint_mixed_rebind_cycle78_2026_07_14.py
```

## Result

Cycle 78 closes the Cycle-72 mixed-transient race while retaining Cycle 63's
actual joint-endpoint property:

> Every B record has both `Z_A` and `Z_C` in its mandatory ancestry, and B5
> is the final B in every conditional schedule.

This is stronger than merely reaching the right terminal map. Cycle 77 and
the Cycle-79 caged repair are mixed-safe smaller constructions, but each
permits at least one B before both endpoints exist.

The first join is generated off support:

```text
W4 + W6       -> Y2   (two-record class)
OPEN_B + Y2   -> YG0  (two-record class)
OPEN_C + YG0  -> GY   (two-record class)
Z_C + GY      -> H_y
H_y + X_B     -> D_y  (also oriented by YG0)
Z_A + D_y     -> B_y  (also oriented by Y2)
```

Thus `B_y`, and the y-side tail it launches, already descend from both
endpoints.

## The post-BZ export constraint

The old z-side order wrote `B0_z` before `B_z`. Once `B_z` formed, all six of
its neighbours were already records. In an append-only nearest-neighbour
model that means `B_z` had no open site through which to certify a later B5.
Stage order alone cannot fix this: the local table still permits any row as
soon as its actual neighbours exist.

Cycle 78 therefore carries the joined y ancestry to `TZ`, then writes the
z-side chain in the opposite causal order:

```text
BTQ -> TJ/J/M guide -> TZ -> D5 -> H_z -> D_z
Z_A + D_z           -> B_z
B_z                  -> B0_z -> D0_z -> AUX_z -> B5.
```

`B0_z` is the open neighbour left for `B_z`; it is the physical export cable,
not a bookkeeping ordering. Consequently `B5` cannot form before `B_z`, and
every downstream B inherits the joint endpoint ancestry.

The exact off-support export rows are:

```text
BTQ          -> TJ pair
JOIN + TJ    -> J1
RING + J1    -> J2
TJ + J2      -> J3
TJ + TJ      -> G1
G1 + J3      -> M
TJ + M       -> TZ
```

`MX` and `GU` are a small isolation cage around the later U row. Without
that cage, the bare TJ input can write U onto still-open guide sites. The
mixed scan detects that theft; `M -> MX`, `G1+MX -> GU`, and `TJ+GU -> U`
remove it.

## Exact certificate

```text
new canonical rows             39
new proper-cubic raw rows     870
full C60/C67/C78 rows         159
full proper-cubic rows      3,464
append-only additions          47
conditional conditions         72
conditional states         10,568
conditional edges          49,142
conditional terminals           1 complete
parasites/conflicts              0
```

The official projection remains exactly six B, six D, and six H records with
the Cycle-14 contents. No non-B/D/H addition occupies current official
support, and every addition avoids the next-only translated block.

The mixed audit retains every 242,033 reachable Cycle-60 state and Cycle 70's
67 exact Cycle-67 phase-availability masks. Correct downstream histories add
15 availability masks. The local scan deliberately admits arbitrary subsets
below each maximum, so it is a safety over-approximation:

```text
interface candidates                 456
retained candidates                  218
mixed local contexts              96,617
apparent wrong contexts              891
apparent wrong target/output classes  51
feasible wrong writes                  0
feasible raw conflicts                 0
feasible Cycle-60 blockers             0
feasible Cycle-67 blockers             0
```

Every apparent wrong context has a present descendant while one of its
mandatory local ancestors is required absent. Therefore none can be the
first bad append. The conclusion is not based on deleting static aliases;
each of the 891 contexts carries the first-bad contradiction.

## Exact comparison with the smaller green repairs

| Construction | Additions | Canonical rows | Mixed contexts | Feasible wrongs | Every B joint? |
|---|---:|---:|---:|---:|---|
| Cycle 77, BY-first | 31 | 27 | 19,240 | 0 | no |
| Cycle 79, caged two-layer guide | 35 | 29 | 69,447 | 0 | no |
| Cycle 78, joint-endpoint export | 47 | 39 | 96,617 | 0 | yes |

Relative to the 35-addition caged repair, Cycle 78 retains every one of its
sites and adds exactly 12. It uses 39 rather than 29 canonical rows. Counting
non-B/D/H output labels, the caged construction has 13 and Cycle 78 has 21:
eight net additional role types. More structurally, the caged route has two
guide roles over four records; Cycle 78 adds a third two-record join layer and
the post-join TJ/J/M export-and-isolation cable needed to leave `B_z` an open
causal outlet.

This is not a global or family-wide minimality result. It is the current
successful joint-endpoint construction after enforcing mixed safety and the
last-B invariant.

## Failed and scoped comparators

Cycle 72's bare `X_B -> D_y` row has one real mixed race: while `OPEN_C` is
delayed, it writes `D1` at the still-open `Z_C` target.

Cycle 76 removes that race but is not mixed-safe. Its
`E+L8+L10 -> YS` row can permanently steal `P1` before `P0` and `P3` before
`P2`; Cycle 79 finds twenty causally feasible contexts in exactly those two
classes.

Cycle 77's zero-site reorder (`Z_A -> B_y -> D_y`) and Cycle 79's `W4/W6`
caged guide both remove their scoped mixed defects. They remain valid smaller
conditional constructions when joint-endpoint B ancestry is not required.

Cycle 63 allowed early H and D signals after `Z_C` but before `Z_A`; its
exhaustive invariant was specifically that no **B** preceded both endpoints.
Cycle 78 preserves that exact invariant rather than silently strengthening it
to all B/D/H records.

## Rebind and boundary

The completed H map is the translated header; the next `q'/a'/b'/c'` stay
open; and the terminal decodes exactly the current and translated programs.

This is a finite candidate-law construction, not exact-law selection,
recurrence, renewal, an occurrence-weight law, a duration calibration, or an
axiom result.
