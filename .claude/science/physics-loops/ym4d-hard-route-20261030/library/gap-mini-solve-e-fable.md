lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:00Z

# gap-mini-solve-e-fable (queue row 1194)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 36be8070a. Not an audit. Not checked by another model. Start 2026-11-20T00:00Z (`date -u`).

Problem of the row: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels used below: PROVED (every step written here, by hand), ARGUED (argument written, a step is not fully written or rests on a named input), GUIDE (numeric or heuristic, never a proof step), OPEN.

Status of this file: in progress. Sections are appended step by step.

## Step 0. Plan (written before any reading of earlier results)

1. Read the RESULT lines of the sibling rows (gap-mini-solve-a to -d) and of the gap lane, `parts/gap.md` (method list, route registry, test table) and the route screening table in `library/gap-mini-solve-b-fable.md` Step 2.1.
2. Name the exact open statement the lane has reduced the gap to, and the attacks already on file for it.
3. Choose one attack that is not on file, or one named unattempted item, and carry it to a proof, a counterexample, or one precise lemma with the reason each way failed.
4. Rule 0a: before a statement is called new, grep `library/open-core.md` and the FINISH rows for it.

## Step 1. What the record holds (read in this session; statements about the record, not evidence)

Read in full: `GOAL.md`; `FINISH.md` L1-84 and L299-360; the row (L1275); the RESULT lines of rows 1178-1190 and 1193; the three sibling files `gap-mini-solve-a-fable.md`, `-b-`, `-c-` and the start of `-d-`; `parts/gap.md` L1-104 and L213-322; `library/gap-council-synthesis.md`.

1. The lane reduces the Jaffe-Witten gap clause to two open inputs (Theorem BP of row 1179; check row 1183: main chain HOLDS AFTER CORRECTION): the continuum datum of the T0 chain, and one lattice estimate (N-phys) of row 1161. (N-phys) is a neutral gap with a level count on one periodic cube of fixed physical side, uniformly in the cutoff. Rows 1180 and 1184: it is a uniform neutral lattice gap at arbitrarily weak coupling with an asymptotic-scaling bound.
2. The wall in the lane's words (`parts/gap.md` L321-322): one selective inequality at every scale between first passage and the seed size. Selective means false for a massless factor.
3. Siblings of this row. Row 1188 (a): the pinned-slice Ward route, Lemma PC. Row 1189 (b): the doubly flat corner, Theorem A8, stop at (Sigma-unif) and (SING). Row 1190 (c): seventeen candidates on file; cube identity; chi-square form of (N-phys). Row 1193 (d): started, no attack written at this pin. Each sibling found the lane's map again and advised against one more fresh choice of route.
4. Consequence for this row: I do not screen routes again. I choose one mechanism question and work it to a proof or to a first failing step.
