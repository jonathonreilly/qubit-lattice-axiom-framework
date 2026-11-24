lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T02:57Z

# Row 1474: the missing tool T2, a representation for an order-one block step

Worker file of queue row 1474 (`gap-k2-t2-representation-fable`), pinned at commit a3c24b36f on
`claude/ym4d-hard-route`. Started 2026-11-24T14:57Z (date -u). Research-stage working state; nothing here is a
public claim. Every statement is marked proved, sketched or guessed. Nothing is committed or pushed from this
machine.

## 0. Plan (written first, per the save protocol)

1. Read the record the row names: rows 1460, 1461, 1466, 1468, 1470, 1471 and their checks;
   `library/gap-k2-tool-design-fable.md` sections 4-6, `library/gap-k2-floor-sizing-opus.md`,
   `library/gap-k2-end-class-fable.md`. Record which representations are already closed and why (cost or closure).
2. State T2 as a precise problem: a class C of local rules, a map S (the Q2 step or another exact self-similar
   map), with (a) S(C) inside C at order-one coupling, (b) the inclusion a finite check of bounded size,
   (c) selectivity under the filter t1-t6 (rows 1386, 1442).
3. Attack: candidate representations not on the closed list; for each, size of one step's check at beta about 2.3.
4. If no candidate survives for a stated class, prove the obstruction for that class.
5. End with the next two rows and their decisive outcomes, and one RESULT line.

Free memory at start: 37 percent (memory_pressure), below the 50 percent bar for a numeric job; no numeric job
is started unless that changes.


## 1. Step 1: the record, and T2 as an exact problem (written 2026-11-24T15:35Z, date -u)

### 1.1 What was read

Row 1474 in full. `gap-k2-tool-design-fable.md` (row 1468) Sections 2 to 11 in full. `gap-k2-floor-sizing-opus.md`
(row 1470) Steps 5 to 7. `gap-k2-end-class-fable.md` (row 1471): headings and the RESULT line. The filter (t1) to
(t5) in `gap-mech-direction2-fable.md` 4.2 to 4.5 (row 1386) and (t6) in the RESULT of row 1442. `gap-ds-gauge.md`
(row 691) Sections 0 to 3.3 in full (Theorem W and its proof). Proposition CA-FAIL with its precision
(`gap-bridge-exercise-opus.md` lines 337 and 368). The RESULT lines of rows 691, 813, 828, 1120 (line 1198 of
FINISH), 1326. Rows 1460, 1461 and 1466 were read only through the uses that row 1468 makes of them (Theorem LOSS,
Lemma LD-1, Corollary LD-2); their files were not opened. That is a skipped step.

### 1.2 The closed list, by the means each one uses

Row 813 (F-findings) sorts every proved gap result by what makes its criterion checkable at one scale: (m1) a
small number at that scale; (m2) a second small number after an exact change of variables; (m3) exact closure;
(m4) a correlation inequality that gives a dichotomy. The representations closed for an order-one step:

| Representation | Means | Closed by | On file |
|---|---|---|---|
| Polymer expansion in plaquette activities | (m1) | closure: ceiling beta 0.0087 for the entry | row 1471 |
| One-link and block Dobrushin, complete analyticity | (m1) | closure: 2/9, 0.3609; false above 1.0109 in the uniform strong form | rows 1340, 1346, 1072 |
| Site tensors, exact contraction | none (in-law evaluation) | cost: rank 67, 13 PB a site; 2^(2 slice + 1) | rows 1418, 1326 (Lemma DIM) |
| Block enclosure, exact 2^4 cube map | (m3) for a map that is not self-similar | cost 6.5e14 gates for eight links; no closure | rows 1341, 1344, 1346 |
| Loop-equation or positivity certificate | none (linear in the density) | closure: patch as large as a seed box | row 1326 (Theorem O, Remark OS) |
| Character sums, heat factors on straight coarse links | (m3) attempted | closure: signed coefficients; no exact heat factor | rows 1425, 1434, 737 |
| Knabe or martingale criterion for the heat-bath generator | (m1) | closure in full L2 (gauge corner); every-boundary premise | row 828 (GC1 to GC4) |
| Cube criterion (W) of Dobrushin-Shlosman type | (m1) at the cube scale | not refuted; no method to verify it | rows 691, 1326 4.1 |
| Convexity (Bakry-Emery, Brascamp-Lieb) | (m1) | closure: hand range only | rows on Langevin gap (beta below 1/4), 34 files |
| Migdal-Kadanoff with interpolation (Tomboulis) | (m3) on a hierarchical lattice | not a proof on Z^4 (Ito and Seiler) | row 848 |

So the lane has no (m2), no (m3) on Z^4, and no (m4). Every (m1) entry is either below the hand range or is a
supremum over boundary values that nobody can evaluate.

### 1.3 T2 as an exact problem, and two remarks that fix what a solution can be

**Problem T2.** Find a set C of local rules (4.2 of row 1468) with readout near 2.3 and a statement S(Phi) such
that: (a) S(Phi) implies that the image of Phi under the next map is in the next class, or directly that every
family that realizes Phi has purity at least 457/625; (b) S(Phi*) for a computed centre Phi*, together with a
stability bound over a tube, is a finite computation of bounded size; (c) the filter (t1) to (t6).

**Remark SOUND (what (c) asks of a finite criterion). PROVED, one line.** If S implies the purity bound on
tori of all large sizes, then S is false for every model without a gap, so (t1), (t2), (t6) hold for S itself.
What the filter tests is the proof of (a): each of its lines must be valid for U(1), Villain U(1) and five
dimensions (then S fails there by a number), or must fail there at a named line. A criterion whose proof of
(a) is group-blind and dimension-blind, such as Theorem W of row 691, passes the filter as a criterion. It
then carries no mechanism: all the content is in the number that S asserts.

**Remark END (a step is not needed where an end criterion holds). ARGUED from rows 691 and 1471.** Row 1471
shows that a Q2 step of strength 0 maps into the end class exactly when the purity statement holds. So the
entry stretch moves no difficulty. A finite criterion of type (W) at readout 2.3 is an end class at order-one
coupling: Theorem W (C) gives a covariance bound on every torus with constants free of the torus, and (D')
gives the twisted actions. The step from that covariance bound to the purity of the sixteen masses is the
telescoping of one boundary link at a time; it is not written here and is OPEN as a written proof (see 4.3). So
T2 for the stretch from 2.3 to the end class is equivalent in strength to: a finite criterion for decay at
readout 2.3 that can be evaluated. This is the seed for a tube of rules. The row asks for a representation
that makes it finite at known cost; Sections 2 to 4 give one and size it.

### 1.4 What CA-FAIL does and does not exclude (re-read; this corrects a phrase of row 1468, not a theorem)

Row 1468 (C4) asks for "no unweighted supremum over all coarse fields" and cites CA-FAIL. CA-FAIL is proved
for volumes that are thin slabs with both faces pinned. It refutes complete analyticity and strong mixing over
all volumes. It does not refute (W) on cubes (row 1326 4.1 says the same: "the weak-mixing form (DS-W) of row
691 is not refuted"). What can make (W) false on cubes is surface order at a special boundary value: row 950
saw the colour direction order at a pinned pi-flux slice from beta about 2.45 up (GUIDE). With such a
boundary value the response to one changed boundary link has of order R^2 disagreeing links, and (W) allows
about R/8 per boundary link. So the state for cubes is: (W) may be true at 2.3 and is expected to fail a
little above; in both cases it is a supremum over a continuum of boundary values and no method evaluates it.
For a block step the coarse field is a field in the bulk, and there (C4) stands as argued in row 1468.

