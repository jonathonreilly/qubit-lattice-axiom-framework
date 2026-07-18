# Compact Pair-Barrier Phase — Cycle 74

**Date:** 2026-07-14
**Authority:** none
**Status:** exact finite candidate-law composition; supplied V-gate packet
rejected only as written
**Constitutional effect:** none

Companion runner:

```text
scripts/compact_pair_barrier_phase_cycle74_2026_07_14.py
```

## Result

The repaired Cycle-68 pair barrier admits a substantially smaller complete
phase route than the 91-site Cycle-67 completion cable. The combined finite
construction has 141 variable sites:

```text
Cycle-60 comb                 52
Cycle-68 F/J/K/A/T shell      51
compact completion/phase      38
```

The exact route is

```text
F -> J -> K -> A -> T
  -> U1 -> U2 -> U3 -> U4 -> GUIDE -> HEAD -> L2 -> C_Q
  -> (Q0,QG) -> Q1 -> Q2 -> PHASE_E -> X_B -> (Z_A,Z_C).
```

Its homogeneous nearest-neighbour table has 131 canonical rows and 2,908 raw
rows under the 24 proper cubic rotations. Every raw input has one output.
Every intended non-comb target was compiled over every one of its local
occupancy subsets; 1,462 subsets were considered and all 383 that retained
the named causal parents were installed.

This is not merely a completed-snapshot check. The runner exhausts all 4,050
local subsets at all 350 candidate targets. It finds 160 apparent bad matches,
or 83 target/output classes. It then expands every present later record through
every minimal parent closure and tests the required/forbidden comb bits against
all 242,033 exact Cycle-60 states. Ninety-two contexts contain a direct ancestor
contradiction and the remaining 68 require an impossible Cycle-60 projection.
No apparent bad match is causally reachable.

There are 39 nearest-neighbour pairs between a later record and a Cycle-60
record. In every pair, every parent closure for the later record already
contains that exact comb record. A later record therefore cannot appear beside
an unfinished comb target and permanently remove its Cycle-60 input row. Once
the comb is complete, lower-rank closure fills all 89 later sites in 18 finite
waves. The last wave writes `Z_A` and `Z_C` as independent peers.

## Exact schedule-complete packet

Cycle 68 supplies the first five rows on the unchanged 51-site shell:

| output | sites | required local contents |
|---|---:|---|
| `F` | 6 | `R2 + S8` |
| `J` | 3 | `2 F` |
| `K` | 9 | `J` |
| `A` | 12 | `F + K` |
| `T` | 21 | `A` |

The compact extension is:

| output | representative | orbit | required local contents |
|---|---|---:|---|
| `U1` | `(4,-1,-3)` | 6 | `A + R2` |
| `U2` | `(4,-1,-2)` | 3 | `MARK + 2 U1` |
| `U3` | `(4,0,-2)` | 3 | `A + S8 + U2` |
| `U4` | `(4,1,-2)` | 6 | `T + U3` |
| `GUIDE` | `(3,1,-2)` | 3 | `A + S8 + U4` |
| `HEAD` | `(3,1,-1)` | 3 | `OPEN_C + GUIDE` |
| `L2` | `(0,-2,0)` | 3 | `HEAD + OPEN_B` |
| `C_Q` | `(0,-1,0)` | 1 | `L2 + W6 + Z0` |
| `Q0` | `(0,-1,1)` | 1 | `C_Q + H1` |
| `QG` | `(1,-1,0)` | 1 | `C_Q + J6` |
| `Q1` | `(1,-1,1)` | 1 | `Q0 + QG` |
| `Q2` | `(2,-1,1)` | 3 | `Q1` |
| `PHASE_E` | `(2,-1,0)` | 1 | `Q2 + QG + E + T` |
| `X_B` | `(2,0,0)` | 1 | `PHASE_E + OPEN_B` |
| `Z_A` | `(1,0,0)` | 1 | `X_B + QG + W6 + Z0` |
| `Z_C` | `(3,0,0)` | 1 | `X_B + OPEN_C` |

For every target, every subset of its other variable neighbours is tabulated
when these contents remain present. The exact coordinate sets are frozen as
assertions in the runner, including

```text
U1 = {(1,-4,-3),(1,-2,-5),(2,-4,-2),
      (2,-1,-5),(4,-2,-2),(4,-1,-3)}

U2 = {(1,-4,-2),(1,-1,-5),(4,-1,-2)}
U3 = {(0,-1,-5),(1,-4,-1),(4,0,-2)}

U4 = {(-1,-1,-5),(0,-1,-6),(1,-5,-1),
      (1,-4,0),(4,1,-2),(5,0,-2)}

GUIDE = {(-1,-1,-4),(1,-3,0),(3,1,-2)}
HEAD  = {(-1,0,-4),(0,-3,0),(3,1,-1)}
L2    = {(-1,0,-3),(0,-2,0),(2,1,-1)}
Q2    = {(1,-2,1),(1,-1,2),(2,-1,1)}
```

The added `QG` singleton is load-bearing. It is adjacent to `C_Q` and `J6`;
requiring both `Q0` and `QG` at `Q1` prevents the extra transient `Q1` image
that previously opened an extra `PHASE_E` and allowed `X_B` to steal `L2`.

## Shortest repaired-shell witness

The runner independently freezes the Cycle-68 shortest legacy counterexample.
There is exactly one reachable rank-26 Cycle-60 state with

```text
S8@(0,-1,-4), R2@(1,-2,-4) present;
R2@(1,-3,-3), S8@(0,-3,-2) absent.
```

The old table can append

```text
F@(0,-2,-4) -> A@(0,-3,-4) -> T@(0,-3,-3),
```

where the last output steals the delayed `F` site. In the repaired shell,
`(0,-3,-4)` is `J`, and the one-`F` signature has no row. This is the exact
local job performed by the pair barrier.

## Supplied V1–V6 gate audit

The supplied auxiliary gate does not compose with the repaired shell as
written. Two independent exact defects appear before any broad search:

1. Its `V2` predicate is `T + V1`, with `V1=U1`. Six of the twelve supplied
   `V2` coordinates retain that input. At the other six, the Cycle-68 repair
   has changed the old neighbouring `T` into `K`, so they see `K + U1`.
2. Three supplied `V5` sites are literally three intended `U4` sites:
   `(0,-1,-6)`, `(1,-5,-1)`, and `(5,0,-2)`. A permanent one-content record
   cannot first be `V5` and later become `U4`.

The exact gate partially closes: `V2=6`, `V3=6`, `V4=12`, `V5=6`, and
`V6=6`. All six intended `U4` sites then have the named parents, but three are
already occupied by `V5`, leaving only three writable `U4` sites. Broadening
`V2` to accept `T` or `K` fills the entire V gate but leaves the same three
site collisions. Deleting the colliding `V5` sites leaves three `V6` sites
missing and zero `U4` sites writable. The ungated compact route needs neither
repair and retains the full sixfold `U4` orbit.

One proposed V4 rejection was also checked and discarded. The intended `V4`
input is a perpendicular T-pair. The earlier suggested pair at
`A@(-1,-3,-3)`, `T@(-1,-2,-3)` and `T@(-1,-4,-3)`, is an opposite pair.
Proper cubic rotations preserve that distinction, so it is not a V4 match.
The V-gate rejection rests on the exact V2 and V5/U4 defects above, not on
that invalid witness.

## No-Go Discipline Gate

The skill-freshness check fetched `origin/main`; this section follows the
newer `origin/main` no-go-discipline text rather than the older installed copy.

The negative is deliberately narrow: **the supplied coordinate/predicate
packet does not deliver its stated six-site U4 continuation after the Cycle-68
repair**. No claim is made that every auxiliary gate is impossible.

### N1 — Five attacks on the narrow rejection

| route | marker | result |
|---|---|---|
| Restore the original `F/A/T` labels so all twelve `V2` sites again see `T+U1` | `RULED OUT BY PRIOR` | Cycle 68 lines 14–44 gives the exact six-class delayed-F theft and the failed pure relabel. |
| Keep the repaired shell and the supplied predicates exactly | `ATTEMPTED` | Six `V2` sites remain absent and three `V5/U4` coordinates collide. |
| Broaden `V2` from `T` to `T-or-K` | `ATTEMPTED` | All V rows close; only three U4 sites remain writable because the coordinate collision is unchanged. |
| Delete the three colliding `V5` records | `ATTEMPTED` | Three `V6` records then fail and zero U4 sites have the full open-parent condition. |
| Write `V5` and later overwrite it with `U4` | `RULED OUT BY PRIOR` | Record fixes at most one permanent content per site (`MINIMAL_AXIOMS_2026-06-29.md`, lines 63–72). |

Relocating `V5` or proving a `V5/U4` content equivalence would be a new gate,
not a repair of this exact packet. Those are kept live in N7 rather than
silently ruled out.

### N2 — Wall independence

| pair | close first closes second? | close second closes first? | independent? |
|---|---|---|---|
| `W1`: six `V2` sites see `K`, `W2`: three `V5/U4` site collisions | no — the `T-or-K` run retains all three collisions | no — deleting collisions retains the six missing exact-`V2` sites | yes |

### N3 — Hidden-condition scan

The load-bearing conditions are explicit: the Cycle-68 repaired labels, the
listed V coordinates and predicates, exact nearest-neighbour inputs under
proper cubic rotations, and one permanent content per site. “Canonical” in
this note refers only to the explicitly computed proper-cubic signature
quotient. No background dynamics or unlisted bridge condition is used.

### N4 — Residual matching

| cited witness | cited residual | present residual | match? |
|---|---|---|---|
| `MIXED_TRANSIENT_PAIR_BARRIER_PHASE_CYCLE68_NOTE_2026-07-14.md`, lines 14–44 | original `F/A/T` shell is unsafe during a delayed Cycle-60 F pair | N1 route that restores the original labels | yes |
| same note, lines 46–83 | exact `J/K` relabel repairs that crossfire | fixed repaired-shell baseline used here | yes |

Cycle 65 is context for the audit method, not evidence that this V gate fails;
its residual is the superseded Cycle-64 table and is not counted here.

### N5 — Rhetoric audit

Tested: each supplied V site, the complete finite V block, and its interface to
the six supplied U4 sites. Not tested: every possible V-site relocation,
content quotient, unbounded lattice gate, or recurrent block. The claim is
therefore restricted to this exact finite packet.

### N6 — Partial-closure scan

The supplied packet does real partial work: all twelve V4, six V2, six V3,
six V5, and six V6 records can form. More importantly, the ungated 38-site
route closes the full target without either wall. No new axiom, primitive, or
owner ruling is requested by this finite repair.

### N7 — Steelman

A hostile reviewer can reasonably argue that the V idea, rather than the gate
class, is still live: relocate the three V5 records, retable V2 against the
new `K` role, or prove that one content can play the downstream functions
currently named `V5` and `U4`. This could produce a valid redesigned gate.
That steelman succeeds against a broad no-go, so the broad no-go is not made;
the result remains an exact-candidate rejection with those redesigns open.

### N8 — Cross-cycle echo

Cycle 64 was rejected by Cycle 65 because terminal signatures hid transient
type races. Cycle 68 then repaired that failure by adding physically distinct
`J/K` local roles. That history shows that a role/cage redesign can retire this
kind of wall. The same mechanism could repair a future V gate, which is why
this note does not call the gate class impossible. It also explains the
present mismatch: the supplied V coordinates were designed against the old
Cycle-62 `T` shell and were not recompiled after Cycle 68 changed nine of
those contents to `K`.

**Gate outcome:** the broad V-gate no-go fails N7 and is not shipped. The
artifact is demoted to the narrow, executable rejection of the exact supplied
packet. All N1–N8 fields for that narrowed claim are recorded above.

## Scope

This is candidate-law engineering on a finite declared footprint. It does not
select the local law from the four axioms, derive record-production weights or
rates, derive Born statistics, identify commit count with physical time, prove
unbounded renewal, or validate the Cycle-63 endpoint/recurrent builder. It
does show that the finite completion-sensitive `C -> X -> {Z,Z}` path itself
can be made exact and schedule-safe without the auxiliary V gate.
