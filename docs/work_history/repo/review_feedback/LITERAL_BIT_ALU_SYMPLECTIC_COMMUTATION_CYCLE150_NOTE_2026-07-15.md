# Literal-bit ALU and symplectic commutation — Cycle 150

Date: 2026-07-15

Authority: none

Disposition: local campaign-positive literal-bit compiler; audit unset

Companion runner:

```text
scripts/literal_bit_alu_symplectic_commutation_cycle150_2026_07_15.py
```

No foundation, axiom, primitive, registry, queue, policy, audit, commit, push,
or PR is changed.

## Result

Cycle 150 pushes the compact quantum compiler below the 32-role Pauli-row
codebook. It constructs a recurrent **literal-bit ALU** on permanent H0/H1
records and uses it to build **physical symplectic commutation**.

The ALU needs two operation roles and eight canonical rows:

```text
left bit + right bit + XOR -> result bit
left bit + right bit + AND -> result bit.
```

Together with a recorded `1`, XOR and AND are a functionally complete Boolean
basis: NOT is XOR with one, and OR is `XOR(XOR(x,y),AND(x,y))`. This is an
expressiveness fact, not yet a claim that every resulting circuit has been
embedded collision-free.

The commutation circuit computes

```text
x0*z0' XOR z0*x0' XOR x1*z1' XOR z1*x1'
```

from literal row bits. Four independent AND records form first; a central
parity record forms only after all four exist. Its proper-cubic quotient needs
six canonical parity rows rather than sixteen coordinate-labelled rows.

Commuting multiplication and pivot remain open. Cycle 150 supplies the
decision bit needed by the measurement algorithm but not yet the replacement
row records. It does not derive equal outcome weights. No axiom addition
follows.

## Recurrent ALU

An ALU target sees five records:

```text
current accumulator H0/H1
operand H0/H1
XOR or AND role
two MARK frame/guard records.
```

The sixth face remains open, so the output bit becomes the next accumulator.

```text
canonical ALU rows                                 8
proper-cubic ALU rows                            192
Cycle-149 rows                                70,652
ALU union rows                                70,844
raw conflicts                                      0
```

All length-three programs are tested over two initial bits, four possible
operation/operand instructions, and all 24 proper-cubic images:

```text
instances                    24 * 2 * 4^3 = 3,072
reachable states aggregate                 12,288
append edges aggregate                       9,216
wrong/unexpected histories                       0
```

Deleting one of five direct parents from each of eight rows gives 40 controls;
none retains the output.

## Symplectic circuit geometry

The parity target is central. Its four axial equatorial neighbours are the
AND-output targets; two MARK records occupy the remaining axial pair. Each AND
unit is rotated so its one open face points toward the center. Their outer
parents are eight literal input-bit records, four AND roles, and four shared
MARK corner guards. A quiet MARK shell prevents the exposed input records from
activating older rows.

The four term records are independent and can form in any order. The central
record then forms. Therefore each exact asynchronous graph has:

```text
states                                   2^4 + 1 = 17
append edges                                  32 + 1 = 33
maximum term frontier                                  4
term-order terminals                                     1
```

The central signature is invariant under proper rotations that permute the
four term positions. Canonicalization groups the sixteen bit patterns into six
geometric/Hamming classes, each of which has one parity output:

```text
canonical parity rows                                6
proper-cubic parity rows                            48
full union rows                                 70,892
raw conflicts                                         0
```

Every pair of 32 signed Pauli rows is tested in every proper-cubic image:

```text
instances                     32 * 32 * 24 = 24,576
reachable states aggregate                    417,792
append edges aggregate                         811,008
wrong parity / unexpected histories                  0
```

The sign bits deliberately do not enter symplectic commutation; the full
signed census verifies that invariance rather than reducing the input list by
assumption. Deleting any of six central parents across the six canonical rows
gives 36 controls; none retains its parity output.

## Mixed-device closure

The 240 new raw rows are added to the Cycle-149 union. Under that enlarged
law:

- all 86,640 prior mixed Clifford/measurement two-event histories retain their
  exact frontiers and terminals;
- the Cycle-144 physical/recurrent terminal retains its two priced fronts;
- no raw conflict or new apparatus write occurs.

The literal-bit and role-level compilers can therefore coexist while the
replacement is developed.

## What this changes in the compactness ledger

Cycle 149's 128-row machine still used one role for each five-bit row. Cycle
150 shows that the first load-bearing operation on those rows—symplectic
commutation—does not require a 32-by-32 role table. It is generated from:

```text
8 Boolean ALU rows + 6 symmetric parity rows = 14 canonical rows.
```

This is not yet a complete replacement of the row-role machine. Gate update
needs bit permutation and phase logic; measurement update also needs signed
commuting multiplication, pivot selection, and two output rows. But the
largest decision fork in the pivot algorithm has now crossed the bare-metal
interface using literal bits.

## N1 — Alternative routes

| Route | Outcome |
|---|---|
| 32x32 commutation table over row roles | viable but 1,024 contexts |
| Host symplectic parity | predecessor only |
| Serial accumulator with precomputed products | rejected; hides AND terms |
| Four physical ANDs plus central parity | positive |
| Sixteen coordinate-labelled parity rows | unnecessary |
| Proper-cubic symmetric quotient | positive at six rows |
| Commuting multiplication/pivot | live next route |
| Universal physical-circuit claim from functional completeness | not made |

## N2 — Pairwise conditions

| Pair | Relation | Treatment |
|---|---|---|
| four AND terms | independent | full Boolean diamond |
| term corpus vs parity | causal join | parity requires all four |
| unsigned bits vs sign bits | sign-invariant commutation | all signed inputs |
| ALU expressiveness vs embedded circuit | strict distinction | only tested circuits claimed |
| commutation vs half-weight premise | decision prerequisite | equal weight not derived |
| commutation vs pivot update | ordered residual | pivot open |

## N3 — Hidden-condition scan

Both ALU roles, all eight truth rows, every three-step instruction tape, four
term targets, eight literal inputs, four AND roles, shared guards, two parity
frames, six canonical parity rows, all 24,576 signed/rotated graphs, every
reachable subset, parent deletions, prior mixed devices, and bound fronts are
explicit. The input bits are supplied record content; conversion from a
32-role row record to five literal bits remains a separate interface.

## N4 — Residual matching

| Evidence | Residual consumed |
|---|---|
| Cycle 148 | symplectic parity formula |
| Cycle 149 | physical row-role update |
| Cycle 150 ALU | literal Boolean operations |
| Cycle 150 circuit | physical commutation record |

It does not consume row-bit decoding, signed multiplication, pivot output,
occurrence/weights, arbitrary-state coverage, or selection.

## N5 — Resolution and rhetoric

Tested: complete Boolean truth tables, all length-three ALU programs, every
signed two-row commutation input, all asynchronous term schedules, every
proper-cubic image, and prior-device coexistence. Not tested: arbitrary Boolean
circuits, arbitrary qubit count, complete tableau update, or a minimum Boolean
basis across all encodings. Licensed phrase: “physical literal-bit symplectic
commutation,” not “measurement derived.”

## N6 — Partial-closure paths

1. Build signed commuting multiplication from XOR/AND/phase records.
2. Route the two commutation bits into a physical pivot selector and emit two
   updated five-bit generator rows.
3. Replace the 32 row roles with generated five-bit bundles and rerun the
   compact gate machine.
4. Only after the conditional pivot closes, return to occurrence and weight
   as the remaining quantum-science gap.

## N7 — Strongest hostile steelman

A hostile reviewer should say the circuit is still supplied: its input bits,
AND apparatus, guards, and parity frame do not grow from the recurrent archive.
Correct. The narrower result is that the symplectic decision itself no longer
lives in a row-role ROM or host function. Four independently scheduled literal
products and one covariant parity join compute it under the same append-only
law, with every input and orientation exhausted. Generation and selection
remain open rather than hidden.

## N8 — Cross-cycle echo

Cycle 148 found compact bit algebra behind the large finite tables. Cycle 149
made row-level updates physical but retained a 32-role dictionary. Cycle 150
crosses that dictionary for commutation and shows how isotropy itself compresses
the parity table. This continues the campaign's recurring lesson: first expose
the semantic lookup, then replace it with causal records, then quotient away
presentation choices. The next record-level atom is signed multiplication and
pivot, not another axiom sentence.

## Verification

```text
PYTHONPATH=scripts python3 scripts/literal_bit_alu_symplectic_commutation_cycle150_2026_07_15.py
```
