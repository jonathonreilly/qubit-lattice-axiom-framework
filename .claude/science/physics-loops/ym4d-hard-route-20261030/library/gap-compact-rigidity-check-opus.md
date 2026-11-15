lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T08:45Z

# Check of row 1017 (gap-compact-rigidity-max), work item W1

FINISH row 1019, `gap-compact-rigidity-check-opus`. Checker: Claude Opus 5.5, max effort, Mac mini worker 2. Same provider as the author (Claude Fable 5.2), so this is not an independent check in the sense of the working rules; it is a second reading by a different model. No subagents. Started 2026-11-15T20:45Z (from `date -u`).

Source under check: `library/gap-compact-rigidity-max.md` at commit 0d3b45d91 (499 lines), work item W1 at L459 and following.

## Plan (at most eight steps; one per response)

1. Read W1 exactly and the whole of row 1017's file; record the statements to check, the tests W1 asks first, the verdict scale and the stop rule. Read the cited definitions in `parts/gap.md` (Corollary Z4, Theorem ZD-c, (W), (PHYS-SEED), (BDD-Delta), the engine axioms).
2. Tests first: run the tests W1 names (counterexamples, edge cases) against the statements before any line-by-line reading.
3. Lemma UF and Theorem CE (compactness, kept properties, the numeric bounds 2.47 x 10^(-5), 256 D_0 + 34.11).
4. Proposition OM (compact limit set, doubling invariance, uniformly recurrent element, stalling functionals).
5. Theorem CR, both directions, with the most care (new equivalent form of (W)).
6. Corollary TRI, Lemma LV, and the FAILS claims (constants log m critical, Lemma PT-inf, Proposition SI).
7. Seeds (a)-(c) and the consumer claim, as far as W1 asks.
8. Verdict table and RESULT line.

(The plan is provisional until step 1 reads W1; it will be revised in place if W1 orders things differently.)

## Step 1: what W1 asks (read at L459 of the source)

W1 (verbatim scope): check line by line Sections 3.1-3.7 and 6.1 of `library/gap-compact-rigidity-max.md`: Lemma UF, Theorem CE (i), (ii)(a)-(e), Proposition OM (a)-(e), Theorem CR, the data A_(m,eps), Lemma PT-inf, Proposition NR, Proposition SI (4.1), Lemma LV, Corollary TRI (5.1). Read first: `gap-crux-restate.md` L29-45, L170-203; `gap-phys-seed.md` L253-257 (Lemma Z), L283-294 (Lemma Z3), L311-323 (Theorem ZD-c, Corollary Z4); `gap-mid-max.md` L63 (Proposition Delta); `gap-crux-exercise3-max.md` L690-713 (Lemma PT). Test first the six points of 5.1 (L348). Then judge: (i) is Theorem CR's equivalence right as stated, with (BDD-Delta) as the only extra hypothesis; (ii) is the admissible-sequence definition right for a trajectory (j_i -> infinity); (iii) does Lemma PT-inf (ii) need more than Lemma Z3. Report the first failing step, or none. Stop rule: no new attack.

Output name: W1 says `library/gap-compact-rigidity-check.md`; FINISH row 1019 and the worker prompt both say `library/gap-compact-rigidity-check-opus.md`. I write the latter only.

Report format (FINISH, Rules): one provenance line, a verdict per statement (ADVANCE, CORRECT-NO-ADVANCE, WRONG), then only the defects that break something, each with its explicit failure.

**Revised plan (replaces the provisional one above).**

1. Read W1 and the cited inputs (this section). Record each input statement as the check uses it.
2. The six test points of 5.1, each with a verdict.
3. Section 3.1 definitions, Lemma UF, Theorem CE (i).
4. Theorem CE (ii) Steps 1-6, with (a)-(e).
5. Proposition OM (a)-(e) and Lemma LV.
6. Theorem CR (most care), judgements (i) and (ii), Corollary TRI.
7. The data A_(m,eps), Lemma PT-inf (judgement (iii)), Proposition NR, Proposition SI.
8. Verdict table, defects ranked, RESULT line.

### 1.1 Inputs, as read at commit 0d3b45d91

(being written)
