# Cycle-67 Terminal B/D/H Rebind — Cycle 72

**Date:** 2026-07-14  
**Authority:** none  
**Status:** exact conditional terminal-to-terminal construction  
**Constitutional effect:** none

Companion runner:

```text
scripts/cycle67_terminal_bdh_rebind_cycle72_2026_07_14.py
```

## Result

Starting from the actual 181-record Cycle-67 terminal, a 27-row homogeneous
strict-nearest-neighbour proper-cubic extension writes the exact Cycle-14
`B/D/H` projection and reaches the translated preparation boundary.

```text
new canonical rows          27
new proper-cubic raw rows  612
full C60/C67/C72 rows      147
full proper-cubic rows   3,206
new records                 31
compiled conditions         49
reachable states           465
append edges             1,307
complete terminals           1
incomplete terminals         0
parasites                    0
output conflicts             0
```

The 31 records are the eighteen official `B/D/H` records plus thirteen
off-support isolation-tail records. No replacement preguide is needed: the
Cycle-67 cable terminal already supplies the missing orientation.

## Exact Cycle-63 overlap

Cycle 67 occupies exactly eleven coordinates in Cycle 63's old generated
footprint.

| coordinate | Cycle 67 | old Cycle 63 |
|---|---|---|
| `(1,-2,1)` | `L10` | `L1` |
| `(1,0,0)` | `Z_A` | `Z_A` |
| `(2,-3,0)` | `L7` | `G2` |
| `(2,-2,0)` | `L8` | `G0` |
| `(2,-2,1)` | `L9` | `K` |
| `(2,-2,2)` | `L10` | `L1` |
| `(2,-1,1)` | `L10` | `G0` |
| `(2,-1,2)` | `L11` | `G2` |
| `(2,0,0)` | `X_B` | `X_B` |
| `(3,-2,0)` | `L7` | `G2` |
| `(3,0,0)` | `Z_C` | `Z_C` |

The three endpoint/output contents agree exactly. The other eight sites keep
their Cycle-67 cable labels; none is relabelled or overwritten.

Every Cycle-72 addition is at a coordinate already used by Cycle 63 and has
the same final content. Twelve old Cycle-63 sites are omitted: eleven obsolete
orientation-preguide coordinates and the optional second `OY` image. Thus the
new terminal uses 31 old coordinates, preserves 11 already occupied old
coordinates, and leaves the remaining 12 unfilled.

## Why the preguide disappears

At the Cycle-67 terminal:

```text
D_y@(2,1,0) sees a singleton X_B context;
D_z@(2,0,1) sees a singleton X_B + L10 context.
```

Those are the only two initially enabled Cycle-72 writes. They may occur in
either order. Once each branch has its `D1`, the canonical `D1+Z_C` class is
exactly the intended pair

```text
H_y@(3,1,0), H_z@(3,0,1).
```

The preserved `L11` cable context also participates in the z-side first-B and
`D0` cages. This uses the actual terminal as local information; it does not
pretend the old `G0/K/L1/G2` contents were written under new names.

## Exact chronology

The early partial order is

```text
Cycle-67 terminal
  |-- D_y --+-- B_y
  |         `-- H_y
  `-- D_z --+-- B_z
            `-- H_z
```

The two D branches commute. Within either branch, the first B and first H also
commute after their D. Consequently this is not strict `B<D<H`, and it is not
the exact Cycle-63 microscopic order either. D records can precede every new B;
an H can precede every new B; and a first B can precede its branch's first H.

The later safety properties survive exhaustively:

- isolated `B5@(2,1,1)` is always the last of the six B records;
- `D5` never precedes `B5`;
- `H5` never precedes `D5`; and
- a complete six-record H header implies all six B and all six D records.

All 465 asynchronous states join the same 31-record terminal. Projection onto
the eighteen official sites is exactly the Cycle-14 `B/D/H` union.

## Rebind

At the terminal, the six H records are the translated header. The next

```text
q'=(3,-1,0), a'=(4,0,0), b'=(5,0,0), c'=(6,0,0)
```

remain open, every new auxiliary avoids the next-only official block, and the
record map decodes exactly the current and translated programs.

## Boundary

This runner exhausts every downstream schedule **from the completed Cycle-67
terminal**. It includes the Cycle-60 and Cycle-67 rows in the checked union,
and none reactivates at that boundary. It does not yet prove that Cycle-72 rows
cannot fire harmlessly or prematurely during every transient Cycle-67 state;
that is a separate mixed-composition audit analogous to Cycle 71.

No recurrence, renewal, exact-law selection, axiom need, probability law, or
duration calibration follows from this finite conditional construction.
