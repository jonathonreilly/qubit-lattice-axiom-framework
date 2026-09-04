# Physical commutation and multiplication atoms — Cycle 151

Date: 2026-07-15

Authority: none

Disposition: local campaign-positive compact measurement atoms; audit unset

Companion runner:

```text
scripts/physical_commutation_multiplication_atoms_cycle151_2026_07_15.py
```

No foundation, axiom, primitive, registry, queue, policy, audit, commit, push,
or PR is changed.

## Result

Cycle 151 places the two computational atoms of the finite stabilizer
measurement algorithm under one physical law:

1. literal-bit symplectic commutation from Cycle 150;
2. physical multiplication of two commuting signed Pauli rows.

Together with the already verified tableau pivot algorithm, these atoms are
sufficient algebraically to reconstruct all 1,800 Cycle-48 conditional
measurement branches. The pivot controller remains open: the two commutation
records have not yet been physically routed into preserve/replace/multiply
outputs for both generator rows.

Multiplication is still role-level. Its input and output are among 32 physical
row roles, whereas commutation already consumes literal H0/H1 bits. Replacing
the multiplication codebook with literal XOR/phase circuits is a deeper
compression route, not silently assumed.

This result does not derive occurrence or equal weights. It implements the
conditional algebra used after an outcome record is supplied. No axiom
addition follows.

## Commuting multiplication quotient

There are 32 signed two-qubit Pauli rows. The exact ordered-pair census is:

```text
all ordered pairs                                  1,024
commuting ordered pairs                              544
```

Multiplication is commutative on that domain. Proper-cubic canonicalization
may exchange the two row-parent directions; because `AB=BA`, the output is
unchanged. The quotient has:

```text
canonical multiplication rows                        288
proper-cubic raw rows                               6,528
Cycle-150 union rows                               70,892
combined rows                                     77,420
raw conflicts                                          0
```

The target sees the two row roles on opposite axial faces and three MARK frame
records. One face remains a guarded open port. Every canonical output is the
signed product checked independently by Cycle 148's bit/matrix algebra.

## Exhaustive physical controls

Every ordered commuting pair is tested in all 24 proper-cubic orientations:

```text
544 * 24 instances                                13,056
initial records per apparatus                          29
enabled writes per instance                             1
wrong/unexpected terminals                              0
```

Deleting each of five direct parents from all 288 canonical rows gives 1,440
controls; none retains the multiplication output.

The multiplication rows are then added to the whole prior machine. All 86,640
mixed Clifford/measurement histories retain their exact frontiers and
terminals, and the Cycle-144 terminal retains exactly its two priced fronts.

## Conditional measurement decomposition

For state generators `g1,g2` and signed measured row `P`:

```text
c1 = symplectic(g1,P)
c2 = symplectic(g2,P).
```

The cases are:

```text
c1=c2=0: P or -P is already in {g1,g2,g1*g2}; outcome certain/impossible
c1=1,c2=0: replace g1 by P
c1=0,c2=1: replace g2 by P
c1=c2=1: replace g1 by P and g2 by g2*g1.
```

Cycle 150 physically computes `c1,c2`. Cycle 151 physically supplies `g1*g2`
or `g2*g1`. The still-missing controller must:

- join the two commutation results;
- select the case without a host branch;
- preserve, replace, or use the product for both output generators;
- in the commuting case, compare signed `P` against `g1,g2,g1*g2` and emit
  certain versus impossible;
- leave both updated rows readable by the next event.

That controller is now a routing/interface problem over established physical
atoms, not an unknown 1,800-entry state-update law.

## N1 — Alternative routes

| Route | Outcome |
|---|---|
| Keep all 1,800 measurement rows | exact expanded implementation |
| Direct 32x32 ordered multiplication ROM | 544 contexts |
| Quotient by commuting exchange | positive at 288 rows |
| Literal phase/XOR multiplier | live deeper compression |
| Host pivot branch | rejected as final interface |
| Physical case join and row routing | live next route |
| Infer occurrence/weight from update machinery | rejected; independent gap |

## N2 — Pairwise conditions

| Pair | Relation | Treatment |
|---|---|---|
| left vs right multiplier input | exchange-equivalent on commuting domain | quotient |
| commutation vs multiplication | independent physical atoms | both tested |
| atoms vs pivot controller | prerequisites | controller open |
| commuting case vs anticommuting case | distinct control branches | explicit |
| conditional update vs outcome occurrence | independent | occurrence open |
| role-level vs literal-bit multiplication | strengthening | literal route open |

## N3 — Hidden-condition scan

All 32 row roles, 544 ordered commuting pairs, 288 canonical signatures, 6,528
raw images, target/port/cage records, every proper-cubic instance, 1,440 parent
deletions, all algebraic pivot cases, 1,800 comparison branches, prior mixed
devices, and bound fronts are explicit. “Sufficient” means the algorithm can
be reconstructed from these functions; it does not claim the physical
controller already exists.

## N4 — Residual matching

| Evidence | Residual consumed |
|---|---|
| Cycle 150 | physical commutation bits |
| Cycle 151 | physical commuting product row |
| Cycle 148 algorithm | exact pivot target specification |

It consumes the multiplication atom. It does not consume controller routing,
literal multiplier compression, occurrence/weight, generated inputs, or law
selection.

## N5 — Resolution and rhetoric

Tested: every commuting signed pair, all rotations, parent deletions, exact
algebraic outputs, full prior mixed histories, and bound-terminal coexistence.
Not tested: arbitrary Pauli count, noncommuting multiplication, complete
physical pivot, or all multiplier encodings. Licensed phrase: “physical
commutation and multiplication atoms,” not “measurement machine compacted.”

## N6 — Partial-closure paths

1. Build the four-case physical pivot controller from `c1,c2`.
2. Add signed membership comparison for the deterministic case.
3. Emit two recurrent updated row records and test mixed event sequences.
4. In parallel, replace the 288-row role multiplier by literal XOR/phase
   circuits and compare law/history cost.

## N7 — Strongest hostile steelman

A hostile reviewer should say the 288-row multiplier is another ROM and the
physical atoms have not yet been wired into the promised measurement update.
Correct. The narrower advance is that exchange symmetry halves the exact
multiplier content, every product is physical and covariant, it composes with
the whole machine, and the residual controller has a four-case truth table
rather than 1,800 unexplained answers. The ROM objection is reduced, not
declared dead.

## N8 — Cross-cycle echo

Cycle 147 made every branch executable in an expanded table. Cycle 148 exposed
the compact pivot algebra. Cycles 149–150 made row updates and commutation
physical. Cycle 151 adds the remaining algebraic product. This repeats the
campaign's bridge pattern: expanded executable target, exact mathematical
compression, then one physical atom at a time. The next atom is control and
routing; the remaining science gap beyond it is occurrence/weight and law
selection, not conditional state update content.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_commutation_multiplication_atoms_cycle151_2026_07_15.py
```
