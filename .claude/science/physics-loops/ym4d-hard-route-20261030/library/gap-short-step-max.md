lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T08:03Z

# gap-short-step-max: the 4D short step, a selective gain at order-one response

Queue row 1018 of `FINISH.md`, pinned at commit df74a7421, branch `claude/ym4d-hard-route`.
Worker: Claude Fable 5.2, max effort, Mac mini worker 3. One session, no subagents.
This is research-stage working state. It grants no status.

Marks used below: PROVED (every step written here), ARGUED (argument written, a step not fully written), OPEN, FAILS (counterexample or failing step written).

## Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Read.** `parts/gap.md`; rows 1009, 1010 (2D short step, [28] (3.52)); `library/gap-pinned-cell-gauge-max.md` and its check; `library/gap-invent-selective-max.md` and its check; the exercise skill at main commit 8b11ae2bb9. Duplicate check against `library/open-core.md` and the FINISH rows (rows 1016, 1017 run in parallel and are not redone). Record what is read and what is established.
2. **Target.** Write the 4D short step as an exact inequality: the quantity R(Q), the class closed under the conditioning the proof uses, the statement R(lQ) <= R(Q) - delta at order-one R(Q). Show by hand that it is false for compact U(1) and for a product with a massless factor.
3. **Route (iii-b), barrier first.** Try to build an averaged or modified model that keeps every identity the tools use (bracket term of Proposition W, reflection positivity) and has no short step. If it exists, name what a proof must use beyond the bracket.
4. **Route (ii), field-dependent covariant moves.** Jacobian control and the curl form of the cost at order-one response; test against Lemma WN and row 1013 C8.
5. **Route (iii-a), energy increment.** Write the dichotomy lemma (response drops, or a structure energy bounded by the action rises); test both halves.
6. **Tests.** Each surviving piece against Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, Lemma SLAB, compact U(1), frozen Q_8 and 2T, the five-dimensional test of `library/gap-crux-fp.md`, the instanton cost of 6.3 of row 1013.
7. **First survivor.** Prove it by hand, or build the counterexample.
8. **Result.** Marks per piece, what stays open, one RESULT line.

## Log

- 2026-11-15T20:03Z. File created. No earlier run of this item exists at the pinned commit.
- 2026-11-15T20:20Z. Step 1, progress marker 1a. Read in full: `GOAL.md`; `FINISH.md` L1-90, L299-356 and rows 1009-1018; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md` (row 1011); `library/gap-invent-selective-max.md` (row 1013); the exercise skill at main 8b11ae2bb9 and its reference `proof-search-governance.md` (both fetched into `/tmp/gss-skill-w3/`). Still to read in this step: the two checks (rows 1014, 1015), rows 1009 and 1010 at the short step ([28] (3.52)), the statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the five-dimensional test, and the files of rows 1016, 1017 if they exist at this pin (to avoid redoing them).
