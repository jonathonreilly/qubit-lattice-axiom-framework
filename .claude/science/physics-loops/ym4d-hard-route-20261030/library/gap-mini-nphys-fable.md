lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T17:12Z

# gap-mini-nphys-fable (queue row 1354)

Started 2026-11-21T05:12Z (date -u), Mac mini Claude worker 2, pinned at commit 33f734aed on branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim.

Item: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the sense of Jaffe and Witten, building on the neutral twist-averaged seed (N-phys) reduction of row 1342 (checked by row 1349) and rows 1341, 1345, 1348, 1351.

Labels used below: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Orientation

Written 2026-11-21T05:18Z (date -u). Read so far, statements only unless a proof is named:

- `GOAL.md` (whole); `FINISH.md` L1-84, L299-360 and the rows 1326, 1331, 1332, 1335, 1340-1354 (RESULT lines).
- `library/gap-seed-audit-fable.md` (row 1342, whole): (N-phys), its two-period form (T-N), Theorem O,
  Proposition C, the model ST_q. Check row 1349 read in the RESULT line only at this point.
- `parts/gap.md` L1-104 (state of attack) and L213-322 (route registry, test table, the exact price).
- This worker's notes on the three route-screening tables (rows 1189, 1194, 1199), on row 1200 and on the
  prior-identity list. They say: about 32 route families derived from scratch are on file already.

The target of this row, in the form this file uses (PROVED GIVEN on file, row 1342 Section 6, check row 1349):

**(T-N).** One admissible physical side L. For all late j (n_j = L/a_j, 4 | n_j, n_j >= 2^70) there is an
integer u_j with 3 <= u_j <= n_j/512 and Z_+(2u_j)/Z_+(u_j)^2 >= 2/3. Here Z_+(v) is the mean, over the eight
temporal twists, of the Wilson partition functions of the torus v x n_j^3 at the coupling beta_j. It equals
Tr(P_0 T^v), with P_0 the projection on the sector of zero electric flux.

What every earlier row found, in one sentence: a proof needs one selective step at a coupling of order one
(false for a massless factor), and no row has one. New inputs named by the queue row: the neutral target, the
rule that an exact computation checked in Lean is a proof step, the block maps and the end class of rows 1341,
1345, 1348, 1351.

Rule 0a for this row: row 1353 (queued in parallel, Mac mini worker 1) owns the statement "carry the Wilson
trajectory through mass-preserving block steps into the neutral end class of row 1351". Its output file is not
on disk at this pin. This row does not read it and chooses its own attack in Step 1.

## Step 1. Choice of attack (in progress)

Reading Proposition CH (row 1332) and the neutral end class (row 1351) before the choice is written.
