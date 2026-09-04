# C129 bridge to orientation-13 writer interface — Cycle 130

Date: 2026-07-15

Authority: none

Disposition: campaign bounded-negative artifact for direct same-port
proper-cubic reuse; audit status unset

Write scope: runner + review note only

Companion runner:

```text
scripts/r_b01_cycle129_bridge_orientation13_interface_cycle130_2026_07_15.py
```

No predecessor, foundation, axiom, primitive, registry, queue, policy, audit,
or git state is edited here. No commit, push, or PR is made. The Cycle-129
runner supplies the executable campaign predecessor; its audit status is not
set here.

## Exact bounded object

Cycle 130 tests

```text
R_B01_CYCLE129_SAME_PORT_DIRECT_ORIENTATION13_INTERFACE
```

The complete Cycle-129 bridge remains anchored at the same generated `R_B01`
port `(5,4,-3)`. Each of its 17 physical bridge-record displacements is acted
on by all 24 proper-cubic rotations. The resulting 408 placements are compared
with the fixed orientation-13 phase interface:

```text
G0 = (5,1,-3)
G1 = (6,1,-3).
```

The test asks only whether an already generated Cycle-129 bridge record can,
under a rotated copy of the same anchored grammar, land directly beside G0 or
G1 and serve as causal provenance. It does not search connectors, translate
the port, or relocate the writer.

## Displacement census

Relative to the R_B01 port, the complete G0 neighbour shell is

```text
(-1,-3, 0)  (0,-4, 0)  (0,-3,-1)
( 0,-3, 1)  (0,-2, 0)  (1,-3, 0).
```

The alternate G1 shell, excluding G0 itself, is

```text
(1,-4, 0)  (1,-3,-1)  (1,-3, 1)  (1,-2, 0)  (2,-3, 0).
```

The exact census is:

```text
bridge records                               17
proper-cubic rotations                       24
rotated placements                          408
G0-shell coincidences                         0
alternate-G1-shell coincidences               3
```

The three G1-shell coincidences are:

| Rotation | Bridge record | Rotated target | Writer meaning |
|---:|---|---|---|
| 3 | `A_0_0` generation 2 | `(6,2,-3)` | old D4 coordinate |
| 7 | second `TY` image, generation 8 | `(6,1,-4)` | otherwise clean alternate neighbour |
| 11 | second `TY` image, generation 8 | `(6,1,-2)` | old D6 coordinate |

Geometry alone therefore produces three apparent parent placements. Exact
prefix replay rejects all three.

## Exact prefix mismatches

### Rotation 3: shared launch, missing fixed context

Rotation 3 leaves the first `OZ` target at `(5,3,-3)`, so the original
`H1 + R_B01 -> OZ` launch remains available. Its next rotated `W3` target is

```text
(6,3,-3) = old D1.
```

At that point the actual local is only

```text
OZ.
```

The Cycle-129 W3 row requires the four-parent local

```text
T_H3 + H0 + R_A01 + OZ.
```

Thus the rotated prefix stops at generation 1, before its generation-2
`A_0_0` shell coincidence. Even if the missing context were supplied, this
copy would permanently occupy old D1 with `W3` and old D4 with `A_0_0`, while
the campaign writer construction requires data contents at both coordinates.

### Rotation 7: clean final shell, wrong launch local

Rotation 7 would place the later `TY` image at the otherwise clean G1
neighbour `(6,1,-4)`. But its generation-0 `OZ` target is

```text
(6,4,-3) = old D0.
```

That site sees unary `R_B01`, not the required `H1 + R_B01`. The rotated
grammar therefore cannot launch. It would also consume old D0 if a new launch
row were invented.

### Rotation 11: occupied launch

Rotation 11 would place `TY` at

```text
(6,1,-2) = old D6.
```

Its first `OZ` target is `(5,4,-2)`, already the permanent Cycle-121 `R_B00`
completion record. The rotated copy fails at generation 0 by occupancy before
any local-row question arises, and the eventual coincidence would consume old
D6.

## Exact conclusion

The Cycle-129 bridge does carry causal provenance. Its original `A_0_0` and
`TY` records are generated through multi-parent histories. The failure is the
interface geometry: anchored at the unchanged R_B01 port, no bridge record
lands in G0's shell, and the only three G1-shell coincidences lack an
executable unoccupied rotated prefix in the actual terminal context.

This is **not a failure of the provenance mechanism**. It is **not a no-go against an R_B01 writer**. The smallest live repairs are:

- a **causally forced connector** from the executable, unrotated Cycle-129 bridge
  into a clean writer-parent site;
- **writer relocation** onto a two-parent corner already created by the
  Cycle-129 bridge;
- a translated bridge anchored at a different physical port or frame face.

No unary prefix is licensed by this result, and **no axiom addition follows**.

## Bare-metal meaning

Causal provenance and geometric reach are separate obligations. Cycle 129
solved the first: its guard is genuinely required before JOINT can form. Cycle
130 shows that rotating the drawing does not automatically rotate the fixed
records surrounding the port. A covariant rule can reuse a local signature
only where the entire local signature exists, not wherever a later output
coordinate happens to look convenient.

The exact mismatch is one interface layer, not missing physics: either carry
the causal output through another locally forced connector or build the writer
where the causal output already has the right neighbours.

## N1–N8 no-go-discipline gate

Status: **PASS only for the direct same-port proper-cubic interface bounded
negative; FAIL for a universal orientation-13, bridge, provenance, writer,
recurrence, or axiom-need no-go.** The current `origin/main`
no-go-discipline body governs this note.

### N1 — Alternative routes

| Route | Marker | Result |
|---|---|---|
| all 24 rotations of all 17 anchored bridge records | `EXHAUSTED / NEGATIVE FOR DIRECT INTERFACE` | zero G0 hits; three G1 hits; every matching prefix fails exactly |
| rotation-3 A00 parent | `ATTEMPTED / NEGATIVE` | W3 prefix has unary OZ instead of four-parent context and occupies D1/D4 |
| rotation-7 TY parent | `ATTEMPTED / NEGATIVE` | OZ launch sees unary R_B01 and occupies D0 |
| rotation-11 TY parent | `ATTEMPTED / NEGATIVE` | OZ launch target already contains R_B00; TY occupies D6 |
| causally forced connector from unrotated bridge | `LIVE / PREFERRED` | adds the missing geometric interface without discarding C129 provenance |
| writer relocation onto a C129 two-parent corner | `LIVE / PREFERRED` | changes the writer geometry rather than forcing an old shell |
| translated port/frame attachment | `LIVE` | changes the anchor and therefore the surrounding context |
| orientation-20 writer redesign | `LIVE` | independent geometry; its tail obligation is still open |

At least four materially distinct construction routes remain. No universal
negative ships.

### N2 — Residual independence

| Pair | First closes second? | Second closes first? | Treatment |
|---|---|---|---|
| causal provenance vs geometric adjacency | no | no | Cycle 129 closes the first; Cycle 130 tests one route to the second |
| displacement coincidence vs executable prefix | no | prefix includes it | one ordered interface test, not two walls |
| direct same-port reuse vs connector | no | connector changes tested family | connector remains live |
| writer relocation vs old-shell repair | no | no | independent constructive branches |
| writer existence vs exact-law selection | no | no | independent residuals |

The three failed coincidences are cases within one direct-reuse family, not
three separate arguments for a broad obstruction.

### N3 — Hidden-condition scan

The exact R_B01 anchor, 17 physical bridge outputs, 16 bridge generations, 24
proper-cubic rotations, 408 displacement placements, fixed orientation-13
G0/G1 shells, Cycle-129 base terminal, first rail slice, occupied sites,
expected generation locals, and writer data coordinates are explicit. A
“hit” means coordinate equality with a shell site; an “executable prefix”
requires each preceding transformed generation to have the same canonical
local in the actual source context. No global rotation of the terminal,
supplied support, scheduler, overwrite, clock, or reader is assumed.

### N4 — Residual matching

| Witness | Witness residual | Cycle-130 residual | Match and use |
|---|---|---|---|
| Cycle 129 campaign construction | guarded head/frame bridge at one anchor | direct writer-parent interface at same anchor | exact predecessor and tested output corpus |
| Cycle 128 campaign artifact | fixed-shell parent must be history-safe and causal | reuse C129 causal records in that shell | exact proposed follow-up |
| rotation-3 coordinate hit | later A00 at D4 | complete rotated prefix | partial match only; prefix fails |
| generic C129 connector | any locally forced extension | zero-extension displacement census | no match; remains live |
| generic writer relocation | arbitrary new data/cage layout | fixed G0/G1 shell | no match; remains live |

Nonmatching residuals constrain rhetoric rather than support enlargement.

### N5 — Resolution and rhetoric

Tested: every physical C129 bridge record, every proper-cubic rotation, both
fixed shells, and the exact transformed prefix through the first failure for
all three shell coincidences. Not tested: any added connector row, translated
anchors, relocated writer sites, alternative frame faces, or every R_B01
writer. “No direct anchored reuse” cannot become “C129 cannot seed a writer”
or “provenance does not work.”

### N6 — Partial-closure paths and axiom discipline

The one-layer interface can be attacked constructively inside the current
rules. A connector may require two existing C129 records and write a fresh
parent at a clean shell site. Alternatively, the writer can be relocated so
its first cage record forms at an already available two-parent corner. Both
paths use strict nearest-neighbour, proper-cubic, append-only rows. This result
does not select axiom text, a primitive, or an import.

### N7 — Strongest hostile steelman

A hostile reviewer should reject a coordinate-only reuse claim: the three
later records reach useful shell coordinates under rotation, but their fixed
support did not rotate with them. One candidate has only unary OZ where four
parents are required, another has unary R_B01 at launch, and the third starts
on permanent R_B00. That kills the exact direct-copy proposal. The same
reviewer cannot reject a connector or relocated writer, because those routes
explicitly change the missing local context rather than pretending it is
present.

### N8 — Cross-cycle echo

Cycles 121 and 129 both repaired full-history aliases with causal provenance.
Cycles 127 and 128 showed that role names and independently enabled records do
not supply causal distinction. Cycle 130 adds the geometric counterpart:
provenance cannot be moved by rotating only the desired endpoint. The next
construction must carry the full local context through a connector or place
the writer at an existing two-parent context. This is a compiler-interface
lesson, not constitutional evidence.

## Verification

```text
python3 scripts/r_b01_cycle129_bridge_orientation13_interface_cycle130_2026_07_15.py
```
