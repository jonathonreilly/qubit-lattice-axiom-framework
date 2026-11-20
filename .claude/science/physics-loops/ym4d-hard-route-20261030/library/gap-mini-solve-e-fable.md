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
