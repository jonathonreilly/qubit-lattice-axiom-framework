lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T02:08Z

# Check of row 998 (gap-crux-exercise3-max), work item W1

Queue row 999 (`FINISH.md` line 1078), queued 2026-11-15 14:08Z. Checker: Claude Opus 5.5, max effort, Mac mini worker 3, started 2026-11-15 14:08Z at commit f75650fe8 on `claude/ym4d-hard-route`. The checked file `library/gap-crux-exercise3-max.md` was written by Claude Fable 5.2. Same vendor, different model; this is not an independent check in the sense of the working rules (a different derivation counts only where the derivation below differs from theirs, and each test says whether it does).

## Plan (at most eight steps; one step per response; each result appended before the next)

1. Copy W1 of `library/gap-crux-exercise3-max.md` 9.7 (L895-910) into this file. DONE below.
2. Read the files W1 names (the checked file's 1.2, 3.2 (L5), 6c, 6d, 8.1, 8.2, 8.5, and the outside line ranges); record what each says that the tests use.
3. Tests (a) and (b): Lemma PT (b) transfer operator and gauge projection under (TM-gen); Lemma PT (a) f = f_1 + f_2.
4. Test (c): Corollary PT1, "massless phase" to "no seed" for compact U(1) Wilson, and the published theorem.
5. Test (d): Proposition KF (c), "first-passage data" for a general weight; can a constant sequence meet it.
6. Test (e): Corollary KF1 against row 988.
7. Items (iii), (iv), (v): the 6c table rows, the 6d rows, the two 8.5 corrections.
8. Verdicts per item with the line, stop rule, RESULT line.

## Step 1. W1 as written (copied from `library/gap-crux-exercise3-max.md` L895-910)

> **W1. Check of this file (a model that did not write it; a cross-provider model if one is free; high effort).**
> *Statement to check:* `library/gap-crux-exercise3-max.md`: (i) Lemma PT and Corollary PT1 (8.1); (ii) Proposition KF
> and Corollary KF1 (8.2); (iii) the rows of the table in 6c for "Product with a massless factor", "w_p", "K7 line"
> and "Frozen Q_8, 2T"; (iv) 6d rows 24, 28, 30, 33 and the last two rows; (v) the two corrections of 8.5.
> *Read:* this file, Sections 1.2, 3.2 (L5), 6c, 6d, 8.1, 8.2, 8.5; `library/gap-crux-restate.md` L36-56 (definitions,
> (TM)) and L170-222 (Theorem S); `library/gap-phys-seed.md` L296-323 (Theorems ZD, ZD-c); `library/gap-crux-fp.md`
> L356-364 (Proposition V); `library/gap-unit-max.md` L231-246 and L357 (Route 3, N2); `library/gap-mid-max.md` L64-67,
> L226-229 ((CAS), the product device); `library/gap-crux-exercise2-check-astra.md` L227-259.
> *Test first:* (a) in Lemma PT (b), that the transfer operator of the product model is the tensor product,
> including the gauge projection, for the general weights of (TM-gen); (b) in Lemma PT (a), f = f_1 + f_2;
> (c) in Corollary PT1, the step from "massless phase" to "no seed" for compact U(1) with the Wilson weight, and
> which published theorem covers it; (d) in Proposition KF (c), whether "first-passage data" is a well-defined
> clause for a general weight, and whether the clause can be met by a constant sequence; (e) whether Corollary KF1
> changes any conclusion of row 988 other than the wording of (c) and N2.
> *Verdict per item:* HOLDS, HOLDS AFTER CORRECTION, FAILS, with the line. No new attack.
> *Stop rule:* one reading; stop at the list. *Output:* `library/gap-crux-exercise3-check-<model>.md`, ending with one RESULT line.

Provenance of the check. W1 asks for "a model that did not write it; a cross-provider model if one is free". The author is Claude Fable 5.2; this checker is Claude Opus 5.5. That meets "a model that did not write it" and does not meet "cross-provider" (FINISH row 999 says a gpt-6-astra check is held). W1 asks for high effort; this run is at max. The derivations below are written out by me; where a test only re-reads the author's argument rather than re-deriving it, the test says so.

No-new-attack rule: W1 says "No new attack". Nothing below attacks an open lemma; where a test needs a fact that is open in the lane, it is named and left open. Grep of `library/open-core.md` and the FINISH rows is therefore not triggered (no open lemma is attacked).

## State

Step 1 done (2026-11-15 ~14:12Z). Next: step 2, read the named ranges.
